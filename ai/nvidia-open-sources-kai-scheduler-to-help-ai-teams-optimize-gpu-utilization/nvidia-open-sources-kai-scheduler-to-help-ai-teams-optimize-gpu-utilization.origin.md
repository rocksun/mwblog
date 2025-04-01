# NVIDIA Open Sources KAI Scheduler To Help AI Teams Optimize GPU Utilization
![Featued image for: NVIDIA Open Sources KAI Scheduler To Help AI Teams Optimize GPU Utilization](https://cdn.thenewstack.io/media/2025/03/38e95859-nvidia-gtp-logo-1024x576.jpg)
At KubeCon Europe, NVIDIA announced today that it is open sourcing [KAI Scheduler](https://github.com/NVIDIA/KAI-scheduler), a GPU-centric Kubernetes scheduler that was originally developed by Run:ai, which NVIDIA acquired last year. Available under the Apache 2.0 license, KAI Scheduler helps its users optimize GPU resource allocations for AI and machine learning workloads in GPU clusters.

NVIDIA argues that traditional resource schedulers are ill-suited for managing AI workloads because GPU demand can fluctuate quite a lot, with bursty inference workloads and sustained model training runs that can extend over days.

KAI Scheduler promises to give these teams a better tool for managing these workloads by, among other things, dynamically adjusting quotas and limits in real time, while also offering a variety of scheduling strategies — gang scheduling, hierarchical queuing, bin-packing, spreading and GPU sharing — to avoid long wait times for access to GPUs.

Sharing GPUs looks like it will be an especially useful feature here. This allows multiple pods to utilize the same GPU, for example. It’s worth noting that NVIDIA already offers a tool called [GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html), a Kubernetes framework for provisioning GPUs, which also includes a GPU time-slicing feature.

GPU Operator, however, is very much focused on working with NVIDIA hardware and large clusters (including NVIDIA’s own DGX racks), while KAI Scheduler is more vendor-agnostic and also supports AI workloads on CPUs.

KAI Scheduler’s approach, other than GPU sharing, focuses on the individual GPUs and the memory available to them. What developers can reserve here is a share of that memory. There is no memory isolation, though.

By default, KAI Scheduler integrates with popular AI tools and cloud native frameworks like Kubeflow’s Training Operator, Ray and Argo.

The code and documentation for KAI Scheduler is now [available on GitHub](https://github.com/NVIDIA/KAI-Scheduler). Quite a few other parts of Run:ai are already open source, too, including the somewhat related [Genv](https://github.com/run-ai/genv) GPU environment and cluster management tools.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)