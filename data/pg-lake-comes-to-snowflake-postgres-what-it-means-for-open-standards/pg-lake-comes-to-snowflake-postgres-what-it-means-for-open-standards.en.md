The [pg\_lake extension](https://www.snowflake.com/en/engineering-blog/pg-lake-postgres-lakehouse-integration/), which was initially released to the open source community in November, is now natively available in [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) Postgres, the cloud data warehouse’s fully managed [PostgreSQL](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) service. pg\_lake is a collection of approximately 15 extensions enabling users to employ PostgreSQL as a data lakehouse. It supports Apache Iceberg tables for rapid queries and transactional workloads; organizations can also use pg\_lake with data in object stores.

[Snowflake Postgres](https://www.snowflake.com/en/developers/guides/getting-started-with-snowflake-postgres/) unifies analytical and transactional workloads by allowing users to access PostgreSQL directly within Snowflake. Consequently, they can read and write to open table formats via SQL; [pg\_lake](https://github.com/Snowflake-Labs/pg_lake/blob/main/README.md) abstracts most of the underlying complexity required to manipulate data of different types and formats.

Snowflake also announced its expansion of [Snowflake Horizon Catalog](https://www.snowflake.com/en/product/features/horizon/), its data discovery, metadata context, and data governance layer, to include the management of data assets accessed through external query systems, like Apache Spark. Additionally, its open data sharing features — applicable across varying clouds and availability zones — now apply to data in Delta Lake and Iceberg tables.

The vendor also revealed a new integration with Microsoft One Lake that provides secure, bi-directional read capabilities for data in Snowflake and Microsoft Fabric.

The interoperability of these features and pg\_lake’s inclusion in Snowflake Postgres not only applies to different data types, formats, clouds, and regions, but also to OLAP, OLT, and advanced machine learning applications.

“You don’t even have to know that it’s Iceberg under the covers, if you’re a customer,” commented [Craig Kerstiens](https://www.linkedin.com/in/craigkerstiens/), director of software engineering for Postgres, Snowflake. “If you just want Postgres, it’s just Postgres. But, it has these superpower capabilities under the covers, with this unified Iceberg catalog, this kind of vectorized engine embedded in, and this easy ability to move data from one to the other.”

## pg\_lake’s extensions

The utilitarian nature of pg\_lake impacts several facets of the application development and deployment lifecycle. By making it accessible through [Snowflake Postgres](https://docs.snowflake.com/en/en/user-guide/snowflake-postgres/about), that lifecycle readily shifts between analytical and transactional workloads that can involve open table formats. The respective extensions contained in pg\_lake include dedicated measures for:

* **Version management:** Version management is of paramount importance for updates and maintenance. In Snowflake Postgres, users are contending with different operating systems, versions of Postgres, libraries, and more. Updating one component without incurring unnecessary downtime and reworking of other components can be laborious. According to Kerstiens, “We’ve got an extension inside pg\_lake that’s responsible for managing all the other extensions. So, when you upgrade library B it won’t conflict with library C.”
* **Data type and format conversions:** The ability to employ SQL as the lingua franca for interacting with the myriad data types in Postgres, including geospatial data, vector embeddings, and more, with that found in Iceberg tables, is as invaluable as it is complex to wrangle together. pg\_lake, however, accomplishes this task for joins, reads, and writes so that, “You’re just writing a SQL query,” Kerstiens said. “You never thought about these other extensions, or this complexity and everything that happened under the hood.”
* **Caching:** Optimizing performance with caching strategies is critical to the success of low latency applications. According to Kerstiens, pg\_lake has mechanisms that “will do the caching for you.” For example, if a user is writing Iceberg files and new files come in, the system can cache the newer ones. There are also mechanisms for optimizing joins and queries with pushdowns. These and other features contributed to Kerstiens’ characterization of Snowflake Postgres as “production-grade, enterprise ready.”

## Open data governance

Snowflake’s utility for [Iceberg](https://iceberg.apache.org/) and open standards also increased with the new functionality in Snowflake Horizon Catalog, which can now manage Iceberg tables the same way it does those in Snowflake’s native storage format. By allowing external query engines like [Trino](https://thenewstack.io/speed-trino-queries-with-these-performance-tuning-tips/) and others to read tables (this capability is in GA) managed by the catalog and write to them (which, according to [Prasanna Krishnan](https://www.linkedin.com/in/prasanna-krishnan-1944aa1/), head of apps, collaboration and Horizon at Snowflake, will be in public preview soon), users get several advantages. “They get a single source of truth of their data,” Krishnan noted. “They don’t have to create copies of it.”

Moreover, they can also extend the access controls of Snowflake Horizon Catalog to those query engines. With this paradigm, organizations query the data directly through Snowflake, which relies on the catalog’s access controls to filter the results accordingly. Thus, one can stipulate a masking policy “on a column so when a privileged user queries this column they can see it and an average analyst can only see it masked,” Krishnan said. “Or, it can be a row access policy in which I only restrict which rows are accessible to which roles.”

## Open data sharing

Snowflakes’ data sharing characteristics, which don’t involve copies, are another useful feature the vendor provides. Previously, this feature was only for objects and tables in Snowflake’s proprietary data format. At present, it’s applicable to [Delta Lake](https://delta.io/) and Iceberg tables. This attribute becomes particularly useful for applications in which different parties are employing respective clouds and are in different geographic regions.

Snowflake’s open data sharing allows them to still access the same data “if you don’t want to move the data or replicate it,” Krishnan said. “Consumers aren’t spending egress costs moving data to a different region every time you query it. Under the hood we use secure, cross-cloud auto-movement to have the data be available in the region where the users are and it’s queried.”

## Extensible, open standards

Snowflake’s expansion of its open data sharing and Horizon Catalog features to include open table formats and external query engines signifies its current focus on open standards. The interoperability furnished by these advancements, as well as by buttressing Snowflake Horizon Catalog with pg\_lake, makes it much easier for developers to work with the tools and formats that are most meaningful to their applications — as opposed to which ones are dictated by vendors.

This fact is particularly true for the data lakehouse capabilities of pg\_lake, which reinforces the analytical and transactional support delivered by Snowflake Postgres. “OLTP and OLAP have always lived in different worlds,” Kerstiens commented. “One is row based; one is columnar. One is point lookups; the other is large scans. They live in different worlds and now we’re starting to bridge that gap and unify them.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/ee3e39b7-cropped-52925a32-jelani-harper-110x110-1.jpg)

Jelani Harper has worked as a research analyst, research lead, information technology editorial consultant, and journalist for over 10 years. During that time he has helped myriad vendors and publications in the data management space strategize, develop, compose, and place...

Read more from Jelani Harper](https://thenewstack.io/author/jelani-harper/)