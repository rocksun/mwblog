<!--
title: BPF：探索Linux动态调度的新时代（或许携手Rust！）
cover: https://cdn.thenewstack.io/media/2024/01/8ce953d2-scheduler-1024x566.png
-->

在一项圣诞黑客项目中，一位Canonical工程师开发了一个能够在用户空间运行的Linux调度器。

> 译自 [BPF Opens a Door to Linux Dynamic Scheduling (Maybe with Rust!)](https://thenewstack.io/bpf-opens-a-door-to-linux-dynamic-scheduling-maybe-with-rust/)，作者 Joab Jackson 是 The New Stack 的高级编辑，负责云原生计算和系统运维的报道。他在过去 25 年里一直报道 IT 基础设施和开发，包括在 IDG 和 Government Computer News 的任职。在那之前，他...

在假期期间，[Canonical](https://thenewstack.io/canonical-brings-real-time-linux-to-amazon-web-services/) Linux 内核工程师 [Andrea Righi](https://www.linkedin.com/in/arighi/) 在进行技术探索时，使用 Rust 编写了一个 Linux 调度器（还得到了 [Berkeley Packet Filter](https://thenewstack.io/linux-technology-for-the-new-year-ebpf/) 的一些帮助），在早期测试中超过了内核自带的调度器性能。

"我非常惊讶地发现它不仅仅能够工作，而且在某些工作负载下，甚至能够胜过默认的 Linux 调度器（EEVDF），" [他在 X 上写道](https://twitter.com/arighi/status/1746938387968254371)。

虽然只是一个原型，但它[完成了它的任务](https://twitter.com/arighi/status/1747243405317423484)，即 "展示在[用户空间](https://www.educative.io/answers/what-is-the-difference-between-the-kernel-and-user-spaces)中实现可运行的调度器是可能的，甚至在特定条件下能够胜过默认的 Linux 调度器"。

一段附带的[视频](https://youtu.be/oCfVbz9jvVQ)显示了一个简单的电脑游戏以每秒 25-30 帧的速度运行，同时机器上正在编译内核。切换到 Righi 的调度器后，游戏的帧率提高到了每秒约 60 帧，同时内核仍在编译中：

## Linux 是否需要更多的调度器？

Linux 内核调度器负责[将 CPU 时间片分配给应用程序](https://www.kernel.org/doc/html/latest/scheduler/index.html)，以确保每个应用程序都能公平获得时间片，通常[通过完全公平调度器](https://docs.kernel.org/scheduler/sched-design-CFS.html)（CFS）算法实现。

尽管 Linux 的一刀切调度器可能需要更新，以适应当今复杂的分布式计算环境。

Righi 的 [scx_rustland](https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_rustland) 是 [sched_ext](https://github.com/sched-ext/scx/) 的一种[实现](https://arighi.blogspot.com/2023/07/implement-your-own-cpu-scheduler-in.html)，sched_ext 是一个用于运行内核线程调度器的实验性 Linux 内核功能，可以使用 Berkeley Packet Filter（在内核中作为 [eBPF](https://thenewstack.io/what-is-ebpf/) [实现](https://lore.kernel.org/bpf/ZVPJTc5ZNEnnYmei@slm.duckdns.org/T/)）创建和[加载](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/)。它是由 Meta 和 Google 的一组工程师编写的，得到了内核社区其他成员的帮助，希望有一天能够被纳入[核心 Linux 内核](https://thenewstack.io/linux-kernel-5-8-will-be-a-big-release-of-small-patches/)。

“在有人尝试将 BPF 引入内核的 CPU 调度器之前，只是时间问题，”LWN.Net（以前是 Linux 每周新闻）主编 Jonathan Corbett 在技术引入后不久的二月[评论](https://lwn.net/Articles/922405/)道。

Corbett 解释说，基于 BPF 的调度器出于多种原因是有道理的：可以更容易地尝试新的调度方法。如今的系统比过去几十年复杂得多，因此需要更多面向特定领域和特定调度解决方案（例如面向游戏和网络的调度器）。这还可以为开发人员提供一种调整 CPU 以适应其应用程序的方法。

值得注意的是，并非 Linux 社区的每个人都支持动态调度的想法，包括 Linux 之父 [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-community-rust-and-linuxs-longevity/) 本人。Linux 调度器维护者 Peter Zijlstra 在 [sched_ext 的首次发布时评论说](https://lwn.net/ml/linux-kernel/Y5b2btWFJeEfTyJg@hirez.programming.kicks-ass.net/)：“我讨厌这一切”，并补充说 Torvalds 曾否决过先前对替代调度器的尝试，因为它们引入了复杂性。

[AMD](https://lore.kernel.org/lkml/20220910105326.1797-1-kprateek.nayak@amd.com/) 和 [Google](https://dl.acm.org/doi/pdf/10.1145/3477132.3483542) 也都提出了替代调度器的建议。

## … 但 Rust 是否能比 C 在 Linux 上更快呢？

在过去的几年里，对于将内存安全的 Rust 编程语言用于关键任务的[兴趣逐渐增加](https://thenewstack.io/microsoft-rust-is-the-industrys-best-chance-at-safe-systems-programming/)，例如构建操作系统内核，[取代了 C、C++](https://thenewstack.io/can-c-be-saved-bjarne-stroustrup-on-ensuring-memory-safety/) 和其他可能[不慎引入安全漏洞](https://thenewstack.io/bjarne-stroustrups-plan-for-bringing-safety-to-c/)的低级语言。Torvalds 对在内核中[使用 Rust](https://thenewstack.io/linus-torvalds-on-community-rust-and-linuxs-longevity/) 保持[开放态度](https://thenewstack.io/rust-in-the-linux-kernel-by-2023-linus-torvalds-predicts/)。

因此，当 Linux 新闻网站 Phoronix 在一篇文章中报道了 Righi 的工作时，焦点放在了 Rust 的使用上，标题大喊大叫：“[用 Rust 编写的 Linux 调度器在游戏性能上显示出色成果。](https://www.phoronix.com/news/Rust-Linux-Scheduler-Experiment)”

但这篇文章引发了一场不小的争论，不是关于调度器，而是关于在 C++ 之上使用 Rust 是否提供了任何固有优势。

“[调度器] 到底有什么不同之处，导致它表现出不同的性能？是因为它不完整，还是因为它真的更好？因为我无法相信 Rust 本身比 C 更好，” [Theprimeagen](https://twitter.com/ThePrimeagen) 在 Twitch 上一则备受关注的[评论视频](https://www.youtube.com/watch?v=s8Q2aj8YiCY&t=92s)中说道。“在 Rust 中可以做什么，在 C 中做不了呢？”

他指出，调度器都涉及权衡。显然，这个调度器经过了针对游戏性能的调整，以牺牲一些其他功能。

“所有这些新闻告诉我们的是，Rust 实现在这个领域可以与 C 实现相媲美，” pseudocomposer 在 [Hacker News 的讨论](https://news.ycombinator.com/item?id=39012690)中写道。“这则新闻为我们提供了更多选择，无论是 C 还是 Rust 的调度器，都意味着对 Linux 社区在各种工作负载下有更好的体验。”

在通过 LinkedIn 联系到时，Righi 回应说 Rust 在允许他启动这个项目时提供了很大的灵活性。

“我不能说 Rust 在性能上做出了太大的贡献，但它允许我在几周内编写了这个调度器，实现和重用了优雅的高级抽象，同时在需要时能够深入到低级细节。”