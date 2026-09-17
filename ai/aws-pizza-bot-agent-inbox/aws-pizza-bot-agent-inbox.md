<!--
title: AWS开源Pizza Bot：为后台AI智能体提供邮件风格的收件箱管理工具
cover: https://cdn.thenewstack.io/media/2026/09/fcb2ec0e-je-design-ot1qsiefioq-unsplash-scaled.jpg
summary: AWS开源了Pizza Bot，这是一个为后台运行的AI智能体设计的邮件风格收件箱。它打破了传统聊天界面的限制，支持智能体异步工作，仅在需要人为介入时通知用户，实现了真正的自动化与任务追踪。
-->

AWS开源了Pizza Bot，这是一个为后台运行的AI智能体设计的邮件风格收件箱。它打破了传统聊天界面的限制，支持智能体异步工作，仅在需要人为介入时通知用户，实现了真正的自动化与任务追踪。

> 译自：[AWS open-sources Pizza Bot: email-style inbox for background AI agents](https://thenewstack.io/aws-pizza-bot-agent-inbox/)
> 
> 作者：Paul Sawers

亚马逊云科技 (AWS) 发布了一款名为 [Pizza Bot](https://github.com/pizza-bot-app/pizza-bot) 的全新开源应用程序，旨在为开发者提供一个类似电子邮件的收件箱，用于管理在后台运行的 AI 智能体。

Pizza Bot 旨在解决的核心问题是：聊天界面并不适合那些在人类用户下班或离线后仍需持续工作的智能体。

因此，Pizza Bot 借鉴了电子邮件的经典机制：完成的工作以未读邮件的形式呈现，而任何需要人工决策的事项都会被呈现在显眼位置以供处理。此外，还有一个“活动”面板，用于展示移交给专业智能体的任务，包括其使用的工具和进度。

> “预定的智能体会自动在后台运行，并将更新直接发送到您的收件箱中，以供审核和分类。”

![Pizza Bot](https://cdn.thenewstack.io/media/2026/09/0a03e23c-whyneed-1024x683.png)

*Pizza Bot（图片来源：AWS）*

AWS Startups 首席技术专家、项目共同创建者 [Joseph Dolivo](https://www.linkedin.com/in/josephdolivo/) 在周四的 [LinkedIn 帖子](https://www.linkedin.com/feed/update/urn:li:activity:7503849029357940738/) 中提到，Pizza Bot 将监控智能体工作的负担从用户身上完全卸下。

他写道：“您不必主动发起每一次对话或等待提示，预定的智能体会自动在后台运行，并将更新直接发送到您的收件箱中，以供审核和分类。”

正如为了强调这一观点，在周四该项目正式发布的 [博客文章](https://aws.amazon.com/blogs/opensource/introducing-pizza-bot-an-open-source-inbox-for-ai-agents-that-work-in-the-background/) 中，创建者们指出，用户不在场实际上是其设计方案的核心原则。

> “该界面默认您不在监视。”

他们写道：“该界面默认您不在监视。我们还没见过其他产品从这个角度出发，而正是这一假设让您能够拥有跨越会话的停顿、值得采取行动的通知，以及生成任务线（Threads）而非仅仅是日志的预定工作。”

尽管有着亚马逊的背景，但 Pizza Bot 目前实际上是一个独立的社区项目，而非一项 AWS 服务。它拥有自己的 [GitHub 组织](https://github.com/pizza-bot-app/)，与亚马逊分离，不提供任何 AWS 支持或服务水平协议——它是完全自托管的。

Pizza Bot 本身是一款适用于 macOS、Windows 和 Linux 的桌面应用程序，同时也提供浏览器和终端客户端。默认情况下，该应用会在本机启动一个本地 Pizza Bot 服务器，开发者可以自行选择底层模型——包括 Anthropic、Amazon Bedrock、Google Gemini、OpenAI、OpenRouter 或通过 Ollama 运行的本地模型。

它还可以通过 MCP 服务器和智能体技能进行扩展；例如，捆绑的浏览器自动化技能使用 [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) 来导航和交互网站。

![通过 Playwright MCP 实现的浏览器技能](https://cdn.thenewstack.io/media/2026/09/48cd699e-extend-1024x683.png)

*通过 Playwright MCP 实现的浏览器技能（图片来源：AWS）*

该服务器也可以运行在始终在线的主机或容器中，让预定的智能体在笔记本电脑合上后继续工作，之后可以在另一台设备上查看其工作动态。

## 技术内幕：LangGraph 与环境智能体（Ambient Agents）

Pizza Bot 的智能体运行时构建于 [DeepAgents](https://www.langchain.com/deep-agents) 之上，这是 LangChain 用于长时间运行智能体任务的开源工具，其底层运行在 [LangGraph](https://www.langchain.com/langgraph)（其用于有状态智能体执行的运行时）之上。这一切的核心在于持久性：LangGraph 在智能体工作时会对其状态进行检查点（checkpoint）处理，允许任务在需要审批时停止、在客户端断开连接后保持状态，并在稍后恢复，而无需从头开始。Pizza Bot 将这些检查点以及任务线和其他应用程序数据本地存储在 SQLite 和普通文件中。

值得注意的是，AWS 自 2025 年 5 月起就有自己的开源智能体 SDK [Strands Agents](https://strandsagents.com/)，但有证据显示（包括该 [示例仓库](https://github.com/aws-samples/langgraph-agents-with-amazon-bedrock) 中的文本），AWS 将 Strands 视为“对于不需要显式图控制流的智能体而言，是一种比 LangGraph 更轻量级的替代方案”。

在回应 *The New Stack* 在 LinkedIn 上提出的问题时，Dolivo 表示他们本可以为 Pizza Bot 使用 Strands，特别是 Strands 现在支持 [TypeScript](https://aws.amazon.com/about-aws/whats-new/2025/12/typescript-strands-agents-preview/) 和 [工作流](https://strandsagents.com/docs/user-guide/concepts/multi-agent/workflow/)。但他解释说，最终选择 LangGraph 是“因为其工具成熟度高，且生态系统广泛”。

“它对许多开发者来说也更熟悉，考虑到我们要将其开源，我们希望降低社区采用的门槛，”他补充道。

Pizza Bot 的理念也与 LangChain 早在 2025 年 1 月提出的想法非常接近，当时首席执行官 Harrison Chase 引入了“[环境智能体（Ambient Agents）](https://www.langchain.com/blog/introducing-ambient-agents)”这一术语，指那些能够响应事件、并发工作且仅在必要时才需要人类参与的智能体。LangChain 的参考实现是一个 [构建在 LangGraph 之上的电子邮件助手](https://github.com/langchain-ai/executive-ai-assistant)。它还开发了所谓的“[智能体收件箱（Agent Inbox）](https://www.langchain.com/blog/introducing-ambient-agents#agent-inbox)”：一个受电子邮件和客户支持软件启发的独立界面，用于跟踪人与后台智能体之间未完成的交互。

## 从“JoeBot”到 Pizza Bot

Pizza Bot 的起源可以追溯到 2025 年 4 月，当时 Dolivo 启动了一个他称之为“业余爱好项目”的“JoeBot”，用于自动化重复性的 CRM 日志记录。后来，他与同事 [Igor Fil](https://www.linkedin.com/in/igorvfil/) 合作，将该脚本转化为 Pizza Bot，这是一个可以在其内部系统执行参数化、确定性“配方”的 MCP 服务器。

这种吸引力很快超出了构建它的工程师范围，传播到非技术领域。随着项目的演进，Dolivo 表示它最终在亚马逊内部拥有了超过 30 名贡献者和超过 2,000 名用户，因此 Pizza Bot 需要一个人们可以打开并使用的前端。

“MCP 服务器需要 MCP 客户端，而指望非技术用户在 IDE 或终端中操作是行不通的，”Dolivo 补充道。“我们必须在人们实际工作的地方满足他们的需求，并端到端地掌控这种体验。”

结果就是本周发布的 Pizza Bot 版本：一个以收件箱而非终端为核心的桌面应用程序。