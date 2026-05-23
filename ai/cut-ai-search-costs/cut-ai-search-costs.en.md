## The cost that’s driving your AI search bill

Every organization running AI-powered search faces the same hidden cost driver: **query embeddings**. Documents are embedded once. Queries are embedded *continuously* for every user, every search, every second. At scale, this quickly becomes one of the largest line items in your AI infrastructure budget.

Together, Vespa AI and Voyage AI have solved this problem with a technique called **asymmetric retrieval**. Use the best embedding model available for your documents (once, at indexing time), then embed queries for free using a tiny, [locally running model](https://thenewstack.io/how-to-run-deepseek-models-locally-on-a-windows-copilot-pc/). Voyage AI’s **voyage-4** model family is built for exactly this. All four models share a common vector space, making the split practical without any reindexing or architectural changes.

> “Every organization running AI-powered search faces the same hidden cost driver: query embeddings.”

**Bottom line for decision-makers:** Your query embedding bill effectively goes to zero and your search path becomes more resilient, all without replacing your existing search infrastructure.

## The problem: Symmetry is expensive

The conventional approach uses the same embedding model for both documents and queries. It’s simple, but it ignores a critical asymmetry in how those two operations work.

|  |  |  |
| --- | --- | --- |
|  | **Document Embedding** | **Query Embedding** |
| **Frequency** | Once per document | Every single request |
| **Latency sensitivity** | None, no user is waiting | On the critical path, 24/7 |
| **Cost @ 10K QPS** | Amortized, negligible | ~$15,500/month |

At 10,000 queries per second with ~30-token queries, you generate roughly **777 billion tokens per month**, all routed through an external API at real cost.

## The solution: Asymmetric retrieval with Voyage AI + Vespa

Voyage AI’s voyage-4 family introduces four models (`voyage-4-large`, `voyage-4`, `voyage-4-lite`, and `voyage-4-nano`) that all produce embeddings in a **shared vector space**. You can embed documents with the most powerful model and query with the smallest, and they remain fully compatible.

Vespa now has native support for this workflow, running `voyage-4-nano` locally inside its container nodes, with no API calls, no rate limits, and no additional cost.

## How it works

### Step 1: index time: documents → `voyage-4-large` (API)

Embed each document once with Voyage AI’s top-tier model. The results are the highest accuracy, with no latency pressure. Cost is fully amortized over the document’s lifetime.

### Step 2: query time: queries → `voyage-4-nano` (local)

Embed every user query with a tiny model running inside Vespa. Runs in single-digit milliseconds on CPU. Zero external API dependency. Zero cost.

[Read the full technical blog](https://blog.vespa.ai/asymmetric-retrieval-spend-on-docs-queries-for-free/).

### Business impact at a glance

|  |  |  |
| --- | --- | --- |
| **Metric** | **Symmetric (traditional)** | **Asymmetric (Vespa + Voyage AI)** |
| Query embedding cost @ 10K QPS | ❌ ~$15,500 / month | ✅ $0 / month |
| Query embedding latency | ❌ API round-trip (10–80ms) | ✅ <5ms on CPU (local) |
| Retrieval quality vs. OpenAI v3 Large | Baseline | ✅ +14.05% NDCG@10 |
| API dependency on the critical path | ❌ Yes, outages affect search | ✅ No, fully self-contained |
| Re-indexing to upgrade the query model | ❌ Required | ✅ Not required |
| Multi-tier document quality | ❌ Not supported | ✅ Supported |

## Why operational resilience matters

Eliminating the external API from the query path is more than a cost optimization, it’s a reliability decision.

> “Eliminating the external API from the query path is more than a cost optimization, it’s a reliability decision.”

|  |  |  |
| --- | --- | --- |
| **Risk** | **Traditional Architecture** | **Asymmetric Architecture** |
| **API outage** | Search goes down | No impact, fully local |
| **Rate limiting** | Dropped/delayed requests on traffic spikes | No rate limits |
| **Scaling** | Days to negotiate a higher API quota | Minutes to add Vespa container nodes |

With asymmetric retrieval, the query path is entirely self-contained. Search works regardless of third-party API status.

## Advanced: two-phase ranking for maximum accuracy

Vespa combines this architecture with a two-phase ranking strategy that delivers both speed and precision at large scale.

Vespa stores document vectors in two forms, compact binary embeddings (16× smaller in memory) for fast first-phase retrieval, and full-precision bfloat16 (on disk) for accurate second-phase reranking. The result is binary-speed search with full-precision accuracy.

### Phase 1: full index scan

Hamming distance on binary vectors. ~1 billion distance calculations per second. Retrieves the top 2,000 candidates from the entire corpus in milliseconds.

### Phase 2: precision reranking

Bfloat16 dot-product on top candidates only. Full-precision vectors are paged from disk for the top 2,000 results. Accurate, and bounded in compute.

[Binary quantization](https://thenewstack.io/why-vector-size-matters/) also reduces storage: a 2,048-dimension vector shrinks from 4,096 bytes to **256 bytes**, a 16× reduction, with negligible impact on final ranking quality.

## Designed for enterprise scale

Vespa separates stateless container nodes (where embedding runs) from content clusters (where data lives), so query embedding capacity and document storage scale independently. Multi-tenant deployments can mix document embedding tiers within the same index, using `voyage-4-large` for premium customers and `voyage-4-lite` for cost-sensitive tiers, while all tenants share the same local query model.

## When to use this architecture

|  |  |
| --- | --- |
| **Scenario** | **Recommendation** |
| High QPS (>1,000 queries/sec) | ✅ Strong fit, savings scale linearly |
| Large document corpus | ✅ Strong fit, document embedding cost is amortized |
| Latency-sensitive applications | ✅ Strong fit, local inference eliminates network round-trips |
| Multi-tenant platforms | ✅ Strong fit, per-tier quality/cost control |
| Low volume (<100 QPS), latency-tolerant | Single model [may be simpler](https://thenewstack.io/ai-unified-data-foundation/) at this scale |
| Maximum quality, cost not a concern | Symmetric voyage-4-large for both is still an option |

## A joint solution from two AI search leaders

[**Vespa AI**](https://vespa.ai/) provides the industry’s leading open-source search and recommendation platform, powering AI applications at Spotify, Yahoo, and Perplexity.

[**Voyage AI**](https://www.voyageai.com/) delivers state-of-the-art embedding models. At the time of writing this blog, `voyage-4-Large` is ranked #1 on the RTEB benchmark across 29 retrieval datasets, outperforming Gemini Embedding 001 by +3.87%, Cohere Embed v4 by +8.20%, and OpenAI v3 Large by +14.05%.

## Get started


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/10/3f0d80bf-bonniechase-600x600.jpeg)

Bonnie Chase is a passionate product marketer at Vespa.ai with a knack for translating complex AI concepts into user-centric solutions. With over a decade in product strategy and go-to-market execution, she thrives at the intersection of technology and customer needs.

Read more from Bonnie Chase](https://thenewstack.io/author/bonnie-chase/)