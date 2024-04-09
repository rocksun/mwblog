
<!--
title: 从Postgres到 ScyllaDB NoSQL速度提升349倍
cover: https://cdn.thenewstack.io/media/2024/03/73155a6d-speed.png
-->

Coralogix 如何将查询处理时间从 30 秒缩短至 86 毫秒——以及对其使用 WebAssembly 和 Rust 进行的后续优化的一瞥。

> 译自 [From Postgres to ScyllaDB NoSQL, with a 349x Speed Boost](https://thenewstack.io/from-postgres-to-scylladb-nosql-with-a-349x-speed-boost/)，作者 Cynthia Dunlop。

对于 [Coralogix](https://coralogix.com/) 来说，速度至关重要，这是一个可观测性平台，开发团队信赖它在问题升级为故障之前发现问题。Coralogix 使用实时流分析管道，提供监控、可视化和警报功能，而无需索引。

Coralogix 的一个关键差异化因素是分布式查询引擎，用于对客户在远程存储中的存档中的映射数据进行快速查询。该引擎使用专门的 [Parquet](https://parquet.apache.org/) 格式查询存储在对象存储（Google Cloud Storage、S3）中的半结构化数据。它最初被设计为 [底层对象存储](https://thenewstack.io/storage/) 之上的无状态查询引擎，但在查询执行期间读取 Parquet 元数据会引入不可接受的延迟。为了克服这个问题，该团队开发了一个元数据存储（简称“元存储”），以实现对执行大型查询所需的 Parquet 元数据的更快速检索和处理。

最初的元存储实现[建立在 PostgreSQL 之上](https://thenewstack.io/postgresql-takes-a-new-turn/)，对于公司的需求来说不够快。因此，该团队尝试了一种新的实现——这次使用 ScyllaDB。剧透：它成功了。该团队取得了令人印象深刻的性能提升——将查询处理时间从 30 秒缩短到 86 毫秒。让我们深入了解他们如何实现这一点，以及他们如何计划使用 [WebAssembly](https://thenewstack.io/webassembly/) 用户定义函数 (UDF) 和 [Rust](https://thenewstack.io/microsoft-rust-is-the-industrys-best-chance-at-safe-systems-programming/) 进一步优化它。

## 元存储动机和要求

在深入了解元存储实现细节之前，让我们退一步，看看最初构建元存储的理由。

Coralogix 的首席软件工程师丹·Harris 解释说：“我们最初将此平台设计为底层对象存储之上的无状态查询引擎，但我们很快意识到，在查询执行期间读取 Parquet 元数据的成本占查询时间的很大一部分。”他们意识到，可以通过将其放在一个可以快速查询的快速存储系统中来加快这一速度（而不是直接从底层对象存储中读取和处理 Parquet 元数据）。

他们设想了一个解决方案，该解决方案将：

- 以分解格式存储 Parquet 元数据，以实现高可扩展性和吞吐量
- 使用 bloom 过滤器有效识别要为每个查询扫描的文件
- 使用事务性提交日志以事务方式添加、更新和替换底层对象存储中的现有数据

关键要求包括低延迟、读/写容量和底层存储可扩展性的可扩展性。为了理解所需的极端可扩展性，请考虑以下内容：单个客户每小时生成 2,000 个 Parquet 文件（每天 50,000 个），每天总计 15TB，仅一天的 Parquet 元数据就达到 20GB。

## 初始 PostgreSQL 实现

Harris 承认：“我们从 Postgres 开始了最初的实现，当时我们理解非分布式引擎不足以满足长期需求。”最初的实现存储了关键信息，例如表示一行组和一个 Parquet 文件的“块”。这包括元数据，例如文件的 URL、行组索引和有关该文件的最小详细信息。例如：

```
Block url: 
s3://cgx-production-c4c-archive-data/cx/parquet/v1/team_id=555585/…
…dt=2022-12-02/hr=10/0246f9e9-f0da-4723-9b64-a12346095d25.parquet
Row group: 0, 1, 2 …
Min timestamp 
Max timestamp
Number of rows
Total size
…
```

为了优化读取，他们使用 bloom 过滤器进行高效的数据剪裁。Harris 解释说：“最终，我们希望支持全文搜索之类的功能。基本上，当我们将这些文件导入我们的系统时，我们可以为我们在文件中找到的所有不同标记构建一个 bloom 过滤器。然后，根据特定查询，我们可以使用这些 bloom 过滤器来剪裁我们需要扫描的数据。”

他们将 bloom 过滤器存储在块分割设置中，将其分解为 32 字节块以实现高效检索。它们独立存储，因此系统不必在查询时读取整个 bloom 过滤器。

![](https://cdn.thenewstack.io/media/2024/03/b1677ab7-image1.jpg)

此外，他们还存储了每个 Parquet 文件的列元数据。例如：

```
Block URL
Row Group
Column Name
Column metadata (blob)
```

Harris 解释说：“我们正在写入的文件非常宽，有时多达 20,000 列。因此，通过仅读取我们需要的元数据，我们可以真正减少任何给定查询所需的 IO 量。”

## ScyllaDB 实现

接下来，让我们看看 Harris 的队友、Coralogix 的高级软件工程师 Sebastian Vercruysse 概述的 ScyllaDB 实现。

### 块数据建模

对于新实现，必须重新审视块建模。以下是一个块 URL 的示例：

```
s3://cgx-production-c4c-archive-data/cx/parquet/v1/team_id=555585/…

…dt=2022-12-02/hr=10/0246f9e9-f0da-4723-9b64-a12346095d25.parquet
```


前半部分是客户的顶级存储桶；在存储桶内，项目按小时分区。在这种情况下，应该用什么作主键？

* (Table url)?？但一些客户的 Parquet 文件比其他客户多得多，并且他们希望保持平衡。
* ((Block url, row group))？这唯一标识了一个给定的块，但由于时间戳不在键中，因此很难列出给定日期的所有块。
* ((Table url, hour))？这有效，因为如果您有 24 小时要查询，您可以非常轻松地查询。
* ((Table url, hour), block url, row group)？这就是他们选择的。通过将块 URL 和行组添加为聚类键，他们可以轻松地在小时内检索特定块，这也简化了更新或删除块和行组的过程。

###  bloom 过滤器分块和数据建模

下一个挑战：如何验证某些位已设置，因为 ScyllaDB 没有提供开箱即用的函数来实现这一点。该团队决定读取 bloom 过滤器并在应用程序中处理它们。但是，请记住，他们每天每个客户最多处理 50,000 个块，每个块包含 262KB 的 bloom 过滤器部分。总共 12GB - 对于一次查询来说，将它们全部拉回应用程序中太多了。但他们不必每次都读取整个 bloom 过滤器；他们只需要其中的一部分，具体取决于查询执行期间涉及的令牌。因此，他们最终将 bloom 过滤器分块并拆分为行，这将读取的数据减少到可管理的 1.6 兆字节。

对于数据建模，一种选择是使用 *((block_url, row_group), chunk index)* 作为主键。这将生成每个 bloom 过滤器 8,192 个 32 字节的块，从而以每个分区约 262 KB 的方式均匀分布。由于同一分区中的每个 bloom 过滤器，因此可以使用单个批处理查询轻松插入和删除数据。但有一个影响读取效率的陷阱：您需要知道块的 ID 才能读取 bloom 过滤器。此外，该方法将涉及访问大量分区；50K 块意味着 50K 分区。正如 Vercruysse 所指出的，“即使使用像 ScyllaDB 这样快速的东西，也很难为 50K 分区实现亚秒级处理。”

另一个选择（他们最终决定）：
*((table url, hour, chunk index), block url, row group). *请注意，这与块分区键相同，在分区键中添加了一个索引，该索引表示查询引擎所需的第 n 个令牌。使用这种方法，扫描跨越 24 小时窗口的五个令牌将产生 120 个分区——与以前的数据建模选项相比，这是一个令人印象深刻的改进。

此外，此方法不再需要在读取 bloom 过滤器之前获取块 ID，从而实现更快的读取速度。当然，总是有权衡。在这里，由于采用了阻止 bloom 过滤器的方法，他们必须将单个 bloom 过滤器拆分为 8,192 个唯一分区。与允许一次摄取所有 bloom 过滤器块的先前分区方法相比，这最终限制了摄取速度。但是，在小时内快速读取给定块的能力对他们来说比快速写入更重要，因此他们认为这种权衡是值得的。

### 数据建模难题

毫不奇怪，从 SQL 迁移到
[NoSQL 涉及相当多的数据建模](https://thenewstack.io/nosql-data-modeling-mistakes-that-ruin-performance/) 返工，包括一些反复试验。例如，Vercruysse 分享道，“有一天，我发现我们搞乱了最小和最大时间戳——我想知道我该如何修复它。我想也许我可以重命名列，然后设法让它再次工作。但是，如果它是聚类键的一部分，您不能在这里重命名列。我想也许我可以添加新列并运行
UPDATE 查询以更新所有行。不幸的是，这在 NoSQL 中也不起作用。”

最终，他们决定截断表并重新开始，而不是编写迁移代码。他们在这一方面的最佳建议是第一次就做对。 :-)

### 性能提升

尽管需要进行数据建模工作，但迁移还是得到了很好的回报。对于元存储块列表：

- 每个节点当前处理 4 到 5 TB。
- 他们目前每秒处理大约 10K 次写入，P99 延迟始终低于一毫秒。
- 块列表结果在大约一小时内生成约 2,000 个镶木地板文件；使用 bloom 过滤器，它们在不到 20 毫秒内得到处理。对于 50K 个文件，时间不到 500 毫秒。
- 它们还执行位检查。但是，对于 50K 个镶木地板文件，500 毫秒足以满足其需求。
- 在列元数据处理中，P50 非常好，但存在较高的尾部延迟。Vercruysse 解释说：“问题在于，如果我们有 50K 个镶木地板文件，我们的执行器将并行获取所有这些文件。这意味着我们有许多并发查询，并且我们没有使用最佳磁盘。我们认为这是问题的根源。”

### ScyllaDB 设置

值得注意的是，Coralogix 在短短两个月内从首次发现 ScyllaDB 转变为使用 TB 级数据投入生产（而且这是一次需要数据建模工作的 SQL 到 NoSQL 迁移，而不是更简单的 Cassandra 或 DynamoDB 迁移）。

该实现是用 Rust 编写的，基于 [ScyllaDB Rust 驱动程序](https://www.scylladb.com/2022/02/22/were-porting-our-database-drivers-to-async-rust/)，他们发现 ScyllaDB Operator for Kubernetes、ScyllaDB Monitoring 和 ScyllaDB Manager 在快速过渡中都很有帮助。由于为自己的客户提供低成本的可观察性替代方案对 Coralogix 来说很重要，因此团队对 ScyllaDB 基础设施的良好性价比感到满意：一个三节点集群，具有：

- 8 个 vCPU
- 32 GiB 内存
- ARM/Graviton
- 带有 500 MBps 带宽和 12k IOPS 的 EBS 卷 (gp3)

使用 ARM 可降低成本，而最终决定使用弹性块存储 (EBS) (gp3) 卷则归结为可用性、灵活性以及性价比。他们承认，“这是一个有争议的决定，但我们正在努力使其发挥作用，并且我们将看看我们能管理多长时间。”

## 经验教训

他们在这里学到的关键经验教训：

- **密切关注分区大小**：使用 ScyllaDB 与使用 Postgres 之间最大的区别在于，您必须非常仔细地考虑分区和分区大小。有效的分区和集群键选择对性能有很大影响。
- **考虑读/写模式**：您还必须仔细考虑读/写模式。您的工作负载是读密集型的吗？它是否涉及读写操作的良好组合？或者，它主要是写密集型的吗？Coralogix 的工作负载相当写密集型，因为它们不断摄取数据，但它们需要优先考虑读取，因为读取延迟对业务至关重要。
- **避免使用 EBS**：该团队承认他们被警告不要使用 EBS：“我们没有听从，但我们可能应该听从。如果您正在考虑使用 ScyllaDB，那么最好查看具有本地 SSD 的实例，而不是尝试使用 EBS 卷。”

## 未来计划：使用 Rust 的 WebAssembly UDF

未来，他们希望在编写足够大的块和读取不必要的数据之间找到中间地带。他们将块拆分为大约 8,000 行，并相信他们可以将它们进一步拆分为 1,000 行，这可以加快插入速度。

他们的最终目标是通过利用 [带有 WebAssembly 的用户定义函数 (UDF)](https://thenewstack.io/scylladbs-take-on-webassembly-for-user-defined-functions/)，将更多工作卸载到 ScyllaDB。通过他们现有的 Rust 代码，集成 UDF 将消除将数据发送回应用程序的需要，从而为块调整和潜在增强提供灵活性。

Vercruysse 分享道，“我们已经用 Rust 编写了所有内容。如果我们能够开始使用 UDF，这样我们就无需将任何内容发送回应用程序，那就太好了。这给了我们更多余地来处理块。”

## 观看完整的技术讲座

您可以在 [我们的技术讲座库](https://www.scylladb.com/tech-talk/from-postgres-to-scylladb-migration-strategies-and-performance-gains/) 中观看完整的技术讲座并浏览幻灯片。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。