All those AI Agents will that will soon be swarming about will need fresh data, which is causing the data platform community to urgently think about ways to better inject analytics directly into decision-making processes.

In October, [Databricks](https://thenewstack.io/databricks-launches-a-no-code-tool-for-building-data-pipelines/) quietly [acquired](https://www.databricks.com/blog/mooncake-labs-joins-databricks-accelerate-vision-lakebase) a technology that will provide a crucial piece to its emerging [Lakebase platform](https://www.databricks.com/product/lakebase) for AI agents: Mooncake, a single package that supports both rich transactional processing and fast columnar analysis.

Selling point? No [ETL pipelines](https://thenewstack.io/aws-makes-etl-disappear-for-aurora-postgresql-dynamodb/) to manage. From within PostgreSQL itself, data can be tapped into for making routing decisions in the transaction process.

Lakebase is a serverless [Postgres](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) service integrated into the company’s [Lakehouse managed data platform](https://thenewstack.io/lakebase-is-databricks-fully-managed-postgres-database-for-the-ai-era/). It is optimized for AI agents (especially the company’s own [Agent Bricks](https://thenewstack.io/databricks-launches-agent-bricks-its-new-no-code-ai-agent-builder/)).

Databricks [purchased](https://techcrunch.com/2025/05/14/databricks-to-buy-open-source-database-startup-neon-for-1b/) serverless PostgreSQL provider Neon in May for $1 billion. This gave the company a PostgreSQL-based transactional platform, one that, [according to Databricks](https://www.databricks.com/blog/databricks-neon), decoupled compute from storage.

The next piece of the puzzle: Mooncake.

## OLTP and OLAP: Torn Asunder

Mooncake was developed by Mooncake Labs, a start-up by three ex-SingleStore engineers to rethink how a combined transactional and analytics database system might operate.

Traditionally, transactional database systems ([OLTP](https://thenewstack.io/new-oltp-postgres-with-separate-compute-and-storage/)) and  analytics database systems ([OLAP](https://thenewstack.io/data-telemetry-is-the-lifeline-of-modern-analytics-and-ai/)) have been run separately from one another (and often by separate departments) within the enterprise.

The commonly-held fear has been that the latency time of transactional processing — which needs to be fast — would be compromised by some long and/or computationally-heavy analytics jobs running on large data sets.

So put OLTP, with its microsecond insert times needed for speedy transactions, over here; and the OLAP system, with its ability to scan massive tables for large-scale analysis, over yonder.

This separation has since become burdensome. Because the two need to exchange data.

“The users are forced to manually duct tape them together with complex and fragile data pipelines that takes hours to sync and sometimes transform data into something that’s hard to read,” explained Mooncake Labs co-founder [Cheng Chen](https://www.linkedin.com/in/cheng-ch/), in a lecture at Carnegie Mellon University’s Database Group’s [Future Data Systems Seminar Series](https://db.cs.cmu.edu/2025/09/future-data-systems-seminar-series-fall-2025/).

Network speeds and computational heft have come to such where combining OLTP and OLAP could be a good idea, in that it opens a whole new vista of how transactions can be handled.

## OLTP and OLAP: Together Forever

Chen was one of three co-founders who came from [SingleStore](https://www.singlestore.com/?utm_content=inline+mention), which offers a Hybrid Transactional/Analytical Processing (HTAP) database system of the same name (formerly MemSQL).

A distributed database system, SingleStore [unifies](https://thenewstack.io/singlestore-offers-fast-vector-processing-for-real-time-ai/) transactional and columnar analytics, as a way to combine these two types of data stores. With a single engine, it uses working memory for transactional rows and disk for column storage. It scales well, and can support multiple formats such as JSON, full-text and vector.

But SingleStore’s design is monolithic, Chen lamented. Because it is run as a single stand-alone query engine, it must compete with the best of both OLTP and OLAP engines already in use. And those willing to adopt an entirely new database system simply to get the benefits of fast analytics on fresh data (for actions such as fraud detection) are relatively few in number.

## Mooncake Bridges PostgreSQL and Iceberg Engines

Instead of trying to build “a magical engine” (Chen’s words) that does both kinds of processing, why not just recreate the functionality as a feature for existing systems?

Mooncake set out to build a “composable” hybrid database system, Chen said.

It is a framework and set of new features built on top of existing OLTP systems and OLAP formats.

The engineering team chose to support PostgreSQL for transactions, for its runaway popularity as an open source database system.

On the analytics side, they went with the open lakehouse formats of [Apache Iceberg](https://thenewstack.io/architects-guide-to-apache-iceberg/) and (Databricks’ own) [Delta Lake](https://thenewstack.io/delta-lake-a-layer-to-ensure-data-quality/), so that data in either of these formats can be accessed by any conversant engine ([DuckDB](https://thenewstack.io/duckdb-in-process-python-analytics-for-not-quite-big-data/), [StarRocks](https://thenewstack.io/starrocks-launches-beta-of-cloud-service-for-its-analytics-engine/), [Trino](https://thenewstack.io/speed-trino-queries-with-these-performance-tuning-tips/), [Apache Spark](https://thenewstack.io/enhancing-the-flexibility-of-sparks-physical-plan-to-enable-execution-on-various-native-engines/)).

## Mooncake: Not an Engine, Just a Feature

Mooncake has two main components. One (“moonlink”) is a real-time layer on top of Iceberg that allows for a “sub-second ingestion” of data.

The second component (“pg\_mooncake”) provides HTAP capability for PostgreSQL, allowing users to add analytical functions to determine transactional routing decisions.

Together, they provide a step forward in the endless divide of transactional and analytics systems, making a bridge to a world of new possibilities from fast analytics. The agents will be pleased.

Check out Chen’s entire talk for a technical deep dive into the challenges of getting Mooncake play nicely with both Iceberg and PostgreSQL:

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)