# 使用您现有的向量数据库在 LLM 中使用您的数据

![使用您现有的向量数据库在 LLM 中使用您的数据的特色图片](https://cdn.thenewstack.io/media/2024/07/176c7349-server1-1024x576.jpg)

[向量数据库](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/) 允许您使用来自内部数据存储的数据来增强您的 LLM 模型。使用本地的事实性知识提示 LLM 可以让您获得针对组织已经了解的情况量身定制的响应。这减少了“AI 幻觉”并提高了相关性。

您甚至可以[询问 LLM](https://roadmap.sh/guides/introduction-to-llms) 在其答案中添加对它使用的原始数据的引用，以便您自己检查。毫无疑问，供应商已经推出了专有的向量数据库解决方案，并将其宣传为“魔杖”，可以帮助您消除任何 AI 幻觉的担忧。

但是，准备好一些好消息了吗？

如果您已经在使用[Apache Cassandra 5.0](https://cassandra.apache.org/_/Apache-Cassandra-5.0-Moving-Toward-an-AI-Driven-Future.html)、[OpenSearch](https://opensearch.org/) 或[PostgreSQL](https://www.postgresql.org/)，那么您的向量数据库成功已经准备就绪。没错：无需昂贵的专有向量数据库产品。如果您还没有使用这些免费且完全开源的数据库技术，那么您的生成式 AI 愿望是迁移的好时机——它们都是企业级的，并且避免了专有系统的陷阱。

对于许多企业来说，这些开源向量数据库是实施 LLM 的最直接途径——并且可能利用[检索增强生成 (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/)——提供量身定制的事实性 AI 体验。

向量数据库存储嵌入向量，嵌入向量是表示与数据片段相对应的空间坐标的数字列表。相关数据将具有更接近的坐标，允许 LLM 理解复杂和非结构化数据集，以实现生成式 AI 响应和搜索功能等功能。

RAG 是一种越来越受欢迎的过程，它涉及使用向量数据库将企业文档中的单词转换为嵌入，以便通过 LLM 对这些文档进行高效且准确的查询。

让我们更详细地了解每种开源技术为向量数据库讨论带来了什么：

## Apache Cassandra 5.0 提供原生向量索引

凭借其[最新版本](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/)（目前处于预览阶段），Apache Cassandra 通过包含开发 AI 应用程序的企业所需的一切，增强了其作为特别高可用性和可扩展的开源数据库的声誉。

Cassandra 5.0 添加了原生向量索引和向量搜索，以及用于嵌入向量存储和检索的新向量数据类型。新版本还添加了特定的 Cassandra 查询语言 (CQL) 函数，使企业能够轻松地将 Cassandra 用作向量数据库。这些新增功能使 Cassandra 5.0 成为支持 AI 工作负载和执行围绕管理智能数据执行企业战略的明智开源选择。

## OpenSearch 提供多种优势

与 Cassandra 一样，[OpenSearch](https://thenewstack.io/how-opensearch-visualizes-jaegars-distributed-tracing/) 是另一种非常流行的开源解决方案，许多寻找向量数据库的人恰好已经在使用它。OpenSearch 为搜索、分析和向量数据库功能提供了一站式服务，同时还提供卓越的最近邻搜索功能，支持向量、词法和混合搜索和分析。

使用 OpenSearch，团队可以加快开发 AI 应用程序的速度，依靠数据库提供其已知的稳定性、高可用性和最小延迟，以及扩展到数十亿个向量的可扩展性。无论开发推荐引擎、生成式 AI 代理还是任何其他结果准确性至关重要的解决方案，那些使用 OpenSearch 利用向量嵌入并消除幻觉的人都不会失望。

## pgvector 扩展使 Postgres 成为强大的向量存储

企业对 Postgres 并不陌生，Postgres 是世界上使用最广泛的数据库之一。鉴于该数据库只需要[pgvector 扩展](https://github.com/pgvector/pgvector) 就可以成为一个特别高效的向量数据库，无数组织只需简单地部署就可以利用理想的基础设施来处理他们的智能数据。
pgvector is particularly well-suited to providing exact nearest neighbor search, approximate nearest neighbor search, and distance-based embedding search, as well as identifying semantic similarity using cosine distance (recommended by OpenAI), L2 distance, and inner product. The efficiency of these features makes [pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/) a powerful and proven open-source option for training accurate LLMs and RAG implementations, while enabling teams to deliver trustworthy AI applications they can be proud of.

## Your AI Challenges' Answer Has Been Right in Front of You All Along?
The solution to customizing LLM responses isn't investing in some expensive proprietary vector database and then trying to circumvent the real risk of vendor lock-in or mismatches. At least it doesn't have to be. Recognizing that available open-source vector databases are among the best choices for AI development—including some you may already be familiar with or even already own—should be a very welcome revelation.

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
Technology is moving fast, don't miss an episode. Subscribe to our YouTube channel to watch all our podcasts, interviews, demos, and more.