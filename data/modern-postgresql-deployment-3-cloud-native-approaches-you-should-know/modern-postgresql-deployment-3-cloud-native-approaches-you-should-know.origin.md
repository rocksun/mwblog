# Modern PostgreSQL Deployment: 3 Cloud Native Approaches You Should Know
![Featued image for: Modern PostgreSQL Deployment: 3 Cloud Native Approaches You Should Know](https://cdn.thenewstack.io/media/2025/01/cd3c93d6-elephant-herd-1927515_1280-1024x682.jpg)
[PostgreSQL](https://thenewstack.io/postgresql-vs-the-cloud-for-genai-4-things-to-consider/) has solidified its position as one of the world’s most popular databases, currently ranking fourth, according to [Statista](https://www.statista.com/statistics/809750/worldwide-popularity-ranking-database-management-systems/). Its adoption is not just steady but accelerating, as found by the [2023 State of PostgreSQL Survey](https://www.timescale.com/blog/the-2024-state-of-postgresql-survey-is-now-open/). Since its initial release in 1990, the methods for installing, deploying, and managing PostgreSQL have evolved.
In this article, I’ll explore three cloud native and open source approaches to deploying PostgreSQL.

## Kubernetes Deployment with CloudNativePG
Deploying PostgreSQL on Kubernetes is the obvious choice in today’s cloud native landscape. Helm charts will make the deployment straightforward but [will not cover day two operations for stateful workloads](https://techcrunch.com/2022/11/25/how-to-run-data-on-kubernetes-6-starting-principles/) such as scaling, backups, failovers, and upgrades. This is where Kubernetes operators come into play.

[CloudNativePG](https://github.com/cloudnative-pg/cloudnative-pg), an open source Kubernetes operator, is gaining significant traction due to its robustness and because it is vendor-neutral and owned by the community. Two years ago, the company behind the project, [EDB](https://www.enterprisedb.com/), [donated the IP](https://www.cncf.io/blog/2024/11/20/cloud-neutral-postgres-databases-with-kubernetes-and-cloudnativepg/) to the community.
The operator stands shoulder to shoulder with other operators like [Crunchy Data](https://github.com/CrunchyData/postgres-operator) and [Zalando](https://github.com/zalando/postgres-operator) but with a strong emphasis on simplicity and data safety. One of the standout features of CloudNativePG is its focus on data integrity and high availability. It supports synchronous replication and automated failover, ensuring that your [data remains consistent and accessible even in the event](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/) of node failures. The project’s recent submission as a [CNCF Sandbox project](https://youtu.be/8HIPMmL433g?t=173) reflects its commitment to open source principles and collaborative development.

## Self-Service with Cloud Foundry Marketplace for Korifi
The rise of platform engineering has amplified the demand for self-service capabilities, allowing developers to deploy and manage [services without heavy reliance on operations](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/) teams. Cloud Foundry has long been a pioneer in providing a developer-centric PaaS experience.

[Korifi](https://github.com/cloudfoundry/korifi) delivers the same developer experience that Cloud Foundry is known for but leverages Kubernetes under the hood instead of virtual machines. Korifi abstracts the complexities of Kubernetes, providing a seamless interface that is well-known and familiar to developers.
One of its key historic features is the Cloud Foundry Marketplace, where platform operators and developers can deploy pre-built applications and services, [including PostgreSQL, which is now available for Korifi](https://thenewstack.io/korifi-at-kubecon-cloudnativecon-eu-2024-key-takeaways/). A simple cf create-service postgresql command is all that’s needed to deploy a PostgreSQL instance.

## Separating Compute and Storage with Neon
Traditional PostgreSQL deployments couple compute and storage resources, which can lead to scalability and resource utilization challenges. [Neon](https://github.com/neondatabase/neon?tab=readme-ov-file) offers a serverless approach, separating storage and computing.

Positioned as a serverless alternative to AWS Aurora PostgreSQL, the standard storage layer is replaced with a distributed architecture that redistributes data across a cluster of nodes. This separation allows computing and [storage to scale](https://thenewstack.io/momento-caching-at-scale-and-more-without-all-the-hassle/) independently, optimizing performance and cost.

One of Neon’s most liked features is its instant cloning and branching of databases, similar to how Git handles code branches. This allows developer teams to create isolated database instances quickly and efficiently.

## Conclusion
While this article is not meant to be an exhaustive list of modern ways to deploy PostgreSQL, the methods discussed reflect three significant trends.

The first is the shift of infrastructure towards cloud native principles. Running stateful workloads on Kubernetes was once considered impractical, but it has now become standard practice, requiring additional effort that Kubernetes Operators fulfill.

The second trend is the growing demand for self-service solutions aligned with platform engineering principles, allowing [developers to provision and manage](https://thenewstack.io/zeroops-helps-developers-manage-operational-complexity/) resources independently.

Lastly, companies are increasingly looking to move away from managed services — for reasons ranging from cost to compliance and security — and adopt open source or [private SaaS](https://www.youtube.com/watch?v=BUpcif_91hI) solutions that offer the same level of features but allow them to completely control their data.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)