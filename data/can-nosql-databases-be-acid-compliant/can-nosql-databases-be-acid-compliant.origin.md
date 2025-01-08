# Can NoSQL Databases Be ACID Compliant?
![Featued image for: Can NoSQL Databases Be ACID Compliant?](https://cdn.thenewstack.io/media/2025/01/f77760ab-content-1024x576.jpg)
The concept of ACID compliance has traditionally been associated with relational databases, leading to misconceptions about its applicability to NoSQL systems. Several reputed sites, such as [AWS](https://aws.amazon.com/?utm_content=inline+mention), assert that[ NoSQL cannot be ACID compliant](https://aws.amazon.com/compare/the-difference-between-acid-and-base-database/). Contrary to these views, ACID (atomicity, consistency, isolation, durability) is not exclusive to relational databases but rather a cornerstone of transaction processing systems.

Let’s explore these misconceptions and why NoSQL databases can — and often do — adhere to ACID compliance.

Early [NoSQL systems](https://thenewstack.io/sql-nosql-and-vectors-oh-my/) prioritized performance and availability, frequently relaxing ACID guarantees, which contributed to the perception that NoSQL is inherently non-ACID compliant.

Another significant source of confusion lies in the interpretation of the “C” (consistency) in ACID. Many mistakenly assume it mandates referential integrity constraints, which NoSQL databases typically do not support. However, ACID’s notion of consistency is broader and does not inherently require referential integrity, allowing NoSQL databases to achieve ACID compliance under the right circumstances.

**The Origins of ACID**
The atomicity, consistency and durability properties were introduced by Jim Gray in his seminal paper on [transactions](https://jimgray.azurewebsites.net/papers/theTransactionConcept.pdf?from=https://research.microsoft.com/~gray/papers/theTransactionConcept.pdf&type=path). While the acronym ACID emerged later, the fundamental concepts originated from Gray’s discussion of transaction processing. Notably, Gray’s definition of consistency does not rely on referential integrity constraints specific to relational databases. Instead, it encompasses a broader notion:

“A transaction is a transformation of state that has the properties of atomicity (all or nothing), durability (effects survive failures) and consistency (a correct transformation).”

Jim Gray and Andreas Reuter later [define consistency](https://archive.org/details/transactionproce0000gray) this way:

“A transaction is a correct transformation of the state. The actions taken as a group do not violate any of the integrity constraints associated with the state. This requires that the transaction be a correct program.”

This highlights that ACID is a framework for ensuring correctness and reliability in transaction processing systems, whether relational or not.

**Transaction Processing Systems: A Broader Context**
Further, Gray and Reuter [define a transaction processing](https://archive.org/details/transactionproce0000gray) system as follows:

“Transaction processing systems (TP systems) manage applications that interact with databases to represent and manipulate real-world states. They often support distributed, [heterogeneous environments with stringent availability and performance requirements](https://thenewstack.io/heterogeneous-processing-requires-data-parallelization-tools-sycl-and-dpc-are-a-good-start/). Historically, TP systems pioneered concepts like fault-tolerant storage, distributed computation and, most notably, the ACID properties.”

Even pre-relational systems, such as [IBM](https://www.ibm.com?utm_content=inline+mention)’s Information Management System (IMS) from the 1970s, supported ACID transactions long before the acronym was coined.

**ACID Properties: A Layered Perspective**
ACID compliance can be understood as a set of guarantees provided by various layers within a database system:

Layer |
Purpose |
Query Layer | Supports
|
These layers illustrate that ACID compliance is a result of coordinated guarantees across the entire database system. In particular, these guarantees are provided by layers below the query language or data model layer, which can add to ACID guarantees by introducing more notions of what integrity constraints this database system has to ensure.

**Consistency: ACID vs. CAP**
A common source of confusion arises from the dual use of the term “consistency” in ACID and CAP (consistency, availability, partition tolerance). In ACID, consistency refers to the correctness of a transaction’s state transformation with respect to user-defined constraints (such as primary keys, referential integrity). [In CAP, consistency](https://aerospike.com/blog/implementing-strong-consistency-in-distributed-database-systems/?utm_source=byline&utm_medium=pr&utm_campaign=The%20New%20Stack) denotes uniform data across replicas in a distributed system.

Note that:

- ACID-compliant distributed databases operating at an isolation level of strict serializability inherently satisfy CAP’s consistency (linearizability) requirement.
- A lack of CAP consistency (linearizability) implies a failure to meet ACID’s atomicity and strict serializability isolation guarantees.
**The BASE vs. ACID Dichotomy**
The BASE (basically available, soft state, eventual consistency) philosophy emerged alongside NoSQL databases to address the scalability needs of web applications. Early NoSQL systems prioritized availability and partition tolerance, often relaxing ACID guarantees. This distinction led to the misconception that NoSQL databases cannot achieve ACID compliance.

However, the evolution of NoSQL systems has blurred these lines. Many modern NoSQL databases now support:

[Strong consistency](https://aerospike.com/glossary/strong-consistency/?utm_source=byline&utm_medium=pr&utm_campaign=The%20New%20Stack)models (C in CAP).- Transactions with serializability guarantees (A, I and D in ACID).
- Enforcement of constraints like primary keys.
**ACID Compliance in NoSQL Systems**
Several NoSQL databases claim ACID compliance, backed by robust technical implementations. Note, however, that not all of these systems may operate at the strict serializability isolation level. For instance:

**DynamoDB:**“DynamoDB supports atomicity, consistency, isolation and durability (ACID) transactions, enabling complex business logic across multiple items within and across tables,” according to[AWS](https://aws.amazon.com/dynamodb/features/).provides multi-document transactions with strict ACID guarantees.[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)**Aerospike**will release support for strict serializable ACID transactions as part of its server release 8.0 in early 2025.**Delta Lake by Databricks**offers ACID-compliant table storage over distributed object stores.
These examples demonstrate that NoSQL databases can and do achieve ACID compliance, making them suitable for mission-critical applications.

**Conclusion**
ACID is not a relic of relational databases but a foundational concept in transaction processing systems. Modern NoSQL databases have evolved to embrace ACID guarantees, challenging the outdated narrative that they are inherently “BASE.” As the database ecosystem continues to innovate, it’s imperative to reframe our understanding of ACID as a property of transactional systems, regardless of the underlying data model.

By dispelling these misconceptions, we can better appreciate the capabilities of NoSQL databases in delivering reliable, consistent and scalable solutions for diverse applications.

*Visit our website to learn more about **Aerospike Database**.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)