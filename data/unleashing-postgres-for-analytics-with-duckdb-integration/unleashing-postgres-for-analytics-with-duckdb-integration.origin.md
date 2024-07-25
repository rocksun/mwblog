# Unleashing Postgres for Analytics With DuckDB Integration
![Featued image for: Unleashing Postgres for Analytics With DuckDB Integration](https://cdn.thenewstack.io/media/2024/07/57a43fe6-duckling-8062337_1280-1024x683.jpg)
The Postgres ecosystem is winning, making it a [preferred choice for developers](https://survey.stackoverflow.co/2023/#technology-most-popular-technologies) for new data workloads and database tools. Much has been written on [“why” Postgres is winning, ](https://www.crunchydata.com/blog/when-did-postgres-become-cool)and there are a number of good reasons — including its extensibility — enabling Postgres to extend to new use cases as requirements emerge, demonstrated by [pg vector](https://github.com/pgvector/pgvector)‘s ability to address a variety of AI requirements.

Despite its popularity for [OLTP](https://thenewstack.io/how-data-integration-is-evolving-beyond-etl/) workloads, [Postgres](https://thenewstack.io/postgres-is-now-a-vector-database-too/) has remained a stretch for performant analytics on larger data sets (OLAP). While there are a number of solutions that modify core Postgres to address OLAP workloads or that use portions of Postgres, each comes with inherent challenges, costs, and limitations associated with using a fork of Postgres.

With Postgres users increasingly looking for Postgres-native solutions to OLAP requirements, trends towards low-cost storage as the center of gravity for data, and the emergence of new standards for data formats, Crunchy Data set out to develop a new solution to extend Postgres to meet these needs. Our solution leverages the known power of Postgres extensions, with an emerging winner in embedded fast query engines — [DuckDB](https://duckdb.org/).

**Love Postgres, Need Analytics**
We help a wide variety of organizations deploy Postgres. From this vantage point, users successfully deploy Postgres for various use cases. In fact, when we are questioned about the use cases Postgres addresses, we have a hard time answering because the answer is that we have really seen them all.

But that is in an OLTP context. OLAP has historically been “the other workload” where Postgres didn’t compete. Yes, there are some solutions out there, but in particular, as users move to the cloud and cloud native approaches, there are not many Postgres-native solutions.

We have seen this most pointedly firsthand: Many [Crunchy Bridge](https://crunchybridge.com/login) customers — who love Postgres — were using Postgres for the OLTP workloads but using a combination of tools to replicate their data to various third-party analytic platforms for analytic queries. In talking to these customers about their requirements, they weren’t happy with moving the data out of Postgres but did not have a great alternative. Could we build one?

**Processing Data Where It Lives, Analytics on Data in S3**
To build a solution for Postgres-native analytics — it was clear that we needed a solution that addressed data where it lives and in the modern formats organizations use. Two significant trends shaped our direction:

- Data increasingly lives in S3. S3 — and similar cloud storage repositories — have exploded in adoption as low-cost, durable storage. They can scale to infinity and are accessible from anywhere. Users can expose their data to many different engines at the same time.
- Open standards for file and table formats are the emerging winners. While many data lakes remain “CSV files in S3,” analytics-optimized formats like Parquet and Iceberg are quickly gaining popularity.
Of course, the prospect of separating the query engine (compute) from the storage (data) has given rise to a number of database projects. This enables storing data in one place at a low cost while efficiently querying the data without moving it to the query engine.

Ultimately, we concluded that S3 is (with caching) the appropriate storage layer for analytical data, and solid S3 integration into PostgreSQL provides the means to address these use cases.

**Postgres Extensibility Once Again Makes It a Winner **
Postgres extensions enable Postgres to address new use cases as requirements emerge. Postgres becomes the leading database for managing spatial data by loading the PostGIS extension. Postgres can support advanced sharding with Citus or transform it into a vector database with pgvector. Every Postgres user has their favorite extension, and many likely use a collection of extensions without considering the power of the Postgres extension framework.

Extending Postgres to support an [external query engine fully takes advantage of this extension capability](https://www.crunchydata.com/blog/how-we-fused-duckdb-into-postgres-with-crunchy-bridge-for-analytics). Using Postgres ‘hooks, we can transparently break down a query plan into parts that can be “pushed down” into this external separate query engine, enabling us to take advantage of the benefits of a specialized engine for these particular workloads. In this specific case, we use DuckDB, an emerging winner in the embedded query engine space.

For those who are less familiar, DuckDB was developed by Hannes Mühleisen and Mark Raasveldt at the Centrum Wiskunde & Informatica (CWI) and actively developed by DuckDB Labs with many community contributions. DuckDB has become a leading embeddable query engine, using modern OLAP techniques to run fast queries against Parquet and files in object storage. Parquet files support compressed columnar data, making that format well-suited for archiving historical time series rows out of transactional Postgres and into an efficient form for long-term OLAP use.

That means we can integrate DuckDB with Postgres by using Postgres extensions, recognizing the parts of the query plan that can be pushed down into DuckDB for vectorized, parallel execution, and constructing the appropriate SQL queries to pass to DuckDB. Again, we use a combination of PostgreSQL hooks to achieve that for filters, aggregates, joins, and more complex query structures. In some cases, the entire query can be pushed down; in others, we merge different subplans.

**Benefits of a Postgres-Native Solution**
But why Postgres for analytics? As Postgres adoption grows and users of all types learn Postgres for application development and OLTP requirements, providing a Postgres-native experience for these analytical queries has a number of benefits.

As a user, your data in S3 will appear as tables that you can query along with all your standard PostgreSQL tables and use in combination with the general simplicity of other PostgreSQL features and extensions, including:

- access controls
- views
- materialized views
- query performance insights with pg_stat_statements
- stored procedures with PL/pgSQL ()
- periodic jobs with pg_cron
- long-lived NVMe and in-memory caches
- dashboard tools
If extending Postgres to support an external query engine for analytic queries sounds a bit complicated, that is probably true. That said, by offering the result as a managed service, users can benefit from the power of this solution without having to worry about low-level details like hooks or query pushdowns. From a user perspective, all you see is the ability to quickly expose your data living in S3 to be queried using standard Postgres. Crunchy Bridge provides the full benefit of managed production-ready Postgres with a developer-focused UX, now with extended capabilities to support fast analytic queries powered by DuckDB.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)