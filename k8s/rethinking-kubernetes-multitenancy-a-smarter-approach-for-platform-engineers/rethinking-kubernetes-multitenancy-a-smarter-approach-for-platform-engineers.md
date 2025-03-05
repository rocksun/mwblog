
<!--
title: 重新思考Kubernetes多租户：一种更智能的平台工程师方法
cover: https://cdn.thenewstack.io/media/2025/03/424672ee-thisisengineering-uyfohhitxho-unsplash-1-scaled.jpg
-->

> 译自：[Rethinking Kubernetes Multitenancy: A Smarter Approach for Platform Engineers](https://thenewstack.io/rethinking-kubernetes-multitenancy-a-smarter-approach-for-platform-engineers/)
> 
> 作者：Lukas Gentele

通过虚拟化 Kubernetes，平台工程师可以简化操作并减少基础设施蔓延。

平台团队致力于为工程师创建“黄金路径”，并通过有效的内部开发者平台 (IDP) 促进整个组织的通用标准。然而，这种努力常常与加速创新相冲突。平台构建者必须考虑如何在不牺牲开发者推动边界和交付真正创新解决方案所需的自主权的情况下，实现一致性。

在 Kubernetes 原生开发的背景下，通用标准和开发者自由之间的紧张关系通常归结为平台团队在确定其团队的工作负载如何在 Kubernetes 上运行时所做的架构决策。平台工程师应考虑采用具有虚拟集群的多租户 Kubernetes 架构，以在强制执行标准的同时保留自主权。为此，他们必须超越典型的解决方案，找到平台“构建块”，从而无需在定制和标准化之间做出选择。

## 为什么平台工程目标在 Kubernetes 上无法实现

目前，组织采用两种方法来协调一致性和合规性与自主性和创新。第一种是单租户架构，其中管理员创建许多集群——每个团队、每个客户等一个集群。通常，公司有数百甚至数千个集群。每个集群都会增加大量成本并需要持续维护；如果没有在其上运行的几个工具和服务，Kubernetes 集群本身就无法运行。在许多情况下，此平台堆栈比它运行的工作负载更大且成本更高！更糟糕的是，这些集群通常即使在没有人使用它们时也会运行，例如在周末。

团队选择此单租户路线是为了通过将每个工作负载分离到其专用集群中来保持[开发者自主权并提高安全性](https://thenewstack.io/software-supply-chain-security-tearing-down-the-silos/)。具有讽刺意味的是，这非常昂贵，并且无法提供所需的自主权。中央 IT 团队通常保留对每个集群中平台堆栈的完全控制权。因此，尽管移交了整个集群，但接收它的开发者或团队可能不会是管理员。RBAC 仍然会限制他们，并且只能访问特定的命名空间。

另一种常见方法是采用 Kubernetes 多租户，它可以降低成本并简化[具有共享集群的运营](https://thenewstack.io/how-to-cut-through-a-thicket-of-kubernetes-clusters/)。多租户很有吸引力，因为它消除了昂贵的平台堆栈的重复，从而使保持自主性非常具有挑战性。通常，多租户场景中的管理员会授予开发者访问 Kubernetes 集群中各个命名空间的权限。由于他们不再拥有集群并且被限制在命名空间中，因此团队在自助服务和生产力方面面临着严重的障碍。例如，如果一个租户是一个内部预生产团队，他们想要安装 ArgoCD 以测试其新的交付工作流程，他们无法这样做，因为 ArgoCD 要求他们安装 CRD。他们必须返回集群管理员并要求他们安装 ArgoCD，但是如果已经运行了不同版本的 ArgoCD 怎么办？

[平台团队需要](https://thenewstack.io/why-successful-platform-engineering-teams-need-a-product-manager/)在单租户独立集群和命名空间隔离之间做出妥协。2021 年，我们研究了这个问题并设计了一个解决方案：虚拟化 Kubernetes，为平台构建者提供了一个强大的“构建块”来构建自定义 IDP。

## 通过虚拟集群实现平台工程的成功

当我们寻求多租户解决方案时，我们的第一个突破是意识到 Kubernetes 几乎就像一台 Linux 主机。Kubernetes 具有用户、权限、RBAC 和命名空间，就像 Linux 主机具有用户、文件夹和权限一样——但是如果没有虚拟化，共享 Linux 主机是很困难的。如果我们将虚拟化添加到 Kubernetes 中会怎样？除了节点和容器之外，如果我们虚拟化控制平面本身会怎样？这时我们发明了虚拟集群，它本质上是将控制平面放入容器内，放入另一个集群的命名空间内，IT 团队可以将这个虚拟集群交给租户。这意味着租户的 KubeContext 指向 [在容器中运行](https://thenewstack.io/run-opentelemetry-on-docker/)的 API 服务器，模拟一个真实的集群。

租户拥有完全的自主权，并且可以充当集群管理员，而不会对组织的一致性和标准产生负面影响。这是因为平台堆栈组件（Cert Manager、Istio、OpenPolicy Agent 等）在底层“宿主”集群中运行，而虚拟集群在租户命名空间内启动。平台团队可以提升租户的权限并解锁自助服务，而无需实际提升他们在宿主集群中的权限。

因此，虚拟集群多租户在平台工程的成功中起着关键作用，因为它使得运行多租户隔离集群成为可能。这结合了标准化和安全性与最大程度的自主性；团队拥有根据其需求量身定制的隔离环境，但仍然遵守组织策略。总体而言，组织需要的传统集群更少，从而降低了复杂性并减轻了管理负担。[平台团队](https://thenewstack.io/a-platform-team-product-manager-determines-devops-success/)只需在少量宿主集群上配置和管理 Cert Manager 或 Ingress Controller 等工具，然后就可以在他们的虚拟集群群中共享这些工具。

与此同时，工程师也获得了充分的自主权和安全实验的空间。他们拥有虚拟集群内的完全访问权限，但除了平台团队提供的共享工具之外，没有其他访问权限。这是难以捉摸的中间地带：轻量级且经济高效，如命名空间，但具有开发人员的自由和独立集群的严格隔离。安全性不再是一个问题，因为即使一个租户启动了一个错误的控制器或引入了另一个漏洞，它也只会影响虚拟集群。相比之下，传统上，这样的错误可能会导致真正的 Kubernetes 集群崩溃。

## 在提升一致性的同时，赋能开发者

虚拟集群是平台工程计划中必要转变的一个例子。为了成功[提高开发人员的生产力](https://thenewstack.io/how-to-boost-developer-productivity-with-generative-ai/)并在系统变得越来越复杂时加强一致性，平台构建者必须发挥创造力，并跳出典型的解决方案。他们不应该寻找全面的 IDP，而应该寻找灵活的“构建块”，以解决他们的团队今天面临的实际、紧迫的问题。这种方法最终会提高生产力，并带来更具创新性、更安全的应用程序。
