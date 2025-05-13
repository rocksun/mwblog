
<!--
title: 模型上下文协议是新的API吗？
cover: https://cdn.thenewstack.io/media/2025/05/6e843875-agentic.jpg
summary: AI原生标准MCP旨在简化LLM与数据/工具连接，类似REST提升API效率。通过结构化描述API，赋能AI Agent自主决策，实现RAG进化。需关注token优化和资源控制，助力Agentic AI革新业务流程。
-->

AI原生标准MCP旨在简化LLM与数据/工具连接，类似REST提升API效率。通过结构化描述API，赋能AI Agent自主决策，实现RAG进化。需关注token优化和资源控制，助力Agentic AI革新业务流程。

> 译自：[Is Model Context Protocol the New API?](https://thenewstack.io/is-model-context-protocol-the-new-api/)
> 
> 作者：Ed Anuff

作为长期参与 API 标准领域的人，我一直对软件如何与软件对话感兴趣。对我来说，AI 最令人兴奋的事情之一就是能够自动化它的关键方面，比如使构建强大的软件代理成为可能，这些代理可以与我们周围的 API 世界进行对话。

现在，[模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 已经成为 AI 原生标准，用于继续沿着 REST、SOAP 和 XML-RPC 等先前标准开创的道路前进。MCP 由 Anthropic 去年年底推出，是一个开放标准，可以简化将数据和工具连接到[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 的过程，从而避免了为每个数据库、工具或云服务创建特定集成、连接器或提示的耗时需求。

随着代理系统的日益复杂，以及开发人员将越来越多的企业功能作为工具提供，拥有清晰且一致的规则对于自主工作流程的增长和成功至关重要。它使 [AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 能够决定以正确的顺序使用哪些工具来完成任务。

这很像 REST 帮助实现了 API 的高效数据交换、灵活性和可扩展性；MCP 与 API 领域发生的事情有很多相似之处，但也有一些重要的差异。

## 您的聊天窗口作为交互点

在 API 领域，我们将 API 视为通用、松散耦合的服务，可以重复用于各种用例，或者视为“体验”API，这些 API 旨在提供支持特定 UX 模式所需的特定功能。Netflix 通常是我们体验 API 的首选示例——它创造了这个术语——但您使用的几乎所有移动应用程序都严重依赖体验 API。

现在我们有了一个新的交互点：您的 ChatGPT 窗口或您的 Claude Desktop。

这是一个例子。我想编辑一个 Excel 电子表格或 Google Sheet。每个都有一个 MCP 服务器，以应用程序能够理解的方式表达功能。例如，Excel MCP 实际上可以声明如下内容：“我以电子表格的形式提供内部状态，这是一个由字母和数字寻址的行和列的矩阵。每个都有一个数值公式，我提供一组工具（或函数）供您使用来修改此电子表格。”

这种体验是如何构建的？它不是通过移动时代的特定用途体验 API 实现的，也不是通过恢复 Web 服务甚至微服务时代的认知负担来实现的。它需要一些新的东西：一种面向能力的的的方法，它公开工具和语义上下文，以帮助 LLM 了解如何使用这些工具来满足用户的请求。MCP 旨在填补这一空白。

开发人员实际上可以通过从 Excel 用户手册中复制和粘贴此信息来创建此 MCP 服务器。

MCP 使您能够向代理提出问题（“为我创建一个关于明年我可以在杂货上花费多少钱的电子表格”），并且在幕后，代理可以使用 MCP 服务器来公开这些功能。因为代理可以推理——它可以将问题分解为任务并迭代地执行它们——所以它可以使用 MCP 通过其他工具和 API 引入额外的上下文，并生成高度相关、有用的响应。

## 检索增强生成——以及更多

因此，上下文是您的提示加上您的代理检索到的上下文。听起来很熟悉？这是因为在许多方面，MCP 是检索增强生成 (RAG) 的演变。但它通过提供一种结构化的方式来描述 API、服务、工具或功能如何向代理描述，从而使其更进一步，以便它知道如何使用它们。

简单来说，[RAG 在推理时将外部信息输入到模型中](https://thenewstack.io/boost-llm-results-when-to-use-knowledge-graph-rag/)。MCP 为哪些工具和功能可用提供了一个明确定义的合同，更重要的是，它提供了关于如何使用它们的丰富的语义描述。

这使得聊天客户端（有时被贬低为简单和基本的 AI 形式——“只是聊天机器人”）非常强大。

## 使模型了解服务
LLM 使用工具的想法起源于 2022 年末的 [ReAct](https://arxiv.org/abs/2210.03629) 论文，并在 2023 年被广泛讨论。Meta 在 2023 年 2 月发布了其 [Toolformer 研究论文](https://scontent-dfw5-2.xx.fbcdn.net/v/t39.2365-6/422713285_707735768229632_5302603543892954301_n.pdf?_nc_cat=104&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=mYerYGIPnDAQ7kNvwFcdOpY&_nc_oc=AdnKg4q64Z5eBatZVV5Tf3lXao6nu-eLoeh4N8RQ9TMkl3k6Npjp0cO1XP7C-DURKKrzFXk9jm9pdIKMmcIMDHjM&_nc_zt=14&_nc_ht=scontent-dfw5-2.xx&_nc_gid=hpc349AG7QaGzzRG3SSHPw&oh=00_AfGmKUEV7l2sySmNuqGgeQcgkMzPOYl7k1lJKboxjkzeQg&oe=68183C8E)，OpenAI 紧随其后在 3 月份发布了函数调用和 JSON 模式支持的预览版，为 LangChain 等框架开辟了道路。

与此同时，人们也在努力将工具的使用模块化和打包。[OpenAI 的 ChatGPT 插件](https://openai.com/index/chatgpt-plugins/) 就是一个很好的例子。这些插件也在 2023 年 3 月推出，并基于 OpenAPI 规范，帮助 ChatGPT 访问最新信息、运行计算或使用第三方服务。微软也采用了插件模型，DataStax 很荣幸成为 GitHub Copilot 插件模型的设计合作伙伴；我们在 2023 年的 GitHub Universe 大会上交付了 [Astra DB extension for GitHub Copilot](https://www.datastax.com/integrations/github-copilot?utm_medium=byline&utm_source=thenewstack&utm_campaign=MCP&utm_content=)。

不幸的是，当时的 LLM 尚未成为推理模型，因此这些插件的效用有限。[使用这些模型实现 Agentic 用例是可能的](https://thenewstack.io/supercharge-your-rag-app-with-agentic-hybrid-search/)，但实际上，它们有些笨拙。

Anthropic 于 2024 年 6 月发布的 Claude Sonnet 3.5 模型，让我们真正看到了该领域的重大进展，使 Cursor 等公司能够在开发者领域利用这些功能，并使 Anthropic 越来越多地推广其模型的一般用途 Agentic 用例，从而引入 MCP 作为将工具打包和集成到 AI 客户端中的标准方法。这意味着开发人员可以构建 MCP 服务器，从而开箱即用地将他们的应用程序和服务集成到代理中，以便代理轻松使用。

## 你可能会错误地使用 MCP

通过 API，我们了解到 API 设计至关重要。像 Stripe 或 Twilio 这样的优秀 API 专为开发人员而设计。对于 MCP 来说，设计也很重要。但是我们为谁编写代码呢？

你不是为人类编写代码；你是为模型编写代码，模型会密切关注你写的每一个字。而且，重要的不仅仅是设计，MCP 的运营化也很重要，这是与 API 世界的另一个相似之处。正如我们过去在 Apigee 所说的那样，API 有好有坏。如果你的后端描述以领域为中心（而不是以业务或最终用户为中心），那么集成、采用以及开发人员使用你的 API 的整体能力将会受到损害。MCP 也可能出现类似的问题。如果 MCP 服务器的描述不清晰、不面向行动或对 AI 不友好，则 AI 可能无法识别或使用该服务器的工具。

最后需要注意的是，在许多方面，对于 AI 领域来说，一切都是非常新的，那就是每个动作都是“按表计费”的。在 LLM 世界中，一切都变成了 token，而 token 就是美元，正如 [NVIDIA 首席执行官黄仁勋 (Jensen Huang) 在今年的 Nvidia GTC 主题演讲中提醒我们](https://www.youtube.com/watch?v=_waPvOwL9Z8) 的那样。因此，AI 原生应用程序（以及这些应用程序连接到的 MCP 服务器）需要注意 token 优化技术，这对于成本优化是必要的。

除了 token/GPU 空间之外，还存在资源优化问题。一个过于热情的代理可能会通过多次调用你的企业后端服务来检索 [它需要的数据](https://thenewstack.io/ai-agents-in-doubt-reducing-uncertainty-in-agentic-workflows/)，从而导致你的企业后端服务崩溃。你的 MCP 服务器需要牢记这一点，并通过缓存等技术来减轻负担，或者告知代理利用 MCP 工具在其推理过程中产生的成本，并建议它采取相应的行动。

## 结论

正如 [我之前写过的](https://thenewstack.io/ai-agents-are-about-to-blow-up-the-business-process-layer/)，Agentic AI 有可能彻底改变业务流程。要充分发挥代理可以注入到企业架构中的自动化和决策能力，并确保准确、相关的结果，就需要它们能够调用外部函数、API 和工具。

虽然 MCP 不是目前正在开发的唯一促进这一点的标准（尽管它是目前的领跑者），但重要的是要理解，促进软件与软件对话的能力是我们所经历的所有主要技术浪潮中取得进展的方式。