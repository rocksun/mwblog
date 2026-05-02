<!--
title: IBM Bob 席卷 8 万开发者：生产力提升 45%，重塑企业级 AI 开发
cover: https://cdn.thenewstack.io/media/2026/05/9560241d-sayyam-abbasi-5dcnacdz_fs-unsplash.jpg
summary: IBM推出智能体开发平台IBM Bob，已在其内部8万名开发者中应用，平均提升45%生产力。该平台聚焦企业级治理、合规与遗留系统维护，支持多模型自动编排。
-->

IBM推出智能体开发平台IBM Bob，已在其内部8万名开发者中应用，平均提升45%生产力。该平台聚焦企业级治理、合规与遗留系统维护，支持多模型自动编排。

> 译自：[IBM Bob hits 80,000 developers with 45% productivity gains](https://thenewstack.io/ibm-bob-agentic-development/)
> 
> 作者：Darryl K. Taft

[IBM](https://thenewstack.io/ibm-tackles-shadow-ai-an-enterprise-blind-spot/) 正押注于 [AI 辅助开发](https://thenewstack.io/three-ai-assisted-development-skills-you-can-start-using-today/)的下一个竞争前沿并非纯粹的[代码生成](https://thenewstack.io/ai-code-generation-trust-and-verify-always/)速度，而是治理、可审计性以及在不容有失的企业环境中部署 AI 的操作规范。

这就是本周发布的 [IBM Bob](https://bob.ibm.com/) 背后的核心逻辑，它是该公司新推出的[智能体开发](https://thenewstack.io/agentic-ai-is-quickly-revolutionizing-ides-and-developer-productivity/)平台。Bob 自 2025 年 6 月起已在 IBM 内部运行，规模从 100 名开发者扩展到其全球员工队伍中的 8 万多名用户。

受访用户报告平均生产力提升了 45%。在特定团队中，这一数字更高。例如，[IBM Instana](https://www.ibm.com/products/instana) 团队报告在选定任务上的时间缩减了 70%，而 [Maximo](https://www.ibm.com/products/maximo) 开发团队估计在通常需要耗时数天的代码生成和重构工作中节省了 69% 的时间。

IBM 指出，这些是用户自报的数据。这一说明很重要。但内部部署本身是一个更有趣的数据点。

IBM 软件部门自动化与 AI 总经理 Neel Sundaresan 在加入 IBM 之前，曾是构建原始 [Microsoft GitHub Copilot](https://thenewstack.io/github-copilot-interaction-data/) 团队的一员。Neel Sundaresan 告诉 *The New Stack*：“我们非常熟悉所有这些企业级工作负载。在我们去敲客户的大门之前，我们就已经有了自己的故事。”

Neel Sundaresan 表示，这个故事涵盖了从 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 应用现代化到 [COBOL](https://thenewstack.io/cobol-everywhere-will-maintain/) 维护，再到 [FedRAMP](https://thenewstack.io/ship-fast-break-nothing-launchdarklys-winning-formula/) 合规工作——这类遗留系统密集、风险敏感的开发工作，正是大多数 AI 编程工具并未真正针对性构建的领域。这是一个刻意的定位举措。IBM 并没有在 Cursor 或 GitHub Copilot 的地盘上追逐它们。

Bob 围绕完整的软件开发生命周期（规划、编码、测试、部署和现代化）构建，协调 IBM 所谓的跨每个阶段的角色化专业智能体。该产品附带 [Bob Shell](https://bob.ibm.com/docs/shell)，这是一个 [CLI](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/)（命令行界面），可以实时创建自归档的审计轨迹，确保每个智能体的操作都是可追溯的。安全控制——包括提示词规范化、敏感数据扫描、实时策略执行和 AI 红队测试——是嵌入到工作流中的，而不是事后补救。

IBM 表示，最后一点是对一个已知问题的直接回应：该公司引用行业数据指出，45% 的 AI 生成代码在没有经过充分审查的情况下就进入了生产环境。

多模型编排层是 Bob 技术架构中最有趣的地方。Bob 不要求开发者选择模型，而是自动路由任务——调用 [Anthropic Claude](https://thenewstack.io/anthropic-doubles-claude-usage-outside-peak-hours/)、[Mistral](https://thenewstack.io/mistral-vibe-cloud-agents/) 开源模型、[IBM Granite](https://www.ibm.com/granite) 以及一套专门为 Bob 环境构建的专有微调模型。较轻的代码补全任务交给更小、更便宜的模型。复杂的推理任务则交给更大的前沿模型。Neel Sundaresan 将 Granite 描述为主要适用于代码补全的小模型，其扮演的角色较为局限。“我会说 90% 以上的任务都是像大任务那样的，”他说。

> “我们不会受成本限制，但我们会参考成本信息。”

这种成本意识的框架是故意的。“我们不会受成本限制，但我们会参考成本信息，” Neel Sundaresan 说道。他将让开发者为简单的提示词自选最新的前沿模型比作“开着法拉利去买牛奶”——技术上可行，但昂贵且没必要。IBM 不向用户暴露底层模型，路由是由系统自动管理的。

IBM 表示，这与那些将模型选择作为功能的工具相比，是一种有意义的哲学差异。

## Bob 2.0？

“如果你看看今天流行的编程助手，很多都是 VS Code 的分支，或者是类似 VS Code 的分支，这为我们提供了 IDE 所需的最低功能。然后所有的 AI 都叠加在上面，你可以构建出惊人的体验，” Neel Sundaresan 说道。接着，在 2025 年，“人们开始问，‘我为什么甚至需要 IDE？我为什么不能在 shell 中完成？’这就是为什么 Claude Code 出现了，也是为什么我们有了 Bob Shell……”他指出。

> “你不需要界面。最好的界面就是没有界面……随着我们向 Bob 演进，2.0 版的 Bob 将成为一个智能体。”

Neel Sundaresan 认为，“你不需要界面。最好的界面就是没有界面，对吧？所以，随着我们向 Bob 演进，2.0 版的 Bob 将成为一个智能体。你可以把 Bob 嵌入到几乎任何你想要的地方，它是一个能让你的体验变得与众不同的 AI 引擎。”

他解释说，Bob 可能会出现在你的手机上或你的应用程序中。它也可能针对咨询顾问，他说道。

“我们有数千名咨询顾问，” Neel Sundaresan 说。“你可以让他们身边跟着一群 Bob 顾问，因为咨询工作的很多负载与工程工作非常不同。”

## 大规模验证——带有附加说明

与此同时，早期的客户结果展示了 IBM 通常为客户所做的工作类型。[Ernst & Young](https://www.ey.com/en_us) 正使用 Bob 在其全球税务平台上加速重构、测试生成和文档编写。云解决方案公司 [Blue Pearl](https://www.bluepearl.co.za/#about) 表示，Bob 将典型的 30 天 Java 升级压缩到了 3 天，节省了 160 多个工程小时，且部署后零缺陷。处理政府现代化项目的 [APIS IT](https://www.apis-it.hr/web/naslovnica) 在[大型机](https://thenewstack.io/broadcom-investing-in-mainframe-success-beyond-code/)和 [.NET](https://thenewstack.io/net-modernization-github-copilot-upgrade-eases-migrations/) 系统上报告称，架构分析速度提高了 10 倍，记录遗留 JCL/PL/I 代码的准确率达到 100%。

“开发企业平台不仅仅是为了速度。它关乎深刻理解嵌入的逻辑、维护架构标准以及负责任地演进系统，” Ernst & Young, LLP 税务平台负责人兼首席产品官 [Christopher Aiken](https://www.linkedin.com/in/neel-sundaresan-a964a2/) 在一份声明中表示。“EY 团队利用 IBM Bob 应用 AI 来更好地解释复杂逻辑并简化变更引入方式，帮助为可扩展的转型奠定更坚实的基础。”

这些案例中贯穿的一致线索是，所有三个案例都涉及那种深度受困于遗留系统的企业环境，而这正是其他工具倾向于避开、而 IBM 所擅长的领域。

## Bob 的定位

智能体编程市场现在已经有来自 AWS (Kiro)、JetBrains (Central)、GitHub (Copilot Workspace) 以及许多其他玩家的严肃入局。Neel Sundaresan 直接承认了这一领域的拥挤。

“我不认为我是为了击败其中某一个产品而存在的，”他说。“虽然有排行榜之类的数据，但如果你看本质，我们所有人都有类似的模型。如果你没有合适的模型，你甚至没有入场券。所以，真正的关键在于你在这些模型之上增加了什么价值，你如何编排这些模型，你如何维持成本——这才是问题所在。”

IBM 的答案是企业针对性：将数十年的 Java、[zSystems](https://www.ibm.com/history/eserver-zseries)、COBOL 和安全合规经验嵌入到工具的工作流中，而不仅仅是营销话术中。随着市场的成熟，这究竟是一个真正的护城河，还是对竞争对手也在努力构建的功能的重新定位，是一个值得后续关注的问题。

Bob 目前作为 SaaS 产品提供，并有 30 天免费试用期。本地化部署（将解决受监管行业的数据驻留要求）被描述为未来的目标，目前尚无明确的时间表。