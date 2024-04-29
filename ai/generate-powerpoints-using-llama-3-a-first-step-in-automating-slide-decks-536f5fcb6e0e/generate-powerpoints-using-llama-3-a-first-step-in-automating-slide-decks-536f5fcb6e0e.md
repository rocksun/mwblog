
<!--
title: 使用Llama-3生成PowerPoint
cover: https://miro.medium.com/v2/resize:fit:1200/1*VszX1H4fpqIMMXIs26_xrA.jpeg
-->

使用 LLM 和 Python-pptx 自动化演示文稿。

> 译自 [Generate PowerPoints using Llama-3 — A first step in automating slide decks](https://medium.com/firebird-technologies/generate-powerpoints-using-llama-3-a-first-step-in-automating-slide-decks-536f5fcb6e0e)，作者 Arslan Shahid。

在企业界，幻灯片无处不在，它通常被用作传达想法和成就的一种方式。过去 4 年，我一直在为大型跨国公司工作，制作幻灯片是大多数人每周都会做的事情。

如果幻灯片是有效利用时间的一种方式，那这不会是一个大问题。很多人会反对这一点，但在我看来，在大多数公司中，幻灯片会占用太多时间。员工本可以利用这段时间实际执行项目并构建内容。

## RAG 流水线

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*VhkB9IUNjP2XljnFnainZQ.png)

*这是幻灯片的基本 RAG 的简单流程图*

Python 有一个名为 Python-pptx 的库，它允许用户以编程方式创建 PowerPoint 演示文稿。提示大型语言模型使用此库并生成可执行代码，将是第一步。

在此流水线中，我们将采用语料库信息，在本例中是 CFA 考试的书。此练习的最终目标是加载页面、提取文本并使用 LLM 生成创建页面幻灯片的代码。

```python
from llama_index.core import SimpleDirectoryReader
#you can use any PDF/text document for this excercise
reader = SimpleDirectoryReader(input_files =['CFA_Fundamentals_2nd_Edition.pdf'])

docs = reader.load_data()
```

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*2dSy5BovpXFqXqqgA_GZcw.png)

*显示文件*

为了更好地检索，建议您对文档执行一些预处理。块大小、删除不必要的信息和空格将能够更好地检索。

Llama-Index 有多种 LLM 集成可供选择，对于此项目，我决定通过 Groq 使用开源模型 llama-3 70。您可以从 Groq 网站获取免费的 API。

```python
from llama_index.llms.groq import Groq

# Initiating the LLM instance, Groq takes in two parameters, model and api_key
llm = Groq(model="llama3-70b-8192", api_key="<insert_your_api-key")
```

下一步是将文档馈送到向量存储中，这将创建一个检索器(retriever)。

```python
from llama_index.core import VectorStoreIndex

# Creates an Index for the documents
index = VectorStoreIndex.from_documents(docs)
```

对于第一个输出，我们希望 LLM 使用我们的查询并以标题和三个要点作为结构化输出。Pydantic 库允许您创建馈送到查询引擎的输出层。

```python
from typing import List, Field
from pydantic import BaseModel, Field


# Creating a Pydantic object for structured output
class Extract(BaseModel):
    title: str = Field(description="Title for the information retrieved")
    bullet_points: List[str] = Field(description="Three bullet-points for the information")
```

## 第一个 LLM 调用

构建提示

```python
from llama_index.core import PromptTemplate

# The prompt
template = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please generate a header, and 3 bullet points for the {query_str}\n"
    "Also fetch sub_titles and numbers to describe the information"

)
qa_template = PromptTemplate(template)
```

```python
# Building the Query Engine, passing in the Prompt and Pydantic model
query_engine = index.as_query_engine(similarity_top_k=3,llm=llm,text_qa_template=prompt,response_mode='tree_summarize', output_cls=Extract)
# Query and response
response=query_engine.query("BlackSholes Option Pricing Formula")
```

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*D3CnfYx2h0D5dYC5lRTUgA.png)

*Black-Scholes Option Pricing*

## 第二个 LLM 调用

现在将 LLM 的输出传递到另一个 LLM 调用中，该调用将输出 python-pptx 代码。

```python
# response.header
from llama_index.core import PromptTemplate
from llama_index.core.program import LLMTextCompletionProgram

#Another Pydantic model to extract output
class Python_code(BaseModel):
    comments: str = Field(description='Comments about the code')
    code:List[str] = Field(description='Python-pptx code')


template = (
    "We have provided  information below. \n"
    "---------------------\n"
    "{title}"
    "{bullet_points}"
    "\n---------------------\n"
    "Given this information, please generate python-pptx code for a single slide with this title & bullet points\n"
    "Separate the bullet points into separate texts"
    "Do not set font size"

)
#This Program would allow to feed the prompt with headers and bullet-points
program = LLMTextCompletionProgram.from_defaults(
    output_cls=Python_code,
    prompt_template_str=template,
    verbose=True,
    llm=llm
)
#Feeding the response of the previous LLM call
output =program(title=response.title, bullet_points=response.bullet_points)

exec(output.code)
```

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*B41CzqVBQIsolSTfVb1e4Q.png)

*生成的 python-pptx 代码。*

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*nDSwHf89PbZoe7PQ5leZoA.png)

*执行上述代码制作并保存了该演示文稿。*

下一步是使用少样本示例和图表/形状等附加功能来改进 RAG 应用程序的输出。如果您喜欢该项目，请关注以获取更新。