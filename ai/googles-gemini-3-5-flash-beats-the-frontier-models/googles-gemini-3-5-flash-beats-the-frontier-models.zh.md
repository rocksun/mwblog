在其 I/O 开发者大会上，Google 于周二发布了两款新的 AI 模型：[Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/#gemini-3-5-flash)，这是其 Gemini 系列中的最新模型，以及 Gemini Omni Flash，这是一款全新的多模态模型，正如 Google 所言，它可以“根据任何输入创建任何内容”。

## Gemini 3.5 Flash

Gemini 3.5 Flash 是 Gemini 3.5 系列中的第一个模型。Pro 版本仍在开发中，预计将于下个月发布，但即使是 3.5 Flash 在大多数基准测试中也超越了现有的 3.1 Pro 模型。

例如，在 [TerminalBench 2.1](https://www.tbench.ai/leaderboard/terminal-bench/2.1) 中，使用 Gemini CLI 解决编程问题时，3.1 Pro 目前得分为 70.3%，而 3.5 Flash 的得分则达到了 76.2%。

虽然这还比不上 OpenAI 的 GPT 5.5，但对于一个 Flash 模型来说，这已经是非常稳健的表现了。

新的 Flash 模型在其他基准测试中也获得了优于 3.1 Pro 的类似结果，包括 GDPval-AA（1656 Elo 对比 1314）、MCP Atlas（83.6% 对比 78.2%）以及 CharXiv 推理（84.2%）。

![](https://cdn.thenewstack.io/media/2026/05/77119212-gemini-3-5__benchmarks__dark-1024x767.jpg)

Gemini 3.5 Flash 基准测试。图片来源：Google。

但或许更有趣的是，它在相当多的基准测试中具有竞争力，有时甚至超越了 OpenAI 的 GPT-5.5 和 Anthropic 的 Opus 4.7 等旗舰模型。

在工具使用基准测试中尤其如此。正如 Google 首席执行官 Sundar Pichai 在今天发布会前的媒体简报中所指出的，Gemini 3.5 Flash 是“将前沿智能与行动相结合的一系列模型中的首个”。

他指出，Flash 接近于最顶尖的前沿模型，而且速度非常快。Artificial Analysis 将其排在 OpenAI 和 Anthropic 的前沿模型之后，但其每秒生成 Token 的速度明显更快（接近每秒 280 个 Token，而 GPT-5.5 和 Opus 4.7 约为 60 或 70 个）。

“Flash 的惊人之处在于，它以不到一半的价格——在某些情况下几乎只有同类前沿模型三分之一的价格——提供了前沿级别的能力，”Sundar Pichai 指出。

Google 指出，3.5 Flash 在运行长周期代理任务（包括代理编码）方面表现尤为强劲。这也是为什么该模型成为 Gemini Spark 核心的原因，Gemini Spark 是 Google 在 I/O 大会上推出的全新个人 AI 代理（目前仅向受信任的测试人员开放）。

鉴于 Flash 模型的能力，Pro 模型可能至少会与来自 OpenAI 和 Anthropic 的同类模型旗鼓相当，并可能在至少某些基准测试中超越它们。

## Gemini 3.5 Flash 可用性

Gemini 3.5 Flash 现在可通过 Google AI Studio 和 Android Studio 中的 Gemini API、Gemini Enterprise Agent Platform（又名 [Vertex AI](https://thenewstack.io/google-gemini-agent-platform/)）、Gemini Enterprise 以及 Google Antigravity 使用。

对于消费者，它也可以在 Gemini 应用和 Google 搜索的 AI 模式中使用。

![Gemini Omni Flash, Google I/O, 2026年5月19日](https://cdn.thenewstack.io/media/2026/05/c838ae3b-screenshot-2026-05-19-at-13.30.31-1024x660.png)

图片来源：*The New Stack*

## Gemini Omni

Gemini Omni 是一款略有不同的模型。在某种程度上，Gemini 模型一直被设计为多模态，但 Omni 将这一特性推向了更深层次。在当前版本中，它有点像 Veo（Google 的视频生成模型），但随着时间的推移，它也将支持图像和音频。

因此，尽管 Google 表示 Omni 可以“根据任何输入创建任何内容”，但目前它仅从视频开始。在过去的一年左右时间里，视频领域取得了长足的进步，Omni 将用户现在对图像模型的许多期待能力带到了视频领域。

与 Gemini 3.5 一样，Omni 目前也仅发布了 Flash 模型，它允许用户更改视频中的特定内容。例如，可以通过添加新角色和对象，或者改变环境、角度和风格，来完全重塑镜头。Google 表示它可以做到这一点，且“绝不会丢失原始场景的连贯性”。

正如 Google 所强调的（其他前沿实验室往往也对其视频模型持相同观点），Omni 的世界模型对重力、动能和流体动力学具有“直观”的理解，这应当能产生逼真的场景。

因为它具有多模态属性（或很快就会具备），Omni 可以接受图像、文本、视频和音频（或这些的任何组合）作为输入来构建最终场景。

![](https://cdn.thenewstack.io/media/2026/05/639626ea-rt_wm_omni__sizzle__sailor__260517.gif)

使用 Gemini Omni 创建。图片来源：Google。

## 为您（及周围人）的安全而设计的数字分身

生成式视频容易被用于深度伪造（deepfakes）和虚假信息活动。Google 表示，它“致力于负责任地开发 AI，并拥有明确的政策来保护用户免受伤害，并监管我们 AI 工具的使用”。在实践中，这意味着你目前可以使用自己的声音和自己的形象化身来创建视频。

“除了分身功能，在编辑视频以改变音频和演讲方面，我们仍在努力进行测试，以更好地了解如何负责任地将这种能力带给用户，”Google 表示。

所有使用 Gemini Omni 创建的视频都将包含 Google 的 SynthID 水印。