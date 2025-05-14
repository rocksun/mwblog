<!--
title: Grafana的eBPF Beyla的未来取决于OpenTelemetry
cover: https://cdn.thenewstack.io/media/2025/05/bd7a218b-osarugue-igbinoba-t_yhxpigu78-unsplash.jpg
summary: Grafana 将 eBPF Beyla 捐赠给 OpenTelemetry，旨在推进基于 eBPF 的自动插桩。此举将扩展 OpenTelemetry 的遥测能力，实现内核级数据采集，并与 Pyroscope 集成实现持续 profiling。OpAMP 协议增强采样和成本控制，提升可观测性效率。
-->

Grafana 将 eBPF Beyla 捐赠给 OpenTelemetry，旨在推进基于 eBPF 的自动插桩。此举将扩展 OpenTelemetry 的遥测能力，实现内核级数据采集，并与 Pyroscope 集成实现持续 profiling。OpAMP 协议增强采样和成本控制，提升可观测性效率。

> 译自：[Grafana's eBPF Beyla Future Hinges on OpenTelemetry](https://thenewstack.io/grafanas-ebpf-beyla-future-hinges-on-opentelemetry/)
> 
> 作者：B Cameron Gain

西雅图 – 大约六个月前，[Grafana](https://thenewstack.io/why-grafana-needs-opentelemetry/) 意识到其 [eBPF](https://thenewstack.io/what-ebpf-means-for-observability-vs-security/) 开源 Beyla 项目更适合通过 [OpenTelemetry 项目](https://thenewstack.io/opentelemetry-whats-new-with-the-second-biggest-cncf-project/) 推广自动插桩。因此，Grafana 决定将 [Beyla](https://thenewstack.io/wp-admin/post.php?post=22724475&action=edit) 捐赠给 OpenTelemetry 项目，该项目于 2021 年获得 [CNCF](https://cncf.io/?utm_content=inline+mention) 孵化状态。

Grafana Labs 希望，此次捐赠将扩展 Beyla（现在的 eBPF [OpenTelemetry](https://github.com/open-telemetry)），使其成为推进 eBPF 覆盖范围的最佳方式，适用于只有 eBPF 才能提供的那些类型的指标，同时通过更广泛的社区扩大其影响。

与 Grafana 对 [Prometheus](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/)（CNCF 的第二古老项目）的管理和捐赠类似，eBPF OpenTelemetry 被认为在遥测数据的扩散中发挥着更广泛的作用，这要归功于 eBPF，这些数据一直延伸到内核，并扩展到整个网络。

eBPF 已经成为一种从内核收集洞察的安全方法。它的可靠性引起了可观测性社区的广泛兴趣。一个强大、基于 eBPF 的自动插桩解决方案，与 OpenTelemetry 的其余部分无缝集成，一直是长期的目标。

> 持续 profiling 对于 [@opentelemetry](https://twitter.com/opentelemetry) 和开源 Pyroscope 来说意义重大，但与今天在[@grafana](https://twitter.com/grafana)保护伞下的版本相比，以前只是一个“hack 版本”，Ryan Perry 在 GrafanaCon 2025 上说。[ @thenewstack](https://twitter.com/thenewstack)[pic.twitter.com/rBHGYx8SXT](https://pic.twitter.com/rBHGYx8SXT)
> — BC Gain (@bcamerongain),May 9, 2025

同时，在 [GrafanaCon](https://grafana.com/events/grafanacon/) 上，[Ryan Perry](https://www.linkedin.com/in/ryanaperry/) 在题为“为什么你应该关心持续 profiling 以及如何开始在 Grafana 中使用 Profiles Drilldown”的演讲中，描述了 [Pyroscope](https://pyroscope.io/) 使用 eBPF 支持持续 profiling 的能力。Ryan Perry 是一位工程总监，他说 profiling 是 OpenTelemetry 开发中的一个关键要素。pyroscope.ebpf 组件为当前主机配置一个 eBPF profiling 作业。收集的性能 profiles 将转发到 forward_to 中传递的接收器列表中。

Perry 说，通过 OpenTelemetry 访问 Pyroscope 数据库中的关键 profiling 指标正变得更加集成，因为查询对于 profile 详细信息变得更加标准化和强大。Perry 也是持续 profiling 工具提供商 [Pyroscope 的 CEO 兼联合创始人，Grafana Labs 于 2023 年收购了该公司](https://grafana.com/blog/2023/03/15/pyroscope-grafana-phlare-join-for-oss-continuous-profiling/)。

根据 Grafana 的文档，其他 Grafana eBPF 项目包括 Grafana Alloy，这是一个轻量级的、一体化的收集器，可以收集、转换和传输可观测性数据。它通过 beyla.ebpf 和 pyroscope.ebpf 等组件支持基于 eBPF 的 profiling 和自动插桩。beyla.ebpf 组件是 Grafana Beyla 的一个包装器，它使用 eBPF 自动检查应用程序可执行文件和操作系统网络层，并捕获与 Web 事务相关的跟踪 span 以及 Linux HTTP/S 和 gRPC 服务的 RED 指标。

Grafana 的开源 Beyla 项目通过 eBPF 提供跟踪，这是为 [遥测](https://thenewstack.io/unified-telemetry-observability-the-future-of-data-management/) 收集跟踪的另一种方式。它的开发与 OpenTelemetry 项目的 profiler 的开发并行，Grafana Labs 作为主要贡献者，深入参与了 profiler 的开发。从一开始，该 profiler 就对用户有用，因为它通过扩展到代码级别来更深入地进行可观测性分析。它通过将统一流中提取的遥测数据扩展到整个网络应用程序的代码级别，从而对指标、跟踪和日志进行更深入的分析。代码被分析和存储。
OpenTelemetry 是一个注重效率和协作的实用项目。当必要时，组件会从头开始开发，但当技术上具有挑战性的功能（例如基于 eBPF 的分析器或自动插桩）已经存在于另一个组织成员的工作代码中，并且共识认为它是一个强大的基础时，就没有必要重新发明轮子，”Grafana Labs 的项目主管兼 OpenTelemetry 的联合创始人 [Ted Young](https://www.linkedin.com/in/ted-young) 在 Grafana Labs 的年度用户大会 GrafanaCon 的场边告诉我。“当它们服务于项目目标时，鼓励利用可用的捷径。这种方法有时会限制采用新的可观测性形式的努力，特别是当插桩的成本过高时。”

没有人希望必须为每种语言单独重新编译代码和应用程序。正如 Young 所描述的那样，总是会寻找捷径。在某些语言中，例如 [Java](https://thenewstack.io/introduction-to-java-programming-language/)，有效的捷径已经存在了很长时间。例如，Java agent 模式非常成熟，允许 OpenTelemetry 的 Java agent 在不需要任何代码更改的情况下运行——只需部署即可，Young 说。

然而，对于许多其他语言来说，情况并非如此。虽然在 [Python](https://thenewstack.io/python/) 中存在一些自动插桩，但它缺乏 Java 的形式化和成熟度。“在像 JavaScript 和 [Go](https://thenewstack.io/introduction-to-go-programming-language/) 这样的语言中，传统的基于 agent 的解决方案几乎不存在，但仍然需要从系统中提取高质量的数据，而无需修改代码，”Young 说。

在 Grafana Labs，大约一年前也发现了对基于 eBPF 的自动插桩的类似需求。该组织开始独立开发这样的解决方案，其目的是使其与 OpenTelemetry 对齐，作为主要数据源。从一开始，目标就是确保与 OpenTelemetry 数据标准的兼容性。这项工作促成了一个名为“Beyla”的项目，这是 Grafana Labs 内部的 eBPF 计划。该解决方案与 OpenTelemetry 的目标非常吻合，从而产生了将其捐赠给社区以促进供应商中立的开发并鼓励更广泛采用的想法。

## 巨大的认知

依靠受信任的供应商中立的 OpenTelemetry 直接从内核提取指标，将通过 eBPF 而不是通过供应商（在本例中为 Grafana）将钩子扩展到整个网络中连接的运行时。对于 OpenTelemetry 的目标，eBPF OpenTelemetry 将吸引更广泛的采用和贡献，因为该项目可能会扩展成为使用 eBPF 自动插桩提取指标的事实上的方式。

“[Nikola Grcevski](https://www.linkedin.com/in/nikola-grcevski-16796717/) 在一篇[博客文章](https://grafana.com/blog/2025/05/07/opentelemetry-ebpf-instrumentation-beyla-donation/?utm_source=chatgpt.com)中写道：“例如，Beyla 可能包含与 Grafana Cloud 轻松集成或与 Grafana Alloy 集成的功能，Grafana Alloy 是我们的 OpenTelemetry Collector 发行版，内置 Prometheus 管道并支持指标、日志、追踪和分析。”

“eBPF 采用的障碍之一是认知。尽管 eBPF 被设计为一种安全高效的内核级技术，但 eBPF 的底层特性引起了人们的担忧，”Young 说。“然而，当这项技术在像 OpenTelemetry 这样受信任的、供应商中立的倡议下被采用和开发时，这些担忧会被社区中建立的信任所缓解。”

## eBPF 用于安全和性能

以前已经存在 eBPF 的替代方案，但由于 eBPF 与其他代码相比具有隔离的设计（从技术上讲，它确实存在于 Linux 内核代码中，但存在于外层），因此 eBPF 消除了许多安全问题。用于可观测性的底层系统钩子的概念并不新鲜。然而，之前的尝试通常涉及引入风险的黑客行为。尽管公司尽了最大努力来保护它们，但这些解决方案本质上是不安全的。那些早期尝试的遗留问题仍然存在，导致了怀疑。随着对安全性的日益关注，建立信任变得至关重要。自动插桩应与手动插桩和更广泛的 OpenTelemetry 生态系统干净地集成，从而生成规范化、统一的数据。

分析是基于 eBPF 的插桩的一个有希望的领域。作为一种自动插桩形式，分析提供了不同的视角和数据集。将分析与 OpenTelemetry 中的 eBPF 技术集成可以产生强大的见解，特别是随着 OpenTelemetry 的分析能力成熟，Young 说。
“出于这些原因，将 eBPF 工作孤立起来毫无意义，”Young 说。“一种共享的、统一的社区方法比保留专有的、Grafana 特定的解决方案更有价值。围绕通用 eBPF 策略的融合使所有利益相关者受益。”

## OpAMP 增强功能

除了 profiling 和 eBPF 之外，另一个令人兴奋的领域是 OpenTelemetry 控制平面协议，即 [OpAMP](https://opentelemetry.io/docs/specs/opamp/)，Young 说。“采样和成本控制在遥测中至关重要，尤其是在大规模情况下。理想情况下，负责数据分析的工具也应该管理数据的收集方式，”他说。“这使得能够直接由了解分析需求的系统做出关于采样和成本优化的更明智的决策。”

手动配置采样参数通常是无效的。最佳值取决于系统行为，而系统行为会随着时间的推移而变化，Young 说。因此，使后端系统能够动态管理收集器和 SDK 提供了一种细致且自适应的方法。OpAMP 的开发就是为了支持这种能力，他说。

“在 Grafana Labs，Grafana Cloud 中的 fleet management 和 adaptive telemetry 等解决方案证明了这一原则，”Young 说。“下一步是将 adaptive telemetry 扩展到 Alloy 等环境，并通过使用 OpAMP 等协议的 fleet management 将其更深入地集成。”