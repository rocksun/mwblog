<!--
title: Chainguard 代理技能服务持续演进，强化 AI 软件供应链安全
cover: https://cdn.thenewstack.io/media/2026/06/8e70c32b-ph4mi-nhat-jfsj-atu2sm-unsplash.jpg
summary: Chainguard 升级了 Agent Skills 服务，通过公共及私有注册表提供经持续强化的 AI 代理技能。该平台旨在解决 AI 代理的安全风险，通过自动化审计、持续修复及补丁机制，为企业级开发提供合规且安全的构建与审查流水线，确保 AI 代理在复杂环境中的安全性与可观测性。
-->

Chainguard 升级了 Agent Skills 服务，通过公共及私有注册表提供经持续强化的 AI 代理技能。该平台旨在解决 AI 代理的安全风险，通过自动化审计、持续修复及补丁机制，为企业级开发提供合规且安全的构建与审查流水线，确保 AI 代理在复杂环境中的安全性与可观测性。

> 译自：[Chainguard Agent Skills matures](https://thenewstack.io/chainguard-agent-skills-matures/)
> 
> 作者：Steven J. Vaughan-Nichols

Chainguard 正加大力度，通过一个新的包含 1,000 多种强化代理技能的公共注册表、私有注册表以及针对企业内部特定技能的强化服务，来保障快速发展的 AI 氛围编程代理世界。

眨眼之间，就会出现一项新的重大 AI 进展。遗憾的是，随之而来的还有安全漏洞。这就是软件供应链安全公司 [Chainguard](https://www.chainguard.dev/) 联合创始人兼首席执行官 [Dan Lorenc](https://www.linkedin.com/in/danlorenc) 最近推出 [Chainguard Agent Skills](https://www.chainguard.dev/agent-skills) 的原因。这是一个[持续维护的强化 AI 代理技能目录](https://www.zdnet.com/article/how-chainguard-is-fixing-trust-in-ai-built-software/)，旨在将“默认安全”实践引入新兴的代理生态系统。现在，Chainguard 已将 Agent Skills 推向了新的水平。

通过此次更新，Agent Skills 为客户提供了受保护的社区技能，并为组织的内部技能提供了一个存储空间。此外，它现在还为那些希望 Chainguard 处理繁重工作以确保其自研代理安全的团队提供了“强化即服务”层级。

Chainguard 工程高级副总裁 [Dustin Kirkland](https://www.linkedin.com/in/dustinkirkland) 告诉我，Agent Skills 使团队能够将代理直接插入其软件构建和审查流水线中，而不必担心受损的技能可能会引入漏洞或泄露数据：“这就是我们为客户提供的隔离防护。”

此版本提供了 1,000 多种最受欢迎的社区技能的强化版本，并且每周都会添加新技能。该[公共目录及其安全代理现已可供任何人提取使用](https://www.chainguard.dev/agent-skills)。

该公司的强化流水线会根据旨在捕捉常见和新兴攻击模式的规则集来扫描公共技能。这些模式包括：

* 过度授权的范围和功能
* 混淆命令和 base64 执行
* 凭据窃取行为
* 从不受信任或可疑的域名下载

简而言之，其理念很简单：将代理技能视为一等软件工件，进行与 [Chainguard 容器](https://thenewstack.io/chainguard-and-the-hunt-for-truly-zero-cve-container-images/) 和 [开源软件包](https://thenewstack.io/chainguard-repository-ai-agents/) 相同的治理、来源追踪和强化。

## 强化是一个持续的过程，而非一次性的关卡

此更新后的服务所做的不仅仅是扫描问题。Chainguard 并没有将其定位为又一个扫描或“发现并标记”服务。当规则集检测到问题时，系统会利用 AI 实际重写并强化该技能。每个强化的技能都附带一份 HARDENING.md 文档，作为审计日志：记录了运行了哪些规则、发现了什么、修改了什么，并确认了修改没有以实质性方式破坏技能的行为。

这里的一个关键设计原则是将强化视为一个持续的过程，而不是一次性的静态审批关卡。Chainguard 明确表示，“今天安全的技能可能会在明天的更新中被攻破。” 欢迎来到 AI 赋能的开发世界，这里每天都会出现安全漏洞。

每当上游技能发生变化时，Chainguard 流水线都会自动重新评估并重新强化它。同时，该公司会持续更新其强化规则以捕获新的攻击模式；当规则集发生变化时，之前强化的技能会再次通过该过程运行。对于最终用户而言，这意味着他们始终提取的是当前强化的版本，而不是依赖可能已经过时数月的单次扫描。

开发人员可以浏览并将强化后的技能安装到一系列代理式编码工具中。具体来说，该服务适用于 Claude Code、Cursor、GitHub Copilot 以及通过其 chainctl 命令行工具使用的 Gemini CLI。其目标是使从“原始社区技能”到“具有审计追踪的强化技能”的切换，成为那些已经在 IDE 和 CLI 中试验代理工作流的团队的无缝升级。

Chainguard 也在尝试解决组织内部代理技能不断蔓延的相关问题。如今，许多此类技能存在于 Slack 讨论串、临时共享文件夹和个人开发人员环境中，几乎没有或完全没有版本控制、访问控制或可观测性。这是一种糟糕的做法。

Chainguard 的解决方案是为内部技能提供适当的注册表命名空间。技能位于 skills.cgr.dev/<org>/<skill_name>:<version>，团队可以使用 chainctl 进行推送和拉取，并通过单个命令在本地安装。

这集中了可发现性，因此团队不再需要重建公司其他地方已经存在的工作流。它还将版本控制规范带入了代理行为中。组织可以将代理固定到特定的技能 SHA，在更改导致问题时进行回滚，并对比版本之间的变化。

权限范围仅限于组织的命名空间。因此，只有该组织才能从其注册表空间推送或拉取技能。对于在严格合规制度下工作或处理敏感数据的团队而言，这种边界非常重要。内部代理技能可以在公司内部共享和重用，而不会泄露到外部。

该公司还为希望 Chainguard 自动强化其内部技能的客户开设了封闭测试版。这包括完整的审计追踪、MCP 集成以及对代理行为的供应链式控制。

通过此测试版，客户可以将自己的技能提交到 Chainguard 的强化流水线，并在标准规则集之上添加自定义检查。作为回报，他们将获得：

* 对其内部技能的自动化审查和补救。
* 与社区技能相同的 HARDENING.md 审计追踪。
* 随着上游代码或规则变化而进行的持续强化循环。

该测试版还附带了 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 集成。对于通过 MCP 服务器和策略引擎展现并执行技能的组织来说，这非常方便。早期参与者将成为首批通过这些渠道使用 Agent Skills 功能的用户。这直接将强化与技能如何暴露给代理以及如何在生产环境中进行治理联系了起来。

这并不适合所有人。其目标用户是那些大规模构建内部代理工具，或在自定义技能具有“真正合规权重”的环境中运营的团队。对于这些组织而言，能够向监管机构或审计人员展示具体的强化流水线和每种技能的审计日志，可能变得像 SBOM（软件物料清单）和来源证明对更传统的软件组件一样重要。

如果这一切听起来很熟悉，那你是对的。Chainguard 将 Agent Skills 定位为该公司在容器和语言生态系统方面早期工作的直接延续。Chainguard 看到了一个熟悉的模式重现。那就是一类新的第三方工件出现，采用速度超过了治理速度，并且在生态系统真正知道如何应对之前，攻击面就已经扩大了。在他们看来，代理技能今天正处于该窗口期。

Chainguard 正在将强化技能的公共目录和私有技能注册表作为标准功能提供给任何拥有 [Chainguard Console](https://c67dcd9a.streak-link.com/C7TcucEnp5LVE__5ugXNRoZ_/https%3A%2F%2Fedu.chainguard.dev%2Fchainguard%2Fchainguard-images%2Fhow-to-use%2Fimages-directory%2F) 帐户的人。该公司还邀请高风险用户参与自定义技能强化的封闭测试版。[您可以立即注册参加封闭测试版。](https://c67dcd9a.streak-link.com/C7KRc2i_f2amC3LIoQtzgcCs/https%3A%2F%2Fwww.chainguard.dev%2Fagent-skills)

这种方法对我来说非常有意义。任何进行 AI 代理赋能开发的人——难道还有人不做吗？——都应该看看这项新服务。