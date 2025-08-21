
<!--
title: Docling：化非结构化数据为 RAG 引擎燃料
cover: https://cdn.thenewstack.io/media/2025/08/a6ad91e2-data.jpg
summary: RAG通过检索外部数据增强LLM，但处理非结构化数据是瓶颈。Docling是一个开源工具，用于解析文档并将其转换为易于GenAI应用程序使用的格式，简化RAG流程，平衡了灵活性和稳定性。
-->

RAG通过检索外部数据增强LLM，但处理非结构化数据是瓶颈。Docling是一个开源工具，用于解析文档并将其转换为易于GenAI应用程序使用的格式，简化RAG流程，平衡了灵活性和稳定性。

> 译自：[From Unstructured Data to RAG-Ready With Docling](https://thenewstack.io/from-unstructured-data-to-rag-ready-with-docling/)
> 
> 作者：Shivay Lamba

检索增强生成 (RAG) 已成为对抗大型语言模型 (LLM) 内容生成中出现的幻觉和其他不准确性的主要方法。然而，RAG 要想有效且高效地扩展，需要合适的数据架构。

如今，公司从其知识产权、运营程序以及营销、销售和客户互动中生成大量数据。 最大的挑战不是收集这些数据，而是提取可用于显著改善客户服务和上市时间的有意义的见解。

[GenAI](https://thenewstack.io/genai-is-quickly-reinventing-it-operations-leaving-many-behind/) 承诺弥合这一差距，使用户能够将大量组织数据转化为更有用的信息。 然而，当数据格式与 LLM 不完全兼容时（例如 PDF 文件或专有文档），这会成为一个障碍。 转换这些数据，使其[可供 LLM 使用](https://thenewstack.io/what-is-a-large-language-model/)，以支持组织需求，可能是一项资源密集且耗时的任务。

首先，组织需要将文档预处理成可供 LLM 使用并用于 [RAG 工作流](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)的格式。 这不仅仅涉及光学字符识别 (OCR) 或[文本提取](https://thenewstack.io/top-10-nlp-tools-in-python-for-text-analysis-applications/)。 这需要提取提供上下文的数据，并实施文档元素感知技术。 例如，如果一个表格跨越多个页面，则必须将其提取为单个表格。 如果文档的布局由包含图像、表格和文本等元素的多个列组成，则应单独提取每个元素，保持其标识及其提取的上下文。

## RAG 使 LLM 更智能、更准确

RAG 是一种旨在克服 LLM 局限性并提供更准确和详细响应的框架。 尽管 LLM 在大量数据集上进行训练，但它们通常难以应对专业知识、最新信息和生成事实上不正确的输出，也称为“幻觉”。 RAG 通过实时动态地从外部来源检索相关数据来缓解这些问题。

RAG 分两个主要阶段运行：摄取阶段和推理阶段。 在摄取阶段，来自外部知识来源的数据会被清理和转换。 必须摄取原始文件并去除噪声。 这可能涉及删除样板文本或不相关的页眉和页脚以及标准化文档编码。 由于保留用于检索的信息保真度至关重要，因此必须将文档分解为有凝聚力的、具有上下文意义的块。 一个块可以是一个段落、列表项、表格或标题。 每个块或段落都富含元数据：来源、节标题、时间戳、标签、作者身份等。 这有助于过滤结果。

在此阶段，向量化将数据转换为嵌入，即多维空间中的数值表示。 生成的嵌入通常存储在向量数据库中，以便在推理期间进行有效检索。

在推理阶段，首先嵌入用户的查询，并将其与外部知识来源的嵌入进行比较。 相似性搜索检索与查询最接近（最相关）的数据点。 之后，将最相关的检索数据插入到预定义的提示模板中。 然后将增强的提示发送到 LLM，LLM 根据其语言理解和外部数据生成上下文相关的响应。 LLM 的提示是从检索到的段落动态组成的，为基于事实的生成设置了严格的界限。 最后，将上下文数据馈送到模型，并使用文档检索系统检索相关文档。

[![RAG 流程：从数据到响应](https://cdn.thenewstack.io/media/2025/08/74369fa4-image2-1024x939.png)](https://cdn.thenewstack.io/media/2025/08/74369fa4-image2-1024x939.png)

*来源：Napkin AI*

鉴于 RAG 包含如此多的步骤，我们将重点关注非结构化数据摄取，因为它通常是最难解决的挑战。

## 非结构化数据是瓶颈

组织正在生成大量数据，包括文本、文档、图像、日志、代码注释、支持电子邮件、报告、手册、聊天记录和文档。 对于大多数组织而言，处理这种种类和数量的非结构化数据是一个挑战。

为什么？ 因为非结构化信息有多种格式：DOCX、PDF、Markdown、网页、原始 HTML、扫描图像等等。 它缺乏架构或一致性，这意味着没有两个团队使用相同的模板。 字段是可选的，并且文档会随着时间的推移而发生变化。 它还包含大量噪声，例如错别字、重复内容、样板或不相关的语言。 由于它不断增长和变化，因此今天准确、相关和最新的内容明天可能就会过时。

将大量非结构化数据转化为可用、可查询的结构化资源是一项艰巨的任务。

## 为什么当前的工具会让开发者感到沮丧

已经涌现出数百种开源和商业工具来解决这个问题的一些方面：用于摄取的 ETL（提取、转换、加载）框架、用于分割的 NLP（自然语言处理）库、用于向量化的嵌入模型、用于检索的混合搜索引擎以及用于将所有内容链接在一起的定制脚本或编排器。

但是，这个生态系统也带来了自身的问题：工具很少在架构或 API 上达成一致，集成很脆弱，并且在不断增长的数据集中维护端到端管道既耗时又容易出错。 开发者常常只能拼凑一次性的工作流程，这些工作流程难以扩展、审计或随着需求的发展而扩展。

因此，我们需要一种能够降低这种复杂性，同时推动强大的开发者体验的解决方案。

## 结构化数据的开源方法：Docling

[![Docling 标志](https://cdn.thenewstack.io/media/2025/08/8d7fdb00-image1-1024x428.png)](https://cdn.thenewstack.io/media/2025/08/8d7fdb00-image1-1024x428.png)

*来源：GitHub*

Docling 是 [IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention) 研究部门制作的开源工具。 它用于解析文档（从 PDF 和 DOCX 到 PPTX 和 HTML 等），并将它们转换为 Markdown 或 JSON 等格式，从而更轻松地为 GenAI 应用程序准备内容。 它支持高级 PDF 处理 OCR 以用于扫描文档，并与 LlamaIndex 和 LangChain 等工具集成以用于 RAG 和问答任务。 其宽松的开源 MIT 许可证允许开发者协作和扩展项目以满足他们的需求。

Docling 的理念很简单：管道应该是模块化的、有主见的和可扩展的，同时消除组装您自己的数据解析器和分块器的重复、容易出错的苦力。

Docling 提供模块化的源连接器。 它包含适用于最常见文件格式（Markdown、PDF、HTML 等）的内置适配器，从而可以轻松地添加新的数据源。 对于每种文档格式，文档转换器都知道要使用哪个特定于格式的后端来解析文档，以及使用哪个管道来编排执行。 它还提供一致的数据建模。 每个提取的片段都包装在一个明确指定的数据模型中，其中直接嵌入了文档、节和实体元数据。

自动分块和注释变得容易。 Docling 推断逻辑中断——无论是节标题、段落还是表格行——并相应地对其进行注释。 此外，Docling 的管道可以通过用户定义的处理器进行扩展。 通过提供可扩展的插件，可以简化附加自定义元数据或与下游标记或丰富服务集成。

Docling 使用[混合分块策略](https://thenewstack.io/augmenting-multi-and-hybrid-cloud-strategies-with-databases/)，该策略实际上了解您的文档结构，在创建用于嵌入的最佳块的同时保留上下文。

来自其他提供商的大多数基本分块器纯粹按字符数（例如每 1,000 个字符）分割文本。 Docling 是不同的。 它尊重段落、节、表格和图像； 维护语义边界，使块有意义且独立； 并智能地处理表格和图像，因此您的嵌入不仅仅是乱码 OCR 文本。

这意味着当以后查询数据时，会检索到上下文丰富的块，而不是随机的句子片段。

## 如何开始使用 Docling

要开始使用 Docling，只需安装 pip 包。

`pip install docling`

安装完成后，您可以在 Python 模块中以编程方式进行文档转换，或使用 Docling 命令行界面 (CLI)。

```py
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # PDF 路径或 URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "### Docling Technical Report[...]"

# docling https://arxiv.org/pdf/2206.01062
```

## 使用 Docling 的示例 RAG 管道

由 Docling 提供支持的 RAG 工作流的高级流程可以从抓取和摄取开始，或者在内容存储库上运行 Docling 的源连接器。 然后可以将解析和分块用于 Docling 发出的 JSON 片段，其中包含每个片段的内容、上下文和元数据。 然后可以将块和嵌入发送到索引阶段的向量数据库。 之后，可能会发生检索和生成，这意味着，当用户或 AI 代理提出问题时，会检索到最佳匹配的嵌入，并在受控提示中将其提供给 LLM。

使用 Docling，不再需要临时脚本或处理各种数据架构。 像 Docling 这样的开源项目确保您不会被迫提交给单个供应商或堆栈。 因此，Docling 在 DIY 的灵活性和使用平台交付的 RAG 管道的稳定性之间取得了平衡。

## 汇集在一起

每个组织都有大量的非结构化数据。 理论上，RAG 提供了一种将这些数据转换为有用的东西的方法，但前提是开发者可以可靠地构建这些数据并管理知识的流动。 这就是像 Docling 这样的开源框架的闪光点。

数据管道生态系统仍然高度分散。 许多组织陷入“框架疲劳”。 每项新需求，例如处理新的文件类型或支持新的分块策略，似乎都需要一个新的库。 需要中断库的版本、处理不完整的文档以及缺乏最佳实践可能会使进入此类生态系统的开发者不知所措。

这就是为什么集成式、有主见的解决方案变得如此有吸引力。 这些平台，如 [Couchbase Capella AI Services](https://www.couchbase.com/products/ai-services/)，通过非结构化数据服务为向量和 RAG 工作流提供统一的非结构化数据摄取和转换。 它不是管理不同的移动部件，而是提供专门为稳健性和易于扩展性而设计的平台工作流。

要了解 Capella AI Services 如何解决开发者最关键的 GenAI 问题，请单击[此处](https://www.couchbase.com/products/ai-services/)。 您也可以在此处注册 Capella AI Services 的私有预览[此处](https://info.couchbase.com/capella-ai-services-signup?_gl=1*pfu69a*_gcl_aw*R0NMLjE3NTQ1ODIwOTMuQ2owS0NRanduZEhFQmhEVkFSSXNBR2gwZzNCMFdxSklOdnh0SmU5djl3Nzd4MHVRZ2hnZVBDWE1MU1BYZmt0eWV5OTFWZEFNeEMwcGVRUWFBdko2RUFMd193Y0I.*_gcl_au*ODYwOTQwNDUuMTc1NTExNzI4Nw..)。