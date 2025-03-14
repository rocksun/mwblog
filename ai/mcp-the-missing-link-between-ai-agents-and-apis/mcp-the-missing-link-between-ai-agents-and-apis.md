<!--
title: MCP：AI Agent和API之间缺失的环节
cover: https://cdn.thenewstack.io/media/2025/03/fb998efb-missing-link-2001.jpg
summary: 重磅！Anthropic推出开源标准MCP，标准化AI Agent的API访问！Speakeasy力推MCP Server Generation，连接LLM与API生态。对比OpenAPI，MCP是动态的Server-Client交互。Vercel、Dub已用上！未来或有更多AI巨头入局，LangChain、AutoGen等Agent框架迎来新机遇！
-->

重磅！Anthropic推出开源标准MCP，标准化AI Agent的API访问！Speakeasy力推MCP Server Generation，连接LLM与API生态。对比OpenAPI，MCP是动态的Server-Client交互。Vercel、Dub已用上！未来或有更多AI巨头入局，LangChain、AutoGen等Agent框架迎来新机遇！

> 译自：[MCP: The Missing Link Between AI Agents and APIs](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)
> 
> 作者：Richard MacManus

去年 11 月，Anthropic 推出了[模型上下文协议](https://modelcontextprotocol.io/introduction)（MCP），这是一个旨在简化 AI 模型与 API 交互方式的开源标准。正如[我们本月早些时候解释的那样](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/)，其愿景是使 MCP 成为 AI Agent 触发外部操作的通用方法。

MCP 在最初的几个月中引起了广泛的兴趣，其中包括来自 [Speakeasy](https://www.speakeasy.com/) 等 API 管理公司的兴趣。API 公司将 MCP 视为连接到 [LLM 的丰富生态系统](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/)和 Agent 框架的链接机制。为了了解更多信息，我采访了 Speakeasy 的 CEO Sagar Batchu。

## 什么是模型上下文协议 (MCP)？

正如其文档中所述，MCP“遵循客户端-服务器架构，其中主机应用程序可以连接到多个服务器”。

从本质上讲，MCP 标准化了 AI Agent 的 API 访问。您也可以将其视为元 API，正如 [Matt Pocock](https://x.com/mattpocockuk/status/1897742389592440970/photo/2) 的这张图所示：

![](https://cdn.thenewstack.io/media/2025/03/b77414ca-mcp-illustration-march2025.jpeg)

Batchu 解释说：“因此，MCP 是一种协议，实际上是 API 之上非常薄的一层，它表示，这是此 API 需要公开的定义，以便 LLM 或 Agent 能够查询并了解更多关于 [...] 任何数据的信息。”

[MCP 客户端](https://modelcontextprotocol.io/clients)可以是像 Claude 这样的 LLM、像 Cursor 和 Windsurf 这样的 IDE，以及各种其他工具（例如 SpinAI，一个用于构建 AI Agent 的 TypeScript 框架）。

至于 MCP 服务器（上图中的橙色块），您可以构建自己的服务器，也可以使用预构建的 MCP 服务器。在其[介绍性博客文章](https://www.anthropic.com/news/model-context-protocol)中，Anthropic 提到有“适用于流行的企业系统（如 Google Drive、Slack、GitHub、Git、Postgres 和 Puppeteer）”的预构建 MCP 服务器。

## Speakeasy 在 MCP 架构中的作用

构建您自己的 MCP 服务器是 Speakeasy 的用武之地。最近，该公司推出了 [MCP Server Generation](https://www.speakeasy.com/post/release-model-context-protocol)，这是一种可以自动创建与 MCP 兼容的服务器的工具。

目前，Speakeasy 的 MCP Server Generation 支持基于 TypeScript 的 SDK。但是，鉴于 Python 在 AI 生态系统中的主导地位，该公司计划很快增加对 Python 的支持。

Batchu 指出，由于 MCP 作为客户端-服务器模型运行，因此与 MCP 服务器交互的 AI Agent 可以使用任何编程语言。他解释说，与传统的 SDK（特定于语言并要求开发人员编写集成代码）不同，MCP 服务器公开了 AI Agent 可以直接访问的端点。

## MCP 与 OpenAPI 相比如何？

[OpenAPI](https://www.openapis.org/) 是一种被广泛采用的 API 定义标准，因此乍一看它也是 API 之上的一种层。但根据 Batchu 的说法，MCP 构建在 OpenAPI 之上，而不是取代它。
他说：“从 OpenAPI 规范到 MCP 的飞跃非常小。OpenAPI 在某种程度上是 MCP 需要的所有信息的超集，然后您将其与 LLM 的特定示例和描述打包在一起，并将其作为服务器运行。”

换句话说：虽然 OpenAPI 提供了 API 功能的结构化定义，但它主要是一个静态规范。相比之下，MCP 引入了客户端-服务器交互模型。MCP 服务器是一个实时的、正在运行的实例，AI Agent 可以实时查询。这意味着 MCP 服务器可以动态响应 AI 生成的请求，从而使 API 更容易被 [Agent 工作流程](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/)访问。

> “从 OpenAPI 规范到 MCP 的飞跃非常小。”
>
> – Sagar Batchu, Speakeasy CEO

正如 Batchu 所说，“区别在于 OpenAPI 规范只是一个定义，而 MCP 服务器实际上是一种服务器-客户端体验。”

在 MCP 出现之前，将 API 与 AI 模型集成一直具有挑战性。Batchu 指出，许多基于 AI 的 API 集成失败，因为模型缺乏必要的模式信息来理解 API 响应。MCP 通过以 AI 可以理解的方式构建 API 交互来解决此问题，从而使集成更加可靠。

## MCP 服务器的实际用例

Batchu 说，Speakeasy 已经有几家客户在使用其 MCP 功能集。像 Vercel、Dub 等公司正在利用 MCP 服务器来增强其 API 驱动的工作流程。
在 Dub（一个链接分享平台）上，营销团队经常创建短链接来跟踪文章表现。现在，他们无需手动搜索分析仪表板，就可以要求 AI 助手检索过去一周点击次数最多的链接。AI 查询 Dub 的 MCP 服务器，获取相关数据，甚至生成可视化效果，而用户无需离开他们的聊天界面。

我询问了潜在的电子商务应用，因为这个领域似乎非常适合 AI 代理。Batchu 建议，想象一下，这样一家公司使用 MCP 来支持 AI 驱动的商业智能。AI 助手可以查询 MCP 服务器以获取销售数据，生成报告，甚至根据实时洞察提出营销策略。这将减少手动数据提取和分析的需求。

![](https://cdn.thenewstack.io/media/2025/03/975446fc-speakeasy-mcp.jpg)

## 竞争标准即将到来？

Anthropic 开发了 MCP，但到目前为止，没有迹象表明 AI 领域的其他巨头会采用它，比如 OpenAI、Google 和 Meta。

Batchu 认为，MCP 范例可能会与其他 AI 驱动的 API 方法一起发展。他指出，[OpenAI 的函数调用](https://thenewstack.io/how-to-build-a-real-time-app-with-gpt-4o-function-calling/)已经提供了一种 AI 模型与外部服务交互的方式，尽管它缺乏 MCP 的标准化、开放性。

“我相信，在一段时间内会有一点模式之争，直到它像 OpenAPI 一样，成为一个标准，”他说。

> “我相信，在一段时间内会有一点模式之争。”
>
> – Batchu

无论如何，Batchu 认为 API 生产者现在是尝试 MCP 的好时机。

“API 生产者应该投资像 MCP 这样的代理工具，并且，你知道，创建一个 GitHub 仓库，构建它，把它发布出去。”

同样，他认为 API 消费者也应该进行实验，尽管他承认他们会面临更多的“ disruption and chaos ”，因为标准仍在变化中。但他对负责将 API 与 AI 结合使用的开发人员有一些建议。

“你可以做的第一件事实际上是去看看 API 是否有 MCP 服务器。你可以将它本地安装到你的 IDE 或 LLM 桌面客户端中，然后实际上开始通过自然语言查询进行集成。”

Batchu 还指出，开发人员有机会使用 MCP 以及像 LangChain 和 AutoGen 这样的[代理框架](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/)，来自动化工作流程并从 API 中动态提取洞察。