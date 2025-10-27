The [Valkey](https://valkey.io/) open source data store has officially released version 9.0, marking its most significant update since the project’s launch as the [Linux Foundation-backed Redis fork](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/). The [Valkey 9.0 release](https://valkey.io/blog/introducing-valkey-9/) introduces multidatabase clustering, atomic slot migration and major performance optimizations designed to handle massive-scale workloads exceeding one billion requests per second.

Among its chief features, [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") 9.0 debuts multidatabase support in cluster mode. With this, developers can operate separate logical databases without sacrificing the high throughput and fault tolerance of distributed clusters. Thus, you can run Valkey in a sharded mode for large data sets or high-throughput use cases. Historically, this has been restricted to just one database, preventing efficient multitenancy of clustered installations.

## Atomic Slot Migration for Seamless Rebalancing

Another noteworthy feature is atomic slot migration. This enables seamless node rebalancing and replication without downtime, improving reliability for enterprise and cloud deployments. Valkey has always been highly scalable to large datasets (e.g., thousand-node clusters). Typically, application usage starts small and grows over time, which requires scaling up a Valkey cluster. This scaling operation has been made more robust by atomically moving a slot rather than on a key-by-key basis.

The update also adds hash field expiration, new configuration options for cluster failover, Lua script safety improvements and optimized pipelining to reduce latency in high-concurrency environments. With zero-copy response handling for large payloads, the engine, Valkey claims, achieves up to 20% higher throughput in internal benchmarks.

Security played an essential role in the release. [Version 9.0 resolves multiple vulnerabilities in Lua scripting environments](https://github.com/valkey-io/valkey/releases) that previously enabled potential remote code execution. The [new release](https://github.com/valkey-io/valkey/releases) also tightens module API controls and introduces enhanced client authentication options, including certificate-based login via TLS.

## Performance Optimizations and Enhancements​

Maintainers describe the release as a stability-focused foundation for the next phase of Valkey’s development, with incremental updates planned to refine its module ecosystem and memory efficiency. The project’s maintainers [emphasized](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/) compatibility with existing Redis clients while positioning Valkey as an [independent, performance-optimized datastore](https://thenewstack.io/valkey-is-a-different-kind-of-fork/) for modern internet-scale applications.

In an interview with The New Stack, [Martin Visser](https://www.linkedin.com/in/martinrvisser/), open source database company [Percona](https://www.percona.com/?utm_content=inline+mention)‘s Valkey technical lead, said, “Valkey adoption has really taken off this year. Among our customers, we are seeing continued efforts to increase deployments and run Valkey in production, after successfully switching their dev and test environments. This has extended to hundreds and thousands of instances.”

Visser added, “We are seeing a mix of different deployment approaches too — some companies want to run Valkey in the cloud, while others want to replace Redis clusters within their on-premise deployments. For us, the majority of customers are migrating their on-prem deployments from Redis to Valkey, then adding selective cloud deployments for certain applications.”

## How Valkey 9.0 Compares to Redis

As for a direct Valkey to Redis comparison, in another interview, [Madelyn Olson](https://www.linkedin.com/in/madelyn-olson-valkey), Valkey project maintainer and AWS engineer, said, “Valkey 9 is a release packed with both major and minor features, with commits from over 40 unique contributors. The release includes the single most requested feature — support for hash field expiration — a new resharding algorithm that is faster and more reliable, and significant performance improvements for clients that send commands in batches. This is what you get when you have a diverse set of contributors to a project. When I look at Redis, I see much less diversity in contributions and a different type of innovation.”

Valkey 9.0 is available now on Docker, GitHub and official Linux repositories, with detailed migration notes for operators upgrading from the 8.x branch.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)