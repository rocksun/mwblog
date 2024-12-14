# Apache Pinot Brings Real Time Analysis to Columnar Data
![Featued image for: Apache Pinot Brings Real Time Analysis to Columnar Data](https://cdn.thenewstack.io/media/2024/12/7e09e53c-pinot-1024x683.png)
Apache Pinot began life as a project within LinkedIn in 2013 as a way to run an analysis against a single metric captured across millions of users of all of the services.

The company had already developed[ Apache Kafka](https://thenewstack.io/why-we-use-apache-kafka-for-real-time-data-at-scale/) to manage the millions of messages its systems were producing each day. Still, this task wasn’t just a message-passing problem but one of analyzing a single column of data, one similar to “who viewed each user’s profile?” quickly enough so it would be useful to its users in real-time.

The feature was originally developed on a combination of Elasticsearch and an online transactional processing (OLTP) database, but it involved running thousands of servers concurrently to get the answer, an expensive proposition.

With Pinot, the company’s engineers were able to bring the number of servers needed down to around 75.

Pinot was born to solve the problem of “running analytical queries for hundreds of millions of users at scale, in a low-cost manner,” explained [Chinmay Soman](https://www.linkedin.com/in/chinmay-soman/), head of product for [StarTree](https://startree.ai/about), which offers a fully managed cloud native version of Pinot.

Pinot brings “simplification in the data stack,” Soman said in an interview with TNS. “The problem is not new. It’s been solved by many legacy technologies. What Pinot brings is the simplification and the scale for these problems.”

## Real-Time Analytics
The technology was quickly picked up by other webscale companies, such as Uber, Google, DoorDash and Stripe. About 1,000 organizations are using the open source version of the software.

Stripe, which does billions of transactions a day, uses Pinot to give payment analysis data back to its merchants: cashflow analysis, late collection payments, revenue-per-user, and so on.

Think of [Apache Pinot](https://pinot.apache.org/) as a combination of analytical and traditional transactional databases. “It’s built an analytical database but can handle the scale of an OLTP database.” It can do large-scale analysis on [Google BigQuery](https://thenewstack.io/bigquery-pricing-a-users-guide/) or [Snowflake](https://thenewstack.io/snowflake-consolidates-platform-expands-ai/) but at a fraction of the time.

Pinot can process hundreds of thousands of [SQL-based](https://thenewstack.io/how-to-write-sql-queries/) queries per second with less than 99-millisecond latency, which is a throughput that even MySQL scaled out to thousands of nodes could match, Soman said. And some of the largest Pinot deployments are indexing up to a million events per second.

Pinot was [open sourced](https://thenewstack.io/reimagining-observability-the-case-for-a-disaggregated-stack/) in 2015 and was first accepted by Apache in 2018. Version 1 of Pinot [was released in September 2023](https://startree.ai/resources/query-time-joins-in-apache-pinot-1-0) and added the ability to do [query-time joins of two tables](https://startree.ai/resources/query-time-joins-in-apache-pinot-1-0), as well as the ability to do “upserts,” a combination of UPDATE and INSERT[ that ensures](https://startree.ai/resources/real-time-upserts-in-apache-pinot-and-startree-cloud) the latest data is either added or updated to the database.

## A Serving Layer for Data
One can think of Pinot as a serving layer for data. Data can be stored in an object store such as [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)‘ Simple Storage Service (S3), and perhaps formatted with [Apache Iceberg](https://thenewstack.io/apache-iceberg-a-different-table-design-for-big-data/).

“Kafka is semi-stateful,” Soman explained, “It will store data for one week, but it is not designed to store stateful data. With Pinot, you can store data wherever you want and query individual items.”

Nor is Kafka an analytics engine. Even [Apache Flink](https://thenewstack.io/how-apache-iceberg-and-flink-can-ease-developer-pain/), often used with Kafka, is designed for more processing and filtering. In fact, all three tools can be used together in a stack referred to as the KFP stack.

[On GitHub](https://github.com/startreedata/pinot-recipes), StarTree offers a series of recipes on where Pinot would be a good fit for tasks such as:
- Batch data ingestion
- Streaming ingestion
- Upserts
- Geospatial processing
- transformation functions
- Similarity search (AI)
In November, StarTree updated its [StarTree Cloud](https://startree.ai/products/startree-cloud) service to include role-based access control (RBAC), pauseless ingestion, schema evolution and data backfill.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)