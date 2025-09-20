<!--
title: 研究表明：eBPF并非网络应用的“万能灵药”
cover: https://cdn.thenewstack.io/media/2025/09/caa3ae4b-wouter-de-praetere-elfmdiihktg-unsplash.jpg
summary: ACM论文集研究质疑eBPF在加速网络工作负载方面的性能优势，指出其在许多情况下并未带来显著提升，甚至降低速度。研究人员建议改进即时编译、扩展ISA、添加调度程序和缓冲区等来优化eBPF技术。
-->

ACM论文集研究质疑eBPF在加速网络工作负载方面的性能优势，指出其在许多情况下并未带来显著提升，甚至降低速度。研究人员建议改进即时编译、扩展ISA、添加调度程序和缓冲区等来优化eBPF技术。

> 译自：[Research: eBPF Not Always a 'Silver Bullet' for Network Apps](https://thenewstack.io/research-ebpf-not-always-a-silver-bullet-for-network-apps/)
> 
> 作者：Joab Jackson

最新一期 [ACM 网络论文集](https://dl.acm.org/journal/pacmnet/charter) 上的一篇研究论文对 eBPF 的性能优势提出了质疑，至少在加速基于网络的工作负载方面是这样。

该论文指出，在许多情况下，eBPF 没有带来显著的性能提升，有时甚至会降低应用程序的速度，这篇论文名为“[揭秘 eBPF 网络应用程序的性能](https://dl.acm.org/doi/10.1145/3749216)”。

论文的作者 [Farbod Shahinfar](https://dl.acm.org/author/Shahinfar%2C+Farbod) 和 [Sebastiano Miano](https://dl.acm.org/author/Miano%2C+Sebastiano)（均来自意大利米兰理工大学）；纽约大学的 [Aurojit Panda](https://dl.acm.org/author/Panda%2C+Aurojit)；以及米兰理工大学和伦敦玛丽女王大学的 [Gianni Antichi](https://dl.acm.org/author/Antichi%2C+Gianni) 写道：“实际上，许多网络应用程序无法从 eBPF 中受益，更糟糕的是，eBPF 的使用会限制应用程序的部署方式。”

[eBPF](https://thenewstack.io/ebpf-has-a-bright-future-in-infrastructure-development/) 是一种通过沙箱和预编译将[编程代码嵌入](https://thenewstack.io/what-is-ebpf/)到操作系统内核本身的技术，其理念是它运行代码的速度比代码在用户空间程序中运行（与内核来回通信）的速度更快。在 eBPF 上运行的代码被编译为平台无关的字节码，并在加载时进行编译。

[![图表](https://cdn.thenewstack.io/media/2025/09/6ed35240-ebpf-demystifying-01.png)](https://cdn.thenewstack.io/media/2025/09/6ed35240-ebpf-demystifying-01.png)

*eBPF 程序的生命周期 (PACMNET)*

eBPF 在[许多网络功能](https://thenewstack.io/performant-and-programmable-telco-networking-with-ebpf/)中找到了早期应用，例如负载均衡、数据包交换和网络加速协议，它被用于过滤和路由数据包和遥测数据。

## 质疑 eBPF 的性能声明

研究人员建立了一系列基准来测试 eBPF [备受吹捧的性能提升](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/) 是否能够实现。

换句话说，研究人员想知道，如果将 eBPF 嵌入到网络应用程序中，它是否会运行得更快？

他们发现，实际上，卸载代码并不总能带来性能提升。

他们写道：“我们发现，应用程序性能是否提高取决于有多少逻辑可以被卸载。”

在某些情况下，他们发现性能有所提高，但在其他情况下，使用 eBPF 几乎没有区别。而在某些情况下，eBPF 实际上使性能变得更加迟缓，不仅对其应用程序如此，而且对其周围的其他应用程序也是如此。

## 基准测试不同的 eBPF 卸载类型

研究人员建立并测量了三种不同类型的基于 eBPF 的应用程序。一个完全在 eBPF 中运行（“**完全卸载**”）。另一个仅卸载代码中对时间最敏感的部分（“**快速路径卸载**”）——可以想到[数据库缓存](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/)。第三个使用 eBPF 来预处理数据（“**预处理卸载**”）。

这些测试在两台通过 100 Gbps 链路互连的 24 核 Intel Xeon 服务器上运行，这些服务器配备了 1.1MB 的 L1 缓存、30MB 的 L2 缓存和 36MB 的 L3 缓存，以及 128GB 的 DDR4 内存。它们都运行 Linux 内核版本 6.8.0-rc7。[Clang](https://clang.llvm.org/index.html), v 14，编译了字节码，目标是 [eBPF 指令集架构 v. 3](https://docs.kernel.org/bpf/clang-notes.html)。

对于**完全卸载**，结果好坏参半。操作单个数据包的应用程序受益，但操作流或消息的应用程序似乎没有通过 eBPF 路由得到改进。

事实证明，eBPF ISA 不支持许多处理器功能，例如单指令多数据 (SIMD)、加密卸载或浮点运算。因此，一些复杂的消息传递操作实际上在用户空间中运行得更快。

研究人员使用 [BMC](https://www.usenix.org/conference/nsdi21/presentation/ghigoff)（一个用于加速 Memcached 键值存储的 eBPF 程序）测试了**快速路径卸载**。

在这里，他们发现好处在很大程度上取决于 BMC 管理的工作负载类型。大量流量被卸载到 BMC 确实会看到更快的性能时间。但是，如果大部分流量需要由用户空间代码处理，那么任何好处都将微乎其微。

对于**预处理卸载**，研究人员发现 eBPF 程序可以通过预处理请求来潜在地减少数据移动。但这不一定会显着提高应用程序本身的性能。

[![图表](https://cdn.thenewstack.io/media/2025/09/59bb8264-ebpf-demystifying-02.png)](https://cdn.thenewstack.io/media/2025/09/59bb8264-ebpf-demystifying-02.png)

减小数据包大小并不能显着提高吞吐量。(PACMNET)

## eBPF 应用程序的“嘈杂邻居”效应

研究人员发现了其他令人不安的消息，即基于 eBPF 的应用程序可能会成为服务器上的不友好的邻居。通过控制操作系统内核，它们会阻碍运行在同一服务器上的其他应用程序的性能。eBPF 专为 Linux 设计，主要在那里使用，但 [Windows 版本](https://thenewstack.io/ebpf-is-coming-for-windows/) 也在开发中。

研究团队写道：“使用 eBPF 的应用程序可能会违反性能隔离。”

## 改进 eBPF 技术的建议

研究人员建议，eBPF 的维护者可以做几件事来减轻其技术的弊端。

一种是改进即时编译，由于操作系统内核的限制，即时编译通常会产生次优代码。即使是常见的操作，例如与内存之间复制（例如，memcpy）也是以低效的方式完成的，从而减慢了任何潜在的优化。

在某种程度上，eBPF 的维护者陷入了困境，因为这个问题不容易解决，“因为这样做会给内核增加显着的复杂性，”研究人员观察到。

尽管如此，他们可以改进生成机器代码的过程。可以扩展 eBPF ISA，包括增加对支持的寄存器数量的强烈要求。

还建议添加调度程序和缓冲区，并实现数据预取。

研究人员总结说，通过这些增强功能，eBPF 可以真正解决广泛的用例，这些用例将受益于更好的性能。

[计算机协会](https://www.acm.org/about-acm) (ACM) 是一个由志愿者领导的科学计算协会，旨在推动计算作为一门科学和一门职业的发展。

[eBPF 基金会](https://thenewstack.io/ebpf-finds-a-home-with-a-new-foundation/) 没有回复置评请求。