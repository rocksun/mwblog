
<!--
title:  利用DuckDB集成释放Postgres的分析能力
cover: https://cdn.thenewstack.io/media/2024/07/57a43fe6-duckling-8062337_1280.jpg
-->

通过将 Postgres 与嵌入式快速查询引擎集成，为您的数据工作负载注入活力。

> 译自 [Unleashing Postgres for Analytics With DuckDB Integration](https://thenewstack.io/unleashing-postgres-for-analytics-with-duckdb-integration/)，作者 Paul Laurence。

Postgres 生态系统正在蓬勃发展，使其成为 [开发人员的首选](https://survey.stackoverflow.co/2023/#technology-most-popular-technologies) 用于新的数据工作负载和数据库工具。关于 [“为什么 Postgres 正在获胜”](https://www.crunchydata.com/blog/when-did-postgres-become-cool) 已经有很多文章，并且有很多充分的理由——包括其可扩展性——使 Postgres 能够随着需求的出现而扩展到新的用例，例如 [pg vector](https://github.com/pgvector/pgvector) 能够满足各种 AI 需求。

尽管 Postgres 在 [OLTP](https://thenewstack.io/how-data-integration-is-evolving-beyond-etl/) 工作负载方面很受欢迎，但 [Postgres](https://thenewstack.io/postgres-is-now-a-vector-database-too/) 在处理大型数据集（OLAP）上的高性能分析方面仍然存在挑战。虽然有一些解决方案修改了核心 Postgres 来解决 OLAP 工作负载，或者使用 Postgres 的部分功能，但每种解决方案都存在使用 Postgres 分支相关的固有挑战、成本和限制。

随着 Postgres 用户越来越多地寻求 Postgres 原生的 OLAP 解决方案，数据重心转向低成本存储，以及数据格式新标准的出现，Crunchy Data 开始开发一种新的解决方案，以扩展 Postgres 以满足这些需求。我们的解决方案利用了 Postgres 扩展的已知强大功能，以及嵌入式快速查询引擎中新兴的赢家——[DuckDB](https://duckdb.org/)。

## 热爱 Postgres，需要分析

我们帮助各种组织部署 Postgres。从这个有利位置来看，用户成功地将 Postgres 部署到各种用例中。事实上，当我们被问及 Postgres 解决的用例时，我们很难回答，因为答案是我们真的已经看到了所有用例。

但这是在 OLTP 上下文中。OLAP 历史上一直是“另一种工作负载”，Postgres 在此没有竞争。是的，有一些解决方案，但特别是，随着用户迁移到云和云原生方法，没有多少 Postgres 原生的解决方案。

我们亲眼目睹了这一点：许多 [Crunchy Bridge](https://crunchybridge.com/login) 客户——他们热爱 Postgres——使用 Postgres 进行 OLTP 工作负载，但使用各种工具将数据复制到各种第三方分析平台以进行分析查询。在与这些客户讨论他们的需求时，他们对将数据移出 Postgres 不满意，但没有更好的选择。我们能构建一个吗？

## 在数据所在的位置处理数据，在 S3 中对数据进行分析

为了构建 Postgres 原生分析的解决方案——很明显，我们需要一个解决方案来解决数据所在的位置以及组织使用的现代格式。两个重要的趋势决定了我们的方向：

- 数据越来越多地存储在 S3 中。S3——以及类似的云存储库——作为低成本、持久存储的采用率激增。它们可以无限扩展，并且可以从任何地方访问。用户可以同时将他们的数据暴露给许多不同的引擎。
- 文件和表格格式的开放标准是新兴的赢家。虽然许多数据湖仍然是“S3 中的 CSV 文件”，但像 Parquet 和 Iceberg 这样的分析优化格式正在迅速普及。

当然，将查询引擎（计算）与存储（数据）分离的前景催生了许多数据库项目。这使得能够将数据以低成本存储在一个地方，同时高效地查询数据，而无需将其移动到查询引擎。

最终，我们得出结论，S3（带缓存）是分析数据的合适存储层，而 PostgreSQL 中强大的 S3 集成提供了解决这些用例的方法。

## Postgres 的可扩展性再次使其成为赢家

Postgres 扩展使 Postgres 能够随着需求的出现而解决新的用例。通过加载 PostGIS 扩展，Postgres 成为管理空间数据的领先数据库。Postgres 可以使用 Citus 支持高级分片，或者使用 pgvector 将其转换为向量数据库。每个 Postgres 用户都有自己喜欢的扩展，并且许多用户可能使用了一系列扩展，而没有考虑 Postgres 扩展框架的强大功能。

将 Postgres 扩展以支持[外部查询引擎充分利用了这种扩展功能](https://www.crunchydata.com/blog/how-we-fused-duckdb-into-postgres-with-crunchy-bridge-for-analytics)。使用 Postgres 的“钩子”，我们可以透明地将查询计划分解成可以“下推”到这个外部独立查询引擎的部分，使我们能够利用专门引擎在这些特定工作负载方面的优势。在本例中，我们使用 DuckDB，它是嵌入式查询引擎领域的新兴赢家。

对于不太熟悉的人来说，DuckDB 由 Hannes Mühleisen 和 Mark Raasveldt 在 Centrum Wiskunde & Informatica (CWI) 开发，并由 DuckDB Labs 积极开发，并获得了许多社区贡献。DuckDB 已成为领先的嵌入式查询引擎，它使用现代 OLAP 技术对 Parquet 和对象存储中的文件进行快速查询。Parquet 文件支持压缩的列式数据，使其成为将历史时间序列行从事务性 Postgres 归档到高效形式以供长期 OLAP 使用的理想格式。

这意味着我们可以通过使用 Postgres 扩展将 DuckDB 与 Postgres 集成，识别可以下推到 DuckDB 以进行矢量化并行执行的查询计划部分，并构建要传递给 DuckDB 的适当 SQL 查询。同样，我们使用 PostgreSQL 钩子的组合来实现过滤器、聚合、联接和更复杂的查询结构。在某些情况下，整个查询可以下推；在其他情况下，我们合并不同的子计划。

## Postgres 原生解决方案的优势

但是为什么选择 Postgres 进行分析？随着 Postgres 的采用不断增长，各种类型的用户都学习使用 Postgres 进行应用程序开发和 OLTP 需求，为这些分析查询提供 Postgres 原生体验具有许多优势。

作为用户，您在 S3 中的数据将显示为表格，您可以与所有标准 PostgreSQL 表格一起查询它们，并与其他 PostgreSQL 功能和扩展的通用简单性结合使用，包括：

- 访问控制
- 视图
- 物化视图
- 使用 pg_stat_statements 的查询性能洞察
- 使用 PL/pgSQL () 的存储过程
- 使用 pg_cron 的定期作业
- 持久性 NVMe 和内存缓存
- 仪表板工具

如果将 Postgres 扩展以支持用于分析查询的外部查询引擎听起来有点复杂，那可能是真的。也就是说，通过将结果作为托管服务提供，用户可以从该解决方案的功能中受益，而无需担心低级细节，例如钩子或查询下推。从用户的角度来看，您所看到的只是能够快速公开您存储在 S3 中的数据，以便使用标准 Postgres 进行查询。Crunchy Bridge 提供了托管生产就绪 Postgres 的全部优势，以及以开发人员为中心的 UX，现在扩展了功能以支持由 DuckDB 提供支持的快速分析查询。
