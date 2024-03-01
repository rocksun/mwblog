<!--
title: 规划Prometheus成功之路
cover: https://cdn.thenewstack.io/media/2024/02/fabf2a2f-prometheus-1024x576.jpg
-->

一文详解在使用 Prometheus 时可能轻松破坏顺畅运行的挑战，以及如何克服这些挑战。

> 译自 [Creating a Path for Prometheus Success](https://thenewstack.io/creating-a-path-for-prometheus-success/)，作者 Arthur Sens 是Coralogix的平台工程师，同时拥有站点可靠性工程和软件工程背景。他积极为Prometheus生态系统做贡献，维护Prometheus-Operator和Prometheus client_golang，同时指导新的开源软件贡献者。

Prometheus是一个易于使用的开源监控和警报工具包。它的流行无疑归功于其高效的时间序列数据收集数据库、灵活的查询语言(PromQL)和一般的可扩展性。此外，它对动态服务发现的支持、与Kubernetes的本地集成以及警报功能，使其成为监控动态的云原生环境的不二之选。[Prometheus](https://thenewstack.io/30-pull-requests-later-prometheus-memory-use-is-cut-in-half/)还拥有一个活跃的[开源社区](https://thenewstack.io/the-unique-steps-needed-to-grow-your-open-source-community/)，不断贡献持续改进和日益增长的采用。

然而，尽管Prometheus提供了这么多好处，但许多挑战也很容易破坏平稳的运行。让我们来看看其中一些。

## 基数经验不足的故事

对Prometheus缺乏经验的人经常遇到高基数问题是很常见的。这些问题可能导致Prometheus实例的增长远远超过预期，从而造成可扩展性和性能问题。

在Prometheus中，基数指指标中独一无二系列的数量。当生成大量不同的指标标签或标签值时，就会发生高基数情况。  

这通常源于对标签的误用或误解。例如，向指标添加高度动态的标签(如时间戳、唯一标识符或用户ID)会迅速增加存储的时间序列数量。

这可能会导致一系列不幸事件:

**存储需求增加**

高基数导致Prometheus需要存储的时间序列数量急剧增加，这可以快速消耗存储资源。当然，这可能会变得昂贵。

**性能降低**

在高基数场景中，查询性能可能会显着降低。Prometheus必须处理大量的时间序列，这可能会减慢查询响应并增加CPU和内存使用量。 

**管理开销**

[管理和维护高基数的Prometheus](https://thenewstack.io/grafana-nixes-cortex-support-for-amazon-managed-prometheus/)实例变得更具挑战性。它需要更仔细的调优，可能还需要更复杂的基础架构解决方案。

## 确保您的存储管理不会出现A-WAL问题

Prometheus中的Write Ahead Log或WAL是一种用于确保数据完整性和防止崩溃或意外关闭时数据丢失的机制。每当Prometheus记录新数据时，它会先将该数据写入服务器文件系统上的WAL，然后再写入数据库。

这种方法意味着如果Prometheus由于任何原因重新启动，它可以使用WAL来恢复任何尚未写入数据库的数据。WAL充当数据库中应该存在的数据的记录，确保如果系统崩溃，不会丢失数据。

然而，WAL的主要挑战之一是重新播放它所需的时间，特别是在崩溃或重新启动后。当Prometheus重启时，它需要处理WAL来重建其内存状态。如果WAL中有大量数据，这个过程可能会很耗时。

在实际情况下，这意味着如果WAL重播过程花费很长时间，Prometheus可能会经历显着的宕机时间，监控和警报暂时不可用——这对依赖实时监控的系统来说肯定不是理想状态。

## 毫不费力地扩展?开玩笑吧!

在Prometheus中处理可扩展性，特别是在大规模和动态环境中，通常需要采用额外的策略和工具。虽然Prometheus是一个单体应用程序，但它确实有许多独立的功能，如抓取和存储指标，通过查询返回指标，警报和记录评估等等。

如果在特定设置中你严重依赖Prometheus的单一功能，你可能会被迫扩展整个Prometheus，尽管你真正需要扩展的只是它的一部分。这就是分布式设置和像Thanos和Cortex这样的工具发挥作用的地方。

它们都通过添加全局查询视图，本机支持Prometheus查询API，提供高效的存储和多集群支持来扩展Prometheus。它们还允许在对象存储(如[AWS](https://aws.amazon.com/?utm_content=inline-mention) S3或Google Cloud Storage)中长期存储Prometheus指标，使其更具成本效益和可扩展性。然而，尽管Thanos和Cortex组件可以分别扩展，从而解决Prometheus的单体扩展问题，但它们的所有附加组件都需要一定级别的专业知识和努力来维护。

简而言之，虽然极有帮助，但Thanos和Cortex都向监控体系结构中引入了额外的组件，这在部署、管理和故障排除方面增加了复杂性。

## 创建成功的框架

如果您想在不遇到这些存储和可扩展性问题的情况下使用Prometheus，请参加我们在CNCF主办的与会期间在欧洲举行的有关使用[Prometheus-Operator](https://github.com/prometheus-operator/prometheus-operator)的[演示](https://colocatedeventseu2024.sched.com/event/1YFi8/architecting-growth-scaling-tactics-for-prometheus-metrics-collection-arthur-silva-sens-nicolas-takashi-coralogix)，以及几天后的KubeCon上的[实践研讨会](https://kccnceu2024.sched.com/event/1YkTo)。

您将了解如何获得Prometheus的所有回报而毫无风险。您还可以见到我和我的同事Nicolas Takashi——我们是Coralogix的平台工程师，以及我们杰出的共同主讲人Bartłomiej Płotka和Mahmoud Amin，谷歌的高级软件工程师，还有Grafana的Jesus Vazquez。
