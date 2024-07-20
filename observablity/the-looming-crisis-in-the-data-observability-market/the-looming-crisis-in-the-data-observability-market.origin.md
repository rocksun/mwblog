# The Looming Crisis in the Data Observability Market
![Featued image for: The Looming Crisis in the Data Observability Market](https://cdn.thenewstack.io/media/2024/07/7a834647-market-2494520_1280-1024x682.jpg)
The [observability market](https://thenewstack.io/observability/) is on the rise. Research firm MarketsandMarkets forecasts that the market will [grow from $2.4 billion in 2023 to $4.1 billion by 2028](https://www.marketsandmarkets.com/Market-Reports/observability-tools-and-platforms-market-69804486.html) at a Compound Annual Growth Rate (CAGR) of 11.7%. KBV Research is also bullish on this market, predicting it will [grow at a CAGR of 12.3% to reach $5.1 billion in 2030](https://www.kbvresearch.com/observability-tools-and-platforms-market/).

Those estimates almost certainly undervalue the market. For instance, Datadog’s 2023 revenues, which are just one of several players in this market, are out of line with those market estimates. Datadog’s revenues topped $2.1 billion in 2023, and while [the vendor is a leader in the space](https://thenewstack.io/datadog-brings-big-observability-directly-to-your-phone/), it certainly isn’t a monopoly power gobbling up an 88% market share.

The observability market is most likely undervalued for a combination of benign and troubling reasons. Analysts slice and dice observability differently on the benign side of the ledger, so it’s natural that their estimates vary, especially for a market amid rapid change.

A more troubling reason the market may be undervalued, however, is because the vendors themselves are limiting the overall value of [observability](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/), mainly due to how they lock data into silos and limit the use cases for observability to the lowest-hanging fruit.

In complex, cloud-based, data-driven environments, observability is the key to keeping various systems running smoothly, but current observability tools limit what insights you can gain with your data. Modern, cloud native observability platforms have [emerged](https://thenewstack.io/rethinking-observability/) that can gather telemetry data, such as logs and traces, and then analyze that data to deliver actionable insights about the state of infrastructure and applications. IT and DevOps teams can use those insights to fix problems, improve availability, and optimize performance.

The [traditional monitoring market](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/) was developed in silos, with separate tools needed to monitor networks, applications, security, etc., and observability was supposed to help break those silos down. The trouble is that current observability tools still lock data into silos, present the insights the vendors think you should have rather than ones you know you need, and they build walled gardens that lock out other tools and data.

Not long ago, simply gathering actionable, real-time data from these sources was enough to sell software licenses, so vendors rushed to snatch the low-hanging fruit. Still, by valuing speed to market over all else, vendors built brittle, proprietary observability tools that are bumping up against their limits.

As the market evolved, the shift from monitoring to observability was, in theory, supposed to help organizations break free from those silos to unlock more value out of existing systems. In its 2023 Magic Quadrant for APM and Observability, research firm Gartner noted that as the market redefines itself around observability, a fundamental break from traditional monitoring is that “observability-centric solutions support an exploratory, analytics-driven workflow that may bear more resemblance to business intelligence (BI) than IT operations.”

This is an important vision for the future, but today’s market is still greatly hampered by legacy path dependencies.

**Data Observability Today: The High Cost of a Fractured Market**
The [data observability](https://thenewstack.io/what-is-data-observability-and-why-does-it-matter/) market is currently dominated by a handful of vendors, including Datadog, New Relic, and Splunk. These vendors meet the critical need of monitoring organizations’ infrastructure and applications.

The problem is virtually no interoperability between any of these vendors’ systems. Because data observability tools emerged to target specific monitoring and observability use cases (application, network, security, etc.), vendor platforms developed path dependencies and numerous lock points, making it difficult, if not impossible, to break down silos.

The need for interoperability also means that observability tools are expensive to deploy, labor-intensive to run, and difficult to leave for a competing solution. Moreover, many tools are needed to deliver significant insights and provide ROI. In a 451 Research report, “Observability platform products and services could disrupt adjacent sectors,” researchers found that most enterprises must invest in multiple monitoring tools to gain a holistic view of their digital systems.

However, the term “holistic” is misleading since these tools provide limited insights into what is happening in these systems, often telling you little more than whether or not everything is currently up and running.

While Gartner may see a future where analytics-driven workflows look more like BI than ITOps, the market is not there yet. While enterprises feel the immediate pain of rising observability costs, the real problem is the long-term loss of value. The value of data erodes because it is locked into proprietary systems. Thus, enterprises can’t do things like take insights from BI and automatically apply business contexts to network observability. This is technically feasible, but it’s practically impossible in closed systems.

The lack of interoperability leads to a lack of control, which in turn leads to a lack of scalability and innovation.

**Building Upon the 4 Key Functionalities of Observability**
The evolution from traditional monitoring to observability is built on four key functionalities: instrumentation, processing/analysis, storage/query, and action. This framework is understood throughout the industry, but today, each vendor handles each common functionality differently.

The four key functionalities that any enterprise-grade observability platform must include are:

**Instrumentation:**An observability solution requires the proper instrumentation to generate telemetry data that helps organizations gain visibility into system behavior and identify potential issues.**Processing/Analysis:**After telemetry data is generated, the following stop data takes as it travels through the observability pipeline to apply advanced analytics techniques to extract meaningful patterns and actionable insights.**Storage/Query:**Data is stored next, where users can query raw telemetry data and derive insights for historical analysis and trend identification.**Action**: Finally, the whole point of collecting and analyzing data is to take action. Observability data enables users throughout the organization to take timely and effective action based on insights. Actions include things like automated remediation and alert triggering.
By leveraging these critical capabilities of observability, enterprises can, among other things:

- Proactively identify and address potential bottlenecks
- Reduce mean time to resolution (MTTR)
- Drive continuous improvement
- Streamline workflows and improve response times
- Automated labor-intensive, error-prone repetitive tasks
- Automatically optimize performance
Each of those four functionalities is necessary to gain insights into what is happening in applications, networks, infrastructure, security devices, and more. Still, each functionality also represents a point where data gets locked into proprietary siloes.

While these lock points benefit vendors, their development isn’t a nefarious conspiracy. Rather, as these systems developed, each focused on separate use cases and relied on different, often proprietary programming languages, APIs, and data formats.

Another reason lock points continue to bedevil this market is that vendors focused their development efforts on offloading and storing vast volumes of data, creating proprietary systems while overlooking how important data portability and sharing are to analyze trends truly.

Today, observability tackles so many moving parts that complexity is more than just under the hood; it is technical complexity. Instead, observability complexity means that software engineers must save countless hours managing various dashboards and alerts because critical data is trapped in different systems, and the data insights are, thus, limited.

To break free from these silos, scale to serve a broader market, and unlock value currently constricted by proprietary choke points, observability solutions need to be interoperable throughout the pipeline. They need to interoperate to provide holistic views of the entire digital business while offering the ability to view and manage these tools through a standard interface.

Fortunately, there is a shortcut to broad interoperability, and it has been used successfully before: open standards.

**From Silos to Platforms to Operating Systems**
As cloud computing and digital transformation initiatives have spread throughout the economy, several technologies have benefited from moving from proprietary systems with poor integration to a platform approach to cloud management, cybersecurity, and WAN connectivity.

Platforms bring numerous benefits, but when they emerge in any given market, they should only be considered a middle step before reaching the true destination: open standards that enable interoperability not just within but also among those platforms.

When platforms begin to displace point solutions, they still lock data and users into the platform. The platform benefits, such as converged features, greater efficiencies, and the ability to manage multiple capabilities through a single pane of glass, only apply to the single-vendor platform. Next, vendors typically build out partners and attract complementary service providers to their product ecosystems, but these ecosystems are built around vendor-specific requirements.

What happens if you want to switch platforms but have a third-party add-on you wish to take along? You’re out of luck if that add-on isn’t in the other ecosystem. What if you’ve acquired another company using a different platform and like to merge the two? Good luck doing that on your own, and if you expect the platform provider to handle it for you, expect professional services costs to skyrocket. Even with platforms, users remain locked in, switching costs stay high, and choices are limited until standards and openness begin to clear the proprietary fog.

This is why, at the next stage of market evolution, when users get fed up with skyrocketing proprietary costs, cheaper open source alternatives tend to emerge. The open options usually offer fewer features and aren’t suitable for organizations that lack developer and IT skills. Still, they do impact larger organizations because they spur vendors to begin the process of standardization.

Once that happens, you’ll invariably see platform providers jockeying to embrace standards and become the standards. Look at any complicated software market, from cloud to Big Data to virtualization, and you’ll see vendors positioning themselves as the market’s operating system.

For some, this is simply a marketing exercise. Still, the truth is most complicated technologies would benefit from an operating system that automatically handles the many tasks that bog down engineers today.

**Could OpenTelemetry Serve as the Foundation for an Observability OS? **
The silo-to platform to standards path is a well-trod one. Still, the observability market has a unique opportunity to blaze a shortcut to openness and portability.

There is already an open observability project that could help pave the way toward an open, scalable observability market: OpenTelemetry, a Cloud Native Computing Foundation project. [OpenTelemetry (OTel)](https://opentelemetry.io/docs/what-is-opentelemetry/) is an open source observability framework with standardized protocols, and it is currently the second most popular open source project today, behind only Kubernetes.

OTel defines consistent formats for instrumenting, generating, gathering, and exporting telemetry data, such as metrics, logs, and traces, to monitoring platforms for analysis. With additional capabilities, OTel’s common framework could efficiently serve as the foundation for a larger telemetry compute layer that handles scheduling, queuing, formatting, etc., all based on open standards.

Interestingly, the reason OTel was created in the first place was to free observability from two existing silos: OpenTracing and OpenCensus. In 2019, OTel was formed to merge those two projects, creating a single open integration framework for end-to-end distributed tracing telemetry, and it became generally available in November 2023.

Using OTel to mature the space rapidly isn’t pie-in-the-sky utopian thinking. The project already has broad support. Backers of OTel include DataDog, Google, IBM, New Relic, Splunk, and many others.

Now, tools built on OTel can collect, export, and analyze telemetry data from any source. With OTel, enterprises own the data they generate, with no vendor lock-in at any point along the [observability and monitoring](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) path. Developers who build on OTel only have a single set of APIs and data conventions to deal with.

**Openness Will Unlock Value in the Observability Pipeline**
Enterprises should push for standards and openness from observability. The reason isn’t simply technical. The real problem with closed systems is that they limit value. Today, enterprises express grave concerns about skyrocketing observability costs because they are locked into overpaying for different tools that do the same task in other areas of the organization.

In contrast, tools that adhere to OTel are beginning to emerge, and these are better able to collect, export, and analyze telemetry data from any source. With the spread of OTel and the development of a standard observability operating system, enterprises will own the data they generate, with no vendor lock-in at any point along the observability and monitoring path.

Today, the reality is that costs are skyrocketing because the network team will use one tool, security relies on something else, and e-commerce prefers yet another. Each team needs observability to optimize performance, but they wouldn’t need to keep overpaying for duplicate tools if they genuinely owned their data.

This means that it is vitally essential for observability buyers to insist on open standards and APIs in general and OTel in particular for observability. Otherwise, the silos that observability platforms were designed to break down will reform around different capabilities and vendor ecosystems, and free and easy data portability will be lost yet again.

Many other markets, from servers to IaaS to containers, exploded once open standards replaced proprietary systems. The same opportunity is at hand for the observability market — if we take it.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)