
<!--
title: 2024年API监控完全指南-指标、工具和经过验证的实践
cover: cover.png
-->

据 Akamai 称，83% 的网络流量通过 API。微服务、服务器和客户端不断通信以交换信息 [1]。即使您进行 Google 搜索以访问本文，也涉及到您的浏览器客户端调用 Google API。鉴于 API 控制着互联网，因此企业严重依赖它们。API 健康状况与业务繁荣直接成正比。

> 译自 [The Ultimate Guide to API Monitoring in 2024 - Metrics, Tools, and Proven Practices | SigNoz](https://signoz.io/blog/api-monitoring-complete-guide/)，作者 Harish R SigNoz Community。

本文涵盖了有关 API 监控的所有内容，因此您的 API 基础设施的健康状况始终处于受控状态。我们还将介绍一些用于监控 API 健康状况的重要指标、可用于 API 监控的顶级工具、最佳实践和未来趋势。

让我们深入了解一下。

## 什么是 API？

在 JavaScript 库发展之前，网页是使用服务器端渲染来呈现的。当客户端发出请求时，服务器会将一个完全水合的 HTML 页面发送回客户端。完全水合的 HTML 指最终在浏览器中看到的 HTML 数据，使用来自数据库的相关信息填充。在此方法中，客户端和服务器紧密耦合。

![JavaScript 库发展之前的网页呈现方式](https://signoz.io/img/blog/2024/03/api-monitoring-complete-guide-before-js.webp)

*JavaScript 库发展之前的网页呈现方式*

然后我们有了最近流行的客户端渲染。客户端和服务器彼此独立。浏览器首先获取基本的 HTML 和 JavaScript 块。稍后，客户端向服务器发出“API 调用”以获取数据、处理数据，然后呈现 UI。

![使用 API 调用呈现网页](https://signoz.io/img/blog/2024/03/api-monitoring-complete-guide-api.webp)

*使用 API 调用呈现网页的方式*

现在人们能够设想 API 在请求生命周期中的位置。

**应用程序编程接口**。正如首字母缩写词所说的那样，它是应用程序提供的接口，其他应用程序可以与之集成。例如，Google 的后端服务器公开了 Web 客户端可以与之集成的 API。

## 了解 API 监控

API 监控是持续观察和分析应用程序编程接口 (API) 的性能、可用性和安全性以确保其正确有效运行的过程。它涉及跟踪各种指标、日志和实时数据，以及时识别和解决问题，从而保持最佳 API 健康状况并防止潜在威胁或故障。

让我们了解 API 监控的不同方面。

### 监控可用性

确保 API 的可用性意味着检查它是否可操作、能够接收请求并提供正确的响应。可用性指标决定了 API 的健康状况。监控 API 所依赖的外部资源至关重要。

### 提高性能

性能监控侧重于 API 对请求的响应程度，尤其是在流量高峰期。它不仅关乎速度，还关乎确保 API 能够在不影响服务质量的情况下处理负载。

### 维护安全性

没有安全性的健康且高性能的 API 毫无用处。API 监控工具可以实时跟踪和分析 API 请求和响应。通过监控异常模式或意外行为（例如流量突然增加或异常 API 调用），组织可以快速检测到潜在的安全威胁或攻击，例如 [DDoS](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack) 攻击或注入攻击。

### API 监控中的关键信号

我们设置了适当的指标，帮助我们根据每个标准直观地了解 API 的执行情况。公司通常在相关指标上设置警报，以检测任何意外行为。对于调试，日志和跟踪非常有帮助。

**指标**

指标是衡量 API 性能和健康状况各个方面的定量数据。它们作为关键指标，提供对 API 的效率、可用性和安全性的见解。通过分析这些指标，公司可以衡量其 API 的整体性能，并做出明智的决策以增强其功能。

**日志**

日志是在 API 执行期间记录的事件、消息或数据点。它涉及捕获有关 API 的相关信息，例如状态、更新、错误和警告。API 开发人员在调试任何应用程序错误时会发现它很有用。即使是基础设施团队也会使用日志来诊断任何事件。

**跟踪**

跟踪是一种技术，它允许我们跟踪每个请求或事务在分布式系统或复杂软件应用程序（可能由相互连接的微服务组成）中移动时的旅程。这涉及捕获有关各个请求的详细数据，因为它们遍历系统内的各种组件或服务。通过这样做，跟踪提供了对请求采取的路径及其时间的宝贵见解，使开发人员能够掌握系统的不同元素如何相互交互。这种可见性有助于查明可能出现的性能瓶颈或问题。跟踪在采用微服务或具有多层的架构中特别有益，因为它促进了跨不同系统组件的全面跟踪和事件关联。

**警报**

警报是设置满足条件的标准的过程，在此条件下执行特定操作。例如，一旦 CPU 使用率超过 80%，就可以设置电子邮件操作。由于这最终可能导致 100% 和整个系统故障，因此事先了解它可以让工程团队有机会分析和防止故障。

通过自动警报、使用指标、日志和跟踪进行更快的调试，您可以设置高效的 API 监控。在单个视图中拥有所有这些信息在防止系统故障、检测扩展问题或处理任何奇怪模式时会提供很大帮助。

## 为什么监控 API 至关重要？

[](#why-monitoring-apis-is-critical)

通过为不同的团队设置 API 监控来跟踪对他们最有用的指标，可以收集大量见解。可用性和性能指标帮助开发团队评估瓶颈并构建弹性软件。资源利用率、DevOps 和管理团队的计费警报，以便他们可以采取适当的措施。RPS、Ingress 和 Egress 带宽指标允许安全团队在发现可疑情况时迅速采取保护措施。

以下是 API 监控至关重要的几个原因：

* 对于大规模系统来说，持续监控至关重要，因为服务请求中的任何故障都会导致业务损失。声誉岌岌可危，服务故障可能会使其瘫痪。
* 通过持续监控和警报，甚至可以在问题出现之前更好地防止故障。
* 持续监控 API 可确保较低的故障率，从而确保客户保留。可靠的服务有机会通过口碑传播。
* 在调试服务故障时，监控 API 也很有帮助。借助日志、跟踪和指标，可以快速有效地执行根本原因分析 (RCA)。
* 产品经理负责制定 API 功能路线图。通过分析趋势和模式，他们可以就资源分配、功能优先级和产品策略做出数据驱动的决策。
* 监控确保 API 指标与关键绩效指标 (KPI) 紧密相连，将技术成就建立在业务现实之上并推动组织成功。
* 采用指标（如 API 使用情况、唯一 API 消费者）对增长/业务团队很有用。这将帮助他们专注于产品收入、采用和客户成功。

## API 监控的一些关键指标

建立一个明确定义和连接 API 指标与关键绩效指标 (KPI) 的框架是确保 API 策略成功最重要的步骤之一。

因此，每个组织都需要确定 API 策略，并在设定的时间范围内将其指标与该目标保持一致。每个团队都会跟踪对他们最重要的指标。

从广义上讲，API 指标有三种类型：

* **运营指标** - 纯粹基于 API 的稳定性、可靠性和性能。
* **采用指标** - 数据点说明最终用户采用 API 的程度。
* **产品指标** - 根据业务目标将 API 链接到业务 KPI。

### 运营指标

以下是 API 监控的一些重要运营指标：

1. **正常运行时间：** 这是决定服务可用性的最重要的指标。它通常与服务级别协议 (SLA) 相关联。它是根据服务器在选定期间可用的分钟数或小时数计算的。
2. **CPU 和内存使用率：** 跟踪资源利用率让我们了解何时需要扩展我们的实例。通过添加更多资源垂直扩展，或通过调整每个实例的吞吐量水平扩展。它还可以向我们发出警报，告知我们异常情况占用了超出预期的过多 CPU 和内存。计算 CPU 利用率涉及一个简单的公式：CPU 利用率 =（用于非空闲任务的总时间 / 总时间）x 100。
3. **错误率：** 错误率（如每分钟错误和错误代码）可以帮助你追踪各个 API 中的问题。400 到 500 范围内的错误代码可能表明有问题的 API 或 Web 服务提供商。它以每分钟发生的错误请求计算。
4. **每分钟/秒请求数 (RPM/RPS)：** 每分钟请求数会追踪每分钟的传入请求数。它描述了在选定时间内接收到的 API 流量。这是一个至关重要的指标，用于了解系统承受的负载。该指标还将揭示 API 在负载增加时的扩展效果。
5. **响应时间（延迟）：** 从请求发起到客户端收到响应所花费的总周转时间。延迟告诉我们 API 服务的响应速度有多慢/快。对于大型公司而言，将延迟保持在尽可能低的水平至关重要，否则用户体验将会恶化。
6. **限制：** 当网络拥塞时，服务器将不再接受任何新的传入请求。所有新请求都将受到限制，这意味着它们将得不到处理。这是因为服务器没有额外的并发带宽来处理。它以 RPS（每秒受到限制的请求数）衡量。

### 采用指标

1. **唯一的 API 消费者：** 根据选定的时间范围，该指标衡量使用 API 服务的唯一消费者的数量。它以消费者的数量计算。常用的时间范围是 DAU（每日活跃用户）、MAU（每月活跃用户）。这些对于了解服务的用户采用情况非常有帮助。
2. **API 使用量增长：** 与追踪 API 消费者非常相似，增长指标追踪给定时间范围内 API 消耗量的增加/减少。
3. **首次调用时间：** 此指标衡量开发人员创建帐户、生成 API 凭证和运行第一个 API 调用所需的时间。让开发人员能够尽快启动并运行是一个重中之重，这使得此指标成为衡量整体 API 开发人员体验的最重要指标。

### 产品指标

1. **收入：** 此指标包括直接和间接来源的总收入。虽然一些 API 直接获利，但其他 API 通过第三方集成产生收入。
2. **API 使用量：** API 消耗按每个 API 分组，从而可以识别使用最多或最少的 API。
3. **用户使用情况细分：** 此指标包含用户对其 API 使用情况的按用户细分，有助于为他们提供更好的服务/支持。

将 API 指标与业务 KPI 保持一致是做出数据驱动决策并确保你的 API 策略提供组织所需价值的主要方式之一。不仅如此，获得对 API 的可见性还可以让基础设施和应用程序团队衡量对他们最重要的运营指标。

## 顶级 API 监控工具

以下列出了 5 种可供你使用的 API 监控工具：

### Signoz

[Signoz](https://signoz.io/) 是一款全栈开源 APM（应用程序性能监控），可用于有效的 API 监控。它旨在原生支持 [OpenTelemetry](https://opentelemetry.io/)，这是一个 [云原生计算基金会](https://www.cncf.io) 旗下的开源项目，正成为对云原生应用程序进行检测的世界标准。

Signoz 可用于监控 API 性能的指标，并且非常适合监控基于微服务或无服务器架构的应用程序中的 API。

### Prometheus

[Prometheus](https://prometheus.io) 是一款开源指标监控工具，最初于 2012 年在 SoundCloud 开发，然后作为开源项目发布。它于 2016 年被 [云原生计算基金会](https://www.cncf.io) 接受，并且是继 Kubernetes 之后第二个从该基金会毕业的项目。

你可以使用 Prometheus 来监控你的 REST API。它是一款用于监控任何类型的时间序列数据（例如端点上的每秒请求数）的优秀工具。

### Graphite

[Graphite](https://graphiteapp.org/) 是一款开源监控工具，专注于存储时间序列数据。它有三个主要组件：Carbon、Whisper 和 Graphite。Carbon 监听时间序列数据，Whisper 存储时间序列数据，Graphite Web 渲染图表。

Graphite 的 UI 可能不太好，但它提供了与 Grafana 的集成，以便构建更好的图表以进行可视化。

### Datadog

[Datadog](https://www.datadoghq.com/) 合成监控允许你创建无代码测试，主动模拟应用程序上的用户事务，并跨系统的各个层监控关键网络端点。它通过 API 和浏览器测试检测面向用户的错误，并启动全系统调查，以优化性能并增强最终用户体验。

### New Relic

[New Relic](https://newrelic.com) 是一款应用程序监控企业工具，提供从应用程序监控和基础设施监控到日志管理的解决方案。**New Relic Synthetics** 功能通过在数千个公共和私有位置模拟流量来提高构建质量，以主动检测和解决问题。它还提供有关 API 性能的警报。

## 一个好的工具应该提供什么？

- **警报：** 当 API 检查失败时发出警报的能力，以最大程度地减少警报疲劳并减少误报。支持基于运行次数、时间范围等的多种警报策略。
- **分析响应数据的能力：** 对于有效的 API 监控，将警报功能扩展到简单的连接或 HTTP 错误之外，以包括基于响应头和正文内容的可自定义条件至关重要。这意味着能够识别特定的标题名称/值并解析 JSON 等标准格式，以根据预期结果验证字段值的正确性。监控中的这种精确性允许对 API 可用性和数据完整性进行有针对性的验证，以满足技术受众的细微需求。
- **响应时间指标：** 在监控 API 的性能时，至关重要的是将整体响应时间分解为其组成部分：DNS 解析、连接建立、SSL/TLS 协商、首次字节时间 (TTFB) 和数据传输阶段。这种细粒度分析不仅阐明了 API 响应所需的总时间，还有助于精确定位可能发生瓶颈的特定部分。例如，延长的 TTFB 表明服务器或后端处理中存在低效率，而延长的 DNS 解析时间可能表明 DNS 服务提供商存在问题。
- **定价：** 定价模式应透明且易于理解，没有隐藏成本。
- **直观的 UI/UX：** 除了其广泛的功能集之外，该工具还必须拥有直观且用户友好的 UI/UX。这确保了轻松导航和理解功能。

## API 监控的最佳实践

API 监控的一些最佳实践包括：

- 在多个用户位置进行测试
- 多个时段的活动感知
- **定义明确的目标：** 定义与业务目标一致的具体目标和关键绩效指标，并在业务目标发生变化时更新这些目标。
- **日志记录和审计：** 维护详细的日志以进行审计、合规性和事件后分析。
- **与 DevOps 集成：** 将 API 监控集成到 DevOps 流程中，以进行持续测试和早期问题检测。

### 结论

总之，建立服务状态网站和利用强大的 API 监控工具是确保服务可靠性和性能的基本组成部分。通过实施最佳实践，例如彻底的测试、明确的目标设定以及与 DevOps 流程的无缝集成，公司可以主动检测问题、优化性能并增强最终用户体验。

请记住，选择提供警报功能、响应数据检查、响应时间指标、透明定价和直观 UI/UX 的工具对于有效的 API 监控至关重要。采用这些实践并利用合适的工具不仅有助于维护服务可用性，还可以推动服务交付的持续改进。保持主动，保持观察，并为你的组织提供合适的工具以成功进行 API 监控。
