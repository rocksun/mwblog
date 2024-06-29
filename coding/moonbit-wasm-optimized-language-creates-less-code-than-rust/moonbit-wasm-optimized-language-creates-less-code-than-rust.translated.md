# MoonBit: A Language Optimized for Wasm with Less Code Than Rust

![MoonBit: A Language Optimized for Wasm with Less Code Than Rust](https://cdn.thenewstack.io/media/2024/06/6c29d018-moonbitlang-1024x573.png)

WebAssembly's initial promise was that many languages could compile to it and then run in the browser or other environments. The problem, however, is that existing languages, like Java, Go, and even Rust, generate a lot of WebAssembly code when compiled, even if they're just printing "Hello World," says IDEA scientist and language developer [Hongbo Zhang](https://github.com/bobzhang).

"The advantage of WebAssembly is not realized," he says. "We say WebAssembly is safe and fast, but when [Go](https://thenewstack.io/golang-variables-and-data-types-an-introduction/) compiles to WebAssembly, it generates a lot of WebAssembly code, and it's not fast anymore because the language semantics don't match Golang very well," Zhang says. "So we think there's an opportunity, a big opportunity, to design a language that's tailored to the semantics of WebAssembly."

That's why Zhang created [MoonBit](https://www.moonbitlang.com/), a new end-to-end [open-source](https://www.moonbitlang.com/blog/moonbitlang-core-opensource#:~:text=MoonBit%20is%20a%20Rust%2Dlike,Core%2C%20under%20Apache%20License%202.0.) [programming language optimized for WebAssembly](https://github.com/moonbitlang), designed for cloud and edge computing as well as front-end applications.

"The reason why we are very focused on WebAssembly is because we think WebAssembly has huge potential. It's a new instruction set, and it's cross-platform — it's safe, it's fast," he says.

Zhang is no stranger to creating languages. He's a core contributor to the OCaml programming language, which is popular in academia. He also worked on ReScript and Flow, Meta's internal programming language. While at Bloomberg, he created the [BuckleScript compiler](https://www.bloomberg.com/company/press/open-source-at-bloomberg-introducing-bucklescript/), which compiles OCaml to [JavaScript](https://thenewstack.io/javascript-framework-maintainers-on-unification-potential/). [Editor's note: BuckleScript has been renamed to the ReScript compiler.]

MoonBit [is written to take advantage of WebAssembly](https://thenewstack.io/webassembly/using-web-assembly-written-in-rust-on-the-server-side/) in a way that existing languages can't, he explains.

"You can't change the semantics of Golang to fit WebAssembly," he says. "If you need to create a new language, then we can leverage the fact that the WebAssembly standard is finalized. So you can make it very fast, generate very small WebAssembly code, and we can get a big advantage."

## Moonbit Draws Inspiration from Rust and Go

This puts it in the same category as the language [Grain](https://thenewstack.io/meet-grain-the-high-level-language-optimized-for-webassembly/), which is also designed to compile to Wasm. Interestingly, Grain's creators cite OCaml as their inspiration. But the difference between the two is that Grain is limited to Wasm, while MoonBit takes a multi-backend language approach and is optimized for other backends — here, server-side development — [including JavaScript](https://www.moonbitlang.com/blog/js-support). It claims to have nearly [eight times the performance advantage](https://www.moonbitlang.com/blog/js-support) over Json5 on the JavaScript backend. MoonBit is also exploring the possibility of an [AI-native language toolchain](https://www.moonbitlang.com/blog/moonbit-ai) to develop [AI applications](https://thenewstack.io/5-best-practices-for-building-reliable-genai-apps/).

"Actually, we support WebAssembly, JavaScript, and native backends, but we are very focused on WebAssembly," Zhang says. "If people care about the WebAssembly platform, they already know WebAssembly, and they want to get some very optimized solutions for that platform, then MoonBit might be a very good choice because the code we generate is comparable to Rust in terms of performance, and it generates even smaller Wasm code than Rust."

In many ways, MoonBit draws inspiration from Rust, he says. For example, it has pattern matching, static typing, and type inference. It's a strongly typed language, like Rust, [Kotlin](https://thenewstack.io/get-started-using-kotlin-multiplatform-with-a-network-listener-project/), and [Java](https://thenewstack.io/remotely-record-java-logs-from-containers/), he adds, meaning it enforces strict rules on data types.

"We took the good things from Rust and tried to make it easy to learn," he says.

He describes it as the essence of Rust, without some of its pain points.
“另一个优势是我们拥有非常快的编译速度，所以 Rust 的一个痛点是编译时间非常长，”他说。“我们可以非常快地编译整个代码……比 Rust 编译快一到两个数量级。”

它与 Rust 的不同之处在于它很快就会附带一个垃圾收集器，该收集器使用自动引用计数 (ARC)。这类似于 Swift 对垃圾收集的方法。这使它能够进行自动内存管理。

张说，MoonBit 的包系统和理念也从 Go 中汲取了灵感。

“Go 的理念是少即是多，我们认为这一点非常重要，”张说。“你必须使语言本身具有凝聚力。我们不想继续添加语法。”

## IDE 已经可用
他说，它也与 Rust 不同，因为它具有容错类型系统和设计理念。

“我们决定使用容错类型系统的原因是，我们希望 IDE 与编译器共享相同的代码库，”他说。“所以对于传统的编译器，当你看到第一个错误时……编译器会在那里停止。但对于开发人员来说，我仍然希望有一个 IDE 来告诉我其他信息是正确的，即使程序不正确。我们有容错类型系统，容错于解析器，所以即使问题处于非常糟糕的状态，类型检查器仍然可以……给你一些信息来指导你进行自动完成。”

他补充说，当 IDE 与编译器不共享相同的代码库时，会导致结果不一致。

IDE 是开发人员可能发现 MoonBit 对 Wasm 有吸引力的另一个原因。对于新语言来说，从一开始就拥有 IDE 是不寻常的。通常，这需要数年时间，张说。

“因为我有很多使用语言工具的经验，我认为让语言对开发人员来说可用且令人愉快的最重要的一件事是他们拥有非常快、非常可靠的 IDE，”他说。“为了实现这一点，我设计了整个语言类型系统，以便快速分解，进行类型检查，然后 IDE 将从那里开始工作。”

他补充说，编译器只检查修改过的路径，因此这会创建一个非常快的 IDE 编辑周期。

## Moonbit 语言的用例
张建议，关心性能的开发人员可能想尝试一下 MoonBit。

“如果他们想在浏览器中或用于无服务器编码使用 WebAssembly，这是首选，”他说。“他们可能关心 WebAssembly，然后一个非常重要的用途也是编译成 JavaScript。不仅编译成 JavaScript，我们还编译成非常高效的 JavaScript 代码；所有生成的 JavaScript 代码甚至比手写的 JavaScript 代码更快。”

他说，MoonBit 可以运行在云端或边缘。它可以专门用于 [Cloudflare Workers](https://thenewstack.io/cloudflare-raises-1-25-billion-for-startups-using-its-workers-platform/)，这是一个支持在 Cloudflare 全球网络边缘运行无服务器代码的平台，因为“运行时本质上是内置的，”他说。“你也可以用它来进行边缘计算和无服务器计算。”

张在 ReScript 上也有前端方面的经验，ReScript 是针对 JavaScript 开发人员的。

“对于 JavaScript 人员来说，我们有几个优势，”他说。“第一，它有一个非常强大、可靠的 IDE，并为你提供最佳性能。”

他补充说，它还使用“非常花哨的优化器来使 [JavaScript 代码](https://thenewstack.io/solid-js-creator-outlines-options-to-reduce-javascript-code/) 更快”来编译 JavaScript。例如，该公司对用 JavaScript 编写的 JSON5 解析器进行了基准测试，并将相同的代码库、相同的算法迁移到了 MoonBit。他说，在该基准测试中，MoonBit 的性能比手写的 JavaScript 代码快大约七倍。

“当人们关心 WebAssembly 后端时，他们可能会选择 MoonBit 作为他们的理想语言选择，”张说。“这就是 MoonBit 的故事从一开始就是 WebAssembly，但我们有一个非常雄心勃勃的目标，所以我们不仅针对 WebAssembly 进行了优化，也针对其他后端进行了优化。”

要探索该语言，请查看 [MoonBit 的在线沙箱](https://try.moonbitlang.com/)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)