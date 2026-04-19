<!--
title: 谷歌与 OpenAI 围攻 Claude 桌面护城河：Anthropic 正在亲手送掉优势
cover: https://cdn.thenewstack.io/media/2026/04/9b9d2e0e-beatriz-camaleao-tt7rrkvvcr4-unsplash-scaled.jpg
summary: 谷歌与 OpenAI 纷纷推出原生桌面应用和“超级应用”，直接挑战 Claude 在桌面端的领先地位。与此同时，Anthropic 因模型争议、宕机及身份验证风波而陷入困境。
-->

谷歌与 OpenAI 纷纷推出原生桌面应用和“超级应用”，直接挑战 Claude 在桌面端的领先地位。与此同时，Anthropic 因模型争议、宕机及身份验证风波而陷入困境。

> 译自：[Google and OpenAI are making a run at Claude's desktop moat, and Anthropic is making it easy](https://thenewstack.io/google-and-openai-are-making-a-run-at-claudes-desktop-moat-and-anthropic-is-making-it-easy/)
> 
> 作者：Matthew Burns

*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 进展，解释它们对于将这项技术投入工作的个人和组织的意义。核心论点很简单：学会使用 AI 的员工将定义其行业的下一个时代，而这份通讯旨在帮助你成为其中一员。*

---

两年来，Anthropic 占据了桌面 AI 领域的主导地位。Claude 已成为高级用户整天开启的产品。本周，Google 和 OpenAI 都发布了极具竞争力的桌面替代方案——来自 Google 的原生 Mac 应用，以及来自 OpenAI 的整合超级应用——而 Anthropic 似乎正让高级用户更容易去考虑这些替代方案。

看看 Anthropic 本周的失误：新的 Opus 4.7 模型早期评价褒贬不一；Claude Code 的重新设计使得 Token 消耗量相对于现有额度成倍增加；又一轮的宕机；以及针对部分用户出人意料的身份验证方案。照这个速度，Google 和 OpenAI 只需要跟上节奏，让 Anthropic 继续令用户失望即可。

## Google 开始重视桌面端

周二，Sundar Pichai [宣布推出 Mac 版 Gemini](https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-mac-os/)，这是一个由小团队在 100 天内使用 Google 的 Antigravity 编码智能体构建的原生 Swift 应用。可以在任何地方通过 Option + Space 唤起，支持屏幕共享和本地文件访问。它的工作方式与 Claude Desktop 和 ChatGPT 的 Mac 应用类似。这只是 1.0 版本，目前还没有太多网页版无法实现的功能。但 Pichai 在他的[发布帖子](https://x.com/sundarpichai/status/2044452464724967550)中提到，团队在“不到 100 天内构建了 100 多个功能”。这是我反复思索的细节。Google 终于以 Anthropic 和 OpenAI 所设定的节奏发布消费级 AI 了。三年来，Google 的问题不在于模型，而在于模型被困在网页界面之后，而其他公司都在发布强大的桌面应用。这种情况正在开始改变。

同周，Google 推出了 [Chrome 中的 Skills 功能](https://thenewstack.io/gemini-chrome-saved-prompts/)——可在选定标签页运行的可重用一键式 Gemini 提示词——并将 [AI 模式引入 Chrome 地址栏](https://blog.google/products-and-platforms/products/search/ai-mode-chrome/)，将其最强大的 AI 搜索直接置于 URL 栏中。Chrome 正悄然成为一个 AI 产品，而不仅仅是一个附带 AI 的浏览器。Google 还[将 Gemini 的个人智能连接到 Google Photos](https://9to5google.com/2026/04/16/gemini-photos-personal-intelligence)，允许 AI 使用你的实际照片库生成个性化图像，无需手动上传，该功能首先向美国的付费订阅者推出。

将这一切堆叠在 Gmail、Docs、Sheets、Drive 和 Meet 之上（在 Workspace Business Standard 及以上版本中已包含 Gemini），Google 正在提出一种捆绑 AI 的策略，这对于数百万已经为 Workspace 付费的组织来说变得越来越难以忽视。Anthropic 没有浏览器。Anthropic 没有电子邮件客户端。Google 两者兼有，现在还有一个 Mac 应用。这就是 Anthropic 通过占据最佳桌面体验而悄悄侵蚀的护城河。Google 刚刚开始把它填回去。

*The Information* 还报道称，Google 和五角大楼[正在商讨一项机密 AI 协议](https://www.theinformation.com/articles/google-pentagon-discuss-classified-ai-deal-company-rebuilds-military-ties)，重建该公司在 2018 年 Project Maven 期间放弃的军事联系。Google 已经与总务管理局（GSA）达成了一项全政府范围的 Gemini 协议，所以这并非白手起家。

## OpenAI 正在为同样的战斗进行整合

Google 不是唯一发力的公司。OpenAI 的超级应用[在本月初具规模](https://thenewstack.io/openais-superapp-takes-shape/)，将 ChatGPT、Codex 和 Atlas 浏览器合并为一个单一的桌面应用程序。应用首席执行官 Fidji Simo 在一份内部备忘录中表示，OpenAI 此前“将精力分散在过多的应用和平台上”，并且“这种碎片化一直阻碍着我们的进步”。所以他们停止了碎片化。

我一直在使用它。Codex 智能体在隔离的 git 工作树中异步运行——多个智能体在同一个仓库上，没有合并冲突——你可以直接在 VS Code 中查看差异（diff）并打开输出结果。ChatGPT 5.5 于 4 月 6 日与其一同发布，改进了记忆管理，因此长时间的会话不会让你觉得每隔几轮就要重新开始对话。实际的区别在于你不再需要在应用之间切换。聊天、编码和浏览共存在一个窗口中，且上下文可以跨应用传递。这就是让它整天留在你桌面上的原因。

超级应用的存在部分是因为 OpenAI 的单个产品落后了——Codex 在开发者竞争中输给了 Claude Code，Atlas 未能撼动 Chrome。Simo 的备忘录基本上承认了这一点。但即使是拥有市场上最大消费级 AI 用户群的 OpenAI，也认定桌面应用是首先需要修复的产品。这说明了 AI 公司关注的重点，尤其是考虑到 Google 也有类似的举动。

## Anthropic 发布了其最佳模型，也经历了最糟糕的一周

让我们从新模型开始。[Opus 4.7 纸面参数看起来很强](https://thenewstack.io/claude-opus-47-launch/)：在 93 项任务编码基准测试中提升了 13%，文档推理错误减少了 21%，在工程评估中的生产任务解决能力提升了 3 倍，价格仍为每百万 Token 5 美元/25 美元。但早期的用户反应褒贬不一。在 [Hacker News](https://news.ycombinator.com/item?id=47793411) 和 Reddit 的 r/ClaudeAI 社区，用户和开发者表示 Opus 4.7 的适应性思维（现在是唯一支持的推理模式）经常在应该思考时选择不思考，迫使他们必须手动设置 `/effort xhigh` 才能恢复基准性能。有人报告称 API 参数正在[返回错误](https://medium.com/vibe-coding/opus-4-7-is-the-worst-release-anthropic-has-ever-shipped-12772c21ca1e)，在新分词器下 Token 成本显著增加，且思考 Token 默认被隐藏。还有人反映该模型在长上下文下的表现变差了，而非变好。尽管 Anthropic 迅速指出基准测试数据有所上升，但对于一部分发声用户来说，早期体验似乎正走向崩盘。Anthropic 可能会解决这些问题（模型发布后的第一周通常会趋于稳定），但当 Google 和 OpenAI 终于赶上 Anthropic 的节奏时，这个时机非常尴尬。

然后是产品问题。Claude.ai、API 和 Claude Code 在周三上午宕机——发生了 40 分钟的主要故障和 73 分钟的部分故障——这是自 2026 年初以来 Claude 多次出现的模式中的最新一次。Opus 4.6 在次日晚上再次宕机。Anthropic [发布了重新设计的 Claude Code 桌面版](https://thenewstack.io/claude-code-desktop-redesign/)，围绕并行会话展开，早期用户报告体验糟糕，多位用户反映在几分钟内就耗尽了 5 小时的额度，这可能是因为四个各占 100K Token 的并行会话累积速度极快。Anthropic 最近关闭了 OpenClaw 和其他第三方工具的订阅访问权限，撤销了 OAuth。此外，*The New Stack* [报道了 Anthropic 的新身份验证要求](https://thenewstack.io/anthropic-claude-identity-verification)，该要求引导部分用户通过 Persona（金融服务使用的 KYC 供应商）提交政府身份证件和自拍，然后才能访问某些功能。Anthropic 表示触发条件很窄，且数据保存在 Persona 而非 Anthropic。*Decrypt* 在[点击此处](https://decrypt.co/364509/claude-anthropic-government-id-kyc-privacy)直言不讳地写道：“你因为担心被监视而转用 Claude。现在它想要你的护照。”

我们的网站还报道了 [Claude Code Routines](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/)，这是新的持久化智能体，可在 Anthropic 的云端彻夜运行，由计划任务、API 调用或 GitHub webhook 触发。Routines 是一个实打实的产品，也是那种能留住开发者的能力。

很难不将所有这些与算力限制联系起来。*Fortune* [报道称 Anthropic 悄悄降低了](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/) Claude 的默认努力程度以节省 Token，且 OpenAI 的营收负责人称 Anthropic 有限的数据中心交易是一个“战略误判”。无论这种说法是否公平，模式是可见的：降低的努力程度、高峰时段更紧缩的配额、切断第三方访问、增加 KYC 摩擦，以及一个在推理方式上存在多项省钱折中投诉的模型发布。

我还没有放弃 Claude。对我来说，它在许多日常任务中仍保持着最佳用户体验，我相信我不是一个人。但本周，甚至连模型发布——这个 Anthropic 历来都能做对的事情——都带来了失望，并让我开始考虑新的替代方案。