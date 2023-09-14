<!-- 
# 实时访问后端数据库的变更数据捕获
https://cdn.thenewstack.io/media/2023/09/9f04c1f9-data-capture-1024x655.jpg
Image from wan wei on Shutterstock.

-->

利用 CDC，您可以从现有的应用程序和服务中获取最新信息，创建新的事件流或者丰富其他事件流。CDC赋予您实时访问后端数据库的能力。

译自 [Change Data Capture for Real-Time Access to Backend Databases](https://thenewstack.io/change-data-capture-for-real-time-access-to-backend-databases/) 。

在我最近发表在 The New Stack 的一篇文章中，我讨论了[实时数据库](https://thenewstack.io/real-time-databases-who-is-using-them-and-why/)的出现和重要性。这些数据库是为支持[事件驱动架构](https://www.tinybird.co/blog-posts/event-driven-architecture-best-practices-for-databases-and-files?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)中的[实时分析](https://www.tinybird.co/blog-posts/real-time-analytics-a-definitive-guide?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)而设计的。它们优先考虑高写吞吐量、低查询延迟，即使进行复杂的分析查询包括过滤、聚合和连接，以及高水平的并发请求。

这一高度专业化的数据库类，包括开源变种如 ClickHouse、Apache Pinot 和 [Apache Druid](https://thenewstack.io/apache-druid-a-real-time-database-for-modern-analytics/)，通常是在从零开始构建实时数据流管道时的首选。但更多时候，实时分析是作为对现有应用程序或服务的补充，其中传统的关系数据库如 [PostgreSQL](https://roadmap.sh/postgresql-dba)、SQL Server 或 MySQL 已经收集了多年的数据。

在我上面链接的文章中，我也简要地谈到了这些联机事务处理(OLTP)数据库在规模化分析方面并不优化。当涉及到分析时，它们无法提供必要水平的并发的相同的查询性能。如果您想更详细地了解为什么，请阅读[此文](https://www.tinybird.co/blog-posts/when-to-use-columnar-database?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)。

## 但互联网就是建立在这些数据库之上的！

基于行的数据库可能不适用于实时分析，但我们无法忽视的是，它们与世界各地和整个互联网的后端数据系统紧密集成。它们无处不在，它们托管着对我们想要构建的许多实时系统和用例至关重要和提供上下文的关键数据集。它们存储有关客户、产品、位置等的事实和维度，这些是我们希望用来[丰富流数据](https://thenewstack.io/the-engineers-guide-to-enriching-streams-and-dimensions/)并构建更强大的用户体验的。

那么，我们该怎么办？您如何将这种面向行的关系数据引入高速的实时分析世界？而且您要如何做到不压垮您的关系数据库服务器？

## 下面是不要做的

目前，从关系数据库获取数据并将其输入到分析系统中的主流模式是使用由编排器调度的批量提取、转换、加载(ETL)进程来拉取数据库中的数据，根据需要转换它，并将其转储到数据仓库中，以便分析人员可以对其进行查询以获得仪表板和报告。或者，如果您觉得高级一点，可以采用提取、加载、转换(ELT)方法，并让分析工程师在您复制到 Snowflake 中的 Postgres 表上构建 500 个 [dbt 模型](https://docs.getdbt.com/docs/introduction)。

对于实时分析来说，这几乎可以说是一种反模式。它不起作用。尤其是在处理实时数据时，[数据仓库是一个糟糕的应用后端](https://thenewstack.io/data-warehouses-are-terrible-application-backends/)。

![](https://cdn.thenewstack.io/media/2023/09/ea33c6c7-image3-e1693581965705.png)
*批量 ETL 进程按计划从源系统读取，这不仅会引入延迟，还会给您的关系数据库服务器带来压力。*

ETL/ELT 本身就不是为实时服务大量并发数据请求而设计的。从本质上讲，它在数据更新及其可用于下游使用者之间引入了不可承受的延迟。使用这些批处理方法，延迟超过一小时是常见的，五分钟的延迟就已算是可以期待的最快速度。

最后，ETL 会让您的应用程序或服务面临风险。如果您按计划(通常低效地)在源系统上执行查询，这会给您的数据库服务器带来压力，从而给您的应用程序带来压力并降低用户体验。当然，您可以创建读取副本，但现在您要付出双倍的存储成本，而且仍然面临相同的延迟和并发约束。

## 利用变更数据捕获(CDC)实现实时分析

然而，感谢实时变更数据捕获(CDC)，希望并未破灭。 CDC 是跟踪对数据库所做的更改(如插入、更新和删除)并实时将这些更改发送到下游系统的一种方法。

变更数据捕获的工作原理是监控数据库的事务日志。 CDC 工具读取事务日志并提取所做的更改。 然后这些更改被发送到下游系统。

![](https://cdn.thenewstack.io/media/2023/09/eff33cce-image2-e1693582016588.png)

变更数据捕获工具从数据库日志文件中读取并将更改事件传播到下游使用者的消息队列。

事务日志(如 PostgreSQL 的预写日志(WAL)或 MySQL 的 “binlog”)以时间顺序记录数据库更改和相关数据。 基于日志的 CDC 最大限度地减少了对源系统的额外负载，这使其优于在源表上直接执行查询的其他方法。

CDC 工具监视这些日志以获取新条目，并将它们追加到 Apache Kafka 等事件流平台或其他消息队列上的主题，在那里它们可以被下游系统如数据仓库、数据湖或[实时数据平台](https://www.tinybird.co/blog-posts/real-time-data-platforms?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)使用和处理。

## 利用变更数据捕获数据进行实时分析

如果您的服务或产品使用了微服务架构，则非常有可能您拥有几个(可能有几十个！)关系数据库，它们正在不断更新有关您的客户、产品甚至您的内部系统运行情况的新信息。 如果您能够实时分析这些数据以实现[实时推荐引擎](https://www.tinybird.co/blog-posts/real-time-recommendation-system?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)或在产品中[实时可视化](https://www.tinybird.co/blog-posts/real-time-data-visualization?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)等功能，或者在内部工具中实现异常检测、系统自动化或运营智能仪表板等功能，那不是很好吗？

例如，假设您经营一家电子商务企业。 您的网站通过一个关系数据库运行，该数据库跟踪客户、产品和交易。 每个客户操作，如查看产品、添加到购物车和购买，都会触发数据库中的更改。

利用变更数据捕获，您可以使这些数据源与实时分析系统保持同步，以提供管理库存、物流和积极客户体验所需的最新详细信息。

现在，当您想在结账期间向购物者展示个性化优惠以提高转换率和增加平均订单价值时，您可以依靠您的实时数据流管道，该管道由最新的变更数据提供支持。

## 如何构建实时 CDC 流管道？

好的，这一切听起来都很棒。 但是您如何构建 CDC 事件流管道呢？您如何将变更从关系数据库流式传输到可以运行实时分析的系统，然后将它们作为 API 暴露，以便您可以将它们纳入正在构建的产品中？

让我们从您需要的组件开始:

- **源数据系统**：这是由 CDC 跟踪的数据的数据库。 它可以是 Postgres、MongoDB、MySQL 或任何其他此类数据库。请注意，数据库服务器的配置可能需要更新以支持 CDC。
- **CDC 连接器**：这是一个监视数据源并捕获数据更改的代理。 它连接到数据库服务器，监视事务日志并将事件发布到消息队列。这些组件是为了浏览数据库模式并支持跟踪特定表而构建的。最常见的工具是 Debezium，这是一个开源的变更数据捕获框架，许多数据栈公司在其上构建了变更数据工具。
- **事件流平台**：这是您的变更数据的传输机制。 变更数据流被封装为消息，这些消息被放置在主题上，在那里它们可以被许多下游使用者读取和使用。 Apache Kafka 是这里的开源首选工具，[Confluent](https://www.confluent.io/?utm_content=inline-mention) 和 [Redpanda](https://redpanda.com/?utm_content=inline-mention) 等提供了一些 Kafka API 的灵活性和性能扩展。
- **实时数据库或平台**：对于批处理分析工作流程如业务智能和机器学习，这通常是一个数据仓库或数据湖。 但我们在这里进行实时分析，所以在这种情况下，我们会选择上面提到的实时数据库或[实时数据平台](https://www.tinybird.co/blog-posts/real-time-data-platforms?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)，如 [Tinybird](https://www.tinybird.co/?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)。 此系统订阅事件流平台上的变更数据主题，并将它们写入一个优化了低延迟和高并发分析查询的数据库。
- **实时 API 层**：如果您的目标与许多其他目标一样，是在变更数据流之上构建面向用户的功能，那么您需要一个 API 层来公开查询并按比例扩展以支持新的服务或功能。 这就是实时数据平台的优势所在，如 [Tinybird](https://www.tinybird.co/?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture) 天然提供了开箱即用的 API 创建。 否则，您可以使用经过验证的对象关系映射(ORM)并自己构建 API 层。

![](https://cdn.thenewstack.io/media/2023/09/7436c15d-image1-e1693582065341.png)
*一个用于 PostgreSQL 的实时 CDC 流管道示例。 请注意，除非您的目标包括 API 层，否则您必须构建一个以支持面向用户的功能。*

将所有这些组件组合在一起，您就拥有了一个建立在源数据系统的最新数据之上的实时分析流管道。 从那以后，您可以构建的仅仅取决于您的想象力(和 SQL 技能)。

## 变更数据捕获：使您的关系数据库实时化

变更数据捕获(CDC)弥合了传统后端数据库和现代实时流数据架构之间的间隔。 通过捕获和即时传播数据更改，CDC 赋予您从现有应用程序和服务中获取最新信息来创建新的事件流或丰富其他事件流的能力。

那么您还在等待什么？是时候利用那个 20 年历史的 Postgres 实例，并充分利用它了。 出发吧，研究适合您数据库的正确 CDC 解决方案，然后开始构建。如果您使用 Postgres、MongoDB 或 MySQL，这里有一些链接可以帮助您开始:

- [Postgres 实时变更数据捕获实用指南](https://www.tinybird.co/blog-posts/postgres-cdc?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)
- [MongoDB 实时变更数据捕获实用指南](https://www.tinybird.co/blog-posts/mongodb-cdc?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)
- [MySQL 实时变更数据捕获实用指南](https://www.tinybird.co/blog-posts/mysql-cdc?utm_source=the-new-stack&utm_medium=paid-publisher&utm_campaign=q3-2023-the-new-stack&utm_content=change-data-capture)
