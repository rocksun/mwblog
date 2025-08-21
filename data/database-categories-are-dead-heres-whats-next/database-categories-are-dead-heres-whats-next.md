<!--
title: 数据库分类已成过去：未来趋势前瞻
cover: https://cdn.thenewstack.io/media/2025/08/1a727615-convergence.jpg
summary: 数据库分类已过时，现代数据库融合为通用平台，可处理多种工作负载。这消除了数据同步、简化查询语言和操作模型，并保证事务一致性。多语言持久性在数据库有硬性限制时有意义，但现在通用平台性能提升，其必要性降低。
-->

数据库分类已过时，现代数据库融合为通用平台，可处理多种工作负载。这消除了数据同步、简化查询语言和操作模型，并保证事务一致性。多语言持久性在数据库有硬性限制时有意义，但现在通用平台性能提升，其必要性降低。

> 译自：[Database Categories Are Dead: Here's What’s Next](https://thenewstack.io/database-categories-are-dead-heres-whats-next/)
> 
> 作者：Jesse Hall

传统的数据库分类方式已经过时。我们十多年来使用的诸如“NoSQL”、“关系型”、“文档”、“键值”和“图”等标签，已不再能描述[现代数据库](https://thenewstack.io/introduction-to-databases/)的工作方式或开发者实际的需求。

这不仅仅是语义上的转变。创建这些类别的基本假设已经改变。现代应用程序不适合放入整齐的数据库类别中，为它们提供支持的系统也不应该这样。

## **分类的陷阱**

数据库类别的出现源于真正的技术限制。在 2000 年代初期，你面临着明确的权衡：

* 关系型数据库提供 [ACID 事务](https://thenewstack.io/acid-compliant-distributed-sql-enters-the-agentic-ai-era/)和结构化查询，但在规模和模式演变方面表现不佳。
* 文档存储提供灵活的模式和横向扩展，但缺乏事务和复杂的查询。
* 键值存储提供原始性能，但查询能力有限。
* [图数据库](https://thenewstack.io/common-uses-cases-for-graph-databases/)擅长处理关系，但在其他访问模式下表现不佳。

这些权衡迫使在开发早期做出架构决策。选择你的毒药：一致性或规模，灵活性或结构，性能或功能。

结果是多语言持久性——为同一应用程序的不同部分使用多个数据库。一个典型的现代堆栈可能包括 [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) 用于事务数据，Redis 用于缓存，Elasticsearch 用于搜索，Neo4j 用于推荐，以及 [InfluxDB](https://www.influxdata.com/?utm_source=vendor&utm_medium=referral&utm_campaign=2025_spnsr-web_tns&utm_content=note&utm_content=inline-mention) 用于指标。

当系统较小且团队有时间管理复杂性时，这种方法是可行的。但在今天的开发环境中，它就行不通了。

## **融合**

现代数据库正在融合到一个不同的架构上：通用平台，可以处理多种工作负载类型，而无需单独的系统。

这种融合的发生是因为最初的技术限制消失了。在 2010 年看似奇特的分布式计算技术已成为标准。CAP（一致性、可用性和分区容错性）定理的权衡看似是根本性的，但通过更好的算法和基础设施证明是可以协商的。

考虑一下数据库领域发生了什么：

PostgreSQL 添加了 JSONB 列，使其适用于文档工作负载。它现在包括全文搜索、时间序列扩展，甚至 [向量相似性搜索](https://thenewstack.io/combining-the-power-of-text-based-keyword-and-vector-search/)，用于 AI 应用程序。

Redis 扩展到简单的键值操作之外，包括用于搜索、图处理、JSON 文档和时间序列数据的模块。

[Apache Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/) 引入了二级索引、物化视图和更灵活的数据建模。

甚至像 SQL Server 和 Oracle 这样的传统关系数据库也添加了 JSON 支持、图功能和 NoSQL 风格的灵活性。

MongoDB 在这种融合中走得最远。最初作为文档数据库，现在它在分布式集群中提供 ACID 事务，由 Apache Lucene 提供支持的全文和向量搜索，以及其他[现代功能](https://www.mongodb.com/products/platform/atlas-database/features/?utm_campaign=devrel&utm_source=third-party-content&utm_medium=cta&utm_content=tns-database-categories-are-dead&utm_term=jesse.hall)。

这种模式超越了任何单一供应商。过去五年中最成功的数据库是那些超越了其原始类别的数据库。

## **这对开发者为何重要**

这种融合的实际影响是巨大的。现代应用程序可以围绕能够处理各种工作负载类型的平台进行整合，而不是管理多个数据库系统。

这种整合消除了整个类别的问题：

* **没有数据同步**。当你的用户资料、会话缓存、搜索索引和分析都位于同一系统中时，你不需要复杂的 ETL（提取、转换、加载）管道来保持数据一致。
* **统一的查询语言**。开发者学习一种语法，而不是 SQL 加上 Redis 命令加上 Cypher 加上你的搜索引擎使用的任何领域特定语言。
* **单一的操作模型**。一种备份策略，一种监控系统，一种扩展方法，一种安全模型。
* **事务一致性**。跨多种数据类型的操作可以使用相同的 ACID 保证，从而消除了困扰多语言架构的分布式事务复杂性。

真正的公司正在看到结果。制药公司正在将临床报告的生成时间从几周减少到几分钟。金融平台正在管理数千亿美元的资产，同时将扩展性能提高 64%。电子商务网站正在实现亚毫秒级的搜索响应时间，而无需单独的搜索基础设施。

## **多语言持久性的清算**

当数据库有硬性限制时，多语言持久性是有意义的。但当这些限制不再存在时，它就显得不那么有意义了。

多语言方法假设专业化总是胜过泛化。但专业化是有代价的：运营复杂性、数据一致性挑战以及管理多个系统的认知开销。

当性能优势明显时，这些成本是可以接受的。当通用平台在其自身领域中匹配或超过专用系统时，权衡计算就会发生变化。

考虑一下搜索。Elasticsearch 成为全文搜索的默认选择，因为关系数据库处理得很差。但是，当 MongoDB 的 Atlas Search 使用与 Elasticsearch 相同的 Apache Lucene 基础提供亚毫秒级的响应时间时，维护单独的搜索集群有什么好处？

同样的逻辑适用于所有数据库类别。当通用平台提供与专用向量数据库相当的向量搜索性能，或与专用系统匹配的时间序列处理时，多个数据库的架构复杂性变得更难证明是合理的。