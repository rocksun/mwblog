
<!--
title: 与LLM API合作：开发人员分享构建AI机器人的经验
cover: https://cdn.thenewstack.io/media/2024/06/172f6adc-ania-kubow-trains-developers-about-ai-bots.jpg
-->

Ania Kubów 是 YouTube 上 Code with Ania Kubów 的主持人。她分享了开发者在开始构建 AI 机器人时需要了解的内容。

> 译自 [Working with LLM APIs: Dev Shares Experience Building AI Bots](https://thenewstack.io/working-with-llm-apis-dev-shares-experience-building-ai-bots/)，作者 Loraine Lawson。

[软件开发人员和培训师 Ania Kubów](https://www.codewithania.com/) 关于使用 [大型语言模型 PaLM 2](https://www.freecodecamp.org/news/how-to-use-the-palm-2-api/) 进行开发的课程已经过时了。在发布仅五个月后，Google 就弃用了 PaLM 2 语言模型，转而支持 [Gemini](https://thenewstack.io/langchain-and-google-gemini-api-for-ai-apps-a-quickstart-guide/)。她告诉 The New Stack，这令人沮丧，但这是技术的本质。

揭秘人工智能 API 是 [Kubów 作为培训师的目标之一](https://www.youtube.com/@aniakubow)。我们询问了 Kubów，在处理 LLM 及其 API 时，[开发人员可以期待什么](https://thenewstack.io/2024-forecast-what-can-developers-expect-in-the-new-year/)。她说，她注意到 [AI API 的趋势](https://thenewstack.io/6-api-trends-and-practices-to-know-for-2024/) 变得更容易使用。

她说：“出现了一种模式，尤其是我使用过的 API，我开始看到更多。”“一开始，即使只是整理文档，你也会阅读一些文档，它看起来可能很混乱。”

AI 的加速发展主要归功于该技术的疯狂采用曲线。

## 注意 AI 数据截止日期

一开始，对于 AI 实际上是什么有很多困惑——可以说，这种困惑仍然围绕着这项技术。Kubów 认为 AI 对程序员的威胁较小，而更像是一个强大的工具。

她说：“我一直喜欢把它想象成 […] 一个非常好的 Google 搜索，因为这本质上就是它。”“你获得了一些经过训练的数据。你将 [数据] 输入到大型语言模型中，这就是你获得的结果。”

由于 AI 依赖于使用截止日期训练的模型——例如，[OpenAI 的 GPT-3.5 模型训练到 2023 年 1 月](https://www.reddit.com/r/OpenAI/comments/1c2cg7t/what_is_your_gpts_training_data_cutoff_date/)——她经常建议开发人员添加自己的数据或抓取网页并将其存储到数据库中，以便向模型添加信息。

她说：“我想提醒开发人员，这是一个非常好的 Google 搜索，[但] 要注意截止日期。”“它引用的是 2023 年的信息，因为这是它拥有的最新知识。所以这是需要注意的事情。”

该截止数据可能很重要，具体取决于 [开发人员如何部署 LLM](https://thenewstack.io/a-new-tool-for-the-open-source-llm-developer-stack-aviary/)。例如，如果你正在构建一级方程式聊天机器人，并且有人问它谁赢得了“最近的比赛”，它可能会说刘易斯·汉密尔顿，因为它的最新数据来自 2023 年，她说。

## 开始使用 AI API

Kubów 建议开发人员从 OpenAI 的 GPT-4 或 [Google 的 Gemini](https://thenewstack.io/how-to-get-started-with-googles-gemini-large-language-model/) 开始使用文本到文本模型。

她解释说：“这是一个 API，然后你可以用它做各种事情。”

她对任何一个 LLM 都没有偏好，她补充说，OpenAI 和 Google 的 Gemini 各有优缺点。

> “编写正确的提示也是在使用你的积分或花钱进行所有这些调用之前你可能想要考虑的事情。”
> ——软件开发人员和培训师 Ania Kubów

Kubów 说，尽管前端必须提供流式传输数据的能力来传递聊天，但 LLM API 的重要之处在于后端。她补充说，开发人员必须了解他们希望聊天机器人做什么，了解他们想要使用的模型，以及他们希望得到的输出类型，这将由开发人员创建的提示来决定。

她说：“最重要的是，以经济高效的方式进行，因为你进行的每次调用都会产生一些费用。”“编写正确的提示也是在使用你的积分或花钱进行所有这些调用之前你可能想要考虑的事情。”

主要是，她看到开发人员正在开发聊天机器人。她构建了各种机器人，包括 [销售 AI 机器人](https://www.youtube.com/watch?v=x2k_wwH6TqY) 和 [多轮对话聊天机器人](https://www.youtube.com/watch?v=l3TLQuwr4G0)。她还使用图像 AI LLM，[构建图像](https://thenewstack.io/3-best-practices-for-image-building-and-scanning/) 分析器，允许用户发送图像并让 AI 为图像添加文本。另一个使用 [DALL-E 和 JavaScript](https://www.youtube.com/watch?v=xv9UbWp_Frs) 根据文本生成图像。

她说：“我为它构建了一个前端，以便在前端上传图像，将其发送到后端，然后后端会将其发送到 AI。”

## 开发人员通常面临的挑战

总体而言，Kubów 发现这些 API 易于使用且不言自明。然而，有些模型可能更难使用。

她说：“显然，更难的模型，比如发送图像或创建向量嵌入的模型，当您可能不理解什么是向量嵌入以及它有什么用时，可能会有点棘手。”“当然，我们以前在 API 世界中很少或根本没有见过向量嵌入。”

她看到开发人员遇到的常见问题是，当他们没有从聊天机器人那里得到预期的结果时。通常，这与编写提示有关。其他问题可能源于 AI 的加速采用曲线——例如，程序员可能已经安装了一个比文档中更新的包。

她说：“这一切都源于我们正在经历的快速变化。”“如果您刚开始，结果可能非常不可预测。”

她建议，开始时的成功关键是密切关注文档。

她说：“如您所知，我一个月或两个月前制作的许多教程现在已经过时了。”“因此，尽可能多地查看文档，以查看最新更新，这绝对是我会推荐的。”
