<!--
title: Linux之父Linus Torvalds回击AI反对者：要么接受，要么分叉代码
cover: https://cdn.thenewstack.io/media/2026/07/985d4d27-gamma-valeri-n1aojmc7lo0-unsplash-scaled.jpg
summary: Linux内核创始人Linus Torvalds近日公开表态，Linux项目将支持AI辅助开发。他强调AI只是工具，呼吁反对者不要逃避，若无法接受可选择离开或分叉项目，核心在于人类开发者需对提交代码的意图负责。
-->

Linux内核创始人Linus Torvalds近日公开表态，Linux项目将支持AI辅助开发。他强调AI只是工具，呼吁反对者不要逃避，若无法接受可选择离开或分叉项目，核心在于人类开发者需对提交代码的意图负责。

> 译自：[Linux creator Linus Torvalds tells AI haters to walk away from Linux, or go fork it](https://thenewstack.io/torvalds-linux-ai-stance/)
> 
> 作者：Adrian Bridgwater

Linux内核的创建者 [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) 在 [lore.kernel.org](http://lore.kernel.org) 邮件列表存档服务上发布了一份措辞强硬的声明，更新了他对在软件开发中使用人工智能（AI）的立场。

作为传统的人性化代码质量的坚定捍卫者，Torvalds 过去对 AI 态度有些不屑，但现在他已转变立场，明确表示支持在 Linux 代码库中使用 AI。

## Linux 并非反 AI 项目

“我意识到有些人真的很不喜欢 AI，但作为最高级维护者，这是我愿意坚决拍板的领域，”Torvalds 写道。“[Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 并非那些反 AI 的项目之一，如果有人对此有意见，他们可以走开源的老路去分叉（fork）它。或者干脆离开。”

这位以观点鲜明著称的芬兰裔美国人确认，他将 AI 视为一种工具，“就像我们 [软件工程师] 使用的其他工具一样”，并进一步同意，在今天“它显然是一个有用的工具”。在保持平衡的同时，Torvalds 也承认，截至目前，很难判断 AI 经济最终会是什么样子。

Torvalds 再次转折写道，他觉得 AI “也可能是一个有点痛苦的工具”，这既来自于它对维护者工作负载的影响，也来自于“它 [不断发现令人尴尬的错误](https://thenewstack.io/ai-coding-tools-create-more-bugs-than-they-fix/)”这一事实。

“但解决方案不是像有些人似乎做的那样，把头埋进沙子里，声嘶力竭地唱着‘啦啦啦，我听不见你’，”Torvalds 写道。“解决方案是确保那些大语言模型（LLM）工具能够帮助维护者，而不是仅仅给他们制造痛苦。在这一点上毫无疑问。”

> “我意识到有些人真的很不喜欢 AI，但作为最高级维护者，这是我愿意坚决拍板的领域。”

“我们并没有强迫任何人使用它，但我会非常大声地无视那些试图阻止其他人使用它的人，”他补充道。

具有讽刺意味的是，正如 Torvalds 自己所承认的那样，即使在他今天看来已不再是问题，但在仅仅一年前，他对使用 AI 的看法可能还不是一个明确的“赞成”。

在 2024 年 10 月的视频故事网站 [TFIR](https://www.youtube.com/watch?v=s4wlrxFf2lM) 上，Torvalds 对 AI 的态度远没有那么乐观。

## Torvalds 在 2024 年的看法：AI 将在五年后发挥作用

“我认为 AI 非常有趣，它将会改变世界，但同时我非常讨厌炒作周期，所以我真的不想参与其中。因此，我目前对 AI 的态度基本上是忽视它，因为我认为围绕 AI 的整个科技行业处于一个非常糟糕的位置，它是 90% 的营销和 10% 的现实，”Torvalds 在视频 37 分 57 秒处说道。

“五年后，情况会发生变化，到那时我们将看到哪些（AI）正在每天用于实际工作负载中，而不是仅仅 [ChatGPT](https://thenewstack.io/openai-codex-chatgpt-mobile/) [被用于] 制造像，呃，很棒的演示，”他补充道。

距离 Torvalds 发表反 AI 炒作周期的抨击实际上已经过去了 21 个月或 637 天，所以这离五年还差得远。

> “我真的不在乎 AI 是否参与编写了代码。我关心的是提交代码的人能够解释他们的意图，为什么要这样做，以及为什么它适合这个项目。”

平心而论，2024 年中后期的企业软件行业头条新闻充斥着 Kubernetes 的回迁分析、[SAP](https://news.sap.com/2024/10/sap-announces-q3-2024-results/) 第三季度云收入 25% 的增长，以及围绕 [Google 的 Memorystore for Valkey 预览版](https://cloud.google.com/blog/products/databases/announcing-memorystore-for-valkey) 的故事。Anthropic 当时处于 [Claude 3.5 Sonnet](https://www.anthropic.com/news/3-5-models-and-computer-use) 阶段，[Microsoft 发布了](https://www.cnbc.com/2024/10/21/microsoft-to-allow-autonomous-ai-agent-development-next-month.html) Copilot Studio 中的自主 AI 代理，以抵御来自 Salesforce 的挑战。

或许那确实是不同的时期。

## 关于 AI 代码质量的辩论已经结束

开源开发者安全公司 [nolabs](https://nolabs.ai/) 的联合创始人兼首席执行官 [Luke Hinds](https://www.linkedin.com/in/lukehinds/) 告诉 *The New Stack*，“Torvalds 的观点完全正确”，我们不应该禁止 AI 工具或把头埋在沙子里——但我们需要坚持让人们对思考负责。

“关于 AI 代码质量的辩论已经结束，老实说，这一直是一种干扰，”Hinds 说。“开源领域重要的问题并没有改变：是否有人为这项贡献背书，并且他们是否足够理解它，以至于可以解释它？我真的不在乎 AI 是否帮助编写了代码。我关心的是提交代码的人能够解释他们的意图，为什么要这样做，以及为什么它适合这个项目。我需要的是判断力的证据，而不仅仅是产出。”

> “Torvalds 的观点完全正确。”

Hinds 反对的失败模式是他解释的维护者已经看到的那种情况，即一个 AI 代码代理生成了 2000 行令人印象深刻的术语评论，以证明一个没有人清楚推导出的变更的合理性。

[Red Hat](https://www.redhat.com/en/keep-your-options-open?sc_cid=7013a000002w5eQAAQ&gclsrc=aw.ds&gad_source=1&gad_campaignid=22010509563&gbraid=0AAAAADsbVMSkcMqQOtpSNEkmRVX6ewYeZ&gclid=Cj0KCQjwguLSBhDLARIsAH-yPrFmZ-MIEzNphkPRa-fLIiaho_n7AET17KE-6UhRIF9blvRysdTSguAaAqxdEALw_wcB) 核心平台副总裁 [Mike McGrath](https://www.linkedin.com/in/mrmikemcgrath/) 告诉 *The New Stack*，他的组织在工作软件工程团队的 AI 辅助开发方面一直“非常公开我们的观点”。

“如果不是合作者，AI 辅助开发也是解决复杂工程挑战和推动开放式创新前进的一个极其强大的组成部分，”McGrath 说。“人类的指导和护栏对于开源中 AI 的可持续使用仍然至关重要，因为我们永远不能忽视这样一个事实：AI 是达到结果的工具，而不是结果本身。我们希望 AI 对每个人都有用，并期待与 kernel.org 的维护者合作，将未来的配套设施和大语言模型打造成对所有人开放且有效的产品。”

## 我们能预测 Torvalds 的下一个观点吗？

虽然试图预测 Torvalds 下一个观点的转变似乎很愚蠢，但他的疯狂中实际上有基于精英管理的逻辑。他很少完全坚持某种特定技术的某种立场，而是倾向于基于什么有效、什么无效以及未来可能有效的工程实用主义。

他的论点可能是：意识形态的一致性固然好，但基于能力的进步和基于客观公开社区评估的发展更好。