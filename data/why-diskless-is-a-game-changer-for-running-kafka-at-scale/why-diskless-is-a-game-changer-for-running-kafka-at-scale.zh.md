[Apache Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/)是最常用的流处理应用程序之一。其高性能、低延迟以及[开源许可](https://thenewstack.io/open-source/)只是[80%的财富100强](https://kafka.apache.org/powered-by)企业使用Kafka来驱动事件驱动型应用程序并交付弹性数据管道的部分原因。

但是，当你开始处理海量高速数据时，你会很快遇到成本、运营和复杂性问题。对于云原生企业而言，在多个云可用区中运行Kafka时，高昂的复制成本是一个非常严重的问题。

最近，Kafka社区提出了[三项Kafka改进提案](https://cwiki.apache.org/confluence/display/KAFKA/The+Path+Forward+for+Saving+Cross-AZ+Replication+Costs+KIPs)，专门用于解决此问题。其中一项是，[KP-1150 无盘主题](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1150%3A+Diskless+Topics)，“提出了一种Apache Kafka中的新型主题，它将复制委托给对象存储，”Aiven（KP-1150的开发者）流服务负责人Filip Yonov[在一篇博文中写道](https://aiven.io/blog/diskless-apache-kafka-kip-1150)。

“无盘并非完全取消磁盘，而是将它们抽象化——利用对象存储（如S3）来降低成本并提高灵活性，”Yonov表示。

## 如何改进您的Kafka架构

如果大规模运行Kafka让您头疼，请于太平洋时间11月20日上午8点 | 东部时间上午11点加入我们的特别在线活动：**[大规模Kafka：实现实时业务影响的更智能架构](https://thenewstack.io/webinar/kafka-at-scale-smarter-architectures-for-real-time-business-impact/)**。

在此次免费网络研讨会期间，Aiven的开源软件工程师（也是KP-1150的主要作者）Greg Harris，Aiven的流处理架构师David Esposito，以及TNS主持人Chris Pirillo，将探讨领先公司如何调整其Kafka架构，以管理更大、更快的数据流并立即产生真正的业务影响。

除了讨论在云中扩展Kafka时应避免的陷阱外，他们还将独家预览Apache Kafka的无盘主题（Diskless Topics），这项突破性技术通过消除本地磁盘使Kafka精简高达80%，显著降低了总拥有成本（TCO），同时简化了操作并开辟了在云中扩展的新途径。

## 立即注册参加本次免费网络研讨会！

如果您无法现场参加，[仍然可以注册](https://thenewstack.io/webinar/kafka-at-scale-smarter-architectures-for-real-time-business-impact/)，我们会在网络研讨会结束后向您发送录音。

## 您将学到什么

通过参加本次特别在线活动，您将获得最佳实践、真实案例和可操作的技巧，包括：

*   Kafka在推动数字原生企业的增长、敏捷性和客户体验方面的作用。
*   在云中运行Kafka时的常见挑战，包括成本、重新平衡和跨可用区复制。
*   如何衡量实时流媒体带来的业务影响。
*   无盘主题（KIP-1150）介绍及其对Kafka未来的意义。
*   实际用例：在单个集群中混合使用无盘主题和经典主题。