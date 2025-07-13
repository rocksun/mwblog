<!--
title: OTel、Fluent Bit和Fluentd：有什么不同？
cover: https://cdn.thenewstack.io/media/2025/07/bfdbfc02-hummingbirds.jpg
summary: 本文介绍了 Fluentd 和 Fluent Bit 的区别与联系，以及如何选择合适的工具。Fluent Bit 轻量且更适合云原生环境，但 Fluentd 在某些用例中仍然适用。OpenTelemetry 的支持是选择的关键因素。
-->

本文介绍了 Fluentd 和 Fluent Bit 的区别与联系，以及如何选择合适的工具。Fluent Bit 轻量且更适合云原生环境，但 Fluentd 在某些用例中仍然适用。OpenTelemetry 的支持是选择的关键因素。

> 译自：[What Are the Differences Between OTel, Fluent Bit and Fluentd?](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd/)
> 
> 作者：Phil Wilkins

*本文是系列文章的一部分。另请阅读：*

- [Fluent Bit, a Specialized Event Capture and Distribution Tool](https://thenewstack.io/fluent-bit-a-specialized-event-capture-and-distribution-tool/)
- [Fluent Bit: Core Concepts](https://thenewstack.io/fluent-bit-core-concepts/)
- [是什么驱动了Fluent Bit的普及？](https://yylives.cc/2025/06/30/whats-driving-fluent-bit-adoption/)
- [Fluentd到Fluent Bit迁移指南](https://yylives.cc/2025/07/02/a-guide-to-migrating-from-fluentd-to-fluent-bit/)

在考虑是否使用 [Fluentd 或 Fluent Bit，甚至 Fluent Bit](https://chronosphere.io/fluent-bit/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform) 或 [Open Telemetry (OTel)](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 时，答案不一定非此即彼。[Fluent Bit 和 Fluentd](https://thenewstack.io/a-guide-to-migrating-from-fluentd-to-fluent-bit/) 从一开始就被设计成可以轻松无缝地通信。由于 [Fluent Bit](https://chronosphere.io/fluent-bit-academy/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform) 和 Fluentd 解决方案在内部构建有效负载的方式，我们可以获取一个 OTel 有效负载，将其包装在 Fluent 模型中，然后再解包。

回答关于 Fluentd 问题的关键在于 OTel 在微服务之外的更多用例中的采用，以及额外适配器的开发速度。

我认为，在未来几年内，新的开发将更多地基于 [Fluent Bit](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/)，因为可能考虑过 Logstash 的开发人员会转向 Elastic 应用程序性能管理 (APM) 代理。然而，生产中的解决方案的变化速度会较慢，[Fluent Bit 将取代 Fluentd](https://chronosphere.io/learn/forward-protocol-fluentd-fluent-bit/?utm_source=TNs&utm_medium=sponsored+content)。现有软件中最有可能的变更驱动因素是 OpenTelemetry 的采用。

通过在 Fluent Bit 中捕获的数据，我们可以解析半结构化内容，从事件中提取更多含义，从而允许执行更明智的下游操作。这个过程可以简单到从某些文本中提取一个值，例如 [日志](https://chronosphere.io/learn/chronosphere-logs-control/?utm_source=TNS&utm_medium=sponsored+content) 条目是否包含错误，提取一个数值供 Prometheus 使用，或者影响事件的路由。这个过程也可以像将自定义格式转换为 JSON 表示形式一样复杂。

自然的下一步是过滤事件，也许是在事件不重要时丢弃它们，或者将它们路由到一个或多个输出。我们可以将数据发送到中央日志存储库，并将事件的数值元素作为指标传递给 [Prometheus](https://prometheus.io/)。

以事件组的形式传输数据比一次传输一个事件更有效。每次对话的开始和结束都有一些小的开销，例如打开和关闭网络连接，或者打开和定位文件的结尾，然后关闭文件句柄。

缓冲或分组事件可以帮助我们权衡这些活动，这是缓冲区的作用之一，无论它们在哪里。由于缓冲区可能不是一个简单的内存结构，因此最好在过滤后执行缓冲，因此如果缓冲区涉及的管理不仅仅是我们已经存储在内存中的数据，那么我们将尽量减少工作量。

最后一步是将事件放置在某个地方。这很可能是另一个 Fluent Bit（充当 OpenTelemetry 节点或简单的日志事件处理器）或 [Fluentd](https://chronosphere.io/learn/fluent-bit-vs-fluentd/?utm_source=TNs&utm_medium=sponsored+content)（利用其更大的插件选项集合或现有的已部署监控基础设施），或者它可以是已插入的受支持的数据存储或自定义输出之一。

下图从架构的角度出发，添加了一些示例来源、目标和技术，使我们能够增强 Fluent Bit。下图强调了 Fluentd 和 OpenTelemetry 兼容工具的灵活性和兼容性，以及各种其他应用程序和技术。

您可能已经注意到，Fluent Bit 不处理数据展示或可视化。这归结为应用程序具有单一职责的理念：做好一件事并做好。对于 Fluent Bit 来说，这一件事就是将**可观测性**数据从需要观察的对象传递到允许我们可视化和分析数据的工具。

[![带有部分可用插件的 Fluent Bit 逻辑架构。](https://cdn.thenewstack.io/media/2025/07/874e9002-image.png)](https://cdn.thenewstack.io/media/2025/07/874e9002-image.png)

带有部分可用插件的 Fluent Bit 逻辑架构。

如果您熟悉 Fluentd 的架构，您会认识到，尽管使用不同的技术实现，但在这个抽象级别上，该架构非常相似。这种相似性反映了这两个解决方案之间的关系，并且是事件处理的一个简单真理。

## Fluent Bit 是 Fluentd 的子代还是继任者？

虽然 Fluent Bit 最初是 [Fluentd](https://www.fluentd.org) 的一个兄弟项目，并在 1.x 版本的后期以及作为 v2.0 的一部分提供了对 OTel 和其他功能的支持，但公平地说，它已经成长为与 Fluentd 平起平坐。这一事实引出了几个问题：

* 我需要学习 Fluentd 才能学习 Fluent Bit 吗？
* Fluentd 现在是遗留解决方案了吗？

要掌握 Fluent Bit，您无需了解任何关于 Fluentd 的知识。但是，如果您从高层次上了解 Fluentd，您会发现掌握 Fluent Bit 很容易。这两个产品之间没有依赖关系。在许多方面，虽然这两个产品有很多重叠，但它们是互补的。

Fluentd 是否是遗留技术是一个架构问题——答案始终是“视情况而定”。Fluent Bit 中包含的驱动程序和功能意味着它可以很好地融入以 [Kubernetes](https://chronosphere.io/learn/kubernetes-component-logs-fluent-bit/?utm_source=TNs&utm_medium=sponsored+content) 为中心的现代云原生生态系统，并能够满足该生态系统的所有需求，尽管某些功能目前在 Fluentd 中不可用。如前所述，Fluent Bit 具有更小、更轻的占用空间，使其适用于容器化用例。

另一个因素是 OpenTelemetry 支持。在撰写本文时，我们尚未看到为 Fluentd 配备 OTel 支持的路线图，这使得 Fluent Bit 成为部署到容器编排环境（如 Kubernetes）以及与 [Istio](https://istio.io/) 等服务一起使用的更好选择。没有什么可以阻止我们在非云原生环境中部署 Fluent Bit，这些环境通常具有更广泛的技术组合可供使用。鉴于 Fluentd 拥有的适配器数量，在可预见的未来，这种情况更适合 Fluentd。

创建自定义插件所需的技能也更容易获得；您只需要掌握 Ruby 或另一种具有内置内存管理功能的面向对象语言，如 [TIOBE 指数](https://www.tiobe.com/tiobe-index) 中所列。虽然 [WebAssembly](https://thenewstack.io/webassembly/) 可以在诸如 [Java](https://thenewstack.io/introduction-to-java-programming-language/) 和 Ruby 等语言中启用对 Fluent Bit 的扩展，但它需要额外的技能来掌握一项仍在向主流证明自己的技术。

至于 Fluentd 是否已成为历史，答案是否定的。主要供应商长期以来一直在投资和使用 Fluentd，这种投资不会轻易放弃。此外，Fluentd 和 Fluent Bit 具有不同的技术，虽然它们有一些共同的想法，但它们以不同的方式执行这些想法。

许多 Fluentd 开发的关键贡献者也在从事 Fluent Bit 的工作。这两种解决方案都在不断发展，以满足 [云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 生态系统所需的需求和创新。云原生理念和 CNCF 影响着软件世界；并非所有的云软件部署都像其他软件那样与 Kubernetes 紧密结合。

简而言之，Fluent Bit 可以做很多事情，并且可以应用于许多用例，但今天，Fluentd 在某些用例中比 Fluent Bit 更适合，反之亦然。

要了解更多关于 Fluent Bit 的信息，您可以下载整本书“[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning)”。