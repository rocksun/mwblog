Valkey 9.1 is now generally available with a focus on improved efficiency, modularity, and ecosystem tooling for production workloads.

At [Open Source Summit North America](https://events.linuxfoundation.org/open-source-summit-north-america/) this week in Minneapolis, one of Valkey’s maintainers and AWS Principal Engineer [Madelyn Olson](https://www.linkedin.com/in/madelyn-olson-valkey/) will announce the general availability of Valkey 9.1. This comes along with new versions of  [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") Admin, Valkey Search, and the Valkey GLIDE client.

This latest version of Valkey, the [popular open-source fork](https://thenewstack.io/valkey-is-a-different-kind-of-fork/) of the [Redis](https://redis.io/) key-value program, is intended for organizations that need “fast, reliable data access without ballooning infrastructure costs” in production environments, Olson says. Developed by a “diverse community of leading technology providers,” the release emphasizes compute efficiency and architectural modularity as key to long-term sustainability in distributed systems.

Olson continues, “Our goal as a project is to ensure that Valkey delivers new functionality while behaving very predictably. Specifically, we want to sustain our best-in-class performance and efficiency. We’re able to consistently achieve this by continually investing in the modularity of the engine, which enables new functionality like full-text search.”

> “…reducing per-key memory usage by up to 10% for common workloads – no tuning, no reconfiguration required.”

## Lower memory, no tuning

At the core of Valkey 9.1 is a reworked internal data layout that lowers memory consumption out of the box. According to Olson, the new version “reworks how it stores and manages data internally, reducing per-key memory usage by up to 10% for common workloads – no tuning, no reconfiguration required.” For cloud-scale deployments, the team pitches this as a direct lever on infrastructure spend, allowing operators to run the same workloads on fewer or smaller instances.

Olson admits these improvements aren’t as exciting as the ones in the earlier 8.x and 9.0 releases. That’s because the Valkey developers were pushing out pent-up feature work into the engine that Redis hadn’t allowed them to release.

## Database-level ACLs arrive

In addition, security changes in 9.1 are designed to tighten protections while minimizing operational burden. The release adds “automated TLS certificate reloading and a new database-level ACL system, providing fine-grained multi-tenant isolation within a single instance.” The database-level ACLs are intended to allow operators to carve up a single Valkey deployment into multiple tenants or applications, with more precise access control.

The project frames these features as a way to “take pressure off developers and add a layer of reassurance that regardless of deployment size and type, Valkey will remain stable and secure.” Olson has also described some of this work as part of a broader push toward “provenance guard” security functions, where AI-assisted tooling helps monitor for anomalies and bugs across the codebase.

Responding to operator requests, Valkey 9.1 introduces a new capability called CLUSTERSCAN. This feature “enables consistent key scanning across an entire cluster, a boon for cluster operators” who need predictable iteration over data without resorting to ad hoc scripts or per-node scans. The project says operators “can expect more consistent performance under heavy load, centering Valkey as a database engine of choice for latency-sensitive, high-throughput applications.”

## Search joins the engine

While Valkey has long been known as a cache and in-memory data store, this release cycle marks the consolidation of search directly into the same system. The Valkey Search module, now at version 1.2, provides “full-text search, numeric filtering, tag-based lookup, and AI-ready vector search into the same system as the data store.” Valkey describes this as a way to “consolidate caching and search behind one system,” eliminating the need to run and operate a separate search platform.

With Valkey Search, “businesses can scale to terabytes of data while maintaining microsecond latency and up to millions of requests per second” for use cases such as search, e-commerce sites, and real-time dashboards and leaderboards. Organizations “no longer need to provision or maintain a separate search platform” because “caching and search run together in a single, highly-performant system, reducing both operational overhead and total cost.”

Olson highlights these combined capabilities as particularly relevant to “the agentic AI space,” where developers “want to have some amount of hybrid searching” that mixes deterministic full-text queries with approximate vector search. In her words, the modular search stack is “primarily useful for” scenarios where teams “want to do some part of the search deterministically with full text, and then some of it approximately with” vector similarity.

Alongside the 9.1 engine release, the Valkey community is shipping Valkey Admin as a generally available tool for cluster operators. First previewed at the [Unlocked conference](https://www.unlockedconf.io/) earlier this year, Valkey Admin is described as “an open source visual cluster management tool” designed to give teams “a real-time view of their Valkey deployment, including cluster topology, per-node performance, and a key browser for inspection.”

On the client side, the open-source Valkey GLIDE library has reached version 2.4, with new features focused on caching and language coverage. The project says GLIDE “introduced support for client-side caching and transparent caching” and “expanded its language support to include C# and PHP,” bringing what it calls “Valkey’s production-grade, Valkey-native client experience to two of the most important enterprise and web application ecosystems.”

GLIDE is described as “an official open source client library for Valkey, built on a shared Rust core that delivers consistent, reliable behavior across multiple programming languages.” It “comes pre-configured with best practices and handles cluster topology, connection management, and request routing automatically so developers don’t have to.” With client-side caching, “applications can now serve frequently accessed data directly from local memory, eliminating redundant network round-trips and reducing server load in read-heavy workloads where the same keys are fetched thousands of times per second.”

For teams building distributed systems, the project claims that GLIDE means “fewer incidents, faster recovery, and a client library that reduces cross-zone and cross-region data transfer costs.” In The New Stack interview, Olson emphasizes that GLIDE’s Rust core underpins a growing set of bindings, saying the team has “finally finished all the languages, including C#, PHP, Java, JavaScript, Python, Go,” and others, and that they feel the client is really GA ready and widely usable.”

## AI agents fight burnout

In her keynote scheduled for Wednesday, Olson plans to showcase how Valkey’s own development process is integrating AI agents. The talk will “outline how AI agents are being used to combat maintainer burnout by automating tedious, time-intensive tasks now” across two main domains: “provenance guard” security functions and “complex backporting and Continuous Integration (CI) testing across the project.”

In her interview, Olson explains that the project uses AI-based agents to scan the codebase, attempt to trigger crashes, and surface bugs, noting that one such effort “found, you know, 20 or so odd bugs, a CVE” after running for “hundreds of hours.” She said the team has also “built a bunch of infrastructure to automate backporting,” with AI agents attempting backports, running the test suite, and iterating until they achieve a clean build, thereby “trying to reduce our effort side” while maintaining human review over core engine changes.-

Olson stressed that for the Valkey core, “we really want to scrutinize kind of the code going in,” describing AI as “another layer of verification” and “great” for quickly generating experimental code. She also adds we’re “trying our best to make sure that, like, the project is still being primarily driven by the maintainers, and then using AI as much as possible to help them, not necessarily replace them.”

That all sounds grand, but are people buying what Valkey is selling? According to Olson, the answer is a strong yes. Olson cites “about 6 million container pulls a week these days” for Valkey compared to “like 24 25 from Redis.” That may not sound that impressive, but it represents “about 17x the weekly pulls from this time last year.”

She described the curve as “very exponential” but noted that they are “kind of past that exponential” phase as they approach saturation among organizations considering the project. Olson said “lots of big enterprises are moving” and that at the Unlocked conference, they heard from “folks like Apple and Uber” about their experiences with Valkey, adding that adoption is “still going well” and that “people still like talking about how easy it is” to migrate.

> “We don’t think Redis is gonna die.”

The project continues to position itself as a long-term peer rather than merely a replacement for Redis. “We don’t think Redis is gonna die,” Olson said, emphasizing that Redis has “such a legacy, such a name,” and that the Valkey community wants to “make sure that we’re competing with them and helping to encourage them to open source more stuff.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)