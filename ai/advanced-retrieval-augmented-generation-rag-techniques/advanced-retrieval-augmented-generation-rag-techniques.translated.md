# 高级检索增强生成 (RAG) 技术

![高级检索增强生成 (RAG) 技术的特色图片](https://cdn.thenewstack.io/media/2024/10/a6dbc655-advanced-rag-techniques-1024x576.jpg)

[检索增强生成](https://zilliz.com/learn/Retrieval-Augmented-Generation?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns) (RAG) 近年来随着其日益普及，经历了许多进步。在 10 月 28 日 [All Things Open (ATO) 2024](https://thenewstack.io/event/all-things-open-2024/) 的演讲中，我将介绍构建更好的 RAG 所需的一些技术。这些技术包括 [分块](https://zilliz.com/learn/guide-to-chunking-strategies-for-rag?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns)、选择 [嵌入模型](https://zilliz.com/blog/choosing-the-right-embedding-model-for-your-data?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns) 和 [元数据结构化](https://zilliz.com/blog/metadata-filtering-hybrid-search-or-agent-in-rag-applications?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns)。

## 构建 RAG 系统的注意事项

构建 RAG 系统时，最重要的事情之一是使其能够处理您需要的数据类型。例如，文本有很多种类型——对话、文档、[问答](https://thenewstack.io/build-an-ai-powered-question-answering-application)、讲座和正式文档。您还必须准确确定您需要从数据中获取什么：是所有文本的转储，还是您在寻找特定的见解，还是仅来自嵌入式图表的信息？

与任何其他数据项目一样，您需要进行分析以确定您正在使用哪些数据、您将如何提取数据，以及需要哪些充实和转换。您的决策包括成本、规模、模型许可证、嵌入数据的时间以及它是否符合您的数据规范。

使用 [向量数据库](https://zilliz.com/learn/what-is-vector-database?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns) 和 RAG 时，非常重要的一部分是确定使用哪种 [嵌入模型](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai)，这些模型来自 HuggingFace、OpenAI、Google、Meta、PyTorch、Jina AI、Mistral AI 或 Nomic A 等提供商。有些模型用于密集 [嵌入](https://milvus.io/docs/embeddings.md?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns)，例如 BAAI/bge-base-en-v1.5，它生成 768 维浮点数向量。还有一些稀疏嵌入模型，它们主要生成零。

您还需要决定使用哪些 [工具](https://zilliz.com/product/integrations)；许多新工具使构建 RAG 不那么依赖手动操作，例如 LangChain、LlamaIndex、LangChain4J 或 Spring AI。您还可以使用 AI 提取-转换-加载 (ETL) 工具，例如 DataVolo、Cloudera DataFlow、Airbyte、StreamNative UniConn、Apache Spark、Apache Flink、Ray 和 Fivetran。

## 展望 RAG 的未来

除了讨论 RAG 领域的新进展外，在我的 ATO 演讲中，我还将分享一些示例，并展望未来，届时新的模型、技术、[向量数据库](https://thenewstack.io/scaling-databases-to-meet-enterprise-genai-demands) 和 AI 的进步将为整个概念注入强大的动力。这些进步包括：

- 分块
- 嵌入模型选项
- 元数据结构化
- GraphRAG
- 多语言与特定语言
- 多模态数据检索
- 查询增强
- 查询路由
- 分层索引
- 混合检索
- 代理 RAG
- 自我反思
- 查询路由
- 子查询

我还将简要概述一个使用 Milvus（一种开源向量数据库）的 RAG 系统，该系统将检索系统与生成模型相结合。通过将从 Milvus 快速检索到的智能上下文添加到您的提示中，您可以减少 LLM 的幻觉，这一点非常重要。

## 立即注册 ATO

立即 [注册](http://www.eventbrite.com/e/916649672847/?discount=NEWS20) 参加 All Things Open，参加我于 2024 年 10 月 28 日星期一美国东部时间上午 10:30 进行的演讲“[高级检索增强生成 (RAG) 技术](https://2024.allthingsopen.org/sessions/advanced-retrieval-augmented-generation-rag-techniques)”。

## 其他资源
[使用 Milvus 和 LlamaIndex 进行检索增强生成 (RAG)](https://milvus.io/docs/integrate_with_llamaindex.md)  
[使用分区键轻松实现高速多租户，为您的 AI 应用赋能](https://medium.com/@tspann/super-charge-your-ai-applications-with-easy-high-speed-multi-tenancy-with-partition-keys-5fa581127dd6)  
[使用 BM25 进行相关性排名](https://medium.com/@tspann/ranking-for-relevance-with-bm25-b2d9dd62e2f8)  
[Milvus 中的量化效果如何？](https://medium.com/@tspann/how-good-is-quantization-in-milvus-6d224b5160b0)  
[YOUTUBE.COM/THENEWSTACK 技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等内容。](https://youtube.com/thenewstack?sub_confirmation=1)