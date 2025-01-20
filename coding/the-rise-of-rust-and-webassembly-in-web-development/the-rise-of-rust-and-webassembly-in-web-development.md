
<!--
title: Rust和WebAssembly在Web开发中的兴起
cover: https://cdn.thenewstack.io/media/2025/01/1f6026cd-getty-images-hqcjql0xgys-unsplashb.jpg
-->

Rust 由于 WebAssembly、新的 Rust IDE 和其他开发工具以及注重性能的用例而越来越受到 Web 开发人员的欢迎。

> 译自 [The Rise of Rust and WebAssembly in Web Development](https://thenewstack.io/the-rise-of-rust-and-webassembly-in-web-development/)，作者 Richard MacManus。

随着支持WebAssembly的[Rust开发者Web框架](https://thenewstack.io/want-a-web-framework-for-rust-not-javascript-try-leptos/)出现，值得关注的是Rust目前在Web开发中的使用频率、开发者使用的工具以及Rust和Wasm未来的适用场景。

在2024年[JetBrains开发者生态系统报告](https://www.jetbrains.com/lp/devecosystem-2024/)中，35%的Rust开发者表示他们已经使用Rust进行Web开发工作。这与系统编程（同样为35%）并列第二，仅次于CLI工具（44%）——这两个项目通常被认为适合Rust，因为它们也适合C++开发者（Rust最具威胁的编程语言）。

在JetBrains报告的其他地方，19%的Web开发者表示他们部署到WebAssembly，而部署到[Linux](https://thenewstack.io/introduction-to-linux-operating-system)的比例为77%，部署到Windows的比例为43%，部署到MacOS的比例为36%。因此，虽然Wasm在Web开发中的使用相当普遍，但仍有很大的增长空间。还值得一提的是，Rust拥有一些最好的编译到Wasm的工具链，例如：

- Wasm-bindgen：连接Rust和JavaScript。
- Wasm-pack：简化Rust的npm打包。
- Cargo-generate：[描述为](https://crates.io/crates/cargo-generate)“一个开发者工具，通过利用预先存在的git仓库作为模板，帮助你快速启动一个新的Rust项目。”

## Rust IDE

在[最新的Stack Overflow调查](https://survey.stackoverflow.co/2024/technology#most-popular-technologies-new-collab-tools-prof)中，所有专业开发者在过去12个月中最有可能使用的集成开发环境(IDE)是Visual Studio Code，74%的受访者使用过它。当查看过去12个月**使用过Rust**的专业开发者时，这个百分比保持不变（75%）。因此，VS Code显然是Rust开发者的顶级IDE。

也就是说，有一个IDE似乎在Rust开发者中特别受欢迎——因为它*没有*被其他开发者广泛使用。36%的专业Rust开发者表示他们使用[Neovim](https://neovim.io/)，而没有使用Rust的专业开发者仅为13%。这意味着Neovim是Rust开发者中第二受欢迎的IDE，仅次于VS Code。

有趣的是，Neovim的赞助商之一是Warp，一个基于Rust的终端，The New Stack的David Eastman[将其描述为](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)“你经常假设会拥有的命令行IDE，但你从未真正拥有过”。

在IDE方面，Rust开发者还有许多其他选择。JetBrains提供了一个[名为RustRover的专用Rust IDE](https://thenewstack.io/the-rust-community-matures-with-jetbrains-rustrover-ide/)，以及IntelliJ IDEA和CLion的Rust插件。其他流行的IDE也支持Rust；例如Emacs和[相对较新的Zed](https://thenewstack.io/zed-a-new-multiplayer-code-editor-from-the-creators-of-atom/)。

RustRover于2023年9月发布，JetBrains对Rust开发者的未来充满信心。去年二月，JetBrains开发者布道者[Vitaly Bragilevsky指出](https://mainmatter.com/blog/2024/02/29/launching-rustrover/)，Rust不仅仅被用作“内存不安全”语言（如C++和C）的替代品。

>……许多人从其他[编程语言]转向Rust。
> JetBrains开发者布道者 Vitaly Bragilevsky

他说：“我们实际看到的是，许多人从其他编程语言转向Rust，他们也带来了全新的想法来用Rust实现一些东西。”例如Web应用程序的想法。

在[之前接受The New Stack的采访](https://thenewstack.io/dedicated-ide-for-rust-released-by-jetbrains/)中，Bragilevsky表示许多开发者从JavaScript和Python社区转向Rust。“这些人可能对他们之前的编程语言有点不满，”他说。“也许他们的性能不够，而他们可以用Rust获得这种性能。有时他们缺乏安全性，而Rust肯定能提供这一点。”

至于Rust开发者在他们的IDE中想要什么，根据JetBrains开发者调查，12%的人表示他们想要更多Web框架支持。因此，这对现有的Rust IDE或新的开发工具产品来说是一个机会。

## 最适合Rust和Wasm的应用程序类型？

去年十一月，软件工程师[Trevor I. Lasn撰写](https://www.trevorlasn.com/blog/webassembly-when-and-when-not-to-use-it)的文章指出，“WebAssembly 擅长将成熟的 C/C++ 或 Rust 库引入 Web”。他以 PDF 生成为例。“与其用 JavaScript 重复发明复杂的字体渲染和布局算法，不如使用经过实战检验的 C++ 库，”他解释道。

> Rust 越来越被视为一种用于复杂数据处理的语言。

同样的原则也适用于 Rust 库——虽然这些库可能不如 C++ 库那样“经过实战检验”，但 Rust 越来越被视为一种用于复杂数据处理的语言。而且由于 Rust 可以高效地编译成 WebAssembly，这意味着可以直接在 Web 浏览器或边缘环境中进行高性能数据处理。

Rust 在 Web 开发中的其他用例包括实时数据可视化、图像和视频处理以及游戏引擎。

尽管如此，Rust 不会很快取代 JavaScript——Web 应用中的业务逻辑仍然最好由 JS 处理，并且 Wasm 的 DOM 操作能力有限。此外，如果不仔细操作，Wasm 可能会迅速使事情变得过于复杂。正如 Lasn 所观察到的那样，“如果你不是在进行大量的计算或使用其他语言的现有库，WebAssembly 可能会增加不必要的复杂性。”

无论如何，Web 开发正日益成为 Rust 开发人员的用例。因此，我们可以预期围绕 Rust 的开发工具生态系统将相应地发展。
