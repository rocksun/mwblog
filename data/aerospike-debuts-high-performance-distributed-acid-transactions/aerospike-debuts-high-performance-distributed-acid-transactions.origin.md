# Aerospike Debuts High-Performance Distributed ACID Transactions
![Featued image for: Aerospike Debuts High-Performance Distributed ACID Transactions](https://cdn.thenewstack.io/media/2025/02/8091e800-aerospike-1024x768.png)
The traditional trade-off for distributed databases with high write speeds was availability for consistency. Version 8 of Aerospike’s [performant multimodal database](https://thenewstack.io/from-db2-to-real-time-with-aerospike-founder-srini-srinivasan/), which was unveiled Wednesday, helps dispel this notion by offering real-time distributed ACID transactional support at scale.

[Already known](https://thenewstack.io/how-to-manage-45-billion-client-records-with-aerospike/) for its high-performance online transactional processing (OLTP), [Aerospike](https://aerospike.com?utm_content=inline+mention)’s engine has been updated with key features that are ideal for ensuring consistency without sacrificing speed. In addition to providing distributed ACID transactions, version 8 guarantees strict serializability of those transactions.
There are also intuitive transaction APIs that allow for multiple operations within a transaction while simplifying the developer experience.

## Supporting Consistency
According to [Aerospike](https://aerospike.com/) CTO [Srini Srinivasan](https://www.linkedin.com/in/drvsrini), the objective of the release is to “move, collectively, the field forward for having higher-performance databases which also support consistency. And, we try to minimize that compromise of performance and availability while you’re adding strong consistency.”

Aerospike’s ACID properties ensure transactions don’t interfere with each other while producing well-understood results. This point is critical to organizations in regulated spaces like finance, which process what Srinivasan estimated is up to hundreds of millions of transactions — each of which possibly contains multiple records — each second.

Such organizations are “using us for high performance, but they need to denormalize the data and put it in a single record,” Srinivasan said. “And, if they have a necessity to link multiple records together, while still keeping them separate for regulatory reasons, that requires you to implement proper transactions, which is what Aerospike 8 does.”

Most importantly, the updated engine shifts the onus of maintaining consistency from the application level to the database level, liberating developers from such vital concerns.

## Consistency and Performance
Prior to unveiling Aerospike Database 8, Aerospike provided transactional consistency for single-record operations. The distributed ACID characteristics of the new version supply consistency for more sophisticated transactions. “When you add the multirecord ACID distributed transaction support, you can change multiple records within the same transaction,” Srinivasan explained. Moreover, developers can realize the atomicity, consistency, isolation and durability ([ACID](https://thenewstack.io/can-nosql-databases-be-acid-compliant/)) benefits for respective transactions across distributed systems spanning clouds, data centers and geographic locations.

Atomicity ensures transactions either do or don’t happen. Isolation means other transactions don’t access the records a transaction is currently accessing. Durability means the system won’t lose the data. Most importantly, these boons are provided for high-performance applications. Aerospike’s “algorithms to provide consistency are crafted to provide higher availability than many other algorithms,” Srinivasan said. “That’s actually unique.”

## Strict Serializability
The [strict serializability](https://stackoverflow.com/questions/60365103/differences-between-strict-serializable-and-external-consistency) of Aerospike Database 8’s distributed ACID transactions is also a key feature for developers. This property, which Srinivasan said guarantees the order of transactions are executed in the database in the order in which they occur, means addressing these issues isn’t part of the app-building process. If an organization is transferring funds from one bank account to another and withdrawing money from the latter in a series of operations, with strict serializability, “If a transaction finishes before another one starts, that is exactly how the database will execute it,” Srinivasan said.

Strict serializability means each new transaction accessing the database is updated with changes to the database made by previous transactions. Additionally, Aerospike’s strict serializability for multirecord transactions doesn’t compromise the performance of the single-record transaction support the database previously had. In fact, it achieves the former without “slowing down the single records,” Srinivasan commented.

## Exonerating Applications and Developers
Aerospike Database 8’s new features transfer the burden of ensuring consistency from the applications relying on the database to the database itself. This development is meaningful for two reasons. Firstly, it results in more dependable applications, reliable uptime and better performance. According to Srinivasan, many algorithms designed to provide consistency in Aerospike can be implemented at the application level. “What that would mean is the applications would have to keep track of the state of every transaction they’re executing outside the database,” Srinivasan revealed. “And then, if the application server dies, then you lose state. So, it’s very, very hard to avoid data loss.”

Secondly, it’s difficult to identify bugs in distributed systems, which could create problems with the order in which transactions are executed. In addition to furnishing the aforementioned guarantees for consistency and the proper order of transactions, Aerospike supplies other tools to maintain consistency at the database level.

According to Srinivasan, resources such as [Jepsen’s testing capabilities](https://jepsen.io/) enable “a third-party application developer to check, ‘Hey, this database, does it work? Is it a proof for the algorithm?’ It makes it easy for application programmers. They don’t have to do all the hard work. They just write the apps and they can depend on these guarantees, and they can get verification that these are indeed being met.”

## Transaction API Savviness
Aerospike Database 8 also contains a transaction API that’s useful for enabling complex transactions for OLTP systems. With the API, once a transaction begins, it’s possible to do a number of operations in it before the transaction end phase is reached. “At that point, you’re not guaranteed that the transaction will commit, because until that time somebody else might have interfered,” Srinivasan said. “But, that’s all done at the end-transaction phase. You basically put an envelope around all kinds of operations you’re doing on the database. That’s the API.”

Aerospike Database 8 also supports [Spring](https://spring.io/) to improve the developer experience of using this framework with the database. According to Srinivasan, “Application developers can just program in Spring, and then, underneath the covers, we provide a library which translates the Spring API’s application call into underlying API calls at the database level. The Spring developer doesn’t need to know the APIs of the Aerospike database.”

## Moving the Field Forward
Many NoSQL databases started out prioritizing availability over consistency before gradually adding properties for the latter. Aerospike’s distinction is that it is a distributed, high-performance multimodal database (with support for vectors, key-value, graph formats and document formats) that enables consistency for sophisticated, multirecord transactions.

With its consistency guarantees, it allows developers to concentrate on building the best logic for their applications without compromising their productivity, or progress, by worrying about concerns that are now handled at the database level.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)