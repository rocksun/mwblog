
<!--
title: SUSE 将 StackState 与 Rancher 结合，用于 Kubernetes 可观测性
cover: https://cdn.thenewstack.io/media/2024/09/f557915f-suse.png
-->

此新平台为由 Rancher 管理的所有 Kubernetes 集群的开发团队提供开箱即用的可观察性。

> 译自 [SUSE Combines StackState, Rancher for Kubernetes Observability](https://thenewstack.io/suse-combines-stackstate-rancher-for-kubernetes-observability/)，作者 Chris J Preimesberger。

[SUSE Linux](https://www.suse.com/) 正在快速利用其近期收购获得的员工和知识产权。继 [2024 年 6 月收购](https://www.suse.com/news/suse-acquires-stackstate/) 全栈可观测性平台制造商 [StackState](https://www.stackstate.com/) 之后，SUSE 现在为开发人员铺平了一条快速路径，可以通过新一代可观测性平台识别和解决其容器化云环境中的问题。

截至 9 月 5 日，StackState 现已集成到 SUSE 的 [Rancher Prime 3.1](https://www.suse.com/solutions/enterprise-container-management/#rancher-product)  高级容器管理服务中，旨在为企业 IT 团队阐明和加速云原生可观测性。这家总部位于卢森堡的公司声称，Rancher Prime 现在提供实时的、上下文丰富的洞察力，并简化了故障排除流程，这使得 IT 团队能够专注于创新，而不是管理危机。

IT 系统的全栈可观测性是指 [监控](https://thenewstack.io/whats-the-difference-between-observability-and-monitoring/) 和 [理解](https://thenewstack.io/modern-apps-demand-advanced-observability-and-live-debugging/) 从底层基础设施到应用程序层的整个系统的 [能力](https://thenewstack.io/whats-the-difference-between-observability-and-monitoring/)。它为 IT 团队提供了系统运行状况和性能的完整视图，使他们能够快速识别和解决问题。

这包括监控系统所有组件的指标、日志和跟踪，以及它们之间的关系和依赖关系。通过使用 [全栈可观测性](https://thenewstack.io/whats-the-difference-between-observability-and-monitoring/)，IT 团队可以主动识别和预防问题并提高系统性能，从而带来更好的最终用户体验。

## 不仅仅是“可观测性工具箱”

“SUSE Observability 不仅仅提供了一个可观测性工具箱，它还能在五分钟内为开发人员带来价值，”SUSE 可观测性副总裁 [Andreas Prins](https://www.linkedin.com/in/andreasprins/?originalSubdomain=nl) 告诉 The New Stack。“安装包附带 28 个预先配置的仪表板和 40 多个监控器。这些仪表板相互连接，即使开发人员不是 Kubernetes 专家，也能清楚地了解应用程序、命名空间或集群中发生的情况。

“此外，监控器会在环境中出现问题时立即检测到问题。其优势在于，您不需要丰富的可观测性经验就能发现许多问题。每个监控器还包含一个独特的修复指南，帮助开发人员有效地解决问题。”

该公司表示，Rancher Prime 与 StackState 相结合提供了几个关键的高级优势：

* **强大的跨团队协作**: 该平台通过将所有云原生应用程序集中在一个视图中，促进了团队之间的协作和创新。
* **应用程序性能监控**: 开箱即用的基于 eBPF 的集群外可见性，包括数据库、端点、应用程序和队列等组件。
* **自动数据关联**: Rancher Prime 现在包含一个强大的关联引擎，可以自动连接来自各种来源的指标、事件、日志、跟踪和变更信息，创建一个统一的时间线，简化了对根本原因和长期趋势的识别。
* **高级依赖关系映射**: 自动发现和可视化服务、应用程序和基础设施组件之间的关系，提供 IT 环境的整体视图。此功能有助于查明变更的确切时间和影响，使故障排除更快、更准确。
* **开箱即用的连接仪表板**: 将所有可观测性数据集中到用户友好的开箱即用仪表板中，这些仪表板提供实时和历史洞察力。这消除了对多种工具的需求，并减少了上下文切换，从而显著提高了运营团队的效率。

## UI 扩展识别关键系统健康信号

SUSE 在此版本中为可观测性带来了哪些新元素或创新？“这是两个产品开始集成的第一个版本，”Prins 说。“Rancher 现在有一个 UI 扩展，可以直接在界面中显示关键的健康信号。这使平台工程师能够深入了解其工作负载的健康状况，并在出现问题时快速跳转到 SUSE Observability。

“通过此次发布，平台工程师可以为 Rancher 管理的所有 Kubernetes 集群向开发团队提供开箱即用的可观察性。这将显著提高工作负载的可靠性。此外，随着开发和运营团队变得更加自主，它还将减轻平台团队的故障排除负担，”Prins 说道。

“最后，Rancher 用户将体验到更快的 MTTR（平均修复时间或平均解决/恢复/还原时间），因为所有健康信号都集成到一个解决方案中。”

**具体来说，Kubernetes 在此次发布中扮演着什么角色？**

“Kubernetes 发挥着重要作用，因为 SUSE Observability 与不同的 Kubernetes 风格无关，”Prins 说道。这意味着在 [Google Kubernetes Engine](https://cloud.google.com/?utm_content=inline+mention)、[Amazon Kubernetes Service](https://aws.amazon.com/?utm_content=inline+mention) 或 [Rancher Kubernetes Engine](https://rke.docs.rancher.com/) 上运行的集群“现在都通过 Rancher 进行管理，从而获得完整的可观察性。从可观察性的角度来看，跨集群甚至云提供商运行的工作负载可以在统一视图中捕获。这使得在任何平台上运行任何 Kubernetes 风格的客户都可以通过 Rancher Prime 完全控制其分布式环境，”他说道。

SUSE 表示，由于 IT 环境日益复杂，端到端可观察性对于云原生应用程序非常重要。随着企业采用云和容器技术，传统的监控方法变得不足，需要更新的方法。

该公司表示，Rancher Prime Observability 现已推出，Rancher Prime 客户无需支付额外费用。
