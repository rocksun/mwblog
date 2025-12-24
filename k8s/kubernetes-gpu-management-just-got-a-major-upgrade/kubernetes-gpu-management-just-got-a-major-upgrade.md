<!--
title: Kubernetes GPU 管理重磅升级
cover: https://cdn.thenewstack.io/media/2025/12/b6de86d4-for-thumbnail-7.png
summary: Kubernetes通过DRA解决GPU请求痛点，并通过新的工作负载抽象实现AI智能调度。这些基础功能将塑造未来十年Kubernetes上AI工作负载的运行方式。
-->

Kubernetes通过DRA解决GPU请求痛点，并通过新的工作负载抽象实现AI智能调度。这些基础功能将塑造未来十年Kubernetes上AI工作负载的运行方式。

> 译自：[Kubernetes GPU Management Just Got a Major Upgrade](https://thenewstack.io/kubernetes-gpu-management-just-got-a-major-upgrade/)
> 
> 作者：Michelle Gienow

“作为一名底层系统工程师，如果你工作做得好，没人知道你的存在——但只要你工作做得不对，所有人都会知道你的存在。”

Nvidia 杰出工程师 [Kevin Klues](https://www.linkedin.com/in/klueska) 的这一观察，突显了为什么 Kubernetes 开源社区一直在悄然构建基础性功能和抽象，这些将塑造未来十年组织运行 AI 工作负载的方式。

视频

在亚特兰大举行的 [KubeCon + CloudNativeCon North America 2025](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) 大会上，New Stack 创始人兼出版商 [Alex Williams](https://thenewstack.io/author/alex/) 主持了一场小组讨论，与 Klues 和 Amazon Web Services 首席产品经理 [Jesse Butler](https://thenewstack.io/how-kubernetes-became-the-new-linux/) 探讨了两个值得更多关注的进展：动态资源分配（DRA）以及一项可能改变多节点 AI 部署的即将推出的工作负载抽象。

## DRA：像存储一样工作的 GPU

[动态资源分配（DRA）](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) 已在 [Kubernetes 1.34](https://thenewstack.io/kubernetes-v1-34-introduces-benefits-but-also-new-blind-spots/) 中普遍可用，解决了长期以来在 Kubernetes 中请求 GPU 资源时遇到的困扰。

Klues 说：“以前请求访问资源时唯一的调节器就是简单的计数。你可以说‘我想要两个 GPU’，但你不能说要什么类型的 GPU，也不能说一旦获得 GPU 后你希望它如何配置。”

Butler 称 DRA 是“我见过最优雅的事物之一”，它借鉴了持久卷和持久卷声明的概念模型——这些是存储团队多年来一直使用的熟悉抽象。不同之处在于，DRA 适用于任何专用硬件，而不仅仅是存储，这意味着第三方供应商现在可以引入自己的设备驱动程序，并以标准化方式使硬件可供 Kubernetes 用户使用。

## 用于智能调度的全新工作负载抽象

但仅靠 DRA 不足以应对复杂的 AI 部署。有时，你需要多个节点上的多个 Pod 同时上线，或者相反，一个都不要上线。这正是 Kubernetes 一项新抽象（简称“工作负载抽象”）旨在解决的问题。

Klues 说：“你希望能够表达这样的意思：我可以让这些 Pod 的某个子集启动，但如果我不能得到所有的 Pod，那么我一个都不想要启动。而至少在今天，你在 Kubernetes 世界里还无法真正表达这一点。”

一个基本实现计划在 12 月 17 日的 [Kubernetes 1.35](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/) 版本中发布，不过 Klues 强调前方仍有大量工作。这项抽象将允许用户定义具有调度约束和拓扑要求的 Pod 分组，有点像增强版的节点选择器。

Klues 说：“这将塑造未来十年 Kubernetes 的运作方式”，他强调，这些功能正在形成的 [设备管理工作组](https://github.com/kubernetes-sigs/wg-device-management) 强烈欢迎社区参与。

如需完整对话——包括关于代理式 AI 架构、小型语言模型以及在大型语言模型时代 Unix 哲学为何依然重要的讨论——请查看完整采访。