**P99 CONF is a virtual conference** on high-performance, low-latency applications. Its 2026 event ran [October 21–22](https://p99conf.io/agenda/). Here, we cover five of its [60-plus](https://p99conf.io/session/how-scylladb-eliminates-read-amplification-at-scale/) sessions. The recordings are available on demand at p99conf.io after registration.

Database storage design balances [read amplification](https://slatedb.io/docs/design/overview/), write amplification, and space amplification (RUM conjecture). Improving one can increase another, depending on the workload and configuration. The five talks below show how engineers make those trade-offs across different database systems.

## **Almog Gavra**, Co-Founder at Responsive (now Databricks)

Gavra frames database design around [read amplification](https://slatedb.io/docs/design/overview/) (data read per result), write amplification (data written per logical write), and space amplification (storage used relative to live data). A log favors fast writes but makes reads work harder; a sorted array does the reverse. As Gavra put it, “I think about LSM trees as a mechanism for tuning between these two extremes.”

LSMs were built for local disks, but their [immutable files](https://slatedb.io/blog/introducing-slatedb/) also fit object storage. Gavra points to Amazon S3’s lower storage cost, durability, and availability, then names the trade-offs: objects must be replaced rather than edited, each GET and PUT has a price, and cold reads are slower. In his example, a local NVMe cache miss takes about 150 microseconds, versus 20–30 milliseconds for S3 Standard — roughly two orders of magnitude. LSMs batch writes into immutable files; caching helps keep object-store reads off the hot path.

Gavra’s [SlateDB](https://slatedb.io/) is an open-source, object-store-native LSM library. It exposes a key-value interface over stores such as S3, GCS, and R2, so developers can build data systems without implementing their own LSM.

**Michael Litvak** (Senior Software Engineer) and **Felipe Cardeneti Mendes** (Technical Director), ScyllaDB

ScyllaDB’s presentation examines [Logstor](https://www.scylladb.com/2026/07/06/scylladb-vs-aerospike-wide-column-vs-key-value/), an opt-in storage engine for read-intensive key-value workloads, not a replacement for its existing LSM engine. For each key, an in-memory index stores a hash and the record’s location on flash. A read can return a cached value or find the record with one disk I/O, avoiding an LSM search across SSTables, Bloom Filters, and Indexed data structures. Tables using either engine can run in the same cluster with ScyllaDB’s existing drivers and consistency options.

The speakers’ preliminary read-dominant test sustained 1.1 million reads per second with p99.9 latency below one millisecond and p99.99 latency around 1.5 milliseconds. That test used 2 KB values; the earlier LSM examples in the talk used 1 KB values, so the results are not direct comparisons. They also reported similar throughput and sub-millisecond p99.9 latency in an 80% read, 20% write workload.

Logstor pays for those reads with a larger RAM index and more work on writes. Even a small update writes the full new value to a log, leaving the old record as dead space; segment compaction later reclaims it. The speaker positions it for bounded key sets, frequent overwrites, and point lookups where the extra memory is acceptable. During this talk, Mendes called the trade-off “optimized for time at the sacrifice of space.”

**Madelyn Olson**, Principal Software Engineer at AWS

Not every bottleneck is storage. Olson begins with Amazon ElastiCache customers who saw sudden p50 latency spikes, then tests where Valkey’s main execution thread reached its limit.

In Olson’s unpipelined GET benchmark, with about three million keys and 650 clients, p50 latency rose sharply near 150,000 requests per second. Valkey already had [I/O threads](https://valkey.io/blog/valkey-8-0-0-rc1/), but they sat idle while the main thread executed commands. The team used lockless queues to keep network I/O and command parsing active on those threads while command execution stayed on the main thread.

Olson reported a new ceiling of about 1.2 million requests per second in that workload — roughly eight times the earlier threshold. (This is the talk’s workload-specific result, rather than a general throughput guarantee.)

For horizontal scaling, Valkey 9.0 introduced atomic [slot migration](https://valkey.io/blog/atomic-slot-migration/). The source shard keeps ownership while it streams a snapshot and subsequent changes to a target, then transfers ownership once the target catches up. Olson said a roughly 40 GB, three-to-four-shard test ran about 10 times faster without load and about five times faster under a heavy GET workload. If a migration fails before handoff, the staged transfer can be aborted without losing end-user data.

The I/O threads can be added or removed as workload demands change. Olson’s operating advice is to use horizontal scaling for baseline capacity and vertical scaling for short bursts, while keeping command execution single-threaded for now. Her guiding principle? “Efficiency trumps headline numbers.”

**Nathan VanBenschoten**, Chief Architect at turbopuffer

VanBenschoten described turbopuffer’s search index at a scale of 100 billion vectors, representing more than 200 TiB of dense vector data. The company reports 200 ms p99 latency at more than 1,000 queries per second and 92% recall in early results. Object storage is the durable backing store, but this high-query-rate workload pins its data in local [SSD caches](https://marketplace.turbopuffer.com/blog/ann-v3). Hierarchical clustering groups nearby vectors; [RaBitQ](https://p99conf.io/session/searching-100b-vectors-on-object-storage-200ms-p99/) binary quantization shrinks a shadow index to one bit per dimension, allowing the search to narrow candidates before reranking a small subset using full-precision vectors.

The uncompressed search was limited by the bandwidth needed to move vectors from storage into memory. Quantization shifts more work into higher cache tiers, but it also increases arithmetic intensity, making the system CPU-bound.

“Often when you push down one bottleneck, a new one emerges,” VanBenschoten said. That gives the team a different optimization target, including more efficient vector instructions.

To hold an index this large on SSDs, turbopuffer splits it across machines. VanBenschoten says its separated compute-and-storage architecture favors fewer, [larger shards](https://p99conf.io/session/searching-100b-vectors-on-object-storage-200ms-p99/): a replacement machine can point to object storage and hydrate its local cache instead of receiving a full shard from another node. Queries fan out to the shards, and a coordinator combines their top results.

**Georg Kreuzmayr**, Software Engineer at TigerBeetle

TigerBeetle is a financial transactions database. In this talk, Kreuzmayr describes the concept of “diagonal scaling”: keeping hot data on local NVMe while extending the storage hierarchy to shared object storage for colder data.

A failed machine doesn’t need to reconstruct data already stored in object storage. As a scale illustration, he estimates that recovering 128 TB over a 100 Gbps network takes about three hours at line rate; if recovery takes longer than the interval between failures, a cluster can enter a failure spiral.

That design needs an object storage client compatible with TigerBeetle’s single-core transaction processing. Kreuzmayr cites the AWS C++ SDK’s blocking `getaddrinfo` call as one mismatch: A call on that core would stall transaction work. SDK thread pools, runtime allocation, and dependencies also conflicted with the project’s design goals.

TigerBeetle therefore built its own multi-cloud client rather than adapting the official SDKs. It supports S3, Azure, and GCP and can be tested with simulated I/O and injected faults.

Built in Zig, the client includes custom DNS, TLS, and HTTP components, uses `[io\_uring](https://p99conf.io/session/the-fastest-object-storage-client-in-the-world/)` and zero-copy sends, and allocates its working memory at startup. Kreuzmayr says the implementation is under 40,000 lines of code and has no dependencies beyond its toolchain. Those choices follow TigerStyle’s three principles: safety, performance, and developer experience.

In the talk’s S3 `PutObject` test — 8 MB requests over plain HTTP without checksums on an AWS `c7gn.metal-24xlarge` instance — Kreuzmayr reports uploads around 20 times faster than official SDKs and five times faster than a research implementation. For `GetObject`, he reports about three times the SDK throughput and roughly 25% more than the research implementation. He attributes the smaller download gain to the cloud TCP receive path. These are results for the stated test setup. The conference summarizes the broader client comparison as [4–10](https://p99conf.io/session/the-fastest-object-storage-client-in-the-world/) times faster than official GCP and AWS SDKs.

Kreuzmayr’s takeaway is that building the client required more upfront work but made the code easier to test and tune. As he puts it, “code stops being technical debt and ends up being an asset.”

# Performance is a process

Across the five talks, engineers identify different bottlenecks in storage, search, networking, and scaling. Their designs improve specific workloads while introducing new costs or complexity elsewhere.

***Watch these and more than 200 other P99 CONF talks on demand at*** [***p99conf.io***](http://p99conf.io)***. Registration is required. P99 CONF is a ScyllaDB community.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/11/1c01c260-doug-sillars.jpg)

Doug is a lifelong learner and educator, having focused his career on improving developer knowledge and experiences.  A Google Developer Expert for the web, O’Reilly author, international keynote speaker, and a prolific blogger, he relishes in simplifying the complex. When...

Read more from Doug Sillars](https://thenewstack.io/author/doug-sillars/)