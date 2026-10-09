**The frenetic pace of AI development** is challenging data center design and operational paradigms. The twin pillars of hyperscale computing – intelligent processors and the memory that feeds them – are no exception. Hyperscale operators have invested heavily in GPU clusters and high-bandwidth memory to drive AI model training and inference. While those investments have pioneered historic performance gains, they also exposed a design rift that data center architects are racing to close.

One of today’s most pressing AI compute challenges is no longer defined by accelerating processor cycles – it’s about serving a diverse array of compute engines with data – efficiently, consistently, and at scale.

This is because AI workloads are redefining the role of data in the data center. Where it was once accessed intermittently or in predictable batches, [data today is continuously consumed](https://thenewstack.io/ai-consumes-lots-of-energy-can-it-ever-be-sustainable/), recalled, and recombined across training, inference, and complex agentic workflows. As a result, data lakes and other storage systems that once housed raw or semi-structured data and performed a modicum of offline analysis are now expected to function as high-throughput delivery platforms.

> “One of today’s most pressing AI compute challenges is no longer defined by accelerating processor cycles – it’s about serving a diverse array of compute engines with data – efficiently, consistently, and at scale.”

For data center managers responsible for budgets, infrastructure planning, and long-term roadmaps, the shift introduces a new set of trade-offs.

## AI data lakes and the changing nature of data

Data centers have long relied on centralized, cost-effective repositories to store vast [amounts of raw data](https://thenewstack.io/modus-enterprise-context-warehouse/), ranging from text and images to video content and physical sensor outputs. These storehouses, or data lakes, are accessed when needed and typically for batch-oriented analytics.

But AI changed the scope and the behavior of the data lake model.

AI training workloads access large datasets repeatedly, often across distributed clusters. AI inference ups the ante by generating data access events that extend beyond a single query. What looks like a simple request can trigger dozens of underlying operations, each requiring access to stored data, intermediate results, or contextual information.

As such, AI data lakes aren’t just for [storing data](https://thenewstack.io/medium-scylladb-feature-store/). They deliver output continuously and at high speed by enabling concurrent access from multiple pipelines and the rapid ingestion of new data under sustained loads.

> “In practical terms, AI data lakes are no longer passive storage vaults; they’re active, persistent, and increasingly central to overall system performance.”

In practical terms, AI data lakes are no longer passive storage vaults; they’re active, persistent, and increasingly central to overall system performance.

## Why conventional storage approaches break down

The problem facing hyperscale data centers is that their storage architecture wasn’t designed for AI inference workloads. Traditional data lakes assumed that only a fraction of stored data would be accessed at any given time. They tolerated latency and were optimized for cost per terabyte rather than throughput per workload. That model worked well for reporting and analytics. It struggles under constant, parallel access patterns.

At the same time, GPU clusters are expensive to build and operate. They consume significant power and require advanced cooling solutions. Simply adding more compute or DRAM-based high-bandwidth memory is not always feasible. Power budgets, space, and replacement cycles impose physical and economic limits.

> “The problem facing hyperscale data centers is that their storage architecture wasn’t designed for AI inference workloads.”

This pressure is also reshaping the way some cloud providers structure their storage services and service-level agreements (SLAs). Long before the rise of generative AI, hyperscalers had already begun segmenting customers into storage performance tiers defined by latency, throughput, IOPS, and data availability guarantees. Lower-cost archival and capacity tiers emphasized cost and scale, while premium tiers increasingly relied on all-flash infrastructure to deliver faster response times and predictable performance. AI is accelerating that transition. As inference workloads demand near-continuous access to massive datasets, more customers are being pushed toward higher-performance storage tiers that can sustain parallel data retrieval without bottlenecks.

## QLC NAND and the concept of ultra-high-capacity flash

These challenges demand a different approach to storage, one that balances capacity, performance, and efficiency at scale.

Quad-level cell, or QLC, NAND flash increases storage density by encoding four bits per cell, enabling significantly higher capacities than other NAND configurations. Advances in architecture and manufacturing have pushed enterprise SSD capacities to new levels, including recent demonstrations of 256TB NVMe drives built specifically for AI workloads.

These ultra-high-capacity SSDs support data-intensive applications such as AI data lakes, where both scale and sustained throughput are critical. By increasing capacity per device, they allow data centers to store more data in fewer drives, reducing the physical footprint of storage infrastructure.

The benefits extend beyond space savings. Higher density translates into power efficiency, measured in terabytes per watt. This is a key consideration for hyperscale environments where energy consumption is a primary constraint.

These improvements also reflect a broader shift in how flash is being designed. Rather than serving as a general-purpose storage medium, NAND flash addresses the specific demands of AI, where sustained access patterns and large datasets dominate.

## Rethinking SSD architecture for AI scale

As capacities reach hundreds of terabytes per drive, new engineering challenges emerge. One of the most significant is managing data efficiently over time.

Traditional SSD designs rely on background processes to recycle and reorganize data, maintaining performance and endurance. At very high capacities, these processes can become inefficient without careful management. Frequently rewriting large volumes of data is neither practical nor energy efficient and can shorten a drive’s lifespan.

To address this, newer architectures are focusing on reducing unnecessary data movement. By rethinking how I/O operations are handled and optimizing data placement, it is possible to minimize write amplification and improve overall system efficiency.

These changes may seem incremental, but at hyperscale they translate into substantial cost savings and faster time to value.

## Implications for data center strategy

For data center managers, the rise of AI data lakes and ultra-high-capacity flash offers a way to scale storage and support sustained AI workloads without proportionally increasing cost, power consumption, or physical footprint.

In practice, this means adopting a more segmented storage approach, where high-performance tiers remain near the compute layer. At the same time, high-capacity QLC-based systems anchor the data lake and create a more balanced architecture that supports both current workloads and future needs.

Regardless of which memory is adopted or where it is applied, AI data lakes will continue to grow in size and importance. As models grow more complex and inference workloads expand, the pressure on storage systems will only increase.

> “By enabling dense, efficient, high-throughput storage, QLC NAND provides a practical path forward for organizations seeking to scale their AI capabilities.”

At the same time, constraints around power, space, and cost will limit the effectiveness of brute-force approaches. The future of data center design depends on balanced architectures that integrate compute, memory, and storage more cohesively.

High-capacity QLC NAND flash is poised to play an important role in that evolution. By enabling dense, efficient, high-throughput storage, QLC NAND provides a practical path forward for organizations seeking to scale their AI capabilities.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/f6e05198-cropped-d83d7806-mrinal.png)

Mrinal is Senior Vice President, Flash Product Engineering, Sandisk. He brings more than 21 years of experience in Flash memory, product engineering, and DRAM, driving technology innovation, product differentiation, and next-generation storage solutions. A prolific inventor with 20+ patents, he...

Read more from Mrinal Kochar](https://thenewstack.io/author/mrinal-kochar/)