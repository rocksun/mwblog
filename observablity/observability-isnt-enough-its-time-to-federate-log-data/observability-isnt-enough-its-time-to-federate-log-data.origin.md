# Observability Isn’t Enough. It’s Time To Federate Log Data
![Featued image for: Observability Isn’t Enough. It’s Time To Federate Log Data](https://cdn.thenewstack.io/media/2025/01/2382f5c2-log-1024x576.jpg)
Over the last decade, observability has gone from being a [buzzword to a best practice](https://devops.com/observability-matters-but-are-you-observing-the-right-things/). And enterprises are reaping the benefits with faster mean time to resolution (MTTR), [better user experience ](https://intellyx.com/2024/11/20/in-todays-real-time-multicloud-world-who-owns-the-customer-experience/)and less downtime.

[Observability](https://thenewstack.io/observability/) is now table stakes — customers expect nothing less than smoothly running applications, no matter how big the event. Enterprises looking for a competitive advantage need to find ways to use their observability data for other use cases, not just for compliance and security purposes, but for active analysis, business intelligence (BI) and training [machine learning models](https://thenewstack.io/llm/).
So what do enterprises need to do to extract more value from that data for valuable use cases like predicting customer churn, systems capacity and inventory needs while detecting issues like threats and anomalies? These are the kinds of questions that must be answered to determine whether a business will thrive or fail.

## Observability Platforms Don’t Work for Data Federation
For enterprises that are already sending log data primarily to observability platforms, a potential first step is to export data to a data lake, and then use tools like [Apache Spark](https://thenewstack.io/apple-comet-brings-fast-vector-processing-to-apache-spark/) and [Databricks](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/) to analyze that data further. But exporting data adds additional complexity and costs, not to mention the potential security risk of moving data around.

Instead, the best practice is data federation. With data federation, you can query data across many different sources without moving it. With this approach, no additional pipeline is needed; there are no egress costs and none of the security risks that come with migrating data.

Most importantly, your teams aren’t blocked from accessing and analyzing the data they need to do their jobs.

Some observability platforms such as Splunk are embracing the move to federated data. But many platforms remain walled gardens. Even when they’re able to connect with other analytics platforms designed for BI, machine learning and data science, they typically won’t have the high-fidelity, long-term data that’s required for those use cases.

That’s because it’s typically too expensive to retain data very long in the first place, and practices like downsampling are common, lowering the fidelity and quality of stored data.

They are observability platforms first and foremost, which they should be, and they aren’t designed for storing big data for long-term analytics. However, log data has become big data — not just for the businesses that are ingesting terabytes of log data every day (and often quickly discarding it due to high costs), but for the most innovative enterprises that are looking to gain new insights from petabytes of log data kept in data lakes and warehouses.

As a result, keeping log data in an observability platform and then exporting it or federating it to another analytics platform isn’t really an effective approach.

## Using High-Performance Data Lakes for Federation
Instead, the answer is to keep that log data in a storage solution that works for both real-time and long-term analytics. With the right storage solution, data federation can be the glue that brings observability and unified analytics together into a truly comprehensive view that gives your business a competitive edge.

But what constitutes the right storage solution?

The solution must be cost-effective to keep data long term, which typically means using cheap commodity object storage — in other words, a data lake.

However, traditional data lakes, while cost-effective, don’t work well for real-time analytics, and it can be challenging to analyze huge volumes of data quickly as well, so data lakes aren’t always effective for unified, long-term analytics either.

So in addition to being cost-effective, they must have high performance with the ability to query data, whether it’s a minute or a year old.

Recently, AWS introduced S3 Tables to improve the performance of object storage. The [jury is still out on how impactful S3 Tables will be](https://dataengineeringcentral.substack.com/p/aws-s3-tables-the-iceberg-cometh) — and whether [compute for tasks like compaction could drive up costs more than expected](https://meltware.com/2024/12/04/s3-tables.html) — but it’s a major step in the right direction. The same can be said for other open table formats like [Iceberg](https://thenewstack.io/how-apache-iceberg-and-flink-can-ease-developer-pain/), which are dramatically improving the performance of querying object storage, though it’s still necessary to build separate real-time streaming pipelines for ingesting data.

The age-old axiom still prevails: Use the right tool for the job. A data lake like S3 Tables can have many generalist advantages, but it still won’t provide the same level of performance that a solution designed specifically for log data can. With data federation, you can pick and choose different tools for different kinds of data depending on the use case, so there’s no need to limit yourself to one solution. For instance, your organization may combine a mixture of data lakes and specialized solutions depending on the data type and use case.

## Not Just a Single Pane of Glass for Observability
Observability platforms often tout the ability to see all your operational data using a “single pane of glass.” While data federation can help provide a unified view for operations, [monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/), this single pane of glass shouldn’t come at the expense of having other tools to analyze and understand your data.

Typically, the data ingested into an observability platform is no longer readily available for other use cases like long-term analytics, as this graphic shows.

With this approach, the goal of log and telemetry data is for it to be analyzed (and usually stored) in an observability platform. The majority of that data is ingested and kept for a short period of time (typically a few months at most) before it’s discarded, aggregated or moved to frozen storage.

In this model, the observability platform is the be-all, end-all. While using data federation to provide a single pane of glass can increase support for more ingest sources, provide compatibility with cost-effective log storage solutions and improve security by minimizing the movement of data, it assumes that the sole value of telemetry data is for systems observability.

But what about the data analytics platforms, machine learning models, billing systems and other tools that can extract additional value from that data? To make this data accessible for these use cases, observability platforms can’t just be the federated backend for telemetry data — they must also be a federated frontend for platforms like Databricks.

## Observability Is Just One Stop in the Journey
The following graphic illustrates how an observability platform can have the capacity to both ingest data and be a federated backend for data sources while also being a federated frontend for other tools such as data analytics platforms.

As discussed previously, observability platforms simply aren’t structured to store data for other analytics tools. This is in large part because they aren’t designed for long-term retention or cost-effective storage for large volumes of data. And they’re built around a limiting paradigm where telemetry data only has value for a short time and only for observability.

A more effective approach for federating log data looks like this.

With this approach, a cost-effective log storage solution designed for scale is the preferred resting place for large volumes of log and event data. Observability solutions are one, but not the only, frontend for analyzing federated data.

This approach — where storage and the UI/analytics are decoupled — can be considered “headless observability,” but it involves a major paradigm shift for observability solutions. In this paradigm shift, they are no longer focused on storing data — or if they are, they must develop integrations with other analytics tools while providing long-term, cost-effective storage.

With the current paradigm, using an observability platform as a “single pane of glass” for all your log data will preclude using that data for long-term analytics. At the same time, you still need observability tools because platforms like Databricks just won’t give you the same level of application monitoring that an observability platform can.

Forward-thinking organizations will adopt a mix of analytical frontends (for example, Splunk and Databricks) and data storage solutions. Regardless of the use case, and whether they are frontend, backend or both, solutions must have the following qualities:

**They must embrace data federation.**In the case of analytical frontends, that means the ability to connect with many different backend data sources. And often it will also mean being a backend data source for yet another analytical frontend. Observability solutions that are unable to be a backend data source for other analytical frontends should embrace a shift to “headless observability” where they query but do not store data.
In the case of storage backends, that means having rich ecosystems of connectors and integrations that allow for querying data in other analytical tools without exporting it. In other words, integrations must support both *ingest* from other sources and sending *analytics* to other sources.

**They must combine performance and cost-effectiveness.**Enterprises can store data cheaply in data lakes, but until recently, the trade-off was lower query performance. Alternatively, they could use tightly coupled local storage for performance, but that quickly led to high costs for larger volumes of data.
The new paradigm involves finding ways to maximize the performance of cost-effective commodity cloud storage to make it performant for both real-time and historical analytics. This is now a basic requirement, at least when it comes to log storage solutions.

In the case of analytical frontends (such as observability platforms that still rely on expensive, tightly coupled storage), that means accepting that they aren’t always the right tool for storing data, but they can still provide a powerful UI for analytics and offer value with features ranging from anomaly detection to a full suite of observability products.

When evaluating new solutions across observability, cybersecurity, analytics and log storage, these considerations should be top of mind for enterprises. For enterprises that are stuck in contracts with observability or other platforms that don’t provide data federation, it’s time to seriously consider new solutions or risk losing out to companies that can more effectively make data-driven decisions.

For the enterprises offering solutions in these spaces, supporting data federation and building rich connector ecosystems is a basic requirement for future growth. The walled garden approach that many observability platforms have taken will no longer work. While it may create vendor lock-in (and short-term profits) for the platforms that take this approach, it will also come with higher costs and lower value — not a winning recipe for future growth.

These enterprises will also have to take a long, hard look at pricing models that penalize customers for expensive, tightly coupled storage architectures and instead provide pricing that better aligns with value.

Finally, for both customers and platforms, there is a final, crucial consideration in play when it comes to connector ecosystems. Does a platform’s ecosystem focus first and foremost on bringing value to customers through best practices like data federation? Or does it instead push customers into greater reliance on the platform (making it easier for data to come in, but not go out), hoping that the garden will be attractive enough to hide the walls?

Ultimately, it’s not the size of the ecosystem that matters, but whether the connectors it contains allow your teams to work with data when and where they need it. And that means using these ecosystems to extend the value of telemetry data beyond observability.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)