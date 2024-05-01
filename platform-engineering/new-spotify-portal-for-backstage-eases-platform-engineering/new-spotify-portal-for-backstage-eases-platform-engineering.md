
<!--
title: Spotify Portal for Backstage 简化平台工程
cover: https://cdn.thenewstack.io/media/2024/04/1f03f273-pia-nilsson-spotify-backstage.jpeg
-->

创建 Backstage 的路径涉及尊重 Spotify 的协作文化和开发人员自主权。其新门户旨在将这种精神带给所有 Backstage 用户。

> 译自 [New Spotify Portal for Backstage Eases Platform Engineering](https://thenewstack.io/new-spotify-portal-for-backstage-eases-platform-engineering/)，作者 Jennifer Riggins。

伦敦 — 当 [Pia Nilsson](https://www.linkedin.com/in/pia-nilsson-02b47b1/) 于 2016 年来到音频流媒体公司 [Spotify](https://thenewstack.io/how-spotify-achieved-a-voluntary-99-internal-platform-adoption-rate/) 时，她惊叹于自己所见 — 但并非以一种好的方式。

“我发现这是一家非常友好、协作、透明、充满激情的公司。但它太混乱了。基础设施非常混乱。我从未觉得自己在工作中几乎毫无用处，”现任 [Spotify](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/) 工程高级总监兼 [Backstage](https://backstage.io/) 总经理的 Nilsson 告诉 The New Stack。

“没有办法找出问题所在。我不得不重新成为一名工程师，通过生态系统倒推回去才能理解它，”她说，因为 Spotify 虽然已经成立十年，但仍然像一家初创公司一样运作。

每个小队都有自己的背景，没有集中的文档和标准。“学习曲线太深了，”她说。“你一次又一次地学习，因为它以如此不同的方式实现。”

她并不孤单。那时，[开发人员入职平均需要 110 天](https://thenewstack.io/how-spotlify-adopted-platform-engineering-culture/)。如果 Spotify 有这个问题，那么规模较小的公司该如何管理？

该公司解决了其问题，其解决方案 Backstage 是一个用于构建开发人员门户的开源平台，它正在帮助其他组织也解决类似的问题。

今天，[Spotify 今天推出了一个新的内部开发人员门户](https://info.backstage.spotify.com/roadmap)，即 Backstage 的 Spotify 门户，作为基于 Backstage 构建的一个功能齐全、低代码到无代码的门户，进入私人测试阶段。

## 问题：中断太多

Nilsson 花了几十年时间作为一名工程师探索工程文化以及它如何构建大规模基础设施。试图回答：我们如何实际快速交付高质量代码？

这正是促使她加入 Spotify 的“奇妙的自主文化”的原因。但是，随着音频流媒体平台的扩展，开发速度大幅下降。其每季度开发人员调查显示，并不是技术减慢了他们的速度。

人们找不到东西。而且他们一直被打断，因为协作文化包含了轻拍肩膀、开发人员自主权、激进的透明度和内部采购。

“我们如何在不告诉 Spotify 的所有这些人该做什么的情况下帮助他们？因为我们讨厌那样，”Nilsson 说。“我们需要保持协作精神，他们需要与同事交谈。”

[Backstage 软件目录和开发人员平台](https://thenewstack.io/spotifys-backstage-a-strategic-guide/) 成为 Nilsson 和她的同事的答案。继续阅读，独家了解用于构建开发人员门户的最流行的开源框架如何不仅解决了 Spotify 的社会技术问题，而且还外包以解决数千个其他团队的问题。

## 保持自主权，但减少上下文切换

Spotify 的工程文化以其对 [开发人员快乐](https://thenewstack.io/measure-developer-joy-not-developer-productivity-atlassian-says/) 和自主权的关注而闻名。早在 2016 年，[平台团队](https://thenewstack.io/platform-engineering/) 就开始寻找有关是什么让某些团队比其他团队更快乐的模式。

平台团队发现，后端开发人员明显更快乐一些，因为有人创建了一个跨所有后端组件的共享目录。与此同时，机器学习工程师、Web 开发人员和负责播放列表、用户和版税等的功能团队，每个人都有自己的平台或网页门户。

每个工程组都有自己的服务需要担心，有些有 [文档](https://thenewstack.io/an-engineers-best-tips-for-writing-documentation-devs-love/)，有些没有。这导致了良好的工程文化，但在大约 400 个 Spotify 小队中造成了很多上下文切换。

“我们希望整合所有这些。这不仅仅是一个技术问题 — 尽管它是一个技术问题 — 它在很大程度上是心理上的，”Nilsson 说。“你需要帮助人们完全拥有他们实际工作的权利。”

因此，平台团队在 2017 年开始创建后来成为 Backstage 的东西。

## Backstage 的“第一批组成部分”

Nilsson 的团队选择数据团队作为其“第一批组成部分”，让他们加入 Backstage。她说，这涉及“解决人们不想失去授权的问题”。“那是他们的工作。他们实际上是数据专家，”她说。

直到今天，Spotify 数据团队仍然维护着自己的 Backstage 主页，以及其庞大的数据生态系统。

Backstage 的秘诀——她开玩笑说这不是秘密，因为它开源了——是它的可扩展性。

“在这个示例中，我们允许数据人员编写一个小型 Backstage 插件，并通过 [GitLab](https://about.gitlab.com/?utm_content=inline+mention) 的一项名为 [代码所有者](https://docs.gitlab.com/ee/user/project/codeowners/) 的功能来维护其所有权。”她表示，Backstage 本质上是一个主页，由一个 [单一存储库](https://thenewstack.io/monorepos-hal-9000-approved-code-management-and-collaboration/) 组成，每个团队“可以完全维护他们负责的内容的所有权”。

这也是一个战略决策，因为一开始，Backstage 团队只有七个人。

“这样做的好处是分散决策。决策应由了解问题的人做出，”Nilsson 说。“我拥有的这个小团队了解可发现性的问题，以及我们如何帮助人们找到他们需要的内容，而向 Backstage 贡献插件的人员则完全拥有这些插件的所有权。”

## Backstage 大规模采用的秘诀

在两年内，Backstage 已在 Spotify 中实现大规模采用——100% 自愿。

“我经常与许多采用者交谈，他们认为需要聘请这个庞大的 Backstage 团队，因为他们认为 Backstage 是一个整体，”Nilsson 说。“但随后他们错失了心理方面”，因为没有一个团队愿意放弃自己的职责。

她补充说：“我总是建议每个人保持精简，因为这样你就可以做所有这些你不应该做的事情。相反，你需要帮助他们打造他们将拥有并引以为豪的 Backstage 插件。”

与 Spotify 文化的所有事物一样，它展示和分享，而不是讲述。Nilsson的团队组织了许多社区会议，邀请来自各个职能和领域的员工来演示他们的 Backstage 插件，展示他们的领域知识和他们能够更快交付的功能。

现在 Spotify 的 Backstage 拥有 200 多个内部 Backstage 插件，以实现更大的可扩展性。

Nilsson指出，一种常见的工程模式是解决业务问题。一旦解决，你才会构建抽象层或用户界面。对于 Spotify 来说，从每个小队解决自己的问题开始。然后，Backstage 使团队能够在顶部构建用户界面 (UI) 并将其列在一个共享 UI 组件库中，进而实现可重用性。

## 更好的保留率，更快的软件开发

借助 Backstage，Spotify 的开发人员活动、软件开发生命周期和开发人员保留率都有了显着提高。开发人员入职时间从 110 天缩短到 20 天。而 Backstage 频繁用户——使用该门户网站频率高于另一半员工的那一半员工——更有可能在 Spotify 停留更长时间。

![频繁使用 Backstage 的用户在 GitHub 中活跃度高出 2.3 倍，在减少 17% 的周期时间内创建的代码更改是其两倍，部署软件的频率是其两倍，其软件部署时间是其三倍，并且他们更有可能在一年后仍在 Spotify。](https://cdn.thenewstack.io/media/2024/04/d845cccc-backstage-roi-1024x321.jpeg)

*Spotify 关于频繁使用 Backstage 的开发人员的数据表明，这些门户网站有助于提高他们的工作效率，并更有可能留在组织中。*

“我相信，至少对我自己而言，如果我像这样被启用，我会更快乐，”Nilsson说。她引用了 Spotify 的口号：快乐的开发人员，快乐的代码。“如果工作是一种乐趣，你不会离开。”

Spotify 看到 Backstage 和 [开发人员快乐](https://thenewstack.io/how-intercom-ships-industry-leading-developer-experience/) 之间存在可衡量的联系。

她继续说道：“如果我们保持这种非常协作、透明、信任的环境，信任人们自己的判断和专业知识，如果我们拥有这种文化，那么 Backstage 肯定はその核心部分。”

但是，你如何 [衡量开发人员体验](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/) 和文化？

作为最大的 [Google Cloud Platform](https://cloud.withgoogle.com?utm_content=inline+mention) 客户之一，Spotify 与 Google 建立了长期的合作关系，建立在相似的工程文化之上，包括定期进行 [开发人员调查](https://thenewstack.io/github-developer-productivity-at-30-billion-messages-per-day/)。

## “我们始终将自己视为第一个客户”

十多年来，Nilsson的团队一直进行每季度的工程满意度调查，工程人员分为三部分，以获得更持续的每月反馈。这些定性数据与所有 Spotify 平台产品（包括 [Backstage Insights 插件](https://backstage.spotify.com/marketplace/spotify/plugin/insights/)）中的定量数据相结合。

“我们一直视自己为头等消费者，”Nilsson 说道，并增加了更多开发人员经验数据到反馈组合中。“

吃自己的狗粮是创造人们想要使用的工具的方式，”她说，这是平台组织的另一项核心准则。

Nilsson表示，Spotify 肯定是最早的平台工程团队之一，早在 2016 年就开始招募产品人员，“这是维护面向人类问题的技术问题解决方法的一种方式”。

她认为，让产品经理、设计师和产品所有者与工程师合作，可以帮助以社会技术的方式定义平台战略。

Spotify 还举办年度[黑客周](https://newsroom.spotify.com/2023-03-16/tips-for-creating-a-successful-hack-week/)，公司期望从人力资源到敏捷教练的每位员工都能黑进自己的工作，无论是关于人、流程还是技术，或是这些因素的组合。Backstage 产品的受益来自于工程师们对自己的开发体验进行黑进。

Spotify 也习惯于同事在其他团队进行嵌入式工作，以培养移情心智和成长心态。对于平台团队而言，由于他们的同事是他们的客户，让[平台工程师嵌入应用团队可以亲身了解开发难题](https://thenewstack.io/how-platform-teams-can-align-stakeholders/) — 避免只构建他们认为最好的内容的坏习惯。“

最近，我们让一位工程师去从事台式机应用程序的工作。他在平台组织的 CI 团队中深入工作，所以与实际的 Spotify 应用程序相去甚远，”Nilsson 说。“当他回来的时候，他带回了这么多见解，他把这些见解带回了平台组织。”

## 创建一个行业标准

平台工程在过去 18 个月里兴起的原因之一是科技行业裁员，导致大多数团队用更少的资源做更多的事情。“Backstage 从来不是为了裁员，”Nilsson 说。“恰恰相反。这是为了帮助入职人员以及我们已经拥有的团队，我们希望加快速度。”

但尽管它最初是作为内部产品构建的，但 Spotify 有一种精神，即为了创建行业标准——例如围绕内部开发人员门户和目录——[你应该开源它](https://github.com/spotify)。

Backstage 既是商业产品，也是开源工具，开源框架拥有 3,000 多家公司采用者和 2,200 多位贡献者。每个人都欢迎作为贡献者加入这个开放生态系统，其中包括 150 个外部 Backstage 插件，包括 [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention) 和 Travis CI。

“然后我们出售一些我们认为可以提供巨大价值的企业产品。而且多年来，我们已经从内部进行了扩展和实战检验，”她说，其中包括 Backstage 实验平台，该平台在 Spotify 应用团队内部使用十年后公开发布。

## 推出“Backstage in a Box”

无论是免费增值还是高级版，Backstage 都可能继续主导平台工程领域，Forrester 预测，到今年年底，一半寻求 [平台主导软件开发方法的公司将采用 Backstage](https://www.forrester.com/what-it-means/ep352-tech-trends-2024/)。

今天推出的 Spotify Portal for Backstage 是其继续主导市场的计划的最新一步。

“我们从 2020 年以来听到的是‘我们喜欢 Backstage，每个人都想使用它’，但并不是每个人都有 [TypeScript](https://thenewstack.io/typescript/) 开发人员，而且从没有 [内部开发人员门户] 和没有完成我们所做的所有工作（例如了解复杂性，然后意识到我们的解决方案是什么）开始的复杂性——多年来没有完成这项准备工作，使得 Backstage 变得非常困难，”Nilsson说。

“总会有客户问：你能帮我简化一下吗？”

Spotify Portal for Backstage 在设计上是自以为是的，它具有一个设置向导和一个目录向导，承诺帮助团队在不到五分钟的时间内开始工作。它还附带了一个软件目录和软件模板，以帮助公司为后端服务、网站等制定黄金路径，使开发人员能够在几秒钟内启动新项目。

这个新门户还包括流行的 Backstage 插件 [Soundcheck](https://backstage.spotify.com/marketplace/spotify/plugin/soundcheck/)、[TechDocs 文档](https://backstage.io/docs/features/techdocs/)、[搜索](https://backstage.io/docs/features/search/getting-started/) 和一个新的配置管理器。

此外，Spotify 今天宣布了两项企业咨询和支持服务。

Nilsson说，Spotify Portal for Backstage，“吸引了渴望与我们合作以构建有史以来最好的 Backstage 体验的客户”。
