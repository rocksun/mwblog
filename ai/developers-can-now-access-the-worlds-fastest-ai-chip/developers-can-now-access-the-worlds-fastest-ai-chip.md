
<!--
title: 开发者现在可以访问世界上最快的AI芯片
cover: https://cdn.thenewstack.io/media/2024/08/df525111-getty-images-hch5fqzxshc-unsplash.jpg
-->

Cerebras——英伟达的芯片竞争对手——推出了一个AI云服务，据称其速度比普通云提供商快10到20倍。

> 译自 [Developers Can Now Access the World's Fastest AI Chip](https://thenewstack.io/developers-can-now-access-the-worlds-fastest-ai-chip/)，作者 Agam Shah。

AI 计算仍然处于拨号上网的水平。从 LLM 获取答案可能很慢。但现在，芯片制造商 Cerebras 推出了一个 AI 云服务，它声称比普通云提供商快 10 到 20 倍。

这项名为 [Cerebras 推理](https://inference.cerebras.ai/) 的服务提供了对世界上最大、最快的 AI 芯片的访问权限，该芯片轻松超越了单个或多个 Nvidia GPU 的组合。

Cerebras 的 WSE-3 AI 芯片尺寸约为 46,225 平方毫米，是 Nvidia H100 GPU 的 56 倍。Cerebras 在其数据中心中组装了这些大型 AI 芯片。

该公司还欢迎开发者使用免费的 API 密钥在其上构建 AI 应用程序，尽管可用的自定义选项非常有限。该服务上可用的模型包括 Llama 3.1 及其 80 亿和 700 亿参数变体。

即将推出的模型包括具有 4050 亿参数的 Llama 3.1、Mistral 的 Large 2，该模型具有 1230 亿参数，于一个月前 [宣布](https://mistral.ai/news/mistral-large-2407/)，以及 Cohere 的 [Command R](https://cohere.com/command)。

## 数字背后的故事

根据 [Artificial Analysis](https://artificialanalysis.ai/models/llama-3-1-instruct-8b/providers) 上的独立基准测试，Cerebras 芯片对具有 80 亿参数的 Llama 3.1 的响应时间为每秒 1,842 个 token 。

在相同的 LLM 上，微软 Azure 的输出速度为每秒 51.5 个 token ，亚马逊为 92.2 个 token 。这使得 Cerebras 比主要云提供商快 20 倍。

> “我们的大多数用户是推理应用程序开发者，他们只想在开源模型的堆栈之上进行构建。”
>
> – Andy Hock，Cerebras Systems

数字会随着更大的上下文大小和 LLM 大小而变化，这些大小对内存和数据要求很高。

开发者可以控制开发的前端，但不能在后端进行太多操作，例如自定义模型或控制硬件。

“我们的大多数用户是 […] 推理应用程序开发者，他们只想在 [开源] 模型的堆栈之上进行构建，”Cerebras Systems 产品管理副总裁 Andy Hock 在接受 The New Stack 采访时表示。

## 开发者需要了解什么

与 Cerebras 兼容的模型本身是用标准 Pytorch 编写的。

开发者将获得一个免费的 API 密钥，并且可以轻松地将聊天机器人或其他 AI 应用程序迁移到 Cerebras 的推理云服务。

例如，开发者可以通过交换 API 密钥并将指向从 OpenAI 指向 Cerebras 的云服务来更改一行代码。只需更改一两行代码即可。

> Cerebras 用户可以使用个性化数据构建 RAG 或自定义模型。

“因此，他们只是在等待并准备接收您的传入 API 调用，将数据扔到晶圆上的权重上，并生成答案，”Hock 说。

“如果他们想运行一些不是 Llama 8B、不是 Llama 70B 的东西……他们可以与我们合作构建和部署它，”Hock 说。

客户可以使用个性化数据构建 RAG 或自定义模型。这将需要安装 Ollama 并创建本地向量数据库。使用 Pinecone 和 Docker 的示例在 [此处](https://github.com/Cerebras/inference-examples/tree/main/rag-pinecone-docker) 中概述，而 Weaviate 和 Hugging Face 的示例在 [此处](https://rag-weaviate-cerebras.streamlit.app/) 中概述。您可以查看 [其他示例](https://inference-docs.cerebras.ai/examples)，此外，Cerebras 推理平台还与 OpenAI 客户端库 [兼容](https://inference-docs.cerebras.ai/openai)。

该公司表示正在讨论“简单按钮”和定制功能。但 Hock 说，首要任务是让服务正常运行，以便开发者能够访问这些芯片。

“在接下来的 60 天里，我们将从市场中了解很多关于这种新型性能的信息。我们有一些非常令人兴奋的合作伙伴关系和应用程序项目即将到来，”他补充道。

## 定价

与云提供商相比，Cerebras 的推理并不便宜。但与 CPU 和 GPU 一样，您必须为性能付费。

好消息是：API 是免费的。

Llama 3.1-8b 的免费层（速度为每秒 1,800 个 token ）的每日 token 限制为 100 万个，每分钟 30 个请求。付费层每 100 万个输入或输出 token 收取 10 美分，请求数量不限。

Llama 3.1-70B 的免费层（速度为每秒 450 个 token ）的每日 token 限制为 100 万个，30 个请求。付费层每分钟每 100 万个输入或输出 token 收取 60 美分。

Cerebras 还为想要运行自定义模型的用户提供企业模型。
谷歌和 OpenAI 最近一直在提高使用 API 访问 LLM 的客户的价格——这激怒了那些使用谷歌 AI 工具构建应用程序的客户。同样，Cerebras 推理的价格可能会随着其走出实验阶段而上涨。Cerebras 的芯片制造成本很高，它需要收回资金来建立其云基础设施。

## 范围

Cerebras 的 AI 速度为代理（或代理）建模打开了大门，其中单个提示被分散并发送到许多不同的模型。这些模型会对其进行审查、分析并生成结果，这些结果会传播到其他模型中，然后汇总回来。

> “我们有合作伙伴正在构建将我们的 LLM 与多个其他模型链接起来的应用程序。”
>
> – Hock

“我们有合作伙伴正在构建将我们的 LLM 与多个其他模型链接起来的应用程序。例如，在将文本发送到我们的 LLM 推理之前进行语音到文本转换，然后输出到文本到语音模型，”Hock 说。

一旦更多模型可用，开发人员就可以在 Cerebras 云上执行此操作。

“作为开发人员，您可以完全灵活地将我们的 LLM 推理有效地串联到多模态工作流程中，”Hock 说。

目前还没有简单的按钮功能可以做到这一点。开发人员将不得不为这种工作流程定制不同模型的脚本。

## 幕后

Cerebras 能够实现如此显著的速度提升是有原因的。

该芯片比单个英伟达 GPU 大 57 倍。在生产中，单个英伟达的 H100 GPU 从一块大晶圆上切割下来。相反，Cerebras 将其整个芯片放在了一块晶圆上。

> “我们正在组装的东西是 GPU 无法实现的。”
>
> – Cerebras 首席执行官 Andrew Feldman

4 万亿晶体管芯片的巨大尺寸和晶圆工程使其具有性能优势。Cerebras 声称它比英伟达 DGX 服务器中的 H100 芯片快 10 倍。

“我们正在组装的东西是 GPU 无法实现的，”Cerebras 首席执行官 Andrew Feldman 在新闻发布会上说。

现有的 AI 安装涉及一个复杂的互连 GPU 网络，这些 GPU 具有独立的内存单元，协同工作。处理器和集成内存之间的距离造成了瓶颈，导致速度下降。

Cerebras 将其 SRAM 内存放在了巨型芯片内部，从而解决了带宽问题。

“速度转化为质量，更强大、更相关的答案，”Feldman 说。

结果来自 16 位数据类型，它需要速度但会生成更准确的答案。许多云提供商正在将 8 位或 4 位数据类型量化，这会以牺牲质量为代价来提高速度。

## Cerebras 与英伟达

Cerebras 可能拥有更好的硬件，但它不是英伟达，英伟达的 GPU 存在于一些最强大的生成式 AI 系统中。

OpenAI 和微软已经构建了自己的硬件，而谷歌的 AI 系统依赖于 TPU。英伟达将在今年年底发布下一代 Blackwell。大多数专有和开源大型语言模型已经针对在 GPU 上运行进行了调整。

Cerebras 没有软件生态系统，该生态系统围绕 Llama 和 Mistral 等开源 AI 模型构建。开发人员将是帮助该公司推理服务取得成功的关键，并且它为开发人员提供了 Discord 和 Slack 频道。

也就是说，Cerebras 的芯片在高性能计算和 AI 训练领域表现出色。它还与中东最大的数据中心提供商 G42 合作，在美国建立 AI 数据中心。
