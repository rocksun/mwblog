<!--
title: 微软CEO Satya Nadella：你在为AI支付双重代价，第二种代价更惨重
cover: https://cdn.thenewstack.io/media/2026/06/5a5a0078-ghariza-mahavira-oq_mjoayun0-unsplash-scaled.jpg
summary: 微软CEO Satya Nadella指出，企业使用AI存在双重代价：金钱成本及向模型泄露核心专利知识的隐形成本。他建议企业应构建私有AI架构，将核心知识资产保留在内部，以确保技术投入能转化为真正的企业竞争力。
-->

微软CEO Satya Nadella指出，企业使用AI存在双重代价：金钱成本及向模型泄露核心专利知识的隐形成本。他建议企业应构建私有AI架构，将核心知识资产保留在内部，以确保技术投入能转化为真正的企业竞争力。

> 译自：[Microsoft CEO Satya Nadella says you're paying for AI twice — the second price is worse](https://thenewstack.io/nadella-reverse-information-paradox/)
> 
> 作者：Amanda Caswell

微软董事长兼首席执行官 Satya Nadella 近日在网上分享了他对企业级 AI 隐形成本的思考。

在周日于 X（前身为 Twitter）发布的一篇长文中，Nadella 将这一问题描述为一种“反向信息悖论”，并指出 AI 彻底颠覆了诺贝尔奖得主、经济学家 Kenneth Arrow 的经典信息悖论。

Arrow 的悖论关注的是卖方困境，即如何在不披露信息的情况下证明信息的价值。而 Nadella 认为，企业级 AI 将这种负担转移到了买方身上，买方必须共享专有流程和机构专业知识，才能从模型中获得最佳结果。

“本质上，你需要为智能支付两次代价，一次是用金钱，另一次是用更宝贵的东西：你必须揭示的专有知识，才能使这些智能发挥作用，”他写道。“你越希望模型表现出色，就越需要向它输入更多的此类知识。”

> “本质上，你需要为智能支付两次代价，一次是用金钱，另一次是用更宝贵的东西：你必须揭示的专有知识，才能使这些智能发挥作用。”

## 当“废气”成为竞争优势

据 Nadella 所述，每一次与企业 AI 系统的交互都会产生他所谓的“废气”，这些废气逐渐捕捉了组织的运作方式。

“每一次修正都被提炼为机构知识，”Nadella 写道。“这是一种竞争对手永远买不到的知识，也是一种几乎无法察觉的泄露方式：通过轨迹、修正和评估一点点流失。”

> > “每一次修正都被提炼为机构知识。这是一种竞争对手永远买不到的知识，也是一种几乎无法察觉的泄露方式：通过轨迹、修正和评估一点点流失。”

随着时间的推移，成千上万次的互动创造了一个内部组织知识库，其价值可能超过了最初喂给系统的原始文档。员工使用 AI 的频率越高，组织的专业知识就越深地融入到这些系统的运作方式中。

## 重新定义信任边界

在实践中，这些知识宝库可能会推动企业走向模型无关（model-agnostic）的 AI 技术栈，在这种技术栈中，提示词（prompt）和记忆存储仍然由企业控制——即使底层基础模型发生变化。

在帖子中，Nadella 还抨击了当前的 AI 商业实践，认为模型提供商声称拥有从公共数据中学习的广泛权利，同时限制了客户在其自身组织内重复使用或构建知识的能力。

一些观察家可能会认为，这个观点出自微软 CEO 之口具有某种讽刺意味。Nadella 警告称，企业面临着将宝贵的组织知识流失给 AI 系统的风险，但微软销售的 Copilot，其价值部分取决于对企业数据的广泛访问。Copilot 的工作原理是遍历 Microsoft Graph，使其能够推理用户已经获得访问权限的文档、电子邮件、聊天记录和其他信息。

安全研究人员对这类系统如果组织拥有过于宽松的访问控制可能暴露的敏感信息量表示担忧。[Concentric AI 的研究](https://www.techradar.com/pro/microsoft-copilot-has-access-to-three-million-sensitive-data-records-per-organization-wide-ranging-ai-survey-finds-heres-why-it-matters)显示，在 2025 年上半年，Copilot 每个组织访问了近 300 万条机密记录，而 [EPC Group 的审计](https://www.myworkdrive.com/blog/microsoft-365-copilot-oversharing)发现，约 80% 的企业 Microsoft 365 租户存在严重的过度共享风险，包括薪资信息、并购文件和客户数据，这些数据都可能通过 Copilot 浮出水面。[美国众议院也曾因数据安全担忧禁止员工使用 Copilot，但随后取消了该禁令](https://www.reuters.com/technology/us-congress-bans-staff-use-microsofts-ai-copilot-axios-reports-2024-03-29/)。

## 微软的区别

然而，微软在*访问*企业数据以回答用户请求与*使用*该数据来训练基础模型之间做出了区分。该公司表示，通过 Microsoft Graph 检索的信息[不会用于训练其 AI 模型](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection)，并且 Copilot [尊重现有的权限、身份控制和敏感度标签](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy)。

尽管如此，其商业策略依然昭然若揭：Nadella 周日的“[反向信息悖论](https://x.com/satyanadella/status/2076323181154230284?s=46)”帖子实际上是一份通往 Azure 的路线图。Nadella 建议构建的一切都在云基础设施上运行。本质上，企业可以更换基础模型，但他们不会更换云平台。

## 拥有你自己的 AI 学习循环

为了应对将信息交给前沿实验室的趋势，Nadella 概述了企业级 AI 架构的几个优先事项。他的建议包括：

* 将组织记忆保留在企业租户内部。
* 构建私有的评估和学习系统。
* 将编排层与任何单一基础模型解耦。
* 保持在不丢失积累的组织知识的情况下更换模型的能力。

综上所述，Nadella 的论点回归到这样一个观点：企业应该拥有自己的学习循环，而不是将其一部分交给提供 AI 模型的公司。

Nadella 通过引用 Palantir 首席执行官 Alex Karp 的话加强了这一观点，[后者也持有类似观点](https://thenewstack.io/karp-mensch-ai-lockin/)，即企业希望对自己的 AI 基础设施拥有完全的所有权。

## 模型无关的编排正在兴起

最终，通过保持对生产手段的控制，企业终于可以确保当他们投资 AI 时，复合价值能留在其所属的业务内部。像 LangChain 和 Haystack 这样的工具之所以受到欢迎，正是因为它们让工程团队能够将基础模型视为即插即用的商品，而不是硬编码的依赖项。

“技术型客户想要的是对计算、模型、数据栈及其 Alpha 的控制权，”Nadella 引用 Karp 的话说。“他们想确保自己拥有生产手段，而不是将其转移给他人。”

> “他们想确保自己拥有生产手段，而不是将其转移给他人。”