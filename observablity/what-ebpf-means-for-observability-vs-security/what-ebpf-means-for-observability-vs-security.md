
<!--
title: eBPF对可观测性与安全性的意义
cover: https://cdn.thenewstack.io/media/2025/03/d218b58c-ebpf-observability-image.jpg
summary: 🔥颠覆认知！eBPF已成云原生可观测性与安全利器！通过seccomp BPF、Tetragon等项目，实现运行时安全。OpenTelemetry (OTel)集成Elasticsearch，增强数据分析。但需警惕eBPF滥用，结合Linux security model，避免性能开销。服务网格场景下，iptables或为更优解！
-->

🔥颠覆认知！`eBPF`已成云原生可观测性与安全利器！通过`seccomp BPF`、`Tetragon`等项目，实现运行时安全。`OpenTelemetry (OTel)`集成`Elasticsearch`，增强数据分析。但需警惕`eBPF`滥用，结合`Linux security model`，避免性能开销。服务网格场景下，`iptables`或为更优解！

> 译自：[What eBPF Means for Observability vs. Security](https://thenewstack.io/what-ebpf-means-for-observability-vs-security/)
> 
> 作者：B Cameron Gain

[扩展的伯克利包过滤器 (eBPF)](https://thenewstack.io/what-is-ebpf/) 的采用率稳步上升，因为该技术已经发展了 10 多年。自创建以来，它一直是将代码直接从内核并通过沙箱分发到整个网络的卓越方式。
它能够收集信息并与网络上的代码和应用程序进行交互，本质上涵盖了由内核控制或连接到内核的任何代码或应用程序的完整范围。

鉴于 eBPF 在包括 Kubernetes 在内的各种环境中的广泛覆盖，eBPF 对[可观测性](https://thenewstack.io/observability-in-2025-opentelemetry-and-ai-to-fill-in-gaps/)、[安全监控](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) 和 [网络](https://thenewstack.io/networking/) 来说都是福音。在可观测性和安全性之间，存在一些重叠，但 eBPF 的用例在很大程度上是不同的。由于我们将在下面探讨的原因，eBPF 尚未充分发挥其在这两种情况下的潜力。

许多 eBPF 的功能可以说属于安全性和可观测性的范畴。[Bill Mulligan](https://www.linkedin.com/in/bamulligan) 是 [Cilium](https://cilium.io/) 和 eBPF 社区在 [Cisco](http://cisco.com/?utm_content=inline+mention) 的 [Isovalent](https://isovalent.com/) 的传播者，他告诉 The New Stack，eBPF 可以在监控大量文件操作时滤除噪音。

Mulligan 说：“eBPF 用于可观测性通常是最简单的切入点，以最小的风险提供即时可见性。“但它的影响远不止于此。它正在重塑我们保护和运营现代基础设施的方式，甚至让我们能够做一些事情，比如定制 [调度以获得更好的游戏性能。](https://bsky.app/profile/arighi.bsky.social/post/3lgqkh6y7lk2e)”

Mulligan 说，eBPF 已经用于在生产中执行安全策略，从过滤系统调用 ([seccomp BPF](https://www.kernel.org/doc/html/v4.17/userspace-api/seccomp_filter.html)) 或通过 [Tetragon](https://thenewstack.io/tetragon-ebpf-for-kubernetes-the-verdict-is-out/) 等项目启用运行时安全执行。例如，他指出，Google 将其用于其大部分内核安全：“关键是适当地使用 eBPF。”

事实上，他说，eBPF 比传统的安全机制（如内核模块或用户空间轮询）效率高得多。

“然而，像任何工具一样，它需要经过深思熟虑地应用。如果未经过适当优化，高频事件、频繁的用户空间转换和复杂的映射查找可能会引入开销，”Mulligan 说。“关键是通过利用 [Linux security model] 钩子、选择性事件跟踪和高效的数据结构来平衡性能和保护，以最大限度地减少影响，同时仍然执行强大的安全策略。”

## eBPF 和可观测性
eBPF 如何有益于可观测性取决于可观测性提供商如何利用它来帮助组织实现其可观测性目标。他们的方法将根据使用它们的组织的特定需求而有所不同，从而确保数据收集和可管理性之间的平衡。

但是，正确的工具和平台必须采取越来越细致的方法，因为一些组织可能需要或可能不需要了解内核的可见性，而另一些组织将寻求可能不需要在内核级别进行数据监控和抓取的解决方案。

风险在于，eBPF 数据收集可能会变成日志和指标的消防水管，当用户试图分析事件或进行调试时，这些日志和指标可能会让用户不知所措。[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) (OTel) 等资源可用于在完全实施可观测性解决方案之前帮助确定数据的上下文。OTel 是一套用于收集可观测性数据的标准实践，在组织和减少 eBPF 生成的大量数据涌入方面发挥着关键作用。

[Elastic](https://www.elastic.co/observability?utm_content=inline+mention) 将 [Elastic profiling agent](https://thenewstack.io/otel-elastic-collaborate-to-make-observability-more-accessible/) 捐赠给 OTel 项目，使 OTel 的 eBPF 指标和可观测性受益。监控和可观测性提供商 Elastic 致力于以主要方式进一步将 [Elasticsearch 项目与 OTel](https://thenewstack.io/elasticsearch-goes-deep-on-opentelemetry-with-ebpf-donation/) 集成，并将其视为增强用户搜索体验的重要基石。

通过利用 Elasticsearch 对各种数据库和数据类型进行数据搜索和可观测性分析，用户可以受益于其多功能性和稳健性。OTel 在这种集成中发挥着关键作用，它是一个中心组件，能够在各种环境中实现无缝的数据监控和分析，从内核到整个网络。

## eBPF 与安全性

eBPF 在许多（但不是所有）用例中为安全性提供了强大的支持。考虑到某些情况下的开销，最好继续使用 eBPF 收集信息以增强整体可观测性，但安全性的实际实施可能会造成过多的负载。

Isovalent 开源负责人 [Liz Rice](https://www.linkedin.com/in/lizrice/?originalSubdomain=uk) 在 O’Reilly 出版的她的书“[Learning eBPF](https://github.com/lizrice/learning-ebpf)”中写道，安全工具和报告事件的可观测性工具之间的区别在于“安全工具需要能够区分正常情况下预期的事件和表明可能发生恶意活动的事件”。

Rice 在她的书中描述的一个案例是，一个应用程序将数据写入本地文件作为其正常处理的一部分。虽然该应用程序预计会写入 `/home/<username>/< filename`，但 Rice 写道，这种活动“从安全角度来看，你并不感兴趣”。

然而，她补充说，如果应用程序写入 Linux 中许多敏感文件位置之一，用户会希望收到通知：“它不太可能需要修改存储在 `/etc/passwd` 中的密码信息。”

在某些用例中，eBPF 可能看起来可以充当安全功能，但实际上并非如此。在某些情况下，当 eBPF 用于收集安全修复的信息时，甚至可能造成安全漏洞。

正如 Rice 在她的书中引用的那样，在 DEFCON 29 的一次演讲“[Phantom Attack: Evading System Call Monitoring.](https://media.defcon.org/DEF%20CON%2029/DEF%20CON%2029%20presentations/Rex%20Guo%20Junyuan%20Zeng%20-%20Phantom%20Attack%20-%20%20Evading%20System%20Call%20Monitoring.pdf)”中讨论了一个黑客窗口。此外，[seccomp_unotify](https://wiki.linuxfromscratch.org/lfs/ticket/4876?utm_source=chatgpt.com) 的手册页明确指出，“因此，应该绝对清楚的是，seccomp 用户空间通知机制不能用于实施安全策略！”

在 Gartner 的报告“[Hype Cycle for Monitoring and Observability, 2024](https://www.gartner.com/en/documents/5611691)”中，分析师 [Simon Richard](https://www.gartner.com/en/experts/simon-richard) 写道：“eBPF 提高了应用程序的可观测性、安全性和性能。但是，大多数企业不会直接使用 eBPF。技术供应商确实在其产品和服务中使用 eBPF 作为底层技术，以提高在 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 上运行的程序的性能和安全性。

“eBPF 允许技术非常精湛的组织安全快速地更改 Linux。与替代方法（例如使用 Linux 内核模块或向上游提交到 Linux 发行版）相比，这是一个进步。”

Gartner 建议“技术非常精湛的组织”可以从 eBPF 中受益，以实现可观测性，这表明其采用和应用可能会带来挑战，尤其是在需要内部 eBPF 专家团队直接检测 eBPF 的情况下。

[Solo.io](https://solo.io?utm_content=inline+mention) 开源负责人兼 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) 技术监督委员会成员和大使 [Lin Sun](https://thenewstack.io/author/lin-sun/) 告诉 The New Stack：“我不认为供应商应该盲目地采用 eBPF。供应商应该根据技术的技能和可用性，选择最适合解决他们所面临的问题的方案。”

正如 Gartner 指出的那样，eBPF 很困难，需要技术技能和知识才能直接实施，尤其是在没有可观测性和安全提供商可能提供的抽象层的情况下。

它在主要云提供商（如 [Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention)、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure 和 [Google Cloud](https://cloud.google.com/?utm_content=inline+mention)）提供的超大规模服务中的部署对用户来说仍然很大程度上是透明的。虽然 eBPF 现在通常用于任何可观测性提供商的产品中，但获得可操作的见解取决于它在何处应用于可观测性。

对于[服务网格](https://thenewstack.io/introduction-to-service-mesh/)，最好使用合适的替代方案。Sun 说，对于 Kubernetes 上的服务网格的可观测性和安全性，依赖 iptables 规则可能更有意义。

她说：“当我们用 eBPF 替换 iptables 时，我们没有观察到太多改进，这样做可能会引入额外的要求。”