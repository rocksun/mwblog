Supermetal recently added [Iceberg sink support](https://supermetal.io/blog/iceberg-target), and I wanted to take it for a spin. A couple of months ago, [I tested the newly announced Kafka sink](https://supermetal.io/blog/cdc-benchmark-supermetal-debezium-flink), so you can think about this post as a continuation of this blog post series.

I wanted to compare Supermetal with typical open-source tools for writing data to Iceberg: Kafka Connect, Flink, and Spark.  My goal was to measure a realistic end-to-end pipeline: getting data from [Postgres](https://thenewstack.io/why-ai-workloads-are-fueling-a-move-back-to-postgres/) and writing it to Iceberg.

These workloads are typically used for data archival, so I didn’t want to focus on the latency comparison – the latency requirements are usually pretty flexible. Instead, I primarily focused on throughput during the snapshotting phase.

To make the comparison normalized, I didn’t test the scale-out scenarios. I wanted to understand how much throughput a single node (with the same resource allocation across tests) can deliver.

**Supermetal completed snapshotting in 13 minutes. Flink took 90-116 minutes, Kafka Connect 120 minutes, and Spark over 3 hours.**

As we’ll see below, CDC [performance was the biggest bottleneck](https://thenewstack.io/why-your-apps-biggest-performance-bottleneck-might-be-ssl-tls/), at least for Flink and Kafka Connect / Debezium. Also, most tools completely decouple sources and sinks: this is a great architectural principle to follow. Supermetal’s approach is pretty unique: the Iceberg writer can switch between configuration options depending on the CDC source phase (snapshotting vs. live). I wouldn’t call it coupling; it is closer to the *sideways information-passing* technique [found in some databases](https://datafusion.apache.org/blog/2025/09/10/dynamic-filters/).

*Disclosure: This work was sponsored by Supermetal. All benchmarks were executed myself in my AWS account. All numbers and findings are shared as is.*

## Test setup

![Diagram comparison Postgres to Iceberg data pipelines](https://cdn.thenewstack.io/media/2026/04/70222467-12.jpg)
> “CDC performance was the biggest bottleneck, at least for Flink and Kafka Connect / Debezium… most tools completely decouple sources and sinks: this is a great architectural principle to follow. Supermetal’s approach is pretty unique: the Iceberg writer can switch between configuration options depending on the CDC source phase.”

I used the TPC-H dataset with a scale factor (SF) of 50. If you’re not familiar with it, it consists of 8 tables of different sizes. With SF=50, the largest table (lineitem) has 300M rows, the second-largest (orders) has 75M rows, and so forth.

On the infra side, I had:

* AWS RDS Aurora Postgres 16 Serverless, 48 ACUs max.
* AWS MSK 3.9 with 3 express.m7g.xlarge brokers.
* AWS EKS 1.34 using m8i.xlarge nodes (4 CPU cores, 16 GB RAM).
  + All workloads used a single node almost exclusively (configured to request 3 CPU cores and 13 GB of RAM). Flink TaskManager used 4 task slots. Debezium Iceberg sink connector used 4 tasks. Spark had a single executor and used all available resources.
* Iceberg tables are powered by AWS Glue and AWS S3.

And here are the versions that were used in the test:

* Latest Supermetal build (provided by the Supermetal team as a Docker image).
* Flink CDC 3.5.0 with Flink 1.20 deployed using the Flink Kubernetes Operator 1.13.
* Debezium 3.4.3.Final with Kafka Connect 4.1.1 deployed using the Strimzi Operator 0.51.0.
* Spark 4.1.1 deployed using the Spark Kubernetes Operator 0.8.0.
* Flink, Kafka Connect, and Spark all used Iceberg 1.10.1 connectors.

[Supermetal](https://supermetal.io/) supports [Postgres CDC sources](https://docs.supermetal.io/docs/main/sources/pg/) and [Iceberg sinks](https://docs.supermetal.io/docs/main/targets/iceberg/).

Unlike Kafka Connect, Supermetal doesn’t rely on Kafka or any kind of external orchestrator: data can be delivered directly from a source to a sink (with optional object storage buffering).

I chose to deploy Supermetal using a JSON config file (a good fit for containerized workloads). The config file just describes sources and sinks. Here’s what it looks like for a complete Postgres to Iceberg pipeline:

```

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

This is the complete pipeline, no more configuration needed! You don’t even need to specify the table names explicitly; they can be discovered at runtime.

Iceberg sink supports different catalogs (including REST, AWS Glue, and AWS S3 Tables), and you can choose between Iceberg V1, V2, or V3 support. More advanced configuration options include Append vs Merge on Read, Parquet target file size, and compression.

Finally, Supermetal adjusts file flushing configuration automatically based on the current phase:

* During the snapshot phase, it uses the configured target file size (512 MB by default). This ensures that the snapshot-phase files are large enough and don’t even need compaction.
* During the live CDC phase, the “flush\_interval\_ms” configuration (10 seconds by default) is enabled, allowing you to easily control end-to-end latency.

This is a pretty unique feature! Other tools don’t really differentiate between lifecycle phases (snapshot vs live CDC) at the Iceberg sink level; CDC and other connectors are completely decoupled.

### Results

Supermetal only needed 13 minutes to sync all data! Here’s the BytesUploaded metric for the underlying S3 bucket:

![BytesUploaded chart for S3 bucket](https://cdn.thenewstack.io/media/2026/04/8153ff39-1-1024x445.png)

The CPU and memory stayed fairly low during the test:

![Graphs of CPU and memory utilization](https://cdn.thenewstack.io/media/2026/04/74828bcf-2-891x1024.png)

You can see that Supermetal was using no more than 5% of the allocated memory! There was no need to think about tuning. Snapshot phase benefits from inter- and intra-table parallelization.

Note: Supermetal uses append-only mode during snapshotting! It doesn’t track table-level keys or perform deduplication at that stage.

File sizes for the largest table (lineitem) look ideal, the same as the specified Parquet target size:

![Table showing sizes of each parquet file](https://cdn.thenewstack.io/media/2026/04/373de8f4-3-1024x224.png)

## Flink

[Apache Flink](https://github.com/apache/flink) supports the Postgres CDC connector (via [Flink CDC](https://github.com/apache/flink-cdc)), as well as [the Iceberg connector.](https://iceberg.apache.org/docs/latest/flink/) We can combine these connectors and write data directly from Postgres to Iceberg.

We could alternatively use Apache Kafka in the middle: first capture CDC data as a set of topics, then consume from those topics and write to Iceberg. We’ll actually have to follow this approach for Kafka Connect and Spark. But since it’s possible to avoid [Kafka in the case of Flink](https://thenewstack.io/why-python-data-engineers-should-know-kafka-and-flink/) and write data directly, we’ll implement that.

The Iceberg connector documentation recommends using Flink SQL to define tables. However, this comes with a few downsides:

* All table schemas have to be explicitly defined.
* Most importantly, each Postgres-to-Iceberg table combination is a separate SQL statement that must be created for each table. Thanks to Statement Sets, they can be executed within the same Flink pipeline, but it’s still a lot of boilerplate.
  + If we were to follow this approach, we’d need to allocate **one replication slot for each table source**. This is really wasteful and doesn’t scale.

However, the Iceberg connector comes with a powerful feature called [Dynamic Sink](https://iceberg.apache.org/docs/latest/flink-writes/#flink-dynamic-iceberg-sink). It allows you to register a single sink and dynamically route data to different tables. It also handles table registration and schema evolution.

DynamicRecord is a core primitive in the Dynamic Sink:

```

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

It wraps Flink’s RowData with additional metadata for routing.

Another important note is that the Flink Iceberg sink only flushes data during a checkpoint. It means that the Flink checkpoint interval becomes the primary way to control the flush size.

### Results

I started a Flink job **with upserting enabled**, but without any tuning and a 30-second checkpoint interval. It took about **3.5 hours** to complete!

After investigating, I realized that the problems identified in [the previous blog post](https://supermetal.io/blog/cdc-benchmark-supermetal-debezium-flink) remain highly relevant here: even if the Iceberg sink is extremely efficient, a slow CDC source still affects overall throughput.

So I had to increase the fetch size and split size first to 5000 (from 1024) and 50000 (from 8096), then to 8000 and 80000, respectively. Going higher started to cause out-of-memory issues. These options control how quickly data is retrieved from the underlying database.

I also increased the Flink checkpoint interval to 5 minutes.

Any tuning applied to the Iceberg sink (e.g., changing distribution mode) didn’t seem to help.

The optimized version finished in just under two hours. Here’s the BytesUploaded metric for the underlying S3 bucket:

![BytesUploaded chart for Flink S3](https://cdn.thenewstack.io/media/2026/04/38a262de-4-1024x410.png)

The CPU and memory usage were high, but not disturbing:

![Chart of CPU and memory usage for Flink S3](https://cdn.thenewstack.io/media/2026/04/3b59d6f8-5-879x1024.png)

Parquet file sizes were all over the place:

![Parquet file sizes for Flink S3](https://cdn.thenewstack.io/media/2026/04/27b267c5-6-1024x235.png)

It’s hard to control them precisely: there is a “write.target-file-size-bytes” configuration, but it looks like the file creation is primarily controlled by the checkpoint interval.

I disabled upserting and switched to append-only mode. This version of the job finished in 1.5 hours.

![BytesUploaded chart in append-only mode](https://cdn.thenewstack.io/media/2026/04/57ee223d-7-1024x318.png)![CPU and memory utilization chart in append-only mode](https://cdn.thenewstack.io/media/2026/04/e0aa704b-8-845x1024.png)

Produced Parquet files looked much more uniform:

![Parquet file sizes in append-only mode](https://cdn.thenewstack.io/media/2026/04/d1482b41-9-1024x200.png)

## Kafka Connect

[Kafka Connect](https://kafka.apache.org/42/kafka-connect/overview/) also supports the Postgres CDC connector (via [Debezium](https://debezium.io/)) and [the Iceberg connector](https://iceberg.apache.org/docs/latest/kafka-connect/). But Kafka Connect depends on using Kafka as an intermediate layer.

The Iceberg connector configuration I used looked like this:

```

topics: debezium.public.lineitem, # the rest of the topics

# Transform Debezium envelope into CDC format and set _cdc.target for routing
transforms: debezium
transforms.debezium.type: org.apache.iceberg.connect.transforms.DebeziumTransform
transforms.debezium.cdc.target.pattern: ${env:ICEBERG_GLUE_DATABASE}.{table}

# Catalog (AWS Glue)
iceberg.catalog.catalog-impl: org.apache.iceberg.aws.glue.GlueCatalog
iceberg.catalog.warehouse: s3://${env:ICEBERG_S3_BUCKET}/
iceberg.catalog.io-impl: org.apache.iceberg.aws.s3.S3FileIO

# Table settings
iceberg.tables.dynamic-enabled: true
iceberg.tables.route-field: _cdc.target
iceberg.tables.auto-create-enabled: true

# Commit coordination
iceberg.control.topic: iceberg-control
iceberg.control.commit.interval-ms: 300000

```

“dynamic-enabled” and “route-field” options enable behavior similar to the Dynamic Sink in Flink: data can be routed to different tables automatically, thanks to the additional metadata exposed by DebeziumTransform.

The commit interval was set to 5 minutes, the same as the Flink checkpointing interval.

The current version of the connector doesn’t seem to support upserting.

I suspected the CDC source would be the biggest bottleneck here as well (and it turned out to be the case). So I also applied some tuning to the Debezium source, primarily increasing linger.ms and batch.size (until I started getting MESSAGE\_TOO\_LARGE errors).

### Results

It took Kafka Connect connectors about two hoursto complete. Here’s the BytesUploaded metric for the underlying S3 bucket:

![BytesUploaded chart for Kafka Connect](https://cdn.thenewstack.io/media/2026/04/dd188f65-10-1024x349.png)

The CPU was especially high during the whole run:

![CPU and memory utilization for Kafka Connect](https://cdn.thenewstack.io/media/2026/04/640f3e5f-11-1024x1024.png)

The CPU bottleneck was concerning, but profiling didn’t show anything suspicious:

![CPU profiling chart for Kafka Connect](https://cdn.thenewstack.io/media/2026/04/dff82aca-12-1024x578.png)

It looks like a pretty even distribution between the source (CDC processing, JSON serialization) and the sink (JSON deserialization, Parquet writing).

The underlying Parquet sizes looked well distributed:

![Parquet file sizes for Kafka Connect](https://cdn.thenewstack.io/media/2026/04/b11ea65f-13-1024x220.png)

## Spark

[Apache Spark](https://spark.apache.org/) doesn’t have a first-class CDC connector like Flink or Kafka Connect. So, to build a complete Postgres-to-Iceberg pipeline, I used Kafka Connect with the Debezium connector to capture Postgres tables as Kafka topics. Then the Spark job consumed data from Kafka and wrote it to Iceberg. [Spark has excellent support for Iceberg](https://iceberg.apache.org/docs/latest/spark-getting-started/) since it was one of the first tools to support it.

Unfortunately, Spark doesn’t support the concept of Dynamic Sink (from Flink) or field-based routing (Kafka Connect). When it comes to writing to multiple sinks, we have a few options:

* foreachBatch: a special operator that gives you precise control over batch writes. You can find many examples online; however, [Databricks does not recommend](https://docs.databricks.com/aws/en/structured-streaming/foreach#write-to-multiple-locations) using it for writing to multiple sinks.
* Query per table approach: not a “true” routing, but it’s a good enough workaround. We simply iterate over the list of input topics during startup and start a streaming query for each table.

The query per table approach creates a series of queries like this:

```

Dataset&lt;Row> raw = spark.readStream()
    .format("kafka")
    .options(kafkaOptions)
    .option("subscribe", topic)
    .option("startingOffsets", "earliest")
    .load();

Dataset&lt;Row> result = … // data parsing and processing

result.writeStream()
    .format("iceberg")
    .outputMode("append")
    .trigger(Trigger.ProcessingTime(triggerIntervalMs))
    .option("checkpointLocation", checkpointBase + "/" + table.name())
    .toTable(fullTableName);

```

### Results

I only focused on load-testing the Spark part of the job, from Kafka to Iceberg.

I started with the foreachBatch approach; however, it took over 4 hours.

I switched to the query-per-table approach and started iterating on tuning:

* Increased Kafka Consumer settings (max.poll.records, fetch.max.bytes, etc.) to reduce the overhead of making many polls when fetching data from Kafka.
* Adjusted maxOffsetsPerTrigger. Set it too low, and you end up with many small files (with extra overhead); set it too high, and you get a single batch for the whole topic partition.
* Triggers, batch caching, optimized parsing and filtering, memory, shuffle partitions…

Despite all my efforts, the best run took 3 hours and 20 minutes. Here’s the BytesUploaded metric for the underlying S3 bucket:

![Chart showing the BytesUploaded metric for Kafka](https://cdn.thenewstack.io/media/2026/04/a494720b-14-1024x423.png)

The executor CPU stayed pretty low:

![CPU and memory usage for Kafka](https://cdn.thenewstack.io/media/2026/04/c057e381-15-873x1024.png)

I attribute this level of performance to Spark’s architecture: it’s designed for a large scale-out infrastructure, and it’s really struggling on a single executor with just a handful of cores. Eight independent queries (one for each topic) competed for 4 task slots, and each query also paid its own checkpoint and Iceberg commit overhead.

The underlying Parquet sizes looked uniform (mostly controlled by maxOffsetsPerTrigger):

![Parquet file sizes for Kafka](https://cdn.thenewstack.io/media/2026/04/29134308-16-1024x180.png)

## Data correctness

I validated that all tools correctly synchronized the data without any loss or duplication. All table counts matched between Postgres and Iceberg.

> “Supermetal achieves at least 7x faster snapshotting performance without any tuning. I attribute this primarily to a very fast CDC source and low serialization/deserialization overhead.”

I also spot-checked actual data and only noticed minor differences in column order and additional metadata columns.

## Summary

Here’s the final comparison of the best test runs:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Tool** | **Total Time (Min)** | **Tuning Effort** | **Commit Frequency** | **Write Mode** | **Specific Configuration Details** |
| **Supermetal** | **13** | **No tuning** | 10s flush (Live CDC only) | Append-only (Snapshot) / Merge-on-Read (Live) | Out-of-the-box configuration. Target file size 512 MB (default). Highly optimized for low-latency live changes. |
| **Flink** | 116 | Manually tuned | 5 min (checkpoint) | Upserting | Checkpoint interval increased from 30s. Fetch size 8k, split size 80k (increased from defaults). |
| **Flink** | 90 | Manually tuned | 5 min (checkpoint) | Append-only | Same tuning as the upserting run, but without the primary key tracking / deduplication overhead. |
| **Kafka Connect** | 120 | Manually tuned | 5 min | Append-only | Required careful adjustment of connector configuration. `linger.ms` and `batch.size` were tuned for stability and throughput. Upserting is unsupported in this standard setup. |
| **Spark** | 200 | Manually tuned | Trigger interval / maxOffsetsPerTrigger | Append-only | Only consumed from a pre-populated Kafka topic (no snapshot). Primary tuning involved optimizing the `maxOffsetsPerTrigger` for the Structured Streaming job. |

Supermetal achieves at least 7x faster snapshotting performance without any tuning. I attribute this primarily to a very fast CDC source and low serialization/deserialization overhead. Slower CDC source was confirmed as an issue for Flink and Debezium [in the other benchmark](https://supermetal.io/blog/cdc-benchmark-supermetal-debezium-flink).

Also, Supermetal can distinguish snapshotting and live CDC phases end-to-end, enabling sink-level optimizations such as using append-only mode and a target file size for rolling files during snapshotting, and switching to merge-on-read mode and a time-based interval during the live CDC phase.

Flink showed the best time after that, but it required pretty aggressive tuning. Both Flink and Kafka Connect offer ways to dynamically route source data into multiple Iceberg tables; Spark requires creating a separate query for each table.

Finally, I’d like to note that this test focused on single-node performance. Of course, most other tools can be scaled out horizontally (all Iceberg sinks; on the CDC side, only Flink offers this capability at the moment). But this can become very expensive very quickly. Supermetal can also be horizontally scaled to a degree, for example, using a single table as the unit of scaling.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/09/18e76fd5-cropped-ce83f985-yaroslav-tkachenko.jpg)

Yaroslav Tkachenko is a Software Engineer, Consultant, and Advisor specializing in data streaming & data-intensive applications. Currently, Yaroslav is a Founder at Irontools, building tooling for data processing technologies and consulting companies in the data streaming space. Previously, Yaroslav was...

Read more from Yaroslav Tkachenko](https://thenewstack.io/author/yaroslav-tkachenko/)