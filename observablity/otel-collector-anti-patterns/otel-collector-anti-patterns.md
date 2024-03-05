
<!--
title: OpenTelemetry Collector反模式
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
-->

[OpenTelemetry Collector](https://opentelemetry.io/docs/collector) 是我最喜欢的 OpenTelemetry (OTel) 组件之一。它是一个灵活且强大的数据管道，允许您从一个或多个来源摄取 OTel 数据，对其进行转换（包括批处理、过滤和屏蔽），并将其导出到一个或多个可观测后端进行分析。它与供应商无关。它具有可扩展性，这意味着您可以为其创建自己的自定义组件。有什么不喜欢呢？不幸的是，就像许多现有的工具一样，它也很容易养成一些坏习惯。

> 译自 [OpenTelemetry Collector Antipatterns](https://opentelemetry.io/blog/2024/otel-collector-anti-patterns/)，作者 Adriana Villela 。

## 反模式

### 1. Collector 部署模式使用不当

仅仅使用 Collector 是不够的。还取决于你的 Collector *如何* 在你的组织中部署。没错 - Collectors，复数。因为一个通常不够。

Collector 有两种部署模式：代理模式和网关模式，两者都是必需的。

在 [代理模式](https://opentelemetry.io/docs/collector/deployment/agent/) 中，Collector 与应用程序并排放置，或与应用程序位于同一主机上。

![](https://opentelemetry.io/blog/2024/otel-collector-anti-patterns/otel-collector-agent.png)

在 [网关模式](https://opentelemetry.io/docs/collector/deployment/gateway/) 中，遥测数据被发送到负载均衡器，然后负载均衡器确定如何在 Collector 池中分配负载。因为你有一个 Collector 池，所以如果该池中的一个 Collector 发生故障，池中的其他 Collector 之一可以接管。这可以保持数据流向你的目标，而不会中断。网关模式通常按集群、数据中心或区域部署。

![](https://opentelemetry.io/blog/2024/otel-collector-anti-patterns/otel-collector-gateway.png)

那么你应该使用哪一个呢？代理和网关都使用。

如果你正在为你的应用程序收集遥测数据，请将 Collector 代理与你的应用程序并排放置。如果你正在为基础设施收集数据，请将 Collector 代理与你的基础设施并排放置。无论你做什么，都不要使用单个 Collector 收集所有基础设施和应用程序的遥测数据。这样，如果一个 Collector 发生故障，你的其他遥测收集将不受影响。

然后可以将 Collector 代理的遥测数据发送到 Collector 网关。因为网关位于负载均衡器之后，所以你没有导出遥测数据（通常到你的可观测性后端）的单点故障。

**要点**：拥有正确的 Collector 部署配置以将数据发送到你的可观测性后端，可确保你的遥测收集基础设施具有更高的可用性。

### 2. 不监控你的 Collector

部署多个 Collector 代理和 Collector 网关很好，但这还不够。了解你的某个 Collector 何时出现故障或数据何时丢失不是很好吗？这样，你可以在事情开始升级之前采取行动。这就是监控你的 Collector 非常有用的地方。

但是如何监控 Collector？OTel Collector 已经发出 [用于其自身监控的指标](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/monitoring.md)。然后可以将这些指标发送到你的可观测性后端进行监控。

### 3. 未使用正确的 Collector 发行版（或未构建自己的发行版）

OpenTelemetry Collector 有两个官方发行版：[Core](https://github.com/open-telemetry/opentelemetry-collector) 和 [Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib)。

Core 发行版是 OTel 开发人员开发和测试 Collector 的精简发行版。它包含一组基础 [扩展](/docs/collector/configuration/#service-extensions)、[连接器](/docs/collector/configuration/#connectors)、[接收器](/docs/collector/configuration/#receivers)、[处理器](/docs/collector/configuration/#processors) 和 [导出器](/docs/collector/configuration/#exporters)。

Contrib 发行版供非 OTel 开发人员进行实验和学习。它还扩展了 Core 发行版，并包括由第三方（包括供应商和个人社区成员）创建的组件，这些组件对整个 OpenTelemetry 社区很有用。

Core 和 Contrib 本身都不打算成为你的生产工作负载的一部分。仅使用 Core 本身过于精简，不适合组织的需求。（尽管它的组件绝对是必需的！）虽然许多 OpenTelemetry 从业者在其各自的组织中部署 Contrib，但它有许多组件，你可能不需要每个导出器、接收器、处理器、连接器和扩展。这将是过度的，你的 Collector 实例最终会变得不必要地臃肿，从而可能增加攻击面。

但是，如何挑选和选择您需要的组件？答案是构建您自己的发行版，您可以使用名为 [OpenTelemetry Collector Builder](/docs/collector/custom-collector/) (OCB) 的工具来实现。此外，在某些时候，您可能需要创建您自己的自定义 Collector 组件，例如处理器或导出器。OCB 允许您集成您的自定义组件，并挑选和选择您需要的 Contrib 组件。还值得一提的是，一些供应商构建了自己的 [Collector 发行版](/ecosystem/distributions/)。这些是 OTel Collector 发行版，经过精心挑选，以满足该供应商特有的 Collector 组件。它们可能是自定义、供应商开发的组件和精心挑选的 Collector Contrib 组件的组合。使用特定于供应商的发行版可确保您仅使用您需要的 Collector 组件，从而再次减少整体膨胀。

*重点：* 使用正确的发行版可减少膨胀，并允许您仅包含您需要的 Collector 组件。

### 4. 不更新您的 Collector

这个简短而有力。保持软件最新非常重要，Collector 也一样！通过定期更新 Collector，它允许您随时了解最新版本，以便您可以利用新功能、错误修复、性能改进和安全修复。

### 5. 在适当的情况下不使用 OpenTelemetry Collector

OpenTelemetry 允许您通过两种方式将遥测信号从您的应用程序发送到可观测性后端：

对于非生产系统，“直接从应用程序”发送遥测数据很好，如果您刚开始使用 OpenTelemetry，但这种方法不适合也不建议用于生产系统。

- [直接来自应用](https://opentelemetry.io/docs/collector/deployment/no-collector/)
- [通过 OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)

向非生产系统“直接从应用程序”发送遥测数据，如果你刚开始接触 OpenTelemetry 而言，是再好不过了，但对于生产系统来说，既不适合也不建议使用这种方法。[OpenTelemetry 文档建议使用 OpenTelemetry Collector](https://opentelemetry.io/docs/collector/#when-to-use-a-collector)。为什么呢？

[根据 OTel 文档](https://opentelemetry.io/docs/collector/#when-to-use-a-collector)，Collector “允许你的服务快速卸载数据，Collector 可以处理额外的操作，如重试、批处理、加密，甚至敏感数据过滤”。

查看一些其他 Collector 优势：

* Collector 可以提高应用程序发出的遥测质量，同时还可以最大程度地降低成本。例如：对 span 进行采样以降低成本，使用额外元数据丰富遥测，以及生成新遥测，例如从 span 派生的指标。
* 使用 Collector 来摄取遥测数据，可以轻松地更改为新的后端或以不同的格式导出数据。如果我们想要更改遥测的处理或导出方式，则该更改发生在一个地方（Collector！），而不是为您的组织中的多个应用程序进行相同的更改。
* Collector 允许您接收各种格式的数据，并转换为所需的导出格式。当从其他一些遥测解决方案过渡到 OTel 时，这非常方便。
* Collector 允许您摄取非应用程序遥测。这包括来自 Azure、Prometheus 和 Cloudwatch 等基础设施的日志和非应用程序指标。

话虽如此，在某些用例中，人们不希望或无法使用 Collector。例如，当从 IOT 设备在边缘收集数据时，最好将数据直接发送到其可观测性后端，而不是本地 Collector，因为该边缘上的资源可能有限。

*重点：* 一般来说，使用 OpenTelemetry Collector 为您管理遥测数据提供了额外的灵活性。

## 最后的想法

OpenTelemetry Collector 是一个用于摄取、处理和导出 OpenTelemetry 数据的强大且灵活的工具。通过充分利用它并避免这五个陷阱，您的组织可以很好地实现可观测性卓越。