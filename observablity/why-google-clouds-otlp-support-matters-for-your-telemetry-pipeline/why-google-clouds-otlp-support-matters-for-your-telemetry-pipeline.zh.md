[谷歌云](https://cloud.google.com/?utm_content=inline+mention)的工程师已使谷歌云可观测性（特别是 [Cloud Trace](https://cloud.google.com/trace/docs/overview)）支持 [OpenTelemetry 协议 (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/) 摄取，以实现近乎直接且更具供应商中立性的跟踪数据摄取。

既然用户可以通过遥测 (OTLP) API 使用 OTLP 发送其跟踪数据，谷歌云在许多情况下推荐这种方法，包括与 [OpenTelemetry Collector](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/) 结合使用时预期会有大量跟踪数据的用户。谷歌对该协议的采用和集成涉及大量的工程工作，并且指标和日志的 OTLP 支持路径和可用性因产品和区域而异。

与此同时，谷歌的做法与 [微软 Azure](https://news.microsoft.com/?utm_content=inline+mention) 和 [亚马逊云科技](https://aws.amazon.com/?utm_content=inline+mention) 类似。在不要求第三方工具或供应商的情况下，Azure 和 AWS 也支持 OTLP，涵盖 Azure Monitor OTel 支持、适用于 OpenTelemetry 的 AWS Distro 和 X-Ray OTLP 摄取。

## 原生 OTLP 集成的关键优势

根据 [谷歌文档](https://cloud.google.com/learn/what-is-opentelemetry) 的定义，OTLP 是一种旨在以供应商中立的方式将遥测数据从源传输到目标的交换协议，谷歌云可观测性对 OTLP 的支持在许多情况下减少了开发人员集成特定供应商导出器的先前要求。这有助于确保核心遥测管道在适当配置后，在支持 OTLP 的可观测性后端之间保持标准化并易于互操作。

谷歌将这种核心关系定义为消除了一个必要的转换步骤，将复杂性从客户端（Collector）转移到云后端。

[![显示谷歌云可观测性如何与 OpenTelemetry 协议集成的图表。](https://cdn.thenewstack.io/media/2025/10/047495d8-google-cloud-otlp-1024x576.png)](https://cdn.thenewstack.io/media/2025/10/047495d8-google-cloud-otlp-1024x576.png)

该图显示了进程内和基于 Collector 的配置如何使用原生 OpenTelemetry 协议导出器来通信遥测数据。（来源：谷歌云）

谷歌云在九月份发布的一篇由公司产品经理 [Sujay Solomon](https://www.linkedin.com/in/sujay-solomon/) 和 [Keith Chen](https://www.linkedin.com/in/keith-chen-a4640679/) 撰写的[博客文章](https://cloud.google.com/blog/products/management-tools/opentelemetry-now-in-google-cloud-observability/)，指出了 OTLP 集成用于发送跟踪数据的好处。这些好处包括：

*   **供应商中立的遥测管道：** 根据谷歌的博文，使用进程内或 Collector 的原生 OTLP 导出器消除了在遥测管道中使用特定供应商导出器的需要。
*   **遥测数据完整性：** 确保遥测数据在传输和存储过程中保持 OpenTelemetry 数据模型，而无需转换为专有格式。
*   **与您选择的可观测性工具的互操作性：** 能够将遥测数据发送到一个或多个支持原生 OTLP 的可观测性后端，而无需额外的 OTel 导出器。
*   **降低客户端复杂性和资源使用：** 能够将遥测处理逻辑（例如将过滤器应用于可观测性后端）转移到后端，减少了对自定义规则的需求，从而降低了谷歌云可观测性的客户端处理开销。

## OTel Collector 在谷歌云可观测性中的新角色

[![Cloud Trace 中跟踪探索页面的截图。](https://cdn.thenewstack.io/media/2025/10/e7da2810-google-cloud-trace-explorer-1024x576.png)](https://cdn.thenewstack.io/media/2025/10/e7da2810-google-cloud-trace-explorer-1024x576.png)

Cloud Trace 中的跟踪探索页面，其中突出显示了使用 OpenTelemetry 语义的字段。（来源：谷歌云）

谷歌云可观测性中最近增加的原生 OTLP 摄取功能，与 [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) 直接且关键相关，因为它从根本上改变了 Collector 在谷歌云可观测性中的主要作用和配置。上面描述的显而易见的好处是消除了转换步骤，因此 Collector 从谷歌云可观测性后端摄取跟踪数据所需的配置相对最少。

OpenTelemetry Collector 用于充当过滤器以监控遥测数据。它适用于涉及多个应用程序或[微服务](https://thenewstack.io/introduction-to-microservices/)的情况，特别是出于安全考虑。因此，OpenTelemetry Collector 属于可观测性代理的范畴。在此公告之前，用户可能使用 [Fluent Bit](https://thenewstack.io/fluent-bit-core-concepts/)、Vector 等可观测性代理来将跟踪数据摄取到谷歌云可观测性中。

## 可观测性代理和数据收集的作用

可观测性代理在可观测性的核心运作中发挥着关键作用。它们处理数据传输，以确保遥测数据准确传输。代理通常提供数据收集、数据处理和数据传输功能，在监控系统性能方面发挥着关键作用。它们有助于识别“未知未知”问题，从而在性能问题变得严重之前进行故障排除和缓解。这是可观测性功能的黄金标准。

这样，可观测性代理在用于数据收集时，会收集从一个或多个源发送给它的数据。除了接收数据，它还将数据发送到端点，例如用于 [Grafana](https://thenewstack.io/grafanas-cto-on-the-state-of-the-observability-market/) 面板的可视化。代理可以配置为收集某些类型的日志、跟踪和指标以实现可观测性。

最初，如果您已经部署了一个经过检测以直接向可观测性平台发送遥测数据的应用程序，您可以选择不使用可观测性代理。当监控无法进行检测的应用程序时，Collector 会很有用。

如果没有可观测性 Collector 功能，则需要单独配置每个后端或用户监控，这可能很麻烦。相反，可观测性 Collector 充当所有微服务的单一端点，通过 Collector 促进的统一接入点简化了对应用程序和微服务的访问。利用可观测性代理作为 Collector，您可以集体查看和管理微服务，在 Grafana 等平台上提供整合视图。虽然 Grafana 在没有 OpenTelemetry Collector 的情况下提供了一些替代方案，但 Collector 显著简化了这一过程。

## OTLP 对日志和指标支持的现状

应该指出的是，谷歌云的公告是关于 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 用于跟踪的。日志和指标，特别是日志，仍然是正在进行的工作，原因包括实施基于角色的访问控制 (RBAC)、合规性问题以及所需的工程工作。

目前，Azure 和谷歌云（在三大云供应商和超大规模厂商中）通过 OTLP 协议直接支持 OpenTelemetry 的指标摄取。AWS 通常使用适用于 OpenTelemetry 的 AWS Distro (ADOT) Collector。AWS 和谷歌云没有广泛可用的直接 OTLP 日志摄取功能，而 Azure 通过 OTLP 进行的日志摄取在很大程度上仍然受限。

## 谷歌简化遥测管道的策略

再次强调，正如谷歌的 Solomon 和 Chen 在他们的公司博客文章中所写，这是超大规模厂商之间整合和改进可观测性数据摄取的持续发展竞争的一部分。

他们写道，谷歌云可观测性最近的举措“是我们简化遥测管理并培育开放云环境战略的基石。我们理解，在当今复杂的云环境中，跨不同系统、不一致的数据格式和海量信息管理遥测数据可能会导致可观测性差距和运营开销增加。”

“我们致力于简化您的遥测管道，首先侧重于所有遥测类型的原生 OTLP 摄取，以便您可以无缝地将数据发送到谷歌云可观测性。这将有助于促进真正的供应商中立性和互操作性，消除对复杂转换或特定供应商代理的需求。”