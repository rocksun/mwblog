<!--
title: Canva为什么选择MCP Server而不是AI Agent用于应用开发者
cover: https://cdn.thenewstack.io/media/2025/05/09eb8dd0-canva_mcp_server_for_devs.jpg
summary: Canva 推出 MCP Server赋能开发者平台，加速 AI 应用构建！放弃 AI Agent，拥抱 Anthropic 的 MCP 协议，开发者可使用 Gemini、Claude 或 GPT 等 LLM，通过 MCP Server 无缝访问 Canva API、SDK 和文档，简化开发流程，提升效率！
-->

Canva 推出 MCP Server赋能开发者平台，加速 AI 应用构建！放弃 AI Agent，拥抱 Anthropic 的 MCP 协议，开发者可使用 Gemini、Claude 或 GPT 等 LLM，通过 MCP Server 无缝访问 Canva API、SDK 和文档，简化开发流程，提升效率！

> 译自：[Why Canva Chose MCP Server Over AI Agent for App Developers](https://thenewstack.io/why-canva-chose-mcp-server-over-ai-agent-for-app-developers/)
> 
> 作者：Loraine Lawson

[Canva 上个月为其开发者平台推出了](https://www.canva.dev/blog/developers/canva-dev-mcp-server/)模型上下文协议 (MCP) 服务器。它使用 [MCP](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype/) 而不是 [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)，这让我们可以初步了解开发者在不久的将来可能从托管自己应用市场的公司那里获得什么。它还展示了 MCP 如何成为构建应用程序的变革者。

MCP 是一种新兴的开放标准，[来自 Anthropic](https://www.anthropic.com/news/model-context-protocol)，它提供了一种让 AI 模型与外部数据源和工具交互的方式。可以将其视为一种通用语言和一组规则，允许[大型语言模型](https://thenewstack.io/the-new-shadow-it-llms-in-the-wild/)与其自身之外的系统进行对话。MCP 服务器将 LLM 的请求翻译成系统能够理解的语言，然后以标准化格式将信息返回给 LLM。这让开发者可以通过提供额外数据或支持更复杂的任务来以新的方式使用模型，而无需构建 AI agent 或重新训练 LLM。

## Canva 的 MCP 用例

Canva 的生态系统负责人 Anwar Haneef 向 The New Stack 解释说，Canva 的 MCP 服务器将使使用其开发平台的数千名 Web 开发者以及这些程序员所依赖的 AI 系统能够更轻松地访问 Canva 文档和 API。

他说，在 MCP 服务器之前，[构建 Canva 应用程序](https://thenewstack.io/canva-launches-developer-platform-eyes-generative-ai-apps/)是一个漫长的过程。开发者必须与 Canva 来回沟通，Canva 会审查应用程序以确保它们符合 Canva 的外观和风格。

他说：“通常情况下，应用程序提交后，我们会进行审查流程。设计师会尝试从用户体验的角度确保其设计良好。”

Canva 在其[市场](https://www.canva.com/apps/)上拥有 600 多个应用程序，Haneef 估计其中约有 150 个启用了 AI。审查过程耗时，并且每次应用程序更改后都需要进行额外的审查。Canva 希望加快这一过程。

他说：“通过 MCP，我们意识到我们可以有效地将使用我们开发工具的工作‘左移’到 Canva 之外的开发者。” “我们创建了一个 MCP 服务器，可以轻松访问 Canva 开发者 API、SDK 和文档。”

借助 MCP 服务器，Canva 有效地将反馈专业知识带到了开发者的工作区，缩短了反馈循环的长度。

Haneef 说：“我们的目的是，当他们提交应用程序时，开发过程中会有大量的反馈和自动化，从而简化提交和发布过程。”

他补充说，MCP 服务器允许开发者留在他们的 IDE 中，同时仍然获得 Canva 使用的 UI 工具包的外观和风格。

## MCP 与 Agents

Canva 考虑构建一个 [AI agent](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/) 来协助开发者，但最终放弃了这条路线，因为很多人都在这样做，并且向开发者收费，包括 Windsurf 和 Cursor。

他说：“开发者已经在为它们 [agents] 付费，并在他们日常工作中使用它们。” “我们为它提供更高层次的改进可能不会增加太多，但确保这些 LLM 具有正确的上下文来构建与我们的平台相关的代码——这具有很大的影响。”

这与科技行业之前对 AI 的期望有所不同，即公司将训练 AI agent 来执行特定任务，而开发者必须使用该组织的 AI。

相反，MCP 服务器使用开发者正在使用的本地模型。它通过开发者 AI 对 Canva 的调用来调用，然后从 Canva 获取开发者创建应用程序所需的信息。

Haneef 说：“我们不希望他们依赖我们的 [AI] 模型并进行各种变体，而是希望开发者使用他们感到舒适的工具——无论他们使用 Gemini、Claude 还是 GPT，或者其他任何工具。” “基本上，我们为他们的模型提供输入以供使用，然后将其呈现出来，这就是 MCP 至关重要的原因。”

## 部署 MCP 服务器

Haneef 说，构建 MCP 服务器并非易事。

他说：“有[文档](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)，但没有明确的标准。” “工具仍在涌现。”
Canva 与专门构建 MPC 服务器的经验丰富的公司合作，他补充说。Canva 的工作就是以轻量级且易于理解的格式提供信息，以便 AI 能够理解，他解释说。这意味着回到第一性原理并重新评估其开发者产品。

Canva 做的更改之一是修改其文档以启用标记语言访问，以便 AI 代理可以轻松地解析它，而无需浏览 JavaScript 或图像。该公司还重新思考了其支持开发者和创建应用程序的整个过程。他表示，它选择 MCP 是因为它已经获得了 [IDEs](https://thenewstack.io/best-open-source-ides/) 的欢迎。

“现实情况是标准在不断发展，因此我们希望确保我们所做的事情是经过深思熟虑的，”他说。“我们专注于向代理提供内容之上的上下文。”

MCP 服务器还避免了开发者将信息发送给 Canva 的问题，而组织往往对此感到不满。

这让开发者更加安心，因为他们知道数据正在被发送到他们的 AI 中，但数据不会离开他们的 AI 或内部系统。

MCP 服务器现已可用。Haneef 补充说，Canva 开发者的另一个途径是使用 Zapier，它为其集成（包括 Canva Connect API）提供 MCP 服务器访问。