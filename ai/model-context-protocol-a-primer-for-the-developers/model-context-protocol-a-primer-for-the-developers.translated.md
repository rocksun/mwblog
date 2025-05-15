# 模型上下文协议：开发者入门指南

![模型上下文协议：开发者入门指南的特色图片](https://cdn.thenewstack.io/media/2025/04/57146db4-mcp-1024x683.png)

[模型上下文协议](https://modelcontextprotocol.io/introduction) (MCP) 正逐渐成为将外部资源集成到[自主工作流](https://thenewstack.io/agentic-ai-is-the-next-frontier-in-enterprise-operations/)中的黄金标准。虽然开发者可以使用特定于大型语言模型 (LLM) 的机制来集成工具，但 MCP 正迅速成为集成的 REST 等效项。

本系列向 Python 开发者介绍 MCP 的基本原理及其架构。我将从 MCP 的动机和高级架构开始，然后详细介绍服务器和客户端的实践实现。

## 什么是模型上下文协议？

Anthropic 于 2024 年 11 月[宣布](https://www.anthropic.com/news/model-context-protocol)的 MCP 是一种[开放标准](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)，旨在[简化 AI 模型](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/)与外部工具、数据源和资源交互的方式。
Anthropic 将 MCP 引入作为 LLM 的通用工具连接器。它将其比作 USB-C 标准化硬件连接的方式，允许开发者通过单个协议将任何工具或数据源与其 AI 应用程序集成。通过采用与语言无关的方法并为 Python、TypeScript、Java、Kotlin 和 C# 提供 SDK，MCP 消除了对自定义的一次性集成的需求。

MCP 通过两个主要组件运行：服务器，用于公开工具、资源和提示；客户端，用于将 AI 模型连接到这些服务器。通信通过 HTTP 上的 [JSON-RPC](https://www.jsonrpc.org/) 处理，支持同步和异步工作流。安全性是不可或缺的，通过显式权限和本地优先设计确保隐私。MCP 已经得到主要 AI 平台的支持，并促进了快速的生态系统增长，使其成为构建强大的、具有上下文感知能力的 AI Agent 的基础技术。

[LangChain](https://github.com/langchain-ai/langchain-mcp-adapters)、[OpenAI Agent SDK](https://openai.github.io/openai-agents-python/mcp/)、[Google Agent Developer Kit](https://google.github.io/adk-docs/tools/mcp-tools/) 和 [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/introducing-model-context-protocol-mcp-in-copilot-studio-simplified-integration-with-ai-apps-and-agents/) 是原生支持 MCP 的一些框架和平台。

## 深入了解 MCP 服务器和 MCP 客户端

[自主工作流](https://thenewstack.io/agentic-ai-is-the-new-web-app-and-your-ai-strategy-must-evolve/)需要两个基本要素才能自主运行：最新的数据和对现有系统的访问。数据作为上下文提供给 LLM，以提供事实信息，这有助于 LLM 做出决策。一旦做出采取行动的决定，它们就需要对系统的编程访问，这些系统通常作为 API 公开，并作为工具提供。
有趣的是，MCP 服务器和客户端可以在没有任何 LLM 依赖项的情况下运行。当客户端与 LLM 集成时，它构成了自主工作流的基础。

在 MCP 架构中，服务器抽象了对数据和工具的访问。例如，数据库可以作为资源成为 MCP 服务器的一部分。客户端具有对此资源的只读访问权限以获取数据。资源还支持参数以应用过滤器或限制与客户端共享的数据。例如，员工工资单信息是资源的理想选择。

此外，MCP 服务器还公开了工具，使客户端能够执行超出获取数据的操作。虽然资源支持只读访问，但工具支持调用操作数据或采取行动的 API。例如，调用 Stripe API 以完成支付交易是工具的绝佳选择。

除了资源和工具之外，MCP 服务器还可以充当预定义提示的中心。客户端可以检索这些提示并将它们发送到 LLM。这实现了一致且标准的提示存储库。

可以查询 MCP 服务器以检索它们公开的资源、工具和提示的列表。这充当基本的发现机制。总而言之，MCP 服务器可以向客户端公开资源、工具和提示。客户端做什么取决于开发者的想象力。

MCP 客户端位于宿主应用程序、聊天机器人或 Agent 中。宿主应用程序的典型示例是 [Claude Desktop](https://claude.ai/download) 和 [Cursor AI](https://www.cursor.com/)。开发者可以使用与一个或多个 MCP 服务器交互的多个客户端创建一个自主应用程序。
我们可以创建一个不与 LLM 通信的 MCP 客户端。但是，该客户端可以成为 LLM 访问 MCP 服务器的强大管道。

在典型的工作流程中，主机应用程序（例如，聊天机器人或代理）连接到 MCP 服务器，检索可用的资源和工具，并以预期的格式将其传递给 LLM。

基于提示，LLM 可能会返回到主机以访问资源或通过 MCP 客户端调用工具。大多数代理框架（例如 OpenAI Agents SDK 和 Google ADK）通过使 LLM 和主机应用程序之间的往返过程透明化来抽象此功能。

## MCP 服务器和 MCP 客户端之间的通信

MCP 架构最关键的方面是通信协议。MCP 服务器支持两种传输协议：[STDI](https://mcp-framework.com/docs/Transports/stdio-transport/)[O](https://mcp-framework.com/docs/Transports/stdio-transport/) 和 [SSE](https://mcp-framework.com/docs/Transports/sse)。

第一种选择很简单，对许多开发人员来说是显而易见的。想象一下，通过传递几个参数来调用命令行工具，并将输出复制并粘贴到聊天机器人窗口中作为提示的一部分。

当使用 STDIO 作为传输协议时，MCP 客户端直接调用 MCP 服务器并传递所需的参数。然后，它捕获从服务器输出的内容（写入到控制台），并将其传递给主机应用程序。

在这种情况下，客户端和服务器共享同一个进程。服务器将简单地执行命令并立即退出。每次客户端调用服务器时，都会重复此过程。从本质上讲，客户端和服务器在进程内运行，不涉及任何远程调用或 RPC。当客户端和服务器位于同一台机器上，并且由于长时间运行的进程而没有延迟时，这种方式效果最佳。最重要的是，当使用 STDIO 传输时，MCP 服务器和客户端共享 1:1 连接。

MCP 支持的第二种传输协议是服务器发送事件 (SSE)。它使服务器能够通过单个、长期的 HTTP 连接将实时更新推送到客户端。一旦客户端启动连接，服务器就会在事件发生时流式传输数据，从而无需重复轮询。这种方法对于诸如实时新闻提要或通知之类的应用程序特别有效，在这些应用程序中，更新主要从服务器流向客户端。

与 REST 相比，SSE 提供了更低的延迟和更高的效率，因为 REST 需要客户端重复轮询服务器以获取新数据，从而增加了开销和延迟。SSE 还提供自动重新连接，并且可以与大多数防火墙无缝协作，从而使其在实时场景中更加强大。

MCP 使用 SSE 而不是 [WebSockets](https://thenewstack.io/the-challenge-of-scaling-websockets/) 进行远程通信，主要是因为 SSE 为只需要服务器到客户端流式传输的场景提供了更简单、更强大的解决方案。SSE 通过标准 HTTP 运行，从而更易于与防火墙和受限网络配合使用。它还允许服务器将实时更新推送到客户端，而无需管理全双工 WebSocket 连接的复杂性。

在 MCP 中，客户端到服务器的通信通过 HTTP POST 请求处理，而 SSE 处理从服务器到客户端的流式更新，这与 AI 工具和资源通知的典型交互模式相匹配。与双向且通常更复杂的 WebSocket 协议相比，这种方法减少了开销，简化了实现，并提高了与现有基础架构的兼容性。

虽然 SSE 是通信技术，但 JSON-RPC 是 MCP 使用的有线协议。JSON-RPC 是一种轻量级、无状态协议，专为远程过程调用而设计，非常适合 AI 工作流程中所需的快速、动态交换。

在 MCP 中，每个交互（例如，调用工具、获取数据或列出可用功能）都编码为 JSON-RPC 消息，其中包括方法名称、参数和用于跟踪响应的标识符。这种方法允许 MCP 客户端和服务器无缝通信，而不管其底层实现语言如何，并确保所有请求、响应和通知都遵循可预测的、可互操作的格式。通过构建在 JSON-RPC 之上，MCP 简化了集成，支持错误处理，并允许开发人员创建灵活的、可组合的代理工作流程，这些工作流程可以与各种外部工具和资源进行交互。

与 STDIO 传输协议不同，SSE 可以支持由单个 MCP 服务器同时服务的多个客户端。当 MCP 服务器远程托管在平台即服务 (PaaS) 和无服务器运行时等环境中时，这非常有用。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.