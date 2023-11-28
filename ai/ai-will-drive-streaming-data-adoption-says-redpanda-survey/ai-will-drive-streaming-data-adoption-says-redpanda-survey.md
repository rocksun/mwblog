<!--
title:AI推动流数据使用仍需时日
cover: https://cdn.thenewstack.io/media/2023/11/b07231a5-streaming-data-1-1024x576.jpg
-->

一份新报告显示，尽管72%的受访者认为AI将在1-2年内推动流数据的应用，但实时分析仍是最主要的使用场景。

> 译自 [AI Will Drive Streaming Data Use — But Not Yet, Report Says](https://thenewstack.io/ai-will-drive-streaming-data-adoption-says-redpanda-survey/)，作者 Lawrence E Hecht 已经为企业IT B2B市场和技术政策问题生成了可操作的见解和报告，历时近25年。他定期与客户合作，开发和分析有关开源生态系统的研究。除了他的咨询工作之外，...

根据[一份新报告](https://go.redpanda.com/state-of-streaming-data-report-2023-24)指出，72%的流数据专家认为，在未来1到2年内，[人工智能和机器学习(AI/ML)](https://thenewstack.io/ai/)将推动流数据的采用。

然而，AI/ML既不是当前[流数据](https://thenewstack.io/what-is-data-streaming/)用户的首要用例，也不是他们采用该技术的主要动机。[实时分析](https://thenewstack.io/real-time-databases-who-is-using-them-and-why/)迄今为止是最常见的用例，提高生产力是使用该技术的最大动机。

[Redpanda](https://redpanda.com/?utm_content=inline-mention)流数据平台进行的一项调查的受访者中，大多数担任IT角色的300名美国受访者于7月和8月完成了调查。

总的来说，59%的调查参与者表示他们当前正在使用流数据；其余41%的人预计会在未来的某个时间采用该技术。由于受访者的自我选择，市场上的总体采用水平可能更低。

即使在当前用户中，只有不到一半(46%)的人已经完成了他们的流数据解决方案的实施。许多实施不完整，因为流数据没有用于许多正在使用的应用程序中。

[Confluent](https://www.confluent.io/?utm_content=inline-mention)的另一份报告发现，[47%的流数据组织至少有10个关键系统依赖于该技术](https://www.confluent.io/blog/2023-data-streaming-report/)。这个群体可能还没有完成向流数据的数据迁移，但他们的实施相对成熟。

![](https://cdn.thenewstack.io/media/2023/11/83191c22-confluentstreamingcriticalsystems.png)

*流数据部署状态。来源：“2023 流数据报告的主要见解”，Confluent。该报告基于Freeform Dynamics对2，250名IT和工程领导者的调查，他们的组织正在使用流数据。受访者来自澳大利亚、德国、法国、印度、新加坡、英国和美国。*

## 数据量将推动基础架构变化

随着使用流数据的系统数量的增加，数据量肯定也会增加。根据Redpanda的研究，82%的具有流数据的组织每天至少生成10GB的分析工作负载的数据量，几乎有同样多的组织(76%)处理相同数据量的交易流数据工作负载。

为了了解未来不久的数据基础架构需要适应的量，第一步是确定将依赖于流数据的系统数量。接下来，估计每个应用程序的数据使用量的增加程度。

尽管AI/ML可能需要[大量数据来创建模型](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/)，但它通常不需要“快速数据”。访问数据的速度并不总是一个关键指标，因为只有少数AI/ML用例实际上需要[实时的流数据](https://thenewstack.io/stream-processing-101-whats-right-for-you/)。其余的可以使用更传统的批处理技术。

## 使用流数据的主要原因

虽然AI/ML得到了很多关注，但它不是最常见的用例。Redpanda调查中，71%的流数据使用者使用实时分析，64%使用流数据支持电子商务交易。[物联网(IoT)](https://thenewstack.io/edge-computing/)、欺诈检测和个性化也得到了普遍支持。

仍然令人印象深刻的是，47%的调查参与者的情况是AI/ML使用流数据。为了理解背景，早在2019年The New Stack与[Lightbend](https://www.lightbend.com/)进行的一项[研究](https://thenewstack.io/vendors-compete-for-users-of-stream-processing-technologies/)中，研究人员发现33%的流数据用户将该技术用于AI/ML。

60%的Redpanda受访者将提高生产力作为使用流数据技术的原因。49%的业务敏捷性是第二大动机。43%也将支持AI/ML作为动机。

在业务目标方面，64%的用户认为流数据正在造福[网络安全](https://thenewstack.io/security/)，同样比例的人也在广泛寻找他们的流数据中的异常。

![](https://cdn.thenewstack.io/media/2023/11/85d9611a-streaming-data-use-cases.png)

*来源:“流数据状态”，Redpanda。*

![](https://cdn.thenewstack.io/media/2023/11/03a2c892-streaming-data-business-goals.png)

*来源:“流数据状态”，Redpanda。*

## 流选项很复杂

当被问及使用流数据的感知技术挑战时，Redpanda调查的参与者中有42%列出了安全和数据隐私。其他关键发现:

- 数据一致性(35%)和复杂性(29%)被列为使用流数据的其他主要挑战。
- 尚未开始使用流数据的人几乎比当前用户(40%对21%)更有可能担心复杂性。

在业务挑战方面，成本/价格被最常提及。获得必要的内部技能也有问题，因为[数据工程师需求量很大](https://thenewstack.io/why-data-jobs-are-hot-and-how-to-get-one/)。

## 流数据分析：工具

根据Redpanda的调查，当前用户中有66%使用流数据分析工具，4%部署流数据库(如[Materialize](https://thenewstack.io/materialize-managed-real-time-data/))，51%使用操作数据库(如[Apache Cassandra](https://thenewstack.io/vector-search-is-coming-to-apache-cassandra/))，41%使用数据湖或数据仓库。

只有三分之一(34%)实际上正在使用状态流处理框架。谷歌的流数据是调查中最大数量受访者使用的框架，其次是[Apache Flink](https://thenewstack.io/3-reasons-why-you-need-apache-flink-for-stream-processing/)和NiFi。虽然它们在列表中较低，但新兴供应商[DeltaStream](https://www.deltastream.io/)和[Quix](https://www.quix.io/?utm_content=inline-mention)的使用比其几个竞争对手更频繁。

这些选项之间的区分令人困惑，因为许多数据平台将这些功能捆绑在一起。例如，尽管Redpanda调查中77%的当前用户表示他们有兼容Kafka的平台，但只有7%的用户明确使用Kafka流。

[Aiven](https://aiven.io/platform?utm_content=inline-mention)和Redpanda等数据平台与一系列流处理框架和数据库兼容。它们没有让用户决定特定技术，而是根据可以集成的数据源和类型数量进行竞争。

![](https://cdn.thenewstack.io/media/2023/11/a2a14986-pipelinecomponents.png)

*来源:“流数据状态”，Redpanda。*
