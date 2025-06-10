<!--
title: 当今GitOps工具的7个主要差距
cover: https://cdn.thenewstack.io/media/2025/05/120318c3-gaps-gitops-tools.jpg
summary: 现有 GitOps 工具如 Argo CD 和 Flux CD 在多集群管理、策略部署、SLO 回滚等方面存在差距。未来需应用感知的 GitOps 平台，具备灵活回滚、高级部署策略、简化多集群部署、GitOps 驱动的应用程序晋升、内置审批策略、高级 RBAC 和内置可观测性等能力，实现更智能、安全的 Kubernetes 部署。
-->

现有 GitOps 工具如 Argo CD 和 Flux CD 在多集群管理、策略部署、SLO 回滚等方面存在差距。未来需应用感知的 GitOps 平台，具备灵活回滚、高级部署策略、简化多集群部署、GitOps 驱动的应用程序晋升、内置审批策略、高级 RBAC 和内置可观测性等能力，实现更智能、安全的 Kubernetes 部署。

> 译自：[7 Major Gaps in Today’s GitOps Tools](https://thenewstack.io/7-major-gaps-in-todays-gitops-tools/)
> 
> 作者：Ayaan Bordoloi

GitOps 已经彻底改变了基础设施管理和软件交付流程。凭借 [Git](https://roadmap.sh/git-github) 作为单一事实来源，[GitOps](https://thenewstack.io/4-core-principles-of-gitops/) 用更快、更自动化的方法取代了传统的、手动的和容易出错的部署流程。像 Argo CD 和 Flux CD 这样的工具通过利用 GitOps 作为其在 [Kubernetes](https://thenewstack.io/kubernetes/) 部署中的核心原则，在讨论中占据主导地位。

然而，随着云原生环境的不断发展和部署变得越来越复杂，这些领先的工具在维护安全性、可扩展性和最佳实践方面面临着新的挑战。那么，为了满足云原生组织对更智能、更安全的 Kubernetes 部署的需求，今天的 GitOps 应该是什么样的呢？

## GitOps 工具的兴起：Flux 和 Argo CD

Weaveworks 在 2017 年创造了“GitOps”一词。GitOps 背后的核心思想是使用 Git 作为声明式基础设施和应用程序部署的单一事实来源。

在 GitOps 之前，团队严重依赖自定义脚本（Python、Bash 等）或手动命令（`kubectl apply`）来部署应用程序。这些手动方法带来了一些挑战，例如难以跟踪更改或重复部署，并且缺乏标准化意味着流程通常容易出错。

[GitOps 出现](https://thenewstack.io/extending-cicd-and-gitops-for-better-k8s-app-deployments)是为了应对这些挑战，而 Flux 是第一个采用这种模式的工具。Flux 通过直接从 Git 仓库拉取更改而不是将更改推送到集群，从而简化了部署。然后出现了 Argo CD，它通过提供可视化仪表板和提高可用性来解决 Flux 的局限性，从而实现了更广泛的企业采用。
Flux 和 Argo CD 共同为由 GitOps 驱动的现代、可靠和可扩展的软件交付铺平了道路。

## GitOps 工具中仍然存在的差距

虽然 GitOps 改进了软件交付，但这些 GitOps 工具也引入了它们自己的一系列[挑战](https://thenewstack.io/extending-cicd-and-gitops-for-better-k8s-app-deployments/)。团队开始面临回滚、审批流程和管理过多工具的问题。

以下是当前 GitOps 工具中的一些常见差距。

### 多集群管理障碍

使用这些 GitOps 工具管理多个 Kubernetes 集群通常会引入显著的复杂性。组织必须选择为每个集群部署单独的 Argo CD 实例（这会导致很高的运营开销），或者为所有 Kubernetes 集群使用单个集中的 Argo CD 实例（这可能成为单点故障）。这种架构挑战使得跨多个环境维护可见性、控制和弹性变得困难，并且多集群 GitOps 成为一个真正的挑战。

### 缺少基于策略的部署

像 Flux 和 Argo CD 这样的 GitOps 工具仅充当 Git 到 Kubernetes 的同步工具。虽然它们擅长使集群状态与 Git 中定义的状态保持同步，但它们缺乏对基于策略的部署的本地支持，而这些部署控制着部署应该如何以及何时发生。

例如，组织可能希望强制执行手动审批、应用安全或合规性检查，或者将部署限制在特定的时间窗口内。这些策略对于防止未经验证或无意的更改进入生产环境是必要的。

### 没有原生的基于 SLO 的回滚

当前的 GitOps 工具缺乏对由服务级别目标 (SLO) 驱动的回滚的本地支持。基于 SLO 的回滚允许团队在部署影响关键用户体验指标时快速恢复到之前的稳定版本。如果没有此功能，团队将被迫编写自定义脚本或依赖外部工具，这会增加复杂性和工具蔓延。

### 缺乏 GitOps 晋升能力

在 GitOps 中，“晋升”是指通过在 Git 中进行声明式更改，将应用程序从一个环境移动到另一个环境的过程，例如从开发到测试，然后再到生产。当前的 GitOps 工具缺乏对 GitOps 晋升的本地支持。团队通常必须依赖手动步骤、分支管理或自定义管道来跨环境晋升应用程序，这与 GitOps 自动化和一致性的核心原则背道而驰。

## 对应用程序感知的 GitOps 的需求

为了克服当前 GitOps 工具的局限性，下一代平台必须超越基本的 Git 到 Kubernetes 的同步。它们需要是应用程序感知的、设计上安全的，并且足够灵活以支持[大规模的复杂交付](https://thenewstack.io/the-ultimate-guide-to-software-distribution)。以下是一个现代 GitOps 平台应该提供的：

### 灵活的回滚能力
回滚不仅仅是恢复 Git 提交。GitOps 平台需要支持基于实时指标（如 SLO 违规、错误率或延迟峰值）的智能、自动回滚。这可以最大限度地减少用户影响，而无需依赖手动干预或自定义脚本。

### 支持高级部署策略

像金丝雀发布、蓝绿部署和灰度发布这样的[部署策略](https://devtron.ai/blog/kubernetes-deployment-guide/)不应需要额外的设置或第三方工具。团队应该能够在 GitOps 平台中直接配置和执行高级部署模式，而不是集成像 Flagger 这样的第三方工具。

### 简化多集群部署

处理[跨多个集群的部署](https://devtron.ai/blog/managing-kubernetes-resources-across-multiple-clusters/)不应复杂或脆弱。一个现代的 GitOps 平台应该能够通过一个统一的视图轻松地管理不同集群中的应用程序，同时仍然让团队能够灵活地独立控制每个集群。

### GitOps 驱动的应用程序晋升

将[应用程序从开发环境晋升到测试环境再到生产环境](https://devtron.ai/blog/application-promotion-in-devtron/)不应该是一个手动或复杂的过程。一个好的 GitOps 平台应该允许团队在 Git 中定义清晰的晋升工作流程，以便应用程序自动且安全地通过每个环境，而无需额外的步骤或脚本。

### 内置审批策略

[审批策略](https://devtron.ai/blog/approval-based-deployments-on-kubernetes/)应该从一开始就成为 GitOps 流程的一部分。无论是来自队友的快速签字还是对问题的自动检查，该平台都应确保审批门控内置于 GitOps 工作流程中，以便只有安全、经过审查的更改才能被部署。

### 高级的基于角色的访问控制

[基于角色的访问控制 (RBAC)](https://devtron.ai/blog/sso-and-rbac-a-secure-access-strategy-for-your-kubernetes/)应该直接构建到平台中，而不依赖于 Kubernetes 集群，这可能会增加不必要的复杂性。团队应该能够在平台内跨环境、应用程序和工作流程设置详细的权限，从而确保安全性和合规性，而无需不必要的额外开销。

### 内置可观测性

清晰地了解部署、同步状态、应用程序健康状况和历史更改至关重要。在 2025 年，GitOps 平台应提供[内置可观测性](https://devtron.ai/blog/kubernetes-observability/)，使团队能够轻松地排除故障、跟踪回滚并从统一的仪表板监控整个部署过程。

## 现代化应用程序生命周期管理

![Devtron dashboard](https://cdn.thenewstack.io/media/2025/05/ed4367e5-devtron-dashboard.png)

*来源: Devtron.*

[Devtron](https://devtron.ai/product/deployment-with-gitops) 旨在简化现代团队的 GitOps。它支持灵活的回滚、高级部署策略和轻松的多集群管理。凭借内置的审批门控、细粒度的 RBAC 和强大的可观测性功能，Devtron 在整个部署过程中保持安全性、合规性和透明度。其统一的平台使团队能够完全控制，从而使他们能够更智能、更安全地进行部署，从而在不影响质量的前提下加速软件交付。