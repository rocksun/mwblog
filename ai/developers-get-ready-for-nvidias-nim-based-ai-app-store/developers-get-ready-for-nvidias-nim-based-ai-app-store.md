
<!--
title: 开发者：为NVIDIA基于NIM的AI应用商店做好准备
cover: https://cdn.thenewstack.io/media/2024/06/f8ada841-and-machines-1cnbglqibui-unsplash.jpg
-->

NIM（NVIDIA 推理微服务）是一个虚拟化容器，用于提供 AI 功能；该技术将为 NVIDIA AI 应用商店提供支持。

> 译自 [Developers: Get Ready for NVIDIA’s NIM-Based AI App Store](https://thenewstack.io/developers-get-ready-for-nvidias-nim-based-ai-app-store/)，作者 Agam Shah。

[NVIDIA GPU](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) 现在正受到与 Apple iPhone 相同的热情欢迎。正如 iPhone 引领了移动应用开发的兴起一样，NVIDIA 也越来越多地提供开发工具来访问其 GPU 上的 [AI 应用](https://thenewstack.io/llm-app-ecosystem-whats-new-and-how-cloud-native-is-adapting/)。

同样与 Apple 一样，NVIDIA 正在寻求通过一系列软件举措来巩固其早期的 AI 硬件主导地位——包括创建 AI 应用商店。

> 通往 AI 应用市场的途径是通过 NVIDIA 的 NIM（NVIDIA 推理微服务），该服务已于本月广泛推出。

NVIDIA 的 GPU 无处不在，就像 iPhone 一样，在短期内不会消失。根据 [TechInsights 的研究](https://www.techinsights.com/blog/google-third-largest-designer-data-center-processors-2023-without-selling-single-chip)，NVIDIA 在 2023 年出货了 98% 的数据中心 GPU，其中大部分用于 AI。

NVIDIA 首席执行官黄仁勋的愿景是创建一个 AI 市场，创作者可以在其中建立自己的视频、图像、语音和文本模型，然后将这些模型融合到其他模型中。创作者可以下载 LLM 或其他 AI 模型，然后使用 Python 或其他脚本语言创建 AI 应用——然后他们可以将这些应用出售给客户。

通往这个市场的途径是通过 [NVIDIA 的 NIM](https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/)（NVIDIA 推理微服务），该公司在 3 月份的 GPU 技术大会上推出了该服务，并于本月广泛推出。

## 什么是 NIM？

> NIM 是一个虚拟化容器，通过利用 NVIDIA GPU 的部分硬件容量来提供 AI 服务。

NIM 是 NVIDIA 创建 AI 应用商店计划中的开场白，所有内容都在 NVIDIA 的芯片上运行。它是一个虚拟化容器——非常类似于基于 CPU 的[虚拟机](https://thenewstack.io/container-or-vm-how-to-choose-the-right-option-in-2023/)，用于通用应用程序——通过利用 NVIDIA GPU 的部分硬件容量来提供 AI 服务。

下载的容器可以托管预训练的专有和开源大型语言模型。它还可以使用 RAG（[检索增强生成](https://thenewstack.io/retrieval-augmented-generation-for-llms/)）来使用托管在本地文档中的知识增强下载的 AI 服务，这使公司能够创建自己的独特服务。

NIM 可以像提供有关公司服务答案的聊天机器人一样简单，也可以像实施全面的安全计划以保护 AI 数据免遭盗窃或中毒一样复杂。

## AI 市场会是什么样子？

NVIDIA 的最终目标是创建一个 AI 经济，其店面销售其数字智能商品；在这种情况下，基于 NIM。AI 资产将安全地保存在容器中，NVIDIA 为买家和卖家之间的协作和可信连接提供支持。

> 这些容器将可下载——但当然，您需要 NVIDIA 硬件。

NVIDIA 正在遵循 Apple 的蓝图。它将使用 NIM 等软件策略来销售更多硬件，并将客户锁定到其专有硬件中。

Nvidia 的高管过去曾 [传达其意图](https://www.hpcwire.com/2024/04/02/nvidia-exec-secure-ai-economies-could-help-everyone-profit/) 创建 AI 市场。

Nvidia 的 AI 软件高级总监 Erik Pounds 告诉 The New Stack：“Nvidia NIM 为企业提供了一条快速部署高效、优化的 AI 的途径。Nvidia 正在与我们广泛的合作伙伴生态系统合作，提供来自开源和企业提供商的数十个模型作为 NIM 微服务。”

Nvidia 不仅超越了自己的市场——它还将其微服务发布在合作伙伴市场上，就像它在 Hugging Face 上提供的 Llama-3 NIM 一样。

Pounds 说：“基于我们合作伙伴模型的 NIM 微服务服务于企业和医疗保健和机器人等行业的 AI 用例。”

公司将能够创建较小的专有 AI 资产，而不是支持文本、视频、语音和图像的成熟多模态模型。这些容器可以通过 API 和插件链接到其他 NIM 资产。

Trend Micro [最近宣布](https://www.darkreading.com/cloud-security/trend-micro-nvidia-partner-to-secure-ai-data-centers)将 AI 驱动的安全软件移植到 NIM，并将提供给客户。他们可以向 Trend Micro 的 AI 服务（包括实时安全分析和威胁缓解）发送 API 请求，并检索必要的信息或请求操作。

NVIDIA 从其店面向 Pegatron 提供摄像头跟踪 NIM，后者将用于工人安全。该公司还邀请客户将自己的 NIM 添加到店面。

## 开发人员需要了解的有关 NIM 的信息

开发人员可以选择自己的 NIM 容器，其中可能包括预先训练的专有和开源大语言模型，存储在构建在 Kubernetes 之上的容器中。

> 开发人员可以选择自己选择的编程工具。

例如，NVIDIA 提供了一个容器，其中包含 Meta 的 Llama-3 模型，该模型有 700 亿个参数。开发人员可以通过将自己的知识语料库从数据库添加到基础模型中来增强 NIM，并改进 AI 容器以满足特定需求。开发人员可以创建将 NIM 相互连接起来以处理数据、图像、视频和声音的工作流。

开发人员可以选择自己选择的编程工具。容器（更像一个黑匣子）包括 NVIDIA 的专有软件和 AI 框架 NeMo Retriever 以及 Triton 推理服务器。

但是不用担心，在使用 NIM 时可以使用开源。NVIDIA 堆栈还使用标准行业 API 来处理语音、文本、图像和视频。每个 NIM 都具有依赖项、驱动程序和运行时，在构建 Docker 容器时会验证对深度学习框架（如 TensorFlow 和 PyTorch）的依赖项。

例如，NIM 可以理解用于 SAP 和 ServiceNow 的语言，并从其平台中检索一些信息。NVIDIA 对 NIM 的看法是，与当今使用的 CPU 和常规查询系统相比，使用 AI 和 GPU 可以获得更快的结果。

NIM 可以协同工作，以理解来自所有数据类型的结构化和非结构化数据，以生成和交付最终结果。NVIDIA 软件堆栈从数据库中检索信息并将其转换为会话数据。

> “一旦创建，你就可以与它交谈。” – Nvidia 首席执行官 Jensen Huang

“从本质上来说，获取结构化数据或非结构化数据，了解其含义，对其含义进行编码。因此，这现在变成了一个 AI 数据库，”Huang 在 GTC 上说。“一旦创建，你就可以与它交谈。”

[向量嵌入](https://thenewstack.io/how-to-get-the-right-vector-embeddings/)帮助 NIM 使用本地数据中的信息来回答问题或检索系统上的相关文档、视频、图像或音频文件。RAG 使用基础 LLM 浏览本地文档并增强知识，这有助于它提供更准确的响应或检索相关文档。

NVIDIA 已经有一个名为 RTX 的桌面应用程序，它运行类似的功能——Mistral 模型根据用户查询对文本文档和 PC 中的相关文档进行索引。

## 开发人员应学习的其他技能

Technalysis 的分析师 Bob O’Donnell 告诉我，NVIDIA 正在尝试找到将通常在 CPU 上完成的工作负载转移到 GPU 上的方法。

> 使用 NIM 需要了解如何使用 NVIDIA 硬件。

O’Donnell 说，NIM 促进了这种转变，但人们仍在弄清楚如何使用它们，并且发现 GPU 本身可能是一个问题。

使用 NIM 需要了解如何使用 NVIDIA 硬件。了解 CUDA 有帮助，但不是必需的；NIM 与其他框架、API 和开源工具兼容。

开发人员还需要了解 AI 模型的规模。例如，一个完整的 Llama-3 70B 无法在内存不足的 NVIDIA GPU 上运行。

NVIDIA 使得无需担心 GPU，因为 CUDA 中有硬件管理工具，但了解硬件资源会有所帮助。一个脚本允许开发人员选择 GPU 并管理内存容量和其他资源。

> AI 最终将变得多模态，而 NIM 构建在解释不同数据类型之上。

AI 最终将变得多模态，而 NIM 构建在解释不同数据类型（例如图像、文本、视频和语音）之上。NIM 将通过命令行请求不同的文档、嵌入和元数据，数据以 JSON 格式发回。使用 API（提出正确的请求、进行故障排除并将接收到的信息集成到本地 AI 模型中）是开发人员必须掌握的一项关键技能。

## 如何开始使用 NIM

NVIDIA 在其 [AI 网站](https://www.nvidia.com/en-us/ai/) 上提供 1,000 个免费积分，以帮助你入门。

首先，设置一个 Nvidia 开发人员帐户，你可以使用该帐户登录 [NVIDIA 的云服务](https://ngc.nvidia.com)。从那里，从 NVIDIA 获取一个 API 密钥。

开发人员还应安装在他们的系统上安装 [NVIDIA 容器工具包](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)。

您可以从[目录](https://catalog.ngc.nvidia.com/?filters=productNames%7CNVIDIA+Microservices%7Cnvidia_nim_da&orderBy=weightPopularDESC&query=&page=&pageSize=)中选择一个 NIM。例如，您可以选择一个 [Stable Diffusion XL NIM 容器](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nim/collections/stable-diffusion-xl) 或一个 [Llama-3 70B 容器](https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama3-70b-instruct)。NVIDIA 目前共有约 24 个 NIM，未来还会增加。

命令行通常更适合下载和运行 NIM。例如，下载 Llama-3 70B 并将其在 Docker 容器中本地运行的脚本 [在此处提供](https://build.nvidia.com/explore/discover?snippet_tab=Docker#llama3-70b)。请务必输入您的 API 密钥。

用户还可以使用 Python 和 OpenAI API 设置本地 NIM 安装。该脚本建立令牌、硬件和其他运行环境的详细信息。

本地 NIM 可以连接到远程或自托管的其他 NIM，但您需要相关的 API 密钥。
