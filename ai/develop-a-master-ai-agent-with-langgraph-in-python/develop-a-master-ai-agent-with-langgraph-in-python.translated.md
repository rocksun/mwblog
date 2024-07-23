# 使用 LangGraph 在 Python 中开发一个主 AI 代理

![使用 LangGraph 在 Python 中开发一个主 AI 代理的特色图片](https://cdn.thenewstack.io/media/2024/07/f623f0b8-phone-1024x572.png)

[LangGraph](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) 是 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 生态系统中的一个专门工具，旨在简化 [AI 代理](https://thenewstack.io/ai-agents-key-concepts-and-how-they-overcome-llm-limitations/) 的创建和管理。它提供了一个强大的框架来构建有状态的多参与者应用程序，增强了 AI 系统处理复杂工作流和交互的能力。

**LangGraph 的关键组件**

* **状态：** 状态代表代理的当前状态。它充当内存，存储代理在交互过程中做出决策和做出适当响应所需的上下文和信息。
* **节点：** 节点是 LangGraph 中计算的基本单元。每个节点执行特定任务，例如处理用户输入或生成响应。节点可以执行各种功能，包括调用 API 或运行代码，并将更新的状态信息传递给工作流中的下一个节点。
* **边：** 边定义节点之间的控制流。它们通过连接节点并确定数据在图中的路径来指导操作的顺序。边可以引入条件逻辑，使代理能够动态地处理不同的场景。

**使用 LangGraph 构建 AI 代理**

LangGraph 通过提供一个清晰的结构来管理状态、节点和边，简化了开发高级 AI 应用程序的过程。这使得构建能够处理复杂交互的智能、上下文感知代理变得更加容易。

要创建一个 AI 代理，请使用节点和边定义代理的行为和交互。例如，您可以创建一个客户支持代理，该代理使用 OpenAI 的 GPT-3.5-Turbo 模型处理用户查询并提供响应。代理的状态跟踪对话上下文，而节点执行生成响应所需的计算。边控制对话的流程，确保代理对用户输入做出适当的响应。

本教程将指导您使用 LangGraph 构建 AI 代理，并提供分步代码片段。

**设置环境**

在开始之前，请确保您已安装所需的软件包。您可以在代码编辑器中运行以下命令来执行此操作：

```
!pip install openai langchain_community langchain_openai langgraph
```

接下来，导入必要的库并通过连接到您的 OpenAI API 密钥来设置您的环境：

```python
import openai
import langchain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chains import  load_chain
from langgraph import LangGraph

openai.api_key = "your_openai_api_key" # 请记住将 your_openai_api_key 更改为您的实际 OpenAI API 密钥。
```

**创建简单的 AI 聊天代理**

让我们使用 OpenAI 的 GPT-3.5-Turbo 模型创建一个基本的对话界面。以下函数定义了我们的聊天代理：

```python
def create_chat_agent():
    llm = OpenAI(temperature=0.7)
    memory = ConversationBufferMemory()
    conversation_chain = ConversationChain(llm=llm, memory=memory)
    return conversation_chain
```

**构建客户支持场景**

在此场景中，我们模拟了一个名为 Olasammy 的客户与支持代理互动，询问他购买的故障产品。我们将引导对话并检查 Olasammy 是否获得退款。

首先，定义系统提示模板和说明：

```python
system_template = """
You are a helpful and polite customer support agent. 
You are tasked with resolving customer issues.
"""

user_template = """
{history}
Human: {input}
"""
```

**创建节点和边**

我们将定义函数来处理聊天机器人并模拟用户节点：

```python
def chatbot_node(input: str) -> str:
    conversation_chain = create_chat_agent()
    response = conversation_chain.run(input)
    return response

def user_node(input: str) -> str:
    return input
```

**对话延续逻辑**

定义一个函数来决定是继续还是结束对话：

```python
def continue_conversation(response: str) -> bool:
    if "refund" in response.lower():
        return False
    else:
        return True
```

**构建图**

现在，让我们构建 LangGraph 来管理我们的 AI 聊天代理的工作流程：

```python
graph = LangGraph()

# 定义节点
chatbot = graph.add_node(chatbot_node, name="chatbot")
user = graph.add_node(user_node, name="user")

# 定义边
graph.add_edge(user, chatbot, condition=continue_conversation)
graph.add_edge(chatbot, user)
```

**运行模拟**

启动聊天并观察对话流程：

```python
user_input = "Hello, I have a problem with my recent purchase."
graph.run(user_input, start_node="user")
```

**结论**

LangGraph 使用基于图的工作流简化了有状态的多参与者 AI 应用程序的创建。LangGraph 的循环数据流和有状态工作流为更复杂的 AI 应用程序打开了可能性。您可以随意包含增强的对话体验，例如迭代交互、可定制的流程和多代理协作。

借助 LangGraph，开发人员可以构建更智能、上下文感知的 AI 系统，提供卓越的用户交互和解决方案。

AI 革命并非遥远的未来；它正在发生。在这一新时代，构建一支 AI 准备就绪的团队对于保持竞争力至关重要。阅读我们的博客以 [了解如何](https://www.andela.com/blog-posts/building-an-ai-ready-workforce/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack-july&utm_content=building-ai-workforce&utm_term=writers-room)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)