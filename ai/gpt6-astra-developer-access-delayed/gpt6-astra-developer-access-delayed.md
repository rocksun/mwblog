<!--
title: “对混乱的发布表示歉意”：OpenAI在揭幕次日向大部分付费用户推出GPT-6 Astra
cover: https://cdn.thenewstack.io/media/2026/09/f7f96e5e-dima-pechurin-jubjyfvcv00-unsplash-scaled.jpg
summary: OpenAI在发布GPT-6 Astra后因 rollout 进度迟缓引发用户不满。CEO Sam Altman就此道歉，目前该模型已向大部分付费用户及API开发者全面开放。此次延期主要源于底层计算能力扩容与新系统部署的压力。
-->

OpenAI在发布GPT-6 Astra后因 rollout 进度迟缓引发用户不满。CEO Sam Altman就此道歉，目前该模型已向大部分付费用户及API开发者全面开放。此次延期主要源于底层计算能力扩容与新系统部署的压力。

> 译自：["Sorry for the messy rollout": OpenAI launches GPT-6 Astra to most paying users a day after its unveiling](https://thenewstack.io/gpt6-astra-developer-access-delayed/)
> 
> 作者：Amanda Caswell

**更新：截至美东时间9月4日周五下午6:30**，GPT-6 Astra 已在 ChatGPT 上面向所有包含该访问权限计划的付费用户开放。

OpenAI 技术人员核心成员 Thibault Sottiaux 在其 X 账号上发帖称：“好吧没关系，团队和 Astra 做得很好，我们的系统比预期更具可扩展性。Astra 现在也已向所有 Plus 和 Business 用户推出。希望你们玩得开心，并让我们知道使用体验如何！”

周五早些时候，OpenAI 首席执行官 Sam Altman 在 X 上发帖称：“GPT-6 Astra 现已面向 Work/Codex 中的所有 Pro、Enterprise 和 Business Premium 用户开放，并可在 API 中使用。我们将随后开始向 Plus 和 Business 用户推送。感谢大家的耐心等待。”

根据该公司的定价分层文档，支付 8 美元/月 ChatGPT Go 计划的用户没有，将来也不会获得访问 GPT-6 Astra 或 GPT-5.6 的权限。

![](https://cdn.thenewstack.io/media/2026/09/8f9c93c8-screenshot-2026-09-04-at-18.25.22-1024x402.png)

Sottiaux 在周四晚上 OpenAI 宣布 Astra 首发之后、向用户发布之前发帖称：“我们正在开始发布 GPT-6 Astra，并且正尽可能谨慎且快速地进行。”

---

*我们于美东时间周五中午 12:24 发表的原始报道如下：*

**OpenAI 于周四发布了 [GPT-6 Astra](https://thenewstack.io/astra-arc-agi-benchmark/)**，但许多希望对其进行测试的开发者仍在等待访问权限。

在发布消息数小时后，OpenAI 首席执行官 Sam Altman 对他所称的“混乱的发布（messy rollout）”表示歉意，并承认针对 API 客户或 ChatGPT 订阅者的广泛访问尚未开始。

> “首先，对混乱的发布表示歉意，”

“首先，对混乱的发布表示歉意，”Altman 在 X 上的一篇帖子中写道。他补充说，OpenAI 预计将在“不久的将来”开始更广泛的发布，首先从 ChatGPT Pro 订阅者开始。

对于开发者来说，这造成了一种不同寻常的困境。OpenAI 已经公布了 Astra 的 API 文档和定价，包括其 105 万个 token 的上下文窗口、最高支持 128,000 个输出 token，以及每百万输入 token 10 美元和每百万输出 token 50 美元的标准 API 费率。但端点本身仍在部署中，OpenAI 尚未具体解释发布过程中出了什么问题。因此，虽然 Astra 的基准测试结果令人印象深刻，但想要根据自己的工作负载评估这些声明的开发者和独立审查人员仍在等待。

## 开发者为何在等待

OpenAI 的 Codex 工程负责人 [Thibault Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/) 在他自己的 [X 帖子](https://x.com/thsottiaux/status/2095651088502591861) 中提供了关于幕后发生情况的更多细节。他表示，发布过程需要“几天”才能完成，并且 OpenAI 在扩大访问权限的同时，正在上线新系统并增加计算资源。

“我们正在开始发布 GPT-6 Astra，并且正尽可能谨慎且快速地进行，”Sottiaux 写道。他补充说，在发布期间，“许多新颖的系统将首次在大规模下运行”，并且 OpenAI 正在“投入大量的计算资源”。

> “我们正在开始发布 GPT-6 Astra，并且正尽可能谨慎且快速地进行，”

虽然这并不能证明计算能力导致了延迟，但它确实让我们深入了解了 OpenAI 在扩大访问权限时所面临的问题。该公司最初的公告称，Astra 最初将提供给有限的组织群体，ChatGPT Plus、Pro、Business 和 Enterprise 用户，以及 OpenAI API、Microsoft Azure 和 AWS Bedrock 预计将在“未来几天”跟进。

已经获得早期 API 访问权限的开发者在发布本身之外已经遇到了意外。正如《The New Stack》本周报道的那样，[Astra 的 API 引入了一种新的安全触发中断机制](https://thenewstack.io/astra-api-safety-stops/)，看起来像是超时但实际上并不是——这对于围绕该模型构建生产工作流的开发者来说可能会产生真正的影响。

## 简述补偿性重置（Banked resets）

在用户等待的同时，OpenAI 正试图通过其所谓的“补偿性重置（banked reset）”来至少弥补部分延迟。

Sottiaux 表示，自 9 月 3 日起，付费 ChatGPT 订阅者每维持一天无法访问 Astra，就会获得一次补偿性重置，并补充说“团队正在竭尽全力尽快提供访问权限。”

> “团队正在竭尽全力尽快提供访问权限。”

OpenAI 之前在 ChatGPT Work 和 Codex 中使用过补偿性重置，让用户在达到限制后有一种补充使用量的方法。它们不是额外的 API 额度，也不是使用限制的永久性增加，而是用户可以保存到需要时使用的重置次数。

Astra 的不同之处在于 OpenAI 分发它们的方式：付费 ChatGPT 订阅者每多一天无法访问，就获得一次。到目前为止，OpenAI 尚未宣布为等待通过 API 使用 Astra 的开发者提供任何类似的补偿。

这一举措符合 OpenAI 在人工智能收费模式上进行实验的更广泛模式：该公司最近宣布了一种[基于结果的定价模型](https://thenewstack.io/openai-outcome-based-pricing/)，即仅在模型产生正确结果时才收费；这是其定价策略仍在不断变动的另一个迹象。

## 计算能力使发布复杂化

OpenAI 表示，Astra 将在“未来几天”内向 Plus、Pro、Business 和 Enterprise 用户以及 OpenAI API、Microsoft Azure 和 AWS Bedrock 发布，并优先考虑 Pro 订阅者。Sottiaux 表示，发布过程应该需要几天时间完成。

对于开发者而言，最大的未解之谜是广泛的 API 访问权限何时到来，以及它是否会伴随更严格的使用限制。Astra 的 [持久代理（persistent-agent）功能](https://thenewstack.io/openai-astra-persistent-agents/) 也使得对于开发者而言，等待变得更加重要。

OpenAI 没有立即回应《The New Stack》关于发布问题、补偿性重置或 API 时间表的问题。