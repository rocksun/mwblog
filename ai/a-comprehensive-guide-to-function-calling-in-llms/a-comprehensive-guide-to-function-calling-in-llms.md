
<!--
title: LLM函数调用指南
cover: https://cdn.thenewstack.io/media/2024/05/0d3fe93b-allison-saeng-rv7vwjki4fg-unsplash.jpg
-->

深入了解 LLM 中的函数调用，以及我们适合函数调用的商业和开源 LLM 列表。

> 译自 [A Comprehensive Guide to Function Calling in LLMs](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/)，作者 Janakiram MSV。

减少大型语言模型中幻觉的已验证技术之一是 [检索增强生成](https://thenewstack.io/retrieval-augmented-generation-for-llms/)，或 RAG。RAG 使用检索器搜索外部数据，在将提示发送到生成器（即 LLM）之前，使用上下文对提示进行增强。

虽然 RAG 是最流行的方法，但它最适合从已编入索引并存储在 [向量数据库](https://thenewstack.io/vector-databases-long-term-memory-for-artificial-intelligence/) 中的非结构化数据构建上下文。在 RAG 检索上下文之前，一个批处理过程会将非结构化数据转换为文本嵌入，并将其存储在向量数据库中。这使得 RAG 在处理不常更改的数据时非常理想。

当应用程序需要实时数据的上下文（例如股票报价、订单跟踪、航班状态或库存管理）时，它们依赖于 LLM 的函数调用功能。RAG 和函数调用的目标都是用上下文补充提示——无论是来自现有数据源还是实时 API——以便 LLM 能够访问准确的信息。

具有函数调用功能的 LLM 是 [AI 代理](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) 开发的基础，这些代理可以自主执行特定任务。例如，这些功能允许将 LLM 与其他 API 和系统集成，从而实现涉及数据检索、处理和分析的复杂工作流的自动化。

## 仔细了解函数调用

函数调用，也称为工具使用或 API 调用，是一种允许 LLM 与外部系统、API 和工具交互的技术。通过为 LLM 提供一组函数或工具及其描述和使用说明，该模型可以智能地选择和调用适当的函数来完成给定的任务。

这种能力改变了游戏规则，因为它使 LLM 能够摆脱基于文本的限制并与现实世界互动。LLM 不再仅仅生成文本，现在可以通过利用外部工具和服务执行操作、控制设备、从数据库中检索信息以及执行广泛的任务。

并非每个 LLM 都能够利用函数调用功能。那些经过专门训练或微调的 LLM 具有确定提示是否需要函数调用的能力。[伯克利函数调用排行榜](https://gorilla.cs.berkeley.edu/leaderboard.html) 提供了 LLM 在各种编程语言和 API 场景中的表现的见解，展示了函数调用模型在处理多个、并行和复杂函数执行方面的多功能性和鲁棒性。这种多功能性对于开发能够跨不同软件生态系统运行并处理需要同时执行操作的任务的 AI 代理至关重要。

应用程序通常使用函数调用功能两次调用 LLM：一次将提示映射到目标函数名称及其输入参数，再次将被调用函数的输出发送到生成最终响应。

下面的工作流显示了应用程序、函数和 LLM 如何交换消息以完成整个周期。

![](https://cdn.thenewstack.io/media/2024/05/9aebddbf-function-calling-1024x474.png)

**步骤 1**：用户发送可能需要访问该函数的提示——例如，“新德里的当前天气如何？”

**步骤 2**：应用程序将提示与所有可用函数一起发送。在我们的示例中，这可能是提示以及函数 get_current_weather(city) 的输入模式。LLM 确定提示是否需要函数调用。如果是，它会查找提供的函数列表——及其各自的模式——并使用填充有函数集及其输入参数的 JSON 字典进行响应。

**步骤 3**：应用程序解析 LLM 响应。如果它包含函数，它将按顺序或并行调用它们。

**步骤 4**：然后将每个函数的输出包含在最终提示中并发送到 LLM。由于模型现在可以访问数据，因此它会根据函数提供的事实数据做出回答。

## 集成 RAG 和函数调用

RAG 与函数调用的集成可以显着增强基于 LLM 的应用程序的功能。基于函数调用的 RAG 代理利用了这两种方法的优势——利用外部知识库进行准确的数据检索，同时执行特定函数以有效完成任务。

在 RAG 框架内使用函数调用可以实现更结构化的检索流程。例如，可以预定义一个函数，根据用户查询提取特定信息，RAG 系统从一个综合知识库中检索这些信息。这种方法确保响应不仅相关，而且精确地针对应用程序的需求量身定制。

![](https://cdn.thenewstack.io/media/2024/05/5026cffa-rag_function_call-1024x835.jpeg)

例如，在客户支持场景中，系统可以从数据库中检索产品规格，然后使用函数调用为用户查询格式化此信息，确保响应一致且准确。

此外，RAG 代理可以通过预定义的函数与外部数据库和 API 动态交互来处理复杂查询，从而简化应用程序工作流并减少手动干预的需要。这种方法在快速决策至关重要的环境中特别有益，例如金融服务或医疗诊断，系统可以提取最新的研究或市场数据并立即应用函数来分析此信息。

## 选择支持函数调用的 LLM

构建[代理工作流](https://www.quixl.ai/blog/the-integration-of-ai-agents-in-enterprise-systems-a-guide-to-agentic-workflows/)和 RAG 代理时，选择支持函数调用的正确 LLM 非常重要。以下是适合函数调用的商业和开放 LLM 列表。

**OpenAI GPT-4 和 GPT-3.5 Turbo**

OpenAI 的 GPT-4 和 GPT-3.5 Turbo 模型是最著名的支持函数调用的商用 LLM。这使开发人员能够定义 LLM 在推理期间可以调用的自定义函数，以检索外部数据或执行计算。LLM 输出包含函数名称和参数的 JSON 对象。然后，开发人员的代码可以执行此操作，并将函数输出返回到 LLM。

**Google Gemini**

Google 的 Gemini LLM 还可以通过 Vertex AI 和 Google AI Studio 来调用函数。开发人员可以定义函数和描述，Gemini 模型可以通过返回结构化的 JSON 数据，在推理过程中调用这些函数和描述。

**Anthropic Claude**

Anthropic 的 Claude 3 系列 LLM 有一个 API，可以实现与 OpenAI 的模型类似的功能调用功能。

**Mistral**

开源的 Mistral 7B LLM 已展示出函数调用能力，允许开发人员定义模型推理期间可调用的自定义函数。 

**NexusRaven**

NexusRaven 是一款专门为高级函数调用而设计的开源 13B LLM，在调用网络安全工具和 API 方面的一些基准测试中甚至超越了 GPT-4。

**Gorilla OpenFunctions**

Gorilla OpenFunctions 模型是一种经过 API 文档微调的 7B LLM。它可以从自然语言提示中生成准确的函数调用和 API 请求。 

**Fireworks FireFunction** 

FireFunction V1 是一种基于 Mixtral 8x7B 模型的开源函数调用模型。在结构化信息生成和路由决策的实际用例上，它达到了接近 GPT-4 的质量水平。

**Nous Hermes 2**

Pro Hermes 2 Pro 是一个出色的 7B 参数模型，擅长函数调用、JSON 结构化输出和常规任务。它在 Fireworks.ai 内置的函数调用评估中获得了 90% 的准确率，在结构化 JSON 输出评估中获得了 81% 的准确率。Hermes 2 Pro 在 Mistral 7B 和 Llama 3 8B 模型上都进行了微调，为开发者提供了众多选择。

在即将发表的有关函数调用的文章中，我将探讨如何使用商业和开放 LLM 实现此功能，以便构建一个可以访问实时数据的聊天机器人。
