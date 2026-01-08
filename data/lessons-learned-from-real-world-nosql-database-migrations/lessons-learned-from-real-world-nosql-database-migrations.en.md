In “[Battle-Tested Tips for a Better NoSQL Migration](https://thenewstack.io/what-matters-most-for-nosql-migrations/),” I shared my top strategies for planning, executing and de-risking a NoSQL database migration. I discussed key steps like schema and data migration, data validation and important considerations such as technology switches, tooling, edge cases and the idea that you might not need to migrate all your data.

Now, let’s analyze how teams actually migrated their data — what challenges they faced, trade-offs, how they proceeded and lessons learned. These are all real-world examples with names and identifying details obfuscated.

## Streaming Bulk Load (DynamoDB to ScyllaDB)

First example: A large media streaming company that decided to switch from DynamoDB to ScyllaDB to reduce costs.

One interesting aspect of this use case is that the team had an ingestion process that overwrote their entire data set daily. As a result, there was no requirement to forklift their data from one database to another. They could just configure their ingestion job to write to ScyllaDB in addition to DynamoDB.

[![](https://cdn.thenewstack.io/media/2026/01/b4c4b250-image1.png)](https://cdn.thenewstack.io/media/2026/01/b4c4b250-image1.png)

As soon as the job kicked in, data was stored in both databases. Since DynamoDB and ScyllaDB data models are so similar, that greatly simplified the process. It’s more complex when switching from a document store or a relational database to wide-column NoSQL.

As I mentioned in the previous article, a migration from one technology to another almost always requires making some changes. Even with similar databases, features and inner workings vary. Some of this team’s migration concerns were related to the way ScyllaDB handled out-of-order writes, how they would implement record versioning and the efficiency of data compression. These were all valid and interesting concerns.

The main lesson from this migration is the need to understand the differences between your source database and target databases. Even databases that are quite similar in many respects, such as ScyllaDB and DynamoDB, do have differences that you need to recognize and navigate. As you explore these differences, you may eventually stumble upon room for improvement, which is exactly what happened here.

The use case in question was very susceptible to out-of-order writes. Before we explain how they addressed it, let’s cover what an out-of-order write involves.

### Understanding Out-of-Order Writes

Out-of-order writes occur when newer updates arrive before older ones.

For example, assume you’re running a dual-write setup, writing to both your source and target databases at the same time. Then you plug in a migration tool (such as the [ScyllaDB Migrator](https://migrator.docs.scylladb.com/stable/)) to start reading data from the source database and writing it to the destination one. The Spark job reads some data from the source database, then the client writes an update to that same data. The client writes the data to the target database first and the Spark job writes it after. The Spark job might overwrite the fresher data. That’s an out-of-order write.

[![](https://cdn.thenewstack.io/media/2026/01/8bb1d5a4-image2a.png)](https://cdn.thenewstack.io/media/2026/01/8bb1d5a4-image2a.png)

[Martin Fowler](https://martinfowler.com/eaaDev/RetroactiveEvent.html) describes it this way: “An out-of-order event is one that’s received late, sufficiently late that you’ve already processed events that should have been processed after the out-of-order event was received.”

With both [Cassand](https://thenewstack.io/benchmarking-apache-cassandra-40-nodes-vs-scylladb-4-nodes/)ra and ScyllaDB, you can handle these out-of-order writes by using the CQL (Cassandra Query Language) protocol to explicitly set timestamps on writes. In our example, the client update would include a later timestamp than the Spark write, so it would “win” — no matter which arrives last.

This capability doesn’t exist in DynamoDB.

### How the Team Handled Out-of-Order Writes in DynamoDB

The team was handling out-of-order writes using DynamoDB’s Condition Expressions, which are very similar to lightweight transactions in Cassandra. However, Condition Expressions in DynamoDB are much more expensive (with respect to [performance as well as cost](https://thenewstack.io/mongodb-vs-scylladb-performance-scalability-and-cost/)) than regular non-conditional expressions.

How did this team try to circumvent the out-of-order write using ScyllaDB? Initially, they implemented a read-before-write prior to every write. This effectively caused their number of reads to spike.

After we met with them and analyzed their situation, we improved their application and database performance considerably by simply manipulating the timestamp of their writes. That’s the same approach that another customer of ours, [Zillow, uses to handle out-of-order events](https://www.scylladb.com/users/case-study-zillow-scales-background-and-real-time-workloads-with-scylla/).

## Engagement Platform: TTL’d Data (ScyllaDB Self-Managed to ScyllaDB Cloud)

Next, let’s look at a migration across different flavors of the same database: a ScyllaDB to ScyllaDB migration. An engagement platform company decided to migrate from a self-managed on-premises ScyllaDB deployment to the ScyllaDB Cloud managed solution, so we helped them move data over.

No data modeling changes were needed, greatly simplifying the process. Though we initially suggested carrying out an online migration, they chose to take the offline route instead.

[![](https://cdn.thenewstack.io/media/2026/01/6e9341e0-image3a.png)](https://cdn.thenewstack.io/media/2026/01/6e9341e0-image3a.png)

### Why an Offline Migration?

An offline migration has some clear drawbacks: There’s a data loss window equal to the time the migration takes and the process is rather manual. You have to snapshot each node, copy the snapshots somewhere and then load them into the target system. And if you choose not to dual-write, switching clients is a one-way move; going back would mean losing data.

We discussed those risks upfront, but the team decided that these risks wouldn’t outweigh the benefits and simplicity of doing it offline. (They expected most of their data to be expired with TTL (Time to Live) eventually).

Before the production migration, we tested each step to better understand the potential data loss window.

In most cases, it is also possible to completely shift from data loss to a temporary inconsistency when carrying out an offline migration. After you switch your writers, you simply repeat the migration steps again from the source database (now a read-only system), therefore restoring any data that wasn’t captured as part of the initial snapshot.

### A Typical TTL-Based Migration Flow

This team used TTL data to control their data expiration, so let’s discuss how a migration with TTL data typically works.

First, you configure the application clients to do dual-writing but keep the client reading only from the existing source of truth. Eventually, the TTL on that source of truth expires. At this point, you can switch the reads to the new target database and all data should be in sync.

[![](https://cdn.thenewstack.io/media/2026/01/bbe70652-image4.png)](https://cdn.thenewstack.io/media/2026/01/bbe70652-image4.png)

### How the Migration Actually Played Out

In this case, the client was only reading and writing against a single existing source of truth. With the application still running, the team took an online snapshot of their data across all nodes. The resulting snapshots were transferred to the target cluster and we loaded the data using Load and Stream (a ScyllaDB extension that builds on the Cassandra `nodetool refresh` command).

[![](https://cdn.thenewstack.io/media/2026/01/b2c8a07b-image5a.png)](https://cdn.thenewstack.io/media/2026/01/b2c8a07b-image5a.png)

Rather than simply loading the data for the node and discarding the tokens, which the node is not a replica for, Load and Stream actually streams the data to other cluster members. This greatly simplifies the overall migration process. Instead of just loading the data and dropping the tokens that aren’t needed, Load and Stream actually streams the data to other nodes in the cluster.

After the team’s Load and Stream completed, the client simply switched reads and writes over to the new source of truth.

# Messaging App: Shadow Cluster (Cassandra to ScyllaDB)

Next, let’s explore how a messaging app company approached the challenge of migrating more than a trillion rows from Cassandra to ScyllaDB.

Since Cassandra and ScyllaDB are API compatible, such migrations shouldn’t require any schema or application changes. However, given the criticality of their data and consistency requirements, an online migration approach was the only feasible option. They needed zero user impact and had zero tolerance for data loss.

### Using a Shadow Cluster for Online Migration

The team opted to create a “shadow cluster.” A shadow cluster is a mirror of a production cluster that has the same data (mostly) and receives the same reads and writes. They created it from the disk snapshots from nodes in the corresponding production cluster. Production traffic (both reads and writes) was mirrored to the shadow cluster via a data service that they created for this specific purpose.

[![](https://cdn.thenewstack.io/media/2026/01/c2439988-image6.png)](https://cdn.thenewstack.io/media/2026/01/c2439988-image6.png)

With a shadow cluster, they could assess the performance impact of the new platform before they actually switched. It also allowed them to thoroughly test other aspects of the migration, such as longer-term stability and reliability.

The drawbacks? It’s fairly expensive, since it typically doubles your infrastructure costs while you’re running the shadow cluster. Having a shadow cluster also adds complexity to things like observability, instrumentation, potential code changes and so on.

### Negotiating Throughput and Latency Trade-offs During Migration

One notable [lesson learned from this migration](https://thenewstack.io/lessons-learned-leading-high-stakes-data-migrations/): how important it is to ensure the source system stability during the actual data migration. Most teams just want to migrate their data as fast as possible. However, migrating as fast as possible could affect latencies, and that could be a problem when low latencies are critical to the end users’ satisfaction.

In this team’s case, the solution was to migrate the data as fast as possible, but only up to the point where it started to affect latencies on the source system.

And how many operations per second should you run to migrate? At which level of concurrency? There’s no easy answer here. Really, you have to test.

## Wrapping Up

The “best” NoSQL migration approach? As the breadth and diversity of these examples show, the answer is quite simple: it depends. A daily batch ingestion let one team skip the usual migration steps entirely. Another had to navigate TTLs and snapshot timing. And yet another team was really focused on making sure migration didn’t compromise their strict latency requirements. What worked for one team wouldn’t have worked for the next — and your specific requirements will shape your own migration path as well.

I hope these examples provided an interesting peek into the types of trade-offs and technical considerations you’ll face in your own migration. If you’re curious to learn more, I encourage you to browse the library of ScyllaDB user migration stories. For example:

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/09/93cd3bc0-cropped-c57adbb6-felipe-cardeneti-mendes-.png)

Felipe Cardeneti Mendes is an IT specialist with years of experience on distributed systems and open source technologies. He is co-author of three Linux books and is a frequent speaker at public events and conferences to promote open source technologies....

Read more from Felipe Cardeneti Mendes](https://thenewstack.io/author/felipe-cardeneti-mendes/)