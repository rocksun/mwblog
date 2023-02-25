# WebAssembly 真的是未来吗？

本文翻译自 [Is WebAssembly Really the Future?](https://thenewstack.io/is-webassembly-really-the-future/) 

Wasm 的前景比以往任何时候都更加光明。但接下来路线图会将我们引向何方？

![](https://cdn.thenewstack.io/media/2023/02/6b0fd145-drew-beamer-xu5mqq0chck-unsplash-e1677144349212-1024x683.jpg)

[云原生计算基金会 (CNCF) ](https://cncf.io/?utm_content=inline-mention)最近的[年度调查](https://www.cncf.io/reports/cncf-annual-survey-2022/)包括关于 [WebAssembly (Wasm)](https://thenewstack.io/how-webassembly-could-streamline-cloud-native-computing/) 的大胆声明：“容器是新常态，WebAssembly 是未来。”

这句话预示了很多事情，不仅是关于 WebAssembly 的路线图和发展，还有它在计算领域的当前地位。据 CNCF 报道，37% 的最终用户组织已经有一些使用 WebAssembly 部署应用程序的经验。根据 CNCF 报告，虽然其中许多用途是为了测试 Wasm 的优点，但 [WasmEdge](https://wasmedge.org/) 和 [WAMR](https://github.com/bytecodealliance/wasm-micro-runtime) 是使用最多的运行时。

“WebAssembly 是未来，因为它越来越多地用于 serverless、容器化和插件技术，预计将显着影响网络、serverless、游戏和容器化应用程序。”CNCF 生态系统负责人 [Taylor Dolezal](https://www.linkedin.com/in/onlydole) 在电子邮件回复中 告诉 The New Stack 。

但是 WebAssembly 的采用将走向何方，它的路线图和未来在计算中的位置是什么样的？让我们看看 Wasm 在容器、边缘和其他应用程序、编程语言和 serverless 方面的集成及其未来。

## 未来已现

可以说，您可以说 Wasm 与未来无关，但在它最初创建时所针对的所有主要 Web 浏览器中的使用已经非常重要。但是，虽然 Wasm 在浏览器方面已经成熟，但在它成为未来的一部分之前，还需要做更多的工作才能将其用于后端应用程序，还有在边缘设备中的使用和部署。

事实上，它并不像将 [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) 添加到 Wasm 然后通过托管 Wasm 运行时的 Wasi 运行包那么简单。对于[机器学习](https://thenewstack.io/machine-learning/)和数据分析等 Python 专门适配的后端应用程序，其在 Wasm 中的应用与大量刚刚开发和编译的第三方依赖项密切相关。

可轻松用于将 WebAssembly 借给后端应用程序的 Wasm [平台即服务 (PaaS)](https://thenewstack.io/pipelines-paas-continuously-delivering-continuous-delivery/) 产品或平台尚不存在，也就是说，Wasm 在浏览器之外的应用才刚刚兴起。

Enterprise Management Associates 的分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 告诉 The New Stack：“在可靠和高效地支持生产用例方面，有很多基础需要涵盖。” “究竟还缺少什么，我们会一路发现。那时开源项目和商业供应商会来弥补这些差距，并提供尽可能好的开发人员和 DevOps 体验。”

将服务器端 (ss-Wasm) WebAssembly 与用于浏览器应用程序的 Wasm 区分开来，ss-Wasm 前景广阔，而采用 ss-Wasm 的道路很长，而且“其中大部分仍然需要映射”，首席执行官兼首席执行官 Wiqar Chaudry ，即提供项目协作平台的 Xymbia 的创始人告诉 The New Stack。

“有两个非常简单的衡量标准：在创建软件时，Wasm 是否有明确的经济价值主张？它会降低成本，帮助公司和开发商赚更多钱，还是有助于解锁其他类型的未实现价值？” Chaudry 说，他也参与了 [Wasmer](https://wasmer.io/) 项目，目前担任顾问。

“第二个是它的技术价值主张。它是否吸引了足够多的开发人员并解决了足够多的技术难题，让他们承担使用 Wasm 作为其堆栈的一部分的开销？”

## 有 WASI 吗？

就目前而言，WASI 已成为将 Wasm 的范围扩展到浏览器之外的最佳候选者。它被描述为 WebAssembly 的[模块化系统接口](https://wasi.dev/)，事实证明它有助于解决在任何有正确配置的 CPU 的地方运行 Wasm 运行时的复杂性——这一直是 WebAssembly 自创建以来的主要卖点之一。

Fermyon Technologies 的联合创始人兼首席执行官 [Matt Butcher](https://www.linkedin.com/in/mattbutcher/) 告诉 The New Stack：“我相信 WebAssembly 作为通用技术的关键特性是支持 [WebAssembly 系统接口 (WASI)](https://thenewstack.io/mozilla-extends-webassembly-beyond-the-browser-with-wasi/)”。 “WASI 允许开发人员在他们的代码中使用熟悉的系统习惯用法，例如打开文件和读取环境变量，但不会破坏 WebAssembly 安全模型。随着 WASI 支持的普及，我们将看到 WebAssembly 用例的爆炸式增长。”

然而，WASI 仍在走向成熟。 “WASI 的第一个版本让我们看到了 WebAssembly 的潜力。第二个版本，预览版 2，将在几个月后发布，”Butcher 说。 “预览版 2 中添加的网络功能将开辟大量新用途。”

Cosmonic 的首席执行官兼联合创始人 [Liam Randall](https://www.linkedin.com/in/hectaman) 表示，WebAssembly 将利用组件和 WASI 将通用应用程序库抽象为通用的可插入组件。他说，发布-订阅消息传递或特定 SQL 服务器等组件作为抽象而不是与特定库的紧密耦合交付给应用程序。

“当容器出现时，它们更小，启动速度更快，并且为开发人员提供了比虚拟机更小的配置和维护表面积，”Randall 说。 “WebAssembly 模块延续了这一趋势，体积更小，启动速度更快，并利用组件来减少开发人员编写和维护的代码量。

“更重要的是，组件模型是一种新的应用程序方法，它允许以能力为导向的安全性，并使平台运营商更容易安全地运行应用程序。”

Wasm 使用 WASI 进行系统级集成 API 进一步增加了它作为通用运行时的可行性，Dolezal 说：“WebAssembly 在安全环境中托管不受信任的代码的能力也是一个重要的好处。”

## 容器关系

正如 CNCF 报告所说，容器确实是“新常态”，尤其是在云原生领域。在某些用例中，Wasm 可以取代容器，但总体而言，WebAssembly 和容器的采用将同步增长。

“我绝对相信 Kubernetes 和 Wasm 是互补的产品，其中 Kubernetes 负责配置和扩展基础设施，而 Wasm 则在此基础设施之上交付应用程序，包括其运行时，”Volk 说。

Kubernetes 采用的路径可以作为 Wasm 如何以及何时可能被大规模采用的可能模型。 “Kubernetes 之所以被广泛采用，是因为存在大量可以广泛的使用、扩展和支持的 Kubernetes 和工具。” Chaudry 说。 “如果 Kubernetes 不像 AKS、EKS 或 GKE 那样容易获得，我们就会看到更少的采用和使用。 WebAssembly 将走同样的路。”

Wasm 也只解决了容器所做的一些问题，他说：“容器更复杂，并且具有更高的操作开销。两者之间的权衡使得两者同步增长是合理的。”

Butcher 说，当 DockerHub 开始支持新的工件存储规范时，Wasm 社区意识到，与其重新发明轮子，不如将 Wasm 运行时存储在 Docker Hub 等 [Open Container Initiative](https://thenewstack.io/oci-reveals-governance-structure-amid-debate-focus/) 注册表中。

例如，本月 Fermyon 的 Spin 0.8 开始支持 OCI 注册中心。 “虽然我们最初不确定 OCI 注册管理机构是否是正确的分发机制，但标准的演变与 Docker Hub 的支持相结合改变了我们的想法，”Butcher 说。 “我们致力于使用 OCI 注册表分发 WebAssembly 应用程序，并且今天就可以这样做。”