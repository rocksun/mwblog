<!--
title: AI劣质内容席卷开源，96%代码库面临风险
cover: https://cdn.thenewstack.io/media/2026/03/dedb3857-sara-oliveira-lrcuhurala8-unsplash-scaled.jpg
summary: 人工智能生成的劣质内容正在DDoS攻击开源软件，导致维护者工作量剧增，一些项目因此关闭。这不仅浪费了维护者的时间，还引入了安全风险，并侵蚀了开源社区的真实性与信任。为应对危机，社区正在探索多种策略，包括制定AI使用政策、利用平台工具、建立贡献者声誉系统和加密身份证明。文章强调，开源生态系统的未来，很大程度上取决于贡献者的问责制和社区的协作。
-->

人工智能生成的劣质内容正在DDoS攻击开源软件，导致维护者工作量剧增，一些项目因此关闭。这不仅浪费了维护者的时间，还引入了安全风险，并侵蚀了开源社区的真实性与信任。为应对危机，社区正在探索多种策略，包括制定AI使用政策、利用平台工具、建立贡献者声誉系统和加密身份证明。文章强调，开源生态系统的未来，很大程度上取决于贡献者的问责制和社区的协作。

> 译自：[96% of codebases rely on open source, and AI slop is putting them at risk](https://thenewstack.io/ai-slop-open-source/)
> 
> 作者：Bill Doerrfeld

冗长的修改。毫无意义的描述。贡献者无法解释的拉取请求。人工智能正在用劣质内容对开源软件（OSS）进行 DDoS 攻击，一些维护者因此选择退出。

正如 [Anaconda](https://www.anaconda.com/)（一个 Python 数据科学平台）的现场首席技术官 [Steve Croce](https://www.linkedin.com/in/steve-croce-1060082/) 告诉 *The New Stack* 的那样，“它正在对维护者的工作量产生深远影响。”他补充说，作为回应，维护者们正在[取消漏洞赏金计划](https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/)并引入更严格的贡献者指南。

一些项目，如 [Jazzband](https://github.com/jazzband)，已被迫完全停止运营。[Jannis Leidel](https://www.linkedin.com/in/jezdez/)，主要维护者和 Python 软件基金会主席，[写道](https://jazzband.co/news/2026/03/14/sunsetting-jazzband)“铺天盖地的 AI 生成的垃圾 PRs 和问题”使他的项目无法持续。

根据咨询公司 Red Monk 的高级分析师 [Kate Holterhoff](https://www.linkedin.com/in/kateholterhoff/) 博士的说法，现在进入门槛极低，这使得利用传统的开源参与激励模式变得更容易。她告诉 *The New Stack*，“它正在以前所未有的方式危及维护者和贡献者之间的契约。”

例如，负责开源 Godot 游戏引擎的 Rémi Verschelde [在 BlueSky 上分享道](https://bsky.app/profile/akien.bsky.social/post/3meyerixvhs2p)，处理 AI 劣质内容“令人心力交瘁，士气低落”。[其他项目维护者](https://www.theregister.com/2026/02/18/godot_maintainers_struggle_with_draining/)报告说，面对这种洪水般的涌入，冷漠感日益增长，时间也浪费了。

公平地说，现在几乎所有的软件开发人员都使用 AI，许多社区也依赖它来生成合法的修复和贡献。但是，低质量提交的数量正变得不可持续，特别是考虑到 60% 的维护者是[无偿志愿者](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/)。

GitHub [已意识到这个问题](https://github.com/orgs/community/discussions/185387)，并发布了工具来帮助维护者，甚至建议[完全禁用 PRs](https://www.theregister.com/2026/02/03/github_kill_switch_pull_requests_ai/)，同时探索长期解决方案。然而，目前核心问题的修复仍然难以捉摸。

下面，我们将探讨这个问题，并考虑正在出现的管理危机的策略——希望能在它彻底压垮[世界上大部分依赖的](https://thenewstack.io/is-open-source-in-trouble/)开源生态系统之前。

## AI 劣质内容背离了开源的初衷

开源以前也面临过生存威胁，包括[许可协议的转变](https://thenewstack.io/open-source-is-at-a-crossroads/)、[资金缺口](https://www.infoworld.com/article/3557846/how-do-we-fund-open-source.html)和[维护者倦怠](https://thenewstack.io/how-maintainer-burnout-is-causing-a-kubernetes-security-disaster/)。但“劣质内容末日”引入了一种新型的压力。

最直接的风险是维护者时间的浪费。一位开发者估计，审阅者审查和修正一个拉取请求所需的时间是使用 AI 生成该请求的[12倍](https://webmatrices.com/post/vibe-coding-has-a-12x-cost-problem-maintainers-are-done)。

生成干净、可读且可维护的代码仍然很困难。低质量的 AI 贡献需要不成比例的时间来评估和响应，这会降低士气，并可能淹没高价值的提交。

安全风险是另一个担忧。“AI 生成的贡献可能会引入微妙的漏洞、理解不足的依赖项或不完整的修复，从而扩大攻击面，”Anaconda 的 Croce 补充道。

情况可能迅速恶化。在一个离奇的事件中，一个怀恨在心的 AI 代理[发表了一篇猛烈抨击](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/)一位开源维护者的文章，因为其代码建议被拒绝。该维护者 [Scott Shambaugh](https://www.linkedin.com/in/wsshambaugh/)，Leonid Space 的创始人兼 [matplotlib](https://matplotlib.org/) 的贡献者，表示他感到有必要迅速回应以保护自己的声誉。

Shambaugh 告诉 *The New Stack*，“我当时真切地感觉到‘哦，我需要抢先一步’，这样我的版本的事实才能占据主导地位。”

对他来说，这一事件反映了开源领域真实性更广泛的侵蚀。他说，过去，你的声誉与你的贡献息息相关，人们参与其中是为了回馈社区、获得认可并通过协作反馈循环进行学习。

维护者反过来也以管理为荣。但如今，通过快速生成的 PR 来迅速利用漏洞赏金系统或在开源中获得凭证的尝试正在破坏这种动态。

Shambaugh 说：“如果你只是将一个 AI 代理指向一个 GitHub 问题，它可以在 30 秒内解决并编写一个 PR。”“如果那真是我们想要的，维护者自己就能做到。”

## 管理开源中 AI 生成贡献的方法

那么，开源维护者和整个科技行业可以做些什么来管理 AI 劣质内容的涌入呢？

没有单一的解决方案。相反，它可能需要结合新的贡献者政策、平台工具、声誉和验证系统，以及来自基金会和其他社区主导的倡议的指导。

## 为贡献者制定 AI 政策

一种回应是更清晰的贡献者指南。目标通常不是关闭外部贡献的大门或彻底禁止 AI，而是确保其使用能带来更高质量的提交。

有效的政策明确了期望，例如：允许哪些类型的 AI、何时需要披露以及贡献者在提交之前应如何验证其工作。

Red Monk 的 Holterhoff 最近[汇编了关于开源社区中 AI 政策的研究](https://redmonk.com/kholterhoff/2026/02/26/generative-ai-policy-landscape-in-open-source/)，确定了基金会和项目之间 63 种正式方法。这包括来自 [Blender](https://devtalk.blender.org/t/ai-contributions-policy/44202)、[Fedora](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/)、[Firefox](https://blog.mozilla.org/en/mozilla/mozilla-open-source-ai-strategy/)、[Ghostty](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)、[Linux 内核](https://canartuc.medium.com/the-linux-kernel-said-no-to-your-ai-coding-assistant-930b87c30447)和 [WordPress](https://make.wordpress.org/ai/handbook/ai-guidelines/) 的努力，以及来自 Eclipse Foundation、[Linux Foundation](https://www.linuxfoundation.org/legal/generative-ai)、[Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects) 等的指导。

虽然方法各异，但组织倾向于在披露使用情况的前提下允许 AI 的使用。其他组织则将 AI 辅助的贡献仅限于已批准的问题。14 个项目彻底禁止 AI 贡献，而 12 个项目尚未决定。

数据还表明，越接近关键基础设施，标准就越严格。“你越深入技术栈，对 AI 的宽容度就越低，”Holterhoff 告诉 *The New Stack*。

然而，执行仍然是一个灰色地带。对 Holterhoff 来说，无论政策多么宽松，都应以社区规范为基础。每个项目也如此不同，这意味着 AI 政策将取决于具体情况。

因此，问题与其说是 AI 本身，不如说是它的使用方式和背后的意图。“只有当你无法理解它，或者只是随意抛出它时，它才成为劣质内容，”Holterhoff 说。

同样，对于 [Wundergraph](https://wundergraph.com/) 的首席解决方案工程师 [Ahmet Soormally](https://www.linkedin.com/in/ahmet-soormally) 来说，重点应该放在加强善意的贡献上。

Soormally 告诉 *The New Stack*：“这与 AI 是否帮助你编写 PR 无关。”“关键在于你交给下一个人或模型的是什么。如果它臃肿、不清晰或难以理解，你不是在帮忙；你只是在增加噪音。”

另一个选择是使用 GitHub 自己的工具来应对其所谓的开源“[永恒的九月](https://github.blog/open-source/maintainers/welcome-to-the-eternal-september-of-open-source-heres-what-we-plan-to-do-for-maintainers/)”。维护者可以限制 PRs 仅限协作人员，完全禁用它们，或引入基于标准的门控。

一些人正在构建定制防御措施。一位开发者创建了一个 [Anti-Slop GitHub Action](https://github.com/peakoss/anti-slop) 来自动过滤可疑的 PR。

Agentic AI Foundation 开发者体验副总裁 Angie Jones [在她个人博客](https://angiejones.tech/stop-closing-the-door-fix-the-house/)中建议使用 [Agents.MD](http://agens.md) 文件，部署 AI 来审核 AI 提交，进行良好测试，并自动化检测低质量 PR。

然而，对某些人来说，这些措施还不够。正如 Flux CD 维护者 Stefan Prodan [在 LinkedIn 上指出](https://www.linkedin.com/posts/stefanprodan_updated-ai-usage-policy-for-contributions-activity-7420221057237860352-OuhJ/)的，鉴于 GitHub 在 AI 辅助编码方面的投资，它本身缺乏明确的动力来遏制 AI 劣质内容。

开发者 Yuri Sizov [在 BlueSky 上发帖](https://bsky.app/profile/yurisizov.bsky.social/post/3mexrz5b5i22x)补充道：“这个平台鼓励这种行为，”并称“它本身就吸引了更多‘打酱油’的开发者提交低质量贡献。”

因此，一些项目正在探索替代托管平台。例如，Linux 发行版 Gentoo 正在从 [GitHub 迁移到 Codeberg](https://www.theregister.com/2026/02/17/gentoo_dumps_github_for_codeberg_over_copilot_nagware/)。

## 贡献者声誉系统

另一种在开源中维护质量和信任的方法是引入声誉系统。

一个例子是 [vouch](https://github.com/mitchellh/vouch)，一个由 HashiCorp 创始人 Mitchell Hashimoto 设计的信任管理系统。[Ghostty 项目](https://github.com/ghostty-org/ghostty)目前正在试验它。

正如 Hashimoto 在 vouch 的 README 中所写，AI 工具使得“轻易创建看似合理但质量极低的贡献”变得容易。Vouch 通过要求贡献者在与项目互动之前获得受信任方的担保来解决这个问题。

另一个项目 [good-egg](https://github.com/2ndSetAI/good-egg) 根据 GitHub 贡献者的贡献历史为其分配分数，这可用于验证声誉和真实性。

## 身份的加密证明

除了人工证明，一些人主张将 AI 生成的贡献与可验证的身份绑定。

对 Shambaugh 来说，AI 代理身份的问题超越了开源，延伸到整个互联网的信任。他告诉 *The New Stack*：“短暂的身份可以一键更改，可以无限复制，几乎无法追溯。”“我不认为我们已经准备好让一百万个这样的东西大规模地出现在互联网上。”

新兴方法旨在通过加密验证来解决这个问题。例如，[Treeship](https://www.treeship.dev/) 是一个开源项目，它使用基于区块链的技术来创建保护隐私的 AI 代理行动证明。

正如 Treeship 创始人 [Revaz Tsivtsivadze](https://www.linkedin.com/in/tsivtsivadze/) 告诉 *The New Stack* 的那样：“在采用 AI 代理时存在信任问题。它是一个黑匣子；没有人知道代理的决策、记忆或工具调用中包含了什么。”

他补充道：“你可能会遇到各种 AI 代理，比如恶意的、流氓的或不受信任的第三方。”“AI 代理的加密证明是信任 AI 代理作为经济行为者的关键。”

Tsivtsivadze 表示，代理行为的防篡改记录可用于开源项目，以跟踪代理身份、行为、时间戳和底层决策过程。

虽然 Treeship 等技术在代理商务中有更广泛的潜在应用，但他认为这种验证有助于通过确保代理与真实人类行为者相关联，从而减少开源中的 AI 劣质内容。

其他社区努力旨在提高整个开源的问责制标准。

一个例子是由 Wundergraph 牵头的 [Open Source AI Manifesto](https://www.human-oss.dev/)，它为生成式 AI 在开源中的使用设定了期望，强调所有权、责任和真实性。该[项目](https://github.com/OSSAIManifesto/manifesto)还提供了一个徽章，维护者可以用它来表示负责任的 AI 使用。

Wundergraph 的 Soormally 说：“AI 可以扩展代码生成，但不能扩展问责制。”“那一部分仍然属于我们。”

Croce 还指出了一个更根本的问题：许多开源项目仍然资金不足且人手短缺。[NumFOCUS](https://numfocus.org/) 和 [Open Source Endowment](https://endowment.dev/about/) (OSE) 等倡议旨在提供急需的支持。

Croce 补充道：“寻找为这些审查提供更多资源和能力的方法，无疑是一种权宜之计，也是开源软件未来绝对必需的。”

## 开源的未来取决于问责制

根据 2026 年的 [State of Open Source Report](https://www.openlogic.com/resources/state-of-open-source-report)，开源仍在快速发展，在欧盟的使用比在美国更明显。在日益增长的[数字主权](https://www.cio.com/article/4038164/why-cios-need-to-respond-to-digital-sovereignty-now.html)担忧中，避免厂商锁定现在是开源的首要驱动力。

毫无疑问，开源被广泛依赖——根据 [2024 年 Synopsis 报告](https://www.intel.com/content/www/us/en/developer/articles/guide/the-careful-consumption-of-open-source-software.html)，96% 的商业代码库包含开源。但“劣质内容末日”提出了一个棘手的挑战。

那么，对于开源维护者来说，问题是这一切是否值得。

Holterhoff 说：“如果你把生活变成地狱，他们就不会再做了。”“如果他们的劳动没有得到报酬，并且他们放弃了，那么开源社区就会蒙受损失。”

令人担忧的是，尽管维护者已经[敲响了警钟](https://leaddev.com/software-quality/open-source-has-a-big-ai-slop-problem)，但目前尚不清楚基金会或平台将如何响应以维持生态系统。

> “如果我们在 AI 驱动的世界中不积极管理贡献质量，我们不仅会面临安全问题或技术债务。我们正在将生态系统本身置于危险之中。”

“如果我们在 AI 驱动的世界中不积极管理贡献质量，我们不仅会面临安全问题或技术债务，”Croce 说。“我们正在将生态系统本身置于危险之中。”

目前，这归结为贡献者的问责制。“问责制是真正的标准，”Croce 补充道。“贡献者需要理解并支持他们提交的内容。”

如果没有单一的技术解决方案，或许呼吁人类“做正确的事”会有所帮助。因为如果没有基本的问责制和信任，开源模式本身就会开始崩溃。