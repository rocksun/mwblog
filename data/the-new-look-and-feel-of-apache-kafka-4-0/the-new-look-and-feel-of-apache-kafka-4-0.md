<!--
title: Apache Kafka 4.0的全新外观和体验
cover: https://cdn.thenewstack.io/media/2025/03/ce8cc676-kafka.png
summary: 重磅！Apache Kafka 4.0发布，默认运行KRaft，告别ZooKeeper！新增Kafka Queues (KIP-932)，突破consumer扩展限制。KIP-848加速consumer group rebalancing，提升自动缩放能力。KIP-1112实现代码注入，KIP-1076/1091增强可观测性，集成OpenTelemetry等工具，云原生时代更进一步！
-->

重磅！Apache Kafka 4.0发布，默认运行KRaft，告别ZooKeeper！新增Kafka Queues (KIP-932)，突破consumer扩展限制。KIP-848加速consumer group rebalancing，提升自动缩放能力。KIP-1112实现代码注入，KIP-1076/1091增强可观测性，集成OpenTelemetry等工具，云原生时代更进一步！

> 译自：[The New Look and Feel of Apache Kafka 4.0](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/)
> 
> 作者：Jelani Harper

最近推出的 Apache Kafka 4.0 在开源分布式事件流平台的几乎每个方面都进行了一些升级。最近的版本有许多 Kafka 改进提案 (KIP)——它们提供了来自开源社区的新功能——涵盖 Kafka Streams、Kafka Connect 以及 Kafka brokers、consumers、producers 等。

然而，该版本最重要的部分可能不涉及任何 KIP。[Kafka 4.0](https://kafka.apache.org/blog) 是第一个默认运行 [Apache Kafka Raft](https://thenewstack.io/kafka-drops-zookeeper-for-real-time-kraft/) (KRaft) 的版本，它是 Kafka 中 [Raft 协议](https://thenewstack.io/raft-native-the-foundation-for-streaming-datas-best-future/) 的实现。因此，该平台现在完全摆脱了 Apache ZooKeeper，这是一种集中式服务，用于维护分布式应用程序的配置、同步、命名约定等信息。

根据 [Sandon Jacobs](https://www.linkedin.com/in/sandonjacobs)，[Confluent](https://www.confluent.io/?utm_content=inline+mention) 的高级开发者倡导者，淘汰 ZooKeeper 绝非突然。“迁移计划已经存在一段时间了，”Jacobs 评论道。“社区并没有隐瞒 ZooKeeper 即将消亡的事实。因此，在过去的几个版本中，这项工作一直在进行中。”

4.0 版本还包含 Kafka 队列的早期访问版本 ([KIP-932](https://www.morling.dev/blog/kip-932-queues-for-kafka/))，它允许用户将 Kafka consumers 扩展到超过给定主题的分区数量。其他值得注意的功能包括大幅改进了在不停机的情况下重新平衡 consumer groups 的能力，以及加速将逻辑输入到 Kafka Streams 应用程序中的机制。

## KRaft 取代 ZooKeeper

Kafka 用 KRaft 替换 [ZooKeeper](https://zookeeper.apache.org/) 有很多原因。有些与成本效益有关；另一些与正常运行时间和应用程序稳定性有关。“你现在不必担心运行另一个 ZooKeeper 集群了，”Jacobs 解释说。“少一个移动部件总是更好。少一个故障点。”作为 Kafka 部署的元数据协调层，ZooKeeper 在使用 Kafka 时负责几个重要的考虑因素。这些担忧大多涉及操作，并且由于 ZooKeeper 是 Apache 基金会提供的开源资源，但它位于 Kafka 部署之外，因此这些担忧更加严重。

因此，它增加了流数据拓扑的复杂性。“现在，你不需要你的operators说我需要创建一个 ZooKeeper 集群；我需要创建一个 Kafka 集群，”Jacobs 说。“我需要管理 ZooKeeper 和 Kafka 之间的 TLS 之类的事情。我不再管理 ZooKeeper 的计算了。”ZooKeeper 被广泛用作管理复制主题信息和分区的元数据的一种手段，以确定哪些分区可以根据副本的同步情况充当领导者等因素。“在某些时候，所有这些都迁移到了 KRaft 中，”Jacobs 说。

## Kafka 队列

[Kafka 队列](https://cwiki.apache.org/confluence/display/KAFKA/KIP-932%3A+Queues+for+Kafka) 克服了 consuming 应用程序遇到的一些限制，因为 Kafka 是一个基于主题的系统，而不是基于队列的系统。有关主题的信息被分区以进行并行处理并相应地复制。根据 Jacobs 的说法，“你的分区确实决定了，或者是由你的消费模型决定的。”
在 4.0 版本之前，在 Kafka 中将 consumer group 的成员数量扩展到超过主题的分区数量在很大程度上是不切实际的。在传统的基于队列的消息传递系统（如 Amazon Simple Queue Service (SQS)）中，consumer 应用程序可以创建任意数量的线程“用于消费，这些线程将只获取队列中下一个可用的事件”，Jacobs 说。但在 Kafka 4.0 之前，用户实际上仅限于将 consumer groups 的成员扩展到主题的分区数量，因为如果他们尝试做更多的事情，“你最终会得到 consumer group 的空闲成员”，Jacobs 说。“他们不会得到分区分配；他们不会消费任何数据。”
Queues for Kafka 通过支持类似于基于队列的消息传递系统的方式来纠正这种情况。Jacobs 补充说，它有效地通过先进先出 (First In, First Out) 的范例“尽其所能”地从每个分区进行消费。因此，消费者可以扩展到特定主题的分区数量之外。然而，Kafka 主题中的分区语义几乎可以保证按照事件写入的顺序从分区进行消费。如今，Queues for Kafka 中无法保证这种连续的消费顺序。Jacobs 评论说：“在处理顺序很重要的情况下，您仍然希望坚持使用传统的消费者组。”“如果您想进行横向扩展并完成工作，并且顺序不太重要，那么 Queues for Kafka 就是您应该考虑的。”

## Consumer Group Rebalancing

[KIP-848](https://cwiki.apache.org/confluence/display/KAFKA/KIP-848%3A+The+Next+Generation+of+the+Consumer+Rebalance+Protocol) 加速并简化了消费者组的重新平衡。从历史上看，例如，在流量高峰期间，当新分区被分配以添加机器时，Kafka 会出现一些停机时间。在此过程中，一些消费应用程序停止运行的情况并不少见。KIP-848 改善了这种情况，因此理想情况下，当重新平衡消费者的分区时，消费不会停止。

Jacobs 说：“这是一个性能问题。”“您不必因为组中出现了一个新成员就必须停止所有人。”这些功能可以通过 Kubernetes 等框架增强自动缩放部署。当向上扩展以满足预定义阈值的需求时，系统会自动“添加您想要加速消费的 pod，而其他 pod 则像往常一样继续运行”，Jacobs 说。

## Code Injections and Observability

[KIP-1112](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1112%3A+allow+custom+processor+wrapping) 将代码插入到 Kafka Streams 中的 Processor API 和 DSL 处理器中，并具有自定义的进程包装功能。它消除了手动剪切和粘贴代码（对于开发人员来说可能很耗时）到处理器中的操作，否则需要统一地向它们添加例如审计逻辑。

Jacobs 说，与传统的手动方法不同，“现在您可以实际定义一个处理器包装器类，并且您可以将其添加到您的 Streams 配置和拓扑配置中，以便它将应用于您的拓扑中的所有处理器。”

[KIP-1076](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1076%3A++Metrics+for+client+applications+KIP-714+extension) 和 [KIP-1091](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1091%3A+Improved+Kafka+Streams+operator+metrics) 通过在系统的 brokers 上提供统一的客户端指标和新的详细状态指标来提高 Kafka 的可观测性能力。它们提高了消息传递服务的能力，可以将“客户端指标报告回 Kafka，以便您可以设置您选择的 OpenTelemetry 收集器，并利用您已经投资的工具（如 Datadog）来获取有关您的生产者和消费者、您的管理客户端的指标到该平台中”，Jacobs 说。

## Better With Time

Kafka 4.0 中提供新功能的许多 KIP 通常都可用。它们中的大多数旨在减少开发人员所需的时间和精力，以最大限度地利用作为当代流数据应用程序基础的最普遍的平台之一的价值。为此，可以对 4.0 版本中的任何 KIP 进行改进——就像他们改进平台本身一样。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。