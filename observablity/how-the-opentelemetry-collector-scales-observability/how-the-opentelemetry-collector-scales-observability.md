<!--
title: OpenTelemetry Collector 如何扩展可观测性
cover: https://cdn.thenewstack.io/media/2023/12/cf17a616-opentelemetry.png
-->

在KubeCon+CloudNativeCon 2023的两场演讲中展示了可观测性领域中的各种工具和服务。

> 译自 [How the OpenTelemetry Collector Scales Observability](https://thenewstack.io/how-the-opentelemetry-collector-scales-observability/)，作者 B. Cameron Gain。

你可以不使用 OpenTelemetry  Collector ，这是一个开源的可观测性框架，但你可能不想这样做，特别是在部署和监控大规模应用程序时。

尤其在涉及多个应用程序或微服务时，你可能希望使用 OpenTelemetry  Collector ，特别是出于安全考虑。

随着 OpenTelemetry 不断扩大其范围，并广泛被接受为一种使用你喜欢的可观测性工具的统一界面或组件，以满足 OpenTelemetry 标准的供应商。

OpenTelemetry Collector 是一个可观测性管道中间件，可以在规模上接收、处理和导出数据。Dynatrace 的高级软件工程师 Evan Bradley 在上个月的 KubeCon + CloudNativeCon 上与 Honeycomb.io 的高级软件工程师、开源专家 Tyler Helmuth 一起，在一场名为“OTTL Me Why Transforming Telemetry in the OpenTelemetry Collector”的演讲中解释了这一点。

“那么为什么你可能想要使用 Collector 呢？嗯，有很多原因，但第一个重要的原因是你可以在边缘进行处理——在边缘处理允许你将这项工作分配到多台机器上，这可以帮助提高管道中的数据吞吐量，” Bradley 说道。“你可以在边缘或管道的任何其他位置运行 Collector ，因为它可以部署在任何地方，可以在容器化、虚拟化或甚至作为服务环境中部署。此外，你可以在数据的原点附近或距离较远的地方进行处理，比如在管道的关键点，比如在安全网络边界的入口点。”

由于 Collector 快速而多才多艺，它被设计得能够很好地适应不同的用例，Bradley 表示。“它的设计考虑了高吞吐量和低延迟，因此不会减慢你的管道。此外，它对 CPU、内存和磁盘空间的要求也很低，” Bradley 表示。

OpenTelemetry 做了什么？

OpenTelemetry  Collector 用于收集从一个或多个源发送给它的数据。除了接收数据外，它还将数据发送到端点，例如用 Grafana 面板进行可视化。

通过配置，它可以用于收集特定类型的日志、跟踪和指标，以实现可观测性。

最初，你可以选择不使用它，特别是在使用一个监控应用程序时，该应用程序直接将所有数据收集并传输到可观测性平台，或通过 OpenTelemetry 进行传输，收集指标、日志、跟踪等。

但是，当监控多个应用程序或微服务时，采用这种方法就变得具有挑战性。没有 OpenTelemetry  Collector ，你需要为每个后端或用户监控单独配置，这可能很繁琐。

相反，OpenTelemetry  Collector 作为所有微服务的单一端点，简化了通过 Collector 提供的统一点访问应用程序和微服务。

利用这个 Collector ，你可以集体查看和管理它们，在像 Grafana 这样的平台上提供了一个统一的视图。虽然 Grafana 在没有 OpenTelemetry  Collector 的情况下提供了一些替代方案，但 Collector 显著简化了这个过程。

自定义 Collector 

根据情况，可以定制一个 Collector ，通过选择你需要的组件来适应实际情况，Bradley 表示。对于现有选项不可用的情况，所有 Collector 组件都使用相同的核心 API 编写，允许你利用这些组件添加自己的代码来完成任务，” Bradley 表示。

数据通过 Collector 的管道进行组织，由各个组件组成，每个组件处理特定的任务，Bradley 表示。 Collector 有五类组件，但在他的演讲中，接收器、处理器和导出器被涵盖了。上面的图表演示了一个示例管道，在左侧的某个点进入 Collector ，经过管道处理，并在右侧发射出去，Bradley 表示。

通过 OpenTelemetry 转换语言（OTTL），OpenTelemetry  Collector 的过滤器或处理函数可以用于过滤它接收和发送的遥测数据的种类。Helmuth 展示了 OTTL 如何支持过滤功能。

在他的演示中，Helmuth 展示了什么时候降低摄取量是有意义的，通过删除被归类为已完成的事件，因为它们被认为是不必要的，他说。

在上图中，意图是利用过滤处理器来实现决定要丢弃哪些数据的决策，该处理器基于 OTTL 条件运行。这些条件与底层遥测进行交互而不对其进行更改。过滤处理器使用 OTTL 条件选择要丢弃的数据；当条件满足时，处理器移除数据，Helmuth 说。

对于 Kubernetes 对象接收器的情况，它将以日志形式发出 Kubernetes 事件，其中这些事件存在于日志主体的嵌套映射中。

任何不按预期结构排列的主体（即不类似于 K8s 事件的主体）都将被丢弃，Helmuth 描述。在上图的顶部框中，主体是包含对象键内嵌映射的映射，因此条件未满足，数据得以保留。相反，在上图的第二个框中，主体是一个字符串，不符合预期的映射结构，Helmuth 说。

针对遥测数据收集，存在不同的替代方案。因此，OpenTelemetry  Collector 属于可观测性代理的一类。可观测性代理，如 OpenTelemetry  Collector 、FluentBit、Vector 等，“表现出高度的健壮性，并执行各种任务以实现其显著的成果，” Google 的软件开发员 Braydon Kains 在他的 KubeCon + CloudNativeCon 演讲中说道：“How Much Overhead How to Evaluate Observability Agent Performance”。

在演讲结束时，提出了关于哪个 Collector 是最佳的问题。Kains 描述了谷歌云 Ops 代理是两个代理的融合。在幕后，它将 Fluent Bit 用于日志收集，而使用 OpenTelemetry 进行指标和追踪数据的收集，他说。

团队管理一个负责为底层的 OpenTelemetry 和 Fluent Bit 生成配置的中央配置层。这些配置包括为主要在虚拟机上运行的用户（如普通 VM）量身定制的推荐优化，以便使用 OpenTelemetry 高效地收集指标，他说。

“有很多旋钮需要跟踪，对于新手来说可能很难追踪所有这些内容，” Kains 说。“我们承担了跟踪这些旋钮的责任，并试图提出在大多数一般情况下都会最优的设置。”

BC Gain 是 ReveCom Media 的创始人和首席分析师。他对计算机的痴迷始于在20世纪80年代初，在当地的视频游戏厅里，他黑客攻击了一个《Space Invaders》游戏机，以25美分的价格整天玩游戏。然后...
阅读更多有关 B. Cameron Gain 的信息
