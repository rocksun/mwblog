The traditional database taxonomy is broken. The labels we’ve used for over a decade like “NoSQL,” “relational,” “document, “key-value” and “graph” no longer describe how [modern databases](https://thenewstack.io/introduction-to-databases/) work or what developers actually need.

This isn’t just semantic drift. The fundamental assumptions that created these categories have changed. Modern applications don’t fit into neat database buckets, and neither should the systems that power them.

## **The Category Trap**

Database categories emerged from real technical limitations. In the early 2000s, you had clear trade-offs:

* Relational databases provided [ACID transactions](https://thenewstack.io/acid-compliant-distributed-sql-enters-the-agentic-ai-era/) and structured queries but struggled with scale and schema evolution.
* Document stores offered flexible schemas and horizontal scaling but lacked transactions and complex querying.
* Key-value stores delivered raw performance but minimal query capabilities.
* [Graph databases](https://thenewstack.io/common-uses-cases-for-graph-databases/) excelled at relationships but performed poorly for other access patterns.

These trade-offs forced architectural decisions early in development. Pick your poison: consistency or scale, flexibility or structure, performance or functionality.

The result was polyglot persistence — using multiple databases for different parts of the same application. A typical modern stack might include [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) for transactional data, Redis for caching, Elasticsearch for search, Neo4j for recommendations and [InfluxDB](https://www.influxdata.com/?utm_source=vendor&utm_medium=referral&utm_campaign=2025_spnsr-web_tns&utm_content=note&utm_content=inline-mention) for metrics.

This approach worked when systems were smaller and teams had time to manage complexity. It doesn’t work in today’s development environment.

## **The Convergence**

Modern databases are converging on a different architecture: general-purpose platforms that handle multiple workload types without requiring separate systems.

This convergence happened because the original technical limitations disappeared. Distributed computing techniques that seemed exotic in 2010 became standard. CAP (consistency, availability and partition tolerance) theorem trade-offs that appeared fundamental proved negotiable with better algorithms and infrastructure.

Consider what’s happened across the database landscape:

PostgreSQL added JSONB columns, making it viable for document workloads. It now includes full-text search, time series extensions and even [vector similarity search](https://thenewstack.io/combining-the-power-of-text-based-keyword-and-vector-search/) for AI applications.

Redis expanded beyond simple key-value operations to include modules for search, graph processing, JSON documents and time series data.

[Apache Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/) introduced secondary indexes, materialized views and more flexible data modeling.

Even traditional relational databases like SQL Server and Oracle added JSON support, graph capabilities and NoSQL-style flexibility.

MongoDB took this convergence furthest. What started as a document database now provides ACID transactions across distributed clusters, full-text and vector search powered by Apache Lucene and other [modern features](https://www.mongodb.com/products/platform/atlas-database/features/?utm_campaign=devrel&utm_source=third-party-content&utm_medium=cta&utm_content=tns-database-categories-are-dead&utm_term=jesse.hall).

The pattern extends beyond any single vendor. The most successful databases of the last five years are those that transcended their original categories.

## **Why This Matters for Developers**

The practical impact of this convergence is enormous. Instead of managing multiple database systems, modern applications can consolidate around platforms that handle diverse workload types.

This consolidation eliminates entire classes of problems:

* **No data synchronization**. When your user profiles, session cache, search indexes and analytics all live in the same system, you don’t need complex ETL (extract, transform, load) pipelines to keep data consistent.
* **Unified query language**. Developers learn one syntax instead of SQL plus Redis commands plus Cypher plus whatever domain-specific language your search engine uses.
* **Single operational model**. One backup strategy, one monitoring system, one scaling approach, one security model.
* **Transactional consistency**. Operations that span multiple data types can use the same ACID guarantees, eliminating the distributed transaction complexity that plagued polyglot architectures.

Real companies are seeing the results. Pharmaceutical companies are reducing clinical report generation from weeks to minutes. Financial platforms are managing hundreds of billions in assets while improving scaling performance by 64%. E-commerce sites are achieving sub-millisecond search response times without a separate search infrastructure.

## **The Polyglot Persistence Reckoning**

Polyglot persistence made sense when databases had hard limitations. It makes less sense when those limitations no longer exist.

The polyglot approach assumes that specialization always beats generalization. But specialization has costs: operational complexity, data consistency challenges and the cognitive overhead of managing multiple systems.

These costs were acceptable when the performance benefits were clear. As general-purpose platforms match or exceed specialized systems in their own domains, the trade-off calculation changes.

Consider search. Elasticsearch became the default choice for full-text search because relational databases handled it poorly. But when MongoDB’s Atlas Search delivers sub-millisecond response times using the same Apache Lucene foundation as Elasticsearch, what’s the benefit of maintaining a separate search cluster?

The same logic applies across database categories. When a general-purpose platform provides vector search performance comparable to specialized vector databases or time series processing that matches purpose-built systems, the architectural complexity of multiple databases becomes harder to justify.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/4e8b017a-cropped-bd1fcda7-jesse-hall-600x600.jpg)

Jesse Hall is a staff developer advocate at MongoDB and a global voice in developer education and modern app architecture. He helps developers build full-stack apps with MongoDB Atlas, JavaScript, TypeScript and Next.js — creating content that bridges hands-on implementation...

Read more from Jesse Hall](https://thenewstack.io/author/jesse-hall/)