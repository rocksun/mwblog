For decades, distributed [databases](https://thenewstack.io/databases/) have been built around the assumption that [storage](https://thenewstack.io/storage/) will live close to compute.

The farther [data](https://thenewstack.io/data/) travels over the network, the reasoning goes, the greater the potential for delay. Local RAID (redundant array of independent disks) arrays, network-attached storage (NAS), and cluster file systems keep data close, making it quick and easy to access.

But in a distributed system, keeping the entire data store close to compute makes scaling slow, cumbersome, and expensive. Each time a node or cluster is replicated, its associated data must be replicated as well.

It isn’t ideal, but until recently, there wasn’t any reasonable alternative. Databases had to scale. Service-level agreements (SLAs) had to be met. Wide-area networks weren’t reliable enough to support high-performance databases at scale. Database designers accordingly spent a great deal of energy solving problems related to coordination, consistency, and replication logic.

But imagine things were different. What if they didn’t have to worry about the network, where their data lived, or how to get it from Point A to Point B? How would they design a database then?

That’s the intriguing question raised by the advent of cloud object storage services like [AWS S3](https://thenewstack.io/werner-vogels-6-lessons-for-keeping-systems-simple/), [Google Cloud Storage](https://thenewstack.io/storage/cloud-storage-services-for-cloud-native-applications/), and Microsoft Blob Storage.

## What is cloud object storage?

The structure of cloud object storage services couldn’t be simpler. They’re essentially giant heaps of data, accessed via an API, through key/value pairings.

Their unlimited storage capacity and their “everywhere” availability make them revolutionary. They can hold billions of records — images, logs, training data, whatever you need — and crucially, they can make every one of those records available to compute anywhere in the world, at any level of workload.

S3 is extremely reliable. It’s designed for 11 nines of durability (that’s 99.999999999%) and 99.99% availability, and it replicates data automatically across Amazon’s regional facilities. This means data on S3 is extremely safe and highly available without the need to manage physical disks or replication.

In addition, S3 scales seamlessly. There are no fixed volumes. No need for capacity planning. The amount of data you can store is practically unlimited, and performance scales with parallel access rather than being limited by a single-server bottleneck. These guarantees free architects from worrying about low-level storage failures, capacity, and edge cases involving consistency.

> What services like S3 lack in sheer speed, they more than make up for in reliability and ease of maintenance.

In short, cloud object storage provides a highly durable, always-on, strongly-consistent single source of truth. It’s not as fast as local storage, but it doesn’t have to be. What services like S3 lack in sheer speed, they more than make up for in reliability and ease of maintenance. Instead of worrying about shards, segmentation, and software-defined networks, a database can simply retrieve data with confidence that it will be delivered in a reasonable amount of time.

What this means is that for the next generation of distributed databases, cloud object storage will, for all intents and purposes, be the network.

## Architectural patterns emerging around object storage

Building on cloud object storage enables several architectural patterns that were previously impractical.

* **Ephemeral compute clusters:** Keeping object storage separate from compute makes it easier to spin up clusters temporarily for a specific job and tear them down afterward. This is especially useful for AI agents, which often construct temporary databases to accomplish tasks. Compute can be spun up at will without the overhead of data replication.
* **Event-driven workflows:** The arrival of a new object in S3 can trigger a Lambda function, start a training job, or notify downstream consumers. This sort of workflow would be impractical in a system with highly replicated data, but it’s trivial when data is centralized in a single store.
* **AI and ML pipelines:** Many distributed machine learning workflows benefit from a centralized object storage data store. Training datasets, feature stores, model checkpoints, and experiment logs all commonly live in object stores. Frameworks like TensorFlow, PyTorch, and SageMaker are designed to stream data directly from object storage.
* **Tiering storage at large scale:** Databases often classify data as either in-demand (“hot”) or rarely accessed (“cold”). Hot data is stored on high-speed flash storage, while cold data is stored on a more cost-efficient spinning disk. Provisioning hot and cold storage normally requires manual intervention and careful capacity planning. But with cloud object storage, the database can automatically handle tiering, shuffling data between the object store and the high-speed cache based on demand. The availability and infinite capacity of the object store make planning unnecessary.

## Example: TiDB X

Now let’s see how these capabilities translate into a real-world design. [**PingCAP**](https://www.pingcap.com/) uses cloud object storage as the foundation for [**TiDB X**](https://www.pingcap.com/blog/introducing-tidb-x-a-new-foundation-distributed-sql-ai-era/), the latest version of our popular [open source](https://thenewstack.io/open-source/) distributed SQL database, TiDB.

![A chart showing TiDB X’s architecture with built-in object storage.](https://cdn.thenewstack.io/media/2026/01/0e642228-screenshot-2026-01-30-at-19.24.06-1024x584.png)

TiDB X’s architecture with built-in object storage.

As shown in the diagram above, TiDB X fully separates compute and storage, using S3 for the shared backend. Compute nodes scale independently up and down. Fast local caches and Raft ensure consistency and low-latency access for hot data. Instead of keeping the entire data store close by, TiDB X keeps only the most active data near compute. TiDB X monitors query patterns, latency targets, and data characteristics, then reshapes itself in response to demand.

Its object storage-based architecture streamlines recovery and backup processes. By using S3 for primary data persistence, TiDB X reduces the overhead of traditional backup maintenance, enabling significantly faster completion times. This design also mitigates the impact of node failures: since local state functions primarily serve as a cache for durable, replicated storage, a failed instance can be replaced by retrieving its required state directly from object storage to resume operations.

From an operational perspective, cloud object storage makes [TiDB X both highly adaptable and extremely cost-efficient](https://www.pingcap.com/blog/introducing-tidb-x-a-new-foundation-distributed-sql-ai-era/#:~:text=Smarter%20economics%3A%20Usage%2Dbased%20pricing%20and%20RU/s%20enforcement%20so%20your%20database%20costs%20stay%20predictable%20and%20aligned%20with%20real%20demand.). Its autoscaler responds not just to preset infrastructure thresholds, but to contextual signals like query patterns, latency targets, and data types. This enables it to reshape its resources in real time to address different tasks.

In sum, by building atop AWS’s high-performance object data store, TiDB X demonstrates how a cloud database can achieve elasticity, performance, and simplicity without sacrificing consistency or scale.

## S3 as the communication fabric

Keeping large relational data stores close to compute resources has always been a compromise. It was an expensive solution to a problem created by the limitations of traditional networking.

With architectures like TiDB, we see that the sheer power and scale of services like S3 have made the old workarounds unnecessary. They’ve rendered traditional architectures increasingly obsolete. More than that, they’ve enabled practices, such as ephemeral compute, suited to a world where users are more likely to be AI agents than humans.

As AI reshapes business organizations and best practices, the database itself is changing form. In large part, it’s services like S3 that are making that shift possible. By making data placeless, ubiquitous, and effortlessly accessible, cloud object storage is overturning the assumptions that once guided database design. The result will be databases that are more flexible and resilient  — ones that are simpler to manage and scale almost effortlessly.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/6a7f3a53-cropped-bc64a625-max-liu.png)

Max Liu is the co-founder and CEO of TiDB, powered by PingCAP. He has more than 10 years of experience in system infrastructure and software technologies. He is the co-author of the following open source projects: TiDB, TiKV and Codis,...](https://thenewstack.io/author/max-liu/)