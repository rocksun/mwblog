<!-- 
# 揭谜可观测性 — 深入了解 OpenTelemetry 的顶级使用场景
https://d33wubrfki0l68.cloudfront.net/77d39e94a86d3b28084a4e68d30db0b14c30b7d2/a7edc/assets/images/otel-use-cases-cover-e4d9a90731a102e14d243e2af7a7c259.webp 

-->

OpenTelemetry可以用于生成和收集遥测数据，如日志、指标和追踪。使用OpenTelemetry进行可观测性的优点是其开源免费，能够避免您受制于某一供应商。您可以把OpenTelemetry应用于多个场景中。

译自 SigNoz 社区的 [Unlocking Observability - Dive into OpenTelemetry's Top Use Cases](https://signoz.io/blog/opentelemetry-use-cases) 。

OpenTelemetry是一个开源项目，已成为实现现代应用程序全面可观测性的标准。它是一个与供应商无关的检测库，提供了一套工具、API和SDK来创建和管理遥测数据(日志、指标和追踪)。

OpenTelemetry的顶级使用场景有:

- [分布式追踪](https://signoz.io/blog/opentelemetry-use-cases#distributed-tracing)
- [应用性能监控](https://signoz.io/blog/opentelemetry-use-cases#application-performance-monitoring)
- [指标监控](https://signoz.io/blog/opentelemetry-use-cases#metrics-monitoring)
- [日志和事件收集](https://signoz.io/blog/opentelemetry-use-cases#logging-and-event-collection)
- [上下文传播](https://signoz.io/blog/opentelemetry-use-cases#context-propagation)
- [异常监控](https://signoz.io/blog/opentelemetry-use-cases#exceptions-monitoring)
- [服务依赖分析](https://signoz.io/blog/opentelemetry-use-cases#service-dependency-analysis)

在我们讨论这些场景之前，让我们先简要了解一下OpenTelemetry。

## 什么是 OpenTelemetry?

OpenTelemetry是一个开源的工具、API和SDK集合，目的是规范我们生成和收集遥测数据(追踪、指标和日志)的方式。 一旦收集了数据，就可以导出到各种可观测性平台，为开发者和运维人员提供对软件性能和运行状况的洞见。

## OpenTelemetry 的主要使用场景

使用 OpenTelemetry 的一大好处是它可以让您摆脱供应商锁定。您可以随时切换到任何支持 OpenTelemetry 的可观测性后端进行存储和进一步分析。 如果您正在找一个本机支持 OpenTelemetry 数据的可观测性后端，[SigNoz](https://signoz.io/)是一个不错的选择。

OpenTelemetry 可以帮助您生成以下遥测数据:

- 追踪
- 指标
- 日志

您还可以关联这些数据，以更好地理解软件系统的运行情况。 需要注意的是，OpenTelemetry 专注于遥测数据的生成和收集，它不提供存储后端或任何可视化和分析收集数据的前端客户端。

OpenTelemetry 提供了一个 [OpenTelemetry Collector](https://signoz.io/blog/opentelemetry-collector-complete-guide/)，它可以帮助收集、处理和发送数据到不同的端点。

使用 OpenTelemetry 客户端库生成的数据都包含非常丰富的上下文信息。一个优秀的 [OpenTelemetry 后端](https://signoz.io/blog/opentelemetry-backend/)可以让您充分利用 OpenTelemetry 数据进行分析。

下面让我们详细探讨 OpenTelemetry 的几个主要使用场景:

### 分布式追踪

分布式追踪是 OpenTelemetry 的核心功能之一。它允许您追踪请求在分布式系统的不同服务之间的流动路径。这对于微服务架构尤为重要，一个用户请求可能会触发多个服务之间的调用链。

OpenTelemetry 为大多数编程语言(如 [Java](https://signoz.io/docs/instrumentation/java/)、[Python](https://signoz.io/docs/instrumentation/python/)、[Javascript](https://signoz.io/docs/instrumentation/javascript/)、[Golang](https://signoz.io/docs/instrumentation/golang/) 等)提供了追踪 SDK。

追踪数据可以让您可视化请求的路径，这对故障排除和优化此类系统的性能至关重要。

下图展示了 OpenTelemetry 原生后端 SigNoz 中的追踪界面:

![图片](https://d33wubrfki0l68.cloudfront.net/276a05777796f8a328a11d78ae520d9d2d57352d/961b1/img/blog/common/signoz_flamegraphs.webp)

### 应用性能监控

OpenTelemetry 原生后端(如 SigNoz)可以从追踪数据生成应[用性能监控图表](https://signoz.io/docs/userguide/metrics/#what-are-application-metrics)。您可以直接获取延迟、请求速率、错误率等统计图表。

OpenTelemetry 还允许您创建自定义指标，以获取应用程序的具体运行指标。

下图展示了 OpenTelemetry 原生后端 SigNoz 中的 APM 监控图表，包括 p90、p99 延迟、请求速率、apdex 等:

![图片](https://d33wubrfki0l68.cloudfront.net/4eaf566a9eeaa1445460f1f0fe636e471c4add62/ee534/img/blog/common/signoz_charts_application_metrics.webp)

### 指标监控

OpenTelemetry 提供了一个独立的组件 OpenTelemetry Collector(简称 OTel Collector)。您可以使用 OTel Collector 来收集各种指标，如主机指标、数据库指标、k8s 基础设施指标等。

您可以在 OTel Collector 中配置不同的[接收器](https://signoz.io/blog/opentelemetry-collector-complete-guide/#configuring-receivers)来收集各类指标。

下图展示了一个由 OTel Collector 收集指标的主机指标监控面板:

![图片](https://d33wubrfki0l68.cloudfront.net/d9a9bc8892ad75b4ec3e83644e18c2b018e77340/4894b/img/blog/common/signoz-infra-metrics.webp)

### 日志和事件收集

OpenTelemetry 允许您捕获和管理应用程序生成的日志和事件。它为 [Java](https://signoz.io/docs/userguide/collecting_application_logs_otel_sdk_java/)、[Python](https://signoz.io/docs/userguide/collecting_application_logs_otel_sdk_python/) 等语言提供了日志 SDK。使用 OpenTelemetry 日志 SDK，您可以生成结构化日志，这些日志也可以与追踪等其他数据关联。

日志功能有许多遗留问题需要兼容，OpenTelemetry 在日志支持方面，既要兼容各种遗留日志和日志库，又要在可能的情况下进行改进，与其他可观测数据更好地集成。

下图展示了一个由 OpenTelemetry 驱动的日志管理界面:

![图片](https://d33wubrfki0l68.cloudfront.net/b0ac3b3326a12519d1e0bf36ff969de496d37467/70ff5/img/blog/common/signoz_logs_raw_color.webp)

### 上下文传播

在分布式系统中，在请求移动到不同服务时，保持其上下文信息非常重要。OpenTelemetry 通过[上下文传播](https://signoz.io/blog/opentelemetry-context-propagation/)，可以确保请求关键信息(如追踪 ID、Span ID 等)随着请求在系统中流转。这对于复杂的多服务环境来说是必不可少的。

您还可以根据需要在服务之间传递其他重要信息。

### 异常监控

使用 OpenTelemetry 追踪数据，您可以监控应用程序中的异常。很少有后端工具可以做到这一点。像 SigNoz 这样的 OpenTelemetry 原生后端允许您从 OpenTelemetry 数据中监控异常。

下图展示了 SigNoz 中的异常监控界面:

![图片](https://d33wubrfki0l68.cloudfront.net/da9429c9e9271915c923be2d2cccaf249d14a589/3ce57/img/blog/common/signoz_exceptions_monitoring.webp)

### 服务依赖分析

基于 OpenTelemetry 的后端(如 [SigNoz](https://signoz.io/))可以让您分析应用程序中不同服务之间的依赖关系。通过可视化组件之间的交互，您可以识别关键路径、潜在瓶颈及优化机会。

## OpenTelemetry vs 供应商探针对比

与供应商的可观测性代理相比，OpenTelemetry 有许多优势:

- **灵活性**：OpenTelemetry 的供应商中立特性意味着您可以在不重新检测应用程序的情况下切换可观测性平台。而供应商的代理可能会将您绑定到其平台。
- **标准化**：OpenTelemetry 试图提供统一的可观测性标准。这可以简化不同语言环境中的检测。
- **社区支持**：作为开源项目，OpenTelemetry 受益于广泛的贡献者社区。供应商的代理可能不具备这样强大的社区。
- **可定制性**：虽然供应商的代理可能针对其平台进行了优化，但 OpenTelemetry 在定制和扩展性方面提供了更大的灵活性。

## OpenTelemetry 和 SigNoz

OpenTelemetry 正在悄然成为检测云原生应用程序的标准。它是避免供应商锁定的正确选择。它也使公司的监控体系更加一致，并可以随时间构建知识库。

OpenTelemetry 非常容易上手。您可以[在此](https://signoz.io/docs/instrumentation/)查看相关检测说明。由于 OpenTelemetry 不提供后端，您还需要选择一个支持它的后端。支持 [OpenTelemetry 的 APM](https://signoz.io/blog/opentelemetry-apm/) 可以作为不错的后端选择。

SigNoz是一个全栈的开源APM，您可以用它作为 OpenTelemetry 的后端。它提供了统一的日志、指标和追踪视图，并具有遥测数据之间的智能关联功能。

## 开始使用 SigNoz

最简单的运行 SigNoz 的方式是使用 SigNoz Cloud 云服务。您可以[在此](https://signoz.io/teams/)注册一个免费账号，并获得 30 天免费全功能试用。

您也可以自己安装和自行托管 SigNoz。它可以通过一个简单的安装脚本，在 macOS 或 Linux 系统上用三步完成安装。

该脚本会在 Linux 上自动安装 [Docker 引擎](https://docs.docker.com/engine/install/)。不过在 macOS 上，您需要先手动安装 Docker 引擎，然后再运行脚本。

```bash
git clone -b main https://github.com/SigNoz/signoz.git
cd signoz/deploy/
./install.sh
```

您可以访问我们的文档获取更多安装选项。

[https://signoz.io/docs/install/](https://signoz.io/docs/install/)

如果您喜欢这篇文章，欢迎查看 SigNoz 的 GitHub 仓库:

[https://github.com/SigNoz/signoz](https://github.com/SigNoz/signoz)