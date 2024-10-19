# 使用 Python 的多智能体系统中的协同智能

![使用 Python 的多智能体系统中的协同智能的特色图片](https://cdn.thenewstack.io/media/2024/10/f76df61f-transportation-1024x576.jpg)
[metamorworks](https://www.shutterstock.com/g/chombosan) 在 Shutterstock 上。

近年来，[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 通过生成类似人类的文本、解决复杂问题和自主执行任务，重新定义了人工智能的能力。

然而，随着任务变得更加复杂和跨学科，单个 AI 模型可能并不总是足够。这就是 [多智能体系统](https://thenewstack.io/genai-multi-agent-systems-a-secret-weapon-for-tech-teams/) (MAS) 在 LLM 中的概念发挥作用的地方。MAS 允许多个 AI 智能体协作，每个智能体专门负责问题的不同方面，共同努力实现共同目标。

本教程将使用 [Python](https://thenewstack.io/what-is-python/) 探索 LLM 中多智能体系统的最新趋势。我们将介绍什么是多智能体系统、它们为什么重要以及如何使用 LangChain 等工具使用 Python 分步实现它们。

**什么是多智能体系统？**

多智能体系统 (MAS) 是一个环境，其中多个自主智能体相互交互、合作甚至竞争以解决问题。每个智能体都有自己的能力、优势和关注领域，使系统能够更有效地处理复杂的任务。这些系统在需要协作、并行任务执行甚至协商的场景中表现出色。

在 LLM 中，多智能体系统可以：

- 协作完成需要多个专业领域的任务（例如，一个智能体专注于数学，而另一个智能体处理自然语言理解）。
- 互相协商以解决目标冲突。
- 并行解决复杂的、多步骤的问题，
[提高速度和准确性](https://thenewstack.io/accuracy-improves-when-large-language-models-collaborate/)。

**多智能体系统的用例**

- **财务规划**: 一个智能体可以专注于分析股票趋势，而另一个智能体可以预测市场的未来行为。
- **医疗保健**: 一个智能体专注于诊断分析，而另一个智能体协助患者病史回顾，共同为全面的医疗保健建议提供帮助。
- **供应链优化**: 智能体可以专门从事物流、采购或需求预测，从而改善整个供应链的决策。

**为什么要使用多智能体系统？**

- **专业化**: 不同的智能体专门负责不同的任务，使解决问题更加高效。
- **并行性**: 智能体可以同时工作，显着减少完成多步骤操作所需的时间。
- **协作**: 多个智能体共同努力，利用其独特的优势来实现最佳结果。
- **适应性**: 智能体可以实时协商或调整策略，以适应不断变化的任务。

**使用 Python 设置多智能体系统**

让我们从理论转向实践。在本节中，我们将演示如何使用 Python 和 LangChain 库构建多智能体系统，该库允许不同 LLM 支持的智能体之间无缝交互。

**安装依赖项**

首先，我们需要安装 LangChain 并设置一个 LLM 服务，例如 OpenAI。

```bash
pip install langchain openai
```

您还需要一个 OpenAI API 密钥，您可以通过注册 OpenAI 的 API 服务来获取。

**初始化智能体和工具**

首先，我们将定义我们的 LLM（GPT 模型）以及我们的智能体将使用的一组工具。这些工具可以是任何东西，从计算器到网络搜索功能。让我们初始化协作解决涉及信息检索和数学计算的任务的智能体。

**工作原理**

- **智能体协作**: 在此示例中，一个智能体使用搜索工具（例如 SERP API）获取实时汇率，而另一个智能体使用计算器工具将汇率乘以 1,500。
- **任务分解**: LLM 将任务分解为子任务（获取汇率和执行计算），并将这些子任务分配给相应的智能体。

**构建复杂的智能体系统**

现在我们已经看到了一个基本示例，让我们构建一个更复杂的系统，该系统涉及多个智能体来解决问题的不同部分。考虑一个场景，我们正在构建一个旅行助手，它可以处理与预订航班、查看天气和执行预算计算相关的多个查询。

**分步代码：旅行助手多智能体系统**

```python
from langchain.agents import Tool, AgentExecutor
from langchain.agents.tools import Tool
from langchain.llms import OpenAI
from langchain.chains import  LLMChain
from langchain.chains.conversation.memory import ConversationBufferMemory

# 初始化 LLM
llm = OpenAI(temperature=0.7)

# 定义工具
tools = [
    Tool(
        name="book_flight",
        func=lambda query: f"预订从 {query} 出发的航班",
        description="预订航班。输入城市名称。"
    ),
    Tool(
        name="get_weather",
        func=lambda city: f"{city} 的天气很好",
        description="获取城市的天气信息。输入城市名称。"
    ),
    Tool(
        name="calculate_budget",
        func=lambda amount: f"您的剩余预算为 {amount} 美元",
        description="计算预算。输入金额。"
    )
]

# 创建智能体
agent = AgentExecutor.from_tool_names(
    tools,
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

# 与智能体交互
print(agent.run("我想要预订从巴黎出发的航班，然后查看巴黎的天气，最后计算一下我的剩余预算。"))
```

**发生了什么？**

- **航班智能体**: `book_flight` 智能体处理任务的航班预订部分。
- **天气智能体**: `get_weather` 智能体检索巴黎的天气数据。
- **预算智能体**: `calculate_budget` 智能体根据用户的输入计算用户的剩余预算。

### EDITOR'S RESPONSE
在这种情况下，每个代理都负责解决更大问题中的特定部分，并协同工作以提供全面的结果。整个过程由 LLM 驱动，LLM 协调代理的工作。

**多代理系统的先进用例**

**医疗保健协作**

在医疗保健领域，不同的代理可以专注于患者治疗过程的不同部分。例如：

- 一个代理可以分析医学影像。
- 另一个代理审查患者的病史。
- 第三个代理提供诊断建议。

通过协同工作，这些代理可以生成一份综合报告，帮助做出更准确、更快速的医疗决策。

**供应链优化**

多代理系统可用于管理供应链的不同方面：

- 物流代理跟踪运输时间。
- 采购代理监控库存水平。
- 预测代理预测未来需求。

它们共同可以优化供应链，减少延误，降低成本，提高整体效率。

**结论**

多代理系统 (MAS) 代表了人工智能驱动解决方案发展中的一个突破性趋势。通过允许多个代理协同工作，每个代理都有自己的专业领域，MAS 极大地提高了大规模问题解决任务的效率和有效性。借助 LangChain 等 Python 工具，实现多代理系统变得越来越容易，使开发人员能够创建超越简单自动化的智能系统。

*您是否想探索与 AI 代理和 Python 合作的可能性？阅读 Andela 的博客，了解如何在 Python 中使用 LangGraph 开发主 AI 代理！*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。