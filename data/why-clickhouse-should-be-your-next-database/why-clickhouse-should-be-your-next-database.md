# 为什么 Clickhouse 应该成为您的下一个数据库？

这个数据库系统在集群中可以轻松扩展，因此您的数据可以比真人秀明星的自负心态还要庞大。

翻译自 [Why Clickhouse Should Be Your Next Database](https://thenewstack.io/why-clickhouse-should-be-your-next-database/) 。

![](https://cdn.thenewstack.io/media/2023/07/94ea1cd4-house2-1024x658.jpg)

今天，我们将进入令人激动的数据库领域。我能听到你叹息：“又要学习另一个数据库？真的吗？”但在你冲向山丘之前，请允许我向您介绍 [ClickHouse](https://thenewstack.io/clickhouse-rapidly-rivals-other-open-source-databases-in-active-contributors/) ，数据库多元宇宙中的刺猬索尼克。

## 闪电般快速：揭秘 ClickHouse 架构

ClickHouse 是一个开源的面向列的数据库管理系统（DBMS），旨在对庞大的数据集进行[实时分析查询](https://thenewstack.io/two-sizes-fit-most-postgresql-and-clickhouse/)和更新。而所谓的“庞大”是指“如果您将其打印出来，可能需要一片森林的纸”。

### ClickHouse速度背后的原因是什么？

为了揭开这个谜团，让我们深入了解其架构。

![](https://cdn.thenewstack.io/media/2023/07/2410c465-image1.png)
*ClickHouse 架构的示意图，一个面向列的系统*

ClickHouse 就像大学管理员使用的强大系统。作为学生，您可能想要快速查看一项作业或测试的成绩，这是一个简单直接的交易。然而，管理员需要执行更复杂的操作。他们正在计算班级平均分，评估整个学期的成绩分布，分析学生在所有科目中的表现模式等等。为了完成这些任务，他们不仅仅查看一个学生的成绩，而是分析来自所有学生的海量数据。

### 扩展性如何？

我有提到 ClickHouse 喜欢大数据吗？这个[数据库系统在集群中扩展](https://roadmap.sh/guides/scaling-databases)得非常好，因此您的数据可以变得比真人秀明星的自负还要庞大，而 ClickHouse 仍然可以轻松处理。需要向集群中添加更多节点？没问题。想要保持数据的复制以提高可用性？ ClickHouse 会说：“当然，为什么不呢？”

![](https://cdn.thenewstack.io/media/2023/07/aacdf144-image2.png)
*显示 ClickHouse 在集群中的可扩展性的示意图。*

## ClickHouse 独特之处是什么？

ClickHouse 的独特之处是其真正的面向列的 DBMS 设计。这种独特的架构确保了紧凑的存储，值之间没有额外的数据，这一特点显著提高了处理速度。支持定长值，ClickHouse 保证了高效的空间利用，增强了其高速性能。值得注意的是，ClickHouse 每秒处理数亿行的能力超过了 HBase 和 Cassandra 等系统，树立了新的行业标准。

ClickHouse 的独特性还体现在其作为数据库管理系统的灵活功能上。ClickHouse 不仅局限于单个数据库，还能实时创建表和数据库、加载数据和执行查询。这种适应性确保了无缝的数据库操作，无需重新配置或重启服务器。

增强 ClickHouse 独特性的其他功能包括：

* **数据压缩**：这一基本特性极大地提升了性能。
* **数据的磁盘存储**：ClickHouse 将低延迟的数据提取与使用常规硬盘的成本效益相结合。
* **并行和分布式处理**：ClickHouse 利用多核和多服务器环境加速大型查询，这是面向列的 DBMS 中的一项罕见功能。
* **SQL 支持**：ClickHouse 对 SQL 的广泛支持使其在处理各种查询时脱颖而出。
* **向量引擎**：通过向量处理数据提高了 CPU 效率，这是 ClickHouse 卓越性能的独特方法之一。
* **实时数据更新和快速索引**：ClickHouse 的持续数据添加和快速索引满足实时需求。
* **适用于在线查询**：ClickHouse 具有低延迟，确保立即处理查询，这是在线操作的关键要求。

总之，这些功能的综合使得 ClickHouse 成为一个强大、灵活和高效的系统，独特地适用于处理大规模、实时数据处理需求。

## ClickHouse 的优势：实际应用案例

为了证明我没有在开玩笑，让我们看看一些实际应用案例。

### Cloudflare

没错，这个几乎支撑了一半互联网的公司每天都在使用 ClickHouse 进行实时查询分析，处理着数 TB 的数据！Cloudflare 使用 ClickHouse 来管理每秒高达 600 万请求的实时 DNS 查询分析，涉及处理 TB 级的数据。从架构角度来看，ClickHouse 的列式数据库设计发挥了关键作用。

新架构包括：

* **Kafka 消费者** - 每个分区有 106 个 Go 消费者消费 Cap'n Proto 原始日志并提取/准备 100 多个 ClickHouse 字段所需的数据。消费者不再执行任何聚合逻辑。
* **ClickHouse 集群** - 36 个节点，x3 的复制因子。它处理非聚合请求、日志摄取，然后使用材料化视图生成聚合结果。
* **区域分析 API** - 用 G o重写和优化的 API 版本，具有许多有意义的指标、健康检查和故障转移场景。

![](https://cdn.thenewstack.io/media/2023/07/2c587eb1-image3.png)
*Cloudflare 中央数据中心基于 Clickhouse 的服务器图表。来源：https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/*

正如你所看到的，新数据管道的架构更简单且具有容错能力。它为 Cloudflare 超过 700 万个客户域中的所有网站提供分析，总计每月超过 25 亿的独立访客和超过 1.5 万亿的每月页面浏览量。

### Yandex.Metrica

作为世界第二大网络分析平台，[Yandex.Metrica 使用 ClickHouse 处理超过一万亿行的数据](http://www.devdoc.net/database/ClickhouseDocs_19.4.1.3-docs/introduction/ya_metrika_task/)。一万亿行！Yandex 使用 ClickHouse 来进行以下工作：

* 存储用于会话重放的数据。
* 处理中间数据。
* 构建具有分析功能的全局报告。
* 运行用于调试 Yandex.Metrica 引擎的查询。
* 分析来自 API 和用户界面的日志。
  
这些使用案例以及处理的庞大数据量充分证明了 ClickHouse 的能力，但有趣的部分是 ClickHouse 如何处理这种规模。 ClickHouse 的底层架构设计，包括其分布式存储和计算能力，使 Yandex 能够轻松处理如此大量的数据。 ClickHouse 实施的灵活分片和复制策略确保数据的可靠性和高可用性，这是 Yandex 在高容量、高速度数据场景中的关键要素。

## PostgreSQL vs. ClickHouse: 分析比较

让我们来看看在处理典型的点击流和流量分析、网络分析、机器生成的数据、结构化日志和网络事件数据等工作负载方面，ClickHouse 与 PostgreSQL 相比如何表现。这个基准测试场景反映了自发分析和实时仪表板中的典型查询。使用的数据集是从世界上最大的网络分析平台的实际流量记录中获取的。ClickHouse 和 PostgreSQL 系统都经过了最佳调优，并在一台配置了 500GB gp2 存储的 c6a.4xlarge 服务器上部署。

基准数据来自 [ClickHouse 基准测试](https://benchmark.clickhouse.com/)。

### 数据加载时间

该参数指的是将数据集加载到数据库中所需的时间。

![](https://cdn.thenewstack.io/media/2023/07/b506de28-screenshot-2023-07-06-at-9.06.14-am.png)

基准测试显示， ClickHouse 加载数据的速度比 PostgreSQL 快得多。具体来说，与 PostgreSQL 相比， ClickHouse 加载数据的速度大约快 23 倍。

### 存储大小

该参数指的是数据库中数据占用的空间。

![](https://cdn.thenewstack.io/media/2023/07/7cf462ab-screenshot-2023-07-06-at-9.06.25-am.png)

ClickHouse 也证明了其存储效率更高。基准测试表明，对于相同的数据集，ClickHouse 使用的存储空间比 PostgreSQL 少 8.5 倍。

### 结论

根据 ClickHouse 的基准测试，当在相同条件下进行优化和部署时，ClickHouse 在数据加载时间和存储大小效率方面明显优于 PostgreSQL 。需要注意的是，这些结果涉及特定的分析场景，实际结果可能因特定的用例和系统调优而有所不同。

您还可以查看 ClickHouse 在[基准测试报告](https://benchmark.clickhouse.com/)中与其他数据库的比较。

## 开始使用 ClickHouse 的最佳方法是什么？

觉得自己可能已经准备好尝试 ClickHouse 了吗？有几种方式可以开始，其中最基本的是使用开源版本。

希望避免自己托管和扩展？ [Tinybird](https://www.tinybird.co/?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database) 是一种被开发人员亲切地称为 “ClickHouse++” 的工具，它不仅具有 ClickHouse 已经强大的功能，还提供[无服务器托管](https://www.tinybird.co/clickhouse?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database)，并为开发人员提供了更多专注于开发的好处，包括：

1. **与多个数据源的本地集成**（如 [Kafka](https://www.tinybird.co/integrations/kafka-data?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database)、[S3](https://www.tinybird.co/integrations/amazon-s3?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database)、[GCS](https://www.tinybird.co/integrations/google-cloud-storage?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database)、[BigQuery](https://www.tinybird.co/integrations/google-bigquery?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database)、[Snowflake](https://www.tinybird.co/integrations/snowflake?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database) S等）。它甚至提供了一个流式 HTTP 端点，可以直接从您的应用程序或服务中捕获事件。
2. **UI、CLI 和 API**：Tinybird 将强大数据库的复杂性抽象成[一个工作流程](https://www.tinybird.co/product?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database)，通过 UI、CLI 和 RESTful API 进行交互。
3. **快速 API 开发框架**：使用 Tinybird ，您可以使用可组合的 SQL 节点查询数据库表，并将查询即时发布为动态、文档化、安全和可扩展的 API ，为应用程序开发提供动力，就像[这个例子](https://www.tinybird.co/blog-posts/designing-and-implementing-a-weather-data-api?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database)中的那样。

## 那么，还在等什么呢？

如果您是数据工程师或软件开发人员，经常处理大量数据并进行实时分析，那么 ClickHouse 是您的最佳选择。一旦您体验了 ClickHouse（和 Tinybird）的速度，就再也回不去了。

## 了解更多

深入了解 ClickHouse ，请访问其[官方文档](https://clickhouse.tech/docs/en/)。

要了解 Tinybird 如何提升您的 ClickHouse 体验，请查阅 [Tinybird 文档](https://www.tinybird.co/docs?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q2-2023-the-new-stack&utm_term=clickhouse-database)。

## 常见问题解答

**问：ClickHouse 适合用于在线事务处理（OLTP）系统吗？**

答：不适合。ClickHouse 主要设计用于在线分析处理（OLAP）。它非常适合对大数据量进行实时分析查询，而不是事务性系统。

**问：ClickHouse 如何管理数据冗余和可用性？**

答：ClickHouse 支持异步多主复制。您可以配置它在不同节点上保留数据的副本，以提高可用性。

**问：ClickHouse 使用哪种语言进行查询？**

答：ClickHouse 使用SQL进行查询。因此，如果您熟悉 SQL ，您将感到非常熟悉。

**问：Tinybird 如何增强 ClickHouse 的功能？**

答：Tinybird 是一个无服务器平台，可以让您在 ClickHouse 之上高速构建实时分析 API 。它提供了针对实时应用程序开发设计的功能，为开发人员提供了更加舒适的开发体验。因此，它就像为您的 ClickHouse 设置添加了一个额外的速度和便利层。