
<!--
title: 如何通过模型上下文协议实施Elicitation
cover: https://cdn.thenewstack.io/media/2025/08/9ac7fbba-getty-images-f21ae8dxxy4-unsplashb.jpg
summary: 本文介绍了如何使用MCP协议中的Elicitation概念，通过示例代码展示了如何构建带有Elicitation的MCP服务器和客户端，实现用户交互式输入，并将结果与Gemini集成进行分析。
-->

本文介绍了如何使用MCP协议中的Elicitation概念，通过示例代码展示了如何构建带有Elicitation的MCP服务器和客户端，实现用户交互式输入，并将结果与Gemini集成进行分析。

> 译自：[How To Implement Elicitation With Model Context Protocol](https://thenewstack.io/how-to-implement-elicitation-with-model-context-protocol/)
> 
> 作者：Janakiram MSV

在[之前的文章](https://yylives.cc/2025/07/25/how-elicitation-in-mcp-brings-human-in-the-loop-to-ai-tools/)中，我介绍了[模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) 中的[Elicitation](https://modelcontextprotocol.io/specification/draft/client/elicitation)概念。本教程演示了一种集成Elicitation的实用方法，用于接收用户输入，而不是将硬编码的参数发送到 MCP 服务器公开的工具。

## 步骤 1：创建环境

让我们从虚拟环境和 `requirements.txt` 文件开始。

```
python -m venv .venv
source .venv/bin/activate
```

创建包含以下内容的 `requirements.txt`：

```
pytz
fastmcp
httpx
google-genai
```

```
pip install --upgrade -r requirements.txt
```

分别为 [FlightAware](https://www.flightaware.com/commercial/data/) 和 [Gemini](https://aistudio.google.com) API 设置环境变量 `AEROAPI_KEY` 和 `GEMINI_API_KEY`。

## 步骤 2：构建并启动 MCP 服务器

以下是带有Elicitation的 MCP 服务器的代码：

```py
# server.py
from fastmcp import FastMCP, Context
from dataclasses import dataclass
import httpx
import os
from datetime import datetime, timedelta
import pytz


mcp = FastMCP("Flight Status Server")


@dataclass
class FlightInfo:
 flight_number: str


@mcp.tool
async def get_flight_status(ctx: Context) -> str:
 """Get live flight status information by collecting flight number interactively."""
 
 # Elicit flight number from user
 result = await ctx.elicit(
 message="Please provide the flight number you want to check",
 response_type=FlightInfo
    )
 
 if result.action == "decline":
 return "Flight number not provided"
 elif result.action == "cancel":
 return "Operation cancelled"
 elif result.action != "accept":
 return "Invalid response"
 
 flight_number = result.data.flight_number
 
 try:
 # Fetch flight data
 flight_details = await _fetch_flight_status(flight_number)
 
 # Format response
 return f"""
Flight Status for {flight_details['flight']}:
• Route: {flight_details['source']} → {flight_details['destination']}
• Departure: {flight_details['depart_time']}
• Arrival: {flight_details['arrival_time']}
• Status: {flight_details['status']}
        """.strip()
 
 except Exception as e:
 return f"Error fetching flight status: {str(e)}"


async def _fetch_flight_status(flight: str) -> dict:
 """Internal function to fetch flight status from FlightAware API."""
 AEROAPI_BASE_URL = "https://aeroapi.flightaware.com/aeroapi"
 AEROAPI_KEY = os.getenv("AERO_API_KEY")
 
 if not AEROAPI_KEY:
 raise ValueError("AERO_API_KEY is not set in environment variables")
 
 def _clean_flight_id(flight_id):
 if "flight_id=" in flight_id:
 return flight_id.split("flight_id=")[1]
 return flight_id
 
 def _utc_to_local(utc_date_str, local_timezone_str):
 utc_datetime = datetime.strptime(utc_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)
 local_timezone = pytz.timezone(local_timezone_str)
 local_datetime = utc_datetime.astimezone(local_timezone)
 return local_datetime.strftime('%Y-%m-%d %H:%M:%S')
 
 # Prepare API request
 flight_id = _clean_flight_id(flight)
 start_date = datetime.now().date().strftime('%Y-%m-%d')
 end_date = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
 api_resource = f"/flights/{flight_id}?start={start_date}&end={end_date}"
 
 # Make API call
 async with httpx.AsyncClient(headers={"x-apikey": AEROAPI_KEY}) as client:
 response = await client.get(f"{AEROAPI_BASE_URL}{api_resource}")
 response.raise_for_status()
 flight_data = response.json()['flights'][0]
 
 # Determine best available times
 dep_key = ('estimated_out' if flight_data.get('estimated_out') else
 'actual_out' if flight_data.get('actual_out') else
 'scheduled_out')
 
 arr_key = ('estimated_in' if flight_data.get('estimated_in') else
 'actual_in' if flight_data.get('actual_in') else
 'scheduled_in')
 
 # Build response
 flight_details = {
 'flight': flight,
 'source': flight_data['origin']['city'],
 'destination': flight_data['destination']['city'],
 'depart_time': _utc_to_local(flight_data[dep_key], flight_data['origin']['timezone']),
 'arrival_time': _utc_to_local(flight_data[arr_key], flight_data['destination']['timezone']),
 'status': flight_data['status']
    }
 
 return flight_details


if __name__ == "__main__":
 mcp.run(transport="streamable-http", host="127.0.0.1", port=8080, path="/mcp")
```

让我们看看帮助我们实现Elicitation的重要的代码片段。

### **定义结构化响应**

```
@dataclass
class FlightInfo:
    flight_number: str
```

此数据类设置了用户输入的预期模式。它确保客户端响应是强类型的，并在返回到服务器时进行验证。

### **声明工具条目**

```
@mcp.tool
async def get_flight_status(ctx: Context) -> str:
    """Get live flight status information by collecting flight number interactively."""
```

此函数定义了客户端可用的工具。 ctx 参数支持与用户进行Elicitation和结构化交互。

### **通过Elicitation要求客户端输入**

```
result = await ctx.elicit(
    message="Please provide the flight number you want to check",
    response_type=FlightInfo
)
```

此调用触发Elicitation过程。服务器发送一条消息，并请求与 FlightInfo 模式匹配的响应。

### **处理来自Elicitation结果的用户操作**

```
if result.action == "decline":
    return "Flight number not provided"
elif result.action == "cancel":
    return "Operation cancelled"
elif result.action != "accept":
    return "Invalid response"
```

这些条件确保了对用户决策的强大处理。服务器根据是否接受、拒绝或取消输入而优雅地退出或继续。

### **使用接受的输入**

```
flight_number = result.data.flight_number
```

在终端中启动 MCP 服务器。

[![](https://cdn.thenewstack.io/media/2025/08/6f10f4fd-mcp-1-1024x894.png)](https://cdn.thenewstack.io/media/2025/08/6f10f4fd-mcp-1-1024x894.png)

## 步骤 3：调用客户端

以下是带有Elicitation的 MCP 客户端的代码：

```py
# client.py
import asyncio
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult
from google import genai
from google.genai import types


async def send_to_gemini(flight_status_result: str, user_query: str = None):
 """Send flight status result to Gemini for analysis."""
 try:
 gemini_client = genai.Client()
 
 # Use the user query if provided, otherwise create a default prompt
 if user_query:
 prompt = f"{user_query}\n\nFlight Status Data:\n{flight_status_result}"
 else:
 prompt = f"Please analyze this flight status information and provide insights:\n\n{flight_status_result}"
 
 response = gemini_client.models.generate_content(
 model="gemini-2.5-flash",
 contents=prompt
        )
 
 return response.text
 
 except Exception as e:
 return f"Error sending to Gemini: {e}"


async def elicitation_handler(message: str, response_type: type, params, context):
 print(f"Server asks: {message}")
 
 try:
 flight_number = input("Enter flight number (e.g., AA123, UA456): ")
 if not flight_number.strip():
 print("No flight number provided")
 return ElicitResult(action="decline")
 return response_type(flight_number=flight_number.strip())
 
 except KeyboardInterrupt:
 print("\nOperation cancelled by user")
 return ElicitResult(action="cancel")
 except Exception as e:
 print(f"Error handling input: {e}")
 return ElicitResult(action="decline")


async def main():
 client = Client("http://127.0.0.1:8080/mcp/", elicitation_handler=elicitation_handler)
 
 async with client:
 while True:
 print("\nFlight Status Tool with Gemini Analysis")
 print("1. Get flight status")
 print("2. Get flight status with custom Gemini query")
 print("3. Exit")
 
 choice = input("\nSelect an option (1-3): ").strip()
 
 if choice == "1":
 try:
 # Get flight status from MCP server
 result = await client.call_tool("get_flight_status")
 print("\nFlight Status Result:")
 #print(result)
 flight_status_text = result.content[0].text
 print(flight_status_text)
 except Exception as e:
 print(f"Error getting flight status: {e}")
 
 elif choice == "2":
 try:
 # Get custom query from user
 user_query = input("\nEnter your question about the flight (e.g., 'Is this flight likely to be delayed?'): ").strip()
 
 # Get flight status from MCP server
 result = await client.call_tool("get_flight_status")
 print("\nFlight Status Result:")
 print(result)
 
 # Send to Gemini with custom query
 print("\nSending to Gemini with your question...")
 gemini_response = await send_to_gemini(result, user_query)
 print("\nGemini Analysis:")
 print(gemini_response)
 
 except Exception as e:
 print(f"Error getting flight status: {e}")
 
 elif choice == "3":
 print("Goodbye!")
 break
 
 else:
 print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
 asyncio.run(main())
```

让我们看看帮助我们在客户端中实现Elicitation的代码片段。

### **定义Elicitation处理程序**

```py
async def elicitation_handler(message: str, response_type: Any) -> Any:
    print(f"Server asks: {message}")
    try:
        flight_number = input("Enter flight number: ").strip()
        if not flight_number:
            return ElicitResult(action="decline")
        return response_type(flight_number=flight_number)
    except KeyboardInterrupt:
        return ElicitResult(action="cancel")
```

当服务器调用 ctx.elicit 时，此函数运行。它打印服务器的提示，捕获用户输入，并返回结构化响应或操作（例如，拒绝或取消）。

### **向客户端注册处理程序**

```
client = Client(
    base_url="http://localhost:8000/mcp",
    elicitation_handler=elicitation_handler
)
```

客户端使用附加的Elicitation处理程序进行实例化。这使其能够在服务器触发Elicitation请求时自动响应。

### **在交互循环中使用处理程序**

```
result = await client.call_tool("get_flight_status", {})
print("Result from server:", result)
```

当客户端调用该工具时，服务器启动的任何Elicitation都会通过注册的处理程序进行路由。仅在Elicitation过程完成后才显示最终的工具结果。

在新终端窗口中启动 MCP 客户端。

[![](https://cdn.thenewstack.io/media/2025/08/ac7fe651-mcp-2-1024x289.png)](https://cdn.thenewstack.io/media/2025/08/ac7fe651-mcp-2-1024x289.png)

选择第一个选项时，您将看到来自工具的原始响应。第二个选项将提示以及工具输出（上下文）发送到 Gemini 进行分析和详细响应。

我希望您发现本教程在调用 MCP 工具时实现[人在循环中](https://thenewstack.io/human-on-the-loop-the-new-ai-control-model-that-actually-works/)有所帮助。