<!--
title: OpenAI RAG还是定制RAG？
cover: https://cdn.thenewstack.io/media/2023/12/8a2ffe0e-shirts-1024x682.jpg
-->

OpenAI助手支持的RAG系统与Milvus向量数据库驱动的定制版本性能对比。

> 译自 [OpenAI RAG vs. Your Customized RAG: Which One Is Better?](https://thenewstack.io/openai-rag-vs-your-customized-rag-which-one-is-better/)，作者 Cheney Zhang。

最近引入的 OpenAI 助手检索功能在人工智能社区引起了广泛讨论。这一内置功能集成了[检索增强生成（RAG）](https://zilliz.com/use-cases/llm-retrieval-augmented-generation?utm_source=vendor&utm_medium=referral&utm_campaign=2023-12-15_blog_openai-rag-vs-custom-rag_tns)能力，用于问答，使 GPT 语言模型能够利用额外的知识生成更准确和相关的答案。[这篇 Zilliz 文章](https://zilliz.com/blog/customizing-openai-built-in-retrieval-using-milvus-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2023-12-15_blog_openai-rag-vs-custom-rag_tns)探讨了 OpenAI 内置的 RAG 检索的限制，并讨论了创建定制检索解决方案可能有益的情境。

让我们将 OpenAI 的 RAG 与基于像 [Milvus](https://zilliz.com/what-is-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2023-12-15_blog_openai-rag-vs-custom-rag_tns) 这样的向量数据库构建的定制 RAG 的性能进行比较。我们将评估每种方法的优势、劣势和细微差别，并回答一个关键问题：哪个更好？

## 什么是检索增强生成？

在我们评估 OpenAI 内置的 RAG 与定制 RAG 系统之前，让我们首先了解一下什么是 RAG。

[RAG](https://zilliz.com/use-cases/llm-retrieval-augmented-generation) 是一个人工智能框架，从外部知识库检索事实，以确保[大型语言模型（LLMs）](https://zilliz.com/glossary/large-language-models-(llms)?utm_source=vendor&utm_medium=referral&utm_campaign=2023-12-15_blog_openai-rag-vs-custom-rag_tns)基于最准确和最新的信息。一个典型的 RAG 系统[包括一个 LLM](https://roadmap.sh/guides/introduction-to-llms)，像 [Milvus](https://milvus.io/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-12-15_blog_openai-rag-vs-custom-rag_tns) 这样的向量数据库以及一些代码作为提示。

## RAG 评估工具：Ragas

评估 RAG 性能是复杂的。我们需要一个公正客观的 RAG 评估工具，以在合适的数据集上评估多个指标，确保可重现的结果。

[Ragas](https://docs.ragas.io/en/latest/) 是一个致力于评估 [RAG 系统](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/)性能的开源框架。它提供了一系列评分指标，测量 RAG 系统不同方面的性能，以提供对 RAG 应用质量的全面多角度评估。

我们将使用忠实度、答案相关性、上下文精度、答案相似性和答案正确性作为评估 OpenAI RAG 和我们定制的 RAG 系统的主要指标。

- **忠实度：** 评估在给定上下文中生成的答案的事实准确性。
- **答案相关性：** 评估生成的答案与问题的相关性。
- **上下文精度：** 分析检索到的上下文的信噪比，并在上下文中排名地面真实相关的项。
- **答案正确性：** 评估生成的答案与基于事实的准确性。
- **答案相似性：** 评估生成的答案与基于事实之间的语义相似度。

查阅 [Ragas 文档](https://docs.ragas.io/en/latest/concepts/metrics/index.html)以获取有关 Ragas 和所有指标的更详细信息。

## RAG 评估数据集：FiQA

我们选择了[金融舆情挖掘与问答（FiQA）](https://sites.google.com/view/fiqa/)数据集进行评估。这个数据集具有一些特性，使其成为我们评估的理想选择，包括：

- 这包含了高度专业化的金融知识，不太可能出现在 GPT 模型的训练数据中。
- 最初设计用于评估信息检索能力，因此提供了作为标准答案（基于真实）的良好注释的知识片段。
- Ragas 及其社区广泛认可 FiQA 作为标准的入门测试数据集。

## 设置 RAG 系统

现在，让我们构建两个 RAG 系统进行比较：一个是 OpenAI RAG，另一个是基于 [Milvus 向量数据库](https://zilliz.com/what-is-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2023-12-15_blog_openai-rag-vs-custom-rag_tns)构建的定制 RAG。

### 设置 OpenAI RAG

我们将使用 OpenAI 助手按照 [OpenAI 官方文档](https://platform.openai.com/docs/assistants/tools/knowledge-retrieval)构建 RAG 系统，包括构建助手，上传外部知识，检索上下文信息和生成答案。所有其他设置将保持默认。

### 设置使用 Milvus 的定制 RAG

我们必须手动设置使用 Milvus 向量数据库存储外部知识的定制 RAG 系统。我们将使用 HuggingFace 的 `BAAI/bge-base-en` 作为嵌入模型，并使用各种 [LangChain](https://zilliz.com/blog/langchain?utm_source=vendor&utm_medium=referral&utm_campaign=2023-12-15_blog_openai-rag-vs-custom-rag_tns-ultimate-guide-getting-started) 组件进行文档导入和代理构建。

有关详细信息，请参阅这个[分步指南](https://github.com/milvus-io/bootcamp/blob/master/evaluation/README.md)。

### 配置比较

我们在下表中总结了两个 RAG 系统的配置细节。更多信息，请查看我们的[实现](https://github.com/milvus-io/bootcamp/tree/master/evaluation)代码。

![](https://cdn.thenewstack.io/media/2023/12/47eb5931-screenshot3.jpg)

*OpenAI RAG 和定制 RAG 的配置比较*

如上表所示，两个 RAG 系统均使用 `gpt-4-1106-preview` 作为 LLM 模型。定制的 RAG 使用 [Milvus 作为向量数据库](https://thenewstack.io/what-is-milvus-vector-database/)。然而，OpenAI RAG 并未透露其内置的向量数据库或其他配置参数。

## 评估结果与分析

使用 Ragas，我们对两个 RAG 系统进行了多个指标的评分，包括上下文精度、忠实度、答案相关性、相似性和正确性。下图显示了我们从 Ragas 中获得的实验分数。

![](https://cdn.thenewstack.io/media/2023/12/3a7e15e4-image1.png)

*OpenAI RAG vs. 定制 RAG 在 Ragas 指标上的对比*

虽然在答案相似性方面，OpenAI RAG 系统略优于 Milvus 驱动的定制 RAG 系统，但在其他关键指标方面表现稍逊，包括上下文精度、忠实度、答案相关性和答案正确性。

Ragas 还使我们能够使用 Ragas Scores 比较两个 RAG 系统，这是通过计算各种指标的调和平均值生成的平均值。调和平均值用于惩罚得分低的项目。Ragas 分数越高，RAG 系统的整体性能越好。下图显示了两个 RAG 系统的 Ragas 分数。

![](https://cdn.thenewstack.io/media/2023/12/c9b0f730-image2.png)

*OpenAI RAG vs. Milvus 驱动的定制 RAG 在 Ragas Scores 上的对比*

如图所示，Milvus 驱动的定制 RAG 系统的 Ragas 分数高于 OpenAI RAG 系统。

在 Ragas 分数和其他关键指标（包括上下文精度、忠实度、答案相关性和正确性）方面，Milvus 驱动的定制 RAG 系统优于 OpenAI RAG 系统。

## 为什么定制 RAG 优于 OpenAI 的内置 RAG？

经过多次比较，我们发现基于向量数据库的定制 RAG 流程比基于 OpenAI 助手的 RAG 系统表现更好。为什么呢？以下是一些最重要的原因。

### OpenAI 助手依赖内部预训练知识而非外部知识

由于其内部代理设置，OpenAI 助手更依赖预训练而非上传的知识。例如，当被问及高中个人财务课程时，OpenAI RAG 系统提供的答案依赖于与基底真相不同的东西。

**问题：**

高中是否有个人财务/理财课程？

**OpenAI RAG 系统的答案：**确实有一些高中教授个人财务和理财课程，尽管这类课程的可用性和要求因国家而异，甚至在一个国家的不同地区也可能差异巨大。以美国为例，经济教育理事会（CEE）进行调查并报告 K-12 学校的财务教育情况。根据他们的调查，截至我上次更新的时候，越来越多的州已将个人财务纳入其教育标准，并有些已经要求学生在毕业前学习个人财务课程。

尽管我无法访问实时数据库或最新研究，但您通常可以通过以下方式获取有关学校财务教育的信息：

1. 查看政府教育网站。

2. 查阅财务教育非营利组织和理事会的报告。



3. 联系当地学校董事会或教育部门。

如果您对特定地点感兴趣或有特定的关注点，请告诉我，我可以提供更直接的信息（如果可用）。



**定制 RAG 系统的回答**
一些高中确实开设了个人财务和理财课程，但这类课程的可用性和要求差异很大。例如，在得克萨斯州休斯顿，一所私立高中提供了一门选择性的半学期个人财务课程，该课程不计入毕业学分。康涅狄格州韦斯特波特的史泰普斯高中引入了一门以使用数学发展财务素养技能为重点的个人财务管理课程，涵盖了收入、银行业务、信用卡、贷款、税收、保险、投资、预算和购买个人财产等主题。密歇根州安娜堡的公立学校提供了一个包括基本货币管理主题的公民课程。此外，在英国，“每个孩子都重要”框架将“取得经济福祉”作为一个重要元素，并且一些学校使用学校奖励系统来教授孩子有关财务和经济的知识。尽管这些例子显示出这类课程存在，但它们并非普遍要求或标准化，课程的深度和焦点可能有所不同。

**数据集中的真实情况**
“我在美国得克萨斯州休斯顿的一所私立高中读书时，他们设有一门半学期的个人财务课程，但这是可选的，不会计入毕业学分。不过你说得对，这应该是一门标准课程。毕竟，在成年生活中谁都需要这些信息，而且并非每个人都上大学。”

…



“我在高中一年级的时候上过一门公民课。那是在密歇根州安娜堡的公立学校上的。它涵盖了非常基础的内容（如如何平衡支票账户、什么是股票、所得税如何工作、什么是利息等）以及对政治和法律体系的概述。不过，那门课很轻松，没有深入探讨个人财务和理财。我同意这样的课程会非常有价值，还有烹饪、营养和基本的家居和汽车维修。”

虽然 OpenAI RAG 系统的回答并没有错，但它缺乏具体性，而且对于无法获取最新研究的承认表明对上传文档知识的使用不完整。相比之下，定制 RAG 系统通过无缝整合地面真相中的具体信息提供了更准确的答案。这种比较展示了定制 RAG 在有效利用外部数据方面的卓越能力，使其成为更可靠和高效的解决方案。

**定制 RAG 在文档分割和数据检索方面优于 OpenAI RAG**

OpenAI 的知识分割和检索策略可能需要优化。有时，检索到的片段是不足的，例如对于有关 IRA 投资的问题，仅提供“PROS: CONS”。相比之下，定制 RAG 流程在回忆相关片段方面表现出色，提供了更全面的回答。

**问题：**更深入参与 IRA 投资的利弊。



由 OpenAI RAG 检索到的片段	`[‘PROS: CONS’]`
由定制 RAG 检索到的片段	`[‘在税率上有很大的不同，被征税的金额也有显著的差异。因此，从 IRA 中提款通常不是一个好主意，你从 IRA 中提款的情况通常不如从可征税的投资中提款（从税收的角度来看）。这是有意设计的。’`

`‘听起来像个坏主意。IRA 建立在复利的基础上。撤回贡献将损害你的退休储蓄，你永远也无法弥补这个损失。相反，考虑无税投资、州债、联邦债、市政债券等。例如，我投资于加利福尼亚市政债券基金，每年给我提供约 3-4% 的红利收入，完全免税。此外，你的基金持有还会有资本增值。当然，存在风险，例如利率变动将影响收益和资本增值，因此请咨询在这个领域有经验的人（或在这里问其他基础问题）。这将给你带来与你从 Roth IRA 中期望的相同的结果，而不会损害你的退休储蓄潜力。’`

`‘除了 George Marian 的出色建议之外，我要补充一点，如果你已经达到 IRA 贡献的上限，那么你应该回到你的 401(k)。因此，先投入足够的钱到你的 401(k) 以获得匹配资金，然后将 IRA 的贡献最大化，以便让你获得更多和更好的投资选择，然后再回到你的 401(k)，直到你也达到上限，假设你有足够的可投资金额用于退休。’



“尽管税收推迟是一个不错的特性，但 401k 并非圣杯。我见过很多 401k 的投资选择很糟糕：表现低劣，费用高昂，选择有限。很高兴你已经最大化了你的 Roth IRA。我对此表示赞赏。只要你的 401k 中的投资选择不错，我会坚持使用它。”

“为他们提供良好便宜的指数基金的退休计划。这些人可能不需要太担心。最后，拥有两个账户更加复杂。请联系比我更了解税收的人，以确定在同一年为两个 IRA 和 401(k) 捐款有哪些限制。”

OpenAI Assistants 检索到了错误的片段。相比之下，定制 RAG 检索到了更相关的片段，提供了更全面的回答，符合问题的细微差别。

其他原因
OpenAI Assistants 不允许用户调整 RAG 流水线的参数进行定制或优化。然而，使用定制 RAG，用户可以完全灵活地进行调整和优化。
OpenAI Assistants 存在文件存储限制，而 Milvus 驱动的定制 RAG 可以快速扩展而没有上限，这使其成为需要更大存储容量的用户更好的选择。
结论



通过使用 Ragas 评估工具进行全面比较和分析，突显了 OpenAI RAG 和基于 Milvus 等向量数据库的定制 RAG 的优劣势。虽然 OpenAI 的 RAG 在检索方面表现良好，但定制 RAG 在回答质量和相关性、召回性能等多个方面都表现出色。寻求强大有效的 RAG 应用程序的开发人员将发现，基于向量数据库的 RAG 解决方案的灵活性和能力更可取，能够取得更好的结果。

Cheney Zhang 是 Zilliz 公司的一位资深算法工程师。凭借对尖端人工智能技术（如 LLMs 和检索增强生成 RAG）的深厚热情和专业知识，Cheney 积极参与了许多创新的人工智能项目，包括 Towhee、Akcio 等...
阅读更多关于 Cheney Zhang 的信息

