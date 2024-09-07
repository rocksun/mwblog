
<!--
title: OpenTelemetry Collector简介
cover: ./cover.png
-->

现在您可能经常听到关于 OpenTelemetry 的消息。也许您已经阅读了 **[https://opentelemetry.io/docs/what-is-opentelemetry/](https://opentelemetry.io/docs/what-is-opentelemetry/)** 上的描述。也许您会问自己，“关于指标、跟踪、日志等等的很多内容——但我如何实际开始使用它？” 如果您有这样的想法，请继续阅读…

> 译自 [An Introduction to the OpenTelemetry Collector](https://medium.com/@joshleecreates/an-introduction-to-the-opentelemetry-collector-4fb47f22e1e8)，作者 Josh Lee。

作为一套开放标准，OpenTelemetry 允许整个生态系统中的可互操作工具使用可移植的遥测格式。但互操作性不仅仅局限于支持 OTLP（OpenTelemetry 使用的网络协议，不要与 O **L** TP 混淆）的工具和框架：

凭借其广泛的扩展，**OpenTelemetry Collector**可以成为所有遥测、可观测性和监控工具之间的通用翻译器——除了其作为收集、处理和转发遥测的管道的更标准角色之外。

## 什么是 OpenTelemetry Collector？

OpenTelemetry Collector是一个可部署的二进制文件（用 Golang 编写），它提供了一个可扩展的框架，用于遥测收集、处理和转发。这对于以下几个原因很有用：

- 在产生大量网络成本之前，可以在服务运行的同一节点或集群上组合、批处理和过滤各个服务的遥测。
- 可以更改遥测过滤和采样规则的配置，而无需更改或重新部署正在监控的服务。
- 可以添加扩展以支持任何可用遥测格式和后端目标之间的转换。

凭借这些功能，Collector通常与监控代理进行比较，但它可以做更多的事情，而不是供应商代理——它的可扩展性使其作为连接所有数据源和遥测数据Receiver的管道非常灵活。

## 插件

Collector插件可以有四种不同的形式：receiver, processor, exporter 和 connector。

这些插件被组合成一个管道，用于处理 Collector 处理的每个信号类型。当前可用的信号是指标、跟踪和日志。社区目前正在开发作为信号类型的 *配置文件*，用于持续性能分析。

![](https://miro.medium.com/v2/resize:fit:1400/0*LwMWCpFWG_OoNwdL)

**Receiver** 收集遥测，可以是拉取或推送的。例如，默认的 OTLP Receiver可以配置为提供 HTTP 或 gRPC 端点，服务可以在这些端点上发送 OTLP 数据；Prometheus Receiver配置为类似于 Prometheus 代理的方式抓取特定端点。

[**Processor**](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor) 可以在将遥测传递到管道中的下一阶段之前对其进行过滤、修改甚至添加。最重要的Processor是批处理Processor，它可以防止Exporter需要持续运行。转换Processor对于使用
[OTTL](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/pkg/ottl/README.md)(OpenTelemetry 转换语言) 在保存遥测之前对其进行过滤和规范化也很有用。

[**Exporter**](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter) 是管道中将遥测发送到下游Processor和数据库的最后阶段。如果需要，可以组合多个Exporter，将部分或全部遥测发送到多个目标。在这篇文章的后面，我们将探讨 ClickHouse Exporter，它可以将所有遥测写入与 SQL 兼容的 ClickHouse 数据库。

[**Connector**](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/connector) 是一种将一个遥测管道中的Exporter连接到另一个管道中的Receiver的方法——例如，跨度指标Connector从导出的跟踪中收集 RED（请求吞吐量、错误率和持续时间）指标，并将这些指标转发到指标管道的Receiver。

## Collector作为中心

通过组合可用的无数Receiver和Exporter，我们可以使用 OpenTelemetry Collector作为中心，无缝地为所有监控技术和存储和分析目标提供兼容性层。

![](https://miro.medium.com/v2/resize:fit:1400/0*UpqBAlAEKctT_kCp)

## Collector发行版

由于Collector是一个可扩展的框架，因此组织打包自己的Collector发行版非常常见（并且鼓励这样做）。这些发行版通常将包含可用社区插件的子集以及一些预设配置。发行版还可以包含独特的插件。

例如，Amazon 提供了 [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/)，它是一个预先配置用于从 AWS 环境收集指标、跟踪和日志的Collector发行版。

您也可以创建自己的生产优化发行版，其中只包含用例所需的扩展。

最后，为了方便起见，有许多现成的Collector容器镜像可用：

- [核心](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions/otelcol): 轻量级Collector版本，插件最少。
- [K8s](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions/otelcol-k8s): 预加载了特定于 Kubernetes 的插件。
- [Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib): 预加载了超过 90 个供应商和贡献者提供的插件。

您选择哪种方法取决于您的用例。contrib Collector非常适合概念验证，而在生产环境中，自定义构建的Collector将提供最佳性能。

## OpenTelemetry Collector在 Kubernetes 上

### 在 Kubernetes 上部署 OpenTelemetry Collector

官方的 [OpenTelemetry Collector Helm Chart](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) 包括将Collector部署为守护进程集、有状态集或部署的选项。在我们的 [Kubernetes 集群日志记录演示](https://github.com/Altinity/demo-opentelemetry-cluster-logs) 中，我们使用 `daemonset`，以便每个Collector实例可以从其本地节点收集日志和指标。

### Kubernetes Receiver - 收集集群和节点遥测

OpenTelemetry Collector提供了一些Receiver，可以收集 Kubernetes 集群的指标和日志。例如，[filelog Receiver](https://opentelemetry.io/docs/kubernetes/collector/components/#filelog-receiver) 可用于收集集群日志，并且还提供用于 [kubelet](https://opentelemetry.io/docs/kubernetes/collector/components/#kubeletstats-receiver) 和 [集群](https://opentelemetry.io/docs/kubernetes/collector/components/#kubernetes-cluster-receiver) 指标的Receiver。

### 资源属性 - 识别应用程序遥测

OpenTelemetry 使用 *资源属性* 来描述基础设施实体。来自 kubernetes 特定Receiver的遥测已使用正确的资源属性进行标记，使我们能够在节点和 Pod 级识别数据点。对于在 Kubernetes 中运行的应用程序，我们可以使用 [Kubernetes 属性Processor](https://opentelemetry.io/docs/kubernetes/collector/components/#kubernetes-attributes-processor) 自动使用相同的节点和 Pod 级描述符标记传入的应用程序遥测。

## 实践

您现在已经对 OpenTelemetry Collector是什么以及它如何充当 Kubernetes 集群等环境的可观测性“粘合剂”有了深刻的了解。我们已经涵盖了基础知识，但我们只是触及了 OpenTelemetry Collector可能性的表面。

在我们的下一篇文章中，我们将介绍 [使用 ClickHouse 和 OpenTelemetry 进行 Kubernetes 集群日志记录](https://altinity.com/blog/kubernetes-cluster-logging-with-clickhouse-and-opentelemetry)，我们将动手使用Collector从 Kubernetes 集群收集日志。我将引导您完成设置和配置，以便您可以开始从所有基于 Kubernetes 的应用程序和基础设施中提取一致且完整的日志。我们还将介绍 Grafana 用于可视化和 ClickHouse 用于存储，完成基于 OpenTelemetry 的端到端监控堆栈。