谷歌周四发布了其Gemini Pro模型的最新版本。虽然它并非在所有任务上都表现最佳，但官方仍处于预览阶段的Gemini 3.1 Pro，在解决复杂问题方面比谷歌之前的主流模型表现好得多——至少根据基准测试是这样。

最近几周，Anthropic和[OpenAI都发布了不少模型](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/)。本月早些时候，谷歌发布了Gemini 3 Deep Think，该模型具有专门的推理模式，性能轻松超越Gemini 3.1 Pro。但该模型仅供[Google AI Ultra订阅者](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/)使用，API访问仍然是邀请制（并且可能需要额外付费）。

据谷歌称，Gemini 3.1 Pro的“核心智能”直接源自Deep Think模型，这解释了为何3.1 Pro在推理基准测试中表现如此出色。

在ARC-AGI-2上，该基准包含一系列对人类来说简单但对大型语言模型而言非常困难的推理任务，谷歌的新模型现在得分77.1%。这比上一代Gemini Pro的31.1%有了显著提升。[Anthropic的Opus 4.6解决了](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/)68.8%的这些挑战，而OpenAI的GPT-5.2（也即将更新）的正确率为52.9%。

通常，所有这些数据都由谷歌自行报告，但Artificial Analysis现在也已将Gemini 3.1 Pro[置于其排行榜首位](https://artificialanalysis.ai/leaderboards/models/)。

![](https://cdn.thenewstack.io/media/2026/02/cd165179-gemini_3-1-pro__benchmarks-scaled.png)

Gemini 3.1 Pro 基准测试（图片来源：谷歌）。

## 大致出色

Gemini 3.1 Pro的推理能力在大多数基准测试中也得到了体现，该模型在其中大多数测试中都领先于竞争对手。

然而，一个主要的遗憾是它在GDPval-AA上的表现不佳，该基准衡量模型在一系列现实世界任务（可能影响一个国家的GDP）上的性能。在那里，该模型不知何故地只获得了1317分，远远落后于Anthropic的Sonnet 4.6的1633分。

至于编程方面，Gemini 3.1现在在Terminal-Bench 2.0智能编程基准测试中也几乎超越了所有竞争对手，尽管OpenAI报告称其最近发布的5.3-Codex编程模型在使用其自身测试框架时得分显著更高（谷歌没有报告使用其自身测试框架的得分，仅报告了基于默认的[Terminus-2测试框架](https://harborframework.com/docs/agents/terminus-2)的基准测试结果）。

在几乎所有其他编程基准测试中，它也要么领先于竞争对手，要么仅相差几个百分点。

与其他Gemini模型一样，Gemini 3.1 Pro具有100万个token的上下文窗口。然而，虽然它可以摄取文本、图片、视频和音频，但其输出被限制在64,000个token。

## 定价

新模型的定价保持不变，每百万输入/输出token分别为2美元/12美元。这使得它（在相似或更优的性能下）比Anthropic的Opus 4.6（每百万输入/输出token成本为5美元/25美元）更实惠。

## 可用性

官方而言，Gemini 3.1 Pro仍处于预览阶段，但谷歌已使其广泛可用。对于开发者而言，新模型现在可通过Google AI Studio、Gemini CLI、Android Studio中的Gemini API以及[Google Antigravity开发平台](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/)访问。

企业可以通过Vertex AI和Gemini Enterprise使用它，而消费者则可以通过Gemini应用程序和NotebookLM获取。