
<!--
title: 谷歌向 Linux 基金会捐赠 Agent2Agent 协议
cover: https://cdn.thenewstack.io/media/2025/06/68d2dd72-img_1173-scaled.jpg
summary: 谷歌将其 Agent2Agent (A2A) 协议捐赠给 Linux 基金会，旨在促进 AI 代理之间的互操作性。A2A 专注于代理之间的连接，而 Anthropic 的模型上下文协议 (MCP) 则侧重于代理与工具和数据源的连接。两者相互补充，共同推动 AI 领域的发展。
-->

谷歌将其 Agent2Agent (A2A) 协议捐赠给 Linux 基金会，旨在促进 AI 代理之间的互操作性。A2A 专注于代理之间的连接，而 Anthropic 的模型上下文协议 (MCP) 则侧重于代理与工具和数据源的连接。两者相互补充，共同推动 AI 领域的发展。

> 译自：[Google Donates the Agent2Agent Protocol to the Linux Foundation](https://thenewstack.io/google-donates-the-agent2agent-protocol-to-the-linux-foundation/)
> 
> 作者：Frederic Lardinois

今年四月，谷歌在其 Cloud Next 大会上宣布了 [Agent2Agent (A2A) 协议](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/)。该协议旨在让 AI 代理更容易[相互交流](https://thenewstack.io/why-are-agent-protocols-like-mcp-and-a2a-needed/)，无论它们使用何种框架构建。由于如今 AI 领域的一切都以闪电般的速度发展，因此在丹佛举行的开源峰会上，谷歌今天[宣布](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)已将该协议捐赠给 Linux 基金会，并将其转移[到一个新的 GitHub 存储库](https://github.com/a2aproject/A2A)。

与谷歌一同加入这个名为 Agent2Agent 的项目的公司包括 AWS、Cisco、Salesforce、SAP 和 ServiceNow。该项目将负责管理协议本身的未来发展，以及 SDK、NPM 包和其他开发者工具。

与类似项目一样，此处的目的是建立代理互操作性的开放标准，围绕该标准培育一个生态系统，并基于标准的 Linux 基金会框架，确保中立的管理。

“当我们开始设计 Agent2Agent 时，我们就知道我们需要一个真正开放的协议，它可以为任何人服务，无论是个人开发者还是大型企业，”谷歌的软件工程师 [Mike Smith](https://www.linkedin.com/in/mike-smith-4b6779107/) 在他的开源峰会主题演讲中表示，他一直在内部推动该项目。“我们知道它需要独立且与供应商无关 […]。因此，我们有了这样的梦想：如果我们能加入 Linux 基金会呢？我看到了其他 Linux 基金会项目的成功。”

## 但 MCP 呢？

[![](https://cdn.thenewstack.io/media/2025/06/ca0013ef-img_1177-scaled.jpg)](https://cdn.thenewstack.io/media/2025/06/ca0013ef-img_1177-scaled.jpg)

*图片来源：The New Stack/Frederic Lardinois。*

在他的主题演讲中，Smith 还谈到了一个关于 A2A 的常见误解：它并非旨在与 [Anthropic 的模型上下文协议](https://thenewstack.io/mcp-is-rss-for-ai-more-use-cases-for-model-context-protocol/) (MCP) 竞争。虽然 MCP 是代理协议中的一个突破性成果，但 MCP 背后的想法是将代理连接到工具和数据源。A2A 的全部意义在于将代理彼此连接。这包括（除其他事项外）使它们可被发现，并帮助它们宣传自己拥有的能力，以便一组代理可以更有效地协同工作以解决给定的问题。

“MCP 很有意义。它绝对是作为与工具交互的协议而流行的，”Smith 说。“代理有点奇怪。它们有点模糊。当您与代理交互时，会发生更多的协商过程。”Smith 解释说，您可能会要求代理做某事，而该代理可能会要求您提供更多信息，或者让您知道它可以完成给定任务的一部分，但不能完成全部。

MCP 和 A2A 相互补充，但正如 Smith 也强调的那样，这些协议仍处于早期阶段，他预计未来会看到更多这样的协议。

[![](https://cdn.thenewstack.io/media/2025/06/8870d006-img_1179-scaled.jpg)](https://cdn.thenewstack.io/media/2025/06/8870d006-img_1179-scaled.jpg)

*图片来源：The New Stack/Frederic Lardinois。*