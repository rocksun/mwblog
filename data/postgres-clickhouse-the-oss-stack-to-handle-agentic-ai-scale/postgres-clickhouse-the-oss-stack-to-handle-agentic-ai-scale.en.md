Postgres is a common pick to bootstrap an application because it’s well known, flexible and dependable. Its flexibility means it can handle most things you throw at it, for a time. As an application scales, Postgres is often pushed to its limits by workloads it wasn’t built for.

The point at which an app reaches these limits hasn’t changed, but the time taken to reach that point has dramatically reduced thanks to AI.

One pattern that has emerged to address this is combining [Postgres](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) with ClickHouse. In this architecture, [Postgres continues to serve transactional workloads](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/), while [ClickHouse handles analytics](https://thenewstack.io/vector-search-without-the-lock-in-why-devs-like-clickhouse/). Both databases are open source, and an ecosystem has developed that brings them closer together.

## Scaling Beyond PostgreSQL

In the AI era, growth that used to unfold over years now happens in months. Developers are reaching the limits of Postgres much sooner because AI-driven workloads accelerate product development, data creation and analytical demand.

This trend isn’t limited to internal dashboards or offline reporting. More often, it’s affecting user-facing applications. Real time dashboards, recommendation systems and search over large datasets all depend on fast analytical queries. Once these features become part of the user experience, [the architecture has to support low-latency access to high-volume data,](https://clickhouse.com/blog/langchain-why-we-choose-clickhouse-to-power-langchain#what-were-the-challenges-you-faced-with-postgres) and Postgres alone is not enough.

## How Postgres + ClickHouse Work Together

Building an application that uses both Postgres and ClickHouse usually involves two main challenges. The first is data integration, meaning how to move the right data into the right database. The second is application integration, meaning how to ensure the application knows which database to query for each operation.

### Data Integration

There are two common patterns for integrating ClickHouse with PostgreSQL.

**Split or dual-write**: Applications write data directly to PostgreSQL and ClickHouse based on the specific use case. The split-write pattern writes data only to the database that needs it, while the dual-write pattern sends all data to both systems simultaneously. This approach works well when there is clear delineation in what data is used for. For example, it’s unlikely that telemetry or user tracking events need to be sent to Postgres when they are likely only used for analysis. Supporting this pattern means updating the application to send data to the right database.

![](https://cdn.thenewstack.io/media/2025/12/c9f2dbcd-image2-981x1024.png)

**Change data capture (CDC)**: All writes occur in PostgreSQL, which remains the source of truth. A [CDC process streams inserts, updates and deletes into ClickHouse](https://clickhouse.com/blog/seemplicity-scaled-real-time-security-analytics-with-postgres-cdc-and-clickhouse#hitting-the-postgres-bottleneck-and-why-cdc-matters) so analytical queries always reflect the latest state without placing extra load on the transactional database. This pattern fits operational analytics use cases, where consistency is essential but [analytical performance remains a priority](https://clickhouse.com/blog/sewerai-sewer-management-at-scale#postgres-to-peerdb-to-clickpipes). It allows teams to maintain transactional guarantees in PostgreSQL while scaling analytical queries independently in ClickHouse.

![](https://cdn.thenewstack.io/media/2025/12/810109d7-image1-1024x907.png)

### Application Integration

The goal of integrating Postgres and ClickHouse is to use each database for the workloads it is strongest at. This means that some queries will remain on Postgres, and some will be moved to ClickHouse.

[Many apps use object relational mappers (ORMs) with Postgres](https://clickhouse.com/blog/moosestack-does-olap-need-an-orm), but this is less common with analytical databases. There are some [open source projects like MooseStack](https://clickhouse.com/blog/clickhouse-powered-apis-in-react-app-moosestack), which can provide an [ORM-like experience for ClickHouse](https://clickhouse.com/blog/eight-principles-of-great-developer-experience-for-data-infrastructure). More commonly, the integration uses [ClickHouse native language clients](https://clickhouse.com/docs/integrations/javascript).

An integration will begin by identifying the queries that will move, such as any queries that are doing large aggregate queries. The API routes for these queries will need to be updated to send the SQL to ClickHouse. It’s possible to use a backward-compatible pattern that allows for these routes to be swapped to and from Postgres or ClickHouse during testing. This pattern is used by [clickhouse.build](https://clickhouse.com/blog/clickhouse-build-agentic-cli-accelerate-postgres-clickhouse-apps), an agentic CLI that can automatically migrate TypeScript codebases to use Postgres and ClickHouse for prototyping.

An alternative approach can be to use a foreign data wrapper (FDW) inside Postgres, which allows queries to be sent to Postgres as-is and pushed down to ClickHouse transparently. This reduces the amount of work needed to start using Postgres and ClickHouse together, though can sacrifice some control over the integration.

## An Open Source Ecosystem

The Postgres and ClickHouse ecosystem has grown into a well-established stack. Many teams now pair the two databases by default, and a set of mature open source and commercial tools make this architecture straightforward to operate at production scale. The focus of these tools is narrow and intentional: reliable Postgres replication, fast ingestion into ClickHouse and smooth integration with existing Postgres workflows.

### **PeerDB**

[PeerDB is an open source project](https://www.peerdb.io/) that delivers high-throughput PostgreSQL CDC and reliable replication into ClickHouse. It supports large update streams, handles schema changes and avoids putting load on the transactional database. PeerDB also underpins managed services like [ClickPipes for ClickHouse Cloud](https://clickhouse.com/blog/postgres-cdc-connector-clickpipes-ga).

### **PostgreSQL Extensibility and FDWs**

The PostgreSQL extension model helps teams shift analytical workloads to ClickHouse without changing their application code. FDWs make this possible by exposing external systems as regular PostgreSQL tables. [Supabase’s ClickHouse FDW](https://supabase.com/docs/guides/database/extensions/wrappers/clickhouse), the open source [clickhouse\_fdw](https://github.com/ildus/clickhouse_fdw), and similar extensions let applications continue issuing familiar SQL through Postgres while the heavy analytical queries run in ClickHouse. This keeps the application layer untouched and provides a smooth path for moving analytics off Postgres as workloads grow.

### **ORMs and Developer Tooling**

Projects like [MooseStack](https://docs.fiveonefour.com/moose#get-started) show that developer tooling is keeping pace. They make it easier to use ClickHouse in environments where ORMs or schema-first development patterns are standard.

Overall, the ecosystem around Postgres and ClickHouse is not just a collection of tools. It is a focused, well-adopted stack designed for teams that outgrow a single online transaction processing (OLTP) database and need a fast analytical engine without losing the familiar Postgres development workflow.

## The Future

Today, many applications start with Postgres and then adopt ClickHouse after the cracks appear. As this timeline shrinks, adopting this architecture makes more sense from the beginning of the product life cycle. Developers should be able to start with Postgres + ClickHouse out of the box with minimal impact to product velocity.

Managed services, hosted replication and deeper integrations across tools are already moving in this direction. The goal is a seamless experience where transactional and analytical systems work together by default.

The core principle remains unchanged: Postgres and ClickHouse are not competing technologies. They complement each other and together form the foundation of a modern open source data architecture that is flexible, transparent and ready for production.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/107f15ff-cropped-b7032276-lionel-palacin-600x600.jpeg)

Lionel Palacin is a product marketing engineer at ClickHouse where he builds public demos to show users the product in action and write blog articles about it. Before that, he spent several years at Elastic working with customers and writing...

Read more from Lionel Palacin](https://thenewstack.io/author/lionel-palacin/)