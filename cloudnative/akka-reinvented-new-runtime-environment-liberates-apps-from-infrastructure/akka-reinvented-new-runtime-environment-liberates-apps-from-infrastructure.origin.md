# Akka Reinvented: New Runtime Environment Liberates Apps from Infrastructure
![Featued image for: Akka Reinvented: New Runtime Environment Liberates Apps from Infrastructure](https://cdn.thenewstack.io/media/2024/11/07d10d03-mobile-953343_1280.png)
The company formerly known as [Lightbend](https://thenewstack.io/lightbend-survey-cloud-native-is-a-process-not-a-place/) has launched into the public availability of the latest version of Akka, the [popular PaaS developer framework](https://thenewstack.io/lightbends-akka-serverless-paas-to-manage-distributed-state-at-scale/) for responsive applications. The updated solution boasts a new runtime environment empowering applications to manage their underlying infrastructure, including compute resources, storage persistence and, perhaps most importantly, location.

According to CEO [Tyler Jewell](https://www.linkedin.com/in/tylerjewell), the reinvented service has been in private production for select customers for the past four years. Lightbend also announced the company has been rebranded as [Akka](https://akka.io/).

The application responsiveness for which [Akka is known](https://thenewstack.io/akka-java-middleware-what-goes-inside-the-containers-counts/) upholds Service Level Agreements (SLAs) for applications by providing a deterministic latency profile for end users, elastically responding to workload changes, and facilitating application upgrades without downtime. In addition to the recently announced runtime environment, the platform includes an SDK and programming libraries.

“You’ve always been able to build these applications with Akka’s libraries,” Jewell said. “But, you had to do it yourself operating. Meaning you had this application; it’s doing great locally. The operator was on their own to figure out how to scale it up and have it adapt. Now, we’re giving that runtime environment so the application can have a home to run and get the SLA it’s looking for.”

Cloud native vendors frequently have SLAs for infrastructure like databases and Kubernetes. Akka inverts that paradigm by enabling SLAs for applications which manage their infrastructure to meet those contracts.

“It’s a different mindset when the application says I’m going to take and maintain responsibility for my SLA, and I’m going to do that in a way that’s independent of the underlying cloud native infrastructure,” Jewell said.

## Like an In-Memory Database
Akka deploys serverlessly in a number of different regions via the Bring Your Own Cloud model (in which customers access the managed service in their cloud of choice) and as a self-hosted option. Its runtime environment decouples applications from their infrastructure by enabling applications written with Akka to function similarly to an [in-memory](https://thenewstack.io/hazelcast-boosts-stream-processing-with-in-memory-computing/), durable database.

According to Jewell, this characteristic means the application is the system of record and is responsible for operations like clustering and data partitioning. However, “The application reacts and responds to the amount of traffic and data that’s there automatically by telling the infrastructure, ‘I need more compute’, or ‘hey, the data’s changing and therefore it needs to be persisted,” Jewell explained.

Akka manages (and guarantees) the compute and persistence required for the data for customers, who have to procure their own storage. Outsourcing these responsibilities means developers can simply focus on coding their applications. “But, what’s more important for the application is that since it’s like its own database, it knows its state, so it has the ability to recover itself without going and talking to the database,” Jewell said. “It knows how to effectively re-sequence itself to recover in any sort of failure situation.”

## Cross-Hyperscaler Portability
The recovery capabilities of the latest incarnation of Akka are attributed to the fact that applications written via this framework maintain the state — and the sequence of the state — either in memory or in persisted storage. As such, application recovery is extremely swift in the event of failure.

Moreover, since “the state, if you will, is available ‘on the network’, it makes the application movable,” Jewell said. “Meaning, the application can actually change locations from one to another and recover its state.” The latest edition of Akka employs these capabilities for developers to simultaneously run the same application in multiple regions.

Applications can also move between hyperscale cloud providers, as well as between cloud and on-premise environments. Users must specify which regions or locations they want the application to deploy. However, such portability is well-suited for reinforcing regulatory compliance, data sovereignty, disaster recovery, [failover](https://thenewstack.io/the-rush-to-fix-the-kubernetes-failover-problem/), and data repatriation. “So, you can move apps between different regions, cloud vendors, or just say I want to completely replicate it because I’ve got end users in different locations,” Jewell added.

Akka — the vendor — is so confident in its capabilities for these use cases that its terms of agreement now include a formal indemnification section applicable to situations in which applications built with Akka become unresponsive. It may be the only vendor to provide such reassurance. “We will compensate our customers for 20 times the period of unreliability,” Jewell mentioned. “If it was something that Akka did to cause the app to become unreliable for a day, we’d pay them 20 days of credit.”

## Multimaster Replication
Akka now incorporates a multimaster [replication model](https://thenewstack.io/why-cloud-data-replication-matters/) that includes multiple write nodes from which to modify data when it’s replicated. According to Jewell, a common replication paradigm involves allowing users to modify or write data from only one of the multiple replicated nodes while the others are read-only. “If you need to modify the data, what happens is your traffic gets routed to the node that allows you to modify it,” Jewell said.

With Akka’s “write-replicated” model, it’s possible to alter replicated data in diverse locations at the same time without latency, network trafficking, or getting locked out of the system. The data can be edited from each location it was replicated to “so you get higher levels of parallelism and concurrency and the system, behind the scenes, reconciles any conflicts,” Jewell said. “It’s kind of like Google Docs, but for your application transaction data. You get better end-user latency and a very predictable end-user experience.”

## Developers First
Nearly each of the tangible benefits provided by Akka’s newly publicly available functionality enhances developer productivity and ingenuity. These professionals can focus more time on writing the most meaningful, utilitarian applications and spend considerably less time determining the infrastructural needs required to keep them in production. The portability gains, uptime advantages, flexibility for reading and writing replicated data, and indemnification of application responsiveness represent what may well be a significant leap forward for cloud native applications.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)