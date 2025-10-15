<!--
title: Wasm 3.0：无组件模型，难迎“Docker时刻”
cover: https://cdn.thenewstack.io/media/2025/10/56fea580-brett-jordan-xp9wozf92jw-unsplash.jpg
summary: Wasm 3.0 功能强大，但WebAssembly的“Docker时刻”因组件模型未完成而延迟。其采用仍在继续，WASI 0.3发布将是关键。
-->

Wasm 3.0 功能强大，但WebAssembly的“Docker时刻”因组件模型未完成而延迟。其采用仍在继续，WASI 0.3发布将是关键。

> 译自：[Wasm 3.0: No Component Model and No 'Docker Moment'](https://thenewstack.io/wasm-3-0-no-component-model-and-no-docker-moment/)
> 
> 作者：B. Cameron Gain

姑且可以认为 [Wasm 3.0](https://thenewstack.io/wasm-3-0-offers-new-way-to-handle-javascript-strings/) 是一个重要的版本。然而，其组件模型尚未完成。可以说，[WebAssembly](https://thenewstack.io/webassembly/) 期待已久的“如同 [Docker](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) 时刻”尚未到来。

我所说的 WebAssembly 的“Docker 时刻”是指 [Solomon Hykes](https://www.linkedin.com/in/solomonhykes) 那条著名的推文，他大致意思是，如果 WASM+WASI 在 2008 年就已经存在、定稿并可正常运行，那么从一开始就不需要 Docker。

所以，WebAssembly 最初的宏伟承诺仍在进行中。“Docker 时刻”——以及我的这个概念如何转化为实际使用——取决于组件模型。而组件模型尚未完成，并有赖于 Wasi 0.3 的发布（下文会详细说明）。

我还认为，它的迟到并不像表面看起来那么严重。也就是说，在过去一年左右的时间里，服务器端出现了一些非常有趣的发展。

“Wasm 的美妙之处在于它已被业界广泛采用。Wasm 3.0 的功能集将改善每个人的体验，而不仅仅是针对浏览器的人，”Bitnami 前联合创始人兼基于 Wasm 的开发工具提供商 Endor 首席执行官 [Daniel Lopez Ridruejo](https://www.linkedin.com/in/ridruejo/) 告诉我。“我认为组件模型规范是对通用 Wasm 规范的补充和构建，它正在稳步推进，即使时间比许多人预期的要长。”

## 更少垃圾

Wasm 3.0 的突出功能——其中一些已开发长达八年，包括（根据文档内容）：

**64 位地址空间：** 内存和表现在可以声明使用 i64 作为其地址类型，而不仅仅是 i32。理论上，这种扩展将 Wasm 应用程序的地址空间从 4 千兆字节扩展到（同样是理论上）16 艾字节。为在浏览器中运行而设计的 Wasm 应用程序——Wasm 最初就是为此而创建的——意味着 64 位内存受限于 16 千兆字节，尽管在服务器端可能跃升到 16 艾字节的潜力尤其巨大。

**多重内存：** 文档指出，并且“与普遍看法相反”，Wasm 一直能够同时使用多个内存对象——因此也有多个地址空间。但在 Wasm 3.0 发布之前，每个内存空间都必须在单独的模块中声明和访问。Wasm 开发者表示，这一点特别有趣，并支持“一次部署，随处运行”，因为现在单个模块可以声明（定义或导入）多个内存并直接访问它们，包括直接在它们之间复制数据。

**[垃圾回收](https://thenewstack.io/time-to-get-the-garbage-out-of-webassembly/)：** 除了进一步支持通过 Wasm 模块分发的代码和应用程序的轻量级和低延迟特性外，Wasm GC 变得更具适应性，灵活性也更高，因为它由编译器来配置源代码值的“工程适用表示”，包括方法表等实现细节。没有内置的对象系统，也没有闭包或其他高级构造，这些都会不可避免地偏向于特定语言。相反，Wasm 仅提供表示此类构造的基本构建块，并纯粹专注于内存管理方面，其开发者表示。

可以说，Wasm（或 WebAssembly）在许多方面都得到了广泛使用，我敢说许多用户甚至没有意识到这一点。无论是使用 Azure 上的 [Hyperlight](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/)、[Spin](https://www.fermyon.com/blog/introducing-spin-v3) 还是 [wasmCloud](https://wasmcloud.com/) 等服务，这些平台都在实现 WebAssembly 的有用功能以及上述新功能。

再说一次，组件模型尚未完成，但许多类似组件的功能已经以各种方式嵌入、提供和解决，用户可以通过 [StackBlitz](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)、endor.dev 等服务加以利用。

在 Endor 的案例中，WebAssembly 功能增添了许多乐趣和实用性。开发者可以在几秒钟而不是几小时或几天内创建可复现的、隔离的测试环境，这得益于 WebAssembly 闪电般的速度。Endor 的开发者表示，开发者还可以运行代理和氛围编程，从而快速安全地测试代码。Endor 提供了一种在浏览器和命令行中执行此操作的方法。

就我而言，在访问 Endor 服务器并安装 shell 后，我仅用了几分钟就获得了第一个“星球大战”的一个非常极客的版本。

## 组件传闻

Wasm 3.0 不包括组件模型的最终定稿。虽然 Endor 已经接近，但那种神奇的、类似 Docker 的时刻——你可以将几乎任何应用程序放入 Wasm 模块中，并将其部署到任何你想要的地方，或者发送到任何你想要的地方，并且可以在任何你想要的地方使用——仍然在开发中。

标准化将意味着可以用任何语言编写应用程序，并通过 Wasm 模块同时（且异步地）分发到任何端点进行部署。一旦最终定稿，组件模型将使 WebAssembly 的用途扩展到网页浏览器和服务器之外。它将允许用户以非常高的速度同时将运行在众多轻量级模块内的不同应用程序部署到数千个端点。

很大程度上取决于组件模型的最终确定，尤其是它与 WASI 的关系，WASI 是连接 WebAssembly 模块和组件的标准接口或 API。它将支持开发所谓的 WebAssembly “世界”，因为兼容的 Wasm 组件群将形成一个类似于 [Kubernetes](https://thenewstack.io/kubernetes/) 的互联基础设施，但没有容器。2024 年发布的 WASI Preview 2 在标准化方面取得了巨大进展，但我们尚未达到目标。2025 年，我们可能无法实现圣杯，但我们可能会看到一些惊喜。有传言称 Wasi 0.3 可能不会在今年最终定稿，这可能会推迟 Wasi 1.0 的发布，从而推迟一个可用的组件模型。

再说一次，WebAssembly 在全球基础设施工作结构中的采用仍在继续，并且不以 Wasi 3.0 的发布为前提。

“组件部分严格归属于 WASI，所以他们没有将其纳入主标准，”[Fermyon](https://www.fermyon.com/?utm_content=inline+mention) 联合创始人兼首席执行官 [Matt Butcher](https://www.linkedin.com/in/mattbutcher/) 告诉我。“因此我同意：我们还没有达到那个关键的 Docker 时刻。但我们正在接近。”