[Go](https://thenewstack.io/introduction-to-go-programming-language/) 已成为[云基础设施](https://thenewstack.io/go-language-fuels-cloud-native-development/)的通用语言，从容器编排、CI/CD 流水线到工程师日常依赖的命令行工具，无处不在。Kubernetes、Docker 和 Terraform 均由其编写，它是构建后端服务的默认选择。

与此同时，[AI Agent 已成为](https://thenewstack.io/coding-agents-team-infrastructure/)几乎所有大型软件供应商的关注焦点，各方竞相为开发者提供原生的构建方式。正因如此，微软现在将其 [Agent Framework](https://github.com/microsoft/agent-framework) 引入 Go，使云原生开发者能够使用他们早已熟练掌握的语言来构建 AI Agent。

[Microsoft Agent Framework for Go](https://github.com/microsoft/agent-framework-go) 自周五起提供公开预览版，它本质上为 Go 开发者提供了与其 [Python](https://github.com/microsoft/agent-framework/tree/main/python) 和 [.NET](https://github.com/microsoft/agent-framework/tree/main/dotnet) 开发人员相同的许多构建模块：支持来自 [Microsoft Foundry](https://thenewstack.io/microsoft-foundry-build-2026-ai-agents/)、Azure OpenAI、Anthropic 和 Gemini 的模型，支持用于将 Agent 连接到外部系统的工具调用和 MCP，以及协调多个 Agent 共同完成任务的能力。

> “Microsoft Agent Framework 专为那些从单次提示词调用转向生产级 Agent 系统的开发者而设计。”

微软高级软件工程师 [Quim Muntal](https://www.linkedin.com/in/quimmuntaldiaz/) 在周五宣布该发布的[博客文章](https://devblogs.microsoft.com/go/)中指出，该 Agent Framework 本身是为那些构建功能更强、运行时间更长的 AI 系统的人准备的。

“Microsoft Agent Framework 专为那些从单次提示词调用转向生产级 Agent 系统的开发者而设计，”Muntal 写道。“这些 Agent 可以使用工具、保持上下文、与其他 Agent 协调、流式传输结果，并作为真实应用程序的一部分进行可观测性管理和治理。”

这正是 Go 长期占据的领域：服务、命令行工具、后台工作线程和云原生应用程序，在该领域 Go 一直是默认选择。Go SDK 将这些功能直接交到了在此领域开发的开发者的手中。

## 微软的 Agent Framework 如何进入 Go

简单回顾一下，[微软于 2025 年 10 月推出了 Agent Framework](https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/)，作为一个用于构建 AI Agent 和多 Agent 系统的开源工具包，将微软早期的两个项目 [AutoGen](https://thenewstack.io/building-multiagent-workflows-with-microsoft-autogen/) 和 [Semantic Kernel](https://thenewstack.io/microsoft-semantic-kernel-for-ai-dev-a-chat-with-john-maeda/) 合并为一个受支持的单一平台。

它在[今年 4 月](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/)实现了正式发布（GA），并在 6 月的微软 Build 大会上，[该公司增加了](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/)一系列新功能和工具：用于上下文管理和人工审批步骤等生产模式的“Agent 工具箱”，通过 Microsoft Foundry 托管的 Agent，一种名为 CodeAct 的更快速的工具调用方法，以及通过新的切换模式支持多个 Agent 串联。

在此过程中，Agent Framework 仅支持 .NET 和 Python。社区中一些人[曾要求支持 Go](https://github.com/microsoft/agent-framework/discussions/1146) 和 Rust，一位微软产品经理早在 2025 年 10 月就[确认](https://github.com/microsoft/agent-framework/discussions/1146#discussioncomment-14662163)公司正在考虑该框架的 Go 版本，但“至少还需要几个月”。

> “这是生产级的编排，而不是聊天循环包装器。”

虽然目前还处于早期阶段，但开发者社区已经对此次发布意味着什么（以及不意味着什么）产生了一些议论。在 [LinkedIn 帖子](https://www.linkedin.com/feed/update/urn:li:activity:7481388476286881792/)中，AI 工程师 Pratik Dhanave 称其为“Go 优先”工程师的一个里程碑，并特别指出了该 SDK 基于图的 workflow 编排，它支持条件路由、子工作流、检查点和人工介入审查等模式。

“这是生产级的编排，而不是聊天循环包装器，”他写道。

Dhanave 还指出了微软自己记录的 Go SDK 尚不支持的功能：切换编排和 CodeAct 等功能虽然在 .NET 中可用，但尚未移植到 Go。“我很欣赏这种在公开预览版中坦诚的态度，”他继续说道。

## Google、OpenAI 和 Anthropic 在 Go 上的立场

就 Google 而言，它一直遵循类似的轨迹，尽管节奏不同。该公司于 2025 年 4 月[推出了自己的 Agent 开发套件](https://thenewstack.io/googles-adk-is-a-new-open-source-framework-for-building-multiagent-systems/) (ADK)，这是一个仅限 Python 的工具包，随后在 11 月[增加了 Go 支持](https://developers.googleblog.com/en/announcing-the-agent-development-kit-for-go-build-powerful-ai-agents-with-your-favorite-languages/)，并在[今年 3 月正式发布了 1.0 版本](https://developers.googleblog.com/adk-go-10-arrives/)。

Go 当然是 Google 的产物，它于 [2009 年](https://opensource.googleblog.com/2009/11/hey-ho-lets-go.html)从公司的开源仓库中走出来，这一举措塑造了随后的云原生世界。它后来成为 Kubernetes 和 Docker 背后的语言，这两个项目定义了现代基础设施的构建和部署方式，这使得 Go 成为平台工程师的默认选择。这种吸引力不仅限于 Google，还扩展到了 [AWS](https://aws.amazon.com/blogs/aws/now-available-version-1-0-of-the-aws-sdk-for-go/)、Cloudflare、微软以及无数其他科技巨头的领域。

鉴于这种吸引力，对 Agent 工具中原生 Go 支持的需求也就不足为奇了。想要构建 Agent 服务、将 AI 功能嵌入现有微服务或编写能够自行决策的基础设施工具的 Go 开发者，过去不得不忍受没有自己语言的官方 SDK 的情况：要么使用原始 HTTP 调用，要么在 Go 服务旁边启动一个独立的 Python 或 Node.js 进程，或者依赖质量和支持参差不齐的非官方社区维护库。

因此，微软显然是在迎合一个成熟的开发者群体。然而，AI 领域的其他大玩家还没有跟进。截至今日，无论是 Anthropic 的 [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) 还是 OpenAI 的 [Agents SDK](https://developers.openai.com/api/docs/guides/agents) 都没有官方支持 Go，[尽管社区有相关请求](https://github.com/anthropics/claude-agent-sdk-python/issues/498)要求[提供此类支持](https://community.openai.com/t/golang-support-for-openai-agents-sdk/1368961)。

微软并不是唯一将 AI Agent 引入 Go 的公司。但它的加入意味着两家最大的云供应商现在为业界最广泛使用的基础设施语言之一提供了第一方 Agent 框架。基础模型领域剩下的两个最大名字——Anthropic 和 OpenAI——正在掉队。