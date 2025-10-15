如果您了解 P99 CONF，您可能已经迫不及待地想参加 P99 CONF 2025。它将于 10 月 22 日和 23 日在您的浏览器上首次亮相，议程中将有许多新演讲者以及一些长期以来的热门演讲者。

如果您还不熟悉 P99 CONF，它是一个为期两天的免费社区活动，专注于性能和低延迟工程。它特意以虚拟方式举行，具有高度互动性和深度技术性。今年，您可以期待来自 Clickhouse、Gemini、Arm、NVIDIA、Pinterest、Rivian/Volkswagen、Meta、Wayfair、Disney、Turso、Neon、PlanetScale、ScyllaDB 等众多公司的第一手工程经验，在此无法一一列举。

P99 CONF 2025 仅剩几天（稍后将详细介绍），我们认为现在是分享 P99 CONF 2024 中最受关注的一些会议的好时机。您还可以在[点播库](https://www.p99conf.io/on-demand/)中一次性观看 200 多个低延迟技术讲座（免费，无限制）。

*[注册 P99 CONF，免费且虚拟](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000Xo0mc&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202025-10-22%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack)*

## 低延迟模式

**Pekka Enberg (Turso 联合创始人兼首席技术官)**

Pekka Enberg 在他的演讲中以一个令人不安的想法开头：“延迟无处不在。”但幸运的是，Enberg 从数据库工程师和“[延迟”书籍](https://lp.scylladb.com/latency-book-offer)作者的角度，对延迟进行了深入思考。这可能就是为什么 Enberg 能够在短短 30 分钟内，提供关于如何查找、测量和消除延迟的极其全面的概述。

Enberg 首先探讨了延迟为何重要，尾部延迟为何比大多数人想象的影響更大，以及平均延迟为何基本没有意义。此处特别提到了协调遗漏的陷阱，这是基于 Gil Tene 在 P99 CONF 过去的主题演讲 “[痛苦指标与后果](https://thenewstack.io/if-p99-latency-is-bs-whats-the-alternative/)” 中提出的观点。

接下来，Enberg 分享了三种消除延迟的方法：避免数据移动、避免工作和避免等待。移动字节不可避免地需要时间，因此共置、复制或缓存可以提供帮助。减少工作通常是最大的胜利。选择正确的算法，在热路径中避免动态内存分配，不要让繁重的同步或操作系统阻碍您的进展。即使是上下文切换这样微小的事件也会损害尾部延迟。

如果无法进一步降低延迟，那么是时候隐藏它了。Enberg 介绍了并行处理请求、跨服务器对冲请求和使用轻量级线程等实用策略。他最后提醒大家，系统调优也很重要：CPU 扩展、交换和中断处理等因素可能会决定您的延迟。核心信息是：测量尾部，从各个角度进行攻击，并将[低延迟](https://thenewstack.io/high-performance-on-a-low-budget/)作为一流的设计目标。

VIDEO

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

## 实现低（延迟）

**Benjamin Cane (American Express 杰出工程师) 和 Tyler Wedin (American Express 全球支付网络站点可靠性工程师副总裁)**

American Express 支付网络团队最近完成了一个为期四年的项目，旨在改造该公司的银行卡支付平台。该系统必须足够快，能够以低延迟和极高弹性处理大量的全球分布式交易。它还需要足够灵活，以便团队能够根据支付行业不断变化的需求迅速调整。

Cane 和 Wedin 阐述了将以前的单体系统拆分为分布式服务所带来的挑战：增加的网络跳数、跨区域延迟、对有状态设备的依赖以及无数蚕食性能和可用性的“小问题”。

他们通过基于单元的架构、数据本地性以及基于 HTTP/2 的服务间通信解决了瓶颈。每个单元都是自主的，拥有自己的 Kubernetes 集群、数据和支持服务。这样，交易就可以在本地处理，而无需跨区域跳数。数据通过三种方法（按偏好顺序）进行分发：用于静态值的预加载直读缓存、用于最终一致性的复制以及在需要强一致性时的事务亲和性。服务调用通过服务网格 (Envoy) 转向 HTTP/2 以平衡负载，并通过使用直接、安全的 Pod 到 Pod 通信来减少对有状态设备的依赖。

学到的主要教训是什么？用 Cane 的话来说：“要获得低延迟，您必须关注本地性：走最直接的路径。要获得低延迟，您必须限制您的依赖。提前将数据推送到您的单元或节点，以便在事务需要时数据就在那里。您还需要使用异步通信而不是同步通信。最重要的是，您必须将延迟和弹性作为平台的一流特性。这正是我们从一开始就做的。我们定义了 SLA [服务级别协议]，设定了低于这些 SLA 的目标，并将其作为平台的核心部分。如果延迟没有达到预期，我们就会停止开发列车并修复它。”

VIDEO

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

## Golang 中的十亿行挑战

**Shraddha Agrawal, Ceph, IBM 高级软件工程师**

Go 到底能跑多快？这正是 Shraddha Agrawal 在她对 [十亿行挑战 (1BRC)](https://www.morling.dev/blog/one-billion-row-challenge/) 的方法中试图发现的。如果您去年错过了，1BRC 旨在有趣地探索现代 Java 在聚合文本文件中 10 亿行数据方面能被推到什么程度。但它的创建者 Gunnar Morling 也期望它“能吸引十几个左右的人”。最终，数百人使用 Go、Rust、C/C++、C#、Fortran，甚至数据库实现了这一挑战——因此这个项目在各个方面都超出了预期。

额外福利：Morling 还在 P99 CONF 2024 上发表了主题演讲，[分享了最快的 1BRC 解决方案](https://www.p99conf.io/session/1brc-nerd-sniping-the-java-community/)处理挑战的 13 GB 输入文件所用的技巧，耗时不到两秒。

从一个幼稚的零并发基线实现开始，Agrawal 测量了解析和聚合数据需要六分钟的运行时。在此基础上，她使用 Go [性能工具指导每个优化步骤](https://thenewstack.io/optimize-database-performance-by-capitalizing-on-the-cpu/)。通过生成约 10,000 个 goroutine（每个城市一个）引入并发，将时间缩短到约 4.5 分钟，但也暴露了通道和调度器开销。从无缓冲通道切换到有缓冲通道，批量处理行并重新思考数据结构带来了渐进式改进。她通过用整数运算替换浮点运算并仅存储 min/max/sum/count 而非完整值列表，同时削减了时间和内存成本。

精益的 MapReduce 风格设计又节省了几秒钟。文件以 64 MB 的块读取，由九个 worker goroutine 并行解析，并由一个 reducer 合并成摘要映射。一个生产者向它们提供数据，这意味着总共只有 10 个 goroutine。这使得通道流量从 1000 万个项目减少到 512 个，并将执行时间缩短到 28 秒。

在视频中，Agrawal 将通过火焰图、工具提示和一路走来学到的经验教训，一步一步地带您完成整个旅程。

VIDEO

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

## 使用 eBPF 和 Netkit 实现零开销容器网络

**Liz Rice, Isolvant（现为思科一部分）首席开源官**

在容器中运行应用程序会带来惊人的网络开销。100 千兆以太网上的基准测试显示，直接在主机上运行的应用程序可以达到接近线速的性能。然而，一旦它们被容器化，吞吐量就会下降到约三分之二。这正是 P99 CONF 的常客 Liz Rice 在她 P99 CONF 2024 的演讲中讨论的问题。

Rice 将吞吐量下降归因于两个主要原因。首先，数据包两次通过网络堆栈。其次，TCP 反压导致套接字缓冲区限制超出，从而导致数据包丢失和吞吐量受限。

接着，她展示了 eBPF 如何绕过主机的上层网络堆栈。Linux 5.10 中新增的辅助函数（`bpf_redirect_peer` 和 `bpf_redirect_neigh`）可以更有效地在命名空间之间重定向数据包。这使得吞吐量更接近原生主机性能：在她的基准测试中约为 90 千兆比特。通过 TCX（对 eBPF 程序在网络堆栈中附加方式的重做），可以获得额外的改进。

Rice 的下一步是 Linux 6.6 中引入的 netkit 设备。这些最小的、可进行 BPF 编程的设备取代了虚拟以太网连接并消除了积压队列。它们还允许在应用程序线程的上下文中重定向数据包。这在吞吐量和延迟方面都带来了好处：容器化应用程序的网络性能与直接在主机上运行的应用程序相匹配。

最后，Rice 展示了这些进步已经集成到 Cilium 中，使得在最新内核上实现零开销容器网络成为可能。

VIDEO

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

## DB/OS 爱恨情仇的下一章

**Andy Pavlo, 卡内基梅隆大学副教授**

这位演讲者为此次演讲提供了一个相当丰富多彩且全面的摘要。我们认为我们的解读无法完全体现其精髓——所以，就如 Pavlo 所说，原文在此：

“数据库管理系统 (DBMS) 是美丽、自由奔放的软件，它们只想尽快帮助用户存储和访问数据。为了实现这一目标，DBMSs 几十年来一直不惜一切代价试图避开操作系统 (OS)。这种规避是必要的，因为操作系统总是试图通过虚假的系统调用语义、不可伸缩的内核级数据结构和过多的数据复制来将自己的意愿强加于 DBMSs 并扼杀它们的雄心。

“许多通过内核旁路方法或自定义硬件来避开操作系统的尝试，其工程/研发成本如此之高，以至于很少有 DBMSs 支持它们。最终，DBMSs 陷入了一种虐待关系：它们需要操作系统来运行其软件并为其提供基本功能（例如，内存分配），但它们不喜欢操作系统对待它们的方式。然而，像 eBPF 这样的新技术允许 DBMSs 在 OS 内核中安全地运行自定义代码以覆盖其功能，这有望颠覆这种权力斗争。

“在这次演讲中，我将介绍一种名为‘用户旁路’的新设计方法，用于使用 eBPF 构建高性能数据库系统和服务。我将讨论与 DBMS 社区相关的 eBPF 最新进展，以及 DBMS 的哪些部分最适合使用它。我将介绍 BPF-DB 的设计，这是一个用 eBPF 编写的嵌入式 DBMS，它在多版本数据上提供 ACID 事务，并完全在 Linux 内核中运行。”

VIDEO

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

## 加入 P99 CONF 2025 社区

就像 P99 CONF 社区一样，P99 CONF 团队也无法停止优化和调优。这就引出了 P99 CONF 2025。以下是议程的一部分：

*   Alexey Milovidov：“Clickhouse 的 C++ 和 Rust 之旅”
*   Chip Huyen：“LLM 推理优化”
*   Sanchay Javeria：“使用 Apache Flink 构建 Pinterest 流媒体应用”
*   Saahil Khurana, Marcus Kim：“Rivian 带有巨型过滤器的推送通知子流”
*   Cristian Velazquez：“让 Uber 的 P99 保持在 1ms 以下的内存优化技术”
*   Geoffrey Blake：“使用 APerf 在干草堆中寻找性能之针”
*   Tanel Poder：“使用 eBPF 实现高效、始终在线的线程级可观测性”
*   Glauber Costa：“我们为什么[用 Rust 重写 SQLite](https://thenewstack.io/why-we-created-turso-a-rust-based-rewrite-of-sqlite/)”
*   AJ. Stuyvenberg：“我们如何用 Rust 重建 Datadog Lambda 扩展”
*   Christian Schwarz：“重构 Neon IO 堆栈：Rust+tokio+io\_uring+O\_DIRECT”

如果您对这些演讲以及关于 AI/ML、分布式数据系统、Kubernetes 和可观测性的更多技术讨论感兴趣，请加入我们，享受大量的学习和技术乐趣。

*[注册 P99 CONF，免费且虚拟。](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000Xo0mc&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202025-10-22%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack)*