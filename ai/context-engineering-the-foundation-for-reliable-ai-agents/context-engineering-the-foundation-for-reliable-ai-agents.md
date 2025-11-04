
<!--
title: 上下文工程：AI智能体可靠性的基石
cover: https://cdn.thenewstack.io/media/2025/10/6bea1b77-question.jpg
summary: 文章阐述了AI智能体中上下文工程的重要性，它整合工具选择、内存、提示工程和检索，以提升推理模型性能。挑战包括非结构化数据提取、上下文窗口限制及内存管理。
-->

文章阐述了AI智能体中上下文工程的重要性，它整合工具选择、内存、提示工程和检索，以提升推理模型性能。挑战包括非结构化数据提取、上下文窗口限制及内存管理。

> 译自：[Context Engineering: The Foundation for Reliable AI Agents](https://thenewstack.io/context-engineering-the-foundation-for-reliable-ai-agents/)
> 
> 作者：Kiran Matty

在智能体世界中，上下文为王。将[Claude](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)、[DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/)或[GPT-5](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/)等高性能推理模型与正确的上下文相结合，可以推动高效的规划和工具使用，改进多步骤推理，从而实现个性化对话、更高的任务准确性和相关响应。

在本文中，我们将阐述上下文工程的必要性及其相关优势，识别开发者在使用它开发AI智能体时面临的挑战，并提出一个高层架构来帮助解决这些问题。

## **解决上下文困境：过多与过少**

企业拥有大量的结构化和非结构化数据。然而，将这些数据直接作为上下文提供给智能体，会导致任务理解上的混淆，原因在于数据固有的噪声和重要信息的丢失，这可能会在超出有限的上下文窗口时损害大型语言模型（LLM）的态势感知能力。正如我之前所写，使用[长上下文并非总是解决](https://thenewstack.io/solving-the-rag-vs-long-context-model-dilemma/)此问题的办法。另一方面，发送过少的上下文可能导致智能体产生幻觉。简单来说：输入垃圾，输出垃圾。

上下文工程是指一系列技术和工具的集合，用于确保AI智能体仅拥有完成指定任务所需的必要信息。基于LangChain的Harrison Chase所描述的[上下文工程](https://blog.langchain.com/the-rise-of-context-engineering/)概念，上下文工程包含以下几个方面：

*   **工具选择** 意味着确保智能体能够访问正确的工具，以检索完成指定任务所需的信息。例如，设想一个场景，智能体被要求完成一项行动，比如为一家四口（两个孩子和一条狗）计划一次毛伊岛之旅。它应该能够检索所有回答用户问题并可靠执行任务所需的工具。
*   **内存使用** 也是一个因素。为智能体配备短期记忆至关重要，它为用户和智能体之间正在进行的会话提供个性化上下文；同时也要配备长期记忆，它提供跨多个会话的上下文，使交互连贯、真实，甚至更加个性化。这涵盖了多种记忆类型，如个人资料、语义、情景、对话和程序性记忆。它还包括工作记忆，用于在多智能体系统中实现智能体之间无缝任务协调的上下文共享。
*   另一个组成部分是 **提示工程。** 这确保智能体能够访问正确的提示，该提示在智能体行为方面被清晰定义，包括具体的指令和约束。
*   最后，是 **检索。** 根据用户的问题动态[检索相关数据](https://thenewstack.io/enterprise-ai-success-demands-real-time-data-platforms/)，并在发送给LLM之前将其插入到提示中，确保AI的成功。这通过使用检索增强生成（RAG）和直接数据库调用来实现。企业通常拥有一个多语言环境，其中包含多个事实来源。在这种情况下，[模型上下文协议](https://modelcontextprotocol.io/docs/getting-started/intro)（MCP）允许开发者以标准化方式从众多数据源检索上下文。

上述上下文与智能体共享，随后与推理LLM共享。通过将相关工具名称及其关联的工具规范、短期和长期记忆的内容、提示以及从RAG、数据库和SaaS服务检索到的相关内容增强智能体提示，可确保任务成功执行。图1展示了上下文工程架构的概念视图。

[![Figure 1: Conceptual view of the architecture for context engineering (source: Couchbase)](https://cdn.thenewstack.io/media/2025/10/e981f99d-image1-1024x455.png)](https://cdn.thenewstack.io/media/2025/10/e981f99d-image1-1024x455.png)

*图1：上下文工程架构概念视图（来源：Couchbase）。*

其工作原理如下。首先，用户向多智能体系统发送请求。然后，智能体应用程序通过API检索上下文，这些API涵盖了目录中的提示和工具；来自向量存储的RAG上下文；来自短期和长期记忆的对话摘要；以及使用各种MCP服务器从操作数据库（包括数据库外部来源）获取的摘要、情绪和提取的实体。

智能体应用程序随后用整合的上下文增强提示，创建智能体提示，该提示被发送到推理模型，如Claude、DeepSeek或GPT-5。推理循环在智能体框架（如LangGraph）内触发，该框架与推理模型交换消息，期间调用了多个相关工具。

根据智能体架构，可能会调用其他智能体并在它们之间共享上下文。之后，生成的答案被发送给用户，并且用户与智能体的对话被存储在内存中，以确保后续会话的连续性。

以下是开发者在上下文工程中面临的一些挑战，以及上述架构如何帮助解决这些挑战。

## **大规模从非结构化数据中提取上下文**

百分之八十的企业数据是非结构化的，并且在很大程度上无法用作上下文。因此，为了提取支持重要用例所需的上下文，开发者目前需要为Spark、Flink或其他数据处理引擎编写抽取、转换、加载（ETL）作业。这些作业[从源数据库读取非结构化数据](https://thenewstack.io/from-unstructured-data-to-rag-ready-with-docling/)，进行处理，然后将结果写回，供智能体后续消费。这些DIY解决方案虽然性能良好，但不仅降低了开发者的速度，还增加了运营和维护开销。

一些示例用例包括：总结文档中“support\_ticket\_desc”字段的详细信息，以便客户支持AI智能体能够轻松理解并采取行动；从“patient\_diagnosis”字段中提取医学术语（疾病、药物、症状），以便分诊智能体能够为患者提供初步诊断；以及标记“email\_content”字段中的文本是“不相关”、“促销垃圾邮件”、“可能是诈骗”还是“网络钓鱼尝试”，以便电子邮件助手可以判断是否自动回复电子邮件。

AI函数允许开发者在SQL语句中调用LLM，并能够编写提示来控制LLM输出的格式、语气和其他方面。例如：开发者使用AI函数，为数据库中存储的产品评论添加情感和摘要。零售AI智能体随后通过工具调用读取这些信息，并根据用户报告问题的严重程度，判断是否向不满意的用户提供有吸引力的优惠以提高客户满意度（CSAT）。该[智能体还会创建产品功能请求](https://thenewstack.io/ai-agents-protocols-driving-next-gen-enterprise-intelligence/)以推动改进。

考虑以下一位客户对搅拌机的性能和耐用性感到失望所留下的产品评论：

*“我根据产品描述和评论对这款搅拌机抱有很高的期望，但从第一天起就让我失望了。电机即使处理软水果也很吃力，使用几分钟后就会过热。我不得不几次在制作冰沙中途停下来让它冷却，这完全违背了拥有‘高速’搅拌机的目的。”*

以下是使用SQL进行的无代码分析：

| SQL Statement | Response |
| --- | --- |
| **SELECT** review\_id, SUMMARIZE(review\_text) AS summary, SENTIMENT(“review\_text”, prompt = “Evaluate the sentiment of the “customer\_review” field on a 5-point scale: very negative, negative, neutral, positive, very Positive”) AS sentiment **FROM**customer\_reviews **WHERE** review\_text IS NOT NULL; | “sentiment”: very negative “summary”: The blender needs a stronger motor to handle frozen fruits and ice without overheating, sharper blades for smoother blends and a better-sealed lid to prevent leaks. Durability should be improved to eliminate loud grinding noises and burning smells after short-term use. |

这需要一个底层数据库，通过在SQL语句中调用领先的LLM，以无代码方式自动完成上述任务。

## **将上下文适配到有限的上下文窗口中**

在上下文方面，少（但相关）即是多！100万+的token限制并不意味着你可以将上下文视为无限内存。每个额外的token都会带来成本、延迟和性能影响。与其用冗长、不必要的上下文填充提示，导致重要细节丢失（尤其是在提示的中间），不如考虑使用RAG等技术来保持上下文精简且高度相关。

列出LLM可以使用的所有可用工具会导致提示冗余，并可能因相似工具具有相似名称或工具规范而使智能体感到困惑。此外，主要由于工具缺乏可重用性和治理而导致的工具泛滥，最大程度地增加了智能体失败的可能性。然而，将所有工具集中编目不仅支持可重用性，而且只检索与回答用户问题相关的工具。这可以与编写良好的工具描述和工具路由结合使用，以提高工具调用准确性。例如，以下API可以只检索智能体应用程序中与回答用户查询相关的工具：

```
catalog.find_tools(query="Plan a trip to Maui")
```

智能体行为对提示的质量高度敏感；因此，应谨慎管理对提示的更改。对所有提示进行版本控制和回滚支持编目，可确保智能体行为的一致性，即使提示发生更改。例如，以下API可以只检索与查询相关的提示，从而保持上下文的准确性：

```
catalog.find_prompt("query="Plan a trip to Maui")
```

您可以通过使用高性能多模型数据库来实现这一点，该数据库允许您通过RAG使用[向量搜索](https://www.youtube.com/watch?v=Z7DoCAbgZgk)从大量结构化和非结构化数据中提取上下文，并存储和选择高度相关的工具和提示。

## **管理智能体内存中的衰减和冲突解决**

智能体内存是上下文工程的关键组成部分。然而，实现内存衰减和冲突解决对开发者来说并非易事。

对话式智能体从其交互中积累了大量数据。如果智能体记住每一个过去的 संदेश，上下文窗口将很快被填满，导致连贯性丧失并无法处理新信息。因此，有必要衰减过时信息。

这里的挑战在于信息衰减的速度不同。例如，零售商的退货政策不像快时尚服装的需求那样频繁变化。因此，需要针对不同用户对话的内存中实现信息特定的生存时间（TTL），以便服装推荐智能体不会从内存中回忆起过时信息。

此外，开发者在必要时需要从内存中删除过时上下文的选项。这要求智能体内存使用支持TTL的数据库来实现，以按所需速率衰减内存，并根据需要以一致的方式删除内存。

在多智能体系统中，单个智能体可能拥有相互冲突的信息，或者在同一用户会话中的多个智能体可能尝试将冲突信息提交到内存。这种冲突可以通过为每条消息使用时间戳并将其作为信息演变过程的上下文与LLM共享来解决。此外，消息还可以用智能体名称和其他信息进行标注，以便LLM可以决定哪条信息与内存相关联。

## **注册预览**

在Couchbase，工程化上下文并快速提供它的能力至关重要，它使开发者能够创建高性能且可靠的智能体。借助目前处于私有预览阶段的Couchbase [Capella AI服务](https://www.couchbase.com/products/ai-services/)和[Capella](https://www.couchbase.com/products/capella/) NoSQL DBaaS，您可以使用一个单一数据平台，该平台包含各种存储——例如操作型、分析型、向量、工具、提示和内存——以利用[SQL++](https://www.couchbase.com/products/n1ql/)提取上下文并增强您的提示。AI函数作为AI服务的一项功能，通过在熟悉的SQL语句中调用领先的LLM，自动从大量数据中提取上下文。使用Couchbase实现的智能体内存能够解决复杂的智能体内存问题，如内存衰减和冲突解决。

注册[Capella AI服务私有预览](https://info.couchbase.com/capella-ai-services-signup?_gl=1*18nnzn9*_gcl_aw*R0NMLjE3NTg1NjY0MTYuQ2owS0NRanc1OFBHQmhDa0FSSXNBRGJEaWx4RTJpeTZLNkh0QTBpUGoxM1FEeVFvQ1dkV2pPRTktRUh3NUpIOUQtY0Q3RmFxY0doRUIzWWFBbURKRUFMd193Y0I.*_gcl_au*ODYwOTQwNDUuMTc1NTExNzI4Nw..)并[免费](https://cloud.couchbase.com/sign-up)试用Capella NoSQL DBaaS，开始构建您的智能体应用程序。