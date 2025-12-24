Tiger Data, formerly known as Timescale, recently open sourced a preview version of [pg\_textsearch](https://github.com/timescale/pg_textsearch), ranked text search using the [Best Matching 25 (BM25) algorithm](https://www.geeksforgeeks.org/nlp/what-is-bm25-best-matching-25-algorithm/) for PostgreSQL.

Its creators have found the response startling. Within days, it had 1,000 stars on GitHub and had 1,800 at last count.

The company changed its name because, although originally focused on creating a time-series database, it found developers using its Postgres implementation for use cases unrelated to time series data. As the company widened its focus — today it offers its own cloud as well Postgres for Agents — the name created confusion, [Mike Freedman](https://www.linkedin.com/in/mfreed/), founder and CTO, explained in an interview.

More recently it has focused on improving search in Postgres for AI applications.

“We heard from our customers who wanted to start exploring AI search, that they needed this general-purpose search primitive. And effectively, there wasn’t anything at the time available in the market that we could offer them, and so that’s why we ended up building a building ourselves and open sourcing it,” he explained.

The preview release of pg\_textsearch is a Postgres extension to improve the relevance and performance of search in the 30+-year-old database.

## The Need for Better Keyword Search in the AI Era

We’ve been hearing a lot about a [resurgence of interest in ‘boring,’ reliable Postgres](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/), especially [since AI has taken off](https://thenewstack.io/why-a-boring-database-is-your-secret-ai-superpower/). Though initially it seemed all the talk was about [vector databases](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/), an emerging pattern is merging [vector](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/) and [keyword search](https://thenewstack.io/combining-the-power-of-text-based-keyword-and-vector-search/), Freedman said.

While search engines like Apache Lucene and Elasticsearch — and native Postgres as well — have offered keyword search for years, AI has hastened the need to improve the relevance of the output they provide.

“AI-native applications, RAG [retrieval-augmented generation] systems, chat agents, and agentic workflows need search not for humans browsing catalogs or engineers querying logs, but for LLMs [large language models] [retrieving context](https://www.tigerdata.com/blog/introducing-pg_textsearch-true-bm25-ranking-hybrid-retrieval-postgres),” senior software engineer [TJ (Todd) Green](https://www.linkedin.com/in/todd-j-green/overlay/about-this-profile/) explained in a blog post.

“The corpus doesn’t change as rapidly as streaming logs, but result quality is paramount: these systems need both semantic understanding from vector search and the precision of keyword matching. The two approaches are deeply complementary: vectors capture conceptual similarity while keywords ensure exact terms aren’t missed.”

He adds: “The challenge is that Postgres native full-text search lacks the ranking signals needed to consistently surface the most relevant results.”

## What Is the BM25 Algorithm?

BM25 (Best Matching 25) is an [algorithm to rank relevance](https://www.tigerdata.com/docs/use-timescale/latest/extensions/pg-textsearch) in information retrieval systems. It’s considered an improvement over [TF-IDF (Term Frequency–Inverse Document Frequency)](https://www.geeksforgeeks.org/machine-learning/understanding-tf-idf-term-frequency-inverse-document-frequency/) approach that search engines have traditionally used.

Using a memtable architecture to index and rank information, pg\_textsearch:

* Uses inverse document frequency to weight rare terms higher.
* Uses term frequency saturation to prevent terms used repeatedly from dominating results.
* Prevents long documents from dominating.
* With relative ranking, focuses on rank order rather than absolute score values.

It supports PostgreSQL 17 and PostgreSQL 18.

With Postgres’ native search, performance degrades dramatically as the corpus size grows because it must consult the tsvector of each matching document. With pg\_textsearch, you can set the memory size for the corpus you’re using and use score thresholds to filter out low-relevance results to improve performance.

Used together with [pg\_vector](https://github.com/pgvector/pgvector?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) and [pg\_vectorscale](https://thenewstack.io/make-pgvector-faster-than-pinecone-and-75-cheaper-with-this-new-open-source-extension/), which adds more advanced algorithms building on the same data types as pg\_vector, developers can combine keyword search with vector search in Postgres via a single SQL query, avoiding the latency and complexity of calling data from multiple data sources, according to the company.

“I think the great parallel is pg\_vector,” said Freedman, referring to response to the open source announcement. “You know, there was this huge rise of all these vector databases, and then pg\_vector came about … and it had broad adoption. And again, the missing piece for modern AI search is the keyword side of it.”

“What we were seeing is a lot of vendors were coming out with kind of their own proprietary implementation, and this wasn’t really solving the broader developer need of, ‘Hey, we want this kind of more ecosystem-friendly software that I could kind of take anywhere.’ I think that fragmentation doesn’t serve anybody when there’s a lot of these proprietary implementations.”

They chose to license it under the permissive Open Source Initiative (OSI)- approved [PostgreSQL license](https://opensource.org/license/postgresql) because they wanted it to be broadly available and broadly adopted, Freedman said.

Meanwhile, more vendors and open source projects are adding BM25 ranking, including Elasticsearch, Apache Solr and Neon, although Freedman said the alternatives tend to have less-permissive licenses.

## How pg\_textsearch Was Built

After some planning for a couple of months, Green set to work on pg\_textsearch in October and the company announced the open source preview in mid-December.

“I think the hardest thing for us to decide was just to commit to it, because the world is changing, right?” said Green in the interview. “A project like this would have taken a small team a significant amount of time, pre-AI tools, and you know that was going to be too long and too expensive for us, so we decided to take a chance on developing this a different way,”

That different way was “essentially, me and the robot,” according to Green, who previously worked as a computer scientist at RelationalAI and on databases at AWS and Pinecone. The robot was [Claude Cloud Opus](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/).

“Yes, I was one of the crazy people who are willing to pay the cost of Opus 4.1 because I found it so much more capable and better matched my workflow than the alternatives. And now we have [Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/), which is even more capable and significantly cheaper. And so that’s essentially my workflow inside, along with using [Cursor](cursor) as an editor,” he said.

Things are moving quickly and he expects a production-ready version to be available early in the new year, possibly January.

“It will depend also on feedback we get from people who just started hammering on this thing this week. We’ve already gotten some very helpful reports, and it’s going to be a function of, you know, how hardened it actually looks once it’s been subjected to kind of usage in the wild,” he said.

Freedman pointed out that because the company runs its own cloud, its instrumentation will allow it to see issues people are running into rather than just relying on reports, which should accelerate the timeline.

“Postgres has basically won developers’ hearts and minds. It is the go-to database for almost every developer today … with AI,  how do we continue to extend it, so that developers can make use of it more and more, and so that they end up with kind of simpler, easier-to-use data architectures, as opposed to having five different databases with their data spread across all these different things, and they have to worry about synchronization and management,” Freedman said. “Instead, we could kind of coalesce a lot of that into Postgres, particularly [what] I like to think of as building for the 99%. It’s built for the 99% of projects out there.

“We’re really bullish about how AI is changing how developers build, and we’re kind of in the middle of rethinking what that experience looks like differently for developers, and how our data infrastructure can support that,” he said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/01/cabe83e0-susan-mug.jpg)

Susan Hall is the Sponsor Editor for The New Stack. Her job is to help sponsors attain the widest readership possible for their contributed content. She has written for The New Stack since its early days, as well as sites...

Read more from Susan Hall](https://thenewstack.io/author/susanhall/)