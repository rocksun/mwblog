
<!--
title: MCP：AI领域的USB-C，简化LLM集成
cover: https://www.infracloud.io/assets/img/Blog/mcp/mcp-1200x628.png
summary: AI开发太难？🔥`MCP`协议来啦！它像USB一样，标准化`LLM`与外部数据源、工具的连接，解决集成复杂、厂商锁定等痛点。`MCP`基于Client-Server架构，支持`TextContent`等多种内容类型，已有`Python`、`Java`等`SDK`。订阅`AI-Xplore`，解锁更多云原生AI新姿势！
-->

AI开发太难？🔥`MCP`协议来啦！它像USB一样，标准化`LLM`与外部数据源、工具的连接，解决集成复杂、厂商锁定等痛点。`MCP`基于Client-Server架构，支持`TextContent`等多种内容类型，已有`Python`、`Java`等`SDK`。订阅`AI-Xplore`，解锁更多云原生AI新姿势！

> 译自：[Model Context Protocol: The USB-C for AI: Simplifying LLM Integration](https://www.infracloud.io/blogs/model-context-protocol-simplifying-llm-integration/)
> 
> 作者：Atulpriya Sharma

随着新模型几乎每天都在涌现，AI应用程序的开发就像计算机的预标准化时代，那时连接设备意味着要同时处理多条电缆和连接器以及自定义驱动程序。今天构建一个AI应用程序非常复杂。开发人员必须处理不同的集成代码，才能将LLM与不同的外部数据源、供应商的特定实现以及最重要的安全问题连接起来。这些导致系统脆弱，开发人员负担过重，并且始终存在供应商锁定的风险。

虽然USB为连接外围设备带来了标准化，但对AI应用程序的USB类型标准的需求也日益增长。这正是模型上下文协议（MCP）所要解决的问题。它有可能成为一种通用标准，以简化AI模型与外部系统交互的方式。

在这篇博文中，我们将探讨MCP及其用于将大型语言模型（LLM）与不同数据源、工具和服务连接的标准化方法。

## Why MCP?

大型语言模型在能够访问正确的上下文时具有变革性，但是将这些模型连接到必要的数据源和工具已成为AI开发中的一个重大瓶颈。当前的方法迫使团队为每个用例构建自定义集成，从而导致代码库分散和整个行业重复工作。

MCP的出现是为了应对阻碍高效、安全AI集成的四个关键挑战：

*   **缺乏标准化**：没有用于将LLM与数据源和工具集成的通用和标准化接口。开发人员被迫为数据源和外部工具创建自定义集成。这导致代码库分散，从而导致实现不一致。
*   **供应商锁定**：使用专有集成会带来供应商锁定的风险。与特定供应商捆绑在一起意味着随着您的需求和技术的发展，转换成本会增加，灵活性受到限制。
*   **集成复杂性**：开发和维护不同的自定义集成工具需要专门的知识。这也减慢了开发过程，并创建了不稳定的系统，这些系统在底层组件更改时可能会崩溃。
*   **安全风险**：跨自定义集成的不一致安全实现会产生漏洞，这些漏洞可能变得非常危险，因为攻击者可以访问敏感数据和关键系统。
*   
## 什么是 MCP？

[模型上下文协议（MCP）](https://github.com/modelcontextprotocol)是由Anthropic（Claude背后的团队）开发的开源协议，旨在标准化AI集成。作为开源，MCP旨在促进协作并建立一个使整个AI生态系统受益的通用标准。

MCP提供了一种标准化方法，用于将LLM应用程序与外部数据源和工具连接。它提供了实现指南，以在AI模型和它们需要运行的上下文之间创建通用接口层。MCP建立了数据访问、工具执行和提示管理的通用模式，从而使开发人员无需构建自定义集成。这使开发人员可以专注于构建灵活的AI应用程序，这些应用程序可以无缝访问文件、数据库、API和其他资源，而无需绑定到专有实现。

因此，您无需为Claude编写自定义集成，也无需为Perplexity编写不同的集成，即可连接到您产品的文档和其他内部工具。借助MCP，您可以实现一个协议，该协议允许您的AI应用程序通过标准化请求无缝访问所有资源。

## MCP 架构和组件

MCP遵循客户端-服务器架构，由5个关键组件组成，这些组件协同工作以在LLM和外部资源之间创建安全和标准化的连接。

*   **MCP主机**：这些是需要上下文AI功能的应用程序。这些应用程序可以是聊天机器人、AI增强型IDE或自定义应用程序。这些主机与MCP客户端集成，以通过该协议访问数据和外部工具。
*   **MCP客户端**：客户端负责维护与MCP服务器的1：1连接。它们处理服务器没有的协议细节。客户端将主机请求转换为标准化的MCP消息，管理连接，并且还处理与服务器的身份验证。
*   **MCP服务器**：这些是生态系统的核心，并通过标准化的MCP接口公开关键功能。服务器可以通过一致的协议提供对数据库的访问或与外部工具和远程API集成。
*   **本地数据源**：这些是MCP服务器可以安全访问的本地文件、数据库和服务。该协议提供细粒度的权限，以确保AI模型仅访问授权的资源。
**远程服务**： 这些是通过 API 在互联网上可用的外部服务，MCP 服务器可以连接到这些服务。它们可能包括知识库、代码库或专用工具。

![](https://www.infracloud.io/assets/img/Blog/mcp/mcp-architecture.webp)

这种架构是模块化和可组合的，因此组织可以为不同的数据源实现不同的服务器，同时具有一致的接口。这也确保了关注点分离，因为主机专注于 AI 功能，客户端处理协议细节，服务器管理数据访问和工具执行。

## 理解协议规范

MCP 为开发人员构建 MCP 客户端或服务器提供了一个蓝图。它有助于理解各种组件如何相互交互，并标准化消息格式、交互模式和错误处理，以实现一致的实现。

### 核心通信模式

MCP 围绕三种主要消息类型构建：

- **请求**： 这些是客户端发送到服务器以启动操作或检索信息的消息。每个请求都有一个唯一的 ID，该 ID 与其对应的响应相关联。
- **响应**： 服务器发送到客户端以响应请求的消息。这些包含请求的信息或状态。
- **通知**： 这些是从服务器发送到客户端的异步消息，没有关联的请求。它们通知客户端相关的状态更改或事件。

这三者实现了同步（从工具获取响应）和异步（通知执行完成）通信。

除了这些核心通信模式之外，还有一些关键的协议概念：

- **资源**： 这些是可以被 LLM 访问的数据的抽象。这些可以是本地文件、数据库、API 调用的结果或工具执行生成的内容。这些资源具有唯一的 ID，可以在整个协议中引用，允许 LLM 请求特定信息。通过标准化资源的识别和交互方式，MCP 为处理数据创建了一致的接口。
- **工具**： 工具代表 LLM 可以通过 MCP 服务器执行的操作。它们支持诸如搜索存储库、查询数据库、执行代码或发送电子邮件等功能。每个工具都有一个明确定义的接口，指定了所需的参数和返回值，从而标准化了 LLM 通过一致的接口与外部系统交互的方式。
- **提示**： 提示提供了一种为提示和工作流定义可重用提示模板的方法。这些创建了标准化的交互模式，定义了多步骤工作流，其中一个步骤的输出是另一个步骤的输入，从而支持跨应用程序共享提示并帮助提示进行版本控制。通过这样做，MCP 能够构建结构化且可管理的 AI 应用程序。
  
## 丰富内容的内容类型 

MCP 还支持不同的内容类型，以实现 LLM 和外部系统之间丰富的交互。其中一些是：

- **TextContent**： 表示可以直接合并到 LLM 中的纯文本或 markdown 文本。
- **ImageContent**： 支持在能够处理图像的模型之间共享视觉内容。
- **EmbeddedResource**： 允许不同的资源相互引用，从而创建 LLM 可以与之交互的信息层次结构。

## MCP 的工作原理：一个简化的示例

假设您的组织构建了一个 AI 代理，可以帮助您安全高效地与企业数据库和销售数据进行交互。

### 用户请求

在此示例中，您通过在 AI 应用程序中键入查询来询问您的 AI 助手应用程序“我们上个季度完成了多少销售额？”。

### 初始化

在幕后，AI 助手应用程序使用 MCP 客户端连接到您公司的 MCP 服务器。客户端发送一个 `InitializeRequest` 消息以建立连接。

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
	"protocolVersion": "1.0"
  }
}

```

服务器确认请求并响应它支持的功能列表。

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "1.0",
    "capabilities": {
      "tools": true
    }
  }
}

```

### 工具发现

客户端需要知道 MCP 服务器有哪些可用的工具，因此它发送一个 `ListToolsRequest`

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "listTools",
  "params": {}
}
```

服务器响应一个查询，列出可用的工具。

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "tools": [
      {
        "name": "querySales",
        "description": "Query sales data by period",
        "parameters": {
          "period": {
            "type": "string",
            "description": "Time period (e.g., Q1, Q2, 2023)"
          }
        }
      }
    ]
  }
}

```

### 工具执行

AI 助手确定需要季度销售数据，并指示客户端进行适当的工具调用。

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "callTool",
  "params": {
    "toolName": "querySales",
    "arguments": {
      "period": "Q1"
    }
  }
}

```

### 数据检索

MCP 服务器收到此请求，根据安全和访问策略对其进行验证，然后查询公司数据库。数据库返回结果，服务器对其进行格式化并发送回客户端。

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "totalSales": 1200000,
    "regions": {
      "East": 450000,
      "West": 350000,
      "North": 250000,
      "South": 150000
    },
    "topProducts": [
      {
        "name": "Enterprise Solution",
        "revenue": 500000
      },
      {
        "name": "Professional Services",
        "revenue": 300000
      }
    ]
  }
}

```

### 响应生成

AI助手通过MCP客户端接收到这些结构化数据，并形成自然语言回复：“上个季度，我们的销售额为120万美元，其中东部地区的业绩最佳，为45万美元。我们最畅销的产品是Enterprise Solution，占我们收入的50万美元。”

以下是上述过程的序列图。

![](https://www.infracloud.io/assets/img/Blog/mcp/response-generation.webp)

## MCP 入门

实施MCP非常简单，使您能够构建可扩展且灵活的AI应用程序。根据您在团队中的角色，有不同的方法可以开始使用MCP。

*   **服务器开发人员**： 如果您主要从事服务器端工作，则[面向服务器开发人员的MCP文档](https://modelcontextprotocol.io/quickstart/server)包含全面的服务器实施指南。这些指南涵盖了从基本服务器设置到高级主题（如安全性、权限模型和处理复杂资源类型）的所有内容。
*   **客户端开发人员**： 客户端SDK可供客户端开发人员使用，以简化集成过程。[MCP客户端开发人员文档](https://modelcontextprotocol.io/quickstart/client)包括客户端实施模式、身份验证最佳实践以及常见集成场景的示例代码。
*   **Claude Desktop用户**： 如果您正在使用Claude Desktop并希望利用现有的MCP服务器，您会找到[Claude Desktop用户的使用指南](https://modelcontextprotocol.io/quickstart/user)，其中解释了如何连接到服务器、授权访问以及使用MCP服务器在Claude界面中提供的增强功能。

此外，还有专门的SDK可用于[Python](https://github.com/modelcontextprotocol/python-sdk)、[Java](https://github.com/modelcontextprotocol/java-sdk)、[Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)和[TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)，它们具有全面的文档、快速入门指南、API参考和示例应用程序，以展示常见的集成模式。

## 总结

模型上下文协议（Model Context Protocol）确实是解决阻碍AI发展的集成挑战所需的USB标准。通过建立连接LLM与外部数据源和工具的标准化方法，MCP消除了先前表征AI集成工作流程的摩擦和冗余。

就像HTTP标准化了Web通信或SQL标准化了数据库交互一样，MCP为AI系统与周围世界交互创建了一种通用语言。

要了解有关AI最新信息的更多信息，请订阅我们的[AI-Xplore网络研讨会](https://www.infracloud.io/webinars/ai-xplore/)。我们会定期举办网络研讨会，并邀请AI专家分享他们的知识。请分享您对本文的看法以及您如何使用AI，以及您遇到的任何有趣的用例。在[LinkedIn](https://www.linkedin.com/in/atulpriyasharma)或[Twitter](https://twitter.com/TheTechMaharaj)上与我联系。