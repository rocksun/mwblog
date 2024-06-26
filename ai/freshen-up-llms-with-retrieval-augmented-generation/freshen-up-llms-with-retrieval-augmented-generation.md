# 利用“检索增强生成”技术为 LLM 注入新鲜元素

像 GPT 这样的大型语言模型是在大型语料库数据上进行离线训练的。这使得模型对于在它们训练之后生成的任何数据一无所知。本文介绍了如何对它们进行更新。

![](https://cdn.thenewstack.io/media/2023/07/1033f031-glasses-gc5dfa4442_1280-1024x682.jpg)
*图片来自 Pixabay 的 Penny 。*  

基础模型，包括像 GPT 这样的[大型语言模型](https://thenewstack.io/how-llms-are-transforming-enterprise-applications/)（LLMs），通常是在大型语料库数据上进行离线训练的。这使得模型对于在它们训练之后生成的任何数据一无所知。

此外，由于基础模型是在公开可用的通用语料库数据上进行训练的，它们在特定领域的任务中效果较差。检索增强生成（Retrieval Augmented Generation，RAG）是一种技术，可以从基础模型外部检索数据，并将相关检索到的数据注入到上下文中，以增强提示信息。

RAG 比预训练或微调基础模型更具成本效益和高效性。它是用于使 LLMs “接地”的技术之一，能够提供与特定用例相关且相关的信息，以确保响应的质量和准确性。这对于减少 LLMs 中的错误回答非常关键。

在本文中，我们将仔细探讨如何使用 RAG 来引入特定领域的知识，并应用于 LLMs 中。

## 为什么要实施 RAG ？

让我们考虑一个简单的场景，您向 ChatGPT 提问关于第 95 届奥斯卡奖（Academy Awards）。由于宣布的日期在 2023 年 3 月，而 ChatGPT 的训练截止日期为 2021 年 9 月，您会得到一个典型的道歉回答。

![](https://cdn.thenewstack.io/media/2023/07/d36829eb-rag-0-1024x356.jpg)

然而，如果在询问同样的问题之前给 ChatGPT 一些上下文，它将能够以有意义的答案回复。

让我们复制并粘贴 Good Morning America 网站上与第 95 届奥斯卡奖相关的[简介](https://www.goodmorningamerica.com/culture/story/oscars-2023-naatu-naatu-1st-song-indian-film-97779963)，这将为提示“注入”额外的上下文。

![](https://cdn.thenewstack.io/media/2023/07/efd62b75-rag-1-793x1024.jpg)

我们的提示现在如下：

![](https://cdn.thenewstack.io/media/2023/07/04ca27f1-rag-2-1024x425.jpg)

正如我们所看到的，那个简单的简介对 LLM 对问题的回答产生了重大影响。根据支持的上下文长度，我们可以向 LLM 提供额外的信息，使其了解特定主题。

尽管我们手动复制和粘贴，但实质上我们实施了一个基本的 RAG 机制，以从 ChatGPT 获取我们想要的结果。

在企业环境中，LLM 可能需要从各种非结构化和结构化数据源中检索信息。因此，复制和粘贴上下文以补充提示不是一个可行的选择。这就是 RAG 提供一个框架和蓝图，以构建特定领域的生产级 LLM 应用的地方。

## RAG 框架

在 RAG 中用于增强提示的外部数据可以来自不同的来源，包括文档库、数据库和 API 。

![](https://cdn.thenewstack.io/media/2023/07/52741c72-rag-3-1024x729.jpg)

### 第一步：提示

用户在此交互中首次为 ChatGPT 提供提示。提示可能包含用户期望在输出中得到的简要描述。

### 第二步：上下文搜索

这是最关键的一步，通过一个外部程序来增强提示，该程序负责从外部数据源搜索和检索上下文信息。这可能包括查询关系数据库，基于关键词搜索一组索引文档，或调用 API 从远程或外部数据源检索数据。

### 第三步：提示增强

一旦生成上下文，它将被注入到原始提示中进行增强。现在，用户的查询中包含了附加的包含事实数据的信息。

### 第四步：推理

LLM 收到带有附加上下文和用户原始查询的丰富提示。这显著增加了模型的准确性，因为它可以访问事实数据。

### 第五步：回复

LLM 将带有事实正确信息的回复发送回聊天机器人。

### 词嵌入和向量数据库在 RAG 中的作用

虽然上述框架解释了实施 RAG 的高级方法，但没有讨论实现细节。

在执行搜索和检索的关键步骤之一是根据输入查询进行语义搜索，以筛选具有相似含义的词汇和句子。为此，我们必须利用词嵌入模型，将文本转换为一组向量。当源数据和提示基于相同的词嵌入模型进行向量化时，我们可以执行语义搜索，匹配具有相似含义的句子和短语。

由于将大型数据语料库基于词嵌入转换为向量对于每个查询来说是昂贵的，因此生成它们一次并将它们存储在数据库中是个不错的主意。向量数据库是一种新的数据库类别，用于存储向量并执行相似性搜索。随着新的文档和数据库添加到流程中，它们可以被转换成向量并存储在向量数据库中。

在本系列的下一部分中，我们将实现 RAG 来增强发送到 OpenAI 的提示。请继续关注。