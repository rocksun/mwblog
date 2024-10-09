# 通过新的 RAG 架构，PDF 文件更容易进入生成式 AI

![Featued image for: PDFs Get an Easier Entry to GenAI via New RAG Architecture](https://cdn.thenewstack.io/media/2024/10/db10f2d2-pdfs-get-easier-entry-genai-rag-arch-1024x576.jpg)

虽然一张图片胜过千言万语，但为 [检索增强生成 (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) 工作流程准备视觉丰富的多模态文档（如 PDF）既耗时又容易出错。在医疗保健或金融服务等对准确性至关重要的行业，放射学报告或财务报表等文档通常包含提供宝贵上下文信息的图像或图表。虽然这些视觉丰富的元素通常被排除在 RAG 工作流程之外，但一种用于从视觉增强文档中检索信息的新方法将简化多模态文档准备，并改变 RAG 和生成式 AI (GenAI) 的潜力。

大多数检索系统主要关注基于文本的表示，而忽略了文档的视觉元素，例如图像、表格和布局。这种限制会降低检索效率，尤其是在这些视觉特征是理解文档内容的关键的情况下。

针对 PDF（或其他复杂格式）的典型现实世界 RAG 管道涉及以下步骤：

- 提取文本和元数据
- 光学字符识别 (OCR)
- 布局分析：提取表格、图表、饼图等。
在完成获取文本表示的处理步骤后，文本可以作为 [检索系统的输入](https://blog.vespa.ai/retrieval-with-vision-language-models-colpali/)。

这些处理步骤可能很耗时，并会影响检索质量，但 Contextualized Late Interaction over PaliGemma ([ColPali](https://arxiv.org/abs/2407.01449)) 是一种新的检索模型架构，专注于文档密集型环境中的 RAG，克服了这些挑战。这种新的检索方法直接将整个渲染后的文档（包括其视觉元素）嵌入到适合检索的向量表示中。

## ColPali 如何改进文档检索

通过将文档视为视觉实体而不是文本，ColPali 为更准确、更具上下文感知的文档检索开辟了新的可能性，尤其适用于视觉丰富的內容。ColPali 通过以下方式代表了文档检索的进步：

- 消除了对复杂预处理步骤的需求
- 保留文档的视觉上下文
- 能够更全面地理解文档
- 简化 RAG 管道

通过绕过传统的文本提取和 OCR 流程，ColPali 不仅简化了检索过程，而且有可能提高 RAG 系统中检索信息的质量和相关性。

ColPali 的架构建立在两个关键概念之上：来自 [视觉语言模型](https://thenewstack.io/vision-foundation-models-when-does-size-matter/) (VLMs) 的上下文视觉嵌入和后期交互机制。

### 视觉嵌入

ColPali 使用 PaliGemma 模型，这些模型是 [Google](https://cloud.google.com/?utm_content=inline+mention) 为图像文本压缩等通用任务创建的轻量级 VLM。与传统的纯文本模型相比，VLM 具有独特的优势，因为它集成了 [视觉和文本数据](https://thenewstack.io/ai-needs-more-than-a-vector-database/)，使它们能够处理需要全面理解视觉上下文才能完成的复杂任务，例如解释图像、为视觉输入生成描述性文本以及根据视觉线索回答问题。

使用 [PaliGemma](https://huggingface.co/blog/paligemma)，ColPali 可以直接从文档图像创建高质量的上下文嵌入，而无需进行文本提取、OCR 或布局分析等复杂步骤。这种简化的方法使索引更快、更容易，从而提高了文档检索的效率。检索到文档后，RAG 系统中的生成阶段可以专注于使用文本和视觉信息处理和总结最相关的文档。

该模型能够使用视觉元素和文本，从而能够更全面地理解文档内容。这种方法使 ColPali 能够找到传统纯文本方法可能遗漏的相关文档，尤其是在视觉信息至关重要的场合，例如包含图表或包含图表和图形的科学论文的财务报告。

### 后期交互机制

在检索阶段，[交互](https://jina.ai/news/what-is-colbert-and-late-interaction-and-why-they-matter-in-search/) 描述了通过比较文档的向量表示来评估文档与用户查询的相关性的过程。这种比较有助于系统将文档与查询的意图和内容匹配，从而获得更准确的搜索结果。
Please provide the markdown text you would like me to correct. I need the text to be able to help you.