
<!--
title: 针对Kubernetes的Tetragon eBPF：裁决出炉
cover: https://cdn.thenewstack.io/media/2024/09/abea659d-getty-images-pkuhk2_sqla-unsplash.jpg
-->

Tetragon 的一个关键特性是它如何简化安全可观测性，并且它在不影响性能的情况下增强了可观测性。

> 译自 [Tetragon eBPF for Kubernetes: The Verdict Is Out](https://thenewstack.io/tetragon-ebpf-for-kubernetes-the-verdict-is-out/)，作者 B Cameron Gain。

[Cilium Tetragon](https://github.com/cilium/tetragon) 创建于大约一年前，旨在解决 [Cilium](https://thenewstack.io/cilium-cncf-graduation-could-mean-better-observability-security-with-ebpf/) 的一些缺陷以及 [eBPF](https://thenewstack.io/what-is-ebpf/) 工具（包括商业和开源工具）的一些普遍缺陷。其中一个主要问题是功耗难题。虽然 eBPF 凭借其可观测性和安全功能（从内核深处开始并扩展到不同环境）相对强大，但仍需考虑权衡取舍。[Tetragon](https://thenewstack.io/tetragon-1-0-promises-a-new-era-of-kubernetes-security-and-observability/) 的创建是为了缓解其中的一些挑战，特别是在不影响性能的情况下增强可观测性。

Tetragon 的关键特性之一是它如何简化安全[可观测性](https://thenewstack.io/observability/)。它与各种库无缝集成，这些库可以很好地连接到 [Grafana](https://thenewstack.io/grafana-relies-on-embrace-to-pull-mobile-data/) 和其他控制台等可观测性工具。这简化了监控，使团队更容易获得对其环境的洞察力。

但 Tetragon 的另一个重要（可以说是关键）特性是其 [Kubernetes](https://thenewstack.io/kubernetes/)-原生设计，这意味着它在构建时就高度兼容 Kubernetes。这是因为它与传统的网络系统截然不同。这使得 Tetragon 有可能成为 Kubernetes 环境中特别强大的工具，在 Kubernetes 环境中，其挂钩和集成特别有效。

但自 Tetragon 1.0 发布一周年以来，它对深奥的 Kubernetes 环境进行[监控和可观测性](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) 的可行性是否得到证实？

正如 Kubernetes 安全提供商 [ARMO](https://www.armosec.io/) 的首席技术官兼联合创始人 [Benyamin Hirschberg](https://www.linkedin.com/in/ben-hirschberg-66141890/?originalSubdomain=il) 解释的那样，Tetragon 由 Cilum 项目背后的同一支团队创建，他们是 eBPF 技术的领先团队之一，他们扩展了网络功能。“Cilium 为 eBPF 提供了运行时安全检测和响应功能，也在 eBPF 中，”Hirschberg 说道。

Tetragon 面向 Kubernetes 和云原生环境，尤其是在 Kubernetes 抽象方面。但 Tetragon 不仅仅如此，Rice 在 [开源峰会](https://events.linuxfoundation.org/open-source-summit-europe/) 小组讨论“[eBPF：云基础设施工具的新纪元](https://events.linuxfoundation.org/open-source-summit-europe/program/schedule/?utm_source=google&utm_medium=paid-search&utm_campaign=osseu_2024&utm_term=events-emea-search-lf-osseu_2024&utm_content=osseu_sitelink&campaignid=21416652713&adgroupid=164409738936&creative=703929171036&matchtype=b&network=g&device=c&keyword=open%20source%20summit%20europe%202024&utm_term=open%20source%20summit%20europe%202024&utm_campaign=Events+-+EMEA+-+Search+-+LF&utm_source=google&utm_medium=ppc&hsa_acc=8666746580&hsa_cam=21416652713&hsa_grp=164409738936&hsa_ad=703929171036&hsa_src=g&hsa_tgt=kwd-2321727920560&hsa_kw=open%20source%20summit%20europe%202024&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjw_4S3BhAAEiwA_64Yhk3ygWQGzaTHmF7LjsF1Omlc4fprf__dXG2Q0UH4C36aUcjERr4wnBoCuEMQAvD_BwE)”的问答环节中回应道。借助 Tetragon，用户可以访问可以附加到不同事件的安全配置文件并报告安全块。“您可以在主机上直接使用 Tetragon；它不必与容器或 Kubernetes 一起使用，”Rice 说道。

## Tetragon 由用户空间代理和内核组件组成。

正如 [Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547/?originalSubdomain=ch)（Isovalent 联合创始人兼首席技术官，思科云网络和安全副总裁）在 Tetragon 公开发布时的网络广播中所解释的那样，艰苦的工作发生在内核中的 eBPF 中，从而实现了低开销。代理收集数据并与日志记录或指标系统交互。实时执行发生在内核中，允许系统比必须在用户空间中处理操作更快地采取行动。

由于 Tetragon 深入嵌入内核，因此它在该级别的集成是一项重大成就，进一步巩固了其在增强现代云原生环境中的可观测性和安全性方面的作用。这种深度内核集成不容忽视，它代表着此类工具的重大进步。

性能开销的差异是由于 Tetragon 在内核中过滤事件造成的。传统的解决方案在用户空间中处理所有过滤，导致更高的开销。这种差异也体现在传输控制协议连接请求响应 (TCP-CRR) 中，这是一种网络基准测试，其中 Tetragon 通过减少延迟和连接开销优于传统解决方案。

Isovalent 开源主管 [Liz Rice](https://www.linkedin.com/in/lizrice/?originalSubdomain=uk) 告诉 The New Stack：“由于 Tetragon 旨在根据内核中的安全策略过滤事件，因此从内核流向用户空间的数据减少了。 “Tetragon 还将其 eBPF 挂钩放置在内核内部更深的位置，因此它不易受到几年前在 DEFCON 上记录的 [TOCTOU](https://nordvpn.com/cybersecurity/glossary/toctou-attack/) 攻击，”Rice 说。“它在内核中的有利位置意味着它可以查看在同一台机器上运行的任何应用程序，而无需修改、重新配置甚至重新启动应用程序。”

现在以 Kubernetes 为例：首先，Tetragon 作为代理连接到 Kubernetes API 服务器并检索内核的元数据。 Graf 在发布时解释说，这些元数据包含的内容扩展到命名空间 pod。Tetragon 旨在检测进程是否在 pod 中运行，包括 pod 名称、标签和所有相关详细信息。它还可以自动跟踪执行是在容器内部发生的，还是 kubelet 通过进入 pod 的命名空间（即 kubectl exec 所做的）从外部执行的，Graf 说。

例如，连接到 Hubble UI 的 Splunk 应用程序可以显示受感染的 Node.js 应用程序如何调用反向 shell，从而导致通过横向移动访问内部 Elasticsearch 服务。

“Tetragon 进入了一个已经被另一个著名的 [CNCF](https://cncf.io/?utm_content=inline+mention) 项目“占据”的解决方案空间：Falco。他们做出了一个慎重的设计决定，而不是像 Falco 那样向用户空间规则引擎提供所有 eBPF 事件，而是将他们的策略引擎嵌入到 eBPF 代码中。这种策略可以实现更高的性能（无需将大量事件传输到用户空间），但由于 eBPF 程序的限制，Tetragon 的策略语言不如 Falco 丰富。一方面，Tetragon 是一个非常有前途的项目，另一方面，它没有通过 Falco 长期以来支持的一些基本检测技术。

## 幕后

对于用户来说，抽象级别是这样的：当使用 Datadog、Grafana、Polar Signals 或其他可观测性提供程序时，Cilium（更不用说 eBPF 及其挂钩）在幕后运行。这意味着用户不一定需要了解 eBPF 就可以利用这项备受关注的技术。

在 Polar Signals 的情况下，eBPF 用于构建一个分析器，该分析器显示 CPU 资源使用最多的头条新闻编号。但是，可观测性提供程序 Polar Signals 最初并没有将 eBPF 用于此功能，而是使用完全不同的机制来获取这些数据。“这只是表明它恰好是这项工作的合适工具，但除非你深入研究并试图了解分析器本身是如何工作的，否则你不会知道 eBPF 正在幕后使用，”[Frederic Branczyk，](https://de.linkedin.com/in/frederic-branczyk) Polar Signals 创始人兼首席执行官在上述欧洲开源峰会小组讨论中表示。
