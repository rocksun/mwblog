![Abstract digital spectrum of purple and orange vertical lines on black, symbolizing AI search relevance.](https://cdn.thenewstack.io/media/2026/11/3302ce70-planet-volumes-gcebcjvfzcs-unsplash-1024x576.jpg)

AI agents have had a URL problem for a while. When an agent needs current information but has no search tool, it often makes up the web address it thinks the answer lives at. It might guess something like `docs.example.com/v4.2/auth`, try to load it, and get a “page not found” error because the page doesn’t exist. Then it either keeps guessing or falls back on outdated information from its training.

> “Live web search gives AI agents fresh pages. Deciding which ones to trust over your own data is still a ranking problem.”

Infrastructure providers have noticed. In October, [InfoQ reported](https://www.infoq.com/news/2026/10/cloudflare-web-search-api/) that Cloudflare opened a [beta Web Search API](https://thenewstack.io/deepseek-web-search-api/) in its AI Gateway. Agents can call several search providers through one interface and get live results back with source links, logging, and access controls attached. Cloudflare’s reasoning was refreshingly direct: Without search, agents tend to guess.

This is a welcome change, and live search will probably be a default agent tool within a year, but it solves only the finding part of the problem. Once fresh pages are in front of an agent, something still has to decide which of those pages, and which of your own documents, the agent should actually rely on. That decision lives in your retrieval layer.

## The problem: two pools of evidence, one context window

An agent working inside a company rarely answers from the web alone. It also has the data that makes it useful to that company: product catalogs, documentation, contracts, support history, account records,s and permissions. With web search wired in, every step of a task can now pull from two very different pools.

|  |  |  |
| --- | --- | --- |
|  | **Web results** | **Internal data** |
| **Freshness** | Often hours or days old | Can be months out of date without anyone noticing |
| **Quality** | Uneven: official docs next to forum threads | Curated, but written for a past state of the product |
| **Structure** | Mostly unstructured text | Mix of text, metadata and structured records |
| **Authority** | Has to be inferred from the source | Known, but rarely stored as a field |
| **Access control** | Public | Per customer, region, contract or role |

The agent has to reconcile these, often several times within one task. And the questions it needs answered are ones a search API was never built to handle. When yesterday’s vendor changelog contradicts an internal knowledge base article from last spring, which one wins? Does this result apply to this customer’s version and region? Is the agent even allowed to show it?

Those are ranking and filtering decisions. They depend on your data and business rules, so you have to make them where both are available.

## Why concatenating results breaks in production

The simplest integration is to run a web search, run an internal search, append one list to the other, and let the model sort it out. It may work well at first, but once it’s running against growing data and traffic, it tends to fail in a few predictable ways:

* **Conflicts go unresolved.** The model sees two confident sources that disagree and has no signal for which is newer or more authoritative, so it picks one or blends them into an answer that matches neither.
* **Staleness hides.** A 3-month-old knowledge base article that matches the user’s wording almost exactly will beat a 4-day-old changelog on similarity alone. Nothing in the embedding says the article is out of date.
* **Permissions are applied too late.** If access rules run after retrieval, restricted content may already be in the prompt. If they run crudely, useful results get dropped along with sensitive ones.
* **Cost and latency compound.** A person runs one search and reads the results. An agent can trigger a dozen or more retrieval calls in a single task as it plans, checks, and refines. Sending every candidate to the model on every call adds up quickly, and more context doesn’t reliably produce better answers.

A bigger context window doesn’t fix any of these. Sending the model fewer, better-chosen pieces of evidence does.

> “A bigger context window doesn’t fix any of these. Sending the model fewer, better-chosen pieces of evidence does.”

Clarm, a Y Combinator company that builds sales and support agents for open-source software companies, [hit this early](https://blog.vespa.ai/agentic-ai-powered-sales-for-developers-with-vespa/). Its founder, Marcus Storm-Mollard, said the team realized “search, not generation, was the real problem to solve.” Generating an answer was the easy part. Finding the right information to ground it in was the hard part, which is why Clarm runs text search, vector similarity, and structured filters through a single query instead of stitching separate stores together.

## What changes when agents search across sources

When agents combine live web results with internal data, they need to account for different retrieval methods, metadata, permissions, and ranking signals. Four design considerations stand out.

### 1. Retrieve across methods in one query

Keyword matching catches exact product names, error codes, and version strings, which embeddings are notoriously bad at. Vector search catches paraphrases and intent. Structured filters enforce hard constraints like customer, version, and entitlement.

Within a single indexed collection, hybrid retrieval can combine keyword matching, vector similarity, and structured filters. That does not, by itself, fuse results from an external web search API with results from an internal index. The two-source integration requires a separate design decision.

```

select * from evidence where
  ({targetHits: 200}nearestNeighbor(embedding, q) or userQuery())
  and visibility contains "customer"
  and product_version contains "4.2"

```

The broader lesson is that retrieval systems need to handle lexical matching, semantic similarity, and filtering together. These requirements matter regardless of the search platform chosen. Perplexity hit this wall when it set out to build search in-house for its answer engine. Its CEO, Aravind Srinivas, has summed up the company’s approach as “first solve search, then solve everything else.” But when the team [evaluated existing tools](https://vespa.ai/case-studies/why-perplexity-chose-vespa-for-ai-search/), it found that vector databases couldn’t reliably support even simple Boolean filters, while traditional search backends offered only primitive semantic ranking. It needed lexical retrieval, semantic retrieval, and filtering in one engine, at consumer scale, and chose Vespa to build it.

### 2. Rank on more than similarity

Relevance to the query is only one signal. Agents also need to weigh freshness, source authority, and business rules together: official documentation over forum threads, last week’s changelog over last year’s wiki page, the customer’s contracted version over the latest release.

[Multiphase ranking](https://docs.vespa.ai/en/ranking/phased-ranking.html) is a practical way to do this. A cheap first phase scores thousands of candidates on a blend of signals, and a more expensive learned model reorders the few that remain:

```

rank-profile agent_evidence {
    inputs {
        query(q) tensor&lt;float>(x[384])
    }
    rank-properties {
        freshness(published_at).maxAge: 7776000
    }
    first-phase {
        expression: bm25(body) + closeness(field, embedding) + 0.5 * freshness(published_at) + attribute(source_authority)
    }
    second-phase {
        rerank-count: 100
        expression: xgboost("evidence-ranker.json")
    }
}

```

The important part isn’t the specific weights. It’s that freshness and authority are explicit, inspectable inputs to the score, not something you hope the model infers from the text. (The `maxAge` setting controls how quickly [freshness decays](https://docs.vespa.ai/en/reference/ranking/rank-feature-configuration.html); here it’s 90 days.)

> “The important part isn’t the specific weights. It’s that freshness and authority are explicit, inspectable inputs to the score, not something you hope the model infers from the text.”

[Metal AI](https://blog.vespa.ai/agent-driven-intelligence-on-vespa-cloud/), which builds an intelligence platform for private equity firms, runs into this with due diligence questionnaires. Firms answer thousands of them from investors, and a model can’t freely generate the answers. They have to come from a bank of responses that legal has already approved, and that bank changes over time and lives in documents and spreadsheets. Similarity alone could easily surface an approved answer that’s been replaced. So Metal indexes the answer bank with recency in mind and ranks freshness alongside semantic similarity, so the agent pulls the current approved answer, not just the closest match.

### 3. Treat web results as candidates, not answers

Web search and internal retrieval often return separate result sets, each with its own relevance signals. Simply passing both sets to the model leaves it to reconcile differences in freshness, authority, and relevance.

A more deliberate approach is to evaluate [evidence from both sources](https://thenewstack.io/building-trust-agentic-rag/) against a consistent set of criteria before selecting what goes into the prompt. Vespa’s flexible ranking capabilities can support this approach, but the implementation depends on how the external results are integrated into the retrieval pipeline.

Depending on provider terms and system constraints, teams might index permitted external content into a shared search collection or retrieve from separate systems and apply a subsequent fusion or reranking step. There is no universal fusion method. Each option has trade-offs in latency, freshness, score comparability, and operational complexity.

### 4. Hold up at agent call volume

This isn’t a hypothetical load pattern. At Metal, AI agents handle [95% of retrieval](https://blog.vespa.ai/agent-driven-intelligence-on-vespa-cloud/), not people. When someone asks for a portfolio company’s EBITDA, an agent decides which entity types to query (documents, companies, metrics, activities), applies recency and workflow filters, runs the query, and then keeps going, paginating or pulling related entities until it has enough context to answer. [Clarm sees something similar](https://blog.vespa.ai/agentic-ai-powered-sales-for-developers-with-vespa/) from the other direction: developers working alongside its agents send thousands of queries a day, in sessions that have run as long as 22 hours.

> “They need the precision and controls of expert search, delivered with the low latency and high throughput of consumer search.”

Every one of those calls sits on the critical path to the agent’s answer. Retrieval and ranking need to stay predictable under that load, which favors [running inference where the data already lives](https://blog.vespa.ai/improving-llm-context-ranking-with-cross-encoders/) instead of shipping large candidate sets across the network to a separate ranking service. Every network hop you remove is latency you get back on every call, multiplied by every step of the task. Jon Bratseth, Vespa’s CEO, [describes this](https://vespa.ai/vespa-voice/#relevance-is-your-moat) as the central engineering challenge with agents: They need the precision and controls of expert search, delivered with the low latency and high throughput of consumer search.

## A worked example: the support agent and the changelog

Here’s a scenario most support teams will recognize. A customer upgrades a payments SDK from 4.1 to 4.2, their checkout integration stops working, and they open a ticket.

The agent does what you’d want and searches the web first. It finds the SDK’s changelog from four days ago, which deprecates the authentication call the integration relies on, and a forum thread where another developer posted a workaround. Then it searches internally, returning a March knowledge base article that still tells customers to use the old call, the customer’s account record showing they’re on 4.2, and a restricted engineering ticket about the same bug.

Handed to the model as one long list, this is a trap. The knowledge base article matches the customer’s wording almost exactly, so it ranks well on similarity. The forum workaround reads confidently. The engineering ticket contains notes the customer should never see.

When the retrieval layer is doing its job, both sets of evidence go through the same pipeline. In this example, the team uses a shared collection: web results are indexed into Vespa as short-lived documents alongside internal data, retrieved with one query and scored by rank profiles aligned with the same business rules:

![Diagram showing how both web search API data and internal data go through the same pipeline.](https://cdn.thenewstack.io/media/2026/11/1ed4d624-image-1024x843.png)

For this ticket, that means:

1. The visibility filter excludes the internal ticket at query time, so it never reaches the prompt.
2. The version filter keeps only material that applies to the library version on the customer’s account.
3. Ranking boosts the changelog for authority and recency, demotes the older knowledge base article, and keeps the forum thread as supporting evidence.
4. The model receives three or four well-ordered passages instead of twenty, each with its source.

In this illustrative outcome, the answer cites the changelog, explains the change, and points to the supported fix. The search API helps find fresh evidence, and the retrieval design determines which evidence the agent receives.

## Before you wire web search into an agent

* **Store dates and source types on everything.** Internal or external, every document needs a publication date and a source type you can rank on.
* **Write signals into the documents themselves.** Keep freshness, authority, and source type on each document instead of in a separate feature store. That way they shape ranking from the first phase, not just when reranking the top results.
* **Always include lexical signals.** Even when your embeddings are strong, keyword matching is what catches the exact version numbers, error codes, and product names agents depend on.
* **Filter in the query.** Apply permissions at retrieval time, not in post-processing.
* **Send passages, not pages.** Rank the chunks within each retrieved document and pass only the most relevant spans to the model, sized to what it actually needs per call.
* **Measure retrieval on its own.** Build a test set of real agent questions and track whether the right evidence lands in the top results, separately from how the model phrases the answer.
* **Load-test at agent volume.** Benchmark with the number of retrieval calls a typical task actually makes, not one query per request.

## Final thoughts

Managed web search for agents removes a real, frustrating failure mode, and more teams will adopt it as it leaves beta. That makes the next question more pressing. When an agent can see the open web and your private data at the same time, the quality of its work depends on how well it chooses between them.

Bratseth puts it more simply: [Relevance is your moat](https://vespa.ai/vespa-voice/#relevance-is-your-moat). As models get more capable and more widely available, most companies end up with access to roughly the same intelligence. What sets them apart is their own information and how well their systems use it. He breaks relevance into four parts: comprehensiveness, freshness, recall accuracy, and ranking quality. Live web search helps with the first two. The last two are still yours to build.

The model shouldn’t improvise that choice on every call. It belongs in a retrieval layer you can inspect, test, and tune, where you weigh freshness, authority, permissions, and relevance together. Web search helps agents find evidence. Ranking is how they decide what to believe.

For teams building agents, the practical next step is to [evaluate retrieval quality](https://thenewstack.io/retrieval-ai-agent-architecture/) separately from answer generation: test whether the right evidence appears, whether permissions are enforced before context assembly, and whether fresh and authoritative sources are prioritized when documents conflict.

If you want to try this pattern, [Vespa](http://www.vespa.ai) combines lexical, vector, and structured retrieval with multi-phase ranking in one pipeline, and it’s available as open source or as a managed service on Vespa Cloud. The [RAG Blueprint](https://github.com/vespa-engine/sample-apps/blob/master/rag-blueprint/README.md) walks through how to design the schema, retrieval strategy, and ranking phases step by step, and you can start a [free trial](https://vespa.ai/free-trial/) to build it yourself.

The post [Web search for agents is here: Why ranking still decides the answer](https://thenewstack.io/ai-agent-search-ranking/) appeared first on [The New Stack](https://thenewstack.io).