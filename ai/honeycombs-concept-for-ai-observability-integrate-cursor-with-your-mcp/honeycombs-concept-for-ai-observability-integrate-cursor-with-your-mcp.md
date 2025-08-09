
<!--
title: Honeycomb的AI可观测性概念：集成Cursor与你的MCP
cover: https://cdn.thenewstack.io/media/2025/08/10201d8c-patrycja-jadach-6cq6a1eomio-unsplash.jpg
summary: Honeycomb的MCP服务器将AI模型集成到IDE中，通过查询加速AI辅助调试。面临的挑战包括处理大量数据和避免LLM的查询幻觉。其他SaaS工具在构建MCP服务器时也面临类似问题，需要优化LLM接口设计。
-->

Honeycomb的MCP服务器将AI模型集成到IDE中，通过查询加速AI辅助调试。面临的挑战包括处理大量数据和避免LLM的查询幻觉。其他SaaS工具在构建MCP服务器时也面临类似问题，需要优化LLM接口设计。

> 译自：[Honeycomb’s Concept for AI Observability: Integrate Cursor With Your MCP](https://thenewstack.io/honeycombs-concept-for-ai-observability-integrate-cursor-with-your-mcp/)
> 
> 作者：B. Cameron Gain

[Honeycomb](https://thenewstack.io/honeycomb-says-dont-give-up-on-frontend-observability/) 创建了一个 [模型上下文协议 (MCP)](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype/) 服务器用于[可观测性](https://thenewstack.io/introduction-to-observability/)，这代表了一个雄心勃勃的概念，因为可观测性扩展了其使用和智能。与此同时，它采取了显而易见的步骤，即弄清楚如何通过其 MCP 集成可观测性。

Honeycomb 将您选择的 AI 模型（例如 [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)、Claude Code、Claude Desktop 或 VS Code）直接集成到 IDE 中。当发生好的或糟糕的事情时，无论是为了调试还是分析您的运营或 DevOps 环境中的某些情况，您只需在 IDE 中直接查询它，并释放 ICP，即 Honeycomb 查询的 MCP，正如 Honeycomb 首席执行官 [Christine Yen](https://www.linkedin.com/in/christineyen/) 所描述的那样：“它优雅地解决了代理上下文问题，并加速了 AI 辅助的调试工作流程。”

根据 Honeycomb 的文档：

* AI 代理可以通过在 IDE 中提示它来调查延迟峰值，并且它将使用 MCP 远程运行 Honeycomb 查询并分析跟踪数据。
* MCP 工具经过优化，可避免聊天上下文过载，因此列搜索和跟踪视图等工具可确保代理仅获取相关的遥测数据。

具体来说，Honeycomb 的 MCP 服务器可以访问您环境中所有资源，Honeycomb 的开源主管 [Austin Parker](https://www.linkedin.com/in/austinlparker/) 解释说。这些资源包括面板、触发器、[SLO](https://thenewstack.io/hard-truths-to-consider-when-designing-slos-for-mobile-apps/)、查询等。Parker 说，在适当的客户端（如 Claude Desktop、VS Code 或 Cursor）中运行 MCP 服务器时，您可以为代理提供开放式任务，他们可以使用这些工具来完成这些任务。

Parker 在一篇博客文章中写道，如果您有一个“正在崩溃”的 SLO，Cursor 代理可以检查该 SLO 并在 Honeycomb 中执行调查，以查找更多数据，这些数据可以与您的代码库分析结合使用，以查找和修复错误或提高性能。“一个非常巧妙的技巧是要求代理根据在其他服务（或特定服务）中看到的内容来改进新的或现有服务的检测——它可以使用 Honeycomb 来找出已在使用的特定习语和属性，然后在编辑更多代码时遵循这些模式，”Parker 写道。“它非常擅长将 Honeycomb 与添加到代理上下文的其他数据（例如，OpenTelemetry 语义约定）结合使用，以发现遥测重构的机会（例如，将现有的基于日志的遥测转换为 span）。”

## 建设中

Parker 写道，Honeycomb 在 MCP 服务器设计中面临的最大挑战是“我们的查询数据 API 为任何超出极其基本查询的内容返回的大量令牌”。“虽然这可以通过提示来在某种程度上解决，但这真的只是冰山一角。一些 Honeycomb 帐户可能拥有数万列、数千个触发器和数百个数据集，”Parker 写道。“代理非常容易陷入查询和幻觉的末日循环中，在其中它不断忘记属性的名称，对数据集名称感到困惑等等。”

这个问题不仅仅是 Honeycomb 的问题。其他软件即服务 (SaaS) 工具在构建 MCP 服务器并添加其他集成时也会面临类似的问题。但是，每个 [大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 接口设计都是独一无二的。“您通过标准 JSON API 返回的那种适合程序化访问的响应可能不应该是您返回给 LLM 的内容，”Parker 写道。“MCP 服务器确实提供了一个不错的抽象层，供您在飞行中解决此问题——您可以在返回响应之前对其进行编辑，以简化数据结构、删除不需要的字段等等。”