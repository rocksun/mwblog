<!-- 
# WebAssembly 能否为组件模型将行动整合？
Can WebAssembly Get Its Act Together for a Component Model?
https://thenewstack.io/can-webassembly-get-its-act-together-for-a-component-model/
https://cdn.thenewstack.io/media/2023/09/07a11450-adi-goldstein-eusvweosble-unsplash-e1694705422811-1024x684.jpg
-->

随着新的 componentize-py 项目，Python 可以跻身顶级 WebAssembly 语言之列。

译自 [Can WebAssembly Get Its Act Together for a Component Model?](https://thenewstack.io/can-webassembly-get-its-act-together-for-a-component-model/) 。

WebAssembly 的最后一公里仍在进展中，Wasm 社区争先恐后地确定一个共同的标准。在其他事项中，它正等待组件接口 [Wasi](https://wasi.dev/) 的标准化，这是确保在部署 Wasm 应用程序的不同设备和服务器之间的端点兼容性所需的层。随着在无需配置的众多不同端点之间进行的应用程序开发取得进展，WebAssembly 作为一种广泛采用的工具的生存仍有赖于这样一个标准的完成。但是，社区正积极寻求最终确定组件模块，这在上周由 Linux 基金会赞助的首届 [WasmCon 2023](https://events.linuxfoundation.org/wasmcon/program/schedule/) 期间进行的许多演讲中变得非常明显。

[Fermyon Technologies](https://thenewstack.io/webassembly-5-predictions-for-2023/) 联合创始人兼首席执行官 [Matt Butcher](https://www.linkedin.com/in/mattbutcher/) 对 The New Stack 表示："WebAssembly 在其他运行时技术方面具有少数小优势。组件模型是最大的不同。这开辟了以前从未存在过的开发途径。公平地说，这对WebAssembly 是一个重要的存在时刻。"

## WASI-Preview 2 的实现

本于 7 月发布的路线图反映了 WebAssembly 社区组(CG)和 W3C 内部的 WASI 子组中的标准变化。这包括核心 WebAssembly WebAssembly 组件模型、WASI(WebAssembly 系统接口)以及一些基于 WASI 的接口。

这个提案的组件模型是建立在核心规范之上的，其中包括 WebAssembly Interface Types（WIT）IDL，而 WIT 是用来描述组件接口的高级类型的语言，正如 [Bytecode Alliance](https://bytecodealliance.org/) 技术标准委员会主任兼 Cosmonic 的 CTO [Bailey Hayes](https://www.linkedin.com/in/baileyhayes) 在一篇[博客文章](https://bytecodealliance.org/articles/webassembly-the-updated-roadmap-for-developers)中所解释的。

组件模型增加了带有导入和导出接口的高级类型，使组件可组合和可虚拟化，Hayes 说。这对于允许不同的编程语言在同一模块中发挥作用非常重要，因为它允许创建和组合最初以不同编程语言编写的组件，Hayes 说。

WebAssembly(Wasm) 的最新标准非常重要，因为它们将开发者、社区成员和采用者的努力集中在支持可移植生态系统的工具上，Cosmonic 的首席执行官兼联合创始人 [Liam Randall](https://www.linkedin.com/in/hectaman) 对 The New Stack 表示。“随着关注 WebAssembly 组件的出现，它们使组件能够作为新的容器发挥作用，确保跨各种公司在整个景观中进行开发的可移植性，”Randall 说。“这种标准化还促进了从各种语言创建组件的语言工具之间以及由 WASI 定义的热插拔模块之间的更好协作。这对开发者意味着我们现在可以跨语言隔阂使用代码，为 WebAssembly 生态系统创造一个强大的‘更好地搭配使用’故事。”

换句话说，WASI-Preview 2 是一个激动人心的步骤，因为它解决了性能、安全性和 JavaScript 交互等关键领域的问题——这是通往互操作性的旅程中又一步，[企业管理联盟(EMA)](https://www.enterprisemanagement.com/)分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 对 The New Stack 说。“通用组件模型对于加速 WebAssembly 的采用至关重要，因为它是用户无需更改应用程序代码或配置就可以在任何云、数据中心或边缘位置上运行任何应用程序的先决条件，” Volk 说。

然后，请求访问 GPU、数据库或机器学习模型的 API 调用将独立于所请求组件的特定类型，Volk 说。“这意味着我可以定义数据流应该如何写入 NoSQL 数据库，并且相同的代码功能将适用于 MongoDB、Cassandra 或 Amazon DynamoDB，”Volk 说。

WASI 起初是一个针对 WebAssembly 的类 POSIX 库。然而，它已经超越了这些根源，变得更像 JavaScript 的 WinterCG：一组核心接口，用于通常使用的功能，如文件、套接字和环境，Butcher 说。 “WASI Preview 2 体现了这种远离POSIX、走向真正现代核心功能集的运动。它没有重新实现 20 世纪 70 年代的网络计算愿景，而是转向了当代分布式应用程序的视图。”

组件方面在 Fermyon 使用 Python 编程语言开发 Spin 应用程序的实验性 SDK 中发布新功能方面发挥着关键作用。

关于组件，Fermyon 的新的 componentize-py 可用于使用 Python 和本机代码的组合来构建一个简单的组件，使用 MyPy 对其进行类型检查，并使用 Spin 运行它。然后，用户可以更新应用程序以使用 wasi-http 提议，这是一种与供应商无关的 API，用于发送和接收 HTTP 请求。

“为开发者提供将还没有完全由 CCM 定义的运行时元素集成的能力，这使他们在开发过程中不太可能遇到障碍，因此应该受到欢迎，”Volk 说。

关于 Python，它是“顶级语言选择，对人工智能至关重要”，Butcher 说。 “然而，到目前为止，一些最强大的 Python 库，如 NumPy 一直不可用。原因是这些核心库是用 C 编写的，并动态加载到 Python 中，”Butcher 说。 “谁会想到这个难题的解决方案是组件模型呢？”

随着新的 componentize-py 项目，Python 可以跻身顶级 WebAssembly 语言之列，Butcher 指出。 “最令人兴奋的是，我们距离跨语言边界链接非常接近，Rust 库可以从 Python 使用，或者 Go 库可以从 JavaScript 使用，”Butcher 说。 “多亏了组件模型，我们正处于真正的多语言编程的边缘。”

## 未来的工作

完成对 Wasm 广泛采用至关重要的组件模型的工作仍在继续，作为上述增量步骤的延续，边缘云平台提供商 [Fastly](https://www.fastly.com/) 的杰出工程师 [Luke Wagner](https://twitter.com/luke_wagner?lang=en) 上周在 [WasmCon 2023](https://events.linuxfoundation.org/wasmcon/program/schedule/) 上对 The New Stack 说。 Wagner 将组件定义为“标准可移植、轻量级细粒度跨语言组成模块”。

在他的会议演讲中，Wagner 描述了今年要发布的开发人员预览版本：

* Preview 2：它涵盖了组件模块和 Wasi 接口的一个子集。
* 顶层目标是稳定性和向后兼容性：

> “我们有一个自动转换，将 Preview 1 核心模块转换为 Preview 2 组件，然后我们承诺未来会有一个类似的工具将 Preview 2 组件转换为随后出现的内容，”Wagner 在他的演讲中说。

Wagner 说，Preview 2 的功能包括：

- 第一波语言，包括 Rust、JavaScript、Python、Go 和 C。
- 第一波 Wasi 提议，包括文件系统、socket、CLI、http，可能还有其他。
- browser/node polyfill:jco transpile。
- 以 wasi-virt 的形式进行 Wasi 虚拟化的初步支持。
- 以 Wasm-compose 的形式进行组件组合的初步支持。
- 实验性组件注册工具：以 warg 的形式。
- “明年一切关乎改进并发故事，”Wagner 说。 这是因为 Preview 2 “尽其所能但并发仍然有缺陷。”

Wagner 描述的这些缺陷方面包括：

- 异步接口将过于复杂，无法直接使用，需要手动胶水代码，而总体目标是能够直接使用自动绑定，而无需手动胶水代码。
- 流性能并不如人意。
- 并发目前不是可组合的，这意味着两个进行并发操作的组件在某些情况下会阻塞彼此。而且，如果你虚拟化了其中的一个异步接口，那么你就不得不虚拟化它们全部。

Preview 3 旨在：

- 通过向 Wit 和组件添加本机 future 和 stream 类型来修复这些缺陷。
- 这将为许多语言的无缝、集成的自动绑定铺平道路。
- 提供高效的 io_uring 友好 ABI。

可组合的并发性：例如，在 Preview 2 中，我们需要两个接口来进行 HTTP：一个用于传出请求，一个用于传入请求，具有不同的类型和不同的签名，Wagner 说。 使用 Preview 3，两个接口将合并为只有一个接口，即使用 Wasi 处理程序。

这样就可以实现一个同时导入和导出相同接口的单个组件：然后，它将能够导入用于传出请求的处理程序，并导出用于接收传入请求的处理程序。 因为它们使用相同的接口，所以之后就可以将两个服务链接在一起，只需要使用组件链接直接链接它们，现在执行整个复合请求只是一个异步函数调用，它可以支持模块化而无需微服务用例。

“我们的目标是到今年年底完成 Preview 2 里程碑，这将导致一个稳定的，也许是 beta 版本，”上周 [WasmCon 2023](https://events.linuxfoundation.org/wasmcon/program/schedule/) 之后 Fastly 的杰出工程师 [Luke Wagner](https://twitter.com/luke_wagner?lang=en) 对 The New Stack 说。

“这个想法是，一旦我们达到这个目标，你将可以继续生成 Preview 2 二进制文件并在 Preview 2 引擎中运行它们，所以东西不会中断。”
