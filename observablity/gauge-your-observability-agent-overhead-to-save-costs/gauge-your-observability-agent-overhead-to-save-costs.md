<!--
title: 如何量化开销以节省可观测性Agent成本
cover: https://cdn.thenewstack.io/media/2024/01/7c6e63f2-pressure-3160582_1280-1024x576.jpg
-->

可观测性Agent在运行时可能会消耗大量资源。为避免Agent程序占用过多资源导致不必要的额外成本，可以通过监控Agent自身的资源占用情况，确保其资源消耗维持在合理范围内。

> 译自 [Gauge Your Observability Agent Overhead to Save Costs](https://thenewstack.io/gauge-your-observability-agent-overhead-to-save-costs/)，作者 B. Cameron Gain 是 ReveCom Media 的创始人兼首席分析师。 他对计算机的痴迷始于20世纪80年代初，当时他黑掉了太空侵略者控制台，在当地视频游戏厅每天玩了一天只需25美分。 然后...

我们最近[看了](https://thenewstack.io/how-the-opentelemetry-collector-scales-observability/) [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) 如何用作过滤器来监控遥测数据。当涉及到多个应用程序或微服务时，它适用，特别是出于安全考虑。因此，[OpenTelemetry Collector 属于可观测性Agent的类别](https://thenewstack.io/how-the-opentelemetry-collector-scales-observability/)。可观测性Agent，比如 OpenTelemetry Collector，包括 Fluent Bit、Vector等。

可观测性Agent在可观测性的[工作机制中起着关键作用](https://thenewstack.io/how-to-enable-critical-work-management-outside-of-devops/)。它们[处理数据传输](https://thenewstack.io/lightsteps-opentelemetry-extension-helps-make-lambda-telemetry-data-more-accessible/)，以确保遥测数据能准确传输。Agent通常提供数据收集、数据处理和数据传输，在[监控系统性能](https://thenewstack.io/sentrys-front-end-performance-monitoring-pinpoints-sluggish-api-calls-and-database-queries/)方面发挥关键作用。它们帮助识别未知问题，以便排除并缓解性能问题，在问题出现之前。这是可观测性功能的黄金标准。

通过这种方式，[当用于数据收集时](https://thenewstack.io/acryl-data-unveils-data-observability-capabilities-adds-funding/)，可观测性Agent可收集从一个或多个源发送给它的数据。除了接收数据之外，它还会将数据发送到端点，例如用于 Grafana 面板的可视化。借助它，可以配置收集某些类型的日志、[跟踪和指标以进行可观测性](https://thenewstack.io/thundra-brings-observability-tracing-to-continuous-integration/)。

最初，如果您已经在部署[向可观测性平台直接发送](https://thenewstack.io/acryl-data-unveils-data-observability-capabilities-adds-funding/)遥测数据的已检测应用程序，则可以选择不使用可观测性Agent。当监控无法检测的应用程序时，收集器很有用。由于这也是一个非常常见的用例，当监控无法检测的应用程序时，收集器也很有用，谷歌软件开发人员 [Braydon Kains](https://github.com/braydonk) 告诉 The New Stack。

> 谷歌云的 @RageCage64_ 在 Observability Days 上关于如何衡量您的可观测性Agent性能，@KubeCon_ @CloudNativeFdn @nybooks pic.twitter.com/wGAcUdsXxf
> 
> — BC Gain (@bcamerongain) November 6， 2023

如果没有可观测性收集器功能，您需要为这些功能单独配置每个后端或用户监控，这可能很麻烦。相反，可观测性收集器充当所有微服务的单个终端点，通过收集器促进的[统一点简化了对应用程序和微服务的访问](https://thenewstack.io/gravitational-becomes-teleport-launches-a-unified-access-plane/)。利用可观测性Agent作为收集器，您可以集中查看和管理微服务，在 Grafana 等平台上提供统一的视图。虽然 Grafana 提供了某些不使用 OpenTelemetry 收集器的替代方案，但收集器极大地简化了此过程。

然而，可观测性Agent可能会消耗大量资源。为了解决这个问题，它们本身也可以或正在被监控，以确保它们不会过度消耗资源，从而避免不必要的成本。换句话说，OpenTelemetry Collector、Fluent Bit、Vector 等在实现其卓越成果的同时，都展现出了强大的鲁棒性和执行各种任务的能力，但它们的相对性能可能有所不同。

## 资源挑战

最受欢迎的Agent中大多数都有[从 Kubernetes API 获取元数据](https://thenewstack.io/gitlab-updates-kubernetes-agent-for-experts-compliance-edge-use-cases/)以丰富日志和数据的 Kubernetes 过滤器和处理器。正如谷歌软件开发人员 [Braydon Kains](https://github.com/braydonk) 在他自己的 KubeCon + CloudNativeCon 演讲“[多大的开销如何评估可观测性Agent性能](https://www.youtube.com/watch?v=BIaftvtFPHg)”中所说，除了 OpenTelemetry 之外，[Fluent Bit](https://fluentbit.io/) 和 Vector 也越来越受欢迎。“每个Agent也都有构建自定义处理的方法，如果可用的默认值不符合您的需求，”Kains 在会议[结束后](https://thenewstack.io/this-week-in-programming-in-search-of-the-virtual-conference-stack/)对 The New Stack 说。

“这方面的最大挑战在于，在每秒[处理兆字节数据的流水线](https://thenewstack.io/leaky-data-pipelines-uncovering-the-hidden-security-risks/)上做任何事情都会对您的开销产生乘法效应。特别是对于正则表达式日志或 JSON 日志解析，其影响会迅速增长，”Kains说。“如果您无法足够快地发送数据，我强烈建议增加工作程序数量或利用Agent的线程实现(如果可能)。”

Kains 说，导出是流水线中唯一可以轻松并行化的步骤。大多数后端可以处理时间戳略微无序，而 Fluent Bit 提供的一个特性是，例如，设置 8 个工作程序，创建一个包含 8 个同时发送数据的工作程序的线程池。Kains 说，这可以通过[将数据分派到](https://thenewstack.io/databand-observability-for-data-pipelines/)线程池并让工作程序之一处理较慢的部分，显着提高流水线的效率，以防默认进程不足。

## 如何测试

Kains 说，组织通常需要独立确定哪个Agent最适合它们以及预期的开销。“唯一的方法是尝试运行它。如果您可以复制生产环境，安装Agent，配置它并监控指标，”Kains说。“这是得到答案的最佳方式。”

如果复制生产环境具有挑战性，Kains 建议考虑使用日志生成器或抓取 Prometheus 等[测试工作负载](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/)。AWS 的 LogBench 是一个用于测试日志流水线的好的日志生成器。对于 Prometheus 抓取，设置一个具有文本抓取副本的模拟服务器。“如果您预计高基数场景，特别是对于数据库指标，强制高基数情况以对Agent的性能进行压力测试。如果您对评估结果不满意，请考虑减少工作或卸载工作以减少资源使用。聚合节点和后端处理也可以帮助管理资源使用，”Kains 说。“如果遇到不可接受的性能或发现回归，请为维护人员开启问题，其中包含复制问题的详细信息以及相关的性能数据，比如图表、CSV、Linux perf 报告或 [pprof 配置文件](https://github.com/google/pprof)。”

## 谷歌公司内部

Kains 的团队在谷歌使用谷歌云运维，它合并了两个Agent，使用 Fluent Bit 进行日志收集，使用 OpenTelemetry 收集指标和跟踪。在幕后，团队维护了一个中央配置层，为 OpenTelemetry 和 Fluent Bit 生成配置。这些配置经过优化，主要适用于虚拟机上的用户，例如普通虚拟机，通过 OpenTelemetry 确保高效的指标收集。

Kains 说，一段时间以前，我们对查看 OpenTelemetry 日志是否可以用作 Ops Agent 以取代 Fluent Bit 感兴趣。“这将允许我们完全统一在 OpenTelemetry Collector 上，”Kains 说。“当时，OpenTelemetry 日志还不够成熟，无法承受 Fluent Bit 的吞吐量和内存使用，所以我们当时选择不推进，”Kains 说。“我们还没有更新这些基准，所以很难说今天的情况会如何。”

然而，对于大多数普通用户来说，依靠谷歌基础设施对Agent进行基准测试否则对终端用户来说将非常昂贵且过于复杂。“我运行的基准测试社区无法复制，”Kains 说。“这是我打算在新一年致力于的事情，修改我们的基准测试和性能评估策略和[技术，使其开源](https://thenewstack.io/gdal-the-open-source-technology-behind-google-maps/)，并不依赖任何谷歌专有技术或基础设施。”

然而，使用 AWS Log Bench 甚至是 [Kains 团队创建的脚本](https://github.com/GoogleCloudPlatform/ops-agent/blob/master/integration_test/soak_test/cmd/launcher/log_generator.py)，可以手动为Agent生成日志负载，并直接通过 VM 上的工具(如 [htop](https://htop.dev/))观察和比较指标，并使用可以从 /proc 或类似内容收集信息的脚本收集指标，Kains 说。“我希望创建[指南或工具，可以开源](https://thenewstack.io/a-guide-to-leveraging-open-source-licensing/)以使这种基准测试更容易访问不太技术的用户，”Kains 说。“我还没有确切的计划，但我希望在未来几个月有更多要说的。”
