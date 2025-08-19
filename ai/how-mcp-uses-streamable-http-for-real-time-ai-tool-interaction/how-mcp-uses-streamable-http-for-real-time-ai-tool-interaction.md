
<!--
title: MCP利用流式HTTP实现实时AI工具交互
cover: https://cdn.thenewstack.io/media/2025/08/d4d612fa-ales-krivec-mflfmxgeeay-unsplashb.jpg
summary: 模型上下文协议(MCP)的流式HTTP通过Web实时传输数据，支持AI代理与Web服务交互。它使用单端点和SSE，简化了实现并保持了与现有Web基础设施的兼容性，同时增强了可靠性和效率。
-->

模型上下文协议(MCP)的流式HTTP通过Web实时传输数据，支持AI代理与Web服务交互。它使用单端点和SSE，简化了实现并保持了与现有Web基础设施的兼容性，同时增强了可靠性和效率。

> 译自：[How MCP Uses Streamable HTTP for Real-Time AI Tool Interaction](https://thenewstack.io/how-mcp-uses-streamable-http-for-real-time-ai-tool-interaction/)
> 
> 作者：Janakiram MSV

[模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) 是一种开放标准，用于连接 AI 模型（客户端）与外部工具和数据源（服务器）。对于本地集成，MCP 可以使用简单的 STDIO（标准输入/输出）传输，但对于联网（远程）工具，它依赖于基于 HTTP 的通信。

[流式 HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) 是 MCP 中引入的现代 HTTP 传输，用于处理客户端和服务器之间的流式交互。它于 2025 年初发布，是早期 HTTP+SSE 方法的演变，解决了它的缺点。本质上，流式 HTTP 允许 MCP 通过 Web 以连续的实时流发送和接收数据，而不是仅仅一个请求后跟一个响应。这种新的传输方式支持远程 MCP 服务器（有时称为“远程”工具），并使 AI 代理能够以流畅的交互方式与 Web 服务进行交互。

在本文中，我们将通过一个实际的例子来更详细地了解流式 HTTP。我们将构建一个简单的 MCP 服务器和客户端来分析两者之间的通信。

## 什么是流式 HTTP？

流式 HTTP 是一种基于 HTTP 的通信机制，它支持在单个 HTTP 连接上进行流式响应和双向交互。

简单来说，MCP 客户端通过 HTTP POST 向服务器发送请求，服务器可以使用正常的单个 JSON 消息进行响应，也可以通过启动实时事件流（使用服务器发送事件，SSE）来及时发回多个消息。服务器公开一个统一的 HTTP 端点（例如 `https://example.com/mcp`），该端点接受 POST 请求（用于发送命令）和 GET 请求（用于建立监听流）。

这种单端点设计是一个核心功能 - 所有通信都通过一个 URL 进行 - 与旧的多端点方案相比，它简化了实现。

在底层，流式 HTTP 仍然使用标准的 HTTP 协议（POST、GET）和 SSE，因此它与现有的 Web 基础设施（代理、负载均衡器等）保持兼容，同时支持长时间的数据流。

简而言之，流式 HTTP 是一种机制，允许 MCP 以受控方式通过 HTTP 传输数据流，并在需要时使用 SSE 传递连续的服务器消息。

## 客户端-服务器交互的顺序分析

为了充分理解流式 HTTP 传输的机制，必须从理论概念转向对通信会话的实际顺序分析。以下部分提供了对实际客户端-服务器交互的逐步分解，说明了从会话建立到终止的整个协议生命周期。每个阶段都通过服务器的 HTTP 级别响应进行检查，阐明了每个请求的角色和重要性。

下面是一个简单的 MCP 服务器，它将 Python 列表公开为一个工具：

```
from fastmcp import FastMCP


mcp = FastMCP("Employee Server")


@mcp.tool()
def get_employees() -> list:
 return [
        {"id": 1, "name": "Alice", "role": "Engineer"},
        {"id": 2, "name": "Bob", "role": "Designer"},
        {"id": 3, "name": "Charlie", "role": "Manager"},
        {"id": 4, "name": "Diana", "role": "Analyst"},
        {"id": 5, "name": "Eve", "role": "Intern"},
    ]


if __name__ == "__main__":
 mcp.run(transport="streamable-http", host="127.0.0.1", port=8080, path="/mcp/")
```

我们将从一个客户端调用此服务器，该客户端使用 Google Gemini 对 MCP 的原生支持。代码如下所示：

```
import os
import asyncio
from google import genai
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


import warnings
warnings.filterwarnings("ignore")


MCP_SERVER_URL = "http://127.0.0.1:8080/mcp/"
client = genai.Client()


async def main():
 async with streamablehttp_client(MCP_SERVER_URL) as (read, write, _):
 async with ClientSession(read, write) as session:
 await session.initialize()
 prompt = "Who is the Intern in the company?"
 response = await client.aio.models.generate_content(
 model="gemini-2.5-flash",
 contents=prompt,
 config=genai.types.GenerateContentConfig(
 temperature=0,
 tools=[session],  # Pass the MCP session as a tool
                ),
            )
 print(response.text)


if __name__ == "__main__":
 asyncio.run(main())
```

请注意，我们如何将客户端会话作为工具传递给 Gemini API。

当我们运行服务器和客户端时，我们在服务器控制台上看到以下日志。

[![](https://cdn.thenewstack.io/media/2025/08/5fec1c98-mcp_server_logs-1024x339.png)](https://cdn.thenewstack.io/media/2025/08/5fec1c98-mcp_server_logs-1024x339.png)

让我们检查客户端向服务器发出的每个请求。

### 第 1 阶段：初始化和会话建立

MCP 会话的整个生命周期都从客户端发出的单个基础请求开始。这是初始化阶段，客户端和服务器在此阶段建立共享上下文，协商协议功能，并创建将用于所有后续通信的会话标识符。

日志条目：`POST /mcp HTTP/1.1 200 OK`

该过程在客户端向指定的 MCP 端点发送 HTTP POST 请求时启动，我们将假设该端点是 /mcp。此 POST 请求的主体包含带有方法 initialize 的 JSON-RPC 消息。此消息携带有关客户端功能和所需协议版本的信息。

服务器在接收并成功处理此请求后，会以 HTTP 200 OK 状态代码进行响应。此响应的 Content-Type 标头是 application/json，因为初始化结果是单个同步对象。但是，此响应的最关键部分不在正文中，而是在标头中。服务器包含一个新标头 Mcp-Session-Id，其中包含一个唯一值（例如，Mcp-Session-Id: session-a4b1-c8d3-e5f6）。此标识符是整个会话状态的基础。客户端必须捕获此 ID 并将其包含在所有未来的请求中，以保持会话的上下文。

发送带有空主体的 202 Accepted 响应用作轻量级确认。它向客户端确认服务器已收到并接受了通知以进行处理。这比发送带有完整 JSON 响应正文的 200 OK 更有效，后者专用于产生结果的请求。

响应的主体包含 InitializeResult JSON-RPC 对象。此对象确认成功设置并详细说明服务器的功能，例如它提供的工具和资源，并确认将用于会话的协议版本。在此交换之后，已成功建立有状态会话。

### 第 2 阶段：建立公告通道

现在会话已激活，客户端可以选择打开辅助通信通道以进行服务器启动的消息。此步骤是可选的，但通常由功能齐全的客户端执行，以启用更具交互性和动态性的工作流程。

日志条目：`GET /mcp HTTP/1.1 200 OK`

在成功初始化之后，客户端立即向同一个 /mcp 端点发出 HTTP GET 请求。这不是匿名请求；为了将这个新的、长期存在的连接与刚刚创建的会话相关联，客户端必须包含在上一步中收到的 Mcp-Session-Id: session-a4b1-c8d3-e5f6 标头。该请求还必须包含 Accept: text/event-stream 标头以表明其目的。

服务器识别到有效的会话 ID，并以 HTTP 200 OK 和 Content-Type: text/event-stream 标头进行响应。此响应不会终止。TCP 连接无限期地保持打开状态，从而建立持久的公告通道。从这一点开始，服务器可以随时使用此打开的连接将 JSON-RPC 请求或通知推送到客户端，完全独立于客户端在命令通道上的自身操作。

### 第 3 阶段：客户端启动的带有流式响应的请求

此阶段演示了流式 HTTP 传输的核心优势：处理长时间运行的任务，并提供实时进度更新，所有这些都在单个事务范围内完成。

日志条目 1：`POST /mcp HTTP/1.1 200 OK`（带有 `Content-Type: text/event-stream` 响应）

客户端现在希望执行一项任务，例如运行数据分析脚本。它向 /mcp 端点发送一个新的 HTTP POST 请求。主体包含相关的 JSON-RPC 请求，例如 {“jsonrpc”: “2.0”, “id”: 1, “method”: “tools/execute”, “params”: {…}}。至关重要的是，此请求包含 Mcp-Session-Id 标头以保持会话上下文。

服务器收到此请求并将其识别为长时间运行的操作。它没有等待整个任务完成，而是立即以 HTTP 200 OK 状态代码和 Content-Type: text/event-stream 标头进行响应。此操作保持此特定 POST 请求的连接打开，将其响应正文转换为专用的 SSE 流。

脚本完成执行后，服务器会构造最终的 JSON-RPC 响应对象，其中包括原始请求 ID（例如，{“jsonrpc”: “2.0”, “id”: 1, “result”: {…}}）。此最终结果作为 POST 响应流上的最后一个 SSE 事件发送。在发送此结束消息后，服务器应立即关闭此特定的 SSE 流。此操作完成此 POST 请求的 HTTP 事务。客户端现在已收到所有进度更新和最终结果，所有这些都整齐地限定在启动该任务的请求的范围内。

### 第 4 阶段：服务器启动的通知

此阶段说明了两个通道的独立性。当第 3 阶段中长时间运行的 POST 事务正在进行时，服务器仍然可以与客户端通信有关不相关的事项。

日志条目（概念）：服务器在长期存在的 GET 连接上发送 SSE 数据：块。

假设在数据分析运行时，系统管理员向服务器添加了一个新工具。服务器可以决定通知所有连接的客户端此更新。它构造一个 JSON-RPC 通知（例如，{“jsonrpc”: “2.0”, “method”: “tools/didChange”, “params”: {…}}）并将其作为 SSE 事件发送。但是，它不会在第 3 阶段中从活动的 POST 响应流上发送此通知。相反，它通过第 2 阶段中建立的持久 GET 连接发送它。这演示了“公告通道”的实际运行，传递一个会话范围的常规通知，该通知完全独立于任何特定的客户端启动的命令。

### 第 5 阶段：连接恢复（假设情况）

针对网络故障的稳健性是该协议的关键设计目标。此假设场景演示了连接恢复的内置机制。

由于瞬时网络问题，客户端的长期存在的 GET 连接（公告通道）断开。从该流成功处理的最后一个事件 ID 是 event-id-42。

日志条目：`GET /mcp HTTP/1.1 200 OK`（带有 Last-Event-ID 标头）

客户端的网络库检测到 GET 流的断开连接。要恢复，它立即向 /mcp 端点发出一个新的 HTTP GET 请求。此请求包括两个重要的标头：Mcp-Session-Id 标头，用于与正确的会话重新关联，以及 Last-Event-ID: event-id-42 标头。

Last-Event-ID 标头是无损恢复的关键。服务器收到此请求，使用会话 ID 查找会话的状态和消息历史记录，并使用事件 ID 作为游标。然后，它会重播在旧流上在 event-id-42 之后发送的客户端可能错过的任何消息。一旦客户端赶上，服务器将恢复发送实时消息，从而无缝恢复公告通道，而不会丢失任何数据。此精确机制也可以应用于可恢复的 POST 响应流。

这种分层状态方法是实现这种弹性的原因。HTTP 本身是无状态的，但协议通过两层强制实现状态。Mcp-Session-Id 标头在应用层创建一个持久的逻辑会话状态，将原本独立的 HTTP 请求链接到连贯的对话中。用于 GET 流或流式 POST 响应的开放 HTTP 连接提供短暂的传输级别流状态。协议的稳健性直接源于其在发生中断时使用持久的应用状态重建短暂的传输状态的能力。

### 第 6 阶段：会话终止

生命周期的最后阶段是干净且显式的会话终止，允许服务器释放它正在持有的任何资源。

日志条目：`DELETE /mcp HTTP/1.1 200 OK`

客户端完成所有任务后，它会向 /mcp 端点发送 HTTP DELETE 请求。要指定要终止的会话，该请求必须包括 Mcp-Session-Id: session-a4b1-c8d3-e5f6 标头。

服务器收到此请求，验证会话 ID，然后开始关闭会话。这包括清除存储在内存中的任何会话状态，关闭公告通道的持久 GET 连接，并使会话 ID 失效。为了确认操作成功，服务器会以 HTTP 200 OK 状态代码进行响应，正式结束通信生命周期。

## 结论

流式 HTTP 是 MCP 的基础组成部分，它使 AI 代理能够以丰富且交互的方式通过互联网连接到工具。通过扩展 HTTP 以使其对流友好，并使用 SSE 进行持续更新，它为需要流式传输输出、处理长时间运行的任务以及实时保持同步的 AI 系统提供了所需的灵活性。

与传统的 HTTP 请求-响应模型不同，流式 HTTP 保持对话的活跃：AI 代理可以要求工具执行某些操作并立即开始接收答案或更新，并且该工具甚至可以在同一通信线路上反问问题或发送警报。这种方法显着提高了 MCP 的可靠性（在断开连接时恢复会话）和效率（无需不必要的永久在线连接），同时保持与 Web 标准的兼容性。

在实践中，流式 HTTP 使编码助手可以运行远程构建工具并流式传输实时日志，或者数据分析代理可以查询数据库并随着结果的到来逐步返回结果。它将 HTTP 的简单性与流式传输的强大功能相结合，通过为 AI 和世界之间流式传输上下文和数据提供统一、强大的接口，实现了 MCP“AI 工具的 USB-C”的承诺。