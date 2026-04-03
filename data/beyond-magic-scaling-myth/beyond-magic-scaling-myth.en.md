*The following is an excerpt from the just-published second edition of* [Designing Data-Intensive Applications](https://learning.oreilly.com/library/view/-/9781098119058/)*, by Martin Kleppmann and Chris Riccomini. It is published here with permission from O’Reilly. For more background on the book (known as the bible of data systems) and its evolution*, *see this* [*conversation with the authors*](https://thenewstack.io/data-intensive-applications-rewrite-2026/)*. Also, you can access* [*three book chapters for free*](https://lp.scylladb.com/designing-data-intensive-apps-book-offer)*, courtesy of ScyllaDB.*

Even if a system is working reliably today, that doesn’t mean it will necessarily work reliably in the future. One common reason for degradation is increased load. Perhaps the system has grown from 10,000 concurrent users to 100,000 concurrent users, or from 1 million to 10 million. Perhaps it is processing much larger volumes of data than it did before.

Scalability is the term we use to describe a system’s ability to cope with increased load. Sometimes, when discussing scalability, people make comments along the lines of, “You’re not Google or Amazon. Stop worrying about scale and just use a [relational database.](https://thenewstack.io/when-your-relational-database-isnt-the-right-tool-anymore/)” Whether this maxim applies to you depends on the type of application you are building.

If you are building a new product that currently has only a small number of users, perhaps at a startup, the overriding engineering goal is usually to keep the system as simple and flexible as possible so that you can easily modify and adapt the features of your product as you learn more about customers’ needs [80]. In such an environment, it is counterproductive to worry about hypothetical scale that might be needed in the future. In the best case, investments in scalability are wasted effort and premature optimization; in the worst case, they lock you into an inflexible design and make it harder to evolve your application.

> “Scalability is not a one-dimensional label—it is meaningless to say ‘X is scalable’ or ‘Y doesn’t scale.'”

Scalability is not a one-dimensional label—it is meaningless to say “X is scalable” or “Y doesn’t scale.” Rather, discussing scalability means considering questions like these:

* If the system grows in a particular way, what are our options for coping with the growth?
* How can we add computing resources to handle the additional load?
* Based on current growth projections, when will we hit the limits of our current architecture?

If you succeed in making your application popular, and therefore are handling a growing amount of load, you will learn where your performance bottlenecks lie and along which dimensions you need to scale. At that point, it’s time to start worrying about techniques for scalability.

## Understanding load

First, you need a clear understanding of the current load on the system. Only then can you discuss growth questions (“What happens if our load doubles?”). Often this will be a measure of throughput—for example, the number of requests per second to a service, the number of gigabytes of new data arriving per day, or the number of shopping cart checkouts per hour. Sometimes you care about the peak of a variable quantity, such as the number of simultaneously online users in our social network case study.

Often other statistical characteristics of the load affect the access patterns and hence the scalability requirements. For example, you may need to know the ratio of reads to writes in a database, the hit rate on a cache, or the number of data items per user (followers, in our case study). Perhaps the average case is what matters for you, or perhaps your bottleneck is dominated by a small number of extreme cases. It all depends on the details of your particular application.

Once you understand the load on your system, you can investigate what happens when the load increases. You can look at this in two ways:

* When you increase the load in a certain way and keep the system resources (CPUs, memory, network bandwidth, etc.) unchanged, how is the performance of your system affected?
* When you increase the load in a certain way, how much do you need to increase the resources if you want to keep performance unchanged?

Usually the goal is to keep the performance of the system within the requirements of the SLA while also minimizing the cost of running the system. The greater the required computing resources, the higher the cost. Some types of hardware might be more cost-effective than others, and these factors may change over time as new types of hardware become available.

If doubling the resources will enable you to handle twice the load while keeping performance the same, we say that you have linear scalability, and this is considered a good thing. Occasionally it is possible to handle twice the load with less than double the resources, because of economies of scale or a better distribution of peak load [81, 82]. Much more likely is that the cost grows faster than linearly. There may be many reasons for the inefficiency; for example, if you have a lot of data, processing a single write request may involve more work than if you have a small amount of data, even if the size of the request is the same.

## Shared-memory, shared-disk, and shared-nothing architectures

The simplest way of increasing the hardware resources of a service is to move it to a more powerful machine. Individual CPU cores are no longer getting significantly faster, but you can buy a machine (or rent a cloud instance) with more CPU cores, more RAM, and more disk space. This approach is called vertical scaling or scaling up.

You can get parallelism on a single machine by using multiple processes or threads. All the threads belonging to the same process can access the same RAM, and hence this approach is also called a shared-memory architecture. The problem with a sharedmemory approach is that the cost grows faster than linearly; a high-end machine with twice the hardware resources of a lower-spec machine typically costs significantly more than twice as much. And because of bottlenecks, that machine is unlikely to actually be able to handle twice the load.

Another approach is the shared-disk architecture, which uses several machines with independent CPUs and RAM but stores data on an array of disks that is shared among the machines, which are connected via a fast network: network-attached storage (NAS) or a storage area network (SAN). This architecture has traditionally been used for on-premises data warehousing workloads, but contention and the overhead of locking limit the scalability of the shared-disk approach [83].

By contrast, the shared-nothing architecture [84] (also called horizontal scaling or scaling out) involves a distributed system with multiple nodes, each of which has its own CPUs, RAM, and disks. Any coordination between nodes is done at the software level, via a conventional network.

The advantages of this approach, which has gained popularity in recent years, are that it has the potential to scale linearly, it can use whatever hardware offers the best price/ performance ratio (especially in the cloud), it can more easily adjust its hardware resources as load increases or decreases, and it can achieve greater fault tolerance by distributing the system across multiple datacenters and regions. The downsides are that it requires [explicit sharding](https://thenewstack.io/sharded-vs-distributed-the-math-behind-resilience-and-high-availability/) and incurs all the complexity of distributed systems.

Some cloud native database systems use separate services for storage and transaction execution (see “Separation of storage and compute” on page 16), with multiple compute nodes sharing access to the same storage service. This model has some similarity to a shared-disk architecture, but it avoids the scalability problems of older systems. Instead of providing a filesystem (NAS) or block device (SAN) abstraction, the storage service offers a specialized API that is designed for the specific needs of the database [85].

## Principles for Scalability

The architecture of systems that operate at large scale is usually highly specific to the application. There is no such thing as a generic, one-size-fits-all scalable architecture (informally known as magic scaling sauce). For example, a system designed to handle 100,000 requests per second, each 1 kB in size, looks very different from a system designed for 3 requests per minute, each 2 GB in size—even though the two systems have the same data throughput (100 MB/second).

> “There is no such thing as a generic, one-size-fits-all scalable architecture (informally known as magic scaling sauce).”

Moreover, an architecture that is appropriate for one level of load is unlikely to cope with 10 times that load. If you are working on a fast-growing service, it is therefore probable that you will need to rethink your architecture on every order of magnitude load increase. As the needs of the application are likely to evolve, it is usually not worth planning future scaling needs more than one order of magnitude in advance. A good general principle for [scalability](https://thenewstack.io/beyond-the-code-the-real-work-of-scaling/) is to break a system into smaller components that can operate largely independently from one another. This is the underlying principle behind microservices, sharding, stream processing, and shared-nothing architectures. The challenge lies in knowing where to draw the line between things that should be together and things that should be apart.

Another good principle is not to make things more complicated than necessary. If a single-machine database will do the job, it’s probably preferable to a complicated distributed setup. Autoscaling systems (which automatically add or remove resources in response to demand) are cool, but if your load is fairly predictable, a manually scaled system may have fewer operational surprises. A system with 5 services is simpler than one with 50. Good architectures usually involve a pragmatic mixture of approaches.

*The above was an excerpt from the just-published second edition of [Designing Data-Intensive Applications](https://learning.oreilly.com/library/view/-/9781098119058/), by Martin Kleppmann and Chris Riccomini. It is published here with permission from O’Reilly. For more background on the book (known as the bible of data systems) and its evolution, see this* [*conversation with the authors*](https://thenewstack.io/data-intensive-applications-rewrite-2026/)*. Also, you can access* [*3 book chapters for free*](https://lp.scylladb.com/designing-data-intensive-apps-book-offer)*, courtesy of ScyllaDB.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.