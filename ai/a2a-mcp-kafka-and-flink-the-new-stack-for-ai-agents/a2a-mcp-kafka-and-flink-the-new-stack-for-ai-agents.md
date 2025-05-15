<!--
title: A2A、MCP、Kafka和Flink：AI Agent的新堆栈
cover: https://cdn.thenewstack.io/media/2025/04/a2f99b46-a2a-mcp-kafka-flink-stack-ai-agent.jpg
summary: AI Agent新堆栈来袭！Google的**A2A**协议、Anthropic的**MCP**协议，加上**Apache Kafka**和**Apache Flink**，构建云原生Agent互联互通的未来。摆脱Agent孤岛，实现实时、可观测、可扩展的智能生态系统，速来围观！
-->

AI Agent新堆栈来袭！Google的**A2A**协议、Anthropic的**MCP**协议，加上**Apache Kafka**和**Apache Flink**，构建云原生Agent互联互通的未来。摆脱Agent孤岛，实现实时、可观测、可扩展的智能生态系统，速来围观！

> 译自：[A2A, MCP, Kafka and Flink: The New Stack for AI Agents](https://thenewstack.io/a2a-mcp-kafka-and-flink-the-new-stack-for-ai-agents/)
> 
> 作者：Sean Falconer

在 Web 出现超文本传输协议 (HTTP) 之前，在电子邮件出现简单邮件传输协议 (SMTP) 之前，我们一直受困于自定义集成、碎片化系统和脆弱的工作流程。直到开放协议和共享基础设施出现，互联网才真正实现了规模化，解锁了现代 Web、全球通信和整个经济体。

今天，[AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 也处于这个预标准化阶段。它们功能强大、能力出色且数量快速增长，但它们无法协同工作。一个 agent 分析数据。另一个 agent 起草代码。第三个 agent 自动化客户关系管理 (CRM) 工作流程。但它们是孤立的、各自为政的，并且不知道彼此的存在。

这种情况正在开始改变。

一个新的堆栈正在涌现，以支持互联网的下一层——这一层不是为浏览网站的人类而构建，而是为跨系统协作的自主 agent 而构建。其核心是四个开放组件：

*   用于 agent 发现和通信的协议。[Google 的 Agent2Agent (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
*   用于工具使用和外部上下文的标准。[Anthropic 的模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)
*   用于可靠、解耦协调的事件驱动通信结构。[Apache Kafka](https://kafka.apache.org/)
*   用于丰富、监控和处理 agent 活动流的实时处理引擎。[Apache Flink](https://flink.apache.org/)

让我们探讨一下这些技术如何协同工作，为什么仅靠协议是不够的，以及这个新堆栈如何提供从断开连接的机器人到动态、智能 agent 生态系统所需的基础设施。

## 问题：碎片化的 Agent，脆弱的基础设施

如果炒作是正确的——而且它看起来更像是不可避免的，而不是猜测——大多数公司不会只部署一个 AI agent；他们会部署几十个。这些 agent 将编写代码、分类支持请求、分析客户数据、管理入职、监控基础设施等等。

但今天的工具还没有为那个未来做好准备。

![](https://cdn.thenewstack.io/media/2025/04/4af93a6d-fragmented-agents-1013x1024.png)

*Agent 孤岛 (来源: Confluent)*

我们不仅面临[“Agent 孤岛”问题](https://medium.com/@seanfalconer/the-ai-silo-problem-how-data-streaming-can-unify-enterprise-ai-agents-0a138cf6398c)，即 agent 在孤岛中运行且无法通信；我们还面临着更广泛的生态系统碎片化问题：

*   **Agent 之间不通信**：每个 agent 都在自己的沙箱中运行。CRM agent 不知道数据仓库 agent 刚刚发现了什么。支持 agent 无法响应监控 agent 刚刚标记的相同异常。
*   **工具使用是脆弱且定制的**：如果没有调用工具或外部 API 的标准，agent 最终会使用硬编码的集成和不可重用的逻辑。
*   **框架缺乏一致性**：不同的 agent 运行时使用不同的模型——有些将 agent 视为聊天机器人，有些将 agent 视为有向无环图 (DAG)，有些将 agent 视为递归规划器。没有可移植的执行层或共享状态。
*   **我们构建的方式好像 agent 存在于笔记本中**：今天的大多数 agent 都被设计成一次性原型——线性的、同步的和短暂的。但真正的系统不是笔记本。它们需要处理重试、故障、协调、日志记录和扩展。这需要基础设施。
*   **没有协作的骨干**：没有事件总线，没有共享内存，没有 agent 所做的事情或原因的可追溯历史。一切都锁定在直接 HTTP 调用中或埋在日志中。

正如 [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) 项目所认为的那样，agent 需要遵循云原生原则：它们必须是可观测的、松散耦合的、可重现的和基础设施感知的。但今天，大多数 agent 都是作为脆弱的脚本构建的，由手工拼接在一起，并假定它们是孤立运行的。

结果是什么？孤岛。重复。脆弱性。

解决方案不是将所有 agent 塞进一个单一的平台。而是构建一个共享堆栈，一个基于开放协议、事件驱动架构和实时处理的新基础。

Agent2Agent 通过为 agent 提供用于发现和通信的通用协议来解决部分问题。但是，要超越玩具演示，要达到生产系统所需的规模和可靠性，我们需要的不只是协议。我们需要基础设施。

## Agent 如何对话和行动：A2A 和 MCP
正如前面提到的，今天的 Agent 生态系统很像早期的 Web：强大的系统，每个都在做有用的工作，但都是孤立且不兼容的。就像浏览器曾经在没有标准协议的情况下难以与服务器通信一样，今天的 AI Agent 也不能轻易地发现、通信或相互协作。

Google 的 A2A 协议是一项大胆的尝试，旨在解决这个问题。它不是另一个 Agent 框架：它是一个通用协议，旨在连接*任何* Agent，无论谁构建的它或它在哪里运行。

就像 HTTP 标准化了网站的通信方式一样，A2A 定义了一种 Agent 之间的共享语言。它允许它们：

*   **通过`AgentCard` 宣布功能**，这是一个 JSON 描述符，用于声明 Agent 可以做什么以及如何与之交互。
*   **通过结构化交互（使用 JSON-RPC）发送和接收任务**，其中一个 Agent 请求帮助，另一个 Agent 响应结果或“artifacts”。
*   **使用服务器发送事件 (SSEs) 流式传输更新**，从而在长时间运行或协作任务期间实现实时反馈。
*   **交换富内容**。文件、结构化数据和表单——而不仅仅是纯文本——都是 A2A 消息的一流组成部分。
*   **默认情况下保持安全**，这要归功于对 HTTPS、身份验证和权限的内置支持。

A2A 的前景在于它没有试图重新发明轮子。它借鉴了数十年的互联网协议历史，就像 HTTP 和 SMTP 所做的那样，利用了熟悉的、经过实战考验的 Web 标准。这使得采用更容易，集成更快。

但 A2A 只是整个图景的一半。

Anthropic 的 MCP 解决了另一半：Agent 如何使用工具和访问上下文。MCP 标准化了 Agent 如何调用 API、调用函数以及与外部系统集成——本质上，它们如何在世界中思考和行动。另一方面，A2A 定义了 Agent 之间如何相互交谈。

如果说 MCP 是关于让 Agent 访问工具，那么 A2A 就是关于让他们访问彼此。

这两个协议共同为互联的 Agent 生态系统提供了一个蓝图：

*   **MCP**为单个 Agent 提供智能。
*   **A2A**实现集体智能。

正如 HTTP 和 SMTP 没有孤立地成功一样，它们需要采用、基础设施和开发者工具，A2A 和 MCP 也需要一个生态系统来实现它们的潜力。

但是，即使有了像 A2A 和 MCP 这样的标准化，一个根本问题仍然存在：这些 Agent 通信如何在复杂、动态的企业环境中有效地扩展？仅仅依靠这些协议定义的直接、点对点连接会带来自身的一系列挑战，尤其是在可扩展性、弹性和可观测性方面。 这使我们认识到需要一个强大的底层通信基础设施。

## 我们需要一个事件驱动的骨干，而不仅仅是协议

想象一下，经营一家公司，每个员工只能通过发送直接的、一对一的消息进行沟通。需要分享更新？您必须单独向每个人发送消息。想要协调五个团队的项目？您会被困在手动在每个团队之间传递信息。

现在想象一下，尝试将其扩展到数百名员工。混乱。

这正是构建在直接连接上的 Agent 生态系统中发生的事情。每个 Agent 必须知道与谁交谈、如何联系他们以及他们何时可用。随着 Agent 数量的增长，所需连接的数量呈指数增长。系统变得脆弱、难以管理且几乎不可能扩展。

A2A 和 MCP 为 Agent 提供了沟通和行动的语言和结构，但仅有语言是不够的。为了协调企业中的数十个或数百个 Agent，您还需要基础设施来支持这些消息的移动方式以及 Agent 如何对它们做出反应。

这就是 [Apache Kafka 和 Apache Flink](https://thenewstack.io/building-a-meal-planning-agent-with-apache-kafka-and-flink) 的用武之地。

### Kafka 和 Flink：快速入门

[Apache Kafka](https://www.confluent.io/lp/apache-kafka/?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.kafka_mt.xct_rgn.namer_sbrgn.unitedstates_lng.eng_dv.all_con.kafka-what-is_term.what-is-apache-kafka&utm_term=what%20is%20apache%20kafka&creative=&device=c&placement=&gad_source=1&gbraid=0AAAAADRv2c0xMf9u9gysZ9gIjG7xOxO7U&gclid=Cj0KCQjw_JzABhC2ARIsAPe3ynpCOCYZ1DXfQO31ozymoakcUf_1NqNVBaKF0U7DNqQkc2-ZPmFMlpYaAoKmEALw_wcB) 是一个分布式事件流平台，最初由 LinkedIn 开发，现在是 Apache 软件基金会的一部分。它充当持久、高吞吐量的消息总线，允许系统实时发布和订阅事件流。Kafka 被广泛使用，从金融系统到欺诈检测再到遥测管道，因为它将生产者与消费者分离，并[确保数据](https://thenewstack.io/how-to-handle-bad-data-in-event-streams/)是持久的、可重放的和可扩展的。
[Flink](https://www.confluent.io/learn/apache-flink/), 同样也是一个 Apache 项目，是一个实时流处理引擎。它从一开始就被设计用于有状态、高吞吐量、低延迟的事件处理。Kafka 负责数据的移动，而 Flink 负责在数据流经系统时对其进行转换、丰富、监控和编排。
它们共同构成了一个强大的组合：Kafka 是血液，Flink 是反射系统。

## Kafka 和 Flink：Agent 生态系统的基础设施

正如 A2A 正在成为 agent 世界的 HTTP 一样，Kafka 和 Flink 构成了事件驱动的基础，可以支持可扩展的 agent 通信和计算。它们解决了直接的点对点通信无法解决的问题：

- **解耦**：使用 Kafka，agent 不需要知道谁将消费它们的输出。它们将事件（例如，`"TaskCompleted"`, `"InsightGenerated"`）发布到主题；任何感兴趣的 agent 或系统都可以订阅。
- **可观测性和可重放性**：Kafka 维护每个事件的持久、按时间排序的日志，使 agent 行为完全可追溯、可审计和可重放。
- **实时决策**：Flink 使 agent 能够[实时响应事件流](https://thenewstack.io/real-time-ai-apps-using-apache-flink-for-model-inference/)，根据动态条件过滤、丰富、连接或触发操作。
- **弹性和扩展**：Flink 作业可以独立扩展、从故障中恢复并在长时间运行的工作流中保持状态。这对于执行复杂的多步骤任务的 agent 至关重要。
- **流原生协调**：agent 可以通过事件流进行协调，发布更新、订阅工作流并协同推进状态，而不是等待同步响应。

简而言之：

- A2A 定义了 agent 如何说话。
- MCP 定义了它们如何对外部工具采取行动。
- Kafka 定义了它们的消息如何流动。
- Flink 定义了这些流如何被处理、转换并转化为决策。

## A2A、MCP、Kafka 和 Flink 如何协同工作
像 A2A 和 MCP 这样的协议对于标准化 agent 行为和通信至关重要。但是，如果没有像 Kafka 这样的事件驱动底层和像 Flink 这样的流原生运行时，这些 agent 仍然会陷入孤立的交互中，无法灵活地协调、优雅地扩展或随着时间的推移进行推理。

为了充分实现企业级、可互操作的 AI agent 的愿景，我们需要四个层次：

- **协议**：A2A, MCP – 定义*什么*。
- **框架**：LangGraph, CrewAI, ADK – 定义*如何*。
- **消息传递基础设施**：Apache Kafka – 支持*流动*。
- **实时计算**：Apache Flink – 支持*思考*。

总而言之，这是 AI agent 的新互联网堆栈——构建不仅智能，而且协作、可观测和可用于生产的系统的基础。

![架构图：A2A、MCP、Kafka 和 Flink 如何协同工作](https://cdn.thenewstack.io/media/2025/04/ebbd97e8-a2a-mcp-kafka-flink-architecture.png)

*A2A、MCP、Kafka 和 Flink 如何协同工作。（来源：Confluent）*

## 前进的道路：构建集体智能
我们正处于软件发展的关键时刻。

正如最初的互联网堆栈——像 HTTP 和 SMTP 这样的协议，以及像 TCP/IP 这样的基础设施——开启了全球互联互通的新时代一样，一个新的堆栈正在为 AI agent 涌现。但与人类浏览页面或发送电子邮件不同，这个堆栈是为自主系统协同工作以进行推理、决策和行动而构建的。

A2A 和 MCP 提供了 agent 通信和工具使用的协议。Kafka 和 Flink 提供了实时协调、可观测性和弹性的基础设施。它们共同使得从断开连接的 agent 演示到可扩展的、智能的生产级生态系统的转变成为可能。

这不仅仅是解决工程挑战。这是关于启用一种新型软件，其中 agent 跨越边界进行协作，实时提供洞察和行动流，从而使智能成为一个分布式系统。

但是这个愿景不会自行实现。我们需要构建它：开放地、可互操作地，并牢记上次互联网革命的教训。

因此，下次您构建 agent 时，不要只问它能做什么。问问它如何适应更大的系统。它能沟通吗？它能协调吗？它能进化吗？

因为未来不仅仅是 agent 驱动的；它是 agent 连接的。