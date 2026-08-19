<!--
title: GitHub稳定性存疑，Cursor推出Origin抢占AI编程基础设施高地
cover: https://cdn.thenewstack.io/media/2026/08/6af2f836-puji-ningsih-iqe3s5nigxc-unsplash-scaled.jpg
summary: Cursor近日推出Origin代码托管平台，旨在适配AI代理高频提交的需求。恰逢GitHub全球大面积宕机，Origin的上线凸显了行业对支持AI原生开发、具备高扩展性代码版本管理工具的迫切需求。
-->

Cursor近日推出Origin代码托管平台，旨在适配AI代理高频提交的需求。恰逢GitHub全球大面积宕机，Origin的上线凸显了行业对支持AI原生开发、具备高扩展性代码版本管理工具的迫切需求。

> 译自：["If GitHub was stable, these alternatives would not be as interesting": Cursor launches Origin as GitHub goes dark](https://thenewstack.io/cursor-origin-github-alternative/)
> 
> 作者：Paul Sawers

Cursor正式涉足代码托管领域，推出了 [Origin](https://cursor.com/docs/origin)，这是一个为 AI 代理生成提交（commit）的时代而构建的 Git 兼容平台。

该 [Beta 版本发布](https://cursor.com/changelog/origin-code-hosting)公告于周一深夜发出，此前两个月，[Tomas Reimers](https://www.linkedin.com/in/tomasreimers/) 曾在 [Cursor 旧金山开发者大会](https://thenewstack.io/cursor-origin-github-disruption/) 上预告了这款以代理（agent）为核心的 GitHub 替代品。巧合的是，就在同一天，Elon Musk 的 SpaceX 证实已 [提出 600 亿美元的收购报价](https://thenewstack.io/spacex-cursor-ai-coding/) 以全资收购 Cursor。随着该交易于 [8 月 14 日正式完成](https://cursor.com/blog/joining-spacex)，Origin 成为了 Cursor 作为 SpaceX 全资子公司发布的首款产品。

值得注意的是，Origin 上线当天恰逢 [GitHub 全球范围内宕机](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-github-is-down-worldwide/)，这让原本可能只是常规的 Beta 版发布，成为了 Cursor 为什么要开发 Origin 的“典型案例”。尽管这 [8 小时服务中断](https://www.infoworld.com/article/4210864/github-restores-services-after-nearly-8-hour-outage-disrupts-actions-apis-prs-and-copilot.html) 表面上看似是“天时地利”的巧合，但对 Cursor 来说，GitHub 在此时下线并非好事，因为 Cursor 需要一个功能完备的 GitHub 来帮助新用户顺利上手。正如 SpaceXAI 的 [Matt Palmer](https://www.linkedin.com/in/matt-palmer/) 在 [X 上](https://x.com/mattyp/status/2089413216011165706) 所承认的那样：“我们原本打算早点发布，但 GitHub 宕机了。如果 GitHub 不可用，导入 GitHub 仓库作为入职的第一步并不是最优选择。”

然而，GitHub 的问题早于这次停机。正如 *The New Stack* [在 6 月报道的那样](https://thenewstack.io/github-wants-developers-back/)，过去 12 个月里该平台记录了数百起事故。随着提交量从每年 10 亿次跃升至每月 14 亿次，仅 AI 代理每月就生成超过 1700 万个拉取请求（Pull Request），这种增长导致 GitHub 出现了 MySQL 争用和 Webhook 过载等基础设施瓶颈。

> “Cursor 加入了一众科技公司的行列，致力于为代理全天候工作的世界重建版本控制系统。”

GitHub 首席运营官 Kyle Daigle 在当时接受 *The New Stack* 采访时讨论了扩展性问题：“这不仅仅是正常的扩展，”他说，“现在需要确保我们能够以 30 或 40 倍的年增长率进行扩展”，而不是过去设想的每年翻一番。

快进到今天，Cursor 加入了一众科技公司的行列，致力于为代理全天候工作的世界重建版本控制系统，这些代理查询和推送仓库的速度远超任何人类团队。

## 起源故事

Origin 标志着 Cursor 的野心有了相当大的扩张。到目前为止，其代理主要在其他地方托管的代码上运行；通过 Origin，Cursor 正在推动掌控更多的底层开发基础设施。

在发布之初，它从基础功能做起。用户可以直接在 Cursor 内创建和托管 Git 仓库，新的 Codebase 标签页将作为 Origin 仓库的所在地。

![Cursor Origin 让用户可以直接在 Cursor 内创建和托管 Git 仓库。](https://cdn.thenewstack.io/media/2026/08/8784192e-gifa.gif)

*Cursor Origin 让用户可以直接在 Cursor 内创建和托管 Git 仓库。*

这些仓库在 Cursor 之外依然像普通的 Git 仓库一样运行。开发者可以在本地克隆它们，添加 Origin 远程仓库，并从命令行推送代码——本质上使 Cursor 扮演了通常由 GitHub 等服务所占据的角色。

![将本地仓库推送到 Origin](https://cdn.thenewstack.io/media/2026/08/fd832952-gifb.gif)

*将本地仓库推送到 Origin*

Cursor 并没有要求非此即彼的迁移。现有的 GitHub 仓库可以同步到 Origin 中，并与 Cursor 托管的仓库一起展示，同时 GitHub 仍然是那些在此起步项目的“单一事实来源”。

![同步 GitHub](https://cdn.thenewstack.io/media/2026/08/6a652fdb-gif1.gif)

*同步 GitHub*

拉取请求功能也已内置，包括差异对比、评论、检查和合并。Cursor 的代理直接驻留在代码旁边：用户可以在浏览器中询问有关正在查看内容的疑问，让代理进行更改、更新 PR 或推送分支。

![审查代码 / 询问 Cursor / 合并](https://cdn.thenewstack.io/media/2026/08/d532747d-gif2.gif)

*审查代码 / 询问 Cursor / 合并*

这种组合可以说是 Origin 最重要的部分：仓库、拉取请求和编码代理现在都生活在同一个产品中——这使 Cursor 对代码存储、审查和更改的环境拥有了更多的控制权。

[Coder](https://coder.com/)（一家为企业构建的云开发平台）的首席执行官 [Rob Whiteley](https://www.linkedin.com/in/rwhiteley/) 认为 Origin 是一个“聪明的玩法”——他认为行业大部分精力都投入到了编写代码的工具上，而对于代码产生后的处理却投入甚少。

“GitHub 在代理代码开发的重压下开始出现裂痕，需要一个代理原生的源代码锻造平台，”Whiteley 对 *The New Stack* 表示。“每个人都在集成‘编写代码’的技术栈，从编辑器、聊天到代理、工具和大模型。没有其他人真正集成‘管理代码’的技术栈，即代码存储、版本控制、审查和合并的地方。”

目前，Origin 仅限于 Cursor 的 Pro、Teams 和企业版计划——似乎免费层级暂不提供——而且发布本身是分阶段进行的，因此并非每个人都能立即使用。

## Origin 与 GitHub 有何不同？

目前，不可否认的事实是，它与值得信赖的旧 GitHub 并没有太大区别，这一点 [网络社区也看出来了](https://news.ycombinator.com/item?id=49334209)。Origin 团队对此也毫不避讳。

Origin 的工程师 Tomas Reimers（他是代码审查初创公司 Graphite 的联合创始人，Cursor 在 [2026 年初收购了该公司](https://cursor.com/blog/graphite)）在发布后直接在 Hacker News 上回答了开发者的问题。

> “我们特意将其发布为 GitHub 的替代品，在功能上与他们正面交锋。”

当 [被问及](https://news.ycombinator.com/item?id=49338041) 除了正常运行时间之外，Origin 与 GitHub 有什么区别时，Reimers 说实话承认“非常少”。“我们特意将其发布为 GitHub 的替代品，在功能上与他们正面交锋，”他 [写道](https://news.ycombinator.com/item?id=49338196)。

但他确实指出，更多的功能正在路上：Reimers 解释说，在接下来的几周内，Origin 将开始提供更深入的代理集成，这些工具能够理解代理编写的代码，以及自动将拉取请求推向可合并状态的自动化程序。

“期待我们带来更多功能，”他继续说道。“我们希望发布一个 Beta 版，以便人们可以自己开始尝试我们的可扩展性和可扩展性。在接下来的几周内，您可以期待一系列功能开始改变源代码管理，以便更好地理解和配合代理工作。”

在线社区中的几个人也强调了 Origin 发布的时间点。《实用工程师》（*The Pragmatic Engineer*）通讯作者兼 Graphite 投资者 [Gergely Orosz](https://www.linkedin.com/in/gergelyorosz/) 最初 [在 X 上发文](https://x.com/GergelyOrosz/status/2089397495939891698?s=20) 抱怨 GitHub 尽管拥有大量工程师，但性能问题持续不断。

然而，不到一小时后，Orosz [回来](https://x.com/GergelyOrosz/status/2089414076900233647?s=20) 评论了 Origin。“Cursor 的托管代码服务发布公告的时机也不可能再好了，”他写道。“如果 GitHub 稳定的话，这些替代品就不会这么有趣/流行了！”

正如 Orosz 所言，“这些替代品”已经 [在 GitHub 的阴影下排起了长队](https://thenewstack.io/cursor-origin-github-disruption/)。

## “GitHub 替代品”的激增

与 Origin 最直接的比较或许是 [Entire](https://entire.io/)，这是一个由 [Thomas Dohmke](https://thenewstack.io/thomas-dohmke-interview-entire/) 创立的分布式 Git 网络。Dohmke 于 [去年 8 月](https://thenewstack.io/github-loses-its-ceo-and-independence/) 卸任了 GitHub 的 CEO。本质上，Entire [在区域节点之间镜像仓库](https://thenewstack.io/entire-git-for-agents/)，目前 GitHub 仍然是单一事实来源——尽管一旦团队开始在该平台上原生创建仓库，这种情况可能会改变。该公司 [在 2 月份筹集了 6000 万美元的种子轮融资](https://thenewstack.io/thomas-dohmke-interview-entire/)，投资者包括微软的风险投资部门，并于 [7 月正式进入市场](https://thenewstack.io/entire-git-for-agents/)。

> “Cursor 的托管代码服务发布公告的时机也不可能再好了。如果 GitHub 稳定的话，这些替代品就不会这么有趣/流行了！”

与此同时，GitLab 也在为代理重度的世界重新思考源代码管理，[在 6 月宣布了](https://about.gitlab.com/press/releases/2026-06-10-gitlab-announces-new-capabilities-to-give-enterprises-speed-control-at-agentic-scale/)“下一代源代码管理”的私有 Beta 版，内部代号为 Project Switch。该系统不再让代理克隆整个仓库来读取或更改少量文件，而是让它们向服务器查询任务确切需要的内容，每个代理的可见性都被限制在最低要求范围内。

此外，代码编辑器初创公司 [Zed](https://zed.dev/) [自去年以来](https://zed.dev/blog/sequoia-backs-zed) [也一直在预告](https://zed.dev/blog/introducing-deltadb) 一种新的版本控制方法，并在 8 月初正式推出了 [Delta](https://zed.dev/blog/introducing-delta)，这正如该公司所言，是一个“用于与代理一起编码和审查它们所构建内容的多人协作环境”。

“Delta 保持了代码和对话的连接，因此开发者和代理可以在完全了解代码产生背景的情况下协同工作，”Zed 联合创始人兼 CEO Nathan Sobo 在 Beta 版发布时写道。

在底层，Delta 运行在 [DeltaDB](https://zed.dev/deltadb) 上，它保持了对话和正在进行的工作的实时副本在团队中同步。它与项目现有的 Git 仓库并存，并支持包括 Claude Code 在内的代理工具。在实际效果上，这带来的改变是：当代理不断编辑时，评论会保持在它们所引用的代码上。

尽管 GitHub 存在持续的可靠性问题，但 Whiteley 认为 Cursor 的版本短期内不会成为大型企业的主流选择，这主要是因为切换的成本太高。

“大多数 [企业] 已经花了很多精力、金钱在 GitHub 上进行了标准化，再次迁移意味着今天付出巨大代价却只能获得有限的投资回报率，”他说。“随着‘氛围编程’生成比现在多一个数量级的代码，这种情况可能会改变。如果 Cursor 承诺保持 Origin 的开放性，足以让企业信任并进行集成，那么随着时间的推移，它可能会变得更有吸引力。”

因此，虽然在“GitHub 替代品”领域有着明显的活动热潮，但现在断言其中任何一个是否能长期生存还为时尚早。GitHub 拥有 18 年的先发优势：它于 2008 年推出，普及了大多数这些新进入者试图颠覆的拉取请求审查模型，并于 2018 年被微软收购。它还通过 2021 年推出 Copilot 引发了当前的 AI 编码工具浪潮——正是这一浪潮现在正在产生其自身基础设施难以吸收的数据量。

目前，GitHub 仍然是这些平台中唯一真正能够大规模处理这种开发者活动的平台。然而，作为世界上最有价值的公司之一，SpaceX 拥有 2 万亿美元的超高估值，这使得 Cursor 在投资方面处于有利地位——不仅是在 [其自身的 AI 模型上](https://thenewstack.io/cursors-composer-2-beats-opus/)，而且在其底层的基础设施上。