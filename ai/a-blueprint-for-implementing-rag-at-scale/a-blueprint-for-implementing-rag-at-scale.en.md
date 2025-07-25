[Retrieval-augmented generation (RAG)](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) is essential for most [large language model (LLM)](https://thenewstack.io/what-is-a-large-language-model/) applications because it brings company-specific information into the generation process. If you’re planning to deploy [generative AI](https://thenewstack.io/generative-ai-is-just-the-beginning-heres-why-autonomous-ai-is-next/) in your organization, you’ll almost certainly need RAG. When done right, it improves accuracy, reduces hallucinations and lets LLMs reason over your own proprietary data. The concept sounds simple: Find information relevant to a user’s query and pass it to the LLM so it can generate a better answer. But as always, the devil is in the details.

The rise of generative AI, especially [agentic AI](https://thenewstack.io/the-architects-guide-to-understanding-agentic-ai/), is pushing RAG into more demanding enterprise use cases, and large organizations face a serious scaling challenge. RAG at scale means machine-speed retrieval over massive, diverse datasets, along with fast, efficient coordination between retrieval and generation. As data volumes grow, keeping results relevant, fresh and fast becomes increasingly hard (and expensive). This is even more true when you’re serving lots of users at once or supporting multiturn agent interactions that need to perform deep, multistep research.

## Addressing the Problem of Relevance

Exactly how do you find the most relevant information when you have millions, if not billions, of documents and need to serve thousands, if not millions, of users, all within a tenth of a second? This task is simplified through stepwise refinement:

### Step 1: Define Your Searchable Unit

Your searchable unit (often called a “chunk”) is critical in RAG. It is the unit of information that you will pass to the LLM. You will be searching through these units to find the best information to provide your LLM. Getting it right affects retrieval accuracy, latency and ultimately the quality of LLM responses.

This isn’t just about token limits; it’s about aligning the chunk size and structure with the types of questions users will ask. For example, fact-level queries may benefit from smaller, precise chunks, while broader or reasoning-based queries might require longer spans of text to preserve context. Chunks should respect semantic boundaries like paragraphs or list items, and overlapping windows can help maintain continuity across breaks. Adding metadata (such as source, section, date) also supports better filtering and ranking later in the pipeline. There’s no one-size-fits-all rule — effective chunking depends on your content, query patterns and scale — so treat this as a design decision worth testing and tuning.

### Step 2: Select Your Retrieval Strategy

Your retrieval strategy determines how you find relevant chunks to pass to the LLM. It’s the core of what makes RAG work. Should you use semantic, keyword or a hybrid approach to find the best documents or chunks? What kind of embedding model fits your domain? These decisions shape the way your system understands and surfaces relevant information.

Semantic retrieval (using vector embeddings) excels at capturing meaning, but keyword methods like BM25 (Best Matching 25) can outperform in precision when exact terms or domain-specific phrases matter. Hybrid search — combining both — often gives the best of both worlds. Your choice of embedding model also matters: lightweight models are faster but may lose nuance, while larger models offer richer semantics but at a higher cost and latency. Retrieval isn’t just about finding relevant content — it’s about doing so at the speed and scale your application demands. Balancing accuracy, throughput and cost is key, especially when your users (or agents) depend on fast, reliable answers across billions of documents.

### Step 3: Define Your Ranking Strategy

Ranking decides which retrieved chunks are passed to the LLM and in what order. It’s your second chance to improve relevance before the model starts generating. A decent RAG solution will retrieve many potentially useful documents, but not all of them deserve to be shown to the LLM. To make that call, you need a way to combine different scoring signals: keyword match, semantic similarity, metadata filters and more. Figuring out how to weigh these signals manually is near impossible, especially at scale. That’s why most production-ready RAG systems use machine-learned ranking to optimize quality based on real user behavior or feedback. Multiphase ranking pipelines can refine results through successive filters and scorers, but even a simple learned model can dramatically improve which content makes it into the prompt — and how well the LLM responds.

### Step 4: Address the Impact of Multiple Use Cases

RAG systems rarely serve just one type of user or workflow. Some queries come from human users who need fast, readable answers; others come from AI agents or orchestration layers that can tolerate more latency in exchange for deeper, more context-rich results. Agentic retrieval — where LLMs perform search autonomously — has different characteristics than human search. LLMs can handle more context, don’t mind slower responses and may issue many queries in sequence to solve a single task. Designing a system that serves both humans and machines from the same backend requires trade-offs in latency, ranking depth and retrieval volume. The key is to recognize that not all queries — or users — are equal, and your architecture should be flexible enough to adapt based on the calling use case.

## AI Search Platform Support

To support complex RAG workloads at scale, an AI search platform must do far more than basic keyword or vector matching. It needs to intelligently handle massive, ever-growing document corpora, including very large or unstructured documents that can’t be passed wholesale to an LLM. This means supporting automatic chunking to break large documents into meaningful, retrievable units and ranking those chunks as well as whole documents to ensure only the most relevant content is returned.

The platform must also scale horizontally to handle high query volumes, support low-latency retrieval even under load and allow frequent updates to both content and ranking logic without reindexing the entire dataset. Indexing pipelines should be flexible enough to incorporate metadata, embeddings, and custom features, and fast enough to keep the system fresh with minimal lag.

Ultimately, the platform must strike a careful balance between performance, accuracy and adaptability so it can serve both real-time, user-facing experiences and complex agentic workflows, all from the same infrastructure.

Vespa has created [The RAG Blueprint](https://vespa.ai/solutions/enterprise-retrieval-augmented-generation/the-rag-blueprint/), based on what we have learned from deploying RAG at scale. Available as a free Python notebook and sample application, it goes more in depth on the implementation of these points, offering a hands-on, modular recipe that covers the key design decisions — like chunking, retrieval, machine learned ranking, and performance tuning — grounded in real-world experience. Whether you’re just starting or optimizing an existing system, the blueprint provides a solid foundation for building production-ready, scalable RAG applications.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/d6ac6c60-cropped-9cae470c-kai-borgen.jpeg)

Kai Borgen is a technical product engineer working at Vespa AI. With a background in both business and engineering, his focus lies in bringing technical expertise to business functions, ensuring that organizations stay aligned, effective and ahead of the curve.

Read more from Kai Borgen](https://thenewstack.io/author/kai-borgen/)