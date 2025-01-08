# 不同数据库如何处理高基数数据

时间序列数据、物联网传感器读数、用户行为日志——这些只是现代系统必须处理的数据流的几个例子。它们的共同点是都倾向于高基数，这给数据存储和分析带来了独特的挑战。随着组织越来越依赖数据驱动的决策，了解不同数据库如何处理高基数数据对于构建高效且可扩展的系统至关重要。

本文将探讨高基数数据带来的挑战，检查旨在处理高基数数据的各种数据库工具，并比较各种方法，以帮助您做出关于数据架构的明智决策。

# 高基数的挑战

高基数指的是数据集中唯一元素的数量，当我们查看现实世界的例子时，这是一个特别具体的概念。想象一下一个跟踪热门网站上用户交互的系统——每个用户可能都有一个唯一的标识符，每个会话都会生成一个唯一的ID，每个交互都会创建一个唯一的事件ID。在大规模应用中，这些唯一值可以迅速达到数百万甚至数十亿。

这种大量唯一值会给数据库系统带来重大挑战。当在具有高基数列的表之间执行连接时，潜在的组合会呈指数级增长。例如，将用户交互数据与会话数据连接可能需要将数百万个唯一的用户ID与数百万个唯一的会话ID进行匹配。由于数据库必须维护和处理这些海量独特的组合，因此生成的运算会迅速压垮系统资源。

在需要完全表扫描的操作中，性能下降尤其严重。当数据库需要跨高基数列分析或聚合数据时，它必须在内存中为每个唯一值维护[不同的计数器](https://www.timescale.com/blog/counter-analytics-in-postgresql-beyond-simple-data-denormalization/)或聚合。这会迅速耗尽可用的内存资源，导致查询执行时间变慢，或者在极端情况下导致系统故障。

阅读本文以[了解更多关于高基数的信息](https://www.timescale.com/blog/what-is-high-cardinality)。

# 数据库解决方案：时间序列数据库InfluxDB和TimescaleDB如何处理高基数

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


**Note:** A more detailed overall comparison of these two databases can be found [here](https://www.timescale.com/blog/timescaledb-vs-influxdb-for-time-series-data-timescale-influx-sql-nosql-36489299877/).


As you can see, at low cardinality, the two databases are comparable (although TimescaleDB shows a 30% performance improvement). However, as cardinality increases, the difference is quite significant, as TimescaleDB's insert performance degrades far slower than InfluxDB's, which degrades quite rapidly. At high cardinality, TimescaleDB outperforms InfluxDB by more than 11x.


These results may not be surprising to some, as high cardinality is a known weakness of InfluxDB (sources: [GitHub](https://github.com/influxdata/influxdb/search?q=%22high+cardinality%22&type=Issues&ref=timescale.com), [forum](https://community.influxdata.com/search?q=cardinality+order%3Alatest&ref=timescale.com)).


But why does this happen? Let's take a closer look at how the two databases are engineered.


# B-trees vs. TSI: Two Different Approaches to Handling High Cardinality
We can trace the difference in high-cardinality performance back to fundamental engineering differences between InfluxDB and TimescaleDB.


## InfluxDB and TSI
Because high cardinality has been a known challenge for InfluxDB, their team has been developing something they call "Time Series Index" (TSI) to address this.


Consistent with their approach in other areas, InfluxDB TSI is an internally developed, log-structured merge-tree-based system composed of various data structures, including hash maps and bitsets. This includes an in-memory log ("LogFile") that is periodically flushed to disk and compacted into a disk memory-mapped index ("IndexFile") when it exceeds a threshold (5 MB); and a file ("SeriesFile") containing the set of all series keys across the entire database. (This is described in [their documentation](https://docs.influxdata.com/influxdb/v1.7/concepts/tsi-details/?ref=timescale.com).)


The performance of TSI depends on the interaction of all these data structures. However, because TSI is custom-built, it's difficult to understand its performance under various high-cardinality workloads.


The design decisions behind TSI have also led to some performance-impacting limitations:


- According to the [InfluxDB documentation](https://docs.influxdata.com/influxdb/v1.7/concepts/tsi-details/?ref=timescale.com), the total cardinality is limited to roughly 30 million (although, according to the chart above, InfluxDB starts to underperform well before this), or far below the cardinality often needed in time-series use cases such as IoT (including our example above).
- InfluxDB indexes tags but not fields, meaning that the performance of certain queries cannot be better than a full scan. So, in our previous IoT dataset example, if you want to search for all rows where available memory is zero (e.g., something like `SELECT * FROM sensor_data WHERE mem_free = 0`), there's no way to identify the relevant data points better than a completely linear scan (i.e., `O(n)` time).
- The set of columns included in the index is completely fixed and immutable. Changing which columns in your data are indexed (tagged) and which are not requires a complete rewrite of the data.
- Because InfluxDB relies on hash maps, it can only index discrete values and not continuous values. For example, to search for all rows where the temperature is above 90 degrees (e.g., something like `SELECT * FROM sensor_data WHERE temperature > 90`), again, a full scan of the entire dataset must be performed.
- Even if certain fields/values no longer exist in your dataset, your InfluxDB cardinality is affected by the cardinality across all of your time. This is because the SeriesFile stores all series keys across the entire dataset.


## TimescaleDB and B-trees
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

[立即开始免费试用](https://console.cloud.timescale.com/signup)，看看Timescale如何改变您的高基数数据管理。

## 阅读更多

*本文由Joshua Lockerman、Blagoj Atanasovski和Ana Tavares撰写，并于2024年12月13日在Timescale官方博客上首次发布*。