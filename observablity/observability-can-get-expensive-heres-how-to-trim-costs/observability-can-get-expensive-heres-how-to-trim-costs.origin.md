# Observability Can Get Expensive. Here’s How to Trim Costs
![Featued image for: Observability Can Get Expensive. Here’s How to Trim Costs](https://cdn.thenewstack.io/media/2025/02/6a790864-observability-expensive-2-1024x576.jpg)
Telemetry data feeds are beneficial for developers and operations teams. However, [observability](https://thenewstack.io/observability/) feeds come at a cost. Some large customers spend tens of millions of dollars annually on an observability solution. Depending on the observability provider, these costs may include security coverage.

CFOs and other financial decision-makers are scrutinizing this pay-as-you-go model increasingly, as they are under pressure to [reduce spending](https://thenewstack.io/a-diy-framework-for-optimizing-observability-costs/). As a result, DevOps teams are being asked to be more selective about [the telemetry data they pay for](https://thenewstack.io/whats-driving-the-rising-cost-of-observability/), focusing on observability and service analysis.

As customers and organizations demand more advanced features, they certainly won’t want to pay more. Instead, they will look for ways observability providers can help them reduce costs through better tools or practices.

Telemetry pipelines have already become a critical component of larger organizations’ observability strategies, particularly where there is a need to aggregate and process data from multiple sources, [Gartner](https://www.gartner.com/en) analysts [Mrudula Bangera,](https://www.linkedin.com/in/mrudula-bangera-a4989933/) [Martin Caren](https://www.linkedin.com/in/mcaren/), [Matt Crossley](https://www.linkedin.com/in/matt-crossley-dk) and [Gregg Siegfried](https://www.linkedin.com/in/greggsiegfried/) wrote in a report published in January.

“Telemetry pipelines enable the efficient collection, processing and delivery of such telemetry data, including [logs, metrics and traces](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/),” the analysts wrote. “Organizations should consider the need, cost, value and [return on investment] of telemetry pipelines as they consider their key functional areas.

“It is also worth considering the potential ‘lock-in’ risk of purchasing a telemetry pipeline from the same vendor as their main observability platform.”

## The Risk of Switching Vendors
Organizations face both good and bad choices, and these decisions can be fraught with difficulty. Making the choices more challenging: a proliferation of observability options, vendors and cost considerations.

Many of these options — such as selecting tools for observability and telemetry data collection, especially given the high cost of storage — are seen as ways to improve operations. However, cost always remains a key consideration.

Observability vendors offer intelligent solutions that enhance insights, analytics and a host of other benefits. They offer tools and platforms that can simultaneously reduce costs, for example, by filtering out unnecessary telemetry data that is not useful for observability.

However, there is always risk in switching vendors, even when those vendors promise to reduce costs for these organizations.

As the Gartner analysts write, there are dozens of vendors in the observability market, and organizations frequently struggle to differentiate between them when choosing observability platforms to implement. Increasingly, core features are commoditized with vendors opting to differentiate with higher-level functionality, such as generative AI (GenAI) assistance and cost optimization.

“Be cautious of focusing on functional areas of the specialized and differentiated layers that the organization is unlikely to adopt during the first year,” the Gartner team wrote. “The high cost of observability solutions makes time-to-value critical, and unsubscribing from unused capabilities may be costly or impossible.”

## The End of ‘Store It All’
Historically, the observability industry has had a “store it all” mentality, [Jen Villa,](https://www.linkedin.com/in/jevilla) director of product at [Grafana Labs](https://grafana.com/), told The New Stack.

“Whether it’s metrics, logs, traces, or profiles – especially at enterprise-level companies – daily data collection can easily surpass many millions of metrics series and petabytes of logs,” Villa said.

“At its core, the ‘store it all’ approach is meant to ensure that when something goes wrong, teams have access to everything so they can pinpoint the exact location of the failure in their infrastructure,” she said. “However, this has become increasingly infeasible as infrastructure becomes more complex and ephemeral; there is now just too much to collect without massive expense.”

“Modern tools have become expensive because they’re still using a firehose to fill a water bottle, but the real opportunity lies in tools that can detect threats and issues with less data while maintaining effectiveness.”

— J Stephen Kowski, SlashNext Email Security+
Even if money is not an issue, collecting such vast quantities of data creates “needle in a haystack” problems during incident resolution, Villa said. “Engineers have so much to sift through when they’re trying to resolve a problem that they don’t know where to start — they find themselves drowning in data, waiting on long-running queries that have to parse oceans of data.”

So the real question in response to rising observability costs is, according to Villa, “Do you really need all that data? And the answer is, you do not.

“You can store less of it or more compressed representations of it, and still get the same outcomes. You don’t need to sacrifice costs for capabilities.”

Instead, Villa said, a proper solution should analyze and classify signals based on utility — through alerts, dashboards or queries — to automatically optimize low-value data through aggregation, saving users sometimes up to 80% on costs.

“Something that would otherwise take developers weeks to do — take an inventory of all telemetry collected and eliminate the lower value parts — can be available at the click of a button,” she said.

A proper observability platform can continually analyze telemetry data in order to have the most up-to-date picture of what is useful rather than a one-time, manual audit “that’s essentially stale as soon as it gets done,” Villa said.

“It’s less about organizations wanting to pay less for observability tools, but they’re thinking more long-term about their investment and choosing platforms that will save them down the line,” she said. “The more they save on data collection, the more they can reinvest into other areas of observability, including new signals like [profiling](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/) that they might not have explored yet.”

Moving from a “store it all” to a “store intelligently” strategy is not only the future of cost optimization, Villa said, but can also help make the haystack of data smaller — and thus make it easier to find potentially the harmful needles that lay within.

## Data Collection: Focus on Precision
Organizations’ needs and requirements vary significantly, of course. A database storage company will have different observability needs than an online retail grocery store. There’s no one-size-fits-all approach, [J Stephen Kowski,](https://www.linkedin.com/in/jstephenkowski) field CTO at [SlashNext Email Security+](https://slashnext.com/), told The New Stack.

“It isn’t so binary; this will vary situationally from company to company,” Kowski said. “The ‘collect everything’ mindset from a decade ago has evolved, as smart organizations now focus on precision: collecting only the most meaningful data and using advanced AI to extract maximum value.

“Modern tools have become expensive because they’re still using a firehose to fill a water bottle, but the real opportunity lies in tools that can detect threats and issues with less data while maintaining effectiveness. The future winners in this space will be those who help customers optimize costs by focusing on high-signal data collection and intelligent analysis rather than just gathering more data.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)