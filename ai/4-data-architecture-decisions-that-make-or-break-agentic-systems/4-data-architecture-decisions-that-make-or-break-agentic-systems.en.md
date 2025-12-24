Data teams that thrived in the last wave of Software as a Service (SaaS) platform scale weren’t the ones that chased hype. They were the ones that made a few smart decisions: They adopted cloud-first operations, made cost and capacity visible, and chose architectures that could quickly adapt to changing conditions.

As it turns out, those are exactly the same practices the [agentic era](https://thenewstack.io/agentic-ai-is-the-new-web-app-and-your-ai-strategy-must-evolve/) now demands.

If you look at how data teams are managing their [AI transition](https://thenewstack.io/embracing-ais-transformation-transitioning-from-a-software-developer-to-a-builder/), a clear pattern emerges: The ones with firm control over performance and spend had the easiest time supporting agents. They were already practicing tenant isolation. They were already making online changes during business hours. They were already using [object-storage](https://thenewstack.io/why-ai-loves-object-storage/)-backed recovery. Everything agents required from them, they were already doing. They simply applied the same principles they were already practicing to a new kind of user.

Let’s start from that premise: that agents are your new users. We’ll take a look at what makes them different from other users and how best to support them. Along the way, we’ll discuss four architectural factors that affect the [ability to operate at scale](https://thenewstack.io/scaling-ai-agents-in-the-enterprise-the-hard-problems-and-how-to-solve-them/). And we’ll close with a checklist you can use to evaluate the suitability of your current platform for agent-driven workloads.

## Agents Are Your New ‘Users’

Most data platforms were built for humans and services with relatively stable, predictable demands. Agentic systems are quite different. They spin up short-lived apps, run experiments, trigger migrations, branch off new datasets and tear it all down — often in parallel, and unpredictably.

We’ve seen this firsthand with companies like [Manus](https://www.pingcap.com/case-study/manus-agentic-ai-database-tidb/). It offers a general-purpose agentic AI platform whose “wide research” agent swarms spin up thousands of short-lived workloads every day. It’s no longer managing a single monolithic database, but instead orchestrating millions of tiny, temporary branch-like environments behind the scenes.

At scale, what agents need isn’t a monolithic, ever-growing database. It’s effectively millions of tiny, isolated databases or branches popping in and out of existence. Once you accept that premise, four requirements for agentic architectures naturally follow:

* **Isolation by default:** Per-tenant or per-agent boundaries keep experiments from becoming everybody’s problem.
* **Online change during business hours:** Schemas and indexes must be adjustable within p95/p99 latencies inside service-level objectives (SLOs).
* **Placement and quotas:** Hot data needs to be kept near low-latency compute; cold data can be kept in cheap storage; and noisy tenants need to be isolated.
* **Life cycle automation:** You need the ability to create and retire environments in seconds with clean metadata hygiene and cost attribution.

Here are four architectural choices that support your agentic users’ needs.

## 1. The 2 Separations That Matter for Scalability

Agents can quickly devour shared resources. To keep that from happening, separate compute from storage so you can add query capacity without shifting data. Then separate compute from compute to give online transaction processing (OLTP), analytics and maintenance their own lanes and SLOs.

### Separate Compute From Storage

Attaching stateless SQL/compute engines to durable, shared object storage lets you:

* **Scale elastically:** Adding and removing query capacity without the need for high-wire data copies or weekend migrations.
* **Recover predictably:** New nodes can pull state from storage and warm caches and start serving without saturating peers.
* **Clone quickly:** Copy-on-write branches can be built quickly from metadata rather than complete physical copies.

What to verify:

* Can you add compute nodes in minutes without rebalancing data?
* Do new nodes draw from object storage rather than peers?
* Are cloning and branching incremental and space-efficient?

### Separate Compute from Compute

When thousands of agents are branching data, building indexes and sending queries at the same time, SQL frontends, analytical readers, background maintenance (compaction, backfills), backup/restore and control planes need to be scaled — and governed — independently, to keep them running smoothly.

What to verify:

* Can you rate-limit backfills independently of OLTP traffic?
* Do analytical scans have their own resources and guardrails?
* Can you execute version upgrades for one plane without taking a window on another?

## 2. Make Cost Visible (And Actionable)

Traditional data platforms often idle at 20% to 25% CPU while maintaining extra headroom “just in case.” That’s survivable with human users; it’s untenable in an environment where agents are spinning up thousands of short-lived workloads. The fix is to make the cost per query visible — for example, through request-unit (RU) accounting — in the same pane engineers already watch.

That way, engineers know which queries to optimize and what savings to expect. Product and finance can set budgets and caps that map to real work, and platform teams can recommend improvements based on actual spend, not gut feel.

What to verify:

* Can you attribute costs to tenants, apps and query digests?
* Can you enforce budgets and caps automatically?
* Do you have a “Top Five Digests” loop tied to latency and cost regression tests?

## 3. Treat Object Storage as the Backbone

For agentic architectures, using object storage (S3/Google Cloud Storage/Azure Blob) for the data backbone is not optional. It enables context-aware scaling by pulling data from a shared object store and caching hot data locally for ultra-low latency, ensuring the database is always the right size for the moment. During scale-out or recovery, new compute should pull state from durable storage rather than copying from peers. Backups and long-term snapshots should live there, too.

Benefits:

* **Predictable scale and recovery:** Less cross-node thrash during growth or failover.
* **Tiered economics:** Hot/warm/cold paths you can reason about and budget for.
* **Fast database branching:** Database clones become pointer operations plus object-store semantics.

What to verify:

* Are backups, snapshots and branch metadata stored in object storage by default?
* How long does it take for a new node to start serving traffic after a failure?
* Can you garbage-collect abandoned branches and objects automatically?

## 4. Treat Online Change as a First-Class Capability

When agents are your users, change is constant. Schema evolution, indexing, data movement and upgrades must happen online, with clear visibility into what is happening.

Here’s what that looks like in practice:

* Three-phase schema changes (prepare → reorganize → commit) with multiversion concurrency control so reads/writes continue while backfills run.
* Rate-limited maintenance that respects p95/p99 budgets.
* Rolling upgrades with automatic leader election and no maintenance windows.

What to verify:

* Can you add an index to a hot table at peak and hold p95/p99 inside the SLO?
* Are metadata locks short and predictable?
* Do you have preflight checks, abort thresholds and a rollback plan baked into the pipeline?

## Anti-Patterns To Avoid

So that’s what you should try to do. Here are some things to avoid.

* **Sharding complexity:** App-level sharding looks simple until you own routing, rebalancing, failover and cross-shard joins forever.
* **One big pool:** Treating all compute as fungible leads to noisy-neighbor incidents and tail-latency spikes.
* **Invisible spend:** Billing at the instance level hides per-query waste; remember, you can’t manage what you can’t see.
* **Peer copy dependency:** Recovery and scale-out processes that depend on busy neighbors are vulnerable to collapsing under pressure.

## A Minimal Evaluation Checklist

Use the following checklist to compare platforms for agentic workloads:

1. **Database provisioning:** How many isolated databases, schemas and branches can you create per minute? How are they tracked and retired?
2. **Two separations:** Check compute/storage independence and compute/compute independence under live load.
3. **Cost model:** How well can engineers monitor per-query cost by tenant/app? What caps exist and how are they enforced?
4. **Object storage:** Demonstrate node join and recovery that draws from object storage. Measure time to service.
5. **Online change:** Test the ability to add an index during peak; check p95/p99, error rates and abort thresholds.
6. **Failure drill:** Kill a leader or availability zone (AZ); watch election, client retries and tail latency.
7. **Metadata hygiene:** Prove that abandoned branches and objects get garbage collected without manual tickets.

Agentic systems don’t require a brand new approach to infrastructure. The right architecture for agents is the right architecture for any large-scale modern use case. But agents are a forcing function.

Data teams don’t have the luxury of sticking with monolithic platforms that are slow to scale and hard to manage. Agents will bring those old architectures to their knees. But as the most successful data teams have found, if you design for flexibility, visibility and performance using the methods described above, you’ll ship faster with fewer weekend fire drills, even when your “users” number in the millions — and most of them aren’t human.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/6a7f3a53-cropped-bc64a625-max-liu.png)

Max Liu is the co-founder and CEO of TiDB, powered by PingCAP. He has more than 10 years of experience in system infrastructure and software technologies. He is the co-author of the following open source projects: TiDB, TiKV and Codis,...](https://thenewstack.io/author/max-liu/)