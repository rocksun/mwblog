<!--
title: 可观测性查询语言标准工作启动
cover: https://cdn.thenewstack.io/media/2024/01/e8814975-nature-3162233_1280-1024x682.jpg
-->

可观测性查询语言标准工作组寻求建立统一的可观测性语言标准。

> 译自 [Work Commences on the Observability Query Language Standard](https://thenewstack.io/works-commences-on-the-observability-query-language-standard/)，作者 B. Cameron Gain。

[2023年标志着可观测性领域的重大进步](https://thenewstack.io/observability-in-2024-more-opentelemetry-less-confusion/)，关键的发展包括OpenTelemetry项目达到通用可用性和Elastic Common Schema合并到OpenTelemetry中。

然而，在这些进步中，一个关键的挑战仍然存在——可观测性数据库缺乏标准化的查询语言。

在我2023年和2024年为可观测性文章进行报道时，一个显著的发现曝光了出来。一个名为可观测性查询语言标准工作组的新工作组已经出现，它在[云原生计算基金会](https://cncf.io/?utm_content=inline-mention)可观测性技术咨询小组下运作。

该小组旨在通过努力达成共同标准来解决各种可观测性数据库查询语言之间当前不兼容的问题——与OpenTelemetry项目的原则相符的标准。

长期以来，数据库一直在使用不同的查询语言来查询各种可观测性方面，例如Lucene用于日志查询，PROMQL用于指标。这种多样性导致系统之间缺乏互操作性和兼容性，阻碍了无缝的通信和集成。

[可观测性查询语言标准工作组](https://github.com/cncf/toc/issues/1034)通过建立统一的可观测性语言标准，以消除这种差距，促进可观测性生态系统内的凝聚力和协作。

OpenTelemetry 项目的主要开发者 [Dotan Horovits](https://www.linkedin.com/today/author/horovits) 是 Logz.io 的首席开发倡导者，也是 CNCF 的云原生大使。他指出，2023 年，OpenTelemetry 项目在可观测性的三大支柱上都取得了显著的进步，实现了总体可用性。

这包括将 [Elastic Common Schema 集成到 OpenTelemetry](https://thenewstack.io/opentelemetry-and-elastic-common-standard-comes-not-too-soon/) 中，以及决定停用 OpenCensus。此外，他说，正在推进将 Prometheus 协议正式化为 IETF 开放标准 (RFC2119) 的工作。

## CI/CD 标准化

Horovits 表示，这些举措解决的关键挑战之一是持续集成/持续交付(CI/CD)流水线缺乏标准化。尽管许多 CI/CD 工具会发出遥测数据，但缺乏标准化的方法、规范或语义约定对于[使用可观测性工具进行有效监控](https://thenewstack.io/next-gen-observability-monitoring-and-analytics-in-platform-engineering/)构成了重大障碍。为了应对这一挑战，2023 年 CNCF 下设立了一个新的倡议，以扩展 OpenTelemetry 的功能，使其涵盖 CI/CD 使用案例。

OpenTelemetry 在 [DevOps 场景中已经因其在监控生产系统](https://thenewstack.io/qa-why-observability-data-sampling-can-cost-devops-teams-time-and-money/)和减少平均识别时间(MTTI)与平均恢复时间(MTTR)方面的有效性而受到认可，Horovits 说，它已准备好在 CI/CD 可观测性中发挥关键作用。该倡议旨在利用 OpenTelemetry 作为开放统一的规范，为标准化的 CI/CD 遥测数据奠定基础。这种方法不仅可以确保一致性，还可以促进用于 CI/CD 流水线中收集和传输遥测数据的专门工具的开发。

正如可观测性查询语言标准工作组所展示的那样，标准化可观测性查询语言的努力以及扩展 OpenTelemetry 以支持 CI/CD 使用案例，无疑显示了进展。这些举措不仅为增强互操作性铺平了道路，还为更简化和高效的可观测性生态系统奠定了基础——这样的生态系统将更好地满足[现代技术和开发](https://thenewstack.io/ai-engineering-what-developers-need-to-think-about-in-2024/)实践的不断变化的需求。
