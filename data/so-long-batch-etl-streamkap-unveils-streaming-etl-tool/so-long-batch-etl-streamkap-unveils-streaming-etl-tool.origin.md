# So Long, Batch ETL: Streamkap Unveils Streaming ETL Tool
![Featued image for: So Long, Batch ETL: Streamkap Unveils Streaming ETL Tool](https://cdn.thenewstack.io/media/2024/08/db715b71-streaming-4198529_1280.jpg)
The number of real-time data processing frameworks for organizations accelerating the time required to manage — or just move — data for low latency business opportunities is legion. Common options include [streaming data platforms](https://thenewstack.io/confluent-wants-to-make-batch-processing-a-thing-of-the-past/), [real-time databases](https://thenewstack.io/how-to-introduce-real-time-data-predictions-with-redpanda/), [time-series databases](https://thenewstack.io/install-the-influxdb-time-series-database-on-ubuntu-server-22-04/) and a wealth of other tooling designed to address these needs.

[Streamkap](https://streamkap.com/), a 2022 startup that recently garnered $3.3 million in seed and pre-seed funding, is distinguished from nearly each of these choices in two pivotal ways. First, although it’s architected atop both [Apache Kafka](https://thenewstack.io/kafka-3-8-brings-faster-startups-to-java-developers/) and [Apache Flink](https://thenewstack.io/apache-flink-2023-retrospective-and-glimpse-into-the-future/), the platform doesn’t entail a significant infrastructural investment.
Users don’t need to redesign existing processes for it. Instead, it delivers what Streamkap CEO [Paul Dudley](https://www.linkedin.com/in/pauldudley) termed an “application-like experience.”

Second, Streamkap specializes in delivering streaming extract, transform and load (ETL) — which isn’t synonymous with streaming data processing — to drastically expedite traditional batch processing while fitting neatly into that same, familiar paradigm.

“Consumers are starting to have the expectation that the experiences they get are powered by real-time data, so businesses have to figure out ways to do that,” Dudley said. “Rather than having to shift their whole architecture to enable it, we’re trying to make it easy to remove what is often the biggest bottleneck, which is their batch ETL.”

## Streamkap for Pipelining Data
Although Streamkap can support routing data from event-producing endpoints to analytics tools, its quintessential use case is pipelining data from transactional databases to analytical targets (like [Snowflake](https://www.snowflake.com/?utm_content=inline+mention)). Its Kakfa and Flink foundation, coupled with its reliance on [change data capture](https://thenewstack.io/change-data-capture-for-real-time-access-to-backend-databases/) (CDC) and platform features for accommodating schema changes, make this a reality for the enterprise.

“Streamkap is powered by streaming architecture, but it doesn’t require a company to completely re-architect their whole data stack,” Dudley remarked. “They just get faster data.”

## Kafka and Flink
In general, Streamkap relies on [Kafka](https://kafka.apache.org/) for straightforward ETL jobs without significant transformations, and Flink for those that do involve such transformations. Kafka’s publisher subscriber model is essential to Streamkap’s ETL service, durability and overall resiliency while increasing the speed of this pre-analytics process.

According to Dudley, this Kafka attribute endows Streamkap with “a ton of resilience and a distributed log. So, if there are failures on the source or destination side, our system can be the resilient center of that and replay data; if the destination fails, we’re there, retaining data.”

As such, Kafka is a vital component of the pipelines Streamkap builds. [Flink](https://flink.apache.org/) is no less so, particularly as the sophistication of the ETL requirements increases.

Dudley described a use case in which a fashion retailer integrates data from MySQL with low latency event data from its website to provide real-time personalization — similar to that of TikTok — for site viewers. “That’s powered by Flink, because you’re joining data from two different data sources and you have to maintain state to effectively do that, so Flink is the tool,” Dudley noted.

However, because of the low infrastructure management requirements Streamkap has, users need not concern themselves about the particulars of which streaming data resource is involved in their application. The ETL tool masks this complexity, giving users “low latency data that’s easy to access,” Dudley said.

## Change Data Capture
Streamkap predominantly relies on CDC for loading data from source to target. It offers connectors to a number of popular sources (including data lakes, cloud data warehouses, databases and more), many of which are based on CDC.

According to Dudley, CDC is optimal for the subsecond latency data delivery characteristic of streaming data, because “the log of a database that we’re reading from for change data capture is effectively a streaming source. The source itself is event-driven. Every new change to the database gets written to that log as an event. That lends itself very well to streaming.”

Streamkap also incorporates an incremental snapshot model, which is useful for ensuring all the data, and the data’s changes, have been moved from source to target. It’s particularly useful for its assistance in the backfill process for target systems.

“For a backfill, you want to be able to capture your new streaming events in parallel with it, so that those things aren’t dependent on one another, and make sure that the backfill is not putting too much load on the source database,” Dudley explained. “We do both of those things.” Moreover, because of the resiliency afforded by Kafka, users don’t have to backfill as frequently as they do with batch ETL processing methods.

## Schema Drift Support
In addition to its historical snapshots, Streamkap also provides a schema drift support feature that allows for changes to schema without slowing or breaking [data pipelines](https://thenewstack.io/simplified-data-pipelines-with-pulsar-transformation-functions/). When developers want to alter schema by say, adding a column, those changes are smoothly propagated to the downstream data model in a streamlined manner.

“What our system does, it automatically accounts for new columns, or new changes in data type, and ensures your data continues flowing without having to stop if a change gets made,” Dudley mentioned.

Streamkap also provides in-app alerting capabilities paired with automatic monitoring to notify users of changes. These mechanisms are “designed to keep customers up to date if there’s been changes on the actual pipeline itself, if there’s any issues,” Dudley revealed.

## In Proper Perspective
By scaffolding its platform atop Flink and Kafka, Streamkap employs some of the most modern and effectual tools for transforming and transporting streaming data. The fact that it’s positioned as a streaming ETL tool illustrates the longstanding nature of the ETL model, its continuing enterprise relevance and its inevitable transition from batch to real-time applicability.

Batch processing may yet endure across the data ecosystem, particularly for organizations still using legacy systems. However, the need to hasten the data integration requirement so that it occurs at the pace of contemporary consumer and business demands is readily apparent — and manifest in Streamkap’s recent funding, if not its very presence.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)