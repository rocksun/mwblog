# Tackling the Challenges of Logical Replication in PostgreSQL
![Featued image for: Tackling the Challenges of Logical Replication in PostgreSQL](https://cdn.thenewstack.io/media/2024/08/a1e52279-global-1024x576.jpg)
Distributed Postgres vendor [pgEdge](https://thenewstack.io/startup-pgedge-tackles-the-distributed-edge-with-postgres/) continues to tackle the complexities of [logical replication](https://thenewstack.io/heres-when-to-use-write-ahead-log-and-logical-replication-in-database-systems/) with its latest version, known as the “Constellation Release,” which offers enhanced parallel processing, large object support and error handling.

The greater throughput, flexibility and control make pgEdge a viable open source alternative for legacy database workloads requiring [multimaster capability](https://www.pgedge.com/solutions/benefit/multi-master), according to [Phillip Merrick](https://www.linkedin.com/in/phillipmerrick/), pgEdge CEO. Today these workloads are typically running on legacy platforms such as [Oracle](https://developer.oracle.com/?utm_content=inline+mention) Goldengate, he said in an email.

These workloads need the ability to take both read and write traffic at multiple nodes in a distributed database cluster to achieve low data latency or very high levels of availability (four or five nines) or both. An example might be a financial services application that operates across multiple regions or a critical e-commerce application that can never be down, he explained.

Merrick and his cofounder [Denis Lussier](https://www.linkedin.com/in/denislussier/), who together previously created EnterpriseDB, built [pgEdge](https://www.pgedge.com/) on open source [PostgreSQL](https://thenewstack.io/postgresql-takes-a-new-turn/) with the idea that a few nodes in a geographically distributed cluster, each handling reads and writes, can offer low latency, high availability, resiliency and performance.

Though a powerful feature, [logical replication in Postgres](https://www.pgedge.com/blog/logical-replication-features-in-pg-17) presents challenges including consistency, synchronization, conflict resolution and overhead, affecting performance.

The Constellation Release features include:

: This PostgreSQL plugin replacement makes media assets for existing applications, such as binary files, images and other non-relational data types, compatible with logical replication. These large files in PostgreSQL databases can now run on pgEdge without modification. Though Postgres supports large objects as chunks in catalog tables, replicating these tables requires special handling, according to its[Large object logical replication (LOLOR](https://www.pgedge.com/blog/pgedge-platform-support-for-large-object-logical-replication))[GitHub page](https://github.com/pgEdge/lolor). With LOLOR, this data is stored in non-catalog tables to make replication across multiple database instances or servers easier. It replicates data based on logical changes such as insert, update and delete operations rather than physical changes at the storage level and employs[change data capture](https://thenewstack.io/real-time-data-access-across-highly-distributed-environments/)to ensure synchronization in near real-time to other database instances. This is especially useful in distributed systems where consistency, availability and fault tolerance are critical, according to pgEdge.**Replication exception handling and logging**: With an updated error handling and logging mechanism, replication errors are logged into a new exception table to prevent them from blocking subsequent changes. This enhances visibility into replication errors for easier troubleshooting without interrupting overall system operation.**Replication repair mode**: A new function allows users to use or opt out of using “repair mode” on a specific database node. This extra control can be used to prevent replication changes during error resolution or while modifying the state of a single database node. It also supports error remediation by external tools without affecting the entire cluster.
While counting these features as part of this release, the company announced automated Data Definition Language (DDL) replication and Snowflake sequences in April.

DDL is used to create and modify Postgres objects through command statements like `CREATE`
, `ALTER`
and `DROP`
. Postgres traditionally required modifications to table definitions through DDL commands be made manually on each node. With this automation, you can update the database schema on a single node, and the changes are seamlessly propagated to other nodes within the cluster.

[Snowflake sequences](https://docs.pgedge.com/platform/advanced/snowflake#snowflake-sequences) address the complexity of managing sequences in multimaster replication scenarios. In a distributed multimaster Postgres system, the sequence must be updated across different regions and if each node updates the sequence independently it creates conflicts that cannot be resolved. This replacement for PostgreSQL sequence definitions provides a unique sequence — a timestamp, a counter and a unique node identifier — within a cluster that can be used across different regions without the need to write code or modify schema.
The company announced its free tier Cloud Developer Edition in January and its [vector search capability](https://thenewstack.io/extension-pgvector-makes-pgedge-a-distributed-vector-database/) using open source extension [pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/) last October.

In the fourth quarter, pgEdge said it will add high-performance parallel replication, which it calls “a game-changer in the industry” to its capabilities.

High-performance parallel replication is the ability to run multiple data replication streams on each network connection between nodes, using multiple CPUs at each node for significantly higher levels of data throughput, Merrick explained. Current replication architectures for Postgres only permit one stream between nodes, placing an upper limit on replication performance.

This boost in replication throughput in high-traffic, cross-region transactional workloads will enable users to manage larger volumes of data replication across distributed clusters in high-demand environments while reducing lag times and ensuring timely synchronization.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)