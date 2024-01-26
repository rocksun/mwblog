<!--
title: 时间去哪儿了? - Rust编译速度问题研究
cover: https://cdn.thenewstack.io/media/2024/01/07bf0685-rust-build-crab-1024x643.jpg
-->

针对Rust程序构建时间的不满，Oxide的工程团队展开了对整个编译过程的调查。

> 译自 [Where Does the Time Go? Rust’s Problem with Slow Compiles](https://thenewstack.io/where-does-the-time-go-rusts-problem-with-slow-compiles/)，作者 Joab Jackson 是 The New Stack 的高级编辑，负责云原生计算和系统操作的报道。他已经在IT基础设施和开发方面报道了超过25年，包括在IDG和Government Computer News的任职。在那之前，他...

虽然许多人对[Rust编程语言](https://thenewstack.io/bpf-opens-a-door-to-linux-dynamic-scheduling-maybe-with-rust/)的神奇之处[赞不绝口](https://thenewstack.io/how-to-write-your-own-email-server-in-rust/)，但一个持续存在的抱怨仍然层出不穷：编译Rust程序需要很长时间。

“我真的觉得当涉及到编译时间时，Rust社区患有集体斯德哥尔摩综合症。这太糟糕了。我知道修复这个问题很困难，但编译器离良好的生产力要求还差得很远，” [Python Flask](https://flask.palletsprojects.com/en/3.0.x/)的创始人[Armin Ronacher](https://github.com/mitsuhiko)[在X](https://twitter.com/mitsuhiko/status/1749773861153910968)（以前被称为Twitter的平台）上写道。他对Rust编译速度慢的批评只是[众多](https://thenewstack.io/google-busts-confirms-common-myths-about-rust-programming/)声音之一。

周一，[Oxide](https://thenewstack.io/oxide-launches-the-worlds-first-commercial-cloud-computer/)在[Discord上举办了一个虚拟聚会](https://discordapp.com/channels/1042492311080288306/1199149409607372940)，讨论了这个问题。

## 编译时间的禅意

Oxide首席技术官[Bryan Cantrill](https://thenewstack.io/bryan-cantrill-on-ai-doomerism-intelligence-is-not-enough/)对长时间的编译并不陌生。

他回忆起在[Sun Microsystems](https://thenewstack.io/sun-microsystems-a-look-back-at-a-tech-company-ahead-of-its-time/)的某个时候，编译一个操作系统内核需要超过24小时才能完成。他承认，在漫长的构建过程中获得满足感，因为“编译花费很长时间是因为它正在为我解决真正困难的问题。”

但他也承认，长时间的构建也带来了困扰，一种沉重的感觉，认为这段时间可以用在其他地方，无论是对人还是对机器都是如此。

“最令人沮丧的一件事情之一是，当你作为程序员真的觉得Rust正在做一些它不需要做的工作时，” Cantrill说道。

因此，公司让工程师们努力找出为什么Rust应用程序需要这么长时间的问题。正如这次在线讨论所揭示的那样，这实际上成为了一场相当大的冒险...

## Oxide如何使用Rust

一家专注于提供[本地云设备](https://thenewstack.io/in-pursuit-of-a-superior-server-oxide-computer-ships-its-first-rack/)的硬件公司，Oxide使用Rust构建其控制平面（“[Omicron](https://github.com/oxidecomputer/omicron)”）以及其他基础设施软件（Oxide的每个人似乎都喜欢Rust的先进包管理系统[Cargo](https://thenewstack.io/rust-is-surging-ahead-in-webassembly-for-now/)）。

这些项目一开始规模较小，但随着它们的不断扩大，编译时间变得越来越慢。Cantrill表示，当进行单一更改并查看结果时，这可能特别令人沮丧，因为这涉及大量重复构建。

更糟糕的是，随着编译时间的增长，要弄清楚构建的哪些部分占用了所有时间变得越来越困难。如果没有工具揭示它们最初构建时为什么需要这么长时间，构建时间就无法缩短。

Rust编译器被设计为经典的批处理编译器（尽管它已经扩展了一些增量功能），这意味着即使只进行了增量更改，您也必须等待整个应用的编译时间。执行cargo build命令，生成的构建时间可能会达到48秒、三分钟或更长时间。但在打破他们的流程之前，程序员只会等待一段时间，Cantrill观察到。

![Zoom](https://cdn.thenewstack.io/media/2024/01/de1d0eea-build-unit-time.png)

*（来源：Oxide Discord）*

## Rust如何编译代码

cargo build --timings有一个标志，当调用时，提供了一个构建图，逐个crate地显示正在构建的内容以及构建每个crate需要多长时间。

在这些 crate 内部发生的情况仍然有些神秘，因此对其进行优化可能是一个挑战，Oxide 软件工程师肖恩·克莱恩（[Sean Klein](https://www.linkedin.com/in/sean-klein-17637362/)）表示：“关于接下来该去哪里，没有一个答案。有很多不同的答案，” 他说。

诸如 [cargo-llvm-line](https://github.com/dtolnay/cargo-llvm-lines)s 或 [cargo-bloat](https://github.com/RazrFalcon/cargo-bloat) 这样的工具可以显示生成的二进制文件为什么具有特定的大小，但这些测量只是估算编译时间本身的代理。

在单态化（[Monomorphization](https://rustc-dev-guide.rust-lang.org/backend/monomorph.html)）中存在一个明显的问题，这取决于你如何看待它，可能是 Rust 的一个特性或 bug。如果在应用程序的多个地方使用了一个小的通用函数，Rust 将为每种具体情况编译该通用函数。结果是：程序运行快，编译时间慢。

Oxide 工程师史蒂夫·克拉布尼克（[Steve Klabnik](https://github.com/steveklabnik)）创建了一个消除所有这些通用函数重复构建的 10 行函数。“通过进行这个小改变，你可以帮助编译器不做太多的工作，”[拉取请求文档](https://github.com/oxidecomputer/dropshot/pull/597)写道。这从 Omicron 的构建时间中减少了五秒。

还致力于解决这个问题的是 Oxide 工程师雷恩·帕哈里亚（Rain Paharia），他在 Oxide 和在他们在 [Meta](https://thenewstack.io/meta-solves-pythons-problem-of-the-not-so-immutable-objects/) 的前职位上花费了大量时间研究这个问题。

当一个 crate 被重新构建时，它的所有依赖也会以传递方式被重新构建，他们说。

例如，广泛使用的 [syn-crate](https://crates.io/crates/syn)，一个解析库具有约 15 个功能，程序的[过程宏](https://doc.rust-lang.org/reference/procedural-macros.html)（一种方便的功能，用于在编译时扩展程序代码）可能调用其中的任何一个。

在编译时，所有这些功能都会被重新构建，而不管实际上调用了哪些...

“突然间，你有了这种可以构建的功能或功能集的组合爆炸。由于 syn 是如此核心，每一件依赖于 syn 的事物都会被重新构建，” 帕哈里亚说。“目前情况有点灾难。这一点都不好。”

## 问题解决了吗？

帕哈里亚构建了一些绕过问题的工具，如 [cargo-hakari](https://crates.io/crates/cargo-hakari)，一个命令行应用程序，使用一个[空 crate](https://crates.io/crates/workspace-hack) 可以加速编译速度 20-25%。该 crate 指定了程序中处处使用的所有功能的联合，因此它们只会被编译一次，而不是多次。

他们发现 cargo-hakari 在一定程度上减少了构建时间... 但并非完全解决。因此，帕哈里亚使用了一个名为 "[unit graph](https://doc.rust-lang.org/nightly/nightly-rustc/cargo/core/compiler/unit_graph/type.UnitGraph.html)" 的新（不稳定的）Rust功能，该功能指定了构建过程中的每个原子步骤，构建依赖于应用程序的依赖图。

在研究输出时，帕哈里亚发现，尽管他们采取了预防措施，但由于各种隐晦的行为，比如 Rust 如何处理插件的 panic，以及 Rust 如何总体处理过程宏，编译器仍然在重新构建许多重复的对象。

此外，通过 [Build Scripts](https://doc.rust-lang.org/cargo/reference/build-scripts.html) 导入非 Rust 代码可能消耗大量资源。尽管 Oxide 团队似乎共同热爱 Build Scripts，即使它们在承受性能损耗的同时。

## 对 Rust 编译时间仍需进一步努力

Rust 确实有一个“[self-profiling](https://blog.rust-lang.org/inside-rust/2020/02/25/intro-rustc-self-profile.html)”标志，它会告诉你构建特定宏所需的时间。以 JSON 的形式提供了每个动作花费的时间轴，以“内部编译器传递”为单位，但如果没有大量后续分析，这对于了解不是很有用。

“这有点信息，但不像，你是在哪个模块上工作？” 克莱恩说。他指出，围绕这个输出还可以构建更多工具，以提供更多关于编译时间的洞察。

那么，为什么你的 Rust 编译时间这么慢呢？Magic 8球说：稍后再来检查。

完整的讨论可以在[这里](https://share.transistor.fm/s/a46ddac5)阅读。
