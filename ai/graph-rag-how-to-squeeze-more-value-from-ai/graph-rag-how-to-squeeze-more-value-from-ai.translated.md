# 图 RAG：如何从 AI 中榨取更多价值

![图 RAG：如何从 AI 中榨取更多价值的特色图片](https://cdn.thenewstack.io/media/2024/10/54702e16-graph-rag-squeeze-value-1024x576.jpg)

如今，似乎每个人都在做[检索增强生成 (RAG)](https://thenewstack.io/fixing-relevancy-in-retrieval-augmentation)，并且越来越多的人正在添加知识图谱来构建[图 RAG](https://thenewstack.io/boost-llm-results-when-to-use-knowledge-graph-rag/)。但他们中的许多人却卡在了研发阶段，难以（至少有点困难）将他们的概念验证投入生产。

图 RAG，就像大多数 AI 技术一样，也受制于一些难以避免的规则：

**强大的潜力：**图 RAG 可以为企业带来显著的价值。**易于上手：**实现简单的图 RAG 很直观。**难以完善：**将图 RAG 从概念验证阶段过渡到生产阶段很困难。

一家在图 RAG 方面取得成功的企业是[Glean](https://www.glean.com/)，这是一个连接组织内部数据并通过人工智能 (AI) 接口和代理使其全部可搜索和交互的平台。Glean[刚刚在最新一轮融资中获得了超过 2.6 亿美元](https://www.glean.com/blog/glean-series-e-prompting-launch)，这得益于其核心平台的强大功能、普及程度和盈利能力——其基础是图 RAG。

Glean 已经实施了一个基于图 RAG 的平台，该平台可以增加价值、降低成本并简化内部流程，从而使用最新的工具更容易开始使用图 RAG。即便如此，特定的图 RAG 挑战可能会使从研发过渡到生产变得困难，但有一些方法可以最大限度地提高成功的几率。

## 在正确的时间连接正确的信息是 $$$$

需要注意的是，Glean 是其自身产品的强大用户。如果您想知道这家拥有众多知名客户（包括 Pinterest、Reddit 和 Instacart）的五岁公司成功的秘诀，那么规模如此之大的运营良好的组织通常会简化其作为组织的运营方式。Glean 运行在 Glean 上这一事实——以及其客户非常满意——必须是其产品最有力论据之一——以及其增加企业价值的潜力。

Glean 的客户之一是“全球最大的网约车公司之一”，该公司在尝试构建内部解决方案但未能达到预期后，转向了 Glean。在一个月内，该公司在 Glean 平台上的使用量是其内部解决方案的两倍。

我们 DataStax 非常喜欢 Glean，既从作为客户的角度来看，也从最近作为合作伙伴[整合 Langflow 和 Glean](https://www.datastax.com/blog/glean-datastax-partner-to-help-developers-harness-enterprise-search?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean) 的角度来看。但这里的主要观点是，Glean 的故事不仅完美地展示了图 RAG 的强大功能和价值，也展示了即使对于一些科技巨头来说，正确使用图 RAG 也是一项挑战。

这家大型网约车公司表示，在切换到 Glean 后，它平均每周为每位员工节省 2 到 3 个小时，每年节省超过 2 亿美元——所有这些都来自员工“更快地找到信息”，Glean 的 CMO [Matt Kixmoeller](https://www.linkedin.com/in/mattkix/) [告诉 VentureBeat](https://venturebeat.com/data-infrastructure/how-to-take-advantage-of-a-generative-tool-fueling-gleans-260m-raise-graph-rag/)。时间就是金钱，节省大量时间就是节省大量金钱——但前提是工作要做好。

在下面，我将讨论中等水平的图 RAG 和优秀的图 RAG 之间的一些细微差别，但首先让我们谈谈如何轻松上手。

## 开始使用图 RAG 很容易

那么，如果一家大型网约车公司无法有效地构建自己的平台，为什么我会说自己实现图 RAG 很容易呢？

首先，支持 RAG 和图 RAG 的技术在过去一年中取得了长足的进步。12 个月前，大多数企业甚至没有听说过检索增强生成。现在，不仅 RAG 支持是最好的 AI 构建工具（如[LangChain](https://python.langchain.com/docs/tutorials/rag/)）的关键功能，而且现在还有[Langflow](https://www.datastax.com/blog/rag-development-is-hard-enter-langflow?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean)，一个基于 LangChain 的 RAG 的可视化 IDE，它允许您几乎无需代码即可设置 RAG 系统。

### 一些入门资源

* [LangChain 文档](https://python.langchain.com/docs/tutorials/rag/)
* [Langflow 文档](https://www.datastax.com/blog/rag-development-is-hard-enter-langflow?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean)
* [Glean 博客](https://www.glean.com/blog/)
* [DataStax 博客](https://www.datastax.com/blog/)
关于 RAG，还有很多东西要学，正如我们的 [检索增强生成指南](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean) 所解释的那样，但你不需要了解所有这些才能开始。只需几分钟就可以（免费）启动并运行 RAG 应用程序 [使用 Langflow 和 DataStax Astra DB](https://docs.datastax.com/en/langflow/examples/vector-rag-example.html)。

[图 RAG](https://medium.com/building-the-open-data-stack/a-guide-to-graph-rag-a-new-way-to-push-the-boundaries-of-genai-apps-f616d47758a0) 是 RAG 策略的一种较新的变体，因此软件工具通常与普通 RAG 一样成熟。但仍然有一些简单的方法可以开始。
如果你已经在使用 LangChain，那么最快的实现图 RAG 应用程序的途径之一是 [GraphVectorStore](https://www.datastax.com/blog/now-in-langchain-graph-vector-store-add-structured-data-to-rag-apps?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean)，它最近被添加到 LangChain 中。它本质上是在典型的向量存储中添加了图功能。有了它，你可以 [轻松地将 RAG 转换为使用链接的图 RAG](https://thenewstack.io/boost-llm-results-when-to-use-knowledge-graph-rag/)，这些链接可能已经存在于你的文档数据集中。

许多刚接触图 RAG 的人认为，从普通 RAG 到图 RAG 的复杂性存在巨大差距，或者他们需要一个专门的图数据库。但 [你不需要图数据库](https://www.datastax.com/blog/knowledge-graphs-for-rag-without-a-graphdb?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean) 来做图相关的事情，包括图 RAG。

即使是扩展图 RAG 系统也可以很简单，正如文章“[通过消除边来扩展知识图](https://thenewstack.io/scaling-knowledge-graphs-by-eliminating-edges/)”所解释的那样。

几乎所有 AI 领域的主要参与者都提供资源来帮助你理解和开始使用 RAG（甚至还有 [Coursera 课程](https://www.coursera.org/projects/introduction-to-rag)）。

有了所有可用的工具和教程，开始使用图 RAG 是最容易的部分……

## 但将图 RAG 推向生产却很难
图 RAG 似乎有望增强检索增强生成 (RAG) 系统，尤其是在传统向量搜索无法处理涉及跨不同上下文和格式的多个文档的复杂查询时。然而，将图 RAG 推向生产会带来独特的挑战。

### 了解图 RAG 的作用
通常，RAG 系统在简单场景中表现出色，但在需要跨不同知识库聚合信息时会遇到困难。这通常会导致系统错过关键文档——不是因为故障，而是因为这些文档与用户的查询缺乏足够的语义相似性。

例如，如果必要的信息嵌入在密集的、详细的内容中，或者如果文档涵盖了一系列语义上松散相关的主题，那么 RAG 系统可能会忽略相关文档。当处理需要一般信息和特定信息的语义搜索查询时，这尤其成问题。

### 解决检索差距
图 RAG 旨在解决的核心问题是普通检索增强生成系统的局限性，这些系统仅依赖于语义接近度，[因此无法检索语义上不太明显但相关的信息](https://towardsdatascience.com/vector-embeddings-are-lossy-heres-what-to-do-about-it-4f9a8ee58bb7)。修改 [向量](https://thenewstack.io/why-vector-size-matters) 搜索以增强检索通常涉及对嵌入进行复杂的调整，这不仅在技术上要求很高，而且成本高昂，并且可能对用户查询的特定细微差别无效。

与其改进语义模型以强行匹配——这可能会导致更多问题——不如集成知识图，提供更具针对性的方法。知识图能够连接语义模型遗漏的相关概念。例如，通过知识图链接地理或上下文相关的术语，[例如“太空针”和“下皇后安妮区”，](https://towardsdatascience.com/your-documents-are-trying-to-tell-you-whats-relevant-better-rag-using-links-386b7433d0f2) 比尝试调整嵌入以实现相同结果更直接、更可靠。

### 构建有效的图 RAG 系统
成功实现图 RAG 的关键在于准确地捕获和利用数据之间的非语义关系。通过用结构化的、基于图的数据增强语义搜索，我们可以增强文档检索，以更好地响应复杂查询。
为了总结我们试图用图 RAG 解决的问题：在非结构化文档中出现的许多概念之间存在半结构化、非语义信息连接。我们希望利用这种连接信息来补充语义向量搜索，以便检索最适合回答用例中提示和问题的文档。我们只是想让检索变得更好，并且我们想使用一些外部信息或外部逻辑来实现这一点，而不是仅仅依靠语义向量搜索来连接提示和文档。

### 集成图和 RAG 的指导原则
在构建和测试图 RAG 应用程序时，请牢记以下一些指导原则：

- 图应该包含高质量、有意义的概念和连接。
- 概念和连接应该与用例集中的提示相关。
- 图连接应该补充而不是替代向量搜索。
- 应该优先考虑一、两步图连接的实用性；仅在专门的用例中才应依赖超过三步的连接。
遵循这些原则旨在共同提高可解释性，防止过度复杂化，并最大限度地提高构建和使用图 RAG 系统的效率。

### 将图 RAG 推向生产的挑战
大多数开发人员都明白，构建像图 RAG 这样的系统存在很多不确定性。在数据准备和加载、构建知识图、查询和遍历图、结果编译和提示构建以及工作流程中的几乎任何其他点，都可能发生意想不到的事情。虽然最初实现图 RAG 并不困难，但以下是一些进一步构建和测试图 RAG 应用程序的后续挑战：

**图 RAG 的效果并不比普通 RAG 好多少：** 这是一个非常常见的症状，可能有多种原因。一种可能是向量搜索在没有使用图检索增强生成的情况下找到了正确的文档。**你（仍然）看到幻觉：** 这通常不是由图引起的，即使在禁用 RAG 的图方面时，也无法生成相关的响应。**图太大：** 太多的边或节点会导致缩放问题以及在图遍历期间建立的连接质量问题。**图太小：** 边或节点数量少会导致建立的意义深远的图连接数量少。**你的实现需要增加部署复杂性：** 困难的部署始终是一个挑战，尤其是在涉及新的、专门的软件工具的情况下。**你的实现无法扩展：** 这篇关于[扩展知识图](https://thenewstack.io/scaling-knowledge-graphs-by-eliminating-edges/)的文章讨论了这一挑战并给出了一个可能的解决方案。
这个潜在问题列表并不全面，但它代表了我们一直在关注的一些潜在问题。为了解决这些问题，我们开始构建工具来简化[从实验到生产的迁移，使用 Langflow API](https://www.datastax.com/blog/experimentation-to-production-datastax-langflow-api-public-preview?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean)。希望它可以帮助解决其中的一些问题。

## 简化图 RAG 的成功
Glean 的工程经理[Arjun Landes](https://www.linkedin.com/in/arjunlandes/)在 VentureBeat 中指出，“我们能够构建如此复杂的知识图并将其与 LLM [大型语言模型] 相结合，这才是真正的力量所在。” 我不知道他们系统的细节，但我同意这种力量在于组合，而 Glean 似乎做得很好。
重要的是要注意，Glean 的内部文档数据集是图 RAG 的理想用例。它有效地连接了内部元素，如人员、项目和产品——由于组织数据的范围有限，与维基百科上的海量数据相比，这是可以管理的。这种关注可能通过使 Glean 的挑战更容易解决，而对 Glean 的成功做出了重大贡献。

### 拥有正确的数据是关键
即使在理想的用例中，知识图的质量也是关键；它必须在正确的时间连接正确的元素，而不会用不相关的数据淹没系统。过于密集的图可能会给系统带来负担，迫使它筛选过多的信息，而稀疏但高质量的图可能会通过关注基本连接而超越传统的 RAG 系统。
Glean excels at integrating knowledge bases across platforms, which is more about solid data engineering than AI prowess. The emergence of [generative AI](https://thenewstack.io/when-and-how-will-enterprise-genai-apps-get-real) (GenAI) and [large language models (LLMs)](https://thenewstack.io/the-current-state-of-llms-riding-the-sigmoid-curve) has made it easier to integrate different data types, enabling Glean to consolidate disparate data sources into a cohesive RAG system.

Glean's user interface also stands out, offering a seamless experience that masks the complexity of the integrated technologies. This user-centric design makes its system not only effective but also accessible, enhancing the overall user experience.

## Looking Ahead

The advancement of graph RAG systems marks a move towards more sophisticated applications of AI models in processing and linking complex data. This evolution promises to improve efficiency and has the potential to revolutionize knowledge management across industries.

As we move forward, the principles established today are poised to pave the way for groundbreaking applications in the near future, potentially ushering in a new era of what some call the "intelligent age."

For more information, check out the [DataStax Graph RAG Guide](https://medium.com/building-the-open-data-stack/a-guide-to-graph-rag-a-new-way-to-push-the-boundaries-of-genai-apps-f616d47758a0?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean).

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
Technology is moving fast, don't miss a beat. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.