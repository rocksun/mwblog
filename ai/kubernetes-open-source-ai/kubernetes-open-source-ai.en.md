At CES 2026, NVIDIA CEO Jensen Huang made the case that AI will proliferate when open innovation is activated across every company and every industry. If that’s the future (and the trajectory of DeepSeek, Llama, Mistral, and the broader open-model ecosystem suggests it is), then the infrastructure that runs AI can’t be proprietary either.

> “As AI becomes the dominant consumer of compute, the community is closing the gap between ‘possible’ and ‘first-class.'”

Kubernetes has been running AI workloads almost as long as it has existed. It was not originally designed for AI, but AI teams have always found ways to make GPU workloads run, even when the core APIs didn’t understand GPUs beyond a simple integer count. As AI becomes the dominant consumer of compute, the community is closing the gap between “possible” and “first-class.” Here’s where that work stands.

## Describing the hardware

The original device plugin API worked when all you needed was a count of available GPUs. It breaks down when a [workload needs a specific partition of a shared GPU](https://thenewstack.io/kubernetes-primer-dynamic-resource-allocation-dra-for-gpu-workloads/), when multiple pods need to share a single device, or when training jobs need high-speed interconnects across nodes.

[Dynamic resource allocation (DRA)](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) changes this. Vendors expose structured device information through ResourceSlices, and workloads declare ResourceClaims describing what they need. The scheduler matches claims to devices, reasoning about attributes, sharing policies, and topology. DRA gives us the primitives. It reached GA in Kubernetes 1.34, and the policies to use those primitives effectively are the next frontier.

## Scheduling AI workloads

Distributed training and inference jobs require gang scheduling, where all pods start together or not at all, to prevent resource deadlocks. But placement also depends on understanding the cluster’s physical topology: landing pods on nodes that share a network spine or high-speed interconnect domain can dramatically reduce communication overhead.

The [KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler), accepted into the CNCF Sandbox, provides DRA-aware gang scheduling, hierarchical queues with fairness policies, and topology-aware placement for large-scale clusters. [Topograph](https://github.com/NVIDIA/topograph) discovers the underlying network topology and exposes it, enabling schedulers to make smarter placement decisions across cloud and on-premises environments. The Workload API discussions in the broader community are pushing these scheduling patterns further upstream.

## Serving the workloads

Inference is where production GPU cycles increasingly concentrate, and where [Kubernetes](https://thenewstack.io/ai-kubernetes-observability-practices/)’ assumptions break hardest. The horizontal pod autoscaler scales on CPU and memory. LLM inference needs to scale with KV cache utilization, request queue depth, and time-to-first-token. Scaling on the wrong metrics means wasting GPU hours or missing latency targets.

[Inference Gateway](https://github.com/kubernetes-sigs/gateway-api-inference-extension) extends the Gateway API with model-aware routing. The [llm-d](https://github.com/llm-d/llm-d) and [Dynamo](https://github.com/ai-dynamo/dynamo) communities are collaborating on distributed serving with prefix-cache-aware routing and disaggregated prefill/decode, creating entirely new scheduling and autoscaling demands. The building blocks are emerging, but the abstractions that tie them together will likely span both Kubernetes primitives and higher-level control planes.

And the next wave is already arriving. Teams are beginning to orchestrate autonomous AI agents as containerized workloads on Kubernetes, adding yet another class of compute to manage.

> “Open-source AI doesn’t stop at the model weights. The infrastructure needs to be open too, and the community is ready to build it.”

The [Kubernetes AI Conformance Program](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/), launched at KubeCon North America 2025 with twelve certified vendors, is a start. But the patterns to solve these problems exist across the organizations running AI at scale, even if implementations differ. That knowledge is currently locked inside individual companies. It belongs upstream, in the open, where it can compound.

Open-source AI doesn’t stop at the model weights. The infrastructure needs to be open, too, and the community is ready to build it.

*This guest column is being published ahead of [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), the Cloud Native Computing Foundation’s flagship conference, which will bring together adopters and technologists from leading open-source and cloud-native communities in Amsterdam, the Netherlands, from March 23-26, 2026.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/03/365cdf72-cropped-446be760-nathan-nathan-taber-us-600x600.jpeg)

Nathan Taber focuses on GPU-accelerated Kubernetes and health-automation patterns for large-scale AI infrastructure. Previously, he was a founding member of the Amazon EKS team at AWS, where he helped shape Kubernetes on AWS through work on EKS, Karpenter, and the...

Read more from Nathan Taber](https://thenewstack.io/author/nathan-taber/)