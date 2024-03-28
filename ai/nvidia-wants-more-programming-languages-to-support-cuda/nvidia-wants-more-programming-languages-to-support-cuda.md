
<!--
title: NVIDIA希望有更多支持CUDA的编程语言
cover: https://cdn.thenewstack.io/media/2024/03/4374a15f-woman-7780330_1280.png
-->

CUDA 并行计算平台可以使用 C++、Fortran 和 Python 进行编程，但该公司正在寻找其他人来运行其 GPU。

> 译自 [NVIDIA Wants More Programming Languages to Support CUDA](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/)，作者 Agam Shah。

NVIDIA 正在寻求扩展对更多编程语言的支持，因为它试图吸引更多开发者为其 GPU 编写应用程序。

该公司的 [CUDA 编程框架](https://thenewstack.io/how-nvidia-gpu-acceleration-supercharged-milvus-vector-database/) 目前支持的语言包括 C++、Fortran 和 Python。但新的编程语言正在不断发展，该公司热衷于向使用这些语言的开发者开放其 GPU 访问权限，NVIDIA 的 HPC 架构师 Jeff Larkin 在本月早些时候该公司 [GPU 技术大会](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/) 的技术会议上表示。

Larkin 没有提供有关正在考虑哪些编程语言的具体信息。

“我的团队肯定在监控这些语言，并试图寻找参与这些语言的机会。但 [C++、Fortran 和 Python] 是我们产品中今天专门支持的语言。我知道一些技术，我无法在这里提及，这些技术也将进一步支持更多语言，”Larkin 说。

Larkin给出了某些编程语言如何利用其 GPU 的一些示例，并提到了 Judia 和 [Rust](https://thenewstack.io/the-rust-community-matures-with-jetbrains-rustrover-ide/)。

## 为什么要切换到 GPU？

早期的编程模型围绕 CPU 展开。x86 架构是老大，而 GPU 则被降级为游戏和图形。

快进到今天，AI 已成为 GPU 的现实。NVIDIA 认为，CPU 在处理 AI 交易方面效率低下，而功耗更高的 GPU 将提供更多成本节约。

Larkin说：“通常，尽管 GPU 使用的功率更大，但它使用得更有成效，这就是你开始看到节省的地方。”“你的操作速度会更快，能效也会更高。”

NVIDIA 正在将其自己的基于 ARM 的 CPU（称为 Grace Hopper）与 GPU 紧密结合。但开发者 [需要 CUDA 才能充分利用 GPU](https://thenewstack.io/zluda-a-cuda-for-intel-gpus-needs-a-new-maintainer/)。

## CUDA 的工作原理

[NVIDIA GPU](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) 的核心是 Tensor Core，这是当今推动大多数 AI 计算的热门技术。Tensor Core 能够进行低精度数学和矩阵乘法，以进行 AI 计算。

矩阵计算风格建立在 GEMM 算法之上，该算法利用了 Tensor Core，并且是 NVIDIA AI 计算模型的核心。GEMM 算法与 CUDA 中的库配合使用，以便程序员与 GPU 核心进行交互。

这些库包括：

- **cuBLAS：** 这是 NVIDIA 首选的库，可直接访问 Tensor Core 并提供最大性能。“这是自 CUDA 诞生以来一直存在的、基本的工具，即线性代数 API，”CUDA 架构师 [Stephen Jones](https://developer.nvidia.com/blog/author/stjones/) 在 GTC 的演讲中说道。cuBLAS 提供了利用 GPU 性能的最简单方法。它自动配置 Tensor Core，开发人员无需调整参数，cuBLAS 开箱即用。
- **CUTLASS：** 更底层的 CUTLASS 库为编码人员提供了 C++ 和 Python 接口，以便使用 GPU 的 Tensor Core。开发人员可以控制 Tensor Core 的使用，这意味着开发人员的工作量更大。CUTLASS 与自动执行该过程的 cuBLAS 不同。NVIDIA 正在为 Python 开发人员构建更多工具以访问 CUTLASS，这是一项最新开发且正在进行中的工作。“你可以使用 PyTorch 扩展，因此你可以从 CUTLASS 发射 PyTorch 代码，并且可以自动将 CUTLASS 扩展 Tensor Core 自定义内核从 Python 引入 PyTorch，”Jones 说道。
- **cuBLASLt：** 此库介于 cuBLAS 和 CUTLASS 库之间，并为 Tensor Core 提供不同级别的控制。“CUTLASS 实际上调用中间的那个，cuBLASLt，你也可以自己访问。这是一个公共库。它提供了高级 API，你可以真正控制 Tensor Core 所做工作的更多方面，”Jones 说道。cuBLASLt 具有用于 GEMM 库的高级 API，为混合精度计算打开了大门，其中涉及混合和低精度计算。
- **cuBLASDx：** 这可以在设备端执行 cuBLAS 中选择的线性代数函数，从而提高性能和吞吐量。“这个想法是获取你的 cuBLAS 核心，只使用一个 GEMM 核心在你的内核中激活它，就像你使用 CPU 中的 cuBLAS 所做的那样，”Jones 说道。

## Python 是优先事项

NVIDIA 正在寻求将其 SDK 和框架的访问权限扩展到 Python，这为更多开发人员提供了可访问性。反过来，这将为其 GPU 带来越来越多的开发人员。

“着眼于 Python 堆栈，你必须全面投资，贯穿始终，”Jones 说道。

NVIDIA 希望使 Python “成为完整的 Nvidia 体验，并使 Python 开发人员和整个 CUDA 生态系统对 Python 程序员可用且可访问，”Jones 说道。

目标是向更多开发人员提供更多 SDK、框架和特定于领域的语言，位于[堆栈顶部](https://thenewstack.io/the-new-stacks-top-kubernetes-stories-of-2021/)。同时，对用户隐藏底层（加速库、系统库和实用程序以及设备内核）。Jones 说，这仍然是一项正在进行的工作。

NVIDIA 一直致力于将自己的库和工具与流行的 Python 框架（如 [PyTorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/)）集成在一起。

“JIT 编译在 Python 中非常重要，因为 Python 是一种非常依赖于运行时解释的语言，并且你不断动态生成数据。循环中的编译器完全正常。事实上，Python 解释器基本上就是其中之一，”Jones 说道。

## 编写好程序，收获回报

编程（并正确地进行编程）对于提高 AI 的能效非常重要。

公司正在衡量每笔交易的成本并试图降低成本。AI 存在加密问题——运行它需要大量能量——并且在 GTC 上，推理成本受到了密切关注。

Jones 认为，GPU 在最终方程式中更有效：在考虑机架空间、时间和功耗时，它们可以提供更多的 FLOPS（每秒浮点运算）。

“没有人关心你购买了多少服务器，没有人关心你租用了多少数据中心，你每月都在租用电力，因为电力是计算真正重要的指标，”Jones 说道。

NVIDIA 引入了新的数据类型 FP4 和 FP6，它们精度较低，但可以每瓦特榨取更多性能。

该公司在 GTC 上推出了一款代号为 Blackwell 的新 GPU。一款名为 DGX-B200 的新服务器有八个 Blackwell 芯片，功耗约为 1,000 瓦。它取代了 H100 GPU，后者是 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention)、Meta、Tesla 和其他公司 AI 计算工作的 GPU。

NVIDIA DGX 系统副总裁兼总经理 [Charlie Boyle](https://www.linkedin.com/in/charlie-boyle-0201a8/) 在一次采访中表示，与 DGX-H100 相比，DGX-B200 系统功耗相似，但性能提高了两到三倍。

## 没有更新 CUDA

NVIDIA 的硬件和软件模型很像 Apple 的：硬件和软件齐头并进。软件是为硬件设计的，反之亦然。

NVIDIA 试图将开发者锁定在 CUDA 中，这是一种专有开发模型。为此，NVIDIA GPU 支持其他编程模型，例如 [OpenAI 的 Triton](https://openai.com/research/triton) 和开源开发模型。

该公司的目标是将硬件和软件集成到所谓的“AI 工厂”中，其中输入是原始数据，输出是结果。客户看不到硬件和软件。

通常，NVIDIA 会随新 GPU 发布新版本的 CUDA。然而，Jones 在 GTC 会议期间没有提供 CUDA 的任何重大更新。NVIDIA 最近发布了 CUDA 版本 12.4，并可能在本月晚些时候分享更多详细信息，因为其 Blackwell GPU 的发布临近。
