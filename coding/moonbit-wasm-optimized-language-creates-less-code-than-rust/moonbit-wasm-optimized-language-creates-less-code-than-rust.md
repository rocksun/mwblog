
<!--
title: MoonBit：Wasm 优化语言，代码量少于 Rust
cover: https://cdn.thenewstack.io/media/2024/06/6c29d018-moonbitlang.png
-->

MoonBit 是一种端到端的编程语言，针对 WebAssembly 进行了优化，同时也可以编译成 JavaScript 和汇编代码。

> 译自 [MoonBit: Wasm-Optimized Language Creates Less Code Than Rust](https://thenewstack.io/moonbit-wasm-optimized-language-creates-less-code-than-rust/)，作者 Loraine Lawson。

WebAssembly 最初的承诺是，很多语言都可以编译成它，然后在浏览器或其他环境中运行。然而，问题在于现有的语言，例如 Java、Go 甚至 Rust 在编译时会生成大量的 WebAssembly 代码，即使它们仅仅是打印“Hello World”，IDEA 科学家、语言开发人员 [Hongbo Zhang](https://github.com/bobzhang) 说。

“WebAssembly 的优势还没有体现出来，”他说“我们说 WebAssembly 是安全且快速的，但是当 [Go](https://thenewstack.io/golang-variables-and-data-types-an-introduction/) 被编译到 WebAssembly 时，它生成了非常大量的 WebAssembly 代码，而且它不再快速，因为语言语义与 Go 并不十分匹配，”章说。“所以我们认为存在一个机会，一个巨大的机会，来拥有一种专为 WebAssembly 语义而设计的语言。”

所以 Zhang 创建了 [MoonBit](https://www.moonbitlang.com/)，这是一种新型[端到端开源编程语言，针对 WebAssembly 而优化](https://github.com/moonbitlang)，同时专为云计算和边缘计算以及前端应用程序而设计。

“我们对 WebAssembly 非常重视，因为我们认为 WebAssembly 具有非常大的潜力。它是一种新型指令集，跨平台——安全且快速。”他说。

Zhang 并不陌生于创建语言。他是 OCaml 编程语言的核心贡献者，该语言在学术界广受欢迎。他还与 ReScript 和 Meta 的内部编程语言 Flow 合作。在彭博期间，他创建了 [BuckleScript 编译器](https://www.bloomberg.com/company/press/open-source-at-bloomberg-introducing-bucklescript/)，将 OCaml 编译成 [JavaScript](https://thenewstack.io/javascript-framework-maintainers-on-unification-potential/)。 [编者按：BuckleScript 已更名为 ReScript 编译器。]

MoonBit 是为了以现有语言无法做到的方式对 WebAssembly 进行利用而编写的，他解释道。

“你不能改变 Golang 语义以适应 WebAssembly，”他说。“如果你需要制作一种新语言，那么我们可以利用这一事实，因为 WebAssembly 标准已经确定完成了。所以你可以让它非常快，生成非常小的 WebAssembly 代码，并且我们可以获得非常好的优势。”


## Moonbit 的灵感来自于 Rust 和 Go

这使其与同样设计为编译成 Wasm 的 Grain 语言处于相似的分类中。有趣的是，Grain 的创建者将 OCaml 作为他们的灵感来源。但两者之间的差异在于，Grain 仅限于 Wasm，而 MoonBit 采取了多后端语言方法，并针对其他后端（此处指服务器端开发）进行了优化，包括 JavaScript。它声称在 JavaScript 后端比 Json5 具有近八倍的性能优势。MoonBit 还正在探索 AI 原生语言工具链的可能性，以开发 AI 应用程序。

“事实上我们支持 WebAssembly、JavaScript 和原生后端，但我们对 WebAssembly 的优先级很高，”Zhang表示。“如果人们关心 WebAssembly 平台，他们就已经了解 WebAssembly，并且他们希望针对该平台找到某种非常好的解决方案，那么 MoonBit 可能是一个非常好的选择，因为我们生成的代码在性能方面可与 Rust 媲美，并且它还生成了比 Rust 更小的 Wasm 代码。”

他说，MoonBit 在很多方面都借鉴了 Rust。例如，它具有模式匹配、静态类型和类型推断。他补充说，这是一种像 Rust、Kotlin 和 Java 那样的强类型语言，这意味着它对数据类型强制执行严格的规则。

“我们取用了 Rust 中的优点，并尝试让它易于学习，”他说。

他将其描述为没有 Rust 部分缺点的 Rust 优点。

“另一个优势是我们拥有非常快的编译速度，所以 Rust 的一个痛点是编译时间非常长，”他说。“我们可以非常快地编译整个代码……比 Rust 编译快一到两个数量级。”

它与 Rust 的不同之处在于它很快就会附带一个垃圾收集器，该收集器使用自动引用计数 (ARC)。这类似于 Swift 对垃圾收集的方法。这使它能够进行自动内存管理。

Zhang说，MoonBit 的包系统和理念也从 Go 中汲取了灵感。

“Go 的理念是少即是多，我们认为这一点非常重要，”Zhang说。“你必须使语言本身具有凝聚力。我们不想继续添加语法。”

## IDE 已经可用

他说，它也与 Rust 不同，因为它具有容错类型系统和设计理念。

“我们决定使用容错类型系统的原因是，我们希望 IDE 与编译器共享相同的代码库，”他说。“所以对于传统的编译器，当你看到第一个错误时……编译器会在那里停止。但对于开发人员来说，我仍然希望有一个 IDE 来告诉我其他信息是正确的，即使程序不正确。我们有容错类型系统，容错于解析器，所以即使问题处于非常糟糕的状态，类型检查器仍然可以……给你一些信息来指导你进行自动完成。”

他补充说，当 IDE 与编译器不共享相同的代码库时，会导致结果不一致。

IDE 是开发人员可能发现 MoonBit 对 Wasm 有吸引力的另一个原因。对于新语言来说，从一开始就拥有 IDE 是不寻常的。通常，这需要数年时间，Zhang 说。

“因为我有很多使用语言工具的经验，我认为让语言对开发人员来说可用且令人愉快的最重要的一件事是他们拥有非常快、非常可靠的 IDE，”他说。“为了实现这一点，我设计了整个语言类型系统，以便快速分解，进行类型检查，然后 IDE 将从那里开始工作。”

他补充说，编译器只检查修改过的路径，因此这会创建一个非常快的 IDE 编辑周期。

## Moonbit 语言的用例

Zhang建议，关心性能的开发人员可能想尝试一下 MoonBit。

“如果他们想在浏览器中或用于无服务器编码使用 WebAssembly，这是首选，”他说。“他们可能关心 WebAssembly，然后一个非常重要的用途也是编译成 JavaScript。不仅编译成 JavaScript，我们还编译成非常高效的 JavaScript 代码；所有生成的 JavaScript 代码甚至比手写的 JavaScript 代码更快。”

他说，MoonBit 可以运行在云端或边缘。它可以专门用于 [Cloudflare Workers](https://thenewstack.io/cloudflare-raises-1-25-billion-for-startups-using-its-workers-platform/)，这是一个支持在 Cloudflare 全球网络边缘运行无服务器代码的平台，因为“运行时本质上是内置的，”他说。“你也可以用它来进行边缘计算和无服务器计算。”

Zhang在 ReScript 上也有前端方面的经验，ReScript 是针对 JavaScript 开发人员的。

“对于 JavaScript 人员来说，我们有几个优势，”他说。“第一，它有一个非常强大、可靠的 IDE，并为你提供最佳性能。”

他补充说，它还使用“非常花哨的优化器来使 [JavaScript 代码](https://thenewstack.io/solid-js-creator-outlines-options-to-reduce-javascript-code/) 更快”来编译 JavaScript。例如，该公司对用 JavaScript 编写的 JSON5 解析器进行了基准测试，并将相同的代码库、相同的算法迁移到了 MoonBit。他说，在该基准测试中，MoonBit 的性能比手写的 JavaScript 代码快大约七倍。

“当人们关心 WebAssembly 后端时，他们可能会选择 MoonBit 作为他们的理想语言选择，”Zhang说。“这就是 MoonBit 的故事从一开始就是 WebAssembly，但我们有一个非常雄心勃勃的目标，所以我们不仅针对 WebAssembly 进行了优化，也针对其他后端进行了优化。”

要探索该语言，请查看 [MoonBit 的在线沙箱](https://try.moonbitlang.com/)。
