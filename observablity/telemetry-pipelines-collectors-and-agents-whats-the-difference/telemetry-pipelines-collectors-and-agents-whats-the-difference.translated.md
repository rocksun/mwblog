# 遥测管道、采集器和代理：有什么区别？

![Featued image for: Telemetry Pipelines, Collectors and Agents: What’s the Difference?](https://cdn.thenewstack.io/media/2025/02/e8570450-telemetry-pipelines-collectors-agents-1024x576.jpg)

不久前，选择可观测性解决方案还很简单：你要么完全投入某个供应商，*要么*完全致力于开源。绝不可能两者兼顾。

但随着 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry) 和 [Prometheus](https://thenewstack.io/know-the-hidden-costs-of-diy-prometheus) 等标准的出现，这些严格的界限已经消失。如今，你可以将供应商解决方案与开源技术相结合，构建理想的可观测性堆栈。虽然这种灵活性非常强大，但也意味着要在不断变化和重叠的术语中摸索。

可观测性适合所有人，但当我们[甚至无法就](https://thenewstack.io/apm-vendors-are-creating-confusion-about-observability-dont-fall-for-it/)应用程序性能监控 (APM) 的定义达成一致时，理解起来可能会觉得具有挑战性。即使在可观测性领域工作了十年，无论是作为从业者还是在供应商处，我仍然会对大量新术语和概念感到困惑。有时，这让我想抓狂。

以[遥测管道](https://thenewstack.io/the-case-for-telemetry-pipelines/)为例。

当我第一次听说它时，我有很多问题：这是一个特定的产品吗？一种新的工具类别？它与我们多年来使用的采集器和代理有*什么*不同？这些问题引发了与同事的长期辩论，每个人都有自己的定义。

这让我陷入了一个研究的兔子洞——而且显然我并不孤单。Gartner 报告称，2021 年至 2023 年间，客户组织对遥测管道的咨询[增加了 500%](https://chronosphere.io/learn/what-you-need-in-a-telemetry-pipeline/)。鉴于我们有这么多人试图理解这个概念，我知道现在是时候给出一个明确的解释了。所以这是我的定义：

遥测管道是一个系统，它从各种来源收集、转换和路由遥测数据（日志、指标和追踪）到各种监控和分析工具。遥测管道不是为不同的信号管理单独的代理或采集器，而是通过统一的路由处理数据，从而提高可观测性的效率和可扩展性。

## 那么，什么是代理和采集器？

如果遥测管道的工作是收集、处理和导出遥测数据，那么代理和采集器是做什么用的？如果你的头已经开始晕了，相信我，我经历过。当我第一次开始探索遥测管道时，我想定义代理、采集器和遥测管道之间清晰、通用的区别。

但是，我越深入研究，就越意识到这些术语并不总是能完全对应于严格的定义——不同的团队和供应商以略有不同的方式使用它们。也就是说，有一个大致的参考框架仍然很有帮助。

### 代理：遥测的第一英里

代理就像你当地的邮递员——它们在源头运行，从特定的应用程序或系统收集遥测数据，并将其转发到中心位置。它们通常作为 sidecar 与应用程序一起运行或在同一主机上运行，专注于数据传递的“第一英里”。

### 采集器：中间英里的聚合器

采集器就像一个区域邮局，从多个代理（或直接从应用程序和基础设施）收集遥测数据，然后将其转发到最终目的地。采集器可以接收和路由遥测数据。

### 遥测管道：整个系统

遥测管道就像整个邮政系统，负责处理端到端的的可观测性数据。它不仅仅是转发数据，还可以根据你的需求对遥测数据进行规范化、丰富、过滤和动态路由。

## 现实世界中的遥测管道

虽然邮政服务这个比喻有助于提供一个基本的理解水平，但现实情况是，“代理”、“采集器”和“遥测管道”这些术语并没有普遍接受的、一成不变的定义。这些定义会根据上下文和实现而变化。当你理解这些术语之间的关系时，就更容易在术语丛林中穿梭——更重要的是，构建一个适合你的遥测管道。

让我们看看两个领先的开源遥测管道是如何使用这些术语的。

### OpenTelemetry Collector

[OpenTelemetry Collector 文档](https://opentelemetry.io/docs/collector/)将其描述为*“一种与供应商无关的接收、处理和导出数据的方式。”* 听起来是不是很熟悉？这是因为它与我对遥测管道的定义完全匹配。
尽管它作为一个遥测管道发挥作用，但它被称为“Collector”，这可能会让你认为它只是一个没有数据处理能力的中继站。术语的重叠还不止于此。在设置 OpenTelemetry Collector 时，你需要配置 [pipelines](https://opentelemetry.io/docs/collector/architecture/#pipelines) —— 处理日志、指标、[events](https://thenewstack.io/why-events-are-the-critical-telemetry-type-youre-missing) 或 [traces](https://thenewstack.io/distributed-tracing-is-failing-how-can-we-save-it/) 的特定数据路径。

接下来是 OpenTelemetry Collector 如何部署的问题。它可以充当代理（第一英里遥测收集）或网关（集中式处理中心）。但更棘手的是：在其他监控系统中，该网关部署被称为“collector”，而 OpenTelemetry 将该术语保留给程序本身。这种微妙但重要的不一致性迫使你重新思考这些词的含义，具体取决于你使用的生态系统。

这并非 OpenTelemetry 独有；[Fluent Bit](https://fluentbit.io/) 也具备遥测管道的所有要素——它收集、处理和路由遥测数据——但它也使用“pipelines”进行配置，并且可以部署为代理或集中式网关。在 Fluent Bit 的世界中，“pipeline”可以是整个 Fluent Bit *或*其中的各个管道。核心功能相同，但术语略有不同。

## 了解更多

我在这里分享了我对这些术语的理解，这些见解来自我的研究、实际经验以及与同事的长期对话。但总有更多东西需要学习，语言是流动的、不断发展的并且会受到解释的影响。如果您有建议或不同的看法，我很乐意听到，请在 [Mastodon](https://hachyderm.io/@paigerduty) 或 [Bluesky](https://bsky.app/profile/paigerduty.com) 上与我联系。如果您正在寻找快速参考，我们的 [Telemetry Pipeline Glossary](https://docs.chronosphere.io/pipelines/concepts) 是一个很棒的书签资源。

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)