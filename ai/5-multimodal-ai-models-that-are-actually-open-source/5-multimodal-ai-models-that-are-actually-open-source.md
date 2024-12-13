
<!--
title: 5个实际开源的多模态AI模型
cover: https://cdn.thenewstack.io/media/2024/12/7ffb0188-oleg-ivanov-pnx4vnp_fgm-unsplashb.jpg
-->

了解最新的开源多模态AI系统，以下列出了五个领先的选项，包括其功能和用途。

> 译自 [5 Multimodal AI Models That Are Actually Open Source](https://thenewstack.io/5-multimodal-ai-models-that-are-actually-open-source/)，作者 Kimberley Mok。

多模态AI正吸引着大量关注，这要归功于其诱人的前景：设计用于处理文本、图像、音频和视频组合的AI系统，成为多面手。

虽然市场上已经存在许多[强大的、专有的多模态AI系统](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/)，但[小型多模态AI模型](https://thenewstack.io/5-small-scale-multimodal-ai-models-and-what-they-can-do/)和开源替代方案也正在迅速发展，因为用户不断寻求更易访问和更易适应的选项，并优先考虑透明度和协作。为了让您了解最新的开源多模态AI系统，我们将概述一些更受欢迎的选项，包括它们的功能和用途。

## 1. Aria

最近推出的[Aria](https://github.com/rhymes-ai/Aria) AI模型来自[Rhymes AI](https://rhymes.ai/)，被誉为[世界首个开源的多模态原生专家混合](https://www.rhymes.ai/blog-details/aria-first-open-multimodal-native-moe-model) (MoE) 模型，它可以在一个架构中处理文本、代码、图像和视频。

与更大的模型相比，这个多功能模型相对强大，但效率更高，因为它根据任务[选择性地利用](https://arxiv.org/pdf/2410.05993)其框架的相关子集（或“小型专家”）。其架构设计易于扩展，可以添加新的“专家”来处理新任务，而不会给系统带来压力。Aria擅长长多模态输入理解，这意味着它能够快速准确地解析长文档和视频。

![](https://cdn.thenewstack.io/media/2024/12/348e4131-aria.png)

*Aria的架构。*

## 2. Leopard

[Leopard](https://github.com/tencent-ailab/Leopard)由圣母大学、腾讯AI西雅图实验室和伊利诺伊大学厄巴纳-香槟分校(UIUC)的跨学科研究团队开发，是一个开源的多模态模型，专门设计用于富文本图像任务。

Leopard旨在解决多模态AI领域的两大挑战，即高质量多图像数据集的稀缺性以及图像分辨率与序列长度之间的平衡。为此，该模型使用精心策划的[数据集](https://huggingface.co/datasets/wyu1/Leopard-Instruct/tree/main)进行训练，该数据集包含超过100万个高质量的人工和合成数据片段，这些片段是从现实世界示例中收集的。它也[公开提供](https://huggingface.co/datasets/wyu1/Leopard-Instruct/tree/main)用于其他模型。

腾讯美国高级研究员、Leopard的创建者之一[Wenhao Yu](https://www.linkedin.com/in/wenhao-yu-242355153/)向The New Stack解释说：“Leopard凭借其新颖的自适应高分辨率编码模块而脱颖而出，该模块根据输入图像的原始纵横比和分辨率动态优化视觉序列长度的分配。”“此外，它使用像素洗牌将长的视觉特征序列无损压缩成较短的序列。这种设计使模型能够处理多个高分辨率图像，而不会牺牲细节或清晰度。”

这些特性使Leopard成为多页文档理解（例如幻灯片、科学和财务报告）、数据可视化、网页理解以及部署能够处理视觉复杂环境中任务的多模态AI代理的优秀工具。

![](https://cdn.thenewstack.io/media/2024/12/fd2720de-leopard.png)

*Leopard的整体模型流程。*

## 3. CogVLM

CogVLM利用深度融合技术来获得高性能，代表[认知视觉语言模型](https://arxiv.org/pdf/2311.03079)，这是一个开源的、最先进的视觉语言基础模型，可用于[视觉问答](https://blog.roboflow.com/what-is-vqa/) (VQA)和图像字幕。

CogVLM使用[基于注意力的融合机制](https://openreview.net/pdf?id=c72vop46KY)融合文本和图像嵌入，并冻结网络层以保持高性能。它还采用[EVA2-CLIP-E](https://arxiv.org/pdf/2303.15389)视觉编码器和多层感知器(MLP)适配器，用于将视觉和文本特征映射到同一空间。

## 4. LLaVA

[大型语言和视觉助手](https://llava-vl.github.io/) (LLaVA) 是另一个开源的、最先进的选项。它利用[Vicuna](https://huggingface.co/lmsys/vicuna-7b-v1.5)解码语言，并使用 CLIP 对指令遵循的文本数据进行微调。该模型已使用由 ChatGPT 和 GPT-4 生成的指令遵循的文本数据进行训练。LLaVA 使用可训练的投影矩阵将视觉表示映射到语言嵌入空间。

作为多功能的视觉助手，LLaVA 可用于创建更高级的聊天机器人，这些聊天机器人可以处理基于文本和图像的查询。


## 5. xGen-MM

也被称为 BLIP-3，这是来自[Salesforce](https://www.salesforce.com/) 的一套最先进的开源多模态模型，它包含一系列变体，包括一个[预训练基础模型](https://huggingface.co/Salesforce/xgen-mm-phi3-mini-base-r-v1.5)，一个[指令微调模型](https://huggingface.co/Salesforce/xgen-mm-phi3-mini-instruct-interleave-r-v1.5)和一个旨在减少有害输出的[安全微调模型](https://github.com/salesforce/LAVIS/tree/xgen-mm?tab=readme-ov-file)。

一个重要的进展是，这些系统使用一个庞大的、开源的万亿token“[交错”图像和文本数据数据集](https://blog.salesforceairesearch.com/mint-1t/)进行训练，研究人员将其描述为“最自然的多种模态数据形式”。这意味着这些模型擅长处理包含文本和多个图像的输入，这在广泛的设置中可能非常有用——例如自动驾驶汽车，或医疗保健中的图像分析和疾病诊断，或创建交互式教育工具，或宣传营销材料。


## 结论

围绕[开源 AI 的实际定义](https://thenewstack.io/the-open-source-ai-definition-is-out/)仍然存在持续的[激烈争论](https://thenewstack.io/why-open-source-ai-has-no-meaning/)，充斥着大型科技公司对其 AI 模型进行“[开源洗白](https://thenewstack.io/calls-to-ban-open-source-are-misguided-and-dangerous/)”以获得更广泛的信誉和声望的指控。

无论开源 AI 的争论如何发展，很明显，仍然需要真正开源的系统——以及数据集——这些系统强调透明度、协作和可访问性，并且真正符合开源精神。
