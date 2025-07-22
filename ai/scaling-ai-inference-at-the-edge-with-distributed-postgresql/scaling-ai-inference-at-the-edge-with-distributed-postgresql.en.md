Whether it’s for training or for inference, data is the bedrock of AI applications. Today, inference workloads get the most buzz thanks to the explosion of interest in chatbots, but inference is also essential for real-time decision-making in Internet of Things (IoT) devices, mobile apps, smart sensors and more.

Powering modern AI workloads is no small feat, requiring ultra-low latency, [high availability](https://thenewstack.io/distributed-postgres-high-availability-for-mission-critical-apps/) and real-time data processing and synchronization. What’s already a tall order is made all the more challenging in distributed environments, where maintaining models across geographies requires seamless data replication and conflict resolution.

That’s where traditional, centralized cloud-based AI inference falls short.

Sending data to and from a centralized system consumes enormous amounts of bandwidth. It also introduces latency, slowing responses that impact everything from search to real-time analytics. In a distributed world, where compute and data are physically separated, centralized inference is a bottleneck. And for applications requiring immediate responses (e.g., autonomous vehicles, healthcare, utilities), even small delays matter.

But inference doesn’t have to be centralized. Many of these challenges can be solved by moving AI inference to [the edge](https://thenewstack.io/edge-computing/). By bringing both the model and compute closer to the data source and distributing AI workloads across your edge nodes, you can significantly reduce latency, improve data privacy, ease bandwidth costs and improve system efficiency.

There’s a catch, though: AI inference at the edge only works if the architecture underneath can support it.

## Architecting for Distributed Inference

[Antony Pegg](https://www.linkedin.com/in/antonypegg/), director of product management at [pgEdge](https://www.pgedge.com/), explained in an interview: “The whole point of the edge is, you’re distributing the workload to be as close as possible to where you need the work to be done. That means the compute itself needs to be moved there.”

You can’t run inference at the edge unless your data and write operations are there, too. That requires a shift from centralized architecture to a [multi-master active–active architecture](https://www.pgedge.com/solutions/benefit/multi-master).

Pegg explained the difference: “With the traditional architecture, you’ve got one node that accepts all the writes, and then you have copies that get the updates, but they’re only for reading — until the primary node goes wrong… and then one of the other two read-only nodes needs to be promoted to becoming the writing node and take over.”

Multi-master active–active is the opposite — “decentralized by design,” as Pegg calls it. Read and write operations can occur at any node, and changes are automatically replicated across the network — no single primary needed. This setup allows edge locations to read and write locally, ensuring data remains synchronized across all nodes, even amid connectivity issues.

In this way, multi-master active–active guarantees high availability, faster response times, and seamless data replication and synchronization — key ingredients for maintaining the integrity of AI models and their inferences.

Still, some organizations have reservations about ditching the centralized status quo for a distributed approach.

## Misconceptions Linger About Edge AI

Despite the clear benefits of moving AI inference to the edge with a multi-master active–active architecture, common misconceptions make some organizations hesitant to get on board:

### Misconception #1: Edge Hardware Can’t Handle AI Workloads

Some people think edge devices simply can’t handle the demands of AI workloads. Hardware requirements, in particular, seem to be the hang-up: “So many people still assume that edge hardware is just too weak [and doesn’t have] the ability to distribute updates to the underlying models themselves,” said Pegg.

But in reality, modern chips are already capable of running complex models efficiently, even in quantized or distilled versions — and Pegg said this shouldn’t be a surprise: “For decades, we’ve been on a geometric progression of increasing ability and miniaturization… it’s all about shrinking down for efficiency.”

### Misconception #2: Edge Inference Is Only for Low-Stakes Use Cases

Another outdated idea is that edge inference is only useful for low-stakes or niche use cases. Again, Pegg deftly dispelled this notion by pointing to real-world deployments: “It’s already being used for mission-critical systems, like healthcare, manufacturing, defense, autonomous vehicles. A lot of this stuff’s been in the works for, I can say, literally decades.”

One example: [Telecom providers](https://aws.amazon.com/blogs/industries/distributed-inference-with-collaborative-ai-agents-for-telco-powered-smart-x/?utm_source=chatgpt.com) are already using distributed inference with collaborative [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) across edge, regional and cloud layers to power real-time applications like network optimization and smart infrastructure monitoring.

### Misconception #3: You Still Need a Single Source of Truth

Perhaps the biggest mental roadblock to adopting AI inference at the edge is the persistent belief that you still need a single source of truth.

Pegg believes this is the hardest mindset to shake, as we’ve been taught to believe that the cloud means “we need a single source of truth. And the implementation pattern that comes from that is a single place to write everything.”

So far, he said, most organizations have come to accept the concept of distributed reading — but that’s only half the battle. Now, people need to grasp “that the writing and the actual compute have to be pushed away from the central architecture, which means your architecture needs to be modular and compact and replicable.”

And this is exactly what multi-master active–active architecture enables.

In fact, once teams move past the mental hurdle, the lack of a single source of truth becomes a benefit: “When you don’t have a single source of truth,” said Pegg, “you don’t have a single source of failure.”

Because every node is active, the system is fault-tolerant. If one region goes offline temporarily, the others continue operating; when the offline region comes back online, the other nodes can catch it up immediately, ensuring continuous data availability even during unexpected outages — a critical requirement for AI applications that need uninterrupted access to data for real-time processing and decision-making.

### Misconception #4: Compute Must Stay Centralized

Similar to the attachment to a single source of truth, many organizations are stuck on the idea that you need a centralized stack to do compute, whether that’s for training or inference.

Pegg insists this mindset needs to shift: “You need to separate the two [training and inference], and then re-architect your system to break up and distribute that inference — and then trust that that inference itself can coordinate from multiple locations to create the shared consistency.”

For Pegg, this isn’t a technical problem; it’s a trust problem: “These are all steps of trust and change that need to be overcome — to believe that it not only *can* be done, but believe it *already is* being done.”

## Why This Shift Matters Now

As is often the case with technology inflection points, it’s adapt now — or get left behind.

Teams that embrace distributed inference will pull ahead with lower latency, faster time to insights, higher reliability, lower cost, and greater data provenance and sovereignty.

In many ways, it all comes down to speed. As Pegg put it: “Speed is king. Anything you can do to cut down latency improves pretty much any metric you measure your business by.” For edge AI workloads, “The closer it is to you, the faster you can have it compute and give you the decision-making information you need right there and then.”

The same logic applies to cost. With centralized systems come massive bandwidth, hardware and cloud expenses — but edge inference keeps costs slim: “The less you have to send and the shorter you have to send [it], the cheaper your costs. And the smaller the hardware and the infrastructure you need to put in place to run it, the cheaper your costs.”

That’s not a small consideration. Over-budget cloud spend is an enduring problem for many organizations, with [84% struggling to manage it effectively](https://www.flexera.com/about-us/press-center/new-flexera-report-finds-84-percent-of-organizations-struggle-to-manage-cloud-spend). And with [McKinsey predicting compute demand will hit $7 trillion by 2030](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers) (largely driven by AI and bandwidth-intensive workloads), it’s never been more timely — or urgent — to rethink architecture.

Distributed inference also helps with data provenance and sovereignty. When you can segment which data stays local and which gets shared, it’s easier to comply with different regulations, like GDPR and the California Consumer Privacy Act (CCPA).

## Distributed PostgreSQL for AI at the Edge

The performance, speed and resilience advantages all make a strong case for moving AI inference to the edge — but only if the data layer can keep up.

That’s why many companies [using PostgreSQL](https://roadmap.sh/postgresql-dba) are turning to [distributed PostgreSQL](https://www.pgedge.com/solutions/benefit/ai-inference-at-the-edge) with a multi-master active–active architecture to reduce latency, ensure data consistency and eliminate single points of failure — and that’s where pgEdge stands out.

[Enquire AI](https://www.pgedge.com/solutions/benefit/ai-inference-at-the-edge) is one such example of a company putting the multi-master architecture in action.

Enquire AI is a digital expert network that integrates AI and human intelligence. Its international customer base means the company faces tough data residency and response time requirements — and high latency is a thorny challenge that contributes to excessive application response times and degrades the customer experience. Although the company was already using [AWS](https://aws.amazon.com/?utm_content=inline+mention) Relational Database Service (RDS), it opted to transition to pgEdge Cloud instead of AWS Aurora, deploying a two-node cluster in the US East and Mumbai regions. Now, with a distributed database set up across two regions, Enquire AI can count on [higher availability](https://www.pgedge.com/solutions/benefit/postgresql-high-availability), lower latency and easier data residency compliance.

[pgEdge delivers a distributed PostgreSQL architecture](https://www.pgedge.com/products/what-is-pgedge) purpose-built for the edge. Its multi-master active–active setup allows every node to handle reads and writes, replicating changes automatically across the network. That means no primary and no single point of failure — just consistent data.

For AI workloads, that data proximity is everything. “If you’re still centralizing the inference,” Pegg explained, “then you’ve halved the benefit.” While active–active replication ensures consistency, inference still needs data to act on. “Without that, you’re missing what the compute needs,” Pegg explained. By storing data locally, pgEdge allows AI systems to act on it immediately for inference or for decision-making. “Without us,” Pegg added, “you can’t really distribute the compute because the compute needs the data to go with it.”

According to Pegg, that multi-master active–active concept is what sets pgEdge apart. “We support the whole paradigm shift of it being distributed, miniaturized, shrunk down and made to run locally — and then having that shared truth distributed, fault-tolerant and low latency. Plus, we’re fully open source and fully standard PostgreSQL.”

That combination means quicker updates, lower latency, lower bandwidth costs and faster decision-making — the foundation for building scalable, intelligent systems at the edge.

[Learn more](https://www.pgedge.com/landing-pages/multi-master-whitepaper) about how a fully open, fully standard approach to multi-master distributed Postgres can solve high availability and low latency challenges for AI inference at the edge across industries.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.