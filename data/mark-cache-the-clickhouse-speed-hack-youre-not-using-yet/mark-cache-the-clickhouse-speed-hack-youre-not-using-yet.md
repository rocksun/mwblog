
<!--
title: Mark Cache：你还没用上的ClickHouse速度秘诀
cover: https://cdn.thenewstack.io/media/2025/06/166b35cb-abstract.png
summary: ClickHouse提速秘诀：用好Mark Cache！作为内存驻留优化，它通过缓存MergeTree表中granules的marks，加速数据访问，尤其在高并发场景下效果显著。通过调整`mark_cache_size`，监控`system.events`和`system.asynchronous_metrics`，平衡多层缓存，可显著提升查询速度和资源效率。
-->

ClickHouse提速秘诀：用好Mark Cache！作为内存驻留优化，它通过缓存MergeTree表中granules的marks，加速数据访问，尤其在高并发场景下效果显著。通过调整`mark_cache_size`，监控`system.events`和`system.asynchronous_metrics`，平衡多层缓存，可显著提升查询速度和资源效率。

> 译自：[Mark Cache: The ClickHouse Speed Hack You’re Not Using (Yet)](https://thenewstack.io/mark-cache-the-clickhouse-speed-hack-youre-not-using-yet/)
> 
> 作者：Anil Inamdar

对于从事高吞吐量分析工作负载的开发人员和工程师来说，[ClickHouse](https://www.instaclustr.com/support/documentation/clickhouse/) 已经成为一种 [首选的在线分析处理 (OLAP) 数据库](https://thenewstack.io/clickhouse-rapidly-rivals-other-open-source-databases-in-active-contributors/)。它速度快、重量轻、开源，并且专为大规模实时性能而构建。但是，[最大限度地发挥 ClickHouse 的潜力](https://thenewstack.io/vector-search-without-the-lock-in-why-devs-like-clickhouse/) 需要比默认配置更多的工作。如果你的团队依赖 ClickHouse 来支持仪表板、流处理或即时分析，那么有一个关键的内部机制值得调整：mark cache（标记缓存）。

Mark cache 在某种程度上仍然被忽视，但它在 ClickHouse 如何实现高性能方面发挥着基础性作用，尤其是在查询大型数据集时。如果使用得当，它可以缩短查询时间、减少磁盘 I/O 并提高工作负载的整体响应能力。

## 什么是 Mark Cache？

从本质上讲，mark cache 是一种内存驻留优化，用于 ClickHouse 如何访问存储在其 MergeTree 表中的数据。ClickHouse 将数据存储在压缩文件中，每个文件都分成“granules”（最小的可检索单元）。这些 granules 由“marks”（标记）索引，或者说是元数据指针，告诉 ClickHouse 每个 granule 在压缩文件中的起始位置。因此，ClickHouse 可以直接跳到它需要的数据，而无需扫描或解压缩整个文件来满足查询，前提是它可以访问相关的 marks。

这就是 mark cache 的用武之地。它将这些 marks 存储在内存中，因此当执行查询时，ClickHouse 可以立即定位和访问相关的数据块，从而绕过代价高昂的文件操作。如果所需的 marks 不在缓存中，ClickHouse 必须读取和解析文件的各个部分才能找到它们，从而减慢执行速度。

## 为什么 Mark Cache 对实际性能至关重要

在重复或高并发工作负载下，mark cache 的效果变得尤为明显，例如每隔几秒刷新一次的仪表板、点击 ClickHouse 以填充用户指标的 API 或跨时间窗口执行聚合的流数据管道。这些都是重复访问相同列和数据范围的场景。

每当发生这种情况时，mark cache 都会帮助 ClickHouse 短路冗余工作。它可以最大限度地减少从磁盘读取的数据量，避免不必要的解压缩，并保持内存操作的紧凑性和可预测性。

即使超越了纯粹的速度，mark cache 也有助于提高资源效率。通过限制数据访问的范围，它可以帮助避免过多的 CPU 周期，并减少磁盘或网络连接存储上的争用。最终结果是更快的查询、更少的系统负载，以及最终用户和依赖及时洞察的应用程序的更好体验。

## 为你的工作负载调整 Mark Cache

ClickHouse 不会自动为你的特定需求调整 mark cache。你需要配置它。关键变量是 `mark_cache_size`，它设置 ClickHouse 将分配用于存储 marks 的最大内存量。这不是一刀切的。太小，你的缓存会不断地清除有用的 marks，导致更多的缓存未命中。太大，你可能会使操作系统、文件系统缓存或其他 ClickHouse 组件资源不足。

要正确调整它的大小，首先要了解你的数据布局。具有许多部分的大的 MergeTree 表需要缓存更多的 marks。这意味着更高的内存要求。针对宽表的频繁查询，或者只访问少数列但经常访问的查询，将从充足的 mark cache 中获益更多。

查询模式也起着关键作用。如果用户或应用程序经常重复类似的查询（或者如果分析仪表板驱动重复的访问模式），则 marks 被重用的机会会大大增加。在这些情况下，将更多内存投入到 mark cache 中可以产生强大的性能投资回报。

最后但并非最不重要的一点是，评估可用的总系统内存。ClickHouse 的性能取决于 mark cache、未压缩缓存和操作系统级别缓存的组合。使其中任何一个资源不足都会损害整体性能。调整 mark cache 的大小必须结合你的更广泛的系统配置来完成。在 [Instaclustr](https://www.instaclustr.com/)，我们在生产部署中看到的是，积极监控和根据工作负载行为调整 mark cache 的团队看到了可衡量的收益——不仅在速度方面，而且在系统可靠性和资源效率方面也是如此。

## 可观测性以监控命中和未命中

一旦启用了标记缓存并确定了大小，下一步就是可观测性。您需要跟踪您的查询从缓存中受益的频率，以及它们错过并回退到磁盘访问的频率。

ClickHouse 通过 `system.events` 和 `system.asynchronous_metrics` 表提供可见性。

这些内部表公开了有用的计数器，例如：

```sql
SELECT metric,value FROM system.asynchronous_metrics WHERE metric LIKE'Mark%'
```

这揭示了标记缓存的命中和未命中情况，帮助您了解缓存是否真正提供了实际价值。高未命中率可能表明您的缓存大小不足，或者您的查询过于多样化而无法从缓存中受益。
您还可以使用以下命令监控整体内存使用情况：

```sql
SELECT formatReadableSize(value) AS mark_cache_usage
FROM system.asynchronous_metrics
WHERE metric = 'MarkCacheBytes';
```

如果您正在使用像 [Grafana](https://grafana.com/) 或 [Prometheus](https://prometheus.io/) 这样的可观测性工具，这些指标可以被导出和可视化，以提供对缓存性能的实时洞察。可以配置警报，以便在命中率降至阈值以下或内存消耗过高时发出警告。

## 不要孤立地进行调整

另一个非常常见的错误是将标记缓存视为一个独立的调整旋钮。事实并非如此。在 ClickHouse 中进行有效的性能调整意味着平衡多个缓存层，包括标记缓存、未压缩缓存和操作系统的页面缓存。如果您优化了标记缓存但忽略了其他缓存，性能瓶颈可能会在其他地方重新出现。

最好的方法是整体性的。使用可观测性来跟踪所有缓存层。了解您的内存是如何划分的。进行增量更改并衡量它们的影响，不仅要考虑缓存命中率，还要考虑整体查询延迟和系统负载。

## 小改变带来巨大成果
标记缓存不是 ClickHouse 中最引人注目的功能，但这正是它如此强大的原因。只需进行一些调整和定期监控，它就可以以最小的努力释放主要的性能改进。

对于在生产环境中扩展 ClickHouse 的工程团队来说，调整标记缓存可能是良好性能和卓越性能之间的区别，尤其是在实时分析是业务核心的情况下。无论您是提供指标仪表板、支持产品分析还是启用流数据管道，标记缓存都是一个值得使用的 ClickHouse 功能。