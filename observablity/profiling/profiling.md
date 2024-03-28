
<!--
title: OpenTelemetry宣布支持分析
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
-->

2023 年，OpenTelemetry 宣布已实现日志、指标和跟踪的稳定性。虽然这是我们在项目成立之初的最初目标，但实现我们为云原生应用程序启用内置可观测性的愿景要求我们继续与社区共同发展。今年，我们很自豪地宣布，在 2022 年瓦伦西亚 KubeCon + CloudNativeCon Europe 大会上创建 Profiling SIG 恰好两年后，我们通过合并分析数据模型 OTEP 并致力于在今年实现稳定的规范和实施，朝着这一目标迈出了重要一步！

> 译自 [OpenTelemetry announces support for profiling](https://opentelemetry.io/blog/2024/profiling/)，作者 OpenTelemetry Authors; Docs CC BY。


## OpenTelemetry 宣布支持分析

2023 年，OpenTelemetry 宣布其 [日志、指标和跟踪](https://www.cncf.io/blog/2023/11/07/opentelemetry-at-kubecon-cloudnativecon-north-america-2023-update/) 已实现稳定性。

虽然这是我们在项目组建之初的最初目标，但实现我们为云原生应用程序启用内置可观测性的愿景要求我们继续与社区共同发展。今年，我们很自豪地宣布，在 2022 年 Valencia KubeCon + CloudNativeCon Europe 大会上创建分析 SIG 恰好两年后，我们通过合并分析数据模型 OTEP 并致力于今年实现稳定的规范和实施，朝着这一目标迈出了重要一步！

OpenTelemetry 分析信号的这一里程碑反映了分析 SIG 内部的协作努力，其中来自各种分析供应商和最终用户的投入至关重要。这包括来自社区成员的大量贡献，例如：

- Felix Geisendörfer（Datadog）
- Alexey Alexandrov（Google）
- Dmitry Filimonov（Grafana Labs）
- Ryan Perry（Grafana Labs）
- Jonathan Halliday（Red Hat）

SIG 的集体努力一直专注于确定最适合分析的数据格式，社区内的积极讨论和提案证明了这一点。

在此之前达到的部分先前里程碑包括：

- 建立 [分析愿景对齐](https://github.com/open-telemetry/oteps/pull/212)（2022 年 8 月）
- 提议 [v1 分析数据模型](https://github.com/open-telemetry/oteps/pull/237)（2023 年 9 月）
- 提议 [v2 分析数据模型](https://github.com/open-telemetry/oteps/pull/239)（2023 年 11 月）

所有这些都对塑造 OpenTelemetry 分析功能的方向和演变发挥了至关重要的作用。这些由社区主导的讨论和贡献强调了该项目对包容性和协作的承诺，确保利用广泛的见解和专业知识来推动 OpenTelemetry 的发展。

## 什么是分析？

分析是一种在运行时动态检查应用程序代码的行为和性能的方法。持续分析可以深入了解代码级别的资源利用情况，并允许存储、查询和分析这些分析数据，并跨不同属性进行分析。对于开发人员和性能工程师来说，这是一种重要的技术，可以准确了解其代码中发生的情况。OpenTelemetry 的 [分析信号](https://github.com/open-telemetry/oteps/blob/main/text/profiles/0239-profiles-data-model.md) 扩展了在此领域所做的工作，并且作为业界首创，将分析与来自应用程序和基础设施的其他遥测信号联系起来。这使开发人员和运维人员能够将资源耗尽或不良的用户体验与其服务相关联，而不仅仅是受影响的特定服务或 Pod，还可以关联到最负责任的功能或代码行。

我们很高兴看到业界对这一愿景的接受，许多组织走到一起帮助定义分析信号。更具体地说，以下两项捐赠正在进行中：

- Elastic 已 [承诺捐赠](https://github.com/open-telemetry/community/issues/1918) 其专有的基于 eBPF 的分析代理 [1](#fn:1)
- Splunk 已开始 [捐赠其基于 .NET 的分析器](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pull/3196) 的流程

这些捐赠是为了加速 OpenTelemetry 分析的交付和实施。

## 这对用户意味着什么？

分析将支持自身与其他信号（例如日志、指标和跟踪）之间的双向链接。您将能够轻松地从资源遥测跳转到相应的分析。例如：

- 指标到分析：您将能够从 CPU 使用率或内存使用率的峰值转到消耗该资源的特定代码部分
- 跟踪到分析：您将能够了解不仅是跨服务延迟的位置，而且当延迟是由代码部分引起时，它将反映在附加到跟踪或跨度的分析中
- 日志到分析：日志通常会提供某些内容出现问题时的上下文，但分析将使您能够从仅仅跟踪某些内容（例如内存不足错误）转到准确查看哪些代码部分正在使用内存资源

这些只是其中几个，这些链接也可以反向工作，但更普遍的是，分析通过使用户能够轻松查询和了解其应用程序的全新维度，从而帮助实现可观测性的承诺，而无需额外的代码/工作。

## 一个正在行动的社区

如果没有致力于 [分析 SIG](https://github.com/open-telemetry/community/tree/main/sig-profiles) 的贡献者，这项工作是不可能完成的，他们致力于：
**OpenTelemetry 每天都在发展。**

我们最近通过了一个新的里程碑，每月有超过 1000 名独立开发者为该项目做出贡献，代表了 180 多家公司。在我们的最热门存储库中，OpenTelemetry 每月下载量超过 3000 万次，并且新的开源项目正在以稳定的速度采用我们的标准，包括：

- [Apache Kafka](https://cwiki.apache.org/confluence/display/KAFKA/KIP-714%3A+Client+metrics+and+observability)
- [数十个其他项目](/ecosystem/integrations)

我们还加深了与 CNCF 及其外部的其他开源项目的集成，例如：

- [OpenFeature](https://openfeature.dev)
- [OpenSearch](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/23611)

此外还集成了 Kubernetes、Thanos、Knative 以及更多其他项目。

2024 年有望成为 OpenTelemetry 的又一个重要年份，因为我们将继续实施和稳定现有的跟踪、指标和日志信号，同时增加对分析、客户端 RUM 等的支持。现在是参与的绝佳时机 - 查看我们的 [网站](https://opentelemetry.io) 了解更多信息！