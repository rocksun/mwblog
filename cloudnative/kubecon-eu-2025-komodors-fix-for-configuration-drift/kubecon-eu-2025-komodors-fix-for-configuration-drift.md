
<!--
title: KubeCon 欧盟 2025：Komodor 针对配置漂移的修复
cover: https://cdn.thenewstack.io/media/2025/03/4facffee-komodor.png
summary: KubeCon爆款预定！Komodor平台重磅推出新功能，一键修复Kubernetes配置漂移！自动检测偏差，结合AI Agent Claudia进行根本原因分析，更有时间线视图助你快速定位问题。无缝集成GitOps引擎(Argo, Flux)及cert-manager, ExternalDNS等，告别手动更改和IaC部署难题！
-->

KubeCon爆款预定！Komodor平台重磅推出新功能，一键修复Kubernetes配置漂移！自动检测偏差，结合AI Agent Claudia进行根本原因分析，更有时间线视图助你快速定位问题。无缝集成GitOps引擎(Argo, Flux)及cert-manager, ExternalDNS等，告别手动更改和IaC部署难题！

> 译自：[KubeCon EU 2025: Komodor's Fix for Configuration Drift](https://thenewstack.io/kubecon-eu-2025-komodors-fix-for-configuration-drift/)
> 
> 作者：Joab Jackson

下周在伦敦参加 [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 的 Kubernetes 网络管理员应该光临 N330 展位，了解他们如何防止 [Kubernetes 配置漂移](https://thenewstack.io/reddit-no-longer-haunted-by-drifting-kubernetes-configurations/)。

据该公司称，新的 Komodor 服务经过精心调整，可以检测漂移并帮助管理员撤消其可能造成的损害。 它是市场上首批解决此问题的商业产品之一。

该服务会自动标记与预期配置的偏差。 它会监控发布推广，检测资源消耗中的异常情况，同时标记任何重大更改。

它作为该公司同名平台的一项新功能提供。

## Komodor 平台

[Komodor](https://www.youtube.com/watch?v=00OowbUvj5Y) 作为一个 [软件服务](https://thenewstack.io/komodor-workflows-extend-kubernetes-troubleshooting/) 提供，是一个 [Kubernetes](https://thenewstack.io/kubernetes/) 管理平台，旨在简化操作并帮助解决问题，特别是对于大规模集群部署以及多云和混合云部署。

该服务旨在运营和管理大规模 Kubernetes 集群，通过 GUI 监控它们的健康状况和可靠性，用户可以在其中查看和管理所有集成的 Kubernetes 集群及其当前状态。 用户可以使用工作区将其视图范围限定到特定环境、集群、团队和应用程序。

[Itiel Shwartz](https://www.linkedin.com/in/itiel-shwartz-18542853/?originalSubdomain=il) 在接受 The New Stack 采访时表示，为了工作，Komodor 需要在每个 Kubernetes 集群之上安装一个“非常精简的代理”，以捕获集群内部发生的一切，包括管理操作、配置更改以及部署等事件。Itiel Shwartz 是 [Komodor](https://komodor.com/about-us/) 的联合创始人兼 CTO。

![](https://cdn.thenewstack.io/media/2025/03/f4ab8a69-komodor-drift-management-screenshot.png)

用于 Kubernetes 的 Komodor 管理平台。

这种设置还提供了许多额外的好处，例如成本优化和开发人员的自助故障排除。 它提供问题的根本原因分析，有时通过其 AI 代理 [Claudia](https://komodor.com/blog/introducing-klaudiaai-redefining-kubernetes-troubleshooting/) 的帮助。

Komodor 在云原生环境中发展起来，并与 [GitOps](https://thenewstack.io/gitops-git-push-all-the-things/) 引擎（如 [Argo](https://thenewstack.io/how-far-can-you-go-with-argo/) 和 [Flux](https://thenewstack.io/why-flux-isnt-dying-after-weaveworks/)）以及常见的 Kubernetes 运算符和自定义资源（如 [cert-manager](https://thenewstack.io/how-cert-manager-got-to-500-million-downloads-a-month/) 和 [ExternalDNS](https://github.com/kubernetes-sigs/external-dns)）集成。

## 漂移的挑战

越来越多的 Komodor 用户（包括大型金融服务公司和财富 500 强公司的管理员）在其 Day 2 运营中注意到，随着时间的推移，他们的 Kubernetes 部署可能会偏离其原始配置或“期望状态”。

这通常称为配置漂移。

这可能是由多种原因造成的，包括：

- **手动更改，** 或在不更新真实来源（如 Git 存储库）的情况下直接修改集群配置。
- **自动化中的不一致，** 例如自动化脚本中的错误或疏忽。
- **基础设施提供商之间的差异** 是由于底层硬件的差异。
- **配置错误的部署，** 例如不正确的参数。
- **不完整的推广，** 可能是由于服务中断或各种硬件故障。
- **过时的容器镜像或应用程序**是无意中安装或从未更新的。

这些更改可能发生在手动部署中，甚至通过 [基础设施即代码 (IaC) 部署](https://thenewstack.io/introduction-to-infrastructure-as-code/) 发生，这些部署旨在防止此类无意的恶作剧。

Shwartz 说，即使是 GitOps 环境也不能免受漂移的影响。 在大规模、多集群环境中，GitOps 可能会变得棘手，并且多环境部署可能难以完全在 GitOps 框架内表达和管理。

## Komodor 将如何帮助修复配置漂移

Komodor 通过自动检测偏差来管理配置漂移，并提供识别根本原因的工具。
服务的一个关键方面是时间线视图，它显示了集群的行为如何随时间变化，并提供了属性如何变化的并排视图，Shwartz 指出。它可以按事件发生的顺序显示事件序列，这有助于查明异常的原因。

无需花哨的服务即可检测到漂移，可以使用诸如 `Kubectl Diff` 命令甚至基本的日志分析之类的工具，但是它们可能会使管理员在数据的海洋中无助地挣扎。

其他商业漂移检测工具包括 [Quali Torque](https://www.quali.com/torque/) 和 SUSE 的 [StackState](https://www.stackstate.com/)。