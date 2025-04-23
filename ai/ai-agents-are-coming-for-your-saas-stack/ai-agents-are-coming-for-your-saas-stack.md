<!--
title: AI Agent将变革你的SaaS技术栈
cover: https://cdn.thenewstack.io/media/2025/04/56e4fbda-headway-5qgiuubxkwm-unsplash-scaled.jpg
summary: Agentic AI重塑SaaS！百万TPS挑战下，需从CRUD到对话中心架构转变。LLM无状态性、多模态输入、实时处理成关键。Akka蓝图含流式端点、Agent适配器、Agent编排、上下文数据库及生命周期管理，加速云原生Agentic AI应用交付，避免“孤岛”和“框架陷阱”，赋能企业数据交互。
-->

Agentic AI重塑SaaS！百万TPS挑战下，需从CRUD到对话中心架构转变。LLM无状态性、多模态输入、实时处理成关键。Akka蓝图含流式端点、Agent适配器、Agent编排、上下文数据库及生命周期管理，加速云原生Agentic AI应用交付，避免“孤岛”和“框架陷阱”，赋能企业数据交互。

> 译自：[AI Agents Are Coming for Your SaaS Stack](https://thenewstack.io/ai-agents-are-coming-for-your-saas-stack/)
> 
> 作者：Tyler Jewell

Agentic AI 正在迅速崛起，成为一项变革性的技术力量。近几个月来，Google 上对该术语的搜索量增加了 15,000%。行业领导者称其为“第五次计算浪潮”，并将其定位为从根本上重塑企业应用程序的角色、它们的运作方式以及它们与用户的交互方式。

虽然像 ChatGPT 这样的 AI 助手可以理解自然语言并按需完成任务，但 AI Agent 通过自主实现目标并与其他系统交互，将自动化提升到了一个新的水平。与静态且更具确定性的传统[机器人流程自动化](https://thenewstack.io/robocorp-makes-remote-process-automation-programmable/) (RPA) 系统不同，现代 agentic 系统是随机的、自适应的且以目标为导向的。

当软件即服务 (SaaS) 应用程序与 agentic AI 服务集成时，将会发生最重大的转变，从而创建 Gartner 所谓的“应用/AI 生态系统”。目前，只有不到 1% 的 SaaS 系统通过 agentic 服务得到了增强，但 [Gartner 预测](https://www.gartner.com/en/newsroom/press-releases/2024-03-11-gartner-predicts-one-third-of-interactions-with-genai-services-will-use-action-models-and-autonomous-agents-for-task-completion-by-2028?utm_source=chatgpt.com)，未来四年内，全球三分之一的 SaaS 将支持 AI。

**规模和架构挑战**

其规模影响是惊人的。在当前的移动计算时代，大型系统通常每秒处理大约 10,000 笔事务 (TPS)。在 agentic 时代，由于可能有数十个 AI 助手持续帮助每个用户，事务量可能会增加两个数量级，达到大约 100 万 TPS。

agentic 转变需要从以事务为中心的系统到以对话为中心的系统的根本性架构变更。传统的 SaaS 应用程序构建在无状态业务逻辑之上，该逻辑针对关系数据库执行 CRUD 操作。相比之下，agentic 服务在服务本身内维护状态，并存储每个事件以跟踪服务如何达到其当前状态。

一个关键的架构挑战源于[大型语言模型](https://thenewstack.io/what-large-language-models-can-do-well-now-and-what-they-cant/) (LLM) 的无状态性质。与维护状态的数据库不同，LLM 不记得之前的对话。这就需要维护一个对话日志，其中每次新请求都必须包含所有先前的交流，以提供上下文。随着这些日志的增长，它们最终会达到 token 容量限制，需要仔细的管理策略。

**多模态输入和实时处理**

Agentic 系统不限于基于文本的聊天界面。它们将越来越多地整合物联网 (IoT) 传感器、指标、音频和视频输入，从而创建必须处理、增强并转发到适当模型的[实时数据流](https://thenewstack.io/bridging-the-data-gap-real-time-user-facing-analytics/)，而不会使系统不堪重负。在 agentic 系统实时处理的内容与速度较慢、成本较高的 LLM 可以处理的内容之间取得平衡仍然是一个微妙的挑战。

**性能和成本考虑因素**

Agentic 应用程序的性能概况与传统的 CRUD 应用程序截然不同。关系数据库的延迟通常为 10-30 毫秒，而 LLM 的延迟则高出 100 倍。此外，与仅使用数据库的环境相比，每次事务的成本增加了多达 10,000 倍，其中最复杂的 LLM 每次事务的成本比数据库调用高出 850,000 倍。

人们对成本持乐观态度，因为在过去三年中，LLM 的定价每年持续下降 90%，同时保持了相同的准确性水平。这一趋势表明成本效率将继续提高，尽管不会以同样惊人的速度提高。

**生产挑战**

将 agentic 系统投入生产仍然很困难。Gartner 的一项调查发现，52% 的组织未能成功部署其 agentic 系统。失败的原因包括实验性方法、数据质量问题、安全问题、行不通的成本等式以及不适合并发、内存管理或 24/7 运行的技术。许多组织需要八个多月的时间才能从概念验证过渡到生产。

部署策略各不相同，组织会考虑云原生平台 (62%)、虚拟私有云（约三分之一）和自托管 Kubernetes 环境（约一半）。许多组织同时考虑多种部署模型。

**SaaS 和 Agentic AI 的未来**

虽然 Agentic AI 服务将越来越多地增强 SaaS 应用程序，但它们不太可能完全取代它们。Agentic 处理循环的高延迟使其不适合高容量、实时用户交互。这意味着 SaaS 应用程序仍然需要提供必要的 API 和多用户并发接口。

SaaS 应用程序的接口将变得越来越多元化，具有更多的视听交互。特定应用程序可能主要（70-80%）是 Agentic 的，比例因用例而异。

对于考虑 Agentic 服务的企业来说，关键成本因素包括 LLM 托管（通过按 token 定价的云服务或自托管）、计算和内存需求、用于语义搜索的[向量数据库存储](https://thenewstack.io/onehouse-automates-vector-embedding-for-its-data-lakehouse/)以及 Agentic 平台本身。虽然运营管理与传统的 SaaS 系统类似，但最大的挑战是确保随着 AI 模型的演进，其具有可解释性和可追溯性。

随着我们进入这个新时代，组织必须仔细平衡性能、成本和[用户体验注意事项，才能成功实施 Agentic AI 系统](https://thenewstack.io/graphql-can-compose-headless-systems-to-boost-user-experience/)，从而充分发挥其变革潜力。

**Akka 建议的 Agentic 服务蓝图**

Akka 已经开发了一个全面的 Agentic 服务蓝图，其中包含五个基本要素。首先，流式传输端点对于处理多模式实时数据是必要的。其次，[Agent 连接适配器支持与向量数据库的集成](https://thenewstack.io/how-ai-agents-are-about-to-change-your-digital-life/)、LLM 和第三方系统。第三，Agent 编排是核心，提供支持并行处理和人机协作方法持久工作流。第四，平台本身必须存在一个上下文数据库，包括内存中和持久化两种形式，以维护历史记录并支持这些系统的对话风格。最后，生命周期管理提供治理机制，整个系统需要安全性、可扩展性和可观测性。

Akka 通过将 LLM 视为事件驱动的机器而不是基于批处理的系统来区分其平台。他们的适配器是非阻塞的，具有反压功能，允许事件从 LLM 流回系统进行推理或流出到端点。一个关键优势是 API 服务和 Agentic 服务在共享计算上运行，避免了“孤岛问题”，并提高了常规服务和昂贵的 LLM 调用的效率。

Akka 平台旨在加速 Agentic AI 应用程序的交付，因为这些技术正从数据科学部门转移到核心交付组织。有两个常见的陷阱：“工作流孤岛”问题，它降低了生产力并增加了成本；以及“框架陷阱”，即最初简单的工具面临着生产问题，如锁定并发和内存管理挑战。

Akka 将此视为堆栈演进，创造了“A-tier 架构”一词来描述 Agentic 服务如何增强而不是取代现有的 SaaS 架构。他们的实现包括非阻塞异步 LLM 适配器、自动内存中和持久上下文数据库、一个基准测试为 1000 万 TPS 的事件驱动系统、开发人员友好的工作流工具以及具有复制过滤功能的多区域部署功能，以满足合规性要求。

Akka 有几个成功的实现，包括开源 SMILE 项目，该项目为 Amazon 和 Google 等主要公司的机器学习 (ML) 系统提供支持；Swiggy，其延迟提高了 90%；以及 Horn 等初创公司，该公司为视频通话提供 AI 增强功能；以及 Coho AI，据报道，该公司使用 Akka 将上市速度提高了 75%。

展望未来，Akka 认为该行业正朝着通过元数据结构更好地与业务数据库和系统集成，从而使 LLM 能够与企业数据交互并对其采取行动。他们的方法将 Akka 定位为[构建 Agentic AI 服务](https://thenewstack.io/tutorial-build-a-rag-agent-with-azure-ai-agent-service-sdk/)的最快方式，这些服务既能推理又能进行交易。