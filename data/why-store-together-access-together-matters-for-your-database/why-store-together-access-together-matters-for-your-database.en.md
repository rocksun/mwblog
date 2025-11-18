When your application needs several pieces of data at once, the fastest approach is to read them from a single location in a single call. In a [document database](https://thenewstack.io/empower-modern-app-developers-with-document-databases/), developers can decide what is stored together, both logically and physically.

Fragmentation has never been beneficial for performance. In [databases](https://thenewstack.io/introduction-to-databases/), the proximity of data — on disk, in memory or across the network — is crucial for scalability. Keeping related data together allows a single operation to fetch everything needed, reducing disk I/O, memory cache misses and network round-trips, thereby making performance more predictable.

The principle “store together what is accessed together” is central to modeling in document databases. Yet its purpose is to allow developers to control the physical storage layout, even with flexible data structures.

> Understanding the core principle of data locality is essential today, especially as many databases emulate document databases or offer similar syntax on top of SQL.

In contrast, SQL databases were designed for data independence — allowing users to interact with a logical model separate from the physical implementation managed by a database administrator.

Today, the trend is not to separate development and operations, allowing faster development cycles without the complexity of coordinating multiple teams or shared schemas. Avoiding the separation into logical and physical models further simplifies the process.

Understanding the core principle of data locality is essential today, especially as many databases emulate document databases or offer similar syntax on top of SQL. To qualify as a document database, it’s not enough to accept JSON documents with a developer-friendly syntax.

The database must also preserve those documents intact in storage so that accessing them has predictable performance. Whether they expose a relational or document API, it is essential to know if your objective is data independence or data locality.

## Why Locality Still Matters in Modern Infrastructure

Modern hardware still suffers from penalties for scattered access. Hard disk drives (HDDs) highlighted the importance of locality because seek and rotational latency are more impactful than transfer speed, especially for online transactional processing (OTLP) workloads.

While solid state drives (SSDs) remove mechanical delays, random writes remain expensive, and cloud storage adds latency due to network access to storage. Even in-memory access isn’t immune: on multisocket servers, non-uniform memory access (NUMA) causes varying access times depending on where the data was loaded into memory by the first access, relative to the CPU core that processes it later.

Scale-out architecture further increases complexity. Vertical scaling — keeping all reads and writes on a single instance with shared disks and memory — has capacity limits. Large instances are expensive, and scaling them down or up often requires downtime, which is risky for always-on applications.

> More nodes increase the likelihood of distributed queries, in which operations that once hit local memory must now traverse the network, introducing unpredictable latency. Data locality becomes critical with scale-out databases.

For example, you might need your maximum instance size for Black Friday but would have to scale up progressively in the lead-up, incurring downtime as usage increases. Without horizontal scalability, you end up provisioning well above your average load “just in case,” as in on-premises infrastructures sized years in advance for occasional peaks — something that can be prohibitively costly in the cloud.

Horizontal scaling allows adding or removing nodes without downtime. However, more nodes increase the likelihood of distributed queries, in which operations that once hit local memory must now traverse the network, introducing unpredictable latency. Data locality becomes critical with scale-out databases.

To create scalable database applications, developers should understand storage organization and prioritize single-document operations for performance-critical transactions. CRUD functions (insert, find, update, delete) targeting a single document in MongoDB are always handled by a single node, even in a sharded deployment. If that document isn’t in memory, it can be read from disk in a single I/O operation. Modifications are applied to the in-memory copy and written back as a single document during asynchronous checkpoints, avoiding on-disk fragmentation.

In MongoDB, the WiredTiger storage engine stores each document’s fields together in contiguous storage blocks, allowing developers to follow the principle “store together what is accessed together.” By avoiding cross-document joins, such as the `$lookup` operation in queries, this design helps prevent scatter-gather operations internally, which promotes consistent performance. This supports predictable performance regardless of document size, update frequency or cluster scale.

## The Relational Promise: Physical Data Independence

For developers working with [NoSQL databases](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/), what I exposed above seems obvious: There is one single data model — the domain model — defined in the application, and the database stores exactly that model.

The MongoDB data modeling workshop defines a database schema as the physical model that describes how the data is organized in the database. In relational databases, the logical model is typically independent of the physical storage model, regardless of the data type used, because they serve different purposes.

SQL developers work with a relational model that is mapped to their object model via object relational mapping (ORM) tooling or hand-coded SQL joins. The models and schemas are normalized for generality, not necessarily optimized for specific application access patterns.

The goal of the relational model was to serve online interactive use by non-programmers and casual users by providing an abstraction that hides physical concerns. This includes avoiding data anomalies through normalization and enabling declarative query access without procedural code. Physical optimizations, like indexes, are considered implementation details. You will not find `CREATE INDEX` in the SQL standard.

In practice, a SQL query planner chooses access paths based on statistics. When writing `JOIN` clauses, the order of tables in the `FROM` clause should not matter. The SQL query planner reorders based on cost estimates. The database guarantees logical consistency, at least in theory, even with concurrent users and internal replication. The SQL approach is database-centric: rules, constraints and transactional guarantees are defined in the relational database, independent of specific use cases or table sizes.

Today, most relational databases sit behind applications. End users rarely interact with them directly, except in analytical or data science contexts. Applications can enforce data integrity and handle code anomalies, and developers understand data structures and algorithms. Nonetheless, relational database experts still advise keeping constraints, stored procedures, transactions, and joins within the database.

The physical storage remains abstracted — indexes, clustering, and partitions are administrator-level, not application-level, concepts, as if the application developers were like the non-programmer casual users described in the early papers about relational databases.

## Codd’s Rules Still Apply to SQL/JSON Documents

Because data locality matters, some relational databases have mechanisms to enforce it internally. For example, Oracle has long supported “clustered tables” for co-locating related rows from multiple columns, and more recently offers a choice for JSON storage as either binary JSON (OSON, Oracle’s native binary JSON) or decomposed relational rows (JSON-relational duality views). However, those physical attributes are declared and deployed in the database using a specific data definition language (DDL) and are not exposed to the application developers. This reflects [Codd’s “independence” rules](https://www.geeksforgeeks.org/dbms/codds-rules-in-dbms/):

* **Rule 8**: Physical data independence
* **Rule 9**: Logical data independence
* **Rule 10**: Integrity independence
* **Rule 11**: Distribution independence

Rules 8 and 11 relate directly to data locality: The user is not supposed to care whether data is physically together or distributed. The database is opened to users who ignore the physical data model, access paths and algorithms. Developers do not know what is replicated, sharded or distributed across multiple data centers.

## Where the SQL Abstraction Begins to Weaken

In practice, no relational database perfectly achieves these rules. Performance tuning often requires looking at execution plans and physical data layouts. Serializable isolation is rarely used due to scalability limitations of two-phase locking, leading developers to fall back to weaker isolation levels or to explicit locking (`SELECT ... FOR UPDATE`). Physical co-location mechanisms — hash clusters, attribute clustering — exist, but are difficult to size and maintain optimally without precise knowledge of access patterns. They often require regular data reorganization as updates can fragment it again.

The normalized model is inherently application-agnostic, so optimizing for locality often means breaking data independence ( denormalizing, maintaining materialized views, accepting stale reads from replicas, disabling referential integrity). With sharding, constraints like foreign keys and unique indexes generally cannot be enforced across shards. Transactions must be carefully ordered to avoid long waits and deadlocks. Even with an abstraction layer, applications must be aware of the physical distribution for some operations.

## The NoSQL Pivot: Model for Access Patterns

As data volumes and latency expectations grow, a different paradigm has emerged: give developers complete control rather than an abstraction with some exceptions.

NoSQL databases adopt an application-first approach: The physical model matches the access patterns, and the responsibility for maintaining integrity and transactional scope is pushed to the application. Initially, many NoSQL stores delegated all responsibility, including consistency, to developers, acting as “dumb” key-value or document stores. Most lacked ACID (atomicity, consistency, isolation and durability) transactions or query planners. If secondary indexes were present, they needed to be queried explicitly.

This NoSQL approach was the opposite of the relational database world: Instead of one shared, normalized database, there were many purpose-built data stores per application. It reduces the performance and scalability surprises, but at the price of more complexity.

## MongoDB’s Middle Road for Flexible Schemas

MongoDB evolved by adding essential relational database capabilities — indexes, query planning, multidocument ACID transactions — while keeping the application-first document model. When you insert a document, it is stored as a single unit.

In WiredTiger, the MongoDB storage engine, BSON documents (binary JSON with additional datatypes and indexing capabilities) are stored in B-trees with variable-sized leaf pages, allowing large documents to remain contiguous, which differs from the fixed-size page structures used by many relational databases. This avoids splitting a business object across multiple blocks and ensures consistent latency for operations that appear as a single operation to developers.

> Locality defined at the application’s document schema flows all the way down to the storage layer, something that relational database engines typically cannot match.

Updates in MongoDB are applied in memory. Committing them as in-place changes on disk would fragment pages. Instead, WiredTiger uses reconciliation to write a complete new version at checkpoints — similar to copy-on-write filesystems, but with a flexible block size. This may cause write amplification, but preserves document locality. With appropriately sized instances, these writes occur in the background and do not affect in-memory write latency.

Locality defined at the application’s document schema flows all the way down to the storage layer, something that relational database engines typically cannot match with their goal of physical data independence.

## Why Does Locality Change the Application Performance?

Designing for locality simplifies development and operations in several ways:

* **Transactions**: A business change affecting a single aggregate (in the domain-driven design sense) becomes a single atomic read–modify–write on one document — no multiple roundtrips like `BEGIN`, `SELECT ... FOR UPDATE`, multiple updates and `COMMIT`.
* **Queries and indexing**: Related data in one document avoids SQL joins and ORM lazy/eager mapping. A single compound index can cover filters and projections across fields that would otherwise be in separate tables, ensuring predictable plans without join-order uncertainty.
* **Development**: The same domain model in the application is used directly as the database schema. Developers can reason about access patterns without mapping to a separate model, making latency and plan stability predictable.
* **Scalability**: Most operations targeting a single aggregate, with shard keys chosen accordingly, can be routed to one node, avoiding scatter–gather fan-out for critical use cases.
* MongoDB’s optimistic concurrency control avoids locks, though it requires retry logic on write conflict errors. For single-document calls, retries are handled transparently by the databases, which have a complete view of the transaction intent, making it simpler and faster.

## Embedding Versus Referencing in Document Data Modeling

Locality doesn’t mean “embed everything.” It means: Embed what you consistently access together. Bounded one-to-many relationships (such as an order and its line items) are candidates for embedding. Rarely updated references and dimensions can also be duplicated and embedded. High-cardinality or unbounded-growth relationships, or independently updated entities, are better represented as separate documents and can be co-located via shard keys.

MongoDB’s compound and multikey indexes support embedded fields, maintaining predictable, selective access without joins. Embedding within the same document is the only way to guarantee co-location at the block level. Multiple documents in a single collection are not stored close together, except for small documents inserted at the same time, as they might share the same block. In sharding, the shard key ensures co-location on the same node but not within the same block.

In MongoDB, locality is an explicit design choice in domain-driven design:

* Identify aggregates that change and are read together.
* Store them in one document when appropriate.
* Use indexes aligned with access paths.
* Choose shard keys so related operations route to one node.

## What MongoDB Emulations Miss About Locality

Given the popularity of the document model, some cloud services offer MongoDB-like APIs on top of SQL databases. These systems may expose a MongoDB-like API while retaining a relational storage model, which typically does not maintain the same level of physical locality.

Relational databases store rows in fixed-size blocks (often 8 KB). Large documents must be split across multiple blocks. Here are some examples in popular SQL databases:

* **PostgreSQL JSONB**: Stores JSON in heap tables and large documents in many chunks, using [TOAST, the oversized attribute storage technique](https://www.postgresql.org/docs/8.2/storage-toast.html). The document is compressed and split into chunks stored in another table, accessed via an index. Reading a large document is like a nested loop join between the row and its TOAST table.
* **[Oracle](https://www.oracle.com/developer?utm_content=inline+mention) JSON-Relational Duality Views**: Map JSON documents to relational tables, preserving data independence rather than physical locality. Elements accessed together may be scattered across blocks, requiring internal joins, multiple I/Os and possibly network calls in distributed setups.

In both scenarios, the documents are divided into either binary chunks or normalized tables. Although the API resembles MongoDB, it remains a SQL database that lacks data locality. Instead, it provides an abstraction that keeps the developer unaware of internal processes until they inspect the execution plan and understand the database internals.

## Conclusion

“Store together what is accessed together” reflects realities across sharding, I/O patterns, transactions, and memory cache efficiency. Relational database engines abstract away physical layout, which works well for centralized, normalized databases serving multiple applications in a single monolithic server. At a larger scale, especially in elastic cloud environments, horizontal sharding is essential — and often incompatible with pure data independence. Developers must account for locality.

In SQL databases, this means denormalizing, duplicating reference data, and avoiding cross-shard constraints. The document model, when the database truly enforces locality down to storage offers an alternative to this abstraction and exceptions.

In MongoDB, locality can be explicitly defined at the application level while still providing indexing, query planning and transactional features. When assessing “MongoDB-compatible”systems on relational engines, it is helpful to determine whether the engine stores aggregates contiguously on disk and routes them to a single node by design. If not, the performance characteristics may differ from those of a document database that maintains physical locality.

Both approaches are valid. In database-first deployment, developers depend on in-database declarations to ensure performance, working alongside the database administrator and using tools like execution plans for troubleshooting. In contrast, application-first deployment shifts more responsibility to developers, who must validate both the application’s functionality and its performance.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/8edf2224-cropped-b288acf6-franck-pachot-.png)

Franck Pachot is a developer advocate at MongoDB who is a seasoned database consultant and cloud evangelist with extensive experience in Oracle, PostgreSQL and cloud technologies. Known for his deep technical expertise, Franck is a sought-after speaker and mentor in...

Read more from Franck Pachot](https://thenewstack.io/author/franck-pachot/)