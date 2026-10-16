<!--
title: OpenAI承诺提前六个月通知，GPT-4o用户却只剩三个月
cover: https://cdn.thenewstack.io/media/2026/10/fe1b843a-nick-hillier-yd5rv8_wzxa-unsplash-scaled.jpg
summary: OpenAI宣布将于2027年1月退役GPT-4o等四个模型，仅给开发者三个月迁移时间，这违背了其承诺的六个月提前通知政策，引发对迁移成本和模型行为变化的担忧。
-->

OpenAI宣布将于2027年1月退役GPT-4o等四个模型，仅给开发者三个月迁移时间，这违背了其承诺的六个月提前通知政策，引发对迁移成本和模型行为变化的担忧。

> 译自：[OpenAI promised developers six months’ notice. GPT-4o users got three.](https://thenewstack.io/openai-gpt4o-api-shutdown/)
> 
> 作者：Amanda Caswell

**OpenAI 将于 2027 年 1 月 14 日在其 API 中退役四个 GPT-4 模型。** 该公司周三向开发者发送的弃用通知涵盖了 GPT-4o、GPT-4o mini、GPT-4.1 和 GPT-4.1 mini，以及它们的带日期快照和在其基础之上构建的所有微调模型。

在只有三个月时间来迁移生产流量的情况下，OpenAI 推荐的替代品 GPT-6 Luna 在处理推理和工具调用时的差异之大，以至于更换模型 ID 可能只是迁移中最简单的部分。

> 在只有三个月时间来迁移生产流量的情况下，OpenAI 推荐的替代品 GPT-6 Luna 在处理推理和工具调用时的差异之大，以至于更换模型 ID 可能只是迁移中最简单的部分。

## GPT-4o 的漫长告别

GPT-4o 于 2024 年 5 月 13 日作为 OpenAI 的旗舰产品发布，并建立了一批忠实拥趸，其忠诚度甚至改变了公司的计划。当 GPT-5 在 2025 年 8 月取代它时，Reddit 上充满了抱怨声，OpenAI 在第二天就将其重新提供给付费的 ChatGPT 订阅者。这种暂缓退役的状态一直持续到 2026 年 2 月 13 日，当时 GPT-4o 和 GPT-4.1 从 ChatGPT 中消失了。两者仍然可以通过 API 使用，但这种访问权限现在也正在日薄西山。

届时，OpenAI 表示只有 0.1% 的 ChatGPT 日活用户仍在选择 GPT-4o，尽管该模型继续为围绕它构建的应用程序提供 API 请求。

GPT-4.1 是一次不同类型的发布，于 2025 年 4 月 14 日推出，是一个[仅限 API 的系列](https://openai.com/index/gpt-4-1/)，完全跳过了 ChatGPT，直接面向开发者，具有更强的代码编写能力、更好的指令遵循能力、高达 100 万个 Token 的上下文空间，以及更可靠的 diff 格式，方便任何将模型放飞到大文件上的用户。

OpenAI 的首席产品官 [Kevin Weil](https://www.linkedin.com/in/kevinweil/) 在发布直播中称它们为[“专为开发者训练的模型”](https://thenewstack.io/openai-releases-new-models-trained-for-developers/)，而 [Sam Altman 在 X 上发文](https://x.com/sama/status/1911830886896799931)表示开发者对它们“看起来非常满意”。

## Luna 定价藏有细节

Luna 是 GPT-6 中速度最快、价格最低的层级，在纸面上它涵盖了 GPT-4.1 提供的基础功能，具有 [105 万个 Token 的上下文窗口](https://developers.openai.com/api/docs/models/gpt-6-luna)、结构化输出和函数调用。每百万输入 Token 收费 0.10 美元，每百万输出 Token 收费 0.50 美元，它比 [GPT-5.6 Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/) 更便宜，后者的输入收费是其两倍，输出则是每百万 Token 1.20 美元。

一旦提示词超过 272,000 个输入 Token，整个请求的输入速率就会翻倍，输出速率则会提高 50%。这可能会蚕食 RAG 管道以及处理大型代码库的编码智能体所节省的成本。

OpenAI 的[迁移指南](https://developers.openai.com/api/docs/guides/latest-model)指出，GPT-6 Luna 默认采用中等推理工作量，但仅支持通过将 `reasoning_effort=none` 设置为参数来进行 Chat Completions 的函数调用。结合推理和工具调用需要使用 Responses API。启用推理也排除了温度（temperature）、`top_p`、`top_logprobs` 和 `logprobs`，而 GPT-4.1 对所有这些都提供了支持。

该公司建议使用 Codex 中的 Docs 技能来跨项目更新 API 调用，但这些更改无法解释模型行为上的差异。Anthropic 上个月也遇到了类似的问题，当时 [Opus 5.5 引入了四个破坏性变更](https://thenewstack.io/claude-opus-agent-migration/)，导致现有的智能体集成中出现 400 错误。其他更改则改变了智能体的行为而没有触发错误，使得这些回归问题更难以捕捉。

## Luna 不支持微调

新的自助式微调任务将于 2027 年 1 月 6 日结束，即 GPT-4 模型退役前八天。现有的微调模型将继续提供推理请求，直到 1 月 14 日，这留出了一个很短的窗口期来并行运行替代模型。

> 新的自助式微调任务将于 2027 年 1 月 6 日结束，即 GPT-4 模型退役前八天。

## 承诺六个月，实际给三个月

其他截止日期在 [OpenAI 的弃用时间表](https://developers.openai.com/api/docs/deprecations)上，其中包括 GPT-4.1 nano、第一个 GPT-4o 快照，以及定于 10 月 23 日退役的更早的 GPT-3.5、GPT-4 和 o 系列模型。GPT-5 和 o3 快照紧随其后，定于 12 月 11 日退役，选定的传统音频、实时和转录模型则计划于 2027 年 1 月 20 日退役。GPT-5.1、GPT-5.3-Codex 和 GPT-5.4-Nano 定于 4 月 1 日退役。

List models API 现在包含一个 `shutdown_date` 字段，使得自动检查即将到来的退役成为可能。需要更多时间的客户或许可以通过专用容量让旧模型继续运行，尽管他们必须与 OpenAI 的销售团队进行协商。

三个月的警告期也短于 OpenAI 自己的弃用政策，该政策承诺对一般可用模型给予至少六个月的通知。该政策允许出于安全或合规原因的例外情况，但对于为什么 GPT-4o 和 GPT-4.1 只获得一半时间的原因，目前没有任何解释。

> 三个月的警告期也短于 OpenAI 自己的弃用政策，该政策承诺对一般可用模型给予至少六个月的通知。