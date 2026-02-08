<!--
title: pg_lake 登陆 Snowflake Postgres：对开放标准意味着什么
cover: https://cdn.thenewstack.io/media/2026/02/d8c681a1-alexander-mils-yrkuerek6i0-unsplash.jpg
summary: Snowflake Postgres 现已原生支持 pg_lake 扩展，将 PostgreSQL 用作数据湖仓，支持 Iceberg 表。它统一了分析与事务工作负载，增强开放数据治理和共享，提升开放标准互操作性。
-->

Snowflake Postgres 现已原生支持 pg_lake 扩展，将 PostgreSQL 用作数据湖仓，支持 Iceberg 表。它统一了分析与事务工作负载，增强开放数据治理和共享，提升开放标准互操作性。

> 译自：[pg_lake comes to Snowflake Postgres: What it means for open standards](https://thenewstack.io/pg_lake-comes-to-snowflake-postgres-what-it-means-for-open-standards/)
> 
> 作者：Jelani Harper

[pg_lake 扩展](https://www.snowflake.com/en/engineering-blog/pg-lake-postgres-lakehouse-integration/)于去年11月首次向开源社区发布，现已原生支持 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) Postgres，即云数据仓库的全托管 [PostgreSQL](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) 服务。pg_lake 是大约15个扩展的集合，使用户能够将 PostgreSQL 用作数据湖仓。它支持 Apache Iceberg 表，可实现快速查询和事务性工作负载；组织还可以将 pg_lake 与对象存储中的数据配合使用。

[Snowflake Postgres](https://www.snowflake.com/en/developers/guides/getting-started-with-snowflake-postgres/) 通过允许用户直接在 Snowflake 中访问 PostgreSQL，统一了分析和事务性工作负载。因此，他们可以通过 SQL 读写开放表格式；[pg_lake](https://github.com/Snowflake-Labs/pg_lake/blob/main/README.md) 抽象了操作不同类型和格式数据所需的大部分底层复杂性。

Snowflake 还宣布将其 [Snowflake Horizon Catalog](https://www.snowflake.com/en/product/features/horizon/)（其数据发现、元数据上下文和数据治理层）的功能扩展，以管理通过外部查询系统（如 Apache Spark）访问的数据资产。此外，其开放数据共享功能（适用于不同的云和可用区）现已适用于 Delta Lake 和 Iceberg 表中的数据。

该供应商还公布了与 Microsoft One Lake 的新集成，为 Snowflake 和 Microsoft Fabric 中的数据提供安全的双向读取功能。

这些功能和 pg_lake 在 Snowflake Postgres 中的互操作性不仅适用于不同的数据类型、格式、云和区域，还适用于 OLAP、OLTP 和高级机器学习应用程序。

Snowflake Postgres 的 Postgres 软件工程总监 Craig Kerstiens 评论道：“如果你是客户，你甚至不需要知道底层是 Iceberg。”“如果你只想要 Postgres，它就是 Postgres。但是，它在底层拥有这些超能力，拥有统一的 Iceberg 目录，内嵌了矢量化引擎，并且能够轻松地将数据从一个移动到另一个。”

## pg_lake 的扩展

pg_lake 的实用性影响了应用程序开发和部署生命周期的多个方面。通过使其可通过 [Snowflake Postgres](https://docs.snowflake.com/en/en/user-guide/snowflake-postgres/about) 访问，该生命周期可以轻松地在涉及开放表格式的分析和事务性工作负载之间切换。pg_lake 中包含的各个扩展包括针对以下方面的专用措施：

*   **版本管理：** 版本管理对于更新和维护至关重要。在 Snowflake Postgres 中，用户正在处理不同的操作系统、Postgres 版本、库等。更新一个组件而不引起不必要的停机和返工其他组件可能很费力。据 Kerstiens 说：“我们在 pg_lake 内部有一个扩展，负责管理所有其他扩展。因此，当你升级库 B 时，它不会与库 C 冲突。”
*   **数据类型和格式转换：** 将 SQL 用作通用语言，与 Postgres 中各种数据类型（包括地理空间数据、向量嵌入等）以及 Iceberg 表中的数据进行交互，既宝贵又复杂。然而，pg_lake 为连接、读取和写入完成了这项任务，因此“你只需编写 SQL 查询”，Kerstiens 说。“你从未考虑过其他这些扩展，或底层发生的复杂性。”
*   **缓存：** 使用缓存策略优化性能对于低延迟应用程序的成功至关重要。据 Kerstiens 说，pg_lake 拥有“将为你完成缓存”的机制。例如，如果用户正在写入 Iceberg 文件，并且有新文件进入，系统可以缓存更新的文件。还有通过下推优化连接和查询的机制。这些以及其他功能促使 Kerstiens 将 Snowflake Postgres 描述为“生产级、企业级就绪”。

## 开放数据治理

Snowflake 对 [Iceberg](https://iceberg.apache.org/) 和开放标准的效用也随着 Snowflake Horizon Catalog 中的新功能而增加，该功能现在可以像管理 Snowflake 原生存储格式中的表一样管理 Iceberg 表。通过允许外部查询引擎（如 [Trino](https://thenewstack.io/speed-trino-queries-with-these-performance-tuning-tips/) 等）读取由目录管理的表（此功能已全面可用）并写入这些表（据 Snowflake 应用程序、协作和 Horizon 负责人 Prasanna Krishnan 称，该功能即将进行公开预览），用户可以获得多项优势。“他们的数据拥有单一事实来源，”Krishnan 指出。“他们不必创建副本。”

此外，他们还可以将 Snowflake Horizon Catalog 的访问控制扩展到这些查询引擎。通过这种范式，组织直接通过 Snowflake 查询数据，Snowflake 依赖目录的访问控制相应地过滤结果。因此，可以“在列上规定掩码策略，这样特权用户查询此列时可以看到它，而普通分析师只能看到被掩码的数据”，Krishnan 说。“或者，它可以是行访问策略，我只限制哪些行可以访问哪些角色。”

## 开放数据共享

Snowflake 的数据共享特性不涉及副本，是供应商提供的另一个有用功能。以前，此功能仅适用于 Snowflake 专有数据格式中的对象和表。目前，它适用于 [Delta Lake](https://delta.io/) 和 Iceberg 表。当不同方使用各自的云且位于不同地理区域时，此特性特别有用。

Krishnan 说，Snowflake 的开放数据共享允许他们在“不想移动数据或复制数据”的情况下仍然访问相同的数据。“消费者无需在每次查询时支付将数据移至不同区域的出口费用。在底层，我们使用安全的跨云自动移动功能，使数据可在用户所在区域获取并进行查询。”

## 可扩展的开放标准

Snowflake 将其开放数据共享和 Horizon Catalog 功能扩展到包括开放表格式和外部查询引擎，这标志着其目前对开放标准的关注。这些进步所提供的互操作性，以及通过 pg_lake 加强 Snowflake Horizon Catalog，使开发人员更容易使用对其应用程序最有意义的工具和格式——而不是由供应商规定的工具和格式。

这一事实对于 pg_lake 的数据湖仓功能尤其如此，它增强了 Snowflake Postgres 提供的分析和事务支持。Kerstiens 评论道：“OLTP 和 OLAP 一直生活在不同的世界中。”“一个是基于行的；一个是基于列的。一个是点查询；另一个是大数据扫描。它们生活在不同的世界中，现在我们开始弥合这一差距并统一它们。”