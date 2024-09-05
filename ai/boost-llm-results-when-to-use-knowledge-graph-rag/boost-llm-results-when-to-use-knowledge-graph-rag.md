
<!--
title: 提升LLM结果：何时使用知识图谱RAG
cover: https://cdn.thenewstack.io/media/2024/08/7f543328-rag.png
-->

通过知识图谱增强 RAG 可以帮助检索，使系统能够更深入地挖掘数据集以提供详细的响应。

> 译自 [Boost LLM Results: When to Use Knowledge Graph RAG](https://thenewstack.io/boost-llm-results-when-to-use-knowledge-graph-rag/)，作者 Brian Godsey。

有时，检索增强生成 (RAG) 系统无法深入文档集以找到所需的答案。我们可能会得到泛泛的或肤浅的回复，或者我们可能会得到回复，其中 [RAG](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval) 系统检索到的细节很少，然后用不相关或不正确的信息填补空白——这被称为“[幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)”。

深度知识库和文档集可能包含我们用 RAG 提示回答问题所需的所有信息，但 [RAG 系统](https://thenewstack.io/enhancing-ai-coding-assistants-with-context-using-rag-and-sem-rag/) 可能无法找到所有信息，尤其是在所需信息分散在多个文档和不同主题或子主题中的情况下。特别是，向量检索通常会产生一组很好的文档，但这些文档中的一些概念需要更多信息才能让系统理解它们，因此直接检索与这些概念相关的其他文档将很有帮助。

以下是一些可能存在这些问题的类型的数据集：

- 经常相互引用的文档集合。
- 包含章节、术语定义和词汇表的文档，其中检查交叉引用是了解给定主题的完整情况的唯一方法。
- 大型维基或知识库，其中几乎每段都包含指向其他页面和外部网站的 HTML 链接。

此类数据集通常存在于：

- 法律文件
- 技术文档
- 研究和学术出版物
- 高度互联的网站

如果您的组织拥有深度且复杂的数据集，其中包含相互关联的文档和其他内容，则标准 RAG 实现可能无法成功解决一些最常见的用例，尤其是在提示要求提供详细的解释时，这些解释包括广泛和高度具体的层面的信息。将实现转换为 [图 RAG](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/)，这意味着用 [知识图谱](https://hackernoon.com/how-to-use-knowledge-graphs-for-retrieval-augmented-generationwithout-a-graph-db) 增强 RAG 系统，该图谱可以帮助检索，可以使系统能够更深入地挖掘数据集，以提供对请求详细和专业信息的提示的详细且正确的响应。

让我们探讨知识图谱如何提高 RAG 系统性能的关键概念，这种图谱可能是什么样子以及如何开始在您自己的数据上构建图 RAG 系统。

## 图谱如何提供帮助？

简而言之，知识图谱与 [向量存储](https://www.datastax.com/guides/what-is-a-vector-database?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval) 相结合，可以提供一种方法来直接连接在向量空间中可能不接近或不相似，因此在检索过程中不会被认为是“相关”的文本块。

典型的 RAG 系统从向量存储中检索与提示最相关的文档（或“[块](https://www.datastax.com/blog/chunking-to-get-your-data-ai-ready?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval)”，根据向量相似性的度量。如果这些文档包含指向其他文档的链接或引用，那么很明显，文档的作者认为它们是有意义地相关的。如果文档是有意义地相关的，为什么我们不想利用这些信息来更深入地挖掘并获得更多可能有助于回答提示的细节？

重述一下情况：我们拥有通过链接或引用明确且直接相关的文档，我们希望确保我们的 RAG 系统在检索文档时考虑这些连接。构建一个链接文档的网络会产生一个图结构，我们可以遍历该结构以找到在典型文档检索过程中可能无法找到的相关文档，使用图来增强 RAG；这被称为图 RAG。

主要思想是我们已经拥有一个隐式且高置信度的图，它通过直接链接和引用将文档相互关联，我们希望我们的 RAG 系统在依赖不太确定的向量相似性和相关性分数来填充响应中的细节之前，充分利用这些已知的、高确定性的连接，这将有更高的风险以幻觉进行响应。
## 我们可以使用哪些类型的连接？

定义图的可能性是无限的，但我们发现，在图 RAG 中使用最有效和最有效的连接类型是那些定义明确且有意义的连接。也就是说，我们希望清楚地知道什么是连接，什么是没有连接的，因此我们倾向于避免为模糊的概念（如一般主题和情感）定义连接。我们希望这些连接是有意义的，从某种意义上说，两个文档在 [图中存在连接使得每个文档中的内容](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/) 很可能与另一个文档相关。以下是定义图 RAG 中文档之间连接的一些最有用方法。

### HTML 链接

如今，连接文档最清晰、最明显的方法之一是在一个文档中直接链接到另一个文档，从 HTML 链接在基于 Web 的文档中的意义上来说。从人类的角度（而不是 AI 的角度）来看，如果我们点击一个文档中的链接并最终到达另一个文档，那么它们之间就存在一个链接。这可以通过任何数量的链接提取工具在软件中定义和实现。通常，文档的作者添加链接是有原因的，因此它们之间存在有意义的连接。这样，HTML 链接是我们可以在知识图中使用的文档之间最明确和最有意义的链接之一。

从 HTML 链接构建知识图在技术文档和大型维基或知识库等数据集上非常有效。这些类型的数据集的互连性质使得图 RAG 特别适用于深入研究专业细节、定义和子主题，这些细节、定义和子主题可能无法通过向量搜索单独找到。

从 HTML 文档中提取链接的一些示例代码：

```python
from bs4 import BeautifulSoup
from ragstack_langchain.graph_store.extractors import HtmlLinkEdgeExtractor

html_link_extractor = HtmlLinkEdgeExtractor()

# starting with an HTML document called `html`
soup = BeautifulSoup(html.page_content, "html.parser")
content = select_content(soup, url)

# Extract HTML links from the content.
html_link_extractor.extract_one(html, content)
```

有关使用 HTML 链接提取构建图的图 RAG 的端到端示例，请查看最近的这篇文章，“[使用以内容为中心的知识图实现更好的 LLM 集成和相关性](https://www.datastax.com/blog/better-llm-integration-and-relevancy-with-content-centric-knowledge-graphs?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval)”。

### 关键词和主题

虽然从基于一般主题或情感的连接构建图对于图 RAG 的目的来说可能过于模糊和不确定，但通常可以使用定义明确且有意义的高度专业化的关键词和主题。特别是，专业领域内的关键词可以有效地用于在图 RAG 中建立文档之间的连接。专业关键词并不总是包含在文档的向量嵌入表示中，因此将从知识图提供的更强大、更刻意连接中受益。

有一些优秀的工具可以提取关键词；以下是如何 [使用“keyBERT”提取关键词](https://github.com/MaartenGr/KeyBERT) 的简单示例：

```python
from keybert import KeyBERT

doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal).
         A supervised learning algorithm analyzes the training data and produces an inferred function,
         which can be used for mapping new examples. An optimal scenario will allow for the
         algorithm to correctly determine the class labels for unseen instances. This requires
         the learning algorithm to generalize from the training data to unseen situations in a
         'reasonable' way (see inductive bias).
      """

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc)
```

这将提取专业领域关键词：

```py
>>> kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None)
[('learning algorithm', 0.6978),
 ('machine learning', 0.6305),
 ('supervised learning', 0.5985),
 ('algorithm analyzes', 0.5860),
 ('learning function', 0.5850)]
```

我们将这些关键词如何转化为知识图取决于我们的用例和数据模型。一个例子可以在 [RAGStack 文档关于知识图 RAG 的部分](https://docs.datastax.com/en/ragstack/knowledge-graph/knowledge-graph.html) 中找到。

使用有意义的关键词作为节点构建图，这些节点连接到包含它们的文档，这可能是一种有效的图 RAG 策略。请注意，要通过图将文档相互连接，我们必须遍历图到深度为 2 或更大：从文档到其关键词的一步，以及到包含这些关键词的其他文档的第二步。

### 术语和定义

在法律文件、学术出版物和研究作品中，我们有术语和定义作为列表或词汇表，通常出现在文档的开头或结尾。在这些情况下，在整个文档中引用这些术语和定义非常有用，这样我们就可以始终清楚地了解所表达的内容。如果没有这些术语的定义，文档的某些部分可能会变得模糊或几乎毫无意义。

一个特别恰当的例子是大量文档的情况，这些文档是租户和房东之间的合同；我们将使用我们的 RAG 系统查询它们。这些文档通常会在加载到数据存储之前进行分块，这意味着出现在文档开头或结尾的任何术语和定义本身并不包含在分块中。由于存在许多不同租户和房东之间的合同，任何引用“租户”或“房东”一词的分块在没有将其与所讨论的特定租户和特定房东联系起来的情况下将是模棱两可的。

在这种情况下，拥有一个明确地将文档片段与其中出现的术语的适当定义连接起来的知识图将非常有用。提取这些定义和术语以及将它们连接到文档的正确片段的具体实现将取决于原始文档本身的格式、术语表或定义相对于文档其余部分的结构等。许多文本和文档解析器可用于此目的，并且正在进行工作以将该过程标准化为图 RAG。

当文档被分割并加载到向量存储中时，除非我们以某种方式捕获它，否则文档结构中所有超出片段的部分都会丢失。对于许多 RAG 用例，系统能够知道每个文档片段在文档的整体结构中的位置、所有标题和副标题、页码以及哪些片段紧接在给定片段之前和之后将非常有用。

在与每个片段连接的知识图中保留此信息对于图 RAG 的目的有两个主要优势。首先，了解片段在文档中的位置使我们能够提取附近的文本，这可能是紧接在片段之前和之后的片段、同一页面的文本或同一部分的文本——所有这些都可能为初始片段中提到的主题提供支持证据和细节。其次，一些文档包含对其他部分编号、标题和页码的交叉引用，因此拥有一个允许 RAG 系统直接检索所引用部分中的片段的知识图将非常有用。

## 我们如何构建这个图来改进我们的 Rag 系统？

我们在 [这篇关于以内容为中心的知识图的文章](https://www.datastax.com/blog/better-llm-integration-and-relevancy-with-content-centric-knowledge-graphs?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval) 中详细介绍了更多技术细节，其中我们解释了如何使用 `langchain`、`ragstack`、Cassandra 和相关工具从基于 Web 的技术文档构建知识图。我们从文档中出现的 HTML 链接构建知识图，这可能是为图 RAG 构建知识图的最简单和最有用的方法之一。

要处理 HTML 文档并为图 RAG 添加适当的元数据，我们可以使用以下辅助函数：

```py
from markdownify import MarkdownConverter
from ragstack_langchain.graph_store.extractors import HtmlLinkEdgeExtractor

markdown_converter = MarkdownConverter(heading_style="ATX")
html_link_extractor = HtmlLinkEdgeExtractor()

def convert_html(html: Document) -> Document:
url = html.metadata["source"]
soup = BeautifulSoup(html.page_content, "html.parser")
content = select_content(soup, url)

# Use the URL as the content ID.
html.metadata[CONTENT_ID] = url

# Extract HTML links from the content.
html_link_extractor.extract_one(html, content)

# Convert the content to markdown and add to metadata
html.page_content = markdown_converter.convert_soup(content)

return html
```

一旦文档被处理并且添加了适当的元数据，它们就可以加载到像下面示例这样的图向量存储中，该示例使用 [Astra DB](https://www.datastax.com/products/datastax-astra?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval) 作为底层数据存储，以及 `CassandraGraphStore` 作为 `GraphVectorStore` 的实现，它既充当知识图又充当向量存储：

```py

import cassio
from langchain_openai import OpenAIEmbeddings
from ragstack_langchain.graph_store import CassandraGraphStore

# Initialize AstraDB connection
cassio.init(auto=True)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create knowledge store
graph_store = CassandraGraphStore(embeddings)

...  # load and process your documents, e.g. `convert_html` above

# Add documents to knowledge store
graph_store.add_documents(docs)
```

## 了解更多
要了解有关优化图 RAG 的知识图的构建和使用的更多信息，请阅读这篇最近的文章，“[通过消除边来扩展知识图](https://thenewstack.io/scaling-knowledge-graphs-by-eliminating-edges)”。这包括对 Langchain 中方便的“GraphVectorStore”的介绍。

有关 DataStax 如何帮助您快速且只需最少的代码更改即可开始使用图 RAG 的最新更新，请查看我们在 [RAG 与向量图](https://www.datastax.com/products/vector-graph?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval) 上的工作。
