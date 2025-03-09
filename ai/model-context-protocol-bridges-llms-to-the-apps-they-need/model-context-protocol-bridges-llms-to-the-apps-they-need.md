
<!--
title: Anthropic的MCP将LLM连接到它们需要的应用程序
cover: https://cdn.thenewstack.io/media/2025/03/da0fefca-tamanna-rumee-8yd0ndi1shy-unsplash-mcp.jpg
-->

MCP 看起来像是 API 之上的一个额外层。但 Anthropic 的工程师们有一个更大的愿景，即让 MCP 成为 AI 智能体触发外部动作的通用方法。

> 译自：[Anthropic's MCP Bridges LLMs to the Apps They Need](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/)
> 
> 作者：Joab Jackson

“这非常像微服务，但我们正在引入智能，”[Anthropic](https://www.anthropic.com/company) 应用 AI 工程师 [Mahesh Murag](https://www.linkedin.com/in/maheshmurag/) 说道，他描述了 [模型上下文协议](https://modelcontextprotocol.io/introduction) (MCP)，这是一个在 Anthropic 诞生的开源项目，旨在标准化应用程序如何为 LLM 及其驱动的代理提供上下文。

Murag 上个月在纽约举行的 [AI Engineer Summit](https://www.ai.engineer/summit/2025) 上发表了讲话，他的演讲引发了人们对 MCP（首次发布于 11 月）的浓厚兴趣，因为人们讨论了简化开发人员流程的最佳方式，以使代理与计算世界的其他部分进行交互。

## 今天的代理格局

MCP 的灵感来自 [语言服务器协议](https://microsoft.github.io/language-server-protocol/) (LSP)，这是一种 IDE 理解 [编程语言](https://thenewstack.io/programming-languages/) 所有不同功能的标准。

如今，代理必须逐个地与这些资源进行交互，从而积累了大量的日常开发工作。或者更糟的是，用户可能必须手动剪切和粘贴上下文（和配置）数据。

可能存在插件，但它们是为每种特定类型的连接而设计的。

或者它们可能被限制在特定平台，例如 OpenAI 的 [Work With Apps](https://reindeersoft.com/news/openai-launches-work-with-apps-feature-for-seamless-macos-integration) 功能，该功能适用于 [Macs](https://thenewstack.io/homebrew-for-macos-developers/)（和 OpenAI）。

通过 MCP，代理将有一种标准的方式来访问数据、工具和提示（预先编写的模板）——如果它被模型制造商和应用程序供应商广泛采用。

Anthropic 的一篇 [博客文章解释说](https://www.anthropic.com/news/model-context-protocol)：“开发人员现在可以根据标准协议进行构建，而不是为每个数据源维护单独的连接器。” “随着生态系统的成熟，AI 系统将在不同的工具和数据集之间移动时保持上下文，从而用更可持续的架构取代当今碎片化的集成。”

> 很多人对 MCP 感到 FOMO。
> 
> 这是它解决的问题：
> 
> — Matt Pocock (@mattpocockuk)
> [March 6, 2025](March 6, 2025)

## 代理将如何找到资源

Murag 在他的演讲中说，MCP 不会取代 [代理框架](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/)，而是通过提供可插拔的连接器和适配器来补充它们，并通过提供与工具交互的一致方式来简化开发人员的生活。

MCP 在一组 [规范和 SDK](https://github.com/modelcontextprotocol) 中定义，涵盖客户端和服务器实现。

该文档介绍了创建“服务器”的过程，该服务器使用 [Python](https://thenewstack.io/what-is-python/)、[Node](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) 或 [Java](https://thenewstack.io/introduction-to-java-programming-language/) 为 LLM [提供](https://modelcontextprotocol.io/quickstart/server) 天气预报。MCP 服务器可以本地安装或由第三方运行。

示例服务器有一组“辅助函数”，用于查询和格式化来自国家气象局 API 的数据。工具执行处理程序执行每个工具的逻辑。然后，它可以安装在 Anthropic 的 [Claude Desktop](https://claude.ai/download) AI 服务（或您首选的代理）上。

[同样](https://modelcontextprotocol.io/quickstart/client)，用户客户端软件（它是 AI 应用程序本身的一部分）初始化一个会话，收集可用工具的列表。
它还维护对话上下文，执行查询并处理响应，并为用户提供命令行界面。

Murag 解释说：“一旦您的客户端与 MCP 兼容，您就可以将其连接到任何服务器，而无需进行额外的工作。” “如果您是工具或 API 提供商，或者想要让 LLM 访问重要数据的人，您可以构建一次 MCP 服务器，并在所有这些不同的 AI 应用程序中看到它的采用。”

在企业方面，运行 [向量数据库接口](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/) 的团队可以将其转换为 MCP 服务器，公司中的其他团队可以从中构建他们的应用程序。

据推测，服务提供商都希望提供自己的服务器。因此，就像微服务一样，MCP 需要一个注册表，一个查找和发现资源的地方。Murag 说：“如今，一个巨大的问题是发现。”
因此，该项目还维护了一个 MCP 服务器的[开源存储库](https://github.com/modelcontextprotocol/servers)，为数十种服务提供参考实现，例如 [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps)、[PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 和 [Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)。

![](https://cdn.thenewstack.io/media/2025/03/af835164-mcp-01.png)

## MCP 会蓬勃发展吗？

Murag 的演讲在 AI 圈子里引起了巨大的兴趣。

AI 代理开发者 John Rush 在 X 上[写道](https://x.com/johnrushx/status/1897655569101779201)：“在 MCP 出现之前，人们必须编写代码才能通过 API 将 AI 工具连接到外部系统。这意味着每个连接都必须预先编码。”

“MCP 是一个标准协议。这意味着每个 AI 工具只需实现一次，然后它就可以通过该协议连接到数千个外部工具。”

Julian Harris 在 X 消息中[表示](https://x.com/julianharris/status/1897589990382506175)，通过为“任何 API 提供成为 LLM 工具插件的标准接口”，MCP 是一种“以极低的摩擦方式丰富 LLM 上下文”的方法。

并非所有人都印象深刻。一位观察员将其比作 [AI 领域的 Zapier](https://x.com/julianharris/status/1897589990382506175)，并指出它只是在使用 API 时增加了额外的步骤。

另一个可能的障碍：其他 LLM 服务提供商，如 Grok 和 ChatGPT 目前不支持它，这些系统设计者很可能会尝试推出自己的标准。

但 Murag 指出，MCP 本身与 Anthropic 的 AI 服务 Claude 没有任何关联。

的确。Dagger 创始人 Solomon Hykes [指出](https://x.com/solomonstre/status/1897784401125412896)，他的[公司平台](https://thenewstack.io/ai-dev-tools-how-to-containerize-agents-using-dagger/)可以作为“Claude Code 的开放替代方案”，因为它“完全开源，支持任何模型，并且是 MCP 原生的”。

在此处欣赏 Murag 的[完整演示](https://youtu.be/kQmXtrmQ5Zg)。