Ask any data architect what seemed impossible to cost-effectively achieve just five years ago, and you’ll hear about real-time fraud detection systems processing millions of transactions per second, AI-powered search engines that understand context across petabytes of unstructured data and distributed analytics platforms that respect data sovereignty while enabling global insights.

These aren’t aspirational use cases anymore, but production workloads running — and running well — on 100% [open source data infrastructure](https://thenewstack.io/your-open-source-data-infrastructure-is-ready-for-agentic-ai/).

The difference between these implementations and legacy data strategies largely comes down to making the right architecture choices that can evolve with your applications. Where traditional approaches treated data infrastructure as a cost center to be minimized, the smarter direction today is building systems that actively optimize for performance, cost and operational flexibility simultaneously.

Open source data infrastructure technologies are uniquely positioned to enable these intelligent architectures, offering the customization depth and community innovation that proprietary systems simply cannot match.

The production workloads that seemed impossible five years ago are now achievable because of specific architectural innovations that have matured across the [open source ecosystem](https://thenewstack.io/what-do-cloud-native-and-kubernetes-even-mean/).

## **Tiered Storage Transforms Real-Time Data Economics**

[Apache Kafka](https://kafka.apache.org/) has long been the backbone of enterprise real-time data pipelines, but its storage model created a costly paradox. To maintain low latency for real-time processing, organizations had to store all data in high-performance storage tiers — even the vast majority of records that would rarely be accessed again. A fraud detection system might need millisecond access to the last hour of transactions, but could tolerate higher latency for historical pattern analysis. Yet both data sets sat in the same expensive storage layer.

Kafka’s [tiered storage](https://www.instaclustr.com/support/documentation/kafka/useful-concepts/kafka-tiered-storage/) fundamentally restructures these economics. The architecture separates Kafka’s log storage into hot and cold tiers, automatically managing data placement based on access patterns. Recently produced data remains in low-latency local storage, while older segments migrate to object storage like S3. The crucial innovation is that Kafka consumers can still access cold-tier data transparently through the same API.

Hot-tier access maintains sub-10 millisecond p99 latency, while cold-tier retrieval typically adds 50 to 100ms. For the majority of real-time use cases, where recent data drives decisions and historical data supports periodic analysis, these trade-offs deliver 70 to 80% storage cost reductions without compromising core functionality. A retail platform processing clickstream data can now retain months of historical events for machine learning (ML) model training at marginal cost, where previously they might have archived or deleted that data within weeks.

## **AI-Powered Search Makes Unstructured Data Useful**

Enterprise search has been a persistent disappointment. Traditional keyword-based systems return too many irrelevant results, while advanced options require specialized query languages that most users never learn. Vector search and embedding models are finally changing that equation.

OpenSearch, PostgreSQL with [pgvector](https://github.com/pgvector) and [Apache Cassandra 5.0](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/) with vector search capabilities now enable semantic search at scale. Documents and queries are encoded as high-dimensional vectors using language models, with similarity measured in vector space rather than through keyword overlap. When a customer service representative searches for “shipping delay complaints,” the system understands the semantic relationship to records mentioning “late delivery” or “order not arrived” without requiring exact phrase matches.

Index structures like hierarchical navigable small world (HNSW) enable approximate nearest neighbor search that returns results in milliseconds, even across billions of vectors. For enterprises with existing OpenSearch or PostgreSQL deployments, the path to AI-powered search doesn’t require wholesale platform replacement. Adding vector capabilities to current systems allows teams to enhance search functionality iteratively, proving value before committing to full migration.

Even better, the operational impact extends beyond search boxes. Vector embeddings enable recommendation engines that understand content relationships, anomaly detection systems that identify unusual patterns in logs and chatbots that can reason over enterprise knowledge bases.

## **ClickHouse Makes Operational Analytics Performant**

Data warehouses have traditionally been batch-oriented systems, ingesting data on scheduled intervals and optimized for complex analytical queries over historical datasets. [ClickHouse](https://www.instaclustr.com/blog/clickhouse-a-beginners-guide-to-the-fastest-open-source-olap-dbms/) and similar open source columnar databases are collapsing the boundary between operational and analytical workloads, enabling sub-second queries over billions of rows of recent data.

[ClickHouse achieves its performance](https://thenewstack.io/vector-search-without-the-lock-in-why-devs-like-clickhouse/) through aggressive compression and columnar storage optimized for analytical access patterns. Where row-oriented databases store all fields for a record contiguously, columnar systems store each column separately. When an analytical query needs to aggregate a few columns across millions of rows, only the relevant columns are read from disk. Combined with codec-based compression that can achieve 10x or better compression ratios, queries can often operate entirely in memory even on massive datasets.

Migration from traditional data warehouses requires rethinking data modeling. ClickHouse favors denormalized wide tables over normalized schemas with joins. For organizations with mature Snowflake or Redshift deployments, the decision isn’t necessarily replacement so much as it’s identifying workloads where real-time performance matters more than the features of established platforms.

## **Hybrid Infrastructure Finally Works**

Legacy on-premises systems represent enormous vested investments that enterprises cannot simply abandon. Yet these systems increasingly need to interoperate with modern cloud native services for analytics, ML and real-time processing.

Kubernetes has emerged as the integration layer enabling hybrid deployments. While initially designed for microservices orchestration, Kubernetes now hosts stateful workloads, including databases and message queues. It abstracts infrastructure differences, allowing applications to deploy portably across on-premises data centers and public clouds.

The data plane integration matters as much as the control plane. Change data capture tools like Debezium stream database changes from legacy systems into Kafka topics, making decades-old data [available for real-time processing](https://thenewstack.io/mark-cache-the-clickhouse-speed-hack-youre-not-using-yet/) without modifying battle-tested production databases.

Managed open source services provide operational leverage for enterprises building hybrid architectures. Running Kafka, ClickHouse or OpenSearch reliably requires deep operational expertise in those specific technologies. Managed services let organizations focus on integration patterns and data models rather than cluster tuning and version upgrades.

## **Making Intelligent Infrastructure Real**

The trends reshaping enterprise data infrastructure share a common thread beyond their open source foundations. They all represent architectural choices that optimize for multiple dimensions simultaneously rather than treating performance, cost and flexibility as competing concerns.

For technical leaders evaluating these technologies, the question isn’t whether to adopt them but rather how to sequence implementation. Starting with tiered storage for existing Kafka deployments offers immediate cost savings with minimal risk. Adding vector search to current databases enables AI features without platform migration. The key is identifying which capabilities address your most pressing constraints today while building toward a more intelligent architecture over time.

The 100% open source code nature of these technologies provides unusual flexibility in adoption paths. You can experiment with ClickHouse on a subset of analytical workloads before committing to full migration. I’m not saying you should deploy everything simultaneously, but the low barrier to experimentation means the cost of validating these approaches in your specific context is remarkably low.

Looking toward 2026, which, somehow, is already on the horizon, the infrastructure trends accelerating now will increasingly become baseline expectations. The enterprises moving quickly on intelligent data infrastructure today are building the foundation for what comes next. Those who wait will find themselves not just behind on current capabilities but unprepared for the next wave of requirements that build on these foundations.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/04/2557b440-anilinamdar.jpg)

Anil Inamdar is the Global Head of Data Services at NetApp Instaclustr, which provides a managed platform around open source data technologies including Cassandra, Kafka, Postgres, ClickHouse, and OpenSearch. Anil has 20+ years of experience in data and analytics roles....

Read more from Anil Inamdar](https://thenewstack.io/author/anil-inamdar/)