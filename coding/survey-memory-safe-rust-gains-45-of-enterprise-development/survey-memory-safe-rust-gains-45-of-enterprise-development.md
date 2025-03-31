
<!--
title: 调查：内存安全 Rust 获得企业开发 45% 的份额
cover: https://cdn.thenewstack.io/media/2025/02/2cb93b83-jay-heike-fc-0gi4yylm-unsplash-1.jpg
summary: 重磅！内存安全语言 Rust 崛起，企业采用率飙升至 45%！云原生后端、WebAssembly 和嵌入式成热门用例。开发者大爱 Linux + VS Code，但 Zed 编辑器异军突起！编译速度仍是挑战，但 Rust 的未来，一片光明！
-->

重磅！内存安全语言 Rust 崛起，企业采用率飙升至 45%！云原生后端、WebAssembly 和嵌入式成热门用例。开发者大爱 Linux + VS Code，但 Zed 编辑器异军突起！编译速度仍是挑战，但 Rust 的未来，一片光明！

> 译自：[Survey: Memory-Safe Rust Gains 45% of Enterprise Development](https://thenewstack.io/survey-memory-safe-rust-gains-45-of-enterprise-development/)
> 
> 作者：Darryl K Taft



# 调查：内存安全 Rust 获得企业开发 45% 的份额

![Featued image for: Survey: Memory-Safe Rust Gains 45% of Enterprise Development](https://cdn.thenewstack.io/media/2025/02/2cb93b83-jay-heike-fc-0gi4yylm-unsplash-1-1024x683.jpg)

[Rust](https://thenewstack.io/rust-programming-language-guide/) 编程语言已经跨越了一个关键的采用门槛，现在有 45% 的组织在生产中大量使用这种[编程语言](https://thenewstack.io/programming-languages/)——根据 [2024 State of Rust Survey](https://blog.rust-lang.org/2025/02/13/2024-State-Of-Rust-Survey-results.html)（Rust 基金会进行的一项年度调查）显示，比 2023 年增长了 7 个百分点。([Rust Foundation](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/))。

Rust 的采用率不断增长，原因有很多，其中最重要的是，它代表了一种[内存安全](https://thenewstack.io/c-committee-divided-on-memory-safety-plans/)的替代方案，可以替代 [C 和 C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) 等语言。

根据调查，组织主要选择 Rust 来构建正确且无错误的软件 (87.1%)、性能特征 (84.5%)、安全属性 (74.8%) 和开发乐趣 (71.2%)。

“Rust 被理所当然地认为是一种安全的语言和生态系统。因此，我们喜欢尝试领先于未来可能出现的潜在安全问题，”Rust 基金会技术总监 [Joel Marcey](https://thenewstack.io/rusts-expanding-horizons-memory-safe-and-lightning-fast/) 在之前接受 The New Stack 采访时表示。“基金会正在进行的一些项目，如 Painter 和 Typomania，试图正面解决这些潜在问题，我们试图了解如果出现易受攻击的代码，或者人们试图抢注 crate 名称的潜在途径。”

## 热门用例和开发环境

报告称，Rust 似乎特别受创建服务器后端 (53.4%)、Web 和网络服务、云技术和 [WebAssembly](https://thenewstack.io/webassembly/) 的欢迎。它似乎也在嵌入式用例中获得越来越多的关注。

IDC 的分析师 [Arnal Dayaratna](https://www.idc.com/getdoc.jsp?containerId=PRF004946) 在 12 月告诉 The New Stack，Rust 的“所有权模型和借用检查器保证了内存安全，而无需垃圾回收，使其成为在嵌入式系统、云原生基础设施和汽车应用等领域构建可靠软件的理想选择”。

关于首选开发环境，Linux 仍然是主要的开发平台 (73.7%)。然而，尽管 [VS Code](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) 仍然是领先的编辑器，但其使用率下降了 5 个百分点，从 61.7% 降至 56.7%，但 [Zed](https://zed.dev/) 编辑器获得了显着的吸引力，从 0.7% 增至 8.9%。此外，报告称，“十分之九的 Rust 开发人员使用当前的稳定版本，这表明对该语言的稳定性充满信心”。

![](https://cdn.thenewstack.io/media/2025/02/06c38abe-what-ide-do-you-use-1-1.png)

来源：Rust 基金会

## 工作中的 Rust

与此同时，Rust 的使用越来越频繁，并且更有可能在工作中使用。

调查显示，专业 Rust 的采用率显着增加，现在有 38% 的受访者在工作中将 Rust 用于大部分编码，高于 2023 年的 34%，并且 45% 的组织对 Rust 进行了重要的使用（比 2023 年增长了 7 个百分点）。总体而言，82% 的受访者表示 Rust 帮助他们的公司实现了目标，并且每天使用 Rust 的比例增加到 53%（比 2023 年增长了 4 个百分点）。

当被问及为什么在工作中使用 Rust 时，47% 的受访者表示需要精确控制他们的软件，高于两年前提问时的 37%。

![](https://cdn.thenewstack.io/media/2025/02/65cc3dd7-reasons-rust-used-at-work-1-1.png)

来源：Rust 基金会

## 持续的挑战

尽管取得了积极进展，但 Rust 仍然存在一些关键挑战。例如，编译速度仍然是首要问题。“这似乎是 Rust 用户长期关注的问题。与往常一样，人们正在努力提高编译器的速度，例如启用[并行前端](https://blog.rust-lang.org/2023/11/09/parallel-rustc.html)或默认切换到[更快的链接器](https://blog.rust-lang.org/2024/05/17/enabling-rust-lld-on-linux.html)，”报告称。

此外，其他挑战包括对调试 Rust 的支持不足以及 Rust 编译器工件的磁盘使用率高。然而，报告称，“另一方面，大多数 Rust 用户似乎对其运行时性能、编译器的正确性和稳定性以及 Rust 的文档非常满意”。
最后，虽然一些受访者表示希望更快地实现功能稳定（25.6% 希望更快的发展）；57.9% 的人表示他们对 Rust 目前的发展速度感到满意。

*Lawrence Hecht contributed to this article.*

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)