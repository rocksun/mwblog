<!--
title: MCP与API网关：不可互换的各自定位
cover: https://cdn.thenewstack.io/media/2025/10/2d9e530c-gateway12.jpg
summary: 传统API网关难以处理有状态的MCP协议，其会话、流式和多路复用等特性需要Agentgateway等专用网关来解决。
-->

传统API网关难以处理有状态的MCP协议，其会话、流式和多路复用等特性需要Agentgateway等专用网关来解决。

> 译自：[MCP vs. API Gateways: They’re Not Interchangeable](https://thenewstack.io/mcp-vs-api-gateways-theyre-not-interchangeable/)
> 
> 作者：Christian Posta

我合作的组织正在迅速采用[模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)，通过[AI 代理](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/)将其服务和数据连接到 AI 模型，但它们遇到了熟悉的挑战：如何在提供路由、速率限制、可观测性和开发者门户的同时，保障对 MCP 服务器和工具的访问安全。

API 早期采用的经验教训让我们痛苦地认识到，当服务在没有适当网关控制的情况下暴露时，会导致安全漏洞、性能灾难和运营混乱。

如果你正在企业中构建和暴露 MCP 服务器，你可能会问我经常听到的那个问题：“我们能直接使用现有的[API 网关](https://thenewstack.io/api-gateway-ingress-controller-or-service-mesh-when-to-use-what-and-why/)来处理 MCP 吗？”

简短的回答是“也许可以”，但真正的问题是：你“应该”这样做吗？API 网关并非为 MCP 用例而构建。事实上，大多数 API 网关供应商最终都会构建专用的 MCP 网关。

让我们探讨一下 API 和 MCP 之间根本的范式差异，以及为什么现有基础设施（API 网关）必须演进。

## API 是无状态的，MCP 是有状态的

在我们深入探讨基础设施应该做什么之前，我们需要了解这两种方法之间明显的区别。API 是“无状态”服务，它们独立地处理每个请求。REST API 大量使用底层传输协议 (HTTP) 来实现协议语义。实际上，这意味着在 API 网关中进行路由、授权和实施策略所需的所有信息都存在于 HTTP 请求头和 URL 结构中。

你的 API 网关可以通过检查以下内容来做出智能决策：

*   **方法** (`GET`, `POST`, `PUT`, `DELETE`)
*   **路径** (`/users/123/orders`)
*   **请求头** (`Authorization: Bearer xyz`, `Content-Type`)
*   **查询参数** (`?limit=10&offset=50`)

API 网关很少对请求体进行操作。如果进行操作，通常是为了进行一些次要转换，或将部分内容提取到请求头或元数据中以用于路由。请求体通常遵循可预测的模式（例如 Open API Spec），可以在需要时使用简单的映射规则进行验证和转换。最重要的是，每个请求都是独立的，调用之间无需维护任何会话状态。

远程 MCP 服务器则完全颠覆了这种模型。首先，MCP 客户端会通过“初始化”消息[连接到 MCP 服务器](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/)并协商各种协议设置。其次，服务器会分配一个会话 ID（例如 `Mcp-Session-Id`），用于协调该客户端的所有后续交互。此会话维护关键上下文/状态，包括：

*   客户端和服务器之间协商的协议能力（哪些可选功能可用）。
*   之前工具调用和响应的工具结果/上下文。
*   异步工具调用状态；流式更新/通知。
*   从服务器到客户端的请求信息状态。

与 REST API 不同，REST API 的每个请求在请求头中都携带着完整的上下文，而 MCP 请求在 HTTP 层中包含最小的路由信息。整个协议都包含在 HTTP 请求体中。一个典型的 MCP 请求如下所示：

```
POST /mcp
Mcp-Session-Id: session_abc123
Content-Type: application/json

{
  "jsonrpc": "2.0", 
  "method": "tools/call",
  "params": { 
    "name": "database_query",
    "arguments": { /* complex nested structure */ }
  },
  "id": "call_456"
}
```

所有有意义的信息都存在于 JSON-RPC 请求体中：方法类型、被调用的特定工具以及参数。HTTP 层只是一个“哑”传输。

更具挑战性的是，MCP 服务器可以通过服务器发送事件 (SSE) 主动向客户端发起通信，发送进度更新、流式结果，甚至新的请求（诱导、采样等）。这种双向、会话感知的通信模式与 API 网关围绕设计的请求-响应模型有着根本性的不同。

## 你能将 API 网关用作 MCP 网关吗？

如我们所见，这两种模型之间存在根本性的差异。但它们也有相似之处，对吗？它们都通过 HTTP。我们可以应用 JWT/令牌/OAuth 风格的安全。而且，API 网关能够对请求体进行操作也并非牵强。那么，你是否能使用现有的[API 网关来管理 MCP 服务](https://thenewstack.io/solocon-explore-service-mesh-api-gateways-graphql-ebpf/)呢？

[![](https://cdn.thenewstack.io/media/2025/10/60cb4d80-image1-1024x141.png)](https://cdn.thenewstack.io/media/2025/10/60cb4d80-image1-1024x141.png)

以下是你的 API 网关可能需要执行的一些功能（非穷尽列表）：

*   解析请求体和响应 (JSON-RPC)，实现协议语义。
*   对请求体中的部分内容（工具列表、工具调用、资源请求等）注入策略决策（允许/拒绝）。
*   来自 MCP 客户端的单个 HTTP POST 可能会导致多个响应以流式（SSE）方式返回。
*   需要一种在流中注入策略执行的方法。
*   一旦流建立，代理从 MCP 服务器到 MCP 客户端的请求。
*   在 MCP 客户端和 MCP 服务器之间进行差异协商。
*   向 MCP 客户端呈现单个逻辑 MCP 服务器（虚拟 MCP 服务器），该逻辑服务器在后端可能由多个 MCP 服务器组成。

API 网关可以完成其中一些功能，所以让我们从简单到复杂，看看常见的 MCP 网关模式：

*   简单直通代理
*   部分协议理解
*   MCP 协商
*   MCP 多路复用

## 简单直通代理

在最基本的层面，你的 API 网关可以作为 MCP 流量的直通代理。在这种场景下，网关将 MCP 请求视为带有 JSON 负载的普通 HTTP POST。它不理解 JSON-RPC 结构或 MCP 语义，但仍然可以提供一些价值：

### **运行良好的方面：**

*   HTTP 级别的认证（API 密钥、OAuth 令牌）
*   每个客户端或 IP 的基本速率限制
*   传输层安全 (TLS) 终止和证书管理
*   请求/响应日志记录和指标

[![](https://cdn.thenewstack.io/media/2025/10/5920c6b1-image3-1024x208.png)](https://cdn.thenewstack.io/media/2025/10/5920c6b1-image3-1024x208.png)

例如，你可能需要检查 HTTP `Authorization` 请求头中是否包含 JWT，并针对可信的 IdP [验证 JWT](https://thenewstack.io/using-jwts-to-authenticate-services-unravels-api-gateways/)。这是基本的 HTTP 处理，任何 API 网关都可以做到。如果响应是 SSE 流会怎样？幸运的是，大多数现代 API 网关也能返回事件流。如果我们想对响应实施一些策略（例如，客户端可以看到哪些工具），那么我们需要理解 SSE 事件。简单的直通代理方法不允许我们这样做。

### **网关在 SSE 方面的局限性：**

*   **没有流式策略执行：** 网关无法检查或过滤单个 SSE 事件。
*   **可观测性有限：** 无法跟踪进度、检测错误或衡量每个事件的延迟。
*   **没有流中授权：** 无法在流进行过程中撤销访问或应用策略。
*   **会话上下文丢失：** 多个 SSE 事件是同一逻辑 MCP 操作的一部分，但网关将其视为独立的块。

想象一下，这就像在数据库前面放置一个通用反向代理。你可以获得连接池和基本监控，但没有查询级别的洞察或策略。一旦你需要理解流经代理的内容，这种方法就已经无法满足需求了。

## 部分协议理解

这就是[事情变得有趣（和复杂）](https://blog.christianposta.com/building-an-mcp-gateway-on-top-of-apigee/)的地方。通过足够的定制开发，你可以让你的 API 网关解析 MCP JSON-RPC 有效负载，并提取有意义的信息用于策略决策。大多数 API 网关通过 JavaScript/Lua/模板策略或类似的脚本机制支持自定义请求体解析。例如，[在 Apigee 中](https://blog.christianposta.com/building-an-mcp-gateway-on-top-of-apigee/)，你可以调用 JavaScript 扩展策略来实现自定义解析和策略。

### **可能实现的功能：**

*   更好地理解 JSON-RPC 请求。
*   应用工具级别的授权（“市场营销用户不能调用 database\_query”）。
*   基本的请求转换和验证。

[![](https://cdn.thenewstack.io/media/2025/10/2b8f9f28-image2-1024x237.png)](https://cdn.thenewstack.io/media/2025/10/2b8f9f28-image2-1024x237.png)

**痛苦的现实是：** 这种方法很快变得脆弱且维护成本高昂：

*   **动态解析复杂性：** MCP 工具列表的工具长度是任意的。你的 JSONPath 表达式会变得越来越复杂和脆弱。
*   **性能开销：** JavaScript 策略比原生网关策略慢。
*   **维护负担：** 每个新的 MCP 工具都可能需要更新网关策略。你的基础设施团队将与你的 MCP 服务器开发紧密耦合。
*   **有限的流式支持：** 尽管某些网关支持 SSE，但在流中应用策略的复杂性呈指数级增长。

实际情况是，你最终会在现有网关之上再构建一个网关，并努力实现新功能或榨取性能提升。

## MCP 协商

MCP 协商涉及网关积极参与 MCP 协议会话，不仅仅是代理请求，还可能根据策略决策修改、过滤或增强请求。例如，一个 MCP 客户端可以用某个版本的 MCP 协议连接到 MCP 网关，而 MCP 网关可以协商/代理到另一个不同的版本。当 MCP 服务器更新到新版协议时，不可能一次性更新所有 MCP 客户端，因此这种能力在企业环境中至关重要。

其他协商用例则建立在先前的模式之上：

*   **版本屏蔽：** 在执行 MCP 服务器升级时，保护 MCP 客户端免受破坏性更改的影响。
*   **请求过滤：** 根据向后兼容性要求从发现响应中移除工具。
*   **响应净化：** 根据用户权限级别从工具响应中去除敏感数据。
*   **上下文注入：** 向工具调用添加企业上下文（用户 ID、租户信息）。
*   **错误处理：** 将 MCP 协议错误转换为符合企业审计要求的事件。

传统的 API 网关在这方面举步维艰，因为它们缺乏原生的 JSON-RPC 理解和会话感知策略引擎。

## MCP 多路复用

这就是传统 API 网关举步维艰的地方。MCP 多路复用涉及将多个后端 MCP 服务器聚合成一个单一的逻辑端点，我们称之为“虚拟 MCP”。

例如，客户端连接到一个 MCP 端点，但实际上可以访问来自多个后端服务器的工具：

*   来自 weather-service.internal 的天气工具
*   来自 analytics-service.internal 的数据库工具
*   来自 notification-service.internal 的电子邮件工具

AI 代理不再需要了解并连接到数十个不同的 MCP 服务器，而是连接到一个虚拟化端点，该端点提供所有企业工具的统一接口。

[![](https://cdn.thenewstack.io/media/2025/10/4fd51832-image4-1024x499.png)](https://cdn.thenewstack.io/media/2025/10/4fd51832-image4-1024x499.png)

**复杂性急剧增加：** 实现这一点需要传统 API 网关根本不具备的功能：

1.  **会话扇出：** 当客户端发送“tools/list”时，网关必须查询所有后端服务器并合并结果。
2.  **请求路由：** 工具调用必须根据工具名称路由到正确的后端。
3.  **响应多路复用：** 必须将来自多个后端的流式响应合并到单个 SSE 流中。
4.  **状态协调：** 必须跨多个后端连接管理会话 ID 和协议协商。
5.  **错误处理：** 单个后端中的故障不应破坏整个虚拟会话。

这种协议感知聚合和虚拟化水平超出了传统 API 网关的设计处理范围。你本质上需要重写网关的核心请求/响应处理逻辑以支持 MCP 会话语义。

## Agentgateway：从头开始为 MCP 构建

[Agentgateway](https://agentgateway.dev/) 是一个开源的 Linux 基金会项目，它吸取了构建 API 网关的经验教训，专门用 Rust 为 MCP 等 AI 代理协议构建。与针对无状态 REST 交互进行优化的传统 API 网关不同，agentgateway 原生理解 JSON-RPC 消息结构，维护有状态会话映射，并处理 MCP 固有的双向通信模式。

这种深入的协议感知能力使其能够正确地多路复用和解复用 MCP 会话，将客户端请求扇出到多个后端 MCP 服务器，聚合工具列表，并维护服务器向客户端发起消息时所需的关键双向会话映射。Agentgateway 的基础架构与 MCP 面向会话、流式通信模型完美契合，而不是与为请求-响应 API 设计的架构抗争。

![](https://cdn.thenewstack.io/media/2025/10/cb209113-image6.gif)

在此基础上，agentgateway 作为原生 MCP 网关、大语言模型 (LLM) 网关和代理到代理 (A2A) 代理，提供传统 API 网关无法实现的安全、可观测性和治理能力。

它支持 MCP 多路复用以联合来自多个后端服务器的工具，应用细粒度授权策略来控制客户端可以访问哪些工具，并无缝处理 stdio 和 HTTP Streamable 传输。

当与[云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 项目 [kgateway](https://kgateway.dev/) 集成作为控制平面时，agentgateway 变为 Kubernetes 原生，使团队能够使用标准网关 API 资源管理 MCP 服务，同时代理负责协议特定的复杂性。

这种专门构建的方法提供了企业在生产 MCP 部署所需的性能、安全性和操作简便性——避免了改造 API 网关带来的脆弱性、维护负担和架构折衷。