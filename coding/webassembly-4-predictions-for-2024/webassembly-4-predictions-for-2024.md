<!--
title: 2024年WebAssembly四大预测
cover: https://cdn.thenewstack.io/media/2023/12/78ab52a8-wasm-predictions-2024-1024x768.jpg
-->

Wasm的进展将帮助我们构建更好、更安全、更具可移植性的应用程序，充分享受真正共享函数的好处。

> 译自 [WebAssembly: 4 Predictions for 2024](https://thenewstack.io/webassembly-4-predictions-for-2024/)，作者 Matt Butcher 是Fermyon公司的联合创始人兼首席执行官，这是一家专注于在云端使用WebAssembly的公司。马特是Helm、Brigade、CNAB、OAM、Glide和Krustlet的原始创作者之一。他还撰写了许多书籍，包括《学习Helm》...

去年，我将2023年称为 [WebAssembly 之年](https://thenewstack.io/webassembly-5-predictions-for-2023/)。回顾过去，我可以说这个预测应验了。几个 WebAssembly（Wasm）标准取得了重大进展。多种编程语言都取得了巨大的进步。Python 和 Ruby 现在在它们的发布版中包含了 Wasm 支持，而官方的 Go 项目正在增加对 Wasm 和 WebAssembly 系统接口（WASI）的支持。

Spring I/O 的团队在巴塞罗那主办了第一届 [Wasm I/O 大会](https://wasmio.tech/)，几个月后 Linux Foundation 在西雅图主办了 [WasmCon](https://events.linuxfoundation.org/wasmcon/)。[GlueCon](https://www.sw2con.com/) 和 [DockerCon](https://www.dockercon.com/2023/home) 都设有 WebAssembly 的专题。[Suborbital 被 F5（NGINX 的制造商）收购](https://suborbital.dev/)，Adobe 试图收购 Figma（但被[监管机构阻挠](https://www.theverge.com/2023/12/18/24005996/adobe-figma-acquisition-abandoned-termination-fee)），显示出行业两家最注重 Wasm 的公司已经证明了市场价值。在整个年度内，分析报告和新闻文章对 WebAssembly 的成熟度和潜力的看法逐渐变得乐观。

展望 2024 年，我看到 WebAssembly 的未来有四个关键事件。

## 1. Wasm 是人工智能的完美搭档

在开发者工具领域的一个引人注目的现象是编程语言范式经常与基础设施的进步相结合。Java 伴随着上世纪90年代的 Web 而出现。Python 成为大数据语言，随着 NoSQL 风格的数据库的兴起。Go 语言随着容器生态系统的崛起而蓬勃发展。

这一趋势将在人工智能不断发展的过程中持续存在，但在这里技术的赢家将是 [WebAssembly](https://thenewstack.io/webassembly/what-is-webassembly/)。有三个原因使 Wasm 成为与人工智能工作负载的理想匹配。

- Wasm 的平台中立性，包括对 GPU 的支持，使其能够在各种硬件上实现可移植性。开发者可以在本地使用速度较慢（但便宜）的 CPU 或 GPU 推理构建 AI 应用，然后部署到具有大规模（且昂贵）AI 级 GPU 的云系统。而开发者无需一次次地询问：“部署环境的 GPU 架构是什么？”
- Wasm 的快速启动时间意味着可以按需进行 AI 推理，而无需等待虚拟机或容器上线。这反过来意味着在昂贵的 GPU 资源上通过提高效率来节省金钱。
- Wasm 的可移植性和小型二进制大小意味着应用程序可以尽可能地靠近数据和 GPU。

2024 年 AI 的一个重要主题之一将是效率。我们如何减少时间？如何降低成本？如何在相同的硬件上运行更多的应用程序？Wasm 是提高效率的利器。

## 2. 三个重要的标准已完成

Wasm 是在万维网联盟（W3C）的支持下进行标准化的。核心 Wasm 标准在多年前就已经完成。但有三个附加标准对 Wasm 的成功至关重要：

- WASI
- 内存管理
- 组件模型

这三个标准都已经在过去的几年中处于进行中的状态。在 2023 年，这三个标准都经历了重大的增强和进展。

WASI 将在 2024 年初进入第 2 预览。这个阶段引入了网络支持，这是最后一个重要功能。鉴于标准和参考实现的加快步伐，我相信 WASI 将在 2024 年底之前达到 1.0 版本。

在Wasm的内存管理扩展中，允许使用者语言将内存管理委托给主机运行时。虽然这是Wasm工作的低级细节，但一旦实施了这一规范，像Kotlin、Java和.NET这样的语言就不需要实现自己的内存管理器。这加速了将Wasm支持添加到最重要和广泛使用的语言中。

最后，[Wasm组件模型](https://thenewstack.io/can-webassembly-get-its-act-together-for-a-component-model/)释放了Wasm的真正潜力。有了组件模型，一个Wasm二进制文件可以将另一个视为库。而且，库的源语言并不重要。这意味着在计算机科学历史上，任意语言的库可以首次共同工作。你的Rust应用可以导入一个Python库，而这个Python库又可以使用Go语言编写的内容。这将改变开发者处理依赖和库的方式。组件模型已经有一些实现，但规范将在2024年完成并投入生产。

## 3. Wasm的根基在服务器端

Wasm最初是为在浏览器中执行而编写的。但是现在，Wasm的势头似乎更多地集中在服务器端。Fermyon公司的首席技术官[Radu Matei](https://github.com/radu-matei)最近表示，在参加WebAssembly会议时，“每个人都在谈论云和服务器。在客户端Wasm上，我几乎找不到一次讨论。”

在浏览器中使用WebAssembly的情况不会消失。像Figma和Adobe这样的公司已经展示了它在高性能浏览器计算中的价值。但我认为，WebAssembly的主要用例将是[在云端](https://thenewstack.io/where-does-webassembly-fit-in-the-cloud-native-world/)。在2023年，我预测无服务器函数将成为一个甜蜜点，根据我们在Fermyon的证据（10万次[Spin](https://thenewstack.io/webassembly-providers-speed-ahead-to-fill-serverless-gaps/)下载和成千上万的应用程序部署到Fermyon Cloud），它确实开始起飞。但云端不仅仅涉及编程模型。

我预计WebAssembly将在Kubernetes生态系统中取得重大进展，并开始在关注效率、可伸缩性和成本的重要场景中出现。从边缘到数据中心，WebAssembly的归宿将是服务器端。

## 4. 渐进增强意味着WebAssembly双向发展

关于服务器端的故事有一个值得特别提及的细微差别。在过去的几年里，我们看到了可以（可选地）在客户端、服务器端或两者之间执行的Web开发框架的兴起。

在这样的应用程序中，开发者编写一个包含所有逻辑的代码库。但在构建时，应用程序可能会被构建为完全在客户端上运行，或者有一些逻辑在服务器端执行。客户端渲染（CSR）和服务器端渲染（SSR）描述了这些情况。

在这新兴的框架类别中，有些已经开始利用WebAssembly。[Leptos框架](https://leptos.dev/)允许开发者用Rust编写Web应用程序，然后将它们编译为CSR或SSR版本。CSR版本已经使用了WebAssembly。Fermyon最近与Leptos合作尝试了一些有趣的事情：我们能否在客户端和服务器两侧运行WebAssembly？答案是[完全肯定的](https://www.fermyon.com/blog/leptos-spin-get-started)。

未来，我们是否能够用[Python](https://thenewstack.io/python-and-webassembly-elevating-performance-for-web-apps/)、Go、Rust或其他语言编写我们的Web应用程序，并使它们在这种双重CSR/SSR模式下执行？前景是不错的。在2024年，我认为我们将看到更多的项目会做到这一点。这是通向WebAssembly真正优势的第一步：作为一种二进制格式，它已经能够在几乎任何地方运行，但像这样的工具将使智能地定位二进制文件在运行它们最有意义的地方成为可能。可能是在云端、浏览器端或边缘端，但理想情况下决策将自动完成。开发者不必再多想。

## 2024年是WebAssembly投入生产的一年

如果说2023年是WebAssembly爆发的一年，那么2024年将是WebAssembly投入生产的一年。AI应用将利用Wasm的可移植性和GPU无关性。组件模型将使我们能够共享库，而不受原始语言的限制。已完成的规范意味着坚实的实现。我们将看到一类新兴的Web应用程序，可以在客户端或服务器端运行。

在我的职业生涯中，我多次因为在合适的时间出现在合适的地方而受益。我经历了Web应用程序的兴起、内容管理系统的发展、公共云的开端以及容器生态系统的崛起。然而，没有一个像WebAssembly（Wasm）一样让我如此激动。与它一起出现的技术组合意味着我们将构建更好、更安全、更可移植的应用程序，并且（感谢组件模型）能够真正共享功能。Wasm有潜力改变应用程序开发和平台运营的方式。

而我们在2024年将有最前排的座位观看这一切发生。
