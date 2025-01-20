# eBPF 工具识别跨区域 Kubernetes 网络流量

![Featued image for: eBPF Tool Identifies Cross-Zone Kubernetes Network Traffic](https://cdn.thenewstack.io/media/2025/01/241cafef-poh-wei-chuen-boyqvkeveg4-unsplash-1024x683.jpg)

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

## 隆重推出 Kubezonnet

生成的开源程序 [Kubezonnet](https://github.com/polarsignals/kubezonnet)（KUBErnetes cross-ZONe NETwork monitoring）于上周发布。

Kubezonnet 由四名 Polar Signals 工程师构建，用于监控和测量 Kubernetes 集群生成和使用的 Google 跨区域网络流量。

正是 eBPF 的可编程性及其与 Kubernetes 元数据的集成，使 Polar Signals 能够开发专门用于监控 Pod 流量的软件。

该软件部署在 Kubernetes 上，因此安装它就像应用清单一样简单。它需要在传统主机路由模式下运行 [Cilium CNI](https://thenewstack.io/cilium-cncf-graduation-could-mean-better-observability-security-with-ebpf/) 和 Linux 内核 6.4 或更高版本，用于 [Netfilter](https://blogs.oracle.com/linux/post/introduction-to-netfilter)，这是该版本中引入的 Linux 内核网络流量过滤器。

该软件使用 eBPF 来跟踪网络数据包并聚合流量数据。
Kubezonnet has two components: an agent and a server.

An agent is deployed on each node.

As the engineers explain, Kubezonnet uses the Netfilter post-routing hook to track network packets leaving Pods and aggregates traffic data at 10-second intervals.

The collected data is sent to one or a set of central servers, which resolve the source and destination IPs to Kubernetes Pods and nodes. This process determines the region of the nodes to identify inter-region traffic.

Statistics are exposed as [Prometheus metrics](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/), used to monitor total inter-region traffic per Pod and provide detailed insights into traffic patterns between specific Pods via traffic logs.

The server can be deployed per cluster or per region.

The software can generate metrics such as the top 20 Pods by inter-region network traffic per second over the last five minutes, measured in megabytes.

It can also calculate cumulative amounts, such as the top 20 Pods by inter-region network traffic over the past week, measured in gigabytes. This cumulative data is more useful when trying to figure out why cloud bills are spiking.


## How Polar Signals Reduced Inter-Region Traffic

Polar Signals deployed Kubezonnet on its own network to identify areas where inter-region traffic seemed excessive.

The culprit was the database.

Database traffic "was previously hard to detect because many services interact with the main database, and many services transfer a lot of bytes over the network," Polar Signals founder [Frederic Branczyk](https://www.brancz.com/) wrote in a [blog post](https://www.polarsignals.com/blog/posts/2025/01/09/introducing-kubezonnet) explaining the technology.

Traffic logs revealed a single workload was responsible for the bulk of the traffic.  Addressing this was straightforward, Branczyk wrote.

However, the biggest bottleneck was the many rule evaluations across the company's monitoring stack. Some redesign alleviated this traffic congestion; engineers simply set up a [Thanos stack](https://thenewstack.io/thanos-takes-scalable-highly-available-prometheus-monitoring-to-cncf-incubation/) in each region, which not only reduced traffic but also improved the robustness of the monitoring system through redundancy.

Looking ahead, the company plans to build an alerting system to notify engineers when certain network thresholds are reached, preventing future surprise large cloud bills. It also plans to build support for [IPv6](https://thenewstack.io/why-is-ipv6-adoption-slow/) and add more traffic metrics.

Want to know how much (expensively) your Kubernetes traffic is traversing between your cloud provider's availability zones? Kubezonnet can help.

[YOUTUBE.COM/THENEWSTACK
Technology moves fast. Don't miss an episode. Subscribe to our YouTube channel for all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)