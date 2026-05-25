<!--
title: Jaeger 如何利用 ClickHouse 达成 1000 万个 Span 的 8.6 倍压缩率
cover: https://cdn.thenewstack.io/media/2026/05/711a2e46-kyunghee-yim-dwrac_e0fpi-unsplash-scaled.jpg
summary: 本文介绍了Jaeger v2.18原生集成ClickHouse作为存储后端的实践。通过优化主键设计与物化视图，其在千万级数据基准测试中实现了8.6倍的压缩率与极速查询性能。
-->

本文介绍了Jaeger v2.18原生集成ClickHouse作为存储后端的实践。通过优化主键设计与物化视图，其在千万级数据基准测试中实现了8.6倍的压缩率与极速查询性能。

> 译自：[How Jaeger hit 8.6× compression on 10 million spans with ClickHouse](https://thenewstack.io/jaeger-clickhouse-storage-backend/)
> 
> 作者：Mahad Zaryab

作为 [Jaeger](https://www.jaegertracing.io/) 的维护者，在过去几年里，我一直看到用户不断请求对 [ClickHouse](https://clickhouse.com/) 的支持。在 Jaeger v2.18.0 中，我们终于实现了这一功能。最让我兴奋的不单单是 ClickHouse 的可用性，而是它的架构实际上是为大规模遥测数据量身定制的。它能吞吐海量的、仅追加（append-only）的写入流，并在几毫秒内处理复杂的分析聚合，为团队提供了一个高效且生产级的存储后端。

对于刚接触该项目的人来说，Jaeger 是一个毕业于云原生计算基金会（CNCF）的[分布式追踪](https://thenewstack.io/distributed-tracing-sampling-opentelemetry/)平台，旨在监控复杂微服务并对其进行故障排查。它跨服务边界追踪请求，以暴露延迟瓶颈和根本原因，从而最终缩短团队的平均修复时间（MTTR）。通过原生集成 ClickHouse，Jaeger 现在可以利用列式存储，为数十亿个 Span 提供极快的查询性能和高比例的数据压缩。

在本文中，我将解释为什么 [ClickHouse](https://thenewstack.io/vector-search-without-the-lock-in-why-devs-like-clickhouse/) 是存储追踪数据的理想选择、其底层模式（Schema）是如何设计的，以及你今天如何开始在 Jaeger 中使用它。

## 为什么列式存储更胜一筹

从本质上讲，追踪问题包含两个方面：一是存储海量的半结构化事件数据，二是跨多个维度（服务、操作、标签、持续时间、时间范围和 Trace ID）快速搜索这些数据。Cassandra 和 Elasticsearch 为 Jaeger 社区提供了很好的服务，但它们也带来了运维成本。索引开销增加了延迟和费用，扩展变得复杂，保留策略的决定也迫使人们做出痛苦的权衡。

### 高吞吐量写入与低延迟查询

ClickHouse 是一款列式 [OLAP 数据库](https://thenewstack.io/how-to-run-olap-and-oltp-together-without-resource-contention/)，专门为解决这些限制而设计：高吞吐量写入、强力压缩和快速分析查询。对于追踪而言，这几乎是理想的选择。追踪数据本质上是重复的——相同的服务名称、操作名称、状态码和标签会一遍又一遍地出现。列式布局正是在这种重复性中大放异彩。

> “追踪数据本质上是重复的——相同的服务名称、操作名称、状态码和标签会一遍又一遍地出现。列式布局正是在这种重复性中大放异彩。”

### 真正有意义的压缩

我们测量了追踪数据上显著的压缩收益。像 “auth-service” 或 “payment-gateway” 这样的服务名称会出现数十万次。操作名称、标签键和状态码也是如此。在行式数据库中，这种冗余是无法压缩的。而在列式数据库中，ClickHouse 会将相同的值分组，使其极易被压缩。结果如何？在我们的基准测试中，spans 表实现了 8.6 倍的压缩率。

### 实时分析

ClickHouse 还为对追踪数据进行更复杂的分析查询打开了大门。由于在列式存储上进行聚合非常高效，Jaeger v2.18 包含了原生 ClickHouse SPM 方法，可以直接从存储的 span 中计算服务级延迟、调用率和错误率。这使团队能够直接从其追踪数据中生成微服务的核心健康和性能指标，而无需外部指标管道。

## 设计 Schema 模式

Schema 设计是事情变得棘手的地方。我们需要针对 Jaeger 的核心查询模式进行优化：通过 Trace ID、服务和操作进行 Trace 查找；属性过滤；时间范围查询；以及支持[服务性能监控 (SPM)](https://www.jaegertracing.io/docs/2.17/architecture/spm/) 功能的聚合。这些约束并不总是朝同一个方向作用。

Ha Anh Vu 之前写过一篇非常优秀的[文章](https://medium.com/jaegertracing/making-design-decisions-for-clickhouse-as-a-core-storage-backend-in-jaeger-62bf90a979d)，对 Jaeger v1 的 ClickHouse Schema 进行了基准测试，那项工作奠定了基础。然而，Jaeger v2 采用了 OpenTelemetry 数据模型，这迫使我们重新审视几个决定。

设计空间在[架构决策记录 (ADR)](https://github.com/jaegertracing/jaeger/blob/v2.18.0/docs/adr/008-clickhouse-storage-schema.md) 中有详细记载。以下章节将带您了解一些值得理解的关键决策。

### 主键的折衷方案

在 ClickHouse 中，主键并不是唯一性约束。相反，它定义了磁盘上的排序顺序，并支持稀疏索引（每 8,192 行粒度一个索引）。选择主键是该 Schema 中最具杠杆效应的单一决策。

我们有两个选择主键的候选方案：

1. **针对 Trace 检索进行优化**：按 `trace_id` 排序。一个 Trace 的每个 span 都会落在一个连续的块中，因此 GetTrace 是一次寻道 + 顺序读取。然而，搜索查询需要为此优化付出代价，因为 `service_name` 和 `operation_name` 过滤器完全无法使用主键索引。
2. **针对搜索进行优化（已采纳）**：按 `(service_name, name, start_time)` 排序。按服务、操作和时间窗口过滤的搜索查询将直接转换为主键（primary-key）查找。

这一决策归结于一种非对称的权衡。按 `trace_id` 排序会使搜索性能变得极差，但按 `(service_name, name, start_time)` 排序对 Trace 检索的影响要小得多，因为我们可以通过两种低成本机制恢复大部分丢失的性能：

1. 在 `trace_id` 上构建 `bloom_filter` 跳数索引，这使得引擎无需读取即可证明某个粒度（granule）不能包含给定的 ID。
2. 一个 `trace_id_timestamps` 物化视图，用于告诉搜索路径每个匹配的 Trace 的时间范围，以便后续的 `GetTraces` 调用可以剪裁分区和粒度。

早期使用按 `trace_id` 排序的 Schema 进行的基准测试运行清楚地显示了这种非对称性。Trace 检索大约需要 27 毫秒，但搜索查询大约需要 880 毫秒。重新按 `(service_name, name, start_time)` 排序将 Trace 检索推迟到大约 100 毫秒（虽然变慢了，但仍远低于交互式阈值），同时将多过滤器搜索降低到大约 140 毫秒。

### 存储有类型的属性

在 Jaeger v1 中，标签总是字符串。v2 读取器 API 接收一个有类型的 Map，其中属性可以是 Bool、Int64、Float64、String 或复杂类型之一（Bytes、Slice、Map）。我们需要跨这些类型进行查询，因此存储层不能将所有内容都折叠为字符串。

该 Schema 利用了 ClickHouse 的 [Nested](https://clickhouse.com/docs/sql-reference/data-types/nested-data-structures/nested) 列，每种原始类型一个，并在 span、event、link、resource 和 scope 级别重复。可以将其视为每行内部的一个迷你表；每个表都可以有自己的一组属性名称和值。这种方法让属性过滤器能够使用与查询常规表相同的查询语义。

然而，值得注意的是，仅针对属性的搜索本质上更为昂贵，因为它们无法充分利用 ClickHouse 的主键索引。该表的索引围绕顶级结构化字段（特别是 `service`、`operation` 和 `time`）进行了优化。为了获得最佳的查询性能并防止繁重的列扫描，用户应始终将属性过滤器与这些字段结合使用，以限制 ClickHouse 必须扫描的数据量。

### 物化视图

Jaeger 的某些查询不符合 spans 表的排序顺序。例如，Jaeger UI 需要快速加载已知服务名称和操作的完整列表，而 Trace 搜索通常需要高效访问 Trace 时间范围。

我们没有使用高昂的表扫描来解决这些问题，而是使用物化视图来预先计算数据。在 ClickHouse 中，[物化视图](https://clickhouse.com/docs/materialized-view/incremental-materialized-view)会自动将对源表的插入进行转换，并将结果写入优化后的目标表中。

这种方法用于加速服务名称、操作和 Trace ID 时间戳范围的查询。

### 五个层级的属性

从 span 的 Schema 中可能无法立即看出一个技术挑战：存储层如何解释属性查找。例如，在搜索 `http.status_code=200` 时，系统无法自然地区分 “200” 是字符串、整数、span 级属性还是 resource 级属性。根据服务的不同，同一个逻辑键可能会被分类在 `str_attributes` 或 `int_attributes` 下，并且它可能存在于五个数据层级（resource、scope、span、event 或 link）中的任何一个。

为了解决这个问题，我们维护了一个专用的 [attribute_metadata](https://github.com/jaegertracing/jaeger/blob/v2.18.0/internal/storage/v2/clickhouse/sql/create_attribute_metadata_table.sql) 表，该表由 spans 表的物化视图填充。这允许读取器在查询时查找过滤键，并仅查询已观测到的类型和层级的列。

## 大规模下的 Span 吞吐量

我们在单节点部署上使用分布在 100 万个 Trace 中的 1000 万个 span 对 ClickHouse 后端进行了基准测试。该基准测试测量了写入吞吐量、压缩率、Trace 检索以及过滤搜索延迟。

后端在写入期间持续保持超过 50k spans/秒的吞吐，在 spans 表上实现了 8.6 倍的压缩率，并将磁盘上的 span 数据减少了近 6 GiB，降至约 722 MiB。Trace 检索平均约为 100 毫秒，而大多数搜索查询保持在 50 毫秒以下。更复杂的过滤查询在大约 140 毫秒内完成。

> “后端在写入期间持续保持超过 50k spans/秒的吞吐，在 spans 表上实现了 8.6 倍的压缩率，并将磁盘上的 span 数据减少了近 6 GiB，降至约 722 MiB。”

这些数据令人鼓舞，但应在基准测试环境和数据集的背景下进行解读。完整的分析方法、配置和查询细节可在[基准测试报告](https://github.com/jaegertracing/jaeger/blob/main/internal/storage/v2/clickhouse/BENCHMARKING.md)中找到。

### 开始使用

从 Jaeger v2.18.0 开始，ClickHouse 支持作为 Alpha 阶段的存储后端提供。您需要一个正在运行的 ClickHouse 实例以及 ClickHouse 后端的 Jaeger v2配置。详细说明请参见[安装指南](https://www.jaegertracing.io/docs/2.18/storage/clickhouse/)。

迄今为止，作为 Jaeger 维护者是我职业生涯中最有成就感的一部分。如果您想就这项工作进行交流、做出贡献或报告问题，请在 [GitHub](https://github.com/jaegertracing/jaeger/issues) 上提交 Issue，或者在 CNCF 的 #jaeger Slack 频道中找到我们。