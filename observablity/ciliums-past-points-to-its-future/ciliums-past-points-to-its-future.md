
<!--
title: Cilium的过去指向其未来
cover: https://cdn.thenewstack.io/media/2024/05/c2fe16a1-hadija-9cgmkmzyhh0-unsplash-1.jpg
-->

Cilium 的未来不仅涉及 Kubernetes 和容器，还涉及虚拟机、边缘用例和其他环境。

> 译自 [Cilium's Past Points to Its Future](https://thenewstack.io/ciliums-past-points-to-its-future/)，作者 B Cameron Gain。

[Cilium](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/) 显然作为一项动态且流行的开源项目，正在经历许多变化，该项目大量利用 [eBPF](https://thenewstack.io/what-is-ebpf/)，但其最初原因仍然得到控制：一个提供安全、[可观测性](https://thenewstack.io/observability/) 和网络功能的工具。其功能或挂钩从内核扩展到整个网络，包括云、本地或其他基础设施。此定义涵盖了许多内容，而 Cilium 应继续适应和扩展，以满足基础设施需求的变化。

在本文中，我们着眼于 [Cilium](https://cilium.io/) 的未来，这在很大程度上涉及无处不在的扩展，当然不仅仅是 [Kubernetes](https://thenewstack.io/kubernetes/) 和 [容器](https://thenewstack.io/containers/)，还包括虚拟机、边缘用例和其他环境。当然，思科的收购及其与其他工具的集成也将对其未来发挥作用。

但它最初存在的理由是什么？作为其创建者，编写了 Cilium 代码的第一行，[Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547/?originalSubdomain=ch)，他是 [Isovalent](https://thenewstack.io/isovalent-open-sources-tetragon-ebpf-based-observability-platform/) 的首席技术官，他在 3 月份的 KubeCon + CloudNativeCon Europe 演讲中描述了他所说的四项支柱，这些支柱没有改变。

回顾他在 [LinuxCon](https://events.linuxfoundation.org/archive/2022/open-source-summit-north-america/about/linuxcon/) 上的演讲，该演讲于 2016 年在多伦多举行，当时 Graf 最初开始描述 Cilium 项目，作为一种使用 eBPF 提供快速 IPv6 容器网络的方法。Graf 描述的四项支柱现在仍然像当时一样：

- 可扩展性，适用于容器，“因为我们不再仅仅考虑虚拟机”以及策略和地址。
- 可扩展性：“因为当时用户空间网络是主流并且正在接管”，所以有必要“恢复内核相关性”并“在内核中尽可能地像在用户空间网络中一样可扩展”。
- 简单性
- 性能：“当然，我们希望数据包快速移动，”Graf 说。

虽然可以追溯到他 2016 年的原始演讲，但 Graf 说“这仍然完全是 Cilium 今天的模样”：

![](https://cdn.thenewstack.io/media/2024/04/2092ae83-capture-decran-2024-04-26-162935.png)

作为 [CNCF](https://cncf.io/?utm_content=inline+mention) 项目，Cilum 的开发特别专注于 Kubernetes，用于连接、防火墙管理和集群监控。正如 Isovalent 的高级技术营销工程师 [Nico Vibert](https://uk.linkedin.com/in/nicolasvibert) 在他的电子书 [“KubernetesNetworking and Cilium: An Instruction Manual for the Network Engineer,”](https://isovalent.com/books/kubernetes-networking-and-cilium/) 中所写，Kubernetes 仍然是一个非常难以管理的动物，而 Cilium 提供了一个开源选项来简化艰巨的任务。“尽管我拥有 CCIE [思科认证互联网专家] 并且在网络行业工作了近 20 年，但我仍然觉得 Kubernetes 网络令人困惑。”然而，Kubernetes 网络方面以及现在已成为 Kubernetes 的事实网络平台：Cilium。

## 最佳 CNI

“在网络项目开始时，Kubernetes 集群的操作员和架构师必须选择一个 CNI [容器网络接口]，该接口提供所需的网络、安全和可观测性功能……并且在大多数 CNI 评估中获胜的往往是 Cilium 项目，”Vibert 写道。

事实上，从开发早期阶段开始，设计一个适用于 Kubernetes 的最佳 CNI 一直是 Cilium 创建者的既定目标。“任务非常、非常简单：将 eBPF 引入 Kubernetes 并成为尽可能好的 CNI，”Graf 说。“这本质上是一个任务划分，我们仍在朝着这个目标努力。”

尽管 Kubernetes 备受关注，但世界并不局限于此。组织通常会混合搭配不同的环境，跨越不同的云环境和本地环境。“我们希望将 Cilium 基本上也带到世界其他地方。因此，简单性、可扩展性、安全性，不需要十几种不同的工具。我们希望将它带到 Kubernetes 之外，用于您的虚拟机、服务器、边缘、多云连接，”Graf 说。“当您考虑连接时，您应该只考虑 Cilium：如何安全地做到这一点，如何做到可扩展，无论是针对容器、Kubernetes、一堆服务器还是虚拟机。Cilium，这是我们对未来的愿景：Cilium 应该成为标准或下一代网络层。”

Cilium 通常仍然是大基础设施的一部分，并且不存在于所谓的单一控制面板等其他基础设施中。这种集成和协作通常与许多其他复杂层结合在一起，通常与云原生基础设施结合在一起。随着其适用性继续进入其他不同环境，该项目涉及大量集成和集成开发工作。

### 层级

在网络层级上，Cilium 涵盖第 4 层（传输层）和第 7 层（应用程序层）以供其使用。同时，它与 [思科](http://cisco.com/?utm_content=inline+mention) 的集成将在许多方面值得考虑。正如 [Torsten Volk](https://www.linkedin.com/in/torstenvolk)，[企业管理协会 (EMA)](https://www.enterprisemanagement.com/) 的分析师，[最近解释的那样，](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/) 思科收购 Isovalent 意味着两者将共同涵盖 [Splunk](https://thenewstack.io/splunk-opentelemetry-and-the-future-of-observability/) 和 [AppDynamics](https://thenewstack.io/appdynamics-why-todays-developers-are-in-a-good-place/) 集成、思科 ACI 集成、Intersight 集成和跨思科平台的 Tetration 集成。

“通过收购 Isovalent，Cilium 与思科广泛产品组合的集成在多个层面具有战略意义。除了通过利用 eBPF 技术扩展思科在网络和安全可观察性方面的能力外，它还增强了公司在其现有平台（如 Splunk、AppDynamics 和 Intersight）上提供集成解决方案的能力，”Volk 说。“此次收购使思科能够提供更全面的基础设施管理和可观察性解决方案，这对现代复杂基础设施环境的性能和安全性至关重要。这种集成带来了向基础设施管理的更统一方法迈进，与行业向融合的智能解决方案的趋势保持一致，这些解决方案可以支持动态的云原生应用程序。”

至于第 3 层，它确实在某些方面涵盖了这一点，但这是通过将 Cilium 与其他不同类型的项目与 eBPF 集成来完成这项工作的，特别是对于策略。对于第 3 层来说，与 [Tigera](https://www.tigera.io/) 开发的 Calico 有很多重叠和利用，正如 Graf 所描述的，“他们肯定做对了”。

Volk 表示他同意，因为 Cilium 与其他以 eBPF 为中心的项目的集成以实现第 3 层功能，特别是在策略执行中，这是一个战略举措，可以增强云原生环境中网络管理的粒度和灵活性。“利用 Tigera 开发的 Calico 进行第 3 层，补充了 Cilium 的功能，允许对网络分段和安全策略采用稳健的方法。该领域的专家认可 Calico 的方法，这突显了其在管理现代分布式系统中固有的复杂网络挑战方面的有效性，”Volk 说。“人们认识到，这些技术的结合提供了一个全面的解决方案，符合行业对可扩展、安全和高效网络运营的需求。”

Graf 解释说，以前，网络要求“你必须学习如何进行子网寻址，甚至让两个 Pod 相互连接”。虽然 Cilium 提供了多网络，但它在第 3 层的核心概念是“每个人都可以与每个人交谈”，Graf 说。“然后，您可以采取策略来细分您想要的内容。我们还希望将策略与寻址分开。”
