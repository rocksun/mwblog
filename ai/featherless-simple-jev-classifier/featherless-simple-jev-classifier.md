<!--
title: 为什么Featherless说送披萨不需要开坦克
cover: https://cdn.thenewstack.io/media/2026/09/bca67036-zoshua-colah-scaled.jpg
summary: 无服务推理提供商Featherless推出开源库Simple Jev，将开源AI模型转化为高速的零样本分类引擎。公司CEO Eugene Cheah认为，用前沿大模型处理分类任务就像用坦克送披萨，既慢又贵。Simple Jev通过跳过文本生成直接输出概率，大幅降低了延迟与成本，推动轻量化专用模型的发展。
-->

无服务推理提供商Featherless推出开源库Simple Jev，将开源AI模型转化为高速的零样本分类引擎。公司CEO Eugene Cheah认为，用前沿大模型处理分类任务就像用坦克送披萨，既慢又贵。Simple Jev通过跳过文本生成直接输出概率，大幅降低了延迟与成本，推动轻量化专用模型的发展。

> 译自：[Why Featherless says you don't need a tank to deliver a pizza](https://thenewstack.io/featherless-simple-jev-classifier/)
> 
> 作者：Adrian Bridgwater

**关于模型的大小、形状和规模**哪种最适合每项任务的争论短时间内不会消失。无服务推理提供商 [Featherless](http://featherless.ai/) 现在也加入了这场争论。该公司发布了 [Simple Jev](https://simple-jev.featherless.ai/)，这是一个开源库，可将开源AI模型转换为高速的 [零样本分类引擎](https://huggingface.co/tasks/zero-shot-classification)。

延续本月 [TypeSafe](https://typesafe.ai/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 推出的闭源纯文本 [Jev](https://thenewstack.io/typesafe-jev-system-one/)，Featherless 的 Simple Jev 将结构化决策功能扩展到了开源模型，并在 Featherless 的托管端点上提供了图像功能。它使应用程序能够评估传入的数据并返回分类分配或二元选择，而无需生成对话文本。

## 不要用坦克送披萨

Featherless 的首席执行官兼联合创始人 [Eugene Cheah](https://www.linkedin.com/in/eugene-cheah-a47791126/) 告诉 *The New Stack*，使用最前沿的尖端模型来分类诸如支持工单之类的事情，在工具过载方面“就像用坦克送披萨一样”。

“当然，披萨坦克最终也能到达目的地，但它速度慢、价格昂贵，而且是错误的交通工具，”Cheah 说。“企业需要随时随地快速反应，而这正是行业长期以来一直忽视的一种不同类型的AI。”

Featherless 托管的 Simple Jev 端点还包含用于决策工作流的 [视觉支持](https://thenewstack.io/which-vision-language-models-should-you-use-for-your-apps/)。目前该功能仅适用于 Gemma 或 Qwen 模型，它允许开发团队使用图像作为上下文来进行即时分类。通过绕过对话文本，该软件减少了延迟并削减了计算使用量。

> “披萨坦克最终会到达，但它速度慢、价格昂贵，而且是错误的交通工具。”

Featherless 仔细阐明了其对多模态视觉支持的立场。Cheah 承认，大型闭源模型可以处理这些任务。不过，他坚持认为“这是错误的工作工具”，因为它们是通过“庞大的数万亿参数 LLMs”生成文本来达到目的的，而开发人员显然要为这种服务支付前沿价格。

“整个行业一直如此关注 LLMs 的规模，以至于有一段时间没有退后一步去思考成本和效率。Simple Jev 从不‘编写’答案：我们在模型即将做出选择的地方停下它，读取它对每个允许选项的分数，并输出概率，”Cheah 解释道。

## 什么是零样本分类引擎？

对于新手来说，零样本引擎使用预训练的语言模型将输入分类到未见过的目标类别中，而无需特定于任务的训练数据。由于零样本引擎对未经过明确训练的输入进行分类，因此它依赖迁移学习来预测新输入的类别，而无需事先接触。

“但分类器并不新鲜；这是 ChatGPT 出现之前大学教授 AI 的内容。新鲜的是（这里归功于 Jev）为其设计良好的零样本 API。核心部分已经存在，而且我们非常熟悉，这就是为什么我们能如此快地把它做起来。温故而知新，”Cheah 热情地说道。

在阐述他的团队是如何构建新工具时，Cheah 认为“任何毕业的 AI/ML 博士都可以从一句话中重新实现 Simple Jev。”

“他们会实现一个‘共享前缀、两阶段、仅预填充、基于 logits 的分类器’来做到这一点。我们将其开源以使其更易于复制和更高效，我预计还会有数百个开源的 Jev 克隆，”Cheah 补充道。

> “任何毕业的 AI/ML 博士都可以从一句话中重新实现 Simple Jev。我预计还会有数百个开源的 Jev 克隆。”

Featherless 还推出了免费的公共端点，称这将允许开发人员在没有 API 密钥或登录的情况下测试分类模型（演示限制为 2,000 个 Token 的上下文和每秒两次请求）。对于生产环境使用，Simple Jev 的定价起步为每百万输入 Token 0.03 美元，输出 Token 免费，而 TypeSafe 的 Jev 定价为每百万输入 Token 0.042 美元。这是一个可能会上涨的测试版底价，Featherless 自己的列表显示其基于 Qwen 的分类器每百万输入 Token 为 0.28 美元和 0.30 美元。那么这很贵，还是像小凯撒披萨优惠一样便宜？

“从字面意义上讲，它几乎便宜得无法计量，”Cheah 详细说道。“假设对图像/段落文本进行分类时的典型决策大约是 500 到 1,200 个 Token，因此按每百万 0.03 美元计算，你为一项决策支付的大约是千分之三美分。从宏观角度来看，每 *百万* 次决策大约是 15 到 35 美元。而且输出也是免费的。”

## **告别** 单体通才模型

Featherless 敦促我们告别其所谓的“单体通才模型”，并提供了其最新的工具，承诺数百万个轻量级的专用模型将推动未来。

***“***首先他们说开源模型永远赶不上。然后他们说开源只在少数孤立情况下获胜。很快他们就会说闭源模型只在少数孤立情况下获胜，”Cheah 补充道。

正如 Featherless 首席执行官所承认的那样，分类器并不新鲜。作为模型工具链工程的子分类，其他零样本视觉和多模态分类技术已经存在了一段时间。

## 其他在零样本领域工作的模型

最早于 2021 年初推出的 [OpenAI 的 CLIP](https://openai.com/index/clip/) 可以合理地被称为零样本图像分类的早期开源先驱。该模型从自然语言监督中学习视觉概念，并可应用于任何视觉分类基准。

[微软的 Florence-2](https://www.microsoft.com/en-us/research/publication/florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks/) 于 2024 年夏天作为开源权重视觉-语言基础模型面世。它承诺克服“空间层次结构和语义粒度”的复杂性，据说非常适合零样本和微调任务，包括视觉对象检测、定位和分割以及图像标题生成。零样本视觉标记和对象分类领域的其他竞争者包括 [Roboflow](https://roboflow.com/) 和 [Mixpeek](https://mixpeek.com/)。

**“**这个领域的每个人都站在彼此的肩膀上；这就是开源的工作方式。CLIP 和其他工具是改变行业的伟大工具。我们正在用当今的模型把一个古老的想法带回来，因为有时候你不需要坦克；你需要一个小而快的工具，”Cheah 总结道。

Simple Jev 现在作为一个完全开源的库在 [GitHub](https://github.com/featherless-ai/simple-jev) 上提供。Featherless 表示，它为开发人员提供了一个专用的模型蒸馏工作流（一个将大型前沿模型的功能转移到更小、高效架构中的过程），将大型前沿模型的复杂提示和决策压缩为更小、高度高效的开源模型以用于生产。