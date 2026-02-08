<!--
title: Anthropic为MCP引入UI框架，赋能交互式应用
cover: https://cdn.thenewstack.io/media/2025/12/e7613ca2-img_0986-scaled.jpg
summary: Anthropic发布MCP协议的UI框架扩展，使AI聊天界面具备交互式应用体验，增强第三方服务集成，提升AI实用性。
-->

Anthropic发布MCP协议的UI框架扩展，使AI聊天界面具备交互式应用体验，增强第三方服务集成，提升AI实用性。

> 译自：[Anthropic extends MCP with a UI framework](https://thenewstack.io/anthropic-extends-mcp-with-an-app-framework/)
> 
> 作者：Frederic Lardinois

通过MCP协议，Anthropic创建了人工智能模型和代理与第三方应用程序对话的事实标准。去年12月，Anthropic将MCP协议捐赠给[Agentic AI基金会](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/)后，今天发布了MCP的一个主要新开放扩展，该扩展将允许MCP服务器在聊天界面内提供交互式的应用体验。

Anthropic当然正在将此功能直接集成到Claude的网络和桌面体验中。然而，值得强调的是，这是一个开放协议，因此任何其他聊天机器人提供商都可以采用此协议，并且任何第三方服务都能够构建这些应用程序。

目前，Goose、Visual Studio Code（面向内部人员）以及本周晚些时候来自Anthropic竞争对手OpenAI的ChatGPT都已支持MCP Apps。

Anthropic的一些早期合作伙伴包括Amplitude、Asana、Box、Canva、Clay、Figma、Hex、monday.com和Slack。例如，通过Box MCP App，用户将能够在聊天体验中搜索文件并内联预览文档——然后还可以就这些文档提问。

同时，通过Slack应用，用户可以使用AI模型撰写和编辑消息草稿，然后将其发布到Slack。其中包括，正是MCP Apps框架允许直接在Claude中编辑这些消息。

![](https://cdn.thenewstack.io/media/2026/01/ee28fd87-slack-claude-mcp-app.gif)

*Slack MCP应用（图片来源：Slack）。*

“企业对AI的需求不仅仅是强大的模型。他们还需要一种可靠的方式让这些模型在真实的业务环境中运行。通过与Anthropic合作，我们正在将Salesforce直接带入客户的工作流程中，并提供具有上下文、数据、治理和信任的执行层，”Salesforce战略技术合作高级副总裁Nick Johnston在今天的声明中表示。“这就是驱动Agentic企业的原因。”

很快，Slack的所有者Salesforce也将把其Agentforce、Data 360和Customer 360应用带到Claude。

![](https://cdn.thenewstack.io/media/2026/01/3976b808-mcp-apps-asana.png)

*Asana MCP应用（图片来源：Asana）。*

Anthropic在[11月首次提出](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/)的MCP Apps的一些典型使用场景包括使用仪表盘进行交互式数据探索、配置向导、文档审查和实时监控。

MCP Apps的核心依赖于提供用户界面元数据和用户界面资源（HTML和JavaScript）以渲染它们的工具。

## 构建MCP Apps

![](https://cdn.thenewstack.io/media/2026/01/5006ec35-screenshot-2026-01-26-at-12.44.42.png)

*定义MCP应用的核心原语（图片来源：Anthropic）。*

将这种交互式UI体验带到Claude和其他以聊天为中心的AI工具中，感觉是一个合乎逻辑的下一步。无论好坏，聊天仍然是与AI模型交互的默认方式，但一段时间以来，它一直显得相当有限。

Anthropic当然不是第一个想到这一点的人。OpenAI通过其[Apps SDK](https://developers.openai.com/apps-sdk/)提供了一个有些类似的框架，其核心也使用了MCP。Anthropic指出，OpenAI Apps SDK和开源MCP-UI项目（由Ido Salomon和Liad Yosef创建）都开创了许多这些模式。

“这些项目证明，UI资源可以并且确实自然地融入MCP生态系统，各种规模的企业都正在将OpenAI和MCP-UI SDK用于生产应用程序，”Anthropic团队写道。

在可预见的未来，编写[MCP-UI](https://mcpui.dev/)应用的开发者将能够继续这样做。

“MCP Apps建立在MCP-UI和ChatGPT Apps SDK的基础之上，为人们提供丰富、视觉交互的体验，”OpenAI技术人员Nick Cooper说。“我们很自豪能支持这个新的开放标准，并期待看到开发者用它构建出什么，因为我们正在增加ChatGPT中可用应用的范围。”

在安全方面，Anthropic指出它实施了多项防护措施，以确保您在MCP主机上运行的第三方代码不会突破其沙盒。这些措施包括具有受限权限的沙盒iframe、主机在渲染前审查HTML内容的能力、可审计的UI到主机消息，以及用户必须明确批准UI发起的工具调用。