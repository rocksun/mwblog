
<!--
title: Kafka的大规模GitOps
cover: https://cdn.thenewstack.io/media/2024/05/bf7c9f79-01.-cover@2x.png
-->

拥抱 IaC，以可扩展且自动化的方式配置 Kafka 资源、编排部署和管理客户端配置。

> 译自 [GitOps for Kafka at Scale](https://thenewstack.io/gitops-for-kafka-at-scale/)，作者 James White。

管理像 [Kafka](https://thenewstack.io/top-10-tools-for-kafka-engineers/) 这种分布式系统中的复杂基础设施所需的不只是人工干预，还需要可扩展且自动化的方法。

根据 Confluent 的 [2023 年数据流报告](https://assets.confluent.io/m/52436fc9cd4844f4/original/20230510-RPT-Data_Streaming_Report.pdf?utm_medium=report&utm_campaign=tm.campaigns_cd.brand-2023q2-brandhub&session_ref=https://www.google.com/)，74% 的 IT 主管认为集成方法和标准的使用不一致是阻碍数据流推进的障碍和挑战。

随着部署规模和复杂性的不断增加，平台团队跟踪配置、更新和依赖关系变得一项艰巨的任务。同时，确定所有权、发现现有资源和跨团队[数据](https://thenewstack.io/data/)共享也成为开发团队面临的挑战。

GitOps 和基础设施即代码 (IaC) 是 DevOps 和云原生领域的基础性实践。可以在 [Kafka 中运用这些实践](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/)，以实现一致性、标准化和业务敏捷性。

在 Kafka 的上下文中，GitOps 涉及：

- 部署自动化
- Kafka 资源配置
- 访问权限配置
- Kafka 客户端配置

自动化这些流程使开发人员能够快速实施更改，引入治理最佳实践，并减轻负责 Kafka 运营的平台团队的负担。

## 手动配置管理无法扩展 

最初，具有有限数量的专注范围的 Kafka 项目可以使 ops 和平台团队处理请求保持可管理。这些团队通常通过 Jira 工单和手动资源配置来处理 Kafka 资源请求（例如，主题创建、配置、分区修改、模式注册）和访问请求。

然而，随着收养的增加，请求的激增，kafka基础设施的复杂性在增加，团队通常不得不增加人手来支持它。这种方法很快变得繁琐且效率低下。临时更改也增加了人为错误、不一致和错误配置的风险。例如，访问控制列表 (ACL) 条目中的一个简单的拼写错误很容易导致故障或未经授权的消费者。

手工流程缺乏版本控制、可追溯性和透明性。

## IaC是Apache Kafka的基础

如果没有 GitOps，IaC 对于 Apache Kafka 来说是基础性的，您面临着主题名称混乱、分区数量疯狂以及没有统一策略来管理代理、生产者/消费者和安全配置的风险。

要想将采用规模扩展到大量团队、资源和项目，自动化是必不可少的。否则，您期望如何管理超过 100 个传输层安全性 (TLS) 证书、3500 个 Avro 模式、1000 个主题和 5000 个 ACL？清单还在继续！

## 适用于配置管理的 GitOps 

主题、题目、连接配置和安全配置可以很多且变化多端。如果不进行适当管理，大量的配置可能会导致性能下降和可靠性问题。

GitOps 允许将 Kafka 配置存储在存储库中，作为 YAML 或 JSON 文件。以下示例演示了如何使用 [Conduktor](https://conduktor.io/) 资源进行 GitOps。cd



任何资源配置策略的变体都可以存储为 IaC，从而允许将其编排为 CI/CD 工作流中的检查。这可以在不影响与 Kafka 的众多配置相关的风险的情况下实现 Kafka 资源的自动化配置。

从设计上讲，它引入了一个总体治理层。该过程最大程度地减少了部署错误，减少了人工干预，并引入了一个安全框架，以便大规模使用 Kafka。

利用 IaC 使平台团队能够将管理其 Kafka 配置的责任推给域所有者。这有助于消除对平台团队的一些依赖性，而平台团队很少拥有特定 Kafka 配置背后的相关业务背景。

“你真的需要那么多的 [分区](https://www.conduktor.io/kafka/kafka-topics-choosing-the-replication-factor-and-partitions-count/)？”听起来耳熟吗？通过赋能域所有者，平台团队可以专注于提供支持 IaC 实施的工具、框架和工作流。

这种责任的转变促进了问责制和所有权文化，这对扩展至关重要。问问你自己：你等了多久才创建了你的最后一个主题？如果答案超过几个小时，你很可能遇到了瓶颈。

利用 IaC 方法确实会引发有关公司应如何运营的问题。你应该实施哪种方法？

**集中式方法**：一个存储整个公司 Kafka 配置的存储库。**分散式方法**：每个团队或域的多个存储库。

正确的选择取决于公司的结构以及敏捷性和治理要求之间的权衡。

| 集中式 | 分散式 |
|---|---|
| 优点 | |
| 缺点 | |

也许最好的解决方案是考虑一种混合方法，即由团队管理不太重要的配置，而由中心管理最重要的配置以实现一致性和合规性。

## 将资源策略和 CI/CD 相结合就能解决所有问题，对吗？错了！

在 Kafka 生态系统中，你必须超越资源配置才能了解其他挑战和复杂性所在。流应用程序直接连接到 Kafka，并且它们的的行为和配置通常不受 GitOps 原则支配。

你知道 Kafka 中有 [超过 100 个客户端配置设置](https://www.conduktor.io/kafka/kafka-options-explorer/) 吗？如果没有 Kafka 专业知识，许多人倾向于使用其 Kafka 客户端的默认设置。这应该没问题，对吗？也许一开始没问题，但随着扩展，你需要考虑这些默认设置对你的网络、磁盘、服务质量和成本的影响。

如果你不熟悉以下 Kafka 客户端配置，请查阅 [Kafka 选项浏览器](https://www.conduktor.io/kafka/kafka-options-explorer/) 以获取完整列表。

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| acks=all | batch.size=16384 | linger.ms=0 | fetch.min.bytes=1024 | compression.type=lz4 |

虽然上面的一些内容显示了默认设置（例如 batch.size 和 linger.ms），但使用压缩类型不是默认的 Kafka 客户端设置。但是，它可以用来提高性能，减少网络负载并节省存储成本。同样，使用 acks 值 all 不是默认值，但在需要最大可靠性和持久性的情况下建议使用。

## Kafka 客户端配置是一个雷区

最终，Kafka 客户端配置是一个雷区，要求开发人员了解每个设置的复杂性和后果是一个很大的要求。但是，一个配置不当的影响可能会对你的整个 Kafka 平台和底层应用程序产生严重影响。

通过一些自动化，可以避免客户端配置错误。

这是一项关于客户端配置的策略，用于强制使用：

- 一个压缩格式来节省存储并减少网络带宽。
- acks（确认）等于 -1，以获得最高级别的持久性和可靠性。
- 用于消息路由和过滤的记录头。

此类策略使团队能够自主运行，但可以在全局级别对 Kafka 生产者/消费者设置保持总体控制。

## 使用代理在客户端配置中强制执行最佳实践

如前所述，应用程序直接连接到 Kafka，并且它们的配置通常不受 GitOps 支配。解决此问题的架构方法之一是通过 Kafka [代理](https://docs.conduktor.io/gateway/)。

代理充当处理 Kafka 请求的中介，然后将它们转发到 Kafka 代理。这可能包括根据客户端配置策略评估请求，甚至在将请求发送到代理之前对其进行处理（例如，字段级加密）。
## 代理方法集中了配置验证

代理方法集中了配置验证，这带来了跨客户端的一致性和合规性，而无需更改每个客户端应用程序。这降低了一个错误信息的客户端给其他人造成问题以及维护客户端库以保持最新的风险。

## GitOps 为管理 Kafka 带来了业务敏捷性和一致性

随着 Kafka 采用的扩展，新应用程序将带来新的需求、团队和复杂性。利用 GitOps 方法管理 Kafka 资源、客户端配置和规则，重点放在 Kafka 开发中的自动化、可追溯性和协作。

如果您正在扩展 Kafka 采用，并且需要一个带来一致性、标准化和业务敏捷性的框架，请联系我们并预订 [Conduktor 演示](https://www.conduktor.io/contact/demo/)。

## [YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。