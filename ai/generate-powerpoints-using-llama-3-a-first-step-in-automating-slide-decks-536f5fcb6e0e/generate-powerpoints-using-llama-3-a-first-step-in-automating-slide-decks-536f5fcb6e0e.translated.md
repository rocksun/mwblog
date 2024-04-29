# 使用 Llama-3 生成 PowerPoint — 自动化幻灯片集的第一步

## 使用 LLM 和 Python-pptx 自动化演示文稿

在企业界，幻灯片无处不在，它通常被用作传达想法和成就的一种方式。过去 4 年，我一直在为大型跨国公司工作，制作幻灯片是大多数人每周都会做的事情。

如果幻灯片是有效利用时间的一种方式，那这不会是一个大问题。很多人会反对这一点，但在我看来，在大多数公司中，幻灯片会占用太多时间。员工本可以利用这段时间实际执行项目并构建内容。

*正在寻找人来解决您与大型语言模型和数据科学相关的问题？请点击此处：* [https://form.jotform.com/240744327173051](https://form.jotform.com/240744327173051)

## RAG 管道

Python 有一个名为 Python-pptx 的库，它允许用户以编程方式创建 PowerPoint 演示文稿。提示大型语言模型使用此库并生成可执行代码，将是第一步。

在此管道中，我们将采用语料库信息，在本例中是 CFA 考试的书。此练习的最终目标是加载页面、提取文本并使用 LLM 生成创建页面幻灯片的代码。

```python
from llama_index.core import SimpleDirectoryReader

# 您可以对该练习使用任何 PDF/文本文档
reader = SimpleDirectoryReader(input_files=['CFA_Fundamentals_2nd_Edition.pdf'])
docs = reader.load_data()
```

为了更好地检索，建议您对文档执行一些预处理。块大小、删除不必要的信息和空格将能够更好地检索。

Llama-Index 有多种 LLM 集成可供选择，对于此项目，我决定通过 Groq 使用开源模型 llama-3 70。您可以从 Groq 网站获取免费的 API。

```python
from llama_index.llms.groq import Groq

# 初始化 LLM 实例，Groq 采用两个参数，模型和 api_key
llm = Groq(model="llama3-70b-8192", api_key="<insert_your_api-key")
```

下一步是将文档馈送到矢量存储中，这将创建一个检索器。

```python
from llama_index.core import VectorStoreIndex

# 为文档创建索引
index = VectorStoreIndex.from_documents(docs)
```

对于第一个输出，我们希望 LLM 使用我们的查询并以标题和三个要点作为结构化输出。Pydantic 库允许您创建馈送到查询引擎的输出层。

```python
from typing import List, Field
from pydantic import BaseModel, Field

# 为结构化输出创建 Pydantic 对象
class Extract(BaseModel):
    title: str = Field(description="检索到的信息的标题")
    bullet_points: List[str] = Field(description="信息的三个要点")
```

## 第一个 LLM 调用

### 构建提示

```python
from llama_index.core import PromptTemplate

# 提示
template = (
    "我们提供了以下背景信息。\n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "根据这些信息，请为 {query_str} 生成一个标题和 3 个要点\n"
    "还要获取子标题和数字来描述信息"
)
qa_template = PromptTemplate(template)
```

### 构建查询引擎，传入提示和 Pydantic 模型

```python
query_engine = index.as_query_engine(similarity_top_k=3,llm=llm,text_qa_template=prompt,response_mode='tree_summarize', output_cls=Extract)
```

### 查询和响应

```python
response=query_engine.query("BlackSholes 期权定价公式")
```

## 第二个 LLM 调用

现在将 LLM 的输出传递到另一个 LLM 调用中，该调用将输出 python-pptx 代码。

```python
# response.header
from llama_index.core import PromptTemplate
from llama_index.core.program import LLMTextCompletionProgram

# 另一个 Pydantic 模型来提取输出
class Python_code(BaseModel):
    comments: str = Field(description='有关代码的注释')
    code:List[str] = Field(description='Python-pptx 代码')

template = (
    "我们提供了以下信息。\n"
    "---------------------\n"
    "{title}"
    "{bullet_points}"
    "\n---------------------\n"
    "根据这些信息，请为具有此标题和要点的单个幻灯片生成 python-pptx 代码\n"
    "将要点分成单独的文本"
    "不要设置字体大小"
)

# 此程序允许使用标题和要点来提供提示
program = LLMTextCompletionProgram.from_defaults(
    output_cls=Python_code,
    prompt_template_str=template,
    verbose=True,
    llm=llm
)
```

### 提供前一个 LLM 调用的响应

```python
output =program(title=response.title, bullet_points=response.bullet_points)
```

### 执行代码

```python
exec(output.code)
```

下一步是使用少样本示例和图表/形状等附加功能来改进 RAG 应用程序的输出。如果您喜欢该项目，请关注以获取更新。