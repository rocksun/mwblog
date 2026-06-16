<!--
title: Fable 5与Mythos 5模型持续停用：Anthropic面临严峻挑战
cover: https://cdn.thenewstack.io/media/2026/06/c8906d03-photo-album-1-01-1024x576.png
summary: Anthropic因Fable 5模型被曝存在网络攻击安全漏洞，遭美国政府强制下架并实施出口管制。尽管Anthropic称漏洞较小且存在误解，但因拒绝修复及与政府的立场分歧，目前模型仍处于停用状态，凸显了AI安全监管与企业责任间的严峻挑战。
-->

Anthropic因Fable 5模型被曝存在网络攻击安全漏洞，遭美国政府强制下架并实施出口管制。尽管Anthropic称漏洞较小且存在误解，但因拒绝修复及与政府的立场分歧，目前模型仍处于停用状态，凸显了AI安全监管与企业责任间的严峻挑战。

> 译自：[Fable 5 and Mythos 5 remain suspended: "The ball is in Anthropic’s court"](https://thenewstack.io/fable-5-and-mythos-5-remain-suspended-the-ball-is-in-anthropics-court/)
> 
> 作者：Frederic Lardinois

周五晚上，Anthropic突然[禁用](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)了其新的旗舰模型 Fable 5 和 Mythos 5。此前，美国政府获悉 Fable 5 存在一种特定的越狱方法，并对其下达了出口管制令。由于该命令适用于所有外国人（包括身在美国的外国人），Anthropic除了对所有人禁用这些模型外别无选择。

目前尚不清楚此次越狱的具体内容，Anthropic认为政府指出的只是“小漏洞”，而且“看起来都相对简单”，并未超出其他公开模型的能力范围。

当 Anthropic 宣布 Fable 5 和 Mythos 5 时，曾指出 Fable 5 在英国 AI 安全研究所和其他外部测试人员的帮助下，进行了广泛的红队安全演习。Anthropic 内部测试显示，该模型完成对抗性网络任务的成功率约为 5%。

Fable 5 [模型卡片](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf) 也特别指出：“如果发现公共通用越狱方法，我们将迅速采取行动更新防御措施，以确保其对所有已知攻击保持稳健。”但根据目前的信息，此次问题并非关于通用越狱，而是适用于一个非常具体的问题。

截至周六上午，Anthropic 尚未更新其之前的声明，该声明总结称这一切“是一场误解”。

## 这不仅仅是一个误解？

考虑到现在是 2026 年，情况变得更加复杂。周六，[总统科学技术顾问委员会](https://en.wikipedia.org/wiki/President%27s_Council_of_Advisors_on_Science_and_Technology)联合主席、白宫前 AI 与加密货币主管 David Sacks 在 [推特](https://x.com/davidsacks/status/2065853007619588171) 上发布了美国政府版本的事件经过。

Sacks 认为，“Anthropic 和[美国政府]的一位高度可信的合作伙伴”报告了此次越狱，政府要求 Anthropic 首席执行官 Dario Amodei 改进护栏以修复越狱问题，否则就下架模型。“Dario 拒绝了，”Sacks 写道。

## Amazon 的角色

根据 [华尔街日报](https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578) 和 [The Information](https://www.theinformation.com/articles/amazons-jassy-raised-concerns-anthropic-model-trump-crackdown) 的独立报道，正是 Amazon 首席执行官 Andy Jassy 向“包括财政部长 Scott Bessent 在内的美国官员”报告了 Amazon 研究人员发现的越狱问题。

报道称，那些 Amazon 研究人员发现了让 Fable 5（带有安全护栏的 Mythos 5 版本）协助进行网络攻击的方法。Anthropic 在发布 Fable 5 时曾指出，已设置护栏以防止其协助用户发动网络攻击或制造生物武器等。

事实上，许多用户很快抱怨该模型[拒绝回答无害的问题](https://thenewstack.io/fable-5-developer-reactions/)。通常，当系统检测到潜在的不安全提示时，Claude 也会悄悄转而使用之前的旗舰模型 Opus 4.8。

由于这次越狱是由 Amazon 报告的，这些研究人员很可能是在 [Amazon Bedrock](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/) 上测试了 Fable 5，Amazon 称该平台与直接通过 Anthropic 使用 Claude 具有相同的安全机制。

Sacks 认为，Anthropic 为其不愿下架模型的立场进行辩护，“称越狱并不严重”，并采取了一种修辞手段，将 Anthropic 置于其自设的困境中。

“这并非可信合作伙伴和美国政府所认为的那样；这种轻描淡写的语言也不符合 Anthropic 作为 AI 安全公司的品牌形象，”他写道，“很难理解他们怎么能声称允许网络武器运行的越狱不被定义为‘严重’。”

正如自该报道发布以来许多评论员所指出的那样，正是 Anthropic 声称 Mythos 5 对公众发布过于危险。同样是 Anthropic，将其品牌建立在作为认真对待 AI 安全的前沿实验室之上。

现在 Sacks 可以反过来攻击该公司并写道：“过去，Anthropic 总是说安全必须是重中之重，必须被极其认真地对待。而在这种情况下，Anthropic 将消费类模型的持续提供置于安全之上。”

## 接下来会发生什么？

最明显的解决方案是 Anthropic 设置新的护栏，使这种特定的越狱变得不可能——尽管考虑到这些非确定性模型的性质，其他越狱可能很快就会出现。

不过，很有可能我们会相对较快地看到修复方案，出口管制将被解除，模型也将重新可用。

然而，这确实为美国政府如何处理 AI 安全开创了先例，其他位于美国的 AI 前沿实验室肯定会密切关注这一点。毕竟，AI 的发展方式一直是这些实验室之间的不断博弈，一个接一个地超越对方——Fable 5/Mythos 5 也不太可能是 AI 模型开发的巅峰。

这对 OpenAI 和 Google 的下一批模型意味着什么还有待观察。毕竟，美国政府已经提议在发布新模型之前进行自愿安全测试，而这件事很可能会将这一想法再次推向风口浪尖。

值得注意的是，Anthropic 一直是比任何人都更积极[倡导](https://darioamodei.com/post/policy-on-the-ai-exponential) AI 监管的公司。

## “球在 Anthropic 那边”

当然，所有这些都因 Anthropic 与特朗普白宫之间紧张的关系而变得更加复杂。

Sacks 在他的推文中认为情况并非如此，并表示“政府重视 Anthropic 的技术能力，并认为这个问题虽然严重，但应该很容易解决。球在 Anthropic 那边。”