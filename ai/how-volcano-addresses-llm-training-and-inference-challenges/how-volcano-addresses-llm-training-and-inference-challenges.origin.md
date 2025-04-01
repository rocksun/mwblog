# How Volcano Addresses LLM Training and Inference Challenges
![Featued image for: How Volcano Addresses LLM Training and Inference Challenges](https://cdn.thenewstack.io/media/2025/04/4e542594-volcano-kubecon-europe-1024x576.jpg)
The increasing adoption of [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) has heightened the demand for efficient AI training and inference workloads. As model size and complexity grow, distributed training and inference have become essential. However, this expansion introduces challenges in network communication, resource allocation and fault recovery within large-scale distributed environments. These issues often create performance bottlenecks that hinder scalability.

## Addressing Bottlenecks Through Topology-Aware Scheduling
In LLM training, model parallelism distributes workloads across multiple nodes, requiring frequent data exchanges. Network communication can become a bottleneck, particularly in heterogeneous environments with InfiniBand (IB), RoCE or NVSwitch configurations. Communication efficiency depends on network topology — fewer switches between nodes typically result in lower latency and higher throughput.

One approach to mitigating this challenge is network topology-aware scheduling, which optimizes workload placement to minimize cross-switch communication. A key component of this strategy is the HyperNode, an abstraction for representing network topology via [Custom Resource Definitions](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/) (CRDs).

Unlike label-based methods, HyperNode provides a hierarchical structure that reflects actual network layouts, improving management and optimization. Nodes within the same HyperNode communicate more efficiently than those spanning multiple layers.

![HyperNode architecture](https://cdn.thenewstack.io/media/2025/04/f1c5b204-hypernode-architecture.jpg)
Source: Huawei

Topology constraints can also be specified for jobs through the networkTopology field, with options for strict (Hard Mode) or flexible (Soft Mode) enforcement. This granular control helps ensure workloads are deployed in optimal network environments, reducing latency and improving throughput.

## Managing Multicluster Environments for Scalability
As AI workloads expand, single Kubernetes clusters may no longer suffice for large-scale training and inference. While multiple clusters can address this limitation, managing them efficiently presents challenges.

The Cloud Native Computing Foundation (CNCF) incubating project [Volcano](https://volcano.sh/) extends scheduling capabilities to multicluster environments, integrating with the Kubernetes management system [Karmada](https://thenewstack.io/karmada-finally-brings-multicloud-control-to-kubernetes) to enable cross-cluster scheduling for distributed workloads. Features such as queue priority scheduling, job priority scheduling and multitenant fair scheduling help optimize resource allocation and ensure equitable access across tenants. This approach simplifies multicluster management while supporting scalable AI workloads.

![Architecture of Volcano - Karmada interactions](https://cdn.thenewstack.io/media/2025/04/9dd710c1-volcano-architecture.png)
Source: Huawei

## Improving Stability With Fine-Grained Fault Recovery
Fault recovery is critical in distributed AI training and inference. Traditional methods often restart entire jobs upon a single pod failure, leading to resource inefficiencies. With checkpointing and resume-from-checkpoint techniques, full restarts are often unnecessary.

Fine-grained job fault recovery allows policies to restart only failed pods or associated tasks, reducing unnecessary disruptions. Timeout configurations can further minimize interventions; if a Pod recovers within the allotted time, no restart is triggered. This approach enhances stability and efficiency in distributed workloads.

## Future Developments in Distributed Workload Management
Ongoing advancements in distributed workload management include:

**Task-level network topology affinity scheduling:**Support for distributed inference scenarios, such as integration with lws.**HyperNode auto-discovery and status updates:**Automation for HyperNode life-cycle management.**Dynamic resource allocation (DRA):**Improved management of heterogeneous resources.**Dynamic GPU partitioning:**Support for Multi-Instance GPU (MIG) and Multi-Process Service (MPS) to enhance GPU utilization.
To learn more about Volcano, check out our [GitHub repository](https://github.com/volcano-sh/volcano), join the conversation on [Volcano Slack](https://cloud-native.slack.com/archives/C011GJDQS0N) or attend our [weekly meetings](https://zoom.us/j/91804791393) and review past [meeting notes](https://docs.google.com/document/d/1YLbF8zjZBiR9PbXQPB22iuc_L0Oui5A1lddVfRnZrqs/edit#heading=h.u99fvvct3m1z).

*To learn more about Kubernetes and the cloud native ecosystem, join us at KubeCon + CloudNativeCon Europe in London on April 1-4.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)