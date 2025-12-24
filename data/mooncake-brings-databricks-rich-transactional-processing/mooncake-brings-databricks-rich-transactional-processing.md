<!--
title: Mooncake赋能Databricks：解锁强大事务处理新境界
cover: https://cdn.thenewstack.io/media/2025/12/0041afda-annie-hatuanh-idwwqjugcxm-unsplash.jpg
summary: Databricks收购Mooncake，将其PostgreSQL与Iceberg结合，为AI智能体提供无ETL的实时HTAP能力，解决传统OLTP/OLAP分离问题。
-->

Databricks收购Mooncake，将其PostgreSQL与Iceberg结合，为AI智能体提供无ETL的实时HTAP能力，解决传统OLTP/OLAP分离问题。

> 译自：[Mooncake Brings Databricks Rich Transactional Processing](https://thenewstack.io/mooncake-brings-databricks-rich-transactional-processing/)
> 
> 作者：Joab Jackson

所有即将蜂拥而至的AI智能体都需要新鲜数据，这使得数据平台社区正紧急思考如何更好地将分析直接注入决策过程。

去年10月，[Databricks](https://thenewstack.io/databricks-launches-a-no-code-tool-for-building-data-pipelines/)悄然[收购](https://www.databricks.com/blog/mooncake-labs-joins-databricks-accelerate-vision-lakebase)了一项技术，该技术将为其新兴的面向AI智能体的[Lakebase平台](https://www.databricks.com/product/lakebase)提供关键组件：Mooncake，一个支持丰富事务处理和快速列式分析的单一软件包。

卖点是什么？无需管理[ETL管道](https://thenewstack.io/aws-makes-etl-disappear-for-aurora-postgresql-dynamodb/)。数据可以直接从PostgreSQL内部获取，用于在事务处理中做出路由决策。

Lakebase是一项无服务器[Postgres](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/)服务，它集成到该公司的[Lakehouse托管数据平台](https://thenewstack.io/lakebase-is-databricks-fully-managed-postgres-database-for-the-ai-era/)中。它针对AI智能体进行了优化（特别是该公司自有的[Agent Bricks](https://thenewstack.io/databricks-launches-agent-bricks-its-new-no-code-ai-agent-builder/)）。

Databricks于去年5月以10亿美元[收购了](https://techcrunch.com/2025/05/14/databricks-to-buy-open-source-database-startup-neon-for-1b/)无服务器PostgreSQL提供商Neon。这为该公司提供了一个基于PostgreSQL的事务平台，[据Databricks称](https://www.databricks.com/blog/databricks-neon)，该平台将计算与存储分离。

难题的下一个组成部分：Mooncake。

## OLTP和OLAP：支离破碎

Mooncake由Mooncake Labs开发，这家初创公司由三位前SingleStore工程师创立，旨在重新思考事务和分析数据库系统如何结合运作。

传统上，事务数据库系统（[OLTP](https://thenewstack.io/new-oltp-postgres-with-separate-compute-and-storage/)）和分析数据库系统（[OLAP](https://thenewstack.io/data-telemetry-is-the-lifeline-of-modern-analytics-and-ai/)）在企业内部是相互独立运行的（通常由不同的部门负责）。

人们普遍担心，事务处理（需要快速）的延迟时间会因在大型数据集上运行一些耗时且/或计算量大的分析作业而受到影响。

因此，将需要微秒级插入时间以实现快速事务的OLTP放在一边；将能够扫描海量表格进行大规模分析的OLAP系统放在另一边。

这种分离此后变得繁重。因为两者需要交换数据。

“用户被迫手动将它们与复杂而脆弱的数据管道连接起来，这些管道需要数小时才能同步，有时还会将数据转换为难以阅读的形式，”Mooncake Labs联合创始人[Cheng Chen](https://www.linkedin.com/in/cheng-ch/)在卡内基梅隆大学数据库小组的[未来数据系统研讨会系列](https://db.cs.cmu.edu/2025/09/future-data-systems-seminar-series-fall-2025/)讲座中解释道。

如今，网络速度和计算能力已经发展到可以将OLTP和OLAP结合起来是一个好主意，因为它为事务处理方式开辟了全新的前景。

## OLTP和OLAP：永远在一起

Chen是来自[SingleStore](https://www.singlestore.com/?utm_content=inline+mention)的三位联合创始人之一，SingleStore提供同名（前身为MemSQL）的混合事务/分析处理（HTAP）数据库系统。

作为分布式数据库系统，SingleStore[统一](https://thenewstack.io/singlestore-offers-fast-vector-processing-for-real-time-ai/)了事务和列式分析，从而结合了这两种数据存储类型。它使用单一引擎，对事务行使用工作内存，对列存储使用磁盘。它具有良好的扩展性，并支持JSON、全文和向量等多种格式。

但Chen感叹，SingleStore的设计是单体的。因为它作为一个独立的查询引擎运行，所以它必须与现有最好的OLTP和OLAP引擎竞争。而那些仅仅为了在新鲜数据上获得快速分析（用于欺诈检测等操作）的益处而愿意采用全新数据库系统的人相对较少。

## Mooncake连接PostgreSQL和Iceberg引擎

既然不是尝试构建一个“神奇引擎”（Chen的原话）来完成两种处理，为什么不将这种功能作为现有系统的一个特性来重现呢？

Chen表示，Mooncake致力于构建一个“可组合的”混合数据库系统。

它是一个框架和一套新功能，构建在现有OLTP系统和OLAP格式之上。

工程团队选择支持PostgreSQL进行事务处理，因为它作为开源数据库系统广受欢迎。

在分析方面，他们选择了开放的湖仓格式[Apache Iceberg](https://thenewstack.io/architects-guide-to-apache-iceberg/)和（Databricks自己的）[Delta Lake](https://thenewstack.io/delta-lake-a-layer-to-ensure-data-quality/)，这样这些格式中的数据就可以被任何兼容的引擎访问（[DuckDB](https://thenewstack.io/duckdb-in-process-python-analytics-for-not-quite-big-data/)、[StarRocks](https://thenewstack.io/starrocks-launches-beta-of-cloud-service-for-its-analytics-engine/)、[Trino](https://thenewstack.io/speed-trino-queries-with-these-performance-tuning-tips/)、[Apache Spark](https://thenewstack.io/enhancing-the-flexibility-of-sparks-physical-plan-to-enable-execution-on-various-native-engines/)）。

## Mooncake：不是引擎，只是一个功能

Mooncake有两个主要组件。其中一个（“moonlink”）是Iceberg之上的一层实时层，可以实现数据的“亚秒级摄取”。

第二个组件（“pg\_mooncake”）为PostgreSQL提供了HTAP能力，允许用户添加分析功能以确定事务路由决策。

它们共同推动了事务和分析系统之间无休止的分歧，为快速分析带来的新可能性世界搭建了一座桥梁。智能体们将会很高兴。