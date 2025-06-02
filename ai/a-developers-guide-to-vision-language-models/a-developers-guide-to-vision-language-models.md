
<!--
title: Vision Language Models (VLMs) 开发者指南

Large language models (LLMs) are capable of solving a variety of natural language tasks, but are limited in their ability to reason about the visual world. Vision language models (VLMs) combine the power of LLMs with visual encoders, allowing them to process and reason about images and videos.

大型语言模型（LLM）能够解决各种自然语言任务，但在对视觉世界进行推理的能力方面受到限制。视觉语言模型（VLM）结合了 LLM 的强大功能和视觉编码器，使它们能够处理和推理图像和视频。

This guide provides an overview of VLMs, including their architecture, capabilities, and applications. It also covers the challenges of working with VLMs and provides guidance on how to get started.

本指南概述了 VLM，包括它们的架构、功能和应用。它还涵盖了使用 VLM 的挑战，并提供了有关如何入门的指导。

What are Vision Language Models?

什么是视觉语言模型？

Vision language models (VLMs) are multimodal models that can process and reason about both images and text. They typically consist of two main components:

视觉语言模型（VLM）是多模态模型，可以处理和推理图像和文本。它们通常由两个主要组件组成：

*   **A visual encoder:** This component is responsible for encoding images into a set of visual features. This is often a convolutional neural network (CNN) or a vision transformer (ViT).
*   **A language model:** This component is responsible for processing and generating text. This is often a large language model (LLM) such as GPT-3 or PaLM.

*   **视觉编码器：** 此组件负责将图像编码为一组视觉特征。这通常是卷积神经网络（CNN）或视觉 Transformer（ViT）。
*   **语言模型：** 此组件负责处理和生成文本。这通常是大型语言模型（LLM），例如 GPT-3 或 PaLM。

VLMs work by first encoding an image into a set of visual features using the visual encoder. These features are then fed into the language model, which uses them to generate text. For example, a VLM could be used to generate a caption for an image, answer questions about an image, or even generate new images based on a text prompt.

VLM 的工作原理是首先使用视觉编码器将图像编码为一组视觉特征。然后将这些特征馈送到语言模型，该模型使用它们来生成文本。例如，VLM 可用于生成图像的标题、回答有关图像的问题，甚至根据文本提示生成新图像。

Capabilities of VLMs

VLM 的功能

VLMs have a wide range of capabilities, including:

VLM 具有广泛的功能，包括：

*   **Image captioning:** VLMs can be used to generate captions for images. This can be useful for a variety of applications, such as automatically tagging images in a database or creating descriptions for images on a website.
*   **Visual question answering:** VLMs can be used to answer questions about images. This can be useful for applications such as customer service or education.
*   **Image generation:** VLMs can be used to generate new images based on a text prompt. This can be useful for applications such as art generation or product design.
*   **Visual reasoning:** VLMs can be used to reason about the visual world. This can be useful for applications such as robotics or self-driving cars.
*   **Object Detection**: VLMs can be used to identify objects within an image, along with bounding boxes.

*   **图像字幕：** VLM 可用于生成图像的字幕。这对于各种应用非常有用，例如自动标记数据库中的图像或为网站上的图像创建描述。
*   **视觉问答：** VLM 可用于回答有关图像的问题。这对于客户服务或教育等应用非常有用。
*   **图像生成：** VLM 可用于根据文本提示生成新图像。这对于艺术生成或产品设计等应用非常有用。
*   **视觉推理：** VLM 可用于推理视觉世界。这对于机器人技术或自动驾驶汽车等应用非常有用。
*   **物体检测：** VLM 可用于识别图像中的物体以及边界框。

Applications of VLMs

VLM 的应用

VLMs are being used in a variety of applications, including:

VLM 正被用于各种应用，包括：

*   **E-commerce:** VLMs can be used to improve the customer experience by providing more information about products. For example, a VLM could be used to generate a description of a product based on an image of the product.
*   **Healthcare:** VLMs can be used to improve the accuracy of medical diagnoses. For example, a VLM could be used to analyze medical images and identify potential problems.
*   **Education:** VLMs can be used to create more engaging and interactive learning experiences. For example, a VLM could be used to create a virtual tour of a museum or historical site.
*   **Robotics:** VLMs can be used to improve the ability of robots to interact with the world. For example, a VLM could be used to help a robot identify objects in its environment and navigate to them.
*   **Search**: VLMs can be used to improve search results by allowing users to search for images using text queries.

*   **电子商务：** VLM 可用于通过提供有关产品的更多信息来改善客户体验。例如，VLM 可用于根据产品的图像生成产品的描述。
*   **医疗保健：** VLM 可用于提高医疗诊断的准确性。例如，VLM 可用于分析医学图像并识别潜在问题。
*   **教育：** VLM 可用于创建更具吸引力和互动性的学习体验。例如，VLM 可用于创建博物馆或历史遗址的虚拟导览。
*   **机器人技术：** VLM 可用于提高机器人与世界互动能力。例如，VLM 可用于帮助机器人识别其环境中的物体并导航到它们。
*   **搜索：** VLM 可用于通过允许用户使用文本查询搜索图像来改善搜索结果。

Challenges of Working with VLMs

使用 VLM 的挑战

While VLMs have a lot of potential, there are also a number of challenges associated with working with them. These challenges include:

虽然 VLM 具有很大的潜力，但使用它们也存在许多挑战。这些挑战包括：

*   **Data:** VLMs require large amounts of data to train. This data can be expensive and time-consuming to collect and label.
*   **Compute:** VLMs are computationally expensive to train and deploy. This can make them difficult to use for resource-constrained applications.
*   **Bias:** VLMs can be biased by the data they are trained on. This can lead to unfair or inaccurate results.
*   **Interpretability:** VLMs can be difficult to interpret. This can make it difficult to understand why they are making certain predictions.

*   **数据：** VLM 需要大量数据进行训练。收集和标记这些数据可能既昂贵又耗时。
*   **计算：** VLM 在训练和部署方面需要大量的计算资源。这使得它们难以用于资源受限的应用。
*   **偏差：** VLM 可能会受到它们训练数据的偏差影响。这可能导致不公平或不准确的结果。
*   **可解释性：** VLM 很难解释。这使得很难理解它们为什么做出某些预测。

Getting Started with VLMs

VLM 入门

If you are interested in getting started with VLMs, there are a few things you can do:

如果您有兴趣开始使用 VLM，您可以做以下几件事：

*   **Learn more about VLMs.** There are a number of resources available online, such as research papers, blog posts, and tutorials.
*   **Experiment with existing VLMs.** There are a number of pre-trained VLMs available online that you can use to experiment with.
*   **Build your own VLMs.** If you have the resources, you can build your own VLMs from scratch.

*   **了解更多关于 VLM 的信息。** 网上有很多资源，例如研究论文、博客文章和教程。
*   **尝试现有的 VLM。** 网上有很多预训练的 VLM，您可以使用它们进行实验。
*   **构建您自己的 VLM。** 如果您有资源，您可以从头开始构建您自己的 VLM。

Here are some resources to help you get started:

以下是一些可以帮助您入门的资源：

*   [Hugging Face Transformers library](https://huggingface.co/transformers/model_doc/vision-encoder-decoder.html)
*   [TensorFlow Models](https://www.tensorflow.org/tutorials/text/image_captioning)
*   [PyTorch Image Models](https://pytorch.org/vision/stable/models.html)

Observability

可观测性

As with any machine learning model, it is important to monitor VLMs in production to ensure that they are performing as expected. This includes tracking metrics such as accuracy, latency, and resource usage. It is also important to have a system in place for detecting and addressing any issues that may arise.

与任何机器学习模型一样，重要的是在生产中监控 VLM，以确保它们按预期运行。这包括跟踪准确性、延迟和资源使用情况等指标。同样重要的是建立一个系统来检测和解决可能出现的任何问题。

[Arize AI](https://arize.com/) is a machine learning observability platform that can be used to monitor VLMs in production. Arize provides a variety of features, such as:

[Arize AI](https://arize.com/) 是一个机器学习可观测性平台，可用于在生产中监控 VLM。Arize 提供了各种功能，例如：

*   **Real-time monitoring:** Arize can be used to monitor VLMs in real-time, providing you with up-to-date information on their performance.
*   **Alerting:** Arize can be configured to send alerts when certain metrics fall below a certain threshold.
*   **Debugging:** Arize provides tools for debugging VLMs, such as the ability to drill down into individual predictions and see the data that was used to make them.

*   **实时监控：** Arize 可用于实时监控 VLM，为您提供有关其性能的最新信息。
*   **警报：** 可以将 Arize 配置为在某些指标低于某个阈值时发送警报。
*   **调试：** Arize 提供了用于调试 VLM 的工具，例如深入研究单个预测并查看用于进行预测的数据的能力。

Conclusion

结论

Vision language models are a powerful new tool that can be used to solve a variety of problems. However, they are also complex and challenging to work with. By understanding the challenges and following the guidance in this guide, you can get started with VLMs and start building your own applications.

视觉语言模型是一种强大的新工具，可用于解决各种问题。但是，它们也很复杂且具有挑战性。通过了解这些挑战并遵循本指南中的指导，您可以开始使用 VLM 并开始构建您自己的应用程序。
cover: https://cdn.thenewstack.io/media/2025/05/f25ff361-pexels-ana-claudia-quevedo-estrada-922193-4529589b.jpg
summary: 多模态AI崛起！本文详解开发者如何玩转视觉语言模型(VLM)，架构核心在于视觉/语言编码器、Transformer和任务Head。训练VLM需掌握对比学习、PrefixLM、掩码建模等技术，更可利用预训练模型微调。VLM广泛应用于图像生成、VQA等领域，速来解锁！
-->

多模态AI崛起！本文详解开发者如何玩转视觉语言模型(VLM)，架构核心在于视觉/语言编码器、Transformer和任务Head。训练VLM需掌握对比学习、PrefixLM、掩码建模等技术，更可利用预训练模型微调。VLM广泛应用于图像生成、VQA等领域，速来解锁！

> 译自：[A Developer’s Guide to Vision Language Models](https://thenewstack.io/a-developers-guide-to-vision-language-models/)
> 
> 作者：Kimberley Mok



# 开发者视觉语言模型指南

![Featued image for: A Developer’s Guide to Vision Language Models](https://cdn.thenewstack.io/media/2025/05/f25ff361-pexels-ana-claudia-quevedo-estrada-922193-4529589b-1024x576.jpg)

最近[多模态 AI](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/) 的出现意味着 AI 系统现在在本质上变得越来越通用，因为它们以集成的方式同时处理和生成各种数据模态——包括文本、图像、音频和视频。

视觉语言模型 (VLM) 是多模态 AI 中用途更广泛的子集之一，它结合了[自然语言处理](https://thenewstack.io/get-started-with-text-classification/) (NLP) 和[计算机视觉](https://thenewstack.io/mastering-the-fundamentals-of-computer-vision-with-python/) (CV) 功能来处理高级视觉语言任务——例如图像字幕、视觉问题解答以及文本到图像的搜索和生成。

## 视觉语言模型的架构

视觉语言模型能够处理基于文本和图像的输入，模型的计算机视觉部分分析和解释视觉数据，模型的自然语言处理部分分析和理解文本。在某种程度上，可以将 VLM 想象成能够理解单词和图像的多价大型语言模型 (LLM)。

一般来说，VLM 由以下主要组件组成：

**视觉编码器：** 这部分从视觉输入中提取形状、图案和颜色等视觉线索，并将它们转换为[向量嵌入](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai/)——或高维空间内数据点的数值表示——AI 模型可以理解这些数值表示。过去，VLM 使用卷积神经网络从图像中提取特征。现在，许多 VLM 通常会使用视觉 Transformer (ViT)，它将图像分成固定大小的“补丁”，然后像基于 Transformer 的语言模型解析句子中的单词一样处理它们作为token。
**语言编码器：** 此组件评估单词之间的语义含义和上下文关联，并将该信息转换为[文本嵌入](https://thenewstack.io/beginners-guide-to-openai-text-embedding-models/)。
**投影仪/融合机制：** 这一重要元素将来自视觉和语言编码器的特征嵌入对齐到共享的多模态空间中。
**多模态 Transformer：** 该集成组件在组合的视觉和语言嵌入上运行，通常在模态内使用[自注意力机制](https://www.ibm.com/think/topics/self-attention)，该机制衡量序列中单词 token 的上下文重要性，从而允许模型预测句子中最可能的单词顺序。此外，它在模态之间使用[交叉注意力机制](https://www.geeksforgeeks.org/cross-attention-mechanism-in-transformers/)来学习图像和单词之间的关系，以及使用[位置编码](https://medium.com/thedeephub/positional-encoding-explained-a-deep-dive-into-transformer-pe-65cfe8cfe10b)来保留图像补丁和文本 token 之间的上下文关系。
**特定于任务的 Head：** 这些 Head 调整最终输出，以适应模型旨在执行的任何特定任务。特定于任务的 Head 的一些示例包括分类 Head、生成 Head 和问答 Head。

![](https://cdn.thenewstack.io/media/2025/05/b946a105-vlm-architecture-diagram-via-nvidia.jpg)

常见 VLM 架构图（通过 [NVIDIA](https://www.nvidia.com/en-us/glossary/vision-language-models/)）。

## 训练 VLM 的学习技术

训练 VLM 的策略通常涉及多种技术，这些技术有助于对齐和融合来自视觉和语言组件的数据。
**对比学习：** 这种方法通过将图像和文本嵌入映射到共享的嵌入空间中，训练模型来区分相似和不相似的数据点对。当模型在由配对图像和文本组成的数据集上进行训练时，它会生成一个相似度分数。然后，它学习最小化匹配嵌入对之间的距离，同时最大化不匹配的嵌入对之间的距离。对比模型的一个例子是 [CLIP](https://openai.com/index/clip/)，它使用三步流程来执行零样本预测。

**PrefixLM：** 这是一种用于预训练语言模型的 NLP 学习技术，其中文本的一部分（即前缀）用作输入，模型学习预测序列的下一部分。对于 VLM，PrefixLM 通常与简化的 [SimVLM](https://arxiv.org/pdf/2108.10904.pdf) 架构结合使用，以提供零样本学习能力，从而允许模型基于图像及其关联的文本前缀有效地预测下一个文本序列，并使用视觉转换器。

**Frozen PrefixLM：** 这种训练技术建立在 PrefixLM 的基础上，但在训练期间语言模型的参数被冻结，从而产生计算效率更高的训练过程。

**Masked modeling（掩码建模）：** 通过这种方法，基于文本或图像的输入的部分内容会被随机遮盖。然后，VLM 将学习预测和“填充”被遮盖输入的缺失部分，可以通过使用 [masked language modeling](https://www.ibm.com/think/topics/masked-language-model) 来在给定未遮盖图像时生成缺失的文本信息，或者通过使用 [masked image modeling](https://medium.com/@vyhao02/a-brief-history-of-masked-image-modeling-family-15ca1f21cc15) 来在给定未遮盖文本标题时重建图像的缺失像素。[FLAVA](https://flava-model.github.io/)(Foundational Language And Vision Alignment) 是一个采用这种掩码技术的模型示例，以及对比学习。

**Generative model training（生成模型训练）：** 这种方法训练 VLM 以生成新的输出，具体取决于给定的文本和图像输入。这可能意味着根据文本输入生成图像（文本到图像），或与图像相关的文本标题或摘要（图像到文本）。[基于生成式文本到图像扩散的 VLM](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/) 的示例包括 Midjourney 和 Stable Diffusion。

**Pretrained models（预训练模型）：** 为了降低从头开始训练 VLM 的成本和时间，还可以使用预训练的 LLM 和视觉编码器构建一个 VLM，并添加额外的映射网络层以对齐图像和文本表示。[Knowledge distillation](https://www.v7labs.com/blog/knowledge-distillation-guide) 是一种可用于将知识从预训练的“教师”模型转移到更简单、更轻量级的“学生”模型的技术。或者，也可以通过使用 [Transformers](https://github.com/transformerlab/transformerlab-app) 和 [SFTTrainer](https://huggingface.co/docs/trl/en/sft_trainer) 等工具来调整和微调现有 VLM 以用于特定应用。

## 视觉语言模型的用途

视觉语言模型可用于需要合成视觉和文本信息的各种应用，包括：

- 图像生成
- 图像标题和摘要
- 图像分割
- 图像检索
- 对象检测
- 视频理解
- 可视化问答 (VQA)
- 用于智能文档理解的文本提取
- 在线内容审核和安全
- 为交互式系统提供支持，例如教育和医疗保健
- 远程医疗、自动化诊断工具和虚拟健康助手

## 结论

视觉语言模型只是 [多功能且功能强大的多模态 AI 模型](https://thenewstack.io/the-emergence-of-generalist-multimodal-ai-models/) 不断增长的子类型之一。但与开发和部署任何 AI 模型一样，在潜在的 [偏差](https://thenewstack.io/tools-for-addressing-fairness-and-bias-in-multimodal-ai/)、成本、复杂性和 [幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/) 方面始终存在挑战。在即将发布的文章中，我们将介绍用于训练 VLM 的一些数据集、用于评估它们的基准，以及一些知名的 VLM 及其功能。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)