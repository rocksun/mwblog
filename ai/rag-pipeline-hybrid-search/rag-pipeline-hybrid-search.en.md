## And how to fix it with hybrid search

A few months ago, one of our users filed a bug report that stuck with me. They had built a customer-support agent on top of a RAG (retrieval-augmented generation) pipeline. They encountered the following scenario: A user asked whether they could return a laptop purchased three weeks earlier. The agent retrieved a return policy document, quoted a 30-day window, and told the customer to ship it back. Perfectly confident answer. Completely wrong.

The document was real — it just happened to be from 2023, and the current policy has since changed to a 14-day window for electronics. Vector similarity has no notion of recency or scope, as the cosine distance between the query embedding and the 2023 policy was excellent. Why wouldn’t it be? The words were almost identical.

When I dug into this, I realized it wasn’t really a bug. It was an architectural problem. This laptop return request changed how I think about what a database needs to do in the AI era.

## The gap nobody talks about

As teams move RAG from prototype to production, we’re seeing this type of problem more frequently. We’ve spent the last two years as an industry fixated on hallucination, or models making things up. RAG was the answer: ground the model in real documents. And it works. But somewhere along the way, we started treating retrieval as a solved problem. It isn’t.

Here’s the thing I keep coming back to: Semantic similarity and factual correctness are not the same thing. A vector search finds documents that are close in meaning to your query. That’s useful, but “close in meaning” doesn’t mean “correct for this context.” A deprecated policy is semantically similar to the current one. A document scoped to enterprise customers is semantically similar to a query from a free-tier user. A confidential document in tenant A’s namespace is semantically similar to a query from tenant B.

> “A vector search finds documents that are close in meaning to your query. That’s useful, but ‘close in meaning’ doesn’t mean ‘correct for this context.'”

I call this the “retrieval accuracy gap.” (It’s another type of RAG.) It’s the distance between what vector similarity thinks is relevant and what your application actually requires to be correct. And you can’t close it with better embeddings. The missing information — timestamps, scopes, permissions — is structured data. It lives in columns, not in vector space.

This is a database problem.

## What I mean by hybrid search

When I say hybrid search, I mean something specific: a single database query that combines vector similarity with structured SQL predicates. Not a two-phase pipeline where you do a vector search, get back 100 candidates, and then filter in application code. A single query, optimized holistically by the database engine.

The difference matters more than it sounds. When filtering happens in application code, you’re doing the expensive work — scanning the full vector index — before applying the cheap constraints. That’s backward. A database that understands both vector and relational operations can use selectivity estimates to decide whether to filter first or scan first. It’s the same query planning logic we’ve had in relational databases for decades. It just needs to extend to vector indexes.

Let me show you what this looks like concretely. Assume a schema like this:

```

CREATE TABLE documents (
  id         BIGINT PRIMARY KEY AUTO_INCREMENT,
  content    TEXT,
  embedding  VECTOR(1536),
  team_id    BIGINT NOT NULL,
  doc_type   VARCHAR(50),
  updated_at DATETIME NOT NULL,
  status     ENUM('active','deprecated','draft'),
  INDEX idx_embedding USING HNSW (embedding),
  INDEX idx_team_status (team_id, status)
);

```

Nothing exotic. Standard relational schema with a vector column. Here are three query patterns that address the failure modes I described.

### Pattern 1: recency filtering

The stale-document problem disappears when you add a time constraint:

```

SELECT id, content,
       VEC_COSINE_DISTANCE(embedding, @query_vec) AS distance
FROM documents
WHERE status = 'active'
  AND updated_at >= NOW() - INTERVAL 90 DAY
ORDER BY distance
LIMIT 5;

```

The WHERE clause prunes the candidate set before the vector scan. In a 10-million-row corpus, this typically eliminates 60–80% of the rows. The database gets faster *and* more accurate at the same time. That’s the kind of tradeoff I like.

### Pattern 2: tenant isolation via join

This is the pattern I worry about most, because when it fails, it’s a security incident, not just a bad answer:

```

SELECT d.id, d.content,
       VEC_COSINE_DISTANCE(d.embedding, @query_vec) AS distance
FROM documents d
JOIN user_permissions p
  ON p.team_id = d.team_id
WHERE p.user_id = @current_user
  AND d.status = 'active'
ORDER BY distance
LIMIT 5;

```

A relational join against a permissions table. No matter how semantically similar a document is to the query, the user never sees content outside their scope. The constraint is enforced by the database engine, not by application code that someone might forget to update.

Try doing this with a standalone vector database. You’d have to duplicate your entire ACL into metadata tags, re-index every time permissions change, and hope your tag-based filtering handles the combinatorial explosion of permission groups. I’ve watched teams try this. It doesn’t end well.

### Pattern 3: category ranking with aggregation

Sometimes the right answer isn’t a single document but a pattern across many documents. This query groups matches by type and finds where the signal is densest:

```

SELECT d.doc_type,
       COUNT(*)                                  AS match_count,
       MIN(VEC_COSINE_DISTANCE(d.embedding, @query_vec)) AS best_dist,
       GROUP_CONCAT(d.id ORDER BY
         VEC_COSINE_DISTANCE(d.embedding, @query_vec)) AS doc_ids
FROM documents d
WHERE d.status = 'active'
  AND VEC_COSINE_DISTANCE(d.embedding, @query_vec) &lt; 0.3
GROUP BY d.doc_type
ORDER BY match_count DESC, best_dist ASC
LIMIT 3;

```

This tells the LLM: *“The answer is most likely in the FAQ documents (7 matches) rather than the blog posts (2 matches).”* Then you retrieve the top documents from the winning category. It’s a GROUP BY. Vector databases can’t do GROUP BY. This is relational algebra, and it changes retrieval quality dramatically when your corpus contains overlapping document types.

## What the numbers look like

We modeled both approaches after production workloads against a 10-million-row enterprise knowledge base. This includes 18 months of content, a mix of document types, and 500 queries with human-labeled ground truth. Here’s what we found:

|  |  |  |
| --- | --- | --- |
| **Metric** | **Pure Vector (top-5)** | **Hybrid (top-5)** |
| **Recall@5** | 72% | 94% |
| **Precision@5** | 58% | 87% |
| **Stale doc in top 5** | 23% | < 1% |
| **Cross-tenant leak rate** | 8% | 0% |
| **p50 latency** | 45 ms | 62 ms |
| **p99 latency** | 120 ms | 155 ms |

The latency cost is 15–30 milliseconds. Invisible to the user. The zero cross-tenant leak rate isn’t a statistical improvement as it’s a guarantee enforced by a relational join. That’s the kind of property you can bring to a security review.

What I find interesting is that hybrid search is actually faster in many real-world cases because the structured filters dramatically reduce the vector search space. When 70% of your corpus is pruned before the vector scan even starts, the wall-clock time drops. Please keep in mind that results will vary depending on corpus distribution and filtering selectivity.

## The “vector sidecar” anti-pattern

I want to talk about an architectural pattern I see all the time, because I think it’s the root cause of most RAG quality problems in production.

The pattern goes like this: you have a primary database—usually MySQL or PostgreSQL—where your application data lives. Then you stand up a separate vector database for embeddings. Now you need a sync pipeline to keep them consistent. Every document insert, update, and deletion has to propagate to both systems. You’re maintaining two schemas, two connection pools, two monitoring dashboards, and a fragile ETL job in between.

I call this the vector sidecar, and it creates three problems that compound over time:

* **Consistency windows.** There’s always a gap where the two systems disagree. A document can be marked as deprecated in your primary database, but still gets returned by the vector store until the sync catches up. In the return-policy example, this is exactly what happened as the policy was updated in the primary database, but the vector index was stale.
* **No cross-system joins.** You can’t join your ACL table against your vector index in a single query. So you end up duplicating permission data as metadata tags, which means every permission change requires a re-index. At scale, this gets expensive and error-prone.
* **Double the operational surface.** Two databases mean two sets of on-call rotations, two capacity planning models, and two failure modes. I’ve been building distributed systems for over a decade, and the single most effective way to improve reliability is to reduce the number of moving parts.

> “I’ve been building distributed systems for over a decade, and the single most effective way to improve reliability is to reduce the number of moving parts.”

The alternative is straightforward: put vectors and structured data in the same database. One connection string. One transaction boundary. One consistency model. The database handles the query planning, deciding whether to scan the vector index first or filter first based on selectivity estimates.

This is one of the reasons we built vector support directly into [TiDB](https://www.pingcap.com/tidb/). When we started seeing our users run into these exact problems—consistency bugs, cross-tenant leaks, operational complexity—the answer wasn’t a better [sync pipeline](https://thenewstack.io/telemetry-pipelines-collectors-and-agents-whats-the-difference/). It was eliminating the need for a sync pipeline entirely.

## Why SQL compatibility matters here

There’s a practical dimension to this that I think is underappreciated. When we made the decision years ago to implement the MySQL wire protocol in TiDB, it was about reducing adoption friction. But in the AI era, it turns out to have a deeper benefit.

SQL is the lingua franca of application development. Every ORM speaks it. Every connection pool supports it. Every engineer on your team has written SQL queries. When your AI database speaks the same protocol, the hybrid search patterns I described above aren’t exotic since they’re just SQL queries. Your team doesn’t need to learn a new query language, a new client library, or a new operational model. They write the same SQL they’ve always written, with a vector distance function added.

I’ve learned from watching thousands of TiDB deployments that adoption barriers matter more than feature lists. The best architecture is the one your team can actually ship.

## When you don’t need hybrid search

I want to be honest about where pure vector search is perfectly fine, because I think the credibility of any technical recommendation depends on acknowledging its limits.

* **Single-tenant, single-document-type corpora.** If you’re building a knowledge base search over one product’s documentation for one team, a pure [vector search with a good embedding model](https://thenewstack.io/the-secret-sauce-for-vector-search-training-embedding-models/) will serve you well. The failure modes I described arise from heterogeneity, such as multiple tenants, document types, or time horizons.
* **Exploratory or creative use cases.** If the user is brainstorming—“find me something related to this idea”—approximate retrieval is actually what you want. Strict correctness isn’t the goal.
* **Human-in-the-loop workflows.** If a human reviews every result before it’s acted on, the cost of an occasional stale document is manageable. The stakes [change when agents take actions autonomously](https://thenewstack.io/how-autonomous-agents-are-changing-infrastructure-management/).

If correctness is optional, vectors are enough; if correctness is required, they aren’t. But the moment you have multiple tenants, documents that expire, or any scenario where an incorrect retrieval leads to an incorrect action without human review, you need hybrid search. For most production RAG systems, that’s day one.

## The middle layer

I’ve been thinking a lot about where the real leverage is in the AI stack. The industry has invested enormous energy in two layers: the embedding model (how well do we encode meaning?) and the generation model (how well do we synthesize answers?). Both are important. But between them sits a third layer that’s been treated as a commodity: the database query that actually retrieves context.

This middle layer is where correctness lives. The embedding model turns a question into a vector. The generation model turns documents into an answer. But the retrieval query determines which documents the model sees. Get this wrong, and everything downstream is wrong too, no matter how good your embedding or your LLM.

Hybrid search—combining vector similarity with relational filters in a single query, in a single database—is how you close the retrieval accuracy gap. It’s not a sophisticated technique. It’s standard SQL with a distance function. The only prerequisite is a database that doesn’t force you to choose between vectors and relations.

When we started building TiDB more than a decade ago, our thesis was that the database should adapt to the application, not the other way around. That meant MySQL compatibility, so you didn’t have to rewrite your app. It meant horizontal scalability, so you didn’t have to re-architect at growth inflection points. And now it means native vector support, so you don’t have to bolt on a separate system to build AI features.

The thesis hasn’t changed. The applications have.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/00b4347d-cropped-44729a2f-ed-huang.png)

Ed Huang is co-founder and CTO of TiDB powered by PingCAP. While he was at Wandou Labs, he worked on clustering Redis and created and open sourced Codis, a proxy based high performance Redis cluster solution. Ed then decided to...](https://thenewstack.io/author/ed-huang/)