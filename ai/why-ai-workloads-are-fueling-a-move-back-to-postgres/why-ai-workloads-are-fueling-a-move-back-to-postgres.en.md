I have spent the last couple of years watching the database landscape move through waves of excitement and disappointment. Vectors, graph, multimodal and NoSQL systems all took turns in the spotlight. Each wave promised simpler development and new possibilities. Some delivered. Some did not. Most made sense in their moment.

Then AI arrived. AI did not simply stretch existing systems. It broke the assumptions that shaped the last generation of managed database services. It exposed hidden trade-offs that were easy to ignore when workloads were lighter and changes were slower.

It also pushed teams to rethink how they work with data. Today, I see a clear shift in the market. Teams are moving back to Postgres. More and more new applications start with Postgres in the stack. [Postgres is becoming the database of AI](https://thenewstack.io/why-a-boring-database-is-your-secret-ai-superpower/). If an engineer is building some new application today, they are very likely going to use Postgres in their stack. It’s the [most popular database system in 2025](https://www.trytami.com/p/most-popular-technologies-in-2025) by far.

I want to explain why this shift is happening (at least in my humble opinion). I want to describe why Postgres is silently becoming the anchor of modern AI development. I also want to explain why many teams should consider leaving fully managed databases behind.

This is not about nostalgia and self-hosting in the old sense. It is about a new model that keeps the benefits of managed services while giving teams the performance, cost control and data locality they need for the next decade. The new model is BYOC (Bring Your Own Cloud).

## How AI Workloads Broke the Managed Database Model

The entire managed database ecosystem grew during a period of predictable workloads. Lift-and-shift migrations into the cloud were the backbone of the growth of services like Amazon Relational Database Service (RDS) or Azure Managed SQL. First, you lift-and-shift onto the plain Elastic Compute Cloud2 (EC2) instance, and then you move to RDS. Straightforward playbook, everyone did the same thing. No brainer.

Most applications behaved like classic Software as a Service (SaaS) products. They had modest working sets. They used straightforward online transaction processing (OLTP) patterns. They scaled gradually. They relied heavily on network-attached storage, autoscaling groups and stable indexing structures. Performance was usually good enough. Latency was acceptable. Costs were manageable. And then AI showed up.

AI workloads behave very differently. They are bursty. They rely on heavy parallelism. They use vector search and high-dimensional embeddings. They ingest large datasets continuously. They require frequent experiments, fast cloning and many isolated environments. They also require tight proximity between compute nodes and data storage. The gap between old and new patterns creates friction that managed databases cannot hide anymore.

I speak with engineering teams every week. They all describe similar experiences. They try to scale a managed Postgres instance during a model rollout. They hit IOPS limits. They hit throttling windows. They see latency spikes at the exact moment they need predictability. They also see cost blowups because the only way to remain safe is to overprovision every environment. These problems accumulate slowly at first. Then they become unmanageable once AI workloads reach production scale.

This is the moment when teams start questioning the managed model itself.

## The Convergence on Postgres for Modern Development

Almost every major database vendor now talks about PostgreSQL compatibility. Some treat it as simple marketing. They feel FOMO and want to “jump on the Postgres ship.” It’s unclear how their offer adds value to the already competitive Postgres market, but they make the jump first and worry about the go-to-market strategy later. Others rebuild their entire engine around it.

These vendors do that because they anticipate developers’ needs. Developers want a stable and well-understood SQL system. They want strong transactions. They want predictable joins. They want broad tooling support. They want a database that does not lock them into a single company or architecture. They want open source.

> Postgres has decades of refinement that newer systems cannot match. And it’s production-proven and rock solid.

Postgres delivers all of this without forcing teams into a specialized model. It is flexible enough to serve as an OLTP engine. It can handle analytics. It can store vectors. It can run time series workloads. It can serve as a cache. It has extensions for almost everything. It has decades of refinement that newer systems cannot match. And it’s production-proven and rock solid.

AI strengthens this convergence. AI teams want fewer moving parts. They want simpler pipelines. They want transactional safety combined with analytical capability, as they don’t have time to figure out new database architectures.

They want to move fast in this emerging market. They want vector search without maintaining a separate vector store. They want to test new features on real data without complex data sync jobs. They want to query across data models. Postgres gives them the opportunity to unify these workloads in one place.

> I see more teams removing entire layers of their data stack because they realize that Postgres can handle the vast majority of their needs with the right infrastructure behind it.

I see more teams removing entire layers of their data stack because they realize that Postgres can handle the vast majority of their needs with the right infrastructure behind it. They get lower latency. They get fewer operational surprises. They get a simpler development workflow. Most importantly, they get a single, well-understood data system that fits both the application and the AI pipeline.

The shift is not theoretical. It is visible in product roadmaps across the industry.

## **Why Managed Postgres Cannot Handle AI Scale**

We have now established that Postgres is the new center of gravity. The next question is where and how to run it. For years, the default answer was simple. Use RDS. Use Aurora. Use Cloud SQL. The pitch was simple: Let someone else run Postgres.

“The days of DBAs are gone,” they said. Most developers liked this idea. It removed infrastructure responsibility from the critical path. It reduced operational overhead. It shifted the responsibility of managing databases to the cloud vendor.

But the model has a hidden constraint. A managed database means a one-size-fits-all solution. Users depend heavily on network storage. They accept network latency. They accept fixed IOPS limits. They accept multisecond cold starts. They accept the cost structure that comes with these designs. These trade-offs made sense 10 years ago. But why would you need to pay for IOPS in 2025? The pricing model still treats IOPS as scarce, even though modern Non-Volatile Memory Express (NVMe) changes the equation.

AI workloads demand extremely fast storage and predictable performance. They also require large and frequent database clones for testing and experimentation.

Managed databases struggle in both areas. The internal storage layers of managed systems create unavoidable bottlenecks. The cloning mechanisms depend on snapshot-restore cycles or full-blown physical copies. Both approaches are slow and expensive, especially at scale.

Once a team hits these limits, the only fix is overprovisioning. You keep increasing the instance size. You maintain oversized replicas. You run full staging environments 24 hours a day, even when they sit idle. Your costs grow faster than your product. This is the opposite of what teams want in the AI era.

This is the point where teams begin looking for alternatives that give them the full power of Postgres without the restrictions of managed systems.

## **The Rise of BYOC Postgres**

I see a new pattern emerging across teams building serious AI features. They want Postgres in their own cloud account. They want control over compute and storage. They want to colocate data with GPUs. They want unlimited IOPS. But first and foremost, they still want the benefits of an automated experience that gives them backups, replication and monitoring.

This is the BYOC model. It is not traditional self-hosting. It is a managed platform that runs inside your own cloud environment. You keep full control over infrastructure. You keep your cloud discounts. You keep your security posture. You also keep control over where data physically lives, which matters for data residency and regulatory requirements.

This model aligns naturally with compliance frameworks like SOC 2, HIPAA, GDPR and CCPA. Data never leaves your account. Encryption is handled with your own keys. Key management integrates with your existing key management service setup. Tenant isolation follows the same boundaries you already trust across the rest of your infrastructure.

The platform takes care of operational complexity like backups, replication, upgrades and failure handling. You stay in control of policies, access and audit boundaries. For many teams, this is the first time managed Postgres actually fits their security and compliance model instead of fighting it.

## How Data Locality and Local Storage Improve Performance

To further add to BYOC benefits, with the right tooling, this model resolves performance problems by removing the networked storage bottleneck. Solutions such as [Vela](https://vela.simplyblock.io/) let you deploy Postgres on the same instance where your storage is, leveraging the speed and performance of local NVMe devices attached to the instance. Using [distributed simplyblock storage](https://www.simplyblock.io/) “under the hood,” it provides resilience and scalability, as well as copy-on-write functionality, which are otherwise not available with local storage. And that’s all deployed and managed in your own cloud. All you need to do is provision a cloud instance with local NVMe devices.

Results? Storage latency drops into the microsecond range. IOPS limits disappear. Parallel ingestion becomes not only practical but required to reach the database’s limits. Extensive vector indexes no longer punish the system during rebuilds. Queries stay predictable even under heavy load.

BYOC also solves the cost problem because you pay the cloud provider directly for compute, RAM and storage. There is no markup. There are no IOPS charges. There is no forced overprovisioning of many full-size environments. You only run the compute you actually need, and additional environments are spun up in seconds, with or without an existing dataset. This model works especially well when combined with database cloning.

And this brings me to the most critical workflow shift.

## **Cloning and Branching Become Central To AI Development**

AI development depends on fast experimentation. Teams need to test new models on real data. They need to validate prompts and embeddings. They need to run migrations. They need to isolate feature branches. They need to replay events. They need to evaluate pipelines with safety. This workflow requires a constant stream of clean environments.

Traditional managed databases create clones by copying the entire dataset. This approach is slow, expensive and wasteful. It limits the number of environments you can maintain. It forces developers to cut corners. It also delays testing because each clone takes real time to produce.

> Once a team experiences clone-based workflows, they rarely go back.

Modern Postgres platforms change this with thin clones that rely on copy-on-write semantics. A clone starts instantly because it shares the underlying data with the production database. Storage consumption grows only as the clone diverges. Performance remains stable. You can create as many clones as you want. You can attach them to and automate them for your CI pipelines. You can tie them directly to feature branches. You can destroy them as soon as the test ends.

[![](https://cdn.thenewstack.io/media/2025/12/fdc15dac-image3.png)](https://cdn.thenewstack.io/media/2025/12/fdc15dac-image3.png)

Figure 1

This model fits AI development perfectly. It lets you run parallel experiments without waiting for terabytes of data to copy. It enables you to compare results across environments. It allows you to build confidence before deploying changes. It also reduces the number of full-sized databases you need to pay for.

Once a team experiences clone-based workflows, they rarely go back.

## The Importance of the Postgres Ecosystem for AI

AI systems usually depend on many specialized databases. You had the transactional database for the product. You had a vector store for embeddings. You had a data warehouse for analytics. You had a time series system for metrics. You had a full-text search engine for retrieval. You had pipelines that moved or synchronized data between them. This architecture created complexity and cost because data had to move constantly.

[![](https://cdn.thenewstack.io/media/2025/12/0deb59bf-image2.png)](https://cdn.thenewstack.io/media/2025/12/0deb59bf-image2.png)

Figure 2

One of the key strengths of Postgres is its ecosystem. Thanks to its community, Postgres handles embedding search with [pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/). It handles analytical workloads at low to mid-range scales because NVMe-backed storage removes many historical read bottlenecks (and [PostgreSQL 18](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) adds async-read support). It handles time series data with and without extensions. It handles caching patterns through materialized views. It handles event ingestion and stream processing with logical replication. And it still handles OLTP with the strong consistency it’s known for.

The ability to run all of these workloads on a single system changes the shape of the AI backend. You get fewer moving parts. You get lower latency because data stays local. You get simpler deployment patterns. You get reproducible pipelines. And you get less operational overhead.

The Postgres ecosystem provides the ability to turn the database into “something more than just a database,” which is what everyone really wants in the age of AI. [SQL is a 50-year-old technology](https://thenewstack.io/why-ai-and-sql-go-together-like-peanut-butter-and-jelly/), and its (re)adoption is not meant to be a step back, at all. It is meant to be a step forward. Postgres provides a stable base, and the value is extracted on the other layers of its ecosystem.

## Developer Velocity: The Hidden Driver of the Shift

Performance and cost are easy to measure. Developer velocity is more challenging to quantify but equally important. AI development involves constant iteration. Developers need fast feedback. AI agents need even faster feedback. Both need safe environments. Developers also need a reliable way to test schema changes and validate new ideas on real data without fear.

I strongly believe that managed databases were never designed for developers to build modern applications on them. They do not offer clone-based or branch-based workflows. They were designed to provide a stable endpoint. Everything else happened outside the database. This increases the gap between code changes and database changes and increases the amount of data to be transmitted between the database and application. It also slows down the feedback loop.

Modern Postgres platforms, such as Vela, [Neon](https://thenewstack.io/neon-branching-in-serverless-postgresql/) or [Supabase](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/), close this gap. They give developers a simple interface for creating branches, running tests and merging changes. The database behaves like part of the development process rather than a distant service. The result is faster iteration and fewer surprises in production.

Once teams experience this workflow, they start to question why they ever accepted a slower model. The impact on release cycles is measurable. Developers spend less time waiting. They spend more time building. They catch issues earlier. They deploy with more confidence.

Velocity becomes a strategic advantage. The teams that can test and ship faster gain more ground every week. Postgres with branching and cloning supports this pace. It gives you the safety net you always wanted but could never achieve with manual processes.

## **So, Why Is Everything Moving Back to Postgres?**

After speaking with hundreds of teams and watching their infrastructure evolve, I believe the shift back to PostgreSQL is not a temporary trend. It is a long-term course correction brought on by the demands of AI and modern application development.

Postgres has the right mix of features, maturity and extensibility. It works for OLTP. It works for OLAP at reasonable scales. It works for vector search. It works for time series. It works for real-time analytics. It works for event-driven systems. In most of the cases, it just works for any type of workload.

The problem was never Postgres. The problem was the environment in which Postgres ran. Managed systems used designs that no longer fit the needs of AI. BYOC platforms fix that. They combine the control of self-hosting with the convenience of a managed service. They let teams keep their cloud account and their security posture while gaining high-performance Postgres with instant cloning and modern storage.

This model brings Postgres back to the center of the architecture. It also brings control back to the teams who rely on it. AI demands this level of control.

The new stack is built around Postgres in your own cloud, supported by a platform that handles the operational complexity.

This is why everyone is moving back to Postgres. It is the proper foundation for the next decade of AI applications. It gives teams the flexibility, performance and cost control they need. It lets developers build with confidence. And it simplifies the entire data landscape in a way that matches the speed of modern development.

I believe this shift has only just begun. The next generation of AI platforms will not be built on a patchwork of specialized systems. They will be built on a unified data foundation. That foundation is Postgres. It will run close to compute. It will handle all workloads. And it will give teams complete control over their most important asset: their data.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/11/f2577ed6-0e06-4790-81af-7a0f442f71f2.jpg)

Rob Pankow is the co-founder and CEO of simplyblock, a cloud infrastructure company that helps enterprises optimize their storage costs and performance. With over a decade of experience in the technology sector, he focuses on analyzing market dynamics and helping...

Read more from Rob Pankow](https://thenewstack.io/author/rob-pankow/)