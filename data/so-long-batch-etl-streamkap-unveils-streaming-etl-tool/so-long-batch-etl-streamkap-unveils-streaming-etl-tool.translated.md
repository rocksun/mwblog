# So Long, Batch ETL: Streamkap Unveils Streaming ETL Tool
![So Long, Batch ETL: Streamkap Unveils Streaming ETL Tool 的推荐图片](https://cdn.thenewstack.io/media/2024/08/db715b71-streaming-4198529_1280.jpg)

For organizations looking to accelerate their data management speeds — or just move data — to capitalize on low-latency business opportunities, there’s a seemingly endless number of real-time data processing frameworks to choose from. Popular options include [streaming data platforms](https://thenewstack.io/confluent-wants-to-make-batch-processing-a-thing-of-the-past/), [real-time databases](https://thenewstack.io/how-to-introduce-real-time-data-predictions-with-redpanda/), [time-series databases](https://thenewstack.io/install-the-influxdb-time-series-database-on-ubuntu-server-22-04/) and a plethora of other tools designed to address these needs.

[Streamkap](https://streamkap.com/), a startup founded in 2022 that recently closed $3.3 million in seed and pre-seed funding, differentiates itself from nearly all of these options in two key ways. First, while it’s built on top of [Apache Kafka](https://thenewstack.io/kafka-3-8-brings-faster-startups-to-java-developers/) and [Apache Flink](https://thenewstack.io/apache-flink-2023-retrospective-and-glimpse-into-the-future/), the platform doesn’t require a significant infrastructure investment. 
Users don’t need to re-architect existing processes for it. Rather, it offers what Streamkap CEO [Paul Dudley](https://www.linkedin.com/in/pauldudley) calls a “more application-like experience.”

Second, Streamkap is laser-focused on providing streaming extract, transform and load (ETL) — which is not the same as stream processing — to dramatically speed up traditionally batch processes, all while fitting neatly into the same, familiar paradigm.

“Consumers are coming to expect that the experiences they have are powered by real-time data, so businesses have to figure out how to do that,” Dudley said. “We’re trying to make it easier for businesses to remove what’s often the biggest bottleneck, which is their batch ETL, without having to change their entire architecture to do it.”

## Streamkap for Data Pipelines
While Streamkap can support routing data from event-producing endpoints to analytics tools, its typical use case is pipelining data from transactional databases to analytical destinations, such as [Snowflake](https://www.snowflake.com/?utm_content=inline+mention). Its Kakfa and Flink foundation, coupled with its reliance on [change data capture](https://thenewstack.io/change-data-capture-for-real-time-access-to-backend-databases/) (CDC) and the platform’s ability to adapt to schema changes, makes this a reality for enterprises.

“Streamkap is powered by a streaming architecture, but it doesn’t require companies to completely rebuild their entire data stack,” Dudley said. “They just get faster data.”

## Kafka and Flink
Generally speaking, Streamkap relies on [Kafka](https://kafka.apache.org/) for simple ETL jobs that don’t involve a lot of transformations, while Flink is leveraged for jobs that do involve such transformations. Kafka’s publish-subscribe model is essential to Streamkap’s ETL services, persistence and overall resilience, while increasing the speed of this pre-analytics process.

According to Dudley, this aspect of Kafka gives Streamkap “extreme resilience and a distributed log. So if the source or the destination goes down, our system can be the resilient center and replay the data; we also persist the data if the destination goes down.”

As such, Kafka is a critical component of the pipelines Streamkap builds. [Flink](https://flink.apache.org/) is equally important, especially as ETL needs become more complex.

Dudley described a use case in which a fashion retailer integrated data in its MySQL with low-latency event data from its website to provide real-time personalization to website visitors, similar to TikTok. “That’s powered by Flink, because you’re joining data from two different data sources, and you have to maintain state to do that effectively, so Flink is the tool for that,” Dudley noted.

However, because Streamkap is so low-touch when it comes to infrastructure management, users don’t need to concern themselves with the details of which stream processing resources are involved in their applications. The ETL tool masks this complexity, giving users “easy access to low-latency data,” Dudley said.

## Change Data Capture
Streamkap relies heavily on CDC to load data from sources to destinations. It offers connectors for a number of popular sources, including data lakes, cloud data warehouses, databases and more, many of which are CDC-based.
根据 Dudley 的说法，CDC 是以亚秒级延迟交付流数据的最佳选择，因为“我们从中读取变更数据捕获的数据库日志实际上是一个流数据源。数据源本身是事件驱动的。对数据库的每一个新更改都会作为事件写入该日志。这非常适合流式传输。”

Streamkap 还包含一个增量快照模型，这对于确保所有数据及其更改都已从源移动到目标非常有用。它对于协助目标系统的回填过程特别有用。

“对于回填，您希望能够与其并行捕获新的流事件，以便这些事件不会相互依赖，并确保回填不会对源数据库造成过大的负载，”Dudley 解释道。“我们同时做这两件事。” 此外，由于 Kafka 提供的弹性，用户不必像使用批处理 ETL 处理方法那样频繁地进行回填。

## 模式漂移支持

除了历史快照之外，Streamkap 还提供了一个模式漂移支持功能，该功能允许在不减慢或破坏 [数据管道](https://thenewstack.io/simplified-data-pipelines-with-pulsar-transformation-functions/) 的情况下更改模式。当开发人员想要通过添加列等方式更改模式时，这些更改会以简化的方式平滑地传播到下游数据模型。

“我们的系统所做的是自动考虑新列或数据类型的新更改，并确保您的数据在进行更改时能够继续流动，而无需停止，”Dudley 提到。

Streamkap 还提供应用内警报功能以及自动监控功能，以通知用户更改。这些机制“旨在让客户了解实际管道本身是否发生变化，以及是否存在任何问题，”Dudley 透露。

## 正确的视角

通过在其平台上搭建 Flink 和 Kafka，Streamkap 利用了一些最现代、最有效的工具来转换和传输流数据。它被定位为流式 ETL 工具这一事实说明了 ETL 模型的悠久历史、其持续的企业相关性以及其从批处理到实时应用的必然转变。

批处理可能仍然存在于整个数据生态系统中，特别是对于仍在使用遗留系统的组织而言。然而，加快数据集成需求以使其跟上当代消费者和业务需求的步伐的需求是显而易见的——这体现在 Streamkap 最近的融资中，即使不是它的存在本身。

[YOUTUBE.COM/THENEWSTACK
技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等内容。](https://youtube.com/thenewstack?sub_confirmation=1)