<!--
title: 无需框架构建AI Agent：分步指南
cover: https://www.pondhouse-data.com/blog/BlogHeader_AiAgentsFromScratch.jpg
summary: 手把手教你零框架构建 AI Agent！告别 LangChain 和 AutoGPT，直接调用 GPT-4o API，解锁 PostgreSQL 数据库和 Wikipedia 工具。掌握 Prompt 工程、工具集成和内存管理，无需复杂架构，小白也能轻松上手！更有增强的模式意识数据库工具等你探索。
-->

手把手教你零框架构建 AI Agent！告别 LangChain 和 AutoGPT，直接调用 GPT-4o API，解锁 PostgreSQL 数据库和 Wikipedia 工具。掌握 Prompt 工程、工具集成和内存管理，无需复杂架构，小白也能轻松上手！更有增强的模式意识数据库工具等你探索。

> 译自：[How to Build AI Agents Without Frameworks: A Step-by-Step Guide](https://www.pondhouse-data.com/blog/ai-agents-from-scratch)
> 
> 作者：None

AI Agent 常常过于复杂。从本质上讲，它们只是具有使用工具和记住上下文能力的语言模型。虽然像 [LangChain](https://www.langchain.com/) 或 [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) 这样的框架可以帮助你快速入门，但它们增加了抽象层，这会让你更难理解实际发生的事情，也更难为特定用例定制你的 Agent。

在本教程中，我们将从头开始构建一个 AI Agent，直接调用 GPT-4o 的 API。你将学习如何创建一个可以查询 PostgreSQL 数据库、从 Wikipedia 获取信息并通过简单的数据库存储来维护对话上下文的 Agent。没有框架，只有干净的代码和清晰的概念。

目标是证明 AI Agent 不需要复杂的架构。我们将专注于基本组件：用于工具使用的提示工程、在 PostgreSQL 中存储对话历史记录以及管理 LLM 及其工具之间的交互流程。

最后，你将确切地知道什么是 Agent，它是如何工作的以及如何构建它们。如果你仍然决定使用框架 - 那也没关系。但是，你将更好地了解底层发生的事情。

让我们首先了解是什么使某个事物成为 AI Agent，然后逐步构建一个。

## 什么是 AI Agent？

AI Agent 从根本上来说只是一个可以执行以下操作的语言模型：

- 了解它有哪些可用的工具
- 决定何时使用这些工具
- 记住之前的互动
- 根据所有这些信息做出决定

### 什么是工具？

工具（有时称为“函数”或“能力”）只是 Agent 可以调用以与外部世界交互的函数。它们只是具有以下特征的 Python 函数：

- 对它们的功能的清晰描述
- 定义的输入参数
- 结构化输出

这是一个工具的具体示例：

```py
def search_wikipedia(query: str) -> str:
    """
    Searches Wikipedia and returns the first paragraph of the most relevant article.

    Args:
        query: The search term to look up on Wikipedia

    Returns:
        str: The first paragraph of the most relevant Wikipedia article
    """
    return wikipedia.summary(query, sentences=3)

# This is how we describe the tool to the LLM
wikipedia_tool_description = """
Tool: search_wikipedia
Description: Searches Wikipedia and returns a summary of the topic
Input: A search query string
Example: To learn about Python programming, use: search_wikipedia("Python programming language")
"""
```

当我们让我们的 Agent 访问此工具时，我们实际上是在告诉它：“你可以通过调用此函数来搜索 Wikipedia。” 然后，LLM 根据用户的问题，决定是否需要使用此工具来提供好的答案。当我们说“LLM 决定”时，我们的意思是，我们使用可用的工具提示 LLM，并要求它决定使用哪一个。然后，AI 模型只是返回一个带有工具名称的文本响应。

**工具的常见示例包括：**

- 数据库查询
- 网络搜索
- API 调用
- 文件操作
- 计算器函数
- 电子邮件发送功能

为了将 Agent 和工具的概念结合在一起，我们看到没有涉及任何魔法。这只是 AI 模型交互和一堆 python 函数。

将这些结合在一起，AI Agent 的伪代码可能如下所示：

```py
# This is what an agent interaction basically looks like
def agent_interaction(user_input, available_tools, conversation_history):
    # 1. We tell the LLM what it can do
    prompt = f"""You have access to these tools:
    - query_database: Executes SQL queries
    - search_wikipedia: Searches Wikipedia articles

    Previous conversation:
    {conversation_history}

    User question: {user_input}

    Decide if you need to use a tool to answer. If yes, specify which tool and how to use it."""

    # 2. The LLM decides what to do
    llm_response = gpt4_call(prompt)

    # 3. We execute the tool if needed and get the final answer
    if "use query_database" in llm_response:
        # Execute database query and get result
        data = execute_query(extract_query(llm_response))
        return get_final_answer(data)

    return llm_response
```

这是 Agent 的核心概念。其他一切——复杂的规划、多次工具调用、复杂的内存系统——只是这个基本模式的扩展。

**关于 Agent 的常见误解：**

- 它们不需要复杂的编排框架
- 它们不需要自主运行（尽管它们可以）
- 它们不需要复杂的规划算法（尽管这些算法可以帮助完成复杂的任务）

**构建有效 Agent 的关键不在于你使用的框架，而在于：**

- 编写清晰的提示，帮助 LLM 了解其功能
- 实施 Agent 可以使用的可靠工具
- 通过某种形式的内存存储来维护相关上下文

在以下各节中，我们将使用真实代码来实现此模式，构建一个可以实际查询数据库和搜索 Wikipedia 的 Agent。你将看到复杂性来自你的用例的特定要求，而不是来自 Agent 架构本身。

## 为什么要构建没有框架的 Agent？

通常建议使用像 LangChain 和 AutoGPT 这样的框架来构建 AI Agent。虽然它们对于快速原型设计很有用，但有令人信服的理由可以避免使用它们：

### 了解真正发生了什么

```py
# With a framework:
agent = Agent.from_toolkit(SQLToolkit, WikiToolkit)
result = agent.run("Find users who like pizza")

# Without a framework - what's actually happening:
def process_query(user_input: str):
    prompt = f"""You have these tools:
    1. SQL queries: Execute database queries
    2. Wikipedia search: Look up information

    User question: {user_input}

    Think step by step:
    1. Do I need any tools to answer this?
    2. If yes, which tool and how should I use it?
    """

    response = gpt4_call(prompt)
    if "SQL" in response:
        query = extract_sql(response)
        data = execute_query(query)
    if "Wikipedia" in response:
        data = search_wikipedia(topic)
        return get_final_answer(data)
```

无框架版本更加明确。你可以清楚地看到：

- LLM 被告知了什么
- 何时调用工具
- 如何做出决定

### 灵活性和控制

框架通常对以下方面做出假设：

- 工具应该如何构建
- 提示格式应该是什么
- 内存应该如何工作

当你需要自定义其中任何一个时，你最终会与框架作斗争，而不是与它合作。

### 更简单的调试

当框架出现问题时：

```py
# Framework error:
AgentError: Tool execution failed: SQLToolkit.query failed with error:
Invalid chain configuration...

# Without framework:
try:
    data = execute_query(query)
except SQLException as e:
    print(f"SQL error: {e}")  # Clear what went wrong
```

**注意：** 这或多或少是你应该在没有框架的情况下构建 Agent 的最重要原因。框架抽象掉了任何 AI Agent 的核心 - LLM 交互。在不添加额外基础设施的情况下，你不知道使用的确切提示、回复的特定 LLM 答案以及使用的工具。这使得调试成为一场噩梦。

### 更低的学习成本

构建 Agent 需要理解：

- LLM Prompt 工程
- 工具集成
- 内存管理

框架增加了另一层：

- 框架特定的概念
- 配置选项
- 集成模式

当您只需要基本原理时，为什么还要同时学习两者？

### 性能和资源

框架通常：

- 加载不必要的组件
- 添加网络调用
- 包含未使用的功能

直接实现让您：

- 只加载您需要的内容
- 优化关键路径
- 控制资源使用

**注意：** 可以说，原始性能对于 AI Agent 来说不是最重要的，因为 AI 模型的交互本身就很慢。 因此，加载一些额外的模块并不会增加太多。

### 何时使用框架

在以下情况下，框架是有意义的：

- 您正在构建一个快速原型
- 您需要预构建的工具
- 您最初正在学习 Agent 概念

但对于生产系统或当您需要完全控制时，直接实现通常更好。

让我们继续从头开始构建我们的 Agent，您将看到直接实现是多么的简单。

## 逐步构建 AI Agent

在我们深入研究代码之前，让我们了解一下我们将在第一步中构建什么。 我们将从定义我们的工具开始 - 我们想要赋予我们的 Agent 的能力。

### 步骤 1：定义工具

在此步骤中，我们将创建两个工具：

1. 一个 PostgreSQL 查询工具，允许 Agent 查询您的数据库并搜索存储在数据库中的信息。
2. 一个 Wikipedia 搜索工具，允许 Agent 在 Wikipedia 中查找信息。

我们可以看到这两个工具截然不同，因此根据用户的问题，Agent 应该能够决定使用其中一个工具。

在为 OpenAI 的函数调用定义工具时，我们需要每个工具的三个组件：

- 一个 schema，告诉 LLM 该工具的作用以及如何使用它。 这基本上只是 python 函数的 json 描述。 一旦你看到例子，它就会变得更清楚。
- 该工具的实际实现（Python 函数）
- 错误处理，以确保我们的 Agent 在出现问题时表现得体

schema 特别重要，因为它充当 LLM 的文档。 将其视为编写 API 文档 - 您描述工具的越好，LLM 就会越好地使用它们。 重要的是 `name`（应与函数名称匹配）、`description`（工具的作用）和 `parameters`（我们需要什么函数参数值）。

对于我们的数据库工具，我们将：

- 仅允许 SELECT 查询以确保安全
- 以 JSON 格式返回结果以便于解析
- 包括数据库连接问题的错误处理

对于 Wikipedia 工具，我们将：

- 将结果限制为三个句子，以保持响应简洁
- 处理消歧义页面和缺失的文章
- 在搜索失败时返回结构化的错误消息

以下是我们如何实现这些工具：

```py
import json
import psycopg2
import wikipedia
from typing import Dict, List, Any
from openai import OpenAI

# First, we define how the LLM should understand our tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "query_database",
            "description": """Execute a PostgreSQL SELECT query and return the results.
                            Only SELECT queries are allowed for security reasons.
                            Returns data in JSON format.""",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": """The SQL SELECT query to execute.
                                        Must start with SELECT and should not
                                        contain any data modification commands."""
                    }
                },
                "required": ["query"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_wikipedia",
            "description": """Search Wikipedia and return a concise summary.
                            Returns the first three sentences of the most
                            relevant article.""",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The topic to search for on Wikipedia"
                    }
                },
                "required": ["query"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

# Now implement the actual tool functions
def query_database(query: str) -> str:
    """
    Execute a PostgreSQL query and return results as a JSON string.
    Includes safety checks and error handling.
    """
    # Security check: Only allow SELECT queries
    if not query.lower().strip().startswith('select'):
        return json.dumps({
            "error": "Only SELECT queries are allowed for security reasons."
        })

    try:
        # You should use environment variables for these in production
        conn = psycopg2.connect(
            "dbname=your_db user=your_user password=your_pass host=localhost"
        )

        with conn.cursor() as cur:
            cur.execute(query)

            # Get column names from cursor description
            columns = [desc[0] for desc in cur.description]

            # Fetch results and convert to list of dictionaries
            results = []
            for row in cur.fetchall():
                results.append(dict(zip(columns, row)))

            return json.dumps({
                "success": True,
                "data": str(results),
                "row_count": len(results)
            })

    except psycopg2.Error as e:
        return json.dumps({
            "error": f"Database error: {str(e)}"
        })
    except Exception as e:
        return json.dumps({
            "error": f"Unexpected error: {str(e)}"
        })
    finally:
        if 'conn' in locals():
            conn.close()

def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia and return a concise summary.
    Handles disambiguation and missing pages gracefully.
    """
    try:
        # Try to get the most relevant page summary
        summary = wikipedia.summary(
            query,
            sentences=3,
            auto_suggest=True,
            redirect=True
        )

        return json.dumps({
            "success": True,
            "summary": summary,
            "url": wikipedia.page(query).url
        })

    except wikipedia.DisambiguationError as e:
        # Handle multiple matching pages
        return json.dumps({
            "error": "Disambiguation error",
            "options": e.options[:5],  # List first 5 options
            "message": "Topic is ambiguous. Please be more specific."
        })
    except wikipedia.PageError:
        return json.dumps({
            "error": "Page not found",
            "message": f"No Wikipedia article found for: {query}"
        })
    except Exception as e:
        return json.dumps({
            "error": "Unexpected error",
            "message": str(e)
        })
```

### 步骤 2：创建 Agent 类 - 详细设计

在实现代码之前，让我们准确地了解我们正在构建什么以及它是如何工作的：

**核心概念**

AI Agent 本质上是一个循环：

- 接收用户输入
- 决定是否使用工具
- 如果需要，使用工具
- 制定响应

**关键组件设计**

**1. 消息管理**

- 我们需要将对话历史记录维护为消息列表
- 每条消息都有一个特定的角色：“用户”、“助手”或“工具”
- 历史记录为 LLM 做出更好的决策提供了上下文
- 将其视为聊天应用程序的状态管理

**2. 工具执行系统**

- 像命令调度程序一样工作：
- LLM 决定使用一个工具
- 我们收到一个结构化的函数调用
- 我们将其映射到我们实际的 Python 函数
- 我们处理执行和任何错误
- 我们为 LLM 格式化结果

**3. 主要处理循环**

```
User Input → LLM Decision → [Tool Use?] → Final Response
                              ↓
                        Execute Tool(s)
                              ↓
                     Feed Results back to LLM
```

**错误处理策略**

我们需要三个层次的错误处理：

1. 工具级别错误（例如，数据库连接失败）
2. LLM 级别错误（例如，API 问题）
3. 常规处理错误（例如，JSON 解析）

**消息流示例**

```
User: "How many users are in our database?"
│
├─► LLM Thinks: "I need to query the database"
│    │
│    ├─► Calls query_database tool
│    │    │
│    │    └─► Returns user count
│    │
│    └─► Formulates final response with data
│
└─► Final Response: "There are 1,234 users in the database"
```

这种设计允许：

- 关注点分离清晰
- 易于调试和监控
- 使用新工具进行灵活扩展
- 强大的错误处理
- 可维护的代码库

请注意，我们将通用 Agent 结构实现为一个循环的一部分。 这意味着我们将工具调用的结果发送回 LLM，然后 LLM 决定是制定最终答案还是调用另一个工具。

**实现**

```py
from typing import List, Dict, Optional, Any
from openai import OpenAI
import json

class Agent:
    def __init__(self, system_prompt: Optional[str] = None):
        """
        Initialize an AI Agent with optional system prompt.

        Args:
            system_prompt: Initial instructions for the AI
        """
        # Initialize OpenAI client - expects OPENAI_API_KEY in environment
        self.client = OpenAI()

        # Initialize conversation history
        self.messages = []

        # Set up system prompt if provided, otherwise use default
        default_prompt = """You are a helpful AI assistant with access to a database
        and Wikipedia. Follow these rules:
        1. When asked about data, always check the database first
        2. For general knowledge questions, use Wikipedia
        3. If you're unsure about data, query the database to verify
        4. Always mention your source of information
        5. If a tool returns an error, explain the error to the user clearly
        """

        self.messages.append({
            "role": "system",
            "content": system_prompt or default_prompt
        })

    def execute_tool(self, tool_call: Any) -> str:
        """
        Execute a tool based on the LLM's decision.

        Args:
            tool_call: The function call object from OpenAI's API

        Returns:
            str: JSON-formatted result of the tool execution
        """
        try:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            # Execute the appropriate tool. Add more here as needed.
            if function_name == "query_database":
                result = query_database(function_args["query"])
            elif function_name == "search_wikipedia":
                result = search_wikipedia(function_args["query"])
            else:
                result = json.dumps({
                    "error": f"Unknown tool: {function_name}"
                })

            return result

        except json.JSONDecodeError:
            return json.dumps({
                "error": "Failed to parse tool arguments"
            })
        except Exception as e:
            return json.dumps({
                "error": f"Tool execution failed: {str(e)}"
            })

    def process_query(self, user_input: str) -> str:
        """
        Process a user query through the AI agent.

        Args:
            user_input: The user's question or command

        Returns:
            str: The agent's response
        """
        # Add user input to conversation history
        self.messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            max_iterations = 5
            current_iteration = 0

            while current_iteration < max_iterations:  # Limit to 5 iterations
                current_iteration += 1
                completion = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages=self.messages,
                    tools=tools,  # Global tools list from Step 1
                    tool_choice="auto"  # Let the model decide when to use tools
                )

                response_message = completion.choices[0].message

                # If no tool calls, we're done
                if not response_message.tool_calls:
                    self.messages.append(response_message)
                    return response_message.content

                # Add the model's thinking to conversation history
                self.messages.append(response_message)

                # Process all tool calls
                for tool_call in response_message.tool_calls:
                    try:
                        print("Tool call:", tool_call)
                        result = self.execute_tool(tool_call)
                        print("Tool executed......")
                    except Exception as e:
                        print("Execution failed......")
                        result = json.dumps({
                            "error": f"Tool execution failed: {str(e)}"
                        })

                    print(f"Tool result custom: {result}")

                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result)
                    })
                    print("Messages:", self.messages)

            # If we've reached max iterations, return a message indicating this
            max_iterations_message = {
                "role": "assistant",
                "content": "I've reached the maximum number of tool calls (5) without finding a complete answer. Here's what I know so far: " + response_message.content
            }
            self.messages.append(max_iterations_message)
            return max_iterations_message["content"]

        except Exception as e:
            error_message = f"Error processing query: {str(e)}"
            self.messages.append({
                "role": "assistant",
                "content": error_message
            })
            return error_message

    def get_conversation_history(self) -> List[Dict[str, str]]:
        """
        Get the current conversation history.

        Returns:
            List[Dict[str, str]]: The conversation history
        """
        return self.messages
```

### 步骤 3（可选）：向我们的 Agent 添加内存

**注意：** 请考虑您是否需要内存。 您的应用程序是否真的需要存储和检索对话历史记录？ 通常，答案是否定的！ 但是如果您确实需要内存，这里是如何添加它的。

AI Agent 中的内存通常过于复杂。 让我们了解我们实际想要实现的目标：

**什么是 Agent 内存？**

Agent 内存的核心只是：

1. 存储对话及其上下文
2. 在需要时检索相关信息
3. 总结过往的过长交互

**我们将要实现的记忆类型**

**1. 对话历史**

- 存储：用户输入、代理回复、工具使用结果
- 目的：跟踪当前的对话流程

**2. 总结记忆**

- 内容：更长对话的周期性总结
- 原因：防止上下文窗口溢出
- 方法：在 X 条消息后或按需创建总结

**数据库模式**

```sql
CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    session_id UUID,
    user_input TEXT,
    agent_response TEXT,
    tool_calls JSONB,  -- Store tool usage
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE conversation_summaries (
    id SERIAL PRIMARY KEY,
    session_id UUID,
    summary TEXT,
    start_time TIMESTAMPTZ,
    end_time TIMESTAMPTZ,
    message_count INTEGER
);
```

**记忆流**

```
User Input ─► Store in DB ─────────────┐
                                       │
                                       ▼
                            Check Context Length
                                       │
                                       ▼
                          If too long, Summarize
                                       │
                                       ▼
                         Load Relevant Context
                                       │
                                       ▼
                           Send to LLM with
                           Next User Input
```

**AI 代理的记忆实现**

```py
from datetime import datetime
import uuid
from typing import List, Dict, Optional
from dataclasses import dataclass
import psycopg2
from psycopg2.extras import Json, UUID_adapter

@dataclass
class MemoryConfig:
    """Configuration for memory management"""
    max_messages: int = 20  # When to summarize
    summary_length: int = 2000  # Max summary length in words
    db_connection: str = "dbname=your_db user=your_user password=your_pass"

class AgentMemory:
    def __init__(self, config: Optional[MemoryConfig] = None):
        self.config = config or MemoryConfig()
        self.session_id = uuid.uuid4()
        self.setup_database()

    def setup_database(self):
        """Create necessary database tables if they don't exist"""
        queries = [
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id SERIAL PRIMARY KEY,
                session_id UUID NOT NULL,
                user_input TEXT NOT NULL,
                agent_response TEXT NOT NULL,
                tool_calls JSONB,
                timestamp TIMESTAMPTZ DEFAULT NOW()
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS conversation_summaries (
                id SERIAL PRIMARY KEY,
                session_id UUID NOT NULL,
                summary TEXT NOT NULL,
                start_time TIMESTAMPTZ NOT NULL,
                end_time TIMESTAMPTZ NOT NULL,
                message_count INTEGER NOT NULL
            );
            """
        ]

        with psycopg2.connect(self.config.db_connection) as conn:
            with conn.cursor() as cur:
                for query in queries:
                    cur.execute(query)

    def store_interaction(self,
                         user_input: str,
                         agent_response: str,
                         tool_calls: Optional[List[Dict]] = None):
        """Store a single interaction in the database"""
        query = """
        INSERT INTO conversations
            (session_id, user_input, agent_response, tool_calls)
        VALUES (%s, %s, %s, %s)
        """

        with psycopg2.connect(self.config.db_connection) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (
                    self.session_id,
                    user_input,
                    agent_response,
                    Json(tool_calls) if tool_calls else None
                ))

    def create_summary(self, messages: List[Dict]) -> str:
        """Create a summary of messages using the LLM"""
        client = OpenAI()

        # Prepare messages for summarization
        summary_prompt = f"""
        Summarize the following conversation in less than {self.config.summary_length} words.
        Focus on key points, decisions, and important information discovered through tool usage.

        Conversation:
        {messages}
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": summary_prompt}]
        )

        return response.choices[0].message.content

    def store_summary(self, summary: str, start_time: datetime, end_time: datetime, message_count: int):
        """Store a conversation summary"""
        query = """
        INSERT INTO conversation_summaries
            (session_id, summary, start_time, end_time, message_count)
        VALUES (%s, %s, %s, %s, %s)
        """

        with psycopg2.connect(self.config.db_connection) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (
                    self.session_id,
                    summary,
                    start_time,
                    end_time,
                    message_count
                ))

    def get_recent_context(self) -> str:
        """Get recent conversations and summaries for context"""
        # First, get the most recent summary
        summary_query = """
        SELECT summary, end_time
        FROM conversation_summaries
        WHERE session_id = %s
        ORDER BY end_time DESC
        LIMIT 1
        """

        # Then get conversations after the summary
        conversations_query = """
        SELECT user_input, agent_response, tool_calls, timestamp
        FROM conversations
        WHERE session_id = %s
        AND timestamp > %s
        ORDER BY timestamp ASC
        """

        with psycopg2.connect(self.config.db_connection) as conn:
            with conn.cursor() as cur:
                # Get latest summary
                cur.execute(summary_query, (self.session_id,))
                summary_row = cur.fetchone()

                if summary_row:
                    summary, last_summary_time = summary_row
                    # Get conversations after the summary
                    cur.execute(conversations_query, (self.session_id, last_summary_time))
                else:
                    # If no summary exists, get recent conversations
                    cur.execute("""
                        SELECT user_input, agent_response, tool_calls, timestamp
                        FROM conversations
                        WHERE session_id = %s
                        ORDER BY timestamp DESC
                        LIMIT %s
                    """, (self.session_id, self.config.max_messages))

                conversations = cur.fetchall()

        # Format context
        context = []
        if summary_row:
            context.append(f"Previous conversation summary: {summary}")

        for conv in conversations:
            user_input, agent_response, tool_calls, _ = conv
            context.append(f"User: {user_input}")
            if tool_calls:
                context.append(f"Tool Usage: {tool_calls}")
            context.append(f"Assistant: {agent_response}")

        return "\n".join(context)

    def check_and_summarize(self):
        """Check if we need to summarize and do it if necessary"""
        query = """
        SELECT COUNT(*)
        FROM conversations
        WHERE session_id = %s
        AND timestamp > (
            SELECT COALESCE(MAX(end_time), '1970-01-01'::timestamptz)
            FROM conversation_summaries
            WHERE session_id = %s
        )
        """

        with psycopg2.connect(self.config.db_connection) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (self.session_id, self.session_id))
                count = cur.fetchone()[0]

                if count >= self.config.max_messages:
                    # Get messages to summarize
                    cur.execute("""
                        SELECT user_input, agent_response, tool_calls, timestamp
                        FROM conversations
                        WHERE session_id = %s
                        ORDER BY timestamp ASC
                        LIMIT %s
                    """, (self.session_id, count))

                    messages = cur.fetchall()
                    if messages:
                        # Create and store summary
                        summary = self.create_summary(messages)
                        self.store_summary(
                            summary,
                            messages[0][3],  # start_time
                            messages[-1][3],  # end_time
                            len(messages)
                        )

# Update Agent class to use memory.
class MemoryAgent(Agent):
    def __init__(self, memory_config: Optional[MemoryConfig] = None):
        self.client = OpenAI()
        self.memory = AgentMemory(memory_config)
        self.messages = []

        # Initialize with system prompt
        self.messages.append({
            "role": "system",
            "content": "You are a helpful AI assistant..."
        })

    def process_query(self, user_input: str) -> str:
        try:
            # Check if we need to summarize before adding new messages
            self.memory.check_and_summarize()

            # Get context (including summaries) from memory
            context = self.memory.get_recent_context()

            # Add context to messages if it exists
            if context:
                self.messages = [
                    self.messages[0],  # Keep system prompt
                    {
                        "role": "system",
                        "content": f"Previous conversation context:\n{context}"
                    }
                ]

            # Process the query as before...
            response = super().process_query(user_input)

            # Store the interaction in memory
            tool_calls = None
            if hasattr(self, 'last_tool_calls'):
                tool_calls = self.last_tool_calls

            self.memory.store_interaction(
                user_input=user_input,
                agent_response=response,
                tool_calls=tool_calls
            )

            return response

        except Exception as e:
            error_message = f"Error processing query: {str(e)}"
            self.memory.store_interaction(
                user_input=user_input,
                agent_response=error_message
            )
            return error_message

    def execute_tool(self, tool_call: Any) -> str:
        # Store tool calls for memory
        if not hasattr(self, 'last_tool_calls'):
            self.last_tool_calls = []

        result = super().execute_tool(tool_call)

        # Store tool call information
        self.last_tool_calls.append({
            'tool': tool_call.function.name,
            'arguments': tool_call.function.arguments,
            'result': result
        })

        return result
```

### 步骤 4：使用你的 AI 代理

完成所有设置后，使用代理非常简单。方法如下：

```py
from your_agent import Agent, MemoryConfig  # assuming we saved our code in your_agent.py

# Create an agent
agent = Agent(
    memory_config=MemoryConfig(
        max_messages=10,  # summarize after 10 messages
        db_connection="postgresql://user:pass@localhost/your_db"
    )
)

# Simple question-answer interaction
def chat_with_agent(question: str):
    print(f"\nUser: {question}")
    print(f"Assistant: {agent.process_query(question)}")

if __name__ == "__main__":
    chat_with_agent("How many users do we have in our database?")
    chat_with_agent("What's the average age of users from New York?")
    chat_with_agent("Compare our user base in California with PostgreSQL's popularity there")
    chat_with_agent("What were the numbers you just mentioned?")
    chat_with_agent("What are the most interesting trends you can find in our user data?")
```

就是这样！代理将：

- 在需要时使用数据库
- 在适当时搜索维基百科
- 记住之前的上下文
- 自动创建总结
- 在幕后处理所有复杂性 - 但同时让我们能够直接进行调试

输出看起来干净自然：

```
User: How many users do we have in our database?
Assistant: According to the database, we currently have 10,432 registered users.

User: What's the average age of users from New York?
Assistant: I've queried the database and found that users from New York have an average age of 31.5 years.

User: Compare our user base in California with PostgreSQL's popularity there
Assistant: Let me check both sources. According to our database, we have 2,345 users from California. From Wikipedia, PostgreSQL is particularly popular in the Silicon Valley region, being used by companies like Apple, Instagram, and Reddit. In fact, many of our California users (43%) are in the tech industry, which aligns with PostgreSQL's strong presence in the region.
```

### 增强的具有模式意识的数据库工具

可以说，上面的 PostgreSQL 数据库工具有点简单，不是吗？AI 模型应该从哪里知道哪些数据库列可用？你是对的 - 为了更清晰起见，我们省略了这个关键细节。我们将修改我们的数据库工具以包含模式信息，这有助于 LLM 了解哪些数据可用以及如何正确查询它：

```py
def get_database_schema() -> str:
    """Retrieve the database schema information"""
    schema_query = """
    SELECT
        t.table_name,
        array_agg(
            c.column_name || ' ' ||
            c.data_type ||
            CASE
                WHEN c.is_nullable = 'NO' THEN ' NOT NULL'
                ELSE ''
            END
        ) as columns
    FROM information_schema.tables t
    JOIN information_schema.columns c
        ON c.table_name = t.table_name
    WHERE t.table_schema = 'public'
        AND t.table_type = 'BASE TABLE'
    GROUP BY t.table_name;
    """

    try:
        with psycopg2.connect("dbname=your_db user=your_user password=your_pass") as conn:
            with conn.cursor() as cur:
                cur.execute(schema_query)
                schema = cur.fetchall()

                # Format schema information
                schema_str = "Database Schema:\n"
                for table_name, columns in schema:
                    schema_str += f"\n{table_name}\n"
                    for col in columns:
                        schema_str += f"  - {col}\n"

                return schema_str
    except Exception as e:
        return f"Error fetching schema: {str(e)}"

# Updated tool definition with schema information;
# Note that we could also dynamically fetch the schema when needed
tools = [
    {
        "type": "function",
        "function": {
            "name": "query_database",
            "description": """Execute a PostgreSQL SELECT query and return the results.
            Available tables and their schemas:

            users
              - id SERIAL PRIMARY KEY
              - email VARCHAR(255) NOT NULL
              - age INTEGER
              - location VARCHAR(100)
              - signup_date DATE NOT NULL
              - last_login TIMESTAMP WITH TIME ZONE
              - job_industry VARCHAR(100)

            user_activity
              - id SERIAL PRIMARY KEY
              - user_id INTEGER REFERENCES users(id)
              - activity_date DATE NOT NULL
              - activity_type VARCHAR(50) NOT NULL
            """,
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The SQL SELECT query to execute. Must start with SELECT for security."
                    }
                },
                "required": ["query"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

# Updated database query function
def query_database(query: str) -> str:
    """
    Execute a PostgreSQL query with schema awareness
    """
    if not query.lower().strip().startswith('select'):
        return json.dumps({
            "error": "Only SELECT queries are allowed for security reasons.",
            "schema": get_database_schema()  # Return schema for reference
        })

    try:
        with psycopg2.connect("dbname=your_db user=your_user password=your_pass") as conn:
            with conn.cursor() as cur:
                cur.execute(query)

                # Get column names from cursor description
                columns = [desc[0] for desc in cur.description]

                # Fetch results and convert to list of dictionaries
                results = []
                for row in cur.fetchall():
                    results.append(dict(zip(columns, row)))

                return json.dumps({
                    "success": True,
                    "data": str(results),
                    "row_count": len(results),
                    "columns": columns
                })

    except Exception as e:
        return json.dumps({
            "error": str(e),
            "schema": get_database_schema()  # Return schema on error for help
        })

# Usage example:
agent = Agent()

# The agent now knows about the schema and can write better queries
response = agent.process_query(
    "What's the age distribution of users by location and industry?"
)
```


主要改进：

1. 工具描述中的模式信息
2. 包括列类型和约束
3. 错误时返回模式以实现更好的错误处理
4. 具有列名称的详细结果结构

这有助于 LLM：

- 第一次尝试就编写正确的查询
- 了解可用数据
- 更好地处理错误
- 提供更详细的响应