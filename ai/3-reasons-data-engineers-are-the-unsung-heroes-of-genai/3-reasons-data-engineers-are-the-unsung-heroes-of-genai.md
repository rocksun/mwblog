
<!--
title: 为什么说数据工程师是GenAI时代的无名英雄
cover: https://cdn.thenewstack.io/media/2024/03/4ba5b17e-technology-4256272_1280.jpg
-->

随着组织在其产品中添加人工智能，数据工程师将成为扩展基础设施和治理以纳入新模型和技术不可或缺的一部分。

> 译自 [3 Reasons Data Engineers Are the Unsung Heroes of GenAI](https://thenewstack.io/3-reasons-data-engineers-are-the-unsung-heroes-of-genai/)，作者 Barr Moses。

在过去 18 个月中，生成式 AI 的进步在董事会和商业领袖中引起了强烈的兴趣。截至 9 月，87% 的 C 级高管 [IDC 调查](https://www.idc.com/getdoc.jsp?containerId=US50123123&pageType=PRINTFRIENDLY)表示他们至少在探索潜在用例。根据 Salesforce 2023 年 11 月的[报告](https://www.salesforce.com/resources/research-reports/state-of-data-analytics/)，另有 [77% 的商业领袖](https://www.salesforce.com/resources/research-reports/state-of-data-analytics/) 担心他们已经错过了 GenAI 的好处。

但数据领导者明白，无论他们的 CEO 在观看炫目的演示后经历了多少错失恐惧症，实施[最新的 LLM](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) 都必须经过深思熟虑。为了提供有意义的业务价值，[这些模型](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/)需要提供高质量的数据——同时保持安全、隐私和可扩展性。

在大多数组织中，有一些关键贡献者已经在做这项工作：[数据工程师](https://thenewstack.io/top-10-tools-for-data-engineers/)。鉴于公司实现 [企业级 AI](https://www.montecarlodata.com/blog-the-moat-for-enterprise-ai-is-rag-fine-tuning/) 的当前状态，数据工程师将变得越来越重要。

## 数据工程师在企业 AI 中的重要作用

在任何现代数据团队中，数据工程师负责构建和维护数据堆栈的基础设施。他们的管道和工作流使应用程序、分析师、业务消费者和数据科学家能够访问和使用完成工作所需的数据。

随着组织开始将生成式 AI 分层到其产品中，数据工程师将成为扩展现有基础设施和治理以涵盖最新模型和技术不可或缺的一部分。让我们探讨[数据工程师将为 AI 成功做出贡献](https://thenewstack.io/data-engineer-critical-role-for-data-success/)的三种具体方式。

### 1. 促进 RAG 以改善 LLM 输出

目前，大多数在 GenAI 中取得成功的组织正在使用 [检索增强生成 (RAG)](https://www.montecarlodata.com/blog-the-moat-for-enterprise-ai-is-rag-fine-tuning/)。这涉及将知识源或数据集纳入其生成过程——在响应提示时为 LLM 提供对动态数据库的访问权限。例如，通过完全实施 RAG，面向消费者的聊天机器人将能够在支持交互期间提取特定的客户数据以供参考。

对于大多数用例，RAG 比 [微调](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts) 更合适——在较小、特定数据集上重新训练现有 LLM。微调需要大量的计算资源和大量数据，并且通常涉及较高的过度拟合风险。

有效实施 RAG 需要高质量的数据管道，将 [公司数据](https://thenewstack.io/the-next-wave-of-big-data-companies-in-the-age-of-chatgpt/) 输入到 AI 模型中。数据工程师负责确保：

- 数据库准确且相关，并定期更新和进行质量检查
- 检索过程得到优化，并使用正确且在上下文中适当的数据解决提示
- 通过[数据可观察性](https://thenewstack.io/what-is-data-observability-and-why-does-it-matter/) 持续监控和优化数据输入

随着技术的进步，对 RAG 的偏好可能会发生改变，但就目前而言，它通常被认为是企业 AI 最实用的前进道路。它还有助于减少[幻觉](https://www.pinecone.io/learn/options-for-solving-hallucinations-in-generative-ai/)和不准确性，同时提高数据团队的透明度。

### 2. 维护安全和隐私

数据工程师已经在数据治理中发挥了关键作用，确保数据库具有适当的内置角色和安全控制，以确保隐私和合规性。实施 RAG 时，这些控制需要在整个管道中得到扩展和一致应用。

例如，公司的 LLM 不应将其任何客户数据用于其自己的培训，而面向客户的聊天机器人必须在共享敏感数据之前确认用户的身份和权限。数据工程师在维护法规和最佳实践合规性方面发挥着至关重要的作用。

### 3. 可靠、高质量的数据

最终，GenAI 的成功取决于数据质量。如果没有持续向 LLM 提供准确、可靠的数据，即使是最先进的模型也无法产生有用的输出。

在过去五年中，领先的数据工程师采用了可观测性工具（包括自动化监控和警报，类似于 DevOps 可观测性软件），以帮助提高数据质量。可观测性帮助数据团队监控并主动响应事件，例如失败的 Airflow 作业、损坏的 API 和格式错误的第三方数据，这些事件会使数据健康面临风险。借助端到端数据谱系，团队可以了解上游和下游依赖关系。

当可观测性工具应用于包括向量数据库在内的现代 AI 堆栈时，数据工程师可以提供透明度。谱系允许工程师在数据转换为嵌入时跟踪数据源，然后使用该数据生成 LLM 放置在用户面前的富文本。这种可见性帮助数据团队了解 LLM 的操作方式、改进其输出并快速排除事件故障。

正如 CreditKarma 的工程副总裁 Vishnu Ram [告诉我们](https://www.montecarlodata.com/blog-credit-karmas-journey-to-reliable-generative-ai-models-with-data-observability/)：“我们需要能够观察数据。我们需要了解我们正在将哪些数据放入 LLM 中，如果 LLM 提出自己的想法，我们需要知道这一点——然后知道如何处理这种情况。如果你无法观察进入 LLM 的内容和输出的内容，你就完了。”

## 数据工程师是 AI 驱动型组织的未来

AI 技术正在以令人眼花缭乱的速度发展。但即使微调模型和更高级的自定义培训对企业来说变得可行，确保数据质量、安全性和隐私的需求也不会改变。

随着组织投资生成式 AI 应用程序，其数据的质量和可用性将比以往任何时候都更有价值。这意味着工作流和数据工程流程可能会发生变化，但它们在组织中的重要性才刚刚开始。
