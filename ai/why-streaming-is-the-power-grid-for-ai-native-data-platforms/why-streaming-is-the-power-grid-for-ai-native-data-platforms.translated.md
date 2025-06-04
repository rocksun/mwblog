# 为什么流处理是 AI 原生数据平台的电力网

![Featued image for: Why Streaming Is the Power Grid for AI-Native Data Platforms](https://cdn.thenewstack.io/media/2025/05/6b068a06-streaming-power-grid-ai-native-data-platforms-1024x576.jpg)

AI 正在改变每个业务，每个组织都在试图弄清楚他们如何能从 AI 中受益或赋能 AI。无论您目前处于路线图的哪个位置，您都应该了解以下两个事实：AI 需要上下文才能发挥作用，并且 AI 的最新技术正在迅速发展。

[数据仓库](https://towardsdatascience.com/data-warehouse-redefined-f65609454a01/)是第一个事实的关键：它是组织数据蔓延的汇聚地，使其成为 [AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)的完美中央数据源。鉴于第二个事实，我们还需要该平台具有敏捷性，并能够跟上持续的创新。

## 数据飞轮

正如 NVIDIA 首席执行官黄仁勋在[去年的 Snowflake 峰会](https://blogs.nvidia.com/blog/snowflake-summit-2024/)上所说，AI 允许在数据飞轮的每个阶段提取更多信息。

其核心是，飞轮的概念是，使用您产品的人会生成使用数据；更多使用数据将使您更好地了解人们如何从您的产品中受益；反过来，您可以更好地改进产品，最终获得更多的消费（和更多的数据）。让我们分解一下 AI 如何提高您执行这些阶段的能力：

### 更智能的洞察

AI 可以通过多种方式改进数据分析过程。它可以自动编写仪表板和 [SQL queries](https://roadmap.sh/sql) 的样板代码。它可以处理非结构化数据的报告，例如错误报告、用户反馈和支持问题，从而识别常见的趋势和模式。您可以使用嵌入大规模地聚类信息，并识别用户旅程中的差距以及错失的机会。

### 更好的产品

AI 可以通过多种方式集成到产品套件中：实现实时个性化或推荐，使用户能够自动化任务，或使用模型来总结历史活动和趋势。将 AI 集成到产品中时，重要的是添加护栏，衡量性能，并让您和您的用户确信代理的自动化正在按预期工作。最后，产品和开发团队可以将 AI 集成到他们的工作流程中，以更快地交付和测试新功能，从而使他们能够提前而不是推后时间表。

### 更多数据

AI 增强的产品提供了大量机会来捕获和衡量参与度，例如查看发送给聊天机器人的提示，或使用 AI 来推理手动分析过于繁琐的数据。此外，像基于 AI 的自动化这样的功能允许高级用户更深入地使用您的产品并获得更多价值。模型还能够从以前无法使用的数据湖源中清理和提取结构，从而为您提供更多可用的数据。

## 构建 AI 增强的产品

不能简单地将聊天机器人放到现有产品上并称其为 AI 增强的。需要经过深思熟虑，才能看到在哪里可以应用最大的价值，同时避免与这种新的和非确定性技术相关的风险。

要记住的关键是，这些模型是无状态的，并且没有关于您尝试提示它们完成的任务的上下文。您必须向它们提供完成任务所需的所有信息和说明。该上下文必须既准确又最新：过时的信息会损害性能，导致漂移，并在决策中引入风险。

例如，销售开发代表代理需要知道已启动哪些新功能，或者潜在客户可能正在经历哪些痛点。代表您的支持团队工作的 AI 需要能够识别其他最近的问题，推荐常见问题的解决方法，并快速显示有关客户及其产品使用情况的相关历史信息。

为了启用这些代理，您需要一个具有所有这些信息的数据仓库。您需要能够将企业中任何位置的数据添加到中央数据库。此外，仓库中的信息需要是最新的——没有人希望收到旧版本产品的推荐，或者错误地识别出您可以帮助潜在客户解决的痛点。

随着最近 AI 的发展，洞察和行动之间的时间窗口正在缩小。您希望能够在事件发生时立即调用代理来执行操作，而不是在下一个作业运行时。当与 AI 功能的快速创新相结合时，您需要一个足够灵活的数据平台来适应新功能和需求。

## 流处理是敏捷数据平台的关键
构建数据平台在很大程度上取决于你的技术栈、基础设施提供商和行业。然而，它们都具有共同的模式，其中一个模式对于快速迭代至关重要：[流式传输](https://thenewstack.io/data-streaming/)。

[数据流式传输](https://www.redpanda.com/blog/streaming-data-examples-best-practices-tools)是连续的、增量的数据流，被发送到消息总线或预写式日志（WAL）。采用流式传输引擎的主要优势在于，它使你能够解耦生产者（生成事件的应用程序）和消费者（日志中记录的接收者）。这使得可以动态地轻松添加或删除源，实时利用你的数据，将最新信息呈现给你的应用程序，并在事件首次发生时触发代理。

以全文或向量搜索引擎为例。在这些引擎中，索引数据会导致重建磁盘上的各种结构（尤其是在向量数据库中，这需要大型语言模型来计算每个文本片段的嵌入）。这使得批量处理来自单个源的操作更加有效。此外，在你的[检索增强生成](https://docs.redpanda.com/redpanda-connect/cookbooks/rag/)（RAG）管道中测试不同的嵌入模型或不同的分块技术时，长期存在的流的可重放性非常吸引人。

传统上，这不可行，但现代流式传输引擎可以利用[分层存储](https://www.redpanda.com/blog/cloud-native-streaming-data-lower-cost)将冷数据卸载到对象存储，这意味着你可以保持完全的可重放性，而无需连接另一条数据路径。所有这些辅助系统都可以成为原始事件流的物化视图。

另一个例子是利用来自数据库系统的[变更数据捕获](https://www.redpanda.com/guides/fundamentals-of-data-engineering-cdc-change-data-capture)（CDC）并将它们写入流式传输引擎。这使你可以拥有从数据库流式传输更改的消费者，从而实现对数据库事件的反应。它还有助于确保辅助数据系统（例如你的全文/向量搜索或你的分析数据库）具有关系数据库的副本，而无需通过尝试使所有这些系统保持同步来使你的应用程序复杂化。

通常，CDC流非常昂贵，因为它们可能会阻止WAL清理或以不同于传统数据库流量的方式对数据库造成压力。但是，登陆单个CDC流，然后让一个专门构建的系统将数据扇出到各种不同的消费者，可以使平台保持简单和可靠。添加新功能或同步两个系统不需要大量的仔细容量规划，你可以快速地将反应性添加到你的应用程序层。

例如，你可能希望调用一个代理并分析当用户立即降级其帐户时发生了什么。通过`user_plans`表的CDC流执行此操作意味着应用程序层不必重新构建其系统以允许其他应用程序对这些更改做出反应。

## 开放格式 = 自由和灵活性

正如流式传输是上述操作用例的核心一样，这些相同的事件可以物化到你的数据仓库中，为你提供用于分析查询的最新信息。直接事件数据可以转换为开放格式，如Apache Iceberg（某些流式传输引擎可以直接执行此操作，例如[Redpanda的Iceberg Topics](https://www.redpanda.com/blog/redpanda-25-1-iceberg-topics-ga)），或者将其流式传输到专有格式（例如[Snowflake中的Snowpipe streaming](https://quickstarts.snowflake.com/guide/redpanda-connect-ingestion-with-snowpipe-streaming/)）。或者，可以实时连接和处理流，以确保数据以任何形式落地，从而最大限度地提高其可查询性，而无需不断重新处理整个数据集的昂贵批处理作业。

像[Apache Iceberg](https://iceberg.apache.org/)这样的开放格式使你可以自由灵活地从许多不同的查询引擎中进行选择。例如，假设你是Google Cloud Platform用户，但使用Snowflake作为业务分析师和AI团队的数据仓库。

利用Apache Iceberg意味着你可以将Snowflake保留为你的主要数据仓库，还可以启用BigQuery以及所有可用于模型服务和训练的集成，而无需两次存储你的数据。这在不影响任一平台功能的情况下发生，因为Apache Iceberg带有完整的ACID事务模型、定义明确的模式演变策略、时间旅行查询以及通过[Apache Polaris](https://polaris.apache.org/)之类的目录进行细粒度访问控制。专有系统管理数据仓库的数据和元数据。
然而，使用 Iceberg，您可以选择将元数据保存在专有系统中，也可以选择像 Apache Iceberg REST catalog 这样的开放标准来进行元数据管理。

流处理还可以在数据传输过程中对其进行转换和连接，从而避免了大型批处理作业中代价高昂的数据重新处理。例如，如果您的数据在进入数据平台的分析平面中的长期存储之前有合规性或掩码要求，您可以在数据进入数据仓库时对其进行小的无状态转换。

## 最佳实践和 AI 原生数据平台的未来

使用流处理引擎作为数据平台的电力网可以释放极大的灵活性和响应能力，使您可以[实时](https://thenewstack.io/how-to-build-a-scalable-platform-architecture-for-real-time-data)利用您的数据。当您拥有一个快速移动的松散耦合系统时，请记住以下一些最佳实践，以保持系统的稳健性和可靠性。

首先，拥有一个 [schema registry](https://www.redpanda.com/blog/schema-registry-kafka-streaming) 非常重要，这样当设置新的应用程序以从您的数据流中读取数据时，它们可以无缝地安全地处理 schema 的演变。这些 schema 成为团队之间的契约，就像基于 HTTP 的服务具有 API 契约一样。当流式传输到数据仓库时，保持 schema registry 和查询引擎目录之间的 schema 同步可以确保批处理和流处理系统都使用一致的数据视图。将 schema 更改和发布作为 CI/CD 管道和 [infrastructure-as-code (IaC)](https://thenewstack.io/introduction-to-infrastructure-as-code/) 的一部分，还可以帮助您的工程团队在开发过程中更早地发现问题，而不是在暂存或生产环境中。

随着您的组织的发展和团队的变更，拥有 lineage 机制可以帮助您快速追踪问题或了解数据的来源。使用最佳实践，例如 [OpenTelemetry tracing standard conventions](https://opentelemetry.io/docs/specs/semconv/messaging/kafka/) 并使用 [record headers](https://www.redpanda.com/guides/kafka-cloud-kafka-headers) 传播 tracing 特别有用，因为组织为他们的所有可观测性数据采用 OpenTelemetry。

虽然事件驱动的架构可以释放适应性强、弹性好和响应迅速的平台，但它们可能被认为是昂贵的。您可以通过利用 [tiered storage](https://cwiki.apache.org/confluence/display/KAFKA/KIP-405%3A+Kafka+Tiered+Storage#KIP405:KafkaTieredStorage-Solution-TieredstorageforKafka) 等功能来卸载冷存储，[compression](https://www.redpanda.com/guides/kafka-performance-kafka-optimization) 来减少存储大小和带宽，[Google Protocol Buffers](https://protobuf.dev/) 或 [Apache Avro](https://avro.apache.org/) 等高效格式，以及 [tuning batching](https://www.redpanda.com/blog/batch-tuning-redpanda-performance-part-1) 来保持流处理系统的快速和高性能，从而降低成本。与任何系统一样，首先要做好可观测性，并在平台和使用规模扩大时监控使用情况。

虽然围绕安全性和这些新的 AI 应用程序的最佳实践一直在发展，但数据平台的基本原理（例如基于角色的访问控制、细粒度的访问控制列表 (ACL) 和最小权限原则）适用于流处理和批处理数据集。利用 [OpenID Connect](https://www.microsoft.com/en-us/security/business/security-101/what-is-openid-connect-oidc) 等标准进行身份验证和审计日志记录，以统一的方式监控所有系统中的访问。

最后，[real-time streaming data platforms](https://ai.redpanda.com/) 能够实现新兴趋势，例如 AI 运维 (AIOps)，使数据系统能够实时监控、优化和响应变化。如果没有流处理，您将被迫设置一个定期作业，从而增加迭代周期并减少 AI 代理用于处理平台中运维任务的训练数据量。

## 总结

随着技术的进步，洞察和行动之间的差距正在缩小。自动化系统可以即时生成和处理数据，而 AI 正在以前不可能的领域释放这种能力。

流处理作为数据平台的支柱，可以实现所有这些实时用例，并且随着 AI 通过开源模型进一步普及，以及采用这些强大的 AI 模型的成本降低，它将变得更加重要。随着组织希望为其 IT 系统采用越来越多的[自主性](https://www.redpanda.com/blog/autonomy-future-of-enterprise-ai-agent-infrastructure)，重要的是要确保您的数据平台设计为实时响应并跟上创新步伐。

[YOUTUBE.COM/THENEWSTACK](https://www.youtube.com/THENEWSTACK)
技术发展日新月异，不要错过任何一集。订阅我们的 [YouTube 频道](https://youtube.com/thenewstack?sub_confirmation=1) 来观看我们所有的播客、访谈、演示等。