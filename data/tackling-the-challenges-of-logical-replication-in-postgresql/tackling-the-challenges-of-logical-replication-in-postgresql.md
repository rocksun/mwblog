
<!--
title: 解决PostgreSQL逻辑复制的挑战
cover: https://cdn.thenewstack.io/media/2024/08/a1e52279-global.jpg
-->

在最新版本中，分布式 Postgres 供应商 pgEdge 加强了对大型对象的支持，增强了错误处理和自动化。

> 译自 [Tackling the Challenges of Logical Replication in PostgreSQL](https://thenewstack.io/tackling-the-challenges-of-logical-replication-in-postgresql/)，作者 Susan Hall。

分布式 Postgres 供应商 [pgEdge](https://thenewstack.io/startup-pgedge-tackles-the-distributed-edge-with-postgres/) 继续通过其最新版本（称为“星座版”）来解决 [逻辑复制](https://thenewstack.io/heres-when-to-use-write-ahead-log-and-logical-replication-in-database-systems/) 的复杂性，该版本提供了增强的并行处理、大对象支持和错误处理。

pgEdge 首席执行官 [Phillip Merrick](https://www.linkedin.com/in/phillipmerrick/) 表示，更高的吞吐量、灵活性和控制使 pgEdge 成为需要 [多主功能](https://www.pgedge.com/solutions/benefit/multi-master) 的传统数据库工作负载的可行的开源替代方案。他在一封电子邮件中表示，如今这些工作负载通常运行在诸如 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) Goldengate 之类的传统平台上。

这些工作负载需要能够在分布式数据库集群中的多个节点上接收读写流量，以实现低数据延迟或非常高的可用性（四个或五个九）或两者兼而有之。他解释说，一个例子可能是跨多个区域运行的金融服务应用程序或永远不会停机的关键电子商务应用程序。

Merrick 和他的联合创始人 [Denis Lussier](https://www.linkedin.com/in/denislussier/)（他们之前共同创建了 EnterpriseDB）在开源 [PostgreSQL](https://thenewstack.io/postgresql-takes-a-new-turn/) 上构建了 [pgEdge](https://www.pgedge.com/)，其理念是，地理分布式集群中的几个节点（每个节点处理读写）可以提供低延迟、高可用性、弹性和性能。

尽管 [Postgres 中的逻辑复制](https://www.pgedge.com/blog/logical-replication-features-in-pg-17) 是一项强大的功能，但它也存在一些挑战，包括一致性、同步、冲突解决和开销，这些都会影响性能。

星座版的功能包括：

* **大型对象逻辑复制 (LOLOR)**: 此 PostgreSQL 插件替换使现有应用程序的媒体资产（例如二进制文件、图像和其他非关系数据类型）与逻辑复制兼容。现在，这些 PostgreSQL 数据库中的大型文件可以在 pgEdge 上运行而无需修改。尽管 Postgres 支持将大型对象作为目录表中的块进行存储，但复制这些表需要特殊处理，根据其 [大型对象逻辑复制 (LOLOR)](https://www.pgedge.com/blog/pgedge-platform-support-for-large-object-logical-replication) [GitHub 页面](https://github.com/pgEdge/lolor) 所述。使用 LOLOR，此数据存储在非目录表中，以简化跨多个数据库实例或服务器的复制。它根据逻辑更改（例如插入、更新和删除操作）而不是存储级别的物理更改来复制数据，并使用 [更改数据捕获](https://thenewstack.io/real-time-data-access-across-highly-distributed-environments/) 来确保与其他数据库实例的近乎实时的同步。根据 pgEdge 的说法，这在一致性、可用性和容错性至关重要的分布式系统中尤其有用。
* **复制异常处理和日志记录**: 通过更新的错误处理和日志记录机制，复制错误将记录到一个新的异常表中，以防止它们阻止后续更改。这增强了对复制错误的可见性，以便更轻松地进行故障排除，而不会中断整体系统操作。
* **复制修复模式**: 一个新功能允许用户在特定数据库节点上使用或选择不使用“修复模式”。此额外控制可用于在错误解决期间或修改单个数据库节点状态时阻止复制更改。它还支持通过外部工具进行错误修复，而不会影响整个集群。

虽然将这些功能列为本次发布的一部分，但该公司在 4 月宣布了自动数据定义语言 (DDL) 复制和 Snowflake 序列。

DDL 用于通过 `CREATE`、`ALTER` 和 `DROP` 等命令语句创建和修改 Postgres 对象。传统上，Postgres 需要通过 DDL 命令手动在每个节点上进行表定义的修改。通过这种自动化，您可以在单个节点上更新数据库模式，更改将无缝传播到集群中的其他节点。
[Snowflake 序列](https://docs.pgedge.com/platform/advanced/snowflake#snowflake-sequences) 解决了在多主复制场景中管理序列的复杂性。在分布式多主 Postgres 系统中，序列必须在不同的区域进行更新，如果每个节点独立更新序列，就会产生无法解决的冲突。这种对 PostgreSQL 序列定义的替代方案提供了一个唯一的序列——一个时间戳、一个计数器和一个唯一的节点标识符——在一个集群中，可以在不同的区域使用，而无需编写代码或修改模式。

该公司在 1 月份宣布了其免费的云开发人员版，并在去年 10 月宣布了其使用开源扩展 [pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/) 的 [向量搜索功能](https://thenewstack.io/extension-pgvector-makes-pgedge-a-distributed-vector-database/)。

pgEdge 表示，在第四季度，它将添加高性能并行复制，它称之为“行业的游戏规则改变者”。

Merrick 解释说，高性能并行复制是指在每个节点之间的网络连接上运行多个数据复制流的能力，使用每个节点上的多个 CPU 来实现更高的数据吞吐量。当前 Postgres 的复制架构只允许节点之间有一个流，这限制了复制性能的上限。

这种复制吞吐量的提升将在高流量、跨区域的事务工作负载中，使用户能够在高需求环境中管理更大规模的数据复制，同时减少延迟并确保及时同步。

