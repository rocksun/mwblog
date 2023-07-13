# 数据仓库是糟糕的应用程序后端

尽管商业智能分析有用，但它们无法以效益化的方式满足面向数据应用的实时性、延迟性和并发性的需求。

翻译自 [Data Warehouses Are Terrible Application Backends](https://thenewstack.io/data-warehouses-are-terrible-application-backends/) 。

![](https://cdn.thenewstack.io/media/2023/07/add14bab-data-warehouse-1-1024x505.jpg)

日益增长的数据洪流已经成为当今开发者的富余困境。根据 [Seagate 的报告](https://www.seagate.com/www-content/our-story/trends/files/Seagate-WP-DataAge2025-March-2017.pdf)，到 2025 年，全球的数据量将激增至惊人的 163 泽字节，比 2016 年增长 10 倍以上。更多的数据应意味着更深入的洞察和更好的用户体验，但它也会导致问题。

对于面向数据的开发者来说，这种爆炸式增长是一把双刃剑。它提供了一个利用数据和[实时分析](https://www.tinybird.co/blog-posts/real-time-analytics-a-definitive-guide?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_term=data-warehouse-backend&utm_content=inline-mention)来构建用户特征的无与伦比的机会。另一方面，以最小延迟和高并发处理所有这些数据对于典型的现代数据堆栈来说可能是一个巨大的挑战。

特别是，[数据仓库](https://www.tinybird.co/blog-posts/why-data-warehouses?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_term=data-warehouse-backend&utm_content=inline-mention)成为当今公司大数据的首选存储地，它们的在线分析处理(OLAP)方法非常适合针对业务智能报告和仪表盘等目的，对大数据执行复杂的长时间运行的分析查询。

然而，它们当应用后端效果很糟糕。

本文解释了为什么作业池管理、并发约束和延迟问题都阻止了数据仓库有效地作为面向用户的应用程序的存储层发挥作用，以及为什么您应该考虑为您的数据应用堆栈选择替代技术。

## 了解数据仓库

十年前，数据仓库在数据世界中是非常热门的新事物。数据仓库能够存储大量结构化数据并处理复杂的分析查询，它们为企业运行内部业务智能流程设置了新标准。

特别是，数据仓库具有以下三个功能，使分析变得可访问和强大:

1. 它们分离存储和计算，降低扩展成本。
2. 它们利用分布式计算和云网络最大化查询吞吐量。
3. 它们使用众所周知的 SQL 民主化分析。

如果您想深入了解数据仓库的存在原因以及它们为现代数据团队启用的功能，我鼓励您阅读[这个](https://www.tinybird.co/blog-posts/why-data-warehouses)文章。

如今，像 Snowflake、BigQuery、Redshift 和 Azure Synapse 这样的数据仓库在许多公司的数据堆栈中仍然占据重要位置，由于在组织内的优先地位，开发人员可能会倾向于将它们用作面向用户的分析的存储层。它们有能力运行这些用例所需的复杂分析查询;数据已经在那里，您已经为它们支付了费用。有什么不好的呢?

事实证明，有很多不好的地方。以下是为什么应用程序开发人员不能依赖数据仓库作为他们面向用户的分析的存储层的原因。

## 不可预测的作业池和非确定性延迟的世界

数据仓库以作业池的形式处理分析查询。[例如](https://www.tinybird.co/blog-posts/real-time-solutions-with-snowflake)，Snowflake 使用共享池方法并发处理查询，旨在优化可用的计算资源。

这里的问题是:作业池创建了具有固定下限的非确定性延迟。Snowflake 上的一个简单的 **SELECT 1** 可能只需要几毫秒，但更可能的是，由于必须与所有其他查询一起在队列中处理，它至少需要一秒钟或者更长时间。

即使最佳的[查询优化策略](https://www.tinybird.co/blog-posts/5-rules-for-writing-faster-sql-queries)也无法克服这一限制。

在数据仓库上运行查询就像玩“延迟轮盘赌”游戏。您可以每次以相同的方式旋转轮盘，但最终结果(在这种情况下，查询响应的延迟)会不可预测地出现。

现在，如果您是一个在存储层上构建 API 的后端开发人员，您绝不会冒非确定性延迟的风险。用户期望快速响应的 API，响应时间在毫秒级内。事实上，数据库查询应该是请求路径中最快的部分之一，即使与网络延迟相比也是如此。如果您在数据仓库之上构建，情况就不会如此，您的用户会感受到痛苦。

## 可扩展性的幻觉

对于 API 构建者来说，延迟只是方程式的一部分。第二个是并发性。如果您正在构建预期可以扩展的 API，那么[稳固的基础](https://thenewstack.io/the-fundamentals-of-data-api-design/)要求您为大量并发用户提供低延迟响应。

当您深入研究数据仓库的功能时，您会意识到为了真正横向扩展以适应增加的查询并发性，您需要启动新的虚拟数据仓库或者增加群集限制，或者两者兼而有之。例如，如果您想在 Snowflake 上支持每分钟仅 100 个并发查询，您需要 10 个多集群数据仓库。

而启动新数据仓库的成本不菲。去[问问你在数据工程部门的伙伴们](https://www.tinybird.co/blog-posts/5-snowflake-struggles-that-every-data-engineer-deals-with)吧。对于 Snowflake 的例子，您[每个月将支付超过 30，000 美元](https://www.tinybird.co/blog-posts/real-time-solutions-with-snowflake#a-realistic-example)。

Snowflake 等数据仓库中的并发约束呈现了开发实时应用程序时面临的最重大挑战之一。随着大量查询敲打您的数据仓库的大门，以及有限的资源来为它们提供服务，除非您进行扩容，否则您一定会遇到严重的延迟问题。而扩容的成本往往过高。

## 构建缓存层：一种近期趋势及其缺点

好吧，没有人会真的在数据仓库之上直接构建一个应用程序，对吧?显然，您会使用 [Redis](https://redis.com/?utm_content=inline-mention) 或其他[实时数据库](https://thenewstack.io/real-time-databases-who-is-using-them-and-why/)等缓存层，以确保即使在许多并发用户的情况下，您的 API 请求也很快且负载均衡。

![](https://cdn.thenewstack.io/media/2023/07/d9f44aba-image3-e1689172194931.png)

这是一种常见的方法，当您需要支持的应用程序中的数据驻留在数据仓库中时。从理论上讲，这种方法似乎可行。但在现实中，它带来了一些严重的缺点，其中最重要的是数据的实时性。

简单地说，使用缓存层可以大大缩短查询延迟，但它仍然无法用于构建必须始终服务最新事件的流数据之上的应用程序。

想象一个[欺诈检测用例](https://www.tinybird.co/blog-posts/how-to-build-a-real-time-fraud-detection-system)，其中金融机构必须在完成交易(几秒钟)的时间内确定交易是否存在欺诈。这通常涉及基于刚创建的数据的复杂分析过程或[在线机器学习特征库](https://www.tinybird.co/blog-posts/using-tinybird-as-a-serverless-online-feature-store)。如果该数据在您的后端 API 之前进入数据仓库，则不存在任何缓存层可以拯救您。缓存层非常适合通过存储在[批处理 ETL(提取、转换、加载)流程中最近运行的分析](https://www.tinybird.co/blog-posts/event-driven-architecture-best-practices-for-databases-and-files)来启用低延迟的 API 请求，但它无法访问刚创建的数据，因为数据仓库仍在处理这些数据。

## 替代方案：实时数据平台

正如我们所讨论的，在数据仓库之上构建数据密集型应用程序的根本问题归结为无法维持:

* 低延迟查询
* 来自高并发用户
* 在实时数据上

那么，替代方案是什么呢?

对于构建面向用户的应用程序，您应该使用[实时数据平台](https://www.tinybird.co/product)，如 [Tinybird](https://www.tinybird.co/) 。

## 什么是实时数据平台?

实时数据平台帮助数据和工程团队在大规模流数据上创建高并发、低延迟的数据产品。

实时数据平台在引擎盖下使用[列式数据库](https://www.tinybird.co/blog-posts/when-to-use-columnar-database)，因此它可以处理以前只降级到数据仓库的复杂分析工作负载，但速度要快得多。此外，实时数据平台通常提供低延迟发布层，为可能依赖于批处理和流数据源的数据密集型应用程序公开低延迟 API。在流数据平台上按规模构建 API 通常不被考虑，但随着数据的增长，维护和扩展可能会成为巨大的痛点。

## 实时数据平台的参考架构

在实时数据平台之上构建时，请考虑数据堆栈的两种增量架构。

在第一种方法中，数据仓库仍然可以是主要的支撑存储层，而实时数据平台实际上充当发布层。在这种架构中，数据在数据仓库和实时数据平台之间以计划的方式或在摄取时同步，实时数据平台处理额外的转换以及提供低延迟、高并发的 API。

![](https://cdn.thenewstack.io/media/2023/07/7ba0b530-image1-e1689172257371.png)
*实时数据平台如 Tinybird 可以通过使用本机连接器作为数据仓库上的缓存层运行。通过这种方式，它们消除了编写自定义对象关系映射(ORM)代码的需要，但仍可能会遭受一些数据实时性约束。*

在实践中，这类似于在数据仓库上使用实时数据平台作为缓存层，额外的好处是避免了编写自定义 API 代码将缓存连接到应用程序，并具有使用完整联机分析处理(OLAP)的强大功能进行额外的增强或转换的能力。

第二种方法完全绕过数据仓库或并行运行。假设事件数据被放置在某种消息队列或流平台上，实时数据平台订阅流主题并在创建数据时摄取数据，执行必要的转换并为应用程序使用提供 API 层。

![](https://cdn.thenewstack.io/media/2023/07/df9e6486-image2-e1689172310954.png)
*实时数据平台如 Tinybird 可以通过使用本机连接器作为数据仓库上的缓存层运行。通过这种方式，它们消除了编写自定义对象关系映射(ORM)代码的需要，但仍可能会遭受一些数据实时性约束。*

这可能是首选方法，因为它消除了仍存在于数据仓库上使用缓存层的数据实时性问题，并且使用正确的实时数据平台，流式摄取可以非常简单。

## 实时数据平台的好处

1. **原生数据源连接器**：实时数据平台可以与各种数据源和其他技术栈组件集成。这使得统一和连接多个数据源以实现实际用例变得非常简单。例如，您可以将来自 [Snowflake](https://www.tinybird.co/blog-posts/real-time-solutions-with-snowflake) 或 [BigQuery](https://www.tinybird.co/blog-posts/real-time-applications-with-bigquery-connector) 的数据与 [Confluent](https://www.tinybird.co/blog-posts/real-time-streaming-analytics-confluent-connector-tinybird) 或 [Apache Kafka](https://www.tinybird.co/docs/ingest/kafka.html) 的流数据相结合。例如，Tinybird 甚至提供了一个简单的 [HTTP 流端点](https://www.tinybird.co/docs/ingest/events-api.html)，可以轻松地直接在上游应用程序代码中流式传输事件。
2. **实时 OLAP 功能**：与数据仓库一样，实时数据平台为开发人员提供运行复杂 OLAP 工作负载的能力。
3. **经济高效**：使用传统方法在 Snowflake 上建立发布层将需要额外的虚拟数据仓库，从而导致[成本增加](https://www.tinybird.co/blog-posts/real-time-solutions-with-snowflake#snowflake-will-cost---30k-a-month)。相比之下，实时数据平台的[定价模型](https://www.tinybird.co/docs/billing/plans-and-pricing.html)通常以通过发布层处理的数据量为基础，这大大降低了用作应用后端时的成本。
4. **可伸缩性**：许多实时数据平台是无服务器的，因此基础架构随您的业务增长而扩展，使用高级别的性能和可用性来处理大数据。与在裸机服务器上托管数据库或使用托管数据库调整集群设置不同，您可以专注于构建和交付用例，而实时数据平台将在引擎盖下处理规模。
5. **零胶水代码**：即使在数据仓库上使用缓存层，您仍然需要编写粘合代码:将数据从仓库移到缓存的 ETL，以及从缓存发布 API 的对象关系映射代码。相比之下，实时数据平台处理整个数据流，从摄取到发布，零胶水代码。使用本机连接器同步数据，使用 SQL 定义转换，并使用内置文档、认证令牌管理和动态查询参数即时[发布可伸缩 API](https://www.tinybird.co/docs/concepts/apis.html)。

![](https://cdn.thenewstack.io/media/2023/07/07329be8-image4-e1689172386107.png)
*与数据仓库一样，Tinybird 提供了基于 SQL 的转换的 OLAP 存储。与数据仓库不同，它保留了数据的实时性并提供了低延迟、高并发的 API 层以支持应用程序开发。*

当数据仓库作为应用后端失效时， Tinybird 等实时数据平台则大放异彩。与数据仓库一样，这些平台支持大数据量和复杂的分析，但它们以保留数据实时性、最小化查询延迟并扩展以支持高并发的方式做到了这一点。

## 总结

数据仓库不是坏技术，但它们是糟糕的应用后端。尽管它们在业务智能方面强大且有用，但它们无法以具有成本效益的方式处理面向数据应用程序必须支持的实时性、延迟和并发需求。

另一方面，[实时数据平台](https://www.tinybird.co/product)在各种各样的数据密集型应用程序的后端起着非常好的作用，跨许多用例:实时个性化、产品内分析、运营智能、异常检测、基于用量的定价、体育博彩和游戏、库存管理等等。

