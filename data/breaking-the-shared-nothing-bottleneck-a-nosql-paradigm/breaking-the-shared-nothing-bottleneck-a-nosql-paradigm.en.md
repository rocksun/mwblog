While there is no single storage architecture model that fits all NoSQL databases, the often recommended approach is a distributed, shared-nothing architecture using local storage (often flash-based) at each node.

At the storage hardware level, direct-attached storage (DAS) would be an example of shared-nothing architecture. This model provides the desired high performance, low latency, fault tolerance and availability that business-critical NoSQL databases like Cassandra and MongoDB require.

While DAS offers significant advantages, it’s counterproductive to today’s data center climate of reduced CapEx, OpEx and sustainability initiatives. At the same time, critical data services inherent in a shared networked storage system, such as storage area networks (SANs), are missing in DAS.

However, with today’s SAN solutions, you can have your cake and eat it, too: efficiency, data services, resilience and yes, high performance and low latency, too. Modernizing your data platform to a SAN model, using a supplier with a disaggregated, software-defined architecture, can deliver the performance and fault tolerance your NoSQL database requires without compromising efficiency.

## Why Shared-Nothing Is Common for NoSQL

DAS is a prevalent model for performance-sensitive workloads, like [NoSQL databases](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/), because historically local flash, especially [Nonvolatile Memory Express (NVMe) storage](https://www.lightbitslabs.com/nvme-over-tcp/?utm_source=TNS&utm_medium=article&utm_campaign=nov), offered significantly lower latency and higher IOPS (faster read/write operations) than traditional shared storage, like SAN or NAS, accessed over a network. More on that later.

Most NoSQL databases are designed for horizontal scalability and a shared-nothing architecture, where each node is independent and manages its data, making scaling out much simpler and more efficient.

Additionally, some NoSQL databases are explicitly designed for a distributed, shared-nothing system. For example, in Cassandra, each node in a cluster is responsible for a subset of the data and uses its local disk for storage. And while there are flexible deployments for MongoDB, it strongly aligns with DAS due to its replica set and sharding architectures. When data is partitioned and replication is implemented across multiple nodes, there is higher resilience. If one node fails, only a portion of the data becomes temporarily unavailable, and the system can continue to operate using the replicas on other nodes. High resiliency is a requirement for business-critical database workloads.

## The Trade-Offs of Shared-Nothing Architecture

While DAS offers significant advantages, it comes with compromises and trade-offs that are counterproductive with today’s data center initiatives: reducing data center sprawl and energy consumption, reducing operational overhead expenses, managing exponential data growth at scale cost-effectively, supporting corporate sustainability guidelines and many others.

Intrinsically, because each node has its own dedicated storage in a DAS model, this requires more hardware. Hardware resources are often overprovisioned to accommodate unpredictable demand, resulting in lower resource utilization and stranded capacity. Underutilization of storage resources in DAS environments can be significant, potentially ranging from 30% to 70% (or even higher in some cases).

[![](https://cdn.thenewstack.io/media/2025/10/9e7af2bf-image1-1024x276.png)](https://cdn.thenewstack.io/media/2025/10/9e7af2bf-image1-1024x276.png)

Credit: Lightbit Labs

At scale, the CapEx and OpEx burdens of a DAS model can bloat an IT budget. Managing storage across a potentially large number of independent nodes can increase management overhead. Monitoring, upgrades and capacity planning must be performed on individual nodes.

As if bloated IT budgets weren’t painful enough, the biggest sting for those implementing DAS models is sacrificing data management capabilities common in SAN platforms. Advanced data management services (compression, thin provisioning, snapshots, deduplication, tiering, clones, replication) are not inherently available at the storage layer in a shared-nothing model. In a DAS model, the functionality would have to be at the application level, if available at all.

## A New Storage Paradigm for NoSQL

Given the dynamics of CapEx and OpEx budget pressures, along with sustainability initiatives and the need to reduce the sprawl prevalent in data centers today, there’s a shift toward shared storage platforms, like SAN, which can more than adequately replace the shared-nothing architecture for high-performance NoSQL workloads. Modern SAN systems can achieve performance comparable to local NVMe and support highly demanding NoSQL workloads.

The “icing on the cake” of a modern SAN capable of achieving performance equivalent to local flash is with high-speed interconnect technology. Forget Fibre Channel (FC) SAN and iSCSI. A SAN designed with [NVMe over Fabrics (NVMe-oF)](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) will extend the performance benefits of NVMe flash over a network fabric, significantly reducing latency and increasing throughput compared to traditional block protocols like iSCSI. This allows NoSQL applications to access shared storage with performance much closer to local flash, mitigating a key advantage of DAS.

[NVMe over TCP](https://www.lightbitslabs.com/nvme-over-tcp/?utm_source=tns&utm_medium=article&utm_campaign=nov) (NVMe/TCP), as a subset of NVMe-oF, combines the high performance of NVMe with the ubiquity and cost-efficiency of standard Ethernet networks using TCP as its transport layer. Unlike FC, NVMe/TCP operates over ubiquitous and cost-effective Ethernet infrastructure. This architecture model ensures ultra-low latency and high throughput without custom hardware or proprietary drivers.

Many organizations are taking their modernization initiatives to the next level by combining NVMe/TCP with disaggregated and [software-defined systems](https://thenewstack.io/how-software-defined-storage-empowers-developers/). The model bridges the gap between the performance of local storage and resource efficiency. A disaggregated, [software-defined storage](https://www.lightbitslabs.com/product/?utm_source=TNS&utm_medium=article&utm_campaign=nov) architecture with NVMe/TCP as its transport protocol checks all the boxes for supporting high-performance NoSQL workloads at scale: lower CapEx and OpEx costs, reducing data center sprawl and supporting sustainability initiatives, resiliency, high performance and efficiency. At the same time, these organizations have reduced their business risk by decreasing their dependence on proprietary hardware and complicated supply chains.

[![](https://cdn.thenewstack.io/media/2025/10/0cd0ccd7-image2-1024x316.png)](https://cdn.thenewstack.io/media/2025/10/0cd0ccd7-image2-1024x316.png)

Credit: Lightbits Labs

## Summing Up

While the distributed, shared-nothing architecture with DAS has been a historical recommendation for demanding NoSQL databases due to performance advantages, the storage technology has evolved to offer modern solutions with greater business benefits.

For smaller clusters, DAS might suffice, but at scale, it becomes operationally and economically burdensome. If there is pressure in your organization to optimize data center costs, enhance sustainability and simplify operations, then you should re-evaluate your shared-nothing, DAS model.

Modern SAN solutions, designed explicitly for disaggregated, software-defined architecture and high-speed interconnects like NVMe/TCP, offer a compelling alternative. They effectively bridge the performance gap while delivering the crucial data services and efficiency that DAS inherently lacks.

By embracing this modern storage paradigm, organizations can indeed have their cake and eat it too, achieving the high performance and low latency their business-critical NoSQL databases require, without sacrificing the economic and operational benefits of a shared storage infrastructure.

Moving from a shared-nothing model to shared, disaggregated and software-defined will not only support your NoSQL workloads today, but it will also future-proof data infrastructure for continued growth, scale and application demands.

To learn more about supporting NoSQL workloads using modern SAN with NVMe-oF, read my blog post, “[NVMe Storage: A Beginner’s Guide to Lightning-Fast Data Access](https://www.lightbitslabs.com/blog/nvme-storage-a-beginners-guide-to-lightning-fast-data-access/).”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/01/775818af-carolplatz.jpg)

Carol Platz brings over 25 years of technology evangelism and marketing leadership for high-performance data storage solutions to her role as vice president of marketing at Lightbits. Prior to joining the company, she directed marketing for storage startups like WekaIO,...

Read more from Carol Platz](https://thenewstack.io/author/carol-platz/)