The path from proof of concept to production-grade system exposes a familiar pattern in enterprise software. Teams sprint toward product-market fit, then spend years firefighting operational issues they didn’t initially architect for.

In the automotive industry, where data platform decisions affect millions of daily users, meeting this challenge becomes even more important, making effective data management mission critical.

As director of platform engineering at a major automotive company, I’ve lived this reality. I worked on an [internal developer platform (IDP)](https://thenewstack.io/idp-vs-self-service-portal-a-platform-engineering-showdown/) solution that strikes a balance between velocity and enterprise resilience. We learned through the development process that selecting the right distributed database architecture was equally critical to our platform’s success.

## The Challenge

Products often begin by pursuing market fit, with little focus on scale, resiliency or quality. We build quickly, iterate and eventually find market fit, but before we know it, our POC is in production.

I’ve experienced the consequences of this firsthand: Siloed teams, fragmented tooling and engineers that spend more time [managing infrastructure](https://thenewstack.io/infrastructure-eats-strategy/) than delivering business value. We’ve all been on incident response calls with hundreds of people that start with: “Did anyone merge code in the last 20 minutes?”

This operational toil fundamentally changed the way we allocated engineering resources, pulling talent away from innovation toward reactive maintenance. Solving this required rethinking both our platform architecture and our data layer.

## Building the IDP Foundation

Rather than imposing rigid standards, we built a centralized platform that embeds reliability, security and governance directly into the developer workflow. Our architecture incorporated four key elements:

* **Standardized SDLC and CI/CD** streamlined delivery pipelines with automated feedback loops, reducing manual intervention across teams.
* **Declarative infrastructure** through Infrastructure as Code principles, which gave developers a simple interface to complex provisioning operations.
* **Centralized observability** unified metrics and logging, dramatically reducing mean time to recovery by eliminating the need to correlate data from disparate systems.
* **Built-in security and disaster recovery,** automated compliance checks and resilience patterns that removed repetitive tasks while ensuring enterprise-grade protections.

The internal developer platform’s power comes from abstraction layers, particularly the [Open Application Model (OAM)](https://thenewstack.io/oam-the-kubernetes-application-model-bridging-development-and-deployment/). This framework enables developers to define applications based on their traits, including services, configurations and storage requirements. This makes more sense than runtime specifics.

We start by asking: What truly defines an application? It’s not just the runtime, whether a Kubernetes deployment or a Docker container. Applications also require service objects, ConfigMaps, PersistentVolumeClaims and more.

By organizing these components as reusable traits, OAM enabled our cloud infrastructure teams to evolve the platform independently while application teams maintained stable APIs. Critically, we needed this architectural pattern to extend to the data layer.

## Why Database Architecture Was Mission Critical

For automotive applications serving millions of users, database selection carries strategic weight. The wrong choice creates operational bottlenecks, limits deployment flexibility and introduces single points of failure that undermine our entire platform’s resilience.

We had specific requirements that standard database approaches couldn’t satisfy:

* **Data sovereignty** requirements required that data remain in specific geographic regions for regulatory compliance, ruling out centralized database services.
* **Geo-distribution** was non-negotiable for our automotive platform, where users span continents and latency directly affects user experience.
* **Operational consistency** with our cloud native architecture required a database that aligned with Kubernetes native patterns rather than fighting against them.
* **PostgreSQL compatibility** enabled our teams to use existing skills and tooling without retraining or requiring wholesale application rewrites.

## Evaluating Distributed SQL Database Options

We evaluated PostgreSQL, Google Spanner and CockroachDB before selecting YugabyteDB. Each option presented different tradeoffs.

* Standard PostgreSQL offered familiarity but lacked built-in geo-distribution and required complex external replication management.
* Google Spanner provided geo-distribution but locked us into Google Cloud and required us to adopt a new SQL dialect.
* CockroachDB offered distribution but had compatibility gaps that would require application changes.

We chose YugabyteDB primarily for data sovereignty, given the nature of our data, along with various factors related to deployment topologies and built-in replication.

YugabyteDB’s architecture aligned perfectly with our IDP vision, providing:

* Native PostgreSQL compatibility
* Flexible deployment topologies across multiple clouds
* Built-in data replication without external orchestration

Critically, YugabyteDB could be managed declaratively through the same Crossplane operators we used for other infrastructure.

## Integrating Distributed SQL with Open Application Model

We designed the database integration to follow the OAM pattern through a three-layer architecture that treats database infrastructure as declarative platform resources:

### **Control Plane API**

The Control Plane API centralizes resource management, handling database instance provisioning, service account creation and API key management. This layer exposes database capabilities through the same declarative interface developers use for compute and storage resources.

### **Data Plane API**

The Data Plane API manages the operational life cycle of YugabyteDB clusters, orchestrating scaling, backup and recovery operations. It allows us to configure disaster recovery policies, replication topologies and backup schedules that apply automatically without developer intervention.

### **Declarative YugabyteDB Resources**

Declarative YugabyteDB Resources are managed through Crossplane operators to abstract database configurations, role management and security controls into reusable components. Developers can specify database requirements (size, replication factor, geographic distribution, etc.) and the platform provisions appropriately configured clusters.

This process transforms YugabyteDB into a platform primitive that developers can consume without database expertise. When a developer declares they need a geo-replicated database with read replicas in three regions, they simply define those requirements, and the platform handles the implementation details.

## The Result

Our architectural investment delivered measurable results across both developer productivity and database operations:

* **Operational simplification** came from eliminating manual database provisioning and configuration. Teams that previously spent days setting up PostgreSQL replication now get production-ready distributed databases in minutes.
* **Built-in resilience** meant that disaster recovery and failover became platform capabilities rather than per-application concerns. When regional failures occur, automatic failover happens without developer involvement.
* **Real-time analytics** capabilities improved as a result of YugabyteDB’s distributed architecture. We can scale read capacity independently, supporting both transactional workloads and analytical queries without performance degradation.
* **Accelerated time-to-market** resulted from removing database management friction. Teams shipping new services no longer block on database provisioning or spend sprints implementing replication logic.

## Lessons for Platform Engineering

Our experience during this project taught us a critical lesson: Internal developer platforms succeed or fail based on their weakest infrastructure component. A sophisticated IDP with poor database architecture creates bottlenecks that undermine the entire platform’s value proposition.

The key is choosing technologies that align with your platform model. For cloud native platforms built on declarative infrastructure and abstraction layers, databases must integrate as manageable platform resources, rather than as external dependencies that require specialized knowledge.

Our goal was straightforward: to provide developers with the tools they need to deliver consistent, reliable and secure solutions quickly. When developers succeed, the business naturally follows.

For organizations building platform engineering capabilities, my advice is straightforward: Invest equally in platform abstractions and the infrastructure they manage.

The database layer is more than just storage; it’s a foundational platform infrastructure that determines what’s possible at the application layer. Choose wisely, abstract thoughtfully, and make future architectural decisions easy by embedding them directly into your platform from the very start.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/44a0b024-cropped-26853340-gaurav-saxena.jpeg)

Gaurav Saxena is an engineering leader in the field of platform and cloud engineering with over 20 years of experience in the software industry. His technical expertise includes stream-based architectures, Kubernetes, service mesh, data engineering, software supply chain security and...

Read more from Gaurav Saxena](https://thenewstack.io/author/gaurav-saxena/)