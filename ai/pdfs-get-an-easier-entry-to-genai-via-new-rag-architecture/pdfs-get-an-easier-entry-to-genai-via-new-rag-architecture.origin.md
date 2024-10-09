# PDFs Get an Easier Entry to GenAI via New RAG Architecture
![Featued image for: PDFs Get an Easier Entry to GenAI via New RAG Architecture](https://cdn.thenewstack.io/media/2024/10/db10f2d2-pdfs-get-easier-entry-genai-rag-arch-1024x576.jpg)
Although a picture is worth a thousand words, preparing visually rich, multimodal documents, such as PDFs, for a [retrieval-augmented generation (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) workflow can be both time-consuming and error-prone. In industries where accuracy is critical, like healthcare or financial services, documents like radiology reports or financial statements often contain images or charts that provide valuable contextual information. While these visually rich elements are often left out of RAG workflows, a new approach for retrieving information from visually enhanced documents is set to streamline multimodal document preparation and transform the potential of RAG and generative AI (GenAI).

Most retrieval systems focus primarily on text-based representations and are blind to the document’s visual elements, such as images, tables and layouts. This limitation can reduce retrieval effectiveness, especially in cases where these visual features are key to understanding the document’s content.

A typical real-world RAG pipeline for PDFs (or other complex formats) involves steps like:

- Extracting text and metadata
- Optical character recognition (OCR)
- Layout analysis: extracting tables, charts, pie charts, etc.
After completing the processing steps for obtaining text representations, the text can then be used as [input for retrieval systems](https://blog.vespa.ai/retrieval-with-vision-language-models-colpali/).

These processing steps can be time-consuming and affect retrieval quality, but Contextualized Late Interaction over PaliGemma ([ColPali](https://arxiv.org/abs/2407.01449)), a new retrieval model architecture focusing on RAG in document-heavy contexts, overcomes these challenges. This new approach to retrieval directly embeds the entire rendered document, including its visual elements, into vector representations suitable for retrieval.

## How ColPali Improves Document Retrieval
By treating documents as visual entities rather than text, ColPali opens up new possibilities for more accurate and context-aware document retrieval, especially for visually rich content. ColPali represents a step forward in document retrieval by:

- Eliminating the need for complex preprocessing steps
- Preserving the visual context of documents
- Enabling more holistic document understanding
- Streamlining the RAG pipeline
In bypassing traditional text extraction and OCR processes, ColPali not only simplifies the retrieval process but also has the potential to enhance the quality and relevance of retrieved information in RAG systems.

ColPali’s architecture builds upon two key concepts: contextualized vision embeddings from [vision-language models](https://thenewstack.io/vision-foundation-models-when-does-size-matter/) (VLMs) and late interaction mechanisms.

### Vision Embeddings
ColPali uses PaliGemma models, which are lightweight VLMs created by [Google](https://cloud.google.com/?utm_content=inline+mention) for general tasks like image-text compression. VLMs offer a unique advantage over traditional text-only models by integrating [visual and textual data](https://thenewstack.io/ai-needs-more-than-a-vector-database/), allowing them to tackle complex tasks that require a comprehensive understanding of visual context, such as interpreting images, generating descriptive text for visual inputs and answering questions based on visual cues.

Using [PaliGemma](https://huggingface.co/blog/paligemma), ColPali can create high-quality contextual embeddings directly from document images without complicated steps like text extraction, OCR or layout analysis. This streamlined approach makes indexing faster and easier, improving the efficiency of document retrieval. Once the documents are retrieved, the generative phase in RAG systems can focus on processing and summarizing the most relevant ones using text and visual information.

The model’s ability to use both visual elements and text allows for a more comprehensive understanding of document content. This approach enables ColPali to find relevant documents that traditional text-only methods might miss, especially in cases where visual information is essential, like financial reports with charts or scientific papers with diagrams and figures.

### Late Interaction Mechanisms
During the retrieval stage, an [interaction](https://jina.ai/news/what-is-colbert-and-late-interaction-and-why-they-matter-in-search/) describes the process of assessing how relevant a document is to a user’s query by comparing their vector representations. This comparison helps the system match documents to the query’s intent and content, leading to more accurate search results.

ColPali utilizes [late interaction](https://jina.ai/news/what-is-colbert-and-late-interaction-and-why-they-matter-in-search/), which processes queries and documents separately until the final stages of retrieval. This late interaction mechanism enables [rich comparisons](https://blog.vespa.ai/the-rise-of-vision-driven-document-retrieval-for-rag/) between image grid cell vector representations and query text token vector representations. By performing these comparisons at query time, ColPali avoids the heavy computational load of processing images and text together, optimizing retrieval efficiency. This approach speeds up retrieval and reduces the system’s processing requirements, making it well-suited for handling extensive document collections.

## Looking Ahead
ColPali’s architecture sets a new standard for document retrieval, offering a flexible framework that can adapt to emerging VLMs. [Benchmark results](https://arxiv.org/html/2407.01449v2#S5) demonstrate ColPali’s superiority over traditional methods, signaling a paradigm shift in the field. ColPali paves the way for more sophisticated, contextually aware systems that revolutionize document interaction and understanding by efficiently integrating visual information into RAG pipelines.

With ColPali and Vespa, developers can build a complete RAG pipeline for complex document formats like PDFs using only the visual representation of the document pages. Vespa’s sophisticated [tensor](https://docs.vespa.ai/en/tensor-user-guide.html) framework and compute engine seamlessly accommodate ColPali embeddings, allowing for the implementation of late interaction scoring through Vespa ranking expressions.

You can explore ColPali’s potential with our comprehensive [notebook](https://pyvespa.readthedocs.io/en/latest/examples/colpali-document-retrieval-vision-language-models-cloud.html) demonstrating how to utilize ColPali embeddings in Vespa. Dive into the world of visual document retrieval and experience the power of ColPali for yourself!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)