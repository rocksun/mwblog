
<!--
title: eBPF工具识别跨区域Kubernetes网络流量
cover: https://cdn.thenewstack.io/media/2025/01/241cafef-poh-wei-chuen-boyqvkeveg4-unsplash.jpg
-->

Polar Signals百思不得其解，为何会有如此高昂的跨区域流量费用。于是，他们求助于eBPF技术，最终将云账单削减了一半。

> 译自 [eBPF Tool Identifies Cross-Zone Kubernetes Network Traffic](https://thenewstack.io/ebpf-tool-identifies-cross-zone-kubernetes-network-traffic/)，作者 Joab Jackson。

与大多数云提供商一样，Google 不会向用户收取单个可用区内网络流量的费用。Google 目前拥有 [124 个可用区](https://cloud.google.com/about/locations)，分布在 41 个区域。

但是，跨区域传输的数据包必须付费。最后一次检查显示，美国和欧洲之间的数据包传输费用为每 GB 0.05 美元，欧洲与亚洲之间为 0.08 美元。费用会迅速累积。

由于其监控服务的性质，Polar Signals 拥有大量的 Kubernetes 跨区域网络流量。[Polar Signals Cloud](https://www.polarsignals.com/docs/overview) 是一项托管服务，用于存储和分析用户系统持续分析数据的。

持续分析从网络基础设施中的每个进程收集当前堆栈的数据。尽管它使用相对较低的采样率，但用户数据仍然会快速累积。到 2024 年年中，跨区域流量占公司 [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) 账单的近一半。

由于没有可以专门测量跨区域 Kubernetes 流量的工具，公司工程师构建了一个监控器，据 [案例研究](https://ebpf.foundation/case-study-polar-signals-uses-ebpf-to-monitor-internal-cross-zone-network-traffic-on-kubernetes-reducing-these-operating-costs-by-50/)（[eBPF 基金会](https://thenewstack.io/ebpf-finds-a-home-with-a-new-foundation/) 周四发布）显示，该监控器帮助将跨区域流量账单削减了 50%。

秘诀是什么？eBPF。

## eBPF 救援

起初，公司转向商业和开源网络监控工具来描述这种流量。对于其商业平台，公司使用 [Kubernetes](https://thenewstack.io/Kubernetes/) 和 [Cilium](https://cilium.io/) 进行容器网络管理。

对于 Kubernetes，[kubectl](https://thenewstack.io/kubecost-monitor-kubernetes-costs-with-kubectl/) 具有 *top nodes* 命令，该命令可以提供节点级别网络流量（传输和接收字节）的报告。此外，[cAdvisor](https://thenewstack.io/wavefront-monitors-containers/) 集成到 [Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet) 中，它收集网络流量数据。

但是，这些工具都不能轻松识别跨越多个 Google 区域的网络流量。Cilium 本身只能报告网络流量的每日汇总成本，在 Pod 或工作负载级别没有粒度。

因此，公司使用 eBPF 自己构建了一个。

该公司对 [eBPF](https://thenewstack.io/ebpf-is-coming-for-windows/) 并不陌生。该公司已经为其客户创建了一个内存跟踪工具，称为 [Parca](https://www.parca.dev/)，它使用 [eBPF](https://thenewstack.io/what-is-ebpf/)。

eBPF 是一种新的 [Linux](https://thenewstack.io/introduction-to-linux-operating-system) 内核技术，在过去几年中引起了系统提供商的兴趣。它实际上是在 [Linux 内核](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/) 内运行的 [沙箱环境](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/)，开销极小。

小型 [eBPF 程序](https://thenewstack.io/linux-technology-for-the-new-year-ebpf/) 由内核中的钩子或事件触发，例如系统调用或网络事件。

构建此类程序的初始要求包括：

- 准确监控和记录跨区域流量，
- 与 Kubernetes 元数据无缝集成，
- 提供实时指标。

## Kubezonnet 介绍

生成的开源程序 [Kubezonnet](https://github.com/polarsignals/kubezonnet)（KUBErnetes cross-ZONe NETwork monitoring）于上周发布。

Kubezonnet 由四名 Polar Signals 工程师构建，用于监控和测量 Kubernetes 集群生成和使用的 Google 跨区域网络流量。

正是 eBPF 的可编程性及其与 Kubernetes 元数据的集成，使 Polar Signals 能够开发专门用于监控 Pod 流量的软件。

该软件部署在 Kubernetes 上，因此安装它就像应用清单一样简单。它需要在传统主机路由模式下运行 [Cilium CNI](https://thenewstack.io/cilium-cncf-graduation-could-mean-better-observability-security-with-ebpf/) 和 Linux 内核 6.4 或更高版本，用于 [Netfilter](https://blogs.oracle.com/linux/post/introduction-to-netfilter)，这是该版本中引入的 Linux 内核网络流量过滤器。

该软件使用 eBPF 来跟踪网络数据包并聚合流量数据。

Kubezonnet有两个组件：一个代理和一个服务器。

每个节点上都部署了一个代理。

正如工程师们所解释的，Kubezonnet使用Netfilter的后路由钩子来追踪离开Pod的网络数据包，并在10秒的时间间隔内聚合流量数据。

收集到的数据被发送到一个中央服务器，或一组服务器，这些服务器将源IP和目标IP解析为Kubernetes的Pod和节点。这个过程确定了节点的区域，以识别跨区域流量。

统计信息以Prometheus指标的形式暴露出来，用于按Pod监控总跨区域流量，同时也通过流量日志提供特定Pod之间流量模式的详细洞察。

服务器可以部署在每个集群上，或者每个区域上。

该软件可以生成指标，例如过去五分钟内按跨区域网络流量每秒排名前20的Pod，以兆字节为单位衡量。

它还可以计算累积量，例如过去一周内按跨区域网络流量排名前20的Pod，以吉字节为单位衡量。像这样的累积量在试图弄清楚云账单为何飙升时可能更有用。

## 极化信号如何减少跨区域流量

在自己的网络上部署 Kubezonnet 时，Polar Signals 发现跨区域流量似乎过多。

其中一个原因是数据库。

Polar Signals 的创始人 Frederic Branczyk 在一篇解释该技术的博客文章中写道：“数据库流量此前很难检测，因为许多服务与主数据库交互，且许多服务在网络上传输大量字节。”

流量日志显示单一工作负载占主导流量。布兰奇尼克写道，解决这一问题非常简单。

然而，最大的跨边界因素是那些在公司监控堆栈中传播的众多规则评估。通过一些重新工程，缓解了这一交通堵塞；工程师们在每个区域都设置了一个 Thanos 堆栈，这不仅减少了流量，还通过冗余提高了监控系统的稳健性。

展望未来，公司计划建立一个警报系统，以便在达到某些网络阈值时通知工程师，防止未来出现意外高昂的云账单。公司还计划支持 IPv6，并增加更多的流量指标。

你想知道你的 Kubernetes 流量（昂贵地）在云提供商的可用区之间传输了多少吗？Kubezonnet 可以帮忙。