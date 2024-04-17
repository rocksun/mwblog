# 使用 SQL 查询 Apache Kafka

![查询 Apache Kafka with SQL 的特色图片](https://cdn.thenewstack.io/media/2024/04/91a6c0b1-kafka-postgresql-1024x576.png)

Apache Kafka 在大型组织中广泛用于存储和交换数据，但它有一个大问题：你无法轻松查询这些数据。必须始终将数据复制到常规数据库才能对其进行查询。这会减慢数据创新，并迫使企业构建可能发生任何事情的管道。

使组织中的每个团队成员都能使用他们想要的解决方案访问和利用实时数据，是一种变革性策略，它推动了广泛采用和运营效率。这不仅赋予了开发人员权力，还赋予了业务分析师、数据科学家和构建数据驱动型文化的决策者权力。

## Kafka 仅仅用于流式 ETL 吗？

Kafka 在 2011 年开源，当时大型数据库和大数据盛行。从那时起，我们已经了解了很多关于使用这种新方法在数据移动和转换时保持数据动态的信息。

如今，Kafka 主要用于将数据可靠地移动到每个人都可以使用的地方。这可能是一个数据库、数据仓库或数据湖，用户可以对其进行查询（例如 PostgreSQL、ClickHouse、Elasticsearch 或 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention)），分析团队可以使用它，并且可以用来构建仪表盘和机器学习模型。Kafka 通常仅用于其实时功能，并且不包含历史数据——Kafka 中的默认数据保留时间只有几天，之后数据将自动删除。

Kafka 与流处理技术（如 Kafka Streams、Apache Spark 或 Apache Flink）结合使用，以进行转换、过滤数据、使用用户数据对其进行丰富，并可能在各种来源之间进行一些联接。Kafka 非常适合构建流式提取、转换和加载 (ETL)，它可以实时捕获、转换和将数据加载到另一个地方，这与在计划的基础上（每 X 分钟）定义的传统批处理相反。

一切都很好，但 Kafka 有一个很大的缺点：它无法使数据可访问。

## Kafka 对于查询来说不是很好

Apache Kafka 通常是组织中所有数据在移入其他应用程序之前创建的地方。然后所有应用程序通过 Kafka 进行通信并生成数据。但不知何故，这些数据对于包括数据科学家、分析师和产品所有者在内的非开发人员来说几乎无法访问。

即使对于开发人员来说，探索和处理数据也不是一件容易的事，因为没有像 [SQL](https://roadmap.sh/sql) 这样的简单语言来用 Kafka 讨论数据。你通常需要外部工具（如 [Conduktor](https://www.conduktor.io/)）或终端中的高级命令行工具来查看和分析数据——但这只能做到这一步。

并非组织中的每个人都是精通技术的，而组织希望为每个人提供一致的体验，以便平等地进行交流。例如，他们希望整个团队，无论他们对技术有多么熟悉，都能够在无需学习复杂的新工具的情况下开展新项目。

在 Kafka 领域，组织依赖数据工程团队来构建必要的管道和 ETL，以使数据可访问。这些团队还使用 Debezium 等变更数据捕获 (CDC) 工具将数据移出 Kafka，这会稀释数据所有权、安全性和责任。

## 但 Apache Kafka 不是数据库……是吗？

正如 Martin Kleppmann 在 2018 年 Kafka 峰会旧金山分会上所讨论的那样：“[Kafka 是一个数据库吗？](https://www.youtube.com/watch?v=v2RJQELoM6Y)”：Kafka 可以通过构建流处理器来实现数据库的所有原子性、一致性、隔离性和持久性 (ACID) 要求。Kafka 还完全支持一次性事务，Apache 的 [KIP-939](https://cwiki.apache.org/confluence/display/KAFKA/KIP-939%3A+Support+Participation+in+2PC) 提议正在出现，以支持两阶段提交 (2PC) 协议，以便与其他数据库进行分布式事务。

有趣的是，Kleppman 得出的结论是“肯定没有临时查询”，并且你必须将数据移到真正的数据库中才能处理此类问题。六年后，这是仍然存在的一个警告，并且减慢了所有想要使用 Kafka 的人的速度。

## 处理数据混乱

组织在 Kafka 和数据库中拥有大量数据。数据的质量各不相同。规则并非处处相同。没有人对所有事情都有相同的看法。很难知道数据在哪里或真实来源在哪里。这就是我们所说的数据混乱。

将数据从 Kafka 复制到数据库会增加一层复杂性。由于安全模型根本不同，数据的拥有权和安全性变得脆弱，并且可能不一致。
## Kafka 与 SQL：数据保护和生态系统成熟度

**数据保护的差异**

[Kafka](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/)和数据库在数据保护方面有不同的方法。这种不匹配很难修复，尤其是在添加数据屏蔽或字段级加密等要求时。

**数据泄露的风险**

数据泄露事件突显了生态系统中技能、一致性和成熟度的不足。例如，法国政府在 3 月份发生了一次违规行为，[泄露了多达 4300 万人的数据](https://www.theregister.com/2024/03/14/mega_data_breach_at_french/)。

**数据格局的碎片化**

数据产品的快速增长导致了组织内数据格局的碎片化。这种激增产生了数据孤岛，削弱了统一数据策略的潜力。

## SQL：统一数据生态系统的基础

SQL 是一种流行的编程语言，在 [TIOBE 指数](https://www.tiobe.com/tiobe-index/sql/) 中排名第 6 位。

**PostgreSQL：领先的数据库协议**

[PostgreSQL](https://thenewstack.io/a-cheat-sheet-to-database-access-control-postgresql/)是领先的数据库协议，许多供应商都希望与之兼容。Grafana、Metabase、Tableau、DBeaver 和 [Apache Superset](https://thenewstack.io/explore-and-visualize-data-the-apache-superset-way/) 等工具都可以连接到提供与 PostgreSQL 兼容的端点的服务。

**SQL 的优势**

SQL 为构建统一的数据生态系统提供了坚实的基础，而 Kafka 作为其核心中的单一事实来源。PostgreSQL 以其广泛的兼容性和易于上手而脱颖而出。

**Kafka 与 SQL 的集成**

通过对 Kafka 进行现代化以纳入 SQL 功能，我们可以减少对数据管道和复制的需求，提高效率、成本效益、治理和安全性。

## AI 和机器学习 (ML) 的进一步发展

SQL 适用于临时分析和构建数据管道，但它不擅长处理 AI/ML 所需的大量数据。Apache Parquet 和 Apache Iceberg 等技术可以有效地查询大量数据。

**Kafka 作为单一事实来源**

Kafka 作为单一事实来源的能力正在成为现实。Confluent 已宣布 [TableFlow](https://www.confluent.io/en-gb/blog/introducing-tableflow/)，它可以将 Apache Kafka 主题具体化为 Apache Iceberg 表。

## 铺平解放数据之路

Conduktor 和 Kafka 支持实时数据需求，使用 SQL 满足 OLAP 和业务需求，使用 Parquet 和 Iceberg 等文件格式满足 AI/ML 需求。它们正在为数据可访问性和针对各种消费偏好进行优化铺平道路。

**预订演示**

如果你想解放你的数据并使其在组织中更易于访问，请预订 [Conduktor 演示](https://www.conduktor.io/contact/demo/)。

**订阅 YouTube 频道**

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)