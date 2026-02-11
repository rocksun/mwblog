<!--
title: eBPF 进军 RISC 架构：ARM64 和 RISC-V 准备好了吗？
cover: https://cdn.thenewstack.io/media/2026/02/eae0ecf2-getty-images-d4edrcdovze-unsplash.jpg
summary: eBPF 正扩展至 ARM64 和 RISC-V。ARM64 已成熟，但 RISC-V 在 JIT 和内核支持上存在挑战，影响“一次编写，随处运行”。需加强标准化和物理硬件测试以弥合差距。
-->

eBPF 正扩展至 ARM64 和 RISC-V。ARM64 已成熟，但 RISC-V 在 JIT 和内核支持上存在挑战，影响“一次编写，随处运行”。需加强标准化和物理硬件测试以弥合差距。

> 译自：[The RISC architecture frontier: Is eBPF ready for ARM64 and RISC-V?](https://thenewstack.io/the-risc-architecture-frontier-is-ebpf-ready-for-arm64-and-risc-v/)
> 
> 作者：B. Cameron Gain

[扩展伯克利数据包过滤器 (eBPF)](https://thenewstack.io/what-is-ebpf/) 一直在普及的道路上前进，将其在内核中对[可观测性](https://thenewstack.io/introduction-to-observability/)、安全和网络功能的关键作用扩展到应用程序和环境部署的任何地方。自创建以来，它一直是将代码直接从内核并通过沙箱分发到整个网络的卓越方式。它能够收集信息并与网络上的代码和应用程序进行交互，基本上涵盖了由内核控制或连接到内核的任何代码或应用程序的全部范围。

鉴于 eBPF 在包括 Kubernetes 在内的各种环境中的广泛覆盖，eBPF 一直是可观测性、[安全监控](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/)和[网络](https://thenewstack.io/networking/)的福音。在可观测性与安全之间存在一些重叠，但 eBPF 的用例在很大程度上是截然不同的。由于我们将在下面探讨的原因，eBPF 在这两种情况下都尚未充分发挥其潜力。

但这在很大程度上与两件事相关：一切都源于 [Linux 内核](https://thenewstack.io/linux-6-18-all-about-the-new-long-term-support-linux-kernel/)，或者直接从 Linux 内核扩展而来，并且它最初是为 x86 CPU 配置设计的。最近，在广泛宣传中，eBPF 宣布将扩展到 Windows 系统。我无法理解为什么会有人想在 Windows 上运行他们的服务器，但它仍然是一个许多组织乐于使用的传统系统。

## ARM 和 RISC-V

eBPF 项目的开发者和维护者也已将 eBPF 扩展到 ARM 配置。同时，Mac M3 处理器和开源 RISC-V 处理器配置仍在开发中。

这是 DeepComputing 创始人兼首席执行官 [Yuning Liang](https://archive.fosdem.org/2025/schedule/speaker/yuning_liang/) 以及我上周末在 [FOSDEM](https://fosdem.org/2026/) 上的演讲“[RISC 上的 eBPF 可观测性：什么有效、什么失效以及如何测试](https://fosdem.org/2026/schedule/event/8SRBCB-ebpf_observability_on_risc_what_works_what_breaks_and_how_to_test_it/)”的主题。在演讲之前，我调查了 eBPF 在 ARM 和 RISC-V 配置上的现状。

“eBPF 具有变革性，并且大部分生态系统确实是在 x86_64 世界中发展起来的。虽然它被设计为与架构无关，但一旦你离开规范，遇到真实的内核、真实的 JIT 和真实的工作负载，差异就会迅速显现，尤其是在验证器行为、帮助器可用性和性能特征方面，” Grafana Labs 首席软件工程师 [Nikola Grcevski](https://ca.linkedin.com/in/nikola-grcevski-16796717) 告诉 *The New Stack*。

“我想补充的细微之处是，这并不意味着 eBPF 的承诺正在失败——这意味着它正在经受压力测试。ARM 已经表明，当有足够的生产压力时，该模型可以扩展到 x86 之外。RISC-V 现在是需要完成的工作最清晰的信号，” Grcevski 说。“从这个意义上说，你的表述是准确的：‘一次编写，随处运行’今天并非保证，而基于 RISC 的可观测性正是剩余差距（和机遇）最明显的地方。”

## 过渡期

我同意我们目前正处于一个过渡期，“一次编写，随处运行”在 RISC-V 上面临摩擦。然而，将其描述为“不可预测的未完成”忽视了为弥补这些差距正在进行的结构性工作。

eBPF 基金会和内核社区正在积极地将 eBPF 从“Linux 特定功能”转变为标准化的行业规范，[Bill Mulligan](https://www.linkedin.com/in/bamulligan)，[Cisco](http://cisco.com/?utm_content=inline+mention) [Isovalent](https://isovalent.com/) 的 [Cilium](https://cilium.io/) 和 eBPF 社区推广者告诉 *The New Stack*。随着互联网工程任务组通过 ([RFC 9669](https://www.ietf.org/blog/bpf-rfc9669/)) 对 eBPF 指令集进行标准化，现在有了一个关于 eBPF 是什么的正式契约，它独立于底层硬件。这表明你所描述的碎片化不是一个根本性缺陷，而是一个暂时的成熟度差距，随着 RISC-V JIT（即时编译器）与这个新标准对齐，这个差距正在迅速缩小，Mulligan 说。

“eBPF 基金会正在资助工作，以使不同架构相互媲美。重要的是不要将所有非 x86 架构一概而论。ARM64 已经有效‘毕业’了，” Mulligan 说。“由于 Graviton 和 Ampere 的大规模采用，ARM 现在是云原生世界的一等公民。RISC-V 才是真正的前沿阵地。”

一个组织通过将 eBPF 用于 RISC-V 系统上的可观测性和安全实验视为学习沙箱而非生产实验来启动一个沙箱项目，” Grcevski 说。

“该过程首先基于一个已知的 RISC-V 内核，以明确其能力。然后，从小处着手，使用 libbpf 和 CO-RE 进行一个可观测性和一个安全用例——重点关注具体的任务，如系统调用延迟和 execve 跟踪，” Grcevski 告诉 *The New Stack*。“最后，通过期望阅读内核和 JIT 代码、记录发现的差距并上游提交最小复现来及早关闭循环……我同意这种观点，因为虽然 eBPF 字节码在技术上是通用的，但其实现高度依赖于主机架构的特定 JIT 编译器和内核成熟度。”

Grcevski 补充道：

* JIT 对等性：x86_64 的 JIT 编译器是黄金标准；ARM64 几乎达到了，但 RISC-V 仍在追赶。如果 JIT 不支持特定的指令或帮助器，代码的“无关性”就变得无关紧要。
* 内存模型：RISC-V 和 ARM64 使用与 x86 不同的内存一致性模型。这可能导致依赖特定内存排序进行并发的复杂 eBPF 程序中出现细微错误。
* 生产压力：正如 Grcevski 所指出的，生态系统在资金和流量所在的地方得到改善。随着 RISC-V 进入数据中心，这些差距将会缩小，但我们目前正处于这种过渡的“蛮荒西部”阶段。

同时，ARM64 和 RISC-V 之间 JIT 编译成熟度的差异如何影响高频分析的 CPU 开销与传统 x86 部署相比，“这完全取决于生态系统飞轮，” Mulligan 说。“ARM64 已经全速运转，而 RISC-V 才刚刚开始转动这个轮子。我们没有看到根本性的障碍，只是一个新生态系统追赶几十年的领先优势的自然滞后，”他指出。

Mulligan 补充说，由于 ARM64 拥有大量的通用寄存器，其性能通常与 x86 无法区分。RISC-V 的 JIT 较新，有时可能导致比成熟的 x86/ARM 实现更冗长的指令序列。在高速分析（例如，每秒 10k+ 事件）中，这会导致每次探针执行的 CPU 使用率略高，Mulligan 说。“这通常是由于 JIT 编译器中生成的优化程度较低，”他补充道。

## 主要瓶颈

同时，考虑到 RISC-V 内核辅助支持的当前差距，eBPF 在新架构上普及的主要瓶颈是上游开发不足还是缺乏标准化的测试框架？“答案是两者兼有：eBPF 基金会正在考虑投资，使 RISC-V JIT 编译器与 x86/ARM 达到同等水平。内核社区也渴望支持 RISC-V，” Mulligan 说。

另一个问题是，大多数测试都是在 [Quick Emulator](https://www.qemu.org/) 上进行的，它模拟功能但隐藏了硬件特定的时序怪癖、缓存行为和 JIT 边缘情况，Mulligan 说。“我们需要一个更标准化的框架，在其中 eBPF 补丁能够自动在物理 RISC-V 芯片（而不仅仅是模拟器）以及 x86/ARM 运行器上进行测试，” Mulligan 指出。