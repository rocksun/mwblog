The load on the energy infrastructure that AI is placing should not be underestimated.

Most approaches to addressing the AI energy crisis focus on hardware, such as more efficient chips, better cooling, and greener data centers. Those matters, but there’s a faster, cheaper lever that gets less attention — the way organizations process data.

Shifting more workloads from batch processing to real-time data streaming is one of the most accessible and near-term ways to reduce AI’s energy footprint. The main difference is in the load profile. Batch processing creates sharp spikes in demand that require infrastructure to be provisioned for peak load. Streaming flattens that curve, distributing compute more evenly over time.

> “Batch processing creates sharp spikes in demand that require infrastructure to be provisioned for peak load. Streaming flattens that curve, distributing compute more evenly over time.”

The implications for energy consumption are significant and address an important issue. Electricity prices jumped 6.9% last year, and data centers will account for 40% of electricity demand growth through the end of the decade, [according to](https://www.cnbc.com/2026/02/12/electricity-price-data-center-ai-inflation-goldman.html) Goldman Sachs. Meanwhile, hyperscalers are signing long-term power purchase agreements on a vast scale, and grid operators in several regions have [already flagged](https://www.powermag.com/nerc-warns-long-term-grid-reliability-risks-mounting-from-surging-demand-lagging-resources/) [capacity concerns](https://www.eenews.net/articles/ny-grid-operator-finds-multiple-reliability-shortfalls-in-next-5-years/).

## Why batch processing deserves more scrutiny

Batch processing is still the most common approach to data analysis, dating back to the mainframe era. With batch loads, data is accumulated over time, staged in storage, and then processed in large, scheduled runs.

Because these batch jobs run in concentrated bursts, operators have to provision infrastructure for peak load, meaning capacity sits idle between runs and consumes energy without doing any useful work. When a batch job kicks off, CPU and memory demand spike, taxing cooling systems and drawing heavily on power for a relatively short window. Then the cycle repeats.

In energy terms, it’s like flooring the accelerator from a standing start rather than maintaining a steady cruising speed. The approach made sense when compute was scarce, and data volumes were modest, but it’s less practical when AI systems require both speed and scale simultaneously.

## A more efficient architecture

Streaming technologies like Apache Kafka and Apache Flink are already widely used in industries with real-time data needs, like financial services, retail, and telecommunications. But the operational case for streaming now extends beyond [latency into total cost of ownership](https://thenewstack.io/why-latency-and-total-cost-of-ownership-matter-more-in-ai-apps/) and sustainability.

Because data is processed continuously as it arrives, event by event, data streaming shifts the resource profile from spiky and unpredictable to steady and manageable. The compute load is distributed over time, which means peak demand is lower and provisioning can be more precise.

Systems no longer need to be sized for the worst-case burst capacity; they can scale dynamically in response to actual throughput. This reduces idle compute running in reserve, one of the more significant sources of energy waste.

> “Systems no longer need to be sized for the worst-case burst capacity; they can scale dynamically in response to actual throughput.”

There are further efficiencies downstream. [Streaming architectures](https://thenewstack.io/introduction-to-data-streaming/) typically clean and deduplicate data in transit, before it reaches storage. That means data warehouses have less redundant data and the queries that run against them are leaner. Disk I/O, another energy-intensive operation in data processing, is reduced as a result.

Shifting to a decoupled, event-driven architecture also means that individual systems can process data independently, without triggering cascading compute loads across tightly integrated pipelines.

## Where to start

Not every workload needs to move to streaming at once. A strong initial candidate is preprocessing for AI workloads — using a stream processor to filter, aggregate, and normalize [data before it reaches an AI model](https://thenewstack.io/better-context-will-always-beat-a-better-model/). This produces leaner, curated inputs instead of raw logs or wide tables, reducing memory, CPU, and GPU load.

A streaming architecture can also improve AI performance, because agents often need continuous access to current data. Static datasets that are periodically refreshed lead to outdated context or require reprocessing. Batch processing can end up being a bottleneck more than the models themselves.

## Harnessing short-term gain

Migrating data pipelines from batch to streaming typically occurs at the software layer, so it doesn’t require waiting for new power or cooling infrastructure. It won’t eliminate AI’s energy problem, but it offers a fast, low-investment way to measurably reduce unnecessary consumption.

As AI workloads continue to grow, the pressure to be responsible energy stewards will only intensify from regulators, customers, and communities where data centers are built. Hardware improvements are already underway. The software conversation is overdue.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/980f85a3-warren-vella_headshot-600x600.png)

Warren's career started off as a 13-year adventure at the Australian Energy Market Operator (AEMO), where he supported and architected critical energy market integration platforms. After moving from operations into a strategic enterprise architecture role, he joined Confluent as a...

Read more from Warren Vella](https://thenewstack.io/author/warren-vela/)