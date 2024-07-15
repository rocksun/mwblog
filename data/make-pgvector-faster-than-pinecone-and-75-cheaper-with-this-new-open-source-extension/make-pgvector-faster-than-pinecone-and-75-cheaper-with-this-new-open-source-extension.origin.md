# Make Pgvector Faster Than Pinecone and 75% Cheaper With This New Open Source Extension
![Featued image for: Make Pgvector Faster Than Pinecone and 75% Cheaper With This New Open Source Extension](https://cdn.thenewstack.io/media/2024/07/65712007-1.cover_image_postgresql-vs-pinecone-1024x585.jpg)
A common question I hear from developers building AI applications is, “Do I need a [standalone vector database](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/), or can I just use a general-purpose database I already have and know?”

And while general-purpose databases like [PostgreSQL](https://thenewstack.io/postgresql-takes-a-new-turn/) have gained popularity for vector storage and search thanks to their familiarity and extensions like [pgvector](https://github.com/pgvector/pgvector), the one argument for opting to use a dedicated vector database, like [Pinecone](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/), has been the promise of greater performance. The reasoning goes like this: dedicated vector databases have purpose-built data structures and algorithms for storing and searching large volumes of vector data, thus offering better performance and scalability than general-purpose databases with added vector support.

My team at [Timescale](https://www.timescale.com), the PostgreSQL cloud database company, built [pgvectorscale](https://github.com/timescale/pgvectorscale/) to make PostgreSQL a better database for AI and challenge the notion that PostgreSQL and pgvector are not performant for workloads. Pgvectorscale brings specialized data structures and algorithms for large-scale vector search and storage to PostgreSQL as an extension, helping deliver comparable and often superior performance than specialized vector databases like Pinecone.

## Pgvectorscale: High-Performance, Cost-Efficient Scaling for Large Vector Workloads on PostgreSQL
[Pgvectorscale](https://github.com/timescale/pgvectorscale/?ref=timescale.com) is an open source PostgreSQL extension that builds on pgvector, enabling greater performance and scalability (keep reading for the actual numbers). Using pgvector and pgvectorscale, developers can build more scalable AI applications, benefiting from higher-performance embedding search and cost-efficient storage.
Licensed under the [open source PostgreSQL License](https://github.com/timescale/pgvectorscale/blob/main/LICENSE?ref=timescale.com), pgvectorscale complements pgvector by leveraging the pgvector data type and distance functions, further enriching the PostgreSQL ecosystem for building AI applications. While pgvector is written in C, the pgvectorscale extension is written in Rust, giving the community a new avenue to contribute to vector support in PostgreSQL.

Pgvectorscale builds on pgvector with two key innovations:

**StreamingDiskANN vector search index:** StreamingDiskANN overcomes limitations of in-memory indexes like HNSW (hierarchical navigable small world) by storing part of the index on disk, making it more cost-efficient to run and scale as vector workloads grow. Inspired by Microsoft research and then improved by Timescale AI researchers, pgvectorscale’s StreamingDiskANN index optimizes pgvector data for low-latency, high throughput search without sacrificing high accuracy. The ability to store the index on disk vastly decreases the cost of storing and searching over large amounts of vectors since SSDs are much cheaper than RAM.
**Statistical Binary Quantization (SBQ):** Developed by researchers at Timescale, this technique improves standard binary quantization techniques by improving accuracy when using quantization to reduce the space needed for vector storage.
## Pgvector vs. Pinecone: Performance Impact of pgvectorscale
Let’s briefly unpack the claim that pgvectorscale helps PostgreSQL get comparable and often superior performance than specialized vector databases like Pinecone.

To test the performance impact of pgvectorscale, we compared the performance of PostgreSQL with pgvector and pgvectorscale against Pinecone, widely regarded as the market leader for specialized vector databases, on a [benchmark](https://www.timescale.com/blog/pgvector-vs-pinecone/) using a dataset of 50 million Cohere embeddings (of 768 dimensions each).

PostgreSQL with pgvector and pgvectorscale outperformed Pinecone’s storage-optimized index (s1) with 28x lower p95 latency and 16x higher query throughput for approximate nearest neighbor queries at 99% recall.

Furthermore, PostgreSQL with pgvectorscale achieves 1.4x lower p95 latency and 1.5x higher query throughput than Pinecone’s performance-optimized index (p2) at 90% recall on the same dataset. The p2 pod index is what Pinecone recommends if you want the best possible performance, and to our surprise pgvectorscale still helped PostgreSQL outperform it!

This impressive performance, combined with the trusted reliability and [continuous evolution of PostgreSQL](https://www.timescale.com/blog/making-postgresql-a-better-ai-database), makes it clear: building on PostgreSQL with pgvector and pgvectorscale is the intelligent choice for developers aiming to create high-performing, scalable AI applications.

The cost benefits are equally compelling. Self-hosting PostgreSQL with pgvector and pgvectorscale is 75-79% cheaper than Pinecone. Self-hosting PostgreSQL costs approximately $835 per month on AWS EC2, compared to Pinecone’s $3,241 per month for the storage-optimized index (s1) and $3,889 per month for the performance-optimized index (p2).

This result disproves the [claims](https://www.pinecone.io/blog/pinecone-vs-pgvector/?ref=timescale.com) that PostgreSQL and pgvector are easy to start with but not scalable or performant for AI applications. With pgvectorscale, developers building GenAI applications can enjoy purpose-built performance for vector search without giving up the benefits of a fully featured PostgreSQL database and ecosystem.

And those benefits are numerous. Choosing a standalone vector database would mean you lose out on the full spectrum of data types, transactional semantics, and operational features that exist in a general-purpose database and are often necessary for deploying production apps. PostgreSQL also offers abundant tooling and a rich ecosystem — think pg_stat_statements for query statistics, EXPLAIN plans for debugging slow queries, and the numerous connectors, libraries, and drivers for every other technology in your AI data stack.

If you’d like to learn more about pgvectorscale’s performance, here’s a [technical ](https://www.timescale.com/blog/how-we-made-postgresql-as-fast-as-pinecone-for-vector-data/)explanation of how StreamingDiskANN and Statistical Binary Quantization work. There’s also more detail about the benchmarking methodology and results in this [pgvector vs. Pinecone comparison blog post](https://www.timescale.com/blog/pgvector-vs-pinecone).

## PostgreSQL as the Foundation for AI Applications
Databases are critical to building AI applications, and **I think all applications will be AI applications in the future.** The rise of AI applications that leverage LLMs also means that developers demand more from their databases. The good news is that PostgreSQL is evolving to meet changing developer needs, thanks to its rich ecosystem and community.

I believe that PostgreSQL — with its rich ecosystem, multiple data type support, and battle-tested reliability — is the bedrock for the future of data. I’ve heard this concisely expressed as “PostgreSQL for Everything.” And in the future, everything will be infused with AI.

At Timescale, we believe [PostgreSQL is the bedrock of the future of data](https://www.timescale.com/blog/postgres-for-everything/). The strength of the PostgreSQL ecosystem is what makes it the most loved database for professional developers.

![](https://cdn.thenewstack.io/media/2024/07/933ebf28-4.postgres-for-everything_so-2023-1.png)
According to the 2023 Stack Overflow Developer Survey, PostgreSQL is the most popular database choice among professional developers and developers in general.

**I’d argue that PostgreSQL is the ideal foundation for the future of AI applications.** Extensions like pgvector, pgvectorscale, and [pgai](https://github.com/timescale/pgai) lower the barriers to adopting and scaling PostgreSQL for AI applications — whether they be search, RAG, or Agents — by removing the need to adopt a separate vector database and simplifying data architectures.
As the PostgreSQL for AI ecosystem continues to develop, I hope that even more developers can trade complex, brittle data architectures (juggling multiple databases) for the rock-solid foundation, versatile extensions, and straightforward simplicity of PostgreSQL in their AI data stack.

## Build Your AI Applications With PostgreSQL Today
[Pgvector](https://github.com/pgvector/pgvector), [pgvectorscale](https://github.com/timescale/pgvectorscale/), and [pgai](https://github.com/timescale/pgai) are all open source under the [PostgreSQL License](https://github.com/timescale/pgvectorscale/blob/main/LICENSE?ref=timescale.com) and are available for you to use in your AI projects today.
You can find installation instructions on Github (linked above). And if you’re looking for a managed database, you can access all three extensions on [Timescale’s cloud PostgreSQL platform](https://console.cloud.timescale.com/signup).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)