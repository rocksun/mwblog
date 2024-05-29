
<!--
title: 构建数据可视化代理（Plotly）
cover: https://miro.medium.com/v2/resize:fit:1200/1*iyfli_-93wwS5COUsgbCRg.jpeg
-->

Plotly 是我最喜欢的数据可视化库。在广泛撰写有关使用 Plotly 创建高级可视化的文章后，我产生了好奇：我能否通过仅提供 dataframe 和自然语言指令来教语言模型构建我喜欢的可视化？本项目就是尝试此想法的成果，我很高兴与你分享结果。

> 译自 [Building an Agent for Data Visualization (Plotly)](https://medium.com/firebird-technologies/building-an-agent-for-data-visualization-plotly-39310034c4e9)，作者 Arslan Shahid。

## 为什么构建代理？

如果你曾尝试过 ChatGPT 等 LLM，你就会知道它们可以为几乎任何语言或包生成代码。但是，仅依赖 LLM 存在局限性。以下是通过构建代理我旨在解决的一些关键问题：

1. **描述你的数据**：LLM 本质上不知道你的数据集的具体信息，例如列名称和行详细信息。手动提供此信息可能很麻烦，尤其是在数据集变大时。如果没有此上下文，LLM 可能会产生幻觉或发明列名称，从而导致数据可视化中的错误。
2. **样式和偏好**：数据可视化是一种艺术形式，每个人都有独特的审美偏好，这些偏好因图表类型和信息而异。为每个可视化持续向 LLM 提供详细说明很乏味。配备了样式信息的代理可以简化此过程，确保一致且个性化的视觉输出。
3. **代理推理**：ReAct 代理具有“推理”和执行任务的能力，从而产生更准确的响应和更少的幻觉。这种高级提示工程技术已被证明可以产生更强大、更可靠的结果。你可以在此 [论文](https://arxiv.org/abs/2210.03629) 中阅读有关 ReAct 代理的更多信息。

构建代理可以缓解这些问题，为数据可视化和其他任务提供更高效、更定制的方法。

下面你可以看到当我告诉 Llama3:70B（我为最终代理使用的 LLM）构建可视化时的基线。

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*d4rqBr1tdyJ6Mpp39lihSw.png)

*作者图片——用70B 模型询问 Groq，它为数据创建的假名，下面可以看到可视化*

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*jdqCUmOjxG9YrOzluz61Ug.png)

*作者图片 — 当我修复Llama3制作的一些错误时，可视化看起来是这样。不是一个好的输出*


## 设计

要构建此应用程序，我们需要为 LLM 代理配备两个工具，以便帮助它生成更好的数据可视化。一个工具提供有关数据集的信息，另一个工具包含有关样式的信息。

Llama-index 允许将任何查询引擎用作代理工具。由于这两个工具都涉及信息检索，因此查询引擎工具适合我们的需求。

##  dataframe 索引

此工具的目的是分析 dataframe 并将其内容信息存储到索引中。要编制索引的数据包括列名称、数据类型以及值的最小、最大和平均范围。这有助于代理了解他们正在处理的变量类型。

在此示例中，使用了 layoff.fyi 中的数据。但是，该工具可以与任何 dataframe 一起使用。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*HdGrN99qvVhxnBYsPl1jng.png)

### 预处理

预处理至关重要，并且因数据集而异。建议将数据转换为适当的类型（例如，将数字字符串转换为整数或浮点数）并删除空值。

```py
#Optional pre-processing
import pandas as pd
import numpy as np


df = pd.read_csv('WARN Notices California_Omer Arain - Sheet1.csv')

#Changes date like column into datetime 
df['Received Date'] = [pd.to_datetime(x) for x in df['Received Date']]
df['Effective Date'] = [pd.to_datetime(x) for x in df['Effective Date']]
#Converts numbers stored as strings into ints
df['Number of Workers'] = [int(str(x).replace(',','')) if str(x)!='nan' else np.nan for x in df['Number of Workers']]
# Replacing NULL values
df = df.replace(np.nan,0)
```

### 将数据集信息存储到索引

以下是如何实现 DataFrame 索引

```py
from llama_index.core.readers.json import JSONReader
from llama_index.core import VectorStoreIndex
import json

# Function that stores the max,min & mean for numerical values
def return_vals(df,c):
    if isinstance(df[c].iloc[0], (int, float, complex)):
        return [max(df[c]), min(df[c]), np.mean(df[c])]
# For datetime we need to store that information as string
    elif(isinstance(df[c].iloc[0],datetime.datetime)):
        return [str(max(df[c])), str(min(df[c])), str(np.mean(df[c]))]
    else:
# For categorical variables you can store the top 10 most frequent items and their frequency
        return list(df[c].value_counts()[:10])

# declare a dictionary 
dict_ = {}
for c in df.columns:
# storing the column name, data type and content
  dict_[c] = {'column_name':c,'type':str(type(df[c].iloc[0])), 'variable_information':return_vals(df,c)}
# After looping storing the information as a json dump that can be loaded 
# into a llama-index Document

# Writing the information into dataframe.json 

with open("dataframe.json", "w") as fp:
    json.dump(dict_ ,fp) 


reader = JSONReader()
# Load data from JSON file
documents = reader.load_data(input_file='dataframe.json')

# Creating an Index
dataframe_index =  VectorStoreIndex.from_documents(documents)
```

### 样式索引

样式工具作为文档存储，其中包含有关如何使用 plotly 样式不同图表自然语言说明。我鼓励你尝试给出的不同说明。以下是有关如何构建折线图和条形图的说明！

```py
from llama_index.core import Document
from llama_index.core import VectorStoreIndex

styling_instructions =[Document(text="""
  Dont ignore any of these instructions.
        For a line chart always use plotly_white template, reduce x axes & y axes line to 0.2 & x & y grid width to 1. 
        Always give a title and make bold using html tag axis label and try to use multiple colors if more than one line
        Annotate the min and max of the line
        Display numbers in thousand(K) or Million(M) if larger than 1000/100000 
        Show percentages in 2 decimal points with '%' sign
        """
        )
        , Document(text="""
        Dont ignore any of these instructions.
        For a bar chart always use plotly_white template, reduce x axes & y axes line to 0.2 & x & y grid width to 1. 
        Always give a title and make bold using html tag axis label and try to use multiple colors if more than one line
        Always display numbers in thousand(K) or Million(M) if larger than 1000/100000. Add annotations x values
        Annotate the values on the y variable
        If variable is a percentage show in 2 decimal points with '%' sign.
        """)


       # You should fill in instructions for other charts and play around with these instructions
       , Document(text=
          """ General chart instructions
        Do not ignore any of these instructions
         always use plotly_white template, reduce x & y axes line to 0.2 & x & y grid width to 1. 
        Always give a title and make bold using html tag axis label 
        Always display numbers in thousand(K) or Million(M) if larger than 1000/100000. Add annotations x values
        If variable is a percentage show in 2 decimal points with '%'""")
         ]
# Creating an Index
style_index =  VectorStoreIndex.from_documents(styling_instructions)
```

### 构建代理

创建的索引需要基于代理作为工具。Llama-Index 具有可从索引构建查询引擎并将其用作工具的功能。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*jZqKXOoDBHAzZGqG_6ea7g.png)

*图片作者 — 解释 Agent 的工作原理*

```py
#All imports for this section
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool
from llama_index.core.tools import  ToolMetadata
from llama_index.llms.groq import Groq


# Build query engines over your indexes
# It makes sense to only retrieve one document per query 
# However, you may play around with this if you need multiple charts
# Or have two or more dataframes with similar column names
dataframe_engine = dataframe_index.as_query_engine(similarity_top_k=1)
styling_engine = style_index.as_query_engine(similarity_top_k=1)

# Builds the tools
query_engine_tools = [
    QueryEngineTool(
        query_engine=dataframe_engine,
# Provides the description which helps the agent decide which tool to use 
        metadata=ToolMetadata(
            name="dataframe_index",
            description="Provides information about the data in the data frame. Only use column names in this tool",
        ),
\
    ),
    QueryEngineTool(
# Play around with the description to see if it leads to better results
        query_engine=styling_engine,
        metadata=ToolMetadata(
            name="Styling",
            description="Provides instructions on how to style your Plotly plots"
            "Use a detailed plain text question as input to the tool.",
        ),
    ),
]

# I used open-source models via Groq but you can use OpenAI/Google/Mistral models as well
llm = Groq(model="llama3-70b-8192", api_key="<your_api_key>")

# initialize ReAct agent
agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)
```

### 调整 Agent 提示 

Llama-Index 和其他编排包具有默认提示，这些提示可能不适用于你的特定用例。在反复试验时我发现，稍微调整提示有助于防止出现幻觉。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*bUl1t8fO51tZSzOL5VcDeA.png)

*作者图片——这是 ReAct Agent 的默认提示语*

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*884bDCUrDFgx2OhTrgfC5w.png)

*图片来自作者——调整提示，以黄色突出显示所做的更改*

```py
from llama_index.core import PromptTemplate

new_prompt_txt= """You are designed to help with building data visualizations in Plotly. You may do all sorts of analyses and actions using Python

## Tools

You have access to a wide variety of tools. You are responsible for using the tools in any sequence you deem appropriate to complete the task at hand.
This may require breaking the task into subtasks and using different tools to complete each subtask.

You have access to the following tools, use these tools to find information about the data and styling:
{tool_desc}


## Output Format

Please answer in the same language as the question and use the following format:

\`\`\`
Thought: The current language of the user is: (user's language). I need to use a tool to help me answer the question.
Action: tool name (one of {tool_names}) if using a tool.
Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num_beams": 5}})
\`\`\`

Please ALWAYS start with a Thought.

Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num_beams': 5}}.

If this format is used, the user will respond in the following format:

\`\`\`
Observation: tool response
\`\`\`

You should keep repeating the above format till you have enough information to answer the question without using any more tools. At that point, you MUST respond in the one of the following two formats:

\`\`\`
Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: [your answer here (In the same language as the user's question)]
\`\`\`

\`\`\`
Thought: I cannot answer the question with the provided tools.
Answer: [your answer here (In the same language as the user's question)]
\`\`\`

## Current Conversation

Below is the current conversation consisting of interleaving human and assistant messages."""

# Adding the prompt text into PromptTemplate object
new_prompt = PromptTemplate(new_prompt_txt)

# Updating the prompt
agent.update_prompts({'agent_worker:system_prompt':new_prompt})
```

## 可视化

现在进入有趣的部分，在第一部分中，我展示了 Llama 3 如何响应我构建可视化的请求。现在让我们向代理提出类似的请求。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*XScsh0UCE7KyJsh65RBXnQ.png)

```py
response = agent.chat("Give Plotly code for a line chart for Number of Workers get information from the dataframe about the correct column names and make sure to style the plot properly and also give a title")
```

*作者图片 — 你可以了解代理如何分解请求，并在最后用 Python 代码做出响应（你可以直接生成输出解析器，或复制并运行）*

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*dUJWU0JWTwcstLWKuaoBKw.png)

*作者图片 — 通过运行以下代码创建的图表，注释、标签/标题、轴格式完全按照样式化信息进行。并且不会构成数据，因为它已经包含了关于 dataframe 的信息。*

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*D23iVjF9dOsR3G0oCH4-Mg.png)

不断围绕样式指令和代理提示进行调整可以产生更好的回复。该项目还有很长的路要走！然而，它可以帮助你节省时间并提供更好的可视化代码。

## 后续步骤

该项目的下一阶段涉及优化提示和处理常见的故障用例。最终目标是制作一套代理工具，可以帮助我（作为数据科学家）在工作时节省时间。如果您喜欢这个概念，请在 Medium 上关注我。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*qWngCXyfjAv1-cC2-n-9GQ.png)

感谢您的阅读！