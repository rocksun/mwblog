
<!--
title: 让我们开始代理：LangChain和LlamaIndex谈论AI代理
cover: https://cdn.thenewstack.io/media/2024/07/0a0a10f7-aie_agents_2024.jpg
-->

在人工智能工程师世界博览会上，LangChain 和 LlamaIndex 的创始人谈论了从基于 RAG 的 LLM 系统到 AI 代理的演变。

> 译自 [Let’s Get Agentic: LangChain and LlamaIndex Talk AI Agents](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/)，作者 Richard MacManus。

“代理系统”（或“代理工作流”）这个词在上周于旧金山举行的[AI 工程师世界博览会](https://www.ai.engineer/worldsfair)上多次出现。AI 代理是两家领先的 AI 工程初创公司：[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 和 [LlamaIndex](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/) 的重点，这两家公司都在演示中展示了他们对这项技术的独特见解。

在 AI 领域，“代理”一词指的是使用大型语言模型 (LLM) 执行各种任务的自动化软件。但是，[当我参加去年 10 月的第一次 AI 工程师活动](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)时，当时它被称为 AI 工程师峰会，我感觉 AI 代理是该活动中最受炒作的——也是最不可信的——方面。AutoGPT 当时是最热门的代理初创公司（也是 10 月份活动的首席赞助商），但它的演示让我非常怀疑。

## LangChain

在世界博览会上，AutoGPT 似乎没有出现在赞助商名单中，但 LangChain 的创始人兼首席执行官 Harrison Chase 提到了它。在关于代理主题的快速演示中，Chase 开始向 2023 年代理的炒作泼冷水。

“对我来说，AutoGPT 代表了代理炒作的顶峰，”他告诉世界博览会观众。“而且我实际上认为在那之后几个月，人们意识到通用代理架构不够可靠，无法构建可用于生产的系统，因此人们对代理的兴趣有所下降。”

![](https://cdn.thenewstack.io/media/2024/07/70abc3c8-langchain_agents.jpg)

*LangChain 根据自己的理解对 Agent 的历史进行了概述*

他提到了[OpenAI 的助手 API](https://platform.openai.com/docs/assistants/overview) 作为代理的转折点。然后，今年早些时候，LangChain 发布了[LangGraph](https://www.langchain.com/langgraph)，Chase 将其描述为“专为代理而设计”。他指出，LangGraph 被设计为“高度可控且低级”。

“将代理投入生产的公司正在构建定制的认知架构，对他们希望代理的行为方式进行微小的差异编码，”他解释道。但这并不是“通用代理”系统能够提供的。

我在 10 月份对代理的另一个批评是，它们似乎想要将人类排除在外——我认为这是狂妄自大。Chase 的语气要谦虚得多，甚至将“人机交互”列为 LangGraph 的定义特征之一。

LangGraph“附带一个内置的持久层，”他说，“这使得许多非常酷的‘人机交互’模式成为可能。”

![](https://cdn.thenewstack.io/media/2024/07/46b2620f-langgraph1.jpg)

*LangGraph 细节*

Chase 在舞台上宣布发布“LangGraph 的第一个稳定版本”——根据图形显示为 0.1 版本——他说这重申了其“致力于构建一个代理架构，使您能够构建将代理投入生产所需的定制认知架构”。

然后，他回到了 OpenAI 助手 API，他说这是一个很好的代理平台，尽管它有一些缺陷。“它附带了一个特定状态，它期望您的应用程序具有该状态，一个消息列表，而且它有点僵化，不允许您轻松地执行除该状态之外的其他操作，”他说。

![](https://cdn.thenewstack.io/media/2024/07/fddc40b1-openai_assistants_api.png)

*OpenAI Assistant API（来自LangChain）*

这导致 LangChain 为 LangGraph 开发了一个 SaaS 产品，名为 LangGraph Cloud。它为代理提供“一键式部署、可扩展的服务器和任务队列以及集成监控”。

他补充说，LangGraph Cloud 的另一个好处是“它不受 OpenAI 的约束，并且支持您使用 LangGraph 构建的任何认知架构”。

## LlamaIndex

LlamaIndex 的创建者 Jerry Liu 在世界博览会上的一次单独演示中，提出了另一种 AI 代理方法。他将代理定位为 RAG（[检索增强生成](https://thenewstack.io/improving-llm-output-by-combining-rag-and-fine-tuning/)）的自然继承者，RAG 一直是将预训练的 LLM 与外部数据源集成的最常见方法。

“如果你在过去一年左右的时间里关注过我们的 Twitter，基本上我们 75% 的时间都在谈论 RAG，”他说，并补充说，现在已经很常见“不仅进行一次性查询搜索，而且实际上随着时间的推移存储您的对话历史”。

但 Lio 继续说道，“今年，许多人对构建代理工作流感到兴奋，这些工作流不仅可以合成信息，还可以执行操作并与许多服务交互，从而基本上为您提供您需要的东西。”

![](https://cdn.thenewstack.io/media/2024/07/18b3e8d6-from-rag-to-agents.png)

*从 RAG 问答转向“代理工作流”*

LlamaIndex 明智地决定将 AI 代理重新命名为对企业来说不那么令人不寒而栗的东西：他们称之为“知识助手”。

Liu 表示，RAG 只是构建知识助理目标的“开始”。他将 RAG 描述为“在一些已经存在了几十年的检索方法之上，一个美化的搜索系统”。

Liu 继续解释了 LlamaIndex 用户的一系列复杂选项，但总体而言，用户可以使用超越 RAG 的技术构建更高级的代理。他说，用户甚至可以构建“一个通用的多代理任务求解器”， “在那里，你甚至超越了单个代理的能力，走向多代理的编排”。

![](https://cdn.thenewstack.io/media/2024/07/32ec741d-llamaindex_agents1.jpg)

*从简单代理到高级代理*

Liu 似乎创造了“知识助理”一词，以便企业更容易理解 AI 代理的概念，然后他试图解释“代理 RAG”的概念，这又使事情变得更加复杂。

关于代理 RAG，Liu 说：“你不仅直接将查询馈送到向量数据库，最终，一切都是一个 LLM 与一组数据服务作为工具进行交互，对吧？”

嗯，对。

Liu 表示，如果一切都能正常工作，这个过程将产生更高级的代理，例如“个性化的问答系统”，能够随着时间的推移维护用户状态的代理，以及能够从非结构化和结构化数据源中查找信息的代理。

最后，Liu 宣布了 LlamaIndex 的一项新功能，名为（你猜对了）：[Llama Agents](https://www.llamaindex.ai/blog/introducing-llama-agents-a-powerful-framework-for-building-production-multi-agent-ai-systems)。Liu 说：“我们认为这是帮助你构建生产级知识助理的关键要素，尤其是随着世界变得越来越代理化。”

![](https://cdn.thenewstack.io/media/2024/07/e2796003-llama-agents.png)

*Llama 代理预览*

## 代理世界

Harrison Chase 在演讲开始时明显地贬低了去年的 AI 代理轰动事件 AutoGPT。但当然，LangChain 和 LlamaIndex 提供的解决方案是否会更好，还有待观察。

LangChain 的解决方案有一个复杂的口号（“定制认知架构”），但似乎比 LlamaIndex 更简单，LlamaIndex 有一个简单的口号（“知识助理”），但工作流程很复杂。但一年后再来看看它们是否在现实世界中有效。
