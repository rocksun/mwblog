<!--
title: 谷歌智能体开发套件：架构深度解析
cover: https://cdn.thenewstack.io/media/2025/12/f044b6c7-fellipe-ditadi-oenyexyz0-o-unsplashb.jpg
summary: Google ADK通过事件驱动运行时架构，彻底改变AI应用开发。核心组件包括Runner、事件循环、执行逻辑、工具集成和服务层，实现上下文管理、外部功能调用及可扩展性。
-->

Google ADK通过事件驱动运行时架构，彻底改变AI应用开发。核心组件包括Runner、事件循环、执行逻辑、工具集成和服务层，实现上下文管理、外部功能调用及可扩展性。

> 译自：[What Is Google’s Agent Development Kit? An Architectural Tour](https://thenewstack.io/what-is-googles-agent-development-kit-an-architectural-tour/)
> 
> 作者：Janakiram MSV

Google 的 [Agent Development Kit](https://google.github.io/adk-docs/) (ADK) 彻底改变了开发者构建 AI 驱动应用的方式。ADK 不再将大型语言模型视为简单的请求-响应系统，而是引入了一种事件驱动的运行时架构，将智能体、工具和持久化状态编排成内聚的应用。

本文将通过天气智能体的实际实现，探讨 ADK 的核心架构组件及其协同工作方式。

## 理解 ADK 运行时架构

以下代码定义了 Python 中的端到端工作流：

```
import os
import asyncio
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types 


import warnings
warnings.filterwarnings("ignore")


import logging
logging.basicConfig(level=logging.ERROR)




def get_weather(city: str) -> dict:
 print(f"--- Tool: get_weather called for city: {city} ---")
 city_normalized = city.lower().replace(" ", "")
 mock_weather_db = {
 "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
 "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
 "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }
 if city_normalized in mock_weather_db:
 return mock_weather_db[city_normalized]
 else:
 return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}


AGENT_MODEL = "gemini-2.5-flash"


weather_agent = Agent(
 name="weather_agent_v1",
 model=AGENT_MODEL,
 description="Provides weather information for specific cities.",
 instruction="You are a helpful weather assistant. "
 "When the user asks for the weather in a specific city, "
 "use the 'get_weather' tool to find the information. "
 "If the tool returns an error, inform the user politely. "
 "If the tool is successful, present the weather report clearly.",
 tools=[get_weather],
)


session_service = InMemorySessionService()


APP_NAME = "weather_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_001"




session = asyncio.run(session_service.create_session(
 app_name=APP_NAME,
 user_id=USER_ID,
 session_id=SESSION_ID
))


print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")


runner = Runner(
 agent=weather_agent,
 app_name=APP_NAME,
 session_service=session_service
)
print(f"Runner created for agent '{runner.agent.name}'.")


def call_agent(query: str, runner, user_id, session_id):
 print(f"\n>>> User Query: {query}")
 content = types.Content(role='user', parts=[types.Part(text=query)])
 final_response_text = "Agent did not produce a final response."


 for event in runner.run(user_id=user_id, session_id=session_id, new_message=content):
 #print(event)
 if event.is_final_response():
 if event.content and event.content.parts:
 final_response_text = event.content.parts[0].text


 print(f"<<< Agent Response: {final_response_text}")


def run_conversation():
 call_agent("What is the weather like in London?", runner, USER_ID, SESSION_ID)
 call_agent("How about Paris?", runner, USER_ID, SESSION_ID)
 call_agent("Tell me the weather in New York", runner, USER_ID, SESSION_ID)


if __name__ == "__main__":
 try:
 run_conversation()
 except Exception as e:
 print(f"An error occurred: {e}")
```

ADK 运行时作为一个复杂的事件循环，在用户请求、AI 模型调用和外部工具执行之间进行调解。从最高层面看，系统的行为由三种主要交互定义。

首先，用户提交一条消息以及一个会话标识符。这个会话 ID 至关重要，因为它允许运行时在多次交互中保持对话上下文。其次，一个内部事件循环通过协调执行逻辑和持久化服务来处理请求。第三，系统将事件流式传输回用户，包括中间工具调用和最终响应。

下面的架构图揭示了实现这一目标的互连组件。

[![](https://cdn.thenewstack.io/media/2025/12/9b1d980b-event-loop-1024x464.png)](https://cdn.thenewstack.io/media/2025/12/9b1d980b-event-loop-1024x464.png)

## 作为编排器的 Runner

Runner 位于 ADK 架构的中心，是所有用户交互的主要入口点。当您实例化一个 Runner 时，您会将其绑定到一个特定的智能体和一个会话服务，从而创建一个自包含的执行上下文。

```
runner = Runner(
    agent=weather_agent,
    app_name=APP_NAME,
    session_service=session_service
)
```

Runner 包含一个事件处理器，它将原始模型输出转换为结构化事件。与 ADK 智能体的每一次交互都通过 Runner 的 run 方法进行，该方法生成一个事件流，而不是返回单个响应。这种流式处理方法实现了实时反馈，并允许应用程序对工具调用等中间步骤做出反应。

```
for event in runner.run(user_id=user_id, session_id=session_id, new_message=content):
    if event.is_final_response():
        final_response_text = event.content.parts[0].text
```

这种模式与传统的 API 调用显著不同。您的应用程序不是等待完整的响应，而是在事件发生时接收它们——这使得进度指示器、调试输出和动态 UI 更新成为可能。

## 事件循环的工作原理

事件循环代表了 ADK 的核心创新。它作为 Runner 和执行逻辑层之间的双向通信通道，遵循“请求-生成”模式。

当 Runner 收到用户消息时，它会要求执行逻辑进行处理。执行逻辑可能会调用底层的 LLM，调用工具，或者执行回调。这些操作中的每一个都会将事件生成回 Runner，然后 Runner 可以将它们转发给用户或触发额外的处理。

这种架构自然地支持多步骤推理。考虑一下当用户询问天气信息时会发生什么。LLM 首先确定它需要调用 `get_weather` 工具。执行逻辑调用该工具并生成包含结果的事件。然后 LLM 处理工具输出并生成人类可读的响应。每个步骤都会产生流经系统的事件。

## 执行逻辑与工具集成

执行逻辑层处理运行智能体的实际工作。它管理 LLM 调用、工具回调以及您定义的任何自定义逻辑。ADK 中的工具只是带有类型提示的 Python 函数，框架会自动将其暴露给底层模型。

```
def get_weather(city: str) -> dict:
    city_normalized = city.lower().replace(" ", "")
    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
    }
    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}
```

智能体配置将工具绑定到特定模型，并提供指导行为的指令。`instruction` 字段充当系统提示，而 `tools` 参数注册可用函数。

```
weather_agent = Agent(
    name="weather_agent_v1",
    model=AGENT_MODEL,
    description="Provides weather information for specific cities.",
    instruction="You are a helpful weather assistant. When the user asks for the weather...",
    tools=[get_weather],
)
```

当 LLM 决定调用 `get_weather` 时，ADK 会处理整个调用生命周期。它解析模型的函数调用，执行您的 Python 函数，并将结果反馈给模型进行解释。

## 服务层与状态管理

服务层提供持久化能力，将无状态的 LLM 交互转换为有状态的应用程序。该层中有三个主要服务在运行。

会话服务在多次对话中维护对话状态。我们示例中使用的 InMemorySessionService 将所有内容存储在内存中，适用于开发和测试。生产部署通常使用像 Cloud Firestore 或 PostgreSQL 这样的持久化后端。

```
session_service = InMemorySessionService()

session = asyncio.run(session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
))
```

工件服务处理文件存储和检索，使智能体能够处理文档、图像和其他二进制数据。内存服务为应在会话之间持久存在的信息提供长期存储。

服务层通过定义良好的接口连接到外部存储系统。这种抽象允许您在不修改智能体逻辑的情况下切换存储后端。您的天气智能体可以通过简单地更改会话服务实现，从内存存储迁移到分布式数据库。

## 完整的请求流程

跟踪系统中的一个完整请求，可以说明这些组件如何协同工作。

用户发送“伦敦天气怎么样？”并附带他们的会话标识符。Runner 接收到此消息，将其封装在 Content 对象中，并启动事件循环。执行逻辑使用用户消息和可用的工具定义来调用 LLM。

模型将其识别为天气查询，并生成一个 `get_weather` 工具调用，参数为“London”。执行逻辑拦截此调用，调用 Python 函数，并捕获返回值。包含工具结果的事件流回系统。

模型接收到工具输出，并生成一个总结天气状况的自然语言响应。此最终响应事件通过 Runner 流式传输给用户。

在整个过程中，会话服务维护上下文。当用户接着问“巴黎怎么样？”时，会话历史允许模型理解这指的是天气，即使第二个查询中从未出现“天气”这个词。

## ADK 的关键设计影响

ADK 的架构揭示了 AI 应用程序开发的几个重要设计原则。

事件驱动的方法实现了通过同步 API 无法实现的可观测性（observability）和调试。您可以记录每一次工具调用，监控模型推理，并围绕智能体行为构建复杂的分析。

Runner 和执行逻辑之间的分离为测试创建了清晰的边界。您可以模拟执行逻辑来测试 Runner 行为，或者为外部服务注入测试替身以独立验证智能体逻辑。

服务层抽象使您的应用程序能够适应未来的基础设施变化。随着智能体内存和会话存储的托管服务变得可用，迁移所需的代码更改将是最小的。

## 结论

Google 的 Agent Development Kit 提供了一个生产就绪的框架，用于构建超越简单聊天界面的 AI 应用程序。事件循环架构，结合强大的会话管理和灵活的工具集成，使开发者能够创建维护上下文、调用外部功能并跨分布式基础设施扩展的智能体。理解这些架构基础将使您能够构建满足实际需求的复杂 AI 系统。