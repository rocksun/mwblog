Too often, developers are unfairly accused of being careless about data integrity. The logic goes: Without the rigid structure of an SQL [database](https://thenewstack.io/database-categories-are-dead-heres-whats-next/), developers will code impulsively, skipping formal design and viewing it as an obstacle rather than a vital step in building reliable systems.

Because of this misperception, many database administrators (DBAs) believe that the only way to guarantee [data quality](https://thenewstack.io/introduction-to-databases/) is to use relational databases. They think that using a document database like MongoDB means they can’t be sure data modeling will be done correctly.

Therefore, DBAs are compelled to predefine and deploy schemas in their [database of choice before any application can persist or share data](https://thenewstack.io/multicloud-why-its-the-best-choice-for-data/). This also implies that any evolution in the application requires DBAs to validate and run a migration script before the new release reaches users.

However, developers care just as much about data integrity as DBAs do. They put significant effort into the application’s domain model and avoid weakening it by mapping it to a normalized data structure that does not reflect application use cases.

## Different Database Models, Different Data Models

Relational and [document databases take different approaches to data modeling](https://thenewstack.io/why-the-document-model-is-more-cost-efficient-than-rdbms/).

In a [document database](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/), you still design your data model. What changes is where and how the design happens, aligning closely with the domain model and the application’s access patterns. This is especially true in teams practicing domain‑driven design (DDD), where developers invest time in understanding domain objects, relationships and usage patterns.

The data model evolves alongside the development process — brainstorming ideas, prototyping, releasing a minimum viable product (MVP) for early feedback and iterating toward a stable, production-ready application.

Relational modeling often starts with a normalized design created before the application is fully understood. This model must then serve diverse future workloads and unpredictable data distributions. For example, a database schema designed for academic software could be used by both primary schools and large universities. This illustrates the strength of relational databases: the logical model exposed to applications is the same, even when the workloads differ greatly.

Document modeling, by contrast, is tailored to specific application usage. Instead of translating the domain model into normalized tables, which adds abstraction and hides performance optimizations, MongoDB stores aggregates directly in the way they appear in your code and business logic. Documents reflect the business transactions and are stored as contiguous blocks on disk, keeping the physical model aligned with the domain schema and optimized for access patterns.

Here are some other ways these two models compare.

## **Document Modeling Handles Relationships**

Relational databases are often thought to excel at “strong relationships” between data, but this is partly because of a misunderstanding of the name — *relations* refers to mathematical sets of tuples (rows), not to the connections between them, which are *relationships*. Normalization actually loosens strong relationships, decoupling entities that are later matched at query time via joins.

In entity-relationship diagrams (ERDs), relationships are shown as simple one-to-one or one-to-many links, implemented via primary and foreign keys. ERDs don’t capture characteristics such as the direction of navigation or ownership between entities. Many-to-many relationships are modeled through join tables, which split them into two one-to-many relationships. The only property of a relationship in an ERD is to distinguish one-to-one (direct line) from one-to-many (crow’s foot), and the data model is the same whether the “many” is a few or billions.

Unified Modeling Language (UML)-class diagrams in object-oriented design, by comparison, are richer: They have a navigation direction and distinguish between association, aggregation, composition and inheritance. In MongoDB, these concepts map naturally:

* **Composition** (for instance, an order and its order lines) often appears as embedded documents, sharing a life cycle and preventing partial deletion.
* **Aggregation** ( a customer and their orders) uses references when life cycles differ or when the parent ownership is shared.
* **Inheritance** can be represented via polymorphism, a concept ERDs don’t directly capture and workaround with nullable columns.

Domain models in object-oriented applications and MongoDB documents better mirror real-world relationships. In relational databases, schemas are rigid for entities, while relationships are resolved at runtime with joins — more like a data scientist discovering correlations during analysis. SQL’s foreign keys prevent orphaned rows, but they aren’t explicitly referenced when writing SQL queries. Each query can define a different relationship.

## **Schema Validation Protects Data Integrity**

MongoDB is schema-flexible, not schema-less. This feature is especially valuable for early-stage projects — such as brainstorming, prototyping, or building an MVP — because you don’t need to execute Data Definition Language (DDL) statements before writing data. The schema resides within the application code, and documents are stored as-is, without additional validation at first, as consistency is ensured by the same application that writes and reads them.

As the model matures, you can define schema validation rules directly in the database — field requirements, data types, and accepted ranges. You don’t need to declare every field immediately. You add validation as the schema matures, becomes stable, and is shared. This ensures consistent structure when multiple components depend on the same fields, or when indexing, since only the fields used by the application are helpful in the index.

Schema flexibility boosts development speed at every stage of your application. Early in prototyping, you can add fields freely without worrying about immediate validation. Later, with schema validation in place, you can rely on the database to enforce data integrity, reducing the need to write and maintain code that checks incoming data.

Schema validation can also enforce physical bounds. If you embed order items in the order document, you might validate that the array does not exceed a certain threshold. Instead of failing outright — like SQL’s check constraints (which often cause unhandled application errors) — MongoDB can log a warning, alerting the team without disrupting user operations. This enables the application to stay available while still flagging potential anomalies or necessary evolutions.

## **Application Logic vs. Foreign Keys**

In SQL databases, foreign keys are constraints, not actual definitions of relationships, which are evaluated at query time. SQL joins define relationships by listing columns as filter predicates, and foreign keys are not used in the JOIN clause. Foreign keys help prevent certain anomalies, such as orphaned children or cascading deletes, that arise from normalization.

MongoDB takes a different approach: By embedding tightly coupled entities, you solve major integrity concerns upfront. For example, embedding order lines inside their order document means orphaned line items are impossible by design. Referential relationships are handled by application logic, often reading from stable collections (lists of values) before embedding their values into a document.

Because MongoDB models are built for known access patterns and life cycles, referential integrity is maintained through business rules rather than enforced generically. In practice, this better reflects real-world processes, where updates or deletions must follow specific conditions (such asa price drop might apply to ongoing orders, but a price increase might not).

In relational databases, the schema is application-agnostic, so you must protect against any possible Data Manipulation Language (DML) modifications, not just those that result from valid business transactions. Doing so in the application would require extra locks or higher isolation levels, so it’s often more efficient to declare foreign keys for the database to enforce.

However, when domain use cases are well understood, protections are required for only a few cases and can be integrated into the business logic itself. For example, a product will never be deleted while ongoing transactions are using it. The business workflow often marks the product as unavailable long before it is physically deleted, and transactions are short-lived enough that there’s no overlap, preventing orphans without additional checks.

In domain‑driven models, where the schema is designed around specific application use cases, integrity can be fully managed by the application team alongside the business rules. While additional database verification may serve as a safeguard, it could limit scalability, particularly with sharding, and limit flexibility. An alternative is to run a periodic aggregation pipeline that asynchronously detects anomalies.

## **Next Time You Hear That Myth**

MongoDB does not mean “no design.” It means integrating database design with application design — embedding, referencing, schema validation and application‑level integrity checks to reflect actual domain semantics.

This approach keeps data modeling a first‑class concern for developers, aligning directly with the way domain objects are represented in code. The database structure evolves alongside the application, and integrity is enforced in the same language and pipelines that deliver the application itself.

In environments where DBAs only see the database model and SQL operations, foreign keys may appear indispensable. But in a DevOps workflow where the same team handles both the database and the application, schema rules can be implemented first in code and refined in the database as specifications stabilize. This avoids maintaining two separate models and the associated [migration overhead](https://thenewstack.io/mongodb-finds-ai-can-help-with-legacy-system-migration/), enabling faster, iterative releases while preserving integrity.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/8edf2224-cropped-b288acf6-franck-pachot-.png)

Franck Pachot is a developer advocate at MongoDB who is a seasoned database consultant and cloud evangelist with extensive experience in Oracle, PostgreSQL and cloud technologies. Known for his deep technical expertise, Franck is a sought-after speaker and mentor in...

Read more from Franck Pachot](https://thenewstack.io/author/franck-pachot/)