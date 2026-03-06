<!--
title: OpenAI发布GPT-5.4，智能思考与专业版双重升级
cover: https://cdn.thenewstack.io/media/2026/03/a9b3b8af-5.4-thinking_hero-seo-1024x576.png
summary: OpenAI推出GPT-5.4 Thinking和Pro版，作为最强专业模型。它提升了编码、搜索与上下文能力，错误率更低。API用户享百万token窗口，价格上涨但效率更高，并在知识型工作表现卓越。
-->

OpenAI推出GPT-5.4 Thinking和Pro版，作为最强专业模型。它提升了编码、搜索与上下文能力，错误率更低。API用户享百万token窗口，价格上涨但效率更高，并在知识型工作表现卓越。

> 译自：[OpenAI launches GPT-5.4 Thinking and Pro](https://thenewstack.io/openai-launches-gpt-5-4/)
> 
> 作者：Frederic Lardinois

[OpenAI](https://openai.com/) 周四[推出了 GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)，这是其前沿模型的下一个版本。该公司称其为“最强大、最高效的专业工作前沿模型”，并指出它结合了最近发布的 [GPT-5.3-Codex](https://thenewstack.io/openais-gpt-5-3-codex-helped-build-itself/) 模型的编码能力，并改进了对电子表格、文档和演示文稿的支持。

该公司认为，新模型在搜索网络和为需要更长思考时间的查询维护上下文方面表现更好。此外，OpenAI 改进了模型的计算机使用能力，现在允许它在拥有相当多可用工具的生态系统中更高效地选择合适的工具。

OpenAI 声称，这也是该公司迄今为止最真实可靠的模型，“与 GPT-5.2 相比，响应错误率降低 18%，单项声明虚假率降低 33%。”

随着 GPT-5.4 的推出，该公司也取消了面向 API 用户的百万 token 窗口的 Beta 标签。Codex 现在也将支持这个扩展的 token 窗口，但超过 272,000 个 token 的请求将按 2 倍费率计入使用限制。

一个特别有趣的新功能是 GPT-5.4 Thinking 现在可以提前展示其思考计划，允许用户在模型工作时中途引导模型，确保它不会走弯路，同时避免在每次转向之间消耗数千个 token。

You可能想知道：OpenAI 不是在本周早些时候才推出 [GPT-5.3-Instant](https://thenewstack.io/openai-gpt-5-1-instant/) 吗？是的。OpenAI 的版本控制一直有点奇怪，但看起来对于主流模型，我们在这里又跳过了一个版本。5.3-Instant 仍将是 ChatGPT 中的主力模型。

![OpenAI GPT-5.4 基准测试。](https://cdn.thenewstack.io/media/2026/03/a714095d-screenshot-2026-03-05-at-9.07.12-am.png)

*OpenAI GPT-5.4 基准测试（图片来源：OpenAI）。*

## 模型更昂贵，但 token 使用量更少

新模型将提供 Thinking 和 Pro 版本。GPT-5.4 Thinking 将在 ChatGPT、API 和 Codex 代理编码应用中可用。

显著更昂贵的 GPT-5.4 Pro 将仅在 ChatGPT 和 API 中可用，但不在 Codex 中提供。这可能更好。每百万输入/输出 token 30 美元/180 美元（GPT-5.2 Pro 定价为 21 美元/168 美元），5.4 Pro 是 OpenAI 迄今为止最昂贵的模型，你不会希望被这些账单吓到。

同样的涨价也适用于标准 Thinking 模式，其每百万输入/输出 token 将花费 2.50 美元/15 美元，高于之前的 1.75 美元/14 美元。

![](https://cdn.thenewstack.io/media/2026/03/54ffb405-screenshot-2026-03-05-at-9.35.28-am.png)

*OpenAI GPT-5.4 定价（图片来源：OpenAI）。*

然而，OpenAI 认为，更新后的模型在 token 使用方面效率更高。“GPT-5.4 是我们迄今为止最节省 token 的推理模型，与 GPT-5.2 相比，它使用显著更少的 token 来解决问题——这意味着更低的 token 使用量和更快的速度，”OpenAI 在其公告中指出。

“在 API 中，GPT-5.4 的每个 token 定价高于 GPT-5.2，以反映其改进的能力，而其更高的 token 效率有助于减少许多任务所需的 token 总数，”OpenAI 写道。“批量和弹性定价以标准 API 费率的一半提供，而优先处理以标准 API 费率的两倍提供。”

## 基准测试

在标准基准测试中，新模型毫不意外地以显著优势超越其前代产品。即使在编码任务中也是如此，新模型甚至在 SWE-Bench Pro 基准测试中击败了 OpenAI 自己最近发布的 Codex（以及 Google 的 [Gemini 3.1 Pro](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/)）。

在代理使用场景和计算机使用方面，GPT-5.4 Thinking 也表现出色，大部分得分领先于 Anthropic 的 Opus 4.6 和 Google 的 Gemini 3.1 Pro。

对于大多数这些任务，OpenAI 强调新模型在取得这些结果的同时，仍比其前代产品使用更少的 token。

## 更擅长知识型工作

GPT 5.4 Pro 鉴于其高昂的价格，在 OpenAI 提供的基准测试中并不总是比 Thinking 版本表现显著更好。它在 BrowseComp 代理浏览测试中表现更佳，但很少有用户会为此使用 Pro 版。然而，它擅长解决高级数学问题，在 FrontierMath 基准测试中，解决最复杂问题的得分率为 38%，而 Thinking 版本的得分率为 27.1%。

有一个领域，也许是大多数知识工作者应该关注的领域，是它在 GDPval 基准测试中的得分，该测试评估模型处理 44 种职业中实际任务的能力。在该测试中，新模型得分 83%，这意味着在 83% 的比较中，它与行业专业人士持平或超越。Anthropic 的 Opus 4.6 在该测试中得分 79.5%。

OpenAI 还进行了一些内部基准测试。“在一组演示文稿评估提示中，人工评估者在 68.0% 的时间里更喜欢 GPT-5.4 生成的演示文稿，而不是 GPT-5.2 生成的，原因在于其更强的审美、更丰富的视觉多样性和更有效的图像生成使用，”OpenAI 写道。

在另一个内部基准测试中，该模型在一个模拟初级投资银行家工作的电子表格任务中得分 87.5%。

Box 在其早期测试中也看到了类似的改进。“在 Box 比较 GPT-5.2 和 GPT-5.4 的评估中，我们复杂提取任务数据集的整体性能从 72% 提高到 78%。这些成果表明，单次从文档中提取多条信息的能力增强，包括需要多步推理的任务——这是推动和支持企业工作流的关键能力，”Box 人工智能主管 Yashodha Bhavnani 在一份声明中说。

## 可用性

新模型现在正在 ChatGPT 和 Codex 中推出。Thinking 版本将提供给 Plus、Team 和 Pro 用户（企业版和教育版用户需要其管理员启用），而 Pro 模型仅适用于 Pro 和企业版套餐用户。

新模型将在 API 中以 `gpt-5.4` 和 `gpt-5.3-pro` 的形式提供。

![](https://cdn.thenewstack.io/media/2026/03/8d829e62-gpt-5.4-in-chatgpt-scaled.png)

*图片来源：OpenAI。*