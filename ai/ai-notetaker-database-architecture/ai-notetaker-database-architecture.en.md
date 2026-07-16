Imagine you just finished a two-hour meeting. You were wearing a small AI work companion that promised to capture the conversation, structure it, and let you ask questions about it later. Two hours after the meeting, you open the app and ask for the transcript. You wait. The spinner turns. The whole reason you bought the device was so you’d never have to remember a meeting again, and now the one thing it promised to do well — recall what was said — is the thing that’s making you wait.

This is the failure mode that fascinates me about AI hardware products, because it’s not a model problem. The transcription was perfect. The summarization was good. The thing that frayed was the part nobody markets: getting the right bytes off disk and onto the screen at the moment the user asks. That’s a data problem. And for a product whose entire promise is memory, a data problem is a product problem.

> “For a product whose entire promise is memory, a data problem is a product problem.”

I want to walk through a real version of this because the team that hit it, Plaud, makes the most popular AI notetaker on the market, and the architecture that broke is the architecture almost every team in this category starts with. It feels reasonable at launch. It becomes a liability at scale. And the reasons why are worth understanding before you ship, not after.

## First, what was built correctly

It would be easy to tell this story as “they made a mistake.” They didn’t. The original architecture was a sensible set of decisions, and I want to be precise about that before I dissect what went wrong, because the lesson is in the gap between “reasonable” and “right at scale,” not in anyone’s competence.

Plaud’s product generates two very different kinds of data per recording. There’s structured metadata: who recorded it, when, how long, what tags, what state the processing pipeline is in. And there’s the [unstructured payload](https://thenewstack.io/from-unstructured-data-to-rag-ready-with-docling/): the audio file and its transcript, which can run tens of megabytes per session. The team did the textbook thing. They put the structured metadata in MySQL, where relational queries and transactions are cheap, and they put the large objects in S3, where storage is cheap and effectively infinite.

If you’ve built systems, you’ve made this exact call. Object storage for blobs, a relational database for everything you need to query. It’s in every architecture diagram. It’s the default. And for a long stretch of the product’s life, it worked fine.

The problem is not that the decision was wrong. The problem is that it contained a hidden assumption: that the metadata and the content could live in separate systems because they would never need to be consistent with each other in real time. For most applications, that assumption holds. For a product whose core interaction is “give me back exactly what I recorded, right now,” it doesn’t. And the gap between those two worlds is where everything started to fail.

## The transcript sidecar

In my article on [RAG retrieval](https://thenewstack.io/rag-pipeline-hybrid-search/), I identified an anti-pattern I called the vector sidecar: the habit of standing up a separate vector database alongside your primary store, only to discover that the two systems can’t answer a single query together. The Plaud architecture is the same shape, applied to an AI hardware product. Call it the transcript sidecar.

The transcript sidecar is what you get whenever you split structured metadata from unstructured content across two systems with no shared transaction guarantee. The metadata says a recording exists, is complete, and is ready. The content lives elsewhere, reached via a separate call, with its own latency and failure modes. Nothing ties the two together. There is no transaction boundary that spans “the row that says this transcript is ready” and “the object that contains the transcript.”

This produces three distinct compounding problems.

* **Retrieval latency is not a network problem; it’s a data locality problem.** S3 is excellent object storage. It is not a database. When you make object storage the primary retrieval path for tens-of-megabytes payloads under concurrent load, you’re trading the consistency and latency guarantees of a database for the simplicity of a blob store. Under light load, the trade is invisible. Under heavy concurrent load, S3 retrieval latency and its variability become the user’s experience of your product.
* **Consistency gaps open between two systems that fail independently.** The MySQL row can indicate that a recording is ready a moment before the S3 object is durably reachable, or a replica can lag, causing the metadata a user sees and the content they fetch to disagree. With no shared transaction, the application layer inherits the job of papering over the gap, with retries, polling, and reconciliation logic that grows more elaborate every quarter.
* **The schema becomes immovable at exactly the wrong time.** More on this below, but the short version is that the metadata store hit a scale ceiling where changing the schema required a maintenance window. For a product still evolving its feature set, that’s a database governing the roadmap, rather than the other way around.

The unifying insight is the one I keep coming back to throughout this whole series: any time you split data across systems that can fail independently, you have handed the consistency problem to the application layer, where it is not solved so much as managed, and where it compounds over time.

## When the database governs the roadmap

The most interesting failure in the [Plaud story](https://www.pingcap.com/case-study/how-plaud-eliminated-s3-latency-limitless-scale/) isn’t the latency. It’s the schema freeze, because it’s the one that teams least expect and feel most acutely.

With around 300 million rows, the team’s MySQL setup reached a point where schema changes such as adding a column or changing an index — the routine evolution of any growing product — could no longer be performed online without risk. DDL operations on a table that large, on that architecture, meant locking, replication strain, and the real possibility of downtime. So changes had to be batched into maintenance windows.

Sit with what that means. A maintenance window for a schema change is the time the database allows the product team to ship. The roadmap now bends around the database’s limitations. A feature that needs a new column will wait until the next window. The product’s cadence is set by the operational fragility of the data layer. Most teams don’t notice this inversion because it happens gradually, and then one day a product manager asks why a small change is a two-week project, and the answer is “the database.”

> “A maintenance window for a schema change is the time the database allows the product team to ship. The roadmap now bends around the database’s limitations.”

The 300-million-row ceiling is a forcing function that teams hit later than they expect and *should* hit later than they do. Expect, because single-instance MySQL feels limitless right up until it doesn’t. Should, because the architecture that gets you to 300 million rows is rarely the architecture that takes you past it, and the migration is far more disruptive at 300 million rows than it would have been at 30 million. The ceiling is real; it is predictable, and most teams plan for it only after they’ve hit it.

## What changing the architecture actually fixed

Plaud’s resolution was to consolidate the metadata layer into a distributed SQL database (they moved to [TiDB](https://www.tidb.io)), which removed the single-instance ceiling and restored online schema changes. I’m going to use their numbers, but not as a product pitch. I want them as evidence for a claim about where architectural debt goes in a product like this.

|  |  |
| --- | --- |
| **Before (dual-store-brain at scale)** | **After (consolidated metadata layer)** |
| Throughput strained under concurrent load | ~10x QPS headroom |
| Tail latency variable under load | P95 under 10 ms |
| Schema changes require maintenance windows | Online DDL, no downtime |
| Single-instance ceiling at hundreds of millions of rows | Horizontal scale across multiple clusters |

*Figures per Plaud’s reported migration results.*

QPS headroom and tail latency matter, but the first result I’d point to is the online DDL. Restoring the ability to change the schema without a maintenance window is what handed the roadmap back to the product team. The database stopped governing the release cadence. That’s not a performance win you can put on a benchmark chart, but it’s the one the product organization feels every week.

Also notice what the fix did not do: it did not attempt to store 30-megabyte audio files in the database. Large objects can still be [stored in object storage](https://thenewstack.io/slatedb-bottomless-databases-built-on-cloud-object-stores/). The point was never “put everything in one system for its own sake.” The point was that the metadata layer, the part that has to be consistent, queryable, and evolvable in real time, needed to actually behave like a database at scale, instead of becoming the fragile half of a split-brain architecture.

## Where architectural debt goes

Here’s the claim the Plaud numbers are evidence for. When the database is the product, architectural debt does not accumulate in some back-office system that only the platform team feels. It accumulates in the product experience, where every user feels it.

This is the structural difference between an AI note-taker and, say, an internal analytics tool. For a product like this, every meaningful user interaction is a database operation. Recording creates rows and objects. Transcription updates state. Retrieval is a read. Editing is a write. Search is a query. There is no part of the product that isn’t, underneath, the database doing something. Architectural problems surface as product problems, one-for-one. A consistency gap becomes a transcript that is briefly missing. Slow retrieval reads as a product that is slow to remember. A frozen schema means features arrive late.

No user will ever file a bug report that says “your metadata store and your object store lack a shared transaction boundary.” Left unaddressed, this class of debt manifests as a product that feels less dependable precisely when someone depends on it. For a product whose entire value proposition is “trust me to remember,” the debt lands on the promise itself. This is why Plaud’s decision to re-architect when it did matter. The team fixed the data layer before the failure became noticeable to users.

> “You can have the best transcription model in the category and still ship a product that feels unreliable, because reliability for this kind of product is a data architecture property, not a model property.”

This is why I say the database is the product. Not as a slogan. As a literal description of where the product’s quality is determined. You can have the best transcription model in the category and still ship a product that feels unreliable, because reliability for this kind of product is a data architecture property, not a model property.

## The trap is waiting for the whole category

AI hardware is having a moment. Note-takers, wearables, ambient recorders, pendants, badges — each built on the premise that the device will remember so you don’t have to. The category is growing, and the products are getting better at the parts everyone talks about: the models, the form factor, the battery life.

But underneath, almost all of them start with the same architecture Plaud started with, because it’s the reasonable default. Structured metadata in a single-instance relational database. Large content in object storage. No shared transaction boundary. A schema that’s easy to change at ten million rows and frozen at three hundred million. The trap is identical, and it’s waiting at the same place on the growth curve for every team in the category.

The teams that will do well are the ones that recognize this early, understand that, for a memory product, the metadata layer is not back-office plumbing but the spine of the user experience, and plan their [data architecture for the scale](https://thenewstack.io/3-ways-enterprises-can-scale-ai-gains-in-2026/) they’re trying to reach rather than the scale they’re at. Plaud’s migration is the pattern worth studying before you hit 300 million rows, not after. The lesson is cheaper to learn from someone else’s 300 million rows than from your own.

When your database and your product are the same thing, you don’t get to treat the database as someone else’s problem. It is the product. Build it like one.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/00b4347d-cropped-44729a2f-ed-huang.png)

Ed Huang is co-founder and CTO of TiDB powered by PingCAP. While he was at Wandou Labs, he worked on clustering Redis and created and open sourced Codis, a proxy based high performance Redis cluster solution. Ed then decided to...](https://thenewstack.io/author/ed-huang/)