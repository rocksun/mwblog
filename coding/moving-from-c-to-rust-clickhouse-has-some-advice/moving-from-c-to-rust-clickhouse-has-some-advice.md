
<!--
title: ClickHouse：C++转Rust的独家秘籍
cover: https://cdn.thenewstack.io/media/2025/11/45338a44-jen-theodore-gvf_yldx_oy-unsplash.jpg
summary: Clickhouse将Rust渐进集成至C++代码库。C++构建复杂易错，Rust虽安全但混合使用有挑战（如Panic）。暂不完全重写，但认可Rust价值。
-->

Clickhouse将Rust渐进集成至C++代码库。C++构建复杂易错，Rust虽安全但混合使用有挑战（如Panic）。暂不完全重写，但认可Rust价值。

> 译自：[Moving From C++ to Rust? Clickhouse Has Some Advice](https://thenewstack.io/moving-from-c-to-rust-clickhouse-has-some-advice/)
> 
> 作者：Joab Jackson

Clickhouse是一个开源的分析型数据库系统，由150万行代码组成，其中大部分是C++编写的。C++是一种在隐藏可能被恶意攻击者利用的bug方面臭名昭著的不安全语言。

人们常说，[即使是在The New Stack这里](https://thenewstack.io/rust-vs-c-a-modern-take-on-performance-and-safety/)，[Rust编程语言](https://thenewstack.io/rust-programming-language-guide/)凭借其卓越的内存和线程安全处理能力，可以取代[C/C++](https://thenewstack.io/introduction-to-c-programming-language/)。并且有许多大型代码库，例如[Linux内核](https://thenewstack.io/how-ai-helps-maintain-the-linux-kernel/)（C）和Windows（C++）是用一些有数十年历史的变种语言编写的，因此许多人都在问自己同样的问题。

Clickhouse的维护者们走上了这条道路，旨在转换用C++代码编写的Clickhouse功能。甚至可能重写整个代码库。

Clickhouse首席技术官兼联合创始人Alexey Milovidov在[ScylaDB](https://www.scylladb.com/?utm_content=inline+mention)的[虚拟P99 Conf](https://www.p99conf.io/)上的一次[演讲](https://www.p99conf.io/session/clickhouses-c-rust-journey/)中讨论了结果，他提出的操作性问题是：“如果我们今天开始，我们是否会用Rust编写Clickhouse？”

Milovidov解释说，最终，核心开发人员采取了更渐进的迁移路线。他们首先将Rust集成到构建系统中，然后为各种功能构建模块。

在此过程中，他们遇到了许多挑战，包括确保可重现构建和管理依赖项。

“Rust可能很完美，但当你将C++和Rust一起使用时，可能会出现问题，”Milovidov建议道。

## C++的代价是庞大的构建系统

Milovidov指出，用C++编写任务关键型应用程序仍然具有许多优势。“它根深蒂固。它广受认可。它非常流行。很容易雇佣懂C++的人。大学仍然教授C语言，”他说。

但他感叹道，使用C++需要“太多的努力”。他补充说，你“几乎不可避免地”会遇到围绕内存损坏、段错误或竞争条件的安全问题。

事实上，Clickhouse最终构建了一个“庞大的”基于[CMake](https://cmake.org/)的[持续集成系统](https://thenewstack.io/ci-cd/)，仅仅是为了确保捕获和修复所有这些类型的错误。

平均每天有70个拉取请求和145个提交，CI系统产生“数百亿次测试”，这实际上是“数千万次”以不同组合进行的独立测试——所有这些都是为了确保新代码不带任何新bug。

[![Presentation slide](https://cdn.thenewstack.io/media/2025/10/599a26c7-clickhouse-01.jpg)](https://cdn.thenewstack.io/media/2025/10/599a26c7-clickhouse-01.jpg)

C++是个麻烦吗？Milovidov有一整张幻灯片来讨论这个话题…

## Rust之旅

“所以也许是时候用Rust重写了，”核心开发团队想知道。这种语言提供了内存和线程安全。它还提供了更多的库，尤其是在围绕[Apache Iceberg](https://thenewstack.io/dispelling-myths-of-open-source-complexity-with-apache-iceberg/)等新兴数据标准方面。而且这种语言似乎吸引了所有年轻、有抱负的软件工程师。

然而，将[Clickhouse](https://github.com/ClickHouse/ClickHouse)完全重写为Rust将需要数年时间。

相反，团队决定采用迭代方法，其中Clickhouse系统的各个部分可以用Rust重新实现。他们将使用[Corrosion](https://github.com/corrosion-rs/corrosion)与CMake集成。

首先，他们给[SQL](https://thenewstack.io/to-sql-or-not-to-sql-that-is-not-the-question/)添加了一个小函数，一个用于[BLAKE3哈希](https://github.com/BLAKE3-team/BLAKE3)，用Rust编写并[为C++封装](https://github.com/ClickHouse/ClickHouse/pull/33435)。然后，在外部贡献者的帮助下，他们增强了命令行界面[`clickhouse-client`](https://clickhouse.com/docs/interfaces/cli)，提供了更好的历史记录和导航功能。他们还接受了一个拉取请求，用于替代SQL的库，名为[PRQL](https://prql-lang.org/)（Pipelined Relational Query Language），它也是用Rust编写的。

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/0ed32157-clickhouse-02.jpg)](https://cdn.thenewstack.io/media/2025/11/0ed32157-clickhouse-02.jpg)

随着他们对Rust的信心日益增长，项目变得越来越大。下一个Rust测试是集成一个基于Rust的库，用于新兴的[Delta Lake格式](https://thenewstack.io/delta-lake-a-layer-to-ensure-data-quality/)，即[Delta-kernel-rs](https://docs.rs/delta_kernel/latest/delta_kernel/)库。这是一个库在Rust中可用，而C++中可能永远不会有（或很晚才有）的情况。

Clickhouse本可以在内部用C++为Delta Lake编写一个库，但Milovidov说这项工作将是“毫无意义的”。可怜的程序员会花时间编写解析JSON文件和重定向HTTP请求的代码。使用官方的Databricks基于Rust的发布版本更容易。

## Rust和C++的危险

通过这些实验，Clickhouse的开发人员了解了Rust语言的一些缺点，尤其是在与C++结合使用时。

一个挑战是可重现构建，这对于确保代码安全，而不是不小心从互联网上的某个地方下载是必要的。Clickhouse已经完成了C++中的可重现构建过程，但对于Rust，他们必须重新考虑如何再次确保密封构建的过程。

为Rust程序编写C++封装也是一个挑战。弄清楚是在C++还是Rust中分配内存可能很棘手。[模糊测试工具](https://thenewstack.io/developers-are-buzzing-on-fuzzing/)和Clickhouse的CI系统在这里帮助发现了很多错误。

两种语言在压力下的表现存在差异。

与C++相比，Rust程序和库倾向于“panic”太多，不符合Milovidov的喜好。“panic”可能是由于bug（表明需要对库进行更好的测试）。或者代码作者使用“panic”终止代替[调用异常](https://learn.microsoft.com/en-us/cpp/cpp/errors-and-exception-handling-modern-cpp?view=msvc-170)（这往往[不被Rustaceans所认可](https://doc.rust-lang.org/book/ch09-00-error-handling.html)）。

“panic”对于批处理作业来说很酷，但对于实时运行的服务器和交互式应用程序来说，就没那么酷了。

“Rust中的库倾向于过度使用Panic，即使在不合适的情况下也是如此，我们必须找到并修复所有这些情况，以避免服务器应用程序突然终止，”Milovidov说。

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/a5e086de-clickhouse-03.jpg)](https://cdn.thenewstack.io/media/2025/11/a5e086de-clickhouse-03.jpg)

Milovidov声称，Rust代码不应该那么容易“panic”。

就像Clickhouse团队在C++库中发现并修复了bug一样，他们在Rust库中也发现了很多bug。

Milovidov还深入探讨了在同一环境中混合使用C++和Rust所带来的许多特殊性，特别是关于使用清理（sanitization）、管理交叉依赖、交叉编译以及开发人员的代码可组合性等问题。其中许多问题都源于所需构建系统的复杂性。

转向Rust的另一个意想不到的副作用：更多的依赖项。对于整个代码库，Clickhouse只有156个依赖项。当引入Rust模块时，他们发现自己额外管理了672个传递性Rust依赖项（Milovidov打趣说，这仍然没有[NPM](https://thenewstack.io/18-popular-npm-packages-compromised-in-attack/)那么多）。

## Clickhouse的经验

无论如何，目前Clickhouse已决定不使用Rust重写整个数据库系统。但他们对该语言足够自信，允许第三方贡献者用该语言提交自己的Clickhouse附加组件。

“Rust是一种很棒的语言，”Milovidov说。