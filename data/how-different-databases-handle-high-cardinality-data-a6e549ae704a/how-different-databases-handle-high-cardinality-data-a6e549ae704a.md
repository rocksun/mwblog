
<!--
title: 不同数据库处理高基数数据的方式
cover: https://miro.medium.com/v2/da:true/resize:fit:1200/0*3fz34Sd4b1hplCnJ
-->

了解不同数据库如何处理高基数数据，并了解选择正确的索引方案为何如此重要。

> 译自 [How Different Databases Handle High-Cardinality Data](https://medium.com/timescale/how-different-databases-handle-high-cardinality-data-a6e549ae704a)，作者 Team Timescale。

时间序列数据、物联网传感器读数、用户行为日志——这些只是现代系统必须处理的数据流的几个例子。它们的共同点是都倾向于高基数，这给数据存储和分析带来了独特的挑战。随着组织越来越依赖数据驱动的决策，了解不同数据库如何处理高基数数据对于构建高效且可扩展的系统至关重要。

本文将探讨高基数数据带来的挑战，检查旨在处理高基数数据的各种数据库工具，并比较各种方法，以帮助您做出关于数据架构的明智决策。

## 高基数的挑战

高基数指的是数据集中唯一元素的数量，当我们查看现实世界的例子时，这是一个特别具体的概念。想象一下一个跟踪热门网站上用户交互的系统——每个用户可能都有一个唯一的标识符，每个会话都会生成一个唯一的ID，每个交互都会创建一个唯一的事件ID。在大规模应用中，这些唯一值可以迅速达到数百万甚至数十亿。

这种大量唯一值会给数据库系统带来重大挑战。当在具有高基数列的表之间执行连接时，潜在的组合会呈指数级增长。例如，将用户交互数据与会话数据连接可能需要将数百万个唯一的用户ID与数百万个唯一的会话ID进行匹配。由于数据库必须维护和处理这些海量独特的组合，因此生成的运算会迅速压垮系统资源。

在需要完全表扫描的操作中，性能下降尤其严重。当数据库需要跨高基数列分析或聚合数据时，它必须在内存中为每个唯一值维护[不同的计数器](https://www.timescale.com/blog/counter-analytics-in-postgresql-beyond-simple-data-denormalization/)或聚合。这会迅速耗尽可用的内存资源，导致查询执行时间变慢，或者在极端情况下导致系统故障。

阅读本文以[了解更多关于高基数的信息](https://www.timescale.com/blog/what-is-high-cardinality)。

## 数据库解决方案：时间序列数据库InfluxDB和TimescaleDB如何处理高基数

鉴于高基数数据集在时间序列中有多么常见，让我们来看看两个时间序列数据库InfluxDB和TimescaleDB是如何处理这个问题的。

InfluxDB是一个NoSQL数据库，其创建者选择从头开始重建所有内容。相比之下，TimescaleDB是一个SQL数据库，其创建者（即本文作者）选择拥抱并构建在PostgreSQL和已验证的数据结构之上，然后进一步扩展它以用于时间序列、事件和实时分析问题。（顺便说一句，使用正确的扩展，[它还可以推动您的AI应用程序开发](https://www.timescale.com/ai)。）

首先，以下是这两个数据库在数据集基数增加时插入性能的比较。

对于以下比较，我们使用了以下设置：

- TimescaleDB [版本1.2.2](https://github.com/timescale/timescaledb/releases/tag/1.2.2?ref=timescale.com)，InfluxDB [版本1.7.6](https://github.com/influxdata/influxdb/releases/tag/v1.7.6?ref=timescale.com)
- 1台远程客户端机器和1台数据库服务器，两者都在同一个云数据中心
- AWS EC2实例：i3.xlarge（4个vCPU，30 GB内存）
- 4个1 TB磁盘，采用raid0配置（EXT4文件系统）
- 两个数据库都获得了所有可用内存
- 数据集：100-1,000,000个模拟设备每10秒生成1-10个CPU指标，约1亿个读取间隔，约10亿个指标（100个设备一个月间隔；4000个设备三天；100,000个设备三个小时；1,000,000个设备三分钟），[使用时间序列基准套件 (TSBS) 生成](https://github.com/timescale/tsbs?ref=timescale.com) - 用于TimescaleDB (1)和InfluxDB (2)的模式
- 插入时两个数据库都使用了10K批大小
- 对于TimescaleDB，我们根据数据量设置块大小，目标是10-15个块（[更多信息](https://docs.timescale.com/using-timescaledb/hypertables?utm_source=timescale-blog&utm_medium=referral&utm_campaign=influx-benchmark-post&utm_content=seconddocslink#best-practices)）
- 对于InfluxDB，我们启用了[TSI（时间序列索引）](https://docs.influxdata.com/influxdb/v1.6/concepts/tsi-details/?ref=timescale.com)

(1) **TimescaleDB schema:** Table `cpu` (time timestamp, tags_id integer, usage_user double, usage_system double, usage_idle double, usage_nice double, usage_iowait double, usage_irq double, usage_softirq double, usage_steal double, usage_guest double, usage_guest_nice double, additional_tags jsonb); indexes (tags_id, time) and (time, tags_id); Table `tags` (id integer, hostname text, region text, datacenter text, rack text, os text, arch text, team text, service text, service_version text, service_environment text); unique index on all columns


(2) **InfluxDB schema:** Field keys (usage_guest integer, usage_guest_nice integer, usage_idle integer, usage_iowait integer, usage_irq integer, usage_nice integer, usage_softirq integer, usage_steal integer, usage_system integer, usage_user integer), Tag keys (arch, datacenter, hostname, os, rack, region, service, service_environment, service_version, team)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*M-EOK5GNqw4iTpUY)


**注意**：[这里](https://www.timescale.com/blog/timescaledb-vs-influxdb-for-time-series-data-timescale-influx-sql-nosql-36489299877/)可以找到这两个数据库更详细的总体比较。

正如你所看到的，在低基数情况下，两个数据库是可比的（尽管 TimescaleDB 的性能高出 30%）。但随着基数的增加，差异变得相当显著，因为 TimescaleDB 的插入性能下降速度远远慢于 InfluxDB，而 InfluxDB 的性能则急剧下降。在高基数情况下，TimescaleDB 的性能比 InfluxDB 高出 11 倍以上。

这些结果对一些人来说可能并不令人惊讶，因为高基数是 InfluxDB 的一个众所周知的弱点（来源：GitHub、论坛）。

但为什么会这样呢？让我们更仔细地看看这两种数据库的开发情况。


## B-Trees 与TSI：处理高基数的两种不同方法

我们可以将高基数性能的差异追溯到InfluxDB与TimescaleDB在工程决策上的根本不同。


### InfluxDB 和 TSI

由于高基数一直是InfluxDB的一个众所周知的挑战，他们的团队一直在研究一种称为“时间序列索引”（TSI）的东西来解决这个问题。

与他们在其他领域的做法一致，InfluxDB TSI 是一个基于本地日志结构合并树的系统，由各种数据结构组成，包括哈希映射和位集。这包括一个内存中的日志（“LogFile”），当其超过阈值（5 MB）时会定期刷新到磁盘，并且被压缩到一个磁盘上的内存映射索引（“IndexFile”）；一个文件（“SeriesFile”），包含了整个数据库中所有序列键的集合。（在[他们的文档](https://docs.influxdata.com/influxdb/v1.7/concepts/tsi-details/?ref=timescale.com)中有描述。）


TSI 的性能取决于所有这些数据结构的相互作用。然而，由于 TSI 是定制构建的，理解其在各种高基数工作负载下的表现变得难以理解。

TSI 的设计决策也导致了一些具有性能影响的限制：

- [根据InfluxDB的文档](https://docs.influxdata.com/influxdb/v1.7/concepts/tsi-details/?ref=timescale.com)，该总基数限制大约为3,000万（尽管根据上面的图表，InfluxDB在达到该限制之前就已经开始表现不佳），或者远低于物联网（包括我们上面的示例）等时间序列用例中通常所需的数量。
- InfluxDB索引标签但不索引字段，这意味着某些查询无法比全表扫描表现得更好。因此，以我们之前提到的物联网数据集为例，如果想要搜索所有没有空闲内存的行（例如，类似于SELECT * FROM sensor_data WHERE mem_free = 0的查询），就无法比全表线性扫描（即O(n)时间）做得更好来识别相关数据点。
- 索引中包含的列集是完全固定且不可变的。更改数据中哪些列被索引（标记）以及哪些没有，需要完全重写数据。
- 由于依赖哈希映射，InfluxDB 只能索引离散值而不能索引连续值。例如，要搜索所有温度高于 90 度的行（例如，类似于 SELECT * FROM sensor_data WHERE temperature > 90 的查询），则需要再次完全扫描整个数据集。
- InfluxDB 的基数受到所有时间范围内基数的影响，即使某些字段/值不再存在于数据集中也是如此。这是因为 SeriesFile 存储了整个数据集的所有系列键。


### TimescaleDB 和 B-trees

相比之下，TimescaleDB是一个关系型数据库，它依赖于久经考验的用于索引数据的结构：[B-tree](https://en.wikipedia.org/wiki/B-tree)。这一决定使其能够扩展到高基数。

首先，TimescaleDB按时间对您的数据进行分区，一个B-tree将时间段映射到相应的分区（“chunk”）。所有这些分区都在后台进行，对用户隐藏，用户能够访问一个虚拟表（“[hypertable](https://docs.timescale.com/use-timescale/latest/hypertables/about-hypertables/)”），该表跨越所有分区中的所有数据。

接下来，TimescaleDB允许在您的数据集上创建多个索引（例如，对于`equipment_id`、`sensor_id`、`firmware_version`、`site_id`）。默认情况下，这些索引以B-tree的形式在每个chunk上创建。

也可以使用任何内置的[PostgreSQL索引类型](https://www.postgresql.org/docs/current/indexes-types.html?ref=timescale.com)创建索引：Hash、GiST、SP-GiST、GIN和BRIN。您可以[阅读这篇文章以了解有关索引的更多信息](https://www.timescale.com/learn/postgresql-performance-tuning-optimizing-database-indexes)以及如何使用它们来优化PostgreSQL数据库性能。

这种方法对高基数数据集有一些好处：

- 更简单的方法可以更清晰地了解数据库的性能。只要我们要查询的数据集的索引和数据适合内存（这是可以调整的），基数就成为一个非问题。
- 此外，由于辅助索引的范围在chunk级别，因此索引本身的大小仅与该时间范围的数据集的基数一样大。
- 您可以控制要索引的列，包括能够在多列上创建复合索引。您也可以随时添加或删除索引，例如，如果您的查询工作负载发生变化。与InfluxDB不同，在TimescaleDB中更改索引结构不需要重写数据的整个历史记录。
- 您可以对离散字段和连续字段创建索引，特别是由于B-tree非常适合使用以下任何运算符进行比较：`<`、`<=`、`=`、`>=`、`>`、`BETWEEN`、`IN`、`IS NULL`、`IS NOT NULL`。我们上面示例查询（`SELECT * FROM sensor_data WHERE mem_free = 0`和`SELECT * FROM sensor_data WHERE temperature > 90`）将在对数时间或`O(log n)`时间内运行。
- 其他受支持的索引类型在其他场景中可能派上用场，例如，用于[“最近邻”搜索](https://www.timescale.com/blog/understanding-diskann)的GIST索引。

## 结论

现代数据库系统中高基数数据带来的挑战需要复杂的索引解决方案来克服连接操作和全表扫描的固有障碍。InfluxDB和Timescale都具有独特的策略来有效地管理高基数数据。

Timescale的方法利用了B-tree数据结构的强大功能，为处理高基数数据集提供了强大的基础。这种结构不仅能够实现卓越的查询性能，而且还提供了满足各种索引需求所需的灵活性。B-tree架构允许高效的范围查询和点查找，使其特别适合时间序列应用程序，在这些应用程序中，历史分析和实时数据访问都至关重要。
