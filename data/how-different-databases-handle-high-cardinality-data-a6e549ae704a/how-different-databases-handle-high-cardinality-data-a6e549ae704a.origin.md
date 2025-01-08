# How Different Databases Handle High-Cardinality Data
Time-series data, IoT sensor readings, user behavior logs — these are just a few examples of the data streams that modern systems must process. What they share in common is their tendency toward high cardinality, which presents unique challenges for data storage and analysis. As organizations increasingly rely on data-driven decisions, understanding how different databases handle high-cardinality data is vital for building efficient and scalable systems.

In this article, we’ll explore the challenges presented by high-cardinality data, examine various database tools designed to handle it and compare approaches to help you make informed decisions about your data architecture.

# The Challenges of High Cardinality
High cardinality refers to the number of unique elements in a dataset, and it’s a concept that becomes particularly tangible when we look at real-world examples. Imagine a system tracking user interactions on a popular website — each user might have a unique identifier, each session generates a unique ID, and every interaction creates a unique event ID. In large-scale applications, these unique values can quickly number in the millions or even billions.

This abundance of unique values creates significant challenges for database systems. When performing joins between tables with high-cardinality columns, the potential combinations multiply exponentially. For instance, joining user interaction data with session data might require matching millions of unique user IDs with millions of unique session IDs. The resulting operation can quickly overwhelm system resources, as the database must maintain and process these massive sets of unique combinations.

Performance degradation becomes particularly acute during operations that require full table scans. When a database needs to analyze or aggregate data across high-cardinality columns, it must maintain [distinct counters](https://www.timescale.com/blog/counter-analytics-in-postgresql-beyond-simple-data-denormalization/) or aggregates for each unique value in memory. This can rapidly exhaust available memory resources, leading to slower query execution times or, in extreme cases, system failures.

Read this article to [learn more about high cardinality](https://www.timescale.com/blog/what-is-high-cardinality).

# Database Solutions: How Time-Series Databases InfluxDB and TimescaleDB Handle High Cardinality
Given how common high-cardinality datasets are within time series, let’s take a look at how two time-series databases, InfluxDB and TimescaleDB, handle this issue.

InfluxDB is a NoSQL database for which its creators have chosen to rebuild everything from scratch. In contrast, TimescaleDB is a SQL database for which its creators (namely, your authors) have chosen to embrace and build on top of PostgreSQL and proven data structures and then further extend it for time series, events, and real-time analytics problems. (By the way, with the right extensions, [it can also propel your AI application development](https://www.timescale.com/ai).)

First, here is a comparison of how the two databases perform on inserts as the dataset’s cardinality increases.

For the following comparison, we used this setup:

- TimescaleDB
[version 1.2.2](https://github.com/timescale/timescaledb/releases/tag/1.2.2?ref=timescale.com), InfluxDB[version 1.7.6](https://github.com/influxdata/influxdb/releases/tag/v1.7.6?ref=timescale.com) - 1 remote client machine and 1 database server, both in the same cloud data center
- AWS EC2 instance: i3.xlarge (4 vCPU, 30 GB memory)
- 4 one-TB disks in a raid0 configuration (EXT4 filesystem)
- Both databases were given all available memory
- Dataset
- 100–1,000,000 simulated devices generated 1–10 CPU metrics every 10 seconds for ~100 M reading intervals, ~1 B metrics (one-month interval for 100 devices; three days for 4,000; three hours for 100,000; three minutes for 1,000,000),
[generated with the Time Series Benchmark Suite (TSBS)](https://github.com/timescale/tsbs?ref=timescale.com) - Schemas used for TimescaleDB (1) and InfluxDB (2)
- 10 K batch size was used for both on inserts
- For TimescaleDB, we set the chunk size depending on the data volume, aiming for 10–15 chunks (
[more here](https://docs.timescale.com/using-timescaledb/hypertables?utm_source=timescale-blog&utm_medium=referral&utm_campaign=influx-benchmark-post&utm_content=seconddocslink#best-practices)) - For InfluxDB, we enabled the
[TSI (time series index)](https://docs.influxdata.com/influxdb/v1.6/concepts/tsi-details/?ref=timescale.com)
(1) **TimescaleDB schema:** Table cpu(time timestamp, tags_id integer, usage_user double, usage_system double, usage_idle double, usage_nice double, usage_iowait double, usage_irq double, usage_softirq double, usage_steal double, usage_guest double, usage_guest_nice double, additional_tags jsonb); Index on (tags_id, time) and (time, tags_id); Table tags(id integer, hostname text, region text, datacenter text, rack text, os text, arch text, team text, service text, service_version text, service_environment text); Unique index on all the columns together

(2) **InfluxDB schema:** Field Keys(usage_guest integer, usage_guest_nice integer, usage_idle integer, usage_iowait integer, usage_irq integer, usage_nice integer, usage_softirq integer, usage_steal integer, usage_system integer, usage_user integer), Tag Keys(arch, datacenter, hostname, os, rack, region, service, service_environment, service_version, team)

**Note**: a more detailed overall comparison of these two databases can be found [here](https://www.timescale.com/blog/timescaledb-vs-influxdb-for-time-series-data-timescale-influx-sql-nosql-36489299877/).
As you can see, at low cardinality, both databases are comparable (although TimescaleDB outperforms by 30 %). But as cardinality increases, the difference is quite remarkable, as the insert performance for TimescaleDB degrades far more slowly than that of InfluxDB, which falls rather precipitously. At high cardinalities, TimescaleDB outperforms InfluxDB by over 11x.

These results may not be surprising to some, as high cardinality is a well-known weakness for InfluxDB (source: [GitHub](https://github.com/influxdata/influxdb/search?q=%22high+cardinality%22&type=Issues&ref=timescale.com), [Forums](https://community.influxdata.com/search?q=cardinality+order%3Alatest&ref=timescale.com)).

But why does this happen? Let’s take a closer look at how these two databases are being developed.

# B-Trees vs. the TSI: Two Different Approaches for Handling High Cardinality
We can trace the difference in high-cardinality performance to fundamentally different engineering decisions in InfluxDB vs. TimescaleDB.

## InfluxDB and the TSI
Since high cardinality has been a well-known challenge for InfluxDB, their team has been working on something they call the “Time Series Index” (TSI) to address this problem.

Consistent with their approach in other areas, the InfluxDB TSI is a home-grown log-structured merge tree-based system comprised of various data structures, including hashmaps and bitsets. This includes an in-memory log (“LogFile”) that gets periodically flushed to disk when it exceeds a threshold (5 MB) and compacted to an on-disk memory-mapped index (“IndexFile”); a file (“SeriesFile”) that contains a set of all series keys across the entire database. (Described [here in their documentation](https://docs.influxdata.com/influxdb/v1.7/concepts/tsi-details/?ref=timescale.com).)

The performance of the TSI relies on the interactions of all of these data structures. However, because the TSI is custom-built, understanding how it performs under various high-cardinality workloads becomes difficult to understand.

The design decisions behind the TSI also lead to a few limitations with performance implications:

- That total cardinality limit,
[according to the InfluxDB documentation](https://docs.influxdata.com/influxdb/v1.7/concepts/tsi-details/?ref=timescale.com), is around 30 million (although based on the graph above, InfluxDB starts to perform poorly well before that), or far below what is often required in time-series use cases like IoT (including our example above). - InfluxDB indexes tags but not fields, which means that certain queries can not perform better than full scans. So, using our earlier IoT dataset as an example, if one wanted to search for all rows where there was no free memory (e.g, something like
`SELECT * FROM sensor_data WHERE mem_free = 0`
), one could not do better than a full linear scan (i.e.,`O(n) time`
) to identify the relevant data points. - The set of columns included in the index is completely fixed and immutable. Changing what columns in your data are indexed (tagged) and what things are not requires a full rewrite of your data.
- InfluxDB is only able to index discrete and not continuous values due to its reliance on hashmaps. For example, to search all rows where the temperature was greater than 90 degrees (e.g., something like
`SELECT * FROM sensor_data WHERE temperature > 90`
), one would again have to fully scan the entire dataset. - Your cardinality on InfluxDB is affected by your cardinality across all time, even if some fields/values are no longer present in your dataset. This is because the SeriesFile stores all series keys across the entire dataset.
## TimescaleDB and B-trees
In contrast, TimescaleDB is a relational database that relies on a proven data structure for indexing data: the [B-tree](https://en.wikipedia.org/wiki/B-tree). This decision allows it to scale to high cardinalities.

First, TimescaleDB partitions your data by time, with one B-tree mapping time segments to the appropriate partition (“chunk”). All of this partitioning happens behind the scenes and is hidden from the user, who is able to access a virtual table (“[hypertable](https://docs.timescale.com/use-timescale/latest/hypertables/about-hypertables/)”) that spans all of their data across all partitions.

Next, TimescaleDB allows for the creation of multiple indexes across your dataset (e.g., for `equipment_id`
, `sensor_id`
, `firmware_version`
, `site_id`
). These indexes are then created on every chunk, by default, in the form of a B-tree.

One can also create indexes using any of the built-in [PostgreSQL index types](https://www.postgresql.org/docs/current/indexes-types.html?ref=timescale.com): Hash, GiST, SP-GiST, GIN, and BRIN. You can [read this article to learn more about indexes](https://www.timescale.com/learn/postgresql-performance-tuning-optimizing-database-indexes) and how to use them to optimize your PostgreSQL database performance.

This approach has a few benefits for high-cardinality datasets:

- The simpler approach leads to a clearer understanding of how the database performs. As long as the indexes and data for the dataset we want to query fit inside memory, which is something that can be tuned, cardinality becomes a non-issue.
- In addition, since the secondary indexes are scoped at the chunk level, the indexes themselves only get as large as the cardinality of the dataset for that range of time.
- You have control over which columns to index, including the ability to create compound indexes over multiple columns. You can also add or delete indexes anytime you want, for example, if your query workloads change. Unlike in InfluxDB, changing your indexing structure in TimescaleDB does not require you to rewrite the entire history of your data.
- You can create indexes on discrete and continuous fields, particularly because B-trees work well for a comparison using any of the following operators:
`<`
,`<=`
,`=`
,`>=`
,`>`
,`BETWEEN`
,`IN`
,`IS NULL`
,`IS NOT NULL`
. Our example queries from above (`SELECT * FROM sensor_data WHERE mem_free = 0`
and`SELECT * FROM sensor_data WHERE temperature > 90`
) will run in logarithmic, or`O(log n)`
, time. - The other supported index types can come in handy in other scenarios, e.g., GIST indexes for
[“nearest neighbor” searches](https://www.timescale.com/blog/understanding-diskann).
# Conclusion
The challenges posed by high-cardinality data in modern database systems demand sophisticated indexing solutions to overcome the inherent obstacles of join operations and full table scans. Both InfluxDB and Timescale have unique strategies for managing high-cardinality data effectively.

Timescale’s approach leverages the power of B-tree data structures, providing a robust foundation for handling high-cardinality data sets. This structure enables not only superior query performance but also offers the flexibility needed for diverse indexing requirements. The B-tree architecture allows for efficient range queries and point lookups, making it particularly well-suited for time-series applications where both historical analysis and real-time data access are crucial.

[Start your free trial today](https://console.cloud.timescale.com/signup) and see how Timescale can transform your high-cardinality data management.
## Read more
*This article was written by Joshua Lockerman, Blagoj Atanasovski, and Ana Tavares *a*nd originally published **here** on the Timescale official blog on December 13, 2024.*