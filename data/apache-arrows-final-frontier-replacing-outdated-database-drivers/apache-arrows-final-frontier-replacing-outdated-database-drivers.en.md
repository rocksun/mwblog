In the past decade, there has been a [Cambrian-sized explosion](https://evolution.berkeley.edu/the-cambrian-explosion/) of new [analytics-oriented databases](https://thenewstack.io/clickhouse-optimizing-real-time-data-analysis-with-online-analytical-processing/) and [query engines](https://thenewstack.io/snowflake-polaris-aims-for-multiquery-engine-interoperability/), yet the protocols these systems use to transfer data among one another were built for mining row-oriented transfers from transactional systems.

It’s a mismatch that slows down transfers and consumes excessive CPU usage.

Many of these analytical systems use ODBC (Open Database Connectivity), or its Java offshoot JDBC, as a conveyor, or DB-API for Python. But these all protocols copy data from the source by rows, and not by columns, which would be the natural format for a column-oriented database, noted [Ian Cook](https://www.linkedin.com/in/ianmcook/), a core contributor to the [Apache Arrow](https://thenewstack.io/introduction-to-apache-arrow/) open source analytics data framework.

Cook is one of a group of Arrow-savvy engineers who have just launched a company, called [Columnar](https://columnar.tech/), to defeat this communication bottleneck, using the ADBC (Arrow Database connectivity) as the connective API and protocol, which in turn uses the Apache Arrow format.

The company has gathered $4 million in seed funding, and last week formally released the first batch of ADBC drivers, as well as [DBC](https://columnar.tech/dbc), a command-line interface and associated tools for downloading, installing, loading, and configuring ADBC drivers for different environments.

Arrow has been “a big success story, but there’s this final frontier that Arrow has just begun to cross in the last couple of years, and that is displacing the dominant data connectivity standards like ODBC and JDBC, which are growing quite outdated and are grossly inefficient for data analytics applications in particular,” Cook said, in an interview with TNS. “And that’s what we’re working on at Columnar.”

[![](https://cdn.thenewstack.io/media/2025/11/4ad5afd7-dbc.jpg)](https://cdn.thenewstack.io/media/2025/11/4ad5afd7-dbc.jpg)

## Understanding Apache Arrow’s Columnar Format

[Apache Arrow](https://thenewstack.io/apache-arrow-designed-accelerate-hadoop-spark-columnar-layouts-data/) is a massively popular binary format for columnar data exchange created in 2016 by [Wes McKinne](https://wesmckinney.com/)y (who also originated [Python Pandas](https://thenewstack.io/python-pandas-ditches-numpy-for-speedier-pyarrow/)). It [provided a way](https://arrow.apache.org/blog/2025/01/10/arrow-result-transfer/) to [write columnar data contiguously](https://arrow.apache.org/docs/format/Columnar.html) into working memory. Applications could share data there with zero copying, and queries could be answered more quickly.

Arrow responds to a sea change in how most database data is used, shifting emphasis from rows to columns.

The traditional data copying mechanism copies data by rows. Each row from a customer could represent a customer, with individual fields for the *address*, *phone number* and *gender*. If the boss wanted a list of all the subscribers, copying them out row by row made sense.

But as analyzing this data has become more of a thing, analysts found that they may have only needed one or two specific fields, or columns (such as ones for *zip code* and *gender*).

Moving this data into another system, or presenting it as the results for a query, a database driver would copy the column one field at a time, after scanning over the entire row.

In what is essentially a streaming process, Arrow copies just the needed columns over into working memory, essentially eliminating the serialization and deserialization  process.

Thus, Arrow [became widely used](https://thenewstack.io/how-apache-arrow-is-changing-the-big-data-ecosystem/) to exchange data across applications written in different languages, and connectors were made for nearly every language and platform.

[![](https://cdn.thenewstack.io/media/2025/11/0116216d-part-1-figure-1-row-vs-column-layout.png)](https://cdn.thenewstack.io/media/2025/11/0116216d-part-1-figure-1-row-vs-column-layout.png)

From the Arrow documentation.

## Introducing ADBC: The Arrow Database Connectivity Protocol

Just as ODBC is the glue for tying together separate relational database systems, ADBC is set up to be the *lingua franca* for analytical database systems, offering a high-speed connection between them, using Arrow.

Cook and his colleagues, then working at SQL engine provider [Voltron Data](https://voltrondata.com/about),  started work on ADBC as an API for querying databases and data stores and getting back results in the Arrow format.

The canonical version of the specification is written in c *cadbc.h*, and there are dialects for other languages.

Early work has generated a lot of interest: Connectors have been built for BigQuery, Dremio, Databricks, and [Snowflake](https://www.tigrisdata.com/?utm_content=inline+mention).

Snowflake and [DuckDB](https://thenewstack.io/duckdb-in-process-python-analytics-for-not-quite-big-data/) both adopted the API DuckDB found that it reduced query times by more than 90% in many applications. Microsoft adopted it for PowerBI.

## Columnar’s Role in Driving ADBC Adoption

For its launch, Columnar has released ADBC drivers — for Amazon Redshift, MySQL, Microsoft SQL Server, and Trino — and revealed plans for supporting more databases, query engines, and data platforms.

Looking to future opportunities, Arrow could also work in the AI space as well, Cook [posited in a blog post](https://columnar.tech/blog/announcing-columnar/), explaining that this format far surpassed the throughput of JSON-RPC, scoffing at its woefully inefficient base64 encoding. The CUDA ecosystem for GPUs is built around a tabular data model, which could benefit from faster load times as well.

“Over the next year or two, we’re going to be talking to a lot of companies in that space and and trying to pitch them on the benefits of using Arrow,” Cook said.

Columnar’s $4 million seed round was led by Bessemer Venture Partners.

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