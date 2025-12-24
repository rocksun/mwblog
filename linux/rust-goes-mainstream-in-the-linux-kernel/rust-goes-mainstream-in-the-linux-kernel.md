<!--
title: Rust 深度融入 Linux 内核，全面走向主流
cover: https://cdn.thenewstack.io/media/2025/12/00889173-jay-heike-fc-0gi4yylm-unsplash-2-1.jpg
summary: Linux内核中Rust不再是实验性的，现已成为核心部分。因其内存安全优势，将用于新驱动开发，预示底层开发新趋势。
-->

Linux内核中Rust不再是实验性的，现已成为核心部分。因其内存安全优势，将用于新驱动开发，预示底层开发新趋势。

> 译自：[Rust Goes Mainstream in the Linux Kernel](https://thenewstack.io/rust-goes-mainstream-in-the-linux-kernel/)
> 
> 作者：Steven J. Vaughan-Nichols

东京——在仅限受邀者参加的[Linux 内核维护者峰会](https://events.linuxfoundation.org/linux-kernel-maintainer-summit/)上，顶级 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 维护者们决定，正如 Linux 内核开发者 Jonathan Corbet 所说，“与会开发者们的共识是，[Rust 在内核中不再是实验性的](https://lwn.net/Articles/1049831/)——它现在是内核的核心部分，并将继续存在。因此，‘实验性’标签将被移除。”正如 Linux 内核维护者 Steven Rosted 告诉我的，“没有任何阻力。”

这一变化酝酿已久。此次转变标志着五年激烈争论的结束，争论的焦点是这种[内存安全语言](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/)是否应该与 C 语言一同成为世界上部署最广泛的开源操作系统的核心。

## 迹象早已显现

不过，[Rust](https://thenewstack.io/rust-programming-language-guide/) 被接受的这一步早有迹象。在最近的 Linux 基金会 [2025 年韩国开源峰会](https://events.linuxfoundation.org/open-source-summit-korea/)上，Torvalds 曾表示：“我认为我们已经达到了一个阶段，[Rust 真正成为内核的一部分](https://www.zdnet.com/article/what-linus-torvalds-really-thinks-about-ai-and-software-development-might-surprise-you/)，不再仅仅是实验性的东西。”

不，不，它不再是了。这一切始于 Alex Gaynor 和 Geoffrey Thomas 在 2019 年 Linux 安全峰会上表示，大约三分之二的 Linux 内核漏洞来自内存安全问题。理论上，Rust 可以通过使用[其固有的更安全的应用程序编程接口 (API)](https://www.youtube.com/watch?v=RyY01fRyGhM) 来避免这些问题。

在随后的 2020 年 Linux Plumbers 会议上，开发者 Nelson Elhage [在他关于 Linux 中 Rust 的 Plumbers 会议总结中](https://lwn.net/Articles/829858/)解释说，Linux Rust 的支持者们并非“提议将 Linux 内核用 Rust 重写；他们只专注于朝着新代码可以用 Rust 编写的世界迈进。Rust 支持的三个潜在关注领域是利用内核中现有的 API、架构支持以及处理 Rust 和 C 之间的应用程序二进制接口 (ABI) 兼容性。”

与此同时，Linux 内核开发者 Miguel Ojeda 开始将 Linux 代码从 C 迁移到 Rust。他于 2019 年创建了 [Rust for Linux 项目](https://github.com/Rust-for-Linux)，将树外 Rust 模块引入 Linux。

到 2021 年初，Rust 在 Linux 内核之外，正被更紧密地引入这个世界上最受欢迎的操作系统。[亚马逊云科技 (AWS)](https://aws.amazon.com/?utm_content=inline+mention) 发布了用于容器的 [Bottlerocket Linux](https://cc.zdnet.com/v1/otc/00hQi47eqnEWQ6T9d4QLBUc?element=BODY&element_label=Bottlerocket+Linux&module=LINK&object_type=text-link&object_uuid=a8cdbe53-ce50-41b6-8d77-2309830e2c5b&position=1&template=article&track_code=__COM_CLICK_ID__&view_instance_uuid=87c931b4-6981-403a-a1b8-222e738ab692&url=https%3A%2F%2Faws.amazon.com%2Fblogs%2Fopensource%2Fannouncing-the-general-availability-of-bottlerocket-an-open-source-linux-distribution-purpose-built-to-run-containers%2F)，其中部分基于 Rust。大约在同一时间，[Debian Linux](https://www.debian.org/) 开发者 Sylvestre Ledru 使用 [LLVM 编译器基础设施](https://llvm.org/)及其 [Clang C 语言前端](https://clang.llvm.org/)和工具基础设施，将 Rust 版本的 [Coreutils](https://www.gnu.org/software/coreutils/) 移植到 Linux。

## 给 Rust 一个机会

同年三月，[Linus Torvalds 决定给 Rust 一个机会](https://www.zdnet.com/article/linus-torvalds-on-where-rust-will-fit-into-linux/)。他当时告诉我，他属于“观望”阵营——“我对这个项目很感兴趣，但我认为它是由对 Rust 非常兴奋的人驱动的，我想看看它在实践中最终会如何运作。”

Torvalds 补充说，他“个人绝没有‘推动’Rust，[但]考虑到其承诺的优势和避免一些安全隐患，我对此持开放态度，但我也知道有时承诺并不能兑现。”

事实证明，这些承诺得以兑现。在互联网安全研究小组 (ISRG) 和 [谷歌](https://cloud.google.com/?utm_content=inline+mention)的财政支持下，2021 年 9 月 20 日，Ojeda 提交了 Rust for Linux 项目的第一个拉取请求。这增加了初步的 Rust 支持，包括 Kbuild 集成、对内置模块的初步支持以及内核 crate 的开端，其中包含 Alex Gaynor 和 Geoffrey Thomas 提供的安全 Rust 抽象。

在早期，计划并不是用 Rust 重写 Linux；现在也仍然不是，而是有选择地在能够提供最大安全益处且不破坏成熟 C 代码的地方采用它。简而言之，新的驱动程序、子系统和辅助库将是首要目标。

这不是一段轻松的旅程。正如 Ojeda 在 2022 年 6 月所说，“内核是一个庞大的项目，涉及众多利益相关者。从一开始就很清楚，[在内核中添加第二种‘主要’语言将带来技术和管理上的挑战](https://www.memorysafety.org/blog/memory-safety-in-linux-kernel/)。”

他被证明是对的。Rust 在内核中的采用在内核社区内部引发了争议。一些维护者质疑在 Linux 中混合编程范式的成本。例如，在 2021 年内核维护者峰会上，Video4Linux 维护者 Laurent Pinchart 表示[他没有时间“很快停下所有事情来学习 Rust”](https://lwn.net/Articles/869145/)。

## 阻力

尽管 Rust 开始进入，但它仍然面临阻力。正如英特尔 Linux 核心内核架构团队高级首席工程师 Dan Williams 在 [2024 年 Linux Plumbers](https://lpc.events/event/18/timetable/) 会议上所说，“[内核维护者往往非常保守](https://www.zdnet.com/article/rust-in-linux-now-progress-pitfalls-and-why-devs-and-maintainers-need-each-other/)。他们对 C 语言了如指掌，但他们不了解 Rust。”因此，他们“不知道如何审查或调试这些代码，因为他们不理解代码。”

请记住，他们有他们的理由。在一场关于如何让 [Rust 与 Linux 内核的直接内存访问 (DMA)](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/) 应用程序编程接口 (API) 协同工作的争议中，真正的问题归结为，正如资深 Linux 内核开发者 Ted T’so 所观察到的，维护者没有无限的时间，而且[他们不想增加他们的“代码维护负担”](https://lore.kernel.org/lkml/20250208204416.GL1130956@mit.edu/?utm_source=the+new+stack)。

尽管如此，尽管存在争议，越来越多的程序被移植到 Rust。到 2025 年 4 月，Linux 内核包含大约 3400 万行 C 代码，而 Rust 编写的只有 2.5 万行。与此同时，越来越多的驱动程序和更高级别的实用工具正在用 Rust 编写。例如，Debian Linux 发行版的开发者宣布，未来 [Rust 将成为其基础高级软件包工具 (APT) 的必要依赖项](https://thenewstack.io/debian-mandates-rust-for-apt-reshaping-ubuntu-and-other-linux-distros/)。

## C 语言不会消失

这一变化并不意味着每个人都必须使用 Rust。C 语言不会消失。然而，正如几位维护者告诉我的，他们预计会看到更多驱动程序用 Rust 编写。特别是，Rust 对于“叶子”驱动程序（网络、存储、NVMe 等）尤其具有吸引力，因为 [Rust-for-Linux 绑定在内核 C API 之上暴露了安全的封装器](https://mars-research.github.io/doc/2024-acsac-rfl.pdf)。

尽管如此，对于有志成为内核和系统程序员的人来说，Rust 在 Linux 中的新地位预示着一条职业道路，它融合了对 C 语言的深入理解和对 Rust 安全保证的熟练掌握。这种结合可能会定义下一代底层开发工作。