<!--
title: Chainguard：终结AI代理“乱抓”开源包的安全隐患
cover: https://cdn.thenewstack.io/media/2026/03/48e14202-getty-images-a9zzu-fyz2g-unsplash-1.jpg
summary: AI助手引发软件依赖安全问题，攻击者亦利用AI。Chainguard Repository提供统一安全管理，从源头解决，自动提升安全态势，并关注AI技能劫持。
-->

AI助手引发软件依赖安全问题，攻击者亦利用AI。Chainguard Repository提供统一安全管理，从源头解决，自动提升安全态势，并关注AI技能劫持。

> 译自：[Chainguard has a fix for the open source packages your AI agents keep grabbing](https://thenewstack.io/chainguard-repository-ai-agents/)
> 
> 作者：Darryl K. Taft

随着[AI编程助手](https://thenewstack.io/ai-coding-assistants-are-reshaping-engineering-not-replacing-engineers/)和自主代理显著[加速软件开发](https://thenewstack.io/think-like-a-developer-to-help-dev-teams-ship-faster/)，它们正在引入一个大多数组织尚未准备好的安全问题：以机器速度蔓延的依赖。

Chainguard 首席执行官 [Dan Lorenc](https://www.linkedin.com/in/danlorenc/) 告诉《The New Stack》，编程代理有一个盲点。它们的训练数据通常已经过时一年或更久，这意味着当它们需要一个库时，会默认选择较旧的、通常不安全的版本——这并非因为它们粗心，而是因为它们只知道这些。随着越来越多的生产代码由代理编写，这种模式会迅速加剧。

“当你要求代理生成代码时，它的训练窗口通常是一年前的，”Lorenc 说。“所以，它会默认使用所有这些库的旧版本，因为它就是基于这些旧版本训练的。你可以让代理更新代码，但这比人们试图加快速度需要更多的时间和精力。”

## 攻击者也在使用人工智能

同时，Lorenc 表示攻击者也越来越多地使用人工智能——并非为了意外编写易受攻击的软件包，而是以人类研究员需要数天才能达到的规模和速度，发现并利用错误配置。

他说，最近 [Trivy 项目](https://trivy.dev/)（一个来自 [Aqua](https://thenewstack.io/aqua-securitys-trivy-security-scanner-can-scan-anything-now/) 的[漏洞扫描器](https://thenewstack.io/aqua-security-uncovers-major-kubernetes-attacks/)）的一次数据泄露事件就说明了这种威胁。攻击者部署代理，系统性地识别了数十个 GitHub 组织中的已知错误配置，自动化了原本需要数小时手动挖掘的工作。

“几周前 Trivy 项目发生了一次重大数据泄露，”Lorenc 说。“攻击者通过代理去寻找这些已知的错误配置，从而侵入了数十个其他 GitHub 组织。这对于人类来说可能需要七个小时的工作和挖掘。我们看到越来越多的由人工智能驱动的攻击。”

根据 Sonatype 的年度软件供应链报告，仅在 2025 年，就有近 45.5 万个恶意软件包涌入 npm、PyPI 和 Maven Central。Chainguard 表示，平均每个容器带有 600 多个已知 CVE，89% 的生产环境容器镜像包含已知漏洞。

## 开源的单一入口

为了解决这个问题，Chainguard 周二宣布推出 Chainguard Repository，这是一个统一的、默认安全的开源制品存储库。该产品为开发人员——以及与他们一起编写代码的 AI 代理——提供了一个单一的、受管制的端点，用于拉取开源库、容器、操作系统包和虚拟机，并在消费点强制执行可配置的安全策略。Lorenc 说。

从今天起，Chainguard Repository 已在 JavaScript 生产环境中可用，为客户提供超过 7 万个 Chainguard 构建的 npm 包。这些库是在 SLSA Level 3 合规环境中构建的，并在设计上消除了 99.7% 的恶意软件。对于作为备用从上游 npm 注册表提供的软件包，七天冷静期策略会过滤掉在那个窗口内被更广泛研究社区识别出的恶意软件。

## 冷静期困境

然而，冷静期策略有其局限性，Lorenc 说。这种方法最初出现在 [Snyk](https://thenewstack.io/security-firm-snyk-tackles-ai-codings-perfect-storm/) 的研究中，该研究表明等待一周可以避开大多数恶意软件，但它面临一个结构性问题。也就是说，如果所有人都采用它，攻击者只会调整他们的时间线。

“如果每个人都这样做，那么它的效果就会降低，你必须等待更长时间，”Lorenc 告诉《The New Stack》。“有时你需要在此之前获得软件。如果某个地方存在关键 CVE，你不能等七天才能获得新版本。你正在被一只熊追赶，同时又想抓住另一只。”

组织在处理生产依赖中的关键 CVE 时，并非总能等待一周才能获得修补版本。Chainguard 的解决方案是可配置的例外，允许安全团队在关键修复时绕过冷静期，同时在其他地方保持默认态势。

## 超越安全性的治理

治理用例超出了安全范畴。Lorenc 指出，随着 Chainguard 库覆盖范围的扩大，一些客户现在使用策略控制，仅仅是为了管理可用软件包的庞大数量——并非出于安全原因，而是为了工程规范。

“我们有很多客户，现在我们拥有如此多的库，以至于数量实在太多了，他们希望能够控制开发人员获取哪些库，”Lorenc 说。“也许你不需要 17 种不同的数据库客户端或 32 种不同的日期时间解析器。”

Chainguard 正在展望一个时代，届时开发人员和他们的 AI 工具都无法独立做出安全的依赖选择。Chainguard Repository 可以替代或集成现有制品管理器，如 [Artifactory](https://thenewstack.io/jfrog-brings-artifactory-on-prem-for-aws-with-eks-anywhere/)、[Cloudsmith](https://cloudsmith.com/) 和 [Nexus](https://www.sonatype.com/products/sonatype-nexus-repository)，并补充像 Snyk 和 [Sonatype](https://thenewstack.io/sonatype-offers-its-malicious-source-code-blocker-as-a-service/) 这样的 [SCA 扫描工具](https://thenewstack.io/sca-should-be-in-your-toolbox-to-address-supply-chain-risk/)，这些工具能识别漏洞但无法提供“干净”的版本。

“这是一个你可以直接指向所有客户端的单一入口，我们将控制进入其中的内容，”Lorenc 说。“你可以设置任何你需要的策略。”

## 自我改进的安全性

随着 [Chainguard 的 AI 驱动工厂](https://thenewstack.io/chainguard-500-million-builds/)从源代码重建更多软件包，使用该存储库的组织的安全态势会自动改善，无需配置更改或代码更新。Lorenc 表示，他认为这是关键的架构转变：安全不是事后扫描问题，而是在消费点强制执行。

Lorenc 还指出，AI 技能劫持是一种新兴的威胁向量，行业才刚刚开始关注。虽然 MCP 劫持仍处于早期阶段，但对 AI 技能生态系统（如 skills.sh 等平台，代理在运行时动态拉取工具）的攻击已大规模发生。

“我们现在看到很多 AI 技能劫持，”Lorenc 说。“如果你不安全地部署这些工具，它们会在运行时随意拉取工具。几周前 [OpenClaw 的技能生态系统遭遇了一次大规模攻击](https://thenewstack.io/openclaw-moltbot-security-concerns/)。人们就是这样分享 OpenClaw 工作流的。”

## 展望未来

今年晚些时候，Chainguard Repository 将扩展到 Python 和 Java 库、容器镜像、操作系统包和虚拟机。计划发布的其他策略控制包括：CVE 阻止，以防止拉取含有已知关键漏洞的制品；许可证强制执行，以限制制品使用经批准的许可证；以及生命周期结束阻止，以在未维护的依赖项进入生产环境之前将其拒绝。[Chainguard Repository](https://chainguard.dev/libraries/javascript) 现已可用。