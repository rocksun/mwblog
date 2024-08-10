
<!--
title: 大型语言模型函数调用入门
cover: https://cdn.thenewstack.io/media/2024/08/3a32a684-phone.jpg
-->

使用 OpenAI API 实现函数调用以增强 LLM 能力的步骤指南。

> 译自 [Getting Started With Function Calling in LLMs](https://thenewstack.io/getting-started-with-function-calling-in-llms/)，作者 Oladimeji Sowole。

[函数调用](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/) 是 [大型语言模型 (LLM)](https://thenewstack.io/llm/)（如 GPT-4）中的一项强大功能，它允许这些模型与外部工具和 API 无缝交互。此功能使 LLM 能够将自然语言转换为可操作的 API 调用，从而使它们在现实世界应用中更加通用和有用。例如，当用户询问“拉各斯的天气怎么样？”时，配备了函数调用的 LLM 可以将此查询转换为对拉各斯尼日利亚天气 API 的函数调用，从而检索那里的当前天气数据。

这种集成对于构建需要实时数据或需要执行特定操作的先进对话代理或聊天机器人至关重要。函数调用允许开发人员定义各种函数，LLM 可以根据对话的上下文和要求调用这些函数。这些函数充当 LLM 应用程序中的工具，能够执行诸如数据提取、知识检索和 API 集成等任务。

通过函数调用，开发人员可以增强 LLM 的功能，使其具有对话性、交互性和对用户需求的响应能力。本指南将引导您完成使用 [OpenAI API](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/) 实现函数调用的步骤，并提供一个简单实用的示例来说明该过程以增强我们语言模型 (LLM) 应用程序的功能。本分步指南将使用代码片段演示如何根据用户输入动态定义和调用函数。我们将使用电影数据库来获取电影详细信息。

**先决条件**

- 您的机器上安装了 Python。
- OpenAI API 密钥。
- dotenv 库用于管理环境变量。

**设置环境**

首先，让我们设置我们的环境并安装必要的库。

```bash
pip install openai python-dotenv
```

接下来，在您的项目目录中创建一个 **.env** 文件并添加您的 OpenAI API 密钥：

```
OPENAI_API_KEY=your_openai_api_key
```

**初始化 OpenAI API**

从 **.env** 文件中加载 API 密钥并在您的脚本中设置它。

```py
import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
```

**设置 OpenAI API 密钥**

```python
openai.api_key = os.getenv('OPENAI_API_KEY')
```

**定义一个获取电影详细信息的函数**

我们将创建一个从虚拟电影数据库中获取电影详细信息的函数。

```py
def get_movie_details(title):
    """Get details of a movie by its title"""
    movie_database = {
        "Inception": {"title": "Inception", "director": "Christopher Nolan", "year": 2010},
        "The Matrix": {"title": "The Matrix", "director": "Wachowski Sisters", "year": 1999},
        "Interstellar": {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014},
    }
    
    return json.dumps(movie_database.get(title, "Movie not found"))

# Example usage
print(get_movie_details("Inception"))
```

**定义 API 的函数**

现在，我们将定义此函数作为 OpenAI API 要使用的工具。

```py
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_movie_details",
            "description": "Get details of a movie by its title",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the movie",
                    },
                },
                "required": ["title"],
            },
        },
    }
]
```

**定义一个获取完成的辅助函数**

此函数将处理 API 请求并处理响应。

```py
def get_completion(messages, model="gpt-3.5-turbo-1106", temperature=0, max_tokens=300, tools=None, tool_choice=None):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        tools=tools,
        tool_choice=tool_choice
    )
    return response.choices[0].message
```

**示例：获取电影详细信息**

让我们创建一个对话，其中用户询问电影详细信息，而 LLM 调用我们的函数来获取必要的信息。

```py
messages = [
    {
        "role": "user",
        "content": "Can you tell me about the movie Inception?",
    }
]

response = get_completion(messages, tools=tools)
print(response)

# Capture the function call arguments
args = json.loads(response.tool_calls[0].function.arguments)
print(get_movie_details(**args))
```

**控制函数调用行为**

您可以控制模型是否应该自动调用函数。

**自动函数调用**

模型自行决定是否调用函数。

```python
get_completion(messages, tools=tools, tool_choice="auto")
```

**不调用函数**

如果您想强制模型不使用提供的任何函数，下面的代码片段给出了如何实现此操作的示例。

```python
get_completion(messages, tools=tools, tool_choice="none")
```

**强制函数调用**

要强制模型调用特定函数，您可以实现：

```python
get_completion(messages, tools=tools, tool_choice={"type": "function", "function": {"name": "get_movie_details"}})
```

**处理多个函数调用**

OpenAI API 支持在一个回合中调用多个函数。例如，获取多个电影的详细信息：

```py
messages = [
    {
        "role": "user",
        "content": "Tell me about the movies Inception and Interstellar.",
    }
]

response = get_completion(messages, tools=tools)

# Assuming the model returns calls for both functions, you would handle each one.
for tool_call in response.tool_calls:
    args = json.loads(tool_call.function.arguments)
    print(get_movie_details(**args))
```

**将函数结果传递回模型**

您可能希望将从 API 获得的结果传递回模型以供进一步处理。

```py
messages = [
    {"role": "user", "content": "Tell me about the movie Inception."}
]

assistant_message = get_completion(messages, tools=tools, tool_choice="auto")
assistant_message = json.loads(assistant_message.model_dump_json())
assistant_message["content"] = str(assistant_message["tool_calls"][0]["function"])

# Remove "function_call" from the assistant message
del assistant_message["function_call"]

messages.append(assistant_message)

# Get the movie details
movie_details = get_movie_details(messages[1]["tool_calls"][0]["function"]["arguments"])

# Pass the movie details back to the model
messages.append({"role": "tool", "tool_call_id": assistant_message["tool_calls"][0]["id"], "name": assistant_message["tool_calls"][0]["function"]["name"], "content": movie_details})

final_response = get_completion(messages, tools=tools)
print(final_response)
```

**结论**

在本教程中，我们探讨了如何使用 OpenAI API 中的函数调用根据用户输入动态获取和使用数据。通过定义函数并控制它们的调用，您可以创建更具交互性和功能的应用程序。此方法可以应用于各种用例，例如查询数据库、调用外部 API 或执行计算。

请随时扩展此示例以满足您的特定需求，并尝试不同的函数和行为。祝您编码愉快！