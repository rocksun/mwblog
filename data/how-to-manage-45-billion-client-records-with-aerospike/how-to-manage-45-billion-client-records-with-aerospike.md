
<!--
title: 如何使用Aerospike管理450亿条客户记录
cover: https://cdn.thenewstack.io/media/2024/06/c91ac4d6-aerospike-storage-06-adjust.png
-->

上周在 Aerospike 的实时数据峰会上，Adjust 的 Bubunyo Nyavo 解释了该公司如何使用 Aerospike 来帮助客户跟踪其营销渠道的投资回报率。

> 译自 [How To Manage 45 Billion Client Records With Aerospike](https://thenewstack.io/how-to-manage-45-billion-client-records-with-aerospike/)，作者 Joab Jackson。

当您的运营超出单个数据库的能力时，您有哪些选择？

对于总部位于柏林的移动测量服务提供商 [Adjust](https://www.adjust.com/) 来说，答案来自 [Aerospike](https://aerospike.com?utm_content=inline+mention)，这是一个实时、高性能的 NoSQL 键值存储，可以在多个数据中心运行。

在 Aerospike 上周举办的 [实时数据峰会](https://www.realtimedatasummit.com/) 上，Adjust 高级软件工程师 [Bubunyo Nyavo](https://www.linkedin.com/in/bubunyonyavor/?originalSubdomain=de) 解释了该公司如何使用 Aerospike 来帮助客户跟踪其营销渠道的投资回报率。

Adjust 的服务平均每分钟可以生成 5200 万个请求。这些请求可能会触发某种操作的需要，例如查询，当然还有协调状态。客户可能会在 Meta、LinkedIn 或其他社交媒体平台上发布内容，而 Adjust 会收集查看内容的人数以及点击内容的人数。

“根据操作类型，我们会获取一些数据，写入一些数据。有时我们会批量写入，有时会删除数据，然后我们会返回这些请求的响应，”Nyavor 说。

总的来说，该公司在 [Aerospike](https://thenewstack.io/from-db2-to-real-time-with-aerospike-founder-srini-srinivasan/) 中保存了大约 450 亿条记录，这些记录只是记录了设备的状态。平均每条记录 512 字节，这些数据总计 351TB。

数据存储在三个独立的集群中，这些集群位于地理位置分散的数据中心。每个集群有 64 个节点，运行在裸机上，使用 [Gentoo Linux](https://www.gentoo.org/) 作为操作系统。每台服务器大约有 400GB 的 RAM 和 16TB 的 [NVMe 磁盘空间](https://thenewstack.io/why-nvme-is-a-better-choice-for-your-data-center/)，以及一张 10 千兆网络卡。数据备份有两到三份。

“这样，如果一个机架离线，也不会让我们陷入困境，”Nyavor 说。

![显示连接到 Aerospike 的设备平均数量的图表。](https://cdn.thenewstack.io/media/2024/06/498a9684-aerospike-storage-06-adjust-05-1024x587.png)
显示连接到 Aerospike 的设备平均数量的图表。

## 超越键值存储

Aerospike 键值存储 [于 2009 年推出](https://thenewstack.io/from-db2-to-real-time-with-aerospike-founder-srini-srinivasan/)（最初名为 CitrusLeaf），并在在线广告行业迅速找到了受众，用于存储和随后快速分析客户 [cookie](https://thenewstack.io/improving-price-performance-lowers-infrastructure-costs/)。

后续版本 [扩展了分析功能](https://thenewstack.io/aerospike-gets-sql-powered-by-starburst/)，[整合了批处理功能](https://thenewstack.io/latest-aerospike-update-supports-large-scale-data-models/)，并引入了 [二级索引和跨数据中心复制](https://thenewstack.io/aerospike-database-6-secondary-index-queries-json-and-more/)。

在实时数据峰会上，Aerospike 高级开发者体验工程师 [Art Anderson](https://www.linkedin.com/in/artdanderson/) 讨论了 Aerospike 如何也能处理图形和向量数据格式，这可以帮助在线商店轻松构建推荐系统。

对于 Adjust 来说，低延迟至关重要。客户希望数据尽可能接近实时更新。考虑到跨集群通信，这是一个挑战。

与任何具有重复数据的分布式系统一样，Adjust 必须在数据的一致性和可用性之间进行权衡（[CAP 定理](https://thenewstack.io/acid-transactions-change-the-game-for-cassandra-developers/) 的三个支柱中的两个）。

在一致性模式下，始终会提供准确的数据，尽管这可能需要一些时间。在可用性优先模式下，数据将尽快返回给请求者，但可能不包含最新的更改（因为将新数据传播到不同的集群需要时间）。

![Aerospike 的操作模式：一致性和可用性。](https://cdn.thenewstack.io/media/2024/06/e736a74e-aerospike-storage-06-adjust-01-1024x581.png)
Aerospike 的操作模式：一致性和可用性。

“您将获得快速响应，但无法保证数据的最新程度，”Nyavor 解释说，尤其是在 Adjust 写入磁盘的数据量远远大于读取的数据量的情况下。
有几种工具可以提供帮助。Aerospike 提供了一个 [智能客户端驱动程序](https://download.aerospike.com/download/client/)，它知道将请求发送到集群中的哪些节点。数据库系统还允许 Adjust 在快速的固态硬盘上存储二级索引，这是一个优势，因为在服务器自己的主内存中存储它们将是成本高昂的。

“Aerospike 的表现足够好，可以帮助我们利用更便宜的硬件，”Nyavor 说。

总的来说，该系统平均每秒可以执行约 120 万次写入操作和 200 万次 *获取* 操作。

![Aerospike 每秒操作次数在 Adjust 中。](https://cdn.thenewstack.io/media/2024/06/ea38688d-aerospike-storage-06-adjust-02-1024x579.png)

Nyavor 说，大约 50% 的请求在 500 毫秒或更短的时间内完成，考虑到数据库本身的庞大规模，这是一个令人印象深刻的壮举。

![Aerospike 在 500 毫秒内完成的操作（图表）。](https://cdn.thenewstack.io/media/2024/06/6c50f4d1-aerospike-storage-06-adjust-03-1024x590.png)

扫描是较大的操作之一。当用户请求或客户离开程序时，需要删除用户记录。扫描整个集群大约需要三天时间。

“这是一个缓慢而密集的过程，因为它需要大量资源来扫描，”他说。好消息是 Aerospike 可以将扫描操作作为后台任务运行，并在需要执行读写操作时暂时暂停它们。

## 如何升级 Aerospike
根据 Nyavor 的说法，Aerospike 仍然有一些工作要做。

例如，升级过程仍然非常依赖人工操作。

该过程涉及查看更改日志，以确保升级过程中没有出现任何问题。

但总的来说，该数据库非常可配置，你需要了解所有选项才能充分利用它，Nyavor 说。

如果你不知道什么，就问。Aerospike 支持团队在回答问题方面非常有帮助，他补充道。

“不要把文档中你不理解的任何东西视为理所当然，因为它可能会雪球般地滚下来，最终让你自食其果，”他说。
