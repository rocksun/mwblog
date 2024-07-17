
<!--
title: 为大语言模型在结构化数据中自动上下文
cover: https://cdn.thenewstack.io/media/2024/07/e529156d-meaning.jpg
-->

初创公司 illumex 将语义理解嵌入公司数据集，以提高特定领域的 AI 结果。

> 译自 [Automating Context in Structured Data for LLMs](https://thenewstack.io/automating-context-in-structured-data-for-llms/)，作者 Susan Hall。

随着机器学习和生成式人工智能的兴起，用户正在了解到，他们不能仅仅将一堆数据扔进模型，就期望得到可靠的结果。缺失的元素是：上下文。

特别是结构化数据，如果没有对词语的一致定义、它们在特定上下文中的使用方式以及数据之间关系的了解，在[大语言模型](https://roadmap.sh/guides/introduction-to-llms)中就毫无用处。

然而，组织往往将数据存储在各种不同的存储库中，采用不同的格式，命名也不一致。以色列初创公司[illumex](https://illumex.ai/)正在解决这个问题，它称之为数据存储和人工智能应用程序之间的“生成语义结构”，自动创建公司所有数据的知识图谱，包括其含义、上下文和使用情况，以根据业务功能创建本体。

illumex 创始人兼首席执行官[Inna Tokarev Sela](https://www.linkedin.com/in/innatokarev/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=il)表示，这种对齐的业务含义和特定领域的上下文使组织能够信任其人工智能计划的结果。

## 创建知识图谱

Gartner [敦促企业采用语义方法](https://info.cambridgesemantics.com/gartner-adopt-a-data-semantics-approach-to-drive-business-value#:~:text=Per%20Gartner%C2%AE%2C%20%E2%80%9CData%20and,value%20and%20break%20data%20silos.%E2%80%9D) 来处理企业数据，以打破数据孤岛并推动业务价值。它建议使用[知识图谱](https://thenewstack.io/using-chatgpt-for-questions-specific-to-your-company-data/) 作为机器可读的数据结构来表示语义知识。其报告指出：

- 当您想要理解和描述事物的工作原理和关系，或者需要明确地交换或重用数据时，语义模型是必要的。
- 不使用语义建模的企业在获取和整合外部数据或公开内部数据以用于下游任务方面的能力有限。
- 生成式人工智能技术的应用加速了填充知识图谱和根据已知关系标记文档的过程。这项技术降低了丰富数据语义的障碍，并提高了数据互操作性。

在您[将人工智能应用于公司数据](https://thenewstack.io/using-chatgpt-for-questions-specific-to-your-company-data/)之前，您需要对所涉及的术语有一致的定义，但很多时候这种情况并没有发生。

“首先，有时关系型结构化数据没有被正确标记。它包含各种缩写和部分命名。一些数据库的字符限制为八个字符。因此，它们在底层数据中使用了各种各样的创造性名称。为了能够将语义模型与 RAG [检索增强生成] 或其他技术一起使用，您首先需要对所有数据进行语义标记。因此，这就像质量控制，”Sela 说。

首先，该平台[映射公司所有来源的现有数据](https://thenewstack.io/data-fabric-or-data-mesh-find-the-happy-medium/)：数据库、仓库、数据湖和业务应用程序。它通过分析公司各种结构化数据集的元数据来创建知识图谱。该数据的业务逻辑被嵌入到数据血缘中，以及有关术语、工作流程、指标、分析和每个业务功能的标签的行业知识。

“我们结合了数十种语义模型，并非所有模型都是大语言模型，其中一些不是传统的模型，还有一些图模型。它们实际上理解客户现有元数据和使用情况的结构——其关键查询的模式结构，以及业务应用程序的结构。这让我们对现有使用情况的初始理解，”她说。

这些数据可以显示客户与产品、供应商、SKU 等相关联。

“因此，它归结为一个非常丰富的图谱，其中包含所有现有的连接、指标、嵌入其中的分析，以及来自行业知识的所有可能且相关的疑问，也嵌入其中，”她说。

## 跟踪使用情况的发生

Sela 曾在 Sisense 担任助理副总裁兼人工智能主管，并在 SAP 担任机器学习高级总监，她于 2021 年创立了 illumex。其企业用户包括以色列的 Teva 制药工业和纽约的 Carson Optical。该公司最近宣布获得 1300 万美元的种子轮融资。
Illumex continuously monitors and updates its knowledge graph as it receives information about changes in meaning or usage. You can track the origin and transformation of data elements across your entire data ecosystem. You can also see the potential impact of changing one data element on other tables, reports, BI dashboards, or even specific charts.

It interprets prompt questions to map queries to the correct semantics and data objects, and translates prompts into SQL that can be used in GenAI tools like ChatGPT or Llama.

**RAG's Problems**
While touted as a way to augment business AI models with other, more relevant information (like internal company data), illumex product manager Sagi Keren likens setting up RAG to [assembling IKEA furniture without instructions](https://illumex.ai/blog/dont-get-ragged-by-your-rag-why-generative-semantic-fabric-is-the-future/). It requires data preparation, including consistent semantic tagging, setting up vector embeddings, and ongoing maintenance.

This requires tools and processes to continuously monitor the appropriate source and freshness of data to prevent hallucinations or simply irrelevancy. He also pointed to the unexpected costs of calling vector databases too frequently via APIs.

In addition to needing consistent tagging, RAG also needs examples of how the data is used to fine-tune it. Sele said these samples often don't cover all the possible uses of the data.

"You just provide a sample... it can be customized to a certain extent. That's why companies still struggle to get consistent results because that training doesn't really allow for all the questions to be consistent. It even has limited ability to provide reliability when repeating the same question," she said.

"So when you use RAG, it only addresses semantic proximity. Right? It doesn't really address the context of the question. In generative semantic fabric, you actually embed the relationships. So [it] understands that a customer belongs to a specific ID or group. It can actually ask about the sales context or marketing... and it has many contexts embedded."

Sele said while semantic consistency was previously handled through catalogs, that approach doesn't scale in the AI era. Automated [semantic layers](https://thenewstack.io/demystifying-the-metrics-store-and-semantic-layer/) should help alleviate friction between data business users and the technical side.

"I personally don't believe that people who do their daily jobs have to understand how the algorithms work or how the data is named and where it's stored," she said.

"Even if the question is not phrased exactly in the language that the database backend uses, you can... match the customer's question with the right business terms, the right metrics... and then, because its mapping is deterministic, we're able to create SQL from that to run the data source or automatically apply context to any type of LLM runtime. So you can pull in Hugging Face, GPT, and other technologies, as well as

The knowledge graph enables governance teams to see all agreed-upon definitions and control the output users will get. We create automated context for them," she said, adding that this means there's no lock-in to a specific GenAI vendor.

The system integrates with tools like Slack and Microsoft Teams so users can submit queries using natural language.

They can say, "'Okay, this is your question. This is how we understand it.' That will help the customer define this; this is the data source. This is how they understand the logic of your question. So they will also provide feedback to the end user to understand if the conditions are understood and mapped correctly to the underlying data," she said.

In addition to generating a real-time business glossary, it provides column-level lineage of data, automatic tagging of personally identifiable information (PII), data exploration capabilities, and alerts for things like duplicate work, major changes, and the projected impact of changes. Its AI assistant can automatically generate suggested business terms and metrics. With collaborative analytics capabilities, saved queries automatically provide business context, such as data source, usage patterns, associated business terms, and related analyses.

As part of its AI-ready governance, it enables data teams to understand data lineage and apply governance and compliance workflows.

Gartner says [illumex faces the same challenges as any vendor that relies on knowledge graphs, semantics, and metadata](https://get.promethium.ai/cool-vendor-successful-generative-ai-projects-require-better-metadata-management): they need to be widely educated for enterprise-level use.
报告指出，“由于行业仍在努力制定开放的元数据共享标准，illumex 可能会发现难以维持对双向元数据共享的支持。”

[YOUTUBE.COM/THENEWSTACK 科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看所有播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)