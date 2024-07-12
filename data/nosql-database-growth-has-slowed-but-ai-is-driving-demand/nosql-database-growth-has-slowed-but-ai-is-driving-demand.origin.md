# NoSQL Database Growth Has Slowed, but AI Is Driving Demand
![Featued image for: NoSQL Database Growth Has Slowed, but AI Is Driving Demand](https://cdn.thenewstack.io/media/2024/07/5a65fb92-pawel-czerwinski-weizaiwlk1k-unsplash-1024x683.jpg)
Four years ago, I wrote about how [NoSQL databases were growing fast](https://thenewstack.io/redis-in-the-age-of-ai/) — in large part due to their compatibility with Artificial Intelligence (AI) and Machine Learning (ML). But that was *before* the [generative AI boom that began](https://thenewstack.io/top-5-internet-technologies-of-2022/) with OpenAI’s release of ChatGPT in November 2022.

So what has happened to NoSQL databases since ChatGPT arrived on the scene? Are NoSQL database systems — like document stores (MongoDB), key-value (Redis), and wide column (Cassandra) — still growing in the new age of the [vector database](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/)?

Back in 2020, to illustrate the growth of NoSQL database systems, I used the following graph [from DB-Engines](https://db-engines.com/en/ranking_categories):

That showed the steep upward trajectory of systems like MongoDB, Redis and Cassandra from 2013-2020 (although there was a slight dip from all three towards the end of that period). Compared to the flat — and eventually downward — line of traditional relational databases, such as Oracle and MySQL, the NoSQL growth curve was significant.

Here’s the latest popularity chart from DB-Engines, for the past 36 months (3 years):

With the caveat that this graph measures popularity growth (and not actual users), we can see that vector databases have naturally experienced a growth spurt since 2021 — although it appears to have peaked towards the end of last year. Meanwhile, document stores and key-value stores have gone down slightly.

However, if we look at the chart from 2013, we can see that vector database growth hasn’t reached anywhere near the peaks of document stores and key-value stores (let’s disregard the wide column store chart, as its data set appears to have changed on DB-Engines since my 2020 post).

Also, despite a slight dip in growth rate, NoSQL database systems are still among the most popular choices for developers. The graph below shows little change in the top ten database systems for the past two years, with the top six (including MongoDB at 5 and Redis at 6) remaining unchanged. We also see that the top four database systems are all relational; and have significantly more users than MongoDB and Redis.

## NoSQL and Generative AI
When [Redis](https://redis.com/?utm_content=inline+mention) announced a controversial [license change](https://redis.io/blog/redis-adopts-dual-source-available-licensing/) earlier this year, the Linux Foundation almost immediately announced its backing of an open source fork of Redis, [named Valkey](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/). The position of Redis, the company, is that the big cloud providers have an unfair market advantage and the new licensing is its way of trying to get them to pay up. MongoDB had made a similar move to tighten restrictions on its license back in 2018.

I’ll leave the debate about Redis’ new license to others, but I do want to highlight [a blog post](https://redis.io/blog/the-future-of-redis/) that Redis published the day after its announcement. Entitled “The Future of Redis,” it focuses heavily on AI uses for Redis. “We’re staying at the forefront of the GenAI wave,” wrote CEO Rowan Trollope and CTO Yiftach Shoolman, adding that “we were among the first to recognize the need for vector search functionality in a database, even before ChatGPT and LLMs were household names.”

The post detailed plans for an AI-powered assistant called Redis CoPilot (which is [now available](https://redis.io/chat)), “to allow developers to directly interact with their data using language and translate that into code.” It also intends to make Redis “even more cost-efficient for RAG use cases by leveraging product quantization and further improving vector processing performance with the latest hardware and GPU advancements.”

As for [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), it too is targeting generative AI use cases. In a recent post on The New Stack, developer relations team lead Rick Houlihan explicitly [compared its solution to PostgreSQL](https://thenewstack.io/benchmarking-postgresql-vs-mongodb-for-genai/), a popular open source relational database system. Houlihan contended that systems like PostgreSQL were not designed for the type of workloads demanded by AI:

“Considering the well-known performance limitations of RDBMS when it comes to wide rows and large data attributes, it is no surprise that these tests indicate that a platform like PostgreSQL will struggle with the kind of rich, complex document data required by generative AI workloads.”

Unsurprisingly, he concludes that using a document database (like MongoDB) “delivers better performance than using a tool that simply wasn’t designed for these workloads.”

In defense of PostgreSQL, there is no shortage of managed service providers for Postgres that provide AI-focused functionality. Earlier this year [I interviewed a “Postgres as a Platform” company](https://thenewstack.io/how-devs-can-use-postgres-extensions-including-for-ai-apps/) called Tembo, which has seen a lot of demand for AI extensions. “Postgres has an extension called pgvector,” Tembo CTO Samay Sharma told me. “So that allows you to add a simple data type called vector to your existing tables. So even if you have your existing row of data, you could just add a vector data type — which is a transformed embedding.”

## More Than Enough AI Data To Go Around
Of course, every database company now claims that it can be used well with AI. Just last month, [Oracle](https://developer.oracle.com/?utm_content=inline+mention) released [an AI-driven update](https://thenewstack.io/from-english-to-sql-oracle-apex-ai-bridges-the-language-gap/) to its Oracle APEX low-code development platform, which the company says enables non-developers to execute vector queries in less than two minutes, without knowing SQL.

When it comes to AI, there is currently no shortage of demand — and all database companies and projects, SQL or NoSQL, are benefiting from that.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)