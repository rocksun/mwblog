<!--
title: 押注Kubernetes发行版的时代过去了
cover: https://cdn.thenewstack.io/media/2023/12/916b5bb4-clouds-1024x576.jpg
-->

这个时代真正关注的是在同一时间跨多个环境，管理多集群、多发行版的 Kubernetes。

> 译自 [Kubernetes Evolves from ‘Distro’ Bets to Choice at Scale](https://thenewstack.io/kubernetes-evolves-from-distro-bets-to-choice-at-scale/)，作者 Tenry Fu 是 Spectro Cloud 的首席执行官和联合创始人。他在系统软件方面拥有超过 20 年的经验。在 Cisco 收购他之前的公司 CliQr 后，他曾领导 Cisco 的多云管理和私有云解决方案的架构设计。

当我们在三年前启动了我们的生产 Kubernetes 研究项目时，我们的目标是追踪和验证云原生和 Kubernetes 领域发生的一次重大转变。

我们观察到企业 Kubernetes 在许多不同方面变得越来越复杂。组织正在在更多的环境中运行 Kubernetes，每个堆栈中部署的集群和软件元素更多，并在其整个架构中使用更多的 Kubernetes 发行版。

在我们[最新的研究版本](https://www.spectrocloud.com/news/spectro-cloud-report-reveals-top-trends-in-kubernetes-for-2024)中，在芝加哥的 KubeCon 上宣布，我们发现 83% 的组织今天使用了不止一个 Kubernetes 发行版。其中 59% 使用了两到五个；9% 使用了超过 10 个不同的发行版！

这项研究描绘了一个迅速增长和充满活力实验的画面。它还描述了一个新时代，即平台工程团队正在为各种各样的利益相关方提供服务——在同一时间管理跨足多个不同环境的生产集群。

## 你的发行版并不特殊，它只是谜题的一部分

Kubernetes发行版（或称“distros”）有许多不同的变种。它们可能是：

- 与云服务绑定，比如亚马逊使用的 [EKS Distro](https://distro.eks.amazonaws.com/)（EKS-D）。
- 构成开发者使用的平台服务生态系统的一部分，例如 Red Hat OpenShift。
- 针对非常具体的用例 — 边缘是一个很好的例子 — 使用轻量级发行版，如 MicroK8s 或 K3s 或我们[自己的 PXK-E](https://www.spectrocloud.com/news/new-spectro-cloud-palette-edge-platform)，专门为小型设备构建。
- 以安全性为基础构建，减少攻击面，采用 FIPS（联邦信息处理标准）加密和不可变性。
- 优化为简单性，提供一个完整打包的堆栈，从操作系统、Kubernetes 发行版到附加组件和应用程序。
- 拥抱开放性或附带强烈的依赖性或“观点”。

无论是什么驱动力，现实情况是，组织扩展其 Kubernetes 足迹的越多，它们就越需要将分发视为谜题的一部分 — 而不是谜题本身。

许多个别的维护者、社区和供应商付出了辛勤的努力，创新并构建了数以百计的 Kubernetes 发行版。那项工作是有价值的。但没有一个单一的发行版适用于每个用例。

组织需要选择，并且需要工具来同时操作多个分发 — 同样适用于操作系统以及构成完整生产集群的许多软件集成。这个时代真正关乎在规模上管理多集群、多发行版、多环境的 Kubernetes。

## 唯一重要的“观点”是你的观点

多方面的现实是我们构建 Palette 的原因。没有平台应该有很强的观点并将您锁定。我们致力于为客户解决实际的 Kubernetes 问题，不论其 Kubernetes 堆栈的“风格”、供应商和起源如何。我们发现，我们的客户确实需要选择、开放标准和对其现有环境的支持。

在 [KubeCon Europe 2021](https://www.youtube.com/watch?v=WBZVmurXFbQ) 中，GE HealthCare 的 Ben Beeman 提到了我们帮助该公司解决的一个挑战：他谈到了一个“帮助他们处理所有云原生混乱和多层软件”（云原生开源和商业集成）的解决方案，他们需要管理整个堆栈的生命周期，不仅在集成选择方面提供灵活性，而且保持一致性。这根本不是关于发行版的问题。而是关乎更大的图景。

## 你的未来将会是什么样子？

虽然“锁定”和“选择”可能看起来是过度使用的术语，但它们很重要。它们指向一个基本的需求：未来投资无需设计“退出策略”。而这在今天不断变化的市场中尤为重要。

今天 IT 景观的现实是这样的：有望的开源软件项目会失败，就像我们在 [k3OS](https://www.spectrocloud.com/blog/k3os-alternatives-the-best-container-os-for-edge-kubernetes) 中看到的那样。

供应商会转变、倒闭或被收购 —— 最近，D2iQ，以前是 Mesosphere，裁员，其 Konvoy 分发和 DKP 平台的未来成疑。

即使是巨头也不总是安全的。就在不久前，博通完成了对 Broadcom 的收购，并裁员了数千名 VMware 员工，VMware 的合作伙伴报告称尚未完成的销售和续约现在处于悬而未决的状态；Forrester 的分析师建议 VMware 的客户“[做好冲击准备](https://www.forrester.com/blogs/vmware-customers-brace-for-impact/)”。

如果您已经选择了来自这样的供应商的发行版、平台或服务，您如何减轻风险并自信前行呢？

## 答案是：优先考虑开放性和可扩展性

对于那些对之前的选择感到不确定、想要保护现有投资并将其延伸到未来的人，我们在这里提供帮助。

我们最近宣布了[一个面向那些投资于 D2iQ 的 DKP 和 Konvoy Kubernetes 发行版的组织的优惠](https://www.spectrocloud.com/extend-your-d2iq-konvoy-investement)，通过 Palette 从头到尾支持其环境，并使过渡尽可能平稳，包括提供加速培训和极具吸引力的成本激励。

在今年早些时候，[我们宣布了对虚拟机的支持](https://www.spectrocloud.com/news/new-spectro-cloud-palette-unified-platform-to-support-vm-container-and-hybrid-environments)，Palette 中装载了足够的功能以支持生产工作负载。我们自己的发行版（PXK 和 PXK-E）是 100% 针对性强化、策划良好的，同时也是 100% 符合 Cloud Native Computing Foundation（CNCF）的。如果您决定离开 Spectro Cloud，您可以在任何平台上使用它们。

最后但同样重要的是，我们的整个平台是基于成熟的开源技术构建的，例如 [Cluster API](https://cluster-api.sigs.k8s.io/) 及其[可插拔的提供者](https://cluster-api.sigs.k8s.io/reference/providers)用于集群生命周期管理，[KubeVirt](https://kubevirt.io/) 用于虚拟机管理，[Helm](https://helm.sh/) 和 GitOps 用于应用生命周期管理。您将获得一个一站式的企业级平台，但并非被其锁定。

我们一直致力于帮助那些在任何环境、工作负载和堆栈中已经使用任何风格的 Kubernetes 的组织，承认在创新和未来保护现有投资方面需要选择。为什么不让我们来接受挑战呢？
