<!--
title: RAG时代的终结者？Pinecone正亲手推翻自己开创的范式
cover: https://cdn.thenewstack.io/media/2026/05/9c83eebe-macude-mariana-cuesta-xy9w6clpao8-unsplash-scaled.jpg
summary: 向量数据库先驱Pinecone推出Nexus，宣布传统RAG已成瓶颈。其主张通过预编译知识工件取代原始分片检索，以解决智能体效率低、成本高的问题，引领架构升级。
-->

向量数据库先驱Pinecone推出Nexus，宣布传统RAG已成瓶颈。其主张通过预编译知识工件取代原始分片检索，以解决智能体效率低、成本高的问题，引领架构升级。

> 译自：[The company that made RAG mainstream is now betting against it](https://thenewstack.io/pinecone-nexus-rag-obsolete/)
> 
> 作者：Janakiram MSV

Pinecone 刚刚宣告 RAG 时代已经结束。

Pinecone 开创了向量数据库这一类别。它将 RAG（检索增强生成）定义为为语言模型提供事实依据的标准模式。约有 80 万开发者和 9000 名付费客户学习了如何在 Pinecone 的基础设施上进行分块（chunk）、嵌入（embed）和检索。然而，随着周一发布的专为智能体（Agent）打造的知识引擎 Nexus，Pinecone 正在告诉这些开发者：他们曾经学习的这种模式现在成了瓶颈。

## Pinecone 定义的类别，如今被它亲自宣告过时

如果你阅读 Pinecone 对 Nexus 的定位，很难不注意到该公司将“推理时检索”[描述](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/#:~:text=This%20is%20the%20%E2%80%9Cten%20blue%20links%E2%80%9D%20era%20of%20agentic%20retrieval.)为“智能体检索的‘十条蓝色链接’时代”（喻指过时的搜索引擎结果）。

* 它指出，困在“检索-阅读-检索”循环中的智能体只能完成 50% 到 60% 的任务。
* 它指出，智能体 85% 的精力都消耗在获取上下文上。

Pinecone 的观点是：将原始数据块交给前沿模型并寄希望于模型能理解它，这种做法既脆弱、缓慢又昂贵。

这种描述本质上就是换了个说法的 RAG。而这正是 Pinecone 在过去四年里一直遵循的模式，他们为此发布了大量教程、培训内容和一整套开发者关系计划。现在，向量数据库成为了底层基座，而不再是表面层。产品层级已经向上移动了一层。

这种自我揭露式的转型非常罕见。大多数基础设施供应商在市场察觉其衰落时，仍会继续推销旧产品。而 Pinecone 是第一个站出来指明这一点的供应商。

## 知识编译是新的 RAG

核心转变在于将推理过程上移。不再是让智能体在查询时获取 20 个数据块并消耗 Token 来弄清楚它们的含义，Nexus 会预先将源数据编译成类型化的、有据可查的、针对特定任务的“工件”（Artifacts）。智能体查询的是这些工件，而不是原始语料库。周一同步发布的 [KnowQL](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/#KnowQL:-A-Declarative-Query-Language-for-Agents) 为此提供了一套词汇表。它包含六个原语：意图（intent）、过滤器（filter）、出处（provenance）、输出形状（output shape）、置信度（confidence）和延迟预算（latency budget），通过单个声明式调用即可返回结构化且有据可查的响应。

Pinecone 声称，这种方式能将任务完成率提升至 90% 以上，并减少 90% 的 Token 支出。在生产团队证实之前，对这些数据应保持谨慎态度。但即使不看数据，其架构层面的主张也是成立的。“一次编译，多次读取”正是适合智能体工作负载的模式，而且 Pinecone 并不是唯一指向这一方向的厂商。

## 更大的趋势：推理正在全链路上游化

[Anthropic 发布了 Skills](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/)，将其作为编译好的、可重用的上下文包。Cursor rules 在编辑器层执行同样的工作。 [Claude Code 子智能体](https://thenewstack.io/beating-the-rot-and-getting-stuff-done/) 针对每个任务预先打包上下文和工具。LangChain 的 Harrison Chase 数月来一直将其称为“上下文工程”。现在，Pinecone 正在检索层实践这一理念。

这种模式本身并不新颖，但做出这一声明的供应商身份却非同寻常。

**当然，也存在诚恳的质疑。** KnowQL 必须跨越 [SQL 曾跨越的标准门槛](https://thenewstack.io/configure-sql-server-standard-edition-for-high-availability-on-aws/)，而标准并不能仅由一家供应商宣告而生。向量搜索也不会消失，大量的智能体工作负载仍然需要对原始文本进行廉价的相似度计算。改变的是价值在技术栈中所处的位置。

如果接下来的 12 个月正如 Pinecone 所押注的那样发展，向量搜索将变成“管道”式的底层设施，知识编译将成为产品，而“RAG 流水线”将成为开发者口中的过去式，就像我们现在谈论“LAMP 栈”一样——带着一种对过去的敬意。

我在这篇解读中唯一可能判断错误的是时机。类别的消亡通常比宣告其死亡的供应商预想的要长。但方向是明确的，而且正是那个亲手建立该类别的公司，正在指明离开它的道路。

曾经教你做 RAG 的供应商，现在正告诉你停止这样做。