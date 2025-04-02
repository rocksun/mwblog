# 英伟达在近 20 年后对 CUDA 进行重大变革

![Featued image for: NVIDIA Making Radical Changes to CUDA After Nearly 20 Years](https://cdn.thenewstack.io/media/2025/04/23ecc719-boliviainteligente-zs3s9a3jeq-unsplashb-1024x576.jpg)

英伟达宣布将对其 [CUDA](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/) 的运行方式进行全面变革。它还将改变程序员为公司炙手可热的 [GPU](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) 构思和编写 AI 程序的方式。

过去是为独立 GPU 创建运行时，但现在英伟达希望为成千上万的 GPU 创建一个单一运行时。

“我们一直在讨论编程 *a* GPU——我如何让我的程序在一个 GPU 上运行。但现实是没有人再在一个 GPU 上运行了，”英伟达 CUDA 架构师 [Stephen Jones](https://www.linkedin.com/in/stephen-jones-profile/) 在公司最近的 GTC 大会上的一次技术会议上说。

现在，AI 是在成千上万的 GPU 上协同完成的。

“因为未来是这种大规模的数据中心计算，所以我将致力于多节点 CUDA [runtime]，”Jones 说。

英伟达内部正在进行的思考是构建一个跨越整个数据中心的单一运行时系统，而不是独立的 GPU。英伟达已将下一代产品命名为 CUDA DTX，即 CUDA 分布式执行。

“我实际上是在告诉你两年后的事情。我不知道最终会是什么样子，”Jones 说。

英伟达很少谈论 CUDA 的未来，因此当英伟达透露它正在 GTC 上开发下一代 CUDA 时，这有点令人震惊。

在当今的 AI 世界中，无法逃避 [CUDA](https://developer.nvidia.com/cuda-toolkit)。该公司的 GPU 无处不在，即使主要围绕开源工具构建，编码人员也会在编程堆栈中的某个地方遇到英伟达的 CUDA 工具。

如果没有 CUDA 框架，英伟达的 GPU 基本上无法用于 AI，该框架包括库、编译器、运行时和内核。至少，编码人员需要学习如何加载名为 [CuDNN](https://developer.nvidia.com/cudnn) 的神经网络库，才能使用英伟达的 AI 创作工具。

主要的 AI 框架 TensorFlow 和 PyTorch 针对英伟达的 GPU 进行了优化。AMD 的 GPU、Apple Mac 或替代 AI 芯片不需要英伟达的 CUDA 堆栈，但这很少见，因为英伟达的硬件和软件正在推动当今的 AI 发展。

英伟达通常对其 CUDA 编程工具的计划守口如瓶。但它会随着每个新的 GPU 架构发布新版本的 CUDA。CUDA 12——早在 2022 年 [发布](https://thenewstack.io/cuda-12-harnesses-a-nvidias-speedier-gpu-architecture/)，现在是 12.8 版本——是基于 Hopper 架构的。

没有 CUDA 13 的迹象，它应该与 Blackwell 一起发布，Blackwell 是一种取代 Hopper 的新 GPU 架构。该公司尚未谈论该版本。

“CUDA 遵循语义版本控制，因此我们会根据 API 和 ABI 的更改更新版本。当我们引入 Stephen 在他的演讲中谈到的新功能时，我们不希望更改 CUDA 名称或版本控制方法，”英伟达的一位女发言人告诉 The New Stack。

英伟达 CEO 黄仁勋将数据中心设想为一个巨大的 GPU，其中包含成千上万个芯片。这与 CUDA DTX 的愿景一致，CUDA DTX 是一个跨越成千上万个 GPU 运行的单一运行时。这也具有商业意义——英伟达在最近一个季度通过 Blackwell GPU 销售额获得了 110 亿美元的收入。

该公司正在构建 [massive servers](https://thenewstack.io/after-deepseek-nvidia-puts-its-focus-on-inference-at-gtc/) 封装了大量的 GPU。今年的 GB300 NVL72 服务器系统具有 72 个下一代 Blackwell Ultra GPU，以及庞大的 DGX SuperPod，它将通过连接多个 DGX B300 系统来连接 576 个 Blackwell Ultra GPU。

CUDA 将程序分解为数千个较小的块，这些块在 GPU 上单独处理。块进一步分解为数千个线程，这些线程组合成一个单一操作。批量并行性为 GPU 提供了强大的计算能力。

当前版本的 CUDA 是在较低级别上所有加速应用程序和硬件执行的融合。英伟达正试图在 CUDA DTX 中将应用程序连接到不同的硬件。

“当我考虑分布式 CUDA 时，我认为我们需要考虑分布式机器模型和分布式运行时，”Jones 说。

当在 100,000 个节点上运行一个大型 CUDA 运行时时，可能会出现一系列问题，他补充说。“在规模上运行良好的东西不一定在单个 GPU 上运行良好，”Jones 说。
分布式运行时必须是动态的，以便处理和管理硬件资源、拓扑以及在由成千上万个 GPU 组成的复杂结构上的执行。“它必须具有弹性。如果我有一台 10 万节点的机器，总会有东西宕机……这种情况每天都在发生，”他说。

Jones 进一步阐述了分布式 CUDA DTX 及其架构的考虑因素，该架构围绕两个核心组件构建。

第一个是统一机器模型，其中 GPU、CPU、网络、加速器和其他芯片看起来都一样。这意味着开发人员只需编写一次应用程序，而不是为每个芯片编写多次。

“CUDA 的工作是在不影响你能从中获得的性能的情况下，统一机器的功能，”Jones 说。

他指出，机器模型对于将 GPU 视为一个 GPU 而不是不同的硬件至关重要。

Jones 在这里指出，NVIDIA 作为硬件和软件制造商具有优势。该公司可以协商它在硬件和软件中放入的内容。

CUDA DTX 的第二部分是“统一运行时”，其中启动指令/API，创建工作并管理资源、拓扑和执行。

分布式运行时包括异步执行，涉及管理分布式 GPU 网络上的并行操作。

“如果我必须在不同的硬件上以不同的方式分配内存，你会疯掉的，”Jones 说。

Jones 重申 CUDA DTX 的最终设计可能会改变。他还表示，NVIDIA 有“忍者”负责后端工作，以便程序员可以专注于插入 CUDA 并创建应用程序。

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)