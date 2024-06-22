# 更好地将 LLM 与以内容为中心的知识图谱集成

![以内容为中心的知识图谱的特色图片](https://cdn.thenewstack.io/media/2024/06/8f360af6-knowledge-1024x575.png)

使用 [大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 提取知识图谱既耗时又容易出错。这些困难源于 LLM 被要求从内容中提取细粒度的、特定于实体的信息。受 [向量搜索优势](https://thenewstack.io/vector-search-is-coming-to-apache-cassandra/) 的启发，特别是从相对较少清理的内容中获取良好结果的能力，让我们探索一个粗粒度的 [知识图谱](https://thenewstack.io/how-knowledge-graphs-make-data-more-useful-to-organizations/)——内容知识图谱——专注于内容之间的关系。

如果您想直接开始，也可以 [查看此笔记本](https://colab.research.google.com/github/datastax/ragstack-ai/blob/main/libs/knowledge-store/notebooks/astra_support.ipynb)。

## 以实体为中心的知识图谱

从历史上看，知识图谱的节点代表特定的概念（或实体），并使用边来表示这些概念之间的特定关系。例如，使用关于我和我的雇主的信息构建的知识图谱可能如下所示：

这种细粒度的、以实体为中心的知识图谱允许使用图查询语言（如 Cypher 或 Gremlin）表达各种查询。最近，知识图谱已成为一种流行的替代方法，用于存储和检索信息，供 LLM 在高级 [检索增强生成](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_source=thenewstack&utm_medium=byline&utm_campaign=Knowledge-graph&utm_term=all-plays&utm_content=scaling-knowledge-graphs) (RAG) 技术中使用。这些想法很有说服力：知识图谱捕获了向量相似性搜索会遗漏的信息之间的关系，而 LLM 使得能够仅通过提示从非结构化内容中提取知识图谱三元组（源、关系、目标）。这就是为什么这个历史概念与如此多人相关的原因。

但是，从非结构化信息中提取这种细粒度的知识图谱很困难、耗时且容易出错。为了获得最佳结果，您（以及领域专家）需要：

- 使用 LLM 处理所有非结构化内容以提取信息，
- 通过创建“知识模式”（或本体）来指导 LLM 您希望提取的节点和关系类型，
- 检查提取信息的图以确保 LLM 正在提取正确的信息，以及
- 在更改知识模式时重新处理所有内容。

在需要人类专家和将 LLM 应用于所有内容的挑战之间，构建和维护此图的成本很高。底线：大多数使用知识图谱进行 RAG 的示例仅对几个句子或段落进行操作是有原因的。

使用以实体为中心的知识图谱比仅仅将内容分块并将其转储到向量存储中更难扩展和获得良好的结果。有没有办法将向量搜索的优势引入知识图谱——具体来说，使构建像分块和嵌入内容一样容易，同时保留原始内容，直到 LLM 知道要回答的问题？

## 以内容为中心的知识图谱

如果我们从代表内容（例如文本块）而不是细粒度概念或实体的节点开始，则图的节点正是使用向量搜索时存储的内容。节点可以代表特定的文本段落、图像或表格、文档的一部分或其他信息。这些节点代表原始内容，允许 LLM 做它最擅长的事情：处理上下文并挑选出重要信息。在构建细粒度图时，这发生在知道问题之前，因此在确定哪些事实重要时需要推测和/或人类指导。

事实上，这就是我们认为这些以内容为中心的知识图谱更好的部分原因：LLM 擅长处理大量上下文，并且在知道问题时这样做使它们能够在干草堆中找到最有用的针。以实体为中心的知识图谱需要将信息简化为边上的简单注释，这使得它们作为 LLM 的上下文不太有用。

节点之间的边代表各种结构、语义和基于元数据的属性。例如，包含超链接的块可能有一个指向链接内容的 `links_to` 边，或者两个具有共同关键字的块可能有一个边表示类似的内容 `has_keywords: [...]`
. 一段文字可以链接到同一部分中它引用的图像或表格，或者文档中的段落可以链接到关键术语的定义。

从关于 Ben 和 DataStax 的三篇文档开始，一个类似于之前示例的粗粒度图可能是：

由于节点是文档的块，如果 DataStax 上的文章有更多信息，例如成立时间，图就不会改变。使用细粒度方法，我们需要决定是否应该提取这些额外信息。

与细粒度知识图相比，这种方法的主要优势在于：

**无损**: 原始内容保存在节点中，这意味着在创建过程中不会丢弃任何信息（即未提取）。这减少了根据需求变化重新索引信息的需要，并允许 LLM 做它最擅长的事情：根据问题从该上下文中提取答案。**免维护**: 不需要专家来调整知识提取。您可以在现有的向量搜索管道中添加一些基于关键字、超链接或数据其他属性的边提取，然后自动添加链接。**可扩展**: 创建过程可以使用对内容的简单操作来实现，无需调用 LLM 来创建知识图。
### 创建
与细粒度图不同，创建这些粗粒度图的过程要简单得多。不需要领域专家。相反，内容被加载、分块并写入存储。每个块都可以通过各种分析来识别链接。例如，内容中的链接可能会变成 `links_to`
边，并且可以从块中提取关键字以链接到同一主题的其他块。

我们使用多种技术来添加边。每个块都可以用它表示的 URL 以及它引用的 HREF 进行注释。这允许捕获内容之间的显式链接，以及表示诸如文档通过使用片段链接到同一页面内的定义之类的案例。此外，每个块可以与关键字相关联，并且具有给定关键字的所有块将链接在一起。

正在开发更多用于链接的技术，包括基于块属性的自动链接以及使用结构属性（例如页面上的位置）。

### 检索
对这些粗粒度图的检索结合了向量搜索和知识图遍历的优点。可以根据与问题的相似性来识别起点，然后可以通过遵循边来选择其他块，并对遍历的深度（与向量搜索节点的距离）进行限制。

包含通过嵌入距离（相似性）和图距离（相关）相关的节点会导致更广泛的块集。图中的许多边将导致信息加深上下文，而与问题本身无关。这些关系允许扩展上下文或将上下文限制为“附近”的内容。这些额外的相关信息提高了答案的质量并减少了幻觉。

## 案例研究：Astra 支持文章
我们从 [DataStax Astra DB](https://www.datastax.com/products/datastax-astra?utm_source=thenewstack&utm_medium=byline&utm_campaign=knowledge-graph&utm_term=all-plays&utm_content=scaling-knowledge-graphs) 支持网站加载了 1,272 篇文档，以及从这些文档链接的一些外部页面。刮取、解析 HTML、提取超链接、将内容转换为 markdown 并将结果文档写入 Astra DB 存储不到五分钟。

这几乎不需要我做任何工作，除了基本的数据清理和几行代码来填充描述链接的元数据。具体来说，我没有查看数据或尝试创建捕获我想要提取的信息的知识模式（本体）。这一点很重要，因为我不确定 1,272 篇文档中的哪些部分对可能提出的问题有用。

我本可以使用更多 [LangChain](https://www.langchain.com/) 的内置文档加载功能来减少代码，但它遇到了问题，因为它希望在写出所有页面之前将它们全部加载到内存中，所以我不得不自己管理迭代。

对于以内容为中心的图，我们将使用 `KnowledgeStore`
类，该类作为 [ragstack-ai-knowledge-store](https://pypi.org/project/ragstack-ai-knowledge-store/) 的一部分提供。此类提供了基于 [LangChain 接口](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 的以内容为中心的知识图的实现。事实上，它实现了 LangChain 的 `VectorStore`
接口，因此无需更改即可将文档添加到图中。
虽然您可以自己设置链接的元数据，但也有方便的工具可以自动执行此操作。出于我们的目的，我们希望对每个 HTML 文档执行以下操作：

- 使用基于源 URL 的 CSS 选择器来定位内容（例如，从块和链接中排除导航等）。
- 从 HTML 内容中提取链接。
- 将 HTML 内容转换为 markdown。

虽然 LangChain 文档转换器执行此过程的一部分，但它们不容易组合，因此我们只编写了一些代码来清理 HTML：

同样，由于知识图实现了向量存储接口，因此很容易创建检索器并在 LangChain 表达式中使用它：

### 问题
我在所有示例中使用的问题是一个关于 Astra DB 如何实现向量索引的相对简单的问题。

*“Astra 使用什么向量索引算法？”*

这个问题的答案需要阅读文档的多个部分，并将这些信息与外部链接网站上的信息联系起来。

### 仅向量
答案相对肤浅——只是描述了用于实现向量搜索的库（[JVector](https://github.com/jbellis/jvector)）。这个答案是正确的，但它没有包含任何关于 Astra DB 使用的算法或它实际工作方式的细节。

如果我们查看用于回答问题的页面——那些与问题具有最高相似度的页面——我们会发现它没有到达任何更深入的文档：

- https://docs.datastax.com/en/astra-db-serverless/get-started/concepts.html
- https://docs.datastax.com/en/cql/astra/getting-started/vector-search-quickstart.html
- https://docs.datastax.com/en/astra-db-serverless/databases/embedding-generation.html
- https://docs.datastax.com/en/astra-db-serverless/get-started/astra-db-introduction.html

### 深度 1 遍历
将检索器更改为执行遍历很容易，并且可以提供更好的结果。

答案更好；它解释了 JVector 如何为可扩展的向量搜索实现基于图的索引，以及文档如何立即可用。

请注意，生成结果需要更长的时间——17.5 秒（而仅向量搜索需要 6.1 秒）。从我们使用向量搜索检索的前四个文档的边缘进行跟踪导致检索了 31 个文档。额外的标记让 LLM 花费了更长的时间来理解，尽管它们在想出答案方面仍然做得很好。同时，它并不觉得结果深入地回答了问题。也许是因为 LLM 有太多东西要考虑，它没有得到它所能得到的最佳答案。

如果有一种方法可以检索更少的文档，同时最大限度地提高多样性呢？是否有一种方法可以在边缘提供更多相关信息时跟踪它们，尤其是在这些信息增加了检索内容的多样性时？我们可以修改最大边缘相关性 (MMR) 检索来做到这一点。

### MMR 遍历
MMR 遍历搜索执行向量和图遍历的组合以检索特定数量的文档。与传统的 MMR 不同，在选择节点后，其相邻节点也会成为检索候选者。这允许 MMR 遍历探索图，使用多样性参数来决定更喜欢相似节点的程度，以及更喜欢通过向量搜索或图遍历检索的不同节点的程度。

与切换到遍历一样，使用此技术是对 `retriever` 的简单更改：

这个答案似乎更好。它不仅谈到了 JVector 的实现方式，还提供了有关它用于有效处理搜索和更新的一些技术的详细信息。

如果我们看一下检索到的内容，我们会发现它只检索了四个文档（在总共考虑了 15 个文档之后）。它检索了类似结果（例如“入门”和索引概念）以及回答问题所需的更深入的结果（[JVector](https://github.com/jbellis/jvector/) 的文档）。

- https://docs.datastax.com/en/astra-db-serverless/get-started/concepts.html
- https://docs.datastax.com/en/astra-db-serverless/cli-reference/astra-cli.html
- https://github.com/jbellis/jvector
- https://docs.datastax.com/en/cql/astra/developing/indexing/indexing-concepts.html

## 结论
以内容为中心的知识图作为 [RAGStack](https://www.datastax.com/products/ragstack?utm_source=thenewstack&utm_medium=byline&utm_campaign=knowledge-graph&utm_term=all-plays&utm_content=scaling-knowledge-graphs) 的一部分提供预览。您还可以查看案例研究中的 [笔记本](https://colab.research.google.com/github/datastax/ragstack-ai/blob/main/libs/knowledge-store/notebooks/astra_support.ipynb)。我们正在努力将它们贡献给 LangChain，以及对如何创建和遍历边缘的各种令人兴奋的改进。敬请关注该领域的激动人心的后续行动。
[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看所有播客、访谈、演示等。