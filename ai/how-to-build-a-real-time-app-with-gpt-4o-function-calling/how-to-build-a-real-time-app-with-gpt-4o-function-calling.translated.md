# 如何使用 GPT-4o 函数调用构建实时应用

![如何使用 GPT-4o 函数调用构建实时应用的特色图片](https://cdn.thenewstack.io/media/2024/05/96f2ccb9-getty-images-zjuokhavvuo-unsplash-1024x683.jpg)

在我们的 [LLM 中函数调用的指南](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/)中，我们讨论了如何为聊天机器人和代理提供实时数据。现在，我们将通过将 FlightAware.com 的 [API](https://www.flightaware.com/commercial/aeroapi/) 与新的 [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/) 模型集成，进一步探索此概念，以便实时跟踪航班状态。

FlightAware 的 AeroAPI 是一款功能强大的 RESTful API，可按需访问广泛的航班跟踪和状态数据。它允许开发人员通过基于查询的简单系统获取实时、历史或未来的航班信息。该 API 支持基于航班标识符、飞机注册或机场或运营商等位置的详细请求。它旨在以 JSON 格式提供精确、可操作的航空数据，支持从航空公司到机场的整个航空业的运营需求。

在继续之前，请注册 FlightAware 并获取 API 密钥，这对于调用 REST API 至关重要。免费个人层级足以完成本教程。

## 步骤 1：定义获取航班状态的函数

获取 API 密钥后，在 Python 中创建以下函数以检索任何航班的状态。

```python
import requests
import json

AEROAPI_BASE_URL = "https://aeroapi.flightaware.com/aeroapi/"
AEROAPI_KEY = "YOUR_API_KEY"

def get_flight_status(flight):
    """获取航班状态"""
    session = get_api_session()
    data = fetch_flight_data(flight, session)
    return format_flight_details(data)

def get_api_session():
    """初始化请求会话"""
    headers = {"x-apikey": AEROAPI_KEY}
    return requests.Session()

def fetch_flight_data(flight_id, session):
    """获取航班数据"""
    url = f"{AEROAPI_BASE_URL}flights/{flight_id}"
    params = {"filter": "scheduled_departure_time>now-24hours"}
    response = session.get(url, params=params)
    return response.json()

def format_flight_details(data):
    """格式化航班详细信息"""
    flight_details = {}
    flight_details["flight"] = data["flight"]["ident"]
    flight_details["origin"] = data["flight"]["origin"]["code"]
    flight_details["destination"] = data["flight"]["destination"]["code"]
    flight_details["departure_time"] = utc_to_local(data["flight"]["estimated_departure_time"], data["flight"]["origin"]["timezone"])
    flight_details["arrival_time"] = utc_to_local(data["flight"]["estimated_arrival_time"], data["flight"]["destination"]["timezone"])
    flight_details["status"] = data["flight"]["status"]
    return flight_details

def utc_to_local(utc_time, timezone):
    """将 UTC 时间转换为本地时间"""
    import pytz
    utc = pytz.timezone("UTC")
    local = pytz.timezone(timezone)
    return utc.localize(utc_time).astimezone(local).strftime("%Y-%m-%d %H:%M:%S")
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
"description": "获取航班状态",
"parameters": {
"type": "object",
"properties": {
"flight": {
"type": "string",
"description": "航班号"
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
    # 步骤 1：将对话和可用函数发送到模型
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    response_message = response.choices[0].message
```
### Corrected Markdown Format

**Steps:**

1. **Check if the model wants to call a function:**

```
if tool_calls:
    available_functions = {
        "get_flight_status": get_flight_status,
    }
    messages.append(response_message)
```

2. **Send each function call and function response information to the model:**

```
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

3. **Create the final response:**

```
final_response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
)
return final_response
```

**Explanation:**

This chatbot takes a user prompt and processes it using the OpenAI API. It sends the prompt and defined tools to the OpenAI model and processes the response.

Messages are created by embedding the user prompt and sending it to the OpenAI API (`chat.completions.create`). The API processes these messages using the specified tools (if applicable).

For example, when we send the prompt "What is the status of EK524?", GPT-4o determines that it needs to call a function provided in the list of tools and returns the following response:

```
{
    "tool_call_id": "12345",
    "role": "tool",
    "name": "get_flight_status",
    "content": {
        "flight": "EK226",
        "status": "On time"
    }
}
```

Notice that the response includes the function (get_flight_status) and the arguments (EK226).

The next step is to check if any tools were called (i.e., functions in the tools). It executes these functions using the provided arguments, integrates their output into the conversation, and sends this updated information back to the OpenAI API for further processing.

After appending the tool's response to the history, we can call the chat completions endpoint to get the final answer from the LLM.

The `final_response` object contains the answer we are looking for:

```
{
    "messages": [
        {
            "content": "The status of EK524 is On time."
        }
    ]
}
```

Sending a prompt to the function chatbot will return the real-time status of the specified flight.

Here is the complete code for this tutorial:

[Code Snippet]

In this tutorial, we explored how to bring real-time data into an LLM through function calls. In the next part of this series, we will replace GPT-4o with [Gemini Pro](https://thenewstack.io/with-gemini-pro-google-vies-for-top-spot-in-genai-race/) to explore the same concept but with a different model. Stay tuned.

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

Technology moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all of our podcasts, interviews, demos, and more.