# 从 Netflix 到 Walmart：开源 Kafka 实践

![特色图片：从 Netflix 到 Walmart：开源 Kafka 实践](https://cdn.thenewstack.io/media/2025/03/cfcef75f-open-source-kafka-in-action-1024x576.jpg)

从电子商务交易到物联网 (IoT) 传感器数据，再到安全日志等等，企业面临着不断增长的实时数据洪流，这些数据对于客户体验、运营和业务效率至关重要。对于许多企业来说，开源事件流平台 [Apache Kafka](https://kafka.apache.org/) 已经成为解决方案。

想知道如何才能最好地利用 Kafka 吗？

这份快速入门指南涵盖了具体的 Kafka 用例、来自一些最大和最关键数据企业的真实案例，以及帮助您尽快获得所需结果的运营最佳实践。

## Kafka 能为您做什么？

Kafka 在四个关键的企业场景中表现出色：实时数据处理、消息传递、运营指标和日志聚合。

### 实时数据处理

实时数据处理是 Kafka 真正闪光的地方。可以将 Kafka 视为企业的中央神经系统。[开源技术](https://thenewstack.io/how-to-explain-the-security-advantages-of-open-source) 可以即时处理来自多个来源的数百万个事件，同时确保不会丢失任何数据。

例如，电子商务平台可以使用 Kafka 同时[处理客户点击](https://engineering.linkedin.com/kafka/kafka-linkedin-current-and-future)、库存更新和发货状态更改，从而实现实时个性化和库存管理。Kafka 的架构以最小的延迟和最大的可靠性处理这些[海量数据流](https://thenewstack.io/introduction-to-data-streaming)，而其内置的分析功能使团队能够从其数据流中提取即时见解。

### 消息传递

Kafka 的消息传递功能充当数字交换机，实现数百甚至数千个应用程序和系统之间的无缝实时通信。考虑一家处理信用卡交易的金融服务公司：Kafka 可以同时将交易数据路由到欺诈检测系统、客户数据库和分析平台，而不会遗漏任何信息。

随着组织规模的扩大和消息量的增加，Kafka 也会随之扩展，在处理负载的同时确保不会丢失任何关键通信。

### 运营指标

运营指标充当控制塔，Kafka 用于收集和提供数据，以监控整个技术堆栈中的实时指标。无论您是跟踪应用程序性能、系统健康状况还是业务关键绩效指标 (KPI)，Kafka 都为实时监控和警报提供单一的事实来源。

全球企业使用 Kafka 每秒监控数百万个指标，在潜在问题影响客户之前发现并解决这些问题。Kafka 还可以与最流行的监控工具无缝集成，从而轻松地可视化趋势并在需要时采取措施。

### 日志聚合

最后但并非最不重要的一点是，Kafka 将日志管理从令人头疼的问题转变为战略资产。团队无需费力地将来自数十或数百个系统的日志拼凑在一起，而是可以获得对其基础设施中发生的一切的完整实时视图。

当发生安全事件时，分析师可以立即访问和分析来自任何系统或时间段的相关日志。大型企业每天通过 Kafka 处理数十亿个日志条目，使用这些全面的数据进行从威胁检测到应用程序性能优化的一切工作。与在重负载下崩溃的传统日志记录系统不同，即使日志量呈指数级增长，Kafka 也能保持其性能。

## 现实世界的企业如何使用 Kafka？

让我们看看世界上一些最著名的企业是如何[使用 Kafka](https://thenewstack.io/how-we-completed-a-massive-kafka-and-cassandra-migration) 的。

### Netflix 掌握实时个性化

Netflix 在全球拥有约 3 亿用户，每秒[处理](https://thenewstack.io/developer-productivity-engineering-at-netflix/)天文数字般的用户数据。Kafka 是 [Netflix 实时个性化引擎](https://netflixtechblog.com/kafka-inside-keystone-pipeline-dd5aeabaf6bb) 的[骨干](https://netflixtechblog.com/kafka-inside-keystone-pipeline-dd5aeabaf6bb)，可即时处理观看者的行为，以提供精准的内容推荐。每一次点击、暂停和播放决定都会反馈到 Netflix 的 Kafka 系统中，使该公司能够不断改进每个观看者的体验。任何具有数字业务的企业都可以应用类似的方法，将客户数据转化为更个性化的体验。

### Pinterest 支持瞬间内容发现
Pinterest 必须通过即时将用户与其喜爱的内容连接起来，从而保持数亿用户的参与度。[该公司使用 Kafka](https://medium.com/pinterest-engineering/how-pinterest-runs-kafka-at-scale-ff9c6f735be#:~:text=Pinterest%20runs%20one%20of%20the%20largest%20Kafka%20deployments%20in%20the%20cloud.%20We%20use%20Apache%20Kafka%20extensively%20as%20a%20message%20bus%20to%20transport%20data%20and%20to%20power%20real%2Dtime%20streaming%20services%2C%20ultimately%20helping%20more%20than%20250%20million%20Pinners%20around%20the%20world%20discover%20and%20do%20what%20they%20love.) 和有状态的流处理来实时处理数据流，使其推荐引擎能够根据每个用户最近的活动提供建议。Kafka 的 [Streams API](https://kafka.apache.org/documentation/streams/) 提供了这种能力，支持需要处理到达的数据的用例，同时维护多个数据记录的状态信息（能够利用以前的记录）。

### Walmart 扩展实时商务运营

作为美国[最大的零售商](https://nrf.com/research-insights/top-retailers/top-100-retailers/top-100-retailers-2024-list)，Walmart 在美国的庞大零售业务依赖于实时数据处理，以处理其云基础设施中每天数万亿条 Kafka 消息。由于它面临着数据流量的突然高峰，尤其是在像假日季这样的高交易量购物期间，Walmart 的工程团队开发了一种名为 [Messaging Proxy Service](https://medium.com/walmartglobaltech/reliably-processing-trillions-of-kafka-messages-per-day-23494f553ef9) 的创新解决方案，从根本上改变了他们处理消息处理的方式。这种重新构想 Kafka 基础设施的明智策略使 Walmart 能够在高峰期保持高性能，同时降低运营成本。

## 运用 Kafka

处理实时数据并采取行动正变得越来越不是一种优势，而是一种必然。在我看来，Kafka 已经证明了自己是需要自信地处理海量数据流的企业的首选平台。

无论您是制定实时分析策略、支持个性化体验还是实现安全运营现代化，Kafka 都能为您提供所需的基础——并且在其完全开源版本中功能非常强大。

来自 Netflix、Pinterest 和 Walmart 的示例展示了部分可能性以及一些最大的企业正在使用该平台所做的事情。通过正确的方法和最佳实践，您的组织可以加入这些领导者的行列，充分利用您的实时数据。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)