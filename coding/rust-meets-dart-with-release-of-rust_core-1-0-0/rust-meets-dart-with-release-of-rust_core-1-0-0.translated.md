# Rust 与 Dart 携手：rust_core 1.0.0 版本发布

![Rust 与 Dart 携手：rust_core 1.0.0 版本发布的特色图片](https://cdn.thenewstack.io/media/2024/07/81d81aea-getty-images-i34igy4qrje-unsplash-1024x683.jpg)

[rust_core](https://github.com/mcmah309/rust_core) 1.0.0 版本已发布。根据 [r/dartlang subreddit](https://www.reddit.com/r/dartlang/comments/1dtzhyy/rust_core_v100_released/)，rust_core 是 [Dart](https://dart.dev/) 中 [Rust](https://www.rust-lang.org/) 核心库的实现。

通过调整 [Rust 的特性](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/) 以符合 Dart 的原则，该实现的目标是在两种语言之间创建无缝且自然的集成。这使开发人员能够使用以前仅限于 [Rust 开发人员](https://thenewstack.io/aws-gifts-java-rust-developers-with-useful-tools/) 的高级工具，从而实现两种语言之间的平滑过渡。

[项目目标](https://mcmah309.github.io/rust_core/) 指出，“rust_core 努力在每个特性中都带来可靠性和性能。每个特性都经过了严格的测试。超过 500 个有意义的测试套件，并且还在不断增加。”

此外，“对于参与 Dart 编程的 Rust 开发人员，或者对惯用且 [安全编程](https://thenewstack.io/microsoft-rust-is-the-industrys-best-chance-at-safe-systems-programming/) 感兴趣的 Dart 开发人员，我们开发了 ‘rust_core’，一个旨在用 Dart 实现 Rust 核心库的包，”[Henry McMahon](https://github.com/mcmah309) 在去年 11 月的一篇 [博客文章](https://mcmah309.github.io/#/blog) 中写道。

rust_core 项目背后的公司名为 [Voyver](https://voyver.com/)，这是一家专注于人工智能和教育软件领域的初创公司。McMahon 是 rust_core 团队的主要维护者。

“我们在技术栈中主要使用 Dart 和 Rust，”他告诉 The New Stack。“一个通用的 API 被认为是主要由 Rust 开发人员组成的团队和代码库中缺失的部分。rust_core 为我们解决了这个问题。”

## Rust Core 手册

为了支持 1.0.0 版本的发布，该项目还发布了 [Rust Core 手册](https://mcmah309.github.io/rust_core/)。

Rust Core 手册包含一个常见问题解答，其中第一个问题是：[即使我不了解 Rust，为什么要使用 Rust Core？](https://mcmah309.github.io/rust_core/introduction/FAQ.html#why-use-rust-core-even-if-i-dont-know-rust)

在回答中，常见问题解答写道：“从语言的角度来看，我们认为 Dart 在几个方面存在不足，而这个包解决了这些问题：

- Dart 使用未经检查的 try/catch 异常。为了可维护性，首选将错误作为值处理，因此使用 `Result` 类型。
- Dart 有可空类型，但您无法进行特定于空或非空的运算，除非使用大量的 `if` 语句。`Option<T>` 通过零运行时成本解决了这个问题，并且您可以轻松地在可空类型之间来回切换，因为它只是 `T?` 的零成本扩展类型。
- Dart 缺少 Rust 的 `?` 运算符的功能，因此我们在 Dart 中实现了它。
- Dart 缺少内置的 `Cell` 类型或等效类型（以及 `OnceCell` / `LazyCell` ）。
- Dart 的 `List` 类型是数组/向量联合（它是可增长的或不可增长的）。这在类型层面上不可见，这可能会导致运行时异常，并鼓励在任何地方使用可增长的 `List`，即使您不需要，这也会降低性能。因此，我们添加了 `Arr`（数组）。
- Dart 没有切片类型的概念，因此分配子列表是唯一的方法，这效率不高。因此，我们添加了 `Slice<T>`。
- Dart 的隔离之间通信是通过端口（`ReceivePort` / `SendPort`）进行的，它是无类型的，而且很糟糕，我们通过引入 `channel` 来标准化这种通信，用于类型化的双向隔离通信。
- Dart 的迭代方法对于 `Iterable` 和 `Iterator` 来说很缺乏（根本没有！只有 `moveNext()` 和 `current`），而 Rust 有很多有用的方法。因此，我们引入了 Rust 的 `Iterator`。”

与此同时，[Rust 在更广泛的用例中被采用](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/)，在这些用例中，建议使用内存安全的编程。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)