
<!--
title: 利用eBPF增强Kubernetes操作
cover: https://miro.medium.com/v2/resize:fit:551/1*v_XW1Bb5Pv5NoeRYNwfamQ.png
-->

运行 Kubernetes 释放了容器的强大功能，但看到更多功能岂不更好？eBPF（扩展 Berkeley 数据包过滤器）是一种…

> 译自 [Harnessing eBPF for Enhanced Kubernetes Operations](https://medium.com/@renji.bio/harnessing-ebpf-for-enhanced-kubernetes-operations-f22442b1aed8)，作者 Renjith Pillai。

运行 Kubernetes 可以释放容器的强大功能，但如果能看到更多，岂不是更好？eBPF（扩展 Berkeley 数据包过滤器）是 Kubernetes 的游戏规则改变者。它让你可以窥探内部，并微调集群以提高安全性、性能和故障排除能力。本博客系列将探讨 eBPF 如何改变 Kubernetes，深入了解让这一切成为可能的酷炫项目。

## 了解 Linux 内核的核心

每个 Linux 操作系统的核心都是内核，它就像一个协调系统组件的乐团指挥。它在硬件和软件之间进行接口，管理资源，促进通信，并提供安全和进程管理等核心服务。

## 探索自定义内核编程

虽然常规编程通常会避免深入研究内核，因为其复杂性和风险，但在某些情况下，这种深度是必要的。内核编程可以执行诸如为新硬件创建设备驱动程序、优化系统性能和增强安全措施等任务。

## 使用 eBPF 引入安全的内核程序执行

eBPF，即扩展 Berkeley 数据包过滤器，作为在 Linux 内核中安全运行自定义程序的强大解决方案而出现。它促进了诸如数据包过滤、网络监控、安全强制和性能分析等任务，所有这些都在沙盒环境中进行。

## eBPF 的关键方面

- eBPF 赋予开发人员直接在内核中制作和执行自定义程序的能力，服务于数据包过滤、网络监控、跟踪、安全强制和性能分析等多种目的。
- 这些程序在沙盒环境中运行，并在执行前经过彻底**验证**，与用 C 编码的成熟内核模块相比，显著降低了崩溃或安全漏洞的风险。
- 针对卓越性能而设计，eBPF 程序**以最小的开销高效处理大量数据**。通过在运行时将 JIT 编译为本机机器代码，它们确保了最佳执行速度。
- eBPF 程序提供**对各种内核子系统（如网络套接字、跟踪点和系统调用）的动态附加**。此功能可以在不修改内核本身的情况下实现对系统行为的灵活且精确控制。

## eBPF 工作原理的简化说明

下图提供了 eBPF 架构的简化描述。

![eBPF 架构](https://miro.medium.com/v2/resize:fit:640/format:webp/1*v_XW1Bb5Pv5NoeRYNwfamQ.png)

在合并到内核之前，eBPF 程序必须经过一系列特定的验证。此验证过程需要在虚拟机中运行 eBPF 程序，使验证程序能够进行一系列评估。验证程序仔细检查 eBPF 程序在内核中的潜在执行路径，确保不间断执行且不会遇到任何可能导致内核锁定的循环。

在成功完成所有检查后，eBPF 程序将加载并编译到内核中，位于代码路径中的指定位置，等待适当的信号。在收到信号（通常以事件的形式）后，eBPF 程序将部署在代码路径中。随后，字节码将根据其指令收集和执行信息。

从本质上讲，eBPF 的基本功能是为程序员提供一种在 Linux 内核中执行自定义字节码的安全方法，而无需修改内核源代码。

## 为什么在 Kubernetes 中使用 eBPF？

传统的监控工具通常依赖于日志记录或基于代理的检测，这会增加开销并限制可见性。eBPF 在 Kubernetes 环境中表现出色，原因有以下几个：

- **深入可见性：** eBPF 直接探查内核，提供对系统调用、网络活动和应用程序行为的洞察，这是传统工具无法比拟的。
- **精细控制：** 使用 eBPF，你可以根据部署的特定方面定制监控。想要跟踪特定服务的网络流量？或者识别异常的系统调用？eBPF 让你能够做到这一点。
- **轻量且高效：** eBPF 程序经过高度优化，对系统性能的影响很小，使其成为生产环境的理想选择。

## Kubernetes 中的 eBPF 用例

让我们探讨一些引人注目的用例，展示 eBPF 在 Kubernetes 中的强大功能：

* **安全监控：** eBPF 擅长检测可疑活动。您可以编写程序来跟踪与已知漏洞相关的系统调用，或监控网络流量以查找异常模式。这对于入侵检测和预防非常宝贵。
* *示例：* 设想一个 eBPF 程序，它标记任何尝试在受限目录中打开系统文件的进程。这可能表明存在潜在的特权提升尝试。
* **性能调试：** 是否在为速度缓慢的 Pod 而苦恼？eBPF 可以帮助找出瓶颈。您可以跟踪与磁盘 I/O、网络调用和函数执行时间相关的系统调用，以识别应用程序或底层基础设施中的性能问题。
* *示例：* 一个监控容器内函数执行时间的 eBPF 程序可以揭示某个特定代码块是否导致性能下降。
**网络流量管理：** eBPF 使您能够深入了解集群内的网络流量。您可以跟踪 Pod 之间的通信，识别网络拥塞的来源，甚至可以根据特定条件实施自定义过滤规则。
* *示例：* 一个 eBPF 程序可用于将特定 Pod 的出站网络流量限制到仅授权的 IP 地址。
* **服务网格可观测性：** eBPF 在 Istio 或 Linkerd 等服务网格部署中发挥着至关重要的作用。它提供了跟踪跨服务请求、识别瓶颈和解决服务通信问题所需的基本数据。

## Kubernetes 的主要 eBPF 工具概况

**[Cilium](https://github.com/cilium/cilium)** — 基于 eBPF 的网络、安全性和可观测性

Cilium 是一个开源项目，提供基于 eBPF 的网络、安全性和可观测性能力。它专门从头开始设计，旨在将 eBPF 的优势引入 Kubernetes 世界，并解决容器工作负载的新的可扩展性、安全性和可见性需求。

**[Calico](https://github.com/projectcalico/calico)** — 适用于容器和 Kubernetes 的可插拔 eBPF 网络和安全性

Calico 开源版旨在简化、扩展和保护容器和 Kubernetes 网络。Calico 的 eBPF 数据平面利用 eBPF 程序的强大、高速和高效，为您的环境提供网络、负载平衡和内核安全执行。

**[Falco](https://github.com/falcosecurity/falco)** — 云原生运行时安全

Falco 是一种行为活动监控器，旨在检测应用程序中的异常活动。Falco 使用 eBPF 在 Linux 内核层审计系统。它通过其他输入流(如容器运行时指标和 Kubernetes 指标)来丰富收集的数据，并允许持续监控和检测容器、应用程序、主机和网络活动。

**[Pixie](https://github.com/pixie-io/pixie)** — 可编写的 Kubernetes 可观测性

Pixie 是一种用于 Kubernetes 应用程序的开源可观测性工具。Pixie 使用 eBPF 自动捕获遥测数据，无需手动检测。开发人员可以使用 Pixie 查看集群的高级状态(服务映射、集群资源、应用程序流量)，也可以深入查看更详细的视图(Pod 状态、火焰图、单个完整应用程序请求)。

**[Hubble](https://github.com/cilium/hubble)** — 使用 eBPF 的 Kubernetes 网络、服务和安全可观测性

Hubble 是一个完全分布式的云原生工作负载网络和安全可观测性平台。它构建于 Cilium 和 eBPF 之上，以完全透明的方式深入了解服务通信和行为以及网络基础设施。

**[Grafana Pyroscope](https://github.com/pyroscope-io/pyroscope)** — 持续性能分析平台  

Grafana Pyroscope 是一个开源软件项目，用于聚合持续性能分析数据。持续性能分析是一种可观测性信号，允许您深入到行号级别了解工作负载的资源(CPU、内存等)使用情况。Grafana Pyroscope 与 Grafana 完全集成，允许您将性能分析数据与其他可观测性信号(如指标、日志和跟踪)关联。

**[Caretta](https://github.com/groundcover-com/caretta)** — 基于 eBPF 的 Kubernetes 服务映射

Caretta 是一个使用 eBPF 跟踪 Pod 之间网络流量的 Kubernetes 服务映射。它可用于可视化 Kubernetes 集群中服务之间的网络流量，并深入了解网络流量和服务之间的关系。

**[KubeArmor](https://github.com/kubearmor/KubeArmor)** — 容器感知的运行时安全执行系统

KubeArmor 是一个容器感知的运行时安全执行系统，使用 LSM 和 eBPF 在系统级别限制容器的行为(如进程执行、文件访问、网络操作和资源利用)。

总之，Kubernetes 中的 eBPF 生态系统提供了一套强大的工具，用于深入了解和控制容器化环境。从 Cilium 的安全性重点到 Hubble 的可观测性优势，这些项目展示了 eBPF 在优化和故障排除 Kubernetes 集群方面的通用性。但这只是冰山一角！在未来的文章中，我们将更深入地探讨这些工具的具体功能，并提供将它们应用于您的 Kubernetes 生态系统的实际指导。敬请期待对 Kubernetes 中 eBPF 令人兴奋世界的更深入了解！