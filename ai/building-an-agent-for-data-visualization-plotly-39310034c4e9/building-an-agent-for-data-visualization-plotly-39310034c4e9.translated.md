# 构建数据可视化代理（Plotly）

## 用于数据可视化的 ReAct 代理

Plotly 是我最喜欢的数据可视化库。在广泛撰写有关使用 Plotly 创建高级可视化的文章后，我产生了好奇：我能否通过仅提供数据框和自然语言指令来教语言模型构建我喜欢的可视化？本项目就是尝试此想法的成果，我很高兴与你分享结果。

## 让太阳绽放！——在 Plotly 中绘制旭日图的完整指南

### Plotly 中旭日图的初学者到高级指南

pub.towardsai.net

## 没时间了——在 Plotly 中绘制时节省时间

### 在 Plotly（Python）中绘制时节省时间的提示和技巧

python.plainenglish.io

# 为什么构建代理？

如果你曾尝试过 ChatGPT 等 LLM，你就会知道它们可以为几乎任何语言或包生成代码。但是，仅依赖 LLM 存在局限性。以下是通过构建代理我旨在解决的一些关键问题：

**描述你的数据：**LLM 本质上不知道你的数据集的具体信息，例如列名称和行详细信息。手动提供此信息可能很麻烦，尤其是在数据集变大时。如果没有此上下文，LLM 可能会产生幻觉或发明列名称，从而导致数据可视化中的错误。

**样式和偏好：**数据可视化是一种艺术形式，每个人都有独特的审美偏好，这些偏好因图表类型和信息而异。为每个可视化持续向 LLM 提供详细说明很乏味。配备了样式信息的代理可以简化此过程，确保一致且个性化的视觉输出。

**代理推理：**ReAct 代理具有“推理”和执行任务的能力，从而产生更准确的响应和更少的幻觉。这种高级提示工程技术已被证明可以产生更强大、更可靠的结果。你可以在此 [论文](https://arxiv.org/abs/2210.03629) 中阅读有关 ReAct 代理的更多信息。

构建代理可以缓解这些问题，为数据可视化和其他任务提供更高效、更定制的方法。

*正在寻找人来解决你与大型语言模型和数据科学相关的问题吗？请点击此处：* [https://form.jotform.com/240744327173051](https://form.jotform.com/240744327173051)

下面你可以看到当我告诉 Llama3:70B（我为最终代理使用的 LLM）构建可视化时的基准。

# 设计

要构建此应用程序，我们需要为 LLM 代理配备两个工具，以便帮助它生成更好的数据可视化。一个工具提供有关数据集的信息，另一个工具包含有关样式的信息。

Llama-index 允许将任何查询引擎用作代理工具。由于这两个工具都涉及信息检索，因此查询引擎工具适合我们的需求。

# 数据框索引

此工具的目的是分析数据框并将其内容信息存储到索引中。要编制索引的数据包括列名称、数据类型以及值的最小、最大和平均范围。这有助于代理了解他们正在处理的变量类型。

在此示例中，使用了 layoff.fyi 中的数据。但是，该工具可以与任何数据框一起使用。

## 预处理

预处理至关重要，并且因数据集而异。建议将数据转换为适当的类型（例如，将数字字符串转换为整数或浮点数）并删除空值。

# 可选预处理

```python
import pandas as pd
import numpy as np
df = pd.read_csv('WARN Notices California_Omer Arain - Sheet1.csv')
# 将日期类列转换为日期时间
df['Received Date'] = [pd.to_datetime(x) for x in df['Received Date']]
df['Effective Date'] = [pd.to_datetime(x) for x in df['Effective Date']]
# 将存储为字符串的数字转换为整数
df['Number of Workers'] = [int(str(x).replace(',','')) if str(x)!='nan' else np.nan for x in df['Number of Workers']]
# 替换 NULL 值
df = df.replace(np.nan,0)
```

## 将数据集信息存储到索引中

以下是如何实现数据框索引：

```python
from llama_index.core.readers.json import JSONReader
from llama_index.core import VectorStoreIndex
import json
# 存储数值最大、最小和平均值的函数
def return_vals(df,c):
    if isinstance(df[c].iloc[0], (int, float, complex)):
        return [max(df[c]), min(df[c]), np.mean(df[c])]
    # 对于日期时间，我们需要将该信息存储为字符串
    elif(isinstance(df[c].iloc[0],datetime.datetime)):
        return [str(max(df[c])), str(min(df[c])), str(np.mean(df[c]))]
    else:
        # 对于分类变量，你可以存储前 10 个最频繁的项及其频率
        return list(df[c].value_counts()[:10])
# 声明一个字典
dict_ = {}
for c in df.columns:
    # 存储列名称、数据类型和内容
    dict_[c] = {
        'name': c,
        'type': str(df[c].dtype),
        'content': return_vals(df,c)
    }
# 将字典转换为 JSON 字符串
json_str = json.dumps(dict_)
# 创建 JSONReader 对象
reader = JSONReader(json_str)
# 创建 VectorStoreIndex 对象
index = VectorStoreIndex(reader)
```
### MARKDOWN TEXT CORRECTED

dict_[c] = {'column_name':c,'type':str(type(df[c].iloc[0])), 'variable_information':return_vals(df,c)}
# 循环存储信息，作为可加载到 llama-index Document 中的 json 转储
# 将信息写入 dataframe.json
with open("dataframe.json", "w") as fp:
    json.dump(dict_ ,fp)
reader = JSONReader()
# 从 JSON 文件加载数据
documents = reader.load_data(input_file='dataframe.json')
# 创建索引
dataframe_index = VectorStoreIndex.from_documents(documents)
# 样式索引
样式工具作为文档存储，其中包含有关如何使用 plotly 样式不同图表自然语言说明。我鼓励你尝试给出的不同说明。以下是有关如何构建折线图和条形图的说明！
from llama_index.core import Document
from llama_index.core import VectorStoreIndex
styling_instructions =[
    Document(text="""
不要忽略任何这些说明。
对于折线图，始终使用 plotly_white 模板，将 x 轴和 y 轴线减少到 0.2，将 x 和 y 网格宽度减少到 1。
始终提供标题，并使用 html 标签轴标签加粗，如果有多条线，请尝试使用多种颜色
注释线的最小值和最大值
如果大于 1000/100000，则以千（K）或百万（M）显示数字
以 2 位小数点显示百分比，并带有“%”符号
"""
    )
    , Document(text="""
不要忽略任何这些说明。
对于条形图，始终使用 plotly_white 模板，将 x 轴和 y 轴线减少到 0.2，将 x 和 y 网格宽度减少到 1。
始终提供标题，并使用 html 标签轴标签加粗，如果有多条线，请尝试使用多种颜色
始终以千（K）或百万（M）显示数字，如果大于 1000/100000。添加注释 x 值
注释 y 变量上的值
如果变量是百分比，则以 2 位小数点显示，并带有“%”符号。
""")
    # 你应该填写其他图表说明，并尝试使用这些说明
    , Document(text=
""" 一般图表说明
不要忽略任何这些说明
始终使用 plotly_white 模板，将 x 和 y 轴线减少到 0.2，将 x 和 y 网格宽度减少到 1。
始终提供标题，并使用 html 标签轴标签加粗
始终以千（K）或百万（M）显示数字，如果大于 1000/100000。添加注释 x 值
如果变量是百分比，则以 2 位小数点显示，并带有“%”""")
]
# 创建索引
style_index = VectorStoreIndex.from_documents(styling_instructions)
# 构建代理
创建的索引需要基于代理作为工具。Llama-Index 具有可从索引构建查询引擎并将其用作工具的功能。
# 此部分的所有导入
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool
from llama_index.core.tools import ToolMetadata
from llama_index.llms.groq import Groq
# 在索引上构建查询引擎
# 每个查询仅检索一个文档是有意义的
# 但是，如果你需要多个图表，或者有两个或更多具有相似列名称的数据框，则可以尝试使用此方法
dataframe_engine = dataframe_index.as_query_engine(similarity_top_k=1)
styling_engine = style_index.as_query_engine(similarity_top_k=1)
# 构建工具
query_engine_tools = [
    QueryEngineTool(
        query_engine=dataframe_engine,
        # 提供有助于代理决定使用哪个工具的描述
        metadata=ToolMetadata(
            name="dataframe_index",
            description="提供有关数据框中数据的信息。仅在此工具中使用列名称",
        ),
        \
    ),
    QueryEngineTool(
        # 尝试使用描述，看看是否能得到更好的结果
        query_engine=styling_engine,
        metadata=ToolMetadata(
            name="Styling",
            description="提供有关如何设置 Plotly 图表样式的说明"
            "将详细的纯文本问题作为输入提供给工具。",
        ),
    ),
]
# 我通过 Groq 使用了开源模型，但你也可以使用 OpenAI/Google/Mistral 模型
llm = Groq(model="llama3-70b-8192", api_key="<your_api_key>")
# 从工具初始化 ReAct 代理
agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)
## 调整代理提示
Llama-Index 和其他编排包具有可能不适合你的特定用例的默认提示。在实验中，我发现略微调整提示有助于防止出现幻觉。
from llama_index.core import PromptTemplate
new_prompt_txt= """你的目的是帮助在 Plotly 中构建数据可视化。你可以使用 Python 进行各种分析和操作
## 工具
你可以使用各种工具。你负责以你认为合适的任何顺序使用这些工具来完成手头的任务。
这可能需要将任务分解为子任务，并使用不同的工具来完成每个子任务。
你可以使用以下工具，使用这些工具来查找有关数据和样式的信息：
{tool_desc}
## 输出格式
请使用与问题相同的语言回答，并使用以下格式：
```
### 思考：用户的当前语言是：(用户的语言)。我需要使用一个工具来帮助我回答问题。
### 操作：如果使用工具，则工具名称（{tool_names} 之一）。
### 操作输入：以 JSON 格式表示关键字参数（例如 {{"input": "hello world", "num_beams": 5}}) 的工具输入。

```
请始终以思考开头。
请为操作输入使用有效的 JSON 格式。不要执行此操作 {{'input': 'hello world', 'num_beams': 5}}。
如果使用此格式，用户将以以下格式响应：
```

### 观察：工具响应

```
您应该重复上述格式，直到您有足够的信息来回答问题而无需使用任何更多工具。在这一点上，您必须以以下两种格式之一进行响应：
```

### 思考：我可以不使用任何更多工具来回答。我将使用用户的语言来回答
### 答案：[您的答案（与用户问题相同的语言）]

```
### 思考：我无法使用提供的工具回答问题。
### 答案：[您的答案（与用户问题相同的语言）]
```

## 当前对话
以下是包含交替的人类和助手消息的当前对话。"""
# 将提示文本添加到 PromptTemplate 对象
new_prompt = PromptTemplate(new_prompt_txt)
# 更新提示
agent.update_prompts({'agent_worker:system_prompt':new_prompt})
# 可视化
现在进入有趣的部分，在第一部分中，我展示了 Llama 3 如何响应我构建可视化的请求。现在让我们向代理提出类似的请求。
response = agent.chat("为 Number of Workers 提供折线图的 Plotly 代码，从数据框中获取有关正确列名的信息，并确保正确设置绘图样式，还要提供标题")
*正在寻找可以解决您与大型语言模型和数据科学相关的问题的人吗？点击此处：* [https://form.jotform.com/240744327173051](https://form.jotform.com/240744327173051)
通过设置样式说明和代理提示，可以得到更好的响应。该项目还有很长的路要走！但是，它可以帮助您节省时间并提供更好的可视化代码。
# 后续步骤
该项目的下一阶段涉及优化提示和处理常见的故障用例。最终目标是制作一套代理工具，可以帮助我（作为数据科学家）在工作时节省时间。如果您喜欢这个概念，请在 Medium 上关注我。
感谢您的阅读！