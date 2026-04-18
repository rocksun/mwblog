People keep trying to collapse two very different storage jobs into one. S3 is durable, cheap, and effectively bottomless, so the temptation is obvious: why not use it for everything?

The hard part of running Postgres isn’t storing lots of bytes. The hard part is surviving the moments when the database has to stop and wait.

For a durable commit, Postgres must flush the WAL before it can tell the client that the transaction is complete. That flush happens in `XLogFlush()`, and the backend blocks until the kernel says the write is durable. On a good [enterprise NVMe drive](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) with power-loss protection, that can take tens of microseconds. On slower networked storage, it moves into milliseconds. Put anything object-storage-like in that path, and the gap gets much worse.

That difference matters because commit latency is not an abstract benchmark number. For a lightly loaded OLTP system, it sets a real ceiling on how quickly a single session can commit transactions. Group commit helps when many sessions commit at the same time, because several transactions can share a single flush. But many production applications do not run in that sweet spot all day. At lower concurrency, storage latency leaks straight into user-visible response time.

You can see the same pattern in recent [benchmarking work on managed Postgres services](https://clickhouse.com/blog/postgresbench): once workloads spill beyond memory, the systems with faster local storage usually separate themselves more clearly.

> “For Postgres, fsync is a promise, not just a write.”

Not all SSDs behave the same here, either. For Postgres, `fsync` is a promise, not just a write. Enterprise drives with power-loss protection can often acknowledge that promise earlier because the write is protected in a capacitor-backed cache. Consumer SSDs usually have less room to do that safely. That is why two drives that both look “fast” on paper can behave very differently under commit-heavy workloads.

The same problem shows up on reads. [Postgres](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) stores heap data and indexes in 8 KB pages. Miss the buffer cache and a backend blocks on a small page read. OLTP workloads do this constantly: index lookups, heap fetches, visibility checks, then more index lookups. NVMe is good at this. Object storage is not. The problem is not bandwidth. It is that Postgres wants lots of tiny, latency-sensitive reads, while S3 is built around larger, higher-latency object requests.

> “The problem is not bandwidth. It is that Postgres wants lots of tiny, latency-sensitive reads, while S3 is built around larger, higher-latency object requests.”

That mismatch gets worse once the working set no longer fits comfortably in memory. `shared_buffers` and the OS page cache help a lot, but only up to a point. When the database starts missing cache on hot queries, the latency of the underlying storage stops being a background detail and becomes the workload.

MVCC adds its own flavor of I/O amplification. An update does not overwrite a row in place; it creates a new tuple version and updates the affected indexes. Checkpoints bring full-page writes into the WAL stream. Hint bits can turn reads into writes. Vacuum eventually has to clean up dead tuples and keep transaction ID age under control. None of that is accidental. It is part of how Postgres gets concurrency and crash safety. It also means Postgres leans heavily on storage that can absorb a lot of small, scattered I/O without falling over.

That is why modern managed Postgres systems that rely on object storage do not put object storage directly on the hot path. The implementations vary, but the pattern is pretty consistent: keep a fast log, cache, or page-serving layer close to the database, and push colder or reconstructable state to a more durable remote tier. The interesting part is not the branding. It is the convergence. If you look across serious transactional PostgreSQL designs, they keep finding ways to protect the commit path from object-store latency.

Recent upstream work points the same way. PostgreSQL 18 adds asynchronous I/O support and raises expectations around concurrent storage access. That work is about letting Postgres drive fast storage harder, not about making object storage behave like a local SSD. The more Postgres improves at issuing parallel low-latency I/O, the more it benefits from NVMe and other storage that can answer quickly and predictably.

None of this is a knock on S3. [S3 is excellent](https://thenewstack.io/tidb-x-open-source-database/) at the jobs it was built for: WAL archiving, base backups, snapshots, retention, and feeding downstream analytical systems. It is also a good fit for the colder side of replication and migration workflows, whether that means initial loads, backfills, or large cutovers into another system. The operational trick is keeping those jobs out of the commit path. Teams that use [CDC pipelines](https://clickhouse.com/blog/postgres-cdc-year-in-review-2025) or plan [large Postgres migrations](https://clickhouse.com/blog/practical-postgres-migrations-at-scale-peerdb) are usually solving a different problem from the one a transaction commit solves.

The same separation helps with analytics. Postgres is excellent at transactions, but once you start asking it to run large scans and aggregations on the same boxes that handle commits, vacuum, and cache misses, resource contention shows up quickly. That is why so much engineering effort goes into moving analytical work off the OLTP path, whether through replication or a [separate open-source stack for Postgres and analytics](https://clickhouse.com/blog/postgres-clickhouse-oss). The goal is not to make Postgres do less. It is to let it stay good at the thing it already does well.

So the answer is not “NVMe or S3.” It is both, with a clean boundary between them. Let fast local or block storage handle commits, cache misses, checkpoints, and vacuum. Let object storage handle archives, backups, and colder history. Postgres performs very well when the hot path is in the microseconds range, and the cold path is for durability. It starts to struggle when those two jobs are forced into the same layer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/c15429d3-cropped-aa698fc3-alasdair_brown.jpeg)

Alasdair Brown has spent the past decade designing, building and operating data platforms, from user-facing, real-time analytics for top brands, to some of the world's largest nation state cyber-defense systems. He is an advocate for simple data architectures and often...

Read more from Alasdair Brown](https://thenewstack.io/author/alasdair-brown/)