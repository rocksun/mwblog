# RISC-V 在快速发展的处理器生态系统中找到立足之地

在 RISC-V 开源处理器架构能够在数据中心与 x86 和 ARM 架构一较高下之前，它需要从软件开发社区获得更多支持。本文对在巴塞罗那举行的 RISC-V 峰会进行了总结。

翻译自 [RISC-V Finds Its Foothold in a Rapidly Evolving Processor Ecosystem](https://thenewstack.io/risc-v-finds-its-foothold-in-a-rapidly-evolving-processor-ecosystem/) 。

![](https://cdn.thenewstack.io/media/2023/07/b351d998-hiker-geb2d245f9_1280-1024x768.jpg)
图片来自 Pixabay 的 Andrew Martin 。

开发者们从小就听说过 ARM 或 x86 是 PC 和服务器的核心，但现在出现了一种叫做 [RISC-V](https://thenewstack.io/risc-v-the-next-revolution-in-the-open-hardware-movement/) 的替代架构。

在接下来的几年里，一些公司将不可避免地推出运行在 RISC-V 处理器上的 PC 和服务器。这些系统很可能会运行在 Linux 上，因为据称微软并未开发适用于 RISC-V 架构的 Windows 操作系统。

但软件生态系统存在着很大的问题——开发者支持相当不足。[RISC-V International](https://riscv.org/) 正在开发该芯片架构，但其优先事项中更多谈及硬件，而对软件的关注相对较少。

## 初步支持

自近十年前出现以来，RISC-V 迅速得到了包括苹果在内的主要芯片制造商的[支持](https://thenewstack.io/open-source-hardware-the-rise-of-risc-v/)，苹果在其 Apple Silicon 中使用了 RISC-V 控制器。基于 RISC-V 的约 100 亿个芯片核心已经发货。最近， Meta [宣布](https://ai.meta.com/blog/meta-training-inference-accelerator-AI-MTIA/)了一款基于 RISC-V 架构的人工智能推理芯片。

该芯片架构通常被称为 Linux 的[硬件版本](https://thenewstack.io/risc-v-the-next-revolution-in-the-open-hardware-movement/)。它是一个建立在贡献文化和开源精神基础上的免费芯片技术，一个社区共同合作来开发和改进产品。

RISC-V 是一种免费许可架构，意味着任何人都可以将架构的一个版本分叉成自己的芯片。

采用 RISC-V 的芯片可以像乐高积木一样进行编译——企业可以采用基本架构，并在其上添加包括人工智能、图形或安全加速器在内的专有硬件块。

Calista Redmond 在上个月的巴塞罗那 RISC-V 峰会上发表主题演讲时表示：“曾经是一个实验、一个原型的东西，现在正在迅速投入生产。”

RISC-V 的结构使其适用于处理各种应用和复杂计算需求的云原生环境。

其最基本的指令被设计为快速将应用程序转移到像 GPU 或专用数学处理器等加速器中，这些加速器在此类任务上表现优异，如人工智能和分析。

Intel 和 AMD 的芯片已经接近物理极限，而 [RISC-V 的灵活性](https://thenewstack.io/open-source-risc-v-serving-a-side-of-software-with-chips/)为计算机带来了未来的发展方向。

例如，RISC-V 为新的硬件架构提供了一条路径，如稀疏计算，该计划正在由美国情报高级研究计划局研究，其中处理单元更接近存储或内存中的数据。

巴塞罗那超级计算中心提出了在 RISC-V 芯片中合并 CPU 和内存的概念，这将减少机器学习应用程序带来的内存瓶颈。

BSC 的研究员 [Umair Riaz](https://www.linkedin.com/in/umair-riaz871/?originalSubdomain=es) 提到：“我们希望它实际上是在内存附近执行内存密集型操作，比如 memcpy 。”他还提到 spinlock 函数，并表示在内存中执行这些操作将更高效更快速。

对于这种复杂的 RISC-V 芯片编写应用程序，即使是最勇敢的想直接针对硬件编码的程序员也可能会感到吃力。但 Intel 希望为开发人员提供所需的工具，以便在模拟的 RISC-V 环境中开始测试应用程序。

## OneAPI

英特尔的 Codeplay 软件部门最近宣布了 OneAPI Construction Kit ，其中包括开发人员在模拟的 RISC-V 环境中测试代码的工具，这些工具可以在 x86 PC 上运行。

Construction Kit 的主要特点是对 SYCL 的支持，这使得开发人员能够编写和编译不考虑硬件架构的应用程序，而英特尔正在迈出将 RISC-V 支持引入并行编程框架的第一步。

该套件包括对英特尔的 DPC++/C++ 编译器的支持，它允许将 C++ 代码重新编译以在多个硬件架构上使用。

开发者还可以在类似 Raspberry Pi 的开发板或 [Milk-V](https://milkv.io/)、[StarFive](https://www.starfivetech.com/en/site/boards) 等公司的系统上测试 RISC-V 代码。这两家公司提供支持 Linux 的高性能 64 位 RISC-V 系统。

[RISC-V](https://sites.google.com/riscv.org/software-ecosystem-status) 在 Linux 上的支持程度不高。只有少数几个软件包得到了完全支持，其中包括 Ubuntu 操作系统、Gnu 工具链、OpenvSwitch、Apache Nuttx 和 Mozilla 的 Spidermonkey 。

对于 RISC-V 的许多软件包来说，它们运行得还算不错，但仍未得到完全支持。例如，中国的 RISC-V 开发社区报告称，现在在开源 Fedora 上有超过 80% 的软件包得到了 RISC-V 的支持。

一些重要的软件包，如 Pytorch、GCC、TensorFlow 和 OpenJDK ，可以运行，但尚未完全支持。对于 LibreOffice 和 Firefox 等开源应用程序的支持正在逐步增加。谷歌正在加快对 RISC-V 的 AOSP（Android开源项目）的支持，这将是下一个架构规范的重要部分。

RISC-V 服务器芯片制造商 [Esperanto Technologies](https://www.esperanto.ai/) 和 [Ventana Micro Systems](https://www.ventanamicro.com/) 已宣布推出用于云计算的服务器芯片，但对于软件支持或编程模型的讨论并不多。Esperanto 已将 Meta 的 Open Pre-Trained Transformer 模型移植到其 RISC-V 服务器上。

正在开发架构规范的 RISC-V 国际组织正在尝试通过建立 RISC-V 软件生态系统（也称为 RISE ）来解决这一问题，以为 RISC-V 系统创建基础软件工具和中间件。最初的支持者包括谷歌、英特尔、英伟达、高通、三星和 Ventana 等公司。

RISC-V 国际组织的首席技术官 [Mark Himelstein](https://www.linkedin.com/in/heavenstone/) 在峰会上谈到 RISC-V 借鉴了 Linux 文化的文化根源，参与者为共享利益做出贡献。

Himelstein 表示：“这种贡献文化意味着在 RISC-V 和其他开源和开放标准社区中实现上游合并。”他还补充说：“这并不意味着你正在从事那些快速成为商品化的拼图块。”

此外，RISC-V 并没有硬件和软件共同设计的结构，这使得开发人员更容易使用 x86 和 ARM 系统。RISC-V 首先开发硬件规范，而 Linux 兼容性则稍后出现。这与英特尔截然不同，后者在芯片发布前就将 Linux 驱动程序上游化，以确保硬件与最新版本的操作系统兼容。

## 中国方面

RISC-V 的软件努力也缺乏像 Linus Torvalds 那样能够凭借意志力推动项目前进的强大力量。RISC-V 也没有足够的主流地位来吸引大量开发者。

但在中国情况不同，中国正在大规模采用 RISC-V 来创建本土芯片，并减少对西方技术的依赖。中国的开发者正在投入工作，为 RISC-V 兼容的 Linux 操作系统做出贡献。

他们的动力很简单——中国的 RISC-V 计划受到工程技术的驱动，而非政治，开发者们有充足的动机来构建操作系统支持，特别是由于出口限制导致最新的西方芯片技术不为人所知。

中国公司正在开发一些最复杂的 RISC-V 芯片，并且社区每天都在增加对更多软件包的支持。Fedora、Debian、Gentoo 和 Arch Linux、GNU 工具链以及 Clang 等的许多核心贡献者都来自中国。

中国的 RISC-V 社区还在发起一项基层倡议，将对 RISC-V 处理器提供对 AMD 的并行编程框架 ROCm 的支持。AMD 没有回应有关其是否参与将 ROCm 移植到 RISC-V 的请求。