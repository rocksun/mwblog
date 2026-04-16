<!--
title: 13分钟完成Postgres到Iceberg的数据同步：Supermetal对比Flink、Kafka Connect和Spark
cover: https://cdn.thenewstack.io/media/2026/04/aeed84f1-barsrsind-tks30xc8m2u-unsplash-scaled.jpg
summary: 本文对比了Supermetal与Flink、Kafka Connect、Spark在Postgres到Iceberg同步中的表现。Supermetal凭借优化的CDC源和阶段感知配置，在13分钟内完成任务，性能远超传统工具。
-->

本文对比了Supermetal与Flink、Kafka Connect、Spark在Postgres到Iceberg同步中的表现。Supermetal凭借优化的CDC源和阶段感知配置，在13分钟内完成任务，性能远超传统工具。

> 译自：[Postgres to Iceberg in 13 minutes: How Supermetal compares to Flink, Kafka Connect, and Spark](https://thenewstack.io/postgres-iceberg-cdc-benchmarks/)
> 
> 作者：Yaroslav Tkachenko

Supermetal 最近增加了 [Iceberg 接收端支持](https://supermetal.io/blog/iceberg-target)，我想尝试一下。几个月前，[我测试了新发布的 Kafka 接收端](https://supermetal.io/blog/cdc-benchmark-supermetal-debezium-flink)，所以你可以把这篇博文看作是该系列文章的延续。

我希望将 Supermetal 与向 Iceberg 写入数据的典型开源工具进行比较：Kafka Connect、Flink 和 Spark。我的目标是测量一个真实的端到端管道：从 [Postgres](https://thenewstack.io/why-ai-workloads-are-fueling-a-move-back-to-postgres/) 获取数据并将其写入 Iceberg。

这些工作负载通常用于数据归档，因此我不想关注延迟比较——延迟要求通常非常灵活。相反，我主要关注快照阶段的吞吐量。

为了使比较标准化，我没有测试横向扩展场景。我想了解单个节点（在测试中分配相同的资源）可以提供多少吞吐量。

**Supermetal 在 13 分钟内完成了快照。Flink 花费了 90-116 分钟，Kafka Connect 花费了 120 分钟，而 Spark 花费了超过 3 小时。**

正如我们将在下面看到的，CDC [性能是最大的瓶颈](https://thenewstack.io/why-your-apps-biggest-performance-bottleneck-might-be-ssl-tls/)，至少对于 Flink 和 Kafka Connect / Debezium 是这样。此外，大多数工具将源和接收端完全解耦：这是一个值得遵循的伟大架构原则。Supermetal 的方法非常独特：Iceberg 写入器可以根据 CDC 源阶段（快照 vs. 实时）在配置选项之间切换。我不会称之为耦合；它更接近于[某些数据库中发现的](https://datafusion.apache.org/blog/2025/09/10/dynamic-filters/)“侧向信息传递”（sideways information-passing）技术。

*披露：这项工作由 Supermetal 赞助。所有基准测试均由我在自己的 AWS 账户中执行。所有数据和发现均按原样分享。*

## 测试设置

![Postgres 到 Iceberg 数据管道对比图](https://cdn.thenewstack.io/media/2026/04/70222467-12.jpg)
> “CDC 性能是最大的瓶颈，至少对于 Flink 和 Kafka Connect / Debezium 是这样……大多数工具将源和接收端完全解耦：这是一个值得遵循的伟大架构原则。Supermetal 的方法非常独特：Iceberg 写入器可以根据 CDC 源阶段切换配置选项。”

我使用了比例因子 (SF) 为 50 的 TPC-H 数据集。如果你不熟悉它，它由 8 张不同大小的表组成。在 SF=50 时，最大的表 (lineitem) 有 3 亿行，第二大的表 (orders) 有 7500 万行，依此类推。

在基础设施方面，我使用了：

*   AWS RDS Aurora Postgres 16 Serverless，最大 48 ACU。
*   AWS MSK 3.9，带有 3 个 express.m7g.xlarge 代理。
*   使用 m8i.xlarge 节点（4 CPU 核心，16 GB RAM）的 AWS EKS 1.34。
    *   所有工作负载几乎只使用单个节点（配置为请求 3 CPU 核心和 13 GB RAM）。Flink TaskManager 使用了 4 个任务插槽。Debezium Iceberg 接收端连接器使用了 4 个任务。Spark 只有一个执行器并使用了所有可用资源。
*   Iceberg 表由 AWS Glue 和 AWS S3 驱动。

以下是测试中使用的版本：

*   最新的 Supermetal 构建版本（由 Supermetal 团队提供 Docker 镜像）。
*   使用 Flink Kubernetes Operator 1.13 部署的 Flink CDC 3.5.0 和 Flink 1.20。
*   使用 Strimzi Operator 0.51.0 部署的 Debezium 3.4.3.Final 和 Kafka Connect 4.1.1。
*   使用 Spark Kubernetes Operator 0.8.0 部署的 Spark 4.1.1。
*   Flink、Kafka Connect 和 Spark 都使用了 Iceberg 1.10.1 连接器。

[Supermetal](https://supermetal.io/) 支持 [Postgres CDC 源](https://docs.supermetal.io/docs/main/sources/pg/) 和 [Iceberg 接收端](https://docs.supermetal.io/docs/main/targets/iceberg/)。

与 Kafka Connect 不同，Supermetal 不依赖 Kafka 或任何形式的外部编排器：数据可以直接从源传输到接收端（带有可选的对象存储缓冲）。

我选择使用 JSON 配置文件部署 Supermetal（非常适合容器化工作负载）。配置文件仅描述源和接收端。以下是完整的 Postgres 到 Iceberg 管道的样子：

```json
{
    "connectors": [
        {
            "id": "pg_to_iceberg",
            "source": {
                "postgres": {
                    "connection": {
                        "host": "$POSTGRES_HOST",
                        // rest of the connection details
                    },
                    "replication_type": {
                        "logical_replication": {}
                    },
                    "catalog": {
                        "name": "default",
                        "schemas": [
                            {
                                "name": "public",
                                "tables": [
                                    {"name": "lineitem"},
                                    // rest of the table names
                                ]
                            }
                        ]
                    }
                }
            },
            "sink": {
                "iceberg": {
                    "catalog": {
                        "glue": {
                            "warehouse": "s3://$ICEBERG_S3_BUCKET/",
                            "region": "$AWS_REGION"
                        }
                    },
                    "target_namespace": ["$ICEBERG_GLUE_NAMESPACE"],
                    "write_mode": {
                        "merge_on_read": {}
                    }
                }
            },
            "disabled": false
        }
    ]
}
```

这就是完整的管道，不需要更多配置！你甚至不需要显式指定表名；它们可以在运行时自动发现。

Iceberg 接收端支持不同的编目（包括 REST、AWS Glue 和 AWS S3 Tables），你可以选择支持 Iceberg V1、V2 或 V3。更高级的配置选项包括追加（Append）与读时合并（Merge on Read）、Parquet 目标文件大小和压缩。

最后，Supermetal 会根据当前阶段自动调整文件刷新配置：

*   在快照阶段，它使用配置的目标文件大小（默认为 512 MB）。这确保了快照阶段的文件足够大，甚至不需要合并（compaction）。
*   在实时 CDC 阶段，启用“flush\_interval\_ms”配置（默认为 10 秒），让你可以轻松控制端到端延迟。

这是一个非常独特的功能！其他工具在 Iceberg 接收端级别并没有真正区分生命周期阶段（快照 vs 实时 CDC）；CDC 和其他连接器是完全解耦的。

### 结果

Supermetal 仅用了 13 分钟就同步了所有数据！以下是底层 S3 存储桶的 BytesUploaded 指标：

![S3 存储桶的 BytesUploaded 图表](https://cdn.thenewstack.io/media/2026/04/8153ff39-1-1024x445.png)

测试期间 CPU 和内存保持在相当低的水平：

![CPU 和内存利用率图表](https://cdn.thenewstack.io/media/2026/04/74828bcf-2-891x1024.png)

你可以看到 Supermetal 使用的内存不超过分配内存的 5%！无需考虑调优。快照阶段受益于表间和表内的并行化。

注意：Supermetal 在快照期间使用仅追加（append-only）模式！在此阶段它不跟踪表级键或执行去重。

最大表 (lineitem) 的文件大小看起来很理想，与指定的 Parquet 目标大小一致：

![显示每个 parquet 文件大小的表格](https://cdn.thenewstack.io/media/2026/04/373de8f4-3-1024x224.png)

## Flink

[Apache Flink](https://github.com/apache/flink) 支持 Postgres CDC 连接器（通过 [Flink CDC](https://github.com/apache/flink-cdc)）以及 [Iceberg 连接器](https://iceberg.apache.org/docs/latest/flink/)。我们可以结合这些连接器，将数据直接从 Postgres 写入 Iceberg。

我们也可以在中间使用 Apache Kafka：首先将 CDC 数据捕获为一组主题，然后消费这些主题并写入 Iceberg。对于 Kafka Connect 和 Spark，我们实际上必须遵循这种方法。但由于在 [Flink 的情况下可以避免使用 Kafka](https://thenewstack.io/why-python-data-engineers-should-know-kafka-and-flink/) 并直接写入数据，我们将实现这一点。

Iceberg 连接器文档建议使用 Flink SQL 来定义表。然而，这带来了一些缺点：

*   所有表架构都必须显式定义。
*   最重要的是，每个 Postgres 到 Iceberg 的表组合都是一个单独的 SQL 语句，必须为每个表创建。多亏了语句集（Statement Sets），它们可以在同一个 Flink 管道中执行，但这仍然有很多样板代码。
    *   如果我们采用这种方法，我们需要为**每个表源分配一个复制插槽**。这非常浪费且无法扩展。

然而，Iceberg 连接器带有一个强大的功能，称为 [动态接收端 (Dynamic Sink)](https://iceberg.apache.org/docs/latest/flink-writes/#flink-dynamic-iceberg-sink)。它允许你注册单个接收端并动态地将数据路由到不同的表。它还处理表注册和架构演变。

DynamicRecord 是动态接收端中的核心原语：

```java
DynamicRecord record = new DynamicRecord(
    TableIdentifier.of(glueDatabase, tableName),
    "main",
    tableDef.schema(),
    rowData,
    PartitionSpec.unpartitioned(),
    distributionMode,
    WRITE_PARALLELISM
);
```

它用额外的路由元数据封装了 Flink 的 RowData。

另一个重要的注意事项是，Flink Iceberg 接收端仅在检查点（checkpoint）期间刷新数据。这意味着 Flink 检查点间隔成为控制刷新大小的主要方式。

### 结果

我启动了一个**启用了 upsert** 的 Flink 作业，但没有进行任何调优，检查点间隔为 30 秒。它花了大约 **3.5 小时**才完成！

经过调查，我意识到在[之前的博文](https://supermetal.io/blog/cdc-benchmark-supermetal-debezium-flink)中发现的问题在这里仍然高度相关：即使 Iceberg 接收端非常高效，缓慢的 CDC 源仍会影响整体吞吐量。

因此，我不得不首先将获取大小（fetch size）和分割大小（split size）从 1024 和 8096 分别增加到 5000 和 50000，然后分别增加到 8000 和 80000。再往上调就会导致内存溢出问题。这些选项控制从底层数据库检索数据的速度。

我还将 Flink 检查点间隔增加到 5 分钟。

应用于 Iceberg 接收端的任何调优（例如更改分发模式）似乎都没有帮助。

优化后的版本在不到两小时内完成。以下是底层 S3 存储桶的 BytesUploaded 指标：

![Flink S3 的 BytesUploaded 图表](https://cdn.thenewstack.io/media/2026/04/38a262de-4-1024x410.png)

CPU 和内存使用率很高，但并不可怕：

![Flink S3 的 CPU 和内存使用图表](https://cdn.thenewstack.io/media/2026/04/3b59d6f8-5-879x1024.png)

Parquet 文件大小非常零散：

![Flink S3 的 Parquet 文件大小](https://cdn.thenewstack.io/media/2026/04/27b267c5-6-1024x235.png)

很难精确控制它们：虽然有一个“write.target-file-size-bytes”配置，但看起来文件创建主要由检查点间隔控制。

我禁用了 upsert 并切换到仅追加模式。此版本的作业在 1.5 小时内完成。

![仅追加模式下的 BytesUploaded 图表](https://cdn.thenewstack.io/media/2026/04/57ee223d-7-1024x318.png)![仅追加模式下的 CPU 和内存利用率图表](https://cdn.thenewstack.io/media/2026/04/e0aa704b-8-845x1024.png)

生成的 Parquet 文件看起来整齐得多：

![仅追加模式下的 Parquet 文件大小](https://cdn.thenewstack.io/media/2026/04/d1482b41-9-1024x200.png)

## Kafka Connect

[Kafka Connect](https://kafka.apache.org/42/kafka-connect/overview/) 也支持 Postgres CDC 连接器（通过 [Debezium](https://debezium.io/)）和 [Iceberg 连接器](https://iceberg.apache.org/docs/latest/kafka-connect/)。但 Kafka Connect 依赖于使用 Kafka 作为中间层。

我使用的 Iceberg 连接器配置如下：

```yaml
topics: debezium.public.lineitem, # 其余主题

# 将 Debezium 封装转换为 CDC 格式并设置用于路由的 _cdc.target
transforms: debezium
transforms.debezium.type: org.apache.iceberg.connect.transforms.DebeziumTransform
transforms.debezium.cdc.target.pattern: ${env:ICEBERG_GLUE_DATABASE}.{table}

# 编目 (AWS Glue)
iceberg.catalog.catalog-impl: org.apache.iceberg.aws.glue.GlueCatalog
iceberg.catalog.warehouse: s3://${env:ICEBERG_S3_BUCKET}/
iceberg.catalog.io-impl: org.apache.iceberg.aws.s3.S3FileIO

# 表设置
iceberg.tables.dynamic-enabled: true
iceberg.tables.route-field: _cdc.target
iceberg.tables.auto-create-enabled: true

# 提交协调
iceberg.control.topic: iceberg-control
iceberg.control.commit.interval-ms: 300000
```

“dynamic-enabled”和“route-field”选项实现了类似于 Flink 动态接收端的行为：多亏了 DebeziumTransform 暴露的额外元数据，数据可以自动路由到不同的表。

提交间隔设置为 5 分钟，与 Flink 检查点间隔相同。

当前版本的连接器似乎不支持 upsert。

我怀疑 CDC 源在这里也会是最大的瓶颈（事实证明确实如此）。因此我也对 Debezium 源进行了一些调优，主要是增加 linger.ms 和 batch.size（直到我开始收到 MESSAGE\_TOO\_LARGE 错误）。

### 结果

Kafka Connect 连接器花了大约两个小时完成。以下是底层 S3 存储桶的 BytesUploaded 指标：

![Kafka Connect 的 BytesUploaded 图表](https://cdn.thenewstack.io/media/2026/04/dd188f65-10-1024x349.png)

在整个运行过程中 CPU 占用特别高：

![Kafka Connect 的 CPU 和内存利用率](https://cdn.thenewstack.io/media/2026/04/640f3e5f-11-1024x1024.png)

CPU 瓶颈令人担忧，但分析（profiling）并没有显示任何可疑之处：

![Kafka Connect 的 CPU 分析图表](https://cdn.thenewstack.io/media/2026/04/dff82aca-12-1024x578.png)

它看起来在源端（CDC 处理、JSON 序列化）和接收端（JSON 反序列化、Parquet 写入）之间分布相当均匀。

底层的 Parquet 大小分布良好：

![Kafka Connect 的 Parquet 文件大小](https://cdn.thenewstack.io/media/2026/04/b11ea65f-13-1024x220.png)

## Spark

[Apache Spark](https://spark.apache.org/) 没有像 Flink 或 Kafka Connect 那样的一流 CDC 连接器。因此，为了构建一个完整的 Postgres 到 Iceberg 管道，我使用带有 Debezium 连接器的 Kafka Connect 将 Postgres 表捕获为 Kafka 主题。然后 Spark 作业从 Kafka 消费数据并写入 Iceberg。[Spark 对 Iceberg 有很好的支持](https://iceberg.apache.org/docs/latest/spark-getting-started/)，因为它是最早支持它的工具之一。

不幸的是，Spark 不支持（Flink 中的）动态接收端概念或（Kafka Connect 中的）基于字段的路由。当涉及写入多个接收端时，我们有几个选择：

*   foreachBatch：一个特殊的算子，让你精确控制批次写入。你可以在网上找到许多例子；然而，[Databricks 不建议](https://docs.databricks.com/aws/en/structured-streaming/foreach#write-to-multiple-locations)使用它来写入多个接收端。
*   每表一个查询方法：虽然不是“真正的”路由，但这是一个足够好的解决方法。我们只需在启动期间迭代输入主题列表，并为每个表启动一个流式查询。

每表一个查询的方法会创建一系列如下查询：

```java
Dataset<Row> raw = spark.readStream()
    .format("kafka")
    .options(kafkaOptions)
    .option("subscribe", topic)
    .option("startingOffsets", "earliest")
    .load();

Dataset<Row> result = … // 数据解析和处理

result.writeStream()
    .format("iceberg")
    .outputMode("append")
    .trigger(Trigger.ProcessingTime(triggerIntervalMs))
    .option("checkpointLocation", checkpointBase + "/" + table.name())
    .toTable(fullTableName);
```

### 结果

我只专注于对作业的 Spark 部分进行负载测试，即从 Kafka 到 Iceberg。

我首先尝试了 foreachBatch 方法；然而，它花了超过 4 小时。

我切换到了每表一查询的方法，并开始迭代调优：

*   增加 Kafka 消费者设置（max.poll.records、fetch.max.bytes 等），以减少从 Kafka 获取数据时进行多次轮询的开销。
*   调整 maxOffsetsPerTrigger。设置得太低，会导致产生许多小文件（带来额外开销）；设置得太高，会导致整个主题分区变成一个批次。
*   触发器、批次缓存、优化解析和过滤、内存、shuffle 分区……

尽管我付出了所有努力，表现最好的运行也花了 3 小时 20 分钟。以下是底层 S3 存储桶的 BytesUploaded 指标：

![显示 Kafka 的 BytesUploaded 指标图表](https://cdn.thenewstack.io/media/2026/04/a494720b-14-1024x423.png)

执行器 CPU 保持在相当低的水平：

![Kafka 的 CPU 和内存使用情况](https://cdn.thenewstack.io/media/2026/04/c057e381-15-873x1024.png)

我将这种性能水平归功于 Spark 的架构：它是为大规模横向扩展基础设施设计的，在只有几个核心的单个执行器上运行非常吃力。八个独立的查询（每个主题一个）竞争 4 个任务插槽，每个查询还要支付各自的检查点和 Iceberg 提交开销。

底层的 Parquet 大小看起来很均匀（主要由 maxOffsetsPerTrigger 控制）：

![Kafka 的 Parquet 文件大小](https://cdn.thenewstack.io/media/2026/04/29134308-16-1024x180.png)

## 数据正确性

我验证了所有工具都能正确同步数据，没有丢失或重复。Postgres 和 Iceberg 之间的所有表计数都匹配。

> “Supermetal 在没有任何调优的情况下，快照性能至少提高了 7 倍。我主要归因于非常快速的 CDC 源以及极低的序列化/反序列化开销。”

我还抽查了实际数据，只注意到列顺序的细微差别和额外的元数据列。

## 总结

以下是最佳测试运行的最终对比：

| 工具 | 总耗时 (分钟) | 调优工作量 | 提交频率 | 写入模式 | 具体配置细节 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Supermetal** | **13** | **无需调优** | 10s 刷新 (仅限实时 CDC) | 仅追加 (快照) / 读时合并 (实时) | 开箱即用配置。目标文件大小 512 MB (默认)。针对低延迟实时变更进行了高度优化。 |
| **Flink** | 116 | 手动调优 | 5 分钟 (检查点) | Upsert | 检查点间隔从 30s 增加。获取大小 8k，分割大小 80k (比默认增加)。 |
| **Flink** | 90 | 手动调优 | 5 分钟 (检查点) | 仅追加 | 与 upsert 运行相同的调优，但没有主键跟踪/去重开销。 |
| **Kafka Connect** | 120 | 手动调优 | 5 分钟 | 仅追加 | 需要仔细调整连接器配置。`linger.ms` 和 `batch.size` 针对稳定性和吞吐量进行了调优。此标准设置不支持 Upsert。 |
| **Spark** | 200 | 手动调优 | 触发间隔 / maxOffsetsPerTrigger | 仅追加 | 仅从预先填充的 Kafka 主题消费 (无快照)。主要调优涉及优化结构化流作业的 `maxOffsetsPerTrigger`。 |

Supermetal 在没有任何调优的情况下，快照性能至少提高了 7 倍。我主要归因于其非常快速的 CDC 源以及极低的序列化/反序列化开销。在[另一项基准测试](https://supermetal.io/blog/cdc-benchmark-supermetal-debezium-flink)中，较慢的 CDC 源已被确认为 Flink 和 Debezium 的问题。

此外，Supermetal 能够端到端地区分快照和实时 CDC 阶段，从而实现接收端级别的优化，例如在快照期间使用仅追加模式和目标文件大小进行滚动，并在实时 CDC 阶段切换到读时合并模式和基于时间的间隔。

Flink 紧随其后，但它需要非常激进的调优。Flink 和 Kafka Connect 都提供了将源数据动态路由到多个 Iceberg 表的方法；而 Spark 则需要为每个表创建单独的查询。

最后，我想指出本次测试侧重于单节点性能。当然，大多数其他工具都可以横向扩展（所有的 Iceberg 接收端；在 CDC 方面，目前只有 Flink 提供此功能）。但这可能会很快变得非常昂贵。Supermetal 也可以在一定程度上横向扩展，例如将单个表作为扩展单元。