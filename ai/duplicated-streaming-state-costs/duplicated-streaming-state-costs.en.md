![Colorful pixel grids dissolving into scattered squares on navy, evoking real-time state data moving between systems](https://cdn.thenewstack.io/media/2026/11/8df20e8c-anna-magenta-vfd7njx03ss-unsplash-1024x683.png)

**Real-time applications often combine** tools with distinct roles. A typical setup might use Kafka to handle events, Flink to process them, Redis to serve the latest state, and a database to maintain the system of record. Applications that use vector search may add a vector store, too.

This division of responsibilities offers flexibility and independent scaling. It also creates costs when data moves between components or when overlapping state is maintained in more than one place.

> “The copies to question are those maintained largely because processing happens in one system and applications read the results from another.”

Some of those copies are necessary. Replicas protect against failures, checkpoints help systems recover, and durable event logs preserve history. They’re worth paying for. The copies to question are those maintained largely because processing happens in one system and applications read the results from another.

Take a velocity counter tracking a payment card’s transactions over the past five minutes. Flink calculates the count and maintains keyed state to support that computation.

But a fraud-scoring service also needs to retrieve the result. Flink’s internal state isn’t designed for general-purpose serving, and Flink deprecated its [Queryable State](https://flink.apache.org/2023/10/24/announcing-the-release-of-apache-flink-1.18/) feature in 1.18. A common solution is to publish the count to Redis.

That gives applications a dedicated serving layer, with its own scaling and operational requirements. Flink’s working state and the Redis value may overlap but not be identical, and each published update involves serialization, network traffic, and processing before consumers see it.

## Where consistency gets complicated

Keeping state synchronized gets more complicated when applications span availability zones.

Consider a hypothetical payment system that serves reads from asynchronous replicas in several availability zones to reduce cross-zone traffic. A refund goes through, but the update is still making its way to one of those replicas.

A service reading from it could see the transaction as not yet refunded and issue another refund, even though the first has already been processed. Without coordination between the refund paths, the customer could be paid twice.

> “Without coordination between the refund paths, the customer could be paid twice.”

This is an application-design concern wherever decisions depend on asynchronously replicated state. Putting processing and storage on the same platform wouldn’t necessarily prevent it.

The immediate issue is replica lag, combined with an application that decides without atomically checking and updating the state that authorizes the refund. If the refund calls an external payment service, that service also needs an idempotent request mechanism so retries cannot issue the same refund twice.

A separate processing-and-serving design also introduces a publication delay: the processor may calculate an updated value before the serving store receives it. That’s export lag, distinct from replica lag within the serving store. During that lag, a burst of fraudulent transactions can be scored against an out-of-date count. Export lag and replica lag can leave applications reading stale data, but neither should be confused with the check-then-act race that could cause the duplicate refund.

Hazelcast can avoid the separate publication step for workloads where computation runs directly against stored state. Its [entry processors](https://docs.hazelcast.com/hazelcast/5.7/data-structures/entry-processor) can atomically update individual map entries on the member holding the relevant key. That doesn’t make the system automatically strongly consistent during network partitions, though.

Applications needing stronger coordination can use appropriately configured data structures in Hazelcast’s Raft-based [CP subsystem](https://docs.hazelcast.com/hazelcast/5.7/cp-subsystem/cp-subsystem). Using it does not turn an ordinary IMap into a strongly consistent map, or make a map update atomic with an external payment. Separate processing and storage systems can also use strongly consistent coordination.

## The cost of moving state

Memory tends to dominate discussions of in-memory architectures, but CPU and networking costs can matter just as much.

A [2025 paper](https://conferences.sigcomm.org/hotnets/2025/papers/hotnets25-final80.pdf) from UC Berkeley and Databricks, *Rethinking the Cost of Distributed Caches for Datacenter Services*, examined caching economics using synthetic workloads, Meta traces, and production data from Databricks’ Unity Catalog.

> “Memory tends to dominate discussions of in-memory architectures, but CPU and networking costs can matter just as much.”

Using the paper’s Google Cloud pricing assumptions of roughly $17 per vCPU-month and $2 per gigabyte-month of memory, the researchers found that adding in-memory caching cut operating costs by a factor of three to four. The CPU savings outweighed the cost of the additional RAM.

That isn’t a comparison of Hazelcast against Flink and Redis; the study compares caching with no caching. Its remote-versus-linked-cache comparison supports the narrower argument that communication and serialization consume CPU.

The paper also found that per-read version checks for stronger consistency could erase much of the cost benefit, so comparisons need equivalent consistency requirements.

A [2019 paper](https://research.google/pubs/fast-key-value-stores-an-idea-whose-time-has-come-and-gone/) by Google researchers, “Fast Key-Value Stores: An Idea Whose Time Has Come and Gone,” reported a 40% reduction in p99.9 latency for ProtoCache, a component of a Google application, after moving from a remote key-value store to an architecture that [keeps application logic and in-memory state together](https://docs.hazelcast.com/hazelcast/5.7/getting-started/get-started-java).

A separate, illustrative calculation shows the memory cost of maintaining two equivalent working sets. At the paper’s assumed memory price, 400 GB would represent about $800 a month in memory alone, before backups, checkpoints, and other infrastructure.

Maintaining an equivalent amount in both processing and serving tiers would double that figure, although Flink’s intermediate state and the results published to Redis can differ substantially.

Then there’s the work involved in keeping the systems synchronized. Each update must be serialized, transmitted, and processed, and both platforms require monitoring, scaling, and maintenance.

One way to get a sense of this overhead is to count the steps involved in a single read-modify-write operation. With separate processing and serving systems, an event might be ingested, keyed state updated, the result serialized and published, then written to the serving store before an application reads it. That’s potentially four or five serialization or network steps for one update. Running the computation where the state is stored can reduce that to a single step. It’s not a precise measure of cost, but tracing the path of an update can help identify where CPU time and network resources are being spent.

A fair total-cost comparison also needs node counts, instance types, licensing, discounts, and equivalent managed-versus-self-managed deployments. The $800 figure is memory arithmetic, not a total-cost estimate or measured Hazelcast saving.

## Bringing computation closer to the data

[Hazelcast provides one way to bring processing closer to stored data](https://docs.hazelcast.com/hazelcast/5.7/getting-started/get-started-java). Rather than sending information back and forth between separate systems, it distributes data across cluster members according to key and can run computations on the member that holds it. It keeps backup copies in case a member fails.

Hazelcast offers two approaches, depending on the kind of processing involved. Hazelcast’s [Jet engine](https://docs.hazelcast.com/hazelcast/5.7/pipelines/overview) can maintain internal state for windowed stream calculations and publish results to a distributed map that applications can read.

That intermediate state and the result-publication step still exist on the same platform; processing, map writes, and backups may also involve traffic between members. Kafka can remain the durable event log in either design, and the database of record can remain in place.

For applications that need to update stored values directly, Hazelcast also has [entry processors](https://docs.hazelcast.com/hazelcast/5.7/data-structures/entry-processor). These run code against the map entry itself, rather than calculating a result elsewhere and then copying it across.

Take the transaction counter discussed earlier. An entry processor could maintain per-minute transaction counts in a distributed map, and the application could sum the most recent five buckets to calculate the total. This avoids the need for a timer to remove expired transactions, though the result would be accurate to the minute rather than the second. The application would still need to account for late or duplicate events.

Keep entry processors lightweight, since a long-running operation can block other work on the same partition. Network traffic still occurs between clients and the cluster, and Hazelcast still maintains backup copies.

Serialization costs also depend on the [map’s in-memory format](https://docs.hazelcast.com/hazelcast/5.7/data-structures/setting-data-format): the default BINARY format stores serialized values, while OBJECT can reduce conversion work for entry processing. The difference is that, for workloads suited to this approach, there’s no separate processing tier that needs to keep publishing updates to the serving store.

## When separate systems make sense

Keeping processing and storage apart has one significant advantage: each can scale independently.

Consider an application running complex decision rules that produce little more than a yes-or-no answer. It might need substantial CPU capacity but very little storage. A separate processing tier allows teams to add compute resources without expanding the serving infrastructure.

Other applications hold large amounts of state but do relatively little processing. Putting both workloads on one cluster may offer limited savings, particularly if CPU-intensive tasks compete with latency-sensitive reads.

Separate platforms also allow independent deployments, workload isolation, and access to specialized processing features. Hazelcast can offer some of that flexibility within a single cluster, too. Its [lite members](https://docs.hazelcast.com/hazelcast/5.7/maintain-cluster/lite-members) handle compute tasks without storing data, allowing teams to dedicate regular members to storage and add compute capacity separately.

For some workloads, keeping processing and storage on entirely separate platforms will still make sense. But when applications frequently read and update the same state, Hazelcast can reduce data movement between systems.

## What to measure before making the switch

The starting point should be a profile of the existing deployment. How much CPU time goes into application logic, and how much is spent serializing data or communicating across the network? How much state is actually duplicated between processing and serving?

Average response times won’t tell the whole story, either. A system might perform well most of the time but slow down considerably on certain requests. That’s why it’s worth checking p99 and p99.9 request latency, along with throughput and end-to-end latency: the time from an event arriving to its result being readable, including any export lag.

Run the comparison with the same workload, the same end-to-end latency target, and the same durability guarantees. Failure testing matters as well: check recovery time, replay behavior, duplicate handling, and correctness during node failures and network partitions. Backup copies and recovery mechanisms add to the infrastructure bill.

For some applications, independently scaling processing and storage will remain the better choice. Others may find they’re paying to move data between systems when they could do the same work directly against application-accessible state.

Not every copy is unnecessary. Replicas protect against failures, checkpoints support recovery, and stream processors need intermediate state. The copies worth questioning are those maintained largely because processing and serving happen in different systems.

The post [Real-time state has a cost your memory bill won’t show](https://thenewstack.io/duplicated-streaming-state-costs/) appeared first on [The New Stack](https://thenewstack.io).