AI Agent 在演示中表现惊艳，却可能在生产环境中频频出错。Diagrid 的 Catalyst 2.0 旨在提升 Agent 的韧性，并确保其操作在处理高风险任务时具备防篡改记录。

随着 Catalyst 2.0 的发布，[Diagrid](https://www.diagrid.io) 于周二为使用 LangGraph、Microsoft Agent Framework、Google Agent Development Kit、OpenAI Agents SDK 及其他主流框架构建的 Agent 添加了持久化执行和认证层。

该公司指出，此举并非为了让开发者采用另一种新的 Agent 框架，而是让 Catalyst 在现有框架之下运行，并将 Agent 的模型调用、工具调用和交接步骤转化为持久化工作流中的环节。Diagrid 表示，这使得 Agent 在中断时能从上一个完成的步骤恢复，而无需从第一步开始重复整个过程。

“如果 Agent 接收到一个任务，决定运行 100 个工具，却在第 99 个步骤失败，它确实需要从第 99 步重新启动，”Diagrid 联合创始人兼 CTO Yaron Schneider 告诉 *The New Stack*。

Catalyst 基于开源的 [Distributed Application Runtime (Dapr)](https://dapr.io/) 构建（Diagrid 团队曾在微软参与过该项目的开发），并利用其内置的工作流引擎。对于每个支持的 Agent 框架，Diagrid 都提供了一个运行器，用于拦截框架的执行循环，并将操作注册为工作流活动。

“我们接入了它们的 Agent 运行器生命周期，本质上能够实时获取正在执行的 Agent 步骤，并将其作为 Catalyst 工作流引擎的工作流步骤进行注册，”Schneider 说道。

![](https://cdn.thenewstack.io/media/2026/07/d45f2419-catalyst-architecture-light-1024x504.png)

*图片来源：Diagrid*

例如，在 LangGraph 应用中，开发者像往常一样编译图，并将其传递给 Diagrid 的 `DaprWorkflowGraphRunner`。Catalyst 会记录模型和工具调用的输入输出。Dapr 的工作流运行时可以在崩溃后重放编排过程，同时返回已完成活动的存储结果，而无需再次执行它们。

值得注意的是，对于 LangGraph 用户来说，这并不是第一种持久化执行方式。[LangGraph 自身的持久化层](https://docs.langchain.com/oss/python/langgraph/persistence)会在超步边界保存状态，并支持从最后一个成功步骤恢复。其 Agent Server 也提供了持久化任务队列和检查点。

Diagrid 的观点是，Catalyst 在超过 10 个框架中提供了统一的执行模型，并将其扩展到了单个模型和工具调用，且无需开发者为每个框架构建单独的恢复逻辑。Schneider 表示，LangGraph 无疑是 Diagrid 客户中最常见的框架，AWS Strands 和 Microsoft Agent Framework 也均有涉及。他表示，虽然其他受支持的框架属于长尾市场，但支持它们的开发难度很低，因此对 Diagrid 来说非常合理。

## 运行过程的签名记录

然而，Catalyst 2.0 还有第二个部分，对于许多企业用户而言，这一点或许同样重要。通过此次更新，该工具现已将 [Dapr 1.18](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-history-signing/) 中引入的工作流历史签名功能引入到受支持的 Agent 框架中。

“我们保留了一个类似于账本、日记的东西，”Schneider 说。“我们记录输入，记录输出，记录我们与哪些系统进行了交互。”

他将结果描述为一个不可变存储，但也指出 Catalyst 并未将任意数据库变成区块链。它创建了一个签名历史记录，一旦发生后续修改，即可被发现。

Dapr 对批量工作流历史事件计算 SHA-256 摘要，将每个摘要链接到前一个签名，并使用 Dapr sidecar 的 [Secure Production Identity Framework for Everyone (SPIFFE)](https://spiffe.io/) 标识对结果进行签名。它将这些签名和证书与工作流历史一起存储，并在加载工作流状态时验证链条。如果有人修改、删除或重新排序了存储的事件，该验证链就会断裂。

Schneider 表示，Catalyst 客户可以使用自己的证书并保留加密的历史记录，即使在不再运行 Catalyst 的情况下也可以进行检查。该平台可以使用客户选择的数据库，而哈希链则提供了防篡改证据。

## 合规问题的关键一环

Diagrid 将这种防篡改记录定位为对金融服务、医疗保健和其他受监管行业有用。CEO Mark Fussell 表示，公司交流过的一些金融高管认为，缺乏可验证的记录是阻碍在敏感工作流中部署 Agent 的主要障碍。

欧盟《人工智能法案》（AI Act）是 Diagrid 此刻提出这一观点的另一个原因。《人工智能法案》的[第 12 条](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12)要求高风险 AI 系统支持自动事件记录，以便操作员能够追踪其行为、识别风险并监控已部署的系统，而签名的执行历史记录可以帮助满足这一要求。

Fussell 表示，Catalyst 旨在与企业已使用的云服务提供商的 Agent 服务并行运行。团队可以在使用 Catalyst 进行恢复和记录签名工作流历史的同时，保留提供商的身份验证、评估和可观测性系统。Catalyst 可以作为 Diagrid 托管的服务运行，也可以在客户的环境中运行，包括气隙环境。

Diagrid 未披露该新版本的定价。