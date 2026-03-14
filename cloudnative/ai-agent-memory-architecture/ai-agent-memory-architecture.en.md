When you look at how top engineering teams actually build agent memory systems, a pattern emerges: There is a filesystem interface for what agents see and database storage for what persists. The debate was never “filesystem or database;” it was always both, in the right layers.

The idea that filesystems make good agent interfaces isn’t new. Dust.tt was projecting company data into [synthetic filesystems in mid-2025](https://dust.tt/blog/how-we-taught-ai-agents-to-navigate-company-data-like-a-filesystem). Letta’s memory benchmarks showed [filesystem tools outperforming alternatives](https://www.letta.com/blog/benchmarking-ai-agent-memory). LangChain’s [context engineering work](https://blog.langchain.com/how-agents-can-use-filesystems-for-context-engineering/) laid the groundwork.

But in January 2026, the conversation intensified. Vercel published [some evaluations](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash). Harrison Chase shared how [LangSmith Agent Builder implements memory](https://x.com/hwchase17/status/2011814697889316930). Jerry Liu declared, [“Files Are All You Need.” “FUSE is All You Need”](https://www.llamaindex.ai/blog/files-are-all-you-need) hit Hacker News. Anthropic’s Skills feature, which [packages agent capabilities as folders of markdown files](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), quietly reinforced the same pattern.

> “The debate was never ‘filesystem or database;’ it was always both, in the right layers.”

Why the renewed attention? Coding agents like Cursor, Claude Code, and Windsurf have demonstrated that filesystem interfaces work remarkably well — at least for code. The question is whether that success generalizes.

The appeal is understandable. A capable agent might need to interact with REST APIs, SQL databases, vector stores, cloud consoles, file systems, web browsers, and human users—each with different protocols and conventions. That’s a lot of interfaces to juggle.

But when you look at how these teams actually build their systems, a different picture emerges. They’re using databases underneath—and they’re being remarkably transparent about why.

## What is the difference between the filesystem interface and filesystem storage?

Harrison Chase is transparent about LangSmith Agent Builder’s architecture in his post on X: Agents see a filesystem interface, but the actual storage is a database. As he explained in his [technical deep-dive on Agent Builder’s memory system](https://x.com/hwchase17/status/2011834318172422279):

“LLMs are great at working with filesystems, but from an infrastructure perspective, it is easier and more efficient to use a database.”

This isn’t a contradiction. It’s a deliberate architectural choice:

* **Interface** = What the agent sees and interacts with
* **Storage** = Where data actually persists

![Alt text: A two-panel diagram comparing "The Confusion" (Filesystem vs Database as competing choices) with "The Reality" (Agent Access and Data Persistence as independent layers—Interface chosen per use case, Storage as unified backend).](https://cdn.thenewstack.io/media/2026/03/e538e45d-mongodb-article-slide-1.png)

The debate isn’t “filesystem or database”—it’s recognizing that interface and storage are independent decisions.

These are independent decisions. Once you recognize this distinction, the question shifts from “filesystem or database?” to “what interface for what agent type, backed by what storage for what requirements?”

---

## What does a filesystem interface actually provide for AI agents?

Before [MCP](https://thenewstack.io/when-is-mcp-actually-worth-it/) and filesystem abstractions, connecting an agent to external data meant defining custom tool schemas for every data source. Each endpoint needs documentation. Each schema needs examples. As Tony Powell of Arize [observes](https://arize.com/blog/agent-interfaces-in-2026-filesystem-vs-api-vs-database-what-actually-works/): “By the time the LLM is taught how to use a particular API, you’ve gobbled up a bunch of your context window… You’re spending thousands of tokens on education instead of reasoning.”

Filesystem interface offers a different approach: a small set of universal operations that LLMs already understand from their training data. This is the old Unix [“everything is a file” philosophy from the 1970s](https://arxiv.org/html/2601.11672v1), just reappearing at a new scale. As Unix collapsed diverse device interfaces into file operations, and DevOps collapsed infrastructure into code artifacts, agentic AI is collapsing diverse data sources into filesystem operations.

The core operations:

* **List** — Show contents of a location (like ls)
* **Read** — Get contents of a file (like cat)
* **Write** — Create or update a file
* **Search** — Find files by name or content (like find and grep)

The practical benefit is token efficiency: the education already happened during pretraining. As Pekka Enberg of Turso noted in his [post on AgentFS](https://penberg.org/blog/disaggregated-agentfs.html): “Give an agent access to grep, sed, awk, cat, and git, and it becomes unreasonably capable and effective, requiring no custom tools.”

Dust.tt extended this by creating “[synthetic filesystems](https://dust.tt/blog/how-we-taught-ai-agents-to-navigate-company-data-like-a-filesystem)” — projecting APIs and databases into filesystem-like hierarchies. Slack channels become directories. Notion workspaces become folders. The underlying data lives in APIs and databases, but the agent sees a coherent file tree.

![Table comparing the evolution of AI agent data interfaces—Custom Tools, MCP, and Filesystem Interface—highlighting how universal filesystem operations require zero education tokens compared to custom schemas.](https://cdn.thenewstack.io/media/2026/03/c4d52158-table-screenshot-file-systems-vs-databases-2.jpg)

How agent-to-data interfaces have evolved from custom tools to standardized filesystem operations.

---

## Where does the filesystem interface work well for AI agents?

The filesystem pattern has demonstrated clear value for **coding agents**.

This shouldn’t be surprising. Code is already organized as files in directories. Developers think in filesystem terms. Operations map naturally: read a file, edit a file, search the codebase. Tools like Cursor, Claude Code, and Windsurf all use this pattern.

The Letta team provided important context in their [benchmarking analysis](https://www.letta.com/blog/benchmarking-ai-agent-memory): “Agents today are extremely effective at using filesystem tools, largely due to post-training optimization for agentic coding tasks.” The key phrase is “agentic coding tasks”—this is where the training data exists.

**Where the filesystem interface fits well:**

* Coding agents (code is already in files)
* Document processing (docs map to files)
* DevOps and infrastructure (configs are files)
* Knowledge base navigation (hierarchies work)

## Where does the filesystem interface break down for AI agents?

The filesystem pattern isn’t universal. Several contexts expose its limitations, and practitioners who’ve tried it have been candid about the failures.

### Structured data queries

You can’t grep your way through “find all customers who ordered product X but not product Y in Q3.” For queries involving joins, aggregations, or graph traversal, filesystem operations are awkward.

[Vercel’s benchmarks](https://vercel.com/blog/testing-if-bash-is-all-you-need) make this point clearly. When they tested filesystem operations against database queries for structured data:

![Benchmark table comparing AI agent approaches, showing that database queries achieve 100 percent accuracy with significantly lower token usage, cost, and duration compared to Bash and Filesystem methods.](https://cdn.thenewstack.io/media/2026/03/0c8c6dbf-table-screenshot-file-systems-vs-databases.jpg)

The takeaway: For structured data with clear schemas, purpose-built query languages — whether SQL, MongoDB’s query API, or other database interfaces — consistently outperform filesystem operations.

### Performance at scale

The filesystem abstraction hides a critical problem: Each file operation can become an API call. One practitioner on Hacker News [describes abandoning the approach entirely](https://news.ycombinator.com/item?id=46582331): “If you grep (via fuse) you will end up opening lots of files which will result in fetches to some API, and it will be slow… We went as far as implementing this idea in Rust to really test it out, and ultimately it was ditched because, well, it sucks.”

Jerry Liu of LlamaIndex makes a similar observation in “[Files Are All You Need](https://www.llamaindex.ai/blog/files-are-all-you-need)“: “Coding agents are already using CLI tools as their primary means for file search, but we’ve noted that this approach doesn’t scale to massive document collections (1k-1m+).”

The issue is fundamental: Filesystems lack the indexing that makes database queries fast.

### Serverless and cloud-native environments

The filesystem metaphor assumes a filesystem, but many production environments — such as serverless functions, browser-based agents, and edge computing — don’t have persistent local storage.

### Non-coding agent types

Customer service agents need structured customer data. Analytics agents need database queries. The training-data advantage that makes the filesystem interface powerful for coding agents may not carry over to these domains.

## Why are leading teams using database storage for agent memory?

Regardless of which interface pattern you choose, the leading teams have converged on database storage underneath:

![Table illustrating how leading AI teams like LangChain, Dust.tt, Turso, and Letta use different filesystem interface layers while uniformly relying on underlying database storage layers for agent memory.](https://cdn.thenewstack.io/media/2026/03/c1977922-table-screenshot-file-systems-vs-databases-3.jpg)

**The reasons are consistent:**

* **Multi-agent coordination** requires transactions. When multiple agents share state, you need ACID guarantees.
* **Scale** demands indexing. Grep works for small collections; production systems need database-level query optimization.
* **Governance** requires audit trails. Enterprise deployments need traceability on who accessed what, when, and why.
* **Hybrid retrieval** is table stakes. Production systems [need vector search](https://thenewstack.io/why-developers-need-vector-search/), full-text search, and structured queries working together.

Document databases with integrated vector search are particularly well-suited here. A platform that combines flexible document storage, vector embeddings, and full-text search eliminates the need to stitch together multiple systems.

## How should developers choose the interface and storage for agent memory?

The filesystem interface [isn’t the only option](https://www.mongodb.com/docs/atlas/atlas-vector-search/ai-agents/). And for some agent types, it’s not the best one.

Document databases like MongoDB Atlas store data as JSON documents, which are already “file-like” in structure. With [native vector search](https://www.mongodb.com/products/platform/atlas-vector-search), full-text search, and [aggregation pipelines](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/) built in, agents can query directly via [MCP tools](https://www.mongodb.com/docs/mcp-server/get-started/) or API—no filesystem translation layer needed. For analytics agents, customer service agents, or any workflow involving structured data queries, this direct path may outperform the filesystem interface.

The filesystem interface shines when the agent’s training data makes ls and grep more reliable than custom tools, primarily coding agents. But that training-data advantage doesn’t carry over to every domain.

[DIAGRAM 3: The Decoupled Architecture]

![A three-layer architecture diagram showing an Agent at the top connecting to an Interface Layer (with Filesystem, MCP Tools, and Direct API options), which connects to a Storage Layer (Document DB + Vector Search + Full-Text + ACID)](https://cdn.thenewstack.io/media/2026/03/56f78fd1-mongodb-article-slide-2.png)

The emerging architecture decouples interface and storage choices, allowing teams to optimize each layer independently.

**The real questions to ask:**

* **What agent type?** Coding, document, analytics, customer service?
* **What interface fits that type?** Filesystem for coding agents, MCP/direct queries for structured data.
* **What storage requirements?** Scale, multi-agent coordination, governance, retrieval patterns?
* **Do you need a translation layer?** Or can the agent query the database directly?

## The architecture is converging. Here’s what it means for developers

The “filesystem vs. database” framing obscures more than it reveals. The teams building production agent systems have already moved past this debate. They’ve separated the interface from storage, and they’re using databases underneath regardless of which interface they expose to agents.

> “Structured data, non-coding workflows, and serverless environments need different approaches.”

Filesystem interface works well for coding agents and document navigation, where training data exists, and the metaphor fits. But it’s not universal. Structured data, non-coding workflows, and serverless environments need different approaches.

The question was never “filesystem or database?” It was [always both—in the right layers](https://www.mongodb.com/company/blog/technical/converged-datastore-for-agentic-ai).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/03/01adfe08-cropped-631dbe2c-mikiko-bazeley.png)

Mikiko Bazeley serves as a Staff Developer Advocate focused on Agentic Systems and Applied AI, positioning MongoDB as the core memory, state, and coordination layer for next-generation intelligent applications.

Read more from Mikiko Bazeley](https://thenewstack.io/author/mikiko-bazeley/)