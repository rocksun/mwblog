# 使用 Rust 在 eBPF 中捕获性能回归：简介

开发团队应尽可能将性能回归的检测尽早进行。以下是使用连续基准测试工具 Bencher 的方法。

翻译自 [Catch Performance Regressions in eBPF with Rust: Intro](https://thenewstack.io/catch-performance-regressions-in-ebpf-with-rust-intro/) 。

![](https://cdn.thenewstack.io/media/2023/06/2afcb580-shutterstock_2-1024x683.jpg)

*这是一个由五部分组成的系列文章的第一部分。在此阅读第二部分。*

扩展伯克利数据包过滤器（eBPF）在不需要维护内核模块的麻烦情况下，用于扩展Linux内核的功能。从高层次来看，[eBPF](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/) 是 Linux 内核中运行特殊类型字节码的虚拟机。要创建一个 eBPF 程序，需要将诸如 C、C++ 和 Rust 等语言的源代码编译为 eBPF 字节码，然后将该字节码加载到内核中。然后，内核使用 eBPF 验证器对字节码进行检查。

eBPF 验证器评估 eBPF 字节码；它基本上需要解决其中的[停机问题](https://en.wikipedia.org/wiki/Halting_problem)。这是非常重要的一步。验证确保 eBPF 程序不会使内核崩溃。因此， eBPF 在其允许执行的操作上有一些限制。所有程序都限制为一百万条指令；没有无限循环，也没有在 eBPF 内部等待用户空间事件的方式。

一旦 eBPF 字节码经过验证，就可以将其加载到 eBPF 虚拟机中，在内核中运行。 eBPF 程序可以在内核中执行多种不同的任务：跟踪系统调用，探测用户空间，探测内核函数，对 Linux 安全模块（LSM）进行工具化，以及过滤数据包，其中最初的用例是最后一个。当时它只是伯克利数据包过滤器（BPF）。随着时间的推移，随着添加了新的用例，它变得被称为扩展BPF。现在，由于存在众多可能的应用程序，该缩写已被废弃，取而代之的是 eBPF ，现在[只是一堆字母，表示 eBPF](https://ebpf.io/what-is-ebpf/#what-do-ebpf-and-bpf-stand-for) 。

![](https://cdn.thenewstack.io/media/2023/06/d53ebe15-screenshot-2.jpg)

有几种不同的语言和工具集可用于使用 eBPF 。一个基础性的工具是 [libbpf](https://github.com/libbpf/libbpf) ，它是用 C 编写的，并在 Linux 内核源代码树的 [tools/lib/bpf](https://github.com/torvalds/linux/tree/master/tools/lib/bpf) 目录下开发。它是处理 eBPF 的标准工具。然而， `libbpf` 相当低级，因此添加了额外的工具来帮助更轻松地编写 eBPF 程序及其相应的用户空间程序。

一个名为 [bcc](https://github.com/iovisor/bcc) 的工具允许使用 C 编写 eBPF 程序，并使用 Python 和 lua 编写用户空间程序。还有 [ebpf-go](https://github.com/cilium/ebpf)) ，它允许使用 C 编写 eBPF 程序，并使用 Go 编写用户空间程序。最后，还有 Rust 的 eBPF 生态系统。 [libbpf-rs](https://github.com/libbpf/libbpf-rs) 是 `libbpf` 的官方 Rust 封装。然而， `libbpf-rs` 仍然要求使用 C 编写 eBPF 程序。为了在 Rust 中编写 eBPF 程序，创建了一个名为 [RedBPF](https://github.com/foniod/redbpf) 的工具。后来，这被 [Aya](https://github.com/aya-rs/aya) 取代。 Aya 完全摆脱了对 `libbpf` 的依赖，采用纯粹的本地 Rust 实现。

| Library   | Userspace      | eBPF   | Syscalls |
|-----------|----------------|--------|----------|
| libbpf    | C            | C    | C      |
| bcc       | 🐍Python + lua | C    | C      |
| ebpf-go   | 🕳️Go          | C    | C      |
| libbpf-rs | 🦀Rust         | C    | C      |
| RedBPF    | 🦀Rust         | 🦀Rust | C      |
| Aya       | 🦀Rust         | 🦀Rust | 🦀Rust   |

我们将使用 [Rust](https://www.rust-lang.org/) 进行工作，这是一种专注于性能、可靠性和生产力的现代编程语言。这使得它成为进行[系统编程](https://thenewstack.io/microsoft-rust-is-the-industrys-best-chance-at-safe-systems-programming/)的优秀语言，这也导致它[最近作为 Linux 内核中的第一种新语言与 C 并存](https://thenewstack.io/rust-in-the-linux-kernel)。在接下来的系列文章中，我们将使用 Aya 工具集来同时编写 eBPF 和用户空间程序。

在编写 eBPF 程序时，性能至关重要。由于 eBPF 程序在内核中运行，如果它们运行缓慢，可能会拖慢整个系统。单次调用 eBPF 程序可能会给调用添加高达 100 毫秒的延迟。这种性能回归水平在开发中是可以检测到的。然而，除非开发人员已经密切关注，否则很少发生这种情况。大多数开发团队没有建立检测 CI 中性能回归的基础设施，就像对功能回归一样。这使得性能错误只能在生产环境中检测到，此时它们已经影响到用户，并且修复它们的代价最高。

性能错误是错误，开发团队应尽可能将性能回归的检测尽早移至开发周期的左侧。依靠开发人员在每次更改时手动运行基准测试是不可行的。与运行单元测试以防止功能回归的原因相同，应该在 CI 中运行基准测试以防止性能回归。这将需要一个连续的基准测试工具，例如 [Bencher](https://bencher.dev/) 来跟踪基准测试并捕获性能回归。

在这个系列的博客文章中，我们将涵盖以下内容：

* 在Rust中编写基本的eBPF程序
* 在Rust中演进eBPF程序
* 在Rust中进行基准测试eBPF程序
* 在Rust中进行连续基准测试eBPF程序


该项目的所有源代码都是开源的，可以在 [GitHub](https://github.com/bencherdev/bencher/tree/main/examples/ebpf) 上获取。