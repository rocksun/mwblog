**When the image is the bottleneck:** Machine learning changed what a container image looks like. A typical application ships in a few hundred MB and starts in seconds. A modern ML inference image carries a deep-learning framework, the CUDA stack, and sometimes the model weights. These images roughly reach 20 to 30 GB, with some even higher. On the GPU and accelerated instances these run on, pulling one of those images takes several minutes before the application can serve its first request: minutes during which provisioned accelerators are ready to process real work but waiting for images to be pulled.

We hit this bottleneck on a production ML platform [running on Amazon EKS](https://thenewstack.io/eks-kubernetes-etcd-scale/). The team needed pods ready within two minutes, but image pull alone consumed several minutes. Each pod pulled a roughly 30 GB container image on top of loading model data from a shared filesystem. The images were rebuilt on a regular cadence, so worker nodes faced cold pulls with no usable local cache. While the image was pulled, accelerators sat idle, autoscaling lagged demand, and request queues built up.

The natural first suspect for these large image pull times was the network or the registry. After all, 30 GB is a lot of data. However, profiling the image pull path showed neither was the bottleneck on accelerated instances with 100 to 400 Gbps of network bandwidth available. The real constraint was how the software used the hardware already available.

> “The real constraint was how the software used the hardware already available.”

By rethinking the pull pipeline to leverage the network bandwidth, storage throughput, and compute these instances already had, we got those multi-minute pulls down to seconds. The improvements are available by default on EKS Auto Mode today, and we contributed the core changes upstream to containerd and the SOCI snapshotter. This is the story of how we dove into the internals of the image pull path, identified where time was being lost, and rebuilt those stages. It starts where we started: understanding what a large container image looks like and how it gets onto a node.

## What a container image looks like at scale

A container image is not one file. It is a stack of layers plus a small JSON manifest listing them. Each layer is a tar archive of part of the filesystem (the base OS in one, CUDA libraries in another, your code in a third), gzip-compressed. For each layer, the manifest records a digest, a SHA-256 hash of the compressed bytes, so the node can prove it received exactly what was published. When the container runs, these layers are stacked and mounted together into a single unified filesystem.

Here is what real ML images look like when measured directly from their registry manifests:

|  |  |  |  |
| --- | --- | --- | --- |
| **Image** | **Compressed Size** | **Layers** | **Largest Layer** |
| **AWS DJL LMI 21.0 Inference (cu129)** | 16.5 GB | 29 | 9.5 GB |
| **AWS PyTorch Training NeuronX 2.7.0** | 12.8 GB | 21 | 3.9 GB |
| **AWS SageMaker Distribution 4.2.1 GPU** | 10.5 GB | 28 | 9.4 GB |

Notice that layers within an image are not roughly equal in size. A single layer can account for more than half the total image, with individual layers often reaching 9 GB or larger, while the remaining layers are comparatively small. This size disparity has direct consequences for how long a pull takes, as the next sections explain.

Getting each of these layers onto a node involves six stages, and traditionally containerd, the industry-standard container runtime, performed most of these operations sequentially.

## The stages of a pull

![Diagram showing the six stages of a container image pull](https://cdn.thenewstack.io/media/2026/08/4f07e41c-image-1024x378.png)

For each layer, containerd performs six operations in sequence. The first three are the download phase: fetch the compressed bytes from the registry over a single HTTP connection, verify the bytes by computing their SHA-256 and comparing it against the manifest digest, and write the compressed blob to local disk.

The next three are the unpack phase: decompress the gzip archive, verify the decompressed content by computing a second SHA-256, and extract the files into the local snapshot directory managed by a containerd snapshotter, the component that stores and serves the on-disk representation of each layer. By default, containerd downloads up to three layers in parallel, but each layer uses a single connection, and unpacking remains strictly sequential across layers.

Two details are worth noting. Both SHA-256 checks mentioned above are mandated by the Open Container Initiative (OCI) specification, and on a multi-gigabyte layer, each of these hashes requires real work. The first is computed over the compressed bytes and proves the download was not corrupted or tampered with.

The second is computed over the decompressed content. It gives the runtime a stable fingerprint of the layer’s actual filesystem data, which is what allows it to recognize shared layers across images and avoid redundant unpacking. Decompression is another deceptively expensive operation on large layers: gzip often triples a layer’s size on expansion, and because each block depends on the previous one, it runs on a single core. At the same time, the rest of the instance sits idle.

Downloading layers can be parallelized, but the unpack sequence runs layer by layer. Layer two cannot begin until layer one finishes all six stages. The result is that at any given moment during a pull, the node is bottlenecked on only one resource: network bandwidth during download, CPU during decompression and hash verification, or disk throughput during extraction. The other resources sit idle, waiting their turn in the pipeline.

> “Because layers are not equally sized, the single largest layer becomes the long pole in the pipeline.”

Because layers are not equally sized, the single largest layer becomes the long pole in the pipeline. A 10 GB layer that takes a minute to decompress on one core holds up the entire image, even if the other layers finish in seconds. Total pull time is effectively bounded by that one dominant layer moving through all six stages.

## Existing approaches: working around the pull

There are well-known approaches to reducing image pull times. Each works around the bottleneck differently, whether by altering images, caching them, or relying on assistance from other parts of the stack.

**Image size reduction:** The most direct approach is to make images smaller through multi-stage builds, distroless base images, and stripping unused packages. For ML workloads, this hits hard limits. The GPU software stack alone (PyTorch, cuDNN, CUDA) imposes a compressed floor of roughly 3 to 4 GB that no build optimization can remove. Beyond that, ML images are assembled across organizational boundaries: a platform team provides the OS and drivers, a frameworks team adds deep-learning libraries, and researchers contribute application code and model weights. No single team controls the final artifact; model weights frequently end up baked in because serving frameworks expect local paths, and multi-stage builds yield only single-digit percentage savings on images whose bulk is irreducible.

**Image caching (pre-pulling):** Cache images on nodes by snapshotting image content into a volume and mounting it at provisioning time, so subsequent launches skip the pull entirely. This works for stable images but adds a dedicated pipeline stage for each image version. For ML workloads, the challenge goes beyond frequent rebuilds: a common pattern is a single pod consuming an entire node, so nodes scale in and out with each scheduling decision and every new node faces the full cold pull. This limits pre-caching to workloads with long-lived, static node pools.

> “The GPU software stack alone (PyTorch, cuDNN, CUDA) imposes a compressed floor of roughly 3 to 4 GB that no build optimization can remove.”

**Registry-side optimization:** Some approaches serve image content remotely rather than pulling it to the node. Alibaba’s DADI, for example, presents container images as remote block devices that the node mounts on demand without a discrete pull step. This eliminates startup latency for workloads that access only a fraction of their image. Still, the container depends on the network throughout its lifetime and requires purpose-built serving infrastructure that may not be portable across providers.

**Lazy loading:** Instead of pulling the whole image up front, start the container immediately and fetch file content on demand. Projects in this space include eStargz and Nydus (which require converting the image to a new format) and AWS’s SOCI (Seekable OCI), which adds a seekable index alongside the unmodified image. These techniques work well when containers touch only a fraction of their data at startup. Still, ML images densely access the framework, CUDA libraries, and model weights before serving the first request, so nearly all the data ends up being fetched anyway. For these workloads, the pull pipeline itself needs to be faster.

**Peer-to-peer distribution within the cluster:** Tools like Dragonfly (a CNCF graduated project) and Spegel turn nodes that already have an image into seeders for nodes that need it, reducing registry egress and accelerating rolling deployments. For ML workloads, though, the first node still faces the full cold pull, and when images are rebuilt frequently, no node has the new version cached yet. P2P distribution complements rather than replaces improvements to the pull pipeline itself.

## Fixing the image pull pipeline

Out of the six stages in [the pull pipeline](https://thenewstack.io/solving-the-validation-problem/), we focused on two: downloading the layer blob from the registry, and unpacking the layers on the node. These are where the most time is spent and where the serialization cost is highest.

Since SOCI was already an open-source containerd snapshotter plugin with the plumbing to intercept and customize the pull path, it served as a staging ground where we could develop and validate these changes before contributing them upstream to containerd.

### Download: sharding a single layer into multiple requests

containerd traditionally uses a single HTTP connection to download each layer. We identified that splitting a layer into fixed-size chunks and fetching them concurrently over separate connections using HTTP range requests was significantly faster. At the same time, the containerd community also independently added parallel chunked download support in containerd 2.1, and we built on the same principle in the SOCI snapshotter.

However, there is one significant difference that allows us to keep the runtime’s memory footprint constant regardless of image size. The difference is where chunks live between arrival and final assembly. Our implementation writes each chunk directly to the local disk the moment it arrives, while containerd holds it in memory as the layer is assembled. This means the runtime’s memory stays flat whether you are pulling a 1 GB layer or a 15 GB layer, which matters on GPU nodes where system memory is shared with model weights and CUDA contexts.

Once download completes in seconds rather than minutes, the compressed layer hash that previously hid behind it becomes visible. Because the layer is now a complete file on disk rather than a stream consumed once, integrity verification and unpacking can proceed at the same time.

### Unpack: All layers concurrently

After downloading, containerd decompresses and extracts each layer one at a time. This sequencing exists because in some filesystem backends, a later layer can overwrite files from an earlier one, so the order matters. The overlay snapshotter, which is the default on EKS and most Kubernetes clusters, sidesteps this constraint by keeping each layer in its own separate directory. The kernel mounts them together into one unified view only when the container starts. Because each layer extracts to an independent directory, unpacking one layer does not need to depend on another to finish.

With that established, we built an unpack path that decompresses and extracts all layers concurrently. The snapshotter detects whether the backend actually requires ordering and falls back to sequential if it does. For images with multiple large layers, total unpack time goes from the sum of all layers to roughly the time of the single largest one. We contributed this parallel unpack capability upstream to containerd v2.2, so the improvement is available to the broader community.

### What this looks like in practice

With chunked parallel download, a large layer that previously took over a minute on a single connection finishes in single-digit seconds. When you then unpack all layers concurrently rather than sequentially, the full pipeline for a large ML image compresses from several minutes to well under a minute on instances with fast local NVMe storage. The machine spends its available compute and bandwidth actively pulling rather than waiting on serial stages. On larger images and instances with faster storage, the gains are more pronounced because the gap between available hardware capacity and what a single connection can use is wider.

### What’s next

The two changes above address download and layer sequencing, but decompression of a single large layer remains serial. On a 64 vCPU machine, decompressing a layer that expands to 18 GB means a lot of compute sitting idle. Two opportunities stand out:

Parallel decompression within a single layer. Libraries like rapidgzip can locate block boundaries and inflate blocks across cores in parallel.

Parallelizable integrity verification. Today, the layer hash requires a single sequential read over the entire compressed blob after all bytes have landed. A tree-structured hash like BLAKE3 would allow computing the layer digest from independently hashed chunks so that verification could run in parallel with download rather than as a separate pass afterward.

Addressing these opportunities will squeeze out the last remaining serial stages in the pull path, bringing total pull time closer to what the raw hardware is capable of delivering.

## Using parallel download and unpack with Amazon EKS

This image pull optimization is enabled by default on G/P/Trn instances with EKS Auto Mode. You can also benefit from this on other node types through one of two mechanisms:

* Native containerd 2.2: parallel download and unpack built into the runtime. Use when your node already runs containerd 2.2.
* SOCI snapshotter: parallel download and unpack with a memory-bounded download path. Use on older nodes without containerd 2.2 or memory-constrained instances.

EKS AL2023 and Bottlerocket AMIs that ship with containerd 2.2 do not enable this feature by default, but you can set the containerd config explicitly as shown below:

AL2023: add the containerd config through the nodeadm NodeConfig in user data:

```

apiVersion: node.eks.aws/v1alpha1
  kind: NodeConfig
  spec:
    containerd:
      config: |
        [plugins.'io.containerd.transfer.v1.local']
          max_concurrent_downloads = 20
          concurrent_layer_fetch_buffer = 16777216
          max_concurrent_unpacks = 5

```

Bottlerocket (K8s 1.36): Bottlerocket generates the same containerd config from its settings API, so set the equivalent keys in user data:

```

[settings.container-runtime]
  max-concurrent-downloads = 20
  concurrent-download-chunk-size = 16777216
  max-concurrent-unpacks = 5

```

SOCI snapshotter is bundled in the optimized EKS AMIs (AL2023 and Bottlerocket).

Bottlerocket: enable SOCI through EC2 user data:

```

[settings.container-runtime]
  snapshotter = "soci"
 [settings.container-runtime-plugins.soci-snapshotter.parallel-pull-unpack]
  max-concurrent-downloads = 20
 concurrent-download-chunk-size = "16mb"
 max-concurrent-unpacks-per-image = 5

```

Tune chunk size and concurrency under [settings.container-runtime-plugins.soci-snapshotter.parallel-pull-unpack]; the right values depend on your instance type and images.

AL2023: enable SOCI through the nodeadm FastImagePull feature gate, which switches image pulls to SOCI’s parallel-pull-unpack mode, and you can override the SOCI tuning parameters through user-data:

```

apiVersion: node.eks.aws/v1alpha1
  kind: NodeConfig
  spec:
    featureGates:
      FastImagePull: true

```

The image pull problem was never really about the registry, and it was never about needing faster hardware. The network, the storage, and the CPU were always there. When containerd’s pull pipeline took shape, images were measured in hundreds of megabytes, and the sequential approach served that world well.

> “The image pull problem was never really about the registry, and it was never about needing faster hardware.”

As AI and ML workloads pushed images past 20 GB, the gap between available hardware throughput and what the pull path was utilizing became impossible to ignore. For workloads running on the overlay snapshotter with high-bandwidth instances and fast local storage, parallelizing download and unpack closes most of that gap today. Other snapshotters and storage backends may have different constraints, and opportunities like parallel decompression and parallelizable integrity verification remain open.

We have been contributing these changes upstream because this is where they belong: in the runtime itself, available to everyone by default rather than locked behind additional software. Some of that work has already landed in containerd 2.2, and more is in progress.

If you are working on container runtimes, image formats, or compression tooling and any of the open problems described here interest you, we would welcome collaboration. The faster we can collectively close the remaining serial stages, the sooner multi-gigabyte images stop being a [deployment bottleneck](https://thenewstack.io/the-deployment-bottleneck-no-one-talks-about/) for the entire ecosystem.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/7f8a61d7-srisaranbalaji-600x600.png)

Sri Saran Balaji Vellore Rajakumar is a Principal Engineer at Amazon Web Services and a founding engineer of Amazon EKS, where he has spent nearly a decade building the infrastructure that keeps the EKS control plane available and performant at...

Read more from Sri Saran Balaji Vellore Rajakumar](https://thenewstack.io/author/sri-saran-balaji-vellore-rajakumar/)

[![](https://thenewstack.io/wp-content/uploads/2026/06/404962af-cropped-1d0a0b80-neelendra_bhandari-600x600.png)

Neelendra Bhandari is a Senior Software Development Manager at Amazon Web Services, where he leads teams building the Amazon EKS Kubernetes Control Plane. His work spans Kubernetes scalability, etcd reliability, and the systems that power EKS features like Provisioned Control...

Read more from Neelendra Bhandari](https://thenewstack.io/author/neelendra-bhandari/)