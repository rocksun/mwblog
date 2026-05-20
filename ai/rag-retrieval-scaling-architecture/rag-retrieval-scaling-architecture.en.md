In production RAG systems, the biggest bottleneck usually isn’t the LLM. It’s retrieval.

Most teams start with a simple pattern: Encode the query, retrieve a handful of documents [from a vector database](https://thenewstack.io/writer-coms-graph-based-rag-alternative-to-vector-retrieval/), pass them to the model, and generate an answer. With small, well-organized datasets, this feels almost magical. The right document is usually among the top results. Context is clean. The system appears fast, accurate, and reliable.

But this success is an illusion.

As data grows, a few hundred documents become millions with messy metadata, duplicate versions, access controls, and ambiguous language, all under real latency constraints. The probability that the right document appears in the top results drops sharply. Retrieval quality degrades quietly, long before anyone notices.

The system still produces answers. But now the [model is working with an incomplete or irrelevant context](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/). It compensates by filling in the gaps. Responses remain fluent and confident, but increasingly wrong. What looked like intelligence starts to feel unreliable.

> “RAG systems rarely break because the model is weak. They break because retrieval architectures designed for tidy demos collapse under production scale.”

At that point, teams often blame embeddings, prompts, or model size. But the failure happens earlier. RAG systems rarely break because the model is weak. They break because retrieval architectures designed for tidy demos collapse under production scale.

The problem is not intelligence. It is recall.

## The retrieval gap

Imagine a company building an internal knowledge assistant for ten thousand employees. The system must search ten million documents: financial memos, technical specs, project plans, and meeting notes. Responses must arrive within 2 seconds. Financial answers must be correct.

An engineer asks:

*“What was the final decision on the Helios project budget in Q4, ignoring drafts?”*

The system retrieves ten documents. None contains the approved budget memo. Several contain early discussions. The language model produces a confident but incorrect answer.

Nothing is broken. The model behaved exactly as designed. It summarized the context it received. The failure isn’t “LLM hallucination.” The right evidence never made it into the context.

![Workflow diagram showing how a query can cause an LLM to output a wrong answer](https://cdn.thenewstack.io/media/2026/05/64a2a3f6-1.jpg)

This isn’t an edge case. It’s what happens when retrieval systems built for small datasets meet production scale.

## Why retrieval fails at scale

Large corpora behave differently from small ones. Relevant documents are buried deeper in ranking distributions. Metadata matters more. Exact terminology matters more. Permissions and filtering become essential. Latency budgets become strict.

Retrieving only a handful of candidates becomes statistically unreliable. The best document might be ranked 300th by semantic similarity but first by exact keyword match. Or filtered out by metadata. Or overshadowed by drafts.

> “Once retrieval misses the target, the rest of the pipeline cannot recover. No prompt can fix missing context.”

Once retrieval misses the target, the rest of the pipeline cannot recover. No prompt can fix missing context. No larger model can infer information that was never retrieved.

## The architecture that actually scales

Production RAG is not just a smarter prompt or a bigger model. It is a different retrieval architecture.

Instead of fetching a few candidates and hoping one is correct, scalable systems cast a wide net, apply filtering during retrieval, and progressively refine results through multiple ranking stages. Retrieval becomes a unified serving pipeline rather than a chain of disconnected services.

![Workflow diagram showing how scalable systems cast a wider net, receiving higher-quality context and generating a more grounded response.](https://cdn.thenewstack.io/media/2026/05/f2a36faa-2-1024x683.png)

The system retrieves many candidates quickly, filters early, ranks cheaply, reranks selectively, and sends only the best evidence to the model.

### Deep retrieval and progressive ranking

Scalable retrieval works like a funnel. First, gather a large candidate pool using fast approximate methods. Then score all candidates using cheap signals such as lexical relevance and embedding similarity. Finally, apply expensive neural rerankers only to the most promising subset.

This structure controls both quality and cost. Expensive computation is focused where it matters most.

![Workflow diagram showing how scalable retrieval applies expensive neural rerankers to the most promising subset.](https://cdn.thenewstack.io/media/2026/05/abfec88b-3-1024x1024.png)

Wide recall at the top. Precision at the bottom. Without this funnel, systems face a tradeoff between accuracy and latency. With it, they achieve both.

### The four scaling cliffs

Seen this way, the failure modes become clear:

**Cliff #1:** Candidate generation is too shallow. The correct document never enters the ranking pipeline.

**Cliff #2:** Retrieval is fragmented across multiple services. Each [network call adds latency](https://thenewstack.io/p99-conf-3-ways-to-squash-application-latency/) and introduces data inconsistency. Scores from different systems are not directly comparable.

**Cliff #3:** Expensive reranking is applied too broadly. Neural models run on hundreds or thousands of candidates, inflating cost and response time.

**Cliff #4:** Prompt engineering is used as a substitute for retrieval quality. When context is wrong, output remains wrong.

These are not model problems. They are serving architecture problems.

## Building RAG that actually scales

Production RAG requires a different retrieval architecture.

At a small scale, retrieval can behave like a loose pipeline of disconnected components. At the production scale, that approach breaks down. Retrieval must operate as a unified serving system that maximizes recall, controls latency, and progressively refines results.

The following four principles define what scalable retrieval systems get right.

### Principle #1: Treat retrieval as a serving system

The first shift is conceptual: retrieval is not a workflow;, it is a serving problem.

Stop thinking in terms of disconnected steps:

embedding service → vector database → filter script → reranker → LLM

Start thinking in terms of a unified system:

retrieval engine (hybrid search + filtering + ranking) → LLM

In production, these components cannot operate in isolation. Hybrid search, metadata filtering, and ranking must execute together, on the same data, within a single query path.

Vector similarity alone is not enough. Real queries depend on semantic understanding, exact keyword matching, structured filters such as time, entity, and permissions, andas well as learned ranking signals. These signals need to interact directly, not be stitched together across multiple services.

Systems like Vespa are designed around this idea, executing hybrid retrieval and multi-stage ranking inside a single serving layer. This avoids synchronization issues and eliminates unnecessary network hops.

The specific platform matters less than the architecture. What matters is that retrieval is integrated rather than fragmented across services, low latency rather than distributed across multiple execution paths, and progressively selective, moving from broad recall to precise ranking.Once retrieval is treated as a system, the next question becomes: *how do you ensure it actually finds the right information?*

### Principle #2: Hybrid retrieval + large candidate sets

Maximize recall in the candidate generation stage by combining hybrid retrieval with a sufficiently large top-K.

Semantic search captures conceptual similarity, while keyword search captures exact matches. Real-world queries depend on both. For example, a financial approval memo may not be semantically close to “budget decision,” yet it will contain exact project names, dates, and approval language. Pure semantic retrieval can miss it, while pure keyword search can miss related context. Hybrid retrieval combines both signals, significantly increasing coverage.

But the retrieval method alone is not enough. Candidate generation is fundamentally a recall problem, not a precision problem. If the relevant document never enters the candidate set, no downstream ranking model can recover it. That is why top-K should be set intentionally large, especially as corpus size and query ambiguity grow. Hybrid retrieval expands coverage across semantic and lexical signals, while larger candidate sets increase the probability that the correct document survives into later ranking stages. At this stage, recall matters more than precision.

High recall creates the conditions for effective ranking. Without it, the system is operating on an incomplete shortlist.

With a strong candidate set in place, the next challenge becomes efficiency.

### Principle #3: Multi-stage ranking matters

Neural rerankers are powerful, but too expensive to run across large candidate sets.

The solution is a multi-stage ranking pipeline. Early stages use fast, lightweight methods to eliminate obvious mismatches, while later stages apply more expensive models, such as cross-encoders or LLM-based rerankers, only to a smaller and higher-quality subset.

This structure balances relevance, latency, and cost. Early filtering reduces unnecessary computation, while expensive ranking models focus only on plausible candidates.

Without staging, systems face a difficult tradeoff: either run expensive models across everything and sacrifice latency, or restrict the candidate set too early and sacrifice recall. Multi-stage ranking removes that tradeoff, allowing systems to maintain large candidate pools while remaining efficient.

At this point, we have the mechanics. The final principle explains why all of this matters.

### Principle #4: Retrieval quality determines system quality

Language models do not verify facts. They synthesize responses from the evidence they are given.

If the retrieved context is precise, answers are precise. If the context is noisy, answers become uncertain. If the context is wrong, the answers are wrong.

This makes retrieval the dominant factor in system performance. Importantly, retrieval quality is not the result of a single decision, but of the entire pipeline: how candidates are generated, how many documents are retrieved, how ranking is staged, and how much irrelevant context ultimately reaches the model. Focusing on any one component in isolation misses the point because these decisions interact.

That is why retrieval should be evaluated as a system. Measure recall during candidate generation, track how recall changes across ranking stages, inspect how much irrelevant context reaches the prompt, and understand where latency is introduced throughout the pipeline.

When recall is low anywhere in the system, nothing downstream can recover. Improving prompts without improving retrieval is cosmetic optimization. Improving retrieval changes outcomes.

> “Improving prompts without improving retrieval is cosmetic optimization. Improving retrieval changes outcomes.”

RAG does not fail because language models are limited. It fails because retrieval pipelines are underspecified.

Small systems can tolerate shallow retrieval, fragmented components, and brute-force reranking. Large systems require deep candidate generation, unified serving, and staged computation. Scale forces discipline.

Production systems succeed when retrieval is treated as an end-to-end serving problem built around deep candidate generation, hybrid search, early filtering, progressive ranking, and precise context selection.

When the right evidence reaches the model, correct answers follow naturally.

The gap between a working demo and a reliable production system is not mysterious. It is architectural.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/c68dec91-jennypic-600x600.jpeg)

Jenny Morris is a Senior Principal Solutions Architect at Vespa.ai, where she operates at the intersection of AI infrastructure and enterprise strategy, working with organizations to build scalable AI search, personalization, and retrieval-augmented generation (RAG) systems. With deep expertise in...

Read more from Jenny Morris](https://thenewstack.io/author/jenny-morris/)