**We instrumented the full path from pod creation** to first inference response on a GPU node running a 70B-class model. Eight minutes. Six sequential phases. We expected one bottleneck. We found six, and which one dominates depends on model size.

For a 64 GB model, 65% of the startup time is spent recompiling CUDA kernels that produce identical output every time. For a 203 GB model, 92% of the time is spent downloading weights from S3 through a calling pattern that leaves 98% of available bandwidth idle. Both are fixable with configuration changes. Neither is fixed by default.

> “Eight minutes. Six sequential phases. We expected one bottleneck. We found six.”

We define **time to first token served (TTFTS)** as the wall-clock duration from pod creation to the first inference response leaving the GPU. Not time to first token (TTFT), which measures per-request latency once the model is warm. TTFTS is the one-time startup tax. TTFT begins where TTFTS ends.

Here’s what we achieved:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Scenario** | **Description** | **Before** | **After** | **Reduction** |
| **Pod restart on warm node** | Weights loading + compilation on existing node | 1.5-8 min | under 30s | 80-93% |
| **New node from scratch** | Fresh node provisioned, nothing cached | 8-15 min | ~5 min | 40-65% |

The warm-node row is what you pay on every pod restart: scale-up events, rolling updates, OOM recoveries. That’s the 80-93% win, and it requires only configuration changes. The cold-node row includes ~2 minutes of fixed infrastructure cost (node provisioning and framework initialization) that no application-layer optimization can remove. The rest is avoidable waste that we eliminated through platform and configuration fixes. The warm-node optimizations are environment variables and a volume mount that work on any Kubernetes cluster. The cold-node optimizations require EKS Auto Mode, which comes pre-configured with pre-compiled NVIDIA drivers, SOCI (Seekable OCI) parallel image pull, and NVMe instance store mounting.

*All model startup measurements were taken on p5.48xlarge instances running* [*Amazon EKS*](https://aws.amazon.com/eks/) *Auto Mode, with S3 traffic routed directly (bypassing the NAT Gateway) and container images in a private Amazon ECR repository (same region as compute). Model startup improvement ratios (80-93%) hold consistently across instance types (validated on P-family and G-family). Cold-node times vary with network bandwidth and CPU count. For the weights loading and compilation cache configuration, see* [*Accelerate model loading on Amazon EKS*](https://docs.aws.amazon.com/eks/latest/userguide/ml-inference-fast-model-loading.html)*.*

The Kubernetes ecosystem has made real progress on the inference stack in 2026. OCI image volumes are now stable for model delivery. [Dynamic Resource Allocation](https://thenewstack.io/kubernetes-primer-dynamic-resource-allocation-dra-for-gpu-workloads/) (DRA) gives GPUs structured attributes instead of opaque integer counts and provides flexibility in allocating GPUs to workloads. Gateway API has inference-aware routing extensions. But none of these primitives address the full cold-start stack: the six layers between “pod pending” and “first token served,” each with its own bottleneck and its own fix.

## The six layers of cold start

When a new inference pod starts on a freshly provisioned GPU node, it passes through six distinct phases before serving its first request:

1. **Node provisioning.** Karpenter launches an EC2 instance, boots it, and registers it with the Kubernetes API server (~60-90s).
2. **GPU driver initialization.** The driver kernel module must load and expose accelerator devices.
3. **[Container image pull.](https://thenewstack.io/accelerating-eks-image-pulls/)** The inference engine image (8-12 GB compressed) must be transferred to the node and extracted.
4. **Model weights download.** The model files must stream from object storage into GPU memory.
5. **GPU kernel compilation.** torch.compile traces the model graph and generates optimized CUDA kernels.
6. **Engine initialization.** CUDA graph capture, KV cache profiling, and HTTP server startup (30-120s depending on whether compilation is cached).

Each layer has a different bottleneck, a different fix, and a different owner.

## Which layer dominates depends on model size

Before diving into each layer, one finding shaped every decision we made: the bottleneck is not fixed.

We instrumented the model startup path (layers 4 and 5) and measured each phase independently for two model sizes:

**64 GB model** (Qwen3.6-35B-A3B):

* Weights loading: ~29s (35% of model startup)
* torch.compile: ~53s (**65%** of model startup)

**203 GB model** (Llama-4-Scout, TP=4 where TP is tensor parallelism, splitting the model across GPUs):

* Weights loading: ~423s (**92%** of model startup)
* torch.compile: ~34s (8% of model startup)

For models under ~100 GB, compilation dominates. For larger models, network transfer dominates. torch.compile time stays roughly constant (it depends on graph complexity, not parameter count). Weights loading scales linearly with file size.

> “For models under ~100 GB, compilation dominates. For larger models, network transfer dominates.”

This means any single-layer optimization has a ceiling.

## Layer 1: Node provisioning

On EKS Auto Mode and Karpenter-managed clusters, node provisioning takes approximately 60-90 seconds for accelerated instances from pod pending to node Ready. Karpenter calls the EC2 Fleet API directly and reacts to pending pods within seconds, keeping provisioning at the EC2 launch floor.

## Layer 2: GPU driver initialization

The NVIDIA GPU Operator in its default configuration adds **2-3 minutes to node boot** while it compiles the driver kernel module from source. This cost repeats on every new node.

When the platform controls the full stack (OS image, kernel version, driver version, boot sequence) it can pre-compile driver kernel modules at image build time. The node boots, runs modprobe to load an already-compiled .ko file, and the GPU is ready in seconds.

This matters more now than it used to. Blackwell-architecture GPUs (G7, G7e instances) require NVIDIA’s open-source kernel modules exclusively. Older Maxwell/Pascal/Volta GPUs can only run proprietary modules. A cluster with both legacy and next-gen GPU nodes needs different drivers, different AMIs, different upgrade cycles. A managed platform that pre-compiles the correct module per instance family eliminates this complexity.

On EKS Auto Mode, the GPU driver loads in seconds (pre-compiled at image build time), compared to the 2-3 minutes a runtime-compilation approach requires.

## Layer 3: Container image pull

A production vLLM or SGLang inference image is typically 8-12 GB compressed. Standard containerd pulls layers sequentially, decompresses them one by one in memory, and writes them to disk. At this size, sequential pull takes 2-4 minutes on a cold node depending on instance type and available CPU cores. For larger custom images (30-50 GB compressed), containerd can run out of memory entirely during decompression.

EKS Auto Mode uses SOCI’s parallel pull mode, which replaces containerd’s default snapshotter. The SOCI snapshotter downloads layer chunks concurrently via HTTP range requests and writes each chunk directly to its target byte position on disk (no in-memory ordering buffer). Decompression runs in parallel across all available CPU cores.

Pull time is bottlenecked by CPU-bound decompression, not network bandwidth. We confirmed this directly: a p4d.24xlarge with 400 Gbps networking achieved only ~1 Gbps effective pull throughput because CPU decompression was the constraint. On instances with more cores (48+ vCPUs), SOCI parallel pull reduces image pull time from 2-4 minutes to 30-60 seconds. On smaller instances with fewer cores, the improvement is modest because decompression cannot parallelize effectively. For a deeper look at how bounded-memory parallel pull handles images exceeding 30 GB without OOM, see [Bounded-Memory Parallel Image Pulling for Large Container Images](https://arxiv.org/abs/2607.05596).

## Layer 4: Model weights download

The obvious optimization for weights loading: more parallel connections. Split the model files into small chunks, download them concurrently, saturate the network pipe.

We tested it on p5.48xlarge with the 64 GB model streaming from same-region S3. The results were counterintuitive:

|  |  |  |
| --- | --- | --- |
| **Chunk size** | **Connections needed** | **Weights load time** |
| **256 MB** | 256 | 13.98s |
| **512 MB** | 128 | 14.20s |
| **2 GB** | 34 | 13.62s |
| **4 GB** | 17 | 13.35s |
| **8 GB** | 9 | 21.80s (+56%) |

256 parallel connections provided no benefit over 17. The only failure mode was 8 GB chunks (exceeding shard file size), which caused a 56% regression.

Why? Because the open-source [Run:ai Model Streamer](https://github.com/run-ai/runai-model-streamer) (integrated into vLLM and SGLang) processes S3 range requests sequentially within each worker thread. A worker assigned to a 3.9 GB shard file downloads its byte-range requests one after another on a single connection. The parallelism comes from running multiple workers on different *files*, not from splitting one file into more pieces.

We settled on 4 GB chunks matching typical SafeTensors shard size (3-5 GB per file) with an aggressive timeout-and-retry for slow requests. S3 GET latency has a measurable long tail: in our testing, a meaningful fraction of requests took 2-3x longer than median, and a single stalled connection holds up the entire model load. Rather than wait, we kill stalled connections after a few seconds below a speed threshold and retry on a fresh connection. This follows [S3’s own performance guidance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html).

For the 203 GB model, these config-only changes reduced weights loading from 423 seconds to 25 seconds (94% improvement). For the 64 GB model, from 29 seconds to 12 seconds. No code modifications, just environment variables. The tuning consists of three settings: chunk size aligned to shard file boundaries (eliminating the serial sub-request problem), a minimum-speed threshold that kills and retries stalled S3 connections, and explicit concurrency matching the number of shard files per tensor-parallel rank.

## Layer 5: GPU kernel compilation

Every time a vLLM or SGLang pod starts, PyTorch traces the model’s computation graph and compiles it to optimized CUDA kernels. This takes 34-53 seconds depending on model architecture. The output is identical every time for the same model, GPU type, and tensor-parallel configuration.

And Kubernetes throws it away on every pod restart. Pods use ephemeral storage by default. When a pod terminates, its local filesystem is destroyed. The next pod recompiles from scratch.

> “The output is identical every time for the same model, GPU type, and tensor-parallel configuration. And Kubernetes throws it away on every pod restart.”

Point the torch.compile cache directory at local NVMe instance store. GPU instances ship with NVMe that EKS Auto Mode mounts automatically. First pod compiles and writes ~15-30 MB of cached kernels. The second pod on the same node loads pre-compiled binaries in 4-6 seconds. One volume mount and environment variables.

The cache is safe because the compiled artifacts are deterministic: same model architecture + GPU architecture + tensor-parallel degree + PyTorch version equals valid cache. An image update or hardware change triggers exactly one recompilation.

torch.compile time is hardware independent. The same model compiles in ~52 seconds whether running on H100 or A100. The cache hit (4-6 seconds) is equally consistent across GPU types. This means the optimization works identically regardless of instance type.

## Layer 6: Engine initialization

After weights are loaded and kernels compiled, the inference engine must capture CUDA execution graphs and profile KV cache memory. With compiled kernels cached, this completes in 30-45 seconds. Without cache, graph capture triggers additional JIT compilation and takes 60-120 seconds.

This is why the torch.compile cache has an outsized impact: it accelerates not just layer 5 but also layer 6. Cached compilation reduces a 2-3-minute combined phase to a 35-50-second combined phase.

Framework initialization (Python interpreter startup and [PyTorch](https://thenewstack.io/this-is-how-to-optimize-pytorch-for-faster-model-training/) import) adds tens of seconds of fixed overhead that cannot be reduced through configuration.

## The compounding effect

The six layers compound. Platform fixes (layers 1-3) eliminate 4-8 minutes of overhead: pre-compiled drivers replace 2-3 minutes of runtime compilation, parallel pull reduces image transfer time from 2-4 minutes to 30-60 seconds, and Karpenter keeps node provisioning to its hardware minimum. Configuration changes (layers 4-5) cut the remaining model startup by 80-93%. Engine initialization (layer 6) drops from 60-120 seconds to 30-45 seconds once the compile cache is warm. Together, cold-node TTFTS drops from 8-15 minutes to approximately 5 minutes.

### 64 GB model (Qwen3.6-35B-A3B), TP=2:

|  |  |  |
| --- | --- | --- |
| **Configuration** | **First pod** | **Subsequent pod (warm node)** |
| **Baseline (no tuning)** | 82s | 82s |
| **+ S3 chunk tuning** | 65s | 65s |
| **+ torch.compile cache** | 65s | **16s** |
| **Improvement** | -21% | **-80%** |

### 203 GB model (Llama-4-Scout), TP=4:

|  |  |  |
| --- | --- | --- |
| **Configuration** | **First pod** | **Subsequent pod (warm node)** |
| **Baseline (no tuning)** | 457s | 457s |
| **+ S3 chunk tuning** | 59s | 59s |
| **+ torch.compile cache** | 59s | **32s** |
| **Improvement** | -87% | **-93%** |

The warm-node subsequent pod number is what matters most for production. It’s what you pay on every pod restart. The 80-93% reduction is consistent across instance types because the optimizations target software bottlenecks (calling patterns, redundant compilation), not hardware limits.

## The cost of cold starts at scale

Why does any of this matter? Because GPU nodes are expensive and inference traffic is bursty.

A single p5.48xlarge costs $55/hour on-demand. Even G-family instances commonly used for inference cost $10-20/hour. Every minute of cold start is GPU time you’re paying for but not using. If your autoscaler needs 8+ minutes to bring up new capacity, you must over-provision (burn money on idle GPUs) or accept latency spikes during traffic surges.

> “Every minute of cold start is GPU time you’re paying for but not using.”

When model startup drops to 16-32 seconds on warm nodes, the calculus changes. You can scale more aggressively, keep fewer buffer nodes, and respond to traffic spikes without multi-minute startup delays.

## What we learned

1. **Decompose before optimizing.** For 64 GB models, torch.compile dominates (65%). For 203 GB models, S3 loading dominates (92%). Without measuring each phase independently, we would have optimized the wrong layer.
2. **The bottleneck flips with model size.** torch.compile time is roughly constant across model sizes. Weights loading scales linearly. Every team running inference should know which regime they’re in.
3. **“More parallelism” requires understanding the execution model.** 256 connections performing sequential work inside each thread is no faster than 17. The bottleneck was the calling pattern, not the concurrency limit.
4. **15-30 MB can save 53 seconds.** The most impactful optimization for smaller models was persisting a tiny cache file. Always check whether an expensive computation produces deterministic output before trying to make it faster.
5. **Platform-level control enables optimizations that configuration alone cannot achieve.** Pre-compiled drivers, default-on parallel image pull, and NVMe auto-mounting are infrastructure-layer decisions that compound upward. Together with the config-only changes at the application layer, these changes reduce cold start time from minutes to seconds.
6. **The ecosystem is building the right primitives, but cold start lives between them.** OCI image volumes, DRA, inference-aware routing, and local model caches are all real progress. But the compilation bottleneck and S3 tuning gaps sit in spaces that no upstream Kubernetes primitive addresses. Sometimes the highest-impact optimization is a volume mount and two environment variables, not a new API.

For the complete configuration guide, including environment variables, YAML manifests, and instance-specific recommendations, see “[Accelerate model loading on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/ml-inference-fast-model-loading.html)” in the Amazon EKS User Guide.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/fdc3cdcb-gundapun-576x600.jpg)

Sajjan Gundapuneedi is a Sr. Manager of Software Development at AWS leading EKS compute infrastructure. His teams own the full node lifecycle for Amazon EKS: provisioning (Karpenter, Auto Mode, Managed Node Groups, Fargate, Hybrid Nodes), runtime (AMIs, networking, container runtime),...

Read more from Sajjan Gundapuneedi](https://thenewstack.io/author/sajjan-gundapuneedi/)