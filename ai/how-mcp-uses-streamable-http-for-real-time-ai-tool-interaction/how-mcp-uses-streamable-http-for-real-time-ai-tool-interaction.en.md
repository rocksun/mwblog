The [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) is an open standard that connects AI models (clients) with external tools and data sources (servers). For local integrations, MCP can use a simple STDIO (standard input/output) transport, but for networked (remote) tools, it relies on HTTP-based communication.

[Streamable HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) is the modern HTTP transport introduced in MCP to handle streaming interactions between clients and servers. It was released in early 2025 as an evolution of the earlier HTTP+SSE approach, addressing its shortcomings. In essence, Streamable HTTP allows MCP to send and receive data over the web in a continuous, real-time stream — rather than just one request followed by one response. This new transport underpins remote MCP servers (sometimes called “remote” tools) and makes it easier for AI agents to interact with web services in a fluid, interactive way.

In this article, we will take a closer look at Streamable HTTP through a practical example. We will build a simple MCP server and client to analyze the communication between the two.

## What Is Streamable HTTP?

Streamable HTTP is an HTTP-based communication mechanism that supports streaming responses and bidirectional interaction on a single HTTP connection.

In simple terms, the MCP client sends requests to the server via HTTP POST, and the server can respond either with a normal single JSON message or by initiating a live event stream (using Server-Sent Events, SSE) to send back multiple messages over time. The server exposes one unified HTTP endpoint (e.g. `https://example.com/mcp`) which accepts both POST requests (for sending commands) and GET requests (for establishing a listening stream).

This single-endpoint design is a core feature — all communication happens through one URL — which simplifies implementation compared to older multi-endpoint schemes.

Under the hood, Streamable HTTP still uses standard HTTP protocols (POST, GET) and SSE, so it remains compatible with existing web infrastructure (proxies, load balancers, etc.) while enabling long-lived streams of data.

In short, Streamable HTTP is the mechanism that allows MCP to stream data over HTTP in a controlled way, using SSE to deliver continuous server messages when needed.

## A Sequential Analysis of the Client-Server Interaction

To fully understand the mechanics of the Streamable HTTP transport, it is essential to move from theoretical concepts to a practical, sequential analysis of a communication session. The following sections provide a step-by-step breakdown of a realistic client-server interaction, illustrating the entire protocol lifecycle from session establishment to termination. Each phase is examined through the lens of the server’s HTTP-level responses, clarifying the role and significance of each request.

Below is a simple MCP server that exposes a Python list as a tool:

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

We will invoke this server from a client that uses Google Gemini’s native support for MCP. The code is shown below:

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

Notice how we pass the client session as a tool to the Gemini API.

When we run the server and client, we see the following logs on the server console.

[![](https://cdn.thenewstack.io/media/2025/08/5fec1c98-mcp_server_logs-1024x339.png)](https://cdn.thenewstack.io/media/2025/08/5fec1c98-mcp_server_logs-1024x339.png)

Let’s examine each request the client makes to the server.

### Phase 1: Initialization and Session Establishment

The entire lifecycle of an MCP session begins with a single, foundational request from the client. This is the initialization phase, where the client and server establish a shared context, negotiate protocol capabilities, and create the session identifier that will be used for all subsequent communication.

Log Entry: `POST /mcp HTTP/1.1 200 OK`

The process is initiated when the client sends an HTTP POST request to the designated MCP endpoint, which we will assume is /mcp. The body of this POST request contains a JSON-RPC message with the method initialize. This message carries information about the client’s capabilities and the desired protocol version.

The server, upon receiving and successfully processing this request, responds with an HTTP 200 OK status code. The Content-Type header of this response is application/json, as the initialization result is a single, synchronous object. The most critical part of this response, however, is not in the body but in the headers. The server includes a new header, Mcp-Session-Id, with a unique value (e.g., Mcp-Session-Id: session-a4b1-c8d3-e5f6). This identifier is the cornerstone of statefulness for the entire session. The client must capture this ID and include it in all future requests to maintain the session’s context.

The 202 Accepted response, which is sent with an empty body, serves as a lightweight acknowledgment. It confirms to the client that the server has received and accepted the notification for processing. This is more efficient than sending a 200 OK with a full JSON response body, which is reserved for requests that produce a result.

The body of the response contains the InitializeResult JSON-RPC object. This object confirms the successful setup and details the server’s capabilities, such as the tools and resources it offers, and confirms the protocol version that will be used for the session. After this exchange, a stateful session has been successfully established.

### Phase 2: Establishing the Announcement Channel

With the session now active, the client can opt to open the secondary communication channel for server-initiated messages. This step is optional but is typically performed by full-featured clients to enable more interactive and dynamic workflows.

Log Entry: `GET /mcp HTTP/1.1 200 OK`

Immediately following a successful initialization, the client issues an HTTP GET request to the very same /mcp endpoint. This is not an anonymous request; to associate this new, long-lived connection with the session just created, the client must include the Mcp-Session-Id: session-a4b1-c8d3-e5f6 header received in the previous step. The request must also include the Accept: text/event-stream header to signal its purpose.

The server, recognizing the valid session ID, responds with HTTP 200 OK and a Content-Type: text/event-stream header. This response does not terminate. The TCP connection is held open indefinitely, establishing the persistent Announcement Channel. From this point forward, the server can use this open connection to push JSON-RPC requests or notifications to the client at any time, completely independent of the client’s own actions on the Command Channel.

### Phase 3: Client-Initiated Request with Streaming Response

This phase demonstrates the core power of the Streamable HTTP transport: handling a long-running task with real-time progress updates, all within a single, transaction-scoped interaction.

Log Entry 1: `POST /mcp HTTP/1.1 200 OK` (with `Content-Type: text/event-stream` response)

The client now wishes to execute a task, such as running a data analysis script. It sends a new HTTP POST request to the /mcp endpoint. The body contains the relevant JSON-RPC request, such as {“jsonrpc”: “2.0”, “id”: 1, “method”: “tools/execute”, “params”: {…}}. Crucially, this request includes the Mcp-Session-Id header to maintain the session context.

The server receives this request and identifies it as a long-running operation. Instead of waiting for the entire task to complete, it immediately responds with an HTTP 200 OK status code and a Content-Type: text/event-stream header. This action keeps the connection for this specific POST request open, turning its response body into a dedicated SSE stream.

Once the script finishes its execution, the server constructs the final JSON-RPC response object, which includes the original request ID (e.g., {“jsonrpc”: “2.0”, “id”: 1, “result”: {…}}). This final result is sent as the last SSE event on the POST response stream. Immediately after sending this concluding message, the server should close this specific SSE stream. This action completes the HTTP transaction for this POST request. The client has now received all progress updates and the final result, all neatly scoped to the request that initiated the task.

### Phase 4: Server-Initiated Notification

This phase illustrates the independence of the two channels. While the long-running POST transaction from Phase 3 is in progress, the server can still communicate with the client about unrelated matters.

Log Entry (Conceptual): Server sends an SSE data: chunk on the long-lived GET connection.

Suppose that while the data analysis is running, a system administrator adds a new tool to the server. The server can decide to inform all connected clients of this update. It constructs a JSON-RPC notification (e.g., {“jsonrpc”: “2.0”, “method”: “tools/didChange”, “params”: {…}}) and sends it as an SSE event. However, it does not send this on the active POST response stream from Phase 3. Instead, it sends it over the persistent GET connection that was established in Phase 2. This demonstrates the “announcement channel” in action, delivering a session-scoped, general notification that is completely decoupled from any specific client-initiated command.

### Phase 5: Connection Resumption (Hypothetical Scenario)

Robustness against network failure is a key design goal of the protocol. This hypothetical scenario demonstrates the built-in mechanism for connection resumption.

The client’s long-lived GET connection (the Announcement Channel) drops due to a transient network issue. The last event ID successfully processed from that stream was event-id-42.

Log Entry: `GET /mcp HTTP/1.1 200 OK` (with Last-Event-ID header)

The client’s networking library detects the disconnection of the GET stream. To recover, it immediately issues a new HTTP GET request to the /mcp endpoint. This request includes two vital headers: the Mcp-Session-Id header to re-associate with the correct session, and the Last-Event-ID: event-id-42 header.

The Last-Event-ID header is the key to lossless recovery. The server receives this request, uses the session ID to locate the session’s state and message history, and uses the event ID as a cursor. It then replays any messages that were sent on the old stream after event-id-42 that the client may have missed. Once the client is caught up, the server resumes sending live messages, seamlessly restoring the Announcement Channel without any loss of data. This exact mechanism can be applied to resumable POST response streams as well.

This layered approach to the state is what enables such resilience. HTTP itself is stateless, but the protocol imposes statefulness through two layers. The Mcp-Session-Id header creates a durable, logical session state at the application layer, linking otherwise independent HTTP requests into a coherent conversation. The open HTTP connections for the GET stream or a streaming POST response provide the ephemeral, transport-level stream state. The protocol’s robustness stems directly from its ability to rebuild the ephemeral transport state using the durable application state whenever a disruption occurs.

### Phase 6: Session Termination

The final phase of the lifecycle is the clean and explicit termination of the session, allowing the server to release any resources it was holding.

Log Entry: `DELETE /mcp HTTP/1.1 200 OK`

Once the client has completed all its tasks, it sends an HTTP DELETE request to the /mcp endpoint. To specify which session to terminate, the request MUST include the Mcp-Session-Id: session-a4b1-c8d3-e5f6 header.

The server receives this request, validates the session ID, and proceeds to tear down the session. This involves cleaning up any session state stored in memory, closing the persistent GET connection for the Announcement Channel, and invalidating the session ID. To confirm that the operation was successful, the server responds with an HTTP 200 OK status code, formally concluding the communication lifecycle.

## Conclusion

Streamable HTTP is a foundational piece of MCP’s ability to connect AI agents with tools over the internet in a rich, interactive manner. By extending HTTP to be stream-friendly and by using SSE for continuous updates, it provides the flexibility required for AI systems that need to stream outputs, handle long-running tasks, and stay in sync in real-time.

Unlike the traditional HTTP request-response model, Streamable HTTP keeps the conversation alive: an AI agent can ask a tool to do something and start receiving answers or updates immediately, and the tool can even ask questions back or send alerts on the same line of communication. This approach markedly improves reliability (with session resume on drops) and efficiency (no needless always-on connections) for MCP, while remaining compatible with web standards.

In practice, Streamable HTTP makes it feasible for a coding assistant to run a remote build tool and stream back live logs, or for a data analysis agent to query a database and return results gradually as they come. It marries the simplicity of HTTP with the power of streaming, fulfilling MCP’s promise of a “USB-C for AI tools” by providing a unified, robust interface for streaming context and data between AI and the world.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)