随着工程领导者竞相构建具有代理能力的 AI 解决方案，许多人计划进行大规模的基础设施购买。但大多数人并不需要这样做。已经在运行其应用程序的完全开源的数据平台可以通过有针对性的升级来支持强大的 AI 代理。特别是对于长期预算而言，策略应该是尽可能地扩展现有资源，而不是彻底更换。

[代理型 AI](https://thenewstack.io/agentic-ai-is-quickly-revolutionizing-ides-and-developer-productivity/) 看起来很新颖，但其基础设施模式并非如此。代理需要流式输入、持久且可扩展的存储、低延迟检索和用于模型工作的弹性计算。这些与 [Apache Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/)、[Kubernetes](https://thenewstack.io/kubernetes/)、[Postgres](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/)、[Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/) 和 [OpenSearch](https://thenewstack.io/why-opensearch-3-0-is-your-must-have-upgrade-right-now/) 每天处理的模式相同。 提升在于特定于 AI 的优化，而不是替换堆栈。

## **代理型 AI 的现实检验**

代理摄取事件、检索上下文、做出决策、执行操作和学习。这与当今的开源构建块清晰地对应。Kafka 实时移动事件，因此代理可以根据上下文做出反应。Kubernetes 协调突发性的、需要大量 GPU 的工作负载，而不会造成浪费。Postgres（[使用 pgvector!](https://www.instaclustr.com/blog/how-to-improve-your-llm-accuracy-and-performance-with-pgvector-and-postgresql-introduction-to-embeddings-and-the-role-of-pgvector/)）添加了向量相似性搜索，用于检索增强生成 (RAG) 和语义查找。[Cassandra 5.0](https://hackernoon.com/heres-what-to-know-about-apache-cassandra-50https:/hackernoon.com/heres-what-to-know-about-apache-cassandra-50) 添加了全球范围内的本机向量索引。

OpenSearch 将向量搜索引入到熟悉的搜索和分析层。（OpenSearch [k-NN](https://docs.opensearch.org/latest/query-dsl/specialized/k-nn/index/) 通过 `knn_vector` 字段提供向量搜索，并支持常见的方法，如分层可导航小世界或 HNSW。）最终的结果是，可以使用您的团队已经在运行的平台来实现代理型 AI。

所有这些都不需要专有的“AI 就绪”平台，而是需要清晰的模式和紧密的接口。保留您熟悉的基础设施，在需要时添加向量功能，并针对代理的访问模式调整[流式传输和存储](https://thenewstack.io/store-more-pay-less-welcome-to-kafka-tiered-storage/)。

## **您可以立即构建的可组合蓝图**

你可以说我带有偏见，但我认为可组合性胜过单一性。理想情况下，您希望组装一套最少的、经过验证的组件，并按照各自的曲线进行扩展。

一个常见的蓝图可能如下所示：Kafka 或其他流式传输从应用程序、设备和服务中获取事件。特征存储或事件处理层丰富这些事件。Postgres 或 Cassandra 存储操作数据和嵌入。OpenSearch 索引文档和向量以实现快速检索。Kubernetes 调度代理服务、检索工作进程和模型运行时。一切都是可观测的和策略驱动的。

这种方法支持多种代理类型，而无需重建基础。支持代理使用与欺诈代理或文档分析代理相同的流和向量存储。您可以更改提示、检索规则和策略，但您不会更改核心基础设施。

可组合性还降低了风险。您可以添加一个试点代理，而无需干扰关键系统。您可以回滚，而无需与供应商谈判，而且重要的是，您可以在需求变化时更换组件。

## **您可以审计的安全性**

代理将处理客户数据和业务关键型决策，因此您需要透明度和控制。合适的开源数据层可以同时满足这两个要求。您可以审核代码路径、强制执行策略并验证控制。Kubernetes 提供基于角色的访问和网络策略；Kafka 支持加密和细粒度的授权；Postgres 和 Cassandra 提供强大的加密、角色和审计日志记录；OpenSearch 与常见的身份验证提供商和访问控制集成。

零信任立场自然契合。默认情况下，将每个服务、模型和代理视为不受信任，并在每一层强制执行最小权限原则。维护完整的日志记录，并清楚地了解数据流。当您拥有堆栈时，您可以向监管机构和董事会提供具体信息，而不是依赖供应商的保证。

## **从垂直切片开始**

理想情况下，在开始一个代理型 AI 项目之前，您应该根据代理生命周期清点您的堆栈。根据您已经部署的开源数据项目，您可能已经拥有了所需内容的 70% 到 80%。然后，在向量功能能够带来直接价值的地方添加它们。从影响最大的检索路径和最常见的内容类型开始。

我建议首先选择一个用例来验证该模式。良好的首批目标可能包括客户支持检索、销售支持搜索或内部知识助手。构建一个从头到尾运行的小型垂直切片（包括摄取、检索、代理和一个操作路径）。测量延迟、检索准确率和事件发生率。调整并重复。

从第一天起就通过绑定会话、在每个服务之间强制执行身份验证以及详细记录检索和操作来编写安全代码。定义代理绝不能做的事情，并在判断或风险较高的情况下让人类参与其中。

当托管服务对您的开源堆栈有意义时，您也可以选择它们来避免锁定，而无需将控制权让给决定您架构的专有平台。始终保持您的[选项开放并保持数据的可移植性](https://thenewstack.io/use-your-data-in-llms-with-the-vector-database-you-already-have/)。

## **现在就做好准备的优势**

当您已经拥有的开源数据堆栈可以完成大部分繁重工作时，代理型 AI 就触手可及了。立即在此基础上构建，以更快地交付、减少支出并保持对数据和风险的控制。