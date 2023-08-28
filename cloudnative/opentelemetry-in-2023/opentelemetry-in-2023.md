# OpenTelemetry 2023

OpenTelemetry（OTEL）始于 2019 年，当时围绕追踪的两个主要开源项目 [OpenTracing](https://opentracing.io/) 和 [OpenCensus](https://opencensus.io/) [合并](https://medium.com/opentracing/a-roadmap-to-convergence-b074e5815289)，形成了 [OpenTelemetry](https://opentelemetry.io/) 。合并后的项目范围扩展到超越追踪，涵盖了所有的可观测性。OTEL 的使命是帮助组织交付**高质量**、**无处不在**且**可移植的**遥测数据。

翻译自 [OpenTelemetry in 2023](https://bit.kevinslin.com/p/opentelemetry-in-2023) 。[KEVIN LIN](https://substack.com/@treeandforest) 的文章写的清晰明了，可以一窥 OpenTelemetry 的各个部分。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f50d889-0872-4180-8581-2dd9bb5e4e2b_1024x1024.jpeg)

四年后，OTEL 正在兑现其承诺。到目前为止，它已经为可观测性的三大支柱（指标、日志和追踪）提供了稳定的标准，一个可以在任何环境中接收、处理和导出遥测数据的收集器，以及在所有主要编程语言中进行代码 instrument 的 SDK。它还继续扩展其范围，并引入了围绕语义约定和代理管理的额外标准。

如今，OTEL 是 CNCF 中第二活跃的项目，在受欢迎程度上仅次于 Kubernetes。其贡献者分布在所有主要的可观测性供应商中，其协议在可观测性提供者中几乎普遍被采用。

在本文中，我们将介绍 OTE L目前的情况，概述其领域内的各个项目，并谈谈它未来的发展方向。

## OTEL - 名称的含义

OTEL 主要由两种类型的项目组成：规范和实现。

规范是 OTEL 的基础。它们描述了如何捕获、收集、处理和导出遥测数据。规范往往以供应商为中心，因为它们定义了供应商必须实现的通用标准，以与 OTEL 兼容。

实现是用于处理遥测数据的特定客户端库和工具。实现往往以最终用户为中心，因为它们包含了最终用户用于 instrument 其代码的部分。

项目的稳定性通常是基于信号的。每个信号都是特定类型的遥测数据 - 在 OTEL 中，这意味着指标、日志和追踪。

今天的 OTEL 包括以下子项目：

- OpenTelemetry Specification（规范）
- OpenTelemetry SDK（实现）
- OpenTelemetry Protocol（规范）
- OpenTelemetry Collector（实现）
- Open Agent Management Protocol （规范）
- OpenTelemetry Semantic Conventions（规范）

## OpenTelemetry Specification（1.24.0）

OpenTelemetry 规范是 OTEL 的基础 - 它提供了所有其他 OTEL 标准所衍生的 API、SDK 和数据模型。

其发展的简要时间线：

- 2020年9月：追踪信号标记为稳定
- 2021年11月：指标信号标记为稳定
- 2023年4月：日志信号标记为稳定

就成熟度而言，OTEL 规范现在对所有信号都是稳定的。因为直到今年早些时候，日志信号才被认为是稳定的，所以许多 OTEL SDK 在此时仍不支持日志。

## OpenTelemetry SDK（混合）

[OTEL SDK](https://opentelemetry.io/docs/instrumentation/) 提供基于 OTEL 规范的客户端端 instrumentation。对于每个特定于语言的 SDK，每个信号都有不同的成熟度级别。

![OTEL SDK成熟度](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ae23556-1563-47d0-897f-d8bb29a40250_1162x1008.jpeg)
*[每个 SDK 的当前成熟度。](https://opentelemetry.io/docs/instrumentation/)*

## 自动 Instrumentation

根据编程语言，一些 SDK 还支持**自动 Instrumentation**。这是指 SDK 自动将信号（主要是追踪）注入到应用程序中，而无需手动仪表化代码。

自动 Instrumentation 不适用于像 Go 和 Rust 这样的编译语言。尽管如此，您仍然可以通过绕过 SDK 并使用 eBPF 和/或基于服务网格的工具来实现自动追踪注入。

## OpenTelemetry Protocol（OTLP - 1.0）

OTLP 描述了一种用于传递可观测性数据的通用传输协议。在 OTLP 中有两种认可的传输方式：使用 [protocol buffers](https://protobuf.dev/overview/) 的 http 和 [gRPC](https://grpc.io/)。

该规范被视为稳定，并且可以在任何接收、处理或导出 OTEL 数据的服务上实现。该规范由 OpenTelemetry 收集器以及诸如 Grafana 和 Datadog 等可观测性供应商的代理实现。

## OpenTelemetry Collector（0.83.0）

![OTEL收集器](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e800bba-b95c-4b74-8f37-523eee0ecedc_984x698.svg)

[OTEL Collector](https://opentelemetry.io/docs/collector/) 是一个供应商无关的代理，用于收集、转换和发送可观测性数据。

收集器包括以下组件：

- receivers：从不同源推送/拉取数据
- processors：在传输过程中转换/过滤/丰富/推导数据
- exporters：将数据发送到下游目标
- connectors：连接器既是接收器又是导出器，可以将多个管道连接在一起
- pipelines：接收器、零个或多个处理器和导出器的链条
- extensions：提供处理遥测数据之外的附加功能的组件（例如基本身份验证、健康检查等）

各种组件共同构成了一个可观测性管道，允许您从任何来源收集遥测数据，在传输过程中对其进行处理，并将其发送到任何目标。

OTEL Collector 包括两个项目，otel-collector 和 otel-collector-contrib。otel-collector 仅包含 Collector 的核心组件，主要与处理 OTLP 数据相关的逻辑。

otel-collector-contrib 是一个包含了几乎所有可观测性提供者的 exporters 和 receivers 的集合。撰写本文时，其中包括 91 个 receivers、48 个 exporters 和 24 个 processors。

建议最终用户使用 [OpenTelemetry Collector Builder](https://github.com/open-telemetry/opentelemetry-collector/tree/main/cmd/builder) 创建一个带有仅需要的组件的自定义构建版本的 otel-collector-contrib。

除了 otel-collector-contrib，像 AWS 和 Splunk 这样的供应商还提供了自己的自定义 OTEL [分发版](https://opentelemetry.io/docs/collector/distributions/)。

## Open Agent Management Protocol（OpAMP - Beta）

OpAMP 是用于远程代理管理的网络协议。这是 OTEL 的一个最近的补充，在 2022 年引入，为控制代理群提供了供应商无关的标准。这些代理可以是 otel-collector 的实例，也可以是实现 OpAMP 的供应商特定代理。

通过 OpAMP，您可以启用动态配置部署、代理更新和凭证管理等功能。

目前有一个正在进行中的 OpAMP 规范的 [Go 实现](https://github.com/open-telemetry/opamp-go)。

> 注意：如果您有兴趣通过 OpAMP 管理 OTEL 代理 - 这就是我所在的[初创公司](https://www.nimbus.dev/)正在从事的工作。

## OpenTelemetry Semantic Conventions（1.21.0）

OpenTelemetry Semantic Conventions 定义了可观测性数据的一组通用属性。它们涵盖了广泛的领域，包括云资源、数据库、异常和系统等。

语义约定被 OTEL SDK 使用，并在支持自动仪表化的 SDK 中自动应用。常见的语义允许在不同信号之间建立关联，这是我特别感兴趣的内容，其原因可以（可能会）成为一个完整博文的主题。

## 其他

OTEL 是一个庞大的项目。虽然我们涵盖了旗舰项目，但还有 OTEL 的其他部分值得特别提及：

- [OpenTelemetry Transformation Language (OTTL)](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/pkg/ottl/README.md)：一种既高性能又灵活的遥测通用转换语言 - 目前在 `otel-collector-contrib` 中进行设计和实现
- [OTEL Demo](https://opentelemetry.io/docs/demo/)：基于微服务的购物网站，演示了大多数 OTEL 功能和语言 SDK

## 最后的思考

OTEL 起初是竞争性追踪规范的合并，发展成为可观测性的行业标准。过去的四年为在供应商和工具之间构建共同基础奠定了基础。接下来的四年将展示这项工作的成果。
