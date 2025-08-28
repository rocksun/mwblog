Just a few years ago, many enterprises were working toward consolidating log data into a single observability platform. By bringing all their data together in one platform, users would get unified dashboards and the ability to correlate and analyze all their telemetry data in one place. There’d be no more tool fragmentation or chair swivel. And premium observability solutions offered beautiful user interfaces that made the appeal of consolidation especially tantalizing.

However, sending all that telemetry data to a single premium solution comes with a big catch: high costs, especially for [large volumes of logs](https://thenewstack.io/whats-driving-the-rising-cost-of-observability/). As log volumes continue to grow, premium observability platforms have [become too costly](https://thenewstack.io/observability-can-get-expensive-heres-how-to-trim-costs/) and enterprises are looking to reduce the total cost of ownership (TCO) of observability. And many traditional observability platforms have challenges handling the scale of data that’s common today.

As a result, storing data in a single premium platform is no longer the trend. In fact, the opposite is true. Enterprises are moving away from using a single observability platform and toward a tiered approach that stores and analyzes log data in multiple solutions. It’s important to note that this approach shouldn’t be confused with hot/cold [storage systems, where data is kept in different availability tiers](https://thenewstack.io/stop-freezing-your-data-to-death/) to reduce costs.

Instead, this approach divides data into gold, silver and bronze tiers, with the most valuable “gold” data sent to premium observability solutions, while “silver” and “bronze” data are sent to more cost-effective logging solutions or stored in structured data lakes. To save money, enterprises are sending just a small fraction of their observability data to premium platforms — typically under 10% — and sending the rest to more affordable solutions, allowing them to rein in costs.

## Why Enterprises Are Moving Toward Tiered Observability

Multiple trends are driving the push for tiered observability. Enterprises are dealing with high costs for premium [observability platforms along with massive growth in log volumes](https://thenewstack.io/observability-2-0-or-just-logs-all-over-again/). According to the Gartner report, “Get Your Observability Spend Under Control,” “Observability costs are high and are increasing exponentially. In 2024, the median Gartner client spending on observability platforms exceeded $800,000 annually with a single vendor, marking an increase of 20% year over year.”

A large part of the cost increase is due to rising volumes of log data. The report also mentions, “A significant portion of costs is driven by the explosion in telemetry volumes and velocity, often accelerated by a shift to modern architectures and applications. Traditional approaches to telemetry ingestion are inefficient and are no longer suitable for these workloads.”

[As of 2023](https://observability.edgedelta.com/hubfs/Collateral/Charting-Observability-2023.pdf), 37% of enterprises were already ingesting more than a terabyte of log data per day, with 15% of enterprises generating more than 10 terabytes per day. Those numbers have surely gone up in the last few years, and at least a terabyte per day is increasingly the norm for enterprises, not the exception.

According to the Gartner report, “Focus on Telemetry Pipeline to Achieve Success in Your Observability Initiative,” “As organizations continue to transition their infrastructure toward the cloud and transform their observability strategy, the volume, velocity and variety of telemetry data has also increased. Ten years ago, contracts were about 10s [tens] to 100s GBs of logs per day. But today, it is 10s to 100s of TBs.”

So the primary goals of tiered observability are to rein in costs and address the rising volumes of data. But how can enterprises best implement tiered storage without returning to the very pain points that make premium observability platforms so attractive in the first place? Before answering that question, let’s first break down the tiers of tiered observability — and then see how the silver tier provides the versatility needed to balance cost and user experience.

## Breaking Down the Tiers of Tiered Observability

Tiered observability typically comes in three or four tiers: gold, silver and bronze (with platinum occasionally thrown in). Let’s take a look at the three-tier structure.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Tier** | **Priority** | **Solution Type** | **Storage/Retention/Availability** | **Cost** | **Examples** |
| Gold | Revenue-generating, with no tolerance for downtime | Premium observability platform | Short-term retention, stored in SaaS solution, high availability | High, especially at scale | Splunk, Datadog |
| Silver | Important, with limited tolerance for downtime | High-volume OLAP/log analytics solution | Long-term retention, cost-effective object storage, high availability | Cost-effective | Hydrolix, ClickHouse |
| Bronze | All other data | Structured data lakes, open table formats | Long-term retention | Cost-effective | AWS S3 with open table format, such as Apache Iceberg |

The gold tier is reserved for the most mission-critical observability data, where any outages will lead to lost revenue. This data is stored in premium platforms designed specifically for observability, with extensive visualizations, alerts and correlation capabilities. Only a small fraction of data should be stored in this tier (typically under 10%, with less being better). The primary reason is cost, but it’s not the only reason. Another significant reason is that observability platforms tend to be walled gardens. They do observability very well, but they aren’t designed to make data available for use cases like data science and machine learning (ML) training. As a result, data either needs to be exported to other solutions (often leading to additional data pipelines and costs) or its use remains limited to observability.

The silver tier is, in many ways, the most versatile and important tier, and not just for its potential cost savings. The silver tier is typically reserved for data that is important but not as mission-critical for observability as the gold tier. Solutions in this tier are often online analytical processing (OLAP) solutions or have many elements of OLAP, such as highly efficient columnar storage designed for write once, read many (WORM) use cases. Logs, which should be immutable by design, are a perfect example of a WORM use case.

Silver-tier solutions are increasingly building on cost-effective object storage while providing the scale for real-time data ingestion and analytics. Unlike premium observability solutions, they are multipurpose, an advantage when it comes to democratizing data and making it available where it’s needed, whether that’s a premium observability platform like Splunk or an analytics platform like Databricks.

They don’t offer fully developed observability offerings, so there is a potential trade-off when it comes to applying a full observability suite to silver-tier data. Ideally, they include integrations or the ability to federate data in premium observability solutions so ops teams still have access to their favorite tools and visualizations.

What about log data that’s mission-critical for multiple use cases, not just observability? It may actually be better to store in a silver-tier solution that’s interoperable for those use cases instead of sending it to a gold-tier solution, where it’s only used for observability before being discarded due to limited retention periods.

Finally, the bronze tier contains all other data — data that is most likely write once, read never (WORN). It may be data that’s mainly kept for compliance or potential forensic analysis if there’s a breach. Or it may be log data for lower-priority services where downtime isn’t as much of an issue.

While it can be sent to an unstructured data lake and queried with a service like [AWS](https://aws.amazon.com/?utm_content=inline+mention) Athena, this isn’t an efficient method for real-time analytics. By adding structure with open table formats like Apache Iceberg, queries are considerably more efficient. And one of the goals of open table formats is high interoperability, though work still needs to be done to provide that interoperability to users.

Ultimately, both silver- and bronze-tier solutions should offer cost-effective, highly scalable data ingest, storage and analytics. There should be a high degree of interoperability, including with observability platforms, visualization tools (such as Grafana), data analytics platforms (such as Databricks and [Snowflake](https://www.snowflake.com/?utm_content=inline+mention)) and AI/ML development tools, such as MLib and other tools in the Apache Spark ecosystem.

In theory, silver-tier solutions provide faster analytics and higher availability at a slightly higher cost, while bronze-tier solutions are more cost-effective at the expense of availability and speed.

But the lines quickly blur due to the high level of innovation in the areas of data analytics and storage. OLAP-style solutions can provide bronze-tier cost-effectiveness because they are essentially optimized data lakes using extreme compression and built on object storage. And open formats like Iceberg provide the foundation for fast, cost-effective lakehouses.

Ultimately, enterprises really just need a solution optimized for log analytics that’s cost-effective, fast and interoperable. The right solution can provide the best of both silver and bronze, simplifying the concept of tiered observability and making it much more manageable for teams to put in place.

## Tiered Observability With Unified Insights

A tiered approach can come with extra complexity, and many teams may be (rightly) worried that they’ll once again be stuck with fragmented insights. Premium observability platforms offer integrations and an agented approach that can make observability seem relatively effortless. And enterprises may wonder if using multiple solutions will take more technical resources to set up, maintain and use. These are all reasonable concerns, and there are ways to mitigate them.

* **Silver and gold may be enough:** As mentioned in the previous section, silver-tier solutions are building on cost-effective [object storage and using extreme compression to reduce costs](https://thenewstack.io/object-storage-is-key-to-taming-cloud-costs/). That means managing just two tiers, not three — a premium observability solution and a cost-effective log analytics solution. In this way, tiered observability is really still about the best practice of centralizing logs — except most of the logs are centralized outside of premium observability solutions.
* **Data federation and interoperability are crucial:** By focusing on interoperability and a [federated approach](https://thenewstack.io/observability-isnt-enough-its-time-to-federate-log-data/) to querying data, teams can visualize and analyze data using their preferred tools. As an example, combining a [Splunk connector with a cost-effective analytics solution](https://hydrolix.io/blog/visualizing-hydrolix-data-in-splunk/) can allow teams to query and visualize their data in Splunk using Splunk Search Processing Language (SPL). This reduces tool fragmentation and helps unify insights.
* **DIY isn’t necessary:** For enterprises that don’t have the technical resources to commit to a DIY approach, there are turnkey log analytics solutions that are highly scalable. It’s not necessary to build and tune a lakehouse from scratch, though that option does exist and can be the right approach for some enterprises. And for those looking to DIY, the good news is that open source tools like Apache Iceberg are making it easier than ever to build performant data lakes. However, keep in mind that building and maintaining a streaming pipeline designed to scale huge log volumes in real time can remain a major gotcha.

As silver- and bronze-tier solutions continue to focus on interoperability, enterprises will increasingly be able to get the best of both worlds: cost-effective ingest and storage combined with insights from premium observability tools.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/01/9da8c52f-cropped-67e0f9d4-franz-knupfer.jpeg)

Franz Knupfer is director of Content and Research at Hydrolix, a streaming data lake for log and event data. Prior to Hydrolix, he taught and was director of curriculum at a code school, and has also worked in the observability...

Read more from Franz Knupfer](https://thenewstack.io/author/franz-knupfer/)