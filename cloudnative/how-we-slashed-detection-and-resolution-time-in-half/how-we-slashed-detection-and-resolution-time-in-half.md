## 我们如何将检测和解决时间缩短一半

Salt Security 曾部署了 OpenTelemetry ，但发现其不足。因此，公司工程师评估了 Helios ，该工具可以为快速故障排除提供分布式跟踪的可视化。

翻译自 [How We Slashed Detection and Resolution Time in Half](https://thenewstack.io/how-we-slashed-detection-and-resolution-time-in-half/) 。

![](https://cdn.thenewstack.io/media/2023/06/905e0be7-knife-1383834_1280-1024x680.jpg)
*图片来自 Pixabay 的 Steve Raubenstine*

作为 [Salt Security](https://salt.security/) 平台工程总监，我的工作让我能够追求对云原生技术的热情，并解决复杂的系统设计挑战。我们最近解决的一个挑战与我们服务的可见性有关。

或者说，缺乏可见性。

最初，我们决定采用 OpenTelemetry ，但它并没有满足我们的需求，因为我们的系统仍然存在盲点。

最终，我们找到了一个解决方案，帮助我们精确定位服务错误，并将检测和解决问题所需的时间缩短了一半。

但是让我们先回顾一下。

## 70 个服务和每月 500 亿个 Span 的强大规模

在 Salt Security ，我们有大约 70 个基于 Scala、Go 和 NodeJS 的服务，每月生成 500 亿个 Span 。

由于 70 个服务和 500 亿个 Span都 不算小数目，我们需要帮助来获取服务之间的请求的可见性。

### 需要看到的原因

为什么我们需要看到我们的服务内部情况呢？

1. 在宏观层面上，我们需要在对系统进行更改后监控和识别问题。例如，我们需要检测过滤器、异常和任何其他问题流的信号。
2. 在微观层面上，我们需要能够精确找到问题的根源。例如，错误、操作缓慢或不完整的流程，无论它们是否支持 gRPC 或 Kafka 操作，以及它们与数据库的通信。

需要明确的是，当我们说"可见性"时，我们指的是在负载层面上深入的细节。因为数据库中的一个缓慢查询可能会拖慢整个流程，影响我们的操作和客户体验。

获取这种可见性被证明是一个难题。不仅因为服务和 Span 的数量庞大，而且因为某些流程的复杂性。

例如，一个流程可能涉及多达五个服务、三个数据库和成千上万个内部请求。

## 尝试1：OpenTelemetry 和 Jaeger

自然而然，我们首先尝试了 [OpenTelemetry](https://opentelemetry.io/) 和我们自己的 [Jaeger](https://www.jaegertracing.io/) 实例。

这个令人惊叹的开源工具集帮助我们轻松捕获应用程序和基础架构中的分布式追踪和指标。SDK、 Collector 和 OpenTelemetry 协议(OTLP) 使我们能够从所有源收集追踪和指标，并使用 [W3C TraceContext](https://www.w3.org/TR/trace-context/) 和 [Zipkin](https://zipkin.io/) 的 B3 格式传播它们。

下面是我们所采用的 OTel 设置的高级图示：

![](https://cdn.thenewstack.io/media/2023/06/28d67b53-eg1.png)

如你所见，我们使用 OTel 收集器来收集、处理和移动我们的服务的数据。然后，数据被传输到另一个开源工具 Jaeger 中进行查看。

Jaeger 非常出色，但它无法满足我们的需求。当我们遇到错误时，我们无法覆盖系统的关键部分，导致出现盲点。

## Hello，Helios

![](https://cdn.thenewstack.io/media/2023/06/4311de27-eg2.png)

就在那时，我们发现了 [Helios](https://gethelios.dev/) 。 Helios 为快速故障排除提供了分布式跟踪的可视化。我们选择了 Helios 而不是其他解决方案，因为它可以满足我们在宏观和微观层面上的需求，特别是在微观层面上表现出色。

Helios 将后端服务（如数据库和消息队列）和协议（如 gRPC、HTTP、Mongo 查询等）视为一等公民。数据被格式化以符合其所代表的内容。

例如，在查看 Mongo 数据库调用时， Mongo 查询将首先显示出来，并以 JSON 格式呈现。 HTTP 调用将被分解为头部和正文。 Kafka 主题发布或消费消息将分别显示头部和有效载荷。这种可视化使我们极易理解调用或查询为何变慢。

Helios 还提供了对云和第三方 API 调用的超高级支持。对于 Kafka ， Helios 显示其捕获的主题列表。对于 AWS，Helios 显示正在使用的服务列表，并在使用这些服务时进行突出显示。

此外，Helios 团队还基于追踪提出了一整套测试策略！当查看特定 Span 时，我们可以通过单击生成测试。还有许多其他出色的功能，如高级搜索、搜索结果中流程的预览、突出显示未关闭的追踪等等。

我们的 Helios 设置包括：

* 在我们的 Kubernetes 集群上运行的 OTel collector 。
* Helios SDK，由每个服务在任何语言中使用，并包装了 OTel SDK 。
* 两个管道：
    * OTel collector 和 Helios 之间的管道。
    * OTel collector 和 Jaeger 之间的管道，保留一天的数据。（当我们将 Span 发送到 Helios 时，我们使用 3% 的采样率；而当我们将Span发送到 Jaeger 时，采样率更高，但保留时间较短，仅用于开发目的）。
* 发送到 Helios 的 Span 的概率采样率约为 3% 。

## 实践证明一切

将 Helios 作为 OpenTelemetry 的附加层是成功的。在我们进行系统更改或尝试确定问题来源时，我们每天都使用 Helios 。

在一个案例中，我们使用 Helios 识别出一个错误的 Span ，该 Span 是由一个使用 AWS SDK 的 NodeJS 服务在请求 S3 时超时引起的。多亏了 Helios ，我们能够识别问题并迅速修复。

在另一个案例中，我们的一个复杂流程失败了。该流程涉及三个服务、三个数据库、 Kafka 和 gRPC 调用。然而，错误没有正确传播，日志也丢失了。通过 Helios ，我们可以检查追踪并立即了解问题的端到端情况。

我们还喜欢 Helios 的用户界面，它展示了每个流程中涉及的服务。

在 Helios 中，这个复杂流程的展示如下：

![](https://cdn.thenewstack.io/media/2023/06/05bcb9c3-eg3.png)

简单而易于理解，对吧？

## 结束语

我们都熟悉微服务带来的挑战，以及在错误发生时我们对其一无所知的情况。尽管有很多工具可以帮助我们理解问题的存在，但我们缺少一个能够帮助我们准确定位问题所在的工具。

通过 Helios ，我们可以查看实际的查询和有效载荷，而无需深入挖掘 Span 元数据。它们的可视化大大简化了根本原因分析。

我强烈推荐 Helios 用于故障排除。