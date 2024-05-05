
<!--
title: WebAssembly、大型语言模型和 Kubernetes 至关重要
cover: https://cdn.thenewstack.io/media/2024/04/ba06a6f3-jose-castillo-wi8ax3vvmla-unsplash-1.jpg
-->

WebAssembly 使得在机器上下载并运行一个完整的 LLM 变得快速且容易，无需任何重大设置。

> 译自 [WebAssembly, Large Language Models, and Kubernetes Matter](https://thenewstack.io/webassembly-large-language-models-and-kubernetes-matter/)，作者 Torsten Volk。

[WebAssembly (WASM)](https://thenewstack.io/webassembly/) 使得在任何你能在办公桌下、数据中心、[AWS](https://aws.amazon.com/?utm_content=inline+mention) 账户或玉米田里 30 吨收割机的控制单元中找到的硬件上开发、构建、运行和操作完全相同的代码变得非常简单。

虽然我在底特律举行的 2022 年 KubeCon 上与 Fermyon 的首席执行官 [Matt Butcher](https://www.linkedin.com/in/mattbutcher/) 讨论过这一愿景，但如今已经有了实际的生产就绪用例，带来了切实的价值。

## LlamaEdge：一行代码即可在任何地方运行 LLM

开源项目 [Llama](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)Edge 承诺，只需将一行代码粘贴到基本上任何机器上的终端中，几秒钟后就会弹出一个浏览器，显示一个与我们习惯于从 [ChatGPT](https://thenewstack.io/using-chatgpt-for-questions-specific-to-your-company-data/) 中看到的非常相似的 UI。当然，我们既没有在笔记本电脑上运行 ChatGPT 的硬件，[OpenAI](https://thenewstack.io/openai-chats-about-scaling-llms-at-anyscales-ray-summit/) 也没有从许可的角度提供该选项，但是，我们可以运行数十种开源变体。默认情况下，LlamaEdge 会在本地机器上安装一个小型版本的 [Google 的 Gemma](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/) LLM 以立即获得满足感，并且效果很好。

但是，如何在没有任何主要设置的情况下在我的机器上下载并运行一个完整的 LLM 如此快速且容易？这就是 [wasmEdge](https://thenewstack.io/demo-use-webassembly-to-run-llms-on-your-own-device-with-wasmedge/) 发挥作用拯救局面之处。Llama Edge 以预编译代码（字节码）的形式在 WasmEdge 运行时之上运行。它只需要 30MB（不是 GB！）的磁盘空间以及下载你选择的 LLM 所需的空间。下载后，Llama Edge 利用了 wasmEdge 的能力，可以在基本上任何操作系统（Windows、Linux 和衍生产品）和任何硅（英特尔、AMD、英伟达等）之上持续提供 CPU、GPU、RAM 和磁盘资源，而无需任何高级配置。立即在你的机器上打开一个终端并查看：此单一命令…

```bash
bash <(curl -sSfL '<a href="https://raw.githubusercontent.com/LlamaEdge/LlamaEdge/main/run-llm.sh">https://raw.githubusercontent.com/LlamaEdge/LlamaEdge/main/run-llm.sh</a>')
```

… 产生了一个 UI，无需任何进一步的配置。

## 组件是新的容器

[Cosmonic](https://thenewstack.io/cncf-welcomes-webassembly-based-wasmcloud-as-a-sandbox-project/) 的首席执行官 [Liam Randall](https://www.linkedin.com/in/hectaman/) 说：“组件是新的容器。”考虑到我能够在撰写本文的同一台 MacBook 上在一分钟内设置一个完整的 LLM，包括其类似 ChatGPT 的 UI，Randall 的声明完全有道理。如果我在没有 WASM 的情况下安装相同的 LLM，我将不得不遵循许多特定于 MacOS 的步骤：1）安装 homebrew，2）安装必需的软件包，3）查找并克隆所需的 Llama LLM，4）安装 Python 依赖项，5）转换和量化模型文件，以及 6）测试我的安装。但是，由于我正在运行 WasmEdge，因此我不必担心任何这些步骤，甚至不必存在 Python 运行时。LlamaEdge 只需要 wasmEdge 即可运行，仅此而已。

## 但我需要学习 Rust 吗？

作为一名 [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/) 开发人员，我强烈希望不必学习 [Rust](https://thenewstack.io/microsoft-rust-is-the-industrys-best-chance-at-safe-systems-programming/) 就能使用 LLM。我只需要一行命令行代码来设置 LLM，然后如果我想选择一个特定的 LLM 而不是默认的 LLM，则需要另一行代码：

```bash
bash <(curl -sSfL 'https://raw.githubusercontent.com/LlamaEdge/LlamaEdge/main/run-llm.sh') --model llama-2-7b-chat
```

上述命令将用户带到开箱即用的 LLM 选择中。

我仍然没有编写一行实际的 Rust 代码，而是从 [LlamaEdge GitHub 网站](https://github.com/LlamaEdge/LlamaEdge) 复制并粘贴了所需的命令，现在我可以与我的全新 LLM 交谈了。回到 Randall 关于组件是新容器的声明，我现在可以简单地将此模型作为组件导入到我未来的任何 Python 应用程序中。同时，我可以与我的团队或客户共享此组件，以便他们也可以将我的 LLM 纳入他们自己的应用程序中。

这让我回想起我与 Fermyon 的 [Tim Enwall](https://www.linkedin.com/in/timenwall/) 在 [AWS Re:Invent](https://thenewstack.io/open-source-on-aws-stories-from-the-zone-at-reinvent/) 上讨论了以订阅服务的形式提供 WASM 组件的可能性。作为一名行业分析师，如果创建自己的 LLM 并使用过去的出版物对其进行微调，可以将其编译为 WASM 并销售其数字孪生的订阅。

## 另一个用例：用于日志记录及其他领域的的数据管道管理

[Calyptia](https://thenewstack.io/the-combined-power-of-chronosphere-and-calyptia/) 的 FluentBit 可观测性数据管道管理平台允许开发人员以 WASM 程序的形式编写插件。开发人员可以使用 Rust、TinyGo 和 Python 编写用于处理管道数据的函数。

我们现在可以将此连接回我们的 LlamaEdge 示例，让我们的 WASM 管道程序“与”LlamaEdge “对话”，实时分析日志、提取有意义的见解，甚至根据日志的内容自动执行响应。想象一下一个场景，你的 WASM 管道程序检测到日志数据中的异常情况，比如流量异常激增或潜在安全漏洞。然后，它可以查询 LlamaEdge LLM 以更好地理解上下文并提出立即采取的行动，或将问题上交给合适的团队成员。

将 LLM 集成到数据管道中，事件监控和响应过程将变得更加智能和主动。这可能会彻底改变我们处理日志数据的方式，将被动式流程转变为动态、自动化的流程，不仅能发出警报，还能提供可能的解决方案。在数据管道中以分散方式处理遥测数据可以减少必须吸收到一个或多个公司可观测性平台中的数据量，这一点尤其有趣。由于许多可观测性平台根据传入数据量对企业客户进行收费，因此可以明显节省成本。

## Kubernetes的Fermyon平台：更高的密度，更低的成本

[Fermyon](https://thenewstack.io/fermyon-says-webassembly-on-kubernetes-is-now-doable/) 为 Kubernetes 推出了 [SpinKube](https://thenewstack.io/fermyon-says-webassembly-on-kubernetes-is-now-doable/) 框架，使 WASM 应用程序能够在 Kubernetes 上运行，密度更高，因此与容器相比成本更低。SpinKube 利用 WASM 模块的轻量级特性，将更多应用程序打包到每个服务器节点上，减少了所需的计算资源。

SpinKube 框架旨在面向开发人员友好，与现有的 Kubernetes 环境提供无缝集成。开发人员可以部署自己的 WASM 应用程序，就像传统容器化应用程序一样，无需学习新工具或工作流。这种易用性加快了开发周期，并简化了部署过程。

此外，SpinKube 确保应用程序级别的安全性和隔离性，这是多租户环境的一个关键方面。每个 WASM 应用程序在其隔离的沙箱中运行，提供一个安全执行环境，最大程度地降低了漏洞影响主机系统或其他应用程序的风险。

Fermyon对开放标准和社区驱动的开发的承诺在SpinKube的架构中得到了体现。该平台支持广泛的编程语言和工具，使其能够为更广泛的开发者社区所用。这种包容性会培养创新并鼓励在各个行业采用WASM技术。

总之，Kubernetes的Fermyon代表了云原生计算中的一项重大进步。通过提高密度和降低成本，同时保持易用性、安全性以及开放性标准，SpinKube将自己在Kubernetes应用程序部署的未来中定位为关键参与者。这里重要的是要提到Fermyon将SpinKube捐赠给了CNCF沙箱。

## 结语：LLM、开发者生产力和运营成本压力，WASM成功的驱动力

WASM 固有的能力，即在任何有 WebAssembly 运行时的地方始终运行，使得这项技术注定要“将 LLM 移动到数据所在的位置”。

这对于合规性原因来说非常棒，因为企业可以简单地将所需的 LLM “对接”到其相关数据源，而无需请求移动潜在敏感数据的权限。这种可移植性与 WASM 运行时的小尺寸以及在 Kubernetes 上运行 WASM 应用程序的能力（紧挨着传统容器）相结合，可以使在周末闲置的服务器基础设施上运行一些 LLM 推理或模型训练变得更便宜，因此也更容易。一旦到了周一，我们就可以终止我们的 WASM-LLM 应用程序或将它们移动到其他地方。当然，此原则不仅适用于 LLM，还可以适用于许多其他用例。

如果字节码联盟和 W3C WebAssembly 社区组可以加快实施 WebAssembly 组件模型的步伐，以便 WASM 可以普遍使用，那么这项技术将成为真正的游戏规则改变者。[WASI 0.2](https://thenewstack.io/wasi-0-2-unlocking-webassemblys-promise-outside-the-browser/) 是向前迈出的不错一步，但要使该平台为大众市场做好准备，仍有相当多的功课要做。
