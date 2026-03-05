[RISC-V](https://thenewstack.io/risc-v-finds-its-foothold-in-a-rapidly-evolving-processor-ecosystem/) 标准已经发展成熟，与经过长期检验且价格昂贵的 Arm 和 x86 处理器相比，其性能劣势已基本消失。

这对于那些寻求更具成本效益的芯片编程方式，或希望优化芯片 CPU 性能的开发者来说是个好消息——不仅因为 Arm 授权费用高昂，还因为可以自由实现指令集，无需每次都获得 Arm 的许可。

这一点，加上其固有的矢量能力，使得 RISC-V 特别适合 AI 应用，因为 AI 需要多个进程并行运行——RISC-V 特别适合处理这种工作负载。

也许芯片层面 AI 最被低估和鲜为人知的里程碑时刻之一是去年 [Nvidia 的计划](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/) 公布——具体来说，就是 [CUDA](https://thenewstack.io/nvidia-making-radical-changes-to-cuda-after-nearly-20-years/) 将支持 RISC-V 指令集。同样在去年，Linux 内核更新了 RISC-V 的实现驱动和补丁，补齐了长期以来推动向开源 RISC-V 设备迁移的最后一个基本要素。[Canonical 的 Ubuntu](https://thenewstack.io/canonical-extends-ubuntu-linux-support-for-up-to-15-years/) 也支持 RISC-V。

这意味着开发者和设备制造商现在可以像使用 x86 和 Arm 处理器一样，对兼容 Linux 并结合 Nvidia CUDA GPU 的 RISC-V 处理器进行编程和实现指令集。这在相对昂贵的 CPU 和 Arm 处理器短缺，而 RISC-V 替代方案如今更便宜的时候，带来了显著的推动作用。

Nvidia 在其文档中并未对此进行大量评论，也未回复寻求澄清的信息，但 [RISC-V 国际](https://thenewstack.io/open-source-risc-v-serving-a-side-of-software-with-chips/) 组织对此进行了广泛报道。

需要注意的是，尽管这显然可能对 AI 开发带来福音——特别是对于大量 RISC-V 表现出色的边缘和嵌入式设备——Nvidia 尚未正式声明此支持是专门作为一项主要的 AI 扩展战略。即便如此，开发者现在可以在 Nvidia GPU 上随意为 AI 创建和实现指令集——无需担心 Arm 和 x86 的授权和成本。

“AI 框架不断变化，而 CUDA 占据主导地位，”RISC-V OEM [DeepComputing](https://deepcomputing.io/) 的创始人兼 CEO Yuning Liang 告诉我。“新框架层出不穷。而在这所有一切之中，软件仍然是关键。”

工程师们在 RISC-V 处理器上做他们想做的事情，与使用 Arm 和 Intel 或 AMD 的 CPU 许可证完全不同。“过去，你无法要求 Intel 做任何事情。你只能被困住。但现在有了 RISC-V，你可以尽情发挥想象力，做任何你想做的事，并将其做到最好，”他说。

## 没人预料到这一点

在 AI 热潮、LLMs 和谷歌著名的 Transformer 研究论文出现之前，“没人预料到这一点。”“在 AI 出现之前，我不知道 RISC-V 高性能 SoCs 会走向何方，”Liang 说。“幸运的是 AI 来了，所以我们全力投入 AI。”

在 [RISC-V 国际 2025 年年度报告](https://riscv.org/wp-content/uploads/2026/01/RISC-V-Annual-Report-2025.pdf)中，RISC-V 首席架构师 Krste Asanović 评估了年末的状况以及 2026 年将带来的变化：

“在 2025 年，我们进一步努力，发起了有针对性的宣传活动，阐明 RISC-V 的独特特性如何解决特定垂直市场中的特定挑战，”他说。“因此，RISC-V 现在已牢固地成为关键领域决策者的词汇、路线图和采购选择的一部分。今天，我们专注于多个关键垂直领域。”

“在嵌入式和物联网领域，我们已经有了显著的部署。在数据中心和汽车领域，我们看到对通用 RISC-V 计算的兴趣日益增长。同时，在插槽量较小但能力要求较高的市场，如航天和高性能计算 (HPC)，已经提供了巨大的机会。”

当然，还有 AI。“与安全性一样，AI 横向贯穿每个垂直领域，”Asanović 说。“2025 年发生了巨变，可以肯定地说，我见过的几乎每个新的 AI 加速器项目都在使用 RISC-V。这并非偶然：我们从一开始就设计 RISC-V 来支持标量、矢量和矩阵计算，所以它就是能行。相同的核心可以处理控制和数字工作负载，跨性能层扩展，并随 AI 发展。所有主要的行业参与者都开始认识到 RISC-V 将很快成为主导的开放 ISA。在如此多的垂直市场中，我们已经超越了‘是否’的问题。现在的讨论是关于 RISC-V 将如何、何时以及何地被采用。”