周三，安全研究员 Chaofan Shou 发现 Anthropic 发布了 2.1.88 版的 Claude Code，其 npm 包中附带了一个 59.8MB 的源映射文件。源映射用于在调试期间将打包的生产代码连接回原始源文件，而这个源映射将互联网连接到了 1,900 个文件中的 512,000 行未混淆的 TypeScript 代码。

Anthropic 在数小时内撤下了该软件包，证实这是由人为错误导致的打包问题，但镜像文件已在 [GitHub](https://github.com/Kuberwastaken/claude-code) 上。[*The Register*](https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/) 报道称，原始仓库在上传者将其替换为 Python 移植版之前已被 fork 了超过 41,500 次。

此后的报道集中在单个功能上。一个电子宠物系统。动物代号。开发者 [Wes Bos](https://x.com/wesbos/status/2038958747200962952) 发帖称他直接去寻找加载动画中的动词，并发现了 187 个，从“沉思”和“哲学思考”到“胡言乱语”和“光合作用”。

**真正重要的故事是其结构层面。** [*VentureBeat*](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know)、*The Register* 和数十名开发者对泄露代码库的独立分析揭示了一个生产级代理系统，该系统与开源生态系统也在竞相构建的设计模式不谋而合。

对于熟悉操作系统内部机制的开发者来说，这些模式会很熟悉：带有权限门控的系统调用接口、基于能力的隔离进程分叉、用于内存管理的后台守护进程以及用于发布策略的编译时功能标志。

Claude Code 不是一个聊天封装器。泄露的源代码显示它是一个代理操作系统，其架构直接映射到 [CrewAI](https://github.com/crewAIInc/crewAI)、[Google ADK](https://github.com/google/adk-python)、[LangGraph](https://github.com/langchain-ai/langgraph) 和 [AWS Strands](https://github.com/strands-agents/sdk-python) 中团队已在评估用于生产部署的模式。

Claude Code 的工具系统包含 40 多个独立功能，每个功能都作为单独的模块实现，并带有自己的权限门控。文件读取、bash 执行、网络抓取、LSP 集成和 MCP 服务器连接都作为独立的工具存在，代理通过统一接口调用它们。仅基础工具定义就涵盖了 29,000 行 TypeScript 代码。可以将其视为 Unix 内核中的系统调用层。用户空间程序（LLM 推理循环）从不直接触及硬件（文件系统、终端、网络）。每一次交互都通过一个经过权限检查的网关。

![](https://cdn.thenewstack.io/media/2026/03/0f03a531-claude-code-syscall-1024x1005.png)

这种架构解决了 Kubernetes RBAC 为 Pod 级别 API 访问所解决的相同问题。一个只能读取文件但不能执行 bash 命令的代理，其安全配置文件与拥有完全 shell 访问权限的代理不同。

Claude Code 在工具层面强制执行这一点，独立地门控每个功能，以便不同的上下文可以授予不同的权限集。考虑一个 Claude Code 在不熟悉的仓库中运行的场景。工具系统可以限制 shell 执行，同时允许文件读取和搜索，从而防止代理在不受信任的环境中运行任意代码，同时又不损害其理解代码库的能力。这就是细粒度的能力安全性，泄露的代码显示 Anthropic 通过 POSIX 系统几十年来使用的相同架构模式来强制执行它。

工具系统背后的 46,000 行查询引擎处理所有 LLM API 调用、流媒体、缓存和编排。它是代码库中最大的单个模块，并充当内核调度器，决定哪些工具调用要批量处理，哪些响应要缓存，以及如何在长时间运行的会话中管理上下文窗口。

## 多代理集群与进程编排

泄露的源代码显示 Claude Code 可以生成具有受限工具集的子代理，每个子代理都在隔离的上下文中运行。Anthropic 将此系统称为“swarms”（集群），由 `tengu_amber_flint` 功能标志控制。该架构支持两种类型的“队友”：进程内队友（使用 AsyncLocalStorage 进行上下文隔离）和基于进程的队友（在独立的 tmux 或 iTerm2 窗格中运行，并带有颜色编码输出以进行视觉区分）。团队内存同步保持代理之间的协调。

这是带有基于能力安全性的进程分叉。一个父代理识别一个可并行化的任务，生成具有其自身权限子集的子代理，并收集它们的结果。子代理不能提升自己的访问权限。它们在父代理定义的边界内运行。这与容器编排直接并行。在 Kubernetes 中，控制器生成具有特定资源限制和 RBAC 绑定的 Pod。在 Claude Code 中，协调器生成具有特定工具权限和上下文边界的子代理。

CrewAI 通过其“crew”抽象实现了类似的模式，其中具有明确角色的代理在共享任务上协作。Google ADK 使用分层代理树，其中根代理委托给子代理。LangGraph 将相同的工作流建模为具有显式状态转换的有向图中的节点。所有四个系统都解决了相同的问题。复杂任务需要多个并行运行、共享选择性上下文并合并其输出的推理线程。Anthropic 在其闭源 CLI 中构建了其版本。开源生态系统使用不同的隐喻构建了等效版本。融合比实现细节更重要。

## KAIROS 和后台服务中的梦想系统

泄露中最具启发性的功能是 [KAIROS](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know)，一种在源代码中被引用超过 150 次的自主守护进程模式。KAIROS 将 Claude Code 从一个请求-响应工具转变为一个持久的后台进程。它维护仅追加的每日日志文件，接收周期性的 `<tick>` 提示，使其能够决定是主动行动还是保持安静，并强制执行 15 秒的阻塞预算，从而确保主动行动不会中断开发人员的工作流程超过短暂的暂停。

可以将 KAIROS 视为 AI 代理的 systemd 服务。它按照自己的时间表启动、持久化、监视和行动。当处于活动状态时，它使用一种名为“Brief”（简要）的特殊输出模式，提供适合持久助手（不应淹没终端）的简洁响应。

伴随功能 autoDream 作为分叉的子代理在 `services/autoDream/` 目录下运行。在空闲期间，它通过合并跨会话的观察结果、消除逻辑矛盾并将暂定笔记转换为已确认事实来执行内存整合。这是代理状态的垃圾回收。操作系统运行后台进程以整理内存、整合日志和清理缓存。autoDream 为代理在数天或数周的连续使用中积累的知识做同样的事情。

这里讨论的任何主要开源代理框架都没有发布可与之匹敌的后台自主功能。CrewAI、LangGraph、Google ADK 和 AWS Strands 都以请求-响应或工作流触发模式运行。最接近的是 Nous Research 的 [Hermes Agent](https://github.com/NousResearch/hermes-agent)，它最近添加了带有会话记忆的持久多代理配置文件，但没有 KAIROS 实现的主动观察和整合循环。Anthropic 在功能标志背后构建的功能与开源生态系统目前提供的功能之间的差距在此类别中最大。

## 编译时功能门控作为发布策略

泄露的源代码包含 44 个编译时功能标志。其中至少有 20 个门控着已构建和测试但未出现在外部发布版本中的功能。KAIROS、协调器模式、带完整一键通界面的语音模式、ULTRAPLAN（一种将复杂任务卸载到运行 Opus 4.6 的云容器中，最长可达 30 分钟的远程规划模式）以及 Buddy（带有 18 种物种和稀有度等级的 Tamagotchi 式伴侣宠物）都位于在外部构建中编译为 false 的标志之后。

这是成熟的平台工程团队发布软件的方式。Chrome、Android 以及 Google 和 Meta 的大型基础设施项目都使用编译时功能门控来将功能完成与功能发布解耦。

工程师持续将完成的代码合并到主分支。产品经理为构建目标、用户细分或部署环选择性地启用标志。用户看到的发布节奏（Claude Code 每两周发布一个新功能）并不反映开发节奏，开发节奏要快得多。代码库还区分了仅供 Anthropic 员工使用的“Ant-only”工具和所有用户可用的外部工具。

内部工具包括遥测仪表板、模型切换覆盖以及“Undercover Mode”（卧底模式）系统，该系统可防止 Claude 在贡献公共开源仓库时泄露 Anthropic 的内部代号。

> Anthropic 构建了一个完整的子系统来防止其 AI 在 git 提交中泄露内部细节，然后却因构建配置失误而泄露了该子系统本身。

这种讽刺意味十足。Anthropic 构建了一个完整的子系统来防止其 AI 在 git 提交中泄露内部细节，然后却因为构建配置的疏忽而泄露了该子系统本身。

源代码还暴露了 Undercover Mode 旨在隐藏的内部模型代号。根据对泄露的迁移目录的分析，Capybara 指的是 Claude 4.6 的一个变体（之前 [报道](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/) 为“Mythos”的同一模型），Fennec 对应 Opus 4.6，而一个未发布的名为 Numbat 的模型仍在测试中。内部基准测试显示，最新迭代的 Capybara 具有 29-30% 的虚假声明率，比早期版本的 16.7% 有所退步，同时还有一个旨在防止模型过度激进地重写代码的“自信心平衡器”。

## 接下来会怎样

Claude Code 源代码的意外发布提供了一个难得的架构基准。权限门控工具系统、多代理集群、用于内存管理的后台守护进程以及编译时功能门控并非 Anthropic 独有的发明。CrewAI、Google ADK 和 LangGraph 通过完全独立的开发路径达到了能力隔离和代理协调的类似解决方案。这三个层面的趋同证实了这些模式正在成为生产级代理系统的标准架构，无论由谁构建。

后台自主性和跨会话内存整合是 Claude Code 领先幅度最大的地方。这里审查的任何代理框架都没有发布与 KAIROS 或 autoDream 媲美的东西。现在，数千名开发者有了一个具体的参考实现可供研究，这一差距将更快地缩小。

架构细节令人着迷。安全影响是立竿见影的。泄露的源代码暴露了 Claude Code 精确的权限执行逻辑、其钩子编排路径以及它用于决定何时在不熟悉的仓库中执行代码的信任边界。

> “您的构建管道现在是您攻击面的一部分，一个配置错误的忽略文件就能将您最复杂的产品变成一份公开的蓝图。”

攻击者现在有了制作利用这些特定机制的仓库的路线图。时机让情况变得更糟。在泄露发生数小时内，广泛使用的 Axios npm 包发生了另一次供应链攻击，将一个远程访问木马注入到 1.14.1 和 0.30.4 版本中。[*VentureBeat*](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) 报道称，任何在 3 月 31 日协调世界时 00:21 到 03:29 之间通过 npm 安装或更新 Claude Code 的人，可能都引入了受感染的依赖项。

此后，Anthropic 已将其原生安装程序指定为推荐的安装方法，完全规避了 npm 依赖链。Bun 的打包工具默认生成源映射，除非明确禁用，这暗示了 59.8MB 的 .map 文件如何最终出现在 npm 包中的可能机制，尽管 Anthropic 尚未确认导致此问题的具体构建配置。

对于每个通过包管理器发布 AI 代理的团队来说，教训是直白的。您的构建管道现在是您攻击面的一部分，一个配置错误的忽略文件就能将您最复杂的产品变成一份公开的蓝图。