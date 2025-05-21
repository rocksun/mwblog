# Best of All Worlds: Confluent Synthesizes Streaming and Batch Processing
![Featued image for: Best of All Worlds: Confluent Synthesizes Streaming and Batch Processing](https://cdn.thenewstack.io/media/2025/05/6f195642-confluent-1024x768.png)
Data streaming platform provider [Confluent](https://www.confluent.io/?utm_content=inline+mention) unveiled a new feature today that allows users to analyze real-time and historic data with a single query. Available in early access through [Confluent Cloud for Apache Flink](https://thenewstack.io/confluent-cloud-gets-apache-flink-tables/), snapshot queries combine batch and streaming data approaches to support low-latency use cases with enrichment data.

Confluent also unveiled IP filtering functionality for [Apache Flink](https://thenewstack.io/apache-flink-2023-retrospective-and-glimpse-into-the-future/) workloads and beefed up its private networking functionality for Flink.

Snapshot queries blend data from [Kafka topics](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/) with contextual data materialized in [Iceberg or Delta](https://thenewstack.io/the-open-format-movement-heats-up-snowflake-embraces-apache-iceberg/) tables in Tableflow. Users can query this open table format data from environments like Databricks and [Snowflake](https://www.snowflake.com/?utm_content=inline+mention). But instead of relying on two distinct systems — and sets of costs — to query the Kafka topic data and the data materialized in open table formats, users can do so with Confluent Cloud’s resources.

Snapshot queries are particularly advantageous for developers looking to build [agentic AI systems](https://thenewstack.io/how-ai-agents-will-transform-devops-workflows-for-engineers/), real-time applications and event processing workloads in which the latest data requires historic data enrichment. The new feature is also useful for helping developers understand which historical data is the most meaningful for their real-time use cases.

“With snapshot queries, you can really quickly query all this data and interactively develop,” commented [Jean-Sébastien Brunner](https://www.linkedin.com/in/jsbrunner), Confluent director of product marketing. “It can take a lot of time to find the right query for the right project. So, by using snapshot queries, you can really help your developer be more efficient at writing that query.”

## Data Blending
Snapshot queries are predicated on several facets of [Confluent Cloud for Apache Flink](https://www.confluent.io/product/flink/). They rely on a Flink-based query optimizer that determines which data for queries comes from Kafka topics and which comes from the aforementioned open table formats. The feature utilizes [Tableflow](https://www.confluent.io/blog/introducing-tableflow/) to materialize Kafka data in Iceberg and Delta Lake tables, while Flink is also responsible for the data blending process.

The mixture enables users to “have a terabyte of data with a long history, and in Kafka you can have the freshest, real-time data,” Brunner said. “What we do with snapshot queries is combine these two datasets in one query.” Confluent’s data blending process abstracts a significant amount of complexity from users. Organizations simply select whether they want to query with the system’s traditional streaming mode or snapshot mode. When the latter is selected, the user writes one query while the solution queries the desired open table format and the Kafka topic.

The platform then “blends the data together and transforms it with no duplicates,” Brunner said. The blending step enables data from Tableflow to become effectively attached to that of the Kafka topic. The retrieval from the open table formats is expedited because of several factors, including the information about the table’s contents that these formats readily expose.

According to Brunner, different aspects of the tables (including metadata and details about compression and compaction) function effectively like an index. “So, if you’re looking for a specific key, like I want to look for customer X somewhere, we can find that pretty easily without rescanning the topic,” he mentioned. The resulting cost, efficiency and increased productivity benefits are nontrivial.

## Developer Acceleration
The value derived from snapshot queries is equally applicable to production and development use cases. In addition to supporting [agentic AI](https://thenewstack.io/top-three-agentic-ai-use-cases-for-modern-it-operations/) workflows — in which agents need to cross-reference low-latency data based on customer interactions with reference data about customers, for example — these queries are useful for real-time deployments like fraud detection. “For any type of transaction, you may need historical things like how many times has this user made a transaction, or how often has it been from this location,” Brunner said. “As part of that, you may want to automatically take advantage of Tableflow.”

Although snapshot queries support these mission-critical applications, they could have easily been designed to expedite the developer life cycle. For example, developers may need to query their historical data to determine all the contextual factors necessary to analyze use cases like fraud detection. In streaming mode, they’d have to do several interactive queries to glean this information, “which would take a lot of time,” Brunner said. “By using snapshots, you can accelerate that because you can do it 100 times faster.”

## Query Optimization
The increased rapidity and efficiency of snapshot queries are directly attributable to the query optimization Confluent utilizes within [Flink](https://flink.apache.org/). Organizations simply specify what they want the query to do, such as identify factors relevant for detecting fraud in real time. Implicit to the query optimizer’s capacity to blend data from enrichment tables and Kafka topics is its capability for finding the relevant data from each of these resources.

“You don’t need to tell it it’s coming from Tableflow or it’s coming from Kafka,” Brunner mentioned. “The query optimizer knows where to get the data from Kafka topics or Tableflow. It’s part of Confluent’s Flink stack. When you write the SQL, we combine it, we optimize it, and we run it.” In fact, the optimizer may determine that enrichment data from open table formats is unnecessary to answer a query and simply retrieve information from the relevant Kafka topics.

## A Question of Semantics
The true benefit for developers, however, is that when the query optimizer does retrieve information from large amounts of reference data, it couples it with real-time [Kafka](https://kafka.apache.org/) data and reveals what information is pertinent to solve a business problem like fraud detection. Once this backend developer work is solved, that particular query can be input in production settings for real-time applications. With this approach, “When you do a query, you can be confident your streaming query will work and productize that and get the queries that run 24/7 on your latest data,” Brunner said.

This use case underscores the difference in semantics between snapshot queries and streaming mode queries. The former is based on what Brunner described as “the state of the world” (or of the business problem) strictly at the time the query is issued. The latter is based on continuous updates in an ongoing manner. Thus, after doing snapshot queries to find the relevant data for a business problem, users can run streaming queries based on those factors to continually update them in real time.

## Speaks for Itself
Confluent’s snapshot queries broaden the scope of streaming data processing by combining it with batch processing to enhance developer and production use cases. Users can avail themselves of Confluent’s query optimizer in Flink to automate much of the heavy lifting otherwise required to query large amounts of data in open table formats.

Even more beneficial may be the blending and transformation work the vendor has done to make that data readily queryable alongside data from Kafka topics. The resulting gains for performance, developer productivity and real-time deployments speak for themselves.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)