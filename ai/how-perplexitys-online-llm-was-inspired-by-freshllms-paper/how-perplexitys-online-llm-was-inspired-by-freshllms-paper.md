<!--
title: FreshLLM论文如何启发了Perplexity的在线LLM
cover: https://cdn.thenewstack.io/media/2024/01/1bafcfb2-marten-newhall-uafjfsms3yy-unsplash-1024x683.jpg
-->

我们深入探讨Perplexity Copilot背后的技术，这一灵感来自于提出搜索引擎增强LLMs的FreshLLMs论文。

> 译自 [How Perplexity’s Online LLM Was Inspired by FreshLLMs Paper](https://thenewstack.io/how-perplexitys-online-llm-was-inspired-by-freshllms-paper/)，作者 Janakiram MSV。

Perplexity 自 2023 年 12 月在 [AWS re:Invent 主题演讲](https://thenewstack.io/aws-goes-deep-on-ai-chip-power-and-cost-savings/)中首次亮相以来，[一直备受关注](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/)。受到这一方法的吸引，我在其推出时注册了 Copilot。在我可以使用的许多 AI 助手中，我发现[Perplexity](http://www.perplexity.ai/)的 Copilot 是最实用和功能最强大的。这是因为它结合了生成式人工智能和传统的搜索体验，给予了我最好的两全其美的选择。我很快就用它的搜索助手替代了默认搜索引擎。

![Zoom](https://cdn.thenewstack.io/media/2024/01/50a10e49-prplx-copilot-856x1024.jpg)

*Perplexity用户界面*

现在让我们了解Perplexity人工智能的 Copilot 背后的技术。

目前，大型语言模型（LLMs）面临两个主要挑战：过时的数据和[幻觉](https://thenewstack.io/stopping-ai-hallucinations-for-enterprise-is-key-for-vectara/)。由于基础模型的截止日期基于其预训练数据集，它们无法使用最新的数据进行响应。即使是最强大的模型也往往会编造答案，导致幻觉。

第一个问题，即无法访问最新数据，可以通过进行网络搜索并将输出馈送给 LLM 以帮助其做出明智的决策来解决。这可以通过集成 [SerpAPI](https://serpapi.com/) 等 API 来实现，它提供对 Google 搜索的程序化访问。每次发送提示时，LLM 判断是否需要访问网络，然后在需要时调用搜索 API。从多个来源获取的抓取内容然后被汇总并作为上下文添加到提示中，这使得 LLM 能够以有用且有意义的方式回应。

![Zoom](https://cdn.thenewstack.io/media/2024/01/846295e3-online-llms-1024x798.png)

与幻觉相关的第二个问题可以通过一种经过验证的技术来解决，这就是检索增强生成（[Retrieval Augmented Generation](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/)，RAG）。与之前动态调用搜索 API 的方法不同，RAG 期望从一个众所周知的数据存储中检索数据，比如[向量数据库](https://thenewstack.io/vector-databases-long-term-memory-for-artificial-intelligence/)或由外部维护的全文搜索索引。

![Zoom](https://cdn.thenewstack.io/media/2024/01/867046bc-rag-llms-1024x725.png)

重要的是要注意，第一种方法最适用于从公共领域的数据构建的上下文。如果您正在构建一个基于内部和对组织内部数据的私有数据进行问答或摘要的应用程序，那么 RAG 是理想的解决方案。

Perplexity人工智能在其 Copilot 中更多地依赖于基于搜索引擎的方法。对于需要访问私有数据的用例，它提供了一个与 OpenAI 兼容的 API，可以与 RAG 一起使用。

## FreshLLMs：为LLM带来最新数据

Perplexity人工智能受到了论文《[FreshLLMs](https://arxiv.org/abs/2310.03214)：[使用搜索引擎增强的大型语言模型进行刷新](https://arxiv.org/abs/2310.03214)》中解释的机制的启发，该论文提出了搜索引擎增强的LLMs。类似于RAG如何将上下文注入提示中，FreshLLMs倡导从搜索中按发布日期排序的热门摘要注入提示的思想。除了添加上下文之外，它还提议使用[少量示例提示](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)，教导LLM如何基于一些示例做出响应。

FreshLLM将问题分为四类：

- **永不变化**的答案，几乎永远不会变化。
- **慢变**的答案可能在几年的时间内发生变化。
- **快速变化**的答案，如航班状态和天气，可能会多次变化。
- **错误前提**，问题在事实上是不正确的，需要被驳斥。

该论文的作者创建了一个包含600个问题的数据集，分为上述类别。称为FRESHQA基准，它涉及测试模型准确回答问题的能力，通过超过50,000个判断的人工评估来评估事实的正确性。评估使用两种模式：RELAXED，侧重于主要答案的正确性，以及STRICT，确保所有主张都是事实和当前的。该研究突显了LLMs的局限性，特别是在信息迅速变化和错误前提的问题上，并暗示仅仅增加模型大小并不能保证更好的性能。结论是FRESHQA对LLMs提出了重大挑战，表明需要进一步的发展。

![](https://cdn.thenewstack.io/media/2024/01/973162b7-freshqa-1024x441.jpg)

研究发现，预训练的LLMs，如T5、PaLM、GPT-3.5和GPT-4，在FreshQA数据集上遇到了困难。在STRICT模式下，响应准确率在0.8%到32.0%之间，在RELAXED模式下为0.8%到46.4%。对于像GPT 3.5和GPT-4这样的模型，STRICT评估要求所有信息都是事实和当前的，这导致了准确率的显著下降，主要是因为它们无法访问实时信息，导致过时或被拒绝的答案。PALM在STRICT模式下也看到了显著的准确率下降，通常是由于响应中存在的人工痕迹和幻觉。相反，FLAN-PALM和CODEX表现更好，减少了幻觉，这要归功于它们更为简洁直接的回答。

![Zoom](https://cdn.thenewstack.io/media/2024/01/c1f3640d-freshqa-responses-1024x343.jpg)

作者们尝试了一种名为FRESHPROMPT的技术，该技术将上下文相关且最新的信息从搜索引擎引入到预训练的LLM中。给定一个问题，该方法使用问题查询搜索引擎，检索所有搜索结果，包括答案框、有机结果和其他有用的信息，如知识图谱、众包问答平台的问题和答案，以及搜索用户也会提出的相关问题。然后，使用这些信息来教导LLM推理检索到的证据，提高模型根据少量提示提供准确和实时响应的能力。

## Perplexity AI 如何实现 FreshLLMs 的思想

Perplexity AI构建了两个在线LLMs，pplx-7b-online和pplx-70b-online，可以从互联网获取实时信息，使其能够提供最新和准确的响应。这些模型利用了开源模型、内部搜索技术和微调，以有效地利用来自网络的信息。它们的设计旨在通过对时效性查询的响应来克服离线LLMs的限制，并提供最相关和有价值的信息。这些模型可通过API公开访问，允许开发人员将该技术集成到其应用程序和网站中。

模型pplx-7b-online基于mistral-7b，而pplx-70b-online则构建在llama2-70b基础模型之上。它们经过微调，以有效地利用来自网络的片段来增强其响应。据Perplexity称，通过内部数据承包商筛选高质量、多样化和大规模的训练集，以确保在帮助性、事实性和新鲜性方面具有高性能。此外，这些模型定期进行微调，以持续改进性能。这些努力使模型能够通过利用互联网的实时信息提供准确、最新和上下文相关的响应。

除了关注响应的新鲜度和当前性之外，Perplexity AI 确保这些模型提供有帮助且事实准确的答案。

最近，Perplexity AI 宣布推出一个API，以访问其在线模型以及其他模型，如mixtral-8x7b-instruct、llama-2-70b-chat和codellama-34b-instruct。Perplexity Copilot的专业订阅用户将获得5美元的API使用信用。

在我的下一篇文章中，我将为您演示如何基于Perplexity AI的API构建应用程序的教程。请保持关注。
