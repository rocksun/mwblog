# 实时时间序列分析：开发者入门连续聚合

![实时时间序列分析：开发者入门连续聚合](/blog/content/images/size/w2000/2024/11/Real-time-analytics-for-time-series_cont-aggregates-1.png)

在寻找使用TimescaleDB的理由时，您通常会看到一个名为“连续聚合”的功能。这是一个强大的功能，当处理非常大或快速增长的数据集时，它可以帮助您大幅提高性能，使PostgreSQL能够轻松处理实时分析工作负载。让我们更详细地介绍一下。

## 连续聚合到底是什么？

简单来说，TimescaleDB中的[连续聚合](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/about-continuous-aggregates/?ref=timescale.com)是超表的聚合查询的**增量式自动更新的物化视图**。

收集时间序列数据时，您的数据摄取频率通常远高于进一步分析或审计目的所需的频率。解析这些数据可能会出现问题，因为对极其大的数据集执行读写操作需要更长的时间。因此，创建了连续聚合。

![PostgreSQL物化视图与连续聚合的比较表](https://www.timescale.com/blog/content/images/2024/11/Real-Time-Analytics-for-Time-Series_Continuous-aggregates-vs-materialized-views.png)

与常规物化视图不同，*连续聚合仅自动刷新新的或更改的数据，而不是重新计算整个视图*。这会导致数据在后台预先聚合，从而加快源数据的查询和呈现速度。

这使得它们非常适合高效地实时查询大时间范围内的时序数据，因为聚合结果会在后台自动增量刷新，无需人工干预。

## 性能提升，存储减少

使用时间序列数据具有几个明显的优势。这些优势体现在*更快的查询性能*和*降低的存储成本*。

连续聚合通过性能测试实现了这些改进，性能测试显示查询运行时间的即时减少，并且可以使用`DISTINCT`、`ORDER BY`、`FILTER` with `HAVING`以及其他查询子句（*从Timescale 2.7开始*）正常查询您的数据。需要解析的记录更少 = 更快的查询速度和更少的存储数据。

它们也不依赖于原始源数据的存在。这意味着您可以删除底层的超表，同时仍然保留通过连续聚合下采样的数据集。仍然可以在此粒度较低的数据上执行历史分析或审计，同时为新记录腾出空间。

**注意：**
* 每个连续聚合都可以有其自己的*
* 保留策略*
* 以自动删除指定时间段后的一部分数据来自动实现此效果。*从Timescale 2.6开始，您可以将TimescaleDB的原生列式[压缩](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/compression-on-continuous-aggregates/?ref=timescale.com)应用于连续聚合，以进一步压缩磁盘空间。这甚至可以通过

[在一定时间后自动压缩数据，并与数据保留策略结合使用，以删除不再需要的旧数据集。](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/compression-on-continuous-aggregates/?ref=timescale.com#compression-policies-on-continuous-aggregates)

**压缩策略**

## 在现实世界中

用户报告说他们已成功将它们用于各种目的，包括：

- 实时可视化指标
- 对时间序列数据执行数据操作，例如传感器数据、历史股票信息或记录空气污染
- 对物联网设备设置的每日阈值进行强制执行
- 管理面向OLAP的数据库的数据
- 处理需要聚合的数百万（或更多）条现有记录

## 使用连续聚合

假设您需要在仪表板上显示传感器数据以分析结果。

```sql
SELECT
    time_bucket('1 hour', time) as hour,
    device_id,
    AVG(temperature) as avg_temp
FROM sensor_data
WHERE time > NOW() - INTERVAL '1 year'
GROUP BY hour, device_id
ORDER BY hour DESC;
```

当针对数百万行运行时，此类查询可能需要很长时间才能执行。更重要的是，每次执行此查询时，都必须每次运行时重新聚合——消耗不必要的资源并严重影响性能。

这就是连续聚合最有用之处；它们可以用来预先计算结果，形成一个自动更新的智能缓存。我们可以使用连续聚合重写上面的查询：

```sql
CREATE MATERIALIZED VIEW hourly_temps
```
```sql
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 hour', time) as hour,
    device_id,
    AVG(temperature) as avg_temp
FROM sensor_data
GROUP BY hour, device_id;
```

从那里，需要[设置刷新策略](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/refresh-policies/?ref=timescale.com)来自动刷新连续聚合，以最佳方式满足您的用例。您可以出于历史目的保留已从源超表（手动或通过数据保留策略）中删除的连续聚合中的数据，并刷新所有其他数据；或者，您可以选择使连续聚合和超表自动保持同步，同时考虑这些保留策略。

```sql
SELECT add_continuous_aggregate_policy('hourly_temps',
    start_offset => INTERVAL '1 month',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour');
```

此查询在名为`hourly_temps`的连续聚合视图上设置刷新策略。

此处，刷新窗口设置为仅查看当前时间之前最多一个月的数据（就像您使用数据保留策略单独删除一个月前较旧的原始数据一样，并希望保留连续聚合中的历史记录）。如果您更改此窗口之外的数据，则您的聚合将不会重新计算。

刷新窗口在当前时间之前结束一小时，以防止策略尝试刷新仍在写入大量数据的 数据（以及防止实时聚合出现问题，如果已启用）。

此策略每小时运行一次，以增量方式更新一个月到一小时窗口内的连续聚合。

**注意：**
* 除了刷新策略之外，您还可以随时使用 `refresh_continuous_aggregate` 手动刷新连续聚合。现在，您会发现运行如下所示的查询会产生几乎即时的结果：

```sql
SELECT * FROM hourly_temps
WHERE hour > NOW() - INTERVAL '1 year'
ORDER BY hour DESC;
```

**旁注:** 一个常见的问题是是否支持窗口函数。虽然答案是“否”，[这很容易实现：只需创建一个不包含窗口函数的连续聚合，然后在需要查询数据时对连续聚合使用窗口函数即可。](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/create-a-continuous-aggregate/?ref=timescale.com#use-continuous-aggregates-with-window-functions)

__有一个解决方法__
遇到连续聚合问题？查看我们的[故障排除指南](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/troubleshooting/?ref=timescale.com)或与我们和社区联系[—我们很乐意提供帮助。](https://timescale.slack.com/?ref=timescale.com)

__Slack__

## 更多功能

从 TimescaleDB 2.9 开始，您甚至可以将连续聚合堆叠在连续聚合之上，从而实现[分层连续聚合](https://www.timescale.com/blog/an-incremental-materialized-view-on-steroids-how-we-made-continuous-aggregates-even-better/)。*为什么？因为你可以。*（开玩笑。）为了节省存储成本，您可以在第一个连续聚合完成后删除用于计算初始连续聚合的原始原始数据。

可以基于辅助数据集计算其他聚合，就好像它们直接在原始原始数据集上执行一样。这有助于您立即获得性能优势，因为您是在数据集更小、数据点更少的情况下执行聚合，从而允许以更高的速度执行复杂的算法。

需要实时结果？这也是可能的——您可以启用实时聚合以在结果中显示最新的原始数据。（查看有关使用实时聚合的更多信息[此处](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/real-time-aggregates/?ref=timescale.com)。您还可以查看

[性能测试](https://www.timescale.com/blog/achieving-the-best-of-both-worlds-ensuring-up-to-date-results-with-real-time-aggregation/#:~:text=Josh%20Lockerman.-,Testing%20Real%2DTime%20Aggregation,-In%20the%20following).)的结果
您可能会发现值得研究其他执行高效聚合的函数，例如百分位数近似（和

`uddsketch`
[) 以及对变化数据集的数据分析 (](https://docs.timescale.com/api/latest/hyperfunctions/percentile-approximation/uddsketch/?ref=timescale.com#uddsketch-and-percentile_agg-functions)
`percentile_agg()`
[和](https://docs.timescale.com/api/latest/hyperfunctions/counters-and-gauges/counter_agg/?ref=timescale.com)
`counter_agg()`
[).](https://docs.timescale.com/api/latest/hyperfunctions/counters-and-gauges/gauge_agg/?ref=timescale.com)
`gauge_agg()`
从那里，还可以通过超函数扩展连续聚合的功能。超表支持这些功能，并为您提供高级功能，例如简化常用统计聚合的使用、使用计数器聚合函数收集数据以及使用心跳聚合监控系统运行状况。更多信息，请[查看超函数文档](https://docs.timescale.com/use-timescale/latest/hyperfunctions/?ref=timescale.com)。


## 下次

有兴趣阅读更多类似的文章，这些文章将介绍其他 TimescaleDB 功能，例如[SKIP SCAN](https://www.timescale.com/blog/skip-scan-under-load/)，[如何](https://www.timescale.com/blog/scale-postgresql-via-partitioning-hypertables/)使用超表，[或如何](https://www.timescale.com/blog/benchmarking-postgresql-batch-ingest/)导入数据。[关注本系列中的其他文章（或了解我们发布的内容），请订阅 Timescale 时事通讯](https://www.timescale.com/signup/newsletter?ref=timescale.com)。请记住，如果您想试用本文中的任何功能，您可以随时使用[开源 TimescaleDB 扩展](https://github.com/timescale/timescaledb?ref=timescale.com)或[免费试用 Timescale Cloud 30 天，无需信用卡。](https://console.cloud.timescale.com/signup?ref=timescale.com)