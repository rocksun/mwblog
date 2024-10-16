# Advanced Retrieval-Augmented Generation (RAG) Techniques
![Featued image for: Advanced Retrieval-Augmented Generation (RAG) Techniques](https://cdn.thenewstack.io/media/2024/10/a6dbc655-advanced-rag-techniques-1024x576.jpg)
[Retrieval-Augmented Generation](https://zilliz.com/learn/Retrieval-Augmented-Generation?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns) (RAG) has experienced a number of advancements in recent years alongside its increasing popularity. In my talk at [All Things Open (ATO) 2024](https://thenewstack.io/event/all-things-open-2024/) on Oct. 28, I will cover a number of the techniques needed to build better RAG. These include [chunking](https://zilliz.com/learn/guide-to-chunking-strategies-for-rag?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns), choosing an [embedding model](https://zilliz.com/blog/choosing-the-right-embedding-model-for-your-data?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns) and [metadata structuring](https://zilliz.com/blog/metadata-filtering-hybrid-search-or-agent-in-rag-applications?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns).
## Considerations for Building a RAG System
One of the most important things when building a RAG system is making it work with the type of data you need. For example, there are many types of text — conversational, documentation, [Q&A](https://thenewstack.io/build-an-ai-powered-question-answering-application), lectures and formal documents. You also have to determine exactly what you need from the data: Is it just a dump of all text, or are you looking for specific insights, or only information from embedded charts and graphs?

Just like any other data project, you need to do an analysis to determine what data you are using, how you will ingest it, and what enrichments and transformations are required. Your decisions include cost, size, model license, time to embed data and whether it works with your data specifications.

An incredibly important part of using [vector databases](https://zilliz.com/learn/what-is-vector-database?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns) and RAG is determining what [embedding model](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai) to use, from providers like HuggingFace, OpenAI, Google, Meta, PyTorch, Jina AI, Mistral AI or Nomic A. Some models are for dense [embeddings](https://milvus.io/docs/embeddings.md?utm_source=partner&utm_medium=referral&utm_campaign=2024-09-27_blog_ato-talk-preview_tns) such as BAAI/bge-base-en-v1.5, which produces vectors of 768 dimension floating point numbers. There are also sparse embedding models that produce mostly zeros.

You also need to decide which [tools](https://zilliz.com/product/integrations) to use; many new tools make building RAG less manual, such as LangChain, LlamaIndex, LangChain4J or Spring AI. You can also use AI extract-transform-load (ETL) tools such as DataVolo, Cloudera DataFlow, Airbyte, StreamNative UniConn, Apache Spark, Apache Flink, Ray and Fivetran.

## Looking to the Future of RAG
In addition to discussing new advances in the world of RAG, during my ATO talk, I will share some examples and look to the future where new models, techniques, [vector databases](https://thenewstack.io/scaling-databases-to-meet-enterprise-genai-demands) and AI advancements will supercharge the entire concept. These include:

- Chunking
- Embedding model options
- Metadata structuring
- GraphRAG
- Multilingual vs. a specific language
- Multimodal data retrieval
- Query enhancement
- Query routing
- Hierarchical indexing
- Hybrid retrieval
- Agentic RAG
- Self-reflection
- Query routing
- Subqueries
I’ll also share a quick overview of a RAG system that uses Milvus, an open source vector database, to combine a retrieval system with a generative model. By adding smart context quickly retrieved from Milvus to your prompt, you can reduce LLM hallucinations, which is so important.

## Register for ATO Today
[Register](http://www.eventbrite.com/e/916649672847/?discount=NEWS20) for All Things Open now to attend my talk, “[Advanced Retrieval Augmented Generation (RAG) Techniques](https://2024.allthingsopen.org/sessions/advanced-retrieval-augmented-generation-rag-techniques)” on Monday, October 28, 2024, at 10:30 a.m. ET.
### Other Resources
[Retrieval-Augmented Generation (RAG) With Milvus and LlamaIndex](https://milvus.io/docs/integrate_with_llamaindex.md)[Super Charge Your AI Applications With Easy High Speed Multi-Tenancy With Partition Keys](https://medium.com/@tspann/super-charge-your-ai-applications-with-easy-high-speed-multi-tenancy-with-partition-keys-5fa581127dd6)[Ranking for Relevance With BM25](https://medium.com/@tspann/ranking-for-relevance-with-bm25-b2d9dd62e2f8)[How Good Is Quantization in Milvus?](https://medium.com/@tspann/how-good-is-quantization-in-milvus-6d224b5160b0)
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)