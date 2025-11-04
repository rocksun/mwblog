
<!--
title: Apache Arrow的终极前沿：告别过时数据库驱动
cover: https://cdn.thenewstack.io/media/2025/11/01917682-columnar-2.jpg
summary: 现有协议传输慢，Columnar公司推出ADBC，利用Apache Arrow的列式格式，旨在为分析型数据库提供高效数据连接，解决数据传输瓶颈。
-->

现有协议传输慢，Columnar公司推出ADBC，利用Apache Arrow的列式格式，旨在为分析型数据库提供高效数据连接，解决数据传输瓶颈。

> 译自：[Apache Arrow's Final Frontier: Replacing Outdated Database Drivers](https://thenewstack.io/apache-arrows-final-frontier-replacing-outdated-database-drivers/)
> 
> 作者：Joab Jackson

在过去十年中，新的[面向分析的数据库](https://thenewstack.io/clickhouse-optimizing-real-time-data-analysis-with-online-analytical-processing/)和[查询引擎](https://thenewstack.io/snowflake-polaris-aims-for-multiquery-engine-interoperability/)出现了[寒武纪规模的爆发](https://evolution.berkeley.edu/the-cambrian-explosion/)，然而这些系统之间用于数据传输的协议却是为从事务系统中挖掘面向行的传输而构建的。

这种不匹配导致传输速度变慢并消耗过多的CPU使用。

许多此类分析系统使用ODBC（开放数据库连接）或其Java分支JDBC作为载体，或使用DB-API for Python。但Apache Arrow开源分析数据框架的核心贡献者Ian Cook指出，所有这些协议都是按行而不是按列从源复制数据，而按列复制本应是面向列数据库的自然格式。

Cook是一群精通Arrow的工程师之一，他们刚刚成立了一家名为[Columnar](https://columnar.tech/)的公司，旨在使用ADBC（Arrow数据库连接）作为连接API和协议来克服这一通信瓶颈，ADBC又使用了Apache Arrow格式。

该公司已筹集到400万美元的种子轮资金，并于上周正式发布了第一批ADBC驱动程序，以及[DBC](https://columnar.tech/dbc)——一个命令行界面和相关工具，用于下载、安装、加载和配置不同环境下的ADBC驱动程序。

Cook在接受TNS采访时表示：“Arrow是一个巨大的成功案例，但Arrow在过去几年才刚刚开始跨越一个最终的边疆，那就是取代ODBC和JDBC等主导的数据连接标准，这些标准正变得相当过时，并且对于数据分析应用程序来说效率极低。这正是我们在Columnar公司努力的方向。”

[![](https://cdn.thenewstack.io/media/2025/11/4ad5afd7-dbc.jpg)](https://cdn.thenewstack.io/media/2025/11/4ad5afd7-dbc.jpg)

## 理解Apache Arrow的列式格式

[Apache Arrow](https://thenewstack.io/apache-arrow-designed-accelerate-hadoop-spark-columnar-layouts-data/)是一种广受欢迎的用于列式数据交换的二进制格式，由Wes McKinney（也是[Python Pandas](https://thenewstack.io/python-pandas-ditches-numpy-for-speedier-pyarrow/)的创始人）于2016年创建。它[提供了一种](https://arrow.apache.org/blog/2025/01/10/arrow-result-transfer/)[将列式数据连续写入](https://arrow.apache.org/docs/format/Columnar.html)工作内存的方法。应用程序可以在那里零复制地共享数据，查询可以更快地得到响应。

Arrow响应了大多数数据库数据使用方式的巨变，将重点从行转移到列。

传统的数据复制机制按行复制数据。来自客户的每一行可能代表一个客户，包含地址、电话号码和性别等独立字段。如果老板想要一份所有订阅者的列表，逐行复制是合理的。

但是，随着对数据分析的需求日益增长，分析师发现他们可能只需要一个或两个特定字段或列（例如邮政编码和性别）。

将这些数据移至另一个系统，或将其作为查询结果呈现时，数据库驱动程序会在扫描整个行之后，一次复制一个字段。

Arrow通过一个本质上是流式处理的过程，只将所需的列复制到工作内存中，从根本上消除了序列化和反序列化过程。

因此，Arrow[被广泛使用](https://thenewstack.io/how-apache-arrow-is-changing-the-big-data-ecosystem/)以在用不同语言编写的应用程序之间交换数据，并且几乎为所有语言和平台都创建了连接器。

[![](https://cdn.thenewstack.io/media/2025/11/0116216d-part-1-figure-1-row-vs-column-layout.png)](https://cdn.thenewstack.io/media/2025/11/0116216d-part-1-figure-1-row-vs-column-layout.png)

来自Arrow文档。

## 引入ADBC：Arrow数据库连接协议

正如ODBC是连接独立关系数据库系统的粘合剂一样，ADBC旨在成为分析数据库系统的通用语言，利用Arrow在它们之间提供高速连接。

Cook和他的同事当时在SQL引擎提供商[Voltron Data](https://voltrondata.com/about)工作，他们开始研发ADBC，将其作为一种API，用于查询数据库和数据存储，并以Arrow格式返回结果。

该规范的规范版本以 `c *cadbc.h` 编写，并有其他语言的方言。

早期工作引起了广泛关注：已经为BigQuery、Dremio、Databricks和[Snowflake](https://www.tigrisdata.com/?utm_content=inline+mention)构建了连接器。

Snowflake和[DuckDB](https://thenewstack.io/duckdb-in-process-python-analytics-for-not-quite-big-data/)都采用了该API。DuckDB发现它在许多应用程序中将查询时间减少了90%以上。Microsoft在PowerBI中也采用了它。

## Columnar在推动ADBC普及中的作用

为了推出其产品，Columnar发布了适用于Amazon Redshift、MySQL、Microsoft SQL Server和Trino的ADBC驱动程序，并公布了支持更多数据库、查询引擎和数据平台的计划。

展望未来机遇，Cook[在一篇博客文章中提出](https://columnar.tech/blog/announcing-columnar/)，Arrow也能在AI领域发挥作用，他解释说这种格式远远超过了JSON-RPC的吞吐量，并嘲笑其效率极低的base64编码。用于GPU的CUDA生态系统围绕表格数据模型构建，也能从更快的加载时间中受益。

Cook说：“未来一两年内，我们将与该领域的许多公司进行沟通，并努力向他们推介使用Arrow的好处。”

Columnar的400万美元种子轮融资由Bessemer Venture Partners领投。