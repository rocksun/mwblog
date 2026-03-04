<!--
title: Google 推出 Gemini 3.1 Flash-Lite：迄今最快 Gemini 3 模型
cover: https://cdn.thenewstack.io/media/2026/03/a670cb57-rubaitul-azad-58hvxsq7rru-unsplash-scaled.jpg
summary: Google 发布了 Gemini 3.1 Flash-Lite，这是其迄今最快的 Gemini 3 模型，专为高吞吐量开发者工作负载设计。它比上一代功能更强，价格更经济，且在速度和多模态基准测试方面优于主要竞争对手。开发者可以调整模型的推理时间以优化成本。值得注意的是，这是 Gemini 3.1 系列中首个发布的 Flash-Lite 版本。
-->

Google 发布了 Gemini 3.1 Flash-Lite，这是其迄今最快的 Gemini 3 模型，专为高吞吐量开发者工作负载设计。它比上一代功能更强，价格更经济，且在速度和多模态基准测试方面优于主要竞争对手。开发者可以调整模型的推理时间以优化成本。值得注意的是，这是 Gemini 3.1 系列中首个发布的 Flash-Lite 版本。

> 译自：[Google launches Gemini 3.1 Flash-Lite, its fastest Gemini 3 model yet](https://thenewstack.io/google-gemini-3-1-flash-lite/)
> 
> 作者：Frederic Lardinois

在发布其迄今为止功能最强大的人工智能模型 [Gemini 3.1 Pro](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/) 两周后，Google 于周二[发布了](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) Gemini 3.1 Flash-Lite，这是迄今为止 Gemini 3 系列中最快的模型。它每百万输入/输出 token 的价格为 0.25 美元/1.50 美元，也是 Google 迄今为止最经济实惠的 Gemini 3 模型。

该模型旨在满足 Google 所说的“大规模高吞吐量开发者工作负载”，目前已在 [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview) 和 [Vertex AI](https://console.cloud.google.com/vertex-ai/studio/multimodal?mode=prompt&model=gemini-3.1-flash-lite-preview) 的 Gemini API 中提供预览版。它不会在 Gemini 消费者应用程序中提供。

## 基准测试

与 Google Flash-Lite 系列的上一款模型 Gemini 2.5 Flash-Lite 相比，新版本价格显著更高（从 0.10 美元/0.40 美元上涨），但功能也强大得多。

在基准测试方面，它通常优于在开发者中仍然很受欢迎的 Gemini 2.5 Flash，而且价格更低。

![Gemini 3.1 Flash-Lite 基准测试（图片来源：Google）。](https://cdn.thenewstack.io/media/2026/03/3debad88-gemini-3.1-flash-lite-table_1-1024x728.gif)

将新模型与其最直接的竞争对手（如 GPT-5 mini 和 Claude 4.5 Haiku）进行比较时，情况也同样如此。Grok 4.1 Fast 更经济实惠，但速度也显著更慢。Google 承诺 Gemini 3.1 Flash-Lite 每秒可生成多达 363 个 token，这实际上比 Gemini 2.5 Flash-Lite 慢了三个 token，但仍比任何竞争对手快两到五倍。

与其他 Gemini 模型一样，它在一个领域表现出色，那就是多模态基准测试。Google 指出，在 [Arena.ai 排行榜](http://arena.ai/)上，3.1 Flash-Lite 获得了 1432 Elo 分，使其与许多开源模型和上一代商业产品并驾齐驱。

![](https://cdn.thenewstack.io/media/2026/03/a38babc-mmmu_v2.gif)

*图片来源：Google。*

值得注意的是，Google 在今天的发布中没有公布任何 agent 基准测试。该模型旨在用于高吞吐量 agent 任务和数据处理，而非管理其他 agent 群。

为了调整模型的推理时间，开发者可以使用 API 来选择模型在任何给定任务上思考的程度。鉴于它旨在用于高吞吐量任务，当成本可能是一个因素时，这是一个重要的选项（毕竟，在较低的推理设置下，模型会生成更少的 token）。

有趣的是，Google 率先发布了 Gemini 3.1 的 Flash-Lite 版本，而传统上它会先发布功能更强大（且更昂贵）的 Flash 版本，或者像 Gemini 3 那样完全跳过 Flash-Lite。