将 [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 集成到 [Helm](https://thenewstack.io/helm-4-whats-new-in-the-open-source-kubernetes-package-manager/) 生态系统，简化了跨不同环境（包括 OCI 容器和虚拟化基础设施）的 [WASI](https://thenewstack.io/wasi-preview-2-what-webassembly-can-and-cant-do-yet/)-兼容二进制文件的编排。通过利用 Helm 的模板引擎，开发人员可以标准化沙盒模块的生命周期，同时保持高度可移植性。

尽管 Wasm 本身通过基于能力的安全模型提供了故障隔离执行，但通过 Helm 部署通过 [Kubernetes](https://thenewstack.io/kubernetes/)-原生分段加强了这一点。这种结合确保了应用程序同时受益于指令级沙盒和集群范围的管理隔离，有效地增强了微服务架构的安全性。

速度上也有明显的差异。根据 [ReveCom](http://www.revecom.io) 的数据，在比较传统的 Helm 3 插件与 Helm 4 Wasm 插件时，延迟和其他指标方面，延迟可能会有高达 40% 的增加或减少。

Wasm 的“一次编写，随处运行”特性在这里再次闪耀，允许在 x86、ARM 或其他多种不同 CPU 配置上进行安装。

对于 ArgoCD，我们尚未进行测试，但通过 Argo 运行 Wasm 提供的插件功能，Argo 的性能指标可能会略快一些。然而，如上所述，Wasm 模块提供了一层额外的隔离和安全性。这并非说 ArgoCD 缺乏安全性，而是 Wasm 插件为 Helm 增加了一道额外的防护。对于大多数用例而言，性能差异可能可以忽略不计。

## 对比 Kubernetes

乍一看，我记得我曾问过 WebAssembly 是否有一天，尤其是在组件模型最终确定后，可以在某种程度上取代 Kubernetes。我认为在遥远的未来这很可能发生，尽管显然不会完全取代。然而，Helm 支持 WebAssembly 并不会进一步推动这种可能性。如果那一天真的到来，Helm 本身可能会变得无关紧要。

Couchbase 的高级开发人员体验工程师 Shivay Lamba 大体上同意：

“Helm 采用 WebAssembly 插件实际上是增强了 Kubernetes，而不是削弱它。Helm 的 Wasm 插件系统的主要动机是帮助提高可扩展性、安全性和可维护性，”Lamba 说。“虽然 WebAssembly 确实引入了一种引人注目的执行和隔离模型，但 Helm 使用 Wasm 仍然将 Kubernetes 作为控制平面、调度器和生命周期管理器。如果 WebAssembly 要真正取代 Kubernetes，它将需要一个原生的、Wasm 优先的编排模型，完全消除以容器为中心的抽象需求。在这种情况下，Helm 本身确实会变得不那么重要。这项新变化提出的是一种进化式变革，而不是革命性变革。它优化了我们扩展 Kubernetes 工具的方式，而不是挑战 Kubernetes 的作用。”

不过，我们看到的是 Wasm Helm 插件提供了一层很好的额外隔离。在 Kubernetes 上通过 WebAssembly 运行应用程序已经有一段时间了。事实上，如果你正在使用无服务器应用程序，无论是在网络上还是在 LightXL 服务器上，你可能已经在不知不觉中使用了 WebAssembly。

这个插件发布版所做的，尤其是如果你已经在使用 Helm，是它显著减少了在 Kubernetes 和容器化基础设施上通过 WebAssembly 模块运行应用程序所需的工作量。换句话说，所需工作量大大减少。

“Helm Wasm 插件系统的真正价值是实用的：它降低了摩擦。通过减少在现有 Kubernetes 和容器化环境中运行 WebAssembly 工作负载所需的操作和认知开销，它使 Wasm 对那些已经标准化使用 Helm 的团队更易于访问，”Lamba 说。“这与 WebAssembly 最初的‘一次编写，随处运行’的承诺非常吻合，不是通过替换基础设施，而是通过干净地融入其中。重要的是，Wasm 强大的隔离保证得到了保留，同时 Helm 增加了熟悉的打包、分发和生命周期管理。此发布版不是重新定义平台堆栈，而是通过满足开发人员的现有需求来加速采用。”

Helm 的创建者之一，Akamai Technologies 产品管理副总裁兼联合创始人 Matt Butcher 多年前就看到了 Helm 对类似 Wasm 功能的需求。

“早在我们开发 Helm 3 时，我们就意识到需要为我们最专业的用户提供一条途径来定制 Helm 本身的行为。当时我们研究了使用 Lua，”Butcher 说。“但尽管我们付出了努力，我们从未找到一个我们喜欢的模型。现在，几年过去了，WebAssembly 是一个比 Lua 更好的替代方案。”

这有助于实现 WebAssembly 的最初承诺之一：一次编写应用程序，将其打包为 WebAssembly 模块，并在支持 CPU 指令集的众多端点上运行。同时，它继续支持强大的隔离。

“现在你可以用多种语言编写 Helm 插件，并获得 WebAssembly 运行时的所有优势：速度、可移植性、安全性以及标准合规性。WebAssembly 作为插件提供商长期以来一直是一个引人注目的用例，Helm 4 证明了这一点，”Butcher 说。“但这并不是我们将在 Kubernetes 生态系统中看到 Wasm 的唯一地方。[CNCF](https://cncf.io/?utm_content=inline+mention) 项目，如 Spin 和 SpinKube，将继续将 WebAssembly 用于其他目的，例如无服务器函数。”