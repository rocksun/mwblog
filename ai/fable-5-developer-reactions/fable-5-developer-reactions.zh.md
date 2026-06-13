周二，Anthropic 推出了 [Fable 5](https://thenewstack.io/anthropic-claude-mythos-fable-5/)，这是首个备受期待的、面向公众的 Mythos 级模型。

Anthropic 表示，它比其他 Claude 模型能够更长时间地自主工作，并拥有增强的记忆能力以及处理复杂任务的编程技能。

早期的社区讨论表明该模型是一流的；但一些用户对较短的使用窗口、较为保守的护栏以及不可选择的数据保留政策表示怀疑。

## Fable 5 价格：效果很好，但代价高昂

Fable 5 在基准测试中表现卓越。但你不可能不劳而获，至少无法长期如此。

Fable 5 现已面向拥有 Claude Pro、Max、Team 以及基于席位的企业订阅用户，通过 API、Microsoft Foundry、Amazon Bedrock 以及 AWS 上的 Claude 平台提供。其价格为每百万输入 token 10 美元，每百万输出 token 50 美元。6 月 22 日之后，所有这一切都将结束，届时用户必须支付使用积分才能访问该模型——Anthropic 表示这是一种必要的罪恶，原因是容量限制，正如 [*The New Stack*](https://thenewstack.io/anthropic-claude-mythos-fable-5/) 所报道的那样。

但从早期的社区情绪来看，一些用户似乎认为传说中的 Fable 5 值得额外支出。

例如，正如一位用户在论坛 [Hacker News](https://news.ycombinator.com/item?id=48463808) 上发布的那样：“Fable 在‘高’设置下产生的效果明显好于 Opus 4.8 的‘超高’设置。”他们还声称 Fable “‘感觉’更聪明”：“它更昂贵，但也更高效。它能够找到一些 Opus 遗漏的错误。”

Reddit 上的用户也表达了类似的情绪；一位 redditor 在 [r/claudexpolorers](https://www.reddit.com/r/claudexplorers/comments/1u1bg4m/fable_5_is_out_megathread/) 中写道：“Opus 4.7 和 4.8 的负面特征要么不存在，要么得到了控制。”

不过，并非每个人都是即时粉丝。正如另一位用户在同一个 Hacker News 帖中所指出的：“很难确定，因为我没有坐在这里并行运行完全相同的情况来比较这两个模型。”

## 消耗速度确实太快

社区论坛中出现的一个共识是，Fable 5 的使用窗口短得令人沮丧。即使是那些被新模型能力所折服的用户也承认，它可能会以惊人的速度耗尽使用限额。

在 [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1u1cvkc/fable_5_is_insanely_good_but_watch_your_usage_i/) 上，一位声称使用 Max20 计划的 redditor 说，他们看着自己的使用量每分钟上升近 2%：“背景是，我使用 Opus 4.8 做同样的工作时，从未接近过限制。”

其他用户也附和了类似的叙述：

“几分钟内，我的 5x Max 账户从 0% 增加到 43%”；“我在 45 分钟内烧掉了整个 20x Max 计划”；“我用我的第一个测试提示词烧掉了我每周 Max 额度的 20% 和最初的 5 小时会话。”

对于 Fable 5 来说，能力和使用率似乎是一种权衡。虽然一些用户表示新模型优于 Opus，但另一些用户则感叹其使用窗口太短：“我以前使用 Opus 时从未遇到这种情况。”

## 护栏工作过度（且效果不佳）

正如 *The New Stack* 所报道的那样，Fable 5 的护栏是其最显著的特征之一。

早些时候，当 [Anthropic 发布 Claude Mythos 预览版](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) 时，只有 Project Glasswing 中的知名参与者才被授予访问权限，因为该模型被认为对于公众使用来说过于强大。

因此设置了护栏。旨在防止用户滥用该模型复杂的功能，Fable 5 的护栏将阻止模型回答某些问题（即关于网络安全、生物学、化学的问题），然后将其转交给 Opus 4.8。

但早期的社区讨论表明，Fable 5 可能会太频繁地“甩锅”。

“它阻止了我地理、水文学和政治生态学方面的所有工作，”r/claudexpolorers 的一位 redditor 说。r/ClaudeAI 的另一位用户写道：“问了它关于厄米矩阵的问题，这是数学中的一个常见概念。由于安全原因，它切换回了 Opus 4.8。”

在 Hacker News 上，讨论也是如此：“由于拒绝回答，它对我来说无法使用。我正在使用 Claude 在健康数据中寻找模式。”

## 无法避免的数据保留是一个不受欢迎的意外

对于许多用户来说，一件似乎在雷达下悄悄发生的意想不到的事情是 Anthropic 对 Fable 5 的新保留政策：

“我们需要对 Mythos 级模型上的所有流量进行 30 天保留，包括第一方和第三方表面，”Anthropic 在其公告博客文章中写道。

不出所料，用户似乎对这种数据保留的意外并不感到兴奋。尽管 Anthropic 表示不会使用这些数据来训练新的 Claude 模型，但 Hacker News 上的早期反应表达了失望，即便是对数据保留零承诺的企业账户也被卷入了新的数据保留现实中。

其他人预测，这很可能会使 Fable 5 失去在其组织内使用的资格：“这使得它对于 95% 的组织来说瞬间就成了不可行。”

## 也许 Fable + Opus 结合起来会更好？

虽然最初对 Fable 5 的高价格、短使用窗口、有些保守的护栏以及不可商量的数据保留政策有一些抱怨，但社区对该模型实际性能的共识还是相当热烈的。

对于使用率消耗快于预期的用户，r/ClaudeAI 上的一位 redditor 提出了一些建议：“让它做出选择，告诉它在必要时将任务卸载给 Opus、Sonnet、Haiku 或子代理。告诉它为困难的任务节省推理能力。”

另一位 redditor 思考这是否最终会成为默认模式：“我设想 Claude 的未来就是放弃这些用户选择的级别，让 Claude 决定每个请求需要什么级别，甚至在不同的层级上启动代理来处理请求的不同部分。”