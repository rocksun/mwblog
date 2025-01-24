# Boost Your PostgreSQL Performance With Auto Chunk Size Recommendations
As developers, we believe having the right tools to take an application to market faster and with the quality users deserve is absolutely crucial. Our mission is to ensure Timescale Cloud, [our fully managed PostgreSQL cloud](https://www.timescale.com/cloud), is *that* asset on your developer toolbelt. So, we’ve been dedicating a lot of our time and effort to several improvements to enable you to ship faster while enjoying a prime developer experience.

Among these improvements are the recently launched [data migration wizards and Actions hub](https://www.timescale.com/blog/moving-faster-from-poc-to-prod/) and our [SQL Assistant](https://www.timescale.com/blog/postgres-gui-sql-assistant/), a trusty AI companion that will help you write better SQL code, debug with confidence, and much more. These tools live in the Timescale Console and aim to ease onboarding so you can hit the ground running and adopt central features for peak performance quicker, effortlessly moving from proof of concept (PoC) to production.

Today, we bring you the latest addition to our UI tooling, Chunk Size Recommendations — a new feature designed to take the guesswork out of configuring hypertables and empower you to build faster and more scalable systems. This is the first of many recommendations to users where they can improve their existing database configuration to get even better performance from Timescale. Timescale has your back for peak performance, from onboarding to production operation.

And to prove just that, we’re releasing a [companion video](https://www.timescale.com/blog/p/02a56e9e-0d38-4645-9182-8425a4dc9161/#video-how-chunk-size-recommendations-work) as part of our new `EXPLAIN ANALYZE`
series. This series is designed for developers and offers quick, actionable tips to maximize Timescale performance for your applications. Keep your eyes peeled for the next episodes. 👀

But before sharing the first episode, let’s quickly summarize why chunk size matters for your PostgreSQL database performance.

✨ To see all our October launches and stay updated on upcoming ones, [visit our blog post](https://timescale.ghost.io/blog/how-were-bringing-postgres-into-the-ai-era/) or check out the [launch page](https://www.timescale.com/launch/2024).

# Why Chunk Size Matters for Postgres Performance
In TimescaleDB, the core of Timescale Cloud, hypertables partition data into chunks. While this provides powerful capabilities for time-series data, such as easy data retention management and fast query performance, choosing the correct chunk size can make a significant difference. The right size optimizes both write and query performance, reduces metadata overhead, and prevents query planning slowdowns that come from too-small chunks.

Too-small chunks mean your database has to manage more metadata, which can slow down queries and increase planning times, especially as your data grows. Conversely, oversizing chunks can lead to inefficiencies, potentially causing slowdowns when querying recent data. That’s why setting the right chunk size is so critical — and why it’s now simpler than ever with our new Chunk Size Recommendations tool.

# Video: How Chunk Size Recommendations Work
When you log in to the [Timescale Console](https://console.cloud.timescale.com/login), Timescale automatically analyzes your hypertables and flags any tables where chunks are undersized for optimal performance. You’ll receive recommendations tailored to your database usage, presented as a clear, actionable alert.

In the first episode of our `EXPLAIN ANALYZE`
series, [we show you how this tool works](https://youtu.be/xrV6NAQnvnE):

# Try Chunk Size Recommendations Today
Impressive, right? To try Chunk Size Recommendations today and start boosting your PostgreSQL performance with Timescale Cloud and hypertables, [sign up for a free 30-day trial](https://console.cloud.timescale.com/signup/?utm_source=blog&utm_medium=email&utm_campaign=november-abl&utm_content=timescale-cloud-signup), no credit card required.

Plus, keep an eye out for more videos on our `EXPLAIN ANALYZE`
series, where we’ll continue to share practical advice and best practices for making the most out of your Timescale databases. And as always, we welcome your feedback—[let us know](https://slack.timescale.com/) how Chunk Size Recommendations and our other recent features are helping you build better, faster, and more scalable applications.

*This article was written by Grant Godeke, Ana Tavares, and Melanie Savoia, originally published **here** on the Timescale official blog on Nov. 15, 2024, and last updated on Nov. 28, 2024.*