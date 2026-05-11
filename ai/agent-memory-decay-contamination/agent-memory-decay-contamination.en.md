A few months ago, I was reviewing a customer support agent who had a strange failure pattern. A user would chat with it on Monday about a billing issue, get partway through the resolution, and come back on Wednesday to continue. The Wednesday conversation would start from zero. The agent had no idea who the user was, what the previous issue had been, what had already been tried, or what had been promised.

The team had built the agent on a solid foundation. Idempotency keys on action endpoints. Workflow state machines for multi-step processes. Transactional writes for anything that touched billing. The infrastructure for correctness was there. What they didn’t have was a way for the agent to recall and reason about its own history, to know that this user, two days ago, had been promised a refund that hadn’t yet been issued.

That’s the problem I want to talk about. Not the parts of agent reliability that good systems engineering already solves. The harder layer above them: the agent’s ability to remember.

## First, what memory isn’t

Too many [architectural conversations about agent memory](https://thenewstack.io/ai-agent-memory-architecture/) get derailed because people use the word in different ways. Let me clear three of them away.

Memory is not idempotency. If your agent takes the same action twice because the same request hit your endpoint twice, the fix is an idempotency key. The agent doesn’t need to remember; the system needs to recognize the duplicate. Memory is not a workflow state. If your agent is mid-process, the fix is a state machine that records the current step and gates the legal transitions. Memory is not transactional consistency. If two agents are about to act on the same data, the fix is database-level isolation.

All three are necessary. None of them is memory. They keep individual actions correct; they don’t give the agent a sense of history.

## What memory actually is

I’ve come to think of agent memory as having five capabilities that have to work together. Persistent storage is one of them, and it’s the easy one. The others are where most production agents fall short.

* **Persistence:** the agent’s history survives session ends, process restarts, and deployments. Solved by writing to a database.
* **Selection:** the agent decides what is worth remembering. Storing every token of every conversation forever is both expensive and counterproductive. It dilutes the signal at recall time.
* **Compression:** raw history is summarized into something useful. A two-hour conversation becomes a paragraph plus structured facts. Without compression, retrieval cost grows linearly with interaction time.
* **Decay and forgetting:** old memories matter less than recent ones, and some should be forgotten. Without decay, stale information weighs the same as fresh information, which is exactly how RAG pipelines lie to you, [the topic of my last article](https://thenewstack.io/rag-pipeline-hybrid-search/).
* **Contamination prevention:** incorrect memories are worse than no memories. Bad facts, once stored, pollute every future decision. A real memory system flags uncertain memories, downgrades them when they are contradicted, and quarantines them when they are proven wrong.

Most discussions of agent memory collapse all five into the first. They argue about which database to use to store agent state, and call it solved. But persistence without selection gives you a slow agent. Without compression, an expensive one. Without decay, a confidently wrong one. Without contamination prevention, an agent that gets dumber over time. All five are necessary, and the substrate beneath determines which architectures you can build.

> “Persistence without selection gives you a slow agent. Without compression, an expensive one. Without decay, a confidently wrong one. Without contamination prevention, an agent that gets dumber over time.”

## A useful taxonomy

Memory has structure. Borrowing from cognitive science gives me a vocabulary for diagnosing where [agent architectures fail](https://thenewstack.io/serverless-cloud-architecture-is-failing-modern-ai-agents/).

* **Working memory** is the context window: current task, current turn. Fast, ephemeral. This is what most agents have today and confuse with memory in general.
* **Episodic memory** is the history of specific past interactions, with rich metadata: who, what, when, and outcome.
* **Semantic memory** is distilled knowledge. “This customer prefers morning flights.” “The finance API returns amounts in cents.” Queried by meaning, not by time.
* **Procedural memory** is learned behavior: which tool sequences work better than others. Almost nobody has this in production yet. It’s a topic for another article.

Working memory is a prompt string. Episodic memory needs structured time-series queries. Semantic memory [needs vector search](https://thenewstack.io/why-developers-need-vector-search/). The rest of this article focuses on episodic and semantic, where the real production gap lies.

## Why single-purpose stores fall short

The first thing most teams reach for is Redis. Fast, familiar, perfect for working memory. The problem is that key-value stores give you exactly one access pattern: get by key. That fails for episodic recall, which needs queries like “every successful refund I’ve issued for users in this region in the last 30 days.” That’s a relational query, not a key lookup.

The second thing teams reach for is a vector database. Embed past interactions, search by similarity. Useful for semantic memory, but it falls short for episodic recall, which often needs exact predicates: a specific user, a specific time window, a specific outcome. Cosine similarity doesn’t help when you need WHERE clauses. And vector stores typically can’t join against your application data, which means the agent can’t reason about memory in the context of who the user is.

Then there’s contamination handling. When a memory is found to be wrong, you need to update or invalidate it. In a vector store, that’s re-indexing. In a key-value store, mass cache invalidation. In a relational database with vector support, it’s an UPDATE. Memory systems live or die by how reliably bad memories get cleaned up.

## The schema, with the honest caveats

Here’s a reference schema for a layer that handles episodic and semantic memory in a single database.

```

-- Episodic memory: what happened, with outcomes
CREATE TABLE episodic_memory (
  id           BIGINT PRIMARY KEY AUTO_INCREMENT,
  agent_id     VARCHAR(64) NOT NULL,
  user_id      BIGINT NOT NULL,
  session_id   BIGINT NOT NULL,
  action_type  VARCHAR(100) NOT NULL,
  summary      TEXT,           -- compressed form
  raw_payload  JSON,           -- full detail, kept for audit
  outcome      ENUM('success','failure','pending'),
  confidence   FLOAT DEFAULT 1.0,
  superseded_by BIGINT NULL,   -- contamination invalidation
  created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  embedding    VECTOR(1536),
  INDEX idx_agent_user_time (agent_id, user_id, created_at),
  INDEX idx_embedding USING HNSW (embedding)
);
-- Semantic memory: distilled knowledge, with decay metadata
CREATE TABLE semantic_memory (
  id           BIGINT PRIMARY KEY AUTO_INCREMENT,
  agent_id     VARCHAR(64) NOT NULL,
  user_id      BIGINT,
  fact         TEXT NOT NULL,
  confidence   FLOAT DEFAULT 1.0,
  source_count INT DEFAULT 1,
  last_confirmed_at DATETIME NOT NULL,
  contradicted_at   DATETIME NULL,
  created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  embedding    VECTOR(1536),
  INDEX idx_embedding USING HNSW (embedding)
);

```

A few details that the simpler schema I’d have written a year ago didn’t have:

* **Both `summary` and `raw_payload` columns.** Compression isn’t optional. The agent reads `summary` at recall time; `raw_payload` is kept for audit and re-summarization.
* **`confidence` and `superseded_by`.** Memories aren’t immutable. `superseded_by` is a soft-delete pointer for contamination. When memory A is contradicted by memory B, A points to B and is excluded from recall. The original isn’t deleted; audit matters.
* **`source_count` and `last_confirmed_at`.** A fact confirmed by ten interactions is more reliable than one confirmed once. A fact last confirmed two years ago should weight less than one confirmed yesterday. These feed a decay function applied at recall time, not at write time.

**The data stays; its weight changes.** This is the principle running through all of the above. Memory records aren’t rewritten or deleted. They’re annotated, decayed, or superseded.

## Recall queries that reflect real memory behavior

With this schema, recall queries express harder behaviors than “find similar things.” This includes measures such as similarity weighted by recency and confidence, while excluding contaminated memories.

```

-- Semantic recall with decay and contamination filtering
SELECT fact,
       confidence
       * EXP(-DATEDIFF(NOW(), last_confirmed_at) / 90.0) AS effective_weight,
       VEC_COSINE_DISTANCE(embedding, @task_vec) AS distance
FROM semantic_memory
WHERE (user_id = @user_id OR user_id IS NULL)
  AND contradicted_at IS NULL
  AND VEC_COSINE_DISTANCE(embedding, @task_vec) &lt; 0.30
ORDER BY distance, effective_weight DESC
LIMIT 10;

```

The decay term EXP(-days/90) is a half-life of about 60 days. Customer preferences decay slowly. Inventory facts decay quickly. A real memory system tunes this per memory type.

These queries are doing real memory work. They’re not just retrieving rows. They’re modeling how confidence decays, how contamination propagates, how recency interacts with relevance. The database is the substrate. The intelligence lives in the query, not the row.

## Updating memory: optimistic and pessimistic patterns

Memory isn’t write-once. Confidence updates as new evidence arrives. Memories get superseded. These updates can occur concurrently, so we need to be deliberate about concurrency control. Two patterns are common, and the difference matters because they’re often conflated.

Pessimistic locking takes the lock first and holds it for the duration of the operation. Use this when contention is expected, and the operation is short:

```

-- Pessimistic: lock the row, then update
BEGIN;

SELECT confidence, source_count
FROM semantic_memory
WHERE id = @memory_id
FOR UPDATE;

-- Application computes new confidence

UPDATE semantic_memory
SET confidence = @new_confidence,
    source_count = source_count + 1,
    last_confirmed_at = NOW()
WHERE id = @memory_id;

COMMIT;

```

Optimistic concurrency control takes a different approach. No lock at read time; instead, you record the version of the row you read, and at write time you assert the version hasn’t changed. If it has, the update fails and the application retries. Use this when contention is rare and readers vastly outnumber writers:

```

-- Optimistic: read with version, write conditionally

SELECT confidence, source_count, version
FROM semantic_memory
WHERE id = @memory_id;

UPDATE semantic_memory
SET confidence = @new_confidence,
    source_count = source_count + 1,
    last_confirmed_at = NOW(),
    version = version + 1
WHERE id = @memory_id
  AND version = @read_version;

-- If 0 rows affected, another transaction won the race; retry.

```

Both are valid. Memory updates from human reviewers (low-frequency, high-care) fit pessimistic locking. Memory updates from background summarization jobs across millions of records (high frequency, low contention) fit optimistic concurrency. Mixing them carelessly within a single transaction (FOR UPDATE plus a version check on the same row you just locked) does redundant work and signals confusion about which model you’re committing to.

The point isn’t which to use. It’s that the database supports both, that they’re both ACID-correct, and that the agent doesn’t implement either in application code.

## State persistence is not memory, but memory needs it

Let me close with a distinction that matters more than most architecture discussions acknowledge.

What I’ve described in most of this article is a state-and-knowledge persistence layer. It’s the substrate. By itself, it’s not memory in the full sense. Memory is what happens when an intelligent system uses that substrate well: choosing what to remember, summarizing what to keep, weighing old against new, recognizing when something it believed was wrong, and bringing the right recollection to the right moment. The substrate doesn’t do those things. The agent does. But the agent can’t do those things without a substrate that supports them.

> “The substrate doesn’t do those things. The agent does. But the agent can’t do those things without a substrate that supports them.”

The question I’d ask any team building production agents is not “which vector database” or “should we use Redis.” It’s whether the substrate underneath your agent supports the full set of memory behaviors you’ll need within twelve months. Persistence, yes. But also: structured queries against episodic history. Vector recall over compressed summaries. Confidence decay computed at read time. Contamination invalidation as a first-class operation. Both pessimistic and optimistic concurrency. Horizontal [scale as the agent](https://thenewstack.io/cloud-native-and-open-source-help-scale-agentic-ai-workflows/) fleet grows.

This is what we’ve been thinking about as we’ve evolved [**TiDB**](https://www.pingcap.com/) to support agent workloads. Not “a vector database that also does SQL,” and not “a relational database with vectors bolted on.” But a substrate that handles all the storage patterns a real memory system needs, with the consistency and scale properties of distributed SQL. The schema is the easy part. The patterns the substrate enables are where the agent’s actual memory lives.

The workload is new. The discipline is older than that.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/00b4347d-cropped-44729a2f-ed-huang.png)

Ed Huang is co-founder and CTO of TiDB powered by PingCAP. While he was at Wandou Labs, he worked on clustering Redis and created and open sourced Codis, a proxy based high performance Redis cluster solution. Ed then decided to...](https://thenewstack.io/author/ed-huang/)