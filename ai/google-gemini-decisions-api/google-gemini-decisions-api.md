<!--
title: 谷歌开发了一款不会写句子的AI模型——这正是它的核心意义
cover: https://cdn.thenewstack.io/media/2026/11/74340249-graficon-stuff-zgtvz5tacc4-unsplash-1-1024x768.jpg
summary: 谷歌推出全新的Gemini Decisions API及Gemini Decision 1模型，旨在处理AI应用中的日常决策任务，无需生成文本即可提供更快、更具成本效益的评估与概率得分。
-->

谷歌推出全新的Gemini Decisions API及Gemini Decision 1模型，旨在处理AI应用中的日常决策任务，无需生成文本即可提供更快、更具成本效益的评估与概率得分。

> 译自：[Google built an AI model that can’t write a sentence](https://thenewstack.io/google-gemini-decisions-api/)
> 
> 作者：Amanda Caswell

谷歌于周三推出的全新 Gemini Decisions API 旨在处理 AI 应用每天需要执行数千次的常规决策，与传统的生成式模型相比，它具有更低的成本和更快的响应速度。

> ……AI 应用每天需要执行数千次的常规决策，与传统的生成式模型相比，它具有更低的成本和更快的响应速度。

[该 API](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) 没有使用生成式模型来处理每个决策并生成文本响应，而是使用了一个名为 Gemini Decision 1 的新模型，在单次传递中评估预定义的选项。

据谷歌称，在测试的工作负载中，响应时间从 150 到 250 毫秒不等，定价起步为每百万输入 Token 0.10 美元，且不收取输出 Token 费用。

就在几周前，[OpenAI 推出了自己的 Decisions API](https://thenewstack.io/openai-decision-models-deployment/)，与 [TypeSafe AI](https://thenewstack.io/openai-decision-api-luna/) 和微软一同加入了一个日益增长的市场，这些模型专为做出特定决策而构建，无需生成文本。

## 单次传递，不生成文本

该 API 支持 256,000-token 的上下文窗口，针对单个输入最多可评估 1,000 个独立问题，包括多模态内容。其响应包括概率和置信度分数，开发人员可利用这些分数在预定义选项之间进行选择、对照特定标准评估信息，并决定应用程序应如何进行。

谷歌 CEO Sundar Pichai 在 [X 上的帖子](https://x.com/sundarpichai/status/2120581155078729728)中将该模型描述为“专为封闭集选择而构建”，而谷歌 DeepMind 产品经理 Min Choi 和首席科学家 Felix Yu 在发布公告时则将该 API 形容为提供“专为有界选择构建的原语”。

## 谷歌已经在哪里使用了它

谷歌已经在内部使用了该模型，包括在 Gemini Notebook 中，据报道，实时的模型和推理级路由使延迟降低了多达 40%。谷歌搜索也使用它来检测涉及 MCP 工具的潜在对抗行为。

## 基准测试来自谷歌

谷歌的基准测试结果显示，Gemini Decision 1 的表现优于 OpenAI 的 GPT-6 Luna，尽管与 TypeSafe 的 Jev 1.14 的竞争更加接近。

领导谷歌 AI Studio 和 Gemini API 产品的 Logan Kilpatrick 在 [X 上将其描述](https://x.com/OfficialLoganK/status/2120581433639198885)为“我们 Gemini API 中的全新前沿决策模型”。在 JevBench 上，谷歌模型的得分为 92.2%，而 Luna 为 90.9%，Jev 为 90%。

但在七项共享测试中的两项上，Jev 取得了领先，并且运行成本更低，完整的基准测试套件成本为 0.68 美元，而 Gemini Decision 1 为 0.88 美元。在测试的模型中，谷歌的模型还记录了最低的校准误差。

所有的基准测试数据均来自谷歌自己的测试，独立评估尚未确定这些模型在生产环境中的表现如何。[SiliconANGLE 还指出](https://siliconangle.com/2026/11/11/google-enters-the-decision-model-market-with-gemini-decisions-api/)，按单个 Token 计算，Jev 比谷歌的模型更便宜。

> 所有的基准测试数据均来自谷歌自己的测试，独立评估尚未确定这些模型在生产环境中的表现如何。

## 开发者实际支付的费用

开发者只需支付一次发送共享上下文的费用，即使他们针对该上下文提出了多个问题（尽管问题本身仍计入 Token 使用量）。该 API 会分别评估每个问题，因此需要使用一个答案来决定下一步询问什么的工作流程需要另一次调用。

[Gemini Decision 1 通过 Google AI Studio 提供](https://aistudio.google.com/docs/decisions-api)，提供免费的原型设计层，并通过 OpenRouter、LangChain、Vercel 和 LiteLLM 进行集成。谷歌还计划支持 Google Cloud 上的 Gemini，尽管谷歌尚未公布发布日期。

> 开发者只需支付一次发送共享上下文的费用，即使他们针对该上下文提出了多个问题……

该文章最初发布于 [The New Stack](https://thenewstack.io)，原标题为 [Google built an AI model that can’t write a sentence — and that’s the point](https://thenewstack.io/google-gemini-decisions-api/)。