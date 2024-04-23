# 如何使用 LangChain 和 OpenAI 总结大型文档

![用于：如何使用 LangChain 和 OpenAI 总结大型文档的特色图片](https://cdn.thenewstack.io/media/2024/04/194e19a1-alley-1024x576.jpg)

大型语言模型让许多任务变得更加容易，例如制作聊天机器人、语言翻译、文本总结等。我们曾经编写模型来进行总结，然后总是存在性能问题。现在，我们可以使用 [大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 轻松地完成此操作。例如，最先进 (SOTA) 的 LLM 已经可以在其上下文窗口中处理整本书。但在总结非常大的文档时仍然存在一些限制。

**LLM 对大型文档总结的限制**

LLM 中的上下文限制或上下文长度是指模型可以处理的标记数量。每个模型都有自己的上下文长度，也称为最大标记或标记限制。例如，标准 GPT-4 模型的上下文长度为 128,000 个标记。它会丢失超过该数量的标记的信息。一些 SOTA LLM 的上下文限制高达 100 万个标记。然而，随着上下文限制的增加，LLM 会受到近期性和首要性等限制。我们还可以深入研究减轻这些影响的方法。

- LLM 中的首要性效应是指模型更重视序列开头呈现的信息。
- 近期性效应是指模型强调它处理的最新信息。

这两种效应都会使模型偏向输入数据的特定部分。模型可能会跳过序列中间的重要信息。

第二个问题是**成本**。我们可以通过拆分文本来解决上下文限制的第一个问题，但我们不能直接将整本书传递给模型。这将花费很多。例如，如果我们有一本书的 100 万个标记，并且我们直接将其传递给 GPT4 模型，那么我们的总成本将约为 90 美元（提示和完成标记）。我们必须找到一种折衷的方法来总结我们的文本，同时考虑价格、上下文限制和书籍的完整上下文。

在本教程中，你将学习如何考虑模型的价格和上下文限制来总结一整本书。让我们开始吧。

**使用 LangChain 和 OpenAI 总结大型文档**

**设置环境**

要按照本教程进行操作，你需要具备以下条件：

- 已安装 Python
- 一个 IDE（VS Code 可行）

要安装依赖项，请打开你的终端并输入以下命令：

```
pip install -r requirements.txt
```

此命令将安装所有必需的依赖项。

**加载书籍**

你将使用查尔斯·狄更斯的《大卫·科波菲尔》，该书已公开用于此项目。让我们使用 LangChain 提供的 PyPDFLoader 实用程序加载这本书。

```python
import langchain
book = langchain.PyPDFLoader.load("david-copperfield.pdf")
```

它将加载整本书，但我们只对内容部分感兴趣。我们可以跳过序言和简介等页面。

```python
content = book.get_content()
```

现在，我们有了内容。让我们打印前 200 个字符。

```python
print(content[:200])
```

**预处理**

让我们从文本中删除不必要的的内容，例如不可打印的字符、多余的空格等。

```python
import re
content = re.sub(r"[^\x00-\x7F]+", "", content)
content = re.sub(r"\s+", " ", content)
```

[清理数据](https://thenewstack.io/clean-data-is-the-foundation-of-effective-machine-learning/) 后，我们就可以深入研究总结问题了。

**加载 OpenAI API**

在使用 OpenAI API 之前，我们需要在此处对其进行配置并提供凭据。

```python
import openai
openai.api_key = "YOUR_API_KEY"
```

在此处输入你的 API 密钥，它将设置环境变量。

让我们看看这本书中有多少个标记：

```python
num_tokens = len(content.split())
print(num_tokens)
```

这本书中有超过 466,000 个标记，如果我们将它们全部直接传递给 LLM，它将向我们收取很多费用。因此，为了降低成本，我们将实施 K 均值聚类以从书中提取重要的块。

**注意：**使用 K 均值聚类的决定受到数据专家 [Greg Kamradt 的教程](https://www.youtube.com/watch?v=qaPMdcCqtWk&t=870s&ab_channel=GregKamradt%28DataIndy%29) 的启发。

为了获得这本书的重要部分，让我们首先将这本书分成不同的块。

**将内容拆分为文档**

我们将使用 LangChain 的 SemanticChunker 实用程序将书籍内容拆分为文档。

```python
from langchain.summarization import SemanticChunker
chunker = SemanticChunker(
    embedding_model="paraphrase-MiniLM-L6-v2",
    breakpoint_threshold_type="cosine",
)
documents = chunker.split(content)
```

SemanticChunker 接收两个参数，第一个是嵌入模型。此模型生成的嵌入用于根据语义拆分文本。第二个是 breakpoint_threshold_type，它根据语义相似性确定应将文本拆分为不同块的点。

注意：通过处理这些较小的、语义相似的块，我们旨在最大程度地减少 LLM 中的近期性和首要性效应。此策略使我们的模型能够更有效地处理每个小上下文，确保更平衡的解释和响应生成。

**查找每个文档的嵌入**

现在，让我们获取每个生成文档的嵌入。你将使用 OpenAI 默认方法获取嵌入。

```python
embeddings = []
for document in documents:
    embedding = openai.Embedding.create(input=document)
    embeddings.append(embedding)
```

get_embeddings 方法为我们提供了所有文档的嵌入。

**注意：**
**文本嵌入**

OpenAI 特别发布了 text-embedding-3-small 方法，它被认为更便宜、更快。

**数据重排**

接下来，我们将文档内容列表及其嵌入转换为 pandas DataFrame，以便于 [数据处理和分析](https://thenewstack.io/apache-flink-for-real-time-data-analysis/)。

**使用 Faiss 进行高效聚类**

现在，我们将文档向量转换为与 [Faiss](https://github.com/facebookresearch/faiss) 兼容的格式，使用 K 均值将它们聚类到 50 个组中，然后创建 Faiss 索引以在文档之间进行高效相似性搜索。

此 K 均值聚类会将文档分组到 50 个组中。

**注意：**选择 K 均值聚类的原因是每个聚类都会有类似的内容或类似的上下文，因为该聚类中的所有文档都有相关的嵌入，并且我们会选择最接近核心的文档。

**选择导入文档**

现在，我们将仅从每个聚类中选择最重要的文档。为此，我们将仅选择到质心的第一个最近向量。

此代码使用索引上的搜索方法来查找质心列表中每个质心最接近的文档。它返回两个数组：

* D，其中包含最近文档到其各自质心的距离，以及
* I，其中包含这些最近文档的索引。搜索方法中的第二个参数 1 指定仅为每个质心找到单个最接近的文档。

现在我们需要对选定的文档索引进行排序，因为文档按书籍顺序排列。

**获取每个文档的摘要**

下一步是使用 GPT-4 模型获取每个文档的摘要以节省资金。要使用 GPT-4，我们来定义模型。

定义提示并使用 LangChain 制作提示模板以将其传递给模型。

此提示模板将帮助模型更有效、更高效地总结文档。

下一步是使用 LangChain 表达语言 (LCEL) 定义 LangChain 链。

摘要链使用 [StrOutputParser](https://api.python.langchain.com/en/latest/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html) 来解析输出。还有其他 [输出解析器](https://python.langchain.com/docs/modules/model_io/output_parsers/) 可供探索。

您最终可以在每个文档上应用已定义的链以获取摘要。

上面的代码逐个对每个文档应用链，并将每个摘要连接到 final_summary。

**将摘要另存为 PDF**

下一步是设置摘要格式并将其另存为 PDF 格式。

因此，这里有以 PDF 格式显示的书籍的完整摘要。

**结论**

在本教程中，我们探讨了使用 LLM 总结大型文本（例如整本书）的复杂性，同时解决了与上下文限制和成本相关的挑战。我们学习了预处理文本的步骤，并实施了一种结合语义块和 K 均值聚类的策略，以有效管理模型的上下文限制。

通过使用高效聚类，我们有效地提取了关键段落，减少了直接处理海量文本的开销。此方法不仅通过最大程度减少处理的标记数量来显著降低成本，而且还减轻了 LLM 中固有的新近效应和首因效应，确保对所有文本段落进行平衡考虑。

通过 LLM 的 API 开发 AI 应用程序一直备受关注，其中向量数据库通过提供上下文嵌入的有效存储和检索发挥着重要作用。

[MyScaleDB](https://myscale.com/) 是专门为 AI 应用程序设计的向量数据库，它考虑了成本、准确性和速度等所有因素。其 SQL 友好界面允许开发人员在无需学习新知识的情况下开始开发其 AI 应用程序。

如果您想与我们进一步讨论，欢迎加入 [MyScale Discord](https://discord.gg/D2qpkqc4Jq) 分享您的想法和反馈。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。