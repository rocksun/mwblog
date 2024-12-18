
<!--
title: 构建多模态 AI 应用的 7 大工具
cover: https://cdn.thenewstack.io/media/2024/11/37168f9e-google-deepmind-bnoejhgavfe-unsplashb.jpg
-->

多模态人工智能系统可以同时处理多种类型的数据，例如文本、图像和视频。以下列出了我们最喜欢的七个工具。

> 译自 [Top 7 Tools for Building Multimodal AI Applications](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/)，作者 Kimberley Mok。


大型语言模型现在正从早期只能处理一种类型数据输入的单模态时代发展而来。如今，人们的兴趣正转向**多模态大型语言模型**(MLLM)，有报告[指出](https://www.marketsandmarkets.com/Market-Reports/multimodal-ai-market-104892004.html)，到 2028 年，多模态 AI 市场将以每年 35% 的速度增长到 45 亿美元。

多模态 AI 是指能够以集成和上下文的方式同时处理多种类型数据（例如文本、图像和视频）的系统。

MLLM 可用于分析包含文本、图像、图表和数值数据的技术报告，然后对其进行总结。其他潜在用途包括图像到文本和文本到图像搜索、视觉问答 (VQA)、图像分割和标记，以及创建特定领域 AI 系统和 MLLM 代理。

## MLLM 的设计原理

虽然多模态模型可以具有各种架构，但大多数多模态框架都包含以下元素：

* **编码器**：此组件将不同类型的数据转换为机器可读的[向量嵌入](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai/)。多模态模型通常为每种数据类型（无论是图像、文本还是音频）配备一个编码器。
* **融合机制**：此机制将所有不同的模态组合在一起，以便模型能够理解更广泛的上下文。
* **解码器**：最后，还有一个解码器，它通过解析来自不同类型数据的特征向量来生成输出。

## 热门多模态模型

### 1. CLIP

[OpenAI](https://openai.com/) 的[对比语言-图像预训练](https://openai.com/index/clip/) (CLIP) 是一种多模态视觉语言模型，它通过将基于文本数据的描述与相应的图像链接起来来处理图像分类，从而输出图像标签。它具有一个[对比损失函数](https://towardsdatascience.com/contrastive-loss-explaned-159f2d4a87ec)来优化学习，一个基于 Transformer 的文本编码器，以及一个具有[零样本](https://www.kdnuggets.com/2022/12/zeroshot-learning-explained.html)能力的[视觉 Transformer](https://huggingface.co/docs/transformers/en/model_doc/vit) (ViT) 图像编码器。CLIP 可用于各种任务，例如训练数据的图像注释、图像检索以及从图像输入生成字幕。


### 2. ImageBind

这款来自 [Meta AI](https://www.meta.ai/) 的多模态模型能够组合六种不同的模态，包括文本、音频、视频、深度、热成像和惯性测量单元 (IMU)。它可以生成任何这些数据类型的输出。

[ImageBind](https://imagebind.metademolab.com/) 将图像数据与其他模态配对以训练模型，并使用 [InfoNCE](https://arxiv.org/pdf/1807.03748v2) 进行损失优化。ImageBind 可用于仅通过输入文本提示来创建带有相关音频的宣传视频。

### 3. Flamingo

这款来自 [DeepMind](https://deepmind.google/) 的视觉语言模型为用户提供了[少样本学习](https://www.analyticsvidhya.com/blog/2021/05/an-introduction-to-few-shot-learning/)的可能性，它能够处理文本、图像和视频输入以生成文本输出。

它具有一个用于视觉编码器的冻结的、预训练的 [Normalizer-Free ResNet](https://arxiv.org/pdf/2102.06171)，一个生成视觉标记的感知重采样器，以及用于融合文本和视觉特征的交叉注意力层。[Flamingo](https://arxiv.org/pdf/2204.14198) 可用于图像字幕、分类和 VQA。

### 4. GPT-4o

OpenAI 在今年早些时候发布了这款多模态生成式预训练的基于 Transformer 的模型，也称为 [GPT-4 Omni](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/)。

GPT-4o 是一个高性能系统，能够将文本、音频、视频和图像作为输入，并且可以以闪电般的速度生成任何这些数据类型的输出，平均响应时间为 320 毫秒。它也是一个多语言系统，可以理解 50 多种语言。有趣的是，还可以提示 GPT-4o 的生成输出包含更细微的参数（例如语气、节奏和情感），使其成为创建引人入胜内容的强大工具。

### 5. Gen2

这款由 [Runway](https://runwayml.com/) 开发的令人印象深刻的强大的文本到视频和图像到视频模型利用基于扩散的模型，可以使用基于文本和图像的提示来生成上下文感知的视频。

Gen2 ([https://runwayml.com/research/gen-2](https://runwayml.com/research/gen-2)) 利用自动编码器来映射输入视频帧；以及 MiDaS ([https://pytorch.org/hub/intelisl_midas_v2/](https://pytorch.org/hub/intelisl_midas_v2/)), 一个估计输入视频帧深度的机器学习模型。它使用 CLIP 编码视频帧以理解上下文。最后，还有一个跨模态注意力机制来合并从 MiDaS 和 CLIP 中提取的内容和结构表示。该系统使用户能够使用图像和文本提示生成视频剪辑，这些剪辑可以进行风格化以匹配图像。

### 6. Gemini

Google 的 Gemini ([https://gemini.google.com/](https://gemini.google.com/))（前称 Bard ([https://blog.google/products/gemini/bard-gemini-advanced-app/](https://blog.google/products/gemini/bard-gemini-advanced-app/))）是一系列能够处理文本、音频、视频和图像的多模态 AI 模型。

Gemini 有三个版本——Ultra、Pro 和 Nano ([https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/))——并采用基于 Transformer 的架构。它具有更大的上下文窗口，允许它处理更长的格式数据——无论是长视频、文本还是代码——使其成为可在各种不同领域中使用的强大工具。为了增强安全性和响应质量，Gemini 利用监督微调和人类反馈强化学习 (RLHF) ([https://www.datacamp.com/blog/what-is-reinforcement-learning-from-human-feedback](https://www.datacamp.com/blog/what-is-reinforcement-learning-from-human-feedback))。

### 7. Claude 3

这个由 Anthropic ([https://www.anthropic.com/](https://www.anthropic.com/)) 开发的视觉语言模型有三个迭代版本：Haiku、Sonnet 和 Opus. 据该公司称 ([https://www.anthropic.com/news/claude-3-family](https://www.anthropic.com/news/claude-3-family))，Opus 是顶级版本，并在各种基准测试中展现了最先进的性能，包括本科知识和研究生水平的专家推理，以及基础数学。Anthropic 声称它在复杂任务上具有接近人类的理解和流畅程度。

Claude 3 ([https://claude.ai/](https://claude.ai/)) 具有强大的回忆能力，可以处理包含超过 100 万个标记的输入序列。在解析研究论文时，它可以在三秒钟内理解照片、图表、表格和图形，使其成为强大的教育工具。

## 结论

现在有大量的多模态 AI 工具可用，大多数大型科技公司现在都提供某种 MLLM。然而，这些更大的模型可能并不适合所有情况 ([https://thenewstack.io/the-rise-of-small-language-models/](https://thenewstack.io/the-rise-of-small-language-models/))——因此为更小的多模态 AI 系统铺平了道路，我们将在下一篇帖子中介绍这些系统。
