<!-- 
# 解析Kafka: 复杂性所带来的价值
https://cdn.thenewstack.io/media/2023/11/2c5bc159-screenshot-2023-11-03-at-9.57.39-am-1024x588.png
 -->

Kafka在大规模内部托管和管理方面确实很困难，但它提供的实际好处和功能超过了运营方面的挑战。

> 译自 [Decoding Kafka: Why It’s Worth the Complexity](https://thenewstack.io/decoding-kafka-why-its-worth-the-complexity/) 。

[Apache Kafka](https://kafka.apache.org/intro)是一个分布式事件流平台，由LinkedIn处理实时数据流的需求而诞生，功能强大且多样。它非常适合流处理、高性能数据流水线、实时分析、日志聚合、事件存储和事件源等使用场景。

许多公司已经将Kafka作为事件驱动架构的主干，但其他公司却不愿[在技术栈中包含Kafka](https://thenewstack.io/how-to-make-kafka-cloud-native/)。这是因为Kafka的学习曲线陡峭、运维复杂，给人畏惧感。这可能会促使一些组织选择更易管理的其他技术。问题是，这些更简单的替代方案能否提供与Kafka相同的优势？

## Kafka的优势

自十多年前问世以来，Kafka已经成为数据流领域的标准选型，因为它具有以下优势:

- **可扩展性** — 每天可以处理数万亿条消息，按主题划分为数万个分区，部署在数百个或者更多的代理(Broker)上。
- **高性能** — 每秒可以处理数百万条消息和多个GB的数据，延迟保持在毫秒级。
- **容错性和高可用性** — 每个分区的副本配置在多个Broker上，没有单点故障。可以复制整个Kafka集群，复制集群可以部署在不同数据中心甚至不同地区。
- **数据完整性** — 保证分区内消息顺序、恰好一次语义和长期数据保留。
- **丰富的生态系统** — Kafka Streams用于流处理，Kafka Connect用于与源和目标系统集成，支持多种编程语言的客户端库。

凭借这些特性，跨越IT、金融、制造、电信、零售、医疗、运输等多个行业的成千上万的组织已经[将Kafka作为核心技术](https://thenewstack.io/ditching-databases-for-apache-kafka-as-system-of-record/)来处理海量、高频的数据流。

一个例子是R3，一家金融服务领域的公司。R3的主要产品之一是Corda，一个分布式账本技术(DLT)平台，可以用来构建交易、贷款、资产管理和保险等金融应用。[Kafka就是R3用来构建Corda 5(也称为Next-Gen Corda)的技术](https://developer.r3.com/blog/why-kafka-was-selected-for-next-gen-corda/)之一。

> R3高级开发传道师Divya Taori表示: “在为Next-Gen Corda设计运行时基础设施时，主要目标是实现热备份、高可用的配置，实现工作分片以最大化吞吐量、降低成本。”

在选择Kafka之前，还考察了其他选项，比如消息总线、[Apache Flink](https://thenewstack.io/apache-flink-for-real-time-data-analysis/)或Akka集群。但是，评选小组认为，Kafka是Corda 5的最佳选择，因为它“实现了所有必需的功能，并在生产环境大规模使用”，并称“作为高可用、低延迟消息传递的行业标准，Kafka更适合Next-Gen Corda”。

选择Kafka作为Next-Gen Corda技术栈的一部分，似乎是一个正确的决定，带来了正面的结果。

> Divya Taori表示: “通过利用Kafka作为Corda通信基础设施的支柱，Corda 5实现了所需的高可用性、横向扩展性和降低总拥有成本，最终满足了客户的严苛需求。”

[另一个依赖Kafka的公司是客户参与软件供应商MoEngage](https://www.moengage.com/blog/kafka-at-moengage/)。Kafka于2016年首次引入，用于一个小案例。随后，Kafka变得无所不在；如今，MoEngage使用Kafka进行消息传递、流处理、日志聚合、变更日志和状态管理等。

MoEngage最初使用一个大型Kafka集群，监控很少。这种设置一段时间工作良好。但是，随着组织扩大、数据量增加，使用单一Kafka集群变得有问题——出现单点故障，扩展困难，难以在代理之间平均分配负载。MoEngage团队后来根据多集群模型重构了Kafka架构。这不是一个轻松的任务，但似乎是值得的:

> MoEngage数据工程师Amrit Jangid表示:“我们的新Kafka架构为系统带来了大幅提升的可靠性。[...] 与老集群相比，我们现在可以更好地满足对客户的SLA承诺，而且优点是我们实现这一点的成本降低了20%。”

以上只是几个例子，但实际[依赖Kafka的公司名单还要多得多](https://cwiki.apache.org/confluence/display/KAFKA/Powered+By)，包括知名公司如LinkedIn、Twitter、PayPal、Netflix、Spotify、Uber、Cloudflare、Airbnb、Skyscanner、Slack、高盛等。许多组织已经分享了他们如何以及为何要使用Kafka，使用的规模以及获得的好处——我建议你[查看他们的经验](https://github.com/dttung2905/kafka-in-production)。

## Kafka有多复杂？

首先，学习Kafka需要时间和专注。新手可能需要几天或几周掌握基础，需要几个月精通高级特性和概念。此外，需要不断监控和学习集群性能，以及跟进Kafka的发展和新特性。

设置Kafka部署存在挑战，成本高且耗时。根据规模和具体设置，可能需要几天到几周不等。您可能决定专门组建一个平台团队来管理Kafka。以下是涉及的内容:

- 在集群中安装多个Kafka Broker，创建主题和分区，开发生产者和消费者应用。管理多个Kafka集群会增加复杂度。例如，[Uber构建多区域Kafka基础设施提](https://www.uber.com/blog/kafka/)供冗余和跨区域故障转移就非常具挑战性。
- [数百个配置参数](https://kafka.apache.org/documentation/#configuration)需要权衡。比如，更高的副本因子提升数据持久性，但也增加存储需求。另一个例子:严格的一次性语义会降低吞吐量并增加延迟。
- 配置其他组件，如连接器将数据流到其他系统，如Kafka Streams进行流处理，以及ZooKeeper或KRaft节点协调Kafka Broker之间通信。
- 实现安全、监控和测试机制，管理底层硬件或虚拟机。
- 部署后持续监控、维护和优化Kafka，往往比上述所有更困难且昂贵。

![](https://cdn.thenewstack.io/media/2023/11/9b58bcf9-image1b.jpg)

*多区域Kafka架构组件复杂*

总之，大规模托管和管理Kafka存在困难。此外，一些误解使Kafka似乎比实际更复杂:

### 作为消息代理它过于复杂

Kafka不仅是消息代理。它还提供流处理、持久性、灵活的消息语义以及比传统代理更好的可扩展性和性能。这些卓越特性增加复杂度，但权衡似乎合理，否则全球为何有如此多公司使用Kafka?一些企业正从更简单的消息代理迁移到更可靠的Kafka，虽然运维难度增加。

### 必须使用Zookeeper，复杂化事情

Kafka传统上依赖[ZooKeeper](https://kafka.apache.org/documentation/#zk)进行元数据管理和Broker之间协调。但是，正在逐步移除ZooKeeper依赖，用[KRaft](https://kafka.apache.org/documentation/#kraft)取代，将元数据管理迁移到Kafka自身。这简化Kafka架构，增强可扩展性。

自Kafka 3.3起，KRaft可用于新Kafka集群生产。[最近Kafka 3.6发布](https://kafka.apache.org/blog#apache_kafka_360_release_announcement)，甚至可以将基于ZooKeeper的集群升级到KRaft。与此同时，ZooKeeper在3.5中废弃，完全移除计划在Kafka 4.0中。

### Kafka仅针对Java开发者

Kafka使用Java(和Scala)编写，团队中至少1名熟悉Java和JVM的开发者大有裨益。但这不意味仅Java开发者可以使用Kafka。相反，其他语言有大量[Kafka客户端库](https://cwiki.apache.org/confluence/display/KAFKA/Clients#)，如Python、C/C++、Go、.NET、Ruby、PHP和Node.js。这些客户端可以在Kafka中生产、消费、处理数据，集成管理Kafka生态组件。

### Kafka仅适用于科技巨头

确实，LinkedIn、Netflix、Uber等大公司利用Kafka大规模管理海量数据(并有专门团队运维)。但对于中小企业寻求构建面向未来、更高效、模块化和可靠的后端架构，Kafka同样非常值得。此外，如果缺少内部运行Kafka所需资源和知识，可以选择外包给众多Kafka供应商之一。

## 当更简单的不够用时

考虑到Kafka的复杂度，您可能倾向使用更简单的事件驱动工具，如RabbitMQ(查看对比了解[两者差异](https://quix.io/blog/apache-kafka-vs-rabbitmq-comparison)和相似处)。但RabbitMQ能否提供与Kafka相同的优势？答案是否定的。

B2B技术服务销售平台AppDirect决定从[RabbitMQ迁移到Kafka](https://www.appdirect.com/blog/7-steps-to-replacing-a-message-broker-in-a-distributed-system)。尽管RabbitMQ起初表现不错，但在AppDirect从单体转向微服务架构、开始摄入大量新数据源时，性能下降。

> AppDirect高级后端工程师Abid Khan表示: “随着数据量激增，RabbitMQ变得不稳定，需要大量调优。这些变更暂时解决了规模问题，但随着新增微服务和数据源，平台延迟持续增加。”

经过7步迁移后，AppDirect感受到使用Kafka而非RabbitMQ的益处。

> Abid Khan表示: “有了Kafka，AppDirect现在能够处理大量事件。新消息代理中的追踪和可观察性系统将保证高可用性。”

[另一个选择Kafka而非RabbitMQ的公司是网络会议软件提供商Livestorm](https://life.livestorm.co/why-we-chose-kafka-at-livestorm-92c350f2a657)。尽管Livestorm开发人员对RabbitMQ更熟悉，它更简单，但由于庞大的社区、高质量的库、更好的可靠性和吞吐量等因素，首选了Kafka。此外，Kafka被视为可能长期服务于Livestorm的技术，而RabbitMQ更像是一个过渡步骤:

> Livestorm首席工程师Laurent Schaffner表示: “许多公司选择RabbitMQ，因为它易设置，开发者可快速掌握。它可用于服务间通信。但随着公司成长，它们通常会从这类解决方案迁移到数据流。”

在RabbitMQ上使用一段时间后再迁移到Kafka将存在问题:

> Laurent Schaffner表示:“[...] 当我们决定切换时，这会非常痛苦，我们将艰难摆脱已有的消息队列。我们将不得不处理遗留技术，这只会增加开发者的复杂度。”

## 简化Kafka的采用

并非每个人都有时间、资源或意愿来处理Kafka的复杂性。但这不意味着他们无法从Kafka的功能中受益。有一些供应商可以简化Kafka部署的设置、维护和使用。

最知名的是[Confluent](https://www.confluent.io/?utm_content=inline-mention)。由Kafka创造者建立，Confluent有两种形式: Confluent Platform和Confluent Cloud。前者是自管理的Kafka发行版，相比原生Apache Kafka，提供了更多功能。包括用于管理消息模式和网络序列化反序列化的数据的Schema Registry，用于将Kafka与各种数据源和接收端集成的预构建连接器，用于流处理的SQL接口ksqlDB，以及自平衡集群。

而Confluent Cloud是Confluent Platform的完全托管的云原生版本，抽象了大部分运维和基础设施管理的开销。

其他Kafka供应商包括Amazon MSK、Aiven、Instaclustr、Cloudera、IBM Event Streams、Microsoft Azure Event Hubs和Quix。每个都有不同的优势。例如，Cloudera专注大数据分析，而Quix使用Python擅长无服务流处理和数据流水线。

还值得一提的是Redpanda，这是一家与Kafka API和协议兼容的供应商。可以将Redpanda平台视为Kafka的C++克隆。有关更多见解，可以[参见Kafka与Redpanda的比较](https://quix.io/blog/redpanda-vs-kafka-comparison)。

总体来说，有许多Kafka提供商可供评估和测试。选择时需要考虑的因素包括定价、集成、功能、安全合规性、管理工具、数据中心数量和位置以及供应商锁定。

## 结论

Kafka内部管理的初期学习曲线和运维挑战非常陡峭。但是，当您需要可靠大规模处理数据流时，RabbitMQ等更简单的替代方案往往不够用。Kafka提供了一系列优势: 可扩展性、高性能、容错性、高可用性、数据完整性保证和丰富模块化的生态系统。这些功能经过多年广泛实战检验，被成千上万的公司使用，从中小企业到大型科技巨头。使用Kafka不必痛苦。我们看到，有许多供应商可以让您获得Kafka的回报，同时减少或消除其相关的部分或全部复杂性。

请查看Quix，并让我知道您的想法。[Quix是一个Confluent合作伙伴](https://quix.io/blog/quix-and-confluent-partnership)，提供完全托管平台，通过开源Python客户端库[Quix Streams](https://github.com/quixio/quix-streams)来简化基于Kafka的事件流应用开发。为了帮助您从流数据中获取价值，我们提供了无需账户即可[交互体验Quix平台的模板](https://quix.io/templates)。


