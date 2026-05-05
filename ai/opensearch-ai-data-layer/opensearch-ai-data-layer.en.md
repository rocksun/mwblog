Most of the engineering teams I work with started with [open source OpenSearch](https://opensearch.org/) for log analytics and enterprise search. But as their requirements have since shifted to semantic retrieval and agent memory, they’re now trying to figure out just how much of that AI application stack they can consolidate onto infrastructure they already run.

The first quarter of 2026 has been very good news on that front. OpenSearch 3.5 and 3.6, which shipped in February and April, respectively, are worth understanding if you inherited an OpenSearch deployment and are now being asked to run agents on it. Here’s what to know.

## Dense and sparse vector search aren’t interchangeable

Teams like to start with `knn_vector`, and that’s understandable. Point it at your embedding model’s output dimension, enable k-NN on the index, and you are doing approximate nearest neighbor search. The default (Faiss, HNSW, L2 distance) covers a pretty darn wide range of use cases without much configuration.

The change in 3.6 that matters for organizations running this at scale is Better Binary Quantization, now integrated from the Lucene project. BBQ compresses high-dimensional float vectors into compact binary representations using quantization methods derived from RaBitQ, slashing the memory footprint by 32x.

On the Cohere-768-1M dataset, BBQ recall at 100 results is 0.63, compared to 0.30 for Faiss Binary Quantization. With oversampling and rescoring, it exceeds 0.95 on large production datasets. The OpenSearch project is also working to make 32x compression the default, which would eliminate the need for manual tuning.

Where `knn_vector` runs into trouble is term-level precision. Dense semantic search retrieves results based on meaning (which is good!), but it can miss exact-term relevance. A query for a specific product model number or technical identifier, for example, may bring up results that are conceptually similar but not the precise match you wanted.

This is the problem `sparse_vector` alleviates. Instead of representing a document as a point in continuous vector space, it stores it as a map of token-weight pairs. Each token is a vocabulary term, and each weight reflects how central that term is to the document’s meaning.

These 3.6 additions include BBQ flat index support for exact-recall workloads and the SEISMIC algorithm for neural sparse approximate nearest neighbor search, enabling large-scale sparse retrieval *without* a full index scan.

Most production AI search applications use both. Hybrid search combines dense semantic recall with sparse neural precision, and both field types are built around that pattern in mind. Most teams, in my experience, get more mileage out of understanding when each one earns its place in the pipeline than from picking a winner.

> “Hybrid search combines dense semantic recall with sparse neural precision, and both field types are built around that pattern in mind.”

## OpenSearch is absorbing the agent memory problem

Before 3.5, teams building multi-turn conversational agents had to solve memory outside of OpenSearch. You would maintain a session store elsewhere and manage context scoping in application logic (while wiring it all yourself).

OpenSearch 3.5 moves agentic conversation memory directly into the ML commons, with hook-based context management that gives developers the reins over how memory is stored, scoped, and retrieved during an agent session.

OpenSearch 3.6 goes even further. New semantic and [hybrid search](https://thenewstack.io/supercharge-your-rag-app-with-agentic-hybrid-search/) APIs enable agents to search stored memory using vector similarity, keyword matching, or both. An agent engaged in a long conversation can now retrieve contextually relevant prior exchanges rather than relying solely on recency, which matters when the relevant history is not the most recent turn. The V2 Chat Agent provides a cleaner interface for chat-based workflows while retaining tool and memory integration. A rebuilt Dashboards chat interface adds persistent conversation history that’s backed by the ML Commons Agent Memory APIs.

The practical effect of all this is that agent memory is handled natively by the platform rather than reinvented by each team. Hook-based APIs leave enough room for engineers to customize behavior wherever their requirements diverge from defaults, without requiring them to build the whole thing from scratch.

## Some of the less-covered changes that matter in production

Token usage tracking in the ML Commons agent framework is one of the most immediately useful additions in 3.6. Every LLM call during agent execution is instrumented to extract and aggregate token counts (per turn and per model) with no configuration required. It supports Amazon Bedrock Converse, OpenAI v1, and Gemini v1beta. If your team has been running agents without visibility into what API calls cost or which steps are expensive, this is a clear win.

> “If your team has been running agents without visibility into what API calls cost or which steps are expensive, this is a clear win.”

The async encryption refactor is less visible but fixes an important reliability issue. The legacy EncryptorImpl used a blocking CountDownLatch with a three-second timeout to manage master key initialization. During concurrent requests, this caused thread contention and a race condition where multiple tenants hitting the encryption layer simultaneously could trigger duplicate key generation.

The new implementation, contributed by my NetApp Instaclustr engineering colleague [Abdul Muneer](https://www.linkedin.com/in/muneer-kolarkunnu/), replaces that with an ActionListener-based approach that queues requests and processes them once the key is ready. (Side note: want to contribute yourself? Read Abdul’s blog about it [here](https://opensearch.org/blog/how-to-start-contributing-to-opensearch-a-beginners-guide-based-on-my-journey/).) In high-throughput environments, the old design produced intermittent failures under load.

Turning to observability: until 3.6, debugging a failed multi-step agent execution meant cobbling together your own instrumentation. OpenSearch now addresses this with Application Performance Monitoring built on OpenTelemetry standards, bringing RED metrics, distributed traces, service maps, and SLO tracking into OpenSearch Dashboards.

Time-series metrics are routed to Prometheus, trace data stays in [OpenSearch](https://thenewstack.io/opensearch-3-2-delivers-hybrid-search-enhanced-observability-tools/), and Data Prepper handles the split based on query patterns. The agent traces plugin gives teams a dedicated view for debugging agent executions directly from the UI.

## Is OpenSearch becoming the default data layer for AI applications?

The opensearch-agent-server in 3.6 adds in a multi-agent orchestration layer for integrating OpenSearch Dashboards and the [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/). MCP has become the standard for how AI systems communicate with external tools and data sources. Its inclusion here says something about intent. The project is moving toward OpenSearch as a full participant in agentic tooling ecosystems, with MCP as the connective tissue.

That direction was visible with 3.5, when the project introduced the experimental Agent-User Interaction protocol. OpenSearch is building toward a durable, observable, memory-capable substrate for AI applications, with the protocol support required to fit cleanly into a broader agentic stack.

Teams not yet considering agents will still gain clear value from 3.5 and 3.6, particularly on the vector search and compression side. But the roadmap is clear enough, in my view.

OpenSearch isn’t trying to be a better Elasticsearch; it is focused on being the data layer on which AI applications are built.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/04/2557b440-anilinamdar.jpg)

Anil Inamdar is the global head of Data Services at NetApp Instaclustr, which provides a managed platform around open source data technologies including Cassandra, Kafka, Postgres, ClickHouse and OpenSearch. Anil has more than 20 years of experience in data and...

Read more from Anil Inamdar](https://thenewstack.io/author/anil-inamdar/)