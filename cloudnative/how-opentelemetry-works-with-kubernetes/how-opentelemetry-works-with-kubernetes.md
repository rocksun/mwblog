# OpenTelemetry 如何与 Kubernetes 协同工作

翻译自 [How OpenTelemetry Works with Kubernetes](https://thenewstack.io/how-opentelemetry-works-with-kubernetes/) 。

为 Kubernetes 安装 OTEL operator 是一个简单的过程。以下是如何做到这一点以及它如何简化监控 Kubernetes 集群的过程。

![](https://cdn.thenewstack.io/media/2023/04/b6462bf9-open-telemetry-satelllite-2-1024x575.jpg)
照片由 Unsplash 的 Stefan Widua 拍摄。

开源可观测性已成为 DevOps 工具链的重要组成部分，为开发人员、运营工程师和其他利益相关者提供对其应用程序和系统的运行状况和性能的实时可见性。

用于分布式跟踪的 [Jaeger](https://www.jaegertracing.io/) 、用于日志聚合的 [Fluentd](https://www.fluentd.org/) 和用于服务网格可观测性的 [Istio](https://www.fluentd.org/) 等项目扩展了工具集。随着开源可观测性的不断成熟，我们可以期待在自动化、机器学习和分析等领域看到进一步的进展，从而实现更复杂的监控和故障排除能力。

[OpenTelemetry](https://opentelemetry.io/) (OTEL) 是一组工具、API 和软件开发工具包 (SDK)，目前是 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline-mention) 的一个[孵化项目](https://www.cncf.io/projects/opentelemetry/)。它主要侧重于数据收集，而不是存储或查询功能。

OpenTelemetry 的主要目标是为开发人员和最终用户提供一种从其应用程序和系统创建、收集和导出遥测数据的标准方法，并促进不同可观测性工具和平台之间的互操作性。

OTEL 支持多种编程语言，包括 Java、Python、Go、Ruby 等，使其成为从不同类型的应用程序和系统收集遥测数据的多功能解决方案。

一旦 OpenTelemetry 组件收集了遥测数据，就可以将其导出到各种后端，例如提供存储和查询功能的软件即服务解决方案、平台或存储系统。 OpenTelemetry 提供与各种后端的集成，包括 Prometheus、Jaeger、Zipkin 等，从而更容易将遥测数据导出到不同的系统。

将 OTEL 与 Kubernetes 结合使用并不困难。事实上，为 Kubernetes 安装 OTEL operator 是一个简单的过程，在本文中，您将了解如何操作。

使用此 operator ，您可以轻松管理 Kubernetes 集群中的 OpenTelemetry 组件，并将它们配置为将遥测数据导出到您选择的后端。这简化了监控 Kubernetes 集群的过程，并使您能够就应用程序的运行状况和性能做出明智的决策。

## OpenTelemetry 中的基本组件

前四个组件由 instrumentation 开发人员或可观测性公司用于创建可观测性产品。

### 规范（Specification）

该规范提供了一种标准化的方式来定义这些组件的行为和功能，从而确保不同 OpenTelemetry 实现之间的一致性和兼容性。例如，规范定义了 trace 和 metric 数据的格式和语义，确保它们可以被系统中的其他组件正确解释。

### API

OpenTelemetry API 为开发人员提供了一种标准方法，可以使用 trace、metric 和其他遥测数据来 instrumentation 他们的应用程序。 API 与语言无关，并允许跨不同编程语言和框架进行一致的 instrumentation 。

API 为开发人员提供了一种标准方法，可以使用 trace 和 metric 来 instrumentation 他们的应用程序。

### SDK

OpenTelemetry SDK 提供特定于语言的 OpenTelemetry API 实现。 SDK 通过提供用于收集和导出遥测数据的库和实用程序，使开发人员可以更轻松地使用 trace 和 metric 来 instrumentation 他们的应用程序。

### 数据模型 - OTLP

OpenTelemetry 数据模型为遥测数据提供了一种标准化格式，称为 OTLP（OpenTelemetry 协议）。 OTLP 是一种供应商中立的格式，可以更轻松地将遥测数据导出到不同的后端和分析工具。

最后两个组件，OpenTelemetry Auto-Instrumentation 和 Collector ，是为那些想要从他们的应用程序中收集和导出遥测数据到不同后端的开发人员而设计的，而无需编写自己的仪器代码。

### Auto-Instrumentation

OpenTelemetry 包括一个自动 instrumentation 代理，它可以向应用程序注入 trace 和 metrics ，而无需任何手动 instrumentation 代码。这使得向现有应用程序添加可观测性变得容易，而无需对代码进行重大更改。

Auto-Instrumentation 组件可以作为库或代理下载和安装，具体取决于所使用的编程语言或框架。 Auto-Instrumentation 库通过 OpenTelemetry API 调用自动注入应用程序代码，以捕获和导出遥测数据。

### Collector

Collector 组件负责收集来自不同来源（例如应用程序、服务器和基础设施组件）的遥测数据，并将其导出到各种后端。

Collector 可以下载并配置为从不同来源收集数据，并可以在将遥测数据导出到不同后端之前对遥测数据执行聚合、采样和其他操作，具体取决于具体用例。

## 如何创建遥测数据

让我们考虑一个例子，我们有一个电子商务应用程序，其中包含三个工作负载——前端、驱动程序和客户——它们通过 HTTP 相互通信。我们希望收集遥测数据以监控这些应用程序的性能和健康状况。

为此，我们使用 OpenTelemetry API instrument 这些应用程序中的每一个： `logger.log()` 、 `meter.record()` 和 `tracer.span().start()` 。这些 API 允许我们创建遥测信号，例如日志、指标和跟踪。

一旦创建了这些信号，它们就会由 OpenTelemetry Collector 发送或收集，OpenTelemetry Collector 充当集中式数据中心。

Collector 负责处理这些信号，包括批处理、重新标记、PII 过滤、数据丢弃和聚合等任务，以确保数据准确且有意义。一旦 Collector 对数据感到满意，它就会将遥测信号发送到平台进行存储和分析。

收集器可以配置为将这些处理后的信号发送到各种平台，例如 Prometheus、Loki、Jaeger 等开源解决方案或 Dynatrace、New Relic 等供应商。

例如，Collector 可以将日志发送到 Loki 等日志聚合平台，将 metric 发送到 Prometheus 等监控平台，将 trace 发送到 Jaeger 等分布式跟踪平台。然后可以使用存储在平台中的遥测数据来深入了解系统的行为和性能，并确定需要解决的任何问题。

## 定义 Kubernetes Operator 的行为

您可以将 OpenTelemetry Operator 部署到您的 Kubernetes 集群，并让它自动 instrumentation 和收集您的应用程序的遥测数据。

OpenTelemetry Kubernetes Operator 提供了两个自定义资源定义 (CRD)，用于定义 Operator 的行为。这两个 CRD 一起允许您为您的应用程序定义 OpenTelemetry Operator 的完整行为。

这两个 CRD 是：

**otelinst** 。此 CRD 用于定义应用程序的 instrumentation 。它指定要使用 OpenTelemetry API 的哪些组件、要收集的数据以及如何将该数据导出到后端。

使用 otelinst CRD，您可以指定要 instrumentation 的应用程序的名称、语言和运行时环境、跟踪的采样率以及要使用的导出器类型。

**otelcol** 。此 CRD 用于定义 OpenTelemetry 收集器的行为。它指定收集器的配置，包括接收器（遥测数据源）、处理器（用于过滤和转换数据）和导出器（用于将数据发送到后端）。

使用 otelcol CRD，您可以指定用于通信的协议——例如 Google 远程过程调用 (gRPC) 或 HTTP，使用哪些接收器和导出器，以及任何其他配置选项。

## 安装 OpenTelemetry Kubernetes Operator

可以使用多种方法安装 OpenTelemetry Kubernetes operator ，包括：

* **Operator Lifecycle Manager (OLM)** 。这是安装 Operator 的推荐方法，因为它可以轻松安装、升级和管理 Operator。
* **Helm Chart** 。 Helm 是 Kubernetes 的包管理器，它提供了一种在 Kubernetes 上部署和管理应用程序的简单方法。 OpenTelemetry operator 的 Helm Chart 可用，可用于部署 operator 。
* **Kubernetes manifests** 。还可以使用 Kubernetes manifests 安装 Operator，它提供了一种声明式的方式来管理 Kubernetes 资源。可以自定义操作员清单以满足特定要求。

要收集遥测数据，我们需要使用创建遥测信号的代码来 instrument 我们的应用程序。有不同的方法来 instrument 遥测数据的应用程序。

### 显式/手动方法

在这种方法中，开发人员明确地将 instrumentation 代码添加到他们的应用程序以创建遥测信号，例如 log、metric 和 trace 。这种方法为开发人员提供了对遥测数据的更多控制，但它可能既耗时又容易出错。

### 直接集成到运行时

一些运行时，例如 Quarkus 和 WildFly 框架，与 OpenTelemetry 直接集成。这意味着开发人员不需要向他们的应用程序添加 instrumentation 代码——运行时会自动为他们生成遥测数据。这种方法更容易使用并且需要更少的维护，但它可能不如显式/手动方法灵活。

在运行时方法中直接集成的主要缺点是 instrumentation 仅限于受支持的框架。如果应用程序使用不受支持的框架，则遥测数据可能无法有效捕获或可能需要额外的自定义 instrumentation 。

如果所选的运行时或框架仅与特定的可观测性供应商兼容，这种方法也可能导致供应商锁定。

因此，这种方法可能并不适合所有应用程序或组织，尤其是当他们需要灵活选择可观测性栈或需要 instrumentation 各种框架和库时。

### 自动 instrumentation /代理方法

在这种方法中，OpenTelemetry agent 或 auto-instrumentation 库被添加到应用程序运行时。代理/库自动注入应用程序代码并生成遥测数据，无需开发人员添加 instrumentation 代码。


这种方法可能最容易使用并且需要最少的维护，但它可能不太灵活并且可能无法捕获所有相关的遥测数据。

虽然自动 instrumentation /代理方法有很多优点，但主要缺点之一是它可能会消耗更多内存和 CPU 周期，因为它支持应用程序中几乎所有 API 的范围广泛的框架和 instrumentation 工具。这种额外的开销会影响应用程序的性能，尤其是在应用程序已经是资源密集型的情况下。

此外，这种方法可能无法捕获所有必要的遥测数据，或者可能导致误报或漏报。例如，它可能无法捕捉到某些边缘情况，或者可能捕捉到太多数据，导致难以找到相关信息。

然而，尽管存在这些缺点，对于开始使用可观测性的组织，仍然强烈建议使用自动 instrumentation /代理方法，因为它提供了一种快速简便的方法来开始收集遥测数据。

## 如何收集和导出遥测数据

Collector 负责从检测代码接收遥测数据，处理并将其导出到平台进行存储和分析。 Collector 可以配置各种组件，例如 receiver, processor 和 exporter，以满足特定需求。

接收方负责接受来自各种来源的数据，例如 agent 、exporter 或网络，而 processor 可以转换、过滤或增强数据。最后，exporter 将数据发送到存储或分析平台，例如 Prometheus 或 Jaeger。

Collector 有两个发行版，Core 和 Contrib。

[Core](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions/otelcol) 是官方发行版，其中包含稳定且经过良好测试的组件，而 [Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib) 是社区驱动的发行版，其中包含额外的实验[组件](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions/otelcol-contrib)。

您还可以通过选择所需的组件并根据您的要求进行配置来构建自己的收集器。 Collector 是用 Go 编写的，这使得它易于部署和维护。 OpenTelemetry 网站上的文档提供了有关如何设置、配置和使用 Collector 的详细指导。

在某些情况下，OpenTelemetry 可以用作 Prometheus 的替代品，尤其是当您的边缘设备资源有限时。 Prometheus 非常注重监控和警报，而 OpenTelemetry 专为可观测性而设计，并提供超越 metric 的功能，包括 trace 和 log 记录。

此外，OpenTelemetry 可用于将数据导出到各种后端，包括 Prometheus，因此您仍然可以根据需要使用 Prometheus 进行监控和警报。 OpenTelemetry 的灵活性和可扩展性允许您根据您的特定需求和资源限制定制您的可观测性解决方案。

OpenTelemetry Operator 负责部署和管理 OpenTelemetry Collector，它是收集、处理和导出遥测数据的核心组件。它不部署其他 sidecar，例如 Envoy，但可以与它们一起工作以收集额外的遥测数据。

OpenTelemetry Collector 可以部署在不同的模式中，例如 sidecar、daemonset、deployment 或 statefulset，具体取决于特定的用例和要求。

但是，如果目标是从集群中的节点收集日志，那么将收集器部署为守护进程可能是一个不错的选择，因为它可以确保收集器实例在每个节点上运行，从而实现高效可靠的日志收集。

### OTEL Collector配置

以下是使用 otelcol 自定义资源定义部署 OpenTelemetry 收集器的示例 Kubernetes 清单文件：

```yaml
apiVersion: opentelemetry.io/v1alpha1
kind: OpenTelemetryCollector
metadata:
 name: otel-collector
spec:
 config: |
  receivers:
   otlp:
    protocols:
     grpc:
exporters:
 prometheus:
  endpoint: "localhost:9090/metrics"
processors:
 batch:
 queued_retry:
pipelines:
 traces:
  receivers: [otlp]
  processors: [batch]
  exporters: [prometheus]
```

在此示例中，我们定义了一个名为 `otel-collector` 的收集器，它使用 OTLP receiver 接收跟踪数据，使用 Prometheus exporter 将 metric 导出到 Prometheus 服务器，以及两个 processor（ `batch` 和 `queued_retry` ） 来处理数据。 config 字段指定 collector 的配置，以 YAML 格式编写。

使用 OpenTelemetry 收集 trace、metric 和 log 很重要，原因如下：

* **提高可观测性**。通过收集和关联 trace 、metric 和 log，您可以更好地了解您的应用程序和系统的执行情况。这种增强的可观测性使您能够在问题影响您的用户之前快速识别和解决问题。
* **改进了故障排除**。 OpenTelemetry 提供了一种收集遥测数据的标准化方法，可以更轻松地解决整个堆栈中的问题。通过在一个地方访问所有相关的遥测数据，您可以快速找到问题的根本原因。
* **更好的性能优化**。通过访问详细的遥测数据，您可以就如何优化应用程序和系统以获得更好的性能和可靠性做出明智的决策。例如，通过分析 metric ，您可以识别系统中未充分利用或过度利用的区域，并相应地调整资源分配。
* **跨平台兼容性**。 OpenTelemetry 旨在跨多种编程语言、框架和平台工作，这使得从堆栈的不同部分收集遥测数据变得更加容易。这种互操作性对于使用多种技术并需要在整个堆栈中标准化其可观测性实践的组织来说非常重要。

### OpenTelemetry Log

OpenTelemetry Log 提供了一种标准化的方式来收集、处理和分析分布式系统中的日志。通过使用 OpenTelemetry 收集日志，开发者可以避免日志分布在多个系统和不同格式的问题，从而难以分析和排查问题。

借助 OpenTelemetry Log ，开发人员可以从多个来源收集日志，包括遗留日志库，然后使用通用格式和 API 处理和分析它们。这允许更好地与其余的可观察性栈集成，例如 metric 和 trace ，并提供更完整的系统行为视图。

此外，OpenTelemetry Log 提供了一种使用附加上下文信息丰富日志的方法，例如有关请求、用户或环境的元数据，可用于使日志分析更有意义和有效。

## OpenTelemetry 的下一步是什么？

### Web 服务器的 auto-Instrumentation

OTEL 网络服务器模块由 Apache 和 Nginx 工具组成。 Apache 模块负责通过在运行时将检测注入 Apache 服务器来跟踪对服务器的传入请求。它捕获传入请求中涉及的许多模块的响应时间，包括 mod_proxy。这允许捕获每个模块的分层时间消耗。

类似地，Nginx Web 服务器模块还通过在运行时将 instrumentation 注入 Nginx 服务器来启用对服务器传入请求的跟踪。它捕获请求处理中涉及的各个模块的响应时间。

### OpenTelemetry Profiling 

此[文档](https://github.com/open-telemetry/oteps/blob/main/text/profiles/0212-profiling-vision.md)概述了 OpenTelemetry 项目中分析支持的长期愿景。该计划是 OpenTelemetry 社区成员讨论和合作的结果，代表了不同的行业和专业知识。

该文档旨在指导 OpenTelemetry 中分析支持的开发，但不是要求清单。该愿景预计会随着时间的推移而发展，并根据学习和反馈进行完善。

### 开放代理管理协议（Open Agent Management Protocol）

开放代理管理协议 (OpAMP) 是一种网络协议，可以远程管理大量数据收集代理。它允许代理报告其状态并从服务器接收配置，并从服务器接收代理安装包更新。

OpAMP 与供应商无关，因此服务器可以远程监控和管理一组实施 OpAMP 的不同代理，包括来自不同供应商的一组混合代理。

它支持代理的远程配置、状态报告、代理自己的遥测报告、可下载的代理特定包的管理、安全的自动更新功能和连接凭证管理。此功能允许对大量混合代理进行单一管理视图管理。