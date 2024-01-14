<!--
title: 开源支撑下的Perplexity不止于OpenAI套壳
cover: https://cdn.thenewstack.io/media/2024/01/b293c498-perplexity_jan24-1024x550.jpg
-->

Perplexity CEO Aravind Srinivas 是谷歌创始人Larry Page的忠实粉丝。但是他认为自己找到了一种方法，不仅能与谷歌搜索竞争，还能与OpenAI的通用预训练transformer(GPT)竞争。

> 译自 [More than an OpenAI Wrapper: Perplexity Pivots to Open Source](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/)，作者 Richard MacManus 是 The New Stack 的高级编辑，他写关于网络和应用程序开发趋势的文章。此前他于 2003 年创立了 ReadWriteWeb，并将其打造成为世界上最具影响力的科技新闻网站之一。从早期......

AI 搜索引擎 [Perplexity](https://www.perplexity.ai/) 最近因其可作为 ChatGPT 的替代选择而获得了很多关注。与 ChatGPT 不同，Perplexity 默认为它提供的信息引用来源。这一单一功能已成为生成式 AI 的关键，鉴于这项技术持续存在的“幻象”问题。相应地，尽管 OpenAI、微软、谷歌和 Meta 主导着这个市场，但 Perplexity 已成为一个出人意料的强劲竞争者。

我与 Perplexity 联合创始人兼 CEO [Aravind Srinivas](https://www.linkedin.com/in/aravind-srinivas-16051987/)(此前是 OpenAI 和 DeepMind 的研究员)进行了交谈，以进一步了解该产品，包括其最近关注开源语言模型的重点。请注意，本次采访是在该公司本月早些时候宣布 [7360 万美元 B 轮](https://www.reuters.com/technology/perplexity-ai-valued-520-mln-funding-bezos-nvidia-2024-01-04/)融资之前进行的，这在财务上将其推向了大联盟。

![放大](https://cdn.thenewstack.io/media/2024/01/422ccb21-perplexity_js_answer-1024x516.png)

*Perplexity 对 JavaScript 问题的回答。响应中的每个数字都是所引用信息来源的可点击链接。*

## 不仅仅是套壳

Perplexity 的核心是搜索引擎。Srinivas 告诉我，他是“Larry Page的忠实粉丝”，从一开始，当 Perplexity 在 2022 年 12 月推出时，他就想挑战谷歌的搜索引擎。然而，[当时](https://twitter.com/perplexity_ai/status/1600551871554338816) Perplexity 依赖于 OpenAI 的 GPT 3.5 模型和微软必应。它只是 AI 工程社区中一个流行的(且有些贬义)术语“套壳”的其他公司技术。

但在过去的一年中，Perplexity 进化迅速。它现在拥有自己的搜索索引，并基于开源模型构建了自己的语言模型。他们也开始结合自己的专有技术产品。 11月底，Perplexity 宣布了两个新的“在线语言模型”——与搜索索引相结合的语言模型，名为 pplx-7b-online 和 pplx-70b-online。它们是在开源模型 mistral-7b 和 llama2-70b 的基础上构建的。

“我们在 LLaMA-2 发布的那一天就开始使用开源模型”，Srinivas 说，指的是 Meta 在 2023年7月发布的其第二代 LLaMA 模型(名称是“大型语言模型 Meta AI”的首字母缩写)。 当一家名为 Mistral AI 的法国公司在 9月发布了一个名为 Mistral 7B 的开源语言模型时，他们也注意到了。 在那之后，Perplexity 成为不仅仅是一个套壳的策略开始成形。

“这两者之间存在良性竞争”，Srinivas 谈到 Meta 和 Mistral 时说。“这使我们受益，因为我们就像，'好的，我们是这些模型的用户。' 比如，我们要把你的聊天机器人套壳成一个非常高效、快速的推理，我们自己托管——所以我们不是一个套壳。 然后我们会自定义它，根据我们的模型、我们的产品进行微调——这是搜索用例的摘要——然后我们会将其部署给终端用户。”

使用开源模型对 Perplexity 的增长至关重要。 Srinivas 指出“Mistral 的最新模型与我们在 Perplexity 一年前开始使用的 GPT 3.5 一样强大——如果不是更强大的话。”

除了后端技术，Perplexity 的用户界面也与时俱进。其默认界面仍然是聊天机器人(类似 ChatGPT)，但 Perplexity 现在提供了它所说的“Copilot 搜索”——“请求详细信息，考虑您的偏好，深入研究，然后提供精确的结果。”

## Perplexity 对比 ChatGPT

为了快速演示 Perplexity 和 ChatGPT 之间的区别，我向两种产品提出了以下问题:“JavaScript 如何在现代 Web 应用程序中使用？”

首先，披露一下: 在访谈前夕，Perplexity 赠予我一年的 Pro 账户，以便更好地测试其产品。我已经是 ChatGPT Plus 用户，我自己支付费用，所以我能够对两家公司的高级产品进行公平比较。两家公司每月收取 20 美元的高级服务费用。Perplexity Pro 使您能够“从 GPT-4、Claude 2.1、Gemini 或 Perplexity 中选择首选的 AI 模型”。

回答我的查询，ChatGPT 4 回复了一个 10 点的功能和好处列表——包括 JavaScript 在用户交互和实时 Web 应用程序中的使用。这是一个不错的概要，虽然比较高层次，我发现有几行我想验证的。

Perplexity 的答案来自默认的 Perplexity 模型，它更像一篇短文。它与 ChatGPT 一样出色，但它还包括了超过 20 个引文。Srinivas 说，其默认模型基于 GPT-3.5 的微调版本，加上一点 LLaMA-2 —— “我们以某种方式将两者结合在一起。”

![放大](https://cdn.thenewstack.io/media/2024/01/50b8bae8-perplexity_sources-993x1024.png)

*Perplexity 引文*

我用 Perplexity 的“实验”模型尝试了相同的查询，Srinivas 说这是“在内部使用 LLaMA-2 进行微调的”。响应更短，我觉得它不太全面。但这是实验性的，所以您的结果可能会有所不同。事实证明，简洁是其目标之一。

“实验模型并不比 GPT-4 更好”，Srinivas 解释道。“你从中得到什么？它的简洁性[和]事实准确性，没有任何道德化行为。”

## Perplexity 的下一步

如上所述，默认的 Perplexity 模型仍然依赖于 GPT 3.5(和一点 LLaMA-2)。但其意图是摆脱长期依赖 OpenAI 的基础模型。

“我们现在在未来一个季度左右的目标是完全转移所有人到我们的 Perplexity 模型”，Srinivas说。“现在有了选择——我们可以使用 LLaMA-2 作为基础模型，也可以使用新的 Mistral 作为基础模型。”

在搜索方面，我问 Perplexity 的搜索索引与谷歌的搜索索引相比，目前的规模如何？

“我们的索引中有10亿个页面，”他回复道。“但，你知道，我想强调的主要观点是[ ]搜索索引的大小也像大型语言模型的大小一样——索引有多大并不重要。更重要的是数据的质量有多高;有多少高质量的网页？”

他指出，其搜索排名机制类似于谷歌，因为它依赖引文，但有语言模型的特点。Perplexity 的产品引用某个网页的次数越多，它就越重要。为了解释，Srinivas 再次提到了他的偶像Larry Page。

“类似于Larry Page的洞察力，他说网络中重要的网页是那些被其他重要网页引用的网页。只不过我们说的是，网络上重要的网页是那些被大型语言模型引用的网页，在会话式答案引擎的上下文中——聊天机器人。如果越来越多的人定期使用它，我们就会知道网络上越来越多重要的网页——[...]它们被引用的频率，它们是否真的使答案变得更好或更糟。”

鉴于谷歌(拥有Bard)和微软(拥有Bing)已经开始在其AI聊天机器人中也使用引文，Perplexity 在未来一年可能面临艰巨的挑战。但对于一个新融资的年轻创业公司来说，其产品已经很吸引人，而转向开源语言模型似乎是应对这些大型科技企业的最佳方式。
