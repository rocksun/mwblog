<!--
title: OpenTelemetry 采纳进展：Rust、Prometheus 及其他“拦路虎”
cover: https://cdn.thenewstack.io/media/2025/10/884f56d6-john-cardamone-nxh2zbyjc4a-unsplash-1.jpg
summary: OpenTelemetry挑战：实现复杂，Rust支持弱（追踪等仍在开发）。与Prometheus兼容改进中。Rust集成慢因现有Tokio tracing非分布式追踪且维护不足。
-->

OpenTelemetry挑战：实现复杂，Rust支持弱（追踪等仍在开发）。与Prometheus兼容改进中。Rust集成慢因现有Tokio tracing非分布式追踪且维护不足。

> 译自：[OpenTelemetry Adoption Update: Rust, Prometheus and Other Speed Bumps](https://thenewstack.io/opentelemetry-adoption-update-rust-prometheus-and-other-speed-bumps/)
> 
> 作者：B. Cameron Gain

[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 不负众望地实现了其承诺。这个用于[可观测性](https://thenewstack.io/introduction-to-observability/)的开源项目在过去几年中已经发展成为越来越多需要对应用程序进行插桩并标准化[遥测数据](https://thenewstack.io/unified-telemetry-observability-the-future-of-data-management/)的组织的事实标准。它的设计目标是让数据能够被不同的可观测性平台以及用户选择的可视化和存储系统理解。

这个领先的、[Kubernetes](https://thenewstack.io/kubernetes/) 背后的 [CNCF](https://cncf.io/?utm_content=inline+mention) 项目的贡献者们仍然积极地致力于改进 OpenTelemetry 的易用性和实现，并添加新功能。然而，OpenTelemetry 仍处于发展阶段，尚未普遍满足所有组织的需求。

持续改进的目标领域是 OpenTelemetry 对所有[编程语言](https://thenewstack.io/the-key-fundamentals-of-programming-you-should-know/)的指标、日志和追踪的支持。根据 OpenTelemetry 项目的文档，[Rust](https://thenewstack.io/rust-programming-language-guide/) 仍然是 OpenTelemetry 支持较少的语言。针对 Rust 应用程序的[追踪、指标和日志](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/)仍在开发中。OpenTelemetry 文档中列出的所有其他主要编程语言至少支持指标。这主要是由于几个因素，包括与其他常用语言相比，它大规模采用的时间相对较晚，以及指标在插桩方面替代 OpenTelemetry 已经运行良好。

## 复杂性

同时，OpenTelemetry 通常被认为实现和管理起来很复杂，这代表着大规模采用的一个重大障碍。确实，OpenTelemetry 的实现可能具有挑战性和复杂性，例如在超大型、大规模多集群和云环境中。（尽管一旦实现工作完成，OpenTelemetry 作为单一的插桩方案在实际使用中可以大大降低复杂性。）

“[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 既复杂又难以安装，” [Grafana Labs](https://grafana.com/) 的开发者项目总监 Ted Young 在伦敦的 [ObservabilityCon](https://grafana.com/events/observabilitycon/) 期间告诉我。尽管如此，Young 表示，OpenTelemetry 标准化可观测性信号（追踪、指标和日志）的核心承诺无疑满足了现实世界的挑战，特别是在指标和遗留系统领域。但 Young 指出，尽管该项目被视为“未来生存”的关键，但有几个关键领域正在产生摩擦。

对于追踪，在通过 OpenTelemetry 提取入口数据时，确保标签和属性的正确语义约定对开发人员构成了挑战。拥有数百名开发人员的大型组织必须确保语义约定保持一致。Young 表示，这种以开发人员为中心的插桩方法导致追踪中的“数据质量最差”，因为其本质上“更难做到正确”。

缺乏既定且全面的通用约定加剧了这个问题。Young 表示，虽然存在针对 HTTP 标签等标准协议的工作，但许多“非标准协议”——例如“消息传递”或较旧的“远程过程调用”——缺乏必要的约定。这些通用约定对于让可观测性后端“自动理解它所看到的内容”至关重要，从而实现“知识图谱”关联等高级功能。

## Prometheus 未受束缚

已经依赖 Prometheus 获取遥测信号的组织通常认为有必要为指标添加 OpenTelemetry。这样做通常被认为是一种风险，可能会破坏未损坏的东西，同时通过为指标实施 [Prometheus](https://thenewstack.io/prometheus-and-opentelemetry-just-couldnt-get-along/) 可能会增加环境的复杂性。OpenTelemetry 和 Prometheus 之间的兼容性问题仍然存在。

Prometheus 现在与 OpenTelemetry 很好地集成，并且仍然是生态系统的核心部分。这种竞争只是表面上的。尽管如此，Prometheus 2.0 在通过 OpenTelemetry 作为指标后端使用时带来了挑战，早期使采用复杂化。

兼容性问题可以追溯到 Prometheus 3.0 发布之前。在一个非常基本的层面，设计理念存在差异。Prometheus 内部数据格式相关的兼容性问题，特别是直方图和数据转发协议，仍然是 OpenTelemetry 的一个问题。

随着 Prometheus 3.0 的发布，已经有许多改进使得通过 OpenTelemetry 收集指标比过去显著更好、更轻松。如上所述，问题仍然存在，但工作正在进行中，在开源社区的支持下，我可以亲身证实，有很大的动力来克服这些问题，这些问题将在未来的 Prometheus 版本中得到解决。

这是 Prometheus 发挥作用的一个领域。当前的努力包括积极“重构这些标签”，使其更符合 Prometheus 和 [Mimir](https://thenewstack.io/the-great-grafana-mimir-and-cortex-split/) 定义的约定，以改进数据的结构和可整理性。

## Rust 缓慢前行

Rust 是一种较新的编程语言，与 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 甚至 [Python](https://thenewstack.io/what-is-python/) 等流行语言相比，使用起来更困难。但 OpenTelemetry 在与 Rust 兼容性方面的滞后，很大程度上是由于使用开源 [Tokio](https://thenewstack.io/using-rustlangs-async-tokio-runtime-for-cpu-bound-tasks/) 进行追踪已经运行良好。

Young 表示，Rust 已经拥有一个被广泛采用的系统是件好事。然而，Young 说，这也创造了一个“尴尬的局面”，即 OTel 社区正在讨论是否“直接采纳 Tokio tracing 作为官方”解决方案，以使 Rust 社区获得高采用率。尽管其存在局限性，并且原始开发人员缺乏推动力。

OpenTelemetry 社区在与 Rust 生态系统集成方面面临独特的难题，这源于该语言广泛采用的原生工具。Young 说：“Rust 的好处在于它有一个叫做 Tokio tracing 的东西。”“但 Tokio tracing 的问题在于它不是分布式追踪。它更像是，几乎像是，栈追踪……问题在于它们的工作方式有点不同。Tokio tracing 不做分布式追踪。”

OTel 对分布式追踪的需求与 Tokio 对栈追踪的侧重之间的技术鸿沟，又因维护和推动力不足而加剧。Young 说：“Tokio——指 Tokio 公司——他们不是一家可观测性公司，而且 Tokio tracing 看起来已经很少维护了。”“这只是一个尴尬的局面，我们可能最终会采纳 Tokio tracing 作为官方方案。”

未来集成的局面仍然缓慢而不确定。Young 说：“那边没有人负责，对吧？因为看起来没有什么推动力。”“现在对于 Tokio tracing，我感觉，哇，我们该怎么办？但那个社区正在解决这个问题。只是要弄清楚真正应该提供什么，进展很缓慢。”