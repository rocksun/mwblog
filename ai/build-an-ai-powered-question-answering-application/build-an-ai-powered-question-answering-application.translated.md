# 构建 AI 驱动的问答应用程序

![构建 AI 驱动的问答应用程序的特色图片](https://cdn.thenewstack.io/media/2024/09/6e14ce9f-ai-powered-question-answering-application-1024x576.jpg)

您拥有大量数据 - 结构化、非结构化，应有尽有 - 并且您希望将其用于应用程序。无论您是想获得见解还是寻找答案，您都需要一个能够快速准确地提供结果的解决方案。有了合适的工具，这可能比您想象的更容易。

传统的关键词搜索有其局限性，尤其是在[非结构化数据](https://zilliz.com/learn/introduction-to-unstructured-data?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)加入的情况下。在那种情况下，获得快速、相关结果的机会开始下降。但有一种前进的道路。通过将[Milvus](https://zilliz.com/what-is-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)（一个开源向量数据库）与[Haystack](https://haystack.deepset.ai/) 2.0（Deepset 用于构建端到端大型语言模型 ([LLM](https://zilliz.com/glossary/large-language-models-(llms)?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)) 应用程序和[检索增强生成](https://zilliz.com/learn/Retrieval-Augmented-Generation?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns) (RAG) 管道的开源框架）结合起来，您可以构建用户和开发人员渴望的那种高级应用程序。

在本文中，我将解释如何利用 Milvus 和 Haystack 2.0 的强大功能，使用检索增强生成 (RAG) 创建一个 AI 驱动的问答应用程序。让我们深入了解！

**使用 Milvus 存储数据**

要使用数据，您首先需要将其存储在某个地方。由[Zilliz](https://zilliz.com?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns) 开发人员维护的 Milvus 是一个开源[向量数据库](https://zilliz.com/learn/what-is-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)，旨在高效地处理高维向量。向量是非结构化数据（文本、照片、音频文件等）在高维空间中的数值表示。

将数据转换为[向量嵌入](https://zilliz.com/glossary/vector-embeddings?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns) 保留了数据点之间的语义含义和关系。这些[嵌入](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai) 在此空间中越靠近，它们在语义上就越相关。当您将这些向量存储在向量数据库中时，您会快速积累相关的嵌入，从而使搜索上下文相关数据的效率更高。

## 选择向量数据库时要考虑的因素

在[选择向量数据库](https://zilliz.com/blog/how-to-evaluate-a-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns) 用于您的 RAG 管道时，考虑关键功能非常重要。

- 高维
**向量索引：** 向量数据库是否针对高维向量的索引和搜索进行了优化？它应该能够利用高级索引技术，例如分层可导航小世界图（[HNSW](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)）或倒排文件系统（[IVF](https://zilliz.com/learn/vector-index?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)），以创建高效的索引结构。这些索引结构即使在包含数百万或数十亿个向量的海量数据集中也能实现快速相似性搜索。**可扩展性和性能：** 即使您的原型可能使用小型数据集，但规划[生产规模](https://thenewstack.io/scaling-databases-to-meet-enterprise-genai-demands)也很重要。您的向量数据库能否在不牺牲性能的情况下处理海量的向量数据？它应该能够在多个节点或机器之间水平扩展，从而实现分布式存储和并行处理。这种可扩展性确保它能够适应不断增长的数据集和高查询吞吐量，而不会影响应用程序的速度和准确性。**混合搜索：** 您的向量数据库应该支持[混合搜索](https://zilliz.com/blog/a-review-of-hybrid-search-in-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)，使您能够检索跨不同模态或由各种[嵌入模型](https://zilliz.com/ai-models?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)生成的向量。此外，它应该允许您将混合向量搜索与关键字匹配结合起来，以进行更复杂的查询。此功能简化了在向量数据库中查找最相关项目的流程，无论这些项目是基于[元数据](https://zilliz.com/blog/metadata-filtering-hybrid-search-or-agent-in-rag-applications?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)还是表示图像、音频、文本等的向量嵌入。确保您的向量数据库与流行的[集成](https://zilliz.com/product/integrations?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)与流行的机器学习模型：[机器学习模型](https://zilliz.com/ai-models?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)，例如[OpenAI](https://zilliz.com/learn/guide-to-using-openai-text-embedding-models?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)文本嵌入模型，[Cohere](https://zilliz.com/ai-models/embed-multilingual-v3.0?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)多语言模型和[Voyage AI](https://zilliz.com/ai-models/voyage-code-2?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)代码嵌入模型，以简化非结构化数据转换为向量嵌入的过程，以便进行高效的相似性检索。**支持多个索引和距离度量：** 不同的索引算法和[距离度量](https://zilliz.com/blog/similarity-metrics-for-vector-search?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)适用于不同的用例和数据特征。根据您的具体要求，您应该能够[在索引之间进行选择](https://zilliz.com/learn/how-to-pick-a-vector-index-in-milvus-visual-guide?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)，例如 HNSW、IVF、[ANNOY](https://zilliz.com/learn/approximate-nearest-neighbor-oh-yeah-ANNOY?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)或[FAISS](https://zilliz.com/learn/faiss?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)。此外，您可能希望选择欧几里得距离、余弦相似度和内积等距离度量，以便为您的应用程序选择最合适的度量。

## 使用 Haystack 2.0 构建管道
数据安全存储后，您需要构建管道以有效地使用它。这就是 Haystack 2.0 发挥作用的地方。Haystack 是一个开源 [Python](https://roadmap.sh/python) 框架，用于构建可用于生产的 LLM 应用程序、RAG 管道和现代搜索系统，这些系统可以智能地处理大型文档集合。

如何为 LLM 应用程序构建 Haystack 管道？Haystack 提供了您可以链接起来构建自定义数据管道的组件。这些组件可以帮助您执行文档检索、文本生成或摘要等任务。您还可以构建自己的组件或使用示例管道之一作为起点。
[Haystack 2.0 与 Milvus 无缝集成](https://zilliz.com/product/integrations/haystack?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)。这意味着开发人员可以快速将他们的数据管道与 Milvus 的数据存储和检索功能连接起来，从而加速 RAG 管道和 LLM 应用程序的开发。

## 构建 AI 驱动的应用程序

在接下来的部分中，我将向您展示如何使用流行的 RAG 技术以及 Haystack 2.0 和 Milvus 向量数据库构建一个 AI 驱动的问答食谱应用程序。

### 设置和安装

要开始使用 Haystack 和 Milvus 进行构建，以下说明将引导您构建一个基于 RAG 的示例食谱应用程序，该应用程序允许您提出问题、请求食谱并从一组流行的素食食谱中创建膳食计划。您也可以使用您自己的食谱来使其更加个性化。

首先也是最重要的是，确保您的本地机器上安装了 Python。您需要 3.6 或更高版本。如果您需要更新，请在 [Python 页面](https://www.python.org/) 上获取。

要安装必要的软件包：

```
pip install --upgrade pymilvus milvus-haystack markdown-it-py mdit_plain pypdf sentence-transformers
```

### 构建索引管道

接下来，您需要构建索引管道。由于本教程使用 Milvus 作为数据存储，因此您的索引管道（处理和存储文档）将使用 MilvusDocumentStore。

确保您有一些示例文件可以使用和测试。将您的文件放在名为 **recipe_files** 的文件夹中。您可以使用本示例中使用的 [示例文件](https://drive.google.com/drive/folders/1n9yqq5Gl_HWfND5bTlrCwAOycMDt5EMj)，也可以使用您自己的食谱。如果您更改了文件夹名称或文件路径，请更新示例以反映您的选择。您可能还想在示例代码中实现错误检查、处理和日志记录，以捕获可能出现的任何问题。

#### 1. 初始化 MilvusDocumentStore
#### 2. 配置文档处理所需的组件
#### 3. 索引文档

此步骤将 Haystack 组件添加到您的管道中。确保为每个组件配置输入和输出，并将它们按您希望它们运行的顺序排列。

**4. **运行管道

索引处理文档，将它们转换为文本，将它们拆分为块，并将这些块嵌入到高维向量中。

### 集成 RAG 管道

RAG 管道将文档检索与使用 LLM 生成答案相结合。对于本示例，您需要一个 [OpenAI 密钥](https://thenewstack.io/beginners-guide-to-openai-text-embedding-models)。将其设置为环境变量 `OPENAI_API_KEY`。有关 Haystack 支持的模型的完整列表，请参阅 [Haystack 的文档](https://docs.haystack.deepset.ai/docs/generators)。

RAG 管道根据查询检索相关文档，使用检索到的文档为 OpenAIGenerator 生成提示，并使用 LLM 生成答案。然后，它将生成的答案作为最终输出返回。

### 结论

这是一个基本示例，说明了如何将 Milvus 与 Haystack 2.0 集成。将 Milvus 的向量存储、索引和检索功能与 Haystack 的 RAG 管道相结合，您可以构建能够有效地处理和评估文档以提供相关答案的系统。希望本示例能帮助您开始构建高级 LLM 应用程序。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)