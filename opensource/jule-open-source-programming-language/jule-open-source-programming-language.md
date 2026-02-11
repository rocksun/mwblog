<!--
title: Jule 语言：内存安全的 C/C++ 替代方案浮出水面
cover: https://cdn.thenewstack.io/media/2026/02/9088479c-nick-fewings-4pzu15oetxa-unsplash-1.jpg
summary: Jule是一种新兴的内存安全系统编程语言，旨在替代C/C++。它融合了Go的生产力和C的性能，强调内存安全、C/C++互操作性和编译时功能。尽管仍处于测试阶段，面临标准化挑战，但其技术前景乐观。
-->

Jule是一种新兴的内存安全系统编程语言，旨在替代C/C++。它融合了Go的生产力和C的性能，强调内存安全、C/C++互操作性和编译时功能。尽管仍处于测试阶段，面临标准化挑战，但其技术前景乐观。

> 译自：[Memory-Safe Jule language emerges as C/C++ alternative](https://thenewstack.io/jule-open-source-programming-language/)
> 
> 作者：Darryl K. Taft

随着美国政府及其他机构呼吁在关键系统中使用[内存安全的编程语言](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/)，一种新兴的开源 C/C++ [替代品 Jule](https://jule.dev/) 应运而生。

Jule 官网将其描述为一种“简单安全的编程语言，具有内置并发性、一流的 C/C++ 互操作性和强大的编译时功能”。

尽管 Jule 项目始于 2022 年，目前仍处于测试阶段，但它的出现表明，开发者正在关注除了[不内存安全](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/)的 C 和 C++ 之外，以及[内存安全](https://thenewstack.io/introduction-to-go-programming-language/)的 Go 和 [Rust](https://thenewstack.io/rust-programming-language-guide/) 之外的系统编程语言。

事实上，在 2024 年，美国[网络安全和基础设施安全局](https://thenewstack.io/who-should-be-responsible-for-software-security/)和联邦调查局就持续困扰关键基础设施的基本安全漏洞发出了严厉警告。

在一份联合报告中，这些机构警告软件制造商必须在 2026 年 1 月 1 日之前制定内存安全路线图。

报告指出：“对于使用内存不安全语言编写的现有产品，如果在 2026 年 1 月 1 日之前没有发布内存安全路线图，将是危险的，并显著提升国家安全、国家经济安全以及国家公共健康和安全的风险。”

Jule 应运而生，它是一种静态类型、编译型、通用系统编程语言，专注于简洁性、性能和安全性。Jule 手册称，它旨在提供原生级别的性能、可预测的行为和实用的安全性，同时不牺牲清晰性或开发人员的生产力。Jule 旨在提供 Go 的生产力与 C 的性能。

## Jule 的安全性

Jule 深受 Go 和 Rust 的影响，其中 Go 的影响最大。Jule 手册解释说，尽管 Rust 以其严格而全面的安全保障而闻名，但 Jule 也有效地解决了安全问题。然而，Jule 采用了一种不那么严格、更灵活的安全模型，更接近 Go 的理念。与 Go 一样，Jule 会对边界违规和空指针解引用执行运行时检查，以确保基本的内存安全。

同时，Jule 引入了额外的编译时安全分析，并执行静态检查以尽早发现常见的错误类型。

然而，一个关键区别是 Jule 采用了类似于 Rust 的[默认不可变](https://users.rust-lang.org/t/is-immutability-by-default-worth-the-hassle/83668)模型。除非明确声明为可变，否则变量是不可变的。Jule 手册指出，在安全 Jule 模式下，此规则严格执行：不可变内存不能被修改。

## C/C++ 互操作性

Jule 从一开始就被设计为与 C 和 C++ 互操作，并与现有的 C 和 C++ 生态系统共存。它还编译为 C++ 作为中间表示，并利用成熟的后端编译器，例如 [GCC](https://thenewstack.io/rust-support-is-being-built-into-the-gnu-gcc-compiler/) 和 [Clang](https://clang.llvm.org/)。

Jule 不仅仅提供简单的代码翻译；它还提供了专门设计用于简化和[加强互操作性](https://manual.jule.dev/integrated-jule/)的内置语言功能。
Jule 还为其[运行时](https://manual.jule.dev/runtime/)提供了 C++ API，使其更容易扩展 Jule 或将其直接集成到现有的原生代码库中。

Jule 手册指出：“最重要的是，我们拒绝为了采用一种新语言而放弃现有的 C 和 C++ 代码库或重写数千行经过验证的代码。”“我们想要的不仅仅是临时的桥梁或脆弱的变通方案。我们希望互操作性成为语言设计中一流的、有意的组成部分。”

此外，尽管 Jule 具有 C/C++ 互操作性，但手册表示，“我们的首要任务是尽可能使用纯 Jule 开发标准库包和编译器。”“集成现有的 C/C++ 库以实现某个功能并不是一个受欢迎的想法。相反，更倾向于将其设计为第三方绑定库包。”

## 错误处理

手册的常见问题解答中有一个问题：为什么 Jule 使用异常（exceptionals）而不是其他错误处理方法？

回复[称](https://manual.jule.dev/some-questions.html#why-does-jule-use-exceptionals-instead-of-other-error-handling-methods:~:text=Exceptional%20handling%20is%20considered%20to%20be%20more%20efficient%20and%20safer%20in%20using%20an%20alternative%20value%20or%20handling%20exceptional%20and%20returning%20in%20elegant.)：“异常处理在替代值使用或异常处理并优雅返回方面被认为更高效、更安全。异常在可读性和安全性方面被评估为更合适。”

手册称，异常通常类似于 Go 的错误返回。

同时，Jule 手册断言：“由于 Jule 受 Go 的影响很大，许多 Go 代码可以很容易地适应 Jule。Go 和 Jule 具有非常相似的语义。实现现有代码并不太困难。”

此外，在简洁性和可维护性方面，Jule 深受 Go 的影响。

## 效率

Jule 的设计旨在实现高性能，同时保持低内存使用。它针对效率、可预测性和控制至关重要的系统级工作负载。

手册称，Jule 的参考编译器还执行自己的优化以生成高质量的中间表示 (IR)，而不是仅仅依赖后端来提高性能。

此外，为了提高内存效率，Jule 避开了传统反射等运行时开销大的功能，转而依赖编译时反射，它可以在不增加运行时成本的情况下提供相同的表达能力。

Reddit 上的一些[观察者](https://www.reddit.com/user/iMadz13/)指出，Jule 的名字与 [Julia](https://julialang.org/) 太接近，后者是一种专为高性能数值和科学计算设计的高级动态编程语言。

一位名叫 [tegahertz](https://www.reddit.com/user/tegahertz/) 的 Reddit 用户回复道：“是的，它的名字有些相似，但并未受到 Julia 的影响。事实上，我不能说它是一种被设计为 C++ 继任者的语言。它只是一种系统编程的替代语言，但也可以说 C++ 也适合被视为继任者。”

## Jule 的未来

尽管 Jule 仍处于测试阶段，但自称为“[Julenours](https://jule.dev/code-of-conduct)”的社区正在努力使该语言更加稳定并构建一个强大的标准库。

手册中写道：“为了让社区和官方开发者更容易为 Jule 开发任何工具，Jule 官方编译器的大部分内容都包含在标准库中。”“标准库包含词法分析器、解析器和语义分析器等重要阶段，适用于工具开发。”

Forrester Research 分析师 [Andrew Cornwall](https://www.linkedin.com/in/acornwall/) 告诉 *The New Stack*：“Jule 尚未标准化，这意味着无论其技术进步如何，企业都很难对其进行投入。Jule 也缺乏开发工具，所以我预计我们不会看到开发人员普遍采用 Jule 的压力。”

此外，Andrew Cornwall 指出：“用 Jule 编写的代码非常少，因此 AI 代码生成将是基本的。”“目前，Jule 看起来仍处于‘激情项目’阶段。这并不意味着它不会突破——Ruby 也曾是一个激情项目——但它需要更多的动力和额外的视角才能走向成熟。”

尽管 Andrew Cornwall 指出了 Jule 在企业采用方面面临的诸多挑战，但 Futurum Group 分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 提供了更为乐观的技术评估。

Brad Shimmin 告诉 *The New Stack*，关于 Jule，“它看起来很有趣，类似于 Go、[Zig](https://ziglang.org/)，当然还有 Rust，它在安全、性能和简洁性之间取得了许多语言必须保持的微妙平衡。对我来说，它对编译时功能的强调非常突出，这通常会带来更可预测和更高性能的代码执行，这对于系统软件来说是件好事。”