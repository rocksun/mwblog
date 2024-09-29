
<!--
title: 语义路由器及其在设计代理工作流中的作用
cover: https://cdn.thenewstack.io/media/2024/09/51ea8e88-arrow.jpg
-->

语义路由器是一种模式，它使 AI 代理能够为不同的任务选择合适的 LLM，同时减少对 LLM 的依赖。

> 译自 [Semantic Router and Its Role in Designing Agentic Workflows](https://thenewstack.io/semantic-router-and-its-role-in-designing-agentic-workflows/)，作者 Janakiram MSV。

新兴的[代理](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) 工作流模式严重依赖于 LLM 来执行推理和决策。每个代理在任务执行期间多次调用 LLM。对于包含多个代理的工作流，调用次数呈指数级增长，导致成本和延迟都增加。

有各种具有不同功能和能力的语言模型，例如[小型语言模型](https://thenewstack.io/how-to-get-started-running-small-language-models-at-the-edge/)、[多模态模型](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) 和专门构建的[特定任务模型](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/)。代理可以使用这些模型来完成工作流。这会导致成本和延迟*降低*，以及整体准确性的提高。

**语义路由器**是一种模式，它使代理能够为正确的任务选择正确的语言模型，同时通过本地决策减少对模型的依赖。在幕后，语义路由器使用存储在向量数据库中的嵌入来将提示与一组现有短语（也称为话语）进行匹配，以将它们映射到特定路由。该路由可以是适合该任务的 LLM。由于语义搜索决定了目标，因此我们将其称为语义路由器。

![](https://cdn.thenewstack.io/media/2024/09/27123e4f-sr-1-1024x382.jpg)

语义路由器使用与 RAG 管道中检索器相同的技术来执行语义搜索以找到正确的匹配。但它不是返回文本块，而是根据输入返回单个预定义路由。

虽然在技术上可以在代理和 LLM 之间实现语义路由器作为自定义层，但开源语义路由器项目正在越来越受欢迎。

## 语义路由器项目的概述

[Aurelio AI](https://www.aurelio.ai/) 开发了[语义路由器](https://github.com/aurelio-labs/semantic-router)，这是一种创新的开源工具，它改变了基于 AI 的代理中的决策过程。此层通过利用语义向量空间更有效地路由请求来增强 LLM 和代理的功能。与依赖于缓慢的 LLM 生成来进行工具使用决策的传统方法不同，语义路由器利用语义含义的力量来做出快速准确的选择。

该项目提供与各种嵌入模型的无缝集成，包括流行的选项，如[Cohere](https://cohere.com/embed) 和[OpenAI](https://platform.openai.com/docs/guides/embeddings)，以及通过[HuggingFace Encoders](https://huggingface.co/docs/tokenizers/en/api/encoding) 对开源模型的支持。该项目利用内部内存向量数据库，但主流向量数据库引擎，如[Pinecone](https://www.pinecone.io/) 和[Qdrant](https://qdrant.tech/) 可以轻松地替换它。语义路由器根据用户查询做出决策的能力显着减少了处理时间，通常从 5000 毫秒减少到仅 100 毫秒。

语义路由器采用 MIT 许可证，具有可扩展性，允许开发人员将其自由地集成到他们的项目中。该工具解决了 AI 开发中的关键挑战，包括安全性、可扩展性和速度，使其成为创建更高效、更具响应性的代理工作流的宝贵资产。

## 语义路由器的关键组件

**路由和话语**

路由是语义路由器决策过程的支柱。每个路由代表一个潜在的决策或操作，并由一组话语定义，这些话语是映射到特定路由的示例输入。系统将这些话语馈送到每个路由的语义配置文件中。我们将新的输入与这些话语进行比较，以找到最接近的匹配。

在实践中，这允许系统根据输入的语义含义对输入进行分类和响应，而不是依赖于 LLM 生成，而 LLM 生成可能很慢或容易出错。开发人员可以自定义路由以适应特定应用程序，无论是过滤敏感主题、[管理 API](https://thenewstack.io/api-management/) 还是在复杂工作流中编排工具。

**编码器和向量空间**

为了将输入与预定义的话语进行比较，语义路由器使用编码器将文本转换为高维向量。这些向量驻留在语义空间中，向量之间的距离反映了相应文本的语义相似性。距离越短，输入的语义相关性就越高。

语义路由器支持多种编码方法，包括用于高性能 API 驱动的 Cohere 和 OpenAI 编码器，以及用于寻求开源、本地可执行替代方案的 Hugging Face 模型。选择不同编码器的灵活性使开发人员能够根据其特定基础设施定制系统，平衡性能、成本和隐私问题。

**决策层**

一旦输入被编码并与预定义的路由进行比较，语义路由器就会使用 RouteLayers 进行决策。此层聚合路由和嵌入，并管理决策过程。它还支持混合路由，系统可以结合本地和云模型来优化性能。

**本地 LLM 集成**

对于希望完全控制其 LLM 或减少对外部 API 依赖的开发人员，语义路由器通过 LlamaCPP 和 Hugging Face 模型提供对本地模型的支持。消费级硬件，例如运行 Apple Metal 硬件加速的 MacBook 或 [Microsoft Copilot+ PC](https://thenewstack.io/copilot-pcs-understanding-microsofts-evolving-ai-pc-stack/)，可以完全执行路由决策和 LLM 驱动的响应。这种本地执行模型不仅减少了延迟和成本，而且还提高了隐私和安全性。

**可扩展性**

当向工作流程添加更多工具和代理时，可扩展性成为一个问题。LLM 的上下文窗口有限，这意味着它们难以处理大量数据或上下文。语义路由器通过将决策与 LLM 解耦来解决这个问题，使其能够同时处理数千个工具，而不会使系统过载。这种关注点的分离使代理能够扩展，而不会牺牲性能或准确性。

## 使用案例和场景

需要同时管理多个工具、API 或数据集的代理 AI 使用案例特别适合语义路由器。在典型的工作流程中，路由器可以根据输入快速确定使用哪个工具或 API，从而避免进行完整的 LLM 查询。这在虚拟助手系统、内容生成工作流程和大型数据处理管道中特别有用。

例如，在虚拟助手系统中，语义路由器可以有效地将诸如“安排会议”或“查看天气”之类的提示路由到相应的 API 或工具，而无需在每次决策时都涉及 LLM。类似地，请求可以路由到一个经过微调的 LLM，该 LLM 旨在响应医疗或法律术语。这不仅减少了延迟，而且还确保了用户体验的一致性和可靠性。

语义路由器可用于评估提示是否应直接发送到本地运行的小型语言模型，或者是否必须通过调用云中运行的强大 LLM 来将其映射到函数及其参数。这在 [联合语言模型](https://thenewstack.io/federated-language-models-slms-at-the-edge-plus-cloud-llms/) 的实现中尤其重要，这些模型利用了基于云的和本地语言模型。

![](https://cdn.thenewstack.io/media/2024/09/94f5be50-sr-2-1024x697.jpg)

在代理工作流程时代，对高效、可扩展和确定性决策系统的需求比以往任何时候都更加迫切。语义路由器通过利用语义向量空间的力量来做出快速、可靠的决策，同时仍然允许在需要时与 LLM 集成，提供了一个强大的解决方案。它的灵活性、速度和确定性使其成为开发人员构建下一代 AI 系统的必不可少的工具。

随着 LLM 的发展和多样化，像语义路由器这样的工具对于确保代理系统能够执行、扩展并提供一致的结果至关重要。这将帮助开发人员找到在工作流程中使用 AI 的新方法。

在本系列的下一部分，我将引导您完成基于语义路由器实现 RAG 代理的步骤。敬请关注。
