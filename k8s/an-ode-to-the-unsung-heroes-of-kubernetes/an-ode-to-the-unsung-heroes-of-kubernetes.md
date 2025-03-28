
<!--
title: Kubernetes无名英雄颂
cover: https://cdn.thenewstack.io/media/2025/03/d1489308-heart.jpg
summary: 庆祝 Kubernetes 十周年！揭秘其背后无名英雄的贡献，如优化控制平面、`Kube-proxy nftables`、节点授权等。关注性能、安全，解决 `IP exhaustion`，提升 `Pod` 启动可靠性。拥抱 `GenAI`，通过 `Go workspace` 改善开发体验，共建云原生未来！
-->

庆祝 Kubernetes 十周年！揭秘其背后无名英雄的贡献，如优化控制平面、`Kube-proxy nftables`、节点授权等。关注性能、安全，解决 `IP exhaustion`，提升 `Pod` 启动可靠性。拥抱 `GenAI`，通过 `Go workspace` 改善开发体验，共建云原生未来！

> 译自：[An Ode to the Unsung Heroes of Kubernetes](https://thenewstack.io/an-ode-to-the-unsung-heroes-of-kubernetes/)
> 
> 作者：Antonio Ojea; Federico Bongiovanni

去年，我们庆祝了 [Kubernetes 十周年](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/)。作为现代容器编排和云原生计算的基础，[Kubernetes 已经从最初的小项目成长](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)为一个大型的、无处不在的项目，并得到了一个蓬勃发展的全球社区的支持。

在经历了 33 个版本之后，随着 KubeCon 的临近，现在不仅是庆祝该项目显著增长和新功能的绝佳时机，也是表彰那些不总是为人所见，但却确保其持续健康发展的大量贡献者的集体努力的绝佳时机。本文旨在阐明并感谢 [Kubernetes 社区](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/)的辛勤工作。

该项目的起源故事突出了共享知识和经验的力量。最初的贡献不仅仅是代码，还包括宝贵的操作专业知识，这些知识重新定义了现代基础设施。然后，社区扩大了这个基础，将 Kubernetes 推向了新的前沿，发展到包括 GenAI 等尖端技术，并因此创建了一个庞大且不断增长的生态系统。

Kubernetes 的贡献者们明白，真正的力量在于一个模糊了公司界限的社区，在这个社区里，任何人都可以贡献，每个人都可以受益。这种协作环境促进了创新、持续改进和集体责任，确保了项目在不影响质量或产生技术债务的情况下，具有可持续性，并能适应新技术和新挑战。

可以将 Kubernetes 想象成一台高性能引擎，无数的贡献者都在不断地改进它。为了保持这台引擎的平稳运行，由来自不同公司和各个组织的个人贡献者和工程师组成的社区，一直在引擎盖下不断微调其核心组件。

例如，我们共同致力于优化控制平面的速度和效率。这意味着要实现以下功能：

- **Consistent read from cache（从缓存中一致读取）**：通过允许控制平面从缓存中一致地检索信息，我们减少了核心系统的负载，并实现了更快的响应，这在控制平面处理大量请求的大型集群中尤其重要。
- **Kube-apiserver API streaming（Kube-apiserver API 流式传输）**：通过流式传输数据而不是一次发送大型有效负载，这种增强功能实现了控制平面内更快、更高效的通信，从而改善了信息流和整体响应能力。

这种对性能的专注也延伸到了数据平面，即连接应用程序不同部分的网络结构。在这里，诸如以下的改进：

- **Kube-proxy nftables**：Linux 内核中的 nftables 框架，可在 Kubernetes 中提供更高效、更灵活的网络流量管理。这可以提高网络性能并减少资源消耗。
- **Traffic distribution for services（服务流量分配）**：此增强功能允许用户指定流量如何路由到 Kubernetes 中不同服务的首选项。这可以更精细地控制流量，从而提高网络可靠性、效率和性能。

当然，安全性至关重要，社区通过以下增强功能加强了 Kubernetes 的防御能力：

- **Node authorization（节点授权）**：此功能可以更精细地控制可以在集群中每个节点上执行的操作。通过在节点级别限制权限，它可以增强安全性并保护您的集群。

除了原始性能和安全性之外，我们还致力于消除日常使用中的障碍，解决用户的痛点，例如：

- **IP exhaustion with multiple service CIDR（具有多个服务 CIDR 的 IP 耗尽）**：此增强功能允许 Kubernetes 为服务分配多个 CIDR 块，从而增加可用的 IP 地址空间并防止耗尽，这对于大型部署至关重要。这解决了在 Kubernetes 上运行大规模应用程序的用户面临的常见挑战。
- **Improving pod start-up reliability with crash loop backoff tuning（通过崩溃循环退避调整提高 Pod 启动可靠性）**：这有助于防止 Pod 卡在崩溃循环中，从而加快开发生命周期，确保更顺畅、更可预测的应用程序部署和更新。

随着技术的发展，Kubernetes 也必须发展。我们正在积极合作开发一些功能，使您能够适应新的需求，例如：

- **在运行时启用资源更新：** 这允许您动态调整容器化应用程序的资源，从而提高性能和效率。
- **提高 NUMA 和拓扑管理器感知能力：** 这有助于提高对底层硬件拓扑结构敏感的应用程序的性能。
- **通过协调的领导者选举来增强升级体验：** 这使得 Kubernetes 的升级更加可靠和减少中断，从而最大限度地减少应用程序的停机时间。

这不仅仅是优化运行时环境；社区还致力于改善开发人员体验并确保项目的长期健康。这包括以下方面的进展：

- **Go 工作区：** 此功能改进了 Kubernetes 中 Go 代码的组织和管理，从而更容易管理依赖项并确保代码质量。这有助于项目的长期可维护性和稳定性。

这些协作努力确保 Kubernetes 保持强大和适应性，能够满足行业不断变化的需求。

**加入社区**

如果您对开源和 Kubernetes 充满热情，并希望有所作为，请考虑加入社区。有很多方法可以做出贡献，无论是编写代码、审查拉取请求，还是仅仅帮助回答论坛和邮件列表中的问题。您的贡献可以帮助塑造 Kubernetes 的未来，并使其对每个人都更好。

要了解更多关于 Kubernetes 和云原生生态系统的信息，请加入我们在 4 月 1 日至 4 日在伦敦举行的 [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)。

Benjamin Elder 也为本文做出了贡献。