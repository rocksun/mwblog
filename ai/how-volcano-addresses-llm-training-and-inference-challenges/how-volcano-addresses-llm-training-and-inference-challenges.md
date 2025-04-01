
<!--
title: Volcano 如何应对 LLM 训练和推理挑战
cover: https://cdn.thenewstack.io/media/2025/04/4e542594-volcano-kubecon-europe.jpg
summary: Volcano如何应对LLM训练挑战？利用HyperNode实现网络拓扑感知调度，优化InfiniBand等异构环境通信；集成Karmada实现多集群调度，支持队列/作业优先级；细粒度故障恢复提升稳定性。未来将支持任务级拓扑亲和性、DRA和动态GPU分区。
-->

Volcano如何应对LLM训练挑战？利用HyperNode实现网络拓扑感知调度，优化InfiniBand等异构环境通信；集成Karmada实现多集群调度，支持队列/作业优先级；细粒度故障恢复提升稳定性。未来将支持任务级拓扑亲和性、DRA和动态GPU分区。

> 译自：[How Volcano Addresses LLM Training and Inference Challenges](https://thenewstack.io/how-volcano-addresses-llm-training-and-inference-challenges/)
> 
> 作者：Xuzheng Chang

[大型语言模型（LLM）](https://thenewstack.io/what-is-a-large-language-model/)的日益普及，提高了对高效AI训练和推理工作负载的需求。随着模型大小和复杂性的增长，分布式训练和推理已变得至关重要。然而，这种扩展给大规模分布式环境中的网络通信、资源分配和故障恢复带来了挑战。这些问题通常会造成性能瓶颈，从而阻碍可扩展性。

## 通过拓扑感知调度解决瓶颈

在LLM训练中，模型并行将工作负载分布在多个节点上，需要频繁的数据交换。网络通信可能会成为瓶颈，尤其是在具有InfiniBand（IB）、RoCE或NVSwitch配置的异构环境中。通信效率取决于网络拓扑——节点之间的交换机越少，通常延迟越低，吞吐量越高。

缓解此挑战的一种方法是网络拓扑感知调度，该调度优化工作负载放置，以最大程度地减少跨交换机的通信。[自定义资源定义](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/)（CRD）通过HyperNode表示网络拓扑，它是该策略的关键组件。

与基于标签的方法不同，HyperNode提供了一个反映实际网络布局的分层结构，从而改善了管理和优化。同一HyperNode中的节点之间的通信效率高于跨多个层的节点。

![HyperNode architecture](https://cdn.thenewstack.io/media/2025/04/f1c5b204-hypernode-architecture.jpg)

*来源：华为*

还可以通过networkTopology字段为作业指定拓扑约束，并可以选择严格（Hard Mode）或灵活（Soft Mode）执行。这种精细的控制有助于确保将工作负载部署在最佳网络环境中，从而减少延迟并提高吞吐量。

## 管理多集群环境以实现可扩展性

随着AI工作负载的扩展，单个Kubernetes集群可能不再足以满足大规模训练和推理的需求。虽然多个集群可以解决此限制，但有效管理它们会带来挑战。

云原生计算基金会（CNCF）孵化项目[Volcano](https://volcano.sh/)将调度功能扩展到多集群环境，并与Kubernetes管理系统[Karmada](https://thenewstack.io/karmada-finally-brings-multicloud-control-to-kubernetes)集成，以实现分布式工作负载的跨集群调度。队列优先级调度、作业优先级调度和多租户公平调度等功能有助于优化资源分配，并确保跨租户的公平访问。这种方法简化了多集群管理，同时支持可扩展的AI工作负载。

![Architecture of Volcano - Karmada interactions](https://cdn.thenewstack.io/media/2025/04/9dd710c1-volcano-architecture.png)

来源：华为

## 通过细粒度故障恢复提高稳定性

故障恢复在分布式AI训练和推理中至关重要。传统方法通常会在单个Pod发生故障时重新启动整个作业，从而导致资源效率低下。借助检查点和从检查点恢复技术，通常不需要完全重新启动。

细粒度的作业故障恢复策略允许仅重新启动失败的Pod或关联的任务，从而减少不必要的中断。超时配置可以进一步最大程度地减少干预；如果Pod在分配的时间内恢复，则不会触发重新启动。这种方法提高了分布式工作负载的稳定性和效率。

## 分布式工作负载管理的未来发展

分布式工作负载管理方面的持续进展包括：

- **任务级网络拓扑亲和性调度**：支持分布式推理场景，例如与lws集成。
- **HyperNode自动发现和状态更新**：HyperNode生命周期管理的自动化。
- **动态资源分配（DRA）**：改进了异构资源的管理。
- **动态GPU分区**：支持多实例GPU（MIG）和多进程服务（MPS），以提高GPU利用率。

要了解有关Volcano的更多信息，请查看我们的[GitHub存储库](https://github.com/volcano-sh/volcano)，加入[Volcano Slack](https://cloud-native.slack.com/archives/C011GJDQS0N)上的对话或参加我们的[每周会议](https://zoom.us/j/91804791393)并查看过去的[会议记录](https://docs.google.com/document/d/1YLbF8zjZBiR9PbXQPB22iuc_L0Oui5A1lddVfRnZrqs/edit#heading=h.u99fvvct3m1z)。
想了解更多关于 Kubernetes 和云原生生态系统的信息，请于 4 月 1 日至 4 日在伦敦参加 KubeCon + CloudNativeCon 欧洲大会。