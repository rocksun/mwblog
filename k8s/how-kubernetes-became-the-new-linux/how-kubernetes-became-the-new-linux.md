
<!--
title: Kubernetes：新一代Linux的崛起
cover: https://cdn.thenewstack.io/media/2025/11/3bc1d191-for-thumbnail-4.png
summary: 文章讨论了 Kubernetes 的发展，从早期定制化构建到如今的标准化。AWS EKS 推出了 Kro 和 Karpenter 两个项目，旨在为整个 Kubernetes 生态系统而非仅 AWS 客户提供解决方案，反映了 AWS 在开源贡献上的哲学转变，即更倾向于将项目捐赠给 Kubernetes SIG，以促进社区协作和生态系统成熟。
-->

文章讨论了 Kubernetes 的发展，从早期定制化构建到如今的标准化。AWS EKS 推出了 Kro 和 Karpenter 两个项目，旨在为整个 Kubernetes 生态系统而非仅 AWS 客户提供解决方案，反映了 AWS 在开源贡献上的哲学转变，即更倾向于将项目捐赠给 Kubernetes SIG，以促进社区协作和生态系统成熟。

> 译自：[How Kubernetes Became the New Linux](https://thenewstack.io/how-kubernetes-became-the-new-linux/)
> 
> 作者：Michelle Gienow

很久很久以前，大型银行会自己构建 Linux 内核，因为那时还没有 [发行版](https://thenewstack.io/best-linux-distros-for-development/)。他们是先驱，知道自己想要 Linux，但必须自己摸索一切。然而，现在这已经成为世界运转的方式。

“每个人都有商业 Linux 发行版。这就是我们都在运行的，” 亚马逊 EKS 的首席项目经理 [Jesse Butler](https://www.linkedin.com/in/jesse-butler/) 在亚特兰大举行的 [KubeCon + CloudNativeCon North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) 上沉思道。“我认为 Kubernetes 现在也到了这个阶段。我们已经从构建自己的定制集群 API 服务器和控制平面，转向寻找标准来大规模构建我们的企业。”

Butler 的观点是：不再有某个细分市场或某类组织在使用 Kubernetes——每个人都在使用它。这种普遍性改变了像 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 这样的公司如何处理开源贡献。

在本期 The New Stack Makers 播客中，Butler 与 TNS 创始人兼出版人 [Alex Williams](https://thenewstack.io/author/alex/) 坐下来，讨论了 AWS EKS 通过 Kubernetes 社区内的不同 SIG 捐赠的两个开源项目：[Kubernetes Resource Orchestrator (Kro)](https://thenewstack.io/the-kro-project-giving-kubernetes-users-what-they-want/) 和 [Karpenter](https://thenewstack.io/migrating-from-cluster-autoscaler-to-karpenter-v0-32/)。但更重要的是，他们讨论了为什么 AWS 将它们作为 Kubernetes 功能来构建，而不是独立的产品——以及这种转变对生态系统意味着什么。

## 当你的胶水代码变成技术债务

Kro 的催化剂源于看到客户在控制器泛滥方面遇到的困难。正如 Butler 所解释的，一旦自定义资源定义 (CRDs) 让将从云基础设施到网络交换机的各种内容表示为 Kubernetes 资源变得容易，组织就开始构建自定义控制器来粘合其他资源。

“我们的一些客户，即使在四五年前，也有 20 到 30 个自定义资源，” Butler 指出。“所以，在你一个更大的组织里，有一个小团队必须只负责这段代码，而这甚至都不是真正的业务逻辑。”

Kro 的构建是为了自动生成 CRD 和一个微控制器来管理它。平台工程师使用 Kro 的 Simple Schema 在 YAML 中定义他们想要的内容，指定组成资源，Kro 会推断依赖关系，创建一个有向无环图并处理编排。这是“控制器即服务”，但无需离开 Kubernetes 生态系统。

## 没有人想解决的节点配置问题

Karpenter 源于一个不同的痛点：集群自动伸缩器跟不上云原生工作负载。“云原生工作负载通常是突发的、动态的，” Butler 说。预测容量需求的传统方法很快就失效了。

Karpenter 的解决方案？即时节点配置，它不仅根据需求进行扩展，还优化成本。

流行起来的不仅仅是自动化——还有 API 设计。“Karpenter API 允许你尽可能简单——‘嘿，给我一个节点’——或者在节点配置方面达到非常精细的细节，” Butler 说。这种优雅性，加上真正的成本节省，推动了快速采用，并最终促使 Karpenter 被捐赠给 Kubernetes SIG Autoscaling。

这两个项目都反映了 AWS 的一种哲学转变：构建适用于整个 Kubernetes 生态系统的解决方案，而不仅仅是 AWS 客户。

“在 Kubernetes 和云原生软件的背景下，这是一个社区，我们都是客户，” Butler 说。“我们不能只为我们的产品构建一些东西，然后说它是 Kubernetes。”

完整的对话深入探讨了 Kro 的 Resource Graph Definitions、Karpenter 从原型到稳定 API 的演变，以及为什么 AWS 越来越多地将项目捐赠给 Kubernetes SIG，而不是创建竞争性的 [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) 项目。对于任何关注 Kubernetes 从一个粗糙的编排器发展成为企业标准的人来说，这都揭示了最成功的开源项目是如何成熟起来的。