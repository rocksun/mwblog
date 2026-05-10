<!--
title: Datadog 与 T-Mobile 负责人揭秘 AI Agent 在生产环境部署的现实挑战
cover: https://cdn.thenewstack.io/media/2026/05/72129ce4-ubaid-e-alyafizi-chbwef815-m-unsplash-scaled.jpg
summary: 纽约 AI Agent 大会揭示：企业正通过模拟和知识图谱等手段推动 Agent 落地。虽然氛围编程提升了开发效率，但生产环境仍需严格的人力监管以应对幻觉和安全挑战。
-->

纽约 AI Agent 大会揭示：企业正通过模拟和知识图谱等手段推动 Agent 落地。虽然氛围编程提升了开发效率，但生产环境仍需严格的人力监管以应对幻觉和安全挑战。

> 译自：[Datadog and T-Mobile leaders reveal the reality of deploying AI agents in production](https://thenewstack.io/enterprise-ai-agent-adoption/)
> 
> 作者：Eric Newcomer

本周在纽约举行的 [AI Agent 大会](https://www.agentconference.com/) 上，与会发言者表示，通过谨慎的治理和验证，AI Agent 在特定企业职能中的应用正日益普及。

在过去的一年里，新型且功能强大的 AI 编码 Agent 的普及率急剧增长。然而，[Datadog](https://www.datadoghq.com/) 的首席科学家 [Ameet Talwalkar](http://linkedin.com/in/atalwalkar) 在开幕主题演讲中指出，它们生成的代码在生产环境中尚不能完全被信任。

> “人类面临的最困难任务之一不再是构建生产系统，而是审核那些被交付到生产环境中的‘氛围编程’软件。”
> —— Datadog 的 Ameet Talwalkar

Talwalkar 表示：“人类面临的最困难任务之一不再是构建生产系统，而是审核那些被交付到生产环境中的‘氛围编程’软件。”

## 氛围编程软件带来的挑战

他表示，Datadog 正在扩展其可观测性产品线，以模拟真实世界系统，并利用 AI Agent 在生产问题发生前进行预测。

在商业应用中，AI Agent 最普及的用途是客户服务和客户辅助聊天机器人。

例如，T-Mobile 的 AI 工程总监 [Julianne Roberson](https://www.linkedin.com/in/julianne-roberson-07206557/) 表示，T-Mobile 使用 AI Agent 每天处理 20 万次客户对话。她说，这个项目耗时约一年才完成。

Agent 框架供应商 ArklexAI 的联合创始人兼 CEO Zhou Yu 告诉 *The New Stack*，公司的新产品 ArkSim 旨在通过模拟 AI Agent 与客户的互动，缩短面向客户的机器人的上市时间。由于 Agent 的交互是非确定性的，ArkSim 通过收集数据来提升质量。

“你可以使用 Claude Code 在五分钟内构建一个 Agent，但你不知道它进入生产环境后会做出什么，尤其是当你拥有庞大的客户群时，”Zhou Yu 说道。

“你不知道用户会用它做什么。我们为你的用户创建模拟，这样你就能了解用户体验是什么样的，以及如何改进它。”

## 模拟用户体验

“最初，一切都围绕着构建和部署 Agent，”领先的 Agent 框架供应商 [CrewAI](https://crewai.com/) 的创始人兼 CEO [Joe Moura](https://www.linkedin.com/in/joaomdmoura/) 在其主题演讲中表示。“但现在，一切都关乎安全性和企业级应用。”

Moura 告诉 *The New Stack*，CrewAI 根据客户需求增加了企业级功能。他们之所以成为领先的框架，是因为起步早（2003 年），并提供了一个编码了 Agent 最佳实践的专业平台。

Arklex 的 Zhou Yu 告诉 *The New Stack*，尽管沃尔玛仍在使用他们最初的 Agent 框架产品，但 Agent 框架已趋于同质化，这也是他们转向模拟领域的原因。

Moura 表示，在未来，CrewAI 将专注于“纠缠型 Agent（entangled agents）”，这些 Agent 会根据客户的操作自动进行调整。

“我所说的纠缠型 Agent 是指能够随时间推移不断进化的 Agent。除了自我改进的 Agent 之外，其核心理念是纠缠型 Agent 会变得对该企业而言独一无二，”Moura 说道。

## 解决幻觉问题

Akamai 首席技术官 [Bobby Blumofe](https://www.linkedin.com/in/robert-blumofe-258233/) 在主题演讲中表示，大语言模型（LLM）经常产生错误结果和幻觉。仅依赖 LLM 的 AI Agent 很难产生准确的结果。

“大家可能都知道，大多数聊天机器人在从 LLM 中进行采样时，是按概率采样的。同一个聊天机器人在不同时间可能会给你不同的答案，”他说道。

他补充道，将网络搜索信息引入上下文窗口是一个巨大的转变。“当涉及到产生正确结果时，这对我们讨论的所有内容都至关重要。”

[LanceDB](https://www.lancedb.com/) 的创始人兼 CEO [Chang She](https://www.linkedin.com/in/changshe/) 告诉 *The New Stack*，为 Agent 提供知识图谱作为上下文以改善结果也越来越受欢迎。

他表示，LanceDB 已被采纳为 OpenClaw 的存储插件，并通过统一访问语音、视频、文本、结构化和非结构化等多种数据模态，提高了 Agent 开发者的生产力。

他补充道，除了支持流行的开源多模态 Lance 格式外，“现在还有一个新的 Lance Graph 项目，因此你也可以存储知识图谱。”

“我们的第一个想法是，如何将 AI 产品紧密集成到我们的平台中？”云电话提供商 [Ring Central](https://www.ringcentral.com/) 的分析师关系高级总监 [Tim Dreyer](https://www.linkedin.com/in/timgdreyer/) 告诉 *The New Stack*。

“我们看到了提高生产力的需求，因此推出了一款名为 AI Conversation Expert 的产品，作为一种通话后分析工具，”Dreyer 说道。“AI Agent 会分析通话录音，寻找改进空间，并提供指导性见解。”

> “我们的目标不是取代真人坐席。我们是想让他们的工作变得更轻松。如果我们能分担 50% 或 60% 的乏味工作……他们就能有更多时间从事战略性工作。”
> —— Ring Central 的 Tim Dreyer

在 Conversation Expert Agent 取得初步成功后，“我们又增加了 AI 接线员 Agent，”他补充道。“我们的目标不是取代真人坐席。我们是想让他们的工作变得更轻松。如果我们能分担 50% 或 60% 他们必须做的乏味工作，他们就能有更多时间从事战略性工作。”

## 聚焦人为监督

自比尔·盖茨在 2023 年撰写著名的 [AI Agent](https://www.gatesnotes.com/ai-agents) 文章并强调自主性的重要性以来，情况已经发生了变化。

在大会上，很少有发言者或展商将自主性视为推动应用的核心动力；相反，他们更倾向于将其定性为一个长期目标，需要通过采取谨慎的初步步骤来解决或消除错误来实现。

关于 AI Agent 是会取代人类还是“赋能”人类的辩论，现在正处于风口浪尖。

关于企业级 Agent 讨论的一个有力结论是：无论分配给 AI Agent 什么任务和角色，人为监督仍然是必要的。