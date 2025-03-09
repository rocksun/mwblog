Kubernetes 已经改变了我们部署和管理应用程序的方式，但它也引入了新的运维复杂性。随着集群规模的扩大和工作负载变得更加分布式，了解底层发生了什么是前所未有地具有挑战性。传统的监控工具常常显得不足，它们提供的日志、指标和追踪的视图是分散的，无法讲述完整的故事。

这就是 OpenTelemetry 发挥作用的地方。通过标准化跨多个信号的遥测数据收集，OpenTelemetry 实现了强大的关联和更深入的洞察。然而，手动设置和管理可观测性管道可能是一项艰巨的任务。

[OpenTelemetry Operator](https://github.com/open-telemetry/opentelemetry-operator) 应运而生，它是一种 Kubernetes 原生的解决方案，旨在简化和自动化遥测数据收集。它使工程师能够观察他们的 Kubernetes 基础设施和在其上运行的应用程序，而无需花费过多的时间在配置和维护上。

在本次深入探讨中，我们将探索：

- Kubernetes Operator 在自动化可观测性中的作用。
- OpenTelemetry Operator 的关键功能。
- Kubernetes 监控的实际示例。
- 应用程序的自动插桩。
- 部署 OpenTelemetry Collector 的最佳实践。
- 解决常见问题，例如，*“我还需要 Prometheus 吗？”*

让我们开始吧！

[什么是 Operator？](#what-is-an-operator)

Kubernetes Operator 通过使用自定义资源定义 (CRD) 自动化应用程序的部署、配置和管理，从而扩展了 Kubernetes 的核心功能。这些 Operator 封装了运维专业知识，使工程师能够以更少的人工和干预来管理应用程序。

OpenTelemetry Operator 利用 CRD 来管理 OpenTelemetry Collector，自动化应用程序的插桩，并简化遥测数据管道的处理。Operator 确保这些任务集成到您的 Kubernetes 环境中，而无需手动配置。

[OpenTelemetry Operator](#the-opentelemetry-operator)

OpenTelemetry Operator 管理 OpenTelemetry Collector、自动插桩和遥测管道的生命周期，确保跨整个集群的无缝数据处理。

OpenTelemetry Operator 的关键功能之一是管理 OpenTelemetry Collector，它负责摄取、处理和导出遥测数据。Operator 自动化了这些 Collector 的部署和配置，支持各种模式，例如 Deployment、DaemonSet 或 StatefulSet，具体取决于用例。例如，以 DaemonSet 部署的 Collector 可以捕获来自 Kubernetes 节点的指标和日志，而基于 Deployment 或 Statefulset 的设置非常适合集中处理。

Operator 还通过自动将 OpenTelemetry Agent 注入到工作负载中来简化应用程序插桩。此功能称为自动插桩，支持 Java、Python、Node.js、.NET 和 Go 等语言。它无需开发人员修改应用程序代码来集成遥测数据，而是依赖于 Pod 注释和 CRD 配置来为应用程序启用追踪、指标和日志记录。关于 Go 自动插桩需要注意的重要一点是，它利用 eBPF，并且需要您运行一个需要提升权限的 Sidecar 容器。稍后会详细介绍。

动态目标分配是 OpenTelemetry Operator 的另一个有趣功能，特别是对于使用 Prometheus 的组织。OpenTelemetry Operator 的 Target Allocator 组件将 Prometheus 的服务发现与指标抓取分离，从而将抓取目标均匀地分配到各个 Collector。这确保了可扩展性，并防止任何单个 Collector 实例过载。通过与 Prometheus CRD（如 `ServiceMonitor`）集成，Operator 将现有的基于 Prometheus 的设置与 OpenTelemetry 更广泛的功能连接起来。

[在 Kubernetes 中使用 Operator 部署 OpenTelemetry Collector 的策略](#strategies-for-deploying-opentelemetry-collectors-with-the-operator-in-kubernetes)

在收集 Kubernetes 相关的遥测数据时，以一种优化数据收集同时避免重复的方式部署 OpenTelemetry Collector 非常重要。某些遥测数据源（如 Pod 日志）需要在每个节点上都有一个 Collector，而其他遥测数据源（如集群范围的指标）应集中收集，以防止冗余数据摄取。

为了确保高效的可观测性，我们建议使用 DaemonSet 在每个节点上部署一组 Collector。这些节点级 Collector 使用 filelog 接收器处理日志，并通过 kubeletstats 接收器收集 Kubernetes 指标，并与 `k8sattributes` 处理器配对以丰富元数据。
除了这些之外，还应该将单实例收集器部署为 Deployment 或 StatefulSet，以捕获集群范围内的遥测数据。这个中央收集器使用 `k8s_cluster` 接收器和 `kubernetes_objects` 接收器来聚合高级 Kubernetes 指标。为了保持准确性并避免重复报告，此部署应限制为单个副本。

虽然 Sidecar 部署有其用例，但本指南侧重于 DaemonSet、Deployment 和 StatefulSet 模型，因为它们为大多数 Kubernetes 可观测性需求提供了效率和可扩展性的最佳平衡。

如果您想探索演示并查看在不同模式下部署 OpenTelemetry Collector 的配置，请查看以下存储库：[https://github.com/dash0hq/demo-otel-operator](https://github.com/dash0hq/demo-otel-operator)

**DaemonSet 配置**：[otel-collector-daemonset.yaml](https://github.com/dash0hq/demo-otel-operator/blob/main/otel-collector/otel-collector-daemonset.yaml)

**StatefulSet 配置**：[otel-collector-central.yaml](https://github.com/dash0hq/demo-otel-operator/blob/main/otel-collector/otel-collector-central.yaml)

*(此处使用而不是 Deployment，是因为在 Deployment 模式下运行 TargetAllocator 时存在本地问题。)*

[此存储库](https://github.com/dash0hq/demo-otel-operator/)提供了一个小型演示环境，以及如何部署收集器以捕获节点级和集群范围指标的详细示例。

[监控 Kubernetes](#monitoring-kubernetes)

OpenTelemetry Collector 提供了各种接收器来收集和处理来自 Kubernetes 环境的遥测数据。通过利用多个接收器和处理器，可以深入了解集群、节点和工作负载。

**Kubeletstats Receiver**：Kubeletstats Receiver 通过从 Kubernetes Kubelet API 中提取数据来收集节点级指标，包括 CPU、内存和磁盘使用情况。此接收器最好使用 DaemonSet 部署，确保集群中的每个节点都有一个本地收集器，以最大限度地减少延迟并减少集群范围内的网络开销。

**Kubernetes Cluster Receiver**：Kubernetes Cluster Receiver 收集集群范围的指标，例如节点状况、Pod 阶段、资源配额和 Deployment 状态。此接收器应使用单副本 Deployment 或 StatefulSet 部署，以避免跨多个节点重复收集数据。

**Kubernetes Objects Receiver**：此接收器收集 Kubernetes API 服务器对象，例如事件、命名空间和资源配额。与 Cluster Receiver 一样，它应部署在单副本 Deployment 或 StatefulSet 中，以避免冗余。

**Kubernetes Attributes Processor**：Kubernetes Attributes Processor 使用 Kubernetes 元数据（例如 Pod 名称、命名空间和标签）自动丰富遥测数据。此元数据增强了应用程序和基础设施级别遥测之间的关联，从而实现更深入的监控。

如前所述，我们建议以两种模式部署收集器 - 一种作为 `DaemonSet`，另一种作为 `Deployment` 或 `StatefulSet`。这种双管齐下的方法确保捕获节点级指标（通过 DaemonSet）和集群范围指标（通过 Deployment/StatefulSet），以进行全面的监控。下面您可以看到使用 [otelbin.io](https://www.otelbin.io/) 的 OpenTelemetry Collector 配置的可视化。

*DaemonSet 模式下的 OpenTelemetry Collector：*

*Deployment/StatefulSet 模式下的 OpenTelemetry Collector：*

通过将 OpenTelemetry 收集器分成这两种模式，您可以利用不同的 Kubernetes 组件进行数据收集 - 为监控 Kubernetes 集群和应用程序奠定坚实的基础。

[自动检测应用程序](#auto-instrumenting-applications)

手动检测应用程序以实现可观测性可能很乏味且容易出错。OpenTelemetry Operator 通过自动检测简化了此过程，该自动检测将遥测代理自动注入到您的工作负载中。

支持的语言包括 Java、Python、.NET、Node.js 和 Go。以下是如何自动检测 Java 应用程序的示例：

1. 创建一个 `Instrumentation` 资源来配置导出器和采样：

```yaml
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
metadata:
  name: java-instrumentation
  namespace: opentelemetry
spec:
  exporter:
    endpoint: http://otel-collector:4318
  propagators:
    - tracecontext
    - baggage
  sampler:
    type: always_on
```

2. 将以下注释添加到您的部署中：

```yaml
annotations:
  instrumentation.opentelemetry.io/inject-java: "true"
```

*这是最简单的方法，但是，您也可以通过命名空间/检测名称直接引用您的 Instrumentation 资源。*
当应用程序部署后，OpenTelemetry Operator 会自动将 OpenTelemetry Java agent 注入到 pod 中的所有 Java 进程中，从而实现遥测数据的自动收集。您可以浏览该存储库，查看各种受支持语言的已插桩服务的示例。

另一个值得研究的有趣参数是 `addK8sUIDAttributes`：

```yaml
spec:
  resource:
    addK8sUIDAttributes: true
```

它启用了一个可选配置，用于将 Deployment 或 Pod 等资源的唯一 Kubernetes ID (UID) 添加到您的遥测数据中。这使得在大型或高度动态的 Kubernetes 环境中，更容易关联和排除问题，因为 pod 和 deployment 可能会快速出现和消失。如果没有这个参数，您的遥测数据将只用名称进行注释，众所周知，这会使涉及分组的查询更加困难，因为您需要在查询中编码多个分组级别，例如，一个 pod 名称通常不够唯一。

另一个观察结果是，有一些特定于平台的注意事项：当容器镜像基于 Alpine Linux 时，.NET 服务需要额外的参数，并且与 Mac Silicon 不兼容。Go instrumentation 依赖于 eBPF，这会引入安全方面的权衡。如果您想了解更多关于 Go instrumentation 及其影响的信息，请参阅这篇 [博客文章](https://www.dash0.com/blog/exploring-the-opentelemetry-go-automatic-instrumentation-powered-by-ebpf-a-deep-dive)。

这种方法允许平台团队轻松地让开发人员集成可观测性，而无需付出太多努力。但是，对于更精细的遥测数据，开发人员可能需要在他们的应用程序代码中使用 OpenTelemetry SDK 手动定义额外的遥测数据。

## [Target Allocator：无需 Prometheus 即可实现类似 Prometheus 的功能](#target-allocator:-prometheus-like-capabilities-without-prometheus)

在 Kubernetes 中扩展基于 Prometheus 的监控所面临的挑战之一是在多个 Prometheus 实例之间分配抓取目标，同时确保最佳性能。OpenTelemetry Operator 通过 Target Allocator 解决了这个问题，Target Allocator 将抓取目标动态分配给 OpenTelemetry Collector，从而无需完整的 Prometheus 部署。

Target Allocator 的工作原理是利用 Prometheus 服务发现机制，同时将实际的抓取过程卸载到多个 OpenTelemetry Collector。这允许采用更分布式和可扩展的指标收集方法，减少瓶颈并确保 Collector 之间的有效负载平衡。它还使团队能够保留 Prometheus 的抓取模型，而无需运行 Prometheus 本身。

此外，Target Allocator 支持 [Prometheus Operator](https://prometheus-operator.dev/) 自定义资源，这意味着团队可以在其集群中定义 `ServiceMonitor` 和 `PodMonitor` 资源。这允许与 Kubernetes 服务和 pod 进行无缝集成，从而确保为习惯于 Prometheus 的组织提供熟悉的监控工作流程。但是，这些 CRD 默认不包含，必须单独安装，例如，通过官方 Helm chart：

这种方法确保了从 Prometheus 过渡的组织可以继续利用其现有的监控配置，同时逐步采用 OpenTelemetry 更灵活的遥测模型。

## [那么，您需要 Prometheus 吗？](#so-do-you-need-prometheus)

随着 OpenTelemetry 不断发展的功能，一个常见的问题出现了：Prometheus 仍然是必需的吗？答案取决于您的用例。

对于已经围绕 Prometheus 构建了广泛监控基础设施的组织来说，完全替换它可能不切实际。相反，OpenTelemetry 可以通过集成 Target Allocator 并使用 OpenTelemetry Collector 来处理遥测聚合，从而减轻 Prometheus 实例的压力，从而补充现有的 Prometheus 部署。

但是，对于新的部署或希望简化其监控堆栈的团队来说，OpenTelemetry 提供了一个引人注目的替代方案。通过使用 OpenTelemetry Collector 进行抓取、处理和导出指标，组织可以选择完全消除 Prometheus，或者仍然将其用作指标存储，同时仍然利用以前与它相关的强大的服务发现和指标收集功能。

最终，您是否需要 Prometheus 取决于它与您现有工作流程的集成程度以及您希望如何存储指标。

## [在 Dash0 中通过 OpenTelemetry Operator 集成试用](#try-it-out-in-dash0-with-the-opentelemetry-operator-integration)

Dash0 为 OpenTelemetry 数据提供强大的可视化、分析和调试工具。Dash0 集成中心包括一个关于设置 OpenTelemetry Operator 以实现高效数据收集的综合指南，可以在 Kubernetes 部分找到。
为了简化 Kubernetes 可观测性，我们优化了 OpenTelemetry Collector 的配置，确保提供开箱即用的坚实基础。最棒的是什么？数据收集和命名遵循 OpenTelemetry 的语义约定，使您可以无缝地利用诸如 Dash0 的 Kubernetes Pod 视图之类的功能，以获得更深入的见解。

或者深入了解您的 Kubernetes 节点：

通过本文前面讨论的自动插桩功能，您可以获得开箱即用的跟踪、日志和指标（适用于某些语言）。

总而言之，这是一个非常无缝的体验。借助 OpenTelemetry Operator，您可以为 Kubernetes 可观测性奠定坚实的基础，从而可以轻松地以最少的精力收集、处理和分析遥测数据。

## 总结

[总结](#final-words)

OpenTelemetry Operator 是 Kubernetes 可观测性的一个重大进步，它提供了一种 Kubernetes 原生的方式来管理 collectors、自动化工作负载插桩并简化遥测管道。通过降低运营复杂性并加速洞察生成，它使工程师可以专注于重要的事情 - 了解和优化他们的系统。

也就是说，虽然 Operator 功能强大，但并非没有限制。高级配置可能需要更深入地了解 OpenTelemetry Collector 组件，并且某些 Prometheus 特定的功能尚未完全复制。此外，自动插桩，特别是对于像 Go 这样的语言，仍然需要额外的设置，例如 eBPF 代理，并且存在安全方面的权衡。

尽管存在这些挑战，OpenTelemetry Operator 描绘了一个充满希望的未来，工程师可以用最少的精力插桩应用程序，而无需修改应用程序代码。无论您是设置 Kubernetes 监控、利用自动插桩还是在 Dash0 中可视化遥测数据，Operator 都为可观测性提供了灵活且可扩展的基础。

您准备好将 Kubernetes 监控提升到一个新的水平了吗？立即开始探索 OpenTelemetry Operator！

查看此[存储库](https://github.com/dash0hq/demo-otel-operator/)，以在 kind 集群上本地启动并运行 OpenTelemetry Operator。

## 考虑使用 Dash0 Kubernetes Operator 以增强功能

[考虑使用 Dash0 Kubernetes Operator 以增强功能](#consider-the-dash0-kubernetes-operator-for-enhanced-capabilities)

虽然 OpenTelemetry Operator 为 Kubernetes 可观测性提供了强大的基础，但某些组织可能会发现其功能集存在某些限制。如果您正在寻找一种增强的解决方案，该解决方案可以简化设置，同时解决自动插桩和指标收集方面的差距，那么 Dash0 Kubernetes Operator 可能值得探索。

Dash0 Operator 构建在与 OpenTelemetry Operator 相同的许多技术之上，但它专注于以最少的配置提供开箱即用的遥测数据收集。它通过预配置 OpenTelemetry Collectors、处理与 Dash0 后端的身份验证以及为受支持的运行时提供更深入的集成来简化可观测性。除了自动日志收集和 Kubernetes 指标之外，Dash0 Operator 还通过支持 PersesDashboard 和 PrometheusRule 资源来扩展其功能，从而实现监控即代码方法。

通过支持 PersesDashboard，团队可以将仪表板定义和管理为代码，从而确保跨环境的指标可视化效果一致。同时，PrometheusRule 集成允许团队直接在 Kubernetes 中创建和管理警报规则，从而确保监控和警报配置已进行版本控制并无缝集成到 CI/CD 工作流程中。

对于希望更轻松地开始使用 OpenTelemetry，同时受益于扩展功能的团队，Dash0 Kubernetes Operator 提供了一个用于收集、管理和可视化遥测数据的统包解决方案。了解有关 Dash0 Kubernetes Operator 及其如何增强 OpenTelemetry 可观测性的更多信息：[Dash0 Kubernetes Operator Documentation](https://www.dash0.com/documentation/dash0/dash0-kubernetes-operator)。