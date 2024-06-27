# PyTorch、Docker 和 AI 开放性成为 AI_dev Europe 的亮点

![PyTorch、Docker 和 AI 开放性成为 AI_dev Europe 的亮点的特色图片](https://cdn.thenewstack.io/media/2024/06/d5cec598-nahrizul-kadri-oasf0qmrwla-unsplash-1024x578.jpg)

巴黎——[PyTorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/) 的联合创始人上周告诉开源 AI 开发人员，该项目曾考虑在 AI 框架和包括 [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) 和 [JavaScript](https://thenewstack.io/top-10-javascript-libraries-to-use-in-2024/) 在内的语言之间进行更紧密的集成，但最终决定放弃。

[Soumith Chintala](https://www.linkedin.com/in/soumith/) 在 [Linux 基金会 AI dev 大会](https://events.linuxfoundation.org/ai-dev-europe/) 的炉边谈话中发表了讲话，他在讲话中概述了该框架背后的理念。“PyTorch 就像典型的黑客，他们会采取任何捷径来为用户提供良好的性能。我们非常务实。”

当被问及 PyTorch 的未来路线图时，他说：“工具必须发展，但它们不必频繁发展。”

谈到 AI 领域，他说：“我认为我们每六到七年就会看到新的工具出现。” 因此，“我甚至不希望 PyTorch 在短期内需要考虑 2.0 版本。但我们一直在观察，形势一直在变化。”

在 [ChatGPT](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/) 发布后，他说，Transformer 已经成为进行 AI 的主要方法，也许“这是我们需要认真考虑的事情。但总的来说，我们仍然很满意。”

## 与其他语言集成？
有一件事很明显不在议程上，那就是与除 Python 之外的其他语言进行更紧密的集成。

针对观众提出的问题，“我们是否会拥有适用于 Rust 或 JavaScript 的 PyTorch？” 他的回答是“PyTorch 中有一个‘Py’，所以，官方来说，没有。”

Chintala 补充说，团队已经考虑过这个问题。但他继续说，问题总是出现在编译器上。“你必须解析前端代码，编写一个用于各种语言的、消耗用户代码的前端是一个很大的工作量。

“因此，从优先级和研究的角度来看，我们决定不这样做，但我们实际上并不反感 Rust 或 JavaScript。”

## Docker 和 WebGPU
在活动的其他地方，[Docker](https://www.docker.com/?utm_content=inline+mention) 宣布它正在预览对 [WebGPU](https://thenewstack.io/google-talks-web-platform-os-integration-webgpu-and-more/) 的支持，从而无需专门为每个 GPU 供应商的专有驱动程序构建 [Docker 镜像](https://thenewstack.io/the-case-for-environment-specific-docker-images/)。

Docker 位于英国的 CTO [Justin Cormack](https://www.linkedin.com/in/justincormack/?originalSubdomain=uk) 表示，当该公司成立时，开发人员的硬件环境“非常统一。你几乎可以将你的笔记本电脑运送到生产环境。”

但他继续说，AI 爆发及其对 [GPU](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) 的依赖改变了这一点。“我们看到各种各样的加速器在开发人员机器、边缘机器和生产环境中广泛使用，”Cormack 补充道。“有非常非常多的东西。”

他说，这使得“硬件变得非常有趣”，但不可避免地，开发人员“会向我们询问 GPU 使用情况”。理想的情况是，Docker 中有一个可移植的抽象，它在任何地方都可用。他说，答案以 WebGPU 的形式出现，WebGPU 是 [万维网联盟 (W3C)](https://www.w3.org/) 支持的用于在 GPU 上执行操作的 API。

“WebGPU 出现时，它已经存在，并且已经出现在大多数浏览器中，包括所有消费级 GPU 和移动设备，并且它拥有一个生态系统。” 但他补充说，它不仅在浏览器中工作，因为它具有可以移植使用的标准定义，并且作为与 [WebGL](https://get.webgl.org/) 相比的高性能现代堆栈。

Cormack 表示，它正在 [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) 中以预览形式发布 WebGPU 支持，但将来也会将其提供给 Docker Engine 和其他平台。

“我们正在努力的是真正提供包含多个后端的容器镜像，”Cormack 告诉 The New Stack。

首先，这应该让开发人员的生活更轻松，因为他们可能对开发机器中的 GPU 几乎没有选择权。但最终，它可以使应用程序投入生产时更加顺畅。

“我们下一步是展示这条路径是什么样子的，”他说。“因此，你拥有这些预先构建的模型，它们既可以在本地运行，也可以在生产环境中运行。”

## 提高访问权限和开放性
Cormack 表示，该公司也在研究如何与 [Llama](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/) 模型合作：“我们非常高兴能与这些更广泛的社区合作，为所有在不同环境中进行开发和边缘工作的人提供更多 GPU 访问权限，并提高生态系统的可负担性和易用性。”

虽然此次大会强调了开源 AI 的潜力，无论是在增加对 AI 技术的访问方面，还是在为可能被大型科技公司主导的市场带来透明度方面，但也表达了对“[开源洗白](https://thenewstack.io/calls-to-ban-open-source-are-misguided-and-dangerous/)”的担忧。

Linux 基金会 AI 和数据基金会执行董事 [Ibrahim Haddad](https://www.linkedin.com/in/ibrahimhaddad/) 推出了一个工具，允许 AI 模型制造商——以及最终用户——评估模型的真实开放程度。

[isitopen.AI](https://isitopen.ai/) 网站基于该基金会开发的 [模型开放框架](https://arxiv.org/abs/2403.13784?ref=thestack.technology)。该框架将模型分解为 17 个不同的组件，涵盖代码、工具、数据和文档。

模型被分为三类。

**第一类 - 开放科学**涵盖所有组件，所有工件都已发布，包括训练数据集。这使得模型完全可复制。**第二类 - 开放工具**涵盖完整的代码套件，以及关键数据集。- 最底层，
**第三类 - 开放模型**意味着模型的核心，包括架构、参数和基本文档，是在开放许可下发布的。
Haddad 表示，与传统代码相比，AI 的复杂性意味着难以维持对开放性的二元方法，但拥有透明度的滑动尺度总比没有好。

更实际地说，该工具和框架意味着希望使用模型的开发人员和公司将确切地知道给定模型如何与他们自己的框架或内部流程相匹配。这也意味着模型开发人员将更清楚地了解自己的状态——并且不会使用不合适的许可证。值得注意的是，到目前为止，分析过的模型中没有一个达到高于第三类状态的水平。

[YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)