While big models captured all the early glory with their larger context windows, greater parameters and more power, the reality on the ground for many enterprise engineering teams has gotten increasingly frustrating. Scale alone felt like it would generate intelligence, but most AI projects still feel like prototypes because the industry chased model size at the expense of the real bottleneck, retrieval.

We’ve reached the stage where enterprises need accuracy over novelty, with an AI strategy that uses the information they already have instead of hallucinating its way through complex questions. This is why [retrieval-augmented generation (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) has become the main event, making language models stop guessing and start grounding their answers in real data. The companies that master this shift will build production-ready AI systems, while those that don’t will keep building impressive demos that struggle out of the pilot stage.

RAG seems relatively simple enough on the surface: Combine the language understanding of a [large language model (LLM)](https://thenewstack.io/what-large-language-models-can-do-well-now-and-what-they-cant/) with the precision of a search engine, let the system pull relevant documents for context and then generate a response. The reason it’s showing up everywhere, though, is that it solves the [hallucination problem](https://thenewstack.io/agentic-ai-is-key-to-preventing-costly-ai-hallucinations/), which has been the most painful failure mode in AI systems. By forcing the model to color inside the lines and giving it the right context at the right time, retrieval makes AI feel useful in a way that no one can get from an AI that invents facts.

## **The Real Production Gap**

Missing retrieval infrastructure is the real AI production gap. Most large corporations that have tried to bring agentic systems and LLM-driven tools into production never make it past pilot stages, running into brittle workflows that can’t explain their decisions or show where an answer came from. [Carnival Cruise Lines made that clear](https://fortune.com/2025/09/03/with-100-gen-ai-pilot-projects-but-just-six-in-production-carnival-cruise-lines-cio-takes-a-measured-approach-to-artificial-intelligence-journey/) when describing its own challenges, and the story is the same across many organizations where business logic becomes invisible and projects stall when the reasoning chain can’t be inspected.

Because business logic doesn’t translate cleanly into embeddings, you can’t encode precise operational rules into a vector space and expect consistent outcomes. A weak retrieval layer causes the model to behave like a reference library with missing citations — an authoritative presentation without verifiable sources.

This problem compounds when [retrieval pulls from noisy or inconsistent data sources](https://thenewstack.io/ai-wont-save-you-from-your-data-modeling-problems/). The model will ground itself on the wrong material, producing answers that may look polished but rest on rotten foundations. RAG makes this failure mode more visible, forcing companies to deal with an often-painful reality that most data needs serious work before AI can use it effectively. Better retrieval demands better data hygiene, and it’s a necessary correction that teams can no longer pretend to ignore.

## **The Infrastructure Shift Is Underway**

You can see this shift in what the major databases are shipping. Open source databases like [Postgres](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/), [OpenSearch](https://www.instaclustr.com/blog/ai-search-for-opensearch-unlocking-next-generation-search/) and Cassandra are leading the charge, adding vector search (like Postgres [pgvector](https://docs.netapp.com/us-en/netapp-solutions-ai/vector-db/ai-vdb-instaclustr-pgvector.html)), semantic search, hybrid retrieval and graph capabilities that give enterprises the flexibility to build retrieval systems exactly the way they need them. These fully [open source projects evolve faster precisely because contributions](https://thenewstack.io/clouds-code-and-control-the-new-open-source-power-struggle/) come from everywhere — not just bug reports and suggestions, but actual production-tested code from engineers solving real-world problems. The pace of innovation outstrips what any single vendor can match and gives enterprises the flexibility to customize retrieval logic for specific domains while deploying wherever the data lives.

[![](https://cdn.thenewstack.io/media/2026/01/c914d377-image1-1024x837.png)](https://cdn.thenewstack.io/media/2026/01/c914d377-image1-1024x837.png)

The [open source advantage](https://thenewstack.io/how-to-explain-the-security-advantages-of-open-source/) here is practical, not just philosophical. When retrieval becomes critical infrastructure, enterprises cannot afford to treat it as a black box. They need to understand how similarity scoring works, why certain documents rank higher and how to tune behavior for domain-specific queries. Proprietary vector databases might lock teams out of these decisions, while open source projects let engineers inspect, modify and optimize the entire stack.

While retrieval itself has been around for years, what’s changed is how central it’s become to actual AI deployment. Vector-only retrieval has made the production gap worse. While embeddings are powerful, they have limits that enterprises are now confronting, including losing fidelity on numbers, blurred distinctions between similar entries and a struggle with exact business constraints.

## **Why Hybrid and Graph Retrieval Matter**

This is why hybrid retrieval is taking off, with Uber’s Enhanced Agentic RAG combining vector search and BM25-based retrieval to [improve answer accuracy by 27%](https://www.uber.com/en-IN/blog/enhanced-agentic-rag/), and NVIDIA and BlackRock demonstrating that hybrid RAG with graph grounding [can reach 96% faithfulness](https://arxiv.org/html/2408.04948v1) in complex financial Q&A. These are early signals of where the industry is heading, and many of these systems are built on open source foundations that can be adapted and extended for specific use cases.

Because business logic is inherently relational (policies are relational, inventory systems are relational) graph retrieval is returning to connect these relationships in ways that vectors cannot. This restores the ability to model structure, and pairing graph with vector creates range: Graph gives precision and truth while vector gives flexibility. Together, they reflect the real shape of enterprise data.

Open source graph databases and vector stores are making this hybrid approach accessible without forcing companies into proprietary ecosystems. This matters even more as data ownership pressures in the EU make local retrieval a priority, as companies want accuracy without shipping data to external endpoints. But beyond compliance, open source infrastructure gives organizations genuine control. When a proprietary vendor changes its API, deprecates a feature or pivots its product strategy, your retrieval layer doesn’t break. The strong community-driven nature of open source projects like Postgres, Cassandra and OpenSearch means enterprises can depend on stable, well-supported infrastructure that won’t disappear based on quarterly earnings pressure.

When retrieval is critical infrastructure, the ability to modify, extend and truly own your retrieval stack matters. You need to be able to tune it to your domain, inspect how it works and adjust it as your requirements evolve.

## **Observability Is the Missing Layer**

Enterprises want to see which documents were retrieved, understand why those documents ranked higher than others and trace each answer back to the original request. AI governance rules are moving in the same direction, with regulators demanding transparency for both model behavior and agent behavior. Retrieval is the layer that can create this transparency and act as the transaction log for AI, making governance and compliance possible in ways they wouldn’t be otherwise.

The pattern is clear: Companies getting the most value from AI will be the ones that treat retrieval as critical infrastructure. They’ll invest in hybrid systems combining structured search, semantic similarity, vector embeddings and graph reasoning while building retrieval layers that are observable, local and tuned to their domain.

Open source gives them the foundation to do this without vendor lock-in, and the flexibility to adapt as retrieval techniques continue to evolve. The same design rigor that goes into indexing, caching and query planning will be applied to retrieval systems.

## **Building the Future**

RAG’s popularity is a necessary course correction. Models need grounding, guardrails and memory with structure, which are all things that retrieval provides while aligning AI with the real world. Retrieval serves as the bridge between ambition and reliability, taking the promise of AI and giving it a foundation.

The open source community has already proven this model works for databases, operating systems and web infrastructure. Now it’s proving the same for AI retrieval. But many of the companies winning with production AI aren’t using the flashiest proprietary tools, but building on open source foundations they can inspect, extend and trust.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/12/c12c1a8c-cropped-33e03ec9-carlosrolo.jpeg)

Carlos Rolo is manager of Open Source Contributions at NetApp Instaclustr, which provides a managed platform around open source data technologies including Cassandra, Kafka, Postgres, ClickHouse and OpenSearch. With expertise in Rust, Python and a strong foundation in Go, Carlos...

Read more from Carlos Rolo](https://thenewstack.io/author/carlos-rolo/)