# Pgvector vs. Pinecone: Vector Database Performance and Cost Comparison
![Pgvector vs. Pinecone: Vector Database Performance and Cost Comparison](/blog/content/images/size/w2000/2024/06/pgvector-vs-pinecone.png)
**Pinecone** and ** PostgreSQL with the pgvector extension** are two of the most popular vector databases to use when developing AI applications. On one hand, you have Pinecone, which is a proprietary managed vector database, specifically designed for vector workloads. On the other hand, there’s PostgreSQL, the popular and robust general-purpose relational database with the [pgvector](https://www.timescale.com/learn/postgresql-extensions-pgvector?ref=timescale.com) extension, which adds support for vector storage and search.
Both PostgreSQL and pgvector are open source, with the flexibility to deploy locally, self-manage, or from several managed database providers (Timescale included). PostgreSQL is a mature database with advanced production-necessary features for high availability, streaming replication, point-in-time recovery, and observability. Pinecone’s development concentrated on performing fast vector search but is noticeably less mature in operational features.
So the question is: when building an AI application, do you need a standalone vector database like Pinecone, or can you use PostgreSQL, a database you might already be familiar with and know how to operationalize (and already deploy in your data stack)? And what’s more, which of the two is the better choice for large-scale vector workloads that are common in production AI applications like RAG (retrieval-augmented generation), search, and AI agents?
In this blog post, we compare the
**performance, cost, and ease of use** of both Pinecone and PostgreSQL with pgvector, but with an added twist. We also factor in **pgvectorscale**, a new open-source PostgreSQL extension that builds on pgvector for greater performance and scalability, making PostgreSQL a better database for AI applications.
### What is pgvectorscale?
**Pgvectorscale** adds specialized data structures and algorithms for large-scale vector search and storage to PostgreSQL as an extension.
Pgvectorscale complements pgvector by building on its data type and distance functions with a new search index,
**StreamingDiskANN**, which is purpose-built for high performance and cost-efficient scalability. StreamingDiskANN overcomes limitations of in-memory indexes like HNSW (hierarchical navigable small world) by storing the index on disk, making it more cost-efficient to run and scale as vector workloads grow.
Pgvectorscale also adds
**Statistical Binary Quantization**, a compression technique, developed by researchers at Timescale, which improves upon standard binary quantization techniques by improving accuracy when using quantization to reduce the space needed for vector storage. This makes index traversal faster without sacrificing high accuracy.
Before we start benchmarking,
[ to learn more about pgvectorscale. For more information about pgvectorscale, see check the pgvectorscale GitHub repository](https://github.com/timescale/pgvectorscale/?ref=timescale.com) [. For those looking for in-depth technical details,](https://www.timescale.com/blog/pgvector-is-now-as-fast-as-pinecone-at-75-less-cost) __this post about why we built it__ [.](https://www.timescale.com/blog/how-we-made-postgresql-as-fast-as-pinecone-for-vector-data) __our Engineering team goes into heavy detail in this article__
## Pgvector vs. Pinecone: Benchmark Summary
Before we “
[delve](https://www.reddit.com/r/ChatGPT/comments/1bzv071/apparently_the_word_delve_is_the_biggest/?ref=timescale.com)” into the methodology of how we compared Pinecone vs. PostgreSQL with pgvector and pgvectorscale, let’s summarize what we found for those looking for a TL;DR:
- We created a fork of the
[to compare the performance of PostgreSQL (pgvector and pgvectorscale) versus Pinecone on a dataset of 50 million Cohere embeddings.](https://ann-benchmarks.com/?ref=timescale.com) __ANN benchmarking tool__
- Compared to Pinecone’s storage-optimized index (s1), PostgreSQL with pgvector and pgvectorscale achieves
**28x lower p95 latency and 16x higher query throughput**for approximate nearest neighbor queries at 99 % recall, **all at 75 % lower monthly cost**when self-hosted on AWS EC2.
- Compared to Pinecone’s performance-optimized index (p2), PostgreSQL with pgvector and pgvectorscale achieves
**1.4x lower p95 latency and 1.5x higher query throughput**for approximate nearest neighbor queries at 90 % recall, **all at 79 % lower monthly cost**when self-hosted on AWS EC2.
Thanks to pgvectorscale and pgvector, developers can now use the open-source general-purpose PostgreSQL database to achieve comparable (and often superior) performance to specialized vector databases like Pinecone.
And in conclusion, we show that even with large scale vector workloads common in production AI applications,
[. And that developers can resist the temptation to go after the shiny new database, and instead rely on the PostgreSQL foundation they know and love, with extensions for purpose-built performance and scalability. This is also a testament to the commitment and consistent efforts of the PostgreSQL community, of which we are proud members. PostgreSQL is all you need](https://www.timescale.com/blog/how-to-collapse-your-stack-using-postgresql-for-everything/)
Now that you know the destination, let’s begin the benchmarking journey.
## Pgvector vs. Pinecone: Performance and Cost Benchmark Details
Benchmarking methodology
**Benchmarking tool:** We used a fork of the industry standard, the open-source [, to benchmark both Pinecone and PostgreSQL with pgvectorscale. Before testing performance, we modified it to correctly measure queries per second (QPS) when using multiple threads and to run different queries to warm up (versus test) the index. You can find all of our modifications in this ANN-Benchmarks tool](https://ann-benchmarks.com/?ref=timescale.com) [of ANN-Benchmarks.](https://github.com/timescale/ann-benchmarks/tree/pinecone-comparison?ref=timescale.com) __tag of our fork__ **Dataset:** 50 million Cohere embeddings of 768 dimensions each. The dataset was created by concatenating multiple Cohere Wikipedia datasets until we had 50 million vectors of 768 dimensions in our training dataset and 1,000 in our test dataset. Links to datasets are publicly available on HuggingFace here: __Cohere/wikipedia-22-12-en-embeddings__ __Cohere/wikipedia-22-12-simple-embeddings__ __Cohere/wikipedia-22-12-de-embeddings__ **Client machine details:** A standalone client machine ran the ANN-Benchmarks tool. This client machine was in the same region as the Pinecone index and PostgreSQL machine to ensure we had an even playing field regarding network latency. This client machine had 16 CPUs and 64 GB of RAM. We downloaded the dataset before the benchmarking started; it was not streamed during the runs. We used the gRPC version of the Python client for Pinecone, which gave us better results than the HTTP(S) version. **Testing methodology:** The client ran 29,000 queries in each benchmark using training vectors to “pre-warm” the system. Then, the client used the 1,000 “real” test vectors, which were different from the pre-warm set, to query. We only used the figures from the test vectors for the results.
### Machine configuration: Pinecone
**Pod-based indexes:** We benchmarked three Pinecone pod-based indexes, p1, p2, and s1. We did not benchmark the Pinecone serverless index as queries were rate-limited. Pinecone suggests using its serveless offering only for workloads of less than 5 QPS and is thus unsuitable for the scale of our benchmark at the time of testing. See the table below for an explanation of Pinecone’s pod-based indexes. ![Table comparing Pinecone’s pod-based index types. Source: “Great Algorithms Are Not Enough,” Pinecone Blog.](https://www.timescale.com/blog/content/images/2024/06/pgvector-vs-pinecone_table.png)
*Table comparing Pinecone’s pod-based index types. Source: “* *Great Algorithms Are Not Enough* *,” Pinecone Blog.* **General approach:** We benchmarked many different Pinecone pod-based index configurations. We tried storage-optimized (S1) and performance-optimized (P1, P2) pod types with various pod sizes and replica settings. With a limited time and budget, a real-world struggle faced by many developers, we did not explore every combination possible but did our best to explore the space. **Best performing configurations: **the best configurations we found are listed below. **Storage-optimized (s1)**
- Pod type: s1
- Pod size: x4
- Pods: 5
- Replicas: 2
- Total pods: 40
- Pod fullness: 40 %
- Client threads: 32
- Monthly cost: $3,241
**Performance-optimized (s1)**
- Pod type: p1
- Pod size: x8
- Pods: 8
- Replicas: 1
- Total pods: 64
- Pod fullness: 70 %
- Client threads: 16
- Monthly cost: $5,186
**Performance-optimized (p2)**
- Pod type: p2
- Pod size: x8
- Pods: 4
- Replicas: 1
- Total pods: 32
- Pod fullness: 90 %
- Client threads: 16
- Monthly cost: $3,889
### Machine configuration: PostgreSQL with the pgvector and pgvectorscale extensions
**General approach:** We experimented with various PostgreSQL machine, database, and index configurations. We self-hosted the PostgreSQL instance on AWS EC2 to accurately reflect the experience of running fully open-source software for developers. **Machine details: **
- Instance type: r6id.4xlarge
- CPUs: 16
- RAM: 128 GB
- 1x950 GB locally attached NVMe SSD
- OS: Ubuntu 23.10
- Monthly cost: $835
**PostgreSQL settings**
- We placed the data directory on the locally attached NVMe SSD
- PostgreSQL version 16.3; pgvector v0.7.0
- We used
[to tune the PostgreSQL settings](https://github.com/timescale/timescaledb-tune?ref=timescale.com) __timescaledb-tune__ **StreamingDiskANN index:** Rather than using the ( [, we used the StreamingDiskANN index for large-scale approximate nearest neighbor search. The StreamingDiskANN index for pgvector is a key innovation introduced by the pgvectorscale extension. HNSW or IVFFlat indexes in pgvector](https://github.com/pgvector/pgvector?tab=readme-ov-file&ref=timescale.com#hnsw) **StreamingDiskANN index parameters:** Unlike Pinecone, pgvectorscale’s StreamingDiskANN index exposes parameters to users to configure search performance for their specific workload. We used the following index parameters; most are default values, and non-default parameters are marked with an asterisk (*):
- num_neighbors: 50
- search_list_size: 100
- max_alpha: 1.2
- query_rescore: 115 at 90 % recall and 400 at 99 % recall*
- query_search_list_size: 35 at 90 % recall and 75 at 99 % recall*
- num_bits_per_dimension: 2
- All 50 million vectors were in a single table and index
## Benchmark Results: Pgvector vs. Pinecone s1
**Overview:** Pinecone’s s1 index is the most “apples to apples'' comparison to PostgreSQL with pgvector and pgvectorscale because (1) it is optimized for storage, making it suitable for the 50 million vector dataset, and (2) it is the only pod-based index type which keeps raw vectors on disk rather than in fully in memory, mirroring pgvectorscale’s StreamingDiskANN index storage architecture. The s1 pod was Pinecone’s highest accuracy pod, reaching 99 % recall, albeit at the cost of slower query speeds. **A results summary of PostgreSQL with pgvectorscale vs. Pinecone s1:**
- PostgreSQL with pgvector and pgvectorscale achieves
**28x lower p95 latency**for approximate nearest neighbor queries at 99 % recall. ![A bar graph showing that PostgreSQL with pgvector and pgvectorscale achieves 28x lower p95 latency for approximate nearest neighbor queries at 99 % recall.](https://www.timescale.com/blog/content/images/2024/06/pgvector-vs-pinecone_p95-latency.png)
- PostgreSQL with pgvector and pgvectorscale achieves
**16x higher query throughput**(queries per second) for approximate nearest neighbor queries at 99 % recall. ![A bar graph showing that PostgreSQL with pgvector and pgvectorscale achieves 16x higher query throughput (queries per second) for approximate nearest neighbor queries at 99 % recall.](https://www.timescale.com/blog/content/images/2024/06/pgvector-vs-pinecone_ANN-queries.png)
- PostgreSQL costs
**75% less than the cost of Pinecone s1**($3,241/mo on Pinecone vs. $835/mo self-hosted on AWS EC2). ![A bar graph showing that PostgreSQL costs 75% less than the cost of Pinecone s1 ($3,241/mo on Pinecone vs. $835/mo self-hosted on AWS EC2)](https://www.timescale.com/blog/content/images/2024/06/pgvector-vs-pinecone_monthly-cost.png)
## Benchmark Results: Pgvector vs. Pinecone p2
**Overview:** Pinecone’s p2 index is Pinecone’s highest-performance offering. It uses a graph-based index and stores raw vectors in memory, unlike pgvectorscale’s StreamingDiskANN, which combines memory and disk. It also trades off accuracy for speed, achieving a maximum of 90 % recall. We found that with pgvectorscale, PostgreSQL is comparable and actually outperformed Pinecone’s p2 performance-optimized index. **A results summary of PostgreSQL with pgvectorscale vs. Pinecone p2:**
- PostgreSQL achieves
**1.4x lower p95 latency**for approximate nearest neighbor queries at 90 % recall. ![A bar graph showing that PostgreSQL achieves 1.4x lower p95 latency for approximate nearest neighbor queries at 90 % recall](https://www.timescale.com/blog/content/images/2024/06/pgvector-vs-pinecone_p95-at-90.png)
- PostgreSQL achieves
**1.5x higher query throughput**(queries per second) for approximate nearest neighbor queries at 90 % recall. ![A bar graph showing that PostgreSQL achieves 1.5x higher query throughput (queries per second) for approximate nearest neighbor queries at 90 % recall.](https://www.timescale.com/blog/content/images/2024/06/pgvector-vs-pinecone_ANN-90.png)
- PostgreSQL costs
**79 % less than the cost of Pinecone p2**($3,889/mo on Pinecone vs. $835/mo self-hosted on AWS EC2). ![A bar graph showing that PostgreSQL costs 79 % less than the cost of Pinecone p2 ($3,889/mo on Pinecone vs. $835/mo self-hosted on AWS EC2).](https://www.timescale.com/blog/content/images/2024/06/pgvector-vs-pinecone_monthly-cost-pinecone-s2.png)
## Operational Advantages of PostgreSQL vs. Pinecone
Pgvectorscale and pgvector have several operational advantages compared to Pinecone due to its PostgreSQL foundation:
**Rich support for backups:**It supports consistent backups, streaming backups, and incremental and full backups. In contrast, Pinecone only supports a manual operation to take a non-consistent copy of its data called “Collections.” **Point-in-time recovery:**for recovering from operator errors. **High availability:**for applications that need high-uptime guarantees. **Flexibility and control:**Pinecone lacks the ability to control the accuracy-performance trade-off in approximate nearest neighbor searches. Pinecone seems to have only three options for controlling index accuracy; developers can use either the s1, p1, or p2 index types. This locks developers into choosing an accurate-but-very-slow index (s1) or a fast-but-not-accurate index (p2) with no options in between. In contrast, pgvectorscale can be fine-tuned to production requirements using index options. In addition, the PostgreSQL ecosystem supports multiple index types, which can, for example, speed up queries on the associated metadata or perform full-text searches. Plus, partial indexes can speed up queries on key combinations of vector and metadata searches. **Better observability and debugging tools**: Pinecone provides only five observability metrics: request counts, request errors, request latency, vector count, and pod fullness. These can be viewed in their web dashboard or exported through Prometheus or Datadog. While this is valuable, it is really the bare minimum, and when something is not performing well, one has little information available to use for debugging. On the other hand, PostgreSQL has an extremely rich ecosystem of observability tools. For example, the [for Prometheus collects hundreds of metrics by default. Leaving aside the machine-level and OS-level observability tools at hand when self-hosting, PostgreSQL provides the ability to](https://github.com/prometheus-community/postgres_exporter?ref=timescale.com) __postgres_exporter__ [and](https://www.postgresql.org/docs/current/runtime-config-logging.html?ref=timescale.com) __view log messages__ [, get an explanation of how a query will be executed with the](https://www.postgresql.org/docs/current/auto-explain.html?ref=timescale.com) __automatically log slow queries__ [, track statistics of query planning and execution over time with](https://www.postgresql.org/docs/current/sql-explain.html?ref=timescale.com) __EXPLAIN command__ [, track statistics on all aspects of the database with the](https://www.postgresql.org/docs/current/pgstatstatements.html?ref=timescale.com) __pg_stat_statements__ [, view the contents of PostgreSQL’s memory with](https://www.postgresql.org/docs/current/monitoring-stats.html?ref=timescale.com) __cumulative statistics system__ [, and modify the contents of shared_buffers with](https://www.postgresql.org/docs/current/pgbuffercache.html?ref=timescale.com) __pg_buffercache__ [. When something is “not right” in a PostgreSQL database, you have many tools at your disposal to diagnose the issue.](https://www.postgresql.org/docs/current/pgprewarm.html?ref=timescale.com) __pg_prewarm__
## Pgvector vs. Pinecone: Benchmark Summary
**Pgvectorscale** is a new open-source extension that enables developers to build more scalable AI applications using PostgreSQL, with higher-performance embedding search and cost-efficient storage.
To test the performance impact of pgvectorscale, we created a fork of the ANN benchmarks tool to compare the performance of PostgreSQL and Pinecone on a dataset of
**50 million Cohere embeddings**.
Compared to Pinecone’s storage optimized index (s1), PostgreSQL with pgvector and pgvectorscale achieves
**28x** lower p95 latency and **16x** higher query throughput for approximate nearest neighbor queries at 99 % recall, all at 25 % the monthly cost.
Compared to Pinecone’s performance-optimized index (p2), PostgreSQL with pgvector and pgvectorscale achieves
**1.4x **lower p95 latency and **1.5x** higher query throughput for approximate nearest neighbor queries at 90 % recall, all at 21 % of the monthly cost.
Thanks to pgvectorscale, developers can now use the open-source general-purpose PostgreSQL database to achieve
**comparable (and often superior) performance** to specialized vector databases like Pinecone.
## Build your AI applications with PostgreSQL today
Pgvector and pgvectorscale are both open source under the
[ and are available for you to use in your AI projects today. PostgreSQL License](https://github.com/timescale/pgvectorscale/blob/main/LICENSE?ref=timescale.com)
You can find installation instructions on the
[ and pgvector](https://github.com/pgvector/pgvector?ref=timescale.com) [GitHub repositories, respectively. You can also access both pgvector and pgvectorscale on any database service on](https://github.com/timescale/pgvectorscale/?ref=timescale.com) __pgvectorscale__ [.](https://console.cloud.timescale.com/signup?ref=timescale.com) __Timescale’s cloud PostgreSQL platform__
For production vector workloads, we’re offering private beta access to vector-optimized databases with pgvector and pgvectorscale on Timescale.
[. Sign up here for priority access](https://timescale.typeform.com/to/H7lQ10eQ?ref=timescale.com)
### How to get involved
Both pgvector and pgvectorscale are open-source community projects. Here’s how you can get involved:
**Share the news with your friends and colleagues:**Share our posts announcing pgvectorscale on [,](https://x.com/TimescaleDB?ref=timescale.com) __X/Twitter__ [, and Threads. We promise to RT back.](https://www.linkedin.com/company/timescaledb/?ref=timescale.com) **Submit issues and feature requests:**We encourage you to submit issues and feature requests for functionality you’d like to see, bugs you find, and suggestions you think would improve both projects. Head over to the [to share your ideas.](https://github.com/timescale/pgvectorscale/?ref=timescale.com) __pgvectorscale GitHub repo__ **Make a contribution:**We welcome community contributions for pgvectorscale. Pgvectorscale is written in Rust. You can find [.](https://github.com/timescale/pgvectorscale/blob/main/CONTRIBUTING.md?ref=timescale.com) __instructions for how to contribute in the pgvectorscale repo__ **Offer the pgvectorscale extension on your PostgreSQL cloud:**pgvectorscale is an open-source project under the [. We encourage you to offer pgvectorscale on your managed PostgreSQL database-as-a-service platform, and can even help you spread the word. Get in touch via our](https://github.com/timescale/pgvectorscale/blob/main/LICENSE?ref=timescale.com) __PostgreSQL License__ [and mention pgvectorscale to discuss further.](https://www.timescale.com/contact?ref=timescale.com) __Contact Us form__