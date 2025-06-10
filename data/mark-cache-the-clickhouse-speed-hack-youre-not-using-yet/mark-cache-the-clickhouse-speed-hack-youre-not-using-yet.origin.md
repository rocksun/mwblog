# Mark Cache: The ClickHouse Speed Hack You’re Not Using (Yet)
![Featued image for: Mark Cache: The ClickHouse Speed Hack You’re Not Using (Yet)](https://cdn.thenewstack.io/media/2025/06/166b35cb-abstract-1024x572.png)
[ClickHouse](https://www.instaclustr.com/support/documentation/clickhouse/) has become a [go-to online analytical processing (OLAP) database](https://thenewstack.io/clickhouse-rapidly-rivals-other-open-source-databases-in-active-contributors/) for developers and engineers working on high-throughput analytical workloads. It’s fast, lightweight, open source and purpose-built for real-time performance at scale. However, [maximizing the potential of ClickHouse](https://thenewstack.io/vector-search-without-the-lock-in-why-devs-like-clickhouse/) takes more than default configurations. If your team is relying on ClickHouse to power dashboards, stream processing or on-the-fly analytics, there’s a critical internal mechanism worth tuning: mark cache.
Mark cache is somehow still overlooked, but it plays a foundational role in how ClickHouse achieves high performance, especially when querying large data sets. When used properly, it slashes query times, reduces disk I/O and boosts the overall responsiveness of your workloads.

## What Is Mark Cache, Really?
At its core, mark cache is a memory-resident optimization for how ClickHouse accesses data stored in its MergeTree tables. ClickHouse stores data in compressed files, with each file split into “granules” (the smallest retrievable units). These granules are indexed by “marks,” or metadata pointers that tell ClickHouse where each granule starts in the compressed file. So instead of scanning or decompressing the entire file to fulfill a query, ClickHouse can skip directly to the data it needs if it has access to the relevant marks.

That’s where mark cache comes in. It stores these marks in memory, so when a query is executed, ClickHouse can immediately locate and access the relevant data block, bypassing costly file operations. If the needed marks aren’t in cache, ClickHouse must read and parse parts of the file to find them, slowing down execution.

## Why Mark Cache Matters for Real-World Performance
The effect of mark cache becomes especially obvious under repeated or high-concurrency workloads, like dashboards refreshing every few seconds, APIs hitting ClickHouse to populate user metrics or streaming data pipelines performing aggregations across time windows. These are all scenarios where the same columns and data ranges get accessed repeatedly.

Whenever they do, mark cache helps ClickHouse short-circuit redundant work. It minimizes the amount of data read from disk, avoids unnecessary decompression and keeps memory operations tight and predictable.

Even beyond pure speed, mark cache also contributes to better resource efficiency. By limiting the scope of data access, it helps avoid excessive CPU cycles and reduces contention on disk or network-attached storage. The result is faster queries, less load on the system and a better experience for end users and applications relying on timely insights.

## Tuning Mark Cache for Your Workload
ClickHouse doesn’t automatically tune mark cache for your specific needs. You need to configure it. The key variable is `mark_cache_size`
, which sets the maximum amount of memory that ClickHouse will allocate for storing marks. This isn’t one size fits all. Too small, and your cache will constantly evict useful marks, resulting in more cache misses. Too large, and you risk starving the OS, file system cache or other ClickHouse components.

To size it all correctly, start by understanding your data layout. Large MergeTree tables with many parts require more marks to be cached. This means higher memory requirements. Frequent queries against wide tables, or queries that access only a few columns but do so often, will benefit more from an ample mark cache.

Query patterns also play a critical role. If users or applications often repeat similar queries (or if analytics dashboards drive recurring patterns of access), the chances that marks will be reused increase significantly. In those cases, investing more memory into mark cache can yield a strong performance return on investment.

Last but not least, assess the total available system memory. ClickHouse’s performance depends on a combination of mark cache, uncompressed cache and OS-level caching. Starving any one of them can hurt overall performance. Sizing mark cache must be done in context with your broader system configuration. At [Instaclustr](https://www.instaclustr.com/), what we’re seeing across production deployments is that teams who actively monitor and adjust mark cache based on workload behavior see measurable gains — not just in speed, but also in system reliability and resource efficiency.

## Observability To Monitor Hits and Misses
Once mark cache is enabled and sized, the next step is observability. You need to track how often your queries benefit from the cache versus how often they miss and fall back to disk access.

ClickHouse provides visibility via the system.events and system.asynchronous_metrics tables.

These internal tables expose useful counters like:

1 |
SELECT metric,value FROM system.asynchronous_metrics WHERE metric LIKE'Mark%' |
This reveals both mark cache hits and misses, helping you understand if the cache is actually delivering real value. A high miss rate could indicate that your cache is undersized or that your queries are too varied to benefit from caching.
You can also monitor overall memory usage with:

123 |
SELECT formatReadableSize(value) AS mark_cache_usageFROM system.asynchronous_metricsWHERE metric = 'MarkCacheBytes'; |
If you’re using observability tools like [Grafana](https://grafana.com/) or [Prometheus](https://prometheus.io/), these metrics can be exported and visualized to provide real-time insight into cache performance. Alerts can be configured to warn when hit rates drop below thresholds or when memory consumption rises too high.
## Don’t Tune in Isolation
Another all-too-common mistake is treating mark cache as a standalone tuning knob. It’s not. Effective performance tuning in ClickHouse means balancing multiple cache layers, including mark cache, uncompressed cache and the operating system’s page cache. If you optimize mark cache but neglect the others, performance bottlenecks can reappear elsewhere.

The best approach is a holistic one. Use observability to track all cache layers. Understand how your memory is divided. Make incremental changes and measure their impact, not just in terms of cache hits but also overall query latency and system load.

## A Small Change With Outsized Results
Mark cache isn’t the flashiest feature in ClickHouse, but that’s exactly why it’s so powerful. With just a few adjustments and regular monitoring, it can unlock major performance improvements with minimal effort.

For engineering teams scaling ClickHouse in production, tuning mark cache can be the difference between good and great performance, especially when real-time analytics is at the heart of the business. Whether you’re delivering metrics dashboards, powering product analytics or enabling streaming data pipelines, mark cache is a ClickHouse lever worth pulling.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)