OpenAI 宣布，其已将 ChatGPT 中的默认模型替换为 [GPT-5.5 Instant](https://deploymentsafety.openai.com/gpt-5-5-instant/introduction)，据称该模型能够提供更快的响应、更简洁的回答以及更少的错误陈述。

该模型继承了 [3 月推出的](https://thenewstack.io/openai-gpt-5-1-instant/) GPT-5.3 Instant，专为写作、分析和通用查询等日常任务而设计。OpenAI [在博客文章中指出](https://openai.com/index/gpt-5-5-instant/)，“准确性”是该模型的核心卖点。

该公司写道：“Instant 现在更加可靠，在事实性方面有了全面且显著的提升，尤其在对准确性要求最高的领域进步最为明显。”

## 专注于日常使用

简单回顾一下，OpenAI 在 4 月 [发布了其旗舰模型 GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/)，并称其为旨在处理更复杂推理任务的“新一类智能”。GPT-5.5 Instant 作为其轻量化版本并存，处理日常查询，而更繁重的工作可以交给更高端的模型。

这种定位建立在 OpenAI 3 月份对 GPT-5.3 Instant 引入的变革之上。当时，公司表示该模型将减少其所谓的“说教式”响应并减少不必要的拒绝，旨在更直接地回答用户查询。

GPT-5.5 Instant 延续了这一总体精神。重点不在于那些花哨的功能，而在于 ChatGPT 在日常使用中的表现——它希望变得更讨人喜欢。

这些改进反映在视觉推理、数学和科学评估的进步上。例如，在 CharXiv 科学图表推理基准测试中，GPT-5.5 Instant 的得分为 81.6%，高于 GPT-5.3 Instant 的 75.0%。在 MMMU-Pro（一个由学术研究人员开发的多模态推理基准测试）上也有类似的提升，其得分达到 76.0%，而此前为 69.2%。

值得注意的是，这些结果基于 OpenAI 的自述报告，且该公司尚未提供与竞争模型的更广泛对比。

![条形图显示 GPT-5.5 Instant 在 CharXiv 和 MMMU-Pro 推理基准测试中的表现优于 GPT-5.3 Instant](https://cdn.thenewstack.io/media/2026/05/e0d6d248-screenshot-2026-05-05-at-19-46-57-gpt-5.5-instant-smarter-clearer-and-more-personalized-openai.png)

*条形图显示 GPT-5.5 Instant 在 CharXiv 和 MMMU-Pro 推理基准测试中的表现优于 GPT-5.3 Instant。*

在发布模型的同时，OpenAI 正更加强调 ChatGPT 如何使用和解释个人数据。

与以前一样，模型可以利用个人上下文，包括过去的对话、上传的文件和连接的服务。然而，OpenAI 表示，现在正在所有 ChatGPT 模型中引入“记忆源”，这可以显示响应中使用了哪些输入，并允许用户将其删除。

OpenAI 写道：“当响应被个性化时，你可以看到使用了哪些上下文，例如保存的记忆或过去的聊天记录，并在某些内容过时或不再相关时将其删除或更正。”

![ChatGPT 中的记忆源](https://cdn.thenewstack.io/media/2026/05/064897d0-0501_blog__1_-1024x689.png)

*ChatGPT 中的记忆源*

OpenAI 表示，该功能旨在让个性化更易于理解，尽管它可能无法捕捉响应背后的每一个输入。在某些情况下，它只会显示最相关的过往聊天或记忆，而不是系统引用的所有内容；该公司表示计划随着时间的推移扩大这种可见性。

## **竞争模型与可用性**

OpenAI 并不是唯一一家在日常使用中推行更快速、低成本模型的公司。Google 拥有用于低延迟任务的 [Gemini Flash](https://thenewstack.io/googles-new-gemini-3-flash-rivals-frontier-models-at-a-fraction-of-the-cost/)，而 Anthropic 则 [提供 Claude Haiku](https://thenewstack.io/anthropic-launches-claude-haiku-4-5/) 以实现更快速、更便宜的响应。

GPT-5.5 Instant 属于同一类别，旨在处理大多数用户请求，而更复杂的任务在需要时由更重型的模型处理。

定价对于 GPT-5.5 Instant 来说并不是一个重要因素，因为它被定位为 ChatGPT 内部的默认模型，其使用成本被捆绑在订阅层级中，而不是直接暴露在模型层面。更强大的模型仍可通过 API 提供给开发者，而在生产环境中，成本和性能的权衡更为关键。

GPT-5.5 Instant 现已作为 ChatGPT 的默认模型开始推送。