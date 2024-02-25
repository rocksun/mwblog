<!--
title: 浏览器中的WebAssembly日趋成熟并涌现出许多很酷的事情
cover: https://cdn.thenewstack.io/media/2024/02/46b45335-collin-sr0_mna77mu-unsplash-1-1024x683.jpg
-->

期待已久的组件模型将使得 WebAssembly 不再局限于网络浏览器和服务器之中，而能够让用户在众多轻量级模块内运行各种不同的应用程序。

> 译自 [WebAssembly in the Browser Matures and Cool Things Happen](https://thenewstack.io/webassembly-in-the-browser-matures-and-cool-things-happen/)，作者 B. Cameron Gain 是 ReveCom Media 的创始人和首席分析师。他对计算机的痴迷始于 20 世纪 80 年代初在当地游戏厅里用 25 美分玩了一整天太空侵略者控制台的经历。

[WebAssembly](https://thenewstack.io/webassembly/) 正在经历其在浏览器中的使用和应用加速。然而，这并不意味着服务器部署和所谓的组件模型不能充分发挥其在 WebAssembly 中的潜力。

事实上，一些有前途的发展正在出现，无论是在组件模型方面，通过建立 [WASI 2](https://thenewstack.io/wasi-preview-2-what-webassembly-can-and-cant-do-yet/) 预览，还是在服务器空间中，通过 [Fermyon](https://www.fermyon.com/?utm_content=inline-mention) 提供的引人入胜的无服务器开发应用，这些应用是基于 WebAssembly 构建的。

一旦最终确定，这种组件模型将使得 WebAssembly 不仅能够在 [Web 浏览器](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/)和服务器之外看到其不断扩展的使用，而且能够允许用户通过组件接口在成千上万的端点同时运行各种不同的应用程序，而无需改变一行代码。

与此同时，在 WebAssembly 浏览器空间中出现了明显的雪球效应。其中许多发展虽然是零星的，但却非常有趣。

在本文中，我们将探讨一些我们在 WebAssembly 浏览器中遇到的有趣项目，并描述它们。然后我们深入探讨了 WebAssembly 实现其全面潜力所需的步骤。其中很大一部分与开源社区有关。

## CheerpJ 3.0

最近推出的 [CheerpJ 3.0](https://cheerpj.com/) 展示了 WebAssembly 在浏览器中的一个有趣体现，展示了其部署和运行用 [Java](https://thenewstack.io/microsoft-goes-deep-on-java-with-jcp-membership/) 编写的复杂应用程序和运行时的潜力。开发人员可以用任何语言创建应用程序，并通过一键打包和分发，供最终用户测试和使用。

虽然 CheerpJ 3.0 的开发仍在进行中，但它代表了在浏览器中使用 WebAssembly 部署应用程序的重大进步，尤其是在使用 Java 方面。这与其他专注于加密和部署用 C++ 编写的应用程序供浏览器使用的项目相辅相成。

根据 Fermyon 的说法，CheerpJ 3.0 — 标志着其普遍可用的发布 — Java 客户端应用程序，如 Java Applets、Java Web Start 应用程序和独立的 Java 应用程序，可以在现代浏览器上无需本地 Java 安装运行，而保持不变。其理念是使运行时 — 在本例中是 Java — 能够更好地运行，就像用户拥有终端服务器资源一样 — 在浏览器中。

“就像 [Docker](https://www.docker.com/?utm_content=inline-mention) 允许您在您的计算机上运行二进制容器一样，您需要能够拥有技术，并且它有技术可以让您在浏览器中以与在常规平台操作系统上正常运行时相同的方式运行二进制工作负载。” 创建了 CheerpJ 的 [Leaning Technologies](https://leaningtech.com/) 的 CEO 兼创始人 [Stefano Marco Maria De Rossi](https://uk.linkedin.com/in/sderossi) 告诉 The New Stack。

设置 CheerpJ 3.0 相当简单，文档中清晰概述了设置步骤，并且与几乎所有浏览器兼容。在游乐场方面，合并 PDF 文件非常简单：用户将他们的 PDF 文件输入到 API 中，然后点击几下，文件就会被合并。

然而，这种简单性类似于一个 [Hello World 应用程序](https://thenewstack.io/typescript-tutorial-go-beyond-hello-world/)，只代表了一个开始。对于更复杂的应用程序，可以使用 Java 编写并实现到 CheerpJ 3.0 的 WebAssembly 模块中，以便在浏览器间分发和执行。这些示例展示了 WebAssembly 在基于浏览器的应用程序中的多功能性和潜力。

## Falco 的浏览器运行

[Sysdig](https://sysdig.com/) 容器安全提供商的高级开源工程师、[Falco](https://thenewstack.io/falco-plugins-bring-new-data-sources-to-real-time-security/) 核心维护者 [Jason Dellaluce](https://it.linkedin.com/in/jasondellaluce) 在他在 [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 北美的演讲中提到。在他的演讲“[Falco 游乐场：WebAssembly 和运行时安全的鸡尾酒](https://www.youtube.com/watch?v=imvDmhLRFRo)”中，他解释了这个安全平台如何密集地集成 eBPF，需要“填补一个历史性的空白”。这个空白源于 Falco 负责验证规则集并提供指示“如果有什么问题”，然后配置这些规则集以匹配运行时的安全事件，测试“一切是否按预期运行”，Dellaluce 说道。

他认为 Falco 需要一个后端服务器来运行 Falco，然后需要一个 Web 平台供我们的用户在沙盒环境中使用 Falco 进行实验。“这是一个解决方案，但也因为我们需要在我们的开放基础设施中使用服务器而开发、维护和部署代价高昂…… 然后我想到了：WebAssembly 让你能够将大多数语言编写的程序编译成在浏览器客户端本地运行的东西。”

然后，[Falco 游乐场](https://github.com/falcosecurity/falco-playground)就为他的 Google Summer of Code 项目而创建了。“这是我们刚刚启动的新平台，让人们可以玩耍并了解 Falco 规则和测试，” Dellaluce 说道。“这完全是客户端操作，无需任何后端，这要归功于 WebAssembly 的强大力量。”

而且它在浏览器中运行。

在 KubeCon + CloudNativeCon 的演讲[“使用 Container2wasm 转换器在 Wasm 和浏览器上运行基于 Linux 的容器”](https://www.youtube.com/watch?v=AQ_tg_78jqA)中，[Kohei Tokunaga](https://twitter.com/tokunagakohei?lang=fr), 日本 NTT 的软件工程师、BuildKit 的维护者和 [CNCF](https://cncf.io/?utm_content=inline-mention) [Containerd](https://thenewstack.io/how-to-deploy-kubernetes-with-kubeadm-and-containerd/) 的审阅者德长公平描述了如何使用 Container2wasm 转换器在 Wasm 和浏览器上运行 Linux-based 应用程序，而无需修改应用程序应用。正如他所描述的，将应用程序迁移到 Wasm 需要重新编译和重新实现，耗费了时间。

[Container2wasm](https://medium.com/nttlabs/container2wasm-2dd90a18cc9a) 转换器允许在 Wasm 上运行修改后的容器，同时利用 CPU 模拟器。他的团队还为 [VS Code](https://thenewstack.io/this-week-in-programming-all-hail-visual-studio-code/) 创建了一个扩展，以便在浏览器中运行容器。他描述了进一步的项目计划，包括开发性能分析和其他 Container2wasm 的改进。

## Adobe Touch

再次，Wasm 在多种方式中持续发挥作用，利用其针对性的二进制结构。其中包括它在 CPU 层面的功能以及消除容器镜像中易受攻击代码的许多风险，以及其他宣传的优势。在 Adobe 的情况下，资源密集型应用程序 Photoshop 在 PC 上运行时现在[也可以在浏览器中使用](https://www.youtube.com/watch?v=CF5zZZy0R9U&ab_channel=ChromeforDevelopers)。用户可以访问 Photoshop 的命令和功能，而无需下载软件（同样，这要归功于 Wasm）。

Photoshop 可以在浏览器上运行的原因主要是由于 Adobe 使用了开源的 [emscripten](https://emscripten.org/index.html)。Emscripten 是用于为 C 或 C++ 的 Wasm 模块编译的编译器工具链。这意味着您可以使用 emscripten 将用 C 或 C++ 或其他使用 [LLVM](https://thenewstack.io/rust-support-is-being-built-into-the-gnu-gcc-compiler/) 的语言编写的代码编译为 WebAssembly，不仅可以在浏览器上运行，还可以在 Node.js 或其他 WebAssembly 运行时中运行。

## 浏览器中的 Wasm 未来

未来，开发人员特别需要更成熟和稳定的工具，De Rossi 表示。特别是在过去的两年中，Java 的最大投资是关于可用性和开发人员体验，De Rossi 说道。“实际上，其中最大的动机之一是完全重新架构。好吧，这样对于标准 Java 开发人员来说使用起来就非常简单了，这是我们的动机，”De Rossi 说道。“所以我认为，如果你想让这些工具在大规模上真正成功解决这个问题，这非常重要。”

普通软件使用大量的第三方依赖项，其中用户或开发人员没有源代码，而许多企业软件开发人员将使用专有库，De Rossi 表示。“如何使浏览器在这些类型的应用程序中更明智地使用，这些应用程序占据了 99%？专有组件——你如何处理？你如何解决这个问题？”De Rossi 说。“解决方案是[虚拟化](https://thenewstack.io/the-next-evolution-of-virtualization-infrastructure/)——能够在浏览器上运行二进制内容，能够运行 x86 或 [Arm](https://www.arm.com/campaigns/multi-arch-cloud-infrastructure?utm_content=inline-mention) 的二进制内容。这是你需要做的，否则，你将永远无法运行具有专有组件的软件，而且你将始终受到自己的源代码或开源组件的限制。”
