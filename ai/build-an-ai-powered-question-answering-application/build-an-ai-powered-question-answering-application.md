
<!--
title: 构建一个 AI 驱动的问答应用程序
cover: https://cdn.thenewstack.io/media/2024/09/6e14ce9f-ai-powered-question-answering-application.jpg
-->

了解检索增强生成 (RAG) 工具 Haystack 和 Milvus，同时构建一个 AI 驱动的食谱应用程序。

> 译自 [Build an AI-Powered Question-Answering Application](https://thenewstack.io/build-an-ai-powered-question-answering-application/)，作者 Jason Myers。

您拥有大量数据 - 结构化、非结构化，应有尽有 - 并且您希望将其用于应用程序。无论您是想获得见解还是寻找答案，您都需要一个能够快速准确地提供结果的解决方案。有了合适的工具，这可能比您想象的更容易。

传统的关键词搜索有其局限性，尤其是在[非结构化数据](https://zilliz.com/learn/introduction-to-unstructured-data?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)加入的情况下。在那种情况下，获得快速、相关结果的机会开始下降。但有一种前进的道路。通过将[Milvus](https://zilliz.com/what-is-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)（一个开源向量数据库）与[Haystack](https://haystack.deepset.ai/) 2.0（Deepset 用于构建端到端大型语言模型 ([LLM](https://zilliz.com/glossary/large-language-models-(llms)?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)) 应用程序和[检索增强生成](https://zilliz.com/learn/Retrieval-Augmented-Generation?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns) (RAG) 流水线的开源框架）结合起来，您可以构建用户和开发人员渴望的那种高级应用程序。

在本文中，我将解释如何利用 Milvus 和 Haystack 2.0 的强大功能，使用检索增强生成 (RAG) 创建一个 AI 驱动的问答应用程序。让我们深入了解！

## 使用 Milvus 存储数据

要使用数据，您首先需要将其存储在某个地方。由[Zilliz](https://zilliz.com?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns) 开发人员维护的 Milvus 是一个开源[向量数据库](https://zilliz.com/learn/what-is-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)，旨在高效地处理高维向量。向量是非结构化数据（文本、照片、音频文件等）在高维空间中的数值表示。

将数据转换为[向量嵌入](https://zilliz.com/glossary/vector-embeddings?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns) 保留了数据点之间的语义含义和关系。这些[嵌入](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai) 在此空间中越靠近，它们在语义上就越相关。当您将这些向量存储在向量数据库中时，您会快速积累相关的嵌入，从而使搜索上下文相关数据的效率更高。

## 选择向量数据库时要考虑的因素

在[选择向量数据库](https://zilliz.com/blog/how-to-evaluate-a-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns) 用于您的 RAG 流水线时，考虑关键功能非常重要。

1. 高维**向量索引：** 向量数据库是否针对高维向量的索引和搜索进行了优化？它应该能够利用高级索引技术，例如分层可导航小世界图（[HNSW](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)）或倒排文件系统（[IVF](https://zilliz.com/learn/vector-index?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)），以创建高效的索引结构。这些索引结构即使在包含数百万或数十亿个向量的海量数据集中也能实现快速相似性搜索。
2. **可扩展性和性能：** 即使您的原型可能使用小型数据集，但规划[生产规模](https://thenewstack.io/scaling-databases-to-meet-enterprise-genai-demands)也很重要。您的向量数据库能否在不牺牲性能的情况下处理海量的向量数据？它应该能够在多个节点或机器之间水平扩展，从而实现分布式存储和并行处理。这种可扩展性确保它能够适应不断增长的数据集和高查询吞吐量，而不会影响应用程序的速度和准确性。
3. **混合搜索：** 您的向量数据库应该支持[混合搜索](https://zilliz.com/blog/a-review-of-hybrid-search-in-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)，使您能够检索跨不同模态或由各种[嵌入模型](https://zilliz.com/ai-models?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)生成的向量。此外，它应该允许您将混合向量搜索与关键字匹配结合起来，以进行更复杂的查询。此功能简化了在向量数据库中查找最相关项目的流程，无论这些项目是基于[元数据](https://zilliz.com/blog/metadata-filtering-hybrid-search-or-agent-in-rag-applications?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)还是表示图像、音频、文本等的向量嵌入。
4. **确保您的向量数据库与流行的[集成](https://zilliz.com/product/integrations?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)** 与流行的机器学习模型：[机器学习模型](https://zilliz.com/ai-models?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)，例如[OpenAI](https://zilliz.com/learn/guide-to-using-openai-text-embedding-models?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)文本嵌入模型，[Cohere](https://zilliz.com/ai-models/embed-multilingual-v3.0?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)多语言模型和[Voyage AI](https://zilliz.com/ai-models/voyage-code-2?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)代码嵌入模型，以简化非结构化数据转换为向量嵌入的过程，以便进行高效的相似性检索。
5. **支持多个索引和距离度量：** 不同的索引算法和[距离度量](https://zilliz.com/blog/similarity-metrics-for-vector-search?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)适用于不同的用例和数据特征。根据您的具体要求，您应该能够[在索引之间进行选择](https://zilliz.com/learn/how-to-pick-a-vector-index-in-milvus-visual-guide?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)，例如 HNSW、IVF、[ANNOY](https://zilliz.com/learn/approximate-nearest-neighbor-oh-yeah-ANNOY?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)或[FAISS](https://zilliz.com/learn/faiss?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)。此外，您可能希望选择欧几里得距离、余弦相似度和内积等距离度量，以便为您的应用程序选择最合适的度量。

## 使用 Haystack 2.0 构建流水线

数据安全存储后，您需要构建流水线以有效地使用它。这就是 Haystack 2.0 发挥作用的地方。Haystack 是一个开源 [Python](https://roadmap.sh/python) 框架，用于构建可用于生产的 LLM 应用程序、RAG 流水线和现代搜索系统，这些系统可以智能地处理大型文档集合。

如何为 LLM 应用程序构建 Haystack 流水线？Haystack 提供了您可以链接起来构建自定义数据流水线的组件。这些组件可以帮助您执行文档检索、文本生成或摘要等任务。您还可以构建自己的组件或使用示例流水线之一作为起点。

[Haystack 2.0 与 Milvus 无缝集成](https://zilliz.com/product/integrations/haystack?utm_source=vendor&utm_medium=referral&utm_campaign=2024-09-20_blog_haystack-milvus_tns)。这意味着开发人员可以快速将他们的数据流水线与 Milvus 的数据存储和检索功能连接起来，从而加速 RAG 流水线和 LLM 应用程序的开发。

## 构建 AI 驱动的应用程序

在接下来的部分中，我将向您展示如何使用流行的 RAG 技术以及 Haystack 2.0 和 Milvus 向量数据库构建一个 AI 驱动的问答食谱应用程序。

### 设置和安装

要开始使用 Haystack 和 Milvus 进行构建，以下说明将引导您构建一个基于 RAG 的示例食谱应用程序，该应用程序允许您提出问题、请求食谱并从一组流行的素食食谱中创建膳食计划。您也可以使用您自己的食谱来使其更加个性化。

首先也是最重要的是，确保您的本地机器上安装了 Python。您需要 3.6 或更高版本。如果您需要更新，请在 [Python 页面](https://www.python.org/) 上获取。

要安装必要的软件包：

```
pip install --upgrade pymilvus milvus-haystack markdown-it-py mdit_plain pypdf sentence-transformers
```

### 构建索引流水线

接下来，您需要构建索引流水线。由于本教程使用 Milvus 作为数据存储，因此您的索引流水线（处理和存储文档）将使用 MilvusDocumentStore。

确保您有一些示例文件可以使用和测试。将您的文件放在名为 **recipe_files** 的文件夹中。您可以使用本示例中使用的 [示例文件](https://drive.google.com/drive/folders/1n9yqq5Gl_HWfND5bTlrCwAOycMDt5EMj)，也可以使用您自己的食谱。如果您更改了文件夹名称或文件路径，请更新示例以反映您的选择。您可能还想在示例代码中实现错误检查、处理和日志记录，以捕获可能出现的任何问题。

**1. 初始化 MilvusDocumentStore**

```py
from milvus_haystack import MilvusDocumentStore
document_store = MilvusDocumentStore(
   connection_args={
  	 "uri": "http://localhost:19530", #Your Milvus service uri
   },
   drop_old=True,
)
```

**2. 配置文档处理所需的组件**

```py

from haystack.components.writers import DocumentWriter
from haystack.components.converters import MarkdownToDocument, PyPDFToDocument, TextFileToDocument
from haystack.components.preprocessors import DocumentSplitter, DocumentCleaner
from haystack.components.routers import FileTypeRouter
from haystack.components.joiners import DocumentJoiner
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack import Pipeline
# Initialize the components you’ll need in your indexing pipeline
file_type_router = FileTypeRouter(mime_types=["text/plain", "application/pdf", "text/markdown"])
text_file_converter = TextFileToDocument()
markdown_converter = MarkdownToDocument()
pdf_converter = PyPDFToDocument()
document_joiner = DocumentJoiner()
 
document_cleaner = DocumentCleaner()
document_splitter = DocumentSplitter(split_by="word", split_length=150, split_overlap=50)
  
document_embedder = SentenceTransformersDocumentEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")
document_writer = DocumentWriter(document_store)
```

**3. 索引文档**

此步骤将 Haystack 组件添加到您的流水线中。确保为每个组件配置输入和输出，并将它们按您希望它们运行的顺序排列。

```py
preprocessing_pipeline = Pipeline()
preprocessing_pipeline.add_component(instance=file_type_router, name="file_type_router")
preprocessing_pipeline.add_component(instance=text_file_converter, name="text_file_converter")
preprocessing_pipeline.add_component(instance=markdown_converter, name="markdown_converter")
preprocessing_pipeline.add_component(instance=pdf_converter, name="pypdf_converter")
preprocessing_pipeline.add_component(instance=document_joiner, name="document_joiner")
preprocessing_pipeline.add_component(instance=document_cleaner, name="document_cleaner")
preprocessing_pipeline.add_component(instance=document_splitter, name="document_splitter")
preprocessing_pipeline.add_component(instance=document_embedder, name="document_embedder")
preprocessing_pipeline.add_component(instance=document_writer, name="document_writer")
 
preprocessing_pipeline.connect("file_type_router.text/plain", "text_file_converter.sources")
preprocessing_pipeline.connect("file_type_router.application/pdf", "pypdf_converter.sources")
preprocessing_pipeline.connect("file_type_router.text/markdown", "markdown_converter.sources")
preprocessing_pipeline.connect("text_file_converter", "document_joiner")
preprocessing_pipeline.connect("pypdf_converter", "document_joiner")
preprocessing_pipeline.connect("markdown_converter", "document_joiner")
preprocessing_pipeline.connect("document_joiner", "document_cleaner")
preprocessing_pipeline.connect("document_cleaner", "document_splitter")
preprocessing_pipeline.connect("document_splitter", "document_embedder")
preprocessing_pipeline.connect("document_embedder", "document_writer")
```

**4. 运行流水线**

```py
from pathlib import Path
 
output_dir = "recipe_files"
preprocessing_pipeline.run({"file_type_router": {"sources": list(Path(output_dir).glob("**/*"))}})
 
print(document_store.count_documents())
```

索引处理文档，将它们转换为文本，将它们拆分为块，并将这些块嵌入到高维向量中。

### 集成 RAG 流水线

RAG 流水线将文档检索与使用 LLM 生成答案相结合。对于本示例，您需要一个 [OpenAI 密钥](https://thenewstack.io/beginners-guide-to-openai-text-embedding-models)。将其设置为环境变量 `OPENAI_API_KEY`。有关 Haystack 支持的模型的完整列表，请参阅 [Haystack 的文档](https://docs.haystack.deepset.ai/docs/generators)。

```py
Set up the RAG pipeline

from haystack import Pipeline
from haystack.utils import Secret
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.builders import PromptBuilder
from haystack.components.generators import OpenAIGenerator
 
from milvus_haystack.milvus_embedding_retriever import MilvusEmbeddingRetriever
 
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

 
template = """
Answer the questions based on the given context.
 
Context:
{% for document in documents %}
   {{ document.content }}
{% endfor %}
 
Question: {{ question }}
Answer:
"""
 
rag_pipeline = Pipeline()
rag_pipeline.add_component("embedder", SentenceTransformersTextEmbedder(model="sentence-transformers/all-MiniLM-L6-v2"))
rag_pipeline.add_component("retriever", MilvusEmbeddingRetriever(document_store=document_store))
rag_pipeline.add_component("prompt_builder", PromptBuilder(template=template))
rag_pipeline.add_component("llm", OpenAIGenerator(generation_kwargs={"temperature": 0}))
 
rag_pipeline.connect("embedder.embedding", "retriever.query_embedding")
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")
 
question = (
   "What ingredients would I need to make vegan keto eggplant lasagna, vegan persimmon flan, and vegan hemp cheese?"
)
 
response = rag_pipeline.run(
   {
  	 "embedder": {"text": question},
  	 "prompt_builder": {"question": question},
   }
)
 
print(response)
 
{'llm': {'replies': ['To make vegan keto eggplant lasagna, you would need ingredients such as eggplants, basil, almonds, nutritional yeast, olive oil, tofu, spinach, lemon, garlic powder, macadamia nuts, agar agar, and vegan mozzarella.\n\nTo make vegan persimmon flan, you would need ingredients such as persimmon pulp, cornstarch, agar agar, agave nectar, granulated sugar, coconut creme, almond milk, and vanilla.\n\nTo make vegan hemp cheese, you would need ingredients such as sunflower seeds, hemp hearts, miso paste, nutritional yeast, rejuvelac, and salt.'], 'meta': [{'model': 'gpt-3.5-turbo-0125', 'index': 0, 'finish_reason': 'stop', 'usage': {'completion_tokens': 130, 'prompt_tokens': 3016, 'total_tokens': 3146}}]}}
```

RAG 流水线根据查询检索相关文档，使用检索到的文档为 OpenAIGenerator 生成提示，并使用 LLM 生成答案。然后，它将生成的答案作为最终输出返回。

## 结论

这是一个基本示例，说明了如何将 Milvus 与 Haystack 2.0 集成。将 Milvus 的向量存储、索引和检索功能与 Haystack 的 RAG 流水线相结合，您可以构建能够有效地处理和评估文档以提供相关答案的系统。希望本示例能帮助您开始构建高级 LLM 应用程序。
