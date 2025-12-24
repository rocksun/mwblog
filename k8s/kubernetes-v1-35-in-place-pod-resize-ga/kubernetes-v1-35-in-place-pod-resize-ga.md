<!--
title: Kubernetes 1.35：Pod 原地扩缩容，稳定版重磅发布！
cover: https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/k8s-v1.35.png
summary: Kubernetes 1.35: Pod 原地扩缩容功能已升级至稳定版。它允许运行中调整 Pod 的 CPU/内存资源，无需重启。这提升了资源效率和灵活性，并支持无中断自动扩缩。
-->

Kubernetes 1.35: Pod 原地扩缩容功能已升级至稳定版。它允许运行中调整 Pod 的 CPU/内存资源，无需重启。这提升了资源效率和灵活性，并支持无中断自动扩缩。

> 译自：[Kubernetes 1.35: In-Place Pod Resize Graduates to Stable](https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/)
> 
> 作者：Natasha Sarkar (Google)

此次发布标志着一个重要里程碑：**Pod 原地扩缩容**功能（也称为 Pod 垂直扩缩容）在其最初构想提出超过6年后，于 Kubernetes v1.27 中首次作为 alpha 版引入，在 Kubernetes v1.33 中升级至 beta 版，现已在 Kubernetes 1.35 中正式升级至**稳定版 (GA)**！

此次升级是提高 Kubernetes 上运行工作负载的资源效率和灵活性的一个重要里程碑。

## 什么是 Pod 原地扩缩容？

过去，分配给 Pod 中容器的 CPU 和内存资源是不可变的。这意味着更改它们需要删除并重新创建整个 Pod。对于有状态服务、批处理作业或对延迟敏感的工作负载，这是一种极具破坏性的操作。

Pod 原地扩缩容使 CPU 和内存请求和限制变得可变，允许您在运行中的 Pod 内调整这些资源，通常无需重新启动容器。

**关键概念：**

*   **期望资源*：** 容器的 `spec.containers[*].resources` 字段现在代表期望的资源。对于 CPU 和内存，这些字段现在是可变的。
*   **实际资源：** `status.containerStatuses[*].resources` 字段反映了当前为运行中容器配置的资源。
*   **触发调整大小：** 您可以通过利用新的 `resize` 子资源，更新 Pod 规范中期望的 `requests` 和 `limits` 来请求调整大小。

## 如何开始使用 Pod 原地扩缩容？

详细的使用说明和示例可在官方文档中找到：[调整分配给容器的 CPU 和内存资源](/docs/tasks/configure-pod-container/resize-container-resources/)。

## 这对您有何帮助？

Pod 原地扩缩容是一个基础构建块，它实现了无缝的垂直自动扩缩和工作负载效率的提升。

*   **无中断的资源调整** 对延迟或重启敏感的工作负载可以在不中断或不丢失状态的情况下就地修改其资源。
*   **更强大的自动扩缩** 自动扩缩器现在能够以更小的影响调整资源。例如，垂直 Pod 自动扩缩器 (VPA) 的 `InPlaceOrRecreate` 更新模式（利用了此功能）已升级至 beta 版。这使得资源可以根据使用情况自动、无缝地进行调整，并将中断降至最低。
*   **解决瞬时资源需求** 暂时需要更多资源的工作负载可以快速调整。这使得 CPU 启动加速 ([AEP-7862](https://github.com/kubernetes/autoscaler/pull/7863)) 等功能成为可能，应用程序可以在启动时请求更多 CPU，然后自动缩减。

以下是一些用例示例：

*   需要根据玩家数量变化调整大小的游戏服务器。
*   一个预热的工作器，可以在不使用时缩小，但在收到第一个请求时膨胀。
*   根据负载动态扩缩，实现高效的装箱。
*   在启动时增加 JIT 编译的资源。

## Beta 版 (1.33) 和稳定版 (1.35) 之间的变化

自 v1.33 首次发布 beta 版以来，开发工作主要围绕根据社区反馈稳定功能并提高其可用性。以下是稳定版的主要变化：

*   **内存限制降低** 以前禁止降低内存限制。此限制已被解除，现在允许降低内存限制。Kubelet 尝试通过仅在当前内存使用低于新的期望限制时才允许调整大小来防止 OOM-kill。但是，此检查是尽力而为的，不作保证。
*   **优先调整大小** 如果节点没有足够的空间来接受所有调整大小请求，将根据以下优先级重新尝试*延迟*的调整大小：
    + PriorityClass
    + QoS class
    + *延迟*时长，较旧的请求优先。
*   **Pod 级别资源 (Alpha)** 对 Pod 级别资源的 Pod 原地扩缩容的支持已在其自己的功能门后引入，该功能在 v1.35 中为 alpha 版。
*   **增强的**可观测性**：** 现在有新的 Kubelet 指标和 Pod 事件，专门与 Pod 原地扩缩容相关联，以帮助用户跟踪和调试资源更改。

## 接下来是什么？

Pod 原地扩缩容功能升级至稳定版，为 Kubernetes 生态系统中的强大集成打开了大门。目前计划有几个进一步改进的领域。

### 与自动扩缩器和其他项目的集成

计划与多个自动扩缩器和其他项目进行集成，以更大规模地提高工作负载效率。正在讨论的一些项目包括：

*   VPA CPU 启动加速 ([AEP-7862](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/enhancements/7862-cpu-startup-boost))：允许应用程序在启动时请求更多 CPU，并在特定时间段后缩减。
*   VPA 对就地更新的支持 ([AEP-4016](https://github.com/kubernetes/autoscaler/tree/455d29039bf6b1eb9f784f498f28769a8698bc21/vertical-pod-autoscaler/enhancements/4016-in-place-updates-support))：VPA 对 `InPlaceOrRecreate` 的支持最近已升级至 beta 版，最终目标是使该功能升级至稳定版。对 `InPlace` 模式的支持仍在进行中；请参阅 [这个 Pull Request](https://github.com/kubernetes/autoscaler/pull/8818)。
*   Ray 自动扩缩器：计划利用 Pod 原地扩缩容来提高工作负载效率。有关更多详细信息，请参阅 [这篇 Google Cloud 博客文章](https://cloud.google.com/blog/products/containers-kubernetes/ray-on-gke-new-features-for-ai-scheduling-and-scaling)。
*   Agent-sandbox "Soft-Pause"：正在研究利用 Pod 原地扩缩容来更好地改善延迟。有关更多详细信息，请参阅 [GitHub issue](https://github.com/kubernetes-sigs/agent-sandbox/issues/103)。
*   运行时支持：Java 和 Python 运行时不支持在不重启的情况下调整内存。与 Java 开发人员的讨论正在进行中，请参阅 [这个 bug](https://bugs.openjdk.org/browse/JDK-8359211)。

如果您有项目可以从 Pod 原地扩缩容的集成中受益，请使用反馈部分中列出的渠道与我们联系！

### 功能扩展

目前，当 Pod 原地扩缩容与 swap、静态 CPU Manager 和静态 Memory Manager 结合使用时是被禁止的。此外，CPU 和内存以外的资源仍然是不可变的。随着社区需求反馈的增加，正在考虑扩展受支持的功能和资源集。

还计划支持工作负载抢占；如果节点上没有足够的空间来调整高优先级 Pod 的大小，目标是启用策略以自动驱逐低优先级 Pod 或扩容节点。

### 提高稳定性

*   **解决 kubelet-scheduler 竞态条件** Kubelet 和调度器之间存在关于 Pod 原地扩缩容的已知竞态条件。目前正在努力在接下来的几个版本中解决这些问题。有关更多详细信息，请参阅 [该 issue](https://github.com/kubernetes/kubernetes/issues/126891)。
*   **更安全的内存限制降低** 通过将内存使用检查移至容器运行时本身，Kubelet 尽力而为的 OOM-kill 预防检查可以变得更安全。有关更多详细信息，请参阅 [该 issue](https://github.com/kubernetes/kubernetes/issues/135670)。

## 提供反馈

期待在此基础功能上进一步构建，请分享您对如何改进和扩展此功能的反馈。您可以通过 GitHub issue、邮件列表或与 Kubernetes [#sig-node](https://kubernetes.slack.com/archives/C0BP8PW9G) 和 [#sig-autoscaling](https://kubernetes.slack.com/archives/C09R1LV8S) 社区相关的 Slack 频道分享您的反馈。

感谢所有为实现这一期待已久的功能做出贡献的人！