
<!--
title: 如何使用LangChain和OpenAI总结大型文档
cover: https://cdn.thenewstack.io/media/2024/04/194e19a1-alley.jpg
-->

在总结非常大的文档时仍然存在一些限制。以下是一些减轻这些影响的方法。

> 译自 [How to Summarize Large Documents with LangChain and OpenAI](https://thenewstack.io/how-to-summarize-large-documents-with-langchain-and-openai/)，作者 Usama Jamil。

大型语言模型让许多任务变得更加容易，例如制作聊天机器人、语言翻译、文本总结等。我们曾经编写模型来进行总结，然后总是存在性能问题。现在，我们可以使用[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 轻松地完成此操作。例如，最先进 (SOTA) 的 LLM 已经可以在其上下文窗口中处理整本书。但在总结非常大的文档时仍然存在一些限制。

## LLM 对大型文档总结的限制

LLM 中的上下文限制或上下文长度是指模型可以处理的标记数量。每个模型都有自己的上下文长度，也称为最大标记或标记限制。例如，标准 GPT-4 模型的上下文长度为 128,000 个标记。它会丢失超过该数量的标记的信息。一些 SOTA LLM 的上下文限制高达 100 万个标记。然而，随着上下文限制的增加，LLM 会受到近期性和首要性等限制。我们还可以深入研究减轻这些影响的方法。

- LLM 中的首要性效应是指模型更重视序列开头呈现的信息。
- 近期性效应是指模型强调它处理的最新信息。

这两种效应都会使模型偏向输入数据的特定部分。模型可能会跳过序列中间的重要信息。

第二个问题是成本。我们可以通过拆分文本来解决上下文限制的第一个问题，但我们不能直接将整本书传递给模型。这将花费很多。例如，如果我们有一本书的 100 万个标记，并且我们直接将其传递给 GPT4 模型，那么我们的总成本将约为 90 美元（提示和完成标记）。我们必须找到一种折衷的方法来总结我们的文本，同时考虑价格、上下文限制和书籍的完整上下文。

在本教程中，你将学习如何考虑模型的价格和上下文限制来总结一整本书。让我们开始吧。

## 使用 LangChain 和 OpenAI 总结大型文档

### 设置环境

要按照本教程进行操作，你需要具备以下条件：

- 已安装 Python
- 一个 IDE（VS Code 可行）

要安装依赖项，请打开你的终端并输入以下命令：

```
pip install langchain openai tiktoken fpdf2 pandas
```

此命令将安装所有必需的依赖项。

### 加载书籍

你将使用查尔斯·狄更斯的《大卫·科波菲尔》，该书已公开用于此项目。让我们使用 LangChain 提供的 PyPDFLoader 加载这本书。

```python
from langchain.document_loaders import PyPDFLoader

# Load the book
loader = PyPDFLoader("David-Copperfield.pdf")
pages = loader.load_and_split()
```

它将加载整本书，但我们只对内容部分感兴趣。我们可以跳过序言和简介等页面。

```python
# Cut out the open and closing parts
pages = pages[6:1308]
# Combine the pages, and replace the tabs with spaces
text = ' '.join([page.page_content.replace('\t', ' ') for page in pages]
```

现在，我们有了内容。让我们打印前 200 个字符。

```python
text[0:200]s
```

### 预处理

让我们从文本中删除不必要的的内容，例如不可打印的字符、多余的空格等。

```python
import re
def clean_text(text):
   # Remove the specific phrase 'Free eBooks at Planet eBook.com' and surrounding whitespace
   cleaned_text = re.sub(r'\s*Free eBooks at Planet eBook\.com\s*', '', text, flags=re.DOTALL)
   # Remove extra spaces
   cleaned_text = re.sub(r' +', ' ', cleaned_text)
   # Remove non-printable characters, optionally preceded by 'David Copperfield'
   cleaned_text = re.sub(r'(David Copperfield )?[\x00-\x1F]', '', cleaned_text)
   # Replace newline characters with spaces
   cleaned_text = cleaned_text.replace('\n', ' ')
   # Remove spaces around hyphens
   cleaned_text = re.sub(r'\s*-\s*', '', cleaned_text)
   return cleaned_text
clean_text=clean_text(text)
```

[清理数据](https://thenewstack.io/clean-data-is-the-foundation-of-effective-machine-learning/)后，我们就可以深入研究总结问题了。

### 加载 OpenAI API

在使用 OpenAI API 之前，我们需要在此处对其进行配置并提供凭据。

```python
import os
os.environ["OPENAI_API_KEY"] = "your-openai-key-here"
```

在此处输入你的 API 密钥，它将设置环境变量。

让我们看看这本书中有多少个标记：

```python
from langchain import OpenAI
llm = OpenAI()
Tokens = llm.get_num_tokens(clean_text)
print (f"We have {Tokens} tokens in the book")
```

这本书中有超过 466,000 个标记，如果我们将它们全部直接传递给 LLM，它将向我们收取很多费用。因此，为了降低成本，我们将实施 K 均值聚类以从书中提取重要的块。

**注意**：使用 K 均值聚类的决定受到数据专家 [Greg Kamradt 的教程](https://www.youtube.com/watch?v=qaPMdcCqtWk&t=870s&ab_channel=GregKamradt%28DataIndy%29) 的启发。

为了获得这本书的重要部分，让我们首先将这本书分成不同的块。

### 将内容拆分为文档

我们将使用 LangChain 的 SemanticChunker 实用程序将书籍内容拆分为文档。

```python
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
text_splitter = SemanticChunker(
   OpenAIEmbeddings(), breakpoint_threshold_type="interquartile"
)
docs = text_splitter.create_documents([clean_text])
```

SemanticChunker 接收两个参数，第一个是嵌入模型。此模型生成的嵌入用于根据语义拆分文本。第二个是 breakpoint_threshold_type，它根据语义相似性确定应将文本拆分为不同块的点。

注意：通过处理这些较小的、语义相似的块，我们旨在最大程度地减少 LLM 中的近期性和首要性效应。此策略使我们的模型能够更有效地处理每个小上下文，确保更平衡的解释和响应生成。

### 查找每个文档的嵌入

现在，让我们获取每个生成文档的嵌入。你将使用 OpenAI 默认方法获取嵌入。

```python
import numpy as np
import openai
def get_embeddings(text):
   response = openai.embeddings.create(
       model="text-embedding-3-small",
       input=text
   )
   return response.data
embeddings=get_embeddings([doc.page_content for doc in docs]
```

`get_embeddings` 方法可以为我们提供所有文档的嵌入。

OpenAI 特别发布了 text-embedding-3-small 方法，它被认为更便宜、更快。

###  数据重排

接下来，我们将文档内容列表及其嵌入转换为 pandas DataFrame，以便于[数据处理和分析](https://thenewstack.io/apache-flink-for-real-time-data-analysis/)。

```py
import pandas as pd
content_list = [doc.page_content for doc in docs]
df = pd.DataFrame(content_list, columns=['page_content'])
vectors = [embedding.embedding for embedding in embeddings]
array = np.array(vectors)
embeddings_series = pd.Series(list(array))
df['embeddings'] = embeddings_series
```

### 使用 Faiss 进行高效聚类

现在，我们将文档向量转换为与 [Faiss](https://github.com/facebookresearch/faiss) 兼容的格式，使用 K 均值将它们聚类到 50 个组中，然后创建 Faiss 索引以在文档之间进行高效相似性搜索。

```py
import numpy as np
import faiss
# Convert to float32 if not already
array = array.astype('float32') 
num_clusters = 50
# Vectors dimensionality
dimension = array.shape[1] 
# Train KMeans with Faiss
kmeans = faiss.Kmeans(dimension, num_clusters, niter=20, verbose=True)
kmeans.train(array)
# Directly access the centroids
centroids = kmeans.centroids 
# Create a new index for the original dataset
index = faiss.IndexFlatL2(dimension)
# Add original dataset to the index
index.add(array) 
```

此 K 均值聚类会将文档分组到 50 个组中。

**注意**：选择 K 均值聚类的原因是每个聚类都会有类似的内容或类似的上下文，因为该聚类中的所有文档都有相关的嵌入，并且我们会选择最接近核心的文档。

### 选择导入文档

现在，我们将仅从每个聚类中选择最重要的文档。为此，我们将仅选择到质心的第一个最近向量。

```py
D, I = index.search(centroids, 1)
```

此代码使用索引上的搜索方法来查找质心列表中每个质心最接近的文档。它返回两个数组：

* D，其中包含最近文档到其各自质心的距离，以及
* I，其中包含这些最近文档的索引。搜索方法中的第二个参数 1 指定仅为每个质心找到单个最接近的文档。

现在我们需要对选定的文档索引进行排序，因为文档按书籍顺序排列。

```py
sorted_array = np.sort(I, axis=0)
sorted_array=sorted_array.flatten()
extracted_docs = [docs[i] for i in sorted_array]
```

### 获取每个文档的摘要

下一步是使用 GPT-4 模型获取每个文档的摘要以节省资金。要使用 GPT-4，我们来定义模型。

```py
model = ChatOpenAI(temperature=0,model="gpt-4")
```

定义提示并使用 LangChain 制作提示模板以将其传递给模型。

```py
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("""
You will be given different passages from a book one by one. Provide a summary of the following text. Your result must be detailed and atleast 2 paragraphs. When summarizing, directly dive into the narrative or descriptions from the text without using introductory phrases like 'In this passage'. Directly address the main events, characters, and themes, encapsulating the essence and significant details from the text in a flowing narrative. The goal is to present a unified view of the content, continuing the story seamlessly as if the passage naturally progresses into the summary.
Passage:
```{text}```
SUMMARY:
"""
)
```

此提示模板将帮助模型更有效、更高效地总结文档。

下一步是使用 LangChain 表达语言 (LCEL) 定义 LangChain 链。

```py
chain= (
    prompt
   | model
   |StrOutputParser() )
```

摘要链使用 [StrOutputParser](https://api.python.langchain.com/en/latest/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html) 来解析输出。还有其他 [输出解析器](https://python.langchain.com/docs/modules/model_io/output_parsers/) 可供探索。

您最终可以在每个文档上应用已定义的链以获取摘要。

```py
from tqdm import tqdm
final_summary = ""

for doc in tqdm(extracted_docs, desc="Processing documents"):
   # Get the new summary.
   new_summary = chain2.invoke({"text": doc.page_content})
   # Update the list of the last two summaries: remove the first one and add the new one at the end.
   final_summary+=new_summary
```

上面的代码逐个对每个文档应用链，并将每个摘要连接到 final_summary。

###  将摘要另存为 PDF

下一步是设置摘要格式并将其另存为 PDF 格式。

```py
from fpdf import FPDF

class PDF(FPDF):
   def header(self):
       # Select Arial bold 15
       self.set_font('Arial', 'B', 15)
       # Move to the right
       self.cell(80)
       # Framed title
       self.cell(30, 10, 'Summary', 1, 0, 'C')
       # Line break
       self.ln(20)

   def footer(self):
       # Go to 1.5 cm from bottom
       self.set_y(-15)
       # Select Arial italic 8
       self.set_font('Arial', 'I', 8)
       # Page number
       self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

# Instantiate PDF object and add a page
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Ensure the 'last_summary' text is treated as UTF-8
# Replace 'last_summary' with your actual text variable if different
# Make sure your text is a utf-8 encoded string
last_summary_utf8 = last_summary.encode('latin-1', 'replace').decode('latin-1')
pdf.multi_cell(0, 10, last_summary_utf8)

# Save the PDF to a file
pdf_output_path = "s_output1.pdf"
pdf.output(pdf_output_path)
```

因此，这里有以 PDF 格式显示的书籍的完整摘要。

## 结论

在本教程中，我们探讨了使用 LLM 总结大型文本（例如整本书）的复杂性，同时解决了与上下文限制和成本相关的挑战。我们学习了预处理文本的步骤，并实施了一种结合语义块和 K 均值聚类的策略，以有效管理模型的上下文限制。

通过使用高效聚类，我们有效地提取了关键段落，减少了直接处理海量文本的开销。此方法不仅通过最大程度减少处理的标记数量来显著降低成本，而且还减轻了 LLM 中固有的新近效应和首因效应，确保对所有文本段落进行平衡考虑。

通过 LLM 的 API 开发 AI 应用程序一直备受关注，其中向量数据库通过提供上下文嵌入的有效存储和检索发挥着重要作用。

[MyScaleDB](https://myscale.com/) 是专门为 AI 应用程序设计的向量数据库，它考虑了成本、准确性和速度等所有因素。其 SQL 友好界面允许开发人员在无需学习新知识的情况下开始开发其 AI 应用程序。
