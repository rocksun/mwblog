<!--
title: SAS 通过 Viya MCP Server 向 Claude 和 Copilot 等 AI 智能体开放分析引擎
cover: https://cdn.thenewstack.io/media/2026/04/a3b3fd69-img_3755-scaled.jpg
summary: SAS 发布了 Viya MCP Server，通过 MCP 协议允许 Claude、Copilot 等外部 AI 智能体直接调用其分析引擎。SAS 强调将治理视为核心护城河，致力于成为智能体时代的可信后端。
-->

SAS 发布了 Viya MCP Server，通过 MCP 协议允许 Claude、Copilot 等外部 AI 智能体直接调用其分析引擎。SAS 强调将治理视为核心护城河，致力于成为智能体时代的可信后端。

> 译自：[SAS opens its analytics engine to Claude, Copilot and any AI agent with Viya MCP Server](https://thenewstack.io/sas-viya-mcp-governance/)
> 
> 作者：Frederic Lardinois

[SAS](https://www.sas.com/en_us/home.html) 已有 50 年为银行、保险、政府及制造业等受监管行业构建分析和决策软件的经验。现在，它押注治理将成为其在智能体（agent）时代的护城河。

随着 AI 智能体重塑企业软件的消费方式，无论在这个 AI 时代哪种模型或智能体架构获胜，该公司深厚的领域专业知识和[治理](https://www.sas.com/en_us/insights/analytics/ai-governance.html)都可能是保持价值的资产。

正如 SAS 首席技术官 Bryan Harris 周二在德克萨斯州格雷普韦恩举行的 SAS Innovate ’26 大会的主旨演讲中所指出的：“我们用技术赋能人类，以扩展人类的观察和决策能力。自成立以来，SAS 一直在开拓技术突破，帮助您弥补信息鸿沟并获得竞争优势。”

但要在 AI 时代做到这一点，企业——尤其是 SAS 服务的客户——需要能够信任 AI 和 AI 智能体。Harris 认为，SAS 的职责是确保即使大语言模型具有非确定性，也能提供经过验证和校验的可靠结果。

> “我们的角色是确保在关键时刻，通过我们的软件为您提供值得信赖的答案……智能体 AI（agentic AI）只是该技术的又一次进化。”

“我们的角色是确保在关键时刻，通过我们的软件为您提供值得信赖的答案——而智能体 AI 只是该技术的又一次进化，”Harris 在新闻发布会上说道。

![](https://cdn.thenewstack.io/media/2026/04/09713dbd-img_3753-1024x767.jpg)

*图片来源：The New Stack*

## SAS 分析作为可被 MCP 调用的服务

SAS 整体战略的一个核心特征——也是 SAS 在其活动中可能略显低调的一点——是全新的 [Viya MCP Server](https://www.sas.com/en_sg/software/viya/mcp-server.html)，它将其分析和决策能力作为工具，供任何外部 AI 智能体通过模型上下文协议（Model Context Protocol）调用（Viya 是 SAS 的云原生数据和 AI 平台）。

运行 Claude、Copilot 或任何自定义智能体的组织可以使用此 MCP 服务器，例如直接调用 SAS 欺诈检测模型或运行供应链优化，而无需绕过 SAS 为其模型和依赖数据设置的治理机制。

大多数采用 MCP 的供应商都在构建通过协议消费工具的智能体。SAS 也在这样做，但更值得关注的举措是将其自身的分析引擎开放为智能体调用的对象。它将 Viya 定位为受治理的后端，而非编排器，使其成为托管可信模型的地方，无论调用者是谁。

## 智能体、行业模型与治理

MCP 服务器并非 SAS 发布的唯一智能体相关公告。该公司还推出了 Agentic AI Accelerator（一个用于构建受治理智能体的开源框架）；其 CI360 营销平台中的多智能体系统；以及一个能够将为期数天的销售和运营规划周期压缩为持续优化的供应链智能体。

![](https://cdn.thenewstack.io/media/2026/04/380a3a42-img_3750-1024x768.jpg)

*图片来源：The New Stack*

使这些行业智能体不仅仅是 LLM 外壳的原因在于其底层架构。SAS 不构建基础模型；它构建训练于特定领域数据的窄域、专用模型。例如，其欺诈检测模型使用由全球各大银行贡献的财团数据进行训练，包含跨越卡片、数字钱包和申请欺诈的数百万个欺诈事件。供应链智能体则构建在 SAS 现有的优化模型之上。MCP Server 随后使所有这些功能都可从外部调用。

同样的逻辑也延伸到治理本身。SAS 还发布了 AI Navigator，这是一款将于第三季度在 Azure Marketplace 上推出的独立 SaaS 治理产品，它可以对各供应商（包括 Claude、Copilot、开源模型，而不局限于 SAS 自有模型）的 AI 使用案例进行清点和治理。

在某种程度上，治理是 SAS 内部的一个独立产品线，与分析平台相解耦。

![](https://cdn.thenewstack.io/media/2026/04/914786da-img_3733-1024x768.jpg)

*以治理为核心的 SAS Viya 平台。图片来源：The New Stack*

“AI 治理通常被认为是一种合规措施，”SAS AI 伦理、治理和社会影响副总裁 Reggie Townsend 表示。“它其实是增长的驱动力。AI 治理不再是担心影子 AI 让组织陷入风险，而是赋能人们在结构化、透明且安全的环境中挑战 AI 的极限。”

> “AI 治理通常被认为是一种合规措施……它其实是增长的驱动力。AI 治理不再是担心影子 AI 让组织陷入风险，而是赋能人们在结构化、透明且安全的环境中挑战 AI 的极限。”

SAS 在这条路上已经走了一段时间。例如，在 2024 年，该公司开始通过副驾驶（copilots）、合成数据项目和用于模型透明度的模型卡将生成式 AI 集成到 Viya 中。到 2025 年，它引入了智能体，但将其范围限制在决策平台内。SAS 将其描述为“核心业务（Bread and butter）”。现在，SAS 正在此基础上进行构建，同时将该平台定位为其他供应商的智能体可以调用的基础设施。

SAS 的赌注是，即使智能体成为新的界面，即使他们最终无法长期控制智能体平台本身，谁控制了可信的分析和治理，谁就仍然重要。许多 AI 原生初创公司在与大型模型提供商集成时默认就是这么做的，但对于大型企业供应商来说，这并不总是领导层愿意支持的道路。