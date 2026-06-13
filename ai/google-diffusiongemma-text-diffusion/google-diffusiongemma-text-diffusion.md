<!--
title: Google的DiffusionGemma比其其他Gemma模型快4倍
cover: https://cdn.thenewstack.io/media/2026/02/08eb79e4-mitchell-luo-jz4ca36oj_m-unsplash-scaled.jpg
summary: Google发布了实验性模型DiffusionGemma，利用扩散模型原理实现并行文本生成，速度较传统Gemma模型提升4倍。虽然性能略低于标准版，但在特定场景下具备显著的速度优势。
-->

Google发布了实验性模型DiffusionGemma，利用扩散模型原理实现并行文本生成，速度较传统Gemma模型提升4倍。虽然性能略低于标准版，但在特定场景下具备显著的速度优势。

> 译自：[Google's DiffusionGemma is 4x faster than its other Gemma models](https://thenewstack.io/google-diffusiongemma-text-diffusion/)
> 
> 作者：Frederic Lardinois

大约一年前，Google 在其 I/O 开发者大会上[演示了一个扩散模型](https://thenewstack.io/googles-gemini-models-go-deeper/)，但之后就很少提及该技术。

然而，周三 Google 打破了沉默，发布了 [DiffusionGemma](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)，这是一个实验性的 26B 混合专家（mixture-of-experts）模型，它利用扩散技术生成文本的速度比现有的 Gemma 模型快 4 倍。

扩散技术长期以来一直是生成图像的标准（参考 Stable Diffusion）。与逐个单词生成不同，像 DiffusionGemma 或 Inception 的 [Mercury 2](https://thenewstack.inception-labs-mercury-2-diffusion/) 这样的模型可以并行生成单词。

起初，这些文本块看起来毫无意义且似乎是随机的。但随后，通过每一步的迭代，模型会细化文本并减少噪声，直到它变成你想要寻找的答案。如果你曾经观察过扩散图像模型实时生成图像的过程，这本质上是相同的过程，只是应用于文本。

![](https://cdn.thenewstack.io/media/2026/06/89465e57-diffusion_process_3_1.gif)

*来源：Google*

在每一步中，模型并行去噪 256 个 token，这就是它为何能比传统的自回归大语言模型快得多的原因。它基本上是通过每一步迭代来完善文本。

所有这些 token 都相互关注（attend），Google 表示这对于内联编辑（inline editing）、代码补全（code infilling）、处理氨基酸序列和数学图表等用例特别有帮助。

![](https://cdn.thenewstack.io/media/2026/06/1363fff6-updated-intelligence_vs_latency_.width-1000.format-webp.webp)

*来源：Google*

Google 表示，DiffusionGemma 在单个 Nvidia H100 上每秒可以产生超过 1,000 个 token。由于该模型使用了混合专家技术，它不需要将全部 260 亿个参数保留在内存中；相反，它在推理期间仅激活 38 亿个参数。这意味着它可以轻松在具有 18GB 显存的 GPU 上运行。

不过，也存在一些权衡。在所有基准测试中，与 Gemma 4 26B A4B 相比，DiffusionGemma 模型的表现较差。Google 自己也承认了这一点。从技术上讲，扩散模型完全可以达到与传统大语言模型相同的性能，但此处的重点是速度。

“对于要求最高质量的应用，我们建议部署标准的 Gemma 4，”Google 在其公告中表示。

![](https://cdn.thenewstack.io/media/2026/06/68237f49-diffusiongemma__benchmark__bar_l.width-1000.format-webp.webp)

*来源：Google*

## 可用性

该模型现已在 [HuggingFace](https://huggingface.co/google/diffusiongemma-26B-A4B-it) 上提供，对于那些希望使用 [llama.cpp](https://unsloth.ai/docs/models/diffusiongemma) 和（即将推出的）类似本地推理工具在本地运行它的人，可以使用 Unsloth 和其他量化版本。

Google 还与 Nvidia 合作，针对其硬件对模型进行了优化，包括 GeForce RTX 5090 和 4090 等高端 GPU，以及 Nvidia DGX Spark 和 DGX Station（针对那些负担得起的用户）。该模型的 Nvidia NIM 也已可用。