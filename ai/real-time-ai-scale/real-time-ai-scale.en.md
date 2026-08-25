Real-time AI at scale is harder than it looks. Pipelines that hum along in development routinely hit problems in production. It’s always easy to blame the model for all your problems. But issues like rising latency and degrading accuracy can usually be traced back to the data pipeline.

My colleague Tim Koopmans and I recently discussed what typically goes wrong with real-time AI at scale. After Tim shared some hard-fought lessons learned, we talked about how to avoid falling into these traps yourself – including the practices and infrastructure choices that can help you avoid them. You can watch the full video or read the key points below.

## Why AI performance fails at scale

Tim learned the following real-time AI performance lessons the hard way: through fits of frustration while building an ML-based financial trading app.

### You can’t dig yourself out of tail latency

All too often, latency looks fine in testing, then a P99 spike surfaces under real concurrent load. For example, as Tim’s app approached ~740K operations per second, its P99 latency skyrocketed to 3 seconds.

![Chart showing inference latency and request rate (ops/sec).](https://cdn.thenewstack.io/media/2026/08/c01c3eef-image2-1024x419.png)

“I kept blaming the model for being slow, but it turns out the model was fine,” Tim explained. “It was just that the feature lookups were killing me.” Each inference call was doing just a handful of reads, but those reads queued up [behind writes] under load. The average latencies seemed fine, but that [P99 tail latency](https://thenewstack.io/if-p99-latency-is-bs-whats-the-alternative/) was just unacceptable.

> “Tail latency isn’t a bug that you can fix, it’s a property of your architecture.”

Once you hit highly concurrent write throughput, you get lock contention – and that impacts the tail latencies. At this point, retries and bigger caches and connection pool tuning don’t help. As Tim put it, “Tail latency isn’t a bug that you can fix, it’s a property of your architecture. For example, if your storage engine is producing GC pauses at exactly the wrong moment, you’re going to cop a latency spike, no matter what.”

The culprit in Tim’s app was actually Postgres under pressure: “It’s not a slow database, but it was just a database being asked to do too much in this particular case,” Tim continued.

### Stale features kill accuracy

If you notice a mysterious accuracy drop that the model itself can’t explain, feature freshness might be the problem.

![Chart showing "User Profile Staleness" and "Vector Embeddings Staleness."](https://cdn.thenewstack.io/media/2026/08/db751b6e-image4-1024x420.png)

For Tim, this issue was particularly frustrating. User profile (wallet addresses) staleness was blowing past a five-minute SLA target by hours, vector embeddings were going stale, and offline evaluation metrics looked fine the entire time. As Tim put it, “You have this maddening situation where offline evaluation metrics look great, but as soon as you mix it in with online data, that performance is rubbish.”

> “Offline evaluation metrics look great, but as soon as you mix it in with online data, that performance is rubbish.”

When the model was in production, it started making calls that didn’t track. After spending what seemed like ages debugging the model, the model itself turned out to be fine. The problem was that the model was making decisions [based on old data](https://thenewstack.io/better-context-will-always-beat-a-better-model/) (garbage in, garbage out, essentially).

### Vectors indexes need maintenance

No matter what vector database vendors imply, “set it and forget it” isn’t a realistic strategy for embeddings. Every re-embedding pass rots the index a little more, whether you notice it happening or not.

![Four charts showing "Vector Search Recall Rate Degradation," "Vector Query Latency Growth," "Index Size Growth," and "Index Rebuild Lag."](https://cdn.thenewstack.io/media/2026/08/b094a160-image5-1024x484.png)

Tim hit this too. He was re-embedding content every time he improved the model, and the index quality rotted a bit more with every pass. At one point, he noticed that the recall rate (the share of true best-matches an approximate search actually finds) dropped to a dismal 42% – and query latency ballooned at the same time. He explained, “HNSW graphs degrade as they take on mutations. The nasty thing is you don’t really realize that until you realize your results are tainted.”

He advised others to treat a vector index like you’d treat any other database index. It needs the same care, love and attention as anything else you operate. That means:

* Monitor recall accuracy (and results returned)
* Plan for partial builds (or batch builds)
* Know that changing your similarity function, your search parameters, or your embedding model means starting the graph over from scratch.

### You gotta keep ’em separated

Another problem is resource contention – for example, training and serving fighting over the same hardware. Tim had just one machine doing double duty. With everything running on the same infrastructure, GPU, RAM, and CPU were all competing for resources. Side note: Many people don’t realize that vector [search is a CPU cost](https://thenewstack.io/cut-ai-search-costs/), not a memory cost, since you’re traversing a graph rather than just storing vectors.

![Charts showing "Ingestion vs Inference Trade-off" and "Resource Utilization (CPU and Memory)". Resource utilization is also depicted as a semi-circle pie chart.](https://cdn.thenewstack.io/media/2026/08/6eb725bc-image3-1024x466.png)

The fix is the same thing every distributed systems person already knows: [You gotta keep ‘em separated](https://youtu.be/1jOk8dk-qaU?si=ERPxZPk8n-jzvBD7). This is just good engineering principles: separate your write path from your read path, separate training from serving if you can afford it.”

### Retraining is inevitable

Recognize that retraining isn’t optional, and it isn’t free. Every model swap requires transition time.

Tim explained that there’s a dodgy window where the old model is still serving stale predictions and the new one hasn’t warmed up yet. For the database, this could mean new access patterns, cache misses, cold reads or request queues building up. When you notice that data is drifting, or user behavior is changing, the model you trained three months ago is getting worse – that’s the sign that it’s time to retrain.

It’s going to happen eventually, so plan for it. Tim’s own approach was blue-green deployments, canaries, running the old and new model in parallel under different names, and doing the actual cutover at the application layer rather than all at once. If you’re at, say, Tripadvisor scale – with 100 million ML models – you can imagine the process will be considerably more complex.

## Avoiding the doom loop with a high-performance database

These problems tend to build on each other and snowball. Latency causes staleness, staleness degrades accuracy, degraded accuracy triggers retraining, retraining causes contention, and contention makes latency worse again. It can create what Tim deemed a “doom loop.”

Here are some tips for avoiding that doom loop.

### Monitor, monitor, monitor

Be obsessive about monitoring. Watch freshness and backlog in particular because a growing backlog is what eventually drives up tail latency. Also watch index health, since that’s where recall rots. And load test beyond steady state because you can’t really predict when some weird confluence of factors will cause usage to surge.

### Isolate your workloads

This addresses two of the problems from earlier: the write storms that caused tail latency, and training and serving sharing the same infrastructure.  A database that handles concurrent writes well and isolates workloads properly can absorb both.

For example, with ScyllaDB, the write path is lock-free and multi-writer. That means every node takes writes in an active-active fashion, and no row gets locked in the process. As a result, a burst of concurrent writes doesn’t back up into a queue the way it would on a database built around single-writer assumptions.

On top of that, a practice we call “[workload prioritization](https://www.youtube.com/watch?v=8BUsV8xZCcI)” controls how workloads compete for system resources. This ensures latency-sensitive queries are fast, even with other heavy workloads running on the same cluster. That way, a retraining job or a backfill won’t steal resources from whatever’s serving live inference.

### Separate vector indexing

To address the [vector index](https://thenewstack.io/vectors-tensors-ai-search-explained/) problem, keep the index separate instead of bolting it onto the same process as the core database. For example, ScyllaDB Vector Search writes land in the core database first, and the index gets built out of that data asynchronously, as its own service.

![Workflow diagram for ScyllaDB Vector Search](https://cdn.thenewstack.io/media/2026/08/b6d9b919-image1.jpg)

If the index can’t keep up with the write rate (whether from a re-embedding pass or a full rebuild after a similarity function change), it falls behind – but it never misses a write and the core database is not impacted. Even if the vector store goes down, the embeddings still persist in the core database. And because ANN queries are CPU-heavy, keeping them on a separate service means they’re not fighting the core database for the same CPU cycles the writes require.

Under [billion vector benchmarks](https://www.scylladb.com/2025/12/01/scylladb-vector-search-1b-benchmark/), that separated architecture held P99 latency under 10 milliseconds at a concurrency of 300. It handled ~150,000 ANN queries a second with a moderate recall target. Realize that higher recall will bring a latency and throughput tradeoff, and always test this in advance to assess how your own mileage varies.

### Absorb the shock

This one comes down to whether your infrastructure can absorb a sudden change in write pressure or traffic shape without a scramble. The storage engine’s architecture matters a lot here.

For example, ScyllaDB is built on an LSM-tree, which tolerates that kind of write pressure instead of degrading under it. Elastic scaling, with what we call “tablets,” can scale a cluster by something like 10x within minutes instead of hours. That means that if a model rollout changes your access patterns overnight, or you need to absorb a backfill before a big retrain, you don’t end up waiting on a multi-hour resharding job.

## The more things change…

So much about AI is genuinely novel, but the infrastructure problems described above generally are not.

> “Real-time AI is really a distributed systems problem in a costume.”

Tim mentioned that a feature store was probably the primitive use case: the same high write throughput, low latency work, years before anyone called it AI. Real-time AI is really a distributed systems problem in a costume. Once you understand that, you can design for it so you don’t get blindsided by these not-so-new challenges.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/09/93cd3bc0-cropped-c57adbb6-felipe-cardeneti-mendes-.png)

Felipe Cardeneti Mendes is an IT specialist with years of experience on distributed systems and open source technologies. He is co-author of three Linux books and is a frequent speaker at public events and conferences to promote open source technologies....

Read more from Felipe Cardeneti Mendes](https://thenewstack.io/author/felipe-cardeneti-mendes/)