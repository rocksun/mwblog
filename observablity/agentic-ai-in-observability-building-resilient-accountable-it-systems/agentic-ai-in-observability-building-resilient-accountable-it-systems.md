
<!--
title: 可观测性中的智能体AI：构建高弹性、可问责的IT系统
cover: https://cdn.thenewstack.io/media/2025/11/26e15afb-agentic-ai-in-observability.jpg
summary: 文章探讨了智能体AI在IT运营和可观测性中的应用。强调了在追求自动化效率的同时，必须通过透明度、可解释性和问责制来平衡风险。建议采取“设计即透明”、“设计即安全”和“设计即治理”的原则，并实施AI网关、AI可观测性管道等措施，以实现负责任的AI运营。
-->

文章探讨了智能体AI在IT运营和可观测性中的应用。强调了在追求自动化效率的同时，必须通过透明度、可解释性和问责制来平衡风险。建议采取“设计即透明”、“设计即安全”和“设计即治理”的原则，并实施AI网关、AI可观测性管道等措施，以实现负责任的AI运营。

> 译自：[Agentic AI in Observability: Building Resilient, Accountable IT Systems](https://thenewstack.io/agentic-ai-in-observability-building-resilient-accountable-it-systems/)
> 
> 作者：Vikram Murali

随着企业 IT 系统的日益复杂，在分布式架构中保持可见性、性能和弹性变得前所未有的重要。具有自主分析和行动能力的智能体 AI（Agentic AI）的兴起正在重新定义组织如何进行可观测性和运营弹性。其结果是更具前瞻性、适应性的运营模式，可显著降低平均解决时间 (MTTR)，并使团队能够专注于创新而非事件响应。

[智能体 AI](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/) 指的是能够通过规划、推理和行动，以最少的人工干预自主执行复杂、多步骤任务的系统。与对直接命令做出反应的传统 AI 不同，智能体 AI 是前瞻性且以目标为导向的，能够适应不断变化的环境。

但自主性本身并非进步。使 [AI 代理](https://thenewstack.io/ai-agents-in-it-from-hype-to-hands-on-impact) 如此有价值的能力也可能使其行为难以监控、理解和控制。要实现智能体 AI 的潜力，取决于在自动化每个阶段嵌入安全性和问责制，并使用旨在监控 AI 代理性能并标记任何偏离标准的 [可观测性](https://thenewstack.io/observability/) 工具。没有这些基础，提供速度和效率的相同系统可能会带来新的运营风险。

## 平衡自动化与人工监督

企业在开始设计智能体系统时，必须考虑人工干预（HITL）的架构，而不是事后考虑。目标是将自动化的效率与信任所需的可靠性和治理结合起来。

正如我之前所说，在 IBM，这种平衡遵循一个三步连续过程：

*   **自动化执行：** 低风险、可逆的任务——例如日志分析或测试环境操作——可以完全自动化，只需最少的人工监督。
*   **监督自动化：** 中等风险流程需要一个审查和批准步骤，在此过程中，人类在 AI 行动执行前进行验证。
*   **人工干预执行：** 高风险操作——例如客户沟通或生产变更——必须保持在人类的直接控制之下。

随着对自动化的信任不断增长，组织可以将更多受监督的流程转移到自动化类别，尤其是在非生产环境中。我的客户经验表明，目前约有 60% 到 70% 的自动化发生在开发和测试系统中，而 30% 到 40% 发生在生产环境中。

## 自主可观测性的双刃剑

[可观测性平台](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434342025;dc_trk_aid=627069060;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) 已从简单的日志收集发展到能够进行异常检测和关联的高级 AIOps。下一个前沿领域应该包括智能体可观测性——能够解释遥测数据、检测故障并采取纠正措施的系统。

> 无问责制的自动化，大规模运行时风险巨大。

这些能力可以通过消除手动分类和实现主动解决来改变 IT 运营。但它们也带来了新的风险；AI 流程可能会误将流量高峰解释为攻击，或者推断出服务日志之间的虚假关联。

无问责制的自动化，大规模运行时风险巨大。在我看来，每个由 AI 驱动的决策都必须是可追溯的、可解释的并且是受管制的。没有透明度和监督，黑箱自动化就会侵蚀信任，减缓变革性技术的采用。

## AI 问责制的指标和框架

过去两年中，涌现了若干框架来促进 AI 系统的透明度和问责制：

这些框架帮助组织跟踪 AI 行为，记录合规性，并确保可解释性——理解系统为何采取行动，而不仅仅是它做了什么。

诸如 [Google 的模型卡](https://modelcards.withgoogle.com/) 等其他举措提供了记录模型来源和行为的模板。总而言之，这些标准可以帮助实现 AI 系统的可追溯性和可审计性。

## 为什么智能体 AI 需要新的安全措施

与传统的分析工具不同，智能体 AI 不仅仅是观察，它还会采取行动。这种自主性需要在多个维度上采取新的安全措施：

*   **误报和幻觉：** 生成模型可能[错误识别模式](https://arxiv.org/abs/2509.04664)，导致不必要或有害的干预。现代可观测性工具使用特定于 AI 的遥测数据来呈现异常响应或反复重试，这表明模型基础不牢固，需要进行重新训练或参数更新。
*   **失去监督：** [过度依赖自动化](https://thenewstack.io/want-to-mitigate-risk-invest-in-automation/) 可能会掩盖潜在的系统漂移。可观测性工具可以通过监控响应模式的变化或输出的变化来帮助检测漂移，然后提醒团队更新配置或文档以消除偏差。
*   **安全漏洞：** 拥有过多数据访问权限的智能体可能成为[攻击面](https://arxiv.org/pdf/2506.07153)。例如，随着网络犯罪分子开发新的策略，智能体在检测欺诈方面的可靠性可能会降低。可观测性工具可以识别智能体何时访问或调用超出授权范围的服务，以便团队能够重新训练模型以弥补安全漏洞。
*   **合规风险：** 无法解释的 AI 决策可能会根据欧盟 AI 法案等框架触发监管违规。可观测性工具可以提供跟踪数据，以支持这些框架下的可审计性和可解释性要求。

所有这些挑战都强调了同一个原则：[值得信赖的自动化](https://thenewstack.io/automated-systems-scalability-reliability-and-security/) 取决于透明度、可解释性和问责制。

> 值得信赖的自动化取决于透明度、可解释性和问责制。

## 蓝图：带有防护栏的 AI 构建

IBM 将智能体 AI 视为机遇和责任。从我的角度来看，下一代可观测性平台需要围绕三个关键组件进行设计：

*   **设计即透明：** 每个 AI 行动都必须是可审计的，具有清晰的数据 lineage，显示是什么促成了决策以及为什么。
*   **设计即安全：** 可观测性数据通常高度敏感，必须通过加密、身份控制和严格的权限来保护。
*   **设计即治理：** 策略应规定 AI 何时可以自主行动，以及何时需要人工验证——这正是 IBM 所称的策略驱动自动化。

这些防护栏定义了负责任的自动化，将 AI 的效率与企业级的信任相结合。

## 负责任的 AI 运营的实用防护栏

除了增强人类智能与 AI 结合的通用[最佳实践](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798594;dc_trk_aid=627070515;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) 外，请考虑以下将智能体 AI 集成到可观测性和运营中的策略。

*   部署[AI 网关](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798591;dc_trk_aid=627070806;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)，以在执行前验证和授权操作，确保符合安全和变更策略。
*   建立[AI 可观测性管道](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433799998;dc_trk_aid=627070512;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)。将 AI 模型和智能体视为一等可观测组件。捕获每个智能体操作、模型推理和数据交互的 MELT，以实现完整的 lineage 跟踪和可解释性。
*   监控模型漂移和推理透明度。对[大型语言模型](https://thenewstack.io/taming-llm-sprawl-why-enterprises-need-an-ai-gateway-now) 和智能体 AI 系统实施持续验证和漂移检测。可观测性工具可以提供跟踪数据，以帮助突出推理或决策路径中的偏差。
*   实施[安全数据治理](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434342457;dc_trk_aid=627070800;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)，以确保 AI 模型只访问它们需要的遥测数据。
*   将[弹性评分](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798597;dc_trk_aid=627069063;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) 与可观测性指标挂钩，以实现系统健康和恢复就绪状态的统一可见性。
*   为高影响或面向客户的系统维护[人工干预架构](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434342022;dc_trk_aid=627070803;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)。AI 应协助而不是取代人类判断。

随着企业朝着自愈、AI 驱动的环境迈进，这些原则正迅速成为运营必需品。

## 建立对下一代可观测性的信心

AI 必须扩展人类意图，而不是取代它。通过强大的防护栏和透明的设计，企业可以利用智能体 AI 来[自动化 IT 弹性](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798594;dc_trk_aid=627070515;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)，降低 MTTR，并[建立运营信心](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434004125;dc_trk_aid=626964671;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)。

最终，可观测性关乎保障——了解系统是否按预期运行，以及在最关键的时刻自动化是否负责任地行动。当以透明度和治理实施时，智能体 AI 可以将信心提升到一个新的水平。

在下一波数字化运营中取得成功的组织，将是那些将智能与诚信相结合的组织——利用 AI 驱动创新，同时不损害问责制。

可观测性的未来不仅是自主的。它应该是负责任的、可解释的且安全的——这是构建持久弹性企业系统的基础。

*了解更多关于[IBM 可观测性](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798585;dc_trk_aid=627069066;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) 如何通过集成、由 AI 驱动的运营智能来推动弹性、降低成本并优化 IT。*