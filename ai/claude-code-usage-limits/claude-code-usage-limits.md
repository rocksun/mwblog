<!--
title: Claude Code 用户炸锅：使用限制加速，额度耗尽太快了！
cover: https://cdn.thenewstack.io/media/2026/03/df94d454-bekeen-co-ocu9llftdjw-unsplash-scaled.jpg
summary: Claude Code 用户反馈使用限制比以往更快达到，Anthropic已承认并正在调查。有用户称单个提示消耗大量配额，甚至发现潜在的缓存Bug导致成本虚高10-20倍。此问题发生在Anthropic调整高峰期配额后，引发用户不满，甚至考虑转向竞争对手。Anthropic表示将持续调查并适时公布进展。
-->

Claude Code 用户反馈使用限制比以往更快达到，Anthropic已承认并正在调查。有用户称单个提示消耗大量配额，甚至发现潜在的缓存Bug导致成本虚高10-20倍。此问题发生在Anthropic调整高峰期配额后，引发用户不满，甚至考虑转向竞争对手。Anthropic表示将持续调查并适时公布进展。

> 译自：[Claude Code users say they’re hitting usage limits faster than normal](https://thenewstack.io/claude-code-usage-limits/)
> 
> 作者：Meredith Shubel

Claude Code 用户表示他们比以前更快地达到了使用限制——Anthropic 在 Reddit 和 X 上证实了这是一个持续存在的问题。

周一在 [Reddit](https://www.reddit.com/r/Anthropic/comments/1s7zfap/investigating_usage_limits_hitting_faster_than/) 上，Anthropic 承认了用户的疑虑，写道：“我们意识到用户在 Claude Code 中达到使用限制的速度比预期快得多。”

几小时后，通过另一条评论发布了更新：“仍在处理中。这是团队的首要任务，我们知道这阻碍了许多用户。一旦有进展，我们将立即分享。”

## 用户在 Reddit 和 X 上分享困境

这家人工智能公司似乎对造成此问题的原因感到困惑——或者至少他们对根本原因保持沉默。

与此同时，用户们则大声表达他们的困境。

[一位 Reddit 用户](https://old.reddit.com/r/Anthropic/comments/1s8ex9a/nothing_changed/)声称一个提示就消耗了他们限额的10%，这与他们所说的通常只消耗0.5-1%相比，是一个急剧的增加。另一位 Reddit 用户表示同情，并在同一帖子中评论道：“我工作1小时就用完了 Max 5，以前我可以工作8小时……”

X 上也充斥着类似的抱怨。“我每月100美元的套餐，现在30分钟的编程就用掉了我60%的会话限制，”[一位用户](https://x.com/alexoakdev/status/2025153521134567569)抱怨道。“几个月前，这可能只用了5%，我想。”[另一位用户](https://x.com/thegupler/status/2037610036873052515)补充道：“我有两次会话，并没有怎么重度使用，但使用率已经达到91%了。”

还有[一位用户](https://x.com/om_patel5/status/2038757628323430844)声称使用量开始攀升，甚至从一个简单的问候开始：“在专业版（Pro plan）上向 Claude 说‘你好’现在会消耗你整个会话使用量的2%。”

Anthropic 在 Reddit 上发布的相同声明被 Claude Code 团队的一名成员[发布](https://x.com/lydiahallie)到 X 上，指出该公司“正在积极调查，一旦有更新就会分享更多信息。”

## 用户发现的 Bug 可能是问题根源

虽然 Anthropic 尚未说明导致意外达到限制的原因，但[一位 Reddit 用户声称](https://www.reddit.com/r/ClaudeCode/comments/1s7mitf/psa_claude_code_has_two_cache_bugs_that_can/)在逆向工程 Claude Code 二进制文件后，自己发现了这个 Bug，发现“两个独立的 Bug 导致提示缓存损坏，悄无声息地将成本提高了10-20倍。”

他们认为这个 Bug 破坏了缓存历史，迫使 Claude Code 重新处理每个提示，从而推高了使用量。

在 X 上讨论用户提出的 Bug 的帖子中，Anthropic 的技术人员 [Thariq Shihipar](https://www.linkedin.com/in/thariqshihipar/) [回应道](https://x.com/trq212/status/2038684294911279201)：“我们正在积极调查这个问题，但尚不确定它是否真实；提示缓存 Bug 可能非常微妙。”

## 使用限制问题出现在近期政策更新之后

有趣的是，Claude Code 用户配额方面的困境出现在一系列近期政策变动之后。

上周，Anthropic 表示将在高峰时段减少配额，[Shihipar 再次在 X 上](https://x.com/trq212/status/2037254607001559305)解释道：“为了管理对 Claude 日益增长的需求，我们正在调整免费/专业版（Pro）/最大版（Max）订阅用户在高峰时段的5小时会话限制。”

但 Shihipar 的 X 帖子是这家人工智能公司就此话题的唯一表态，似乎起到了官方声明的作用。Shihipar 表示 Anthropic“取得了许多效率提升来抵消这一点”，并且预计只有大约7%的用户会“达到他们以前不会达到的会话限制，尤其是在专业版（Pro tiers）中。”

这篇社交媒体帖子恰逢[为期两周的限时促销活动](https://thenewstack.io/anthropic-doubles-claude-usage-outside-peak-hours/)，在此期间 Anthropic 将 Claude 用户在非高峰时段的使用限制翻倍。

## 用户仍在等待修复

值得注意的是，感到受挫的不仅仅是 Claude Code 用户。

在讨论此问题的同一[帖子](https://old.reddit.com/r/Anthropic/comments/1s8ex9a/nothing_changed/)中，另一位 Reddit 用户补充道：

“不仅仅是 Anthropic。我正在使用3个 OpenAI Plus、1个 Gemini Pro 和5个 Claude Max，每个月到第三周我都会达到所有这些服务的上限，几乎每次5小时的上限。每个服务的交付量都比以前少了。”

即便如此，一些用户已经提出了转用 OpenAI 竞争对手 Codex 的想法，其中[一位写道](https://old.reddit.com/r/Anthropic/comments/1s8ex9a/nothing_changed/)：“我上周才加入，现在就想离开了。”

更令人困惑的是，Anthropic 目前没有提供其套餐的确切使用限制。关于使用和长度限制的[支持文档](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work?utm_source=chatgpt.com)指出“不同的订阅计划（专业版Pro、最大版Max、团队版Team等）有不同的使用额度，付费计划提供更高的限制”，但没有明确说明具体额度。

目前尚不清楚 Claude Code 的使用限制何时能恢复正常水平。当被问及用户何时能期待修复以及问题背后可能的原因时，Anthropic 发言人表示调查仍在继续，一旦取得进展将发布公告。