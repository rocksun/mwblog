*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 进展，并解释它们对使用这项技术的人员和组织意味着什么。核心论点很简单：学习使用 AI 的员工将定义他们行业的下一个时代，而本简讯旨在帮助你成为其中一员。*

---

上周我曾提到[AI 前沿技术正在将](https://thenewstack.io/openai-spacexai-meta-price-war/)智能价格降至一美元。本周，Elon Musk 将技术栈的其中一部分降至了零。

周三，SpaceXAI 在 Apache 2.0 许可证下[开源了其终端编程代理 Grok Build](https://github.com/xai-org/grok-build)。“Grok Build 现在开源了，”[Musk 发文称](https://x.com/elonmusk/status/2077495635687723408)。此举看起来像是对 Claude Code 和 Codex 的直接攻击：免费提供开发者工具、重置使用限制，并迫使竞争工具捍卫其定价。

随后，彭博社公布的数据解释了 SpaceXAI 为何能负担得起这一开源举措。据报道，Claude Code 的背后公司 Anthropic[每月向 SpaceXAI 支付 12.5 亿美元](https://www.bloomberg.com/news/articles/2026-05-20/anthropic-to-pay-spacex-nearly-45-billion-for-computing-deal)用于计算。加上 Anthropic、Google 和 Reflection，SpaceXAI 的计算协议[每月总额约为 23 亿美元](https://www.bloomberg.com/news/articles/2026-07-16/spacexai-identity-crisis-at-elon-musk-s-chatbot-company)。

Musk 在与 Anthropic 争夺开发者的同时，还在向 Anthropic 出租其竞争所需的机器。SpaceXAI 并不需要 Grok 击败 Claude 才能从 Claude 的增长中获利。

开源该工具可能[会扩大编程代理的市场](https://thenewstack.io/anthropic-claudecode-opencode-split/)。即便开发者最终选择了 Claude，SpaceXAI 依然拥有极佳的盈利地位。

## Musk 即便在编程代理竞赛中落败也能获得收益

在整个 2026 年，编程代理变得越来越强大、自主且对 Token 的需求量巨大。Musk 现已将主要的代理工具开源，尽管驱动它的模型运行仍需成本。

Grok Build 与 Claude Code 和 OpenAI 的 Codex 属于同一类别的终端编程代理。正如我们的 Janakiram MSV 在一份[六个月后的比较分析中](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/)所写的那样，竞争早已不再是关于原始模型质量：“一旦每个人都接受了这种模式，竞争就转向了其周围的平台。”Grok Build 于 5 月进入平台大战，其设计优先考虑本地化，在 SWE-bench 上的得分约为 70%。其背后的模型也并非儿戏：[Artificial Analysis](https://x.com/ArtificialAnlys/status/2074942097158021371) 将新推出的 Grok 4.5 置于基准测试的前沿，同时测得其在该性能水平下是最便宜的模型之一。OpenAI 注意到了这一点。其总裁 Greg Brockman[回复道](https://x.com/gdb/status/2077424882502263081)：“如果你能在任何工作负载上获得更好的性价比，我很乐意听听细节，”并公布了他的电子邮件地址。

那么为什么要免费提供这个编程代理呢？因为 SpaceXAI 可以负担得起这场与 OpenAI 和 Anthropic 不同的战争。Musk 可以开源该工具，以激进的价格推销 Grok，并依然从 Anthropic（他试图削弱的公司）那里赚取基础设施收入。

Musk 有足够的计算能力来采取这一举措。据[*彭博商业周刊*](https://www.bloomberg.com/news/articles/2026-07-16/spacexai-identity-crisis-at-elon-musk-s-chatbot-company)报道，xAI 自己的模型在 4 月份仅使用了其可用计算能力的 11%，因此它有充足的余地，且很少限制其客户，尽管据报道 Anthropic 正忙于应对算力紧缺。SpaceX 的首席财务官明确了这一策略：“Elon 认为计算和电力将是限制因素。我们已经看到了这一点。” 这就是其奇怪的形态。SpaceXAI 可以补贴正在与自己最大基础设施客户之一竞争的产品。

## 商业模式比运营它的组织更强大

如果公司无法运营产品，第二个经济地位就毫无价值。这就是 Musk 的故事变得更艰难的地方。[同一篇彭博社文章](https://www.bloomberg.com/news/articles/2026-07-16/spacexai-identity-crisis-at-elon-musk-s-chatbot-company)描绘了一个陷入混乱的运营局面：xAI 的所有 11 位联合创始人都已离职，内部调查发现最常见的抱怨是管理层“似乎不知道自己想要什么”。对于一家销售编程工具的公司来说，最致命的细节是：据报道，xAI 自己的工程师甚至不使用这些工具，而是转而使用 Anthropic 和 OpenAI 的产品。如果构建 Grok 的人都不信任它来编写代码，那么外部开发者为什么要信任它呢？

那个信任问题在开源发布的那一周变得更糟了。Grok Build 在开发者发现它悄悄将整个目录上传到 SpaceXAI 云端后的第二天就开源了。[一位用户观察到](https://x.com/a_green_being/status/2076598897779020159)它获取了“我的 SSH 密钥、密码管理器数据库、文档、照片、视频，所有东西。”[Musk 承诺](https://x.com/elonmusk/status/2076739687658496209)这些数据将被“彻底、完全地删除”。在这种情况下，无论开源发布具有什么战略价值，它也成为了危机公关。

随后全世界阅读了 Grok Build 的代码。[正如 Simon Willison 所写](https://simonwillison.net/#:~:text=xai%2Dgrok%2Dtools,how%20it%20works.)，Grok Build 的部分工具是从其他编程代理移植过来的，包括 OpenAI 的 Codex 和开源的 OpenCode。因此，这个针对 Codex 的工具整合了源自 Codex 的开源许可作品。

这不一定是一场丑闻。这就是开源应该有的运作方式。但打开仓库同时暴露了两件事：Musk 刚刚禁用的隐私机制，以及编程代理层变得多么容易移植。我们的 Paul Sawers 几个月前就指出[工具层是编程代理实现差异化的地方](https://thenewstack.io/coding-agents-team-infrastructure/)。Grok Build 展示了保持这种差异化为私有有多么困难。

抛开组织混乱不谈，这一经济举措既狭隘又聪明。

Musk 不需要从 Anthropic 那里赢回开发者。开源 Grok Build 可以扩大编程代理的市场，即使开发者选择了 Claude，SpaceXAI 也能从中受益。Anthropic 为这种增长背后的计算能力买单。

这就是 Musk 立场的奇怪之处。Anthropic 必须让 Claude 击败 Grok，而 Musk 在它成功时还能赚到钱。