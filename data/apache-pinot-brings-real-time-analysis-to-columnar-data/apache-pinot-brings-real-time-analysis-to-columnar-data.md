
<!--
title: Apache Pinot 将实时分析带入列式数据
cover: https://cdn.thenewstack.io/media/2024/12/7e09e53c-pinot.png
-->

小心了，一个新的开源数据分析数据库系统出现了，它叫做Apache Pinot——而且速度很快。

> 译自 [Apache Pinot Brings Real Time Analysis to Columnar Data](https://thenewstack.io/apache-pinot-brings-real-time-analysis-to-columnar-data/)，作者 Joab Jackson。

Apache Pinot 项目始于 2013 年的 LinkedIn，旨在对数百万用户在其所有服务中捕获的单个指标进行分析。

该公司已经开发了 [Apache Kafka](https://thenewstack.io/why-we-use-apache-kafka-for-real-time-data-at-scale/) 来管理其系统每天产生的数百万条消息。然而，这项任务不仅仅是消息传递问题，而是分析单个数据列的问题，例如“谁查看了每个用户的个人资料？”，需要足够快的速度才能实时为用户提供有用的信息。

该功能最初是在 Elasticsearch 和在线事务处理 (OLTP) 数据库的组合上开发的，但这需要同时运行数千台服务器才能得到答案，这是一个昂贵的方案。

借助 Pinot，该公司的工程师能够将所需的服务器数量减少到大约 75 台。

Pinot 的诞生是为了解决“以低成本方式大规模运行数亿用户的分析查询”的问题，[StarTree](https://startree.ai/about) 产品负责人解释说，StarTree 提供了 Pinot 的完全托管的云原生版本。

Soman 在接受 TNS 采访时表示，Pinot 带来了“数据堆栈的简化”。“这个问题并不新鲜。许多传统技术已经解决了这个问题。Pinot 带来的则是对这些问题的简化和规模化。”

## 实时分析

这项技术很快被其他网络规模的公司采用，例如 Uber、Google、DoorDash 和 Stripe。大约 1000 个组织正在使用该软件的开源版本。

Stripe 每天处理数十亿笔交易，它使用 Pinot 向其商家提供支付分析数据：现金流分析、逾期付款、每用户收入等等。

可以将[Apache Pinot](https://pinot.apache.org/) 视为分析型数据库和传统事务型数据库的组合。“它构建了一个分析型数据库，但可以处理 OLTP 数据库的规模。”它可以在[Google BigQuery](https://thenewstack.io/bigquery-pricing-a-users-guide/) 或[Snowflake](https://thenewstack.io/snowflake-consolidates-platform-expands-ai/) 上进行大规模分析，但时间却只是其中的一小部分。

Soman 表示，Pinot 每秒可以处理数十万个[基于 SQL 的](https://thenewstack.io/how-to-write-sql-queries/) 查询，延迟小于 99 毫秒，即使是扩展到数千个节点的 MySQL 也无法与之匹敌。一些最大的 Pinot 部署每秒最多可索引一百万个事件。

Pinot 于 2015 年[开源](https://thenewstack.io/reimagining-observability-the-case-for-a-disaggregated-stack/)，并于 2018 年首次被 Apache 接受。Pinot 1.0 版本[于 2023 年 9 月发布](https://startree.ai/resources/query-time-joins-in-apache-pinot-1-0)，并增加了执行[两个表的查询时连接](https://startree.ai/resources/query-time-joins-in-apache-pinot-1-0) 的能力，以及执行“upserts”的能力，这是一种 UPDATE 和 INSERT 的组合[，它确保](https://startree.ai/resources/real-time-upserts-in-apache-pinot-and-startree-cloud) 将最新数据添加到数据库或更新数据库。

## 数据服务层

可以将 Pinot 视为数据服务层。数据可以存储在对象存储中，例如[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 的 Simple Storage Service (S3)，并可能使用[Apache Iceberg](https://thenewstack.io/apache-iceberg-a-different-table-design-for-big-data/) 进行格式化。

Soman 解释说：“Kafka 是半有状态的，它会存储一周的数据，但它并非设计用于存储有状态的数据。使用 Pinot，您可以将数据存储在任何您想要的地方并查询单个项目。”

Kafka 也不是分析引擎。即使是经常与 Kafka 一起使用的[Apache Flink](https://thenewstack.io/how-apache-iceberg-and-flink-can-ease-developer-pain/)，也更侧重于处理和过滤。事实上，这三种工具可以一起在一个被称为 KFP 堆栈的堆栈中使用。

[在 GitHub 上](https://github.com/startreedata/pinot-recipes)，StarTree 提供了一系列关于 Pinot 适合哪些任务的示例：
- 批数据摄取
- 流式摄取
- Upserts
- 地理空间处理
- 变换函数
- 相似性搜索 (AI)

11 月，StarTree 更新了其[StarTree Cloud](https://startree.ai/products/startree-cloud) 服务，以包括基于角色的访问控制 (RBAC)、无暂停摄取、模式演变和数据回填。
