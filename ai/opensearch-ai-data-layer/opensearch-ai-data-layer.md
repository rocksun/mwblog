<!--
title: 揭秘 OpenSearch 如何争当 AI 默认数据层
cover: https://cdn.thenewstack.io/media/2026/05/fe0e7b3c-yana-kravchuk-qmtrqesja6o-unsplash-scaled.jpg
summary: OpenSearch 3.5/3.6 通过 BBQ 技术、原生智能体内存管理和混合搜索等更新，大幅提升了 AI 检索效率，旨在从搜索工具转型为 AI 应用的核心数据层。
-->

OpenSearch 3.5/3.6 通过 BBQ 技术、原生智能体内存管理和混合搜索等更新，大幅提升了 AI 检索效率，旨在从搜索工具转型为 AI 应用的核心数据层。

> 译自：[Inside OpenSearch's bid to become the default AI data layer](https://thenewstack.io/opensearch-ai-data-layer/)
> 
> 作者：Anil Inamdar

大多数与我合作的工程团队最初都是使用 [开源 OpenSearch](https://opensearch.org/) 进行日志分析和企业搜索。但由于他们的需求后来转向了语义检索和智能体内存，他们现在正试图弄清楚，可以将多少 AI 应用栈整合到他们已经运行的基础设施上。

2026 年第一季度在这一领域传来了非常好的消息。如果你接手了一个 OpenSearch 部署，并且现在被要求在其上运行智能体，那么 2 月和 4 月分别发布的 OpenSearch 3.5 和 3.6 非常值得深入了解。以下是需要掌握的重点。

## 稠密向量搜索与稀疏向量搜索并非不可替代

团队喜欢从 `knn_vector` 开始，这很容易理解。将其指向嵌入模型的输出维度，在索引上启用 k-NN，你就实现了近似最近邻搜索。默认配置（Faiss、HNSW、L2 距离）无需过多调整即可涵盖极其广泛的用例。

对于大规模运行的组织来说，3.6 版本中最重要的变化是“更好的二进制量化”（Better Binary Quantization，简称 BBQ），该功能现已从 Lucene 项目集成。BBQ 使用源自 RaBitQ 的量化方法，将高维浮点向量压缩为紧凑的二进制表示，从而将内存占用削减了 32 倍。

在 Cohere-768-1M 数据集上，BBQ 在 100 个结果下的召回率为 0.63，而 Faiss 二进制量化仅为 0.30。通过过采样和重打分，它在大型生产数据集上的召回率可以超过 0.95。OpenSearch 项目还致力于将 32 倍压缩设为默认值，这将消除手动调优的必要。

`knn_vector` 遇到困难的地方在于词项级的精度。稠密语义搜索基于含义检索结果（这很好！），但它可能会遗漏精确词项的相关性。例如，查询特定产品型号或技术标识符时，可能会出现概念上相似但并非你想要的精确匹配结果。

这就是 `sparse_vector` 缓解的问题。它不是将文档表示为连续向量空间中的一个点，而是将其存储为词元-权重对（token-weight pairs）的映射。每个词元是一个词汇表术语，每个权重反映了该术语对文档含义的核心程度。

3.6 版本的这些新增功能包括：支持精确召回工作负载的 BBQ flat 索引，以及用于神经稀疏近似最近邻搜索的 SEISMIC 算法，从而在*无需*全索引扫描的情况下实现大规模稀疏检索。

大多数生产级 AI 搜索应用都会同时使用两者。混合搜索将稠密语义召回与稀疏神经精度相结合，而这两种字段类型在构建时都考虑到了这种模式。根据我的经验，大多数团队从理解每种技术在流水线中的适用场景中获益，远比单纯挑选一个“胜者”更有价值。

> “混合搜索将稠密语义召回与稀疏神经精度相结合，而这两种字段类型在构建时都考虑到了这种模式。”

## OpenSearch 正在吸收智能体内存问题

在 3.5 版本之前，构建多轮对话智能体的团队必须在 OpenSearch 之外解决内存问题。你需要在其他地方维护会话存储，并在应用逻辑中管理上下文范围（同时还要自己完成所有连接工作）。

OpenSearch 3.5 将智能体对话内存直接移动到机器学习公共库（ML commons）中，通过基于钩子的上下文管理，让开发人员能够掌控智能体回话期间内存的存储、作用域和检索方式。

OpenSearch 3.6 则更进一步。新的语义和 [混合搜索](https://thenewstack.io/supercharge-your-rag-app-with-agentic-hybrid-search/) API 使智能体能够利用向量相似性、关键词匹配或两者结合来搜索存储的内存。参与长对话的智能体现在可以检索上下文相关的先前交流，而不仅仅依赖于最近的对话，当相关的历史记录并非最近一轮对话时，这一点至关重要。V2 Chat Agent 为基于聊天的流提供了更简洁的界面，同时保留了工具和内存集成。重建的 Dashboards 聊天界面增加了持久的对话历史记录，并由 ML Commons 智能体内存 API 提供支持。

这一切的实际效果是，智能体内存由平台原生处理，而不是由每个团队重复造轮子。基于钩子的 API 为工程师留出了足够的空间，让他们在需求偏离默认值时定制行为，而无需从头开始构建整个系统。

## 生产环境中一些较少被提及的重要变化

ML Commons 智能体框架中的 Token 使用量跟踪是 3.6 版本中最直接实用的新增功能之一。智能体执行过程中的每一次 LLM 调用都经过了检测，无需配置即可提取并聚合 Token 计数（按轮次和按模型）。它支持 Amazon Bedrock Converse、OpenAI v1 和 Gemini v1beta。如果你的团队一直在运行智能体，却无法了解 API 调用的成本或哪些步骤最昂贵，那么这就是一个明显的进步。

> “如果你的团队一直在运行智能体，却无法了解 API 调用的成本或哪些步骤最昂贵，那么这就是一个明显的进步。”

异步加密重构虽然不太显眼，但修复了一个重要的可靠性问题。旧有的 EncryptorImpl 使用带有三秒超时的阻塞式 CountDownLatch 来管理主密钥初始化。在并发请求期间，这会导致线程争用和竞态条件，多个租户同时访问加密层可能会触发重复的密钥生成。

由我的 NetApp Instaclustr 工程同事 [Abdul Muneer] 贡献的新实现，用基于 ActionListener 的方法取代了旧方法，该方法会将请求排队，并在密钥就绪后进行处理。（顺便提一下：想亲自参与贡献吗？点击[此处](https://opensearch.org/blog/how-to-start-contributing-to-opensearch-a-beginners-guide-based-on-my-journey/)阅读 Abdul 撰写的相关博客。）在高吞吐量环境中，旧设计在负载下会产生间歇性故障。

转向可观测性：在 3.6 版本之前，调试失败的多步智能体执行意味着要拼凑自己的检测工具。OpenSearch 现在通过基于 OpenTelemetry 标准构建的应用性能监控（APM）解决了这一问题，将 RED 指标、分布式追踪、服务地图和 SLO 跟踪引入了 OpenSearch Dashboards。

时间序列指标被路由到 Prometheus，追踪数据保留在 [OpenSearch](https://thenewstack.io/opensearch-3-2-delivers-hybrid-search-enhanced-observability-tools/) 中，Data Prepper 根据查询模式处理分流。智能体追踪插件为团队提供了一个专用视图，可以直接从 UI 调试智能体执行情况。

## OpenSearch 是否正成为 AI 应用的默认数据层？

3.6 版本中的 opensearch-agent-server 增加了一个多智能体编排层，用于集成 OpenSearch Dashboards 和 [模型上下文协议](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)（Model Context Protocol，简称 MCP）。MCP 已成为 AI 系统与外部工具及数据源通信的标准。它的加入说明了某种意图。该项目正朝着让 OpenSearch 成为智能体工具生态系统完整参与者的方向发展，而 MCP 则是其中的连接纽带。

这种方向在 3.5 版本中就已显现，当时该项目引入了实验性的智能体-用户交互协议。OpenSearch 正在构建一个持久、可观测、具备内存能力的 AI 应用底层，并提供所需的协议支持，以无缝嵌入更广泛的智能体栈。

尚未考虑智能体的团队仍能从 3.5 和 3.6 版本中获得明确价值，特别是在向量搜索和压缩方面。但在我看来，发展路线图已经非常清晰。

OpenSearch 并不是在努力成为一个更好的 Elasticsearch；它正专注于成为构建 AI 应用的数据层。