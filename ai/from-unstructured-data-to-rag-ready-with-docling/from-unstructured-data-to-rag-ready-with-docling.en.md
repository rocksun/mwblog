Retrieval-augmented generation (RAG) has emerged as a leading method for combating hallucinations and other inaccuracies that affect large language model (LLM) content generation. However, the right data architecture is needed for RAG to scale effectively and efficiently.

Today, companies generate huge amounts of data from their intellectual property, operational procedures and marketing, sales and customer engagements. The biggest challenge is not collecting this data but rather extracting meaningful insights that can be used to significantly improve customer service and time to market.

[GenAI](https://thenewstack.io/genai-is-quickly-reinventing-it-operations-leaving-many-behind/) promises to bridge this gap, enabling users to turn a large amount of organizational data into more useful information. However, this becomes an obstacle when the data is in a format that’s not fully compatible with the LLM (such as PDF files or proprietary documents). Transforming this data to make it [usable by the LLM](https://thenewstack.io/what-is-a-large-language-model/) to support organizational needs can be a resource-intensive and time-consuming task.

To start, organizations need to pre-process documents into formats that can be consumed by the LLM and used in a [RAG workflow](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/). This involves more than just optical character recognition (OCR) or [text extraction](https://thenewstack.io/top-10-nlp-tools-in-python-for-text-analysis-applications/). This requires extracting data that provides context and implementing document element-aware techniques. For example, if a table spans multiple pages, it must be extracted as a single table. If a document’s layout consists of multiple columns with a mix of elements, such as images, tables, and text, each element should be extracted individually, maintaining its identity and the context of its extraction.

## RAG Makes LLMs Smarter and More Accurate

RAG is a framework designed to overcome the limitations of LLMs and provide more accurate and detailed responses. Although LLMs are trained on vast data sets, they often struggle with specialized knowledge, up-to-date information and generating factually incorrect outputs, also known as “hallucinations.” RAG mitigates these problems by dynamically retrieving relevant data from external sources in real time.

RAG operates in two main stages: the ingestion stage and the inference stage. During the ingestion stage, data from external knowledge sources is cleaned and transformed. Raw files must be ingested and stripped away of noise. This may involve removing boilerplate text or irrelevant headers and footers and standardizing document encodings. Because preserving information fidelity for retrieval is crucial, documents must be broken into cohesive, contextually-meaningful chunks. A chunk could be a paragraph, list item, table or heading. Each chunk or passage is enriched with metadata: source, section title, timestamps, tags, authorship, etc. This helps with filtering the results.

At this stage, vectorization converts data into embeddings, which are numerical representations in a multidimensional space. The generated embeddings are usually stored in a vector database for efficient retrieval during inference.

During the inference stage, the user’s query is first embedded and compared with the embeddings of the external knowledge source. A similarity search retrieves the data points closest (most relevant) to the query. Afterward, the most relevant retrieved data is inserted into a predefined prompt template. The augmented prompt is then sent to the LLM, which generates a contextually appropriate response based on its language understanding and the external data. The LLM’s prompt is dynamically composed from the retrieved passages, setting tight boundaries for grounded generation. Finally, contextual data is fed to the model and the relevant documents are retrieved using the document retrieval system.

[![RAG Process: From Data to Response](https://cdn.thenewstack.io/media/2025/08/74369fa4-image2-1024x939.png)](https://cdn.thenewstack.io/media/2025/08/74369fa4-image2-1024x939.png)

Source: Napkin AI

Given that RAG consists of so many steps, we will keep the focus on unstructured data ingestion, as it’s often the hardest challenge to solve.

## Unstructured Data Is the Bottleneck

Organizations are generating such large amounts of data, including text, documents, images, logs, code comments, support emails, reports, manuals, chat logs and documentation. Dealing with this variety and quantity of unstructured data is a challenge for most organizations.

Why? Because unstructured information comes in many formats: DOCX, PDF, Markdown, webpages, raw HTML, scanned images and more. It lacks schema or consistency, which means no two teams use the same templates. Fields are optional and documents drift over time. It also contains a lot of noise, such as typos, repeated content, boilerplate or irrelevant language. Since it’s continually growing and changing, what is accurate, relevant and current today may be obsolete tomorrow.

Turning this large amount of unstructured data into a usable, queryable, structured resource is a massive undertaking.

## Why Current Tooling Leaves Developers Frustrated

Hundreds of open source and commercial tools have sprung up to tackle bits of this problem: ETL (extract, transform, load) frameworks for ingestion, NLP (natural language processing) libraries for segmentation, embedding models for vectorization, hybrid search engines for retrieval and bespoke scripts or orchestrators to link it all together.

But this ecosystem poses its own problems: Tools rarely agree on schemas or APIs, integrations are fragile and maintaining end-to-end pipelines across growing data sets is time-consuming and error-prone. Developers are often left cobbling together one-off workflows, which are hard to scale, audit or extend as needs evolve.

Thus, we need a solution that is able to reduce this complexity while driving a strong developer experience.

## An Open Source Approach to Structured Data: Docling

[![Docling logo](https://cdn.thenewstack.io/media/2025/08/8d7fdb00-image1-1024x428.png)](https://cdn.thenewstack.io/media/2025/08/8d7fdb00-image1-1024x428.png)

Source: GitHub

Docling is an open source tool made by [IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention) Research. It is used to parse documents — from PDF and DOCX to PPTX and HTML and more — and convert them into formats like Markdown or JSON, making it easier to prepare content for GenAI applications. It supports advanced PDF processing OCR for scanned documents and integrates with tools like LlamaIndex and LangChain for RAG and question-answering tasks. Its permissive, open source MIT license allows developers to collaborate and expand the project to meet their needs.

Docling’s philosophy is simple: The pipeline should be modular, opinionated and extensible while abstracting away the repetitive, error-prone toil of assembling your own data parsers and chunkers.

Docling offers modular source connectors. It contains built-in adapters for the most common file formats (Markdown, PDF, HTML, etc.), making it easy to add a new data source. For each document format, the document converter knows which format-specific backend to employ for parsing the document and which pipeline to use for orchestrating the execution. It also provides consistent data modeling. Each extracted fragment gets wrapped in a well-specified data model, with document, section and entity metadata embedded directly.

Automated chunking and annotation is made easy. Docling infers logical breaks — be it section headers, paragraphs or table rows — and annotates them accordingly. Additionally, Docling’s pipeline is extensible with user-defined processors. By offering extensible plugins, attaching custom metadata or integrating with downstream labeling or enrichment services is simplified.

Docling uses a [hybrid chunking strategy](https://thenewstack.io/augmenting-multi-and-hybrid-cloud-strategies-with-databases/) that actually understands your document’s structure, preserving context while creating optimal chunks for embeddings.

Most basic chunkers from other providers split text purely by character count (such as every 1,000 characters). Docling is different. It respects paragraphs, sections, tables and images; maintains semantic boundaries so chunks are meaningful and self-contained; and handles tables and images intelligently so your embeddings aren’t just garbled OCR text.

This means when data is later queried, context-rich chunks are retrieved rather than random sentence fragments.

## How To Start Using Docling

To start using Docling, simply install the pip package.

`pipinstalldocling`

Once installed, you can do the document conversion programmatically in your Python module or use the Docling command-line interface (CLI).

```
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # PDF path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "### Docling Technical Report[...]"

# docling https://arxiv.org/pdf/2206.01062
```

## Example RAG Pipeline With Docling

A high-level flow of a Docling-powered RAG workflow could start with crawling and ingesting, or running Docling’s source connectors on content repositories. Parsing and chunking could then be used for JSON fragments emitted by Docling, which contain content, context and metadata for each fragment. Chunks and embeddings could then be sent to a vector database in the indexing stage. Afterwards, retrieval and generation could occur, which means, when a user or an AI agent poses a question, the best matching embeddings are retrieved and supplied to the LLM in a controlled prompt.

With Docling, there is no more ad-hoc scripting or having to deal with a wide range of data schemas. Open source projects like Docling ensure that you are not forced to commit to a single vendor or stack. Docling thus strikes a balance between the flexibility of DIY and the stability of using a platform-delivered RAG pipeline.

## Bringing It All Together

Every organization has a large amount of unstructured data. RAG in theory offers a way to transform this data into something useful, but only if developers can reliably structure this data and manage the flow of the knowledge. This is where open source frameworks like Docling shine.

The data pipeline ecosystem is still highly fragmented. Many organizations fall into “framework fatigue.” Each new need, like processing a new file type or supporting new chunking strategies, may seemingly require a new library. The need to break versions of libraries, deal with incomplete documentation and a lack of best practices could overwhelm developers entering such an ecosystem.

That’s why integrated, opinionated solutions are becoming so attractive. These platforms, like [Couchbase Capella AI Services](https://www.couchbase.com/products/ai-services/), provide unified ingestion and transformation of unstructured data for vector and RAG workflows via the unstructured data service. Instead of managing different moving pieces, it offers a platform workflow specifically designed for robustness and easy extensibility.

To learn how Capella AI Services addresses developers’ most critical GenAI issues, click [here](https://www.couchbase.com/products/ai-services/). You can also sign up for the private preview of Capella AI Services [here](https://info.couchbase.com/capella-ai-services-signup?_gl=1*pfu69a*_gcl_aw*R0NMLjE3NTQ1ODIwOTMuQ2owS0NRanduZEhFQmhEVkFSSXNBR2gwZzNCMFdxSklOdnh0SmU5djl3Nzd4MHVRZ2hnZVBDWE1MU1BYZmt0eWV5OTFWZEFNeEMwcGVRUWFBdko2RUFMd193Y0I.*_gcl_au*ODYwOTQwNDUuMTc1NTExNzI4Nw..).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/08/565fc9a3-cropped-98d12160-shivay-lambda.jpeg)

Shivay Lamba is a senior developer experience engineer at Couchbase. He specializes in web development, machine learning and DevOps. He also is an open source contributor, maintainer and mentor.

Read more from Shivay Lamba](https://thenewstack.io/author/shivay-lamba/)