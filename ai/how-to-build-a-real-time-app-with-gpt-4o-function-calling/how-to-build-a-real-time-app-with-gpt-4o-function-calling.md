
<!--
title: 如何使用GPT-4o函数调用构建实时应用程序
cover: https://cdn.thenewstack.io/media/2024/05/96f2ccb9-getty-images-zjuokhavvuo-unsplash.jpg
-->

本教程将向您展示如何通过函数调用将实时数据引入 LLM，使用 OpenAI 最新推出的 LLM GTP-4o。

> 译自 [How To Build a Real-Time App With GPT-4o Function Calling](https://thenewstack.io/how-to-build-a-real-time-app-with-gpt-4o-function-calling/)，作者 Janakiram MSV。

在我们的 [LLM 中函数调用的指南](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/)中，我们讨论了如何为聊天机器人和代理提供实时数据。现在，我们将通过将 FlightAware.com 的 [API](https://www.flightaware.com/commercial/aeroapi/) 与新的 [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/) 模型集成，进一步探索此概念，以便实时跟踪航班状态。

FlightAware 的 AeroAPI 是一款功能强大的 RESTful API，可按需访问广泛的航班跟踪和状态数据。它允许开发人员通过基于查询的简单系统获取实时、历史或未来的航班信息。该 API 支持基于航班标识符、飞机注册或机场或运营商等位置的详细请求。它旨在以 JSON 格式提供精确、可操作的航空数据，支持从航空公司到机场的整个航空业的运营需求。

![](https://cdn.thenewstack.io/media/2024/05/2b04f36e-gpt-4-fc-0a-1024x694.jpeg)

在继续之前，请注册 FlightAware 并获取 API 密钥，这对于调用 REST API 至关重要。免费个人层级足以完成本教程。

## 步骤 1：定义获取航班状态的函数

获取 API 密钥后，在 Python 中创建以下函数以检索任何航班的状态。

```python
import ast
import json
import random
from datetime import datetime, timedelta
import requests
import pytz

def get_flight_status(flight):
    """Returns Flight Information"""

    AEROAPI_BASE_URL = "https://aeroapi.flightaware.com/aeroapi"
    AEROAPI_KEY="YOUR FLIGHTAWARE API KEY"
    
    def get_api_session():
        session = requests.Session()
        session.headers.update({"x-apikey": AEROAPI_KEY})
        return session

    def fetch_flight_data(flight_id, session):
        if "flight_id=" in flight_id:
            flight_id = flight_id.split("flight_id=")[1]    
        
        start_date = datetime.now().date().strftime('%Y-%m-%d')
        end_date = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
        api_resource = f"/flights/{flight_id}?start={start_date}&end={end_date}"
        response = session.get(f"{AEROAPI_BASE_URL}{api_resource}")
        response.raise_for_status()
        return response.json()['flights'][0]

    def utc_to_local(utc_date_str, local_timezone_str):
        utc_datetime = datetime.strptime(utc_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)
        local_timezone = pytz.timezone(local_timezone_str)
        local_datetime = utc_datetime.astimezone(local_timezone)
        return local_datetime.strftime('%Y-%m-%d %H:%M:%S')    
    
    session = get_api_session()
    flight_data = fetch_flight_data(flight, session)
    
    dep_key = 'estimated_out' if 'estimated_out' in flight_data and flight_data['estimated_out'] else \
          'actual_out' if 'actual_out' in flight_data and flight_data['actual_out'] else \
          'scheduled_out'
    
    arr_key = 'estimated_in' if 'estimated_in' in flight_data and flight_data['estimated_in'] else \
          'actual_in' if 'actual_in' in flight_data and flight_data['actual_in'] else \
          'scheduled_in'    
    
    flight_details = {
        'flight':flight,
        'source': flight_data['origin']['city'],
        'destination': flight_data['destination']['city'],
        'depart_time': utc_to_local(flight_data[dep_key], flight_data['origin']['timezone']),
        'arrival_time': utc_to_local(flight_data[arr_key], flight_data['destination']['timezone']),
        'status': flight_data['status']
    }
    return json.dumps(flight_details)

flight_info = get_flight_status("EK524")
print(flight_info)
#'{"flight": "EK524", "source": "Dubai", "destination": "Hyderabad", "depart_time": "2024-05-23 22:00:00", "arrival_time": "2024-05-24 03:05:00", "status": "Scheduled"}'
```

虽然代码很简单，但让我解释一下关键步骤。

函数 `get_flight_status` 采用一个航班参数（假定为航班标识符）并以 JSON 格式返回格式化的航班详细信息。它查询 AeroAPI 以基于给定的航班标识符获取航班数据，并格式化关键详细信息，例如来源、目的地、出发时间、到达时间和状态。

让我们看看脚本的组件：

**API 凭据：**

* `AEROAPI_BASE_URL` 是 FlightAware AeroAPI 的基本 URL。
* `AEROAPI_KEY` 是用于身份验证的 API 密钥。

**会话管理：**

* `get_api_session`：此嵌套函数初始化请求。会话对象设置带有 API 密钥的必需标头，并返回会话对象。此会话将处理所有 API 请求。

**数据获取：**

* `fetch_flight_data`：此函数采用 `flight_id` 和 `session` 作为参数。它使用适当的日期过滤器构造端点 URL 以获取一天的数据，并发送 GET 请求以检索航班数据。该函数处理 API 响应并提取相关的航班信息。

**时间转换：**

* `utc_to_local`：根据提供的时区字符串将 UTC 时间（来自 API 响应）转换为本地时间。此函数帮助我们根据城市获取到达和出发时间。

**数据处理：**

该脚本根据估计或实际时间的可用性确定出发和到达时间的键，并回退到预定时间。然后，它构造一个包含格式化航班详细信息的字典。

![](https://cdn.thenewstack.io/media/2024/05/efa590fd-gpt-4-fc-0-1024x88.jpeg)

上面的屏幕截图显示了我们从 FlightAware API 收到的阿联酋航空 EK524 航班的响应，该航班从迪拜飞往海得拉巴。请注意，到达和出发时间是基于城市的当地时间。

我们的目标是将此函数与 GPT-4 Omni 集成，以便它可以实时访问航班跟踪信息。

## 步骤 2：使用 GPT-4o 实现函数调用

让我们从导入 OpenAI 库并对其进行初始化开始。

```python
from openai import OpenAI
client = OpenAI()
```

此行创建 OpenAI 类的实例。此实例（`client`）将用于与 [OpenAI API](https://thenewstack.io/the-promise-of-riches-from-ai-wrappers/) 交互。

我们将定义一个名为 `tools` 的列表，其中包含指定函数 `get_flight_status` 的字典。此函数旨在用作 OpenAI API 上下文中的工具，描述其参数和必需的输入。

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_flight_status",
            "description": "Get status of a flight",
            "parameters": {
                "type": "object",
                "properties": {
                    "flight": {
                        "type": "string",
                        "description": "Flight number"
                    }
                },
                "required": ["flight"]
            }
        }
    }
]
```

繁重的工作发生在下面的函数中，其中 LLM 检查提示以确定是否需要调用函数/工具，然后继续生成适当的响应。

```python
def chatbot(prompt):
    # Step 1: send the conversation and available functions to the model
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
 
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        available_functions = {
            "get_flight_status": get_flight_status,
        }  
        messages.append(response_message)  
        
        # Step 3: send the function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(flight=function_args.get("flight"))
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )  
        return final_response
```

这个叫 chatbot 的功能接受一个用户提示，并使用 OpenAI API 处理它。它将提示和已定义的工具发送给 OpenAI 模型，并处理响应。

消息是通过嵌入用户提示并将其发送到 OpenAI API 来创建的（chat.completions.create）。

如果适用，API 使用指定的工具来处理这些消息。例如，当我们发送提示“EK524 的状态是什么？”时，GPT-4o 确定需要调用工具列表中提供的函数，并返回以下响应：

![](https://cdn.thenewstack.io/media/2024/05/262fb52f-gpt-4-fc-1.jpeg)

注意响应包括函数 (get_flight_status) 和参数 (EK226)。

下一步检查是否调用了任何工具（即工具中的函数）。它使用提供的参数执行这些函数，将其输出整合到对话中，并将此更新的信息发回 OpenAI API 以供进一步处理。

```py
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        available_functions = {
            "get_flight_status": get_flight_status,
        }  
        messages.append(response_message)  
        
        # Step 3: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(flight=function_args.get("flight"))
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  
```

此时，信息列表包括原始提示、具有函数名和自变量的初始响应以及来自函数的实际输出。以下屏幕截图显示了包含所有元素的列表。

![](https://cdn.thenewstack.io/media/2024/05/0ee14975-gpt-4-fc-2-744x1024.jpeg)

将工具的响应附加到历史记录后，我们可以调用聊天完成端点来从 LLM 获取最终答案。

```py
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )  
        return final_response
```

final_response 对象有我们正在寻找的答案：

![](https://cdn.thenewstack.io/media/2024/05/3d11fbaa-gpt-4-fc-3-1024x959.jpeg)

在提示发送给函数之后，聊天机器人将做出回应，提供指定航班的实时状态。

![](https://cdn.thenewstack.io/media/2024/05/a6d0a691-gpt-4-fc-4-1024x198.jpeg)

以下是本教程的完整代码：

```py
from openai import OpenAI

#Initialize the environment variable OPENAI_API_KEY with your api key
client = OpenAI()

#Function is available at https://gist.github.com/janakiramm/2143b909626f5f01d64739e3fe90c9c8

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_flight_status",
            "description": "Get status of a flight",
            "parameters": {
                "type": "object",
                "properties": {
                    "flight": {
                        "type": "string",
                        "description": "Flight number"
                    }
                },
                "required": ["flight"]
            }
        }
    }
]

def chatbot(prompt):
    # Step 1: send the conversation and available functions to the model
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    # Step 2: check if the model wanted to call a function
    if tool_calls:
        available_functions = {
            "get_flight_status": get_flight_status,
        }  
        messages.append(response_message)  
        
        # Step 3: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(flight=function_args.get("flight"))
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            ) 
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )  
        return final_response

res=chatbot("What's the status of EK226?")
print(res.choices[0].message.content)
```

在本教程中，我们探讨了如何通过函数调用为 LLM 提供实时数据。在该系列的下一篇中，我们将用 Gemini Pro 替换 GPT-4o，探索相同概念但使用不同的模型。敬请期待。