我最近写了关于微软 Azure CTO [Mark Russinovich](https://www.linkedin.com/in/markrussinovich) 谈论 [Rust 代码如何在 Windows 中发布](https://thenewstack.io/microsofts-rust-bet-from-blue-screens-to-safer-code/) 的文章，但我没有涵盖他在本月早些时候在西雅图举行的 [RustConf 2025](https://rustconf.com/) 上所说的全部内容。事实上，我甚至没有涵盖一半。

虽然我主要写了关于微软用 [Rust](https://thenewstack.io/rust-programming-language-guide/) 重写 Windows 组件的文章，但这只是 Russinovich 在活动主题演讲中的开场。他花了大量时间展示了一些项目，这些项目揭示了微软实际上已经深入 Rust 的程度。

## 毫秒级的虚拟机

他对 [Hyperlight](https://opensource.microsoft.com/blog/2024/11/07/introducing-hyperlight-virtual-machine-based-security-for-functions-at-scale/) 的讨论确实令人印象深刻。Russinovich 展示了一个在 1.5 毫秒内启动虚拟机 (VM) 的系统。不是 [容器](https://thenewstack.io/introduction-to-containers/)，而是具有适当隔离边界的实际虚拟机。

“听着，我们不希望使用完整的管理程序和完整的操作系统来运行一些我们不信任的用户代码，”他一边说，一边拿出幻灯片展示架构。“对于运行一个微小的函数来说，这太过分了。”

[Hyperlight 最初](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/) 是一个 [C#](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/) 原型，但在性能变得至关重要时，用 Rust 重写了。它现在正在 [Azure Front Door](https://azure.microsoft.com/en-us/products/frontdoor) 中处理真实的流量，客户可以在其中部署处理网络请求的边缘函数。这个用例很有意义——你需要对不受信任的代码进行强大的隔离，但 [传统的虚拟机](https://thenewstack.io/why-chainguard-is-doubling-down-on-virtual-machines-in-a-container-world/) 对于可能每秒运行数千次的函数来说太慢了。

Hyperlight 令人印象深刻的是它的极简性。没有访客操作系统，只有一个小型运行时，为内部运行的代码提供 API。它支持 [WebAssembly](https://thenewstack.io/webassembly/) 和原生二进制文件，但无论哪种方式，与完整的 VM 堆栈相比，攻击面都很小。

此外，Russinovich 说，它完全是开源的。

## 有用的构建集成

微软还解决了如何在现有项目中使用 Rust 而无需重写所有内容的问题。

他们的答案是一个用于 [MSBuild](https://www.incredibuild.com/integrations/msbuild) 的 [Cargo](https://doc.rust-lang.org/cargo/) 插件，它允许你将 Rust 模块放入 [C++](https://thenewstack.io/introduction-to-c-programming-language/) 和 C# 代码库中。Russinovich 承认这是迫不得已的：“我们不能仅仅告诉团队放弃数百万行可用的代码。”

该插件很简单：你编写 Rust 代码，Cargo 构建它，MSBuild 将其视为任何其他依赖项。但是，要正确处理链接和 [ABI](https://en.wikipedia.org/wiki/Application_binary_interface) 细节需要大量工作。微软也开源了这一点，这表明它认为其他公司也将面临同样的问题。

这种实用的工具感觉可以推动 [Rust 的采用](https://thenewstack.io/survey-memory-safe-rust-gains-45-of-enterprise-development/)。大多数公司不会重写整个应用程序，但如果足够容易，它们可能会替换安全关键模块。

## 不糟糕的指南

Russinovich 说，微软还发布了它的“[务实的 Rust 指南](https://microsoft.github.io/rust-guidelines/)”——本质上是它在企业规模上编写 Rust 代码的内部手册。他对此直言不讳：“如果你是一位经验丰富的 Rust 开发人员，那么这一切都不会让你感到惊讶。这实际上是为新手准备的。”

有趣的是，他们制作了两个版本——一个供人类使用，另一个是专门为 AI 编码助手格式化的精简版本。Russinovich 指出：“你可以将其放入你的 Copilot 指令中，AI 实际上会遵循它。”

该指南涵盖了诸如错误处理模式、外部函数接口 (FFI) 最佳实践以及何时使用不同的异步运行时等内容。没有什么革命性的，但是拥有官方的微软建议可以帮助团队避免常见的陷阱。

AI 优化版本是一个聪明的举措，因为现在有很多 Rust 代码都是在 AI 助手的帮助下编写的。拥有与这些工具配合良好的指南表明，微软正在以务实的态度思考开发是如何进行的。

## 重写皇冠上的明珠

然后 Russinovich 解释说，微软正在用 Rust 重写其 [SymCrypt](https://github.com/microsoft/SymCrypt) 加密库。

SymCrypt 不仅仅是另一个库。它是微软的加密核心——处理 Windows、Azure 和 Office 中 RSA、椭圆曲线以及所有其他加密代码的代码。“这实际上是我们最敏感的代码，”Russinovich 说。

但这不仅仅是做一个直接的端口。[Microsoft Research 拥有用于 Rust 的形式验证工具](https://www.microsoft.com/en-us/research/blog/rewriting-symcrypt-in-rust-to-modernize-microsofts-cryptographic-library/)，因此它可以证明新加密代码的数学属性。经过验证的 Rust 甚至可以转换回 C++，以便更轻松地与现有系统集成。

像 [ML-KEM](https://csrc.nist.gov/pubs/fips/203/final)（后量子密钥交换标准）这样的新算法正在从头开始用 Rust 编写。这表明微软认为 Rust 将成为其未来的加密语言，不仅适用于新项目，而且适用于其最关键的现有代码。

它愿意触及 SymCrypt 这一事实表明，它对 Rust 工具和开发人员的专业知识充满信心。

## AI 驱动的代码翻译

演讲中最具未来感的部分涉及应用于代码翻译的 [Microsoft 的 GraphRAG 技术](https://microsoft.github.io/graphrag/)。Russinovich 演示了一个自动将 Python 应用程序转换为 Rust，同时保留结构和功能的工具。

他展示了一个用 [Python](https://thenewstack.io/what-is-python/) 编写的简单横向卷轴游戏：三个文件，总共大约 200 行代码。该翻译工具分析了代码结构，理解了模块之间的关系，并生成了等效的 Rust 代码，该代码可以编译并以相同的方式运行。

Russinovich 在展示来自标准 ChatGPT 翻译的损坏代码时说：“普通的 LLM [大型语言模型] 翻译会产生垃圾。”“但是，如果你让 AI 对整个代码库有一个语义上的理解，它就可以推断出代码实际在做什么。”

演示成功了，但目前尚不清楚这在多大程度上可以扩展到更大、更复杂的代码库。一个三文件的 Python 游戏是一回事；一个百万行的 C++ 应用程序完全是另一回事。

尽管如此，如果微软能够使自动翻译可靠，它就可以解决 Rust 采用的最大障碍。大多数公司都有庞大的现有代码库，他们无法手动重写。

## 现实检验

然而，Russinovich 对 Rust 的缺点直言不讳。他说，微软的内部调查显示，开发人员仍然在互操作性、异步调试和动态链接方面遇到困难。C++ 开发人员的学习曲线确实很困难。

“当你来自 C++ 时，这是一种冲击，”他承认。“你的大脑必须完全重新调整你对内存和所有权的思考方式。”

但他表示，即使是抱怨 Rust 的开发人员也不想回到 C++。几个月后，他们会适应并成为拥护者。性能始终更好。整个类别的错误都会消失。

微软在工具改进方面投入了大量精力——[Visual Studio Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) 集成、调试器支持、更好的错误消息。他们还发现 AI 编码助手在很大程度上帮助了 Rust 的学习曲线。

## 更大的图景

Russinovich 的演讲揭示了微软对 Rust 的押注范围。它不仅仅是将其用于新项目——它正在系统地替换其最关键系统中的 C++。Win32k.sys、Hyper-V、SymCrypt、Azure Data Explorer。这些不是实验；它们是处理大规模生产的系统。

驱动程序框架将此扩展到微软自己的代码之外。如果硬件供应商开始编写 Rust 驱动程序，Windows 将会变得更加安全，而无需微软完成所有工作。

结合 AI 翻译工具，这可能会产生一个引爆点。目前，Rust 的采用受到启动所需工作的限制。但是，如果你可以自动翻译现有代码并将 Rust 模块轻松集成到现有项目中，那么障碍就会开始消失。

这是否真正发生取决于执行情况。自动翻译需要在复杂的代码库上可靠地工作。构建集成需要无缝衔接。驱动程序开发的[安全](https://thenewstack.io/microsofts-rust-bet-from-blue-screens-to-safer-code/)抽象需要完整且有详细的文档。

但微软似乎致力于使其发挥作用。正如 Russinovich 所说：“Rust 正在渗透到我们的核心基础设施中。这将加速发展。”