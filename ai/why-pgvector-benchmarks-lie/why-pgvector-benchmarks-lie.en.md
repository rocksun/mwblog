As an [open source Postgres extension](https://github.com/pgvector/pgvector), pgvector lets you store and query vector embeddings alongside your relational data, using the same tables, transactions, and tooling you already run. Last October, Alex Jacobs [published a post called “The Case Against pgvector](https://alex-jacobs.com/posts/the-case-against-pgvector/)” that’s made the rounds in engineering circles. His argument is that the wave of blog posts evangelizing pgvector as a drop-in replacement for dedicated vector databases glosses over operational realities of running it at scale (I won’t go into those here, but the blog is certainly worth reading).

He wasn’t wrong. Most of what he described was accurate for vanilla pgvector at the time, and it highlighted a gap between what the blog posts promised and what teams encountered when they moved from a local Postgres instance to a prod workload. But the pgvector story has evolved quite a bit in the past few months.

HNSW indexing, introduced in v0.5.0, improved recall and query consistency compared to IVFFlat’s cluster-based approach. Incremental index builds have gotten more capable, and teams running pgvector in managed environments have developed operational patterns that address many of the failure modes Jacobs described.

This article is about how to succeed with pgvector after you’ve decided it’s worth pursuing. The Jacobs position is a fair description of what happens when teams treat pgvector as turnkey technology, but what follows is how to avoid that outcome.

## Laptop vs. production

A “works in a demo, breaks in prod” pattern with pgvector is probably a consequence of scale changes, which change which problems matter. A benchmark on 10,000 vectors at 128 looks clean, with fast queries and index builds. And yet that benchmark tells you next to nothing about how the same setup will function at 5 million vectors and 1,536 dimensions. At that scale, the index itself becomes an infrastructure concern.

An HNSW index across millions of high-dimensional vectors takes significantly more RAM to build than it does to query, and that memory gets drawn from your live production database. Index builds can run for hours, the query planner’s cost estimates on filtered vector queries can vary wildly, and after any deployment (or failover), the first users pay the cold cache penalty while the ANN algorithm finds its footing.

> “A benchmark on 10,000 vectors at 128 looks clean… And yet that benchmark tells you next to nothing about how the same setup will function at 5 million vectors and 1,536 dimensions.”

Think of these as engineering problems with known solutions, not blockers. Yes, they require a different operational mindset than standard relational SQL, and they can become visible only at the workload scale. But the teams caught flat-footed are those benchmarking representative data without a representative scale.

### Benchmarking before committing!

I strongly believe this is the most overlooked step in pgvector implementation. Skip it at your own risk, because it can cause more pain than any other misstep.

Community benchmarks can give you a rough sense of what to expect, but performance in your actual application will vary (often significantly) based on vector dimensions, data distribution, and dataset size. A benchmark run on 10k vectors with 128 dimensions tells you almost nothing about how *your* systems will behave with 5 million vectors at 1536 dimensions.

So before you commit to an index type or database config, run your own benchmarks on a representative dataset. Measure query latency, index build times, and search recall at the same workload scale you expect to hit. That hour you spend benchmarking now will save you from a less fun, much longer rearchitecture later on.

## Choosing and tuning your index strategy

The IVFFlat-versus-HNSW decision is a question of workload fit. Let’s start with IVFFlat. It builds faster and produces more compact indexes, making it a solid choice for periodic batch updates or relatively modest datasets. You control the speed/recall tradeoff by adjusting `lists` (how many partitions to create) and `probes` (how many to scan per query). A critical caveat, though, is that IVFFlat indexes require training data to create effective partitions (that should be built after your data is loaded, not before).

HNSW, however, wins out when you need low query latency and high recall under frequent vector queries. Its graph structure enables faster traversal, but index creation takes longer and uses up more memory. The key parameters here are `ef_search` (how broadly the algorithm explores during queries) and `M` (how many connections each node maintains).

Whichever you choose, though, *benchmark* these parameters against your actual query patterns and recall targets. The gap between default and optimized can be a big one… and then, when you settle on values that do work, store those settings alongside the index definition. When your team updates the embedding model six months from now, the dimensionality and distribution of your vectors will change, so the tuning parameters will need to be adjusted accordingly.

## Designing for hybrid retrieval

One of the more underutilized capabilities of running vector search inside [Postgres](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) is combining it with structured SQL operations. Way too many teams treat pgvector like a standalone vector store that just happens to live in Postgres. Those who do leave significant performance improvements on the table.

Instead of running a vector similarity search across your *entire* dataset, use SQL WHERE clauses to first narrow the candidate set. You could filter by tenant ID, language, content type, or date range. Then let the ANN index do its thing and scan that narrowed set, rather than the full table. Particularly in multi-tenant applications, this approach often improves query performance by an order of magnitude.

You can even go a step further with a two-stage retrieval pipeline. Start by running a fast ANN query to pull the top-N candidates. Then re-rank those candidates using exact distance calculations combined with business logic (freshness, user permissions, popularity weighting, etc.). By doing the re-rank in SQL, you keep the entire operation within a single transaction.

This hybrid approach is where pgvector’s integration with Postgres pays some of its biggest dividends. While purpose-built [vector databases](https://thenewstack.io/how-to-master-vector-databases/) handle similarity search well, combining that with arbitrary SQL filters and transactional business logic typically requires orchestration layers. But with open source pgvector, you just write SQL.

## Partition smart and warm intentionally

The way you structure your tables impacts vector query performance, and any instinct to partition *purely* by data volume misses the point.

Aim to partition on the fields that correlate with your actual query filters. So if your application always filters by tenant, partition by tenant. Then build per-partition vector indexes so the query planner can prune entire partitions at plan time, meaning the vector index only covers a fraction of your total dataset for any given query.

> “Any instinct to partition purely by data volume misses the point. Aim to partition on the fields that correlate with your actual query filters.”

Another piece that bites teams in production is cold-cache performance. After a deployment or failover, the pages backing your vector indexes won’t be in memory. The first users to hit the system pay the cost of loading those pages from disc while the ANN algorithm walks the graph. Enter a tool like `pg_prewarm` that lets you load hot pages into shared buffers *before* traffic comes in. You can build this into your deployment process so the transition from deploy to serving doesn’t degrade performance.

## Know thy boundaries

Every tool has limitations, and pgvector is no exception. The key is understanding them. pgvector is under active development, and version compatibility is a consideration since the tool supports certain Postgres versions but not others. Scaling requires the same kind of manual tuning you’d apply to any Postgres performance challenge, with no auto-tuning layer to handle memory allocation, query optimization, or index configuration.

For applications requiring sub-20ms latency across tens of millions of vectors, pgvector might be a strong starting point that eventually graduates into a purpose-built solution. Starting here lets you validate your use case and understand your query patterns (without the big upfront investment in separate infrastructure). Even if you outgrow it, you’ll migrate with much better knowledge of what you actually need.

## What separates teams that succeed with pgvector

One throughline is that those getting the most out of the pgvector approach it like any other serious Postgres workload. They’re benchmarking on representative data before making big architectural moves, and tuning index parameters deliberately rather than blindly accepting defaults. They’re also designing queries that leverage the full SQL toolkit and have a firm understanding of where pgvector fits well and where it doesn’t.

If your team already runs Postgres and [needs vector search](https://thenewstack.io/why-developers-need-vector-search/), pgvector removes a *significant* amount of architecture complexity from the question. The key is investing the operational effort to run it well. Jacobs was right that the blog posts skip over the hard parts… but the hard parts *are* manageable with the right operational approach.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/03/543f8dc1-naina_ananthaswamy-600x600.png)

Naina Ananthaswamy works in product management at NetApp Instaclustr, which provides a managed platform for open-source data technologies, including Cassandra, Kafka, Postgres, ClickHouse, and OpenSearch. Previously, she held product management roles at Cisco.

Read more from Naina Ananthaswamy](https://thenewstack.io/author/naina-ananthaswamy/)