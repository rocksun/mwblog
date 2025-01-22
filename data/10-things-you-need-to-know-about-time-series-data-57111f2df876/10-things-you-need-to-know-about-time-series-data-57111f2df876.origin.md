# 10 Things You Need to Know About Time-Series Data
We’ve rounded up an all-in-one guide of tips and recommended resources to help you do more with your time-series data. ✅ [Now, is your data time series](https://www.timescale.com/learn/types-of-data-supported-by-postgresql-and-timescale)? You may not think of it that way, but check our list of examples — you may be surprised.

With topics ranging from ways to optimize your database performance and integrate with third-party tools to the things you need to consider when evaluating time-series databases, there’s something for everyone — whether you’re new to time series or an experienced DBA.

The result is **a cheat sheet of things you need to know about time-series databases** sourced from our internal teams and active developer community. (Some may be a refresher, while others may be new to you.)

# 10 things to know about time-series data & recommended resources
## 10. “Big cloud” providers don’t necessarily offer better products.
**Resource: ****What We Learned From Benchmarking Amazon Aurora PostgreSQL Serverless**
No one wants to start out with a database only to find it doesn’t scale or suit their needs as apps and systems grow. As this post points out, time-series databases vary widely in terms of ingest speed, query latency, ease of use, reliability, and more.

We have a history of benchmarking time-series database performance, and we spent weeks analyzing Amazon Aurora Serverless ingest performance, query speed, cost, and reliability. We double-checked the numbers several times because we almost found it hard to believe them, but Timescale’s PostgreSQL cloud platform was:

- 35 % faster to ingest
- 1.15x-16x faster to query in all but two query categories
- 95 % more efficient at storing data
- 52 % cheaper per hour for compute
- 78 % cheaper per month to store the data created
[Check out the full post](https://www.timescale.com/blog/what-we-learned-from-benchmarking-amazon-aurora-postgresql-serverless/) for detailed results, key database consideration criteria, and steps to reproduce the results and run your own benchmarks.
## 9. Time-series data is great for financial services, from traditional stock markets to cryptocurrency.
**Resource: ****Learn how to power a (successful) crypto trading bot with TimescaleDB**
[Read how Felipe, software developer and active TimescaleDB community member, built his crypto trading bot](https://www.timescale.com/blog/blog/how-i-power-a-successful-crypto-trading-bot-with-timescaledb/) — and netted 480x returns — using TensorFlow, Node.js, TimescaleDB, and machine-learning sentiment analysis models, the lessons he learned along the way, and his advice for aspiring crypto traders.
And, if you want to try your own crypto analysis, check out our [Analyze Cryptocurrency Market Data](https://docs.timescale.com/latest/tutorials/analyze-cryptocurrency-data/) tutorial (which includes step-by-step instructions and 5+ sample queries).

Moreover, time-series isn’t just a niche reserved for IoT, oil and gas, and finance; time-series data is everywhere, from tracking package delivery fleet logistics to monitoring systems and applications, predicting flight arrivals, and reporting air quality. ([See our primer on time-series data](https://www.timescale.com/blog/blog/what-the-heck-is-time-series-data-and-why-do-i-need-a-time-series-database-dcf3b1b18563/) to learn more about what makes time-series data unique.)

If you’re not sure where to start or if time-series data applies to your scenario, our [Developer Q&A series](https://www.timescale.com/blog/tag/dev-q-a/) features community members sharing the awesome ways they’re using data to solve problems, improve processes, and, in the case of Felipe’s crypto bot, turn a side project into a money-making machine.

## 8. Continuously optimizing your database insert rate is especially critical for time-series workloads.
**Resource: ****Get our 13 tips to improve PostgreSQL Insert performance**
With time-series data, changes are treated as *inserts*, not overwrites — and when you need to retain all data vs. overwriting past values, optimizing the speed at which your database can ingest new data becomes essential.

To help you improve your database performance and optimize for time-series scenarios, Timescale CTO Mike Freedman ([@michaelfreedman](https://twitter.com/michaelfreedman)) shares [his top tips](https://www.timescale.com/blog/blog/13-tips-to-improve-postgresql-insert-performance/). You’ll get advice for vanilla PostgreSQL — like how to test I/O performance — and a few TimescaleDB-specific recommendations.

## 7. Enabling compression dramatically reduces your storage costs, speeds up queries, and allows you to retain more data.
**Resource: ****Building Columnar Compression for Large PostgreSQL Databases**
Compression algorithms: they’re not magic, but they can dramatically reduce your data storage costs and speed up your queries. Given the relentless nature of time-series data, where data piles up quickly, shrinking your data storage needs is even more critical.

In this article, we’ll tell you the story of how we built a flexible, high-performance columnar compression mechanism for PostgreSQL to improve its scalability.

✨ Fun fact: By combining columnar storage with specialized compression algorithms, we’re able to achieve impressive compression rates unparalleled in any other relational database (+95 %).

## 6. Used and queried effectively, your time-series data can turn into a tool to predict trends and forecast future events.
**Resource: ****Replacing kdb+ With PostgreSQL for Time-Series Forecasting**
[Time-series forecasting](https://www.timescale.com/blog/what-is-time-series-forecasting/) alone is powerful. But, joining time-series data with other relational business data allows you to create more insightful forecasts about how your data (and business) will change over time.
In this Developer Q&A, data scientist Andrew Engel shared his story on how he is creating proofs of concept of machine learning pipelines for time-series forecasting using TimescaleDB.

## 5. If you select the right database, you can integrate it with your favorite third-party and open-source tools.
**Resource: ****See our favorite PostgreSQL extensions for time-series**
With 20K+ extensions to choose from, we love PostgreSQL for its vast ecosystem and extreme extensibility. And, luckily, [many extensions help you work more efficiently with time-series data](https://www.timescale.com/learn/postgresql-extensions) *without* the hassle of switching to a whole new database.

But, where do you start?

To help you find options that might be right for you, we surveyed our internal team members and active community members to source our “must have” extension list, including a few less widely known — but useful — ones.

⭐️ Bonus: installation instructions and sample queries to show you how to get each extension, how it works, and what it allows you to do.

## 4. Database architecture, flexibility, and query language matter — and can vary widely.
**Resource: ****Read how TimescaleDB and InfluxDB are purpose-built differently — and how this impacts performance**
While our [Amazon Aurora benchmark](https://www.timescale.com/blog/what-we-learned-from-benchmarking-amazon-aurora-postgresql-serverless/) demonstrates that choosing the right time-series database isn’t as simple as choosing from the “big” cloud providers, our InfluxDB comparison demonstrates the importance of understanding your requirements, such as a query language, developer onboarding time, ecosystem, and fully managed database options.

We report where InfluxDB outperforms TimescaleDB (low-cardinality queries) and use data to show why TimescaleDB is the better choice if you have high-cardinality datasets, want a flexible hosted database option, and/or don’t want to learn a proprietary query language.

And speaking of query languages, we built [a cheat sheet to help you understand the differences between InfluxQL, Flux, and SQL](https://www.timescale.com/learn/influxql-flux-sql-which-query-language-is-best-with-cheatsheet).

## 3. Grafana is extremely well suited to time series, but there’s a learning curve.
**Resource: ****Watch Guide to Grafana 101: Getting Started With (Awesome) Visualizations**
Grafana is an amazing open-source visualization tool (we love it at Team Timescale) and well-suited to common time-series scenarios, but there are a lot of features that you may not know how, when, or why to use.

To help you see how and why Grafana is ideal for time series, Avthar ([@avthars](https://twitter.com/avthars)) demos how to build 6+ visualizations — from world maps to gauges — for IoT, DevOps, and more. You’ll see real examples and get the best practices, code samples, and inspiration you need to create your own (awesome) visualizations.

## 2. You can host your time-series data and only pay for what you store.
**Resource: ****Navigating a Usage-Based Model for PostgreSQL**
With time-series data, each data point is inserted as a new value instead of overwriting the prior (i.e., earlier) value. As a result, time-series workloads scale **much **faster than other types of data, and you need a database that will grow with you — without astronomical costs or compromised performance.

With Timescale Cloud, [you will only pay for the storage you actually use in your Timescale services without pricing gotchas or hidden costs](https://www.timescale.com/blog/savings-unlocked-why-we-switched-to-a-pay-for-what-you-store-database-storage-model/). This new storage experience is simple, transparent, and saves you money — especially when combined with features like compression and tiered storage.👇

## 1. A relational database for time series can infinitely scale
**Resource: ****Scaling PostgreSQL for Cheap: Introducing Tiered Storage in Timescale**
The final thing we’d like to impart about time-series data: a relational database can scale infinitely. To prove this, we built tiered storage,** **a multi-tiered* *storage* *architecture engineered to enable infinite, low-cost scalability for your time series and analytical databases in the Timescale platform.

With our tiered storage architecture, you can now store your older, infrequently accessed data in a low-cost storage tier while still being able to access it — without ever sacrificing performance for your frequently accessed data. And the best part? It is wildly affordable: our low-cost storage tier has a **flat price of $0.021** per GB/month for data — cheaper than Amazon S3.

# Wrapping Up
To get started with TimescaleDB and put these resources and tips into practice, **try our hosted database for free**** **(30-day trial).

If you prefer to self-manage TimescaleDB, [see our GitHub repository](https://github.com/timescale/timescaledb) for installation options (⭐️ always welcome and appreciated!).

Lastly, [join our Slack community](https://slack.timescale.com/) to ask questions, get help, and learn more about all things time series; our engineers and community members are active in all channels.

*This article was written by Lacey Butler and Ana Tavares, originally published **here** on the Timescale official blog on Nov. 20, 2023, and last updated on Oct. 17, 2024.*