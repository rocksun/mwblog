<!--
title: P99 CONF揭示的五个数据库性能权衡秘密
cover: https://cdn.thenewstack.io/media/2026/10/b257c733-steve-a-johnson-td85e3w3w6i-unsplash-scaled.jpg
summary: 本文通过P99 CONF大会的五场技术演讲，探讨了各大数据库系统在存储设计、I/O优化、向量检索、分布式扩展及云原生客户端开发中所面临的性能瓶颈与权衡取舍。
-->

本文通过P99 CONF大会的五场技术演讲，探讨了各大数据库系统在存储设计、I/O优化、向量检索、分布式扩展及云原生客户端开发中所面临的性能瓶颈与权衡取舍。

> 译自：[What five P99 CONF talks reveal about database trade-offs](https://thenewstack.io/p99-conf-database-tradeoffs/)
> 
> 作者：Doug Sillars

**P99 CONF是一个聚焦于高性能、低延迟应用的虚拟会议**。其2026年度大会于[10月21日至22日](https://p99conf.io/agenda/)举行。在此，我们将介绍其[60多场](https://p99conf.io/session/how-scylladb-eliminates-read-amplification-at-scale/)演讲中的五场。注册后可在 p99conf.io 按需观看演讲录像。

数据库存储设计在[读放大](https://slatedb.io/docs/design/overview/)、写放大和空间放大（RUM 猜想）之间寻求平衡。根据工作负载和配置的不同，优化其中一项可能会加剧另一项。以下五场演讲展示了工程师们如何在不同的数据库系统中做出这些权衡。

## **Almog Gavra**，Responsive（现已被 Databricks 收购）联合创始人

Gavra 围绕读放大（每个结果读取的数据量）、写放大（每次逻辑写入写入的数据量）以及空间放大（相对于实时数据的存储占用）来构建数据库设计。日志有利于快速写入，但会增加读取负担；有序数组则恰恰相反。正如 Gavra 所说：“我将 LSM 树视为在极端之间进行调优的机制。”

LSM 最初是为本地磁盘构建的，但它们的[不可变文件](https://slatedb.io/blog/introducing-slatedb/)也非常适合对象存储。Gavra 指出了 Amazon S3 较低的存储成本、持久性和可用性，同时也指出了其权衡之处：对象必须被替换而不是编辑，每个 GET 和 PUT 都有成本，冷读取速度较慢。在他的例子中，本地 NVMe 缓存未命中的耗时约为 150 微秒，而 S3 Standard 则需要 20 到 30 毫秒——大约相差两个数量级。LSM 将写入批处理到不可变文件中；缓存有助于让对象存储读取远离热路径。

Gavra 的 [SlateDB](https://slatedb.io/) 是一个开源的、原生的对象存储 LSM 库。它在 S3、GCS 和 R2 等存储之上公开了键值接口，因此开发人员无需实现自己的 LSM 即可构建数据系统。

**Michael Litvak**（高级软件工程师）和 **Felipe Cardeneti Mendes**（技术总监），ScyllaDB

ScyllaDB 的演讲探讨了 [Logstor](https://www.scylladb.com/2026/07/06/scylladb-vs-aerospike-wide-column-vs-key-value/)，这是一个面向读密集型键值工作负载的可选存储引擎，并非旨在取代其现有的 LSM 引擎。对于每个键，内存索引存储哈希以及记录在闪存上的位置。读取操作可以返回缓存的值，或者通过一次磁盘 I/O 找到记录，从而避免了跨 SSTables、布隆过滤器和索引数据结构的 LSM 搜索。使用任一引擎的表都可以在同一个集群中运行，并使用 ScyllaDB 现有的驱动程序和一致性选项。

演讲者的初步读密集测试维持了每秒 110 万次读取，p99.9 延迟低于 1 毫秒，p99.99 延迟约为 1.5 毫秒。该测试使用了 2 KB 的值；演讲中早期的 LSM 示例使用了 1 KB 的值，因此结果不能直接进行比较。他们还报告说，在 80% 读取、20% 写入的工作负载中，吞吐量相近，且 p99.9 延迟低于 1 毫秒。

Logstor 通过更大的 RAM 内存索引和更多的写入开销来换取这些读取性能。即使是小的更新也会将完整的最新值写入日志，使旧记录变成死空间；段压缩稍后会对其进行回收。演讲者将其定位用于有界的键集、频繁覆盖以及允许额外内存开销的点查询。在演讲中，Mendes 将这种权衡称为“以牺牲空间为代价优化时间”。

**Madelyn Olson**，AWS 首席软件工程师

并非所有瓶颈都在存储端。Olson 从遇到突发 p50 延迟峰值的 Amazon ElastiCache 客户切入，随后测试了 Valkey 主执行线程达到极限的情况。

在 Olson 的无流水线 GET 基准测试中，拥有约 300 万个键和 650 个客户端，p50 延迟在接近每秒 150,000 次请求时急剧上升。Valkey 已经拥有[I/O 线程](https://valkey.io/blog/valkey-8-0-0-rc1/)，但在主线程执行命令时，它们却处于空闲状态。该团队使用无锁队列来保持网络 I/O 和命令解析在这些线程上活跃，同时将命令执行保留在主线程上。

Olson 报告称，在该工作负载下，新的上限约为每秒 120 万次请求——大约是先前阈值的八倍。（这是该演讲针对特定工作负载的结果，而非通用的吞吐量保证。）

为了实现水平扩展，Valkey 9.0 引入了原子的[槽迁移](https://valkey.io/blog/atomic-slot-migration/)。源分片保留所有权，同时向目标流式传输快照及后续更改，一旦目标追赶上，便转移所有权。Olson 表示，在大约 40 GB、3 到 4 个分片的测试中，无负载下的运行速度快了约 10 倍，在重度 GET 工作负载下快了约 5 倍。如果在交接前迁移失败，可以中止阶段性传输，而不会丢失最终用户数据。

随着工作负载需求的变化，可以添加或删除 I/O 线程。Olson 的运营建议是：使用水平扩展来应对基准容量，使用垂直扩展来应对短时突发，同时目前仍将命令执行保持在单线程。她的指导原则是：“效率胜过头条数字。”

**Nathan VanBenschoten**，turbopuffer 首席架构师

VanBenschoten 描述了 turbopuffer 在 1,000 亿个向量规模下的搜索索引，这些向量代表了超过 200 TiB 的稠密向量数据。该公司报告称，在每秒超过 1,000 次查询的情况下，p99 延迟为 200 毫秒，早期结果的召回率为 92%。对象存储是持久的后端存储，但这种高查询率的工作负载将其数据固定在本地 [SSD 缓存](https://marketplace.turbopuffer.com/blog/ann-v3)中。分层聚类将邻近的向量分组；[RaBitQ](https://p99conf.io/session/searching-100b-vectors-on-object-storage-200ms-p99/) 二进制量化将影子索引缩小到每个维度一位，从而允许在重排使用全精度向量的小型子集之前缩小候选范围。

未压缩的搜索受限于将向量从存储移动到内存所需的带宽。量化将更多的工作转移到更高的缓存层级中，但也增加了算术密度，使系统受到 CPU 限制。

“通常当你打破一个瓶颈时，新的瓶颈就会出现，”VanBenschoten 说道。这为团队提供了不同的优化目标，包括更高效的向量指令。

为了在 SSD 上容纳如此大的索引，turbopuffer 将其拆分到多台机器上。VanBenschoten 表示，其分离的计算与存储架构倾向于采用更少、[更大的分片](https://p99conf.io/session/searching-100b-vectors-on-object-storage-200ms-p99/)：替换机器可以指向对象存储并填充其本地缓存，而不是从另一个节点接收完整的分片。查询会分发到各个分片，协调器则合并它们的顶级结果。

**Georg Kreuzmayr**，TigerBeetle 软件工程师

TigerBeetle 是一个金融交易数据库。在这场演讲中，Kreuzmayr 描述了“对角扩展”的概念：将热数据保留在本地 NVMe 上，同时将存储层级扩展到共享对象存储以存放冷数据。

发生故障的机器不需要重建已存储在对象存储中的数据。作为规模说明，他估计通过 100 Gbps 网络恢复 128 TB 大约需要三个小时的线速时间；如果恢复时间长于故障间隔时间，集群可能会进入故障螺旋。

该设计需要一个与 TigerBeetle 的单核交易处理兼容的对象存储客户端。Kreuzmayr 提到 AWS C++ SDK 中阻塞的 `getaddrinfo` 调用是一个不匹配点：在该核心上的调用会停滞交易工作。SDK 线程池、运行时分配和依赖关系也与该项目的设计目标相冲突。

因此，TigerBeetle 构建了自己的多云客户端，而不是适配官方 SDK。它支持 S3、Azure 和 GCP，并且可以通过模拟 I/O 和注入故障进行测试。

该客户端使用 Zig 编写，包含自定义的 DNS、TLS 和 HTTP 组件，使用了 `[io\_uring](https://p99conf.io/session/the-fastest-object-storage-client-in-the-world/)` 和零拷贝发送，并在启动时分配其工作内存。Kreuzmayr 表示，该实现的代数不到 40,000 行，除了其工具链之外没有其他依赖项。这些选择遵循了 TigerStyle 的三个原则：安全性、性能和开发体验。

在演讲的 S3 `PutObject` 测试中——在 AWS `c7gn.metal-24xlarge` 实例上进行无校验和的纯 HTTP 8 MB 请求——Kreuzmayr 报告上传速度比官方 SDK 快约 20 倍，比研究实现快 5 倍。对于 `GetObject`，他报告的吞吐量约为 SDK 的 3 倍，比研究实现快约 25%。他将较小的下载增益归因于云 TCP 接收路径。这些是针对所述测试设置的结果。会议将更广泛的客户端比较总结为比官方 GCP 和 AWS SDK 快 [4–10](https://p99conf.io/session/the-fastest-object-storage-client-in-the-world/) 倍。

Kreuzmayr 的核心体会是，构建客户端需要更多的前期工作，但使代码更容易测试和调正如他所说，“代码不再是技术债，最终成为了资产。”