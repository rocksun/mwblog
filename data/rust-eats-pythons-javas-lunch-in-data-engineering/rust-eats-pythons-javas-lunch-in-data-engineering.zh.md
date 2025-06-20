[Rust](https://thenewstack.io/rust-programming-language-guide/) 编程语言正在进入新的领域，包括企业数据管道。

虽然大多数行业依赖 [Python](https://thenewstack.io/python/) 和 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 进行数据处理，但越来越多的公司发现 Rust 在性能、安全性和现代设计方面的结合使其成为数据密集型工作负载的变革者。

最新的证据来自 [Singular](https://www.singular.net/)，他们的新 [Extract](https://www.extract.to/) 平台与已建立的 [提取、加载、转换 (ELT)](https://thenewstack.io/the-future-of-data-integration/) 工具相比，性能提高了 17 倍，成本降低了高达 70% —— 全部由 Rust 提供支持。

## 为什么 Rust 对数据工程至关重要

Rust 解决了多年来困扰 [数据工程](https://thenewstack.io/demystifying-data-engineering/) 的根本问题。大多数 ELT 平台运行在为不同目的设计的语言上——Python 为了简单性，Java 为了企业采用。Singular 的首席执行官 [Gadi Eliashiv](https://www.linkedin.com/in/gadie/) 告诉 The New Stack，两者都带来了巨大的开销：不可预测地暂停执行的[垃圾收集器](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/)、消耗内存的运行时环境以及使开发人员远离底层硬件的抽象。

然而，他说，Rust 消除了这些权衡。它提供了 C 级别的性能，并具有内存安全保证，可以防止整个类别的错误，所有这些都包含在一种现代语言设计中，不会让人觉得是倒退。

“我只是爱上了它，因为我确实感受到了指尖的力量，”Eliashiv 说。“我就像，我正在编写可能是内核代码的东西。它非常高效，而且这种语言同时非常现代化。”

## 内存效率革命

数字说明了一切。Singular 的团队比较了他们的遗留 Python 实现和他们的新 Rust 版本之间的等效连接器代码。使用 Rust，他们实现了 20 倍的内存消耗减少。对于多租户 SaaS 平台来说，这是变革性的，他说。

“我们基本上可以在给定的服务器上容纳 20 倍的客户，因此我们可以为客户提供显着的成本节省，”Eliashiv 解释说。该公司报告称，客户的成本节省超过 50%，某些操作的效率比遗留工具高 100 倍。

这种效率提升不是理论上的。他指出，Extract 已经在为包括华纳兄弟和艺电在内的企业客户提供服务，以传统 Python 或 Java 平台难以承受的规模处理数据。

## 内存安全：隐藏的优势

Eliashiv 的团队在网络安全和漏洞研究方面拥有丰富的经验，这让他们对为什么内存安全对生产系统很重要有独特的见解。

“每次有人在 C、C++ 中错误使用数组或结构体时，他们都会释放一些内存区域两次。这是漏洞的来源，”他说。“事实上，我们不必在 Rust 中考虑它，这太不可思议了，因为我们可以编写实际上是 C/C++ 级别效率的代码，而不必担心所有这些事情。”

Eliashiv 说，对于处理敏感企业信息的数据管道来说，这不仅仅是为了防止崩溃，而是为了防止可能导致数据泄露或静默数据损坏的那种内存损坏错误。

## Rust 开发的现实

但 Rust 的采用并非没有挑战。与 Python 丰富的预构建数据连接器生态系统不同，Rust 需要从头开始构建基础设施。

“最初的基础设施花费了一段时间，因为……没有很多人使用 Rust 编写连接器，”Eliashiv 承认。该团队花费了大量时间来构建可以处理他们需要支持的各种 REST API 和数据格式的基础。

然而，一旦该基础设施到位，开发速度就会提高。Rust 编译器的严格检查会在编译时而不是运行时捕获错误，从而减少调试周期并提高对代码质量的信心，他说。

## 扩展 Rust 团队

然而，人才问题对于 Rust 的采用仍然是一个大问题。Eliashiv 的方法是有条不紊的——从公司最好的工程师开始，建立模式和基础设施，然后扩大范围。

“我们选择了公司里最好的工程师，并为这个产品组建了一个特殊的团队，他们是第一批学习 Rust 的人，”他解释说。许多人都有 C 和 C++ 的背景，这 облегчило 了过渡。

作为一项额外的好处，Rust 严格的编译器成为一项培训优势。“与 Python 不同，[新开发人员]破坏代码的可能性非常小，因为有一个编译器，它可以确保你不会把事情搞砸，”Eliashiv 说。“我们更有信心让人们入职并交给他们明确的任务。”

他补充说，像 Cursor 这样的人工智能编码工具帮助加速了这一过程，帮助开发人员理解 Rust 概念，甚至实现了跨职能的贡献。

## 超越数据管道：Rust 不断扩展的范围

其影响不仅仅限于 ELT 平台。

“我认为 Rust 有一个实时变体，你没有完整的标准库，但你可以编写超高效的代码，”Eliashiv 说。“我认为它对于所有这些不同类型的用例来说都很棒。”

他指出，该语言继续快速发展，[异步编程](https://thenewstack.io/3-types-of-asynchronous-programming/) 和生态系统成熟度的改进使其对于要求苛刻的实时应用程序越来越可行。

## 拐点

Rust 在数据工程中的采用标志着更广泛的转变。随着云成本持续攀升和数据量爆炸式增长，Rust 提供的效率提升直接转化为商业价值。性能的改进提供了竞争优势。

SciPlay 的产品总监 [Gal Karniel](https://www.linkedin.com/in/gal-karniel-774288134/) 在一份声明中说：“Extract 为我们提供了我们需要的性能，以及我们的团队想要的简单性——而且所有这些都没有雇用另一位工程师。”

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可播放我们所有的播客、访谈、演示等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

组
用 Sketch 创建。

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft 在巴尔的摩地区的办公室报道 DevOps、软件开发工具和与开发人员相关的问题。他在这个行业有超过 25 年的经验，并且总是在寻找下一个独家新闻。他曾...

阅读更多 Darryl K. Taft 的文章](https://thenewstack.io/author/darryl-taft/)
