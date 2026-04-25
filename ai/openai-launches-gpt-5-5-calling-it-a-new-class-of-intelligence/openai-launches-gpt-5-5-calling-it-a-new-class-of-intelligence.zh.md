AI 模型发布周期继续。周四，OpenAI [发布了](https://openai.com/index/introducing-gpt-5-5/) GPT-5.5 和 GPT-5.5 Pro。不出所料，新模型是迄今为止功能最强大的模型。

GPT-5.5 将在 ChatGPT 和 Codex 中面向所有 OpenAI 付费用户开放，而 GPT-5.5 Pro 将仅在 ChatGPT 中向 Pro、Business 和 Enterprise 用户推出。它很快将登陆 API（但价格也会比以前更贵）。

在 Anthropic 一周前[发布 Opus 4.7](https://thenewstack.io/claude-opus-47-launch/)之后，OpenAI 紧随其后只是时间问题——而且，至少根据我们目前看到的基准测试，GPT-5.5 和 5.5 Pro 在当今许多标准基准测试中击败了 Opus 4.7。不过，在许多基准测试中，GPT-5.4 Pro 的表现依然优于默认的 GPT-5.5。

在发布前的媒体电话会议上，OpenAI 总裁兼联合创始人 Greg Brockman 将 GPT-5.5 描述为“一种新级别的智能。这是迈向更具代理性和直观计算的一大步。”

![](https://cdn.thenewstack.io/media/2026/04/63a3057d-screenshot-2026-04-23-at-10.19.56-1024x483.png)

GPT-5.5 基准测试。来源：OpenAI。

根据 Greg Brockman 的说法，新模型特别擅长在较少指导下工作。“使用起来感觉更加直观，”他说。“它可以查看一个不明确的问题，并弄清楚下一步需要发生什么。对我来说，这确实感觉像是为我们未来将如何使用计算机、如何进行计算机工作——为大规模代理计算的运行方式——奠定了基础。”

尽管具备了这些额外的功能，新模型并不比前代慢，并且使用的 token 更少。“与 [GPT] 5.4 之类的模型相比，它是一个速度更快、思维更敏捷的思想家，且使用的 token 更少，这意味着有更多的前沿 AI 可供企业和消费者使用，这也是我们目标的一部分，”他说（这可能暗示了对 Anthropic 最近容量问题的嘲讽）。

具体而言，GPT-5.5 的每 token 延迟与之前的模型保持一致，同时在 token 使用方面也更有效率。OpenAI 主张 GPT-5.5 能够以“竞争性前沿编程模型一半的成本”提供最先进的智能。

## 基准测试

当然，该模型在编程方面也更出色。OpenAI 研究副总裁 Mia Glaese 指出，例如，该模型现在在“Codex 中的高级工程工作”方面表现好得多。据 Mia Glaese 描述，一位拥有新模型访问权限的早期测试人员将一个草率的氛围编程代码库交给了 GPT-5.5，并要求它将其转变为“漂亮的代码库”。Mia Glaese 说，模型生成的内容基本上就是高级工程师会做的工作。

在基准测试中，包括测试模型如何处理开发人员命令行工作流的 Terminal-Bench 2.0，以及测试模型如何解决真实世界 GitHub 问题的 SWE-Bench Pro，得分分别为 82.7% 和 58.6%。

我们还没有 Anthropic Opus 4.7 的 SWE-Bench Pro 分数，但在 SWE-Bench Pro 上，它达到了 64.3%，这似乎是 Opus 仍占据上风的一个领域。但在 Terminal-Bench 2.0 上，GPT 5.5 得分为 82.7%，而 Opus 仅达到 69.4%。

OpenAI 尚未提供 GPT-5.5 Pro 的编程基准测试。

计算机使用能力也随着这次更新获得了智能提升，正如 OpenAI 首席研究员 Mark Chen 所强调的。“借助 Codex 的计算机使用能力，我们确实开始感觉到我们拥有了一个模型，它在处理计算机使用方面的灵活性和准确性与操纵代码时一样，”他说。

![](https://cdn.thenewstack.io/media/2026/04/076461cc-screenshot-2026-04-23-at-10.25.59-1024x691.png)

GPT-5.5 token 使用对比。来源：OpenAI。

在基准测试中，GPT 5.5 和 Opus 4.7 差距并不大，尽管在 OSWorld-Verified 测试（要求模型在操作系统中执行计算机任务）中，GPT-5.5 以 78.7% 的得分略领先于 Opus 4.7 的 78%。

![](https://cdn.thenewstack.io/media/2026/04/7d7c0ba0-gdpval-1024x663.png)

来源：OpenAI。

在许多学术基准测试中，Opus——以及某种程度上甚至是谷歌较旧的 Gemini 3.1 Pro——继续优于 GPT-5.5，但 GPT-5.5 在 FrontierMath Tier 1-3 和 Tier 4 等数学基准测试中击败了两者。

![](https://cdn.thenewstack.io/media/2026/04/17976f34-screenshot-2026-04-23-at-10.39.17-1024x386.png)

来源：OpenAI。

通过这次更新，OpenAI 再次强调它在构建这次更新时使用了模型本身——以及 Codex。

Greg Brockman 强调的一个有趣观点是，对于 OpenAI 来说，模型本身现在只是一个更大产品的一部分。

“所以我们在 OpenAI，希望为所有试图用计算机完成工作的人带来代理能力，而不不仅仅是软件工程师，”他说。“需要理解的一点是，模型本身不再是整个产品，对吧？你可以把它看作是大脑，但在我们交付的应用、代理装备方面构建身体——这也是我们正在推进的工作。”

## Mythos 时代的 GPT-5.5

鉴于最近关于 Anthropic 的 Mythos 模型及其网络安全能力的讨论，OpenAI 还强调了它如何在此次发布中减轻这些风险。

该公司认为，对于具有先进网络安全能力的模型，最好的前进方向是“确保[这些模型]可以被用于加速网络防御并加强生态系统。”

OpenAI 表示正在部署“行业领先的安全措施”，并计划扩大访问权限以加速各个级别的网络防御。

在 CyberGym 基准测试中，GPT-5.5 得分为 81.8%。据 Anthropic 称，Mythos 得分为 83.1%。

![](https://cdn.thenewstack.io/media/2026/04/e3bb59cd-screenshot-2026-04-23-at-10.55.08.png)

来源：OpenAI。

## 可用性与价格

GPT-5.5 正面向 ChatGPT 和 Codex 中的所有 ChatGPT 付费用户推出，GPT-5.5 Pro 仅限于 ChatGPT 中的 Pro、Business 和 Enterprise 用户。还将有一个 GPT-5.5 Thinking 模式，也将面向所有付费用户开放。

对于那些在 Codex 中需要更高速度的用户（GPT-5.5 在其中拥有 400,000 token 的上下文窗口），OpenAI 还提供了一个 Fast 模式。该模式速度提升 1.5 倍，但成本也增加 2.5 倍。

在 API 中，GPT-5.5 的价格为每 100 万输入 token 5 美元，每 100 万输出 token 30 美元，并将提供 100 万 token 的上下文窗口。这是 OpenAI 之前对 GPT-5.4 收费的两倍。

GPT-5.4 也有分层定价结构，其中 272,000 token 以下的短提示按标准费率收费，而较长提示的输入/输出成本为每百万 5 美元/22.5 美元。

OpenAI 在其博客文章中承认了价格差异：“虽然 GPT-5.5 的价格高于 GPT-5.4，但它更智能，且 token 效率高得多。在 Codex 中，我们精心优化了体验，使得 GPT-5.5 对大多数用户来说能以比 GPT-5.4 更少的 token 提供更好的结果，同时继续在各个订阅层级提供慷慨的使用量。”

对于 GPT-5.5 Pro，每百万输入/输出 token 的成本为 30 美元/180 美元，与 GPT-5.4 相同。