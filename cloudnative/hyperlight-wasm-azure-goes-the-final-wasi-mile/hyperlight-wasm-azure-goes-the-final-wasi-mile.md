
<!--
title: Hyperlight Wasm：Azure在Wasi之路上更进一步
cover: https://cdn.thenewstack.io/media/2025/04/1fdb20b5-benoit-deschasaux-9hpzjldfsk4-unsplash-1.jpg
summary: Azure推出Hyperlight Wasm，拥抱云原生！基于虚拟机监控程序的安全机制，实现WebAssembly模块在Azure虚拟机上的高速部署。支持C、Go、Rust、Python、JavaScript、C#等语言，绕过容器，直达虚拟机。结合WASI，性能卓越，冷启动毫秒级！CNCF已接管，云原生未来可期！
-->

Azure推出Hyperlight Wasm，拥抱云原生！基于虚拟机监控程序的安全机制，实现WebAssembly模块在Azure虚拟机上的高速部署。支持C、Go、Rust、Python、JavaScript、C#等语言，绕过容器，直达虚拟机。结合WASI，性能卓越，冷启动毫秒级！CNCF已接管，云原生未来可期！

> 译自：[Hyperlight Wasm: Azure Goes the Final Wasi Mile](https://thenewstack.io/hyperlight-wasm-azure-goes-the-final-wasi-mile/)
> 
> 作者：B Cameron Gain

伦敦 — 微软 Azure Core Upstream 团队的 [Hyperlight](https://opensource.microsoft.com/blog/2024/11/07/introducing-hyperlight-virtual-machine-based-security-for-functions-at-scale/) 现在包含 Hyperlight Wasm，这标志着在扩展和部署 [WebAssembly](https://thenewstack.io/webassembly/) 模块和组件到 Azure 的 [虚拟机](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/) 上取得了期待已久的进展。

微软还将该项目捐赠给了 [CNCF](https://cncf.io/?utm_content=inline+mention)。

[Hyperlight 项目](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/) 依赖于小型嵌入式函数，这些函数使用基于虚拟机监控程序的保护来大规模保护每个函数调用。每个函数请求也有自己的 [虚拟机监控程序](https://thenewstack.io/4-reasons-devops-engineers-still-rely-on-hypervisors/) 进行保护。

这种兼容性功能已经酝酿多年，实现了 WebAssembly 及其 [polyglot](https://thenewstack.io/webassembly-gets-polyglot-development-boost-in-spin-3-0/) 语言功能的长期承诺。

![](https://cdn.thenewstack.io/media/2025/04/6e86015c-screenshot-2025-04-03-at-12.06.16%E2%80%AFpm.png)

*来源：Microsoft*

有了它，工作负载可以在 Azure 上或任何其他云或本地环境中的虚拟机上以毫秒为单位进行部署、启动和关闭，而无需容器。是的，没错——绕过了对操作系统兼容性的任何担忧，或者将代码部署到虚拟机上的其他问题。这在很大程度上归功于 [WebAssembly System Interface](https://github.com/WebAssembly/wasi) (WASI) 的开发，它提供了与不同端点的互操作性，在 Hyperlight 的例子中，这些端点由虚拟机组成。

由于 WebAssembly 是管道，因此它不再仅限于其他机器语言，例如 [Rust](https://thenewstack.io/rust-programming-language-guide/) 和 C，尽管它也可以处理这些语言。到目前为止，Hyperlight 提供了与以下语言的兼容性，用户可以使用这些语言在 Hyperlight Wasm 中执行工作负载：C、[Go](https://thenewstack.io/introduction-to-go-programming-language/)、Rust、[Python](https://thenewstack.io/python/)、[JavaScript](https://thenewstack.io/javascript/) 和 C#。这里的诀窍与 [容器](https://thenewstack.io/containers/) 非常相似，是将语言运行时也包含在镜像中。

> [@Microsoft]´s Danilo (Dan) Chiarlone and Mikhail Krinkin showed Wasm working on Hyperlight and both with Envoy at[@rejektsio]during their talk
Envoy, and Hyperlight Walk Into a Pod: No Vulnerabilities Allowed.[@thenewstack][pic.twitter.com/GeEiM0enj1]— BC Gain (@bcamerongain)
>
> [March 31, 2025]

与容器化环境（工作负载必须首先在容器内进行打包、分发和收集）不同，Hyperlight Wasm 允许工作负载直接从操作系统分发到虚拟机。这消除了容器化的额外开销，因此提供了与使用 Wasm 发送轻量级工作负载相关的额外轻量级优势。

安全性是 WebAssembly 的一个重要方面，尤其是在此实现中。代码在隔离的环境中运行，并且运行时中嵌入了用 Rust 编写的模块，以解决数字漏洞。微软声称他们已采取广泛措施来增强这方面的安全性。

微软高级开发者倡导者 [Yosh Wuyts](https://www.linkedin.com/in/yoshuawuyts/?originalSubdomain=dk) 和软件工程师兼研究员 [Lucy Menon](https://popl25.sigplan.org/profile/lucymenon) 在一篇博客文章中写道，使用 WebAssembly 运行时构建 Hyperlight 使编程语言能够在受保护的 Hyperlight 微型虚拟机中执行，“而无需事先了解 Hyperlight”。

Wuyts 和 Menon 写道，开发人员可以使用 Hyperlight Wasm 为 wasm32-wasip2 目标进行编译，以便他们可以使用 wasmtime 或 Jco 等运行时在本地运行他们的程序，或者使用 Nginx Unit、Spin WasmCloud（或现在的 Hyperlight Wasm）在服务器上运行它们。“如果做得对，开发人员在开发代码时无需考虑他们的代码将在哪个运行时上运行，”Wuyts 和 Menon 写道。“这是只有通过标准才能实现的开发人员灵活性。”

正如 Wuyts 和 Menon 所描述的那样，当 Hyperlight VMM（虚拟机管理器）创建一个新的虚拟机时，它会创建一个新的内存切片并加载虚拟机访客，而虚拟机访客又会加载 wasm 工作负载，Wuyts 和 Menon 写道。“目前这需要大约 1-2 毫秒，并且正在努力将这个数字在未来降到 1 毫秒以下，”Wuyts 和 Menon 写道。

## 实践
在伦敦举行的 [Rejekts](https://cloud-native.rejekts.io/) 大会上，介绍了 Hyperlight 如何与 Wasm 和 Envoy 协同工作，并进行了演示。本次演示在 Microsoft 工程师 Mikhail Krinkin 和 Danilo (Dan) Chiarlone 的演讲“Wasm, Envoy, and Hyperlight Walk Into a Pod: No Vulnerabilities Allowed”中进行。

本次演讲涵盖了云安全，特别是运行应用程序的隔离方法。Chiarlone 讨论了三个隔离级别：无隔离、弱隔离（使用内核特性）和强隔离（使用 KVM 或 Microsoft Hyper-V 等虚拟机监控程序）。他们描述并展示了如何使用 Hyperlight 库来利用有限的虚拟机监控程序技术来创建微虚拟化环境。正如他们所描述的，Hyperlight 支持安全地运行不受信任的代码，包括 WebAssembly。

Chiarlone 展示了 Hyperlight Wasm 如何运行虚拟机，进入虚拟机，执行访客代码（遵循函数调用），然后让虚拟机退出并恢复执行。Chiarlone 展示的过程涉及 Hyperlight 沙箱在虚拟机监控程序内部的嵌套沙箱（两层隔离），执行代码并输出结果。

Krinkin 演示了将 Hyperlight 与服务网格 Envoy 集成，以沙箱化自定义插件。该示例涉及为处理 TCP 连接的 WebAssembly 模块创建沙箱，强调了配置约束以防止不受信任的代码逃脱沙箱的重要性。

您将准备好利用 Hyperlight 构建具有强大且可扩展的生产解决方案，并具有可靠的深度防御策略。

## 性能基准

提供了性能基准。正如 Chiarlone 和 Krinkin 所展示的，虚拟机中代码冷启动时间的延迟规格以毫秒为单位。当编译为 WebAssembly 代码的应用程序在浏览器以及无服务器或边缘环境中运行时，极快的执行速度也是显而易见的——在浏览器中也是如此，用户访问 http: 地址，应用程序几乎立即运行，因为不涉及下载或其他可能降低性能的初步操作。

由于 WebAssembly 不特定于特定架构（例如 x86 或 ARM），而是抽象了这些架构，因此充当硬件抽象层，Chiarlone 说道。如上所述，WebAssembly 在沙箱环境中执行，应用程序必须显式选择加入特定功能。

在演示中，Chiarlone 说有一些功能使用 Hyperlight 编译为 Wasm。“这些功能被明确授予给应用程序，允许它使用它们，”Chiarlone 说。“但是，除非明确允许，否则不能使用功能三。”