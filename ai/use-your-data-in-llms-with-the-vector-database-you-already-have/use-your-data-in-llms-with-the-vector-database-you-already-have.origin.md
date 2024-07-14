# Use Your Data in LLMs With the Vector Database You Already Have
![Featued image for: Use Your Data in LLMs With the Vector Database You Already Have](https://cdn.thenewstack.io/media/2024/07/176c7349-server1-1024x576.jpg)
[Vector databases](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/) allow you to enhance your LLM models with data from your internal data stores. Prompting the LLM with local, factual knowledge can allow you to get responses tailored to what your organization already knows about the situation. This reduces “AI hallucination” and improves relevance.
You can even [ask the LLM](https://roadmap.sh/guides/introduction-to-llms) to add references to the original data it used in its answer so you can check yourself. No doubt vendors have reached out with proprietary vector database solutions, advertised as a “magic wand” enabling you to assuage any AI hallucination concerns.

But, ready for some good news?

If you’re already using [Apache Cassandra 5.0](https://cassandra.apache.org/_/Apache-Cassandra-5.0-Moving-Toward-an-AI-Driven-Future.html), [OpenSearch](https://opensearch.org/) or [PostgreSQL](https://www.postgresql.org/), your vector database success is already primed. That’s right: There’s no need for costly proprietary vector database offerings. If you’re not (yet) using these free and fully open source database technologies, your generative AI aspirations are a good time to migrate — they are all enterprise-ready and avoid the pitfalls of proprietary systems.

For many enterprises, these open source vector databases are the most direct route to implementing LLMs — and possibly leveraging [retrieval augmented generation (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) — that deliver tailored and factual AI experiences.

Vector databases store embedding vectors, which are lists of numbers representing spatial coordinates corresponding to pieces of data. Related data will have closer coordinates, allowing LLMs to make sense of complex and unstructured datasets for features such as generative AI responses and search capabilities.

RAG, a process skyrocketing in popularity, involves using a vector database to translate the words in an enterprise’s documents into embeddings to provide highly efficient and accurate querying of that documentation via LLMs.

Let’s look closer at what each open source technology brings to the vector database discussion:

## Apache Cassandra 5.0 Offers Native Vector Indexing
With its [latest version](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/) (currently in preview), Apache Cassandra has added to its reputation as an especially highly available and scalable open source database by including everything that enterprises developing AI applications require.

Cassandra 5.0 adds native vector indexing and vector search, as well as a new vector data type for embedding vector storage and retrieval. The new version has also added specific Cassandra Query Language (CQL) functions that enable enterprises to easily use Cassandra as a vector database. These additions make Cassandra 5.0 a smart open source choice for supporting AI workloads and executing enterprise strategies around managing intelligent data.

## OpenSearch Provides a Combination of Benefits
Like Cassandra, [OpenSearch](https://thenewstack.io/how-opensearch-visualizes-jaegars-distributed-tracing/) is another highly popular open source solution, one that many folks on the lookout for a vector database happen to already be using. OpenSearch offers a one-stop shop for search, analytics and vector database capabilities, while also providing exceptional nearest-neighbor search capabilities that support vector, lexical, and hybrid search and analytics.

With OpenSearch, teams can put the pedal down on developing AI applications, counting on the database to deliver the stability, high availability and minimal latency it’s known for, along with the scalability to account for vectors into the tens of billions. Whether developing a recommendation engine, generative AI agent or any other solution where the accuracy of results is crucial, those using OpenSearch to leverage vector embeddings and stamp out hallucinations won’t be disappointed.

## The pgvector Extension Makes Postgres a Powerful Vector Store
Enterprises are no strangers to Postgres, which ranks among the most used databases in the world. Given that the database only needs the [pgvector extension](https://github.com/pgvector/pgvector) to become a particularly performant vector database, countless organizations are just a simple deployment away from harnessing an ideal infrastructure for handling their intelligent data.

pgvector is especially well-suited to provide exact nearest-neighbor search, approximate nearest-neighbor search and distance-based embedding search, and at using cosine distance (as recommended by OpenAI), L2 distance and inner product to recognize semantic similarities. Efficiency with those capabilities makes [pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/) a powerful and proven open source option for training accurate LLMs and RAG implementations, while positioning teams to deliver trustworthy AI applications they can be proud of.

## Was the Answer to Your AI Challenges in Front of You All Along?
The solution to tailored LLM responses isn’t investing in some expensive proprietary vector database and then trying to dodge the very real risks of vendor lock-in or a bad fit. At least it doesn’t have to be. Recognizing that available open source vector databases are among the top options out there for AI development — including some you may already be familiar with or even have on hand — should be a very welcome revelation.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)