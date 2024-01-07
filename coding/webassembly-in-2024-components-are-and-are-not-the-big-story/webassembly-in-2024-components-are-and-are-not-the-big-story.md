<!--
title: 2024年的WebAssembly：组件既是也不是大新闻
cover: https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1-1024x576.png
-->

随着开源项目的集成，WebAssembly的使用正在爆炸式增长，但它在今年的前景取决于组件模型是否会最终确定下来。

> 译自 [WebAssembly in 2024: Components Are and Are Not the Big Story](https://thenewstack.io/webassembly-in-2024-components-are-and-are-not-the-big-story/)，作者 B. Cameron Gain 是 ReveCom Media 的创始人兼首席分析师。他对计算机的痴迷始于 20 世纪 80 年代初，当时他在当地的视频游戏厅破解了太空侵略者控制台，以 25 美分的价格全天播放。然后......

WebAssembly 在 2023 年继续令人惊叹，但正如我们所见，这还远远不够。2024 年 [WebAssembly](https://thenewstack.io/webassembly/what-is-webassembly/) 的大新闻将是它是否能够兑现其通过各种端点和设备同时运行 CPU 指令集来部署应用程序的承诺，无论是从单一端点到端点还是反之亦然，并且可以使用任何编程语言。尽管编程语言问题在 2024 年可能无法解决，但 Rust、[Go](https://thenewstack.io/webassembly-and-go-a-guide-to-getting-started-part-1/) 以及当然还有 JavaScript 等语言如果可能的话，有望在不久的将来帮助实现这个圣杯。

2024 年 WebAssembly 所宣称的诺言实现的最后一公里或可行性，取决于一个组件模型是否会最终确定下来。与此同时，在幕后和不那么张扬的场景下，WebAssembly 正在爆炸式增长。尽管没有广泛讨论，但开源项目正在以各种方式跨组织集成 WebAssembly。在 2024 年，你可能不会看到明确的 WebAssembly 工具和流程，但是类似于 2023 年，你喜欢的许多无服务器应用程序，例如 [Azure](https://thenewstack.io/microsoft-makes-azure-load-testing-generally-available/)，可能会包含一系列支持 Wasm 的功能。

其它幕后示例包括 WASM 在[飞行模拟器](https://thenewstack.io/kubecon-eu-why-webassembly-is-more-than-a-javascript-replacement/)上的使用，这发生在几年前，以及 Adobe 之前提供[从浏览器访问应用程序](https://thenewstack.io/what-business-problems-does-webassembly-solve/)的功能，以及 [Fastly](https://www.fastly.com/) 云边缘平台和服务中的许多改进，这些平台和服务高度依赖于 WASM，将会持续存在。然而，WebAssembly 在幕后工作和与其他工具及流程的结合使用，可能不会像它们所支持的应用程序那样引起那么多关注。

这在无服务器应用程序中尤为明显，WASM 为这些应用程序提供功能支持但运行在后台。

Fermyon 联合创始人兼 CEO [Matt Butcher](https://www.linkedin.com/in/mattbutcher/) 在一次在线交流中告诉 The New Stack: "如果你参加任何三个 WebAssembly 会议 - [Wasm I/O](https://2024.wasmio.tech/)、[WasmCon](https://events.linuxfoundation.org/wasmcon/) 或 [WasmDay](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/cloud-native-wasm-day/)，你会听到的第一大用例与物联网(IoT)、插件系统甚至网络浏览器无关。" 这是服务端执行。WebAssembly 正走在替换第一代服务器端函数的更快、更敏捷运行时的道路上。

当然，还有 AI 的参与，随着它席卷各种软件开发和运维。它已经开始以一些惊人的方式与 WebAssembly 协作。这无疑是 2024 年值得关注的事情，并观察这些协作如何展开。

## 组件的问号

在 WebAssembly 模块中部署运行时中，WebAssembly 组件发挥着关键作用，尽管其标准化仍在进行中。一旦最终确定，此组件模型旨在将 WebAssembly 的使用扩展到网络浏览器和服务器之外。它将使用名为 [WebAssembly 系统接口(WASI)](https://thenewstack.io/mozilla-extends-webassembly-beyond-the-browser-with-wasi/)的组件接口，以高速通过数千个端点同时部署各种应用程序中的轻量级模块，所有这些都无需更改现有代码。

这个理论还在进展中，社区正积极努力实现它。同时，存在对组件概念及其在 WebAssembly 采用中的作用的困惑。9月的 [WasmCon](https://events.linuxfoundation.org/wasmcon/) 主题演讲中，Fastly 的杰出工程师兼 WebAssembly 的原联合创建者 [Luke Wagner](https://github.com/lukewagner) 将 Wasm 组件描述为一个新兴的、标准的、可移植的、轻量级的、细粒度沙箱的、跨语言的和组合模块。

组件是一个包含导入、内部定义和导出的模块。导入包括捕获组件提供的 I/O 及其实现依赖关系的元素，如导入的函数(比如日志函数)。这种方法避免了对固定的系统调用集或固定的运行时全局命名空间的依赖。Wagner 提到了一个正在进行的正式规范，其中包含操作语义、参考解释器和参考测试套件。在 [BindGen](https://thenewstack.io/webassembly/using-web-assembly-written-in-rust-on-the-server-side/) 和 Wasm 工具方面已经取得了实质性进展。

“组件模型使服务器端 WASM 真正激动人心，因为软件开发团队可以通过添加新模块来为其应用程序添加功能，而无需对现有代码进行更改。”[企业管理协会(EMA)](https://www.enterprisemanagement.com/)分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 说。

例如，团队可以添加用于实时分析的服务器端 WASM 模块，为特定用户组提供可能其他用户无法获得的有价值的见解，Volk 说。“这允许软件供应商根据客户需求和支付增强功能的意愿提供定制的应用程序。”他说。

一个里程碑目标被设定在 2024 年。它涉及将组件与全参数链接、值、资源和句柄类型同步。这不仅使 WebAssembly 的使用范围扩展到网络浏览器和服务器之外，还将赋予用户同时以高速部署各种应用程序的能力，跨越成千上万的轻量级模块，同时访问成千上万的端点。这是通过 WASI 实现的。值得注意的是，网络支持(WASI 预览 2 的最后一部分)应该“在 2024 年第一季度上线，消除了一个主要的采用障碍。”Butcher 说。

“前几个组件组合工具已经出现，[Bytecode Alliance](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) 开始发布关于构建组件的指导。”Butcher 说。“我们正处于一个新技术落地的时刻，我们屏息以待，看看这个新技术对生态系统会带来多大影响。”

对于 AI 而言，WebAssembly 支持了[大语言模型(LLM)](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)的大部分功能。我们在 2023 年见证的令人兴奋的发展只是开始。AI 用例发挥了 WebAssembly 的三大优势，Butcher 说。

“第一是硬件中立性。构建与 GPU 无关的 Wasm 应用意味着能够使用各种各样的 AI 硬件。”Butcher 说。“第二是可移植性:尽可能接近大型计算能力(或大数据)。第三是组件模型引入的多语言编程。想象一下从 [JavaScript](https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/) 访问 Python 的数据库 - 就像 JavaScript 与互联网同时出现一样，Wasm 的轨迹与 AI 相连。”

在 WASM 上运行 LLM 使开发团队能够通过以标准化微服务形式添加自定义 AI 模型来为现有应用程序添加基于 AI 的功能，Volk 说。有了组件模型，可以依靠 WASM 运行时为 LLM 提供 GPU、RAM、存储和其他硬件需求，以最大程度提高性能和效率。

“由于 WASM 应用程序是简单的二进制文件，开发人员可以在不涉及复杂部署过程的典型开销的情况下快速更新、替换、克隆、删除或移动它们。”Volk 说。

LLM 提供的灵活性允许快速扩展和适应性，并使开发团队可以进行最小风险的操作中断的实验，Volk 说。开发人员可以添加针对特定目标或用户组的新 AI 模型，甚至可以组合多个 LLM 以添加更多专业知识，然后将其作为高级层出售。

“单个应用程序中可以包含用于技术支持、客户服务和市场分析的单独 LLM。”Volk 说。“然后，这些 LLM 可以就涉及所有三者的问题解决方案进行讨论，或者他们甚至可以要求开发人员添加额外的模型来填补当前的知识空白。”
