No team wants to take on a [database migration](https://thenewstack.io/lessons-learned-leading-high-stakes-data-migrations/). But many teams are migrating [NoSQL databases](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/) to optimize performance at scale, alleviate maintenance burdens and/or control costs. If a migration is on your team’s radar, how do you make the process as painless as possible, with minimal disruption to both your team and your users?

Here are some battle-tested tips for planning, executing and de-risking a NoSQL database migration.

## First Things First

The good news is that migrating from one database to another — or even to the same database under a new topology — is really not that hard. At its core, a migration is just moving data from a source system to a target system. When teams overcomplicate the process, it’s usually because they lack a clear end-to-end understanding of what’s involved.

Before you actually kick off the migration process, you need to decide what type of migration approach to take. There are two main options: online or offline.

* **An offline migration**: Here, you stop the source system, transfer the data over and then switch your clients to use the new database.
* **An online migration**: Here, there’s no application downtime. That creates increased complexity and requires testing to ensure that you’re not introducing an upstream impact to the apps reading and writing to your database.

No matter which route you decide to take, you’ll need to perform three key steps:

* **Schema migration and changes:** Some level of schema tuning is usually required unless you’re migrating to another version of the same database or across two API-compatible databases.
* **Data migration:** Moving your data from one place to another.
* **Data validation:** Validating your data to ensure that everything is working as expected.

## Let It Flow

This brings us to the actual migration flow, which is shown in the following diagram. The stages of the process are split by the dotted vertical lines.

[![](https://cdn.thenewstack.io/media/2025/08/6db85d25-image1.png)](https://cdn.thenewstack.io/media/2025/08/6db85d25-image1.png)

When you start, the application is writing and reading from the source database. You will start migrating the schema at that point. It’s absolutely essential to get your schema set up correctly on your destination database. If you get it wrong, you’ll need to repeat all the migration steps. Discord engineer Bo Ingram and I talked extensively about data modeling strategies in the recent [NoSQL data modeling for performance masterclass](https://lp.scylladb.com/data-model-performance-masterclass-ondemand-register), which is available on demand.

If you’re running an online migration, you also need to start capturing changes as they occur in your source database. The best approach here depends on which databases you’re migrating from (and to). For example, in DynamoDB, you would enable Dynamo Streams. If you’re migrating from [Cassandra to ScyllaDB](https://thenewstack.io/benchmarking-apache-cassandra-40-nodes-vs-scylladb-4-nodes/), then the application’s dual-writing will work just fine most of the time. Other approaches would involve using Kafka, your database’s change data capture (CDC) and similar tools.

Next, it’s time to actually move the existing data. If you enabled CDC in the previous step, then you should wait for all changes to be replayed before you proceed to the next step.

Once that’s done, your source and target databases should both be in sync. At that point, you’ll want to test the migration results before you update the application to use the new database. This can be accomplished in a variety of ways. For example, you could perform a quick comparison of random individual records. Or, you could do a more extensive check, comparing every individual record before you make a go/no-go decision. The level of validation to perform depends on your team’s requirements and risk tolerance.

Finally, once the system is behaving as expected, you switch client traffic to the new setup. You could move all at once, or do it incrementally using a [canary deployment strategy](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.canary-deployment.en.html) as a safety measure (moving one set of users at a time).

## What To Watch Out For

The migration process outlined above is rather straightforward in theory. But in practice, sometimes it’s complicated. For example, you also need to account for aspects such as:

* **Technology switches:** If you are migrating from one database to a different one, then you will quickly realize that some features you rely on aren’t available on the new database. Or, maybe they’re available, but implemented differently. You will also need to understand the target database’s characteristics to ensure that your data modeling scales as your workload grows. And for every application change and data modeling change you make, you’ll want to dedicate sufficient time for testing.
* **Tooling:** Unless you’re a Spark/Scala expert, it is almost impossible for you to find a single tool that lets you migrate from ANY database to ANY database. Even when such tooling exists, it might need further adjustments to work for you specifically, depending on your workload and requirements. And when there is no tooling, you will pretty much need to cook your own tools and processes from scratch.
* **Edge cases:** Some use cases might depend on specific database features — like custom data types (such as counters) or concurrency control techniques (serializability). These can present additional challenges during migration; they might not be directly supported or might behave differently in the target system. You’ll need to identify these cases early and handle them with special care.

## 

## Only Move What Matters

One final, and often overlooked, consideration: You probably don’t need to migrate everything.

Teams usually assume they need to migrate all their data, but that’s often overkill. Being more selective can save considerable time and effort. It also forces you to take a closer look at your workloads, which often reveals issues, like consistency requirements and user behavior patterns, that might otherwise go unnoticed.

When I ask people, “Can you tolerate some level of data loss?” their gut reaction is almost always a resounding “No!” But let’s say you have an IoT use case and your app generates reports hourly/daily/weekly. Dropping a few data points during migration likely won’t matter — especially if your dashboards aggregate data over longer timeframes.

[![](https://cdn.thenewstack.io/media/2025/08/c8a0c6ea-image3.png)](https://cdn.thenewstack.io/media/2025/08/c8a0c6ea-image3.png)

In many cases, users don’t care about data older than a few weeks. If that’s true for your workloads, don’t bother migrating it all. The same goes for logs and traces: Instead of migrating historical data, you might be able to just snapshot it and start fresh on the new system.

Of course, some use cases (like messaging apps, social platforms or financial systems) really do require zero data loss. Any missing record can directly affect the business. But even then, you might still have some level of flexibility over how you structure the migration. For example, maybe you need to migrate 10 tables, but you are able to map a few tables to specific microservices. In that case, you could split the actual migration work into smaller iterations. And maybe some of these tables make use of time to live (TTL) data, so you could migrate only the parts that matter most to your business.

## Final Thoughts

Take time to consider these migration nuances before you start. A bit of planning should help you surface potential challenges and optimization opportunities early, ultimately saving you a lot of time and grief in the long term. And most importantly: Test your migration plan before you run it in production. Skipping this step can lead to painful (and potentially costly) surprises you’ll definitely want to avoid.

*Want to learn more about NoSQL migrations? Watch this* [*NoSQL Migration Masterclass*](https://lp.scylladb.com/database-migration-masterclass-ondemand-register) *with distributed system expert Jon Haddad on demand.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/09/93cd3bc0-cropped-c57adbb6-felipe-cardeneti-mendes-.png)

Felipe Cardeneti Mendes is an IT specialist with years of experience on distributed systems and open source technologies. He is co-author of three Linux books and is a frequent speaker at public events and conferences to promote open source technologies....

Read more from Felipe Cardeneti Mendes](https://thenewstack.io/author/felipe-cardeneti-mendes/)