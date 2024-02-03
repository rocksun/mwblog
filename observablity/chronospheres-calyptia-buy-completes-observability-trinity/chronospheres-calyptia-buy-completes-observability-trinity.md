<!--
title: Chronosphere收购Calyptia补全可观测性三大支柱
cover: https://cdn.thenewstack.io/media/2024/01/931d46a9-chrono-calyptia-1024x684.png
-->

Calyptia不仅在Fluentd方面具备专业知识，而且对可观测性市场的顶尖领域有着敏锐的关注。

> 译自 [Calyptia Buy Completes Chronosphere Observability Trinity](https://thenewstack.io/chronospheres-calyptia-buy-completes-observability-trinity/)，作者 Joab Jackson 是 The New Stack 的高级编辑，专注于云原生计算和系统运维。他已经在IT基础设施和开发领域报道了25年，包括在IDG和Government Computer News的工作经历。

通过在本月早些时候[收购](https://techcrunch.com/2024/01/22/chronosphere-acquires-calyptia-to-extend-its-observability-platform/) Calyptia，[Chronosphere](https://chronosphere.io/?utm_content=inline-mention) 现在具备了一个完整的可观测性平台所需的三个支柱的竞争组件：指标、跟踪和现在的日志。

[Calyptia](https://thenewstack.io/calyptia-core-2-0-tackles-fleet-management-for-observability/) 是[围绕](https://thenewstack.io/calyptia-builds-observability-platform-around-fluentd-fluent-bit/)开源 [Fluentd](https://www.fluentd.org/) 和相关的 FluentBit 流水线构建的，这两个项目是 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline-mention) 的统一日志项目。它们已经成为许多云原生堆栈的事实标配，包括由 [Oracle](https://developer.oracle.com/?utm_content=inline-mention)、[IBM](https://www.ibm.com/?utm_content=inline-mention)、[Microsoft](https://news.microsoft.com/?utm_content=inline-mention)、[AWS](https://aws.amazon.com/?utm_content=inline-mention) 和 Google 运行的堆栈。

除了 Calyptia 在 Fluent bits 方面的专业知识外，使其变得吸引人的是它与 Chronosphere 的核心价值观的良好契合，即为用户保持数据成本低廉，Chronosphere 的首席执行官兼联合创始人 [Martin Mao](https://www.linkedin.com/in/martinmao/) 在接受 TNS 采访时表示。

“在度量方面，我们历史上做得非常好，对于跟踪方面也是如此，” Mao 解释道。“我们为您提供了对数据爆炸的可见性，了解是什么导致了这种情况以及如何解决这些问题。因此，这不仅仅是拥有这些功能，而且还要以可靠的成本拥有它们。”

与 Chronosphere 的竞争对手 DataDog 相比，这种方法确实是一个区别因素，[DataDog](https://thenewstack.io/real-talk-why-is-datadog-so-expensive/) 曾因为[高额的客户账单](https://thenewstack.io/datadogs-65m-bill-and-why-developers-should-care/)而受到批评。

(为了保持可观测性成本的可管理性，Chronosphere 还最近与 [Crowdstrike](https://www.crowdstrike.com/?utm_content=inline-mention) 合作，为 Chronosphere 平台[提供数据存储](https://chronosphere.io/news/chronosphere-unveils-logs-powered-by-crowdstrike/)。)

Mao 表示，Calyptia 在这个价值主张中非常合适。Calyptia 在为企业提供服务方面有着[明确的重点](https://thenewstack.io/calyptia-core-2-0-tackles-fleet-management-for-observability/)，“为市场顶级构建核心流水线产品，” 他说。

## 可观测性的三大支柱

在过去的几年里，曾被称为[监控](https://thenewstack.io/getting-started-with-infrastructure-monitoring/)的概念已经演变为[可观测性](https://thenewstack.io/3-observability-best-practices-for-cloud-native-app-security/)，提供了更多工具来理解性能并帮助进行故障排除。通常，可观测性由三个组件[来实现](https://thenewstack.io/the-3-pillars-of-observability/)：[指标](https://thenewstack.io/why-did-grafana-labs-need-to-add-adaptive-metrics/)、[跟踪](https://thenewstack.io/how-opensearch-visualizes-jaegars-distributed-tracing/)和[日志](https://thenewstack.io/grafana-adds-logging-to-its-enterprise-observability-stack/)。

“历史上，存在不同的解决方案，人们自己拼凑在一起，但行业正在朝着整合为单一平台的方向发展，” Mao 说道。

Chronosphere 计划将 Calyptia 的[日志转换和优化能力](https://calyptia.com/blog/the-fluent-ecosystem)整合到[公司自己的平台中](https://thenewstack.io/chronosphere-metrics-at-the-scale-of-uber/)。

“使用Calyptia，遥测数据可以自动路由到最佳的可观测性解决方案（如Chronosphere）进行监控，也可以路由到帮助维护安全姿态的[SIEM](https://thenewstack.io/what-separates-an-siem-platform-from-a-logging-tool/)平台，以及集成云原生环境中的不同系统，” Calyptia创始人、Fluentd核心贡献者，以及Fluentd的创作者 [Eduardo Silva](https://github.com/edsiper) 在[一篇博客](https://calyptia.com/blog/calyptia-joins-chronosphere-family)中写道。

## 什么是Fluentd？

Fluentd是一个高度可扩展的开源日志处理器，允许用户从多个来源收集遥测数据并将其分发到分析和监控系统。

在FluentBit之上构建的是[Calyptia的可观测性流水线](https://calyptia.com/)，实现了规模化的日志数据路由、转换和优化。用户可以添加过滤器来减少传输的数据量。数据还可以进行丰富化或脱敏，甚至可以实时分析。

到目前为止，FluentBit已被下载了120亿次。Mao 表示，Chronosphere承诺投资于Fluent项目和社区。

“Calyptia加入Chronosphere团队对于所有致力于开源云原生技术未来的人来说都是个好消息，” CNCF 首席技术官 [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/) 在Chronosphere[博客文章](https://chronosphere.io/learn/calyptia-acquisition-announcement/)的声明中表示。
