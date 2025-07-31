[Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox) refers to a phenomenon where the consumption of resources goes up as they become more efficient to use. In the 19th century, the economist William Stanley Jevons noticed that as coal became more efficient to extract, the lower cost led to more demand and more usage. Now this 19th-century paradox is being applied to the explosion in AI usage and productivity. Microsoft CEO [Satya Nadella was referring to Jevons paradox](https://www.npr.org/sections/planet-money/2025/02/04/g-s1-46018/ai-deepseek-economics-jevons-paradox) when he said, “As AI gets more efficient and accessible, we will see its use skyrocket, turning it into a commodity we just can’t get enough of.”

As the solutions for ingesting, retaining and analyzing data get more efficient and accessible, the demand for data — and its value — will continue to grow. By taking advantage of modern data solutions that allow for cost-effective, long-term data retention, enterprises can generate large, quality datasets and improve their AI readiness.

Let’s take a closer look at Jevons paradox and how it applies to both AI and data — then examine how the old paradigm of costly, short-term data retention is being replaced by a new data paradigm that will improve data quality and enable more effective AI models.

## How Jevons Paradox Applies To AI and Data

The basic concept behind Jevons paradox is fairly simple: Greater efficiency leads to more consumption of resources, not less, as more people adopt efficient technologies. Applying this to AI, increased efficiency and lower costs will lead to increased consumption of AI tools.

However, AI models are both compute-intensive to run and generally perform much better when trained on large datasets. That often means huge costs for both compute (training models) and storage (keeping large volumes of data in readily accessible formats).

OpenAI is perhaps the most prominent example, spending an [estimated $4 billion](https://www.axios.com/2024/10/03/openai-investors-profit-money-costs) to keep ChatGPT running in 2024. Much of that cost is due to compute and the huge volume of data ChatGPT needs to run. While OpenAI is a particularly exorbitant example, many enterprises are dealing with similar challenges where models cost considerable amounts to train and run, reducing return on investment (ROI) — and even leading to losses.

Increasing the efficiency (and lowering the cost) of AI is in part dependent on increasing the efficiency of ingesting, storing and analyzing huge volumes of data. In turn, this greater efficiency will lead to more consumption of that data — whether that’s training AI or supporting teams for use cases such as [observability](https://thenewstack.io/observability-2-0-or-just-logs-all-over-again) in data science. In other words, Jevons paradox also applies to data. Data solutions must become more efficient and cost-effective when it comes to big data for AI models to meet expectations and generate not just revenue but actual profit.

Unfortunately, many enterprises are dealing with bottlenecks when it comes to data. The new data-intensive paradigm is clashing with the old paradigm, one where petabytes of data have traditionally been too expensive to retain and analyze.

## The Old Paradigm: Low Availability and Discarded Data

In the old paradigm, enterprises often dealt with huge increases in data (such as logs) in two ways:

* **Quickly moving data to cost-effective storage that’s difficult to access.** Unstructured data may be moved into a data lake, which can quickly become a data swamp if it’s not structured later. It’s often difficult and expensive to query. Meanwhile, security and telemetry data might get moved into frozen storage or archived, where it’s time-consuming and difficult to rehydrate. Because this data isn’t designed to be queried heavily, model training can be both inefficient and expensive.
* **Sampling, aggregating or discarding data, leading to incomplete datasets.** A great deal of data is discarded altogether, either through sampling or aggregating (summarizing data and then throwing the underlying data away). This is especially common with telemetry data. The result is low-fidelity data that can result in inaccurate or delayed models.

The old paradigm treats data as an expensive, and often not very useful, commodity that doesn’t need to be retained long-term. A common example of this approach is observability, where [log data](https://thenewstack.io/observability-isnt-enough-its-time-to-federate-log-data) is kept for a short period of time to mitigate issues when they occur, but then discarded.

It’s easy to see why enterprises traditionally favored this approach. The cost of ingesting, storing and analyzing data was (and is) a real, and often big, number — a bill that cuts into the bottom line. In contrast, the value of data is often much more difficult to quantify. As an example, what’s the value of a content delivery network (CDN) log from a year ago? It may be important to retain it for security and compliance, but otherwise, its value was murky and considered to be zero. But now this data can be used to train models for anomaly detection, user personalization and more, increasing its value.

## The New Paradigm: AI Needs a Lot More Data

When it comes to training AI models, more data is usually better, and it leads to better generalizations and less bias. Less data can result in underfitting and simplistic models that can’t make useful predictions. And some models (such as those focused on anomaly detection) need interesting outliers to become more effective. These outliers may exist only in very large datasets.

To address the data-intensive needs of AI models — and to ensure that models become more effective, efficient and affordable — data solutions must provide full-fidelity data that allows enterprises to train models both now and in the future. These solutions must offer the following:

### High Dimensionality

Logs and other types of data can have hundreds or even thousands of dimensions. While it’s typical to limit dimensionality when training models, enterprises often won’t be able to predict which dimensions they’ll need for future training. The term “[arbitrarily wide, structured events](https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes)” has become buzzy in observability because it allows enterprises to slice and dice data for many different monitoring and observability use cases. For the same reason, arbitrarily wide data is also important for training agentic AI. The ability to slice and dice data in many different ways gives enterprises maximum flexibility for training. All of these dimensions are possible parameters for a model.

### High Cardinality

[High-cardinality](https://hydrolix.io/blog/high-cardinality-data/) columns have many unique values, and when data is high volume, high-cardinality data can be especially costly to store and analyze when data solutions aren’t equipped to handle it. But high cardinality is often an attribute of large, full-fidelity datasets. Cardinality-reduction techniques will also reduce the granularity of the data, making it less accurate for model training. Data solutions must be able to ingest, store and query this data effectively, all while using compression techniques to reduce its size as much as possible.

### On-Demand Availability

The traditional approach of moving large datasets to [frozen or archived storage](https://thenewstack.io/stop-freezing-your-data-to-death) leads to costly, time-consuming data rehydration. Instead, data must be available on demand for model training. For datasets that have many stakeholders accessing them (for example, data science and site reliability teams might need real-time access to the same log data), model training can be scheduled for off-peak hours and weekends, and solutions should be able to quickly scale compute up or down as needed. In other words, data should be “hot” for high availability instead of cold or frozen (leading to low availability). And it also needs to be made available to the platforms for training models, such as the Apache Spark ecosystem.

### Cost-Effective

The traditional approach for ingesting, storing and analyzing high-dimensionality, high-cardinality datasets — and keeping them readily available — is extremely expensive. These solutions typically use SSDs and other costly storage solutions for high availability and fast queries. They weren’t designed for the volume of data many enterprises are now ingesting — often terabytes per day — and they predate agentic AI. Modern solutions maximize the performance of cost-effective, horizontally scalable object storage, making it possible to keep much more data for longer. For example, platforms like Databricks are heavily investing in the Apache Iceberg ecosystem, which uses techniques like columnar storage, Parquet compression and partitioning to make commodity object storage performant.

## A Real-World Logging Example of Jevons Paradox

Let’s take a look at a specific use case where increased efficiency and accessibility have dramatically increased the value of data that was traditionally discarded: CDN logs.

CDNs generate a lot of log data. Global enterprises such as media providers can generate many terabytes of CDN log data every day. And events like the [Super Bowl can generate](https://hydrolix.io/blog/hyperscale-logging/) hundreds of terabytes of CDN log data over the span of just a few hours. Traditionally, CDN log data wasn’t retained because it was too expensive and, therefore, low value. Why would enterprises monitor the CDNs handling deliverability, increased security and reliability on their behalf?

But as modern solutions like Hydrolix made it more cost-effective to retain full-fidelity CDN logs, enterprises began retaining them, and their value became more obvious. They can be used to detect issues like DDoS attacks and monitor performance for use cases like CDN switching.

These are just a few short-term use cases. Meanwhile, enterprises that are retaining CDN logs long-term can use these logs to better understand their users’ behavior and preferences. With a long enough time frame (a year or more), it’s possible to get deep insights into cyclical events like seasonal sales, product releases and other high-revenue, high-impact events that can make or break the bottom line.

The enterprises retaining these logs now have vast, petabyte-scale datasets that can be used for training AI models, giving them a competitive edge over the enterprises that don’t have this data at their disposal. Enterprises in streaming media, broadcasting and other verticals are now analyzing this data for deeper insights.

CDN log data contains valuable information like IP addresses and records of all HTTP requests, including the assets requested, making it possible to create detailed user profiles. AI models can be used to better understand which accounts are at risk of lapsing or which new products best appeal to individual customers, and then send personalized emails or place targeted ads. And CDN log data may contain unusual outliers, such as low-and-slow attacks and other malicious behavior that can be detected over extended periods. AI models can detect and respond to these security anomalies more quickly.

In the span of a few years, CDN log data has gone from a high-cost source of “throw-away” log data to a valuable commodity that can support better performance and security and provide in-depth training to AI models. And this has been made possible by the theory behind Jevons paradox. As modern solutions like Hydrolix make it more cost-effective to ingest, store and analyze big data, it’s becoming an increasingly valuable commodity, and consumption will continue to rise. The enterprises that don’t effectively maximize the value of their data will be left behind when it comes to developing AI models.

## Quality Data in the Age of AI

Quality data is crucial for building AI models — but poor data quality is a huge issue for many enterprises. According to the Gartner report, “[Become AI-Ready by Focusing on Foundational Data Tools and Technologies](https://www.gartner.com/en/documents/5923775)” by Zain Khan, “Through 2025, poor data quality will persist as one of the most frequently mentioned challenges prohibiting advanced analytics (e.g., AI) deployment.”

For many types of data, it takes time to generate large, quality datasets. Consider weather data as an example. A week or month’s worth of weather data simply isn’t going to be very useful for an AI model. A model trained on data in the summer will be inaccurate during every other season. It will have no data on long-term trends such as climate change or patterns in extreme weather events.

Now apply this analogy to sales or operations data. Data from a sale in the summer may be wildly inaccurate for an equivalent sale in the winter. And subtle, long-term trends such as shifts in demand, users, performance and malicious behavior will be undetectable.

Many business leaders want agentic AI and revenue-generating AI models now — but if enterprises don’t have long-term, quality data, they are already well behind the curve, and they won’t be able to create these models yet. It simply isn’t possible to build a quality model without quality data. And because of the old, restrictive data paradigm where data was often discarded, many enterprises don’t have the data they need.

As the well-known saying goes, the best time to plant a tree was 20 years ago, and the next best time is now. Enterprises that are still discarding data due to high costs must rethink their approach and adopt modern data solutions that allow for long-term retention and readily available data regardless of its age. They must plant those seeds today. Some of that data will have obvious value for AI models, but the value of data won’t always be readily apparent or easy to quantify — at least not yet. However, the data that enterprises are retaining today will grow into tomorrow’s AI models. There will be some surprising seedlings in the mix that will create new revenue streams and products. Don’t miss that opportunity by throwing data away.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/01/9da8c52f-cropped-67e0f9d4-franz-knupfer.jpeg)

Franz Knupfer is director of Content and Research at Hydrolix, a streaming data lake for log and event data. Prior to Hydrolix, he taught and was director of curriculum at a code school, and has also worked in the observability...

Read more from Franz Knupfer](https://thenewstack.io/author/franz-knupfer/)