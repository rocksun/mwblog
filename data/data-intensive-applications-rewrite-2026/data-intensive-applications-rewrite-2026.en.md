### How Martin Kleppmann’s iconic book is evolving for AI and cloud-native architectures

Since its release in 2017, *Designing Data-Intensive Applications* has become known as the bible for anyone working on large-scale, data-driven systems. The book’s focus on fundamentals (like storage engines, replication, and partitioning) has helped it age well. Still, the world of distributed systems has evolved substantially in the past decade.

Cloud-native architectures are now the default. Object storage has become a first-class building block. Databases increasingly run everywhere from embedded and edge deployments to fully managed cloud services. And AI-driven workloads have made a mark on storage formats, query engines, and indexing strategies.

So, after years of requests for a second edition, Martin Kleppmann revisited the book – and he enlisted his longtime collaborator Chris Riccomini as a co-author. Their goal: Keep the core intact while weaving in new ideas and refreshing the details throughout. With [the second edition of *Designing* now at the printers](https://learning.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/), let’s look at what Kleppmann and Riccomini shared about the project at Monster Scale Summit 2025. That conversation was recorded mid-revision.

You can watch the entire chat or read highlights below.

VIDEO

Side note: Hear what Kleppmann and Riccomini have to say now that the rewrite is complete. Monster Scale Summit 2026 (free + virtual) features a fireside chat with them, as well as Camille Fournier, antirez, engineers from Discord, Disney, LinkedIn, Nextdoor, Pinterest, Rivian, and 50+ more. The [conference is free and virtual](https://www.scylladb.com/monster-scale-summit/).

## People have been requesting a second edition for a while – why now?

**Kleppmann**: Yeah, I’ve long wanted to do a second edition, but I also have a lot of other things I want to do, so it’s always a matter of prioritization. In the end, though, I felt that the technology had moved on enough.

Most of the book focuses on fundamental concepts that don’t change that quickly. They change on the timescale of decades, not months. In that sense, it’s a nice book to revise, because there aren’t that many big changes. At the same time, many details *have* changed.

The biggest one is how people use cloud services today compared to ten years ago. Cloud existed back then, of course, but I think its impact on data systems architecture has only been felt in the last few years. That’s something we’re trying to work in throughout the second edition of the book.

## How have database architectures evolved since the first edition?

**Riccomini**: I’ve been thinking about whether database architecture has changed now that we’re putting databases in more places – cloud, BYOC, on-prem, on-client, on-edge, etc. I think so. I have a hypothesis that successful future databases will be able to move or scale with you, from your laptop, to your server, to your cloud, and even to another cloud. We’re already seeing evidence of this with things like DuckDB and MotherDuck, which span embedded to cloud-based use cases. I think PGlite and Postgres are another example, where you see Postgres being embedded. SQLite is an obvious signal on the embedded side.

On the query engine side, you see this with systems like Daft, which can run locally and in a distributed setting. So the answer is yes.

The biggest shift is the split between control, data, and compute planes. That architecture is widely accepted now and has proven flexible when moving between [SaaS and BYOC](https://thenewstack.io/saas-is-broken-why-bring-your-own-cloud-byoc-is-the-future/).

There’s also an operational aspect to this. When you talk about SaaS versus non-SaaS, you’re talking about things like multi-tenancy and how much you can leverage cloud-provider infrastructure. I had an interesting discussion about [Confluent Freight versus WarpStream](https://thenewstack.io/with-warpstream-confluent-got-a-new-type-of-kafka-platform/), two competing Kafka streaming systems. Freight is built to take advantage of a lot of the in-cloud SaaS infrastructure Confluent has, while WarpStream is built more like a BYOC system and doesn’t rely on things like a custom network plane.

Operationally, there’s a lot to consider regarding security and multi-tenancy, and I’m not sure we’re as far along as we could be. A lot of what SaaS companies are doing still feels proprietary and internal. That’s my read on the situation.

> “At the time of the first edition, the model for databases was that a node ran on a machine. […] Now we’re increasingly seeing a model where storage is an object store.”

**Kleppmann**: I’d add a little to that. At the time of the first edition, the model for databases was that a node ran on a machine, storing data on its local file system. Storage was local disks, and replication happened at the application layer on top of that.

Now we’re increasingly seeing a model where storage is an object store. It’s not a local file system; it’s a remote service, and it’s already replicated. Building on top of an abstraction like object storage lets you do fundamentally different things compared to local disk storage.

I’m not saying one is better than the other – there are always tradeoffs. But this represents a new point in the tradeoff space that really wasn’t present at the time of the first edition. Of course, object stores existed back then, but far fewer databases took advantage of them in the way people do now.

## We’ve seen a proliferation of specialized databases recently – do you think we’re moving toward consolidation?

**Riccomini**: With my investment hat on, this is the million-dollar…or billion-dollar…question. Which of these is it? I think the answer is probably both.

The reality is that Postgres has really taken the world by storm lately, and its extension ecosystem has become pretty robust in recent versions. For most people, when they’re starting out, they’re naturally going to build on something like Postgres. They’ll use pg\_search or something similar for their search index, pgvector for vector embeddings, and PG analytics or pg\_duckdb for their data lake.

Then the question is: as they scale, will that still be okay? And in some cases, yes. In other cases, no.

My personal hypothesis is that as you not only scale up but also need features that are core to your product, you’re more likely to move to a specialized system. pgvector, for example, is a reasonable starting point. But if your entire product is like Cursor AI or an IDE that does code completion, you probably need something more robust and scalable than pgvector can provide. At that point, you’d likely look at something like Pinecone or Turbopuffer or companies like that. So I think it’s both.

And because Postgres is going to eat the bottom of the market, I do think there will be fewer specialized vendors, but I don’t think they’ll disappear entirely.

## What are some of the key tradeoffs you see with streaming systems today?

**Kleppmann**: Streaming sits in a slightly weird space. A typical stream processor has a one-record-at-a-time, callback-based API. It’s very imperative.

On top of that, you can build things like relational operators and query plans. But if you keep pushing in that direction, the result starts to look much more like a database that does incremental view maintenance.

There are projects like Materialize that are aiming there. You just give it a [SQL query](https://thenewstack.io/how-to-write-sql-queries/), and the fact that it’s streaming is an implementation detail that’s almost hidden.

I don’t know if that means the result for many of these systems is this: if you have a query you can express in SQL, you hand it off to one of these systems and let it maintain the view.

And what we currently think of as streaming, with the lower-level APIs, is used for a more specialized set of applications. That might be very high-scale use cases, or queries that just don’t fit well into a relational style.

**Riccomini**: Another thing I’d add is the fundamental tradeoff between latency and throughput, which most streaming systems have to deal with.

Ideally, you want the lowest possible latency. But when you do that, it becomes harder to get higher throughput.

The usual way to increase throughput is to batch writes. But as soon as you start batching writes, you increase the latency between when a message is sent and when it’s received.

## How is AI impacting data-intensive applications?

**Kleppmann**: There’s some AI-plus-data work we’ve been exploring in research (not really part of the book). The idea is this: if you want to give an AI some control over a system – if it’s allowed to press buttons that affect data, like editing or updating it – then the safest way to do that is through a well-defined API.

That API defines which buttons the AI is allowed to press, and those actions correspond to things that make sense and maybe fulfill certain consistency properties.

More generally, it seems important to have interfaces that allow AI agents and humans to work safely together, with the database as common ground. Humans can update data, the AI can update data, and both can see each other’s changes.

You can imagine workflows where changes are reviewed, compared, and merged. Those kinds of processes will be necessary if we want good collaboration between humans and AI systems.

> “It seems important to have interfaces that allow AI agents and humans to work safely together, with the database as common ground.”

**Riccomini**: From an implementation perspective, storage formats are definitely going to evolve. We’re already seeing this with systems like LanceDB, which are trying to support multimodal data better.

Arrow, for example, is built for columnar data, which may not be the best fit for some multimodal use cases. And this goes beyond storage into things like Arrow RPC as well.

On the query engine side, there’s also a lot of ongoing work around query optimization and indexing. The idea is to build smarter databases that can look at query patterns and adjust themselves over time.

There was a good paper from Google a while back that used more traditional machine learning techniques to do dynamic indexing based on query patterns. That line of work will continue.

And then, of course, support for embeddings, vector search, and semantic search will become more common. Good integrations with RAG (Retrieval-Augmented Generation)…that’s also important. We’re still very much at the forefront of all of this, so it’s tricky.

## More from Kleppmann and Riccomini

Join us at this year’s [Monster SCALE Summit (free + virtual)](https://www.scylladb.com/monster-scale-summit/) to hear the latest from Kleppmann and Riccomini. There’s a full 60-minute deep dive into the biggest shifts influencing the second edition: cloud-native architectures and AI. Attendees get 30-day access to the O’Reilly platform, including the latest edition of *Designing Data-Intensive Applications*.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/01/14adf317-cynthiadunlop.jpeg)

Cynthia Dunlop has been writing about software development and testing for much longer than she cares to admit. She's currently senior director of content strategy at ScyllaDB.

Read more from Cynthia Dunlop](https://thenewstack.io/author/cynthiadunlop/)