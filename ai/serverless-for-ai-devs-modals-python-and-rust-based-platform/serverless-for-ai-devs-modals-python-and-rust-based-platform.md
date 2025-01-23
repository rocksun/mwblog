
<!--
title: 面向AI开发的无服务器：Modal的基于Python和Rust的平台
cover: https://cdn.thenewstack.io/media/2025/01/66ff29cd-osarugue-igbinoba-ekkn8um6mmc-unsplash2.jpg
-->

Modal 支持 AI 推理和数据处理等计算密集型任务，正在重新定义 LLM 和 GPU 时代的无服务器架构。

> 译自 [Serverless for AI Devs: Modal's Python and Rust Based Platform](https://thenewstack.io/serverless-for-ai-devs-modals-python-and-rust-based-platform/)，作者 Richard MacManus。

[无服务器](https://thenewstack.io/serverless/) 在过去十年甚至更长时间里一直是互联网开发的趋势，但在生成式 AI 时代赋予了新的意义。[Modal](https://modal.com/) 专注于提供针对计算密集型和长时间运行的 AI、ML 和数据工作流量身定制的无服务器基础设施，而这些工作流通常对传统的无服务器解决方案来说极具挑战性。它直接面向那些不想处理大型语言模型 (LLM) 和其他 AI 基础设施的巨大计算需求的开发者。

在我们了解 Modal 提供的功能之前，让我们快速回顾一下“无服务器”的含义。“无服务器”一词[大约在 2012 年被创造出来](https://web.archive.org/web/20121017030524/http://www.readwriteweb.com/cloud/2012/10/why-the-future-of-software-and-apps-is-serverless.php)，发表在 ReadWriteWeb 文章中，但真正受到关注是在 AWS Lambda[于 2014 年底发布之后](https://thenewstack.io/serverless-on-public-cloud-the-ultimate-showdown/)。与许多 IT 术语一样，其定义随着时间的推移变得模糊，但基本上是指服务器技术[对开发者来说是抽象的](https://thenewstack.io/serverless-has-unlocked-a-new-world-of-cloud-mashups/)，通常使用云平台。当然，服务器仍然存在，但开发者无需担心配置它们——这就是无服务器提供商所做的。

Modal 采用这一概念，并将其应用于 AI 的计算密集型工作负载。该公司表示，其客户使用 Modal“用于各种用例，包括生成式 AI 推理、LLM 微调、计算生物技术和媒体处理”。

## “困难模式下的 Lambda”

在最近的一篇博客文章中，Modal 的创始工程师 Eric Zhang[将其服务称为](https://modal.com/blog/serverless-http)“困难模式下的 Lambda”。在文章中，他指出了像[AWS Lambda](https://thenewstack.io/theres-a-service-for-that-amazon-web-services-and-serverless-computing/)这样的传统无服务器函数平台的“限制”：

“AWS Lambda 上的函数运行时间限制为 15 分钟，镜像大小为 50 MB。截至 2024 年，它们只能使用 3 个 CPU（6 个线程）和 10 GB 的内存。响应带宽为 16 Mbps。”

Zhang 声称，这在当前 AI 驱动的世界中是行不通的。他指出，Modal 容器“每个可以使用多达 64 个 CPU、336 GB 的内存和 8 个 Nvidia H100 GPU”。他写道，其容器“可能是长时间运行且计算密集型的，具有大型输入和输出”，并补充说，“这与‘无服务器’通常擅长的正好相反”。

> “Modal 容器可能是长时间运行且计算密集型的，具有大型输入和输出。这与‘无服务器’通常擅长的正好相反。”
>
> – Modal 创始工程师 Eric Zhang

Zhang 在详细介绍 Modal 的 HTTP 和 WebSocket 堆栈（使无服务器函数能够接收 Web 请求）的背景下提供了此解释。有趣的是，他指出，“Rust 生态系统对于创建这种自定义网络服务至关重要，该服务需要高性能且正确”。

在 AI 工作负载的计算方面，如今大部分工作都在 GPU 上完成。Modal 从云提供商处租赁 GPU，但它通过抽象 GPU 管理的复杂性（例如配置、扩展和编排）来增加价值。Zhang 还承认 Modal 尚未运行边缘网络：

“虽然我们的无服务器函数已经根据计算可用性在许多不同的云和数据中心运行，但由于 GPU 稀缺，我们目前的服务器仅在弗吉尼亚州阿什本运行。”

## 开发者适用性

虽然 Rust 用于构建 Modal 的 HTTP 和 Websocket 基础设施，但 Python 用于服务的其余大部分功能。首席执行官 Erik Bernhardsson 最近[在 X 上指出](https://x.com/bernhardsson/status/1867969138628411683)，Modal 的后端代码库“很大一部分”仍然使用 Python，“因为它让我们能够更快地迭代”。但是，他补充说，“一旦事情稳定下来，我们需要性能时，我们将用 Rust 重写它”。

至于最终用户，Modal[仅支持 Python](https://modal.com/docs/guide)，但该公司表示“将来可能会支持其他语言”。

![](https://cdn.thenewstack.io/media/2025/01/6aa787b8-modal-playground.png)

*Modal playground.*

在[去年九月](https://www.youtube.com/watch?v=K_r-nX_y9aM)的一次采访中，Bernhardsson 指出，Modal 最初的目标用户是倾向于使用 Python 编写应用程序的“传统机器学习工程师”。但是，该公司希望扩展到其他开发者——特别是 JavaScript 开发者。
“最近涌入AI领域的……人群，实际上并非都是Python开发者，”他说道。“他们……使用JavaScript，然后意识到，哦，我可以调用OpenAI，我可以做所有这些……提示工程。我们对这部分人群的应对并不算特别好。”

## 适合哪些类型的应用程序？

关于Modal适合的应用程序类型，Bernhardsson表示，它在AI推理应用程序方面找到了强大的市场契合点。根据[Oracle的定义](https://www.oracle.com/uk/artificial-intelligence/ai-inference/#:~:text=AI%20inference%20is%20when%20an,way%20that%20mimics%20human%20abilities.)，AI推理发生在“经过训练能够识别整理数据集中的模式的AI模型开始识别它从未见过的数据中的模式时”。

最初，Bernhardsson发现推理用例令人惊讶，但后来意识到Modal的架构——专为快速启动和关闭容器而设计——非常适合此目的。他解释说：“如果你能非常快速地启动容器并关闭它们，你就可以构建这个自动扩展的推理框架。”

> “最大的挑战是……规模、稳定性和性能。”
>
> – Erik Bernhardsson，Modal首席执行官

Modal的最佳应用似乎在于它能够很好地“大规模进行推理”。Bernhardsson提到，他们的许多客户自己进行机器学习训练，然后依靠Modal进行推理工作。

当然，Modal处理大规模数据密集型工作负载的能力是客户对其青睐的重要原因。

“最大的挑战仅仅是规模、稳定性和性能，”Bernhardsson解释道。“当你大规模运行数千个GPU并处理……每秒10,000个请求时，显然你正在构建一个非常不同的产品……所以这是我们在过去几年中不得不花费大量时间去做的事情，只是为了扩展核心系统。”

## AI工程师工具箱中的另一件工具

值得注意的是，Modal可以与其他AI开发工具一起使用，例如[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)，这是一个简化构建由LLM驱动的应用程序的框架。根据[LangChain的文档](https://python.langchain.com/docs/integrations/providers/modal/)，你可以在Modal上部署一个Web端点——非常适合处理繁重的工作负载——来服务LLM模型。然后，LangChain与该端点交互，发送提示并接收LLM生成的响应以进行进一步处理。

总而言之，Modal很好地适应了无服务器模型以满足现代AI开发的需求。将无服务器抽象与计算密集型任务所需的规模相结合，可以帮助开发人员执行构建推理管道、处理大型数据集和部署基于LLM的应用程序等任务。AI工作负载的复杂性只会持续增长，因此最大限度地减少管理基础设施的开销将成为AI工程师关注的首要问题。
