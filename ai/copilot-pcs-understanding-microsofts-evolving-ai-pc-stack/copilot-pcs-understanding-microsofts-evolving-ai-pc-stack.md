
<!--
title: Copilot+PC：了解Microsoft不断发展的AI计算机堆栈
cover: https://cdn.thenewstack.io/media/2024/05/4713ebc2-microsoftpluspc.jpg
-->

数据中心因 AI 工作负载而爆满，但 PC 现已加入循环以承担一些

> 译自 [Copilot+ PCs: Understanding Microsoft's Evolving AI PC Stack](https://thenewstack.io/copilot-pcs-understanding-microsofts-evolving-ai-pc-stack/)，作者 Agam Shah。

数据中心因 AI 工作负载而爆满，但 PC 现在已加入循环，以减轻大型 GPU 安装的压力。

“AI PC”可能是一个流行语，但它也能很好地描述未来几年进入市场的全新类型的 PC。

> “即使是 PC 计算堆栈也将发生革命。”
>
> ——英伟达首席执行官黄仁勋

PC——以前仅限于为逻辑任务运行可执行文件——现在内部有一个小 AI 大脑，它可以推理和做出决策、回答问题、创建程序或改善用户体验。开发人员将编写软件，以便这些大脑吐出最佳答案。

对于用户来说，软件变得越来越大、越来越好，可以在 PC 上加载[大型语言模型](https://thenewstack.io/what-is-a-large-language-model/)，并在没有互联网连接的情况下运行 AI。

“即使是 PC 计算堆栈也将发生革命，”英伟达首席执行官黄仁勋在本月的一次财务收益电话会议上表示。

PC 已经拥有[AI 芯片](https://thenewstack.io/gpu-rich-gpu-poor-whats-new-in-the-ai-chip-boom/)，但它们大多是累赘，因为它们不符合 Microsoft 对 AI PC 的资格要求的最低要求。LLM 尚未经过微调以利用 AI PC 的低功耗优势，但这种情况正在发生改变。

“AI 不是一个芯片问题……而是一个系统问题，”黄仁勋说。

## Microsoft 的 AI PC 概念

Microsoft 在其 [Build 大会](https://thenewstack.io/microsoft-copilot-for-azure-managing-cloud-ops-through-chat/)上宣布了 Copilot+ PC 的概念。

从理论上讲，这些 PC 是在 Windows PC 的引擎盖下运行 AI 的硬件软件协同设计的早期实例。

这家软件公司正在为其希望在 AI PC 中看到的硬件定下基调，其中包括提供至少 45 TOPS（每秒万亿次操作）的专用芯片。

> “我们相信 Windows Copilot Runtime 对于 AI 来说，就像 Win32 对于图形用户界面一样。”
>
> ——Microsoft 首席执行官萨蒂亚·纳德拉

首批合格的 AI PC 是搭载高通芯片的 Copilot+ PC，它们在 Build 开发者大会的间隙宣布。

“我们正在推出 Windows Copilot Runtime，让 Windows 成为您构建 AI 应用程序的最佳平台。我们相信 Windows Copilot Runtime 对于 AI 来说，就像 Win32 对于图形用户界面一样。”纳德拉说。

Microsoft 已通过 Copilot 功能在 Windows 中引入了 AI——输入 PC 中的查询会被重定向到数据中心，数据中心会将答案输出到台式机。

该公司看到了将此类低优先级任务卸载到 PC 的机会，这可以节省带宽并释放其数据中心中的 GPU。Bing 中的 Copilot 功能在很大程度上依赖于 GPT-4 的自定义版本来回答问题。

这些 PC 包含一个 Windows Copilot 库，其中包含有助于将应用程序连接到[Copilot 堆栈](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/)的本地化 API。Microsoft 开发了 ONNX 运行时，这是一个推理运行时，受到主要芯片制造商的欢迎。

需要明确的是，搭载英伟达 RTX GPU 的 Windows PC 也可以运行本地 AI——主要用于聊天机器人和图像生成——方法是手动加载英伟达的 cuDNN 神经网络环境、加载 PyTorch 并安装 Python。但这是一个痛苦的过程，因为堆栈必须在每次重新启动时重新加载——这可能需要 10 分钟或更长时间。

Microsoft 正在使用系统库和驱动程序自动化整个过程，这些库和驱动程序将 AI 工作负载容器化。Microsoft 已经有一个名为 DirectML 的机器学习驱动程序，它更像是一个用于板载机器学习的 DirectX。

## 本地 Copilot

Microsoft 还了解到，AI 已发展到扩展到一系列大型语言模型，这些模型在数学、编码和推理方面的得分不同。有些人可能希望使用其他[开源模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)，而不依赖于 Microsoft 的堆栈。

Microsoft 引入了一个大型语言模型库，开发人员可以在 Windows 11 PC 上安装和加载该库。

“我们提供了 40 多个开箱即用的模型……我们专门设计这些模型在 Copilot+ PC 上本地运行您的输入，从而将闪电般快速的本地推理带到设备上。”纳德拉说。

> Microsoft 的 Copilot+ 集成了 RAG（检索增强生成）技术，以提供更准确的答案。

纳德拉说，自助服务模型包括 Phi Silica，这是 Microsoft 开源 Phi-3-mini LLM 的 38 亿参数版本，“我们专门设计它在 Copilot+ PC 上本地运行您的输入”。PC 上的 Phi Silica LLM 允许 Microsoft 将一些 Copilot 提示从云中的 GPU 中卸载。

Microsoft 的 Copilot+ 集成了 RAG（[检索增强生成](https://thenewstack.io/retrieval-augmented-generation-for-llms/)）技术提供更准确的答案。在这种情况下，响应还依赖于从外部来源提供的数据，例如 PC 信息。这有助于提供更准确的答案，而不是完全依赖于几个月前从互联网上抓取的信息的 LLM。

微软表示，它将提供工具将各种输入提供给其 AI 堆栈，确保开发人员在编写可以在板载 PC 上处理的 AI 应用程序时可以使用图像、语音、视频和文本。微软已为 [向量嵌入](https://thenewstack.io/comparing-different-vector-embeddings/) 做出规定，以确保不同类型的数据可以轻松关联并集成到 AI 功能中。

Windows App SDK 1.6 Experimental 2 具有许多 API，可用于运行聊天机器人、进行计算或解决问题。这些 API 可以连接到应用程序并集成到用户界面中。

在 Build 上，微软还宣布了对 PyTorch 的原生 Windows 支持——这是使用该框架制作的 LLM 的必要条件。现在，用户不必每次在 PC 上加载 LLM 时都经历安装 PyTorch 的繁琐过程。

纳德拉说：“原生 PyTorch 支持意味着数千个 OSS 模型将在 Windows 上开箱即用，让您轻松上手。事实上，借助 WebNN，Web 开发人员终于拥有了一个原生 Web 机器学习框架，让他们可以直接访问 GPU 和 NPU。”

## 设备和芯片制造商

设备上的 AI 只能与硬件一样快，而这些 LLM 是为设备上的 NPU 设计的。谷歌在其 IO 贸易展上 [分享了详细信息](https://thenewstack.io/google-wants-developers-to-build-on-device-ai-applications/)，介绍了开发人员如何编写在智能手机上本地运行的 AI 应用程序。

> 高通是第一个为搭载骁龙精英芯片的 CoPilot+ 推向市场的公司。

去年，英特尔发布了其 [最新一代 x86 芯片](https://thenewstack.io/intels-generational-on-chip-change-apx-will-make-all-the-apps-faster/)，称为 Meteor Lake，它有一个峰值达到 10 TOPS 的 NPU。不幸的是，它不符合 Windows 最低 45 TOPS 的要求，因此无法称为 Windows AI PC，也称为 CoPilot+ PC。

高通是第一个为搭载骁龙精英芯片的 CoPilot+ 推向市场的公司，其 NPU 超过 45 TOPS。所有主要 PC 制造商——包括戴尔、惠普、华硕和联想——都宣布了搭载 AI 芯片的 PC。

高通还推出了自己的 AI Hub 作为开发人员工具的资源。它提供了一个可以通过一些典型的命令行提示安装的 IDE，还提供了一个用于应用程序集成的 API 令牌。

> 英特尔正在加快其下一代 PC 芯片 Lunar Lake 的开发。
 
开发人员将能够下载 LLM 进行测试。API 令牌通常意味着开发人员将能够将 LLM 集成到第三方应用程序中，正如微软在其将 Copilot 引入应用程序的计划中所概述的那样。

英特尔正在加快其下一代 PC 芯片 Lunar Lake 的开发，该公司声称该芯片将满足 AI PC 的最低要求，配备 45 TOPS NPU，并可能通过 GPU 超过 100 TOPS。预计 Lunar Lake 芯片将在几个月内推出。

英特尔还有自己的开发环境 OneAPI，但使用起来很复杂。英特尔提供了一个在 GIMP 中加载 Stability Diffusion AI 以生成图像的示例，但这是一个复杂的过程，涉及安装 OpenVino、运行命令行安装和进一步微调。

英特尔还通过其 Tiber Developer Cloud 服务提供 Jupyter 笔记本，以在其各种芯片上试用 AI，这可能是一个更安全的赌注。但 AI PC 芯片的云版本尚未推出。
