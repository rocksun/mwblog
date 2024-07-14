# 为什么我们在规模化实时数据中使用 Apache Kafka

![为什么我们在规模化实时数据中使用 Apache Kafka 的特色图片](https://cdn.thenewstack.io/media/2024/07/8eb38c8c-kafka-real-time-data-scale-1024x576.jpg)

在一个数字威胁不断演变的世界中，拥有准确的实时数据进行安全扫描至关重要。最新的数据是 [SecurityScorecard](https://securityscorecard.com/) 的生命线。该公司通过利用互联网资源来识别潜在漏洞，包括暴露的服务器、可疑 IP 地址、被盗员工帐户、受恶意软件感染的设备等，为组织提供全面的安全态势视图。

为了跟上不断增加的安全威胁数量，SecurityScorecard 分析了 300 多种问题类型，每天识别出 2000 多亿个安全漏洞。数据收集和处理不仅需要大量数据，还需要准确的、大规模的实时数据。这种需求促使 SecurityScorecard 采用 [数据流](https://www.youtube.com/watch?v=_RcnZ2XfuXw)，并使用 Confluent Cloud 和 Confluent Platform 的组合来构建流数据管道，以更快地扩展并更好地治理数据。

## 用于数据流和处理的实时管道

SecurityScorecard 构建的解决方案从数字来源挖掘数据以识别安全风险。数据流帮助该公司通过在毫秒内分析信息来检测不断变化的威胁，而不是数周或数月。该公司在其平台上构建了开源 [Apache Kafka](https://thenewstack.io/ditching-databases-for-apache-kafka-as-system-of-record/)，因为没有其他系统提供构建所需任何内容的基本工具。

SecurityScorecard 的威胁研究团队过去曾自行管理 Kafka，但每天花费 8 个小时进行维护会分散产品开发时间。该团队依靠 [批处理管道将数据传输](https://thenewstack.io/the-unfortunate-reality-about-data-pipelines/) 到和从 [AWS](https://aws.amazon.com/?utm_content=inline+mention) S3。他们还使用昂贵的基于 REST API 的通信来进行系统之间的数据交换，并使用 RabbitMQ 进行流处理活动。

为了减轻负担，SecurityScorecard 的威胁研究开发团队创建了 [Horus](https://support.securityscorecard.com/hc/en-us/articles/8528362400539-How-SecurityScorecard-collects-data-for-ASI)，这是一个全球分布式系统，能够在 Confluent 之上运行任何基于代理的代码，无论在世界上的任何地方。Horus 使用实时流管道和连接器来处理数据。该团队编写了基于 Python 的应用程序，并将其作为代理部署到此系统中。目前，这些代理已部署在全球各地，以执行诸如 IPv4 扫描、网络爬取、漏洞检测以及与合作伙伴数据源的 API 集成等任务。

自构建 Horus 以来，SecurityScorecard 在流式基础设施方面节省了超过 200 万美元，而这笔钱原本需要用于内部管理开源 Kafka。

除了 Horus 之外，SecurityScorecard 的威胁研究团队还在流式平台上实施了所有 [新系统并刷新了旧系统](https://support.securityscorecard.com/hc/en-us/articles/8528362400539-How-SecurityScorecard-collects-data-for-ASI)。其中一些包括深层和暗网泄露的凭据、泄露密码的集合以及黑客聊天，以及来自 90 多个国家/地区的蜜罐的全球被动传感器数据同步到 Kafka。此外，[BreachDetails](https://support.securityscorecard.com/hc/en-us/articles/19200200869915-Use-BreachDetails-to-respond-faster-to-breaches-in-your-ecosystem)，一个定制的违规事件收集系统，监控公共网络和政府网站以查找数据泄露通知，让客户知道他们的供应商何时遇到安全事件。

## 数据治理和效率的放大

数据治理对 SecurityScorecard 至关重要。该公司使用自定义构建的 Protobuf 库来管理对敏感数据的访问。SecurityScorecard 的目标是使多个团队能够更轻松地共享和治理相同的数据源。Confluent 的 Stream Governance 功能和基于角色的访问控制将允许数据平台团队控制对集群的访问。随着数据治理变得越来越细化，SecurityScorecard 可以将流式传输扩展到更多团队，以增强安全性。
Confluent plays a key role in SecurityScorecard's web scanning and crawling capabilities, pushing billions of records from vulnerability tracking databases to Confluent. This allows any team to "replay" the data. Fully managed connectors, including [PostgreSQL](https://roadmap.sh/postgresql-dba) and AWS S3 Sink connectors, enable teams within the company to access streaming data for a variety of purposes. These source connectors create [a data archive that acts as an asset history](https://thenewstack.io/historical-data-and-streaming-friends-not-foes/), linking data sources together in real time, forming a consistent data layer across the business.

The efficiency of a fully managed system saved SecurityScorecard two full-time positions. A new product, the Attack Surface Intelligence (ASI) module, aggregates petabytes of streaming data from SecurityScorecard through Confluent and pushes it to data receivers via Kafka Connect, enabling customers to search the entire internet for open ports, vulnerable machines, threat actors, malware, and other information. Another product, Automated Vendor Detection (AVD), processes web crawling and partner data in real time to provide a complete view of customer supply chain security, highlighting connections between customers and their vendors.

## Overcoming Data Bottlenecks in a Hybrid Cloud Environment
Previously, [Brandon Brown](https://www.linkedin.com/in/brandon-brown-8529681b/), Principal Software Engineer on the SecurityScorecard architecture team, faced significant challenges in upgrading Kafka versions and managing the operational needs of Amazon Managed Streaming (MSK). These tasks consumed valuable time during scaling that could have been spent developing business applications.

MSK was not meeting SecurityScorecard's operational needs, and operations like version upgrades were difficult and manual. The team needed to determine cluster sizes and faced challenges deciding how many brokers to set up.

Since migrating to Confluent Cloud, these difficult tasks, such as cluster and connector management, have become simpler and more reliable. Brown estimates that by solving this operational problem, his team saves approximately $125,000 per year. The migration also alleviated additional operational overhead, reducing day-2 operations by 80% and lowering projected annual operational costs overall by 48.3%.

Large JSON files also presented challenges when building data pipelines. They required a significant amount of processing time. Brown developed a fan-out process that places messages in specific topics with schemas, enabling the team to subscribe to specific topics and consume data from the Kafka cluster faster. Now, Brown's team consumes binary messages, which do not require filtering.

## Unmatched Scalability and Data Governance
SecurityScorecard previously scanned 80 ports in a month and a half, but now it can scan over 2,000 ports in 10 days. This achievement has helped the company gain new customers who need access to large amounts of data. It has also streamlined the company's systems and scaled data ingestion and processing by 10x to 100x.

Looking ahead, the threat research and data platform team has been using streaming data pipelines to enhance data discovery and shareability across all teams. They plan to work with the core engineering team to leverage [Apache Flink](https://thenewstack.io/3-reasons-why-you-need-apache-flink-for-stream-processing/) to reduce custom service deployments for simple connection tasks, enhancing real-time data processing, integrating observability, and lowering infrastructure costs.

## Recommendations for Building a Reliable Real-Time Streaming Data Pipeline
When building streaming data pipelines, you should establish a definition of timeliness, always use schemas when interacting with other teams, leverage the ecosystem, and only develop and maintain components that are absolutely necessary.

Timeliness is important because it limits how quickly you need to react when something goes wrong and also allows you to define realistic service level agreements (SLAs) to identify anomalies. Schemas ensure that your consumers know the shape of the data they are getting and allow teams to set up data quality rules to flag issues early. Leveraging the ecosystem allows you to take advantage of a wealth of knowledge and battle-tested systems.

While you could write an application to sync data to a data store, by using connectors, you get parallel retry logic and dead letter queues for free. Otherwise, you have to write the application *and* test it, and set up appropriate alerts and monitoring. Ultimately, you will be maintaining a system that keeps you away from using data to develop business value. Using a managed data streaming platform eliminates these issues so you can focus on innovation instead of infrastructure management.

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don't miss a beat. Subscribe to our YouTube
channel to watch all our podcasts, interviews, demos, and more.


### TRANSLATOR'S RESPONSE

### EDITOR'S RESPONSE
[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)