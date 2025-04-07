<!--
title: NVIDIA终于为CUDA添加了原生Python支持
cover: https://cdn.thenewstack.io/media/2024/02/467cc713-python-logo-square.jpg
summary: NVIDIA 拥抱 Python！CUDA 迎来原生 Python 支持，告别 C/C++，AI 开发者福音！新编程模型 CuTile 接口更易理解和调试，加速 C++ 库无缝衔接，性能媲美底层 C++ 代码。拥抱 Pythonic CUDA 堆栈，引爆 GPU 加速！
-->

NVIDIA 拥抱 Python！CUDA 迎来原生 Python 支持，告别 C/C++，AI 开发者福音！新编程模型 CuTile 接口更易理解和调试，加速 C++ 库无缝衔接，性能媲美底层 C++ 代码。拥抱 Pythonic CUDA 堆栈，引爆 GPU 加速！

> 译自：[NVIDIA Finally Adds Native Python Support to CUDA](https://thenewstack.io/nvidia-finally-adds-native-python-support-to-cuda/)
> 
> 作者：Agam Shah

根据 [GitHub 2024 年开源调查](https://github.blog/news-insights/octoverse/octoverse-2024/)，2024 年，Python 成为世界上最流行的编程语言，超过了 JavaScript。

多年来，NVIDIA 的 [CUDA](https://developer.nvidia.com/cuda-toolkit) 软件工具包一直没有原生 Python 支持。但现在情况已经改变。

在 GTC 上，NVIDIA 宣布在其 CUDA 工具包中原生支持并完全集成 Python。开发人员将能够使用 Python 在 GPU 上直接执行算法风格的计算。

“我们一直在努力将加速的 Python 作为头等公民引入 CUDA 堆栈，” CUDA 架构师 [Stephen Jones] 在最近的 GTC 会议的演讲中说。

对于程序员来说，这意味着巨大的影响。CUDA 诞生于 C 和 C++，现在程序员不需要了解这些编程语言就可以使用该工具包。

“CUDA 的 Python 不应该看起来像 C。它应该看起来像 Python，”Jones 说。

> “CUDA 的 Python 不仅仅是将 C 翻译成 Python 语法。”
>
> — Stephen Jones, CUDA 架构师

程序员可以使用自然的 Python 接口和调用函数和库的脚本模型来创建 AI 程序，以便在 NVIDIA GPU 上执行。

“CUDA 的 Python 不仅仅是将 C 翻译成 Python 语法。它必须是 Python 开发人员觉得自然的东西，”Jones 说。

## 原生 Python 打开了新的大门

NVIDIA 对 CUDA 上的 Python 的原生支持为数百万开发人员打开了开发工具包。CUDA 以前要求开发人员了解 C++ 或 Fortran。该编程工具包有一些 Python 工具，但它不是原生支持的。

据 The Futurum Group [称](https://futurumgroup.com/insights/ai-in-context-uxl-to-be-an-open-source-alternative-to-nvidias-cuda/)，CUDA 用户数量在 2023 年仅为 400 万，高于 2020 年的 200 万。但 Python 是世界上增长最快的语言。NVIDIA 将能够接触到数百万 Python 程序员——尤其是在印度和巴西等发展中国家，这些国家的程序员为开源项目做出了热情的贡献。

Python 支持还将使 NVIDIA 的基础设施可以在新兴市场中使用。NVIDIA GPU 的大部分位于美国和欧洲，但印度的电信和基础设施公司正在建设主要的 GPU 装置，这些装置将在未来几年内投入使用。

NVIDIA 正在加大力度招募程序员，并希望[支持更多编程语言](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/)，包括 Rust 和 Julia。

## Pythonic CUDA 是如何构建的

CUDA 包括库、SDK、编译器、主机运行时、工具以及预打包的软件和算法。NVIDIA 已将各个部分添加到整个 [Pythonic CUDA 堆栈](https://nvidia.github.io/cuda-python/latest/)。

NVIDIA 的重点是在不脱离 Python 的情况下提供 GPU 加速。CUDA Python 不能仅仅是内核产品；它需要堆栈中的所有内容和流畅的执行流程，Jones 说。

“你必须能够编写一个内核并将其放入 PyTorch 中，但你还必须能够调用 Pythonic 库以及所有其他东西，”Jones 说。

实际上，编译器层没有任何东西，因为它围绕即时 (JIT) 编译构建。这大大减少了堆栈中 GPU 的树中的依赖项数量。

“保持所有层之间的互操作性将大大提高生产力，并能够端到端地使用 Python，”Jones 说。

最初，NVIDIA 构建了基本 Python 绑定（包括运行时编译器）和 Python 库，例如 cuPyNumeric，它是 NumPy 的直接替代品，NumPy 是 Python 中使用最广泛的计算库。cuPyNumeric 仅更改一个导入指令，NumPy 代码从在 CPU 上运行变为在 GPU 上运行。

> CUDA Core 是“对 CUDA 运行时的 Pythonic 重新构想，使其自然且原生于 Python”。
>
> — Stephen Jones, CUDA 架构师

在过去的一年中，NVIDIA 制造了 [CUDA Core](https://nvidia.github.io/cuda-python/cuda-core/latest/)，Jones 说这是“对 CUDA 运行时的 Pythonic 重新构想，使其自然且原生于 Python”。

CUDA Core 具有 Python 的执行流程，该流程完全在进程中，并且严重依赖 JIT 编译。

“你不应该退出命令行编译器或任何类似的东西，你应该完全在进程中，”Jones 说，并补充说，这大大减少了堆栈中 GPU 的树中的依赖项数量。

NVIDIA 创建了一个名为 NVMath Python 的库，该库具有用于主机端和设备端库调用的统一接口。Jones 说，融合库调用的能力带来了很大的性能提升。

该公司还构建了可以直接从 Python 代码访问加速的 C++ 库的库。

“因为这位于我们多年来构建的基础设施之上……我们没有在 Python 中重新实现这些。我们确保它链接到底层微调的 C++ 代码，因此 [that] 您的性能差异可以忽略不计，”Jones 说。

NVIDIA 还添加了用于分析器和代码分析器的工具。

## 编程模型

Python 使编码变得简单，编码人员不必过多担心底层硬件。考虑到这一点，NVIDIA 正在添加一个编码层，该层与在 GPU 上执行的更高级别的抽象保持一致。

新的编程模型，称为 CuTile 接口，首先为 Pythonic CUDA 开发，随后将推出 C++ CUDA 的扩展。

CuTile “从根本上来说更柏拉图式”，因为今天的 Python 程序员更多地考虑数组而不是线程（这更像是 C++ 的特征）。

开发人员无法神奇地获取 Python 代码并将其导出以进行 GPU 加速。CUDA 通常会获取一个问题并将其分解为数千个较小的块，这些块在 GPU 上单独处理。

这些块被分解成更小的瓦片，这些瓦片运行数千个线程来处理单个元素。这些线程组合成一个单一的操作。

能够一直向下处理线程级别的单个元素，并行地赋予 GPU 强大的计算能力。

但 NVIDIA 认为 GPU 执行不需要一直下降到线程级别。处理也可以在瓦片级别进行，这就是 CuTile 编程模型适合的地方。

与 C++ 不同，Python 在设计上不是粒状的。

CuTile 在较低的粒度级别上将数组映射到 GPU 上，从而使代码更易于理解和调试。“从根本上说，它的性能是一样的，”Jones 说。

瓦片中的数据可以构造为向量、张量或数组。编译器可以更好地将整个数组操作从一个线程块映射到 GPU。

“通常，编译器会比我做得更好，因为编译器深入了解我在做什么……[and] GPU 运行的细节，”Jones 说。

> 与 C++ 不同，Python 在设计上不是粒状的。

“有很多这样的东西。OpenAI 的 Triton 将是一个很好的例子。我认为这些非常适合 Python 程序，”Jones 说。