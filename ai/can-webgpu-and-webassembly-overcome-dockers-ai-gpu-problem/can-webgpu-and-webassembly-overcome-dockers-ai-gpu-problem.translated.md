# WebGPU 和 WebAssembly 能否克服 Docker 的 AI GPU 问题？

![Featued image for: Can WebGPU and WebAssembly Overcome Docker’s AI GPU Problem?](https://cdn.thenewstack.io/media/2024/07/7b93c78a-mariia-shalabaieva-0sqstxwhgnu-unsplash-1024x576.jpg)

巴黎——[WebAssembly](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) 和 [Docker](https://www.docker.com/?utm_content=inline+mention) 已被证明为应用程序和代码可移植性提供了先进的功能。在 WebAssembly 的情况下，其口号是“一次部署，随处运行”。当然，Docker 以其抽象级别而闻名，这在很大程度上促成了 [容器化](https://thenewstack.io/containers/) 的广泛采用，并且可以说，[Kubernetes](https://thenewstack.io/kubernetes/) 凭借其久经考验且值得信赖的方式来移植应用程序。

然而，专家们在 6 月份于此举行的 [AI_dev](https://aidevsummit.co/) 大会上表示，在这两种情况下，GPU 的使用都被证明并非完全是障碍，而是 Docker 和 WebAssembly 的一个速度障碍。在 Docker 的情况下，可以将它的容器作为 GPU 上的抽象进行移植，但这需要为不同的 GPU 添加配置，从而增加额外的工作量。而想法是让 Docker 容器能够在任何地方运行，尤其是在任何 GPU 上运行，而无需额外的配置，例如添加驱动程序，否则您必须在 Docker 中直接支持的 CPU 上进行操作。

在 WebAssembly 的情况下，人们很少讨论的是 WebAssembly 如何被设计为在任何 CPU 指令集上运行。CPU 和 GPU 代表不同类型的指令集。因此，WebAssembly 开发人员一直在寻找一种方法来克服在 GPU 上部署 WebAssembly 的障碍。在这两种情况下，GPU 都是 [大型语言模型 (LLM)](https://thenewstack.io/llm/) 和 AI 功能以及处理的核心。为了扩展 WebAssembly 和 Docker 以用于 AI 应用程序，它们几乎完全以 GPU 为中心。改进 GPU 的抽象一直是一个令人关注的话题，尤其是在过去几个月里。

## WebGPU 登场

[WebGPU](https://thenewstack.io/pytorch-docker-and-ai-openness-highlight-ai_dev-europe/) 似乎提供了一种克服这些 GPU 缺点的方法。借助 WebGPU，WebAssembly 模块和 Docker 容器可以作为抽象直接部署在 GPU 上，而无需为与不同类型的 GPU（当然包括 [Nvidia 的 CUDA](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/) GPU 用于 AI 应用程序）的兼容性进行单独配置。Docker 现在正在发布 WebGPU 的预览版，用于 Docker Engine、[Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) 和其他平台。

WebGPU 一直被用作 [W3C](https://thenewstack.io/dev-news-w3c-accessibility-openai-python-sdk-and-more/) 标准，用于 JavaScript 编写的 API，以实现应用程序与 GPU 的兼容性，尤其是在 Web 上。为了让 WebAssembly 运行 AI 工作负载，WebGPU 充当 Web 上的硬件加速器。WASI-NN 等标准提供了兼容性接口，可以在主机可用的硬件上运行推理，但最近，更新的 WebGPU 标准已显示出其范围扩展到浏览器环境之外的 GPU。

正如 [Justin Cormack](https://uk.linkedin.com/in/justincormack)，Docker 的 CTO 和联合创始人，在其在 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) AI_dev 大会上的主题演讲中解释的那样，Docker 开发人员一直在寻找一种可移植的抽象，尤其是在您本地开发 GPU 的情况下。

“我们花了一些时间研究这些东西，发现 WebGPU 实际上已经存在，并且已经在大多数跨所有消费级 GPU 和移动设备的浏览器中发布，并且它拥有一个生态系统，”Cormack 说。“因此，我们今天宣布，我们将在 Docker 中支持 WebGPU。”

在会议期间，Cormack 解释了 WebGPU 如何展现出巨大的潜力。在与我交谈时，他描述了 WebGPU 如何特别适合移植到 GPU 环境的 Docker 容器。

“这实际上很有趣，因为在很多情况下，只要你能获得硬件卸载，就一直在进行大量工作来抽象化硬件卸载，使其更具可移植性，”Cormack 告诉我。

从历史上看，许多使用 GPU 的应用程序都与 Nvidia CUDA 密切耦合。Cormack 说，复杂的应用程序，例如科学计算，都是针对 GPU 开发的。相比之下，ML 模型的结构要简单得多，需要快速但并非一定准确的操作，并且重复多次。

“这意味着它们不一定需要与特定硬件紧密集成才能正常运行，”Cormack 说。
对于 WebAssembly，[WasmEdge](https://thenewstack.io/rust-and-webassembly-serverless-functions-in-vercel/) 项目维护者兼 [Second State](https://thenewstack.io/demo-use-webassembly-to-run-llms-on-your-own-device-with-wasmedge/) 首席执行官 [Michael Yuan](https://www.linkedin.com/in/myuan/) 描述了 Docker 容器如何与 WebGPU 和开源项目（如 WasmEdge，一个 CNCF WebAssembly 运行时项目，以及 [LlamaEdge](https://github.com/LlamaEdge/LlamaEdge)）一起用于边缘的 AI 应用。

Yuan 描述了 WebGPU 如何真正从浏览器开始。

“您已经看到许多 WebAssembly 组件被编译以在浏览器中运行，利用了 WebGPU，”Yuan 说。“但是，我们与 Docker 的故事侧重于浏览器之外的边缘和服务器端用例。有些人可能会问，‘我在服务器端 AI 上使用 Wasm 来做什么？’事实上，它被广泛用作 AI 模型的嵌入式运行时。”

Yuan 说，对于需要 AI 服务的应用程序，想法是，与其让 AI 模型在提供 API 的单独服务器上运行，不如将开源 AI 模型嵌入到您的应用程序中并一起打包。

“这种方法对于边缘用例、开发用例以及各种其他场景特别有用，”Yuan 说。“您希望将您的大型语言模型与应用程序的其余部分打包在一起，以紧密耦合的元素（如提示和上下文窗口）进行打包。人们正在使用 WebAssembly 作为应用程序与大型语言模型交互的运行时或中间件。”

« GPU 已打破 » 传统上在 CPU 上的云计算范式 » 用于 LLM，但一个

[#Wasm]模块在一个[@Docker]容器中可以提供帮助，来自异构云中高效且跨平台的 LLM 推理，[@juntao]来自 Second State 在巴黎的[#AIDev]大会上。[pic.twitter.com/Fexkae50ym]— BC Gain (@bcamerongain)

[2024 年 6 月 20 日]
使用基于 WasmEdge 构建的 LlamaEdge，它也是用 [Rust](https://thenewstack.io/rust-meets-dart-with-release-of-rust_core-1-0-0/) 编写的，并编译为 WebAssembly，它可以直接嵌入到主机应用程序中。“这允许应用程序访问包含在同一包中的大型语言模型，”Yuan 说。

Yuan 在他的会议演讲“异构云中高效且跨平台的 LLM 推理”中说，该过程针对开发人员，并且“非常容易”，他将其描述为与 Cormack 的主题演讲的扩展。

“您只需写入此 API，然后编译为 Wasm，”Yuan 说。“然后，您可以将 Wasm 应用程序与运行时版本和模型版本一起打包到 Docker 镜像中。”

Yuan 说，为了实现这一点，您需要一个包含嵌入式运行时和嵌入式大型语言模型的单体应用程序。嵌入式运行时允许整个设置在不同的硬件上运行，以及在 Docker 内部的 WebGPU 上运行，以及在 Nvidia 硬件上运行（当在 Docker 上安装了适当的共享以用于语音到文本时），Yuan 说。

模型文件，包括 `tinyen.config`
和 `tinyen.mpk`
，被捆绑到 Docker 镜像中。此外，一个名为 Whisper API 服务器的运行时（用 Rust 编写并编译为 WebAssembly）也包含在同一个 Docker 镜像中。“Docker 镜像中只需要这些，”Yuan 说。

生成的 Docker 镜像如下创建：

Yuan 说，这种设计确保任何应用程序，无论是 [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/) 应用程序、Rust 应用程序还是其他应用程序，都可以与 Docker 镜像中包含的 WebAssembly API 交互。运行此应用程序提供了一个与 OpenAI 兼容的语音到文本 API 服务器，允许上传语音文档，例如 WAV 文件。目前，只支持 WAV 文件，因为 MP3 支持尚未配置，”Yuan 说。

“与 OpenAI 兼容的 API 可用于与该服务器交互，”Yuan 说。“整个 Docker 镜像，包括所有模型文件、LamaEdge 运行时以及其他所有内容，只有 90 兆字节。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)