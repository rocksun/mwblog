
<!--
title: Rust集成到Linux内核面临挑战，但展现出进展
cover: https://cdn.thenewstack.io/media/2025/02/9fc50f48-getty-images-1lk8lc-xq44-unsplash.jpg
summary: Linux内核集成 Rust 争议不断！维护者对 Rust 代码审查和调试存在挑战，担心增加维护负担。Red Hat 工程师尝试维护 DMA 的 Rust 抽象层。Linux 6.13 引入就地模块，Rust 支持迎来重要进展，PCI 和平台驱动程序或将支持 Rust 驱动。
-->

Linux内核集成 Rust 争议不断！维护者对 Rust 代码审查和调试存在挑战，担心增加维护负担。Red Hat 工程师尝试维护 DMA 的 Rust 抽象层。Linux 6.13 引入就地模块，Rust 支持迎来重要进展，PCI 和平台驱动程序或将支持 Rust 驱动。

> 译自：[Rust Integration in Linux Kernel Faces Challenges but Shows Progress](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/)
> 
> 作者：Steven J Vaughan-Nichols

Rust 和 C 的支持者在 Linux 内核中的冲突已经持续了一段时间。[Linus Torvalds](https://www.linkedin.com/in/linustorvalds/)，[Linux](https://thenewstack.io/rust-in-the-linux-kernel/) 的创建者，在 2024 年 8 月的 [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) 上表示，[分歧已经上升到“几乎是宗教战争的意味”。](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/)” 从那时起，情况变得更加敌对。

为什么？Intel 的 Linux 核心内核架构团队的高级首席工程师 [Dan Williams](https://www.linkedin.com/in/djbw/) 在 [Linux Plumbers 2024](https://lpc.events/event/18/timetable/) 会议上解释说，“[内核维护者往往非常保守。](https://www.zdnet.com/article/rust-in-linux-now-progress-pitfalls-and-why-devs-and-maintainers-need-each-other/) 他们对 C 语言了如指掌，但他们不懂 Rust。因此，他们“不知道如何审查这个或调试那个，因为他们不理解代码。”

然而，对于试图使用 Linux 内核的 C 语言基础的 Rust 开发者来说，情况也是如此。最近的爆发源于一月份添加一个 [用于 Linux 内核的直接内存访问（DMA）应用程序编程接口（API）的 Rust 补丁](https://lore.kernel.org/rust-for-linux/20250108122825.136021-3-abdiel.janulgue@gmail.com/#r) 传输的请求。此功能对于 Rust 设备驱动程序具有可用的数据输入/输出（I/O）是必需的。

## Rust 代码和 C API

著名的软件工程师和 Linux 内核维护者 Christoph Hellwig 不想参与此事。他回复说，“[kernel/dma 中没有 rust 代码，请。](https://lwn.net/ml/all/20250108135951.GA18074@lst.de/)” 这是一个奇怪的立场，因为 [该补丁没有将任何代码放在该目录中](https://lwn.net/SubscriberLink/1006805/f75d238e25728afe/)。

当 [Rust for Linux](https://rust-for-linux.com/) 项目的负责人 Miguel Ojeda 要求 Hellwig 提出替代方案时，他回复说，Rust 开发者应该“[将包装器保留在您的代码中](https://lwn.net/ml/all/20250108151858.GB24499@lst.de/)，而不是让别人的生活痛苦。” 在另一封 Linux 内核邮件列表（LKML）的邮件中，Hellwig 写道，“[维护多语言项目很痛苦](https://lwn.net/ml/all/20250110083955.GA5395@lst.de/)，我没有兴趣处理。如果你想使用不是 C 的东西，无论是汇编还是 Rust，你都要编写 C 接口并自己处理阻抗不匹配。”

## Rust 对于维护者来说更难吗？

作为一种替代方案，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 工程师和内核开发者 [Danilo Krummrich](https://de.linkedin.com/in/danilo-krummrich-796885153) “主动 [维护 DMA 的 Rust 抽象层](https://lwn.net/ml/all/Z5qeoqRZKjiR1YAD@pollux/)，作为单独的组件。” Krummrich 补充说，[Rust for Linux](https://thenewstack.io/fosdem-2025-rust-runs-riot-in-linux-despite-backlash/) 开发者正在编写 Rust 代码，该代码将为所有 Rust 驱动程序抽象 C API，并由 Rust 开发者维护。

这对 Hellwig 也不起作用。他回复说，“我也不想要另一个维护者。如果你想因为跨语言代码库而使 Linux 无法维护，请在你的驱动程序中这样做，这样你就必须自己做，而不是将这种癌症传播到核心子系统。”

由于 Steve Ballmer 对 Linux 的批评，“[癌症](https://www.theregister.com/2001/06/02/ballmer_linux_is_a_cancer/)”一直是 [Linux 圈子](https://thenewstack.io/learning-linux-start-here/) 中的一个重要术语。 随之而来的是许多激烈的言语。 我认为高级 Linux 内核开发人员 Ted T’so 一语中的，他说，最终，[Cristoph 担心的是，由于特定的构建中断妨碍了维护者非常有限的带宽，Rust 将使维护者的生活更加艰难](https://lore.kernel.org/lkml/20250208204416.GL1130956@mit.edu/)。 简而言之，并不是内核维护者认为 Rust 很糟糕； 他们没有足够的时间来维护他们的项目。

## ‘Rust 设备驱动程序混乱’
即便如此，一位维护者，[Asahi Linux](https://asahilinux.org/) 的首席开发者 Hector Martin，呼吁 Torvalds “用权威的答案来解决” Rust 设备驱动程序的混乱局面。“如果他不这样做，Miguel 和其他 Rust 开发者应该在审查和准备好后合并这个系列，忽略 Christoph 公开破坏该项目的企图。” 当这不起作用时，Martin 开始 “在社交媒体上进行羞辱”，以表达他的观点。Torvalds 对此并不感到高兴。

Torvalds 回复说：“你接受问题可能出在你身上的事实如何？你认为你更了解情况。但目前的流程有效。它存在问题，但问题是生活的一部分。没有什么是完美的。” 也就是说，Torvalds 继续说道，“如果我们在内核开发模型中存在问题，那么 [社交媒体肯定不是解决方案](https://lkml.org/lkml/2025/2/6/1292)。同样，它肯定不是解决政治问题的方案。”

Martin 通过退出 Linux Apple/ARM 平台开发来回应，他说：“[我不再对内核](https://lore.kernel.org/lkml/20250207-rm-maint-v1-1-10f069a24f3d@marcan.st/#r) 开发过程或社区管理方法抱有任何信心。”

## 来自实时 Linux 的经验教训

那么，在 Rust 和 Linux 方面，未来可以做些什么呢？高级实时 Linux 开发者 Steven Rostedt 建议 Rust 开发者可以效仿 [实时 Linux 的做法，它花了 20 年的时间才加入到主线 Linux 内核中](https://www.zdnet.com/article/20-years-later-real-time-linux-makes-it-to-the-kernel-really/)；那就是 “[将 [Rust] 保留为树外补丁](https://lkml.org/lkml/2025/2/7/1955)。……是的，在树外是非常困难的，因为你必须不断地进行 rebase……但它也为你提供了尝试新方法的完全灵活性。仅仅因为某些东西在树外并不意味着它不能被发布和使用。Red Hat 和 SUSE，以及许多其他公司，在 PREEMPT_RT 处于树外时就发布了它。”

此后，Ojeda 发布了一份“[Rust 内核策略](https://rust-for-linux.com/rust-kernel-policy)”文档，以澄清 Rust 集成工作的状态。此举是为了回应 Linux 社区内对 Rust 在内核开发中的作用日益增长的困惑和争论。

该文档解决了几个关键问题，包括内核维护者期望的支持级别。Ojeda 指出，如何处理 Rust 仍然由每个维护者决定。“一些子系统可能会决定暂时不使用 Rust 代码，通常是出于带宽原因。这是可以接受的，也是预料之中的。” 因此，虽然一些开发者希望 Rust 更快地进入内核，但 Hellwig 的立场是完全可以辩护的。

事实上，Ojeda 继续说道，“对于 Rust，一个子系统可能允许暂时破坏 Rust 代码。其目的是为了方便 Rust 在子系统中的友好采用，而不会给可能正在处理 C 语言方面紧急修复的现有维护者带来负担。尽管如此，应该尽快修复这种破坏，最好是在破坏到达 Linus 之前。”

## Rust 与 Linux 的集成

当涉及到 Rust 与 Linux 的集成时，与 “快速行动，打破常规” 的技术口号不同，规则是 “缓慢行动，稳定事物”。毕竟，尽管有所有严厉的言辞，Rust 集成到 Linux 的进程仍在继续推进。

例如，2025 年 1 月发布的 Linux 6.13 内核为 Rust 支持带来了重大扩展。这个 [内核为 Rust 开发者引入了就地模块](https://www.phoronix.com/news/Linux-6.13-char-misc-More-Rust)、绑定和跟踪事件。Linux 稳定版本维护者 [Greg Kroah-Hartman](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/) 解释说，这意味着 [Rust 支持正处于 “临界点；](https://lore.kernel.org/lkml/Z0lG-CIjqvSvKWK4@kroah.com/) 预计现在会有更多的 rust 驱动程序出现，因为这些绑定已经存在。

下一个合并窗口，希望我们能有 PCI 和平台驱动程序工作，这将完全使几乎所有的驱动程序子系统都能开始接受（或至少获得）rust 驱动程序。这是很多人努力的最终结果，祝贺他们所有人走到这一步，你们以最好的方式证明了我们许多人的错误，即通过可工作的代码。”

简而言之，尽管争论不休，但正如我们在 6.13 中看到的那样，Rust 进入 Linux 的进程仍然缓慢、稳定且富有成效。Rust 将在 Linux 中找到自己的位置。