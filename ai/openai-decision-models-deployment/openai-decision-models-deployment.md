<!--
title: 决策模型突然无处不在，OpenAI 的决策模型现已公开
cover: https://cdn.thenewstack.io/media/2026/10/65af25c3-openai-decisions-api.png
summary: 决策模型近期突然爆火，OpenAI 推出了公开测试版的 Decisions API，支持图文输入与结构化输出。与此同时，Perplexity、Cloudflare 和亚马逊等科技巨头也纷纷推出各自的决策模型，引发市场竞争。
-->

决策模型近期突然爆火，OpenAI 推出了公开测试版的 Decisions API，支持图文输入与结构化输出。与此同时，Perplexity、Cloudflare 和亚马逊等科技巨头也纷纷推出各自的决策模型，引发市场竞争。

> 译自：[Decision models are suddenly everywhere. OpenAI’s is now public.](https://thenewstack.io/openai-decision-models-deployment/)
> 
> 作者：Meredith Shubel

决策模型突然无处不在。OpenAI 的决策模型现已公开。

本周，OpenAI 将其 Decisions API 开放为公开测试版，并加入了图像输入功能，以便根据视觉内容做出快速决策。

该 API 上周首次[发布](https://thenewstack.io/openai-decision-api-luna/)，据推测是对 [TypeSafe 的 Jev 系统](https://thenewstack.io/typesafe-jev-system-one/)的回应。目前 OpenAI 的决策模型定价为每 100 万输入 Token 0.10 美元。不收取输出 Token 费用，也不收取缓存读写费用。

该公开测试版运行在 GPT-6 Luna 上，为所有开发者提供了将文本或图像转换为三种结构化输出的能力：断言（即某事成真的可能性）、选择（即哪个预定义选项最合适）以及评分（即输入在数字范围内的落点）。

但 OpenAI 的 Decisions API 可能只是决策模型海洋中的一条鱼。本周，Perplexity、Cloudflare 和亚马逊也推出了各自的版本，并选择让开发者下载并在自己的基础架构上运行的开源权重模型。

## Decisions API 如何处理图像输入

在一段新[视频](https://www.youtube.com/watch?v=FB6oCmrIj-Y&t=21s)中，OpenAI 展示了图像输入如何帮助应用程序根据视觉理解采取快速行动。

![](https://cdn.thenewstack.io/media/2026/10/b60c58e9-decisions-api-game-1024x574.png)

来源：[OpenAI YouTube](https://www.youtube.com/watch?v=FB6oCmrIj-Y&t=21s)

它以一辆在车流中行驶的汽车的视频游戏为例。利用道路和障碍物的帧，Decisions API 可以选择汽车是应该变道还是继续行驶。

OpenAI 声称，其 API 做出这些决策所需的时间只是推理模型完成同样事情所需时间的一小部分。

拉远视角来看，这家 AI 公司暗示了如果开发者将该 API 与基本的计算机使用任务（如截屏和快速选择下一步操作）配对，这种视觉理解能够实现什么。

![](https://cdn.thenewstack.io/media/2026/10/e91abc84-decisions-api-hugging-face-robot-1024x570.png)

来源：[OpenAI YouTube](https://www.youtube.com/watch?v=FB6oCmrIj-Y&t=21s)

同一段视频还显示，OpenAI 收到了一台[Hugging Face 即将推出的可编程 Microduck 机器人](https://thenewstack.io/hugging-face-microduck-robot)的预览版，这是一款开源双足开发者机器人。

OpenAI 表示，通过将该机器人与 OpenAI 的实时语音模型 [GPT-Live](https://developers.openai.com/api/docs/models/gpt-live-1) 以及 Decisions API 相集成，其决策模型可以分析机器人的摄像机画面，以便就其视线应指向何处做出快速决策。

在给定的示例中，Decisions API 对“跟随苹果”的请求做出了响应，首先识别出水果，然后引导机器人转向它。OpenAI 补充说，GPT-Live 和 Decisions API 的配对可以走得更远，并响应更模糊的命令，例如“跟随水果”。

![](https://cdn.thenewstack.io/media/2026/10/902912a9-decisions-api-animated-character-1024x571.png)

来源：[OpenAI YouTube](https://www.youtube.com/watch?v=FB6oCmrIj-Y&t=21s)

OpenAI 还承诺，其新 API 可以为语音对话带来更多维度。

它展示了与动画角色配对的 GPT-Live 和 Decisions API；前者处理语音，后者介入选择角色应该使用的表情。

## 决策模型突然无处不在。你该如何决定使用哪一个？

TypeSafe 上个月发布 Jev 时掀起了一场不小的风暴。但它在聚光灯下的时间似乎很快就要结束了。除了 OpenAI 涉足决策模型之外，Perplexity、Cloudflare 和亚马逊也都登场了——但它们允许开发者下载模型权重并自行运行。

> Perplexity、Cloudflare 和亚马逊都已登场——但它们允许开发者下载模型权重并自行运行。

Perplexity 的 pplx-decider-v1-27b 本月在 [Hugging Face 上发布](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b)，这是一个根据 Qwen3.8-27B 微调的开源权重决策模型，采用 Apache 2.0 许可证发布。根据其模型卡，它支持与 TypeSafe 和 OpenAI 类似的决策模式：在预定义选项中进行选择并返回是/否概率。

与 OpenAI 不同，Perplexity 展示了其基准测试结果，报道称其决策模型在 11 个基准测试中总体上击败了 Jev，得分为 85.71%，而 TypeSafe 为 84.51%。但这一总分来自各种混合测试；Jev 在 11 个基准测试中的 6 个中拔得头筹，包括 WinoGrande、BBH 和 TruthfulQA binary。

[亚马逊对 Jev 的本地回应](https://thenewstack.io/aws-strands-decider-model/) Strands Decider 2B 也是一个可下载的模型——这一次，它构建于 Qwen3.5-2B 之上。亚马逊表示，在 JevBench 的公共数据集上，它在参数约为 20 亿的公共模型中排名第二。

> 就像 OpenAI 和 Perplexity 的模型一样，Clef 拥有一个视觉编码器，可以接受图像以及文本。而 Jev 和 Strands Decider 目前仅支持文本。

与此同时，Cloudflare 为开发者提供了[两个决策模型](https://blog.cloudflare.com/clef-decision-models) Clef 和 Clef-flash，两者均以 Apache 2.0 开源权重提供，并且可以通过其自身托管的 Workers AI 服务进行访问。就像 OpenAI 和 Perplexity 的模型一样，Clef 拥有一个视觉编码器，可以接受图像以及文本。而 Jev 和 Strands Decider 目前仅支持文本。

比图像或文本输入更重要的是，OpenAI 决定将其模型保留在托管 API 背后，尽管许多同类公司正在开放其版本，以便开发者可以下载并自行运行。随着决策模型成为新常态，它们部署在哪里以及如何部署，可能会成为开发者决定让哪个模型做决定的决定性因素。