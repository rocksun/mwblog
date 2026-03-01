AI agents don’t slot neatly into the way enterprise data stacks were designed. A typical agent needs transactional state (e.g., what just happened), long-term memory, similarity search, relationship-aware data, and the ability to react to data changes in real time. In most organisations, that means stitching together a relational database, a vector store, a graph engine, and layers of middleware to keep everything in sync.

> “AI agents don’t slot neatly into the way enterprise data stacks were designed.”

That architecture can work, but with it comes latency, duplication, and operational overhead. And as agent-based systems reach production, the complexity becomes a real liability. That is why [SurrealDB](https://surrealdb.com/) is setting out to tackle what it calls “architectural sprawl,” with a multi-model database designed to handle structured records, connected data, and AI workloads inside a single engine.

Founded in 2022 by brothers [Jamie](https://www.linkedin.com/in/jaimemorganhitchcock) and [Tobie Morgan Hitchcock](https://www.linkedin.com/in/tobiemorganhitchcock/), the London-based company has just announced the general availability of [SurrealDB 3.0](https://surrealdb.com/3.0), which builds on its existing multi-model foundation with a stronger focus on persistent agent memory, expanded vector capabilities, and a new in-database plugin system.

On top of that, SurrealDB last week [announced](https://surrealdb.com/blog/surrealdb-raises-23m-series-a-extension-to-power-the-ai-native-database-era) it has raised $23 million in fresh funding, bringing its total raised since inception to $44 million.

## Death by a thousand databases

If there’s one thing the modern software stack doesn’t lack, it’s databases. [PostgreSQL](https://www.postgresql.org/) underpins large volumes of structured, transactional workloads. [MongoDB](https://www.mongodb.com/) has become a default choice for document-oriented applications. [Neo4j](https://neo4j.com/) carved out a niche around graph analytics and connected data. [Redis](https://redis.io/), meanwhile, dominates in-memory caching and real-time performance use cases. Each was built to solve a specific class of problem, even if many have expanded on their original capabilities.

SurrealDB, for its part, doesn’t position itself as a wholesale replacement for those systems. Large enterprises have invested years in tuning and scaling existing database stacks, and those platforms continue to serve their core workloads well. Instead, SurrealDB argues that AI-native systems introduce a different set of architectural pressures. Agents often require durable read-write state, low-latency retrieval across structured and unstructured data, and relationship-aware context — all within a single workflow. That combination can stretch conventional database boundaries.

> “SurrealDB reduces… complexity by enabling teams to keep an agent’s core state, contextual memory, and connected data model in one place.”

CEO [Tobie Morgan Hitchcock](https://www.linkedin.com/in/tobiemorganhitchcock/) says SurrealDB is focused on AI-native companies:

“It would be ridiculously expensive to rip and replace the largest deployments,” Tobie Hitchcock tells *The New Stack*. “Rather, SurrealDB is aimed at AI-native companies and use cases — building AI agents; building knowledge graphs; building real-time apps; embedded and edge.”

What makes those workloads different, Hitchcock argues, is how they combine multiple types of data access. Traditional applications can separate transactional updates, search, analytics, and relationship queries into different systems. Agents, by contrast, often need to update state, retrieve relevant context, and reason over connected data in near real time. That can mean data being copied across multiple stores and indexes just to keep everything aligned.

“Legacy patterns that see data shipped to separate indexes and stores add latency, duplication, and bring significant risk,” Hitchcock says.

SurrealDB’s answer, he says, is to consolidate those moving parts into one system — keeping structured state, contextual memory, and connected data together.

“SurrealDB reduces that complexity by enabling teams to keep an agent’s core state, contextual memory, and connected data model in one place,” Hitchcock says.

## Extending the database layer

While SurrealDB has long supported multiple data models inside a single engine, version 3.0 introduces a formal extension system and brings more application logic directly into the database layer.

[Surrealism](https://surrealdb.com/surrealism), as it’s called, is an open source plugin framework that allows developers to define business logic, access controls, and API behaviour as version-controlled modules that run inside SurrealDB itself. Rather than relying solely on external services or stored procedures tied to a single deployment, teams can package and share extensions that execute with full transactional guarantees.

In real terms, that might mean generating mock data directly inside the database for testing, exposing specialised functionality from Rust libraries that would otherwise live in application code, or embedding domain-specific logic — such as language processing or financial calculations — closer to the data it operates on.

Alongside Surrealism, SurrealDB 3.0 also introduces more explicit support for the company’s persistent agent memory. That means structured records, embeddings, and relationship data can be stored and queried together within the same database instance, rather than managed across separate systems. To support that, the release expands vector indexing and similarity search performance, and allows structured data to be queried alongside images, audio, and documents using SurrealQL.

In effect, the database is designed to let agents retrieve semantically similar content, query related records, and update state within the same system.

## The (not so) open source factor

It’s worth noting that while facets of the broader SurrealDB platform are open source, the core database itself is not, a move explicitly designed to prevent third parties from offering it as a managed database service. This reflects a lesson learned across the database ecosystem, where cloud providers have taken open-source projects and commercialised them as hosted services. Companies such as [MongoDB](https://techcrunch.com/2018/10/16/mongodb-switches-up-its-open-source-license/) and [Redis responded](https://techcrunch.com/2019/02/21/redis-labs-changes-its-open-source-license-again/) by shifting to proprietary, source-available [licensing models](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) to retain control over managed offerings.

“As a result, SurrealDB is able to offer a managed platform for running SurrealDB, which is operated by the people who built it,” Hitchcock says. “This means we can deliver the most reliable, secure, and up-to-date experience end-to-end.”

In short, anyone can run and self-host SurrealDB for free, and if they want a fully managed version with the expertise that goes with it, they can pay for it.

This approach has seemingly helped SurrealDB garner some impressive enterprise logos, with the likes of Nvidia, Tencent, Walmart, and Verizon taking pride of place on the company’s homepage. However, the company declined to specify which are paying customers and which are running the self-hosted version.

“Unfortunately, we can’t disclose which of our logos are paying customers due to commercial confidentiality,” Hitchcock says. “We have a healthy mix of commercial customers and large-scale, non-commercial enterprise deployments.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)