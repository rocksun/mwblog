<!--
title: “六合一”：Salesforce将六大核心工具整合进AI Harness框架
cover: https://cdn.thenewstack.io/media/2026/09/3f638c89-imkara-visual-1tckvguhevc-unsplash-scaled.jpg
summary: Salesforce推出了“企业AI Harness”，将Data 360、Informatica、MuleSoft、Tableau、Agentforce和Salesforce Guardian六大核心能力整合，通过统一的AI控制平面，旨在解决企业内部AI代理分散、可观测性差和管理复杂的难题。
-->

Salesforce推出了“企业AI Harness”，将Data 360、Informatica、MuleSoft、Tableau、Agentforce和Salesforce Guardian六大核心能力整合，通过统一的AI控制平面，旨在解决企业内部AI代理分散、可观测性差和管理复杂的难题。

> 译自：["Six tools, one harness": Salesforce loops together a six-pack of favorites](https://thenewstack.io/salesforce-enterprise-ai-harness/)
> 
> 作者：Adrian Bridgwater

**Salesforce**于周四推出了**Salesforce Enterprise AI Harness**，作为该公司一直致力整合的AI框架概念与基础设施的正式合并版。

该组织表示，“没有单一系统”能够完整回答诸如完成客户订单等直接的业务任务；即：[CRM](https://thenewstack.io/ebooks/generative-ai/developers-guide-to-connecting-crm-data-ai-app-experience/) 了解客户，[ERP](https://thenewstack.io/sap-simplifies-erp-data-access-for-developers/) 了解库存，[FSM](https://www.salesforce.com/uk/service/demos/field-service-demo/?d=7013y0000026jq4AAA&nc=7013y0000026mOdAAI&utm_source=google&utm_medium=sem&utm_campaign=emea_xc_field-service_cross-industry&utm_content=cross-segment_non-brand+exact_7013y0000026jq4AAA_english_field-service-demo&gclsrc=aw.ds&gad_source=1&gad_campaignid=22814411436&gbraid=0AAAABAVtBhSZT4yDw4YPgwVsSG91KSugz&gclid=CjwKCAjwqonVBhA4EiwA9wYJ3S4sLzp3sb2oXMmcw3T7Q0jy5mmYr1C-LbY4_GVKWteom3VJSgn5GRoCnf4QAvD_BwE)（现场服务管理）了解交付，而支持团队负责流程……等等。

因此，现代企业中普遍存在一种AI泄露形式，即各个代理及其框架都在尽力实施自动化智能，尽管它们处于相对孤立的块中。

Salesforce的解决方案是将其所谓的“六大受信任能力”（来自其自身的平台工具集）与一个新的AI控制平面相结合，该控制平面旨在支持一个开放且可组合的AI生态系统。

[Salesforce Enterprise AI Harness](https://www.salesforce.com/agentforce/ai-agents/agent-harness/) 涵盖了跨 [Data 360](https://www.salesforce.com/uk/data/demos/data-cloud/?d=7013y0000026jrrAAA&nc=7013y0000026mQQAAY&utm_source=google&utm_medium=sem&utm_campaign=emea_xc_data-360_cross-industry&utm_content=cross-segment_non-brand+phrase_7013y0000026jrrAAA_english_data-cloud&gclsrc=aw.ds&gad_source=1&gad_campaignid=22814411004&gbraid=0AAAABAVtBhRH7jSRiuxEiM18Vq-hSwMOP&gclid=CjwKCAjwqonVBhA4EiwA9wYJ3eigxoIEgR8P63JfKVD6vOojgDTGgl5YbrHZUddjnzcby7vuLLsv3BoC4mMQAvD_BwE)（统一客户数据平台工具）、[Informatica](https://thenewstack.io/informatica-launches-freemium-ai-powered-integrator/)（数据集成与治理）、[MuleSoft](https://www.mulesoft.com/) 和 Agent Fabric（API连接和多代理编排）、[Tableau](https://thenewstack.io/tableau-informatica-thoughtspot-tout-generative-ai/)（商业视觉分析）、[Agentforce](https://thenewstack.io/a-guide-to-building-scalable-ai-agents/)（代理平台）、[Salesforce Guardian](https://help.salesforce.com/s/articleView?id=mktg.mc_pers_guardian_about.htm&type=5)（安全与合规）以及 Salesforce 平台本身的核心技术，通过通用、可组合的架构和统一的体验来实现。

“代理型企业不会由公司选择的模型来定义。模型将持续变化，智能也将日益普及。使企业产生差异化的，是它为该智能带来的可信、专有的上下文（从客户开始），以及它将这种上下文安全地转化为行动的能力，” Salesforce总裁兼首席平台与工程官 Rohan Kumar 在新闻发布会上说道。

> “代理型企业不会由公司选择的模型来定义……使企业产生差异化的，是它为该智能带来的可信、专有的上下文。”

## 这并非 Salesforce 首次涉足框架

需要明确的是，Salesforce 并非到2026年末才开始生产或使用框架；“六件套”内的子系统，例如 [Agentforce Vibes](https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-overview.html)（一种自然语言的氛围编程工具），已经在使用专门的执行框架，包括 [Mastra](https://mastra.ai/) 和 [Claude Agent SDK](https://thenewstack.io/anthropic-pauses-claude-agent-sdk-subscription-change/) 来管理本地代理执行循环。正如所暗示的那样，这是一次更正式、全平台范围的开发。

除了涵盖上下文、代理能力、行动、治理、安全和模型的六方对齐之外，Salesforce 还提供了一个新的AI控制平面，为开发人员提供了一个查看、管理和控制代理的地方。该公司确认软件工程师可以“将这六者作为一个系统一起使用，或者只使用他们需要的部分”，并利用 Salesforce 技术、其他现有第三方技术或两者结合来进行部署。

这里最大的问题很简单：这是一种旨在将更广泛的 Salesforce DNA 散布到软件开发人员生产环境中的表面包装，还是一种真正有用的简化和统一过程，将会受到关注甚至感谢？

在 [G2](https://documentation.g2.com/docs/developer-portal) 开发者论坛和 B2B 软件评论门户等网站上评论的在职工程师提供了一些见解。

## 开发人员和运营专业人士对 Salesforce 堆栈的看法

在谈到将 Agentforce 作为独立工具使用时，运营助理 Ashish B. 在今年8月指出：“一个可以改进的领域是初始设置和配置过程。构建有效的代理需要一些定制化和对工作流的扎实理解。如果平台能提供更简单的配置选项，并对设置特定业务用例的代理提供更清晰、更直接的指导，那么它会变得更好。”

Salesforce 可能一直在倾听。该公司表示，企业 AI Harness 将推理与业务规则、策略和可预测执行所需的控制连接起来。然后，它使这些能力在整个企业中可重用，以便在代理和模型之间共享上下文。这意味着可以在需要的地方安全地调用行动和工作流，并且随着 AI 在业务中的扩展，可以一致地应用治理和安全措施。

> “如果平台能提供更简单的配置选项，并对设置特定业务用例的代理提供更清晰、更直接的指导，那么它会变得更好。”

在 [Gartner Peer Insights](https://www.gartner.com/reviews/market/data-integration-tools/vendor/salesforce-informatica/product/informatica-cloud-data-integration/review/view/6701538) 上撰写关于 Informatica 用户体验的文章时，一位 DevOps 工程师在今年3月表示，该平台对于集成多个数据源“工作得很好”，并支持批处理和实时处理。但他们警告说，“在复杂的工作流中，调试和监控管道可能很困难。初始设置对于新用户来说具有挑战性，需要一定的学习曲线。[用户界面] 在可用性和更快的导航方面可以改进。”

可能考虑到此类反馈，伴随 Enterprise AI Harness 的新 AI 控制平面声称让企业拥有一个共同的地方来查看、管理和控制整个企业的代理和 AI。

“它使公司能够发现和注册代理及 AI 能力，建立身份和策略，管理生命周期，评估性能，实现可观测性（观察行为和结果），并控制成本——涵盖 Salesforce 和第三方 AI。这赋予了企业在 AI 扩展到团队、应用程序、模型和系统时一致的可见性和控制层——而无需分别管理每个代理或 AI 体验，” Salesforce 承诺道。

## 信任的六大支柱

整个 Enterprise AI Harness 的前提都取决于 Salesforce 所称的六大受信任能力。

受信任上下文（Trusted Context）：将客户上下文与数据、元数据、语义、知识、实时信号、记忆以及对整个企业工作方式的理解相结合。受信任代理（Trusted Agency）：为代理提供推理、规划、状态、记忆和编排功能，在需要确定性的地方结合灵活的 AI 推理和确定性控制。受信任行动（Trusted Action）：安全地将 AI 连接到应用程序、API、工作流、工具和业务流程。

顾名思义，受信任治理（Trusted Governance）：治理 AI 所依赖的数据、元数据、策略和流程，具备谱系、质量、护栏和控制措施。受信任安全（Trusted Security）：将身份、权限、隐私、数据保护和运行时安全应用于 AI 可访问的内容以及代理可执行的操作。受信任模型（Trusted Models）：提供基于准确性、性能、成本和需求的智能模型路由的安全保障。

## 与 Claude、Slack、Teams 等的集成

Enterprise AI Harness 是从底层开始“无头”构建的，其能力可通过 MCP、API、技能和插件等技术访问。该公司表示，这将使 Salesforce 的能力超越传统的 Salesforce 应用程序，延伸到 Claude、Slack 和 Microsoft Teams 等服务中。

构成 Salesforce 受信任企业 AI Harness 基础的许多技术现已可用，新的能力和统一体验计划于 2028 财年初开始推广。