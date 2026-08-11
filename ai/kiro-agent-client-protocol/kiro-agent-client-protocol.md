<!--
title: 自由代理：AWS Kiro 如何让代理摆脱编辑器的束缚
cover: https://cdn.thenewstack.io/media/2026/08/c3134c2c-egor-komarov-jrlhwxzoboc-unsplash-scaled.jpg
summary: 本文介绍了 AWS Kiro 如何通过采用代理客户端协议（ACP）实现编辑器与 AI 编码代理的解耦。这一架构变革使开发者能独立选择工具与代理，类似于 LSP 对语言工具的革新，正推动 AI 编程进入标准化、可互操作的新阶段，而治理能力将成为未来的核心竞争力。
-->

本文介绍了 AWS Kiro 如何通过采用代理客户端协议（ACP）实现编辑器与 AI 编码代理的解耦。这一架构变革使开发者能独立选择工具与代理，类似于 LSP 对语言工具的革新，正推动 AI 编程进入标准化、可互操作的新阶段，而治理能力将成为未来的核心竞争力。

> 译自：[Free agents: How AWS Kiro could untie agents from editors](https://thenewstack.io/kiro-agent-client-protocol/)
> 
> 作者：Janakiram MSV

**选择一个编码代理（coding agent）可能很快就不再意味着**必须同时选择一个新的编辑器或终端。随着 AWS 解释了 [Kiro](https://thenewstack.io/aws-kiro-mobile-ios-agentic-coding/) 如何通过围绕“代理客户端协议”（Agent Client Protocol，简称 ACP）构建的单一架构取代三个独立的代理套件，这一设想在本周变得更加真实。此举使 Kiro 的客户端能够通过共享协议与代理进行通信。它最终可能让开发者能够独立地选择他们的编码工具和 AI 代理。

该集成开发环境（IDE）此前依赖于 TypeScript 套件，命令行工具（CLI）使用 Rust，而 Web 端体验则依赖于 Python。这些现在已被[整合](https://kiro.dev/blog/one-agent/)为一个单一的独立代理套件，作为与工作区并行的独立进程运行。

工程上的简化值得注意，但架构上的决定更为深远：AWS 选择 [代理客户端协议](https://agentclientprotocol.org/) (ACP) 作为 Kiro 客户端与 Kiro 自有代理之间的接口。ACP 起源于 [Zed](https://thenewstack.io/fast-rust-based-zed-code-editor-finally-arrives-on-windows/)，目前正与 [JetBrains](https://thenewstack.io/jetbrains-independent-ai-coding/) 联合开发。通过即使为第一方组件也采用生态系统协议，AWS 正在将客户端与代理的边界视为一种标准化接口，而非专有的实现细节。

## 协议成为了架构边界

Kiro 的工程师们描述了一种任何构建过可扩展软件的人都会熟悉的演进过程。早期使用共享库的尝试未能保持分离。客户端应用程序通过深入内部 API，逐渐积累了特定于代理的逻辑，使得边界变得越来越松散。

将代理移入独立进程解决了这个问题。现在客户端完全通过 ACP 进行通信，而执行环境则成为了一种实现细节。无论代理是在开发者工作站本地运行，还是在云端沙箱中运行，客户端都使用相同的协议进行交互。

> 协议保持标准；差异化通过扩展实现。

AWS 刻意扩展了 ACP，而不是创建专有变体。团队引入了 20 多个可由代理调用的方法、15 个可由客户端调用的方法以及 20 种通知类型，所有这些都命名空间化在 `_kiro/` 下。它还为 Web 和 iOS 客户端实现了 WebSocket 传输，同时继续使用 ACP 的标准 stdio 传输进行本地执行。诸如自定义代理和生命周期钩子之类的扩展现在在每个 Kiro 界面上共享一个通用的配置模型，而每个客户端仍然可以自由地提供原生的用户体验和平台特定的工具。

## AWS 在得出这一结论的过程中并不孤单。

多家供应商正得出相同的结论。

[微软在 6 月的 Build 大会上介绍了 Intelligent Terminal 0.1](https://thenewstack.io/microsoft-intelligent-terminal-ai-agents/)，作为一个实验性的 ACP 客户端，可以发现本地安装的代理 CLI。GitHub Copilot CLI 作为默认代理，但该架构在设计时就有意支持多种实现。

JetBrains 紧随其后，在 7 月通过 ACP 将 [Junie](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/) 引入了 [ReSharper](https://blog.jetbrains.com/dotnet/2026/07/22/resharper-2026-2-release/) 2026.2。该公司将此次集成描述为迈向更广泛协议支持的早期步骤，而非最终实现。

尽管这些公告在成熟度上存在显著差异，但它们都汇聚在相同的架构原则上。微软使用 ACP 将终端与代理实现解耦。JetBrains 正在将其 IDE 栈引入该协议。AWS 则在其自身产品内部标准化了这一边界。

这种模式与“语言服务器协议”（Language Server Protocol，LSP）为编程语言工具所实现的成就非常相似。LSP 将编辑器与语言智能分离。ACP 开始将开发者体验与代理实现分离。每个编辑器无需再为每个代理构建定制的集成，双方都可以针对一个通用协议进行开发，从而将集成复杂度从 N × M 关系降低为 N + M。

> 协议在不消除产品差异化的前提下建立了互操作性。

供应商特定的能力不可避免地会重新引入一些专业化。Kiro 的命名空间扩展说明了这种权衡。第三方 ACP 客户端获得标准化的体验，而 Kiro 自有的客户端则受益于更丰富的功能，包括实时引导、规范和高级权限管理。

## 治理成为新的竞争层

标准化通信将创新转移到了其他地方。

Kiro 最显著的差异化在于策略管理，而非传输。该平台用一个统一的能力模型取代了两个不兼容的权限系统，该模型由 [Cedar](https://thenewstack.io/aws-kubernetes-invisible-simplicity/) 提供支持，这是 AWS 设计的一种采用形式化验证技术的授权语言。

此前，CLI 依赖于正则表达式允许和拒绝列表，而 IDE 实现了基于前缀的匹配。新的能力模型围绕功能意图抽象了权限。诸如 `fs_read`、`fs_write`、`shell`、`web_fetch`、`mcp` 和 `subagent` 等能力代表了操作类别，而非单个工具。例如，拒绝 `fs_read` 会阻止所有文件读取操作，无论执行它们的是哪个工具。

策略在多个范围内进行评估，包括 MDM、用户、工作区、代理配置文件和会话，其中明确的拒绝规则优先。

ACP 本身仅提供基本的工具批准语义。AWS 在此基础上构建了一个相当丰富的治理模型。随着企业采用率的加速，这一层很可能成为主要的差异化点。身份集成、审计、授权、策略继承和沙箱化将至少与协议兼容性一样重要。

区分 ACP 与 MCP 也非常重要。MCP 标准化了代理如何与外部工具和服务通信。ACP 标准化了客户端如何与代理通信。它们处理的是栈的互补层，而非相互竞争。

## 一个没有默认分发的生态系统标准

ACP 采用过程中一个值得注意的方面是它出现在了哪里，以及它没有出现在哪里。

截至 2026 年 8 月，[Visual Studio Code](https://thenewstack.io/vs-code-becomes-multi-agent-command-center-for-developers/) 尚未采用 ACP 作为其编辑器与代理架构之间的原生边界。微软的 ACP 实现目前出现在 Intelligent Terminal 中，而不是编辑器本身。

> 一旦客户端-代理边界实现标准化，代理就变成了可替换的组件，而不是嵌入在各个开发工具中的紧密耦合的功能。

尽管缺乏业内最大的编辑器平台，ACP 仍在各个独立实现中不断获得动力。这表明该协议的成功是基于架构本身的优点，而不仅仅是分发优势。

对于开发者而言，这指向了一个根本性的转变。他们使用的编辑器或终端不再需要决定他们运行哪种编码代理。这些决定正逐渐变得独立。一旦客户端-代理边界实现标准化，代理就变成了可替换的组件，而不是嵌入在各个开发工具中的紧密耦合的功能。