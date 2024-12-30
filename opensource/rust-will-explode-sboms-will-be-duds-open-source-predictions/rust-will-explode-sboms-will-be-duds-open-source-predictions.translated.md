# Rust 将爆发，SBOM 将成为废物：开源预测

![Featued image for: Rust 将爆发，SBOM 将成为废物：开源预测](https://cdn.thenewstack.io/media/2024/12/c482b595-opensource-1024x568.png)

这对[开源软件](https://thenewstack.io/open-source/)来说是非凡的一年。从编程工具的突破性进步到关于[许可](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/)和[标准](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/)未来的[激烈辩论](https://thenewstack.io/the-case-against-osis-open-source-ai-definition/)，开源生态系统正以前所未有的速度发展。

随着2025年的临近，现在是反思我们过去所走过的道路以及未来方向的理想时机。以下是我对来年的一些想法、预测和看法，涵盖了我最看好的方面以及我预见到的停滞或挫折。

**Rust 在内核中的决定性一年**

[Rust 融入 Linux 内核](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/) 已经酝酿已久。早在 2021 年 4 月，我在 Google 工作期间，[与 ISRG 合作](https://www.memorysafety.org/blog/supporting-miguel-ojeda-rust-in-linux/)，通过为[Miguel Ojeda](https://ojeda.dev/) 提供一份合同，让他全职从事该项目和其他[内存安全工作](https://thenewstack.io/can-the-safe-c-proposal-copy-rusts-memory-safety/)，从而正式支持[Rust for Linux](https://thenewstack.io/rust-in-the-linux-kernel/)。
我坚信[资助](https://x.com/lorenc_dan/status/1775368864374637042)这类工作是不够的；你需要像 Ojeda 这样经验丰富的工程师的全职投入才能取得成功。这项投资得到了回报：2024 年是[Rust](https://thenewstack.io/rust-programming-language/) 在内核中最终走向主流的一年。驱动程序现在正在[用 Rust 编写](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/)，其势头不可阻挡。

展望未来，2025 年可能会看到 Rust 在内核开发中的应用爆炸式增长。Rust 关注内存安全、性能及其现代编程模型，使其成为新一代内核程序员的理想选择。

仅[内存安全](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/)一项就能防止无数漏洞，这是低级系统编程中一个长期存在的问题。Linux 社区已经开始接受 Rust 的潜力，Google 也正在[尝试在关键项目中使用 Rust](https://www.securityweek.com/google-pushes-rust-in-legacy-firmware-to-tackle-memory-safety-flaws/)，因此随着他们认识到将 Rust 集成到其软件堆栈中的好处，我们应该期待更多组织效仿。

**jj 和 uv：两个值得关注的双字母工具**

我对 2025 年感到兴奋的两个新兴工具是 jj 和 uv。两者都有望重新定义各自的领域。

[Jujutsu (jj)](https://jj-vcs.github.io/jj/latest/) 是一种新的版本控制系统，它巧妙地平衡了与 git 的兼容性，同时引入了更直观的思维模型来处理分支、更改和差异。我一直是 git 的支持者，它的主导地位对社区来说非常棒，但其陡峭的学习曲线和深奥的概念，如有向无环图 (DAG) 和 Merkle 树，可能会让许多开发者望而却步。
Jujutsu 以更简单、更用户友好的方式重新构想版本控制。习惯使用 git 的开发者会欣赏 jj 的互操作性，而新手会发现它更容易学习和使用。到 2025 年底，我预测 jj 由于其对那些对 git 的复杂性感到沮丧的团队的吸引力，可能会占据 git 使用率的两位数份额。

[统一的 Python 包管理 (uv)](https://docs.astral.sh/uv/) 统一了所有现有[Python](https://thenewstack.io/python/) 工具的最佳部分。Python 开发人员长期以来一直苦于支离破碎的包管理器、虚拟环境和依赖项工具生态系统。uv 将这些不同的解决方案统一到一个单一的、连贯的体验中，可以无缝地管理虚拟环境、包依赖项、工具甚至 Python 版本。
仅仅在第一年，uv 就已经在开发者中获得了显著的吸引力，为 pip、venv 和 pyenv 等工具提供了一个急需的现代替代品。我敢打赌，uv 将在 2025 年实现 40% 的采用率，从而改变 Python 项目的管理方式，并为更流畅的工作流程铺平道路。

**SBOM、公平源和 Wasm：不会发生**

虽然我对开源的许多方面都持乐观态度，但我认为明年有一些趋势不会获得发展。
软件物料清单 (SBOM) 将继续处于监管困境。SBOM 持续成为网络安全政策中的热门话题，但其实际影响仍然有限。尽管监管措施不断推进，SBOM 往往感觉像是走过场的合规练习，对实际漏洞管理几乎没有增值作用。除非美国政府和其他利益相关者将重点转向更有影响力的举措，否则 SBOM 在 2025 年不太可能获得任何显著的采用。

公平源许可模式将无法在开源社区获得成功。公平源许可模式对商业用途施加限制，可能会在转向传统开源的企业中获得关注。但是，它不太可能促进有意义的社区参与或大型项目的采用。公平源与开源的理念根本不符，我认为它在 2025 年不会获得显著的势头。

服务器端 Wasm 设计过度且炒作过度。虽然 WebAssembly (Wasm) 在基于浏览器的和插件用例中显示出前景，但其在服务器端的采用仍然缺乏生气。对 WASI 组件模型的反对以及 Bytecode Alliance 内部的治理问题阻碍了进展。容器和无服务器平台仍然是大多数开发人员的首选，我认为服务器端 Wasm 在 2025 年不会达到临界规模。

开源的韧性
今年还会发生什么？当我们经历另一起类似 xz utils 的安全事件时，没有人应该感到惊讶。在广泛使用的实用程序（如 xz utils）中发现漏洞，提醒我们开源固有的风险。不幸的是，随着开源项目的攻击面不断扩大，类似事件几乎不可避免。这就是为什么今年，公司将继续投资于软件供应链安全。

我们一次又一次地看到开源生态系统具有韧性。面对攻击，尽管关于可持续性的争论仍在继续，但开源并没有消失。虽然持不同意见者总是会对公司利用免费软件获利表示担忧，但 2025 年将成为开源的又一个充满活力的年份。

Rust、`jj` 和 `uv` 的兴起突显了社区持续的创新，而对 SBOM、公平源和服务器端 Wasm 的预期有所降低，这提醒我们并非所有趋势都能成功。

有一点是肯定的：开源将继续成为技术发展的驱动力，在未来数年塑造软件开发的未来。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。