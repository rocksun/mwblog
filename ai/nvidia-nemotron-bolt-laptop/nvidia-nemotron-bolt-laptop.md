<!--
title: 英伟达将 74B 智能体模型压缩至 24GB，可在笔记本上流畅运行
cover: https://cdn.thenewstack.io/media/2026/10/e9056735-nemotron-3.5-super-vl-image-1024x576.png
summary: 英伟达发布 Nemotron 3.5 系列模型，包含主打多模态的 120B Super VL 和专为本地笔记本设计的 74B Bolt 模型。Bolt 模型通过两比特量化技术将 740 亿参数压缩至 24GB，支持在本地流畅运行复杂的智能体任务。
-->

英伟达发布 Nemotron 3.5 系列模型，包含主打多模态的 120B Super VL 和专为本地笔记本设计的 74B Bolt 模型。Bolt 模型通过两比特量化技术将 740 亿参数压缩至 24GB，支持在本地流畅运行复杂的智能体任务。

> 译自：[Nvidia squeezed a 74B agent model into 24GB so it can run on your laptop](https://thenewstack.io/nvidia-nemotron-bolt-laptop/)
> 
> 作者：Frederic Lardinois

Nvidia 周四为其 [Nemotron 家族](https://thenewstack.io/nvidias-launches-the-next-generation-of-its-nemotron-models/)添加了几个新成员：Nemotron 3.5 Super VL，这是一个面向企业智能体的 120B 视觉语言模型，以及两个小型 Bolt 模型（[Nemotron 3.5 Bolt 74B-A9B 24GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB/blob/main/accuracy.png) 和 Nemotron 3.5 Bolt E4B 4GB），用于在本地运行编程、研究和对话工作负载。

Nvidia [表示](https://developer.nvidia.com/topics/ai/nemotron)，Bolt 模型旨在“在笔记本电脑上运行日常的智能体任务，平衡处理多步推理、工具调用和网页浏览所需的速度与智能。”

尽管它们的规模截然不同且用途各异，但三者的核心都在于速度和效率。

两个较大的模型现已上市，而较小的 Bolt E4B 4G 模型将于近期推出。

## Nemotron 3.5 Super VL

这里最受瞩目的发布是 Nemotron 3.5 Super VL，这是一个拥有 1200 亿参数的模型，它将推理和工具使用与图像及文档理解结合在了一起。

在发布会上，Nvidia 负责开放模型和软件的副总裁 Kari Briski 指出，这个大型模型旨在提供“多模态智能体任务中的领先准确性——指令遵循、工具调用、多步业务工作流程和视觉理解——其性能可与 Nvidia 最大的推理模型相媲美，而参数量约为其五分之一。”

Super VL 建立在 3 月份发布的 [Nemotron 3 Super](https://thenewstack.io/nvidia-launches-nemotron-3-super-a-120b-open-model-for-large-scale-ai-systems/) 基础之上。两者总参数量均为 1200 亿，其中推理时活跃参数为 120 亿，上下文窗口高达 100 万个 Token。不过，早期模型仅接受文本输入，而 Super VL 现在增加了对图像和视频输入的支持（尽管不支持输出）。

## 与 Qwen 相比结果参半

然而，谈到[基准测试](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16#benchmarks)时，特别是与其他同等规模的开源模型相比，结果则参半。

在 Nvidia 自己的评估中，Super VL 在科学推理和终端任务上优于阿里巴巴的 Qwen3.5-122B-A10B，但在 SWE-bench Verified 和文档理解上的得分略低。

这五个测试分别是 GPQA-Diamond、Terminal-Bench 2.1、SWE-bench Verified、IFBench 和 MMLongBench-Doc。Super VL 在 Terminal-Bench 上的得分为 66.7，而 Qwen3.5 为 48.7，但在 SWE-bench Verified 上落后于对方（71.1 对 71.9）。

Qwen 拥有 1220 亿总参数和 100 亿活跃参数，而 Super VL 拥有 1200 亿总参数和 120 亿活跃参数。较新的 Qwen3.8-Flash-Next 在所有五项测试中得分更高，不过其额外的嵌入和预测组件使其总参数量达到约 1800 亿。

Thinking Machines 的 [Inkling-Small](https://huggingface.co/thinkingmachines/Inkling-Small) 拥有 2760 亿总参数和 120 亿活跃参数。它在终端任务上也落后于 Super VL，但在指令遵循方面得分更高。

Nvidia 还报告称，在 [Hermes Bench 和 LangChain 行为评估](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/#accuracy_and_efficiency_across_agent_tasks)中，Super VL 领先于 Ultra，得分分别为 63.44% 对 56.33% 以及 87.05% 对 84.3%。

不过总体而言，这里的重点显然是速度。

Nvidia [报告称](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/#accuracy_and_efficiency_across_agent_tasks)，在四个 B200 GPU 上完成 10,000 个 SWE-bench Pro 任务的速度快了四倍，尽管其图表显示的准确率低于 Qwen3.8-Flash-Next 和 DeepSeek V4 Flash。

![](https://cdn.thenewstack.io/media/2026/10/bc11fd18-nemotron-super-vl-figure-1-updated-1024x426.webp)

## 混合 Mamba 架构，更快的解码

至于 Nvidia 是如何构建该模型的，值得一提的是，Nemotron 联盟坚持使用 3.5 系列的混合架构，该架构结合了 Mamba-2、注意力机制和混合专家层——但增加了一个视觉编码器。根据其[模型卡](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)，Nvidia 还继续使用来自 Nemotron 3 Ultra 的蒸馏技术对语言模型进行训练，然后才针对软件工程、视觉和智能体任务进行进一步训练。

为了加速文本生成，Nvidia 还使用了 [LiLiCorr](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/#lilicorr_an_open_speculative_decoding_technique)（一种推测解码技术）。通过这种技术，较小的辅助模型可以提前草拟几个 Token，然后由 Super VL 一起检查，而不是逐个生成每个 Token。Nvidia 表示，与没有推测机制的解码相比，这使得 DGX Spark 上的 Token 生成速度提升了多达 2.3 倍。

对于文档工作流程，Nvidia 表示 Super VL 专注于光学字符识别、表格、图表和结构化信息。

在图表推理基准 [CharXiv](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/#combine_text_and_visual_understanding_in_one_workflow) 上，Nvidia 报告准确率为 80.8%，而 Nano Omni 为 63%。Python 代码解释将 Super VL 的结果提升至 84%。

## Bolt 在 24GB 中运行 74B 模型

如果您有兴趣运行本地模型，新的 Bolt 模型可能是这里最有趣的发布——它们的基准测试往往优于大多数同类模型。

Nemotron 3.5 Bolt 74B-A9B 24GB 衍生自 Super VL. 其混合专家架构在每次运行时激活其 740 亿个参数中的 90 亿个。

在 Nvidia 的[测试](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB#benchmarks)中，Bolt 在 Terminal-Bench 2.1 上的得分为 51.0，而以 BF16 测试的 Qwen3.6-35B-A3B 为 44.4，Gemma4 26B-A4B 为 37.2。Bolt 使用混合精度，包括两位专家（two-bit experts）。

为了达到这一规模，Nvidia 使用了两比特量化（two-bit quantization），将 74B 模型的内存占用减少到 24GB。该公司表示，它正在针对 RTX Spark 和 DGX Spark 系统优化该模型，支持 llama.cpp、Ollama、LM Studio 和 vLLM。

![](https://cdn.thenewstack.io/media/2026/10/401bdf3f-accuracy-1024x495.png)

Nemotron Bolt 3.5 24GB 基准测试。图片来源：Nvidia。

该模型的第二个、甚至更小的版本 Nemotron 3.5 Bolt E4B 4GB 计划于本月晚些时候推出。通过这款模型，Nvidia 的目标是 GeForce RTX、Jetson 和 Spark 硬件上的对话和物理智能体，包括需要多轮工具使用和应用程序状态感知的设备助手和交互式角色。

## 可用性

新模型现已在 Hugging Face 上以 [OpenMDW 1.1 许可证](https://openmdw.ai/license/1-1/)开放下载，该许可证允许商业使用和修改。