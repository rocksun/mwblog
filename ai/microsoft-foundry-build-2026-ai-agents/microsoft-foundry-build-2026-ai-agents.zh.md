[智能体AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/) 浪潮带来了大量令人印象深刻的演示。然而，它较少产生的是能够在生产环境中经受考验的智能体——即在真实负载、真实数据和真实合规要求下运行的智能体。

在最近举办的 [Microsoft Build 2026](https://news.microsoft.com/build-2026/) 大会上，该公司直接针对这一差距，发布了对 [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) 的一系列更新，这些更新合在一起，使其更接近企业级运行环境，而非仅仅是一个开发者预览版。

该公司对 [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) 进行了广泛的更新，涵盖托管智能体基础设施、评估工具、开放治理规范、内存、知识检索以及扩展的模型选择。单看每一项，都是合理的常规产品更新。但结合来看，它们表明微软已经认定，企业级AI的下一个竞争前沿并非能力——而是可靠性和可治理性。

> 微软似乎已经认定，企业级AI的下一个竞争前沿并非能力——而是可靠性和可治理性。

“在 Build 2026 上，Microsoft Foundry 添加了更多开发者在生产环境部署智能体所需的平台组件：运行环境、工具、内存、Grounding（依据）、模型、可观测性和治理，”微软开发者体验高级项目经理 [Nick Brady](https://www.linkedin.com/in/nicholasdbrady/) 在一篇总结这些发布内容的 [博客文章](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/) 中写道。

## 无需重构的运行环境

基础设施方面的核心是 [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) 中的托管智能体，微软预计该服务将于 2026 年 7 月初正式商用。其架构是一个托管运行环境，每个会话都在拥有专属计算、内存和持久化文件系统访问权限的独立沙箱中运行。

值得关注的是其对开发框架的包容姿态。基于 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)、[GitHub Copilot SDK](https://github.com/github/copilot-sdk)、[LangGraph](https://www.langchain.com/langgraph) 或其他 SDK 构建的智能体无需重构即可进行部署。该服务支持两种协议：用于兼容 OpenAI 的有状态交互的 Responses API，以及用于透传场景（开发者自行控制请求和响应格式）的 Invocations 协议。第二种选择对于那些已经构建了自定义编排且不打算放弃的团队来说至关重要。

该托管运行环境还支持“例行程序”（Routines，目前处于公开预览阶段），允许任何智能体定时或按计划运行——例如夜间问题分流、每日报告等此类工作负载。长期运行的自主智能体则可以获得持久化状态。

伴随运行环境一同推出的，还有现已正式商用的 [Foundry Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)。Brady 将其描述为一款允许开发者“通过模板或 GitHub Copilot 创建智能体，利用追踪可视化在本地调试运行，连接到 Toolboxes（工具箱），并直接从 VS Code 部署到 Foundry Agent Service”的工具。

随着智能体工具数量的增加，工具治理本身也变成了一个工程难题。Foundry 中的 Toolboxes（工具箱，目前处于公开预览阶段）为每种工具类型为智能体提供了一个单一的托管端点。只需配置一次，将任何 MCP 客户端指向单一 URL，Foundry 就会处理身份验证、生命周期和治理。

“技能”（Skills）在项目范围的目录中进行版本控制，并可作为 MCP 资源进行发现，它们现在已成为 Toolboxes 模型中的一等公民。工具搜索功能（同样处于预览阶段）有助于为每项任务选择合适的工具，而不是将整个目录一股脑抛给模型。这对于保证质量和防止上下文窗口膨胀都至关重要。

Toolboxes 还可以连接到 [Microsoft IQ](https://www.microsoft.com/en-us/ai/microsoft-iq)——包括 Work IQ、带有 Fabric 数据智能体的 Fabric IQ、Ontology 和语义模型——这样智能体就可以直接接入企业数据，而无需为每个数据源定制管道。

## 基于策略而非仅仅基准进行评估

在治理方面的发布中，有两项尤为引人注目。第一项是 ASSERT（Adaptive Spec-driven Scoring for Evaluation and Regression Testing，自适应规范驱动的评估与回归测试评分），这是微软基于微软研究院（Microsoft Research）的工作构建的、用于策略驱动智能体评估的新型开源框架。ASSERT 不是让智能体对照静态基准运行，而是将书面策略转化为具体的、可衡量的评估，并生成针对性的场景，以便在进入生产环境之前暴露安全和质量缺陷。它适用于 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)、CrewAI、[LightLLM](https://github.com/ModelTC/lightllm)、OpenAI 以及其他框架。

第二项是 [智能体控制规范 (ACS)](https://commandline.microsoft.com/agent-control-specification-runtime-governance/)，这是一项开放的行业规范，用于在智能体生命周期的五个检查点设置确定性的安全和防护控制：输入、LLM、状态、工具执行和输出。ACS 表现为一个便携的 YAML 合约——可进行版本控制、可审计，且与框架无关。首批合作伙伴包括 Infosys、KPMG、IBM、Aviatrix、BigSpin 和 CrewAI。

这两者的结合直指一个现实问题。智能体在生产环境中的失败往往不是随机的——它们通常集中在可预测的输入类型、工具误用模式和输出边界案例上。ASSERT 使这些失败模式变得可测试，而 ACS 则使这些控制措施能够在不同框架之间移植，并在不同组织之间可审计。

评估技术栈的其余部分还包括：[引导式护栏设置](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guided-set-up)，这是 [Foundry Agent Builder](https://pnp.github.io/blog/post/copilot-studio-vs-agent-builder-vs-foundry/) 中的一个问卷驱动向导，可在无需安全专家参与的情况下推荐 PII（个人身份信息）过滤器、越狱防护和任务遵守度控制；以及 Rubric 评估器，它能根据智能体的定义和使用场景自动生成加权质量标准。

## 内存与知识

Foundry Agent Service 中的内存（目前处于公开预览阶段）现在涵盖三种类型。在 Build 大会上全新推出的“程序性内存”（Procedural memory）可帮助智能体学习如何在多次运行中执行工作，而不仅仅是记录会话中说了什么。Brady 引用了早期的 Tau-bench 结果，显示在接近基线成本的情况下，绝对成功率提高了 7% 到 14%，这一具体数据足以吸引独立同行去复制验证。用户内存（User memory）跨会话保留偏好和事实。会话内存（Session memory）则保持线程内的上下文。

在知识方面，Foundry IQ 推出了公开预览版的无服务器选项，新增了涵盖 Work IQ、Fabric IQ、文件搜索、Azure SQL 和 MCP 的新知识源，并且知识库（knowledge bases）已正式商用，提供有 SLA 保障的检索。Brady 将这一定位描述为用“Foundry 智能体背后的专属知识层”来取代自定义 RAG 管道。Web IQ 则为需要实时外部上下文的智能体提供了低于 200 毫秒的网页 Grounding，且零数据保留。

## 模型与计算

微软宣布了四款进入公开预览版的原生 MAI 模型：用于聊天和推理的 MAI-Thinking-1、用于图像生成和编辑的 MAI-Image-2.5、用于带说话人日志的语音转文本的 MAI-Transcribe-2，以及用于带声音克隆的多语言文本转语音的 MAI-Voice-2。

[Fireworks AI on Foundry](https://azure.microsoft.com/en-us/blog/introducing-fireworks-ai-on-microsoft-foundry-bringing-high-performance-low-latency-open-model-inference-to-azure/) 现已正式商用，通过单一 Azure 端点带来开源模型推理，并提供企业级 SLA、SOC 2 准备就绪以及 PTU Data Zone 支持——无需独立的物理设施或合同，即可实现对开源模型的企业级访问。

微软还声称，在生成微软技术文档等任务中，Frontier Tuning 的成本效率是 GPT-5.5 的 10 倍以上。这一说法足够具体、可供测试，但也足够笼统，在得到证实之前理应保持怀疑。

## 更宏观的图景

Brady 的总结清楚地表明，Build 2026 上关于 Foundry 的发布旨在实现有机结合。托管运行环境处理部署。Toolboxes 处理工具治理。ASSERT 和 ACS 处理评估与控制。内存处理状态。Foundry IQ 处理 Grounding（接地）。Rubric 和 Agent ROI 将智能体表现与业务成果联系起来。Rubric 是 Microsoft Foundry 中一种新型的评估器类型，目前处于公开预览阶段，它能根据智能体的特定上下文自动生成评估标准。

微软坚称，企业级智能体AI需要平台级的基础设施——而这个平台应当是 Foundry。

这一论点能否立足，在很大程度上不取决于 Build 大会上发布了什么，而取决于企业在尝试将智能体从演示（demo）推向实际部署（deployment）时的真实体验。

这正是微软声称要弥合的差距。