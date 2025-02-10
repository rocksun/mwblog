# WebAssembly 在 Spin 3.0 中获得 Polyglot 开发的推动

![Featued image for: WebAssembly Gets Polyglot Development Boost in Spin 3.0](https://cdn.thenewstack.io/media/2025/01/0834b87b-nigel-hoare-jsszcgea9qc-unsplash-1024x576.jpg)

[Spin 3.0](https://thenewstack.io/wasm-spin-and-spinkubes-rocky-road-to-cncf-sandbox-status/) 的发布展示了开发者和 [平台工程师](https://thenewstack.io/platform-engineering/) 现在可以实现的目标。除了 [WebAssembly](https://thenewstack.io/webassembly/) 长期以来所吹捧的优势，即为部署提供轻量级模块和超低延迟的冷启动时间之外，Spin 3.0 通过允许用户直接从 WebAssembly 的 [polyglot](https://thenewstack.io/building-polyglot-developer-experiences-in-2024/) 功能中获益，从而扩展了使用 WebAssembly 的人员的可能性。其不断扩大的使用已产生了超过 5,625 个 [GitHub stars](https://github.com/fermyon/spin) 以及 230,000 次克隆和下载。

通过这种方式，Spin 3.0 实现了 WebAssembly 的核心承诺之一：使开发人员能够使用他们喜欢的 [编程语言](https://thenewstack.io/programming-languages/)，同时确保无缝集成。例如，[Rust](https://thenewstack.io/rust-programming-language-guide/) 开发人员可以编写 Rust 代码，将其作为模块分发，并将其部署在 [JavaScript](https://thenewstack.io/whats-new-for-javascript-developers-in-ecmascript-2024/) 应用程序中。此外，如果开发人员不喜欢创建自己的模块，他们可以访问开放容器计划 (OCI) 注册表中提供的各种预构建库，以用于模块创建和部署。

组件模型长期以来一直被描述为添加 Rust、[Go](https://thenewstack.io/introduction-to-go-programming-language/) 或另一个库的一种方式，并且“[Fermyon](https://www.fermyon.com/) 首席执行官兼联合创始人 Matt Butcher](https://www.linkedin.com/in/ACoAAAEPS-gBIXfA8q58HH4tGZG5NX4sb6T_lno/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3B1mszaN1ERXSC%2BwvqvdZ54Q%3D%3D) 解释说，“这对用户来说无关紧要”。“它看起来与他们使用的任何其他库相同。Spin 3——我们已经讨论了一段时间能够做到这一点，并且它已经存在于组件模型中大约一年了，”Butcher 说。“但实际上在实践中做到这一点一直是一个繁琐的过程，需要运行工具并说，‘好的，你要连接到这个东西，’只是因为工具还没有到位……所以最终，这种 polyglot 体验也变成了一件对开发人员来说很容易做到的事情。”

很大程度上取决于组件模型的最终确定，尤其是它与 [WASI](https://thenewstack.io/why-wasi-preview-2-makes-webassembly-production-ready/) 的关系，WASI 是将 WebAssembly 模块链接到组件的标准接口或 API。它将支持所谓的 WebAssembly “Worlds”的开发，因为兼容的 Wasm 组件组成了类似于 [Kubernetes](https://thenewstack.io/kubernetes/) 的互连基础设施，但没有容器。2024 年发布的 WASI Preview 2 在标准化方面取得了一些巨大进展，但我们尚未到达那里。在 2025 年，我们可能无法实现圣杯，但我们可能会看到一些令人惊喜的事情。同样，改进的 WASI 和组件标准意味着除了当前稳定的 Rust、Go 和 [C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) 之外，还可以使用更多语言与 WebAssembly 一起使用。

Spin 3.0 对组件模型的依赖也支持 AI 模型开发和训练。

“我们真的想用九种不同的语言再次编写相同的 AI 代码吗？或者我们是否可以简单地说，‘嘿，所有这些 Go 库和 Rust 库，我们可以从 [TypeScript](https://thenewstack.io/typescript/) 调用它们，而这边的这个库，我们可以将它与 Python 一起使用’，这将是一个非常激动人心的时刻，”Butcher 说。“我认为这是我们一段时间以来第一次开启了组件模型的潜力愿景，实际上使开发人员和平台工程师的生活更轻松。”

## 更多内容

Spin 3.0 使开发人员和平台工程师能够轻松开始使用 WebAssembly 模块部署和管理应用程序。一个关键特性是它使用了新完成的 WebAssembly 接口类型 (WIT)，这允许组件互操作，而不管用于创建它们的编程语言如何。这种互操作性强调了 WebAssembly 的兼容性和模块化，类似于微服务。

在支持 WASI API 标准方面也取得了重大进展，包括 WASI 键值和 WASI 配置 API，现在都受到 Spin 的支持。这项工作是更广泛的开源协作的一部分，旨在实现 WASI Cloud。WASI Cloud 是一项标准化 API 的提案，该 API 使应用程序能够通过 Spin 与一组统一的云服务进行交互。
此外，Spin 3.0 集成了可观测性工具（例如 OpenTelemetry），以便更好地了解 WebAssembly 应用程序。这确保了开发人员在部署和管理其应用程序时具有强大的监控和诊断功能。

通过集成 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)，可以更轻松地为 Spin 应用程序可观测性选择和实施您选择的可观测性平台。以前，可以使用 Jaeger 或 Prometheus 等工具通过 Spin 进行 Kubernetes 部署来查看指标，但这需要付出更多努力。现在，通过 OpenTelemetry 集成，该过程变得更加实用和简化。

Spin 3.0 也变得更容易学习、设置和使用。无论您是从事一次性项目还是更复杂的部署，该平台都可以适应各种用例。为此，Fermyon 引入了 Spin 因素，每个因素都提供一组特定的功能。这些功能旨在促进在不同环境中进行部署，使 Spin 更加模块化和适应性强。

此外，当您 Fork 该项目供自己使用时，这些因素简化了该过程，使您能够更有效地实现部署目标。Spin 因素使开发人员更容易访问该平台，无论他们是在进行实验还是实施生产级解决方案。

## 采用 Spin

同时，Spin（或 Kubernetes 的 SpinKube）和 WebAssembly 支持应该会看到更多的可用性。Docker、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)、F5 和 [NGINX](https://www.nginx.com?utm_content=inline+mention)、SUSE 等公司已经在一定程度上依赖 Spin 进行内部使用以及在他们提供的产品中使用。

说到 WebAssembly，Red Hat 产品管理高级总监 [Shobhan Lakkapragada](https://linkedin.com/in/shobhan/) 在 11 月 KubeCon+CloudNativeCon North America 之前的一次预备会议上回答我的问题时说，WebAssembly 是 OpenShift 之上的一个层。它仍然是一种新兴的 Web 应用程序构建技术，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 尚未直接支持。他说，采用仍处于“非常早期阶段”。

通过更新 OpenShift 工作节点上 [CRI-O](https://thenewstack.io/a-security-comparison-of-docker-cri-o-and-containerd/) 的配置以使用 crun-wasm 运行时 Podman，从而能够在 OpenShift 上运行 WebAssembly 工作负载，Red Hat 混合云平台高级总监 [Kirsten Newcomer](https://www.linkedin.com/in/kirsten-newcomer-36ab91) 告诉我。她说，OpenShift 客户将能够使用标准容器工具（注册表、引擎、运行时），包括与 OpenShift 和 Podman 配合使用的工具，方法是在 CRI-O 中实施支持。

Newcomer 说，CRI-O 今天已经支持 wasmedge，但“如果不同的 WASI 运行时（例如 wasmtime 或 wasmer）变得更占主导地位，我们将来可以将其替换掉”。“请注意，我们像运行其他运行时一样在容器中运行 Wasm 运行时。这提供了一个额外的安全层，具有 OpenShift 为所有容器提供的相同保护，包括 SELinux、cgroups 和网络命名空间，”她说。“Podman 还使您能够构建 Wasm OCI 镜像。” 从 OpenShift 4.14 开始，此功能作为开发人员预览版提供。

*Heather Joslyn 为本文做出了贡献。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。