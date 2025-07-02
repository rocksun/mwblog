Probability is the branch of mathematics that deals with uncertainty. It helps us understand the likelihood of different outcomes occurring. Below, we consider two alternative architecture options for scaling a database horizontally and employ probability theory to show that one architecture is more reliable than the other by a factor of 60,000.

## Horizontal Database Scaling Architecture Options

### Application-Level Sharding

[Application-level sharding](https://thenewstack.io/acid-compliant-distributed-sql-enters-the-agentic-ai-era/) uses domain-specific knowledge to [partition data](https://thenewstack.io/databases-what-to-know-about-partitioning/) into multiple database instances running on multiple servers. Each database instance is isolated, enabling workloads to be scaled. This architecture requires custom logic for routing, rebalancing and handling cross-shard operations.

### Distributed SQL

[Distributed SQL](https://thenewstack.io/distributedsql-takes-databases-to-the-next-level/) provides a single logical database that horizontally scales across multiple servers with built-in replication and quorum-based logic to implement global [ACID](https://www.yugabyte.com/acid/) transactions. Additional servers can be added and integrated into the system, enabling workloads to be scaled. Automatic routing, rebalancing and handling of cross-shard operations simplifies development and speeds up time to market.

For this comparison, we assume both architectures run on Google Cloud Platform using VMs hosted as part of the Compute Engine service. [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform provides a monthly uptime service-level objective of 99.9% for a single VM/instance. We use this SLO in our system availability calculations.

## Architecture 1 — Application-Level Sharding

An application-sharded system partitions data across multiple servers that then operate semi-independently.

* Data is manually partitioned across servers — for instance, customers A–F on server 1, G–L on server 2, etc.
* Each server is responsible for only its slice of the data.
* The application must route queries to the correct server.
* If a server fails, its data becomes unavailable, even if the other servers are healthy.

### Availability of a 6-Node Application-Level Sharded System

#### We know that:

* The probability of a node being available, P(node is available) = 0.999.
* Nodes are independent of each other.
* The system needs all six nodes to be available.

In [probability theory](https://en.wikipedia.org/wiki/Probability_theory), independent events are events whose outcomes do not affect each other. For example, when throwing four dice, the number displayed on each dice is independent of the other three dice.

Similarly, the availability of each server in a six-node application-sharded cluster is independent of the others. This means that each server has an individual probability of being available or unavailable, and the failure of one server is not affected by the failure or otherwise of other servers in the cluster.

In reality, there may be shared resources or shared infrastructure that links the availability of one server to another. In mathematical terms, this means that the events are dependent. However, we consider the probability of these types of failures to be low, and therefore, we do not take them into account in this analysis.

Mathematically, if two events A and B are independent, then the probability of both A and B happening together is the product of their individual probabilities:

[![](https://cdn.thenewstack.io/media/2025/07/441f0eaf-2.png)](https://cdn.thenewstack.io/media/2025/07/441f0eaf-2.png)For a six-node database cluster, this would mean:

[![](https://cdn.thenewstack.io/media/2025/07/0ae1ea43-2c.png)](https://cdn.thenewstack.io/media/2025/07/0ae1ea43-2c.png) The six-node sharded architecture, therefore, supports an SLO of 99.4%, which is notably lower than the SLO of the underlying VMs.

## Architecture 2 — Distributed SQL

A distributed SQL database automatically shards the data of a single logical database across multiple servers. Additionally, for resilience, it maintains replicas for each shard and typically uses a quorum-based algorithm to coordinate updates, ensuring strong consistency for reads and writes.

* Each shard of data is replicated across multiple nodes, with one replica designated as the leader.
* A quorum (majority) is required to write data (e.g., 2 of 3 if the replication factor is 3).
* Quorum is also required for reads, which is elegantly achieved by routing the request to the leader, avoiding the need to issue a read to all three replicas and wait for a majority to respond.
* Data is not tied to a single node.
* The system can tolerate node failures and still serve requests.

### Availability of a Six-Node Replication Factor Three Distributed SQL Cluster

Each node manages one or more shards of data. Each shard is in a quorum group, with its data replicated on two other nodes. To protect against availability zone (AZ) outages as well as individual node failures, the cluster is typically distributed across three availability zones, and the data distribution algorithm ensures that replicas of a shard are always placed in different availability zones.

In probability theory, the binomial distribution models the number of expected outcomes during a series of trials or tests.

We can use the binomial distribution to calculate the probability of k servers being available in a cluster of n servers:

[![](https://cdn.thenewstack.io/media/2025/07/de5908b2-3.png)](https://cdn.thenewstack.io/media/2025/07/de5908b2-3.png)

#### We know that:

* P(node is available) = 0.999.
* Nodes are independent of each other.
* The nodes are evenly placed across three availability zones.

* There are many quorum groups spread across the servers.
* The raft groups are organized such that replicas are always in separate availability zones.
* If one node is lost, only one copy of the data is affected, so the cluster remains available.
* If two nodes are lost, so long as they are in the same AZ, only one copy of the data is affected, so the cluster remains available. This further increases availability, but we have not included these calculations for simplicity.
* If three or more nodes are lost, two or more copies of the data are affected, and the cluster would be unavailable.

So, the six-node system is available if:

* All six nodes are up.
* Exactly five nodes are up.

[![](https://cdn.thenewstack.io/media/2025/07/044affff-3a.png)](https://cdn.thenewstack.io/media/2025/07/044affff-3a.png)

This means:

[![](https://cdn.thenewstack.io/media/2025/07/dd8db32b-5.png)](https://cdn.thenewstack.io/media/2025/07/dd8db32b-5.png)

The six-node replication factor (RF) three-quorum-based architecture supports an SLO of 99.998%, notably higher than the SLO of the underlying VMs.

### Availability of a 10-Node Replication Factor 5 Distributed SQL Cluster

To further increase resilience and protect against two simultaneous failures, distributed SQL can be configured to operate with a replication factor RF of five. With this architecture, each node manages one or more shards of data.

Each shard is in a quorum group, with its data replicated on four other nodes. To protect against availability zone (AZ) outages as well as individual node failures, the cluster is typically distributed across five availability zones, and the data distribution algorithm ensures that replicas of a shard are always placed in different availability zones.

#### We know that:

* P(node is available) = 0.999.
* Nodes are independent of each other.
* The nodes are evenly placed across five availability zones.
* There are many quorum groups spread across the servers.
* The raft groups are organized such that replicas are always in separate availability zones.
* If one node is lost, only one copy of the data is affected, so the cluster remains available.
* If two nodes are lost, only two copies of the data are affected, so the cluster remains available.
* If three or four nodes are lost, so long as they are in two or fewer AZs, only two copies of the data are affected, so the cluster remains available. This further increases availability, but we have not included these calculations for simplicity.
* If five or more nodes are lost, three or more copies of the data are affected, and the cluster would be unavailable.

[![](https://cdn.thenewstack.io/media/2025/07/ec2af497-6.png)](https://cdn.thenewstack.io/media/2025/07/ec2af497-6.png)

The 10-node RF5 quorum-based architecture supports a service-level objective of 99.99999%, which is significantly higher than the SLO of the RF3 cluster.

## Architectural Impact on Availability

Traditional architectures are limited by single-node failure risk. Application-level sharding compounds this problem because if any node goes down, its shard and therefore the total system becomes unavailable.

In contrast, distributed databases with quorum-based consensus (like [YugabyteDB](https://www.yugabyte.com/yugabytedb/)) provide fault tolerance and scalability, enabling higher resilience and improved availability.

|  |  |  |
| --- | --- | --- |
| **Architecture** | **Service Level Objective** | |
| **Single Node** | 99.9% | (Three 9s) |
| **6 Node Application-Level Sharding** | 99.4% | (Two 9s) |
| **6 Node RF3 Distributed SQL Cluster** | 99.99% | (Four 9s) |
| **10 Node RF5 Distributed SQL Cluster** | 99.99999% | (Seven 9s) |

The summary table above shows a far greater likelihood of failure using a six-node application-level sharding architecture than a 10-node RF 5 distributed SQL cluster. Specifically:

Likelihood of failure of six-node application sharded compared with 10-node RF5 =

[![](https://cdn.thenewstack.io/media/2025/07/46cb5f12-7.png)](https://cdn.thenewstack.io/media/2025/07/46cb5f12-7.png)

## Does Resilience Matter?

Enterprises that deliver high-throughput, real-time transaction services, such as payment processors and anti-money laundering solutions, are critically dependent on the resilience of their infrastructure.

Every minute of downtime is lost revenue. It erodes trust and potentially causes churn. A platform handling 10,000 transactions per second at $50 each with a 2% fee would lose $600,000 of revenue per minute, just in fees.

Resilience matters. Well-documented processes and runbooks activated during a failure scenario are not enough. Operational resilience for critical services requires resilient, self-healing architectures like distributed SQL.

## Conclusion

Traditional architectures, particularly those using single-node or application-level sharding, are prone to failure and offer limited availability. Distributed SQL databases with quorum-based replication provide significantly higher availability, fault tolerance and resilience.

The difference is not just technical but business-critical. Downtime can result in substantial revenue loss, reputational damage and regulatory risk. As operational demands and regulatory expectations increase, adopting resilient, self-healing architectures is crucial for any enterprise that relies on high-throughput, real-time services.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/1a3386fd-cropped-08c40b34-chris-smith.jpg)

Yugabyte EMEA VP Chris Smith has a background in mathematics and has spent most of his career working with databases and data management platforms in roles spanning software engineering and go-to-market leadership. Before Yugabyte, Chris served as vice president of...

Read more from Chris Smith](https://thenewstack.io/author/chris-smith/)