# 2025 年 WebAssembly 的发展前景

![2025 年 WebAssembly 的发展前景](https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1-1024x576.png)

几年前，我将[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 描述为“超强编译器”，这惹恼了许多支持者。但我认为这种说法仍然成立，因为到 2025 年，WebAssembly 模块应该能够集成用您选择的语言编写的应用程序，并部署到运行兼容 CPU 指令集的任何环境或设备上。这将实现跨不同设备类型的应用程序的同步部署和更新。

从[Mozilla](https://thenewstack.io/mozilla-extends-webassembly-beyond-the-browser-with-wasi/)的一个小众项目发展到集成到各种环境和基础设施的技术，WebAssembly 在过去几年中发展迅速，并已应用于各个行业。

早期的 KubeCon 会议和[WasmCon](https://events.linuxfoundation.org/wasmcon/)、[Wasm/IO](https://2024.wasm.io/)等会议的讨论仅吸引了几百名与会者。相比之下，最近在这些会议和其他会议（例如[KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)）上举办的活动，参与者人数越来越多，他们积极使用和开发 WebAssembly，这反映了它在开源社区中日益增长的重要性。

展望 2025 年，预计 WebAssembly 将在会议上展示的沙盒项目（通常非常引人入胜）之外获得实际应用。向外行解释其功能可能仍然很困难，但将会有更多真实的案例展示[Wasm 的功能](https://thenewstack.io/amexs-faas-uses-webassembly-instead-of-containers/)，因为其应用预计将不仅扩展到浏览器，还将扩展到服务器、[无服务器计算](https://thenewstack.io/serverless-computing-in-2024-genai-influence-security-5g/)、边缘部署和其他领域。在某些情况下，WebAssembly 可能会取代传统的容器，并直接与[Kubernetes](https://thenewstack.io/kubernetes/)集成。此外，WebAssembly 的安全特性也吸引了[美国政府](https://thenewstack.io/the-feds-push-webassembly-for-cloud-native-security/)的关注。

## 最后一公里？

WebAssembly 的主要特性之一尚未实现：标准化，以便用任何语言编写的应用程序都可以通过 Wasm 模块进行分发，以便同时（异步）部署到任何端点。一旦完成，组件模型将使 WebAssembly 的用途能够扩展到 Web 浏览器和服务器之外。它将允许用户以非常高的速度同时在数千个端点上部署运行在众多轻量级模块内的不同应用程序。

这很大程度上取决于组件模型的最终确定，尤其是它与[WASI](https://thenewstack.io/wasi-preview-2-what-webassembly-can-and-cant-do-yet/)的关系，WASI 是将 WebAssembly 模块链接到组件的标准接口或 API。它将支持所谓的 WebAssembly“世界”的开发，因为兼容的 Wasm 组件组形成了类似于 Kubernetes 但没有容器的互连基础设施。[WASI 预览版 2](https://thenewstack.io/why-wasi-preview-2-makes-webassembly-production-ready/)于 2024 年发布，在标准化方面取得了巨大进展，但我们尚未达到目标。在 2025 年，我们可能无法实现最终目标，但可能会有一些令人惊喜的发现。

改进的 WASI 和组件标准意味着除了当前稳定的 Rust、Go 和 C++ 之外，还可以使用更多语言与 WebAssembly 配合使用。

TechTarget 的 Enterprise Strategy Group 分析师说：“在 2025 年，我们需要看到 WebAssembly 系统接口 (WASI) 与 Python 之间的紧密集成，以便每个 Python 开发人员都可以编写可在 Wasm 中运行的应用程序。”“这种集成非常令人兴奋，因为它将使开发人员能够编写可重用的 Python 模块，其他开发人员可以直接将其添加到自己的应用程序中。消除开发人员不断重写现有程序的长期问题将是开发人员生产力的一次重大突破。”

一旦在 2025 年最终确定，组件模型将使 WebAssembly 不仅能够看到其在 Web 浏览器和服务器之外的应用扩展，还能够允许用户部署运行在众多轻量级模块内的不同应用程序。它们通过名为“世界”的组件接口以非常高的速度同时分发到少量到数千个端点，而无需更改一行代码，如上所述。
此外，如上所述，组件模型还将使Wasm能够集成更多[编程语言](https://thenewstack.io/programming-languages/)。

“从发布的第一天起，WebAssembly 的一大赌注就在于语言支持。构建标准二进制格式是一回事，让数十种编程语言编译成这种格式则是另一回事——但这正是 Wasm 所发生的事情，”Fermyon 联合创始人兼首席执行官说。“然而，组件模型正是将这种二进制格式提升到一个新水平的东西。”

有了组件模型，Python 开发人员可以使用 Rust 编写的库，JavaScript 开发人员可以使用现有的 Go 库，”说。“源语言是什么已经不再重要——重要的是它被构建成了一个 Wasm 组件。”

## 边缘微型虚拟机
使用 Wasm 模块作为边缘部署和管理的轻量级和沙盒安全性的想法已经存在一段时间了。根据云供应商的不同，微型虚拟机将允许本地或云端资源通过云端分发来自本地系统的海量数据流量。这是通过与容器相比非常轻量的 Wasm 模块完成的。[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention)Cloud 等公司将在 2025 年标准制定完成后提供不同的版本。

“我们现在可以使用这些轻量级沙箱来处理进入系统的网络流量，”Microsoft Azure 首席技术官兼技术研究员在[Microsoft Ignite](https://ignite.microsoft.com/) 用户大会上说。“这为实时、高效的网络处理带来了令人难以置信的可能性。”

Wasm 模块不会完全取代容器，但它们将逐渐集成到云原生环境中，以弥补传统容器和虚拟机缺乏的许多不足。

说这些将从效率最低的部署类型——虚拟机——转向效率最高的部署类型——WASM 容器——标准 Linux 容器处于中间位置。

“我认为组织将并行运行虚拟机、容器和 Wasm 容器，Kubernetes 将充当掌控者，负责处理策略合规性、弹性和性能，”说。

在许多方面，WebAssembly 都是部署和管理网络边缘设备的缺失拼图。

“我们已经习惯了从客户端和服务器的角度思考问题，边缘让我们措手不及。它打破了我们的思维定势，”说。“凭借 Wasm 几乎可以在任何环境中运行的能力，我们旧的双层客户端-服务器模型正在让位于一个连续的计算模型。边缘计算是 Wasm 成功的重要因素，我们将在 2025 年看到这一点的充分展现。”

## 安全性是真实存在的
WebAssembly 不仅可以为应用程序提供安全保障，还可以作为应用程序的安全措施，这一点在过去几年的研究论文和其他研究中已被证明是有效的。然而，它尚未作为独立的安全措施获得显著的关注。

根据美国政府国家标准与技术研究院 (NIST) 今年早些时候发布的一篇论文“云原生应用程序的数据保护方法”，在 2024 年，WebAssembly 尤其可以也应该集成到整个云原生服务网格领域以增强安全性。该论文中概述的框架可能会导致未来对 WebAssembly 或云原生环境的合规性要求，同时为更广泛地使用 WebAssembly 进行安全奠定基础。

我的预测是，虽然我们可能不会在 2025 年看到 WebAssembly 作为安全措施的广泛采用，但这篇报告可能会启动或准备为认真考虑 WebAssembly 如何作为安全层（特别是对于云原生应用程序）奠定基础。因此，虽然 WebAssembly 可能不需要符合 2025 年的美国政府项目，但它最终可能会成为未来一个关键组件。

“Wasm 的严格安全性可以防止许多工作负载获得足够的资源访问权限，”说。“但在这里，Wasm 贡献者和产品供应商的工作量很大，因为他们可以根据公司在现实生活中运行标准 Linux 容器的情况来确定其路线图的优先级。”

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)