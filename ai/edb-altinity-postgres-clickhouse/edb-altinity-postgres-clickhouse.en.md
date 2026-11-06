**If you have built anything that needs both a system of record and fast analytics**, you know the shape of the problem. Postgres® holds the orders, the accounts, the state your application cannot afford to get wrong. ClickHouse software answers the questions.

A row store tuned for transactions was never built to answer at speed: what happened across a billion events in the last hour, which cohort is churning, what the agent should do next. Both engines are excellent at their jobs. The misery lives entirely in the gap between them.

> “Both engines are excellent at their jobs. The misery lives entirely in the gap between them.”

EnterpriseDB (EDB) has [acquired](https://www.enterprisedb.com/announces/altinity?utm_source=paid_media&utm_medium=press_release&utm_campaign=altinity_announcement) Altinity, the independent company behind Altinity Stable Builds, the Altinity Kubernetes Operator, and Altinity.Cloud.

The headline is corporate. The reason a developer should care is narrower: [The #1 contributor to Postgres](https://www.enterprisedb.com/company/postgres-vitality-index) and the [people who have run ClickHouse software](https://altinity.com/clickhouse-contributions/) in production for nearly a decade now work on one roadmap, and that roadmap is aimed at three pains you live with every week.

## **Pain 1: The CDC job is the product nobody asked for**

Count the moving parts between a committed Postgres transaction and the same row being queryable in ClickHouse software. A replication slot. A connector with its own failure modes. A message broker you size, secure, and patch. A sink that must survive schema changes without silently dropping columns. A dedup strategy, because at-least-once delivery means duplicates.

Monitoring on every hop, because lag in any one of them turns a “real-time” dashboard into a lie. None of that code is your product. All of it is on your on-call rota, and it is the reason the page comes at 3 a.m.

## **Pain 2: Your agent is reasoning over last night’s data**

Agentic workloads changed the economics of staleness. A dashboard 20 minutes behind is annoying. An agent that approves a refund, reprices inventory, or flags a transaction on a 20-minute-old aggregate is wrong, and wrong at machine speed, thousands of times before anyone notices.

> “An agent that approves a refund, reprices inventory, or flags a transaction on a 20-minute-old aggregate is wrong, and wrong at machine speed…”

So developers building agents write the same awkward code: Query Postgres for current state, query ClickHouse software for the trend, stitch the two in the application, and hope the clocks agree. You have become the integration layer, and the integration layer is where the bugs live.

## **Pain 3: You run the stack twice**

Every row-level rule, masked column, and “analysts see aggregates, not customer IDs” policy exists once in Postgres and again in ClickHouse software, and the two drift the first time someone updates one and forgets the other. Operating ClickHouse software on Kubernetes is its own job: Keeper, storage classes, replica placement, backups, upgrades, and one or two engineers who have quietly become “the ClickHouse people.”

And if you took the shortcut of a managed analytics service, your data lives where the vendor says and your bill scales with their pricing model, not with your infrastructure. Two engines, two permission models, two operators, two support contracts, and a lock-in you did not choose.

Read against those three pains, the deal starts to make sense: Each one maps to a pillar of what EDB and Altinity now plan to build together.

## **Pillar 1: One shared layer, not a pipeline**

Today, Postgres, [WarehousePG](https://www.enterprisedb.com/products/warehouse-analytics?_gl=1*bjtjqb*_up*MQ..*_ga*OTMzMTUwODQyLjE3OTM0MDI2NjE.*_ga_ND3EP1ME7G*czE3OTM0MDI2NjEkbzEkZzAkdDE3OTM0MDI2NjEkajYwJGwwJGgxMzI5MjI2NTI0) (EDB’s MPP warehouse), and ClickHouse software can read the same Apache Iceberg tables and query each other. Postgres writes the record and ClickHouse software reads it through the same open table format, with less data movement and integration effort between them. What is planned is one shared catalog and one governance model across all three engines, and one sovereign control plane for Postgres and ClickHouse software.

The organizing architecture is Iceberg as the shared layer today, with EDB’s control plane to follow as the shared operation. Treat the shared catalog as what is being built, not what you can download today. But the design goal is the one you would set yourself: fewer hops, one catalog, no bespoke reconciliation code. The CDC job is meant to stop being something you own.

## **Pillar 2: Live data for agents, governed where it lives**

EDB Postgres AI pairs a sovereign [multi-model data layer](https://www.enterprisedb.com/press-releases/edb-named-leader-multimodel-data-platforms-evaluation) with an agentic runtime and governance enforced in Postgres at the data layer—at the point of action and with an audit trail. For an agent, the goal is that it asks for business context and gets the record and the analysis from one system, rather than your code orchestrating two databases and a queue.

For permissions, one governance model across all three engines is part of the plan. Today, Postgres enforces purpose-bound access for agents, and ClickHouse software enforces its own role-based access. The plan is to define the policy once, where the data lives, and let every engine enforce it instead of re-implementing it in application code or a second permission model. That allows your agents to reason over what is true now without the security review blocking your release.

## **Pillar 3: The operators, the experts, and the choice of where it runs**

Altinity’s answer to running ClickHouse software in production has been the [Kubernetes Operator](https://altinity.com/kubernetes-operator/), with more than 100 million pulls, and Altinity Stable Builds maintained for three years with security and bug-fix backports. That knowledge now sits inside the #1 contributor to Postgres, which also created CloudNativePG and donated it to the open source community, where it is now a CNCF project and the Postgres operator many teams already run. One vendor understands both operators.

The plan is one sovereign control plane that runs Postgres and ClickHouse software, with one support organization behind it on the night they interact badly. Where it runs is yours to decide: bring-your-own-cloud, self-hosted on your own Kubernetes or OpenShift, air-gapped, or fully managed. Altinity.Cloud already deploys into customers’ own cloud accounts, and EDB Postgres AI runs in your own account or on-premises. So if your regulator, your CFO, or your latency budget says the data stays here, the stack follows you rather than the other way round.

## **The one answer**

Three pains, three pillars, one conclusion: The application layer should stop being the place where two databases are reconciled. Postgres keeps the record. ClickHouse software answers the hard questions on the same live data. Everything you delete from the middle is code you no longer debug, monitor, or explain to an auditor.

> “The best pipeline is the one you never have to write.”

The best pipeline is the one you never have to write. For developers who have spent years keeping two databases in agreement by hand and explaining the drift to auditors, product managers, and themselves, that is the promise worth watching. And it is the first thing to test as each planned piece lands.

---

**The software and services described in this announcement are provided by EDB and Altinity, not ClickHouse, Inc. This announcement does not imply sponsorship or endorsement by ClickHouse, Inc. Altinity is an independent company and is not affiliated with ClickHouse, Inc. ClickHouse is a registered trademark of ClickHouse, Inc.* [*clickhouse.com*](https://clickhouse.com/)*.**

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/11/ecb294e7-cropped-b37d8550-suit_max.png.webp)

Max Romanenko is a technology executive with deep expertise in cloud infrastructure, artificial intelligence, and enterprise SaaS platforms. He leads development across transactional, analytical, and AI database technologies at EDB, and shapes the company's hardware and security strategy. Before joining...

Read more from Max Romanenko](https://thenewstack.io/author/max-romanenko/)