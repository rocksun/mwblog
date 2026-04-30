<!--
title: HPE 如何利用智能代理 AI 实现云与 AI 扩张的闭环管理
cover: https://cdn.thenewstack.io/media/2026/04/18bdc962-david-palma-wlqpoh60tc8-unsplash-scaled.jpg
summary: HPE 通过智能代理 AI 构建闭环运营模式，应对混合云与 AI 扩张带来的复杂性。利用 OpsRamp 等工具，实现从被动响应到预测性补救的转变，提升复杂环境下的运维效率。
-->

HPE 通过智能代理 AI 构建闭环运营模式，应对混合云与 AI 扩张带来的复杂性。利用 OpsRamp 等工具，实现从被动响应到预测性补救的转变，提升复杂环境下的运维效率。

> 译自：[How HPE is closing the loop on cloud and AI sprawl with agentic AI](https://thenewstack.io/hpe-agentic-ops-copilot/)
> 
> 作者：Jennifer Riggins

在企业中，没有任何事物是绿地项目（Greenfield）。混合云的复杂性叠加在孤立的团队和系统之上，使得观察、理解、补救和防止停机几乎变得不可能。人手不足的运营和[可观测性](https://thenewstack.io/observability/)团队现在还必须跟上 AI 的步伐。与此同时，企业技术栈面临着比以往任何时候都更多的稳定性与安全性风险。

为了应对这一挑战，[企业运营](https://thenewstack.io/operations/)必须从根本上改变处理 Day 2 及之后工作的方式。在服务或部门之间维持厚重的边界已不再安全——无论如何，它们都会阻碍 AI 投资的回报。

为了生存，组织必须从孤立的、被动的仪表板转向闭环运营模式，并在 AI 代理的支持下，将编排、可观测性和补救视为一个持续的反馈循环。

“你必须明白，Day 2 和 Day 1 处于一个闭环中，因为你所配置的内容，需要基于你对当前现有环境（Brownfield）的理解。而且当出现大量问题时，你可能并不想进行大量的更改，”[Hewlett Packard Enterprise (HPE) 混合云](https://www.hpe.com/us/en/home.html)的高级杰出技术专家 [Phanidhar Koganti](https://www.linkedin.com/in/networkleader/) 告诉 *The New Stack*。

在运营团队目前面临的限制下，唯一的出路似乎是将 AI 技术应用于运营，[从所有噪音中提取信号](https://thenewstack.io/hpe-self-healing-ai-infrastructure/)。这种从 DIY 到自主补救的转变不仅需要引入 AI。

AI 赋能的运营需要平台工程策略、预测分析、新的运营指标等。所有这些并不是为了取代今天的操作员，而是为了优化团队的时间，使他们能够在压力重重的时期变得更快、更具战略性，并希望压力更小。

## **当每种资源都受限时**

“现在的创造力仅受计算成本的限制，而不受容量的限制，”[成果工程宣言（Outcome Engineering Manifesto）](https://o16g.com/manifesto/)在谈到 AI 代理强加给科技行业的变革时如此承诺。然而，AI 实际上让大多数运营团队在时间和可用资源方面感到比以往任何时候都更受限。

“我们的客户面临着在资源大幅减少的情况下继续提供相同 SLA（服务水平协议）的压力，”HPE 数据中心业务部门工程副总裁 [Sridhar Katere](https://www.linkedin.com/in/sridharkatere/) 表示。在实践中，这意味着“在 Day 2 发生问题时，用于排查故障的运营团队成员更少了”。

由运营团队管理的运营代理是扩展故障排除和补救能力的一个机会，且无需扩大团队规模。

HPE OpsRamp 软件最近正式发布（GA）了其[智能代理运营副驾（agentic operations copilot）](https://community.hpe.com/t5/the-cloud-experience-everywhere/operations-copilot-from-hpe-opsramp-software-your-partner-for/ba-p/7264586)。[Phanidhar Koganti](https://www.linkedin.com/in/networkleader/) 解释说：“你可以通过非常高层级的意图来表达你想要实现的目标，这将被转换为详细的部署计划，其中包括数据中心、网络相关的自动化、存储以及使整个基础设施协同工作的各种其他组件。”

AI 还可以帮助运营团队从被动转向主动，同时倡导合理的资源预算。

“当我们说‘问题’时，并不意味着故障的本质仅限于服务中断，”[Phanidhar Koganti](https://www.linkedin.com/in/networkleader/) 说。“如果你即将耗尽容量，意味着光模块可能会失效，这就是你试图预测的二元故障。”

[Sridhar Katere](https://www.linkedin.com/in/sridharkatere/) 解释说，如果一名运营工程师知道某个部件（如交换机）可能会在六周内失效，那么他们不仅有时间防止停机，还可以更好地预算硬件资源，而这些资源目前受到供应链不确定性的极大限制。

“这就是我们正在构建预测分析的地方，以帮助客户提前计划和采购必要的硬件及组件，”他继续说道。

通过最近的收购和持续投资，HPE 正在建立自己的运营控制中心，以定义这种下一代混合多云运营模式。其 [CloudOps 软件套件](https://www.hpe.com/uk/en/software/cloud-ops-suite.html)——以 [HPE OpsRamp 软件](https://www.hpe.com/us/en/opsramp.html)和 [HPE Morpheus 软件](https://www.hpe.com/us/en/morpheus-enterprise-software/features.html)为核心，并可选择添加 [HPE Apstra 数据中心直连（Data Center Director）](https://www.hpe.com/us/en/apstra-data-center-director.html)——旨在帮助组织勾勒出其完整云运营模式的实际需求。

继 OpsRamp 发布 GA 版本后，其他 HPE 产品预计也将很快发布带有对话界面的智能代理系统。

“我们在优化全栈方面所讨论的内容，将适用于整个栈的容量问题甚至性能问题，”[Phanidhar Koganti](https://www.linkedin.com/in/networkleader/) 说，因为企业系统的复杂性是多层级的。

## **运营指标需要重新定义**

虽然平均修复时间（MTTR）——总停机时间除以总事件数——仍然是一个重要的指标，但在面对这种企业级复杂性时，它已不足够。

同样，识别或检测的手段仍然是关键，但当你将 AI 引入其中时，看待它们的方式会有所不同。AI 运营必须优先考虑“平均关联时间”，应用 AI 运营工具来分析日志、指标和追踪，将零散的信号连接成[单个、可追溯的建议操作](https://thenewstack.io/agentic-ai-observability-auditing/)。

> “第一直觉通常认为网络是罪魁祸首，因此网络实现自诊断并回应‘嘿，我不是问题所在’是非常重要的。”

就像著名的蜘蛛侠互相指认的梗图一样，如果他们都指着网络或存储，AI 运营工具还必须优化“平均自证清白时间”（mean time to innocence）。

“第一直觉通常认为网络是罪魁祸首，因此网络实现自诊断并回应说：‘嘿，我不是问题所在’是非常重要的，”[Sridhar Katere](https://www.linkedin.com/in/sridharkatere/) 说道。

在全栈环境中，症状和停机时间很少发生在与原因相同的层级。

> “……故障的症状和故障的原因永远不在同一个层级。”

“我们从大多数客户那里看到的共同点是，故障的症状和故障的原因永远不在同一个层级。我的意思是，例如，症状可能出现在应用层，表现为我的应用事务超时等。而其实际原因可能在网络层或存储层的某个地方，大多数时候，网络是罪魁祸首，”[Phanidhar Koganti](https://www.linkedin.com/in/networkleader/) 说。

“IT 技术栈正变得越来越复杂。你需要各层之间的协作，以及智能代理协作和常规的传统 AIOps 协作。”

企业级复杂性（可能看到多个故障并行发生）需要跨全栈的更紧密集成，以及 AI 来从噪音中过滤重要信号。接下来的步骤是[在适当时让 AI 代理自动补救](https://thenewstack.io/hpe-self-healing-ai-infrastructure/)——但前提是其行为对人类操作员是可解释的。

HPE 还有自己的效能指标，包括衡量其平台预测和排除故障效果的季度 KPI。[Sridhar Katere](https://www.linkedin.com/in/sridharkatere/) 表示，目前该平台——由图谱和 GraphQL 支持，具有高度上下文化的数据栈——在故障排除方面的准确率约为 40%，目标是到年底超过 70%。HPE 正在将其在企业领域近 100 年的经验注入其新的 [CloudOps 软件](https://www.hpe.com/uk/en/software/cloud-ops-suite.html)中，并训练了不同层级的[智能代理技能](https://thenewstack.io/hpe-agentic-ai-ops-burnout/)：平台、驱动程序、贯穿件、可更换单元、系统等。

“我们不是生活在一个静态的世界里。这是一个非常动态的世界。”[Sridhar Katere](https://www.linkedin.com/in/sridharkatere/) 承认，鉴于即使在节奏较慢的企业软件开发生命周期中，事物变化的速度也非常快，这一切都是一个“不断移动的目标”。