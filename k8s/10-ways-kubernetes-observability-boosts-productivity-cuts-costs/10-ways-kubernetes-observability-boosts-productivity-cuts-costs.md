<!--
title: Kubernetes可观测性提升生产力降低成本的10种方法
cover: https://cdn.thenewstack.io/media/2024/03/b20dd601-vision123-1024x576.jpg
-->

工程团队使用集成了Kubernetes管理与编排层的云原生可观测性平台，有助于更快达成业务目标。

> 译自 [10 Ways Kubernetes Observability Boosts Productivity, Cuts Costs](https://thenewstack.io/10-ways-kubernetes-observability-boosts-productivity-cuts-costs/)，作者 Eric Schabell 是 Chronosphere 的布道总监。他在开发社区中被认为是演讲者、讲师、作家和棒球专家。

云原生很快成为数字化转型的首选路径，但它并非没有增加复杂性和成本。不同于基于虚拟机(VM)的基础设施，采用 Kubernetes 的[云原生环境](https://thenewstack.io/cloud-native/)总是在变化；它们包含了数千个[容器](https://thenewstack.io/containers/)和[微服务](https://thenewstack.io/microservices/)，产生更多数据，而且相互依赖性更强。

为了解决这些挑战，工程团队可以使用集成了 Kubernetes 管理和编排层的云原生可观测性平台，以更快实现数字化业务目标、保护收益和支持创新。

如果您的组织希望运行云原生可观测性和 Kubernetes 管理解决方案，以下是在 [Kubernetes 可观测性](https://chronosphere.io/learn/what-is-kubernetes-and-how-does-it-benefit-observability/)方面需要遵循的10条最佳实践。

## Kubernetes 可观测性的 10 个实践步骤

遵循这10个简单步骤，可以帮助您掌控或重新掌控可观测性数据:

### 1. 明确目标

首先，确立数字化转型计划愿景，并设定实现目标。例如，如果是一款允许混合工作模式与客户联系的应用程序，[服务级别目标(SLOs)](https://chronosphere.io/learn/know-the-sre-fundamentals-differences-between-sli-vs-slo-vs-sla/)应该是什么？

反过来，目标平均修复时间(MTTR)是多少，或者组织可以承受多长时间的停机时间？应该允许什么程度的资源峰值，以及可以投入多少资金都应该从一开始就确定。由此向后推，您就可以确定需要什么样的平均检测时间(MTTD)才能实现目标。  

### 2. 选择最佳可观测性解决方案

与每个数字化转型项目一样，您的团队需要寻求尽可能最佳的解决方案或解决方案组合，这将取决于您的用例和目标。监控 Kubernetes 或实现[云原生](https://thenewstack.io/a-ctos-guide-to-navigating-the-cloud-native-ecosystem/)并没有一种固定方法，它取决于您的人员、组织、业务目标和现有技术堆栈。

在为组织选择最佳可观测性解决方案时，需要考虑以下类型工具:

- **开源指标工具**: Prometheus 是 Kubernetes 指标的事实标准。由于它具有可扩展性限制，人们通常会选择添加时序数据库，如 Thanos、Cortex 或 M3DB 用于长期存储。
- **开源日志工具**: 在云原生环境中，许多人会查看日志聚合工具，如 Cloud Native Computing Foundation (CNCF) 项目 Fluentd，它充当数据收集器，可将数据发送到多种不同的后端。
- **开源追踪工具**: Jaeger 开始时是最受欢迎的开源追踪工具之一。后来被 OpenTelemetry 所取代，OpenTelemetry 目前是 CNCF 中活跃程度仅次于 Kubernetes 的项目，是追踪数据的事实标准。
- **开源成本优化工具**: 这些工具报告有关集群和资源的成本信息，以便您采取行动。这一类别中最受欢迎的是 Kubecost 和 OpenCost。
- **非开源工具**: 许多供应商提供可观测性工具。这里最重要的是要评估它们在可观测性数据编码、传输、引入和查询方面对开放标准的使用。寻找这些可观测性供应商与 CNCF 项目的集成，如 Chronosphere 致力于遵守社区标准。

一旦确定所需的解决方案，就该决定如何利用它们了。对于任何依赖 Kubernetes 的云原生生态系统收集器而言，开源都是一个关键特性。

以下是部署和访问可观测性的一些关键方式:

- **开源自主管理(又称 DIY)**: 这是大多数组织的切入点，因为他们希望控制自己的数据和可观测性创新，而不受供应商时间线和锁定的影响。如果环境无需快速或大规模扩展，内部可观测性是一个不错的选择。但是，您必须拥有运行、托管、操作、托管和监控解决方案的资源、经验和规模，且该可用区域与运行应用程序生产环境的区域不同。
- **专有 SaaS 解决方案**: DevOps 和站点可靠性工程(SRE)组织的健康和发展往往是选择 SaaS 的一个主要因素。如果您在非容器化环境中有现有的软件即服务(SaaS)可观测性供应商，您可能可以将其扩展到监控 Kubernetes，但您需要注意一些陷阱:由于定价是为面向 VM 的环境构建的，许可成本高昂;仪表板速度缓慢;由于数据量太大和缺乏对 Kubernetes 集群中关键指标的可见性，导致警报延迟。
- **开源兼容 SaaS 解决方案**: 这条"黄金路径"通过提供对整个堆栈的全面、可扩展的可见性，以及数据控制和无供应商锁定的所有优势，简化了实施过程。完全与 Prometheus 和 OpenTelemetry 兼容的解决方案可以让您获得两全其美的好处。因此，您的组织不仅可以获得开源解决方案带来的回报，还可以获得社区、生态系统和教程的支持。开源服务还提供了回到自托管的退出通道，以应对目标发生变化的情况。

选择解决方案的最后一步是选择云提供商工具。对于单一云环境，使用云提供商的分析和监控工具是明智之举，因为您可以获得价格优势，并借助与现有云基础设施的深度集成实现可见性。无论您使用单云还是多云，您都要对客户体验负责。

### 3. 代码插桩

为了充分利用所使用的工具，并[实现分布式追踪](https://chronosphere.io/learn/what-is-distributed-tracing/)(参见第7点)，您需要检测代码。在实践中，检测代码意味着收集数据，然后将其发送到任何所需位置——不会再像应用程序性能监控(APM)或基础设施监控提供商那样存在供应商锁定。许多解决方案可在没有太多工作量的情况下开箱即用，但通过检测代码，您可以获得最佳可用数据，从而采取最佳行动方案。

在开源世界中，Prometheus 是了解 Kubernetes 集群健康状况的[标准](https://chronosphere.io/resource/inside-prometheus-documentary/)。但是，要谨慎行事，因为您实际上可能不需要所有发出的数据。如果数据对您和组织没有用处，就会成为负担。针对特定用例和业务需求进行调整，始终比一刀切的监控体验更好。如果您正在使用 Prometheus 仪表板学习，请注意这一点。

### 4. 使用仪表板收集和可视化可观测性数据

您的工程师将负责创建可交付数据可视化的仪表板。这样，您就可以迅速掌握系统中正在发生的情况。许多解决方案都包含仪表板系统。例如，Chronosphere 通过 [Query Accelerator](https://chronosphere.io/learn/experience-faster-dashboards-with-query-accelerator/) 技术帮助您体验更快的仪表板。在整个系统中，它运行迅速、高效，无需手动优化。

这种方法更简单，因为您的工程师无需成为查询语言([如 PromQL](https://chronosphere.io/learn/workshop-introduction-to-the-prometheus-query-language/))、环境架构和规模、可观测性解决方案的底层数据模型或测试中的查询在生产环境中的性能等方面的深度专家。

### 5. 跟踪资源利用率

资源利用率的显著变化可能意味着好消息或坏消息——您的客户群体突然激增或出现了故障。无论哪种情况，要用现有的 APM 或基础设施监控工具来了解正在使用多少资源、使用哪种资源、供哪个应用程序使用以及是否过度使用资源，这都是一个挑战。

来自 Chronosphere 的[可观测性数据优化周期](https://chronosphere.io/learn/introducing-the-observability-data-optimization-cycle/)可以通过分析、完善和操作等过程，帮助您的组织更好地了解并采取行动来控制可观测性数据的成本，从而克服这些挑战。

### 6. 日志记录和日志聚合

在云原生世界中，日志记录很重要，因为它帮助团队捕获、聚合和理解系统事件。在云原生架构中，事件数量增加，但独立系统中不相关的日志数量也会增加。这使得很难找到所需的数据并对问题进行故障排查。虽然指标是诊断问题症状的重要工具，但您需要使用跟踪来定位问题，而[日志最适合](https://chronosphere.io/learn/chronosphere-crowdstrike-announcement/)发现问题的根本原因。

要在 Kubernetes 环境中控制日志，您需要能够聚合和过滤数据，以减少浪费，节省成本，并及时轻松地找到所需数据。

### 7. 分布式跟踪

如果没有正确检测代码(参见第2点)，就无法[支持分布式跟踪](https://chronosphere.io/learn/distributed-tracing-is-failing-how-can-we-save-it/)。然而，分布式跟踪可让您查看请求在整个系统中执行的情况。这是您确定某个单一功能运行时间过长的方式，以便在影响客户体验之前深入了解原因。

### 8. 警报和通知 

完成1-7步后，最佳实践是设置警报和通知，发送给您自己或团队。这样，一旦出现问题，就能及时进行分类和修复。

### 9. 遵循最佳实践和更新

这一步是常识性的。新的更新几乎每天都在出现，要实现未来防护并不容易。请跟上解决方案补丁和[可观测性最佳实践](https://chronosphere.io/learn/4-key-observability-best-practices-to-know/)的步伐。在可能的情况下添加自动化，以消除费时且容易出错的手动流程。

### 10. 控制成本

最佳可观测性平台将帮助您[控制云成本](https://chronosphere.io/learn/reducing-costs-with-chronospheres-control-plane/)和可观测性支出。选择诸如 Chronosphere 及其[控制平面](https://chronosphere.io/platform/control-plane/)的解决方案，可为您提供沿着可观测性渠道的不同工具，使组织能够:

- 了解所拥有的数据
- 分析哪些是有用的，哪些是浪费  
- 了解是否有人对某个指标发出警报
- 查看哪个标签导致了最大的基数 - 成本最高，但使用最少

这种透明度可让有价值的才华横溢的工程师专注于对业务更有影响力的项目。在实施成本控制后，您就可以开始微调数据，了解其有用性；根据可观测性支出为团队设置配额，并跨独立微服务运行的团队进行成本核算趋势分析。

## 云原生入门  

对于希望利用数字化转型力量的企业而言，云原生环境是必不可少的，但必须配备可以互相协作的正确工具并采用最佳实践。Chronosphere 及其合作伙伴从头构建，旨在抽象云原生环境的复杂性，优化数据并减少工程师的工作压力。
