**When building AI prototypes,** developers naturally want to get up and running as fast as possible. But move too fast, and those decisions can come back to haunt you if they lead you to make flippant decisions about data infrastructure.

For smaller, less-regulated startups building SaaS or internal applications, the consequences may not be as dire. Wherever you start building, you can usually keep running there even when applications move into production.

But for large-scale enterprises operating in highly regulated environments — think healthcare, finance, government — some developer-friendly database platforms simply can’t meet the security, compliance, deployment, availability, and reliability requirements that emerge when it’s time to [shift into production](https://thenewstack.io/ai-prototype-to-production-postgres).

Yes, you can re-platform. But it’ll cost you in redevelopment work, labor, and operational overhead. Choosing a database that can support both prototyping and production from Day 1 could let you skip those headaches altogether.

## The cost of choosing a database you’ll outgrow

Moving an application from one database platform to another as developers move prototypes into production may not seem like a particularly arduous transaction. After all, since nothing’s in production yet, there’s no real risk of downtime. That changes for teams that don’t discover the mismatch until after launch.

But the risks lie elsewhere, largely in wasted time and money — and they usually don’t reveal themselves until it’s too late to change course cheaply.

When asked what happens when enterprises prototype on developer-friendly platforms without production-ready security, compliance, and deployment flexibility, [Phillip Merrick](https://www.linkedin.com/in/phillipmerrick/), co-founder and CEO of [pgEdge](https://www.pgedge.com/), tells *The New Stack* they may be looking at significant, costly rework:

“You’ve got to look at retargeting the whole application to a new compliant platform, where it can run on-premises in a tightly managed cloud environment. And that’s going to require some amount of rework.”

> “Choose the wrong platform, and you are going to incur additional costs.”

Besides the direct cost of technical work — which can get particularly gnarly if the application relies on proprietary capabilities from the original platform — Merrick cautions enterprises about the additional operational and administrative burdens of moving to and managing a new environment, including a second procurement cycle that few may plan for. It also takes time and resources to establish the necessary [agentic operations strategy](https://thenewstack.io/why-most-ai-projects-fail-its-infrastructure-and-people/).

Bottom line, he doesn’t see any way around the added expense: “Choose the wrong platform, and you are going to incur additional costs.”

---

**More pgEdge coverage in *The New Stack*:**

---

## Why teams don’t realize the problem until it’s too late

Many enterprises are drawn to fast, developer-friendly platforms because they’re snappy, easy to use, and often support agentic AI applications. That’s understandable.

But Merrick tells *The New Stack* that too many developers default to these platforms without considering whether they match their enterprise’s specific production requirements — for example, whether they offer deployment choice. Security by default? High availability?

In the end, that can leave a prototype stuck on infrastructure that just can’t support production in highly regulated industries. That’s because the prototyping platform and the production platform are often two different products, built by different teams for different buyers, not two tiers of the same thing. That’s because the prototyping platform and the production platform are often two different products, built by different teams for different buyers, not two tiers of the same thing.

> “If you prototyped in an environment that doesn’t match up with your enterprise production requirements, then you have no choice but to re-platform.”

Being able to deploy in a tightly controlled cloud environment or on-premises, meet strict security and compliance requirements, and count on 99.99% uptime may not be an immediate priority for a small startup or less-regulated company. Still, it’s non-negotiable for many large enterprises.

“If you prototyped in an environment that doesn’t match up with your enterprise production requirements, then you have no choice but to re-platform,” explains Merrick.

From where he sits, that infrastructure mismatch likely plays an outsized role in why so many generative AI and agentic prototypes never make it into production or, when they do, only produce scant business value. And at this point, the tale of underwhelming AI returns is an old line: [MIT NANDA](https://www.artificialintelligence-news.com/wp-content/uploads/2025/08/ai_report_2025.pdf) reports 95% of organizations are getting “zero return” on Generative AI investments. At the same time, [IDC](https://www.lenovo.com/content/dam/lenovo/iso/iso-channel-marketing/campaigns/bg-campaigns/fy26/hybrid-ai-advantage-with-nvidia/EN/to-channel/ebook/final-file/HybridAI_with_NVIDIA_To-Channel_eBook_English.pdf?refId=bddcd9e7-4486-45af-85b2-0ce22cb6a4ea&) research with Lenovo says that for every 33 AI proofs-of-concept developed, only four make it into production.

## What a database built for both stages looks like

While data infrastructure missteps aren’t solely responsible for AI projects failing to reach production, choosing the right database from Day 1 can remove one obstacle.

Per Merrick, that means finding a platform that does away with the longstanding trade-off between developer speed and enterprise requirements:

“If you’re an enterprise developer, there has been a trade-off: ‘If I want developer speed, am I willing to relax my enterprise requirements for this prototype, knowing that I’m going to have to incur the cost later to re-platform the [application] into my production environment?’”

Specifically, he says such a database platform needs enterprise-grade controls, deployment flexibility, high availability, and scalability — all on the same underlying platform.

> “It’s the comfort of knowing that it’s the same. If your application behaves one way on [the] cloud, it’s going to behave exactly the same way in your cloud or on-premises.”

That consistency is the kicker, as Merrick says it’s what gives developers the ability to move between environments without having to take on excessive rework. As he explains to *The New Stack*: “It’s the comfort of knowing that it’s the same. If your application behaves one way on [the] cloud, it’s going to behave exactly the same way in your cloud or on-premises.”

## It’s possible to scale without re-platforming

pgEdge aims to give developers that continuity with pgEdge Starfleet, a new Postgres cloud database platform designed to bridge the gap between AI prototypes and production.

Merrick describes it to *The New Stack* as “the only 100% [Postgres](https://thenewstack.io/postgres-ai-ground-truth) platform that combines a smooth developer experience and the AI tooling that developers want with the security, compliance, scalability, reliability, and deployment flexibility that the enterprise demands.”

He also claims any developer can use it to get a database up and running in under two minutes, using the free 14-day trial to start building immediately and then deploy into different environments as production needs evolve.

For smaller teams without strict requirements for deployment location or enterprise controls, that may simply mean going into production on pgEdge’s managed cloud, where developers can scale up instance sizes as needed.

But what Merrick stresses as most important for larger enterprises is Starfleet’s ability to support other deployment models: “If, for your production environment, it needs to be your cloud, you can very easily migrate from Starfleet managed to Starfleet BYO Cloud.”

There’s also the option for on-premises deployment via a simple migration to pgEdge Enterprise Postgres, the company’s self-hosted option. “But it’s the very same Postgres platform you’re running on Starfleet,” he points out. “So it is not a re-platform. You’re just moving to a different underlying infrastructure. It’s the same Postgres on top.”

This, he argues, is an important distinction, as some competing platforms use either only modified Postgres or Postgres-compatible databases. In contrast, pgEdge Starfleet allows developers to keep 100% standard Postgres across environments.

In BYO Cloud and on-premises deployments, Merrick adds that developers can go one step further to [multi-master, multi-region Postgres](https://thenewstack.io/scaling-ai-inference-at-the-edge-with-distributed-postgresql) for high availability and true zero-downtime maintenance, which he previously told *The New Stack* is [the solution to the cloud’s high-availability problem](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/).

“So starting with a free trial and then a credit card and going all the way up to globally distributed, multi-region, multi-active Postgres clusters,” he says, “that is a scaling path that nobody else can deliver.”

## And you can keep developer speed, too

Meeting enterprise requirements for deployment, security, and availability can come at the expense of developer convenience during prototyping. But Merrick believes developers shouldn’t have to accept this tradeoff.

“You can have that developer speed. You can have those enterprise requirements. Bingo, that’s what pgEdge Starfleet is all about,” he says.

One way the platform supports speed is by providing tools to reduce the work developers need to do themselves. The [pgEdge Agentic AI Toolkit](https://www.pgedge.com/products/agentic-ai-postgres), which includes an MCP server, a RAG API server, and the [pgEdge Vectorizer](https://github.com/pgEdge/pgedge-vectorizer) extension, connects coding agents to Postgres, supports RAG applications, and automatically creates and maintains vector embeddings.

The other advantage Merrick points to is true copy-on-write database branching.

“As a developer, you are going to want to have the ability to work against a copy of your production data,” Merrick tells *The New Stack*, whether that be to support parallel agentic AI experiments or tackle production debugging.

By creating a logical copy of the whole database and only writing new data when changes are made, copy-on-write branching means developers don’t have to duplicate the existing database for every experiment. This way, developers can spin up isolated database branches for testing or debugging without exposing sensitive data, dealing with long copy times, or consuming excessive disk storage.

“Copy-on-write branching is incredibly powerful. Most Postgres vendors do not implement it,” says Merrick.

To be fair, he adds that Neon popularized the approach years ago. But he also tells *The New Stack* that doing so required completely rewriting the Postgres storage engine, thereby making the resulting platform no longer 100% standard Postgres.

And thus, we are back to the original trade-off: Do developers have to choose between developer speed and production-grade infrastructure?

Merrick says no: “Our innovation is being able to deliver copy-on-write database branching without having to change Postgres at all.” Xata, another Postgres platform, also markets copy-on-write branching on unmodified Postgres.

For developers, it looks like having the best of both worlds.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)