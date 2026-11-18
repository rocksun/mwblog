![In this episode of The New Stack Podcast, Pedro Holanda, lead DuckLake developer and principal engineer at DuckLake, discusses how the open-source table format reduces complexity, improves performance, and makes large-scale data management more accessible.](https://cdn.thenewstack.io/media/2026/11/b52163ee-for-thumbnail-25-1024x576.png)

How much simpler could a data lakehouse get if an ordinary SQL database kept track of its files? That’s the question in this episode of *The New Stack* podcast.

DuckLake is an open-source table lakehouse format created by Amsterdam-based [DuckLabs](https://duckdb.org) that acts as a traffic cop for data management by storing table metadata inside a standard SQL database, rather than scattering manifest files across object storage. Unlike traditional table formats, DuckLake treats lakehouse metadata as a relational database problem. These advanced data lake features, served by Parquet files and SQL databases, reduce the traditional lakehouse complexity.

VIDEO

In October, DuckLake 1.1 launched alongside [DuckDB 2.0.0 LTS](https://duckdb.org/2026/10/21/announcing-duckdb-200). *The New Stack* sat down with [Pedro Holanda](https://www.linkedin.com/in/pdet/), lead DuckLake developer and principal engineer at DuckLabs at their Amsterdam headquarters, to talk about the launch. Holanda has contributed to the [DuckDB open-source project](https://github.com/duckdb/duckdb) since it was an early research prototype, and shares the full evolution of DuckLake to our conversation.

“These lakehouse formats exist so people can exchange their database systems without having to do migrations,” Holanda tells *The New Stack*. Because of the complexity, “you need a database system to keep track of which table has its last version.”

DuckLake applies decades of research, Holanda says, in order to reduce files and therefore complexity at a time of rapid data growth, taking advantage of how everyone who uses database systems is familiar with SQL and how schemas work.

“The simplicity is the way you fetch your data,” Holanda says of DuckLake. “You’re going to issue queries somewhere. The server is going to answer these questions back, and you know exactly which Parquet files you have to read. So the Parquet files don’t change. Just the catalog.”

Maintainers of your data lake often have many maintenance tasks to perform. If you end up with many files, he says, DuckLake lets you glue them into one file to reduce the number of requests. This can also be done across multiple snapshots, further reducing the number of files. It also solves the “small files problem” in streaming data lakes and lakehouses by using inlining and flushing.

Whereas for traditional data lakes, across multiple data sources being inserted at a time, “you end up with so many files, so when you have to query it, you’re going to have to traverse a bunch of metadata files just to figure out which Parquet files you need to read, and then you’re going to have a bunch of Parquet files to read as well,” Holanda says, slowing everything down and frustrating the developer.

DuckLake is known to be fast, simple to use, and not requiring massive server clusters to run. Part of that comes from Parquet being very similar to DuckDB storage: both are columnar and organized in row groups, which keeps the massaging step to a minimum.

“One thing that we realized when we were building DuckLake is that, ‘Hey, we have a database system now, we have a catalog; what if we do this radical idea of storing data on tables?'” he says. “With DuckLake, you get your actual data representation as a table in a catalog, and we call this inlining.”

> “With DuckLake, you get your actual data representation as a table in a catalog, and we call this inlining.”

During Amazon’s Q3 earnings call in late October, CEO Andy Jassy called out the complexity of moving data between data stores and analytics engines, especially as AWS customers’ data generation continues to increase. Amazon is famous for dogfooding, and Jassy pointed to DuckDB’s solution to this complexity as a reason for [its DuckLabs acquisition](https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/).

“With our acquisition of DuckLabs, DuckDB will become the universal SQL dialect of AWS storage and analytics, simplifying data processing with a modern analytics engine that is fast, simple to use and ubiquitous, and where customers will be able to write SQL queries once and then execute using any AWS analytics service,” Jassy said. “For the first time in analytics, customers will have zero migration or portability costs between query engines. This is a big deal, and you can imagine how it will also help agents do efficient querying as well.”

DuckDB and DuckLake remain free and open source under the MIT license, overseen by the independent DuckDB Foundation.

Overall, this recent DuckLake release pairs new features with more than 200 bug fixes for quality and stability, and it runs natively in DuckDB.

The post [DuckLake 1.1 solves the absurd complexity of data lakes at AI scale](https://thenewstack.io/ducklake-sql-lakehouse-metadata/) appeared first on [The New Stack](https://thenewstack.io).