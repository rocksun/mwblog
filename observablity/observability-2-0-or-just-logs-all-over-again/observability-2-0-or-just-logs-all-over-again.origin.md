# Observability 2.0? Or Just Logs All Over Again?
![Featued image for: Observability 2.0? Or Just Logs All Over Again?](https://cdn.thenewstack.io/media/2025/05/89c03043-observability-2-logs-1024x576.jpg)
Lately, there’s been a lot of talk around Observability 2.0 and a broader transformation from the three ([or four](https://thenewstack.io/elastic-profiling-agent-offers-a-4th-pillar-of-observability/), depending on who you ask) [pillars of observability](https://thenewstack.io/observability/#three-pillars) towards a unified source of truth: [arbitrarily wide, structured log events](https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes).

If we boil this down, we’re right back to where we started — kind of. In the beginning, there were logs, and now we’ve come full circle, with wider logs (structured, high-dimensionality time series events) and more of them than ever before (plus high cardinality). So, how did we get here? And where exactly are we headed?

## The Three Pillars of Observability
The three pillars of observability are ** logs, metrics and traces**. If you really want a clever acronym, you add in

**events**to create
**MELT**. However, the basic building block of the observability universe has always been logs. And I’d argue that the evolution of the three pillars has really been an arbitrary approach to dealing with the real issue that needed to be solved: how to get real-time insights into high-volume, high-cardinality time series data.
Back in the early 2010s, when the first wave of observability was emerging, large companies had Splunk, which excelled at centralizing and processing logs. It’s worth reflecting that Splunk had its IPO in April 2012 and was already doing more than $100 million in annual revenue at that point. (Even back then, enterprises were already concerned with the high cost of Splunk, and the volume of logs for most businesses has absolutely exploded since that time.)

But that first wave of observability was more about all the things you *couldn’t* do with logs. It just wasn’t possible to quickly do analytics and aggregations on large volumes of log data.

To solve that problem, we added another pillar, metrics. When I cofounded [InfluxData](https://www.influxdata.com/?utm_content=inline+mention) in 2012, there was a nascent wave of innovation happening within time series databases, which would move away from Graphite/Whisper and lead to things like InfluxDB, Prometheus, Timescale and Facebook’s Gorilla. These tools were intentionally optimized for storing metrics and performing aggregations, and you could provide teams with a holistic view of system health through metrics like average request latency and total errors. This hyper focus was intended to fill the gaps in traditional log management systems.

But you couldn’t use these systems to search strings or drill into logs. Numerical time series data could give you a holistic view, but it didn’t include the granularity to provide root cause analysis so that you could actually fix issues when they came up. And in most cases, these systems dealt with the problems of high volume by creating summary aggregations and discarding the underlying raw data.

The third pillar, distributed tracing, was designed to solve the problem of root cause analysis in distributed systems. Google’s [Dapper paper](https://thenewstack.io/trace-based-testing-the-next-step-in-observability/) was released in 2010, and [Zipkin](https://thenewstack.io/jaeger-vs-zipkin-battle-of-the-open-source-tracing-tools/), another early distributed tracing tool based on the Dapper paper, was open sourced in 2012. Distributed tracing allowed teams to trace requests flowing through an application, making it easier to identify bottlenecks and problems.

From the perspective of high-cardinality, high-volume data, distributed tracing was supposed to help teams sift through the noise and drill down into the details that mattered. But tracing solves a very discrete set of cases well — and everything else badly. It doesn’t help with metrics or logs. And for systems that handle high request volumes, traces can also explode the volume of data further and create even more noise. Sampling (randomly keeping only a small percentage of the traces) can theoretically help solve that problem, but then you are once again losing the benefit of full-resolution observability.

Altogether, the three pillars can give you deep insights into your systems. But despite all the innovation and development, the foundation is wobblier than it should be — because none of the pillars actually addresses the real problem.

## The Three Pillars Don’t Solve High Cardinality
As observability solutions have ostensibly become more mature over the last 15 years, we still see customers struggle to manage their observability estates, especially with the growth of cloud native architectures. So-called “unified” observability solutions bring tools to manage the three pillars, but cost and complexity continue to be major pain points. Meanwhile, the volume of data has kept rising, with 37% of enterprises ingesting more than a terabyte of log data per day ([as of 2023](https://observability.edgedelta.com/hubfs/Collateral/Charting-Observability-2023.pdf)).

Legacy logging solutions typically deal with the problems of high data volume and cardinality through short retention windows and tiered storage — meaning that data is either thrown away after a fairly short period of time or stored in frozen tiers where it goes dark.

Meanwhile, other time series or metric databases take high-volume source data, aggregate it into metrics, then discard the underlying logs.

Finally, tracing generates so much data that most traces aren’t even stored in the first place. Head-based sampling retains a small percentage of traces, typically random, while tail-based sampling allows you to filter more intelligently but at the cost of efficient processing. And then traces are typically discarded after a short period of time.

There’s a common theme here: While all of the pillars of observability provide different ways of understanding and analyzing your systems, they all deal with the problem of high cardinality by [ throwing data away](https://thenewstack.io/the-top-four-consequences-of-discarding-data). If your systems are small and contained, then you’re probably fine — but in that case, too much observability tooling is probably overkill. For the biggest systems that observability is really supposed to help, the three pillars cost too much and deliver too little value.

Observability is all about understanding the state of a system based on its outputs. Throw the outputs away and you don’t really have observability anymore. You have three wobbly pillars, a whole lot of complexity and high costs — and for enterprises that have distributed systems, you still don’t have the true observability you were promised.

## Solving High Cardinality (And Dimensionality)
We don’t need to reinvent better versions of discrete metric, tracing and logging tools. We just need one tool that can solve all three problems.

In this way, we’ve kind of come back to the beginning. It’s really just about logs — wide, structured events. Put another way, observability is all about outputs, and those outputs are logs — metrics and traces can be derived from structured logs. You just need a tool that addresses the issue of query performance in the face of high-cardinality and high-dimensionality data.

### High Cardinality
High-cardinality data consists of many unique values — in other words, it combines high volume with high uniqueness. It’s harder to compress, leading to more data in storage and more compute-intensive reads for querying. We can kind of lump the issues of high volume and cardinality together as massive challenges of working with big data.

As we’ve discussed, most systems attempt to solve this problem by throwing data away or reducing its granularity. We’ll see platforms increasingly using AI to “intelligently” determine which logs to discard and to keep — in other words, trying to separate the signal from the noise. And while AI tools will be extremely useful for detecting patterns and insights, they shouldn’t just be another excuse to throw data away.

The answer instead is a solution designed to ingest, query and analyze massive volumes of log data while remaining cost-effective — all without throwing away the underlying raw data.

### High Dimensionality
For logs to provide the benefits we normally expect from distributed tracing, they need to be able to retain all necessary context. This includes the context needed to logically group and correlate logs together — and to trace a request through a system.

This is where “arbitrarily wide, structured log events” come into play. Logs can be high dimensionality (wide, with a lot of attributes) even without adding this additional context. We’ve seen logs with thousands of fields, and even those that may seem to have murky business value today could result in major regrets if your [data science team](https://roadmap.sh/ai-data-scientist) wants them next year, but you never retained them.

To accommodate varying degrees of dimensionality, even knowing that most users don’t know what data types their log fields are, you need a solution with a flexible schema, like a [data lake](https://thenewstack.io/stop-freezing-your-data-to-death). With a flexible schema, your logs can be arbitrarily wide, have any amount of dimensionality and have shifting data types over time.

To ensure performant analytics with high-dimensionality data, the solution should leverage columnar storage, which is typical for online analytical processing solutions (OLAP), as well as flexible indexing formats to support fields with varying dimensionality. Many OLAP features are a natural fit for log data. For instance, an immutable “write once, read many” approach ensures that logs remain a secure, unalterable source of truth while also improving analytical performance.

## Real-Time Analytics Is About More Than Observability
Ultimately, I don’t think Observability 2.0 is about building a new solution, but rather returning to the root of observability and enabling efficient, high-volume log processing combined with real-time analytics. When we think about log data through the lens of analytics instead of just observability, we can dramatically expand its value.

Log data isn’t just for ops teams focused on application performance, although that’s a mission-critical use case. Instead, it’s part of the bigger observability picture across the entire organization. Log data, and timestamped data in general, provide a foundational story about the past, present and future of your enterprise. Real user monitoring data (traditionally siloed in observability platforms) can provide insights for marketing, advertising and capacity planning. Transaction logs can help data science teams weed out fraud. Meanwhile, cybersecurity teams can use the same data for threat hunting and uncovering advanced persistent threats. And the bigger the data set, the more potential value it has for training AI/machine learning (ML) models for use cases like anomaly detection.

The costs for observability solutions that silo data keep going up. And the original approach for dealing with high volumes of data by throwing it away just creates more gaps for businesses during a time when they are demanding more insights from their data. The real answer is to build solutions that can process high-volume, high-dimensionality logs for real-time analytics while remaining cost-effective — and making sure that those logs are available wherever they are needed.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)