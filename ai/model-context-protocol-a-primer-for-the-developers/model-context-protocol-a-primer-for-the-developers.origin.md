# Model Context Protocol: A Primer for the Developers
![Featued image for: Model Context Protocol: A Primer for the Developers](https://cdn.thenewstack.io/media/2025/04/57146db4-mcp-1024x683.png)
The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is on its way to becoming the gold standard for integrating external resources into [agentic workflows](https://thenewstack.io/agentic-ai-is-the-next-frontier-in-enterprise-operations/). While developers can use large language model (LLM)-specific mechanisms to incorporate tools, MCP is fast becoming the REST equivalent of integration.

This series introduces Python developers to the fundamentals of MCP and its architecture. I will start with MCP’s motivation and high-level architecture, followed by a detailed, hands-on implementation of servers and clients.

## What Is Model Context Protocol?
[Announced](https://www.anthropic.com/news/model-context-protocol) in November 2024, Anthropic’s MCP is an [open standard](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) designed to [streamline how AI models](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) interact with external tools, data sources and resources.
Anthropic introduces MCP as a universal connector of tools to LLMs. It compares it to how USB-C standardizes hardware connections, allowing developers to integrate any tool or data source with their AI applications through a single protocol. By adopting a language-agnostic approach and providing SDKs for Python, TypeScript, Java, Kotlin and C#, MCP eliminates the need for custom, one-off integrations.

MCP operates through two main components: servers, which expose tools, resources and prompts, and clients, which connect AI models to these servers. Communication is handled via [JSON-RPC](https://www.jsonrpc.org/) over HTTP, supporting synchronous and asynchronous workflows. Security is integral, with explicit permissions and local-first design ensuring privacy. MCP is already supported by major AI platforms and fosters rapid ecosystem growth, making it a foundational technology for building robust, context-aware AI agents.

[LangChain](https://github.com/langchain-ai/langchain-mcp-adapters), [OpenAI Agent SDK](https://openai.github.io/openai-agents-python/mcp/), [Google Agent Developer Kit](https://google.github.io/adk-docs/tools/mcp-tools/) and [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/introducing-model-context-protocol-mcp-in-copilot-studio-simplified-integration-with-ai-apps-and-agents/) are some of the frameworks and platforms that natively support MCP.
## A Closer Look at MCP Servers and MCP Clients
[Agentic workflows](https://thenewstack.io/agentic-ai-is-the-new-web-app-and-your-ai-strategy-must-evolve/) require two essential elements to operate autonomously: up-to-date data and access to existing systems. Data is fed as context to LLMs to provide factual information, which helps LLMs make decisions. Once a decision is made to take action, they need programmatic access to systems, which are typically exposed as APIs that become available as tools.
Interestingly, MCP servers and clients can operate without any dependencies on an LLM. When the client is integrated with an LLM, it forms the foundation of agentic workflows.

In the MCP architecture, the servers abstract the access to data and tools. For example, a database can be a part of an MCP server as a resource. A client has read-only access to this resource to fetch data. Resources also support parameters to apply filters or limit the data shared with the clients. For example, employee payroll information is an ideal candidate for a resource.

Additionally, MCP servers also expose tools that enable clients to perform actions that go beyond fetching the data. While resources enable read-only access, tools support calling an API that manipulates data or takes an action. For example, invoking the Stripe API to complete a payment transaction is a great candidate for a tool.

Apart from resources and tools, MCP servers can also act as a hub for predefined prompts. Clients can retrieve these prompts and send them to LLMs. This enables a consistent and standard repository of prompts.

MCP servers can be queried to retrieve the list of resources, tools and prompts they expose. This acts as a basic discovery mechanism. To summarize, MCP servers can expose resources, tools and prompts to the clients. What the client does is left to the imagination of the developer.

An MCP client lives within a host application, a chatbot or an agent. Typical examples of a host application are [Claude Desktop](https://claude.ai/download) and [Cursor AI](https://www.cursor.com/). Developers can create an agentic application with multiple clients interacting with one or more MCP servers.

We can create an MCP client that doesn’t talk to an LLM. However, the client can become a powerful conduit for LLMs to access MCP servers.

In a typical workflow, a host application, such as a chatbot or an agent, connects with the MCP server, retrieves the available resources and tools, and passes them to an LLM in an expected format.

Based on the prompt, the LLM may revert to the host to access the resource or invoke the tool through the MCP client. Most agentic frameworks, such as OpenAI Agents SDK and Google ADK, abstract this functionality by making the round trip between the LLM and host application transparent.

## The Communication Between the MCP Server and the MCP Client
The most crucial aspect of MCP architecture is the communication protocol. An MCP server supports two transport protocols: [STDI](https://mcp-framework.com/docs/Transports/stdio-transport/)[O](https://mcp-framework.com/docs/Transports/stdio-transport/) and [SSE](https://mcp-framework.com/docs/Transports/sse).

The first choice is straightforward and is obvious to many developers. Imagine invoking a command-line tool by passing a few parameters and copying and pasting the output in the chatbot window as a part of the prompt.

When using STDIO as a transport protocol, an MCP client directly invokes the MCP server and passes the required parameters. It then captures the output from the server, which is written to the console, and passes it to the host application.

In this scenario, the client and server share the same process. The server will simply execute the command and exit immediately. This repeats each time the client invokes the server. Essentially, the client and server run in-process without involving any remote call or RPC. This works best when the client and server are on the same machine, and no latency is involved due to long-running processes. The bottom line is that the MCP server and client share a 1:1 connection when using STDIO transport.

The second transport protocol that MCP supports is server-sent events (SSE). It enables a server to push real-time updates to clients over a single, long-lived HTTP connection. Once the client initiates the connection, the server streams data as events occur, eliminating the need for repeated polling. This approach is particularly effective for applications like live news feeds or notifications, where updates flow primarily from server to client.

Compared to REST, SSE provides lower latency and greater efficiency, as REST requires clients to repeatedly poll the server for new data, increasing overhead and latency. SSE also offers automatic reconnection and works seamlessly with most firewalls, making it more robust for real-time scenarios.

MCP uses SSE instead of [WebSockets](https://thenewstack.io/the-challenge-of-scaling-websockets/) for remote communication primarily because SSE offers a simpler and more robust solution for scenarios where only server-to-client streaming is required. SSE operates over standard HTTP, making it easier to work with firewalls and restricted networks. It also allows the server to push real-time updates to the client without the complexity of managing a full-duplex WebSocket connection.

In MCP, client-to-server communication is handled with HTTP POST requests, while SSE handles streaming updates from the server to the client, which matches the typical interaction pattern for AI tools and resource notifications. This approach reduces overhead, simplifies implementation, and improves compatibility with existing infrastructure, especially compared to the bidirectional and often more complex WebSocket protocol.

While SSE is the communication technique, JSON-RPC is the wire protocol used by MCP. JSON-RPC is a lightweight, stateless protocol designed for remote procedure calls, making it ideal for the fast, dynamic exchanges required in AI workflows.

Within MCP, every interaction — such as invoking a tool, fetching data or listing available capabilities — is encoded as a JSON-RPC message, which includes a method name, parameters and an identifier for tracking responses. This approach allows MCP clients and servers to communicate seamlessly, regardless of their underlying implementation language, and ensures that all requests, responses and notifications follow a predictable, interoperable format. By building on JSON-RPC, MCP simplifies integration, supports error handling and allows developers to create flexible, composable agentic workflows that can interact with various external tools and resources.

Unlike STDIO transport protocol, SSE can support multiple clients concurrently served by a single MCP server. This is useful when MCP servers are hosted remotely in environments such as Platform as a Service (PaaS) and serverless runtimes.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)