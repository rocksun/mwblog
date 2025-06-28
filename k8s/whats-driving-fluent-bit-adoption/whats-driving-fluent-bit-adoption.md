
<!--
title: 是什么驱动了Fluent Bit的普及？
cover: https://cdn.thenewstack.io/media/2025/06/08e33b7a-hummingbird.jpg
summary: Fluent Bit因其小巧高效、快速启动的特点，成为云原生环境的首选遥测管道。它支持OpenTelemetry，能整合日志、指标和跟踪，并与Prometheus和Grafana等主流技术无缝集成。此外，它还具备流处理能力，并可与Fluentd透明通信，方便用户扩展和迁移。
-->

Fluent Bit因其小巧高效、快速启动的特点，成为云原生环境的首选遥测管道。它支持OpenTelemetry，能整合日志、指标和跟踪，并与Prometheus和Grafana等主流技术无缝集成。此外，它还具备流处理能力，并可与Fluentd透明通信，方便用户扩展和迁移。

> 译自：[What’s Driving Fluent Bit Adoption?](https://thenewstack.io/whats-driving-fluent-bit-adoption/)
> 
> 作者：Phil Wilkins

*编者按：本文摘自 Manning 出版的“[Kubernetes 上的 Fluent Bit](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)”一书的第 1 章。另请阅读：*

Fluent Bit 已成为云原生环境的首选遥测管道。它受到数千家企业的信任，集成在所有主要云平台中，下载次数超过 150 亿次——证明了其在全球范围内的可扩展性和生产就绪性。随之而来的问题是：Fluent Bit 广泛采用的背后是什么？

使 Fluent Bit 成为重要参与者的驱动因素归结为以下几个关键因素：

* [Fluent Bit 的实现方式](https://chronosphere.io/fluent-bit/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform)完美地满足了云和云原生行业对小尺寸、高效率和快速启动的追求，从而更容易利用容器化环境的弹性。
* [Fluent Bit 配备](https://chronosphere.io/fluent-bit-academy/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform)能够满足 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/)（通常称为 OTel）的快速加速和采用，将日志处理、指标和跟踪结合在一起，以协调观察应用程序的不同方面。因此，可以标准化跨多个服务和服务器跟踪单个事务等任务。
* [Fluent Bit 提供](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/)对其他主流云原生技术的开箱即用支持，特别是那些用于支持监控和可观测性的技术，例如 Prometheus 和 Grafana 的 Loki。

我们认为还有一些其他因素在起作用，但这些趋势更难分离：

* 对流处理和流分析的思想和方法的支持已经可以在诸如 Apache [Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/)、Spark 和 Beam 等技术中看到。Fluent Bit 支持流处理思想的能力目前可能不会影响采用，但将来可能会有所作为。

流处理在云和云原生领域更为显着，但根据其处理方式，它可以为所有行业以及新旧技术领域中的[监控和可观测性](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "monitoring and observability")带来红利。Fluent Bit 的流处理能力使其更具动态性并适应发生的事情。

* 监控领域中最主要的参与者之一是 Fluent Bit 的哥哥 [Fluentd](https://chronosphere.io/learn/forward-protocol-fluentd-fluent-bit/?utm_source=TNs&utm_medium=sponsored+content)。我们可以将其优势归因于许多因素，例如在市场上起步较早，并且是 [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/) 的一部分，或者可以轻松地将新的来源和目标插入到他们的自定义集成中。

Fluent Bit 具有所有这些优势。此外，Fluent Bit 可以与 [Fluentd 部署](https://chronosphere.io/learn/fluent-bit-vs-fluentd/?utm_source=TNs&utm_medium=sponsored+content)透明地通信，从而消除或最大限度地减少 Fluentd 和 Fluent Bit 之间转换的中断，并根据需要在整个组织中混合部署两者。

## 小足迹、效率和速度

Fluent Bit 最初可能通过支持物联网 (IoT) 用例而起步，但物联网所需的特性非常适合云原生，尤其是容器和 [Kubernetes](https://chronosphere.io/learn/kubernetes-component-logs-fluent-bit/?utm_source=TNs&utm_medium=sponsored+content)。原因有二：

1. 首先，通过 Kubernetes 等编排引擎最大限度地动态扩展容器，使得当应用程序被设计为以小足迹运行时（通常在物联网设备上需要），从停滞状态到快速运行的能力变得异常容易。
2. 此外，考虑到容器本身的开销，我们可以采取任何措施来减少 CPU 和内存的消耗都是可取的。一种方法是采用预编译的本机二进制文件（有时称为提前 [AoT] 编译）。此方法消除了运行解释器层的开销（例如，在加载任何应用程序逻辑之前启动解释器的时间以及解释器的额外内存需求）。使用即时 (JIT) 编译器有助于提高性能，但仍然存在编译开销，我们可以在语言虚拟机 (VM)（例如 JVM）中看到这种开销。由于 Fluent Bit 是用 C 编写的，因此它始终被编译成二进制文件，因此没有开销。

## 快速扩展的好处

快速扩展以及资源高效和高性能的价值意味着 Fluent Bit 已被 Amazon Web Services (AWS)、Azure、Google 和 Oracle 等云提供商以及 LinkedIn 和 Lyft 等云服务提供商采用，因为这些特性可以转化为数万美元的节省。

虽然 Fluent Bit 非常紧凑，但它可以扩展以处理工作负载，并允许输入和输出在单独的线程中运行的控件。分离输入和输出操作减少了反压影响多个输入的可能性。

Fluent Bit 中的线程控制选项也具有增加吞吐量的潜力。但是，当我们在容器化环境中工作时，我们需要谨慎使用线程；我们不再有保证的 CPU 核心分配，并且更多的线程可能会导致真正的 CPU 执行比最佳情况更多的上下文切换。

## OpenTelemetry 的影响以及 Fluent Bit 与它的关系

在 OTel 之前，为指标、跟踪和日志的可观测性提供信息的主要规范来自 CNCF 内的几个标准化工作，形式为 [OpenTracing](https://opentracing.io)、[OpenCensus](https://opencensus.io/) 以及隐含地（鉴于其主导地位）Fluentd，以及通过关联，Fluent Bit 的日志记录结构。

不同的标准通常需要不同的工具来捕获此类数据。Fluent Bit 始终捕获一些指标数据；物联网生态系统需要保持软件足迹较小，因此最好使用一个服务同时捕获日志和指标。因此，Fluent Bit 不仅捕获日志，还捕获本地指标（如 CPU、内存和存储使用情况）是有意义的。将所有这些数据源汇集在一起推动了运营监控的简化，从而实现了快速采用，并已被证明具有颠覆性。

Fluent Bit 对 OpenTelemetry 标准的支持及其在 OTel 生态系统中工作的能力不需要任何根本性的改变，尽管它推动了其部分实现的升级。

在某些方面，这些升级已经正式确定了 Fluent Bit 已经做的事情。通过这种一致性，Fluent Bit 完全有能力支持 OpenTelemetry 标准的采用，而无需强制执行它们，从而使其采用可以更加渐进。

当我们开始深入研究 Fluent Bit 的输入和输出功能时，我们将进一步研究与 OpenTelemetry 以及可观测性领域领先产品（如 [Prometheus](https://prometheus.io)，它帮助推动了 OTel 的进一步发展，以及 [Grafana](https://grafana.com/grafana)）的关系。我们还将研究致力于支持 OTel 标准的商业供应商，从而创建一个快速增长的可连接监控工具生态系统。


> **注意：** 如果您需要有关首字母缩略词和术语的快速参考，您可以在[此处](https://opentelemetry.io/docs/concepts/glossary)找到方便的术语表。 

## OTel：传输遥测数据

OTel 的核心是 OpenTelemetry 协议 (OTLP)，它详细说明了遥测数据的数据结构、编码和传输。目前，OTLP 支持使用远程过程调用 (gRPC)（使用协议缓冲区 (Protobuf) 的 HTTP/2）和使用 HTTP 同步的 JSON 进行传输。OTLP 提倡使用 gRPC 作为通信的首选方法，并使用 JSON 作为降级或回退。

OTel 作为一个项目，远远超出了定义 OTLP 的范围。它还提供了标准中描述的功能的实现（有时被称为参考实现），以及工具和库。这些工具和库以多种语言实现。我们可以使用它们来帮助将逻辑注入到应用程序中，并快速获取生成跟踪的数据应用程序。OTel 还具有日志附加器等功能，允许日志记录框架使用 OTLP 规范发送日志。

要了解 Fluent Bit 如何适应开放遥测解决方案，让我们看看 Fluent Bit 可以使用 [OTel 术语](https://opentelemetry.io/docs/concepts/components/)做什么。鉴于其从不同来源收集监控和可观测性数据并将其转换为 OTLP 结构的能力，Fluent Bit 可以充当 OpenTelemetry Collector 的角色。由于 Fluent Bit 构建为在分布式环境中工作，并且可以以 OTLP 格式将数据传递给任何其他符合 OpenTelemetry 规范的收集器（可以是 Fluent Bit 节点或其他产品），因此我们可以将 Fluent Bit 描述为能够用作 OTLP Exporter。

由于 OTel 提供了收集器和导出器功能的实现，因此将 Fluent Bit 称为 OpenTelemetry Collector 或 OpenTelemetry Exporter 可能会引起混淆。标准本身被称为 OTLP，因此将 Fluent Bit 称为符合 OTLP 更清楚，即使不太明显我们可能部署 Fluent Bit 来执行的任务。

此外，在 OpenTelemetry 社区中，对于项目自身实现的收集器（称为 OpenTelemetry Collector）和该功能的其他实现之间存在一些敏感性。我们倾向于将 Fluent Bit 描述为 OTLP Collector（毕竟，协议合规性是收集器功能的关键），并减少 CNCF 项目之间的歧义。

[![Fluent Bit 可以通过其处理由应用程序生成（无论是否借助 OTel 库或工具）的日志 (L)、指标 (M) 和跟踪 (T) 的能力以及与 OpenTelemetry Collector 交互的能力来适应 OpenTelemetry 环境。](https://cdn.thenewstack.io/media/2025/06/79c9e1ea-image1a.png)](https://cdn.thenewstack.io/media/2025/06/79c9e1ea-image1a.png)

Fluent Bit 可以通过其处理由应用程序生成（无论是否借助 OTel 库或工具）的日志 (L)、指标 (M) 和跟踪 (T) 的能力以及与 OpenTelemetry Collector 交互的能力来适应 OpenTelemetry 环境。

协议缓冲区 (Protobuf) 协议缓冲区是 gRPC 的一项关键技术，OTel 使用 gRPC。协议缓冲区具有简洁定义的模式，该模式与 Protobuf 工具结合使用以生成用于发送和接收有效负载的代码。一个定义完善的模式允许该工具创建代码来创建压缩的二进制有效负载表示形式。此模式既是一种优势，也是一种潜在的约束。优势来自于高效的有效负载传输。缺点是模式更改会影响提供者和使用者，并使得实现容错读取器集成模式更具挑战性。此外，鉴于 Protobuf 生成的有效负载是一种压缩的二进制格式，因此很难注入到任何可以容纳转换的通信中间件中。 

## 使用 C、Go、WebAssembly 和 Lua 扩展 Fluent Bit

扩展 Fluent Bit 核心功能的能力非常重要。为 Fluentd 构建的大量第三方插件清楚地表明了这种需求。除了源和目标之外，还需要用于过滤等操作的小段自定义逻辑。对于输入、输出和过滤器，我们可以使用 C、Go（也称为 Golang）和 WebAssembly (WASM) 连接预编译的解决方案。我们可以使用这些解决方案来进一步增加我们对实现语言的选择并提升解耦。

由于过滤器通常需要一种更快、更简单的方法来定义小段逻辑，因此使用 [Lua 作为脚本语言](https://chronosphere.io/learn/control-your-observability-logs-with-ai-lua-and-telemetry-pipeline/?utm_source=TNs&utm_medium=sponsored+content)是有意义的。

### Fluent Bit 和流处理

将处理逻辑实现为事件流经管道的目标并不新鲜。随着软件框架的发展以支持该目标，我们看到了现在被称为流处理或流分析的内容，即复杂事件处理 (CEP)。您可以争辩说，我们已经以[服务总线](https://www.devx.com/terms/enterprise-service-bus)产品的形式存在基本的流处理很长时间了；流处理更多地与技术如何应用有关，而不是技术本身。如果您接受关于服务总线的论点，那么可以合理地断言 Fluentd 和 Fluent Bit 也提供基本的流功能。已经演变的是我们看待流处理和流分析的方式。今天，我们可以识别出流处理和分析的几个显着特征：

* 我们试图通过管道推送的大量数据是流处理的一个关键特征。Fluent Bit 对这些数据量并不陌生，但我们想要处理的量需要服务总线处理的巨大规模。此外，服务总线需要解决一定程度的复杂性，例如跨多个系统的数据完整性，这通常不是流处理的问题。
* 当我们专注于数据时，使用 SQL 几乎是处理数据的通用方法。如果我们能够使用 SQL 来表达对日志事件的检查，我们就可以使数据更容易访问。

您可以下载整本书“[Kubernetes 上的 Fluent Bit](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning)”。