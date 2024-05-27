
<!--
title: OpenTelemetry并非可观测性的“神奇按钮”
cover: https://cdn.thenewstack.io/media/2024/05/8d9624bb-levi-meir-clancy-guit_3xd5de-unsplash.jpg
-->

[OpenTelemetry 已成为](https://thenewstack.io/observability-in-2024-more-opentelemetry-less-confusion/) 可观测性体验的重要组成部分，随着其持续发展，它日益满足开发人员和运维人员的 [DevOps](https://thenewstack.io/devops/) 需求。然而，作为当前的主要开源项目之一，它仍需完善。它的功能——虽然可以说对于可观测性来说已经必不可少——仍处于进行中，其成功取决于社区持续的支持和辛勤工作。它的实用性还取决于与 [OpenTelemetry](https://github.com/open-telemetry) 结合使用的 [可观测性](https://thenewstack.io/observability/) 工具和平台。

> 译自 [OpenTelemetry Is No ‘Magic Button’ for Observability](https://thenewstack.io/opentelemetry-is-no-magic-button-for-observability/)，作者 B Cameron Gain。


“有些人将 OpenTelemetry 视为一个神奇按钮，但最终，它应该帮助你更好地理解你的可观测性数据——这取决于你将它与什么一起使用，”[Ryan Perry](https://www.linkedin.com/in/ryanaperry/)，[Grafana](https://thenewstack.io/grafanas-radical-app-platform-webassembly-kubernetes-and-apis/) 的工程总监告诉 The New Stack。“可观测性的全部意义在于能够询问有关你的系统的问题并获得答案，而无需添加新的孤岛式检测。”

![](https://cdn.thenewstack.io/media/2024/04/30463fed-capture-decran-2024-05-21-172222.png)

*来源：OpenTelemetry 文档。*

## 之前和之后

但在 OpenTelemetry 之前，甚至在可观测性之前，就有监控。遥测数据包括[日志、指标以及最近的跟踪](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/)，提供需要审查或通过监控收集的数据。然而，一旦通过监控收集和观察，如果数据未以适当的方式解析或引导以消除无关的遥测数据，那么它就没有多大意义。

同时，作为一名使用不同遥测数据的运维人员，对事件或性能的观察是有用的，并且在一定程度上一直是有用的。但它达不到可观测性的要求，可观测性涉及基于使用监控收集的数据进行推断的分析和得出可操作的见解。

OpenTelemetry 为可观测性提供了一个标准化流程。它可以看作三个主要组成部分：标准、[SDK](https://thenewstack.io/how-sdks-benefit-api-management/) 和收集器。标准确保互操作性，SDK 简化应用程序检测，收集器充当供应商中立代理。

它用于理解由指标、日志和跟踪组成的遥测数据。它不仅仅是供应商中立，因为它旨在允许用户将他们选择的可观测性工具集成到一个通用方法中，从而统一它们。

自 2019 年成立以来，OpenTelemetry 已可用于容纳由跟踪组成的遥测数据，随后是指标，最近是 2023 年的日志。

这在实践中意味着用户将寻求可观测性来获得理解并执行其他操作。通常，你可以询问有关你的系统的信息实时收集，例如为什么服务器内存不足、为什么跟踪很慢、为什么请求很慢或为什么有错误日志，并且能够在不执行新操作的情况下获得该答案。收集器擅长以随着时间推移越来越集成的形式获取日志、指标、跟踪和配置文件，为你指出正确方向，使用正确的工具来回答你的问题。但在实践中，它是一种工具，例如 Grafana Cloud Profiles（由 OSS 数据库 [Pyroscope](https://github.com/grafana/pyroscope) 提供支持），它可以补充你的可观测性，以“更好地回答你使用日志、指标、跟踪、配置文件或所有这些的某种组合提出的任何问题”，Grafana 的 Perry 说，他也是持续分析工具提供商 [Pyroscope](https://grafana.com/blog/2023/03/15/pyroscope-grafana-phlare-join-for-oss-continuous-profiling/) 的首席执行官兼联合创始人，Grafana Labs 于 2023 年收购了该公司。

领先的可观测性提供商提供 OpenTelemetry 的支持、维护和开发。其中包括 Grafana、

[Honeycomb](https://www.honeycomb.io/?utm_content=inline+mention)、Datadog、Dynatrace、Splunk 等组织。他们有一个共同的利益，那就是让 OpenTelemetry 变得更好。

同时，他们还提供大量工作，在某些情况下，通过提供利用其功能的工具来让 OpenTelemetry 变得更好。这些工具提供不同的分析，通常针对各种用例进行专门化，因为它们竞争提供独特的功能。他们通过为项目本身做出贡献以及创建和改进与 OpenTelemetry 结合使用的解决方案来实现这一点，即提供适当的可观察性所需的深度分析。

对于 Grafana Labs 来说，当然，这是通过其对各种遥测数据的 Grafana 可视化来完成的。Grafana 在提高其可视化和应用程序的可用性方面发挥了至关重要的作用，并且作为其排名前十的贡献者之一，为 OpenTelemetry 做出了重大贡献。

## 互操作性

Grafana 确实是大力支持 OpenTelemetry 的互操作性愿景和缺乏供应商锁定机制的倡导者，Grafana 首席技术官 [Tom Wilkie](https://uk.linkedin.com/in/tomwilkie) 在 4 月份于阿姆斯特丹举行的年度用户大会 [GrafanaCon](https://thenewstack.io/grafana-11-no-need-to-create-promql-queries-for-prometheus/) 期间告诉 The New Stack。“这与 Grafana 的‘大帐篷’理念和我们的开放思维文化产生共鸣。然而，OpenTelemetry 是一个庞大的项目，质量差异很大。一些领域，如指标，尚未完全兑现其承诺，”他说。

例如，在指标中，存在一些问题，例如一旦声明指标就无法将其删除，导致“如果大量流失”，则可能出现内存泄漏，Wilkie 说。“这些粗糙的边缘阻止我们完全推荐将其用于指标的生产用途——但我们正在努力解决这些问题。我们认为消除这些问题是我们的责任。此外，至关重要的是要注意，所有这些都不是专有的，”他说。“我们为该项目做出贡献，确保我们的改进使整个社区受益。我们有自己的 OpenTelemetry 组件发行版，这使我们能够比等待上游批准更快地发布错误修复和安全更新。”

![](https://cdn.thenewstack.io/media/2024/04/59d01f55-capture-decran-2024-05-21-171838.png)

*OpenTelemetry 集成，用于 Grafana Alloy 配置，与 Grafana 应用程序可观察性一起使用。*

Grafana Alloy 发行版的 OpenTelemetry Collector 是开源的，以及它相关的 [.NET](https://thenewstack.io/dev-news-wordpress-6-5-angular-signals-and-net-components/) 和 [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) SDK 的发行版。“客户寻求可以依靠的东西，并提供支持和维护合同，我们提供这些，”Wilkie 说。

![](https://cdn.thenewstack.io/media/2024/04/d4f476ea-capture-decran-2024-05-21-171449-1024x515.png)

## Beyla

Grafana 的开源 [Beyla](https://github.com/grafana/beyla) 通过 [eBPF](https://thenewstack.io/what-is-ebpf/) 提供跟踪，这是收集遥测跟踪的另一种方式。它的开发与 OpenTelemetry 项目的分析器并行，Grafana Labs 作为主要贡献者深度参与了该分析器的开发。分析器应该被证明对用户很有用，因为它通过扩展到代码级别来深入进行可观察性分析。它通过扩展在统一流中提取的遥测数据来实现对指标、跟踪和日志的更深入分析，该流扩展到整个网络中的应用程序的代码级别。代码被分析并存储。

Grafana 的工程总监 [Ryan Perry](https://www.linkedin.com/in/ryanaperry/) 告诉 The New Stack，使用 Beyla，你正在更多地致力于分析，这与跟踪密切相关。“分析可以告诉你你的代码在特定时间段内实际做了什么，将跟踪跨度与分析数据联系起来，”Perry 说。“例如，Beyla 可能会告诉你你的代码运行了七秒，而分析将分解这段时间在不同函数上花费的情况。”
