Anthropic 周二推出了 [Claude Sonnet 4.6](https://www.anthropic.com/claude/sonnet)，这是其主流模型的最新版本。

这个新版本承诺在大多数任务中几乎能与该公司旗舰的 [Opus 4.6 模型](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/)媲美，后者才推出不到两周，但价格却显著降低，每百万输入/输出 token 仅为 3 美元/15 美元（Opus 模型为 5 美元/25 美元）。

与之前的版本和 Opus 4.6 一样，Sonnet 4.6 在 Beta 版中提供 100 万 token 的上下文窗口。

## 基准测试

与旧版 Sonnet 模型相比，Sonnet 4.6 在几乎所有常见基准测试中都轻松超越了它。在执行办公任务时（使用 OpenAI 的 [GDPval 基准](https://openai.com/index/gdpval/)），它甚至击败了最新的 Opus 模型、Google 的 Gemini 3 Pro 和 OpenAI 的 GPT-5.2。

在编码任务方面，Anthropic 长期以来一直优于竞争对手，Sonnet 4.6 的基准测试结果通常与 Opus 4.6 相差一个百分点甚至更少。Anthropic 指出，一些改进包括更好的整体一致性和指令遵循能力。

> Sonnet 4.6……甚至击败了最新的 Opus 模型，以及 Google 的 Gemini 3 Pro 和 OpenAI 的 GPT-5.2。

Anthropic 在其公告中指出，在他们自己的测试中，开发者有 59% 的时间更喜欢 Sonnet 4.6，而不是去年 11 月推出的上一代 Opus 4.5 模型。这反映在已发布的基准测试中，新版 Sonnet 模型远远领先于旧版 Opus。但 Anthropic 也指出，使用过该模型的开发者发现，它不太可能过度设计解决方案，也不太可能出现幻觉或在未能找到正确解决方案时声称成功。

![](https://cdn.thenewstack.io/media/2026/02/5addb4ce-anthropic-sonnet-46-benchmarks.png)

## 计算机使用

至于计算机使用，这是 Anthropic 近期相当关注的另一个领域，新模型在 OSWorld 计算机使用基准测试中也与 Opus 非常接近。然而，Anthropic 认为，基准测试并不总是能说明全部情况。该公司在公告中指出，用户在使用该模型时看到的是“在诸如导航复杂电子表格或填写多步骤网络表单等任务中达到人类水平的能力，然后将其整合到多个浏览器标签页中”。

> 使用过该模型的开发者发现，它不太可能过度设计解决方案，也不太可能出现幻觉或在未能找到正确解决方案时声称成功。

但即使 Anthropic 也承认，尽管这些模型在浏览器中执行某些任务方面表现出色，并在这些基准测试中接近人类水平，但它们仍无法完全匹配最熟练的人类。

![](https://cdn.thenewstack.io/media/2026/02/5a6220d8-claude-sonnet-4.6-demo-video.gif)

对于通过 Claude 开发者平台使用 Claude API 的开发者来说，Sonnet 4.6 现在支持上下文压缩（context compaction），以帮助它跟踪更长的会话（目前处于 Beta 版），以及 [自适应思维](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)（adaptive thinking），因此模型可以根据自身对任务复杂性的评估来设置扩展思维的 token 预算。此功能随 Opus 4.6 一同推出。

## 可用性

在早期的更新中，Sonnet [偶尔](https://thenewstack.io/anthropic-laundoes-claude-sonnet-4-5/)表现优于 Opus，但这次并非如此。不过，未来 Sonnet 4.6 将成为 [claude.ai](https://claude.ai) 上免费和专业版用户的默认模型，以及 Claude 的 Cowork 模式的默认模型。鉴于该模型在许多 Cowork 可能用到的办公任务中优于 Opus 4.6，这很合理。

## Claude Haiku 4.6 在哪里？

Anthropic 唯一尚未更新到 4.6 版本的模型是 Haiku，它是其最小、最快且最经济的模型。Haiku 4.5 于 2025 年 10 月发布，因此它也该更新了，但 Anthropic 通常更新 Haiku 的速度较慢，并且经常跳过一些版本号。