# 开发者指南：NVIDIA 的 AI 应用平台 NIM

![特色图片：开发者指南：NVIDIA 的 AI 应用平台 NIM](https://cdn.thenewstack.io/media/2024/08/d2fa3e65-getty-images-mydwapzss_k-unsplash-1024x767.jpg)

2024 年 3 月，NVIDIA [宣布](https://developer.Nvidia.com/blog/Nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/) 推出 NIM（NVIDIA 推理微服务），这是一套易于使用的 [微服务](https://thenewstack.io/microservices/)，旨在加速生成式 AI 模型在云、数据中心和工作站上的部署。

本系列深入探讨 NIM，探索其关键功能、优势和应用，并为希望利用此生成式 AI 平台的开发者提供全面指南。

NIM 可作为 API、NVIDIA AI Enterprise 软件套件的一部分以及独立容器镜像提供。

## 什么是 NVIDIA NIM？

NIM 代表 NVIDIA 推理微服务，这意味着它是一种用于对生成式 AI 模型进行推理的服务。在宣布推出时，NIM 仅作为 [一套面向开发者的 API](https://thenewstack.io/developers-get-ready-for-nvidias-nim-based-ai-app-store/) 提供。NIM 也是 NVIDIA AI Enterprise 的一部分，该平台建立在 [VMware](https://tanzu.vmware.com?utm_content=inline+mention) 和 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的基础设施软件之上。最近，NVIDIA 开始发布和维护容器镜像，这些镜像可以在配备 NVIDIA GPU 的开发者工作站和服务器上本地部署。

因此，NIM 可作为 API、[NVIDIA AI Enterprise 软件套件](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/) 的一部分 *以及* 独立容器镜像提供。

让我们分别看一下这些内容，以便更好地理解它们。

## NVIDIA NIM API

[NVIDIA NIM API](https://build.Nvidia.com/explore/discover) 是一套行业标准 API，使开发者能够轻松地部署 AI 模型，只需几行代码即可。NIM API 作为无服务器推理端点提供，为迭代和构建生成式 AI 解决方案提供了一条安全、简化的路径。

NIM API 建立在强大的基础之上，包括 [Triton 推理服务器](https://developer.Nvidia.com/triton-inference-server)、[TensorRT](https://developer.Nvidia.com/tensorrt-getting-started)、[TensorRT-LLM](https://docs.Nvidia.com/tensorrt-llm/index.html) 和 [PyTorch](https://pytorch.org/) 等推理引擎。这种架构促进了大规模的无缝 AI 推理，使开发者能够使用最先进的基础模型和微调模型，而无需担心基础设施。

NIM API 与 OpenAI 兼容，使开发者能够在其应用程序中利用 OpenAI 模型和工具的强大功能。开发者可以使用标准 HTTP REST 客户端或 OpenAI 客户端库来使用 NIM API。

NIM API 提供了多个 API 端点，使开发者能够与 AI 模型进行交互，包括：

* **完成端点**: 这使开发者能够根据给定的提示生成文本完成。
* **嵌入端点**: 这使开发者能够为给定的输入文本生成文本嵌入。
* **检索端点**: 这使开发者能够根据给定的查询检索相关文档。
* **排名端点**: 这使开发者能够根据给定的查询或提示对段落或文档列表进行排名。

NIM API 与流行的 LLM 编排工具（如 LangChain 和 LlamaIndex）紧密集成。开发者可以轻松地构建基本的聊天机器人、AI 助手、检索增强生成 (RAG) 应用程序和基于代理的更高级应用程序。

开发者可以通过访问 NVIDIA API 目录来开始使用 NIM API，在那里他们可以找到文档、API 参考信息和发行说明。要使用 NIM API，开发者需要获取 API 密钥，可以通过加入 NVIDIA 开发者计划获得。有一个游乐场可以探索模型、提示、参数和响应。当开发者注册 NIM 时，他们每个人都会收到 5,000 个积分，每个积分对应一次推理调用。

NVIDIA NIM 正在迅速成为开发者访问最新生成式 AI 模型的首选。最近，当 [Google](https://cloud.google.com/?utm_content=inline+mention) [推出](https://developers.googleblog.com/en/smaller-safer-more-transparent-advancing-responsible-ai-with-gemma/) Gemma 2 2B LLM 时，它与 Hugging Face 和 Kaggle 一起在 NIM 上提供了该模型。展望未来，您可以期待其他模型提供商在其 NVIDIA NIM 推理平台上提供其模型。

我将在本系列的后续教程中详细探讨 NIM API。

## NVIDIA AI Enterprise 中的 NVIDIA NIM
[英伟达 AI 企业版](https://www.Nvidia.com/en-in/data-center/products/ai-enterprise/) 是一个全面的、云原生软件平台，它可以加速数据科学管道，简化生产级副驾驶和其他生成式 AI 应用程序的开发和部署。作为该平台的一部分，英伟达 NIM 是一套易于使用的推理微服务，使开发人员能够在任何云或数据中心部署基础模型，同时保持其数据安全。

英伟达 AI 平台的软件层，英伟达 AI 企业版，加速了数据科学管道，简化了生产 AI 的开发和部署——包括生成式 AI、计算机视觉、语音 AI 等。凭借超过 100 个框架、预训练模型、开发工具和微服务，英伟达 AI 企业版旨在加速企业迈向 AI 的领先地位，同时简化 AI，使其对每家企业都触手可及。

英伟达 NIM 是英伟达 AI 企业版平台的关键组成部分，它提供优化的模型性能，并具有企业级安全、支持和稳定性。借助 NIM，开发人员可以使用几行代码轻松部署 AI 模型。这使他们能够专注于构建企业应用程序，而英伟达则处理 AI 模型部署的复杂性。

英伟达 AI 企业版平台可以部署在英伟达 DGX、英伟达合作伙伴认证的硬件以及公共云环境（如 [AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Azure](https://news.microsoft.com/?utm_content=inline+mention) 和 GCP）等系统上。

## 英伟达 NIM 作为自托管容器
对于无法访问英伟达 AI 企业版的开发人员，NIM 可作为自包含镜像提供，可以使用 [Docker](https://www.docker.com/?utm_content=inline+mention) 或 [Kubernetes](https://roadmap.sh/kubernetes) 部署。

NIM 抽象了模型推理内部，包括运行时操作和执行引擎。它们也是最有效的选项，无论它们是与 [TRT-LLM](https://github.com/Nvidia/TensorRT-LLM)、[vLLM](https://docs.vllm.ai/en/latest/) 还是类似的推理引擎一起使用。

NIM 被打包为每个模型或模型系列的容器镜像。每个 NIM 都是一个独立的 Docker 容器，包含一个特定模型，例如 `meta/llama3-8b-instruct`。这些容器附带一个运行时，可以在任何具有足够内存的英伟达 GPU 上运行，但某些模型/GPU 组合比其他组合效果更好。利用任何可用的本地文件系统缓存，NIM 会自动从英伟达的 NGC 目录下载模型。由于每个 NIM 都基于相同的基镜像构建，因此下载其他 NIM 非常快。

要开始使用英伟达 NIM，请从英伟达 Docker 仓库中拉取 NIM 容器，并在配置了 Docker 和英伟达容器工具包的 GPU 机器上使用 `docker run` 命令运行它。要访问 NIM API，请从英伟达 GPU 云生成 API 密钥，并使用 `docker login` 命令对英伟达容器仓库进行身份验证。最后，使用 `docker run` 命令启动 NIM 容器，指定容器名称、仓库和标签。

容器运行后，您可以使用 `curl` 命令执行推理请求来验证部署。此外，您可以使用 OpenAI Python API 库向 NIM API 发送请求。通过遵循这些步骤，您可以轻松地在系统上部署和使用英伟达 NIM。

首次部署 NIM 时，它会检查本地硬件配置和模型注册表中可用的优化模型，然后自动为可用硬件选择最佳模型版本。NIM 下载优化的 TensorRT (TRT) 引擎，并在支持的 GPU 子集上使用 TRT-LLM 库运行推理。对于其他 GPU，NIM 会下载未优化的模型，并使用 vLLM 库运行它。

通过通过 API 提供灵活的微服务套件、与英伟达 AI 企业版的集成以及自托管容器镜像，NIM 为开发人员提供了一个强大、可扩展且安全的 AI 推理平台。

我喜欢 NIM 容器的一点是，它们能够在消费级 GPU（如 [GeForce RTX 4090](https://www.Nvidia.com/en-in/geforce/graphics-cards/40-series/rtx-4090/)）上运行，使开发人员有机会在可访问且价格合理的硬件上快速原型化应用程序。在本系列的后续部分，我将探讨如何在本地部署 NIM 以及构建使用 API 的应用程序。

## 总结
Nvidia NIM represents a significant advancement in the deployment and utilization of generative AI models. By providing a flexible suite of microservices via APIs, integration with Nvidia AI Enterprise, and self-hosted container images, NIM offers developers a powerful, scalable, and secure AI inference platform. Whether leveraging cloud infrastructure or on-premises GPU resources, NIM simplifies the complexities of AI model deployment, enabling rapid development and iteration of AI applications. As I continue this series, I will delve deeper into various aspects of Nvidia NIM, providing detailed guides and tutorials to help developers maximize the potential of this powerful platform.

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 
Technology is moving fast, don't miss a beat. Subscribe to our YouTube channel to watch all our podcasts, interviews, demos, and more.