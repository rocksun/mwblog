# Making Adding AI Apps with Postgres Easier for Developers
![Featued image for: Making Adding AI Apps with Postgres Easier for Developers](https://cdn.thenewstack.io/media/2024/10/dfd06d6b-screenshot-2024-10-28-at-12.05.55 pm-1024x571.png)
With the rise of AI and [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms), developers called on to create AI applications might feel they’ve been shuttled into alien terrain. Open source PostgreSQL database vendor [Timescale](https://www.timescale.com/go/best-postgres-db)’s answer to this is a set of tools to help developers who have no background in AI to build enterprise-grade apps.

![Timescale's tiger logo](https://cdn.thenewstack.io/media/2024/10/6fd1cf11-timescalelogo.jpg)
Timescale logo

The newest addition to its [pgai tool suite](https://github.com/timescale/pgai) is [pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md), which integrates the entire embedding process into [Postgres](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/), allowing developers to create, store and manage vector embeddings alongside relational data without external tools or added infrastructure.

All the tools are built atop [pgvector](https://github.com/pgvector/pgvector), the open source extension enabling vector search in Postgres.

While a number of Postgres vendors have [added pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/) in the mad rush to offer AI capabilities, Timescale maintains that’s not enough to help developers new to AI get started.

“If you think about who is actually building AI applications, it actually falls on to the software developer, the application developer,” explained [Avthar Sewrathan](https://www.linkedin.com/in/avthars/), AI and developer product lead for Timescale. While they have experience building production systems, they might not have AI and ML backgrounds, which traditionally have been the domain of data scientists or research engineers, but they are not necessarily full-stack engineers or backend engineers.

“Vectorizer really deals with, ‘OK, we have vector search capabilities in Postgres, but how do you get started in the first place? And then also, once you’ve created embeddings, how do you get to where you can actually have a production application, and what are the needs and demands along with that?’” he said.

## Embedding Creation on Autopilot
To sum up pgai Vectorizer, he explained, “It’s putting embedding creation on autopilot with one SQL query, and it’s all within Postgres. [It automates] the process of creating embeddings from source data and allows teams to essentially set it and forget it.

As new data is added to their tables, embeddings will automatically be created, and they avoid all these problems around data sync and ensuring that embeddings scale, because everything is automatically synced in the background, just removing work that development teams would have to do themselves otherwise.”

He said clients are increasingly asking about the operational tasks involved with AI, making that a growing area of concern.

With pgai Vectorizer, developers can:

- Manage all data for AI apps — vectors, metadata, event data — on the same PostgreSQL database platform they know.
- Automatically synchronize data changes to vector embeddings in real time.
- Easily switch between embedding models for rapid testing and experimentation without code changes or having to create custom data pipelines.
- Track model versions and ensure backward compatibility during rollouts for smooth transitions.
“pgai Vectorizer is a game-changer. It promises to streamline our entire AI workflow, from embedding creation to real-time synchronization, allowing us to deliver AI applications faster and more efficiently,” said [Web Begole](https://www.linkedin.com/in/webbegole/) CTO at MarketReader. “By integrating everything directly into PostgreSQL, pgai Vectorizer removes the need for external tools and expertise, making it easier for our team to focus on innovation rather than infrastructure.”

‘There’s actually really tough engineering challenges that need to be overcome if you want to build a production-grade application.’

—Avthar Sewrathan, AI product lead for Timescale
Sewrathan pointed to four tasks pgai Vectorizer could replace for developers:

**Building an ETL pipeline —**Taking in source documents or images, orchestrating calls to OpenAI or another model and creating the actual embedding.**Chunking and formatting**— “Before you can create an embedding, you need to get [the data] into the right format and get it into the right size that can fit within the token limits of the embedding model. And so that’s another task that we take away. You configure that in one line of code, and then that automatically runs in the background,” he said.**Scaling and managing your embedding creation pipeline**— “Most developers can take half an hour and write an embedding creation script in[Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/), but to have something that actually scales and deals with OpenAI rate limits, that deals with queuing when you have hundreds of thousands of embeddings to create, that’s one thing that our system does out of the box. It replaces these queuing systems for updates and synchronization.”**Synchronization**— “When you’re building AI applications, you have to have code that checks, ‘OK, in my vector database these embeddings are created.’ [But] do I have the right metadata in my relational database? Or, for example, maybe you have new documents in your relational database, and you need to check if the corresponding vectors are created. This kind of code does [what] I would call synchronization, like staleness checking,” Sewrathan said. You are guaranteed that you know your embeddings will be up to date, and if not, you will get a notification.
“I think a lot of what you see in the industry today is databases adding vector search capabilities that replace vector databases and thinking that that’s enough to make them an essential component of building an AI application. But what we recognize — and we’ve spoken to hundreds of developers over the past more than a year and a half that we’ve been building this project — we’ve seen that vector search is just one part of building an AI system,” Sewrathan said.

“There’s actually really tough engineering challenges that need to be overcome if you want to build a production-grade application. And so our whole thesis is around saying, in terms of pgai, can we give developers a suite of tools that solve, not just vector search, but scaling your AI system, solving embedding creation, solving updating, solving data sync, solving embedding staleness, solving the ability to [access] models inside the database.”

**Initially Just pgai**
In introducing the first tool last June, the company stated in a blog post: “Simply put, we built pgai to help [make more PostgreSQL developers AI engineers](https://www.timescale.com/blog/pgai-giving-postgresql-developers-ai-engineering-superpowers/).”

Short for Postgres artificial intelligence, [pgai](https://github.com/timescale/pgai?tab=readme-ov-file) was designed to simplify the process of building semantic search, retrieval-augmented generation (RAG), and other AI applications with PostgreSQL.

“Simply put, we built pgai to help make more PostgreSQL developers AI engineers.”

—Timescale blog post
“pgai complements pgvector by storing embeddings in the pgvector data type and using Python and PL/Python to interact with model APIs from within a PostgreSQL database, its GitHub page explains. It enables classification, summarization and data enrichment tasks on existing relational data. It creates embeddings directly in the database, skipping the task of having to save them there.

Initially supporting only [OpenAI](https://github.com/timescale/pgai/blob/main/docs/openai.md), pgai and pgai Vectorizer now support [Ollama](https://github.com/timescale/pgai/blob/main/docs/ollama.md), [Anthropic](https://github.com/timescale/pgai/blob/main/docs/anthropic.md) and [Cohere](https://github.com/timescale/pgai/blob/main/docs/cohere.md). The company has announced plans to support more models including Claud and Hugging Face.

**Improved Scaling**
Also introduced in June, [pgvectorscale](https://github.com/timescale/pgvectorscale) takes aim at handling [large-scale, high-performance AI use cases](https://www.timescale.com/blog/pgvector-is-now-as-fast-as-pinecone-at-75-less-cost/).

“Pgvectorscale brings specialized data structures and algorithms for large-scale vector search and storage to PostgreSQL as an extension, helping deliver comparable and often superior performance than specialized vector databases like [Pinecone](https://www.pinecone.io/?utm_content=inline+mention),” the company stated.

It added a StreamingDiskANN vector search index, inspired by [Microsoft](https://news.microsoft.com/?utm_content=inline+mention)’s [DiskANN](https://github.com/microsoft/DiskANN) algorithm, to deal with the limitations of in-memory indexes like HNSW (hierarchical navigable small world) by storing part of the index on disk. With solid-state disks much cheaper than RAM, storing the index on disk represents a vast cost savings.

It also developed statistical binary quantization (SBQ) to improve accuracy while employing the compression of [standard binary quantization techniques](https://jkatz05.com/post/postgres/pgvector-scalar-binary-quantization/) to save storage space.

While pgvector is written in C, pgvectorscale is developed in [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) using the [PGRX framework](https://github.com/pgcentralfoundation/pgrx), adding access for another fast-growing community.

## All Open Source
The compression means lower infrastructure costs, but Sewrathan also pointed to other cost savings as well.

“We think that you actually can have less custom code running and that saves a lot of engineering hours and actually allows smaller teams to do the job. [Previously you might have needed] 10 developers; now you can just do [with] two or three because a lot of things are automated and take place out of the box for you with the Vectorizer,” he said.

In an [article for The New Stack](https://thenewstack.io/make-pgvector-faster-than-pinecone-and-75-cheaper-with-this-new-open-source-extension/), Sewrathan also referred to its benchmark test comparing its version of pgvector against Pinecone, concluding the Postgres extension is not only vastly less expensive, but faster than the standalone vector database.

Touting popular [tried-and-true PostgreSQL](https://thenewstack.io/from-a-fan-on-the-ascendance-of-postgresql/), Sewrathan wrote:

“Choosing a standalone vector database would mean you lose out on the full spectrum of data types, transactional semantics and operational features that exist in a general-purpose database and are often necessary for deploying production apps.”

The pgai tools are open source, but Timescale also offers them as part of a fully managed database service.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)