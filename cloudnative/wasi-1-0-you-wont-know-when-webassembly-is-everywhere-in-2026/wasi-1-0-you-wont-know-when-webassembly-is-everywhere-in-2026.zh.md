[WebAssembly](https://thenewstack.io/webassembly/) 随着 Wasm 3.0 和组件模型的发布取得了巨大进步。然而，WebAssembly 真正成熟的最后一程将随着计划于 2026 年（很可能在 2 月）发布的 [WASI 0.3.0](https://wasi.dev/roadmap) 而到来。

除其他事项外，组件模型标准化的这个最后阶段将意味着 WebAssembly 将能够越来越多地取代 [容器](https://thenewstack.io/introduction-to-containers/)，无论是在 [Kubernetes](https://thenewstack.io/kubernetes/) 内部还是外部，容器都不理想地适用于许多应用程序。这些应用程序包括边缘设备、异步和事件驱动部署、无服务器环境，以及需要通过一次发布同时到达大量（可能无限）端点的部署用例。

## 远超浏览器

事实上，WebAssembly 已经远远超出了浏览器。微软 Azure Core Upstream 首席产品经理 Ralph Squillace 在 [KubeCon+CloudnativeCon North America 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 期间由 [CNCF](https://cncf.io/?utm_content=inline+mention) 共同举办的 [WasmCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/wasmcon/) 闭幕致辞中表示，它正在浏览器、服务器、CDN 和后端服务中可靠地运行，证明了其成熟度和广泛适用性。[Ralph Squillace](https://github.com/squillace) 说：“WebAssembly 已经在几乎所有环境中运行良好。”

Squillace 表示，虽然核心 WebAssembly 故意设计成低级且难以直接使用，但最近的规范工作实现了更高级别的抽象。引用类型和接口类型允许组件暴露有意义的 API，而无需开发人员理解 WASM 的内部机制，从而使工程师更容易接触这项技术。

Squillace 说：“核心层面的规范工作……正是组件模型能够实际传递复杂结构以形成有意义 API 的原因。”

Squillace 说，对于那些对组件特别感兴趣的人来说，[Bytecode Alliance](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) 免费向工程师开放。它专注于支持工程师和开源开发而非市场营销，并提供了包括文档在内的资源，使开发人员能够从零开始使用 WebAssembly 组件。

Squillace 说，这些选择并非相互排斥。WebAssembly 和组件模型不是要取代语言、模块或容器，而是关于互操作性、安全性以及扩展软件在不同语言和环境中的功能。

Squillace 说，WebAssembly 并不完美，但这并非重点。重要的是它所能实现的功能。这是一个由选择参与的人们共同构建的令人兴奋的领域，这就是为什么他说，这次闭幕实际上是一个开端。

## 核心规范

虽然核心 WebAssembly 故意设计成低级且难以直接使用，但最近的规范工作实现了更高级别的抽象。Squillace 表示，引用类型和接口类型允许组件暴露有意义的 API，而无需开发人员理解 WASM 的内部机制。

Squillace 说：“核心层面的规范工作……正是组件模型能够实际传递复杂结构以形成有意义 API 的原因。”

目前，基于 Wasm 的解决方案并非容器的直接替代品，但在许多利用 WebAssembly 优势的场景中，它们正越来越多地被采用。[Endor](https://endor.dev/) 首席执行官兼联合创始人 [Daniel Lopez](https://www.linkedin.com/in/ridruejo/) 告诉我：“组件模型是采用 Wasm 的一个令人信服的理由，即使它仍处于早期阶段。话虽如此，WebAssembly 已经被广泛采用，在许多无服务器和边缘应用中非常流行。”“许多用户——很可能大多数——并没有意识到它正在幕后使用，尤其是在 SaaS 和无服务器服务中。Wasm 已经为许多应用程序和用例提供了支持。在开发者和行业参与者的广泛支持下，进一步的标准化只会帮助加速其采用。”

Wasm 3.0 不包括组件模型的最终定稿。虽然 Endor 接近了，但那种像 Docker 一样神奇的时刻——你只需将几乎任何应用程序放入 Wasm 模块中，然后你可以在任何地方部署它或发送它，并且它可以在任何地方使用——仍然在开发中。

标准化将意味着应用程序可以用任何语言编写，并通过 Wasm 模块分发，以便同时（且异步地）部署到任何端点。一旦最终定稿，组件模型将使 WebAssembly 的用途扩展到网页浏览器和服务器之外。它将允许用户以非常高的速度同时在数千个端点上部署运行在众多轻量级模块内的不同应用程序。

在 KubeCon+CloudnativeCon North America 2025 期间由 CNCF 共同举办的 WasmCon 开幕致辞中，Cosmonic 首席技术官 [Bailey Hayes](https://www.linkedin.com/in/baileyhayes/) 描述了使 WebAssembly 如此强大的核心优势：接近零的冷启动、高工作负载密度以及即使在受限环境中也能良好运行的轻量级、可移植运行时。展望未来，Hayes 预告即将发布的 WASI 0.3.0 版本将是一个重要的里程碑。Hayes 说，它预示了定义下一波基于 WebAssembly 计算的几个特性。Hayes 表示，这些特性包括带有不同语言的惯用绑定的语言集成并发、跨不同语言编写组件的可组合并发，以及由低级 I/O 和零拷贝数据处理实现的高性能流媒体。

## 下一波的关键特性

Hayes 说：“我想强调三个让我对下一波计算最兴奋的关键特性，包括语言集成并发、跨不同语言编写组件的可组合并发，以及支持具有低级 I/O 和零拷贝的高性能流媒体。”

很大程度上取决于组件模型的最终定稿，特别是其与 WASI 的关系，WASI 是将 WebAssembly 模块连接到组件的标准接口或 API。它将支持开发所谓的 WebAssembly“世界”，因为兼容的 Wasm 组件群将形成一个类似于 Kubernetes 但没有容器的互联基础设施。2024 年发布的 WASI Preview 2 在标准化方面取得了巨大进展，但我们尚未完全实现目标。2025 年，我们可能无法实现最终目标，但可能会看到一些惊喜。有传言称 Wasi 0.3.0 可能无法在今年最终定稿，这可能会延迟 Wasi 0.3.0 的发布，并因此延迟一个可用的组件模型。

Lopez 说：“WASI 的标准化过程漫长，但每个新的预览版都让我们离 0.3.0 更近一步。”“鉴于该标准的范围和基础性质，即使花费的时间比预期长，也务必尽可能地做好。”