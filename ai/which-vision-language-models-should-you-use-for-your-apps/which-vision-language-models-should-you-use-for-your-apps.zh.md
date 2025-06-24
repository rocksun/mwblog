视觉语言模型 (VLMs) 是 [多模态 AI](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/) 中一个很有前景的分支，它能够处理文本和图像这两种不同的模态，从而执行各种视觉语言任务，例如图像描述、图像搜索和检索、文本到图像的生成、[视觉问答](https://huggingface.co/tasks/visual-question-answering) (VQA) 和[视频理解](https://blog.fastforwardlabs.com/2021/12/14/an-introduction-to-video-understanding-capabilities-and-applications.html)。

在我们之前关于视觉语言模型的[文章](https://thenewstack.io/a-developers-guide-to-vision-language-models/)中，我们介绍了其底层架构的一些基础知识、训练它们的一些策略以及它们的使用方式。现在，我们将了解目前最广泛使用的 VLM、一些常见的评估工具以及最常用于训练它们的数据集。

## 流行的视觉语言模型

视觉语言模型的发展速度令人印象深刻，新的、更强大的模型不断涌现。以下按任意顺序排列，你可以找到一些最流行的 VLM 及其功能的非详尽列表。

**[GPT-4o](https://openai.com/index/hello-gpt-4o/):** 由 OpenAI 开发，是目前顶级的专有 VLM 之一，擅长视觉理解以及生成文本、视觉和音频内容。

**[Llama 4](https://www.llama.com/):** Meta 强大的开源多模态 AI 模型由一种新的[混合专家](https://www.ibm.com/think/topics/mixture-of-experts) (MoE) 架构提供支持，并拥有令人瞠目结舌的 1000 万个 token 的上下文窗口。它有三种不同的尺寸，其核心理念是原生多模态，无需像之前的模型那样，使用外部“补丁”来处理基于视觉的任务。

**[Gemini 2.5 Flash](https://deepmind.google/models/gemini/flash/):** 这个版本的 Google 旗舰 AI 模型在多模态理解和推理方面表现出更强大、更快速的性能，拥有 100 万个 token 的上下文窗口，并支持多张图像，每个提示最多可包含 3,000 张图像。

**[DeepSeek-VL2](https://github.com/deepseek-ai/DeepSeek-VL2):** DeepSeek AI 推出的这款令人印象深刻的开源 VLM 拥有多个变体，旨在实现各种视觉语言任务中的高级多模态理解。借助其[混合专家](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) (MoE) 架构，该模型能够激活更少的参数以最大限度地提高效率，同时实现与类似模型相媲美的卓越性能。

**[Kimi-VL-Thinking](https://github.com/MoonshotAI/Kimi-VL):** Moonshot AI 的这款 VLM 是一款“高级长程思考变体”，以其在处理较长视频、图像和文档方面的可靠性能而闻名。

**[Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL):** 由阿里云创建，该模型在理解文档和长视频、以及对象定位和多语言 OCR 方面表现出令人印象深刻的能力。

**[Gemma 3](http://developers.googleblog.com/en/introducing-gemma3/):** Gemma 3 有各种尺寸，是 Google DeepMind 针对多功能、高效、轻量级、开放权重且功能强大的多模态 AI 的解决方案，可以在单个 TPU 或 GPU 上运行。

**[Molmo](https://molmo.org/):** Molmo 是艾伦人工智能研究所推出的一系列开源 VLM，以其高性能的多模态交互而闻名，同时由于其创新的训练管道，它比竞争对手使用更少的训练数据，该管道偏爱基于语音的注释而不是大数据集。

**[NVLM](https://research.nvidia.com/labs/adlr/NVLM-1/):** NVIDIA 的一系列开放的、前沿级的多模态 AI 模型以其在视觉语言任务中的最新成果而闻名，尤其是在 OCR 方面优于许多专有和开源模型。

**[Pixtral](https://mistral.ai/news/pixtral-large):** Mistral AI 的多模态 VLM 有两个版本，分别是开放权重的 [Pixtral Large](https://mistral.ai/news/pixtral-large) 和开源的 [Pixtral 12B](https://mistral.ai/news/pixtral-12b)，它们具有强大的多模态解码器和视觉编码器，可提供增强的推理和跨模态理解，例如处理包含交错文本和图像的长文档。

## 评估视觉语言模型

视觉语言模型的性能可以通过特定于任务的指标、特定领域的基准以及人工主导的评估相结合的方式进行评估。

*   **图像描述：** 这项任务结合了计算机视觉和自然语言处理，当模型遇到视觉图像时，会生成文本描述。流行的图像描述指标包括 [BLEU](https://aclanthology.org/P02-1040.pdf)、[ROUGE](https://aclanthology.org/W04-1013.pdf)、[CIDEr](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Vedantam_CIDEr_Consensus-Based_Image_2015_CVPR_paper.pdf)、[SPICE](https://github.com/peteanderson80/SPICE)、[METEOR](https://aclanthology.org/W05-0909.pdf) 和 [CLIPScore](https://aclanthology.org/2021.emnlp-main.595v2.pdf)。有用的基准包括 [COCO Captions](https://github.com/tylin/coco-caption)、[CapArena](https://caparena.github.io/) 和 [Flickr30K](https://www.kaggle.com/datasets/eeshawn/flickr30k)。
*   **视觉问答 (VQA)：** 视觉问答任务要求模型正确回答从问题-图像对中派生出来的问题。对于封闭式、“是”或“否”问题，测量准确率；而更复杂的开放式问题可以使用基于人类的分析来评估，或者重新采用已建立的指标，如 CIDEr。这些类型的任务的一些有用的基准包括 [VQA v2.0](https://visualqa.org/)、[GQA](https://cs.stanford.edu/people/dorarad/gqa/about.html) 和 [OK-VQA](https://okvqa.allenai.org/)。

[![](https://cdn.thenewstack.io/media/2025/06/93d2915d-vqa.png)](https://cdn.thenewstack.io/media/2025/06/93d2915d-vqa.png)

*   **视觉推理和理解：** 根据模型进行逻辑推理的能力对其进行评估。常见的基准包括 [NLVR2](https://github.com/lil-lab/nlvr)、包含超过 11.5K 个多模态挑战的大型 [MMMU](https://mmmu-benchmark.github.io/)、用于视觉数学推理的 [MathVista](https://mathvista.github.io/)、用于对象定位和光学字符识别的 [MMBench](https://github.com/open-compass/mmbench/) 以及用于视觉文档理解的 [DocVQA](https://www.docvqa.org/datasets)。
*   **跨模态检索：** 分为图像到文本或文本到图像检索任务，相关指标包括 [Recall@k](https://milvus.io/ai-quick-reference/what-are-the-key-metrics-used-to-evaluate-visionlanguage-models) 和 [平均精度均值](https://www.geeksforgeeks.org/computer-vision/mean-average-precision-map-in-computer-vision/) (mAP)。

[![](https://cdn.thenewstack.io/media/2025/06/442ef83e-vlm-tasks.png)](https://cdn.thenewstack.io/media/2025/06/442ef83e-vlm-tasks.png)

[来源](https://arxiv.org/pdf/2210.09263)

然而，随着 VLM 的发展并获得更广泛的功能，新的评估策略正在涌现。其中一些包括 [VHELM](https://openreview.net/pdf?id=TuMnKFKPho)（视觉语言模型的整体评估），它在多个层面上评估 VLM，包括视觉感知、推理、稳健性、安全性和毒性以及偏差和公平性。[Image2Struct](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0718553fd6b227a353c6432cf893285-Paper-Datasets_and_Benchmarks_Track.pdf) 是另一种综合方法，用于评估 VLM 从图像中提取结构化信息的能力。

尽管如此，在评估 VLM 的细微差别、流畅性、相关性和创造力方面，人类评估也至关重要，此外，它还可以发现自动指标可能会忽略的任何细微错误。

## 用于训练视觉语言模型的数据集

*   **LAION-5B：** 这个开放的大规模 [LAION-5B](https://laion.ai/blog/laion-5b/) 数据集包含超过 50 亿个经过 [CLIP](https://openai.com/index/clip/) 过滤的、多样化的图像-文本对，带有多种语言的标题；因此，它允许进行稳健的多语言模型训练。
*   **PMD（公共模型数据集）：** [公共模型数据集](https://huggingface.co/datasets/facebook/pmd) 拥有超过 700 亿个图像-文本对，这些图像-文本对来自大规模数据集，如 [COCO](https://cocodataset.org/#home)、[Conceptual Captions](https://ai.google.com/research/ConceptualCaptions/) 和 [RedCaps](https://paperswithcode.com/dataset/tvrecap)，它提供了丰富的多模态数据。
*   **VQA：** 这组数据包含超过 200,000 张图像，每张图像都与五个问题配对，而每个问题又链接到十个基本事实答案和三个不正确的答案。[VQA](https://visualqa.org/) 数据集通常用于微调预训练的 VLM，以用于视觉问答和视觉推理任务。
*   **Visual Genome：** 这个[数据集](https://homes.cs.washington.edu/~ranjay/visualgenome/api.html) 包含超过 100,000 张图像，带有 170 万个问答对，平均每张图像有 17 个问题。与 VQA 数据集相比，[Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/index.html) 在六种类型的问题（谁、什么、哪里、何时、为什么和如何）中提供了更平衡的问题，此外还提供了丰富的对象注释，可捕获各种属性和关系。
*   **ImageNet：** [ImageNet](https://www.image-net.org/) 数据集包含超过 1400 万张带注释和组织的图像，最常用于图像分类和对象识别等任务。对于需要增强可解释性和模型透明度的任务，[ImageNet-X](https://facebookresearch.github.io/imagenetx/site/home) 是另一种选择。

## 结论

有如此多的 VLM 可用，因此很难选择最适合你的用例的模型。[Vision Arena](https://huggingface.co/spaces/WildVision/vision-arena)、[Open VLM Leaderboard](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard) 等排行榜和评估工具包以及开源 [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) 可以帮助开发人员做出选择。

尽管如此，尽管 VLM 具有强大的功能，但在使用 VLM 时仍需要解决一些潜在的挑战，例如偏差、成本、幻觉以及模型难以学习泛化，以便对它以前从未见过的新数据做出准确的预测。

最终，随着视觉语言模型的格局不断发展，我们可以预期模型会变得更加复杂，并且能够处理越来越复杂的任务。

有关更多信息，请查看我们之前关于视觉语言模型的[文章](https://thenewstack.io/a-developers-guide-to-vision-language-models/)，其中概述了 VLM 的架构和一些用于训练 VLM 的学习技术。