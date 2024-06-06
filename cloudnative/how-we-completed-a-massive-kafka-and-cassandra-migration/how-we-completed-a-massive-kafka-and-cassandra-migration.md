
<!--
title: 如何完成Kafka和Cassandra的大规模迁移
cover: ./cover.jpg
-->

了解策略和流程，以及一些最佳实践，让任何大规模、关键任务的 Cassandra 和 Kafka 迁移更加顺利。

> 译自 [How We Completed a Massive Kafka and Cassandra Migration](https://thenewstack.io/how-we-completed-a-massive-kafka-and-cassandra-migration/)，作者 Ben Slater。

无论迁移规模如何，任何数据层迁移都需要进行仔细的规划和执行。话虽如此，我们最近完成的可能是迄今为止执行过的最大规模的 [Apache Cassandra](https://cassandra.apache.org/_/index.html) 和 [Apache Kafka](https://kafka.apache.org/) 迁移（吉尼斯世界纪录尚未对此进行统计……）。

在我看来，这是一个特别有趣的用例，它可以在没有停机时间的情况下实现相当复杂的技术壮举（并且仅使用 Cassandra 和 Kafka 的完全开源版本——这里没有开放核心）。下面，我将分享所使用的策略和流程，以及一些最佳实践，这些实践将有助于使任何大规模、关键任务的 Cassandra 和 Kafka 迁移更加顺利。

## 管理大规模迁移

让我们了解一下这次迁移的规模。这家企业的开源 [Cassandra 部署](https://thenewstack.io/cassandra-5-0-what-do-the-developers-who-built-it-think/) 包括 58 个集群和 1,079 个节点，其中包括 17 种不同的节点大小，分布在 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 和 [Kafka 前端](https://thenewstack.io/apache-kafka-primer/) 上，该公司使用了 154 个集群和 1,050 个节点，共有 21 种节点大小，同样分布在这两个云提供商和六个区域中。正如你所想象的，进行迁移需要大量的时间和精力。时间表要求准备九个月，然后是八个月的谨慎生产迁移。

与任何迁移一样，强大的项目管理和治理至关重要。如果这一步出了问题，你以后会遇到麻烦。我们根据项目管理方法为一些关键角色分配了具体职责，包括一名总体项目经理、一名 Cassandra 迁移项目经理和一名 Kafka 迁移项目经理、每项的技术负责人以及一名关键产品经理。这个 [团队迅速建立了密切的协作](https://thenewstack.io/managing-software-development-team-dynamics-from-within/) 和与企业的清晰沟通，这是获得积极项目成果的另一种行之有效的方法。

在项目的初始阶段，这种密切联系证明了它的价值，因为我们与企业的架构、安全和合规团队同步工作，以满足他们在这些领域的严格要求。这意味着确保迁移的目标环境具有入侵检测、访问日志记录、审计日志、强化操作系统以及帐户级选择加入，以自动配置具有日志传输和其他控制的新集群。我们还启用了自定义 Kafka Connect 连接器的加载过程，以使用实例角色而不是访问密钥进行 Amazon S3 访问，并改进了用于配置单点登录 (SSO) 访问的 SCIM（跨域身份管理系统）API。

在此准备阶段，我们还认识到并采取了优化迁移集群的架构契合度的机会。由于企业的架构在 Kafka 集群级别之上提供了高可用性，因此我们使用 RF2（复制因子 2）来支持在两个可用性区域中运行的 Kafka 集群。我们还准备通过利用最新的 AWS 和 GCP 节点类型来优化成本。

## Kafka 迁移

“流出”方法是 Kafka 迁移的第一个想法：只需将 Kafka 消费者指向源集群和目标集群，将生产者切换为仅向目标集群发送消息，等到从源读取所有消息，然后瞧。限制在于流出不会保留消息顺序，这是许多 Kafka 用例（包括此用例）必不可少的。

[MirrorMaker2](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/hdinsight/kafka/kafka-mirrormaker-2-0-guide.md) 为 Kafka 迁移提供了另一个强大的选择，但是其高度的消费者/生产者应用程序依赖性意味着它不适合这里。

“共享集群”方法——将源集群和目标集群作为单个集群运行——成为剩下的最佳选择。我们继续为每个集群创建详细的变更计划，始终牢记回滚启用。高级步骤从配置目标集群开始，更新配置以匹配源，并将网络环境与源集群加入虚拟私有云对等互连。然后，我们在目标中以观察者模式启动 [Apache ZooKeeper](https://zookeeper.apache.org/)，以及目标 Kafka 代理。

接下来，我们使用 Kafka 分区重新分配来移动数据。其中包括增加复制因子和跨目标和源代理的复制，将首选领导交换为目标代理，然后减少复制因子以移除源代理副本。通过将目标代理重新配置为其初始联系点，然后移除旧代理，从而完成流程。

源环境额外带来了一些皱褶，我们在迁移期间已将其熨平。例如，它跨多个集群共享一个 ZooKeeper 实例，导致我们仔细重新配置和清理每个目标 ZooKeeper 中其他集群的数据。我们还扩展了目标配置以支持企业的特定端口侦听器映射，避免了主要的重新配置工作。

## Cassandra 迁移

零停机 Cassandra 迁移最常见的方法是向现有集群添加数据中心。我们还使用并推荐我们的 Instaclustr Minotaur 一致重建工具（[在 GitHub 上提供](https://github.com/instaclustr/instaclustr-minotaur)）。此开源解决方案解决了源集群中缺少数据副本可能导致重建过程从同一节点复制多个副本的问题，从而导致目标副本减少。Minotaur 确保目标集群至少具有与源集群一样多的副本，并且可以将任何需要的修复推迟到迁移之后。

当我们遇到具有高度不一致性的集群时，对这次迁移使用此方法特别有价值。在一个案例中，集群在迁移后需要两个半月的修复。另一组集群由于在流式传输期间架构更改时 Cassandra 丢弃临时数据，因此每两到三个小时定期丢弃表。我们首先尝试在节点重建期间手动暂停表丢弃，但发现该方法不可持续。最后，我们使用我们的供应 API 检测节点状态并在必要时自动暂停表丢弃。

## 重大挑战，巨大成功

最终，（也许）有史以来最大规模的 Cassandra 和 Kafka 迁移按计划完成，且几乎没有出现问题。我将这一积极成果归功于所有参与者密切合作、周密规划和采用的战略最佳实践，并建议任何参与类似的大型复杂迁移的人员应用这些相同技术。
