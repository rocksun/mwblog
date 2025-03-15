# Strobelight：Meta 用于大规模基础设施的 eBPF 分析器框架

![Featued image for: Strobelight: Meta’s eBPF Profiler Framework for Massive Infra](https://cdn.thenewstack.io/media/2025/03/f405a7c5-strobelight-1024x676.jpg)

想象一下，你负责监控 [Meta 的大规模基础设施](https://thenewstack.io/how-meta-is-reinforcing-its-global-network-for-ai-traffic/)。这想想就很可怕，不是吗？现在，Meta 的工程团队取得了一项突破性进展，他们成功地利用 [eBPF](https://thenewstack.io/what-is-ebpf/) 技术来增强其全公司范围内的分析器 [Strobelight](https://engineering.fb.com/2025/01/21/production-engineering/strobelight-a-profiling-service-built-on-open-source-technology/)。

当我说“增强”时，我指的不是只有专业的性能工程师才会喜欢的细微改进。不，我指的是“[CPU 周期减少 20%](https://ebpf.foundation/case-study-metas-strobelight-leverages-ebpf-to-reduce-cpu-cycles-and-server-demands-by-up-to-20/)，相当于 Meta 顶级服务所需的服务器数量减少 10-20%”。这在计算方面节省了很多，相当于在资金方面节省了很多。

Strobelight 是 Meta 的全公司范围内的分析器框架，旨在为公司的大规模基础设施提供全面的分析能力。它由多个子分析器组成，这些子分析器收集各种类型的性能数据，包括 CPU、GPU 和内存配置文件。该框架的首要任务是识别性能瓶颈并优化 Meta 机器集群中的资源利用率。

Strobelight 最近成功的关键在于集成 eBPF。它支持在 Linux 内核中直接进行高效、低开销的监控和系统事件跟踪。通过[利用 eBPF](https://thenewstack.io/bytedance-to-network-a-million-containers-with-netkit/)，Strobelight 现在可以以对系统资源的最小影响来收集性能数据。

确切地说，根据 [eBPF 基金会](https://ebpf.foundation/) 的说法，[eBPG 使 Meta 能够跟踪](https://ebpf.foundation/case-study-metas-strobelight-leverages-ebpf-to-reduce-cpu-cycles-and-server-demands-by-up-to-20/)在函数调用和执行路径中花费的 CPU 时间；本机和非本机语言（例如，Python、Java 和 Erlang）的调用堆栈；关闭 CPU 时间和服务请求延迟分析；以及 AI/GPU 分析和内存跟踪。

## eBPF 节省成本

除了节省计算时间和现金外，[eBPF 基金会](https://ebpf.foundation/) 声称，在 Strobelight 中使用 eBPF 还通过一个字符的代码更改，每年节省了相当于 15,000 台服务器的容量。这让我印象深刻。它还可以更快地进行调试和性能分析。这使工程师能够在回归到达生产环境之前阻止它们。

借助 eBPF，[Strobelight 现在可以跟踪 GPU 内存分配](https://www.youtube.com/watch?v=5xAghByteYc)并更有效地检测内存泄漏。Meta 软件工程师 Riham Selim 表示，eBPG 可以在任何时间点了解每个 GPU 的内存分配情况。

请注意，eBPF 并不完美。Selim 指出。它缺乏对 GPU 内部结构的可见性；大量的数据可能会让人不知所措；并且它缺乏特定于应用程序的理解。因此，例如，您需要将可观测性代码添加到 [PyTorch 程序](https://thenewstack.io/official-pytorch-documentary-revisits-its-past-and-its-future/)中，而不是仅仅依赖 eBPF。

因此，重要的是要理解 Strobelight 远不止 eBPF。根据 Meta 的说法，“Strobelight……不是一个单一的分析器，而是许多不同分析器（甚至是临时分析器）的协调器，它在 Meta 的所有生产主机上运行，收集有关 CPU 使用率、内存分配和正在运行的进程的其他性能指标的详细信息。”

事实上，Strobe Light 总共有 42 个不同的分析器。其中大多数（但并非全部）都基于 eBPF。

## 安全注入自定义代码

因此，eBPF 对于 Strobelight 至关重要。Meta 工程师指出，“eBPF 允许将自定义代码安全地注入到内核中，这使得以非常低的开销收集不同类型的数据成为可能，并在可观测性领域释放了如此多的可能性，以至于很难想象没有它 Strobe Light 将如何工作。”

不要问我你怎么做。我对[可观测性](https://thenewstack.io/observability/)略知一二，如果没有 [eBPF](https://thenewstack.io/ebpf/)。我什至不知道从哪里开始。幸运的是，由于我们有 eBPF，因此我们不必担心这一点。
想亲自尝试一下吗？你可以的。StrobeLight 的大部分内容最近已在 Apache 2 许可下开源。然而，Meta 尚未开源 Strobelight 的分析器和库。该公司承诺将会这样做，因为通过开放它们，它们将变得“更加强大和有用”。即便如此，这里已经有足够的开放内容，对于任何想要密切关注大型基础设施系统的人来说，Strobelight 仍然值得探索。

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)