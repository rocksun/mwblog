OpenAI 今日发布了 GPT-5.1-Codex-Max，这是其 GPT-5.1-Codex 基础模型的全新变体，专门针对编码任务进行了优化，并为 OpenAI 的 Codex 代理提供支持。

最初的 [Codex 模型](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/) 于大约两个月前推出，当时在大多数基准测试中极具竞争力，并常常领先。但在这个领域，没有人原地踏步。OpenAI 自己在几天前推出了其 GPT 模型（包括 Codex）的 5.1 版本，而本周早些时候推出的 [Google 的 Gemini 3](https://thenewstack.io/google-launches-gemini-3-pro/) 也推动了前沿模型在编码方面的进步。

OpenAI 表示，Codex-Max 专门针对软件工程、数学、研究等领域的代理任务进行了训练。它旨在处理长时间运行的任务；OpenAI 强调，这也是该公司训练的第一个能够跨越多个上下文窗口工作的模型。通过使用压缩技术将上下文压缩成更易于管理的单元，OpenAI 声称 Codex 代理现在可以在“单个任务中处理数百万个 token”。

[![展示 OpenAI Codex-Max 模型在 SWEbench-verified 基准测试中表现的图表。](https://cdn.thenewstack.io/media/2025/11/22f94223-openai-codex-max-swe.png)](https://cdn.thenewstack.io/media/2025/11/22f94223-openai-codex-max-swe.png)

来源：OpenAI。

## Codex-Max 的基准测试表现如何？

这很可能是 Codex-Max 在标准编码基准测试中表现出色的部分原因。例如，在最高设置下，Codex-Max 在 SWE-Bench Verified 基准测试中得分 77.9%，该测试旨在评估代理处理多个流行 Python 项目的实际 pull request 的能力。

GPT-5.1-Codex 模型在高设置下得分 73.1%，[Anthropic 的 Sonnet 4.5](https://thenewstack.io/anthropic-launches-claude-sonnet-4-5/) 得分为 77.2%（尽管加上测试时计算量，得分为 82%），而 Google 的新 Gemini 3 得分为 76.2%。

在 TerminalBench 上，Codex-Max 得分 58.1%，而 GPT-5.1-Codex 达到 52.8%，Sonnet 4.5 为 50%，Gemini 3 为 54.2%。

[![](https://cdn.thenewstack.io/media/2025/11/847cf7d6-codex-bench.png)](https://cdn.thenewstack.io/media/2025/11/847cf7d6-codex-bench.png)

GPT-5.1-Codex-Max 基准测试（来源：OpenAI）。

## Codex-Max 是否更好且更便宜？

与大多数现代模型一样，Codex-Max 将具有不同的推理模式，这些模式决定了模型可以为给定任务使用的推理 token 数量。对于 Codex-Max，OpenAI 增加了一个新的“超高”（xhigh）模式，允许开发者进一步推动模型的重写能力。这显然会增加延迟，并且可能不适用于所有用例，但确实能将准确性提高几个百分点。

然而，基准测试并非万能。模型在实际任务中的表现如何仍有待观察。

但对于开发者来说（尤其是那些使用 API 的开发者）可能更重要的是，在 OpenAI 的测试中，Codex-Max 经常能够用更少的 token 和工具调用产生相似或更好的结果——并且它产生的代码行数更少就能达到相同的结果。因此，OpenAI 认为 Codex-Max 在实际编码任务上比其前代产品快 27% 到 42%。

不过，它肯定会在 Windows 机器上表现出色。OpenAI 指出，这是该公司训练的第一个能在 Windows 环境下运行的模型。

## Codex-Max 的可用性如何？

新模型现在可在 Codex 的 CLI、IDE 扩展、云和代码审查中使用，并且将提供给所有拥有 ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划的用户。希望通过 API 密钥在 Codex 中使用它的用户即将获得访问权限。