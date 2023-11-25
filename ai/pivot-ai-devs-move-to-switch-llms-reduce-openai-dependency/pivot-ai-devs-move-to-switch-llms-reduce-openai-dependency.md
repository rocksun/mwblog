<!--
title: AI开发者减少OpenAI，转向更多语言模型
cover: https://cdn.thenewstack.io/media/2023/11/a4872376-pivot_from_openai-1024x660.jpg
-->

继OpenAI最近的争议后，AI工程师和公司开始减少乃至完全摆脱对其API的依赖。

> 译自 [Pivot! AI Devs Move to Switch LLMs, Reduce OpenAI Dependency](https://thenewstack.io/pivot-ai-devs-move-to-switch-llms-reduce-openai-dependency/)，作者 Richard MacManus 是 The New Stack 的高级编辑，并撰写有关 Web 和应用程序开发趋势的文章。此前，他于 2003 年创立了 ReadWriteWeb，并将其打造成为世界上最有影响力的技术新闻网站之一。从早期开始...

无论过去几天围绕 OpenAI 的剧情如何发展，有一件事是清楚的:那些依赖 OpenAI API 构建的创业公司现在正在重新思考他们的策略。正如 Shawn "swyx" Wang 在剧情泄露到新闻后不久所[指出](https://www.latent.space/p/the-end-of-openai)的那样，"99% 的 AI 工程师的工作以 OpenAI 模型开始，可能也将以 OpenAI 模型结束。" 但是现在，Wang 警告说，"OpenAI 霸权的日子结束了。"

人们预计 OpenAI 的竞争对手，如 Anthropic 和 Google，将从中受益；开源 LLM 如 Meta 的 Llama 2 也是如此。但这种动荡也会渗透到第三方工具中。例如，Swyx 认为，"相对来说，像 LangChain 和 LlamaIndex 这样与模型无关的工具，以及模型路由器和网关，将更有价值。"

## 使用 OpenAI 的优缺点

归根结底，最大的教训是一个熟悉的教训：不要让你的工作项目或创业公司依赖于另一家公司的技术。这是 Twitter 开发人员[早在 2012 年](https://thenewstack.io/developers-twitter-wants-your-bots-and-other-read-write-apps/)(然后在十年后重新学习)就吃到了苦头的事情。

直到上周，AI 工程师们普遍认为 OpenAI 的 LLM 优于所有其他 LLM。今年有人谈论[开源模型](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)正在赶上。Meta 在 7 月宣布的 Llama 2 目前领先于[斯坦福大学的 HELM](https://crfm.stanford.edu/helm/latest/#/leaderboard)(语言模型整体评估)基准排行榜。然而，OpenAI 最新的模型(GPT-4 及以上)还没有被 HELM 评估——感觉是 GPT 仍然是最好的。

OpenAI 的开发者体验也很难打败，主要是因为你不需要自己训练或微调 LLM。你只需要使用 OpenAI 的 API，然后在它上面做提示工程，在[如 LangChain 这样的工具](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)帮助下。

总的来说，使用 OpenAI 的 API 一直被视为 AI 工程最高效、最简单的方法。然而，[过去几天的闹剧](https://www.techmeme.com/231117/p18#a231117p18)生动地展示了依赖一家公司 API 的风险。所以，许多 AI 初创公司现在可能会决定，拥有对 LLM 的直接访问权限(特别是如果它们是开源的)才是更好的选择。

## 评估替代方案

非 OpenAI 的供应商已经站出来帮助创业公司测试替代方案。AnyScale 的 Robert Nishihara [最近](https://twitter.com/robertnishihara/status/1726822892380504429)在 X(原 Twitter)上写道:

“如果你想要并排比较 OpenAI 和开源模型(Llama 2、Mistral、Zephyr 等)，请查看 Anyscale Endpoints。我们提供兼容 OpenAI 的 API(用于推理和微调)。”

即使创业公司决定继续使用 OpenAI 目前市场领先的 GPT 模型，它们也可能决定从 OpenAI 更稳定的合作伙伴那里为它们提供服务：Microsoft。一家名为 Sardine 的 AI 创业公司的创始人兼 CEO Soups Ranjan 在 X 上[评论](https://twitter.com/soupsranjan/status/1726967410362659307)说：“许多公司可能已经将他们的模型服务直接迁移到了 Microsoft 的 Azure AI API。”的确，Ranjan 证实他的公司就是这么做的。

Ranjan 还建议 AI 创业公司应该通过“跨多个模型编排——如 Google 的 PaLM、Anthropic 的 Claude2 或开源模型 Llama”来使其 LLM 多样化。

然而，Ranjan 警告说，开源不是简单的选择，你需要一个坚实的后端来使其工作。他在 X 上写道："不要低估 OpenAI 或 Azure 或 Google Cloud 的超级力量——他们拥有世界级的服务基础设施，可以托管这些需要大量 RAM 或定制 GPU 芯片(如英伟达 A100 或 H100)的大型语言模型，而这些芯片供应非常紧张。"

但最终它可能是值得的。Ranjan 总结说："控制你的模型，控制你的命运。"

## 执行 AI 转型

在 LinkedIn 上，AI 创业家 Aishwarya (AG) Goel 写了[一篇指南](https://www.linkedin.com/pulse/ai-pivot-transitioning-from-openai-hugging-face-aishwarya-ag-goel-g77ec/)，介绍如何让你的创业公司摆脱 OpenAI，转向 [Hugging Face 的开源工具](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)。她概述了如何在该平台上找到模型，使用 Hugging Face 的推理 API 对其进行测试，进行成本分析，并考虑“无服务器部署选项”(她自己的公司提供该服务)。

但要当心，更改 LLM 提供商有隐藏的危险。LangChain 是 OpenAI 的重要合作伙伴，可能是除 OpenAI 自身之外使用最广泛的 [AI 工程](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)工具，它在一条[推文](https://twitter.com/LangChainAI/status/1726995678042210552)中写道：“不同的 LLM 通常需要不同的提示策略。”

LangChain 补充说：“切换 API 端点通常是简单的部分。难点是让一个 LLM 的表现与另一个 LLM 类似。让单个 LLM 表现良好就已经够难的了!”

该公司说目前没有"很好的选择"来做到这一点，但它建议开发人员使用其自己的 [LangSmith Prompt Hub](https://smith.langchain.com/hub) 来测试“适用于你正在使用的模型的提示示例”。

## 是时候扩展业务了

在撰写本文时(美国太平洋时间周三凌晨早些时候)，OpenAI 剧情的最新消息是 Sam Altman 将回任 CEO，并且最终不会加入 Microsoft。如果那确实发生了，许多 AI 工程师和 AI 创业公司将舒了一口气。但他们不应忘记这里的基本教训：不要依赖一家公司来运行你的产品！

其中一位已经开始测试 OpenAI 替代方案的工程师是 Redis 的创造者 Salvatore Sanfilippo(也称为 @antirez)。在一条[推文](https://twitter.com/antirez/status/1726977467678851374)中承认他喜欢 ChatGPT 后，他写道：“如果你的产品使用了 OpenAI API，而你没有尝试这个任务是否可以由微调(通过 LoRa 或其他方式)的 Mistral 7B 来处理......嗯，在这种情况下，你真的错过了一些东西。”

如果 Redis 的创造者正在考虑其他选择——在他的例子中是一个名为 [Mistral 7B](https://mistral.ai/news/announcing-mistral-7b/) 的新的开源 LLM——那么你也许也应该这么做。
