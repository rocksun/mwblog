If you know P99 CONF, you likely can’t wait for P99 CONF 2025. It will be premiering on your browser Oct. 22 and 23 with an agenda featuring lots of new speakers as well as some longtime favorites.

If you’re not yet familiar with P99 CONF, it’s a free two-day community event on performance and low latency engineering. It’s intentionally virtual, highly interactive and deeply technical. This year, you can look forward to first-hand engineering experiences from the likes of Clickhouse, Gemini, Arm, NVIDIA, Pinterest, Rivian/Volkswagen, Meta, Wayfair, Disney, Turso, Neon, PlanetScale, ScyllaDB and too many others to list here.

With P99 CONF 2025 just days away (more on that later), we thought it was a good time to share some of the most talked-about sessions from P99 CONF 2024. You can also binge-watch more than 200 low-latency tech talks (free, ungated) in the [on-demand library](https://www.p99conf.io/on-demand/).

*[Register for P99 CONF, free and virtual](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000Xo0mc&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202025-10-22%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack)*

## Patterns of Low Latency

**Pekka Enberg (Co-founder and CTO at Turso)**

Pekka Enberg begins his talk with a haunting thought: “Latency lurks everywhere.” But fortunately for viewers, Enberg has thought obsessively about latency from both the database engineer perspective and the “[Latency” book](https://lp.scylladb.com/latency-book-offer) author perspective. That’s probably why Enberg can provide an extremely comprehensive overview of how to find, measure and eliminate latency in a mere 30 minutes.

Enberg starts with a look at why latency matters, why tail latency has a greater impact than most people think and why average latencies are essentially meaningless. The trap of coordinated omission gets a special callout here, building on what Gil Tene presented in a past P99 CONF keynote, “[Misery Metrics & Consequences](https://thenewstack.io/if-p99-latency-is-bs-whats-the-alternative/)”.

Next, Enberg shares three ways to eliminate latency: avoid data movement, avoid work and avoid waiting. Moving bytes inevitably takes time, so co-location, replication or caching can help. Doing less is often the biggest win. Choose the right algorithms, avoid dynamic memory allocation in the hot path and don’t let heavyweight synchronization or the operating system impede your progress. Even something as small as a context switch can hurt tail latencies.

If you can’t reduce latency any further, it’s time to hide it. Enberg walks through practical strategies like parallelizing request processing, hedging requests across servers and using lightweight threads. He closes with a reminder that system tuning matters too: Things like CPU scaling, swap and interrupt handling can make or break your latency. The bottom line message: Measure the tail, attack it from every angle and make [low latency](https://thenewstack.io/high-performance-on-a-low-budget/) a first-class design goal.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## Get Low (Latency)

**Benjamin Cane (Distinguished Engineer at American Express) and Tyler Wedin (vice president, Global Payments Network site reliability engineer at American Express)**

The American Express Payments Network team recently completed a four-year project to revamp the company’s card payments platform. The system had to be fast enough to handle massive amounts of globally distributed transactions with low latency and extreme resiliency. It also needed to be flexible enough so the team could rapidly pivot based on the payments industry’s frequently changing needs.

Cane and Wedin walk through the challenges introduced by breaking the previously monolithic system into distributed services: Added network hops, cross-region delays, dependency on stateful devices and the countless “paper cuts” that erode performance and availability.

They addressed the bottlenecks with a cell-based architecture, data locality and HTTP/2–based service-to-service communication. Each cell was autonomous, with its own Kubernetes cluster, data and supporting services. This way, transactions could be processed locally without cross-region hops. Data was distributed using three approaches (in order of preference): Preloaded read-through cache for static values, replication for eventual consistency and transaction affinity when strong consistency was required. Service calls moved to HTTP/2 with a service mesh (Envoy) to balance load, and reliance on stateful devices was reduced by using direct, secure pod-to-pod communication.

The main lesson learned? In Cane’s words: “To get low latency, you have to focus on locality: taking the most direct path. To get low latency, you have to limit your dependencies. Push data to your cells or nodes ahead of time so it’s there when the transaction needs it. You also need to use asynchronous communication instead of synchronous. Most importantly, you have to make latency and resiliency first-class features of your platform. That’s what we did from the start. We defined SLAs [service-level agreements], set targets lower than those SLAs and made this a core part of the platform. If latency wasn’t where it needed to be, we stopped the development train and fixed it.”

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## 1 Billion Row Challenge in Golang

**Shraddha Agrawal, senior software engineer at Ceph, IBM**

How fast can Go really go? That’s what Shraddha Agrawal was trying to discover with her approach to the [1 Billion Row Challenge (1BRC)](https://www.morling.dev/blog/one-billion-row-challenge/). In case you missed it last year, 1BRC was intended to be a fun exploration of how far modern Java can be pushed for aggregating 1billion rows from a text file. But its creator, Gunnar Morling, also expected it “to be interesting to a dozen or so folks.” Ultimately, hundreds of people implemented the challenge in Go, Rust, C/C++, C#, Fortran, even databases – so this project exceeded expectations in every way.

Bonus: Morling also delivered a P99 CONF 2024 keynote [sharing tricks that the fastest 1BRC solutions](https://www.p99conf.io/session/1brc-nerd-sniping-the-java-community/) used to process the challenge’s 13 GB input file in less than two seconds.

Starting from a naive zero-concurrency baseline implementation, Agrawal measured a six-minute runtime for parsing and aggregating the data. From there, she used Go [performance tools to guide each optimization step](https://thenewstack.io/optimize-database-performance-by-capitalizing-on-the-cpu/). Introducing concurrency by spawning ~10,000 goroutines (one per city) cut time to about 4.5 minutes, but it also exposed channel and scheduler overhead. Switching from unbuffered to buffered channels, batching lines and rethinking data structures provided incremental improvements. And she cut both time and memory costs by replacing floating-point arithmetic with integer arithmetic and storing only min/max/sum/count instead of full-value lists.

A lean MapReduce-style design shaved off more seconds. The file was read in 64 MB chunks, parsed in parallel by nine worker goroutines, and merged into summarized maps by a reducer. With one producer feeding them, that meant just 10 goroutines in total. This reduced channel traffic from 10 million items to 512 and cut execution time to 28 seconds.

In the video, Agrawal walks you through the complete journey step by step, with lots of flame graphs, tooling tips and lessons learned along the way.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## Zero-Overhead Container Networking With eBPF and Netkit

**Liz Rice, chief open source officer at Isolvant (now part of Cisco)**

Running applications inside containers can add a surprising level of networking overhead. Benchmarks on 100-gigabit Ethernet show that applications running directly on the host achieve near-wire speed. However, once they’re containerized, throughput drops to about two-thirds. That’s what perpetual P99 CONF favorite Liz Rice tackled in her P99 CONF 2024 talk.

Rice traced the throughput drop to two main causes. First, packets cross the network stack twice. Second, TCP back pressure lets socket buffer limits slip and that causes packet loss as well as throttled throughput.

From there, she showed how eBPF can bypass the host’s upper networking stack. Helper functions added in Linux 5.10 (`bpf_redirect_peer` and `bpf_redirect_neigh`) can more efficiently redirect packets between namespaces. This brings throughput closer to native host performance: around 90 gigabits in her benchmarks. Additional improvements come with TCX, a rework of how eBPF programs are attached in the networking stack.

Rice’s next step was netkit devices, introduced in Linux 6.6. These minimal, BPF-programmable devices replace virtual Ethernet connections and eliminate backlog queuing. They also allow packets to be redirected in the context of the application thread. This pays off in both throughput and latency: Containerized applications match the networking performance of running directly on the host.

Finally, Rice shows that these advances are already integrated into Cilium, making zero-overhead container networking accessible on recent kernels.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## Next in the Sordid DB/OS Love/Hate Relationship

**Andy Pavlo, associate professor at Carnegie Mellon University**

The speaker provided a rather colorful and comprehensive abstract for this talk. We didn’t think our take could do it justice — so here you go, just as Pavlo put it.

“Database management systems (DBMSs) are beautiful, free-spirited software that want nothing more than to help users store and access data as quickly as possible. To achieve this goal, DBMSs have spent decades trying to avoid operating systems (OSes) at all costs. Such avoidance is necessary because OSs always try to impose their will on DBMSs and stifle their ambitions through disingenuous syscall semantics, unscalable kernel-level data structures, and excessive data copying.

“The many attempts to avoid the OS through kernel-bypass methods or custom hardware have such high engineering/R&D costs that few DBMSs support them. In the end, DBMSs are stuck in an abusive relationship: they need the OS to run their software and provide them with basic functionalities (e.g., memory allocation), but they do not like how the OS treats them. However, new technologies like eBPF, which allow DBMSs to run custom code safely inside the OS kernel to override its functionality, are poised to upend this power struggle.

“In this talk, I present a new design approach called ‘user-bypass’ for building high-performance database systems and services with eBPF. I discuss recent developments in eBPF relevant to the DBMS community and what parts of a DBMS are most amenable to using it. And I present the design of BPF-DB, an embedded DBMS written in eBPF that provides ACID transactions over multi-versioned data and runs entirely in the Linux kernel.”

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## Join the Community for P99 CONF 2025

Just like the P99 CONF community, the P99 CONF team can’t stop optimizing and tuning. And that brings us to P99 CONF 2025. Here’s a peek at what’s on the agenda:

* Alexey Milovidov: “Clickhouse’s C++ & Rust Journey”
* Chip Huyen: “LLM Inference Optimization”
* Sanchay Javeria: “Building Pinterest Streaming Apps with Apache Flink”
* Saahil Khurana, Marcus Kim: “Rivian’s Push Notification Sub Stream with Mega Filter”
* Cristian Velazquez: “Memory Optimization Techniques That Kept Uber’s P99 Under 1ms”
* Geoffrey Blake: “Finding Performance Needles in Haystacks with APerf”
* Tanel Poder: “Efficient, Always-On Thread Level Observability with eBPF”
* Glauber Costa: “Why We’re [Rewriting SQLite](https://thenewstack.io/why-we-created-turso-a-rust-based-rewrite-of-sqlite/) in Rust”
* AJ. Stuyvenberg: “How We Rebuilt the Datadog Lambda Extension in Rust”
* Christian Schwarz: “Reworking the Neon IO stack: Rust+tokio+io\_uring+O\_DIRECT”

If you’re intrigued by these talks — and more technical discussions on AI/ML, distributed data systems, Kubernetes and observability — join us for loads of learning and technical fun.

*[Register for P99 CONF, free and virtual.](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000Xo0mc&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202025-10-22%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack)*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/01/14adf317-cynthiadunlop.jpeg)

Cynthia Dunlop has been writing about software development and testing for much longer than she cares to admit. She's currently senior director of content strategy at ScyllaDB.

Read more from Cynthia Dunlop](https://thenewstack.io/author/cynthiadunlop/)