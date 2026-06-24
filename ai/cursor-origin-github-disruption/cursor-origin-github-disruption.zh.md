**本周AI界传出的最大新闻**无疑是Elon Musk旗下的 [SpaceX 已同意收购](https://thenewstack.io/spacex-cursor-ai-coding/) AI 编程初创公司 [Cursor](https://cursor.com/)，这是一笔价值 600 亿美元的全股票交易。

但在同一天，在 Cursor 于旧金山举办的一场 [仅限受邀者参加的开发者大会](https://cursor.com/compile) 上，[Tomas Reimers](https://www.linkedin.com/in/tomasreimers/) 登台 [发布了](https://x.com/morganlinton/status/2066958434805956937) 一个对于开发者工具行业同样具有深远意义的新项目。

这个名为 [Origin](https://cursor.com/origin) 的项目，[是一个兼容 Git 的代码托管平台](https://x.com/cursor_ai/status/2067012220832329782?s=20)，专为 AI 代理（而非人类）承担大部分工作的世界而从头设计。

值得注意的是，Reimers 是 [Graphite](https://graphite.com/) 的联合创始人，这是一家代码审查初创公司，Cursor 在 [去年 12 月](https://tessl.io/blog/cursor-acquires-graphite-to-bridge-code-creation-and-review/) 透露对其进行了收购（该交易显然已于 1 月完成）。当时，一些评论员指出了这笔交易对 GitHub 的影响——其中就包括 Gergely Orosz。

《The Pragmatic Engineer》通讯作者、Graphite 投资者 Orosz 在 LinkedIn 上写道：“我告诉你们：GitHub 最大的竞争对手可能很快就是 Cursor。在我看来，Graphite 是目前市面上最好的 AI 代码审查 + 堆叠 diff + PR 工作流产品。GitHub 已经在追赶 Cursor/Graphite 了。”

简而言之，Graphite 已经构建了 GitHub 正在拼命复制的工作流工具——而在 Cursor 的资源支持下，两者之间的差距只会进一步拉大。现在，有了市值 2.5 万亿美元的 SpaceX 撑腰，事情可能会变得非常有意思。

## Origin 的起源故事

在 Origin 发布前夕，Reimers 在旧金山的舞台上指出，Graphite 的客户群（包括 Shopify、Snowflake、Notion 和 Figma）证明了 Origin 出现之前就已经存在一个亟待解决的问题。

> “当我们被 Cursor 收购后，我们加快了最雄心勃勃的项目——从零开始重构该工具。”

Reimers 说：“过去几年，我们注意到随着这些公司采用 AI 工具，它们所依赖的工具开始变得不可靠。这是因为过去几年 AI 工具彻底改变了我们的行业。它使每位开发者都能成为 10 到 100 倍效能的开发者，但这种变化需要从根本上不同的工具。这就是为什么当我们被 Cursor 收购后，我们加快了最雄心勃勃的项目——从零开始重构该工具。”

**在 SpaceX** 冲向公开市场、一夜之间成为全球最有价值公司之一，并为一家成立四年的初创公司豪掷 600 亿美元的喧嚣中，Origin 容易被忽视是可以理解的。但它试图解决的基础设施问题确实存在。

> Origin 容易被忽视是可以理解的。但它试图解决的基础设施问题确实存在。

**GitHub 作为全球遥遥领先的代码托管平台**，目前正处于艰难时期。正如 *The New Stack* [在 6 月报道的那样](https://thenewstack.io/github-wants-developers-back/)，该平台在过去 12 个月内记录了数百起事故，[难以跟上](https://www.theregister.com/software/2026/06/12/github-outages-persist-as-ai-coding-drives-traffic-surge/5255125) AI 代理生成的代码量。该公司表示，目前每月处理约 14 亿次提交（高于 2025 年全年的 10 亿次），仅代理每月就生成超过 1700 万个拉取请求（pull request）。

讽刺的是：GitHub 曾凭借 [2021 年 Copilot 的发布](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/) 开启了 AI 编程时代，如今却在它的重压下步履蹒跚。对于一些人来说，其日常使用习惯已经出现了裂痕。

[Brian Douglas](https://www.linkedin.com/in/brianldouglas/) 是 GitHub 的前开发者倡导总监，最近 [创办了自己的 AI 基础设施初创公司](https://thenewstack.io/paper-compute-agent-infrastructure/) [Paper Compute](https://papercompute.com/)，他告诉 *The New Stack*，这种转变已经开始。

> “代理正在迅速扼杀人们进行开源的意愿。”

“代理正在迅速扼杀人们进行开源的意愿，”Douglas 说。“我很想看看 GitHub 今天 [月活跃用户] 的数据是什么样，因为我相信有很多人选择在别处进行代码审查——或者专门与代理协作以完成最后一步——这正处于历史最高水平。”

Douglas 本人也身处其中，他说他现在大部分的审查和 PR 工作直接在 AI 编程工具中完成。

“作为 GitHub 的深度用户，我发现自己用它的频率降低了，更多地依赖 Claude 和 Codex 进行审查和 PR 交互，”他说。

## 后 GitHub 时代？

在秋季计划发布之前，Origin 仍处于候补名单模式。参与 Compile 的人员透露了足以勾勒其野心的细节。开发者倡导者兼独立评论员 [Shawn Wang Yuexian](https://www.linkedin.com/in/shawnswyxwang/)（即 swyx）[将其描述为](https://x.com/swyx/status/2066928345246470204) “期待已久的 Git 竞争对手，可针对代理工作负载进行扩展，可通过 API 和 MCP 进行扩展，并内置合并冲突和 CI 失败的代理解决方案。”

无论 Origin 发布时的样貌如何，显而易见的是，市场对替代现状的需求正在增长。自 2008 年 GitHub 普及拉取请求模型以来，软件开发世界发生了巨大变化——这一功能被 Douglas 称为其“有史以来最好的功能”。但拉取请求是为了一个人类有意识地编写和审查代码、一次一改的世界而设计的。那个世界正在迅速远去。

> “现在，项目的创建速度正在压垮 GitHub，而工程师们并没有在看代码。”

“现在，项目的创建速度正在压垮 GitHub，而工程师们并没有在看代码，”Douglas 说。“所以，如果目标是将其放入云端以便代理管理代码，我认为这绝对是一个颠覆的机会。”

因此，随着 AI 代理以人类审阅者无法企及的速度推送代码，拉取请求面临成为一种形式的风险——变成一个需要打钩的选项，而不是一个有意义的质量门禁。这引发了一个更深层次的问题：行业究竟应该如何衡量软件工作的价值？

对于 Douglas 来说，答案在于一个完全不同的单位。提交次数和代码行数——开发者产出的传统代理指标——在 AI 代理可以在几秒钟内生成数千行代码的世界里几乎没有意义。相比之下，Token 直接映射到计算成本，因此映射到产生的实际努力和价值。这种重构非常适合 Cursor。

> “Token 是比提交次数更好的指标。”

“Token 是比提交次数更好的指标，”Douglas 说。“它们对应于与工作努力相关的支出金额。以前，我们假装代码行数是指标，事实证明这是错误的。但 Token 加代理会话等于客户价值——而 Cursor 处于有利地位，可以占据协作堆栈更深层的一部分。”

然而，Cursor 并非唯一持有这一观点的公司，一系列旨在为代理时代重建基础设施的外围努力正在涌现。

在 6 月 10 日于伦敦举行的 [Transcend 大会](https://about.gitlab.com/events/transcend/london/) 上，GitLab [宣布](https://about.gitlab.com/press/releases/2026-06-10-gitlab-announces-new-capabilities-to-give-enterprises-speed-control-at-agentic-scale/) 了其所谓的 [下一代源代码管理 (Next Generation Source Code Management)](https://about.gitlab.com/blog/gitlab-transcend-announcements/) 的私人内测版本——内部称为 Project Switch。[由 GitLab 产品与营销首席官](https://www.youtube.com/watch?v=ekcw1yn21jQ) [Manav Khurana](https://www.linkedin.com/in/mkhurana/) 在台上发布，该新后端保留了 Git 协议，但完全重新设计了底层架构，允许代理在服务器端查询仓库，而不是完整克隆它们。

GitLab 表示，每个代理的任务执行速度最高可提升 50 倍，消耗的 Token 减少多达 3 倍。值得注意的是，Anthropic 是该项目的设计合作伙伴。

“世界上最受欢迎的 Git 平台正在重压下屈服，不仅是因为你的团队在克隆、分支和合并代码，还因为几十个，在某些情况下是数百个代理在同时工作，对这些系统造成了很大压力，”Khurana 说。

在 GitLab 的 Transcend 发布会后的第二天，Zed 联合创始人 [Nathan Sobo 公布了](https://zed.dev/blog/introducing-deltadb) [DeltaDB](https://zed.dev/deltadb) 的细节，这是该公司 [前一年秋天](https://zed.dev/blog/sequoia-backs-zed) 首次预告的一个项目。作为一个比 Origin 或 Project Switch 更激进的方案，DeltaDB 完全取代了 Git 基于提交的模型，取而代之的是一个持续的细粒度 Delta 流——代理执行的每一个操作，都直接链接到产生它的对话。Sobo 证实，测试版将在几周后发布。

与此同时，HashiCorp 联合创始人 Mitchell Hashimoto 预见到了这一点。去年 12 月，他在 X 上写道：“AI 公司正在成为 GitHub 的道路上，比 GitHub 成为一家 AI 公司的速度要快。”

本周 Origin 发布时，他 [转发了自己](https://x.com/mitchellh/status/2066950461790536156?s=46) 的言论，只写了一行字：“Cursor 今天发布了 Origin。更多产品将会出现。”

碰巧的是，Hashimoto [是另一家](https://x.com/mitchellh/status/2066957972992151687?s=20) 名为 East River Source Control ([ERSC](https://ersc.io/)) 的代理原生代码托管初创公司的投资者，该公司正在 [构建](https://ersc.io/blog/ersc-availability) 一个兼容 Git 的平台，旨在每秒处理数千次提交。

## 模型是护城河

对于 Douglas 来说，竞争对手从零开始重建版本控制的努力趋同并不令人惊讶。他指出，在过去一年里，开发者沙箱——编写和测试代码的环境——也出现了类似的动态，因为 [Docker](https://www.docker.com/blog/docker-sandboxes-a-new-approach-for-coding-agent-safety/)、[Cloudflare](https://blog.cloudflare.com/sandbox-ga/) 和 [Vercel](https://vercel.com/sandbox) 等公司进入了该领域，因为那是开发者花费时间的地方。

同样的引力现在正作用于版本控制。开发者的工作方式发生了根本性的变化——曾经他们直接在编辑器中编写代码，而现在许多人把时间花在指导代理替他们编写代码上。IDE 不再主要是一个打字的地方；它越来越成为一个观察、审查和引导的地方。

> “我认为故事中的所有参与者都有机会，我们需要重新思考我们的基础设施来为此做好准备。”

“现在，IDE 正因为开发者已经演变为使用基础模型编写代码而受到影响，他们需要将自己定位为你打开并观察代理编写代码的工具，”Douglas 说。“我认为故事中的所有参与者都有机会，我们需要重新思考我们的基础设施来为此做好准备。”

然而，所有这一切的基础是一个商业现实。Cursor 已经朝着这个位置建设了一段时间，它在 2025 年推出了 [自己的第一方编程模型](https://cursor.com/blog/composer) Composer，并 [在 5 月](https://thenewstack.io/cursor-composer-benchmarks/) [迭代了 Composer 2.5](https://thenewstack.io/cursor-composer-benchmarks/)，使其拥有更便宜的内部推理能力，而不是完全依赖昂贵的 Anthropic 和 OpenAI API 调用。Composer 2.5 在执行等效任务时的成本只是 Claude Opus 的一小部分——在输出 Token 上差异高达十倍。换句话说，拥有模型是使拥有堆栈其余部分变得可行的方法。

“很明显，你不能再仅仅插入一个 OpenAI Key 就期待在这个市场上获得超速增长或长期生存，”Douglas 说。“相反，你需要拥有模型才能获胜。”

SpaceX 的火力是会加速这一雄心壮志，还是使其复杂化，仍有待观察。但那些押注于下一个软件开发时代的公司，并没有等待 GitHub 追赶上来。