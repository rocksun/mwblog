# 为什么 Grafana 需要 OpenTelemetry

翻译自 [Why Grafana Needs OpenTelemetry](https://thenewstack.io/why-grafana-needs-opentelemetry/) 。

Grafana Labs 不可避免地寻求将 OpenTelemetry 用于其著名的面板及其开源替代方案，包括 Grafana 开源工具。

![](https://cdn.thenewstack.io/media/2023/04/097db110-opentelemetry-traces-screenshot-e1681419266367-1024x707.png)

Grafana 通常被认为是最流行的数据可视化可观察性平台。 OpenTelemetry 已成为关键的开源组件，可在不同的可观测性平台之间提供兼容性。 OpenTelemetry 成为 Grafana 用户的主要工具只是时间问题。 Grafana Labs 不可避免地寻求将 OpenTelemetry 用于其著名的面板及其开源替代方案，包括 Grafana 开源工具，例如 Loki（日志聚合）、Mimir（用于 Prometheus metric）和 Tempo（ Trace 后端），以及主要的可观测性工具，例如 Prometheus（用于 metric 和 alert ）和 Graphite（用于收集和存储时间序列数据的平台）。

![](https://cdn.thenewstack.io/media/2023/04/7df2b1a4-capture-decran-2023-04-05-182919.png)

如上所述， Grafana 和 OpenTelemetry 之间存在着互惠关系。从技术角度来看，Grafana 在可观测性和监控领域拥有很多专业知识，“他们还通过向大型和小型组织销售解决方案而获得了相当快速的商业业务”，Lightstep 开发者关系负责人 Austin Parker 说道。“我们从遥测侧面看到的是，组织正在标准化采用像 OpenTelemetry 这样的开源标准，并且 Grafana 帮助 OpenTelemetr y取得成功不仅有利于 OpenTelemetry 本身，也有利于客户并为他们提供更多机会。” Parker 表示。

在用户方面，最近在 OpenTelemetry 阵营中发生了很多事情。在讨论 Grafana 的用户友好型 OpenTelemetry 适配之前，OpenTelemetry阵营已经有了不少进展。

可观测性需要高质量、可移植和准确的遥测数据。OpenTelemetry 的使命是将这种遥测作为云原生软件的内置功能。在 2022 年，该项目继续获得动力，并成为 CNCF 中速度第二快的开源项目。这种速度反映在 OpenTelemetry 被开源和商业监控工具越来越多地采用，以及最近发布的专注于改进 metric、trace、日志收集和处理的项目版本上。”Parker 表示。随着 OpenTelemetry 的不断普及，监控和可观测性解决方案采用它并提供基于 OpenTelemetry 构建分析工具对用户至关重要。OpenTelemetry 对 Kubernetes 集群、数据库事务、消息队列等常见架构组件等资源的标准元数据允许开发人员轻松地在监控工具之间传输和共享知识，并理解复杂系统。

OpenTelemetry 使组织能够了解其服务和基础架构的交互方式以及它们当前和过去的性能特征，从而更快地开发和部署驱动业务的软件，并迅速预测、识别、隔离和修复问题，Splunk 产品管理总监 Morgan McLean 说。

OpenTelemetry 使得这种深度可观测性更加强大和可用于开发人员、DevOps 人员以及创建和运行软件的组织。McLean表示：

* 简化可观测性——OpenTelemetry 使采用可观测性工具和最佳实践变得容易，到目前为止，很少有人能够完全实现这些工具和最佳实践，因为从现有服务和基础设施中提取形状正确的遥测信号非常困难。
* 提高可访问性——通过使用 OpenTelemetry 庞大且持续维护的仪器套件，组织和 DevOps 团队可以从几乎任何基础设施或任何服务中捕获基本数据，如 span, metric, 日志、元数据等。
* 创建更高的一致性和标准化—— OpenTelemetry 为所有数据类型提供了一组一致的语义约定，这意味着来自不同来源的不同信号可以相互关联。例如，缓慢的请求性能可以追溯到特定服务及其底层基础设施，而无需任何猜测或间接。
* 培养数据所有权——OpenTelemetry 可以预处理数据并将其路由到多个目的地，因此组织不会被锁定在单一供应商。此外，开发人员可以使用每种语言的本机 SDK 轻松创建特定于其业务的数据或注释，并且 OpenTelemetry 可以在大多数 metric, trace, 日志和其他遥测数据源之间接收和转换数据。总的来说，这为创建数据的人员和组织释放了数据。
* OpenTelemetry 对于可观测性也很重要，因为它合并并代表了用户从依赖专有可观测性工具到开源选项的转变，同时还有助于弥合开发人员和运营团队成员需求之间的差距。

Grafana Labs 高级工程经理 Fabian Stäber 表示：“当前的监控领域分为针对基础设施和平台工程师的监控解决方案，以及针对应用程序开发人员的应用程序可观测性解决方案。 “基础设施监控通常基于 prometheus 的 OpenMetrics 等开放标准，而应用程序监控通常基于专有工具。 OpenTelemetry 允许应用程序可观测性领域从专有工具过渡到开放标准，这将导致传统基础设施监控与应用程序监控的更紧密集成，” Stäber 说。 “ DevOps 背后的核心思想是打破开发人员和运维人员之间的壁垒。 OpenTelemetry 在打破这些障碍方面发挥着重要作用。”

## 方程式的 Grafana 部分

Grafana 需要适应 OpenTelemetry 用户的需求是多方面的。从宏观意义上讲， OpenTelemetry 和 Grafana “共享一个‘大帐篷’哲学”， Stäber 说。“两者都是开源的，在更广泛的生态系统中很好地集成，并且可以轻松扩展到新的使用场景，”他说。“ Grafana 用户重视 OpenTelemetry 的开放标准和用于仪器化应用程序的工具，并发现 OpenTelemetry 与 Grafana 实现应用程序可观测性非常契合。

Stäber 解释说，Grafana 工程师共同为 OpenTelemetry 收集器做出贡献，以确保它支持 Grafana 的指标数据库 Mimir、Grafana 的日志数据库 Loki 和 Grafana 的跟踪数据库 Tempo，而 Grafana 代理也提供本机 OpenTelemetry 端点。 “对于不需要任何中间件的情况，您可以将 OpenTelemetry 数据直接发送到 Grafana 云的 OTLP 端点，” Stäber 说。 “简而言之，Grafana 随处提供原生 OpenTelemetry 端点。”

正如 Grafana Labs 的社区总监 Richard Hartmann 所指出的那样，Grafana Labs “只发布我们自己正在使用的软件”，它对 OpenTelemetry 的支持有三个方面：“对于我们的任何项目和产品，我们通常是最积极的用户之一。第二个方面是在用户和客户需要到达的地方——引领可观测性空间并构建工具和技术，这些将变得相关，“Hartmann说。“第三个方面是在用户和客户想要到达的地方，在 OpenTelemetry 上关注行业重点，为了支持所有我们项目和产品中都很自然。我们还积极帮助塑造该项目，只有通过使用和扩展 OTel 才能成为领域专家，这也是我们用户和客户合理期望我们成为专家的领域。