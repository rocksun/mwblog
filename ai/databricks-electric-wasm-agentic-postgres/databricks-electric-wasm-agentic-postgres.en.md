Databricks on Tuesday [announced](https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes) that it’s acquiring Electric, the startup behind the WASM-based Postgres project PGlite and the Electric sync engine, as agentic applications change how developers use databases.

The Electric team will join Neon, the serverless Postgres company Databricks acquired for about $1 billion last year and the foundation of its [Lakebase](https://thenewstack.io/lakebase-is-databricks-fully-managed-postgres-database-for-the-ai-era/) database service.

The companies didn’t disclose the terms of the deal.

## What Databricks bought

[PGlite](https://pglite.dev/) is a complete Postgres database in WebAssembly (WASM). It runs in the browser, a Node.js process, or inside the kind of sandboxes agents use to execute code. It supports dynamic extension loading, including pgvector, the preferred Postgres vector extension.

According to the companies, PGlite has grown from 1 million to 13 million weekly downloads over the last year.

## The sync engine at the core of Electric

It’s the Electric sync engine that is core to Databrick’s interest in Electric, though. This engine keeps a central Postgres database that can then be synced in near real-time with browser tabs, mobile apps, or agents. As Databricks notes, this is the multiplayer model of Figma or Google Docs, but applied to Postgres and the agents that use it.

The Neon team, in [its own announcement](https://neon.com/blog/electric-joins-neon), notes that “complex problems like conflict resolution, partial replication, and reconnection logic make real-time sync difficult to build from scratch.” Hence why Databricks likely acquired Electric instead of trying to build this from scratch itself.

As for the future of Electric, the company’s founders James Arthur and Valter Balegas [write](https://electric.ax/blog/2026/08/11/electric-joining-databricks) that “everything we’ve previously open sourced stays open source.” This covers the sync engine, PGlite, Durable Streams, and TanStack DB.

What doesn’t survive the deal, however, is Electric’s hosted service. “Electric Cloud is winding down,” the founders. “Cloud users will need to self-host or move to another provider.”

The deal also extends a string of database acquisitions for Databricks that includes Neon itself and, more recently, the transactional processing startup [Mooncake](https://thenewstack.io/mooncake-brings-databricks-rich-transactional-processing/).

## A database that lives for 10 seconds

As the Databricks team argues, traditional non-agentic applications share one database among many clients, and that database is the most permanent piece of the stack. But agent workloads change this.

In a [recent post](https://www.databricks.com/blog/how-agentic-software-development-will-change-databases) on how agentic development changes databases, Databricks’ Ippokratis Pandis, Nikita Shamgunov, and Reynold Xin write that agents now create roughly four times more databases than human users do on Lakebase. They also stress that the average project now carries about 10 database branches, and that some projects run more than 500 branch iterations deep.

For some types of applications on Lakebase, the average database compute is now alive for under 10 seconds.

Agents, as it turns out, like to branch databases the way they branch code, a pattern Neon [built its architecture around](https://thenewstack.io/neon-branching-in-serverless-postgresql/).

In practice, a coding agent spins up a sandbox, instantiates PGlite inside it, builds and tests against the database, and then either throws the whole thing away or syncs the result with — in the Databricks context — a Lakebase branch. Because Lakebase [separates storage from compute](https://thenewstack.io/new-oltp-postgres-with-separate-compute-and-storage/) and keeps its data in Postgres page formats on object storage, creating that branch is a relatively cheap copy-on-write metadata operation.

“As coding agents drive the cost of creation to zero,” the Neon team writes, “the number of applications explodes, and most of them are small.” A database server, even a serverless one that scales to zero, imposes a floor on what the smallest viable app costs to run. “You can’t have an age of abundance if every app requires a fixed minimum of compute,” the post argues.

## ‘Two halves of the same idea’

It’s worth noting that PGlite didn’t start at Electric. Instead, it began as an experiment by Neon co-founder Stas Kelvich, who compiled Postgres to WASM to see whether it could run client-side. Electric picked the work up and turned it into a production project. “That repo became the basis of PGlite,” Arthur and Balegas write.

As Databricks’ announcement notes, this now “reunites two halves of the same idea.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)