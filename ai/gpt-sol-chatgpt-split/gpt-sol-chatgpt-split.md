<!--
title: GPT-5.6 Sol小幅升级：仅限ChatGPT提升，其余环境维持现状
cover: https://cdn.thenewstack.io/media/2026/06/0a19e99a-joshua-reddekopp-ipdsi8elxng-unsplash-scaled.jpg
summary: OpenAI更新了ChatGPT中的GPT-5.6 Sol模型，旨在提升日常对话质量。该更新不涉及Codex、Work及API版本。新版本引入了可调节的思考深度滑块，虽宣称错误率降低，但缺乏对比基准和透明度，开发人员需自行测试评估。
-->

OpenAI更新了ChatGPT中的GPT-5.6 Sol模型，旨在提升日常对话质量。该更新不涉及Codex、Work及API版本。新版本引入了可调节的思考深度滑块，虽宣称错误率降低，但缺乏对比基准和透明度，开发人员需自行测试评估。

> 译自：[GPT-5.6 Sol just got better in one place and stayed the same everywhere else](https://thenewstack.io/gpt-sol-chatgpt-split/)
> 
> 作者：Amanda Caswell

在将提示词（Prompts）迁移至 [Codex](https://thenewstack.io/openai-codex-cloud-evolution/) 或 Work 之前，在 ChatGPT 中进行测试的团队可能会注意到长任务处理上的差异。

OpenAI 周四宣布，已更新消费者版 ChatGPT 内置的 [GPT-5.6 Sol](https://thenewstack.io/openai-gpt-56-live/)，而 Codex 和 ChatGPT Work 所使用的版本则保持不变。

“由于此版本的 GPT-5.6 Sol 针对日常聊天进行了优化，因此它仅在 ChatGPT 的聊天体验中可用，”OpenAI 在其 [公告](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/) 中表示。“作为此次发布的一部分，驱动 Work 和 Codex 的 GPT-5.6 Sol 版本不会发生变化。”

> “作为此次发布的一部分，驱动 Work 和 Codex 的 GPT-5.6 Sol 版本不会发生变化。”

## 同名，不同模型

ChatGPT 处理任务的方式一直与其他环境略有不同。现在，这些差异可能会变得更加明显。但了解这一点的唯一方法是在它们实际运行的环境中测试提示词。公告中没有任何关于 GPT-5.6 Sol API 模型更改的内容。因此，猜测这对 API 意味着什么还为时过早。

## 滑块取代独立模型

由于 ChatGPT 现在为快速回答和深入探讨使用相同的 Sol 模型，Plus 和 Pro 用户获得了一个新的滑块（适用于网页、移动端和桌面端），用于选择 ChatGPT 在回答问题时投入的思考量。开发人员已经在 API 中做出了这种选择。但他们仍然必须决定何时值得为了更好的答案而[等待和付费](https://thenewstack.io/agentic-ai-token-costs/)。

> 但他们仍然必须决定何时值得为了更好的答案而等待和付费。

## 分类器监控每一个答案

OpenAI 于 7 月发布的 [GPT-5.6 系统卡（System Card）](https://deploymentsafety.openai.com/gpt-5-6?) 指出，Sol 和 Terra 配备了在生成答案时对其进行监控的分类器。如果其中一个检测到问题，系统会暂缓回答，由另一个系统进行核查。OpenAI 会针对每个模型分别调整这些分类器。

系统卡还指出了开发人员可能熟悉的一个问题：GPT-5.6 有时会[超出任务范围](https://thenewstack.io/anthropic-claude-containment-failure/)，并尝试进行用户未请求的更改。虽然 OpenAI 表示这种情况仍然很少见，但它发生的频率比 GPT-5.5 更高。

## 缺乏基准的基准测试

OpenAI 表示，更新后的 Sol 减少了事实性错误。在其针对金融、医疗和法律问题的内部测试中，包含至少一个错误答案的比例比 GPT-5.5 Instant 产生的答案低 68%。将成为免费用户和 Go 用户默认模型的 Luna，其错误率降低了约 62%。

但 OpenAI 并没有发布这些提示词，也没有提供足够的细节供任何人复现这些结果。它还将新的 Sol 与 GPT-5.5 Instant 进行了比较，而不是与 ChatGPT 中之前的 Sol 版本进行比较。这使得人们无法判断 Sol 本身到底改进了多少。

> 这使得人们无法判断 Sol 本身到底改进了多少。

工程团队需要通过在提示词实际运行的环境中进行测试来亲自寻找答案。将该配置与每个提示词一起保存，将使结果更容易复现，并揭示纸面上的升级是否在实践中产生了更好的结果。