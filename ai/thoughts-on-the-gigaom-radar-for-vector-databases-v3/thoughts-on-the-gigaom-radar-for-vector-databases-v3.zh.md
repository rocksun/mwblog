GigaOm 最新发布了其第三版 [矢量数据库雷达图](https://content.vespa.ai/gigaom-report-v3-2025)。该报告使用 GigaOm 的结构化框架评估了 17 种领先的开源和商业解决方案，涵盖了基本功能、关键特性、新兴优势和更广泛的业务标准。

早期版本以 Sonar 报告的形式发布，Sonar 是 GigaOm 用于早期技术探索的格式。转向 Radar 格式标志着一个重要的转变：矢量数据库已超越实验阶段，并正在主流生产环境中得到采用。

在生成式 AI 的驱动下，[向量搜索](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/)已成为企业 AI 堆栈的核心部分。包括 [Oracle](https://www.oracle.com/developer?utm_content=inline+mention)、[IBM](http://www.ibm.com/products/webwhereas-hybrid-integration?utm_content=inline+mention)、Microsoft 等主要数据管理供应商都已在其平台中增加了向量功能。同时，专门从事向量技术的公司也在不断突破检索性能、多模态和相关性的界限。GigaOm 的 Radar 报告捕捉了这两个类别中快速发展的态势。

从报告中可以清楚地看出，正在出现不同的买家细分市场。一方面，大型企业正在扩展其现有数据平台，增加向量功能，以支持早期的 [检索增强生成 (RAG)](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) 项目、语义搜索或使用内部知识来指导 [大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/)。

这些解决方案可以很好地融入现有的生态系统，并提供强大的治理和合规性。对于希望与现有供应商保持一致的 CIO 来说，它们是员工面向的 GenAI 用例的实用选择，在这些用例中，性能和准确性不需要达到生产级水平。

另一方面，我将其描述为 [AI 搜索平台 — 为客户面向的应用而构建的系统](https://thenewstack.io/enterprise-ai-search-vs-the-real-needs-of-customer-facing-apps/)，其中搜索、排名和检索是产品体验的核心。想想类似 Perplexity 的对话式搜索、Spotify 规模的推荐或大规模个性化。

这些 [平台超越了向量搜索](https://thenewstack.io/beyond-vector-search-the-move-to-tensor-based-retrieval/)，将检索与集成的排名管道、多模态搜索、模型推理和分布式执行相结合。在准确性、延迟和规模至关重要的场景中，这类系统是必不可少的。Vespa 就是这类平台的一个例子。

介于这两个市场之间的是专门从事向量技术的公司，包括 Pinecone、Weaviate 和 Milvus。当团队希望快速启动项目时，这些平台表现出色。大多数公司提供服务器无服务器或 SaaS 体验，摩擦极小——启动一个端点，嵌入内容，测试一个 RAG 原型，并立即看到结果。

它们非常适合试点、实验和部门级用例。但是，随着项目的成熟和工作负载变得更加复杂或面向客户，许多团队会遇到问题：集成外部排名管道、调整混合检索、管理多模态或在高查询负载下可靠扩展。这些挑战并不会削弱它们在试点中的价值，但它们有助于解释为什么随着一些组织进入全面生产阶段，它们会“超越”专门的矢量数据库。

在所有细分市场中，有一个主题脱颖而出：单独的向量存储是不够的。有效的 AI 应用程序越来越依赖于混合检索、高级排名、多模态嵌入以及将向量搜索与更广泛的上下文集成的技术。这些趋势以及它们背后的技术考量，已在完整的 GigaOm Radar 报告中得到详细探讨。

## 下一步是什么？

生成式 AI 正在重塑客户体验和员工工作流程。如今，员工期望在家中使用过的直观的、由 AI 驱动的工具也能在工作中可用。但是，在碎片化的企业数据中大规模提供准确、值得信赖的答案仍然是一个真正的挑战。

[Snowflake](https://www.snowflake.com/?utm_content=inline+mention)、Redshift、Oracle 和 PostgreSQL 等主流数据平台已添加了基本的向量功能，使它们“足够好”，可以用于内部 GenAI 搜索，在这些搜索中，延迟和准确性要求不高。

与此同时，先进的客户面向场景，支持深度研究、交互式助手、个性化和大型非结构化搜索空间，需要更多：集成的排名、低延迟检索、多模态支持和大规模性能。这就是 [AI 搜索平台的用武之地](https://thenewstack.io/vector-search-is-reaching-its-limit-heres-what-comes-next/)。

在这个格局中，专门从事向量技术的公司面临被夹在中间的风险——一方面受到低端数据平台的挑战，另一方面受到高端集成 AI 搜索平台的挑战。市场正在迅速成熟，买家对于哪种架构类别适合哪种用例越来越清晰。

总而言之，这些趋势凸显了向量领域的演变速度之快，以及为什么最新的 GigaOm Radar 是一个如此有用的资源。该报告提供了对每个解决方案当前定位、哪些功能最重要以及该领域在未来 12 到 18 个月可能如何发展的结构化、供应商中立的视角。

无论您是正在试验早期的 RAG 原型、扩展现有的企业数据平台，还是构建以搜索为中心的 AI 应用程序，Radar 都提供了一个可靠的框架，帮助团队做出更明智的决策。我鼓励任何探索该领域的人深入阅读完整报告，以获得更深入、更全面的评估。

您可以在 [此处下载报告副本](https://content.vespa.ai/gigaom-report-v3-2025)。