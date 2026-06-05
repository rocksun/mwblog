Microsoft used its [Build 2026](https://news.microsoft.com/build-2026/) developer conference on Tuesday to note that the hard part of enterprise AI is no longer the model. It’s the data context. And the company is betting that [Microsoft Fabric](https://thenewstack.io/microsoft-fabric-goes-all-in-on-real-time-data-intelligence/) can solve it.

The announcements span three areas — a new database platform, a GPU-accelerated [data warehouse](https://thenewstack.io/data-warehouses-are-terrible-application-backends/), and a generally available semantic and ontology layer — each aimed at the same underlying problem: Agents that start from zero every time, with no shared understanding of how an organization works.

[Amir Netz](https://www.linkedin.com/in/amirnetz/), CTO of Microsoft Fabric, tells *The New Stack*, “There is a difference between an AI that we all use in our civilian lives and an AI that is being used in the enterprise.”

“The difference is that you want the AI to be like an employee of a company — an insider who knows how the machinery operates, what the goals are — rather than a stranger on the outside.”

Netz, a 30-year Microsoft veteran who has spent much of that time on [Power BI](https://thenewstack.io/power-bi-gets-low-code-datamart-feature/) and Fabric, positioned the entire platform around what he called the “context layer” — the organizational memory that agents need to reason reliably and act appropriately inside an enterprise.

## A new database for AI-scale workloads

The most significant infrastructure announcement is [Azure HorizonDB](https://azure.microsoft.com/en-us/products/horizondb), a fully managed [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/)-compatible database now entering public preview. Microsoft has long been a PostgreSQL committer, but HorizonDB represents a different order of scale: elastic storage up to 128 TB, compute scaling to 3,072 vCores, and sub-millisecond multi-zone commit latency for high-demand transactional workloads.

The database also ships with capabilities built for AI applications — [vector search](https://thenewstack.io/vector-search-is-reaching-its-limit-heres-what-comes-next/), integrated AI model management, and direct connectivity to [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) and Fabric. The idea is that developers building agent-powered applications shouldn’t have to stitch together separate systems for transactional data, search, and AI.

“What stood out with HorizonDB is that it aligns closely with how we already think about the problem,” says [Mohsin Shafqat](https://www.linkedin.com/in/mohsin-s-0453a17b/), Director of Software Engineering at NASDAQ, in a statement. “Instead of stitching together multiple components, it brings transactional data, vector search, and AI capabilities into a single platform, which simplifies the architecture without forcing a complete rethink.”

## GPU acceleration comes to the data warehouse

Microsoft is also bringing GPU acceleration to Fabric Data Warehouse, entering early access preview in July 2026. The company says it has integrated NVIDIA accelerated computing directly into the warehouse layer — no query rewrites required — and claims up to 7x faster performance than three unnamed cloud data warehouse competitors at 64-user concurrency in internal benchmarks conducted in May 2026.

The underlying research won the Best Industry Paper award at [ACM SIGMOD 2026](https://www.linkedin.com/company/acm-sigmod-2026/posts/?feedView=all).

Netz put the performance numbers in context: “In data warehousing, if you get 10 percent gain in a year, you open the champagne. With GPU acceleration, we are seeing anywhere from 5x to 100x.”

Customers already in preview are reporting real gains. UNC Health says it is seeing up to 5x improvement in query speeds, allowing teams to spend less time on performance management and more on generating insights.

[Ian Buck](https://www.linkedin.com/in/ian-buck-19201315/), Vice President of Hyperscale and HPC at Nvidia, notes that AI agents reasoning over enterprise data require low-latency performance across many simultaneous users — a workload profile for which GPU acceleration is well-suited.

## Fabric IQ goes GA, extends across the agent ecosystem

[Fabric IQ,](https://www.microsoft.com/en-us/microsoft-fabric/features/iq) Microsoft’s semantic and ontology layer for enterprise agents, is now generally available. It sits on top of Power BI’s semantic models — which Netz noted are used by roughly half a million organizations — and extends them with operational context: business entities, relationships, rules, real-time signals from Fabric Real-Time Intelligence, and the actions agents are permitted to take.

Operations agents, which continuously monitor live data and act on predefined business logic, are also now generally available. Ontologies within Fabric IQ are expected to reach general availability in the coming months.

Microsoft is integrating Fabric IQ broadly across its agent ecosystem. It is now accessible as a knowledge source in Microsoft Foundry, integrated as a first-party MCP tool with Microsoft Agent 365, and extended into Microsoft 365 Copilot — including Cowork and Copilot Chat — where it can ground agents in governed Power BI reports and semantic models. Agent Skills for Fabric also bring the same semantic context to GitHub Copilot CLI, letting developers query reports and semantic models directly from the terminal.

Two additional capabilities are reaching general availability: graph in Fabric, which models relationships between business entities and systems, and planning in Fabric, due later this month. Planning is notable because its outputs can be written back into Fabric, giving agents a closed-loop view of the business that spans past data in OneLake, real-time signals, and forward-looking forecasts.

Netz describes the combined effect in terms of temporal coverage: “We had the past. We had the present. The missing piece was the future — what is supposed to happen. Now the ontology can really cover all the tenses.”

## The platform story

Microsoft’s broader pitch at Build 2026 is that Fabric can serve as both the data foundation and the deployment target for enterprise AI — a unified platform that handles operational and analytical workloads — which Netz positioned against [Snowflake](https://thenewstack.io/snowflake-streamlines-data-analysis-for-enterprise-ai/) and [Databricks](https://thenewstack.io/databricks-brings-data-pipeline-service-to-ga/), which he characterizes as primarily analytical.

The argument is that agents that build and run applications need a single platform that can handle both, with shared context layered on top.

A new Database Hub in Fabric, currently in private preview, will enable centralized management of Microsoft’s database portfolio — HorizonDB, Azure Database for PostgreSQL, Azure Cosmos DB — with data mirrored to OneLake. Azure Cosmos DB also received Build announcements: Its Linux Emulator is now generally available, and new AI capabilities including semantic reranking and an agent memory toolkit are in preview. OpenAI, which chose Cosmos DB as its primary operational database, was cited as a reference customer.

Also announced at Build: [Rayfin, a new open-source SDK and CLI](https://thenewstack.io/microsoft-build-2026-rayfin-replit-vibe-coding/) that enables developers and coding agents to build enterprise-grade application backends and deploy them directly to Fabric, with a Replit partnership bringing vibe-coded apps into the platform.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)