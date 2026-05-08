<!--
title: Temporal 为其 Durable Execution 平台推出 Serverless 选项
cover: https://cdn.thenewstack.io/media/2026/05/288c979a-525-scaled.jpg
summary: Temporal 在 Replay 2026 大会推出了 Serverless Workers、独立活动及工作流流功能，旨在通过其 Durable Execution 平台提升 AI 应用的可靠性与可观测性，并深化与 OpenAI 的合作。
-->

Temporal 在 Replay 2026 大会推出了 Serverless Workers、独立活动及工作流流功能，旨在通过其 Durable Execution 平台提升 AI 应用的可靠性与可观测性，并深化与 OpenAI 的合作。

> 译自：[Temporal reveals a serverless option for its Durable Execution platform](https://thenewstack.io/temporal-replay-2026-news/)
> 
> 作者：Chris J. Preimesberger

我们都曾梦想过在所做的每件事上都有安全保障——比如在城市交通中远离违章驾驶员、避免疾病，并确保我们吃的食物不会让我们生病。现在，软件开发中出现了实时护栏，可以确保所有代码都能正常工作且永不崩溃，无论其状态如何。

[Durable Execution (持久执行)](https://temporal.io/blog/what-is-durable-execution) 是一种软件开发框架，它通过自动持久化代码状态使代码具有容错性，允许长时间运行的进程在崩溃、网络故障或重启后，从中断的地方精确恢复。它通过记录步骤将脆弱的代码转换为防崩溃的工作流，在无需手动编写错误处理逻辑的情况下确保可靠性。AI 可能会出错，而这些基础设施护栏为生产环境的高效运作提供了必要的基石。

在 AI 驱动的应用、大中小语言模型以及日益沉重的生产负载时代，这种 IT 基础设施领域的相对较新的创新正迅速成为首选的解决方案。它就像在企业 IT 系统所有的计算活动之下，时刻铺设了一张完全值得信赖、富有弹性的救生网。

> “生产级应用需要一定程度的韧性、扩展性和可观测性。”  
> ——Temporal CTO Maxim Fateev

在本周于旧金山举办的 [Replay 2026 大会](https://replay.temporal.io/)上，[Temporal](https://temporal.io) 联合创始人兼 CTO [Maxim Fateev](https://www.linkedin.com/in/fateev/) 将安全作为一个关键信息。

“生产级应用需要一定程度的韧性、扩展性和可观测性，”Fateev 在这场吸引了 2,000 多名开发者的会议上说道。“我们发明了这种新的抽象，在这种抽象中，我们始终保留代码执行的完整状态。这意味着如果任何进程崩溃或发生其他类型的故障，复活的进程将以相同的状态执行并在此后继续执行。”

“例如，你可以编写一个运行一年的函数，我们可以保证这个函数不会消亡，因为我们始终保留它的状态。”

Temporal 成立于 2019 年，基于最初在 Uber 开发的开源 Cadence 工作流编排引擎，目前正在快速增长，拥有超过 1,500 家付费客户（包括 Nvidia、Netflix、Snap 和 Stripe）以及数万名开源用户。

**常见使用案例**

* **订单处理/电子商务：** 一个多步骤的购买流程（库存检查、支付、发货），即使应用服务器在处理过程中重启，也能正确完成。
* **长时间运行的数据管道 (ETL)**：处理大型数据流，其中单个步骤可能会失败或需要数小时才能完成。
* **智能体 AI 工作流：** 复杂的 AI 智能体操作，涉及多个步骤、数据库读取和可能持续几分钟或几小时的外部 API 调用。
* **分布式事务 (Saga 模式)**：协调分布式微服务，如果某一步骤失败，系统将为之前的步骤运行补偿逻辑。

**关于 Temporal 的核心事实**

* **Temporal 忽略业务错误：** Temporal 只处理 *基础设施* 或 *平台* 故障（如进程崩溃）。业务逻辑错误（如账户余额不足）仍由开发者处理。
* **它基本与 AI 无关：** Temporal 没有任何特殊的 AI 功能。它只是让 *任何* 应用程序，包括 AI 应用程序（如智能体循环或 LLM 生成的代码），变得持久耐用。对 Temporal 而言，AI 代码仅仅是代码，而它能让其变得可靠。
* **LLM 代码契合 Temporal：** LLM 非常擅长编写业务逻辑，但由于它们不擅长使代码具有可扩展性和韧性。Temporal 是 LLM 生成代码的理想目标平台，因为它解决了所有韧性问题。
* **谁在使用它？** 所有人，从微型初创公司到巨大的超大规模企业，以及银行等传统客户。HashiCorp 和 DataDog 是基础设施自动化领域的知名用户。
* **商业模式：** Temporal 以基于消耗的模型提供云端/SaaS 后端集群托管服务。公司保证开源模型与云版本之间的完全兼容性。这反映了公司的信念：每位工程师都应该能够获得构建成功、可靠代码所需的工具。

## **来自 Replay 2026 的新闻**

这家总部位于西雅图的公司在会议上宣布了一些 IT 管理员和开发者会感兴趣的创新消息。

[**Temporal 的 Serverless Workers**](https://docs.temporal.io/) 使用户能够在 AWS Lambda 等无服务器计算平台上运行标准的 Temporal Worker。Fateev 表示，无需预置服务器，无需扩展集群，也无需为闲置计算付费。当任务到达时，Temporal 会调用 Worker，任务完成后，Worker 就会关闭。

Serverless Workers 使用与传统长寿命 Worker 相同的 Temporal SDK（软件开发工具包）。用户以相同的方式注册工作流和活动。区别在于生命周期：Temporal 不再运行长寿命进程，而是在任务到达时按需调用 Serverless Worker。Worker 启动、轮询可用任务、处理任务，并在任务完成后退出。

欲深入了解无服务器调用的工作原理，请点击[此处](https://docs.temporal.io/serverless-workers)。

在开场演讲中，联合创始人兼 CEO [Samar Abbas](https://www.linkedin.com/in/samar-abbas-381997/) 介绍了用于实时可观测性的 Workflow Streams 以及用于持久任务处理的 Standalone Activities，两者都旨在帮助开发者可靠地将 AI 系统投入生产。

Abbas 还描述了与 [OpenAI](http://openai.com) 建立合作的可能性。该公司的应用基础设施副总裁 [Venkat Venkataramani](https://www.linkedin.com/in/veeve/) 在台上解释说：“Temporal 的持久编排框架对于处理我们大规模、复杂的智能体工作流、基础设施控制平面和数据管道至关重要，这加强了该平台对于下一代 AI 产品的重要性。”

[**Standalone Activities (独立活动)**](https://docs.temporal.io/standalone-activity) 允许 Temporal Activity 独立运行，而不仅仅是作为工作流内部的步骤。Standalone Activities 让用户能够提高任务处理的持久性和可调试性，并通过采用用户已熟悉的相同模型来消除复杂的队列和重试逻辑。当用例超出单个步骤时，开发者可以在工作流中直接利用该活动，无需重写。

Standalone Activities 现在已在 Go、Python 和 .NET SDK 中提供公开预览版，并在 Java 和 TypeScript SDK 中提供预发布版，且 [Temporal Cloud](https://temporal.io/cloud) 已支持该功能。

[**Workflow Streams (工作流流)**](https://docs.temporal.io/develop/python/workflows/workflow-streams)：这是使用 Temporal 的 Signal & Update 原语的持久流。这些是与运行中的工作流进行交互的机制。Signal 是异步、可靠的消息，用于向工作流发送数据而无需等待响应。Update 是同步、阻塞调用，允许更改工作流状态并接收返回值，取代了复杂的 Signal/Query 模式。

通过 Workflow Streams，用户可以获得令牌批次和应用级更新，以支持响应式 UI、实时监控和护栏。Workflow Streams 旨在实现实时用户输出，同时保留 Temporal 的可靠性模型。该功能目前处于公开预览阶段。