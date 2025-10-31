***编者注：**以下文章摘自 Manning 出版书籍《[Fluent Bit与Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS)》的第1章，该书是配置Kubernetes日志、指标和追踪管道的指南。此摘录重点介绍了Fluent Bit与OpenTelemetry的关系，以及它在捕获日志以及CPU、内存和存储使用情况等本地指标方面的演变。要更深入地了解Fluent Bit和OTel如何执行不同的功能，请[下载完整版书籍](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS)。*

## OpenTelemetry如何诞生

在OpenTelemetry (OTel) 出现之前，指导指标、追踪和日志可观测性的主要规范来自[云原生计算基金会 (CNCF)](https://www.cncf.io/) 内的几项标准化工作，包括[OpenTracing](https://opentracing.io)、[OpenCensus](https://opencensus.io/?utm_source=sponsored-content&utm_id=TNS)，以及——鉴于其主导地位——[Fluentd](https://chronosphere.io/learn/fluent-bit-vs-fluentd/)，并与之相关联的[Fluent Bit在日志结构化方面的应用](https://thenewstack.io/a-guide-to-fluent-bit-processors-for-conditional-log-processing/)。

不同的标准通常需要不同的工具来捕获这些数据。[Fluent Bit](https://thenewstack.io/fluent-bit-a-specialized-event-capture-and-distribution-tool/) 始终能够捕获一些指标数据；物联网 (IoT) 生态系统需要保持软件占用空间小，因此一个服务同时捕获日志和指标是更优选的。因此，Fluent Bit 不仅捕获日志，还捕获 CPU、内存和存储使用情况等本地指标，这是有意义的。

将所有这些数据源汇集在一起推动了运维监控的简化，从而实现了快速普及并证明了其颠覆性。[Fluent Bit对OTel标准的支持](https://chronosphere.io/learn/observability-pipeline-opentelemetry-fluent-bit/)及其在OTel生态系统内工作的能力不需要任何根本性的改变，尽管它们推动了其部分实现的一些升级。在某些方面，这些升级使Fluent Bit之前已经在做的事情正式化了。通过这种对齐，[Fluent Bit已做好充分准备来支持](https://thenewstack.io/whats-driving-fluent-bit-adoption/) OTel标准的采用，而无需强加它们，从而使其采用更具增量性。

### 来自后续Manning书籍章节的经验

在未来的章节中，当我们开始深入探讨Fluent Bit的输入和输出功能时，我们将进一步研究其与OTel以及可观测性领域的领先产品之间的关系，例如[Prometheus](https://prometheus.io)（它帮助OTel进一步向前发展）和[Grafana](https://grafana.com/grafana)。我们还将研究致力于支持OTel标准的商业供应商，他们创建了一个快速增长的可连接监控工具生态系统。

**注意：** 如果您需要对缩略语和术语进行快速参考，可以在[此处](https://opentelemetry.io/docs/concepts/glossary)找到一个方便的词汇表。此外，附录B列出了几个优秀的资源。（[*下载书籍*](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/) *以查看附录 B。*）

## OTLP和OTel如何协同工作

OTel 的核心是[OpenTelemetry协议](https://opentelemetry.io/docs/specs/otel/protocol/) (OTLP)，它详细说明了遥测数据的数据结构、编码和传输。

目前，[OTLP支持使用远程过程调用 (gRPC) 进行传输](https://betterstack.com/community/guides/observability/otlp/)，其中 HTTP/2 使用 Protocol Buffer (Protobuf)，JSON 则同步使用 HTTP。OTLP提倡将 gRPC 作为首选的通信方法，将 JSON 作为降级或备用方案。

OTel作为一个项目，远不止定义OTLP。它还提供了标准中描述的功能的实现（有时被描述为参考实现），以及工具和库。

这些工具和库以多种语言实现；我们可以使用它们来帮助将逻辑注入应用程序，并快速使数据应用程序生成追踪。OTel还具有日志追加器等功能，允许日志框架使用OTLP规范发送日志。

## Fluent Bit如何融入OpenTelemetry解决方案

为了理解Fluent Bit如何融入OTel解决方案，让我们来看看Fluent Bit可以使用[OTel术语](https://opentelemetry.io/docs/concepts/components)做些什么：

*   鉴于其能够从不同来源收集[监控和可观测性](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "监控和可观测性")数据并将其转换为OTLP结构，Fluent Bit可以扮演OpenTelemetry Collector的角色。
*   因为Fluent Bit旨在分布式环境中工作，并且能够以OTLP格式将数据传递给任何其他符合OpenTelemetry的Collector（可以是Fluent Bit节点或另一个产品），我们可以将Fluent Bit描述为能够充当OTLP Exporter。

图1展示了Fluent Bit如何融入OpenTelemetry环境，它能够处理应用程序生成（无论是否借助OTel库或工具）的日志 (L)、指标 (M) 和追踪 (T)，并能够与OpenTelemetry Collector进行交互。

### Collector vs. Exporter：为Fluent Bit选择合适的角色

因为OTel提供了Collector和Exporter功能的实现，所以将[Fluent Bit称为OpenTelemetry Collector或OpenTelemetry Exporter可能会引起混淆](https://devopscon.io/blog/observability-monitoring/fluentbit-otel-k8s/)。标准本身叫做OTLP，因此将Fluent Bit称为符合OTLP更清晰，即使它不那么明显地说明我们可能[部署Fluent Bit](https://thenewstack.io/how-to-deploy-fluent-bit-in-a-kubernetes-native-way/) 来执行的任务。

此外，OpenTelemetry社区内部对该项目自身实现的 Collector（称为 OpenTelemetry Collector）与其他该功能实现之间的差异存在一些敏感性。我们倾向于将 Fluent Bit 描述为 OTLP Collector（毕竟，协议遵从性是 Collector 功能的关键），并减少 CNCF 项目之间的歧义。

[![Fluent Bit与OpenTelemetry的关系，应用程序生成OTel日志、指标和追踪，Fluent Bit促进它们传输到符合OTel的聚合或处理点。应用程序可以直接或通过OTel组件发送OTLP数据，我们可以将数据路由到其他OTel服务或分析工具。](https://cdn.thenewstack.io/media/2025/10/a1d98481-image1.png)](https://cdn.thenewstack.io/media/2025/10/a1d98481-image1.png)

图1. Fluent Bit与OpenTelemetry的关系，应用程序生成OTel日志、指标和追踪，Fluent Bit促进它们传输到符合OTel的聚合或处理点。应用程序可以直接或通过OTel组件发送OTLP数据，我们可以将数据路由到其他OTel服务或分析工具。

### **Protocol Buffers (Protobuf)**

Protocol buffers 是 OTel 使用的 gRPC 的一项关键技术。Protocol buffers 具有简洁定义的模式，与 Protobuf 工具配合使用可生成用于发送和接收有效载荷的代码。定义良好的模式允许工具创建生成压缩二进制有效载荷表示的代码。这种模式既是优势，也可能是潜在的限制。

优势在于高效的有效载荷传输。缺点是模式更改会影响提供者和消费者，并使实现容忍读取器集成模式更具挑战性。此外，鉴于 Protobuf 生成的有效载荷是压缩的二进制格式，将其注入能够进行转换的任何通信中间件会更加困难。附录 B 中包含了指向 OTel、Protobuf 和相关技术的链接。

## 展望未来：进一步探索Fluent Bit和OTel

随着我们深入阅读《[Fluent Bit与Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/)》一书（可在[此处](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/)下载完整版），我们将更深入地研究Fluent Bit和OpenTelemetry如何执行不同的功能。请注意，在Fluent Bit v3之前，OpenTelemetry协议支持仅限于HTTP和JSON。版本3带来了增强功能，支持HTTP/2，使Fluent Bit能够使用gRPC。这反过来意味着[Fluent Bit可以提供一个完全符合OTLP的实现](https://chronosphere.io/resource/getting-started-with-fluent-bit-and-open-source-telemetry-pipelines/)，而无需利用降级到HTTP和JSON的功能。