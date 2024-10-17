
<!--
title: 云原生网络：Kubernetes 迈入第二个十年
cover: https://cdn.thenewstack.io/media/2024/10/1de4f71f-networking.jpg
-->

随着 Kubernetes 逐渐步入青春期，让我们思考一下它的网络和安全循环系统将如何发展和适应。

> 译自 [Cloud Native Networking as Kubernetes Starts Its Second Decade](https://thenewstack.io/cloud-native-networking-as-kubernetes-starts-its-second-decade/)，作者 Nico Vibert。

Kubernetes 最近[迎来了十周年](https://kubernetes.io/blog/2024/06/06/10-years-of-kubernetes/)。在整个夏季的庆祝活动之后，我作为三个孩子的父亲，有义务提醒 Kubernetes 管理员和运营人员：青春期的孩子并不容易相处。

预计[Kubernetes](https://roadmap.sh/kubernetes) 将进入叛逆期。

它将经历尴尬的成长阶段（随着新的用例迫使 Kubernetes 适应）；它可能会经历身份危机（它是一个平台还是一个 API？）；它将要求更少的监督和更多的独立性（并依赖于 AI 驱动的工具来减少直接的人工监督）。

随着 Kubernetes 进入青春期，让我们考虑其网络和安全循环系统如何发展和适应。随着[KubeCon 北美](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 在盐湖城即将到来，我认为我应该回顾一下其会议日程，并对云原生网络的未来提出一些观察和预测。

## eBPF 将无处不在

[eBPF](https://ebpf.io/) 的势头正在不断增强，这项技术允许您在 Linux（以及即将推出的[Windows](https://thenewstack.io/ebpf-is-coming-for-windows/?utm_source=tldrdevops)）内核中运行自定义程序。除了网络和安全（以及我参与的[Cilium](https://cilium.io/) 和[Tetragon](https://tetragon.io/) 项目）之外，更多用例正在出现，您将在 KubeCon 上了解到：

- 测量[功耗](https://sched.co/1iW8V)：让我们使用 eBPF。
- [引入混沌](https://youtu.be/_5Zabryx0nE?si=KhGFMmeay9LtoJ_-) 来验证我们环境的弹性：让我们使用 eBPF。
- 加速[加密流量](https://sched.co/1i7lP)：让我们使用 eBPF。
- [检测异常](https://sched.co/1i7ms) 在高流量加密流量中：让我们使用 eBPF。

我们是否会进入一个阶段，即不选择 eBPF 作为运行网络程序的平台将成为一种异常？我真诚地希望不会：虽然[eBPF 是一把强大的锤子](https://thenewstack.io/ebpf-security-power-and-shortfalls/)，但我们不应该将每个网络问题都视为钉子。

## 最酷的孩子聚在一起：eBPF 与 OpenTelemetry 相遇

eBPF 能够挂钩每个数据包的能力在一种特定用例中非常强大：网络可见性。

OpenTelemetry 继续成为[最活跃的云原生计算基金会 (CNCF) 项目](https://www.cncf.io/reports/opentelemetry-project-journey-report/) 之一，仅次于 Kubernetes，领先于 Cilium。OpenTelemetry 提供了一个标准的可观察性框架，通过对应用程序进行简单的检测来创建和管理遥测数据。

鉴于网络经常被指责为应用程序性能问题，因此看到[OpenTelemetry Network](https://sched.co/1how7) 等努力令人鼓舞，该项目使用 eBPF 直接从 Linux 内核捕获低级遥测数据。当最好的可观察性工具遇到最有效的 Linux 内核技术时，预计将看到对应用程序健康状况的宝贵见解。

## 回顾过去，展望未来

十年之后，我们可以回顾一下围绕 Kubernetes 网络做出的一些设计决策，并反思它们是否正确，或者是否需要重新考虑。

Ingress API 是 Kubernetes 选择的一个例子，虽然它被广泛采用，但需要重新考虑，Gateway API 是其指定的继任者（稍后将详细介绍）。

服务网格也正在从臃肿的 sidecar 架构演变为[Cilium Service Mesh](https://isovalent.com/blog/post/cilium-service-mesh/) 和 Istio Ambient Mesh 提出的无 sidecar 方法。Istio 社区正在进行深刻的反思：Istio 领导者[现在可以回顾一些做出的决策](https://sched.co/1i7nP) 以及它们如何影响其发展和未来。

也许十周年纪念日是让我们都感到反思的原因：即使是 Kubernetes SIG-Network 小组也在考虑从[容器网络接口插件模型](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) 中迁移。虽然 CNI 一直是 Kubernetes 网络模型的基础，但它实际上早于 Kubernetes。

我们是否应该采用一个新的框架——[Kubernetes 网络接口](https://github.com/kubernetes/enhancements/issues/4410) (KNI) 值得商榷——专门为 Kubernetes 设计？或者我们应该让 CNI 演变到 2.0 版本？我们应该在“[CNI 更新和方向”会议](https://sched.co/1how8) 上了解更多信息。

## Ingress 的落幕时间

[网关 API](https://gateway-api.sigs.k8s.io/) 是我最喜欢的 Kubernetes 生态系统项目之一，不仅因为它解决了其前身 [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) 的一些缺点，还因为它在开发和维护方面的协作性和包容性。

网关 API 为 Kubernetes 集群内部和外部的负载均衡和连接提供了一个新的标准。随着 [近 30 个网关 API 实现](https://gateway-api.sigs.k8s.io/implementations/) 的出现，以及其采用率随着其即将达到 1.2 里程碑而稳步增长，今年的 KubeCon 网关 API 会议将超越入门级会议。它们将提供关于 [网关 API 部署](https://thenewstack.io/multicluster-deployment-strategies-with-the-kubernetes-gateway-api/) 的经验教训。

Ingress 已经运行良好，但现在是时候继续前进：即使是最受欢迎的 [NGINX](https://www.nginx.com?utm_content=inline+mention) Ingress 的维护者也 [期望新的功能和功能只在其网关 API 实现上构建](https://sched.co/1hoxW)。

在 [预览网关 API 未来](https://sched.co/1hoxF) 的 [会议](https://sched.co/1hoxF) 中，预计将看到网关 API 如何最终弥合与剩余 Ingress 功能之间的差距，以便我们能够永远告别。

## AI 用于 Kubernetes 网络

每当我讨论 [AI 和网络](https://www.youtube.com/watch?v=mUbeiDF2B4k) 时，我总是更喜欢将其分解为“用于 AI 工作负载的网络”和“用于改进网络的 AI”。让我们从后者开始。

作为 Cilium 的开发者，Cilium 被认为是事实上的 CNCF 云原生网络层，我尝试使用大型语言模型 (LLM) 来创建网络策略和分析日志。用 [Ollama](https://ollama.com/) 和 ChatGPT 获得的结果至少可以说是不一致的。我期待着看看 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 首席网络工程师 Doug Smith 在他的“[用生成式 AI 自动化 CNI 的疯狂科学家指南](https://sched.co/1i7kI)”教程中是否取得了更大的成功。

更广泛地说，我希望 AI 能够使 Kubernetes 能够做出更明智的网络决策。虽然 Kubernetes 调度程序能够根据工作负载的内存和 CPU 需求和使用情况来放置工作负载，但它通常缺乏网络意识。如果一个带宽密集型工作负载被自动放置在网络需求最小的工作负载旁边会怎样？是否可以根据观察到的网络流量自动生成和实施网络策略？

我认为所有这些用例将在未来几年内成为现实。

## 用于 AI 的 Kubernetes 网络

我们是否应该发展 Kubernetes 网络以适应新兴的 AI 工作负载？

我之前写过关于 [AI 工作负载如何对网络施加巨大压力](https://isovalent.com/blog/post/cilium-the-network-and-security-platform-for-the-cloud-native-ai-era/)。Kubernetes 显然正在成为跨 GPU 集群运行 AI/ML 应用程序的首选平台。但 AI 工作负载不仅需要访问本地 GPU，还需要通过远程直接内存访问 ([RDMA](https://en.wikipedia.org/wiki/Remote_direct_memory_access#:~:text=In%20computing%2C%20remote%20direct%20memory,in%20massively%20parallel%20computer%20clusters.)) 访问远程 GPU。

我们能否使用 Kubernetes 最近的动态资源分配 ([DRA](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)) 功能来请求访问用于网络目的的专用硬件？这就是 [Kubernetes 网络驱动程序](https://github.com/aojea/kubernetes-network-driver) (KND) 项目提出的建议。它可能会被采用，也可能不会被采用，但它勇敢地试图使 Kubernetes 适合其第二个十年。

## 最后的想法

是的，Kubernetes 将经历青少年情绪的变化。但这没关系；它将得到一个社区的支持和指导，这个社区仍然热情好客、支持并决心不断创新，以确保 Kubernetes 成长为一个平衡的成年人。

*要了解更多关于 Kubernetes 和云原生生态系统的信息，请加入我们参加 **KubeCon + CloudNativeCon 北美**，活动将于 11 月 12 日至 15 日在犹他州盐湖城举行。*