
<!--
title: Rust 2024重大时刻
cover: https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1.png
-->

Rust编程语言在2024年取得了显著进展，标志着性能的重大提升以及业界对内存安全编程的信心日益增强。

> 译自 [Big Moments in Rust 2024](https://thenewstack.io/big-moments-in-rust-2024/)，作者 Tim McNamara。

Rust 项目今年的主要目标是开发一个新的版本。[版本](https://doc.rust-lang.org/edition-guide/index.html) 在项目生命周期中创建了可以向语言添加新关键字、向标准库添加内容以及进行其他更改的点。根据[Rust 博客上的一篇文章](https://blog.rust-lang.org/2024/11/27/Rust-2024-public-testing.html)，“这是自 Rust 2015 以来规模最大的版本”。

大多数更改都是细微的，但却是对语言的重要改进。[程序员](https://thenewstack.io/rust-makes-us-better-programmers/) 会发现该语言更容易使用。一个很大的变化是，创建对开放写入访问的共享全局变量的直接引用——Rust 将其称为“可变静态变量”——[现在是不可能的](https://doc.rust-lang.org/nightly/edition-guide/rust-2024/static-mut-references.html)。到目前为止，允许引用一直是该语言中未定义行为的隐藏来源。

我最期待的功能之一是生成器。到目前为止，只向语言中添加了一个`gen`关键字。现在可以开始认真地将生成器引入稳定的 Rust 中。（生成器已经存在于所谓的“夜间”编译器中，该编译器不提供稳定性保证。）

## 越来越多的人使用这种语言

一个有用的跟踪指标是[Visual Studio Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) 扩展程序[rust-analyzer](https://github.com/rust-lang/rust-analyzer) 的官方 Rust 扩展程序的安装数量。目前安装数量为[415 万](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer)。这比年初的[266 万](https://web.archive.org/web/20240110035731/https:/marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer)有所增加。

![](https://cdn.thenewstack.io/media/2024/12/3415c51e-picture2.1.png)

Visual Studio Marketplace 上 rust-analyzer 页面的屏幕截图，显示该扩展程序的安装量为 4,148,456 次。

## 人们交付了优秀的產品

首先，发布了[Tiny Glade](https://store.steampowered.com/app/2198150/Tiny_Glade/)。这款微缩景观建造游戏已被证明非常成功，Rust 社区的大新闻是这款游戏完全是用这种语言编写的。

![](https://cdn.thenewstack.io/media/2024/12/53549d75-picture1.1.jpg)

*来自 Gamescom 2023 未来游戏展游戏预告片的截图。*

更严肃地说，Rust 的优势开始在编写软件库方面显现出来。PNG 图像文件格式的 Rust 实现现在[优于其传统的 C 编写版本](https://www.reddit.com/r/rust/comments/1ha7uyi/memorysafe_png_decoders_now_vastly_outperform_c/)。这是因为 Rust 语言为 SIMD 指令提供了跨平台支持。编写 C 库的人员需要为每个目标架构手动提供实现。

图像处理并非一次性事件。基于 Rust 的[TLS 安全](https://thenewstack.io/jetstack-secure-promises-to-ease-kubernetes-tls-security/) 实现[Rustls](https://github.com/rustls/rustls) 现在[比 BoringSSL 和 OpenSSL 更快](https://www.memorysafety.org/blog/rustls-performance-outperforms/)。资助这项工作的非营利组织，[互联网安全研究小组 (ISRG)](https://thenewstack.io/rustls-looks-to-provide-a-memory-safe-replacement-for-openssl/) 从[Let’s Encrypt](https://letsencrypt.org/) 开始，现在正在努力改进互联网基础设施的各个方面。这包括计算机之间的时间保持等基础知识，以及现在名为[River](https://www.memorysafety.org/blog/river-release/) 的内存安全、高性能反向代理的实现。这旨在挑战[NGINX](https://www.nginx.com?utm_content=inline+mention) 在该领域的统治地位。

未来需要注意的一件事是新成立的[Trifecta Tech 基金会](https://trifectatech.org/)。他们有一个 Rust 编译器的分支，可以生成一个执行压缩和解压缩的可执行文件，该可执行文件的[速度比标准编译器生成的快 14%](https://trifectatech.org/initiatives/codegen/)。预计这些性能改进会随着时间的推移而融入主线。Rust 速度惊人，而且会越来越快。

## 对该语言的信心日益增强

去年三月在[Rust Nation UK](https://www.rustnationuk.com/)会议上，[Lars Bergstrom](https://www.linkedin.com/in/lars-a-bergstrom/)透露，“[Google](https://cloud.google.com/?utm_content=inline+mention)的Rust团队与使用[Go](https://thenewstack.io/go/)的团队一样高效，并且比使用C++的团队[效率高出一倍多](https://thenewstack.io/rust-gets-security-wasi-0-2-support-productivity-boost/)”。

## 编译器在每个版本中都变得越来越智能

对我来说，1.79版本是最有影响力的版本之一。我许多用来解释为什么需要借用检查器的教学示例都停止工作了，因为借用检查器变得更智能了。也就是说，示例代码无法编译——借用检查器过于严格了。

## 人们变得雄心勃勃

美国政府国防研究机构[DARPA宣布了TRACTOR项目](https://thenewstack.io/can-darpas-tractor-pull-c-to-rust-for-memory-safe-overhaul/)，旨在创建工具将不安全的C代码转换为安全的Rust代码。其目的是快速加快用内存不安全语言编写的、大规模重写系统的速度，然后将其移植到Rust。

[安全关键型Rust联盟](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/)于六月宣布成立，旨在将Rust应用于关键行业。这是在汽车、火车和飞机中看到Rust的重要一步。

二月份，Google宣布向[Rust基金会](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/)提供100万美元的资助，以支持改进[Rust和C++互操作性](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/)的计划。这笔资助催生了更广泛的[互操作性倡议](https://foundation.rust-lang.org/news/google-contributes-1m-to-rust-foundation-to-support-c-rust-interop-initiative/)，并出现了[C++/Rust互操作性问题陈述](https://thenewstack.io/the-rust-c-bridge-a-new-path-forward/)。连接C++和Rust将意味着Rust项目更容易扩展现有的代码库。

[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)和Rust基金会已决定启动一个项目来[正式验证标准库](https://github.com/model-checking/verify-rust-std)。他们创建了一个奖励计划，用于验证标准库的部分内容，希望这将能够促使新的工具和技术出现，并最终正式验证整个标准库的正确性。今天的标准库包含数千个`unsafe`关键字的使用。虽然社区相信这些用法是正确的，但这并没有得到保证。正式验证将改变这一点。

## 社区越来越强大

2024年令人高兴的是没有出现困扰前几年的“Rust风波”。事实上，新的沟通渠道出现了。

Rust基金会主办了社区的标志性活动[RustConf](https://rustconf.com/)。虽然这似乎是一个微不足道的成就，但近年来，此次会议一直是分歧和敌意的焦点。

许多专注于该语言的会议和活动都出现了。大型活动现在定期在欧洲各地举行。看到对弱势地区的经济支持，例如[Rustaceans Kenya](https://www.linkedin.com/posts/rust-foundation_the-rust-foundation-was-thrilled-to-support-activity-7275198742897573889-7ZC3?utm_source=share&utm_medium=member_desktop)，尤其令人鼓舞。

2024年也见证了播客领域的复兴。现在有大量的播客提供不同的视角、访谈和形式。

有关2024年[编程语言](https://thenewstack.io/programming-languages/)最大新闻的更多信息，请查看Darryl K. Taft的报告“[2024年编程语言大战：Python领先，Java保持稳定，Rust崛起](https://thenewstack.io/language-wars-2024-python-leads-java-maintains-rust-rises/)”。
