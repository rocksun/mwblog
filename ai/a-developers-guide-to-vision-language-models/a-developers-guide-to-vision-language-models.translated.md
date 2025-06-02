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