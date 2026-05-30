
<!--
title: OpenTelemetry 正式毕业：开源可观测性社区的里程碑
cover: https://news.cdn.dm.dynatrace.com/wp-content/uploads/2026/05/Blog-OTP-0311_OpenTelemetry_At_Enterprise_Scale_2x-1536x864-1.png
summary: 本文宣布 OpenTelemetry 正式从 CNCF 毕业，标志着该开源可观测性标准达到生产成熟度。文章阐述了共享标准的重要意义，并介绍了 Dynatrace 对该项目的深度贡献与支持。
-->

本文宣布 OpenTelemetry 正式从 CNCF 毕业，标志着该开源可观测性标准达到生产成熟度。文章阐述了共享标准的重要意义，并介绍了 Dynatrace 对该项目的深度贡献与支持。

> 译自：[OpenTelemetry graduates: A milestone for the observability Open Source community](https://www.dynatrace.com/news/blog/opentelemetry-graduates-a-milestone-for-the-observability-open-source-community/)
> 
> 作者：Omer Dayan, Mikko Viitanen

2026年5月，OpenTelemetry (OTel) 正式从[云原生计算基金会 (CNCF)](https://www.cncf.io/projects/opentelemetry/)毕业。这一里程碑标志着云原生生态系统达到了生产就绪和成熟状态，这归功于数以百计的企业和数以千计的开发者的共同努力，他们坚信并共同构建了可观测性的开放标准。

## OpenTelemetry 早已是标准，如今获得官方认证

如果你在过去几年中发布过生产代码，OpenTelemetry 几乎肯定已经触及了你的技术栈，无论它是通过 SDK 和收集器，还是通过追踪（traces）、指标（metrics）和日志（logs）。对于许多团队来说，OTel 已经悄然成为构建和运行现代应用程序的默认工具箱的一部分。它解决了一个真实存在的问题：行业需要一种用于遥测数据的通用语言，而 OpenTelemetry 成为了这种语言。

CNCF 的毕业反映了该生态系统的强大实力：多元化的贡献者群体、经过生产就绪验证的广泛厂商支持、全面的安全审计，以及一个由社区构建、服务社区并面向未来可持续发展的治理模型。

## 为什么共享标准能改变一切

毕业使 OpenTelemetry 正式成为可观测性的通用协议和共享语言：

1. 标准协议允许不同的工具（无论是开源的还是商业的）协同工作。
2. 语义约定定义了遥测数据的命名和结构方式。当所有系统都使用同一种语言时，大规模的关联分析就成为了可能。
3. OpenTelemetry 将检测（instrumentation）与后端分析解耦，使团队能够将遥测数据导出到任何后端系统，并在不重写代码的情况下切换分析平台。
4. 标准化、高质量的遥测数据使自动化、异常检测和 AI 驱动的洞察成为可能。随着系统变得更加复杂和自主，一致的协议变得至关重要。

## Dynatrace 热爱 OpenTelemetry 和开源

Dynatrace 自早期阶段就参与了 OpenTelemetry 的塑造，对规范、语义约定、收集器（Collector）以及许多其他领域做出了贡献，确保该标准能在企业规模下发挥作用。Dynatrace 拥有超过 46,000 次贡献和 54,000 次提交，是该项目的主要贡献者之一。

我们的焦点一直非常明确：在不牺牲其开放、厂商中立模型的前提下，让 OpenTelemetry 具备生产就绪能力。

除了 OpenTelemetry，Dynatrace 还积极致力于 30 多个开源项目，包括 W3C Trace Context，以及与 [Kubernetes、JMeter 等的集成。](https://www.dynatrace.com/platform/open-standards/)

## 常见问题解答

### **CNCF 毕业后，OpenTelemetry 稳定吗？**

是的。毕业证实了核心规范、API 和数据模型已经稳定，适合长期生产使用。团队可以放心地在各种环境和用例中采用 OpenTelemetry。

### **OpenTelemetry 会将团队锁定在特定的厂商或后端吗？**

不会。OpenTelemetry 将检测与后端分析解耦。团队可以将遥测数据导出到任何后端，并在不重写检测代码的情况下切换平台。

### **Dynatrace 如何支持 OpenTelemetry？**

[无论您身在何处，Dynatrace 都能为您提供支持](https://www.dynatrace.com/info/whitepapers/streamline-dev-workflows-with-dynatrace-otel/)。您可以原生摄取纯 OpenTelemetry 数据，无需使用专有的代理（agents）。在此基础上，您可以在几秒钟内查询数十亿个 span，跨越数 PB 的数据自动关联指标、日志和追踪，并获得[完整的可观测性上下文。](https://www.dynatrace.com/news/blog/data-in-context-how-dynatrace-solves-the-opentelemetry-analytics-challenge/)

## 想要看 OpenTelemetry 的实际应用吗？

请在 [Dynatrace Hub](https://www.dynatrace.com/hub/detail/opentelemetry/) 了解更多关于 OpenTelemetry 的信息。