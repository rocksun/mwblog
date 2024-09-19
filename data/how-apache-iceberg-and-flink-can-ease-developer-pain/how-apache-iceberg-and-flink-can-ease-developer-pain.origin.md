# How Apache Iceberg and Flink Can Ease Developer Pain
![Featued image for: How Apache Iceberg and Flink Can Ease Developer Pain](https://cdn.thenewstack.io/media/2024/09/bf07b821-thumbnail-2-1024x576.png)
At a high level, data infrastructure is split into an operational estate and an analytical estate.

The operational estate “is where microservices live, this is where our event-driven application lives,” said [Adi Polak](https://github.com/adipolak), director, advocacy and developer experience engineering at [Confluent](https://www.confluent.io/?utm_content=inline+mention), in this episode of The New Stack Makers.

“This is where our stream processing is taking place; we care a lot about being fast. And we care a lot about throughput. We care a lot about latency.”

And in the analytical estate, she said, is where users run long jobs to crunch data: “Usually these are reports or some decision-making process that we are willing to wait a couple of hours to get the information, and it’s not necessarily where we need it right now.” This could be a data lake or data warehouse, for instance.

The operational estate is upstream; the analytical state, downstream. As applications run, they are communicating both upstream and downstream, with many point-to-point connections, Polak said. As a result, there’s a lot of chaos — and potentially, a lot of pain for developers.

With the point-to-point connections inherent in a system where data is a motion, Polak said, “schema evolution” is bound to happen — an application’s schema changes upstream and now it’s having an impact downstream.

“How can we build a healthy contract between those two states and also reflect back on how engineering teams are building?” she asked. “Usually, you’ll have different teams working on different states. So it becomes kind of like an engineering organization challenge sometimes.”

That’s where [Apache Iceberg](https://thenewstack.io/apache-iceberg-a-different-table-design-for-big-data/) and [Apache Flink](https://thenewstack.io/apache-flink-2023-retrospective-and-glimpse-into-the-future/) come in, she told TNS Publisher and Founder [Alex Williams](https://thenewstack.io/author/alex/) in this edition of Makers.

## Iceberg: Saving Time and Costly Errors
Apache Iceberg, developed by [engineers at Netflix](https://thenewstack.io/netflix-open-sources-maestro-a-next-gen-data-workflow-engine/), began as an attempt to solve the problem posed by the proliferation of temporary files generated during large-scale data processing.

It’s a [lightweight, open table layer](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/) that sits on top of storage in the analytical estate, Polak said.

Apache Iceberg “helps us define the contract of tables, the notion of tables. If the table itself, the data, is distributed… which files are related to that specific table, which version, which columns are in the table.”

When an engineer writes a [SQL query](https://roadmap.sh/sql), she added, “this statistical data is being pulled out of tools like Iceberg to improve the performance of the query itself. So it doesn’t go and try and scan all of the data lake; it will only pinpoint to the exact files that it needs. Which you can imagine how it saves cost and time — and potential errors.”

Iceberg has been adopted by [Airbnb](https://thenewstack.io/how-airbnb-and-twitter-cut-back-on-microservice-complexities/), [Adobe](https://thenewstack.io/adobe-developers-use-webassembly-to-improve-users-lives/), [Apple](https://thenewstack.io/apples-open-source-roots-the-bsd-heritage-behind-macos-and-ios/), [Expedia](https://thenewstack.io/how-expedia-group-moved-from-21-platform-stacks-to-1/), [LinkedIn](https://thenewstack.io/linkedin-open-sources-openhouse-data-lakehouse-control-plane/) and [Lyft](https://thenewstack.io/lyfts-tips-for-avoiding-software-crashes/), among other companies.

## Flink: New Trends
Apache Flink is an open source data processing framework, suitable for batch or streaming queries. Recently, Flink has found itself at the center of two architecture trends, Polak said.

One, “some batch processing capabilities are being shifted left into the [stream processing](https://thenewstack.io/3-reasons-why-you-need-apache-flink-for-stream-processing/),” she said. “So things like quality assurance, early on governance, compliance early on. Some more simplistic, aggregations or simplistic filtering that we can do early on, before we’re sending that trial data [to a] data lake. So that’s kind of interesting shift that’s been happening from the analytics estate into the operational estate.”

And two, “some of the microservices are actually looking into if they can move from being a microservices into being a Flink streaming app.”

This movement is happening, Polak said, because microservices “will come up or they’ll always be up, and they always try and query either Kafka or any other source that brings them information, do some processing, and then dump it back into syncing into Kafka or any other data collector or queue that I have there in-house.

“Instead of doing that, we can leverage things like Flink, for [data streaming](https://thenewstack.io/data-streaming/) applications, where Flink is always listening on data coming in,” she said. This would make systems more reliable and achieve lower latency: “The system doesn’t need to go up and load memory. It’s already there. It’s always there and always listening. And then it can process the data, and much faster.”

Polak and Williams talked about how customer demands are accelerating the development of technology that helps abstract the processing and analysis of real-time data.

“Customers want their answers right now,” Polak said. For instance, “if have a flight, and I’m commuting to the airport, I want to know if my flight is delayed right away so I can make decisions, right? Do I leave the house? Do I stay? Do I wait another 15 minutes, and I’m going to hit traffic because of that?”

As customers drive the demand for more real-time information, she said, “it trickles down all the way to the architecture. And then the question is, how my architecture supports that request, knowing that cannot wait an hour to crunch the data.”

Check out the full episode for a deeper dive into Apache Kafka-enabled data streaming and the role Iceberg and Flink play.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)