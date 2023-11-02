<!--
# 使用Apache Flink的4个理由
Image from Pixabay.
https://cdn.thenewstack.io/media/2023/10/5ffe1942-squirrel-1024x683.jpg

-->

译自 [4 Reasons Why Developers Should Use Apache Flink](https://thenewstack.io/4-reasons-why-developers-should-use-apache-flink/) 。

Apache Kafka已经成为企业内流式数据传输的首选平台。但如果数据可以被清洗、丰富后为下游更多应用提供服务，那么流式处理就更有价值。这就是流处理的作用。

流处理允许你持续消费数据流，用额外的业务逻辑处理数据，并将其转化为新的流，以便其他人可以在自己的应用中重复使用。其应用范围广泛，包括实时控制面板、机器学习模型、物化视图，以及事件驱动的应用和微服务。

![](https://cdn.thenewstack.io/media/2023/10/64df5a12-image1a.png)

*流处理用额外的业务逻辑增强数据流，将其转化为新的可重复使用的数据流，以供下游应用和流水线使用。*

处理逻辑的复杂度因具体应用场景而异，范围从简单的过滤和聚合，到更复杂的多路时间关联和任意事件驱动逻辑。因此，与其他选项([如定期批处理](https://javaee.github.io/tutorial/batch-processing001.html)、[ELT](https://www.techtarget.com/searchdatamanagement/definition/Extract-Load-Transform-ELT?Offer=abMeterCharCount_var2)、[经典两层架构](https://www.oreilly.com/library/view/stream-processing-with/9781491974285/ch01.html))相比，流处理的优势因情况而异。

尽管如此，推动采用流处理的关键因素通常属于以下一个或多个类别:

- **延迟:** 流处理大大缩短事件发生和反映在产品或用户体验中的时间，无论是控制面板、机器学习模型还是其他应用。
- **创新和重用性:** 流处理将数据产品转化为可共享的资产，可供下游应用和系统消费和构建。数据流成为可重用的构建块，具有明确定义和一致的访问方式，使其他团队可以轻松在新产品和应用中使用。
- **成本和资源效率:** 持续处理可随时间分配工作，提高资源利用率。此外，上游处理(如预聚合、会话等)极大地减少下游系统(如数据仓库、实时分析数据库等)的成本，并加速其查询。
- **表达性:** 生活不会分批次发生。与定期批处理不同，流处理不会在数据中引入人为边界，从而影响处理逻辑。

## 考虑Apache Flink的四个理由

Flink是最活跃的[Apache项目](https://flink.apache.org/2023/03/23/announcing-the-release-of-apache-flink-1.17/)之一，提供了流处理和批处理的统一框架。像Uber、Netflix、LinkedIn这样的数字化先锋公司使用Flink，传统企业如高盛和Comcast也在使用。

Flink也拥有大型且活跃的贡献者社区，其中包括Apple和阿里巴巴等公司的支持，这有助于保证持续创新。因此，Flink的采用速度与Kafka早期阶段相当。

![](https://cdn.thenewstack.io/media/2023/10/761364fb-image2a.png)

*Flink的增长速度与Kafka生命周期相同阶段基本相当。*

下面是公司选择Flink而非其他流处理技术的四大常见原因：

### 第一: 它是一个强大的执行引擎

Flink拥有强大的运行时，具有卓越的资源优化、高吞吐量与低延迟以及可靠的状态处理。具体来说，运行时可以:

- 实现每秒数千万条记录的持续吞吐量
- 大规模下保持亚秒级延迟
- 跨系统边界保证端到端的恰好一次处理
- 即使在故障和无序事件下也能计算出正确结果
- 管理和在错误时恢复高达数十TB的状态

Flink可根据用例配置各种工作负载，包括流处理、批处理或两者的混合。

### 第二: 兼容多种API和语言

Flink提供了四种不同的API，可满足不同用户和应用需求。Flink还支持多种编程语言，包括Python、Java和SQL。

![](https://cdn.thenewstack.io/media/2023/10/63490d5a-image3a.png)

*Flink提供了多层次的API，抽象级别不同，既可处理常见用例，也可处理不太常见的用例。*

适用于Java和Python的DataStream API通过链接FlatMap、Filter、Process等转换函数创建数据流图。在这些用户定义函数中，你可以访问状态流处理器的基本组件，如状态、时间和事件。这让你可以细粒度控制[记录在系统中的流动](https://thenewstack.io/ditching-databases-for-apache-kafka-as-system-of-record/)以及读写和更新应用状态。如果你熟悉Kafka Streams DSL和Kafka Processor API，使用体验会很熟悉。

Table API是Flink更现代的声明式API。它允许你用连接、过滤、聚合、投影等关系操作以及各种用户定义函数编写程序。与DataStream API类似，Table API支持Java和Python。使用此API开发的程序会进行类似Flink SQL查询的优化，与SQL共享若干特性，如类型系统、内置函数和验证层。该API与Spark Structured Streaming、Spark DataFrame API和Snowpark DataFrame API有相似处，不过那些API更侧重微批和批处理而非流处理。

基于与Table API相同的底层架构，Flink SQL是遵循ANSI标准的SQL引擎，可处理实时和历史数据。Flink SQL使用Apache Calcite进行查询规划和优化。它支持任意嵌套子查询，广泛的语言支持包括各种流连接和模式匹配，拥有广泛的生态系统，包括JDBC驱动程序、目录和交互式SQL Shell。

最后是“Stateful Functions”，它简化了状态化分布式事件驱动应用的创建。这是Flink项目下的一个独立子项目，与Flink的其他API很不相同。Stateful Functions可以理解为一个基于Flink运行时的状态化、容错的分布式Actor系统。

广泛的API选择使[Flink成为流处理的理想选择](https://thenewstack.io/3-reasons-why-you-need-apache-flink-for-stream-processing/)，随着需求和用例的演变，你可以随时间混合使用不同的API。

### 第三: 流处理和批处理融合

Apache Flink[统一了流处理和批处理](https://developer.confluent.io/courses/apache-flink/stream-processing-exercise/)，因为其主要API(SQL、Table API和DataStream API)同时支持有界数据集和无界数据流。具体来说，你可以根据正在处理的数据性质，以批处理或流处理模式运行相同程序。你甚至可以让系统为你选择处理模式。

- 只有有界数据源 → 批处理模式
- 至少一个无界数据源 → 流处理模式

![](https://cdn.thenewstack.io/media/2023/10/b58c017f-image4.png)

*Flink可以在同一平台上统一流处理和批处理。*

流批处理的统一为开发者带来实实在在的好处：

- 在实时和历史数据处理场景提供一致语义
- 在实时和历史数据处理应用间复用代码、逻辑和基础设施
- 在单一应用中组合[历史和实时数据](https://thenewstack.io/historical-data-and-streaming-friends-not-foes/)处理

### 第四: 它已做好生产就绪准备

Flink是一个成熟平台，在最苛刻的生产场景中经受住了检验。表现这一点的特性包括：

- 开箱即用地与Datadog、Prometheus等工具集成的指标系统，也可与自定义解决方案集成
- 通过Flink Web UI进行全面的可观测性、故障排查和调试支持，包括回压监控、火焰图和线程转储
- 保存点，允许你在保持恰好一次语义的前提下，状态式扩展、升级、分叉、备份和迁移应用

## Flink和Kafka: 强大组合

Flink和Kafka经常一起使用，事实上Kafka是Flink最热门的连接器。两者高度兼容，在许多方面Kafka推动了Flink的广泛采用。

需注意，Flink本身不存储任何数据，它对其他地方存储的数据进行操作。可以把Flink视为Kafka的计算层，为实时应用和流水线提供支持，而Kafka是流数据的基础存储层。

![](https://cdn.thenewstack.io/media/2023/10/89ef6dd2-image5.jpg)

*在数据流堆栈中，Flink处理计算需求，Kafka提供存储层。*

随时间推移，Flink在支持Kafka应用方面越来越娴熟。它可以将Kafka用作数据源和数据汇，利用Kafka丰富的生态系统和工具。Flink还原生支持热门的数据格式，包括Avro、JSON和Protobuf。

对Flink来说，Kafka也是一个同样好的匹配。与ActiveMQ、RabbitMQ或PubSub等其他消息系统相比，Kafka为Flink提供持久且无限的数据存储。此外，Kafka允许多个消费者同时读取流并按需倒带。第一个属性补充了Flink的分布式处理范式，第二个对Flink的容错机制至关重要。

## 渴望更多了解Flink？

想深入了解的话，可以在Confluent Developer网站的[Flink 101课程](https://developer.confluent.io/courses/apache-flink/intro/)或这个[Apache Flink培训](https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/overview/)中动手实践。
