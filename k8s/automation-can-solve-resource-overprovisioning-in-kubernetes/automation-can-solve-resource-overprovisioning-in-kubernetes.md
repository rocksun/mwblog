
<!--
title: 自动化可以解决 Kubernetes 中的资源过度配置
cover: https://cdn.thenewstack.io/media/2025/03/41f1dbcb-light.jpg
-->

通过自动化解决 Kubernetes 环境中的低效问题，组织可以显著减少云浪费并提高资源利用率。

> 译自：[Automation Can Solve Resource Overprovisioning in Kubernetes](https://thenewstack.io/automation-can-solve-resource-overprovisioning-in-kubernetes/)
> 
> 作者：Laurent Gil

在云中运行 Kubernetes 应用程序的团队，在试图保证高性能和高可用性时，经常会陷入[过度配置的陷阱](https://thenewstack.io/neglect-kubernetes-resource-management-at-your-peril/)。因此，他们会产生云浪费，这会转化为组织的一项重大成本。

最近，Cast AI 发布了[2025 Kubernetes 成本基准报告](https://cast.ai/kubernetes-cost-benchmark/)，该报告显示，配置的资源和请求的资源之间的差距仍然很大——CPU 为 40%，内存为 57%。这表明团队在集群上部署的工作负载少于其容量。

值得注意的是，在分析的集群中，有 99.94% 的集群过度配置了 CPU，这是一个在主要云提供商（AWS、Google Cloud Platform 和 Microsoft Azure）中普遍存在的问题，资源效率没有显著差异。

这些低效率表明，挑战不在于云平台本身，而在于手动管理 Kubernetes 集群的复杂性。

## 过度配置只是问题的一个方面

Kubernetes 资源利用率的平均水平表明，问题不仅仅与所选计算实例的大小或类型有关。Kubernetes 集群的 CPU 利用率平均为 10%，内存利用率为 22%。这表明团队面临着另一个挑战：为 Kubernetes 工作负载设置正确的请求，而又不会有太多的余量。

尽管 Kubernetes 在云原生环境中得到了广泛采用，但管理云资源仍然是手动的，并且需要大量精力。当团队花费时间在重复性任务上并微观管理云基础设施时，他们倾向于过度配置集群，无法有效地将应用程序分配给它们，并通过在工作负载请求中留下大量余量来产生云浪费。

数据强调需要在 Kubernetes 环境中使用更好的工具和自动化来减少过度配置，提高[资源利用率并消除不必要的云成本](https://thenewstack.io/engineers-guide-to-cloud-cost-optimization-engineering-resources-in-the-cloud/)。

## 提高资源利用率和效率的六种方法

### 灵活的计算代系选择

自动化引擎使团队能够根据实时价格趋势，从不同代系的计算实例中动态选择。这将使他们能够利用最新的硬件来提高性能，或者选择较旧的、具有成本效益的代系来平衡预算。

下图说明了代表三个代系的三个计算实例的价格演变，表明实例选择的灵活性可以改变游戏规则。

![](https://cdn.thenewstack.io/media/2025/03/4ddcdc16-cast-ai-6-1024x563.png)

### 自动化处理器架构选择（x86 与 Arm）

在 x86 和 Arm 处理器之间进行选择可以显著节省成本，因为 Arm CPU 通常比 x86 更实惠。Azure、GCP 和 AWS 等平台上的 Arm 竞价实例始终提供更好的定价，最多可节省 65% 的成本。通过自动化跨架构的工作负载放置，团队可以确保最佳的性价比，而无需手动干预。

云提供商 | 每个 CPU 每小时的平均 x86 竞价价格 | 每个 CPU 每小时的平均 x86 按需价格 | 每个 CPU 每小时的平均 Arm 竞价价格 | 每个 CPU 每小时的平均 Arm 按需价格
---|---|---|---|---
Azure | $0.0254 | $0.1354 | $0.0079 | $0.0474
GCP | $0.0212 | $0.0659 | $0.0156 | $0.0410
AWS | $0.0389 | $0.0783 | $0.0200 | $0.0496

### 用于动态资源扩展的自定义自动缩放器

像 Akamai 这样的公司已经使用自定义自动缩放器来根据实时需求自动调整云资源。这种方法确保应用程序始终拥有必要的资源，同时最大限度地减少低使用期间的浪费。自动缩放优化了成本和性能，无需手动调整。

![](https://cdn.thenewstack.io/media/2025/03/41423561-cast-ai-3-1024x467.png)

### 对工作负载进行装箱以实现最大效率

组织可以通过对工作负载进行装箱来显著减少过度配置，特别是对 spot 友好的、无状态的工作负载。例如，Heureka Group 通过[自动优化](https://thenewstack.io/engineers-guide-to-cloud-cost-optimization-prioritize-cloud-rate-optimization/)工作负载放置和删除未使用的节点，实现了 30% 的计算成本降低。这种技术减少了空闲 CPU 的数量，并提高了整体利用率。

### 基于实时数据的自主请求设置

有状态的工作负载是内存密集型的。下面的示例说明了如果一家公司在工作负载级别使用自动缩放解决方案，并在某个时候将其关闭，可能会发生什么情况。

内存请求的急剧增加迫使系统配置更多资源。反过来，由于内存和 CPU 之间的相关性，这导致 CPU 配置增加，从而导致资源方面的巨额超支。

![](https://cdn.thenewstack.io/media/2025/03/3244f97c-cast-ai-5-1024x407.png)

### 安全地利用竞价实例

竞价实例提供大幅折扣，但由于中断风险，通常未得到充分利用。自动化可以帮助监控价格波动和中断率，从而使团队能够放心地采用[竞价实例用于非关键工作负载](https://thenewstack.io/saving-with-confidence-the-strategic-advantage-of-spot-instances/)。通过自动化此过程，公司可以最大限度地节省成本，而不会影响性能。

## 结论

自动化是解决困扰 Kubernetes 环境的低效率问题的强大解决方案。通过使用自动化工具和最佳实践（如灵活的计算代系选择、动态自动缩放和智能工作负载放置），组织可以显著减少云浪费并提高资源利用率。

随着云环境变得越来越复杂，这种方法对于确保有效利用资源、优化工作负载以及团队在不过度支出云基础设施的情况下继续创新至关重要。

*要了解有关 Kubernetes 和云原生生态系统的更多信息，请于 4 月 1 日至 4 日在伦敦加入我们的 *[KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)* 大会。*
