
<!--
title: Cilium可以在Kubernetes之外作为控制平面吗？
cover: https://cdn.thenewstack.io/media/2024/07/09b8afdd-can-cilium-be-a-control-plane-beyond-kubernetes-copy-2.png
-->

Cilium 联合创始人 Thomas Graf 讨论了基于 eBPF 的工具如何融入更广泛的网络环境。

> 译自 [Can Cilium Be a Control Plane Beyond Kubernetes?](https://thenewstack.io/can-cilium-be-a-control-plane-beyond-kubernetes/)，作者 Alex Williams。

西雅图 - [Cilium](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/) 的创建者之一 [Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547/) 认为，随着容器在 AI API 中的广泛采用以及微分段的新方法，云原生安全市场正在发生变化。

Cilium 是 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) 的毕业项目，基于 [eBPF](https://thenewstack.io/what-is-ebpf/)（扩展的伯克利数据包过滤器）。Graf 还帮助在 [VMware](https://tanzu.vmware.com?utm_content=inline+mention) 收购的 Nicira 开发了 [NSX](https://thenewstack.io/global-speech-networks-embraces-software-defined-networking-vmware-nsx/) 和 Open vSwitch。NSX 的核心是软件定义网络，它将硬件交换机转变为软件。

Cilium 非常受欢迎，现在的问题是：随着 AI 的日益普及，它将取得多少成功？它是一个未来主义的解决方案，还是一把寻找钉子的锤子？

我在西雅图的 [CloudNative SecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/) 与 [Isovalent](https://thenewstack.io/ciscos-strategic-move-in-the-isovalent-acquisition-ebpf/) 的 CTO 和联合创始人 [Graf](https://www.linkedin.com/in/thomas-graf-73104547/) 坐下来，讨论了 Cilium 如何融入更广泛的网络环境。我们探讨了围绕 AI 和外部因素的旋风般的问题，例如如何管理容器的主流采用、无处不在的 API 和数据中的 AI 带来的微分段的更深层次的复杂性。

今年 1 月，[Torsten Volk](https://thenewstack.io/author/torsten-volk/) 在 [The New Stack](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/) 上撰文称，Cillium 将 eBPF 扩展到传输层和应用层，提供了对网络和安全更细粒度和灵活的控制，这在云原生环境中尤其有利。

2022 年，[Isovalent 开源了 Tetragon](https://thenewstack.io/isovalent-open-sources-tetragon-ebpf-based-observability-platform/)，[一个 Kubernetes 原生工具](https://tetragon.io/)，它利用 [eBPF 进行深度可观察性](https://thenewstack.io/groundcover-simplifying-observability-with-ebpf/?nab=1)，同时对性能的影响最小。Tetragon 跟踪各种活动，包括进程执行、权限提升和网络活动。它使用 eBPF 强制执行的内核运行时策略，提供了强大的安全姿态，可以抵御未经授权的操作和 [检查时攻击](https://cwe.mitre.org/data/definitions/367.html) 竞态条件攻击。

## Kubernetes 网络和 AI

Isovalent 现在与使用 [Kubernetes](https://thenewstack.io/kubernetes/) 集群构建 [大型语言模型](https://thenewstack.io/llm/) 的公司合作，这些集群具有复杂的网络需求，主要是因为 AI 工作负载的数据量非常大，Graf 说。

他说，很难想象构建语言模型需要多少数据；当高薪的研究工程师构建这些语言模型时，这些模型必须保密。同时，需要不断地提取数据来构建模型。

然而，与此同时，保护始终容易受到横向攻击的工作负载的复杂性正在增加。生成式 AI 可能很强大，但如果它污染了数据湖会发生什么？

在这种背景下，需要更好的可观察性和控制平面，这些平面可以上下文地管理洪流。

当我们谈论 AI 原生时，我们指的是下一代机器学习或基于自适应学习的策略管理。你不再希望手动创建所有策略。你需要自动化来缓解威胁。如果出现 CVE，你需要缓解它。你识别出威胁，你需要通过自动化自动拒绝它。因此，AI 只是更好的自动化。

但是 Cilium 在下一代自动化中将扮演什么角色？

Graf 说，Cilium 将成为一个通用的数据平面。Cilium 在云原生世界中的地位已经确立，Cilium 将适用于 Kubernetes 之外，成为更广泛行业的分布式数据平面。思科将能够在 [DPU](https://blogs.nvidia.com/blog/whats-a-dpu-data-processing-unit/) 和 [智能网卡](https://thenewstack.io/where-service-mesh-and-smartnics-meet/) 上的交换机上运行。并且随着 [博通最近收购 VMware](https://thenewstack.io/vmwares-private-cloud-solution-emerges-under-broadcom/)，人们对替换 NSX 的兴趣很大。他认为 Cilium 是一项基础技术，可以推动 NSX 的替代产品的开发。
## eBPF 是答案吗？

eBPF 方法可以成为云网络的基石吗？这是一个大问题。eBPF 就像一根数据软管，可能对很多事情都很有用，但对于第 7 层数据呢？它并不适合监控跨越互联网的数据。它可以处理在 Kubernetes 平台上运行的内核服务，但这只是软件工程师现在在如此广阔的攻击面中所需要的部分。

但正如 Volk 指出，Cilium（同样建立在 eBPF 之上）为传输层（第 4 层）和应用层（第 7 层）提供了可编程控制，允许“通过 TCP、UDP、ATP 和 MTCP 等协议执行网络策略，这些协议为应用程序提供端到端通信服务”。

并非所有人都相信 eBPF 可以解决所有网络问题。[Wesley Hales](https://www.linkedin.com/in/wesleyhales/)，[LeakSignal](https://www.leaksignal.com/) 的首席执行官，将 eBPF 看作一把锤子，任何网络问题都是一颗钉子。特别是，Hales 提到了传输中的敏感数据分类。但让我们把这个话题留到下次讨论。

## 云原生安全：点 vs. 平台

今年早些时候，[Cisco](http://cisco.com/?utm_content=inline+mention) [收购了 Isovalent](https://thenewstack.io/ciscos-strategic-move-in-the-isovalent-acquisition-ebpf/)。在 Cilium 中体现了 eBPF 方法，我问 Graf 他如何看待云原生安全领域、服务网格的作用、微隔离以及 Isovalent 对 Cisco 的意义。

**Alex Williams：Tom，云原生安全的完整解决方案是什么样的？客户需要什么？**

**Thomas Graf：** 是的。从应用程序的源头开始，您需要一个解决方案来扫描您的源代码并找出其中的漏洞。

理想情况下，代码图会告诉您哪些漏洞在您的代码中是可访问的。然后，您需要解决方案来保护您的依赖项的供应链：漏洞管理。如果您使用带有 [常见漏洞和披露] 的库，您需要能够跟踪和修复它们。然后，您需要为您的基础设施进行云态势管理。如果您的 [虚拟专用云] 是完全开放的，那么您没有使用安全组。

最好有一个云态势管理解决方案。然后，当您开始运行应用程序时，您需要运行时安全——针对您的云工作负载的 Kubernetes 的威胁缓解。当然，您还需要所有这些的可观察性。比如，您在运行什么？您暴露了什么？您的风险是什么？

您需要优先考虑这些风险，因为对于大多数客户来说，会有大量的发现，您需要弄清楚首先要调查什么。现在人们是否要求更全面的解决方案？他们一直在选择点解决方案，并看到了集成这些解决方案所需的复杂性。

大多数人首先从一个广泛的解决方案开始，然后发现它们不够完整。然后他们转向点解决方案，很快它就变得非常难以管理，主要是因为 [[云原生应用程序保护平台](https://thenewstack.io/4-benefits-of-choosing-a-cnapp-for-cloud-security/)] 空间没有开源标准化。

因此，客户试图退一步说，好吧，我们是想回到一个广泛的解决方案，还是想说服供应商变得更广泛，将多个点解决方案结合起来？这将是未来几年内需要进行的关键讨论。我们如何才能获得一个足够好、也足够广泛的解决方案，以便于管理？

## 服务网格的问题

**Williams：服务网格怎么样？服务网格似乎是 Kubernetes 的一个很好的后续，它通过 API 中心环境提供了代理功能，而您在 Kubernetes 中就有这种环境。因此，它似乎是一个自然的选择，也是公司考虑其整体安全态势的地方。这是准确的吗？**

**Graf：** 是的，我认为这是准确的。我认为服务网格是顶层的一个很好的小层，从概念上讲，它绝对要求您需要一个逻辑连接层，该层引入身份，即引入丰富的安全机制来实现 [零信任](https://thenewstack.io/what-is-zero-trust-security/) 原则。到目前为止，服务网格的实现方式绝对没有让客户满意。

我认为该领域的每个供应商都必须做得更好，找到一个不太显眼的解决方案，就像基础设施的一部分，而不是您需要主动管理的东西。此外，运行服务网格的开销和负担必须大幅降低。

## 微隔离和 NSX

**Williams：那么为什么安全解决方案是 NSX 的答案？**

**Graf:** 嗯，NSX 从根本上来说是分布式防火墙的核心。就像，如果你看一下Cilium，为什么Cilium 如此吸引人？是的，它在做很多网络工作，但它被用来做防火墙微分段和加密。NSX 也是一样的。

移动数据包几乎就像一个实现细节。真正重要的是安全地做到这一点。所以当你购买产品时，你购买的是网络安全应用程序，即使它显然也只在做连接。这几乎就像一个包含的细节。

这几年来，这是否一直是 NSX 的主要卖点？绝对是的。微分段是 NSX 的主要卖点。那么现在，今天的主要卖点是什么？对于 Cilium 来说，它完全一样。很多 NSX 客户会说，Cilium 就是 NSX，但对于容器和 Kubernetes 来说，云原生容器是基于身份的。

所以 Cilium 比上一代更先进，对吧？它不仅仅是为容器扩展；它理解身份是原生集成到云提供商中的。它不仅仅是针对 [虚拟机] 或虚拟化，但主要适用的用例是一样的。

## 思科和 Isovalent

**Williams: Thomas，我们谈到了客户寻求的这些更全面的解决方案。思科 Isovalent 与此相关的背景是什么？**

**Graf:** 所以想想。Isovalent 在云原生和 Kubernetes 领域非常成功。与思科合作，我们现在将我们构建的云原生方法带到更广泛的市场，进入数据中心、边缘和公有云。

因此，我们构建了 Cillium 用于网络安全、分段和云原生网络，以及 Tetragon 运行时安全，使其在数据中心可用，在服务器上运行 Tetragon，在 DHs [数据处理单元] 和交换机上运行 Cillium，并基本上构建了一个安全结构，可以保护不仅 Kubernetes 部分，还可以保护您的整体基础设施。

因此，安全结构适合客户购买的所有这些点解决方案……然后，我认为从思科的角度来看，显然带来了 CNAPP 功能，例如提供一个不仅广泛而且足够深入的整体丰富平台。思科在过去几年中进行了大量收购，以购买每个点的解决方案。现在正在构建一个平台来统一它们，为您提供一个具有强大垂直点解决方案的平台的体验。
