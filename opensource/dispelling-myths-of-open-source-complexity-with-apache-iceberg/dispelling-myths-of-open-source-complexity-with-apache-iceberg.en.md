While everyone agrees on the importance of an AI-ready data foundation, there’s often a disconnect on the right tools for building it. Engineers want to leverage open source software for its flexibility and emphasis on interoperability. On the other hand, business leaders are skeptical and worry about perceived complexity and a lack of enterprise capabilities.

These common hesitancies around open source adoption are often based on outdated assumptions. The modern open data approach is now performant, secure, adaptive and flexible. This kind of architecture doesn’t just simplify the data landscape; it helps organizations move faster, reduce complexity and ultimately drive more insights from their data. To help enterprises feel more confident about the value open source can unlock and encourage greater alignment across technical and business leadership, it’s helpful to unpack misconceptions about open source and illustrate how an open data journey — namely with [Apache Iceberg](https://iceberg.apache.org/) — can supercharge their AI success.

## Misconception 1: Proprietary Is Safer, More Performant

### The Myth

Moving from a proprietary, “hand-designed” format to an open one means sacrificing performance and security.

### The Reality

[Apache Iceberg shares techniques](https://thenewstack.io/new-in-apache-iceberg-3-0-fresh-data-types-null-vals-change-capture/) with many proprietary [table formats](https://thenewstack.io/architects-guide-to-apache-iceberg/) and uses an industry-standard, metadata-driven approach to query planning. Unlike previous generations of table formats, which relied on local storage and fast file access, [Iceberg’s metadata approach](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/) boosts performance by optimizing for cloud-based data. Instead of wasting time listing and inspecting files — a slow, expensive process in the cloud — it uses a metadata layer that includes file statistics, enabling query engines to quickly prune unnecessary data. This reduces expensive S3 operations and allows for faster query execution and lower compute costs.

Iceberg’s primary security benefit lies in its open and standardized format. As an [Apache Software Foundation](https://www.apache.org/) project, its specification is public and vendor-agnostic, preventing vendor lock-in and allowing integrations with a wide range of open and proprietary tools and security systems. Because of this functionality, organizations aren’t tied to a single platform or a vendor’s security model. Instead, they can leverage robust, industry-standard solutions for encryption, access controls and auditing.

Moreover, older formats aren’t equipped for modern data governance requirements like GDPR, but Iceberg is built to handle these efficiently and at scale. Designed to address the limitations of older file-based systems by treating data as a structured table rather than just a collection of files, Iceberg enables fine-grained, row-level operations that are essential for compliance.

### The Business Impact

While proprietary formats are often custom-tuned for one engine, Iceberg offers a far more valuable trade-off: universal interoperability. This allows a business to use a single copy of its data with every major query and transformation engine on the market, eliminating vendor lock-in and enabling businesses to choose the best tool for the job at any given time. With Iceberg, data inertia is a thing of the past. New engines can be tested and used immediately without ETL or a time-consuming migration. This is a strategic advantage that outweighs minor performance differences, which continue to be reduced, for a strong, long-term data strategy.

## Misconception 2: Migrating to a New Format Is a Nightmare

### The Myth

Transitioning to Iceberg from older formats is a complex, costly and high-risk project.

### The Reality

Iceberg was built from Day 1 with migrations from other file-based tables in mind. Its design includes built-in capabilities for importing and migrating tables nondestructively, meaning you can integrate Iceberg without disrupting existing data pipelines. This allows for a phased rollout, where teams can keep their old pipelines running until they’re ready to switch. Another key benefit is in-place migration, which lets you generate Iceberg metadata files on top of your existing Parquet, Avro or Optimized Row Columnar (ORC) data files. This approach is significantly faster and more cost-effective because it prevents users from having to copy massive amounts of data.

The open and interoperable nature of Iceberg means businesses can integrate it with their current query engines and tools, allowing for a gradual adoption and phased rollout. The community has developed clear, step-by-step migration patterns, proving that the process is well-defined and reliable. This enables businesses to adopt Iceberg for new projects or critical tables first, refining their approach before a full-scale migration.

### The Business Impact

The Iceberg ecosystem has matured significantly, with many cloud providers and data platforms now offering built-in support and tools to simplify the migration process. This robust support makes it easier for companies to shift to an open, scalable and governed data platform.

A great example of this is health tracker vendor WHOOP, which used this transition to dramatically improve its operations. By adopting a unified platform with Snowflake and Apache Iceberg, WHOOP was able to significantly reduce infrastructure overhead, saving [20 hours](https://www.snowflake.com/en/customers/all-customers/case-study/whoop/) of compute per day and tens of thousands of dollars per month.

Beyond ease of migration, Iceberg’s interoperability means teams can apply the familiar relational concepts they already use to their massive data sets. This shift allows them to move their focus from writing and debugging complicated, multistep custom transaction logic to simply using an efficient `MERGE INTO` statement. Ultimately, this frees up their time to focus on innovation and driving business [value from their data](https://thenewstack.io/year-of-ai-utility-moving-from-early-wins-to-long-term-value/).

## Misconception 3: Open Source Adds Complexity

### The Myth

A new open standard will add another layer of complexity to an already sprawling data infrastructure.

### The Reality

Yes, tool sprawl is real, and no one wants to add to that problem. That’s why Iceberg’s core benefit is architectural simplification. Instead of needing multiple systems with expensive background processes to keep data in sync, Iceberg allows every engine to work with a single copy of the data. Multiple types of existing tables can be converted to Iceberg, drastically reducing the overall complexity of your data architecture.

Beyond that, features like time travel and transactional semantics are built directly into Iceberg, eliminating the need for custom engineering to achieve these capabilities. With time travel, businesses can instantly audit data changes and even restore past versions, which is critical for compliance and debugging. Transactional semantics ensure data integrity during simultaneous operations, giving teams confidence in the accuracy of their analytics. This shifts teams’ focus from managing complex infrastructure to creating business value.

### The Business Impact

Open source offers enterprises flexibility and interoperable capabilities that provide a competitive edge to stay agile and not be locked into any single vendor. By offering a clearer path to data unification, Iceberg helps organizations eliminate data silos to accelerate time to insight and activate the vast amounts of data they may have but have yet to unlock value from. Open standards are the key to a future-proof data strategy and allow businesses to adopt new, exciting technologies as they emerge without friction.

## The Future Is Open

The perceived risks of open source are, in fact, the keys to unlocking greater simplicity, reliability and business value. The [future of data is not a choice between open source](https://thenewstack.io/building-the-future-together-with-community-driven-open-source/) and proprietary systems, but a harmonious blend of both — with open standards like Iceberg providing the essential foundation for enterprise AI to thrive. By solving data engineering challenges, like infrastructure tuning, disparate tooling and complex data architectures, enterprises are building the necessary foundation for AI success. New tools are being designed with Iceberg in mind, which means if your data is already in an Iceberg table, it’s ready for any new technologies emerging, especially in the AI space. This truly interoperable format ensures enterprises’ data is not just an asset, but a dynamic, future-proof foundation for whatever comes next.

## Getting Started With Iceberg

With the misconceptions about open source dispelled, you may be wondering how to begin your Iceberg journey. Evaluating where to start can feel daunting, but a strategic approach can ensure success. By following these steps, you can begin to transform your data infrastructure from one of complexity to one of simplicity, paving the way for more efficient operations and accelerated business value:

**Step 1: Identify complexity.** Identify where you’re experiencing the most complexity in your current infrastructure. Explore how multiple tools working on a single, [governed copy of your data](https://thenewstack.io/ai-data-dilemma-balancing-innovation-with-ironclad-governance/) could simplify things.

**Step 2: Define success.** Identify what success would look like for a potential test. Is your intention to create fewer pipelines/copies of data? Is the goal faster service-level agreements (SLAs)?

**Step 3: Evaluate solutions.** Evaluate solutions that focus on simplifying your architecture to fully capture the value of this transformation to Iceberg.

This approach ensures that your initial adoption of Iceberg is strategic and successful, building a foundation that will serve as a launchpad for future innovation and growth, so you’re ready for whatever the AI era brings.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/099c37cd-cropped-08a59824-russell-spitzer-600x600.jpeg)

Russell Spitzer is a principal software engineer at Snowflake, where he is focused on Apache Iceberg and Polaris Catalog. Russell is passionate about distributed computing and is involved in several Apache Software Foundation projects like Apache Cassandra, Apache Spark and...

Read more from Russell Spitzer](https://thenewstack.io/author/russell-spitzer/)