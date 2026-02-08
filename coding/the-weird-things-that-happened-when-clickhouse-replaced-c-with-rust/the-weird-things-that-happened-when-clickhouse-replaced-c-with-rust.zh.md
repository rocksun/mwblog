ClickHouse决定将其部分代码库转向 [Rust](https://thenewstack.io/rust-programming-language-guide/) 是一个完美的风暴：一个广受欢迎的数据库与一种势头强劲的语言的结合。虽然ClickHouse因其自身优势而获得广泛采用，但Rust作为一种优雅、现代的编程语言，其爆炸式增长和成为首选语言的地位，可以说当之无愧——不仅在此次ClickHouse案例中如此，在许多项目中也得到了体现，包括 [Linux 内核](https://thenewstack.io/rust-in-the-linux-kernel/) 的部分，取代了 [C 语言代码](https://thenewstack.io/the-obfuscated-c-code-competition-returns/)。

话虽如此，在周日于布鲁塞尔举行的 [FOSDEM 2026](https://fosdem.org/2026/) 上，ClickHouse 的联合创始人兼CTO Alexey Milovidov 明确表达了他所关心的是什么：不是炒作，而是Rust在此次题为“ClickHouse的C++和Rust之旅”的 [演讲](https://fosdem.org/2026/schedule/event/NBLNRY-rust-clickhouse/) 中能为ClickHouse带来什么具体益处。事实上，他明确反对炒作，甚至称其为Rust的负面因素之一，尽管本周FOSDEM对Rust的浓厚兴趣——我个人认为这种兴趣是当之无愧的。

人们对ClickHouse转向Rust的动机和方式表现出巨大兴趣，值得注意的是，这次转型并非一帆风顺，也未像许多人想象的那样代表着一个巨大的转变。事实上，Milovidov 告诉 *The New Stack*，ClickHouse 大约 98% 的运行时仍然是 C++。

然而，在深入探讨这些细节之前：在他周日的演讲结束后，我问 Milovidov 在过去几周里最让他惊讶的是什么。他的回答并非关于 Rust 本身，而是关于最近发生的、令他措手不及的一些意想不到的事情。

在我们的讨论中，Milovidov 表示，他的团队在向 Rust 持续转型期间面临的“最奇怪”的挑战与构建系统和构建基础设施有关。一个具体例子是 Delta 内核库，他发现该库在内存清理器下被禁用。问题源于该库没有提供内存清理器正常运行所需的某些符号，这个问题他在演讲和我们的谈话前“一两天”才发现。这突显了在混合不同语言生态系统时，维护严格测试环境的难度。

“Delta 内核库在内存清理器下被禁用……一些成员所需的符号没有提供，”Milovidov 说。“这很奇怪。”

我们的大部分讨论都涉及澄清 ClickHouse 对 Corrosion 的使用，Corrosion 是一款用于集成 C++ 和 Rust 的开源工具。关于迁移方向有一点需要澄清：这不是从 Corrosion 到 C++ 的迁移，而是在保留 Rust 代码的同时，在 C++ 基础上进行构建。Milovidov 证实，Rust 代码没有改变，库也保持不变。他们不是翻译代码，而是将继续使用 Rust 进行构建。

在演讲中，Milovidov 回忆说，最初转向 Rust 时，正如前面提到的，出现了一个库没有提供某些符号的问题。Milovidov 表示，交叉膨胀（cross inflation）情况好得多，尽管团队付出了巨大的努力，这并不容易。他观察到，由于某种原因，系统最终出现了两个不同版本的 OpenSSL。最后，他提到他们可以在各自的环境中运行它，并以相同的方式将其“粘合”起来，以避免符号带来的意外。

“这和整个项目都需要付出巨大的努力，”Milovidov 说。“这并不容易。”