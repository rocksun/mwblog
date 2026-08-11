Consider a platform team managing a shared GPU cluster with a mix of B200s, H100s, and recently added B300s. Every Monday morning, the on-call engineer finds a queue of pending jobs from the weekend. Training workloads are stuck because they landed on H100s and triggered Out-Of-Memory (OOM) errors. Inference jobs sit idle because the small MIG (Multi-Instance GPU) slices are exhausted, even though larger slices sit empty right next to them.

Their fix? A 200-line Bash script running every 30 minutes to reconfigure MIG profiles, reschedule stuck jobs, and send a Slack alert when it succeeds, or a PagerDuty alert when it fails.

## The root of the problem

Here is what was actually broken: Kubernetes treated every GPU as an identical unit. The resource limit nvidia.com/gpu: 1 was the extent of its awareness. The scheduler had no idea if it was handing a pod a 192GB B200 or an 80GB H100. A training job requiring 150GB of VRAM would land on an H100 and immediately OOM, while B200 nodes sat completely idle nearby.

> “Kubernetes treated every GPU as an identical unit.”

The industry’s accepted “fix” relied heavily on node labels, taints, tolerations, and separate [node pools per GPU](https://thenewstack.io/self-healing-gpu-nodes/) type. Every workload manifest hardcoded hardware assumptions. Adding a single new GPU generation meant updating 40 different Helm charts.

## The MIG illusion

MIG made this worse. MIG slices a single GPU into smaller, isolated partitions, each with dedicated memory and compute. Instead of one inference job monopolizing a B200, you can run seven smaller jobs on the same card.

In theory, this sounds great. But when you enable [MIG in Kubernetes](https://thenewstack.io/managed-k8s-with-gpu-worker-nodes-for-faster-ai-ml-inference/), each profile becomes a separate, rigid resource type (e.g., nvidia.com/mig-1g.10gb, nvidia.com/mig-3g.40gb). There is no fallback logic. You cannot instruct a job to “try a small slice first, and use a large one if nothing else is free.” When small slices run out, jobs sit pending, while large slices go to waste.

> “When small slices run out, jobs sit pending, while large slices go to waste.”

This inefficiency was accepted as the cost of running GPU workloads on Kubernetes. Then, Kubernetes 1.34 shipped.

## Dynamic Resource Allocation (DRA)

Kubernetes 1.34 introduced [Dynamic Resource Allocation (DRA)](https://thenewstack.io/kubernetes-get-the-most-from-dynamic-resource-allocation/), fundamentally changing the scheduling model. GPU drivers now publish structured data. Instead of requesting a generic nvidia.com/gpu: 1, workloads can express explicit intent using Common Expression Language (CEL):

1. “Give me an H100 or better with at least 40GB of memory.”
2. “Give me a MIG slice: small if available, medium if not, or a full GPU if necessary.”
3. “Give me four GPUs connected via NVLink.”

### Example 1: Hardware and memory requirements

*“Give me an H100 or better with at least 40GB memory.”*

|  |
| --- |
| `apiVersion: resource.k8s.io/v1`  `kind: ResourceClaimTemplate`  `metadata:`  `name: h100-or-better-40gb`  `spec:`  `spec:`  `devices:`  `requests:`  `- name: gpu`  `deviceClassName: gpu.nvidia.com`  `count: 1`  `selectors:`  `- cel:`  `# Attribute names are illustrative.`  `# Your NVIDIA DRA driver must expose these fields.`  `expression: >`  `device.attributes["gpu.nvidia.com"].memory >= quantity("40Gi") &amp;&amp;`  `device.attributes["gpu.nvidia.com"].generation in ["H100", "B200", "B300"]`  `---`  `apiVersion: batch/v1`  `kind: Job`  `metadata:`  `name: training-job-h100-or-better`  `spec:`  `template:`  `spec:`  `restartPolicy: Never`  `resourceClaims:`  `- name: gpu`  `source:`  `resourceClaimTemplateName: h100-or-better-40gb`  `containers:`  `- name: trainer`  `image: nvcr.io/nvidia/pytorch:24.12-py3`  `command: ["python", "train.py"]`  `resources:`  `claims:`  `- name: gpu` |

### Example 2: Flexible MIG fallback

*“Give me a MIG slice: small if available, medium if not, or full GPU if needed.”*

|  |
| --- |
| `apiVersion: resource.k8s.io/v1`  `kind: ResourceClaimTemplate`  `metadata:`  `name: mig-prefer-small-then-medium-then-full`  `spec:`  `spec:`  `devices:`  `requests:`  `- name: gpu`  `deviceClassName: gpu.nvidia.com`  `count: 1`  `selectors:`  `- cel:`  `# Prefer any acceptable MIG profile or full GPU`  `expression: >`  `device.attributes["gpu.nvidia.com"].profile in [`  `"mig-1g.10gb",`  `"mig-2g.20gb",`  `"mig-3g.40gb",`  `"full-gpu"`  `]`  `---`  `apiVersion: apps/v1`  `kind: Deployment`  `metadata:`  `name: inference-service-flexible-gpu`  `spec:`  `replicas: 2`  `selector:`  `matchLabels:`  `app: inference-service`  `template:`  `metadata:`  `labels:`  `app: inference-service`  `spec:`  `resourceClaims:`  `- name: gpu`  `source:`  `resourceClaimTemplateName: mig-prefer-small-then-medium-then-full`  `containers:`  `- name: inference`  `image: nvcr.io/nvidia/tritonserver:24.12-py3`  `args: ["tritonserver", "--model-repository=/models"]`  `resources:`  `claims:`  `- name: gpu` |

### Example 3: Topology constraints

*“Give me 4 GPUs that are NVLink-connected.”*

|  |
| --- |
| `apiVersion: resource.k8s.io/v1`  `kind: ResourceClaimTemplate`  `metadata:`  `name: four-nvlink-connected-gpus`  `spec:`  `spec:`  `devices:`  `requests:`  `- name: gpus`  `deviceClassName: gpu.nvidia.com`  `count: 4`  `selectors:`  `- cel:`  `# Attribute names are illustrative.`  `# Some NVIDIA DRA setups may model this through ComputeDomains.`  `expression: >`  `device.attributes["gpu.nvidia.com"].fabric == "nvlink"`  `constraints:`  `- requests: ["gpus"]`  `matchAttribute: "gpu.nvidia.com/nvlinkDomain"`  `---`  `apiVersion: batch/v1`  `kind: Job`  `metadata:`  `name: distributed-training-nvlink`  `spec:`  `template:`  `spec:`  `restartPolicy: Never`  `resourceClaims:`  `- name: gpus`  `source:`  `resourceClaimTemplateName: four-nvlink-connected-gpus`  `containers:`  `- name: trainer`  `image: nvcr.io/nvidia/pytorch:24.12-py3`  `command:`  `- torchrun`  `- --nproc_per_node=4`  `- train.py`  `resources:`  `claims:`  `- name: gpus` |

## The engineering takeaway

This architecture requires one manifest. It eliminates fragile node selectors and the need to duplicate job definitions for every new hardware generation. As GPU clusters become increasingly heterogeneous, mixing H100s, B200s, B300s, and whatever silicon drops next, the old integer-based scheduling model breaks down. DRA represents Kubernetes finally maturing to support the nuanced realities of production AI workloads.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/08/b1a6d7d7-cropped-49386b46-image-14-07-2026-at-2.30-am-600x600.png)

Dawood Abbas Ali is a DevOps/SRE Engineer with hands-on expertise in cloud infrastructure, Kubernetes, and CI/CD across AWS, GCP, Azure, and DigitalOcean. He writes about practical, real-world challenges in modern infrastructure and engineering.

Read more from Dawood Abbas](https://thenewstack.io/author/dawood-abbas/)