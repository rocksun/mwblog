Many legacy data systems weren’t designed to handle the demands of modern [AI workloads](https://thenewstack.io/running-ai-workloads-responsibly-in-the-cloud/). AI models, intelligent agents and automation pipelines demand fast, reliable, explainable and well-integrated access to data. Organizations that succeed in this environment are the ones that organize and manage their data intentionally, instead of just storing it passively. In short, they treat their [data like a product](https://thenewstack.io/live-data-is-rapidly-reshaping-product-development-practices/).

They name it, version it, document it, assign ownership and align it to business outcomes. They make it discoverable through a structured data catalog. They choose the right infrastructure based on how the data is accessed and updated. They don’t avoid difficult datasets (such as real-time streams, unstructured content or emerging external sources) because they know that’s where the most strategic value lies.

## Create Data Products, Don’t Just Store Data

Every important enterprise dataset should be organized and maintained as part of a data product. Each product should have a clear name, purpose and vision, along with comprehensive documentation, a road map and an assigned product manager. This approach brings structure, accountability and intentional evolution to data assets that would otherwise remain unmanaged and underused.

> A well-run data product should be evaluated like any other business product.

A well-run data product should be evaluated like any other business product: If it generates more value than it costs to maintain, it warrants ongoing investment and enhancement. If not, it should be deprecated.

Data products should follow a regular release cycle, with improvements guided by feedback from their most critical consumers — such as underwriting leads, claims operations managers, marketing directors and customer experience executives — who have a deep understanding of what is needed to drive business success.

## Align Data Strategy With Business Criticality

Data productization must be guided by business impact and focus on high-value use cases where data-driven intelligence delivers clear, measurable outcomes. Heavily regulated industries are particularly sensitive to data usage, protection and privacy rules. Examples of highly data-dependent use cases include:

* Dynamic pricing models tailored to behavioral risk signals
* Real-time fraud detection using claim pattern analysis
* AI-assisted underwriting that adapts to emerging lifestyle and biometric trends, proactive churn prevention using sentiment and interaction data
* Regulatory compliance automation through lineage-aware audit trails

Every data product should directly support a critical business function. The legacy mindset of building data lakes “just in case” or storing data without purpose leads to uncurated sprawl and operational waste. Instead, data initiatives must begin with business outcomes. This means systematically engaging business stakeholders — across actuarial, operations, marketing, claims and finance — to understand their current and future data needs.

> This approach transforms data from passive infrastructure into a managed, strategic portfolio.

Your data product road map should be based on the findings from those engagements. Any data asset that is not part of a governed data product, or any product that lacks alignment to a business stakeholder’s need, should be deprecated or archived. This approach transforms data from passive infrastructure into a managed, strategic portfolio, where resources are focused on maintaining and evolving the data products that actively drive the organization’s goals.

## Expose Data Products via MCP-Accessible APIs

AI agents and models work best when they can access data through standardized, pluggable protocols that are compatible across diverse clients and execution environments. Just as REST and SQL enabled broad interoperability in past generations of applications, the Model Context Protocol (MCP) is emerging as a standard interface for AI-native access to enterprise data.

By exposing data products via MCP-accessible APIs, organizations make those [products immediately usable by AI agents](https://thenewstack.io/not-my-fathers-middleware-how-to-be-productive-with-agentic-ai/), large language models (LLMs) and other intelligent clients without requiring custom integration logic. MCP tools define a common interaction pattern that allows agents to discover what a data product can do, send structured queries or actions and receive results in formats they can work with, such as JSON or embeddings. These interfaces also support traditional applications, enabling both AI and non-AI clients to consume the same data product via a consistent toolset.

Each data product should include at least one MCP tool that provides a modular, declarative interface that exposes relevant operations such as search, filtering, lookup, summarization or prediction. These tools sit on top of the data product and abstract away the underlying storage and compute engine. Whether the data is backed by a relational database, vector store or document index, the MCP layer ensures that access is standardized and discoverable.

This approach allows enterprises to future-proof their data architecture. As more AI agents, copilots and retrieval-augmented generation (RAG) pipelines emerge, any system that understands MCP can begin working with enterprise data products immediately and securely, with no need for bespoke connectors or duplicated pipelines.

## Invest in Future-Looking and Emerging Data Sources

Enterprises preparing for the next wave of AI innovation must go beyond traditional datasets such as customers, transactions, claims and web analytics. The most impactful AI applications of the future — such as hyper-personalized customer experiences, [generative assistants and behavioral risk models](https://thenewstack.io/vmwares-dev-centered-approach-to-pre-trained-models-and-generative-ai/) — will depend on emerging, nontraditional data sources that offer deeper context, sentiment and intent.

Forward-thinking enterprises might build a data product portfolio with several high-potential data domains like:

* **Customer sentiment and reputation signals:** Collects and aggregates Net Promoter Scores (NPS), call center sentiment analysis and social media mentions used by marketing and customer experience teams to fine-tune outreach and proactively address dissatisfaction.
* **Consent logs and compliance metadata:** A centralized product that tracks all customer opt-in/opt-out choices, data usage flags and access control policies integrated directly into AI pipelines to ensure real-time policy enforcement.
* **Prompt-response logs and embeddings from LLMs:** Stores every prompt-response pair from internal LLM copilots, along with vector embeddings and human feedback; supports continuous model tuning and helps explain LLM decisions during audits.
* **Biometric and wearable sensor data (with explicit consent):** A product that ingests biometric data from consenting customers’ smartwatches to help model real-time lifestyle risk factors for dynamic underwriting.
* **External enrichment feeds:** A federated product that integrates credit bureau data, climate exposure models, census demographics, geolocation datasets and real-time signals from news, media and public internet sources to enhance customer profiles and sharpen risk segmentation by layering in external context unavailable through internal systems alone.

These are just some examples of how enterprises can stay at the forefront of their industry by using novel data assets — ahead of the competition — to gain a sustained strategic advantage.

## Vectorize All Unstructured Data

As enterprises adopt a data product mindset, it’s no longer enough to focus only on structured datasets. To remain competitive, organizations must also invest in future-looking data sources, many of which are unstructured and traditionally difficult to work with. These include drone footage, satellite imagery, blog posts, legal filings, chat logs, medical notes and customer emails. While rich in insight, these sources are often ignored or underused because they lack the structure needed for easy interpretation and AI readiness.

> Enterprises must treat unstructured data as an integral part of their data product portfolio and transform it into AI-ready formats.

To close this gap, enterprises must treat unstructured data as an integral part of their data product portfolio and transform it into AI-ready formats. This involves building vectorization pipelines that use text and multimodal embedding models to convert raw content (such as documents, emails and transcripts) into [high-dimensional vectors](https://www.sciencedirect.com/topics/computer-science/high-dimensional-data#:~:text=High%2Ddimensional%20data%20refers%20to,to%20its%20complexity%20and%20size.) that capture semantic meaning. These embeddings enable operations like similarity search, semantic clustering and RAG.

More advanced use cases include cross-modal search, where users can find relevant videos or images using natural language — enabling “text-to-video” or “text-to-image” retrieval. Once embedded, data can be indexed in vector databases, making it easily searchable even across large, unstructured content repositories.

By treating unstructured data as a first-class data product and investing in emerging data types, enterprises make previously inaccessible content fully available to modern AI systems. The result is a more intelligent, adaptive organization that can search, summarize and act on all of its data — not just the structured fields in rows and columns.

## Embed Lineage, Consent, Explainability and Governance

As we move toward treating data as a product, product quality must include lineage, consent, explainability and governance. These are not optional features; they are core attributes that define whether a data product can be trusted, reused and deployed in critical workflows.

* **Lineage** provides the traceability necessary to understand where data comes from, how it has been transformed and how it flows through downstream systems. This visibility is essential for debugging, auditing and assessing reliability.
* **Consent** ensures that data is used appropriately and in accordance with legal, regulatory and user-defined boundaries. Data products must enforce fine-grained access controls that reflect data sharing agreements and privacy choices.
* **Explainability** means that downstream consumers — whether human users or machine learning (ML) systems — can understand how the data was generated, what it represents and how it contributes to decisions. This is particularly important for data-feeding models that affect pricing, claims or customer interactions.
* **Governance** encompasses the operational discipline around each data product. Access policies, usage contracts, data quality metrics and audit logs must be in place and maintained over time.

By enabling these practices into the design and release cycle of each data product, organizations ensure responsible data use while scaling AI-driven operations with trust and accountability.

## Publish Data Products in a Structured Catalog

When data is treated as a product, it must be discoverable, understandable and trustworthy [just like any other product in the enterprise](https://thenewstack.io/driving-platform-adoption-the-missed-opportunity-of-marketing/). A core part of delivering on this principle is maintaining a structured, centralized data catalog that provides both human users and AI systems with access to the enterprise data product portfolio.

The catalog should:

* Support rich GUI-based exploration for stakeholders browsing data assets.
* Enable seamless integration with AI tools through standardized API access, such as via the MCP.
* Include rich metadata that describes what the data product is, how it’s structured and what purpose it serves.
* Provide clear ownership and stewardship information, a product description, and references to documentation, usage guidelines and known limitations.
* Surface data lineage, showing where the data comes from, how it was transformed and which downstream systems or AI models consume it.

By publishing data products in a catalog, organizations build a shared understanding of the data landscape and transform an abstract data lake into a navigable ecosystem of trusted, curated assets, allowing AI teams to build with confidence and clarity.

A catalog enables teams to avoid redundant efforts, promotes reusability and supports more confident adoption of AI. Data scientists can trace features back to their raw inputs. Analysts can validate whether a dataset is fit for their use case. Engineers can assess the impact of upstream changes.

## Manage Velocity and Volume

As enterprises shift toward managing data as products, they are encountering a clear operational challenge: Many of these new data products are updating in real time and are significantly larger than traditional datasets. It’s not uncommon for modern data products, especially those built from logs, sensors, video or model-generated content, to reach tens or hundreds of terabytes, and in some cases, petabyte scale.

This increase in data volume and velocity introduces new technical requirements. Some data products must support continuous updates with low-latency access. Others need to be scanned in parallel across large distributed systems. Many must remain cost-efficient to store, yet still offer fast access to support AI workflows, analytics or compliance needs.

> It’s essential to match each data product with infrastructure that meets its performance, latency and scalability needs.

To handle these requirements, enterprises need a broad set of data engines that can meet the demands of modern AI workloads. Many traditional databases and data lakes were not built to accommodate the volume, velocity and access patterns that AI systems require. As a result, they often struggle to serve these workloads efficiently. No single engine can address all needs, so it’s essential to match each data product with infrastructure that meets its performance, latency and scalability needs.

Managing high-volume and high-velocity data requires more than just adding tools — it demands an integrated data platform that brings together a variety of data engines, each optimized for different access patterns such as search, aggregation, real-time updates and batch analytics.

Success comes from being practical and intentional. This includes:

* Selecting the right infrastructure for each data product.
* Monitoring how it performs under evolving demands.
* Adapting the architecture as needs change.

A cohesive platform that supports diverse workloads enables consistent performance and scalability without unnecessary cost or operational complexity.

## Get the Most Value From Your Data

Treating data as a product — with ownership, documentation, versioning and a clear purpose — will help you get the most value from your data. It creates the foundation needed to support modern AI, analytics and automation workloads. Aligning data efforts with business priorities ensures resources are directed toward outcomes that matter, while structured catalogs and well-chosen infrastructure make data more accessible, scalable and reusable across the organization.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/e92364a0-ivannovick.png)

Ivan Novick leads data platform product management at Broadcom's Tanzu division, overseeing real-time data, streaming, OLTP databases, and data warehouses/lakes. He previously spearheaded Tanzu Greenplum innovation for more than a decade, where he drove its evolution from version 4 to...

Read more from Ivan Novick](https://thenewstack.io/author/ivan-novick/)