# Honeycomb.io的Austin Parker：深入探讨OpenTelemetry

![Honeycomb.io的Austin Parker：深入探讨OpenTelemetry的特色图片](https://cdn.thenewstack.io/media/2024/08/81a2400e-opentelemetry-1024x683.png)
![头像](https://cdn.thenewstack.io/media/2025/01/f726e698-austin-parker-honeycomb.jpg)


OpenTelemetry是一个[框架](https://opentelemetry.io/docs/what-is-opentelemetry/)和工具包，用于创建和管理遥测数据，例如[追踪](https://opentelemetry.io/docs/concepts/signals/traces/)、[指标](https://opentelemetry.io/docs/concepts/signals/metrics/)和[日志](https://opentelemetry.io/docs/concepts/signals/logs/)。OpenTelemetry目前是[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)的[第二活跃项目](https://all.devstats.cncf.io/d/1/activity-repository-groups?orgId=1)，仅次于[Kubernetes](https://thenewstack.io/Kubernetes/)。

在盐湖城的[Kubecon+CloudNativeCon北美2024大会](https://thenewstack.io/kubecon-keynotes-wrestle-with-ai-governance-complexities/)上，我们与Honeycomb的[开源](https://thenewstack.io/open-source-in-2025-strap-in-disruption-straight-ahead/)总监[Austin Parker](https://www.linkedin.com/in/austinlparker/)进行了交流，讨论了整体[可观测性](https://thenewstack.io/Observability/)以及OpenTelemetry的现状。

Parker是[OpenTelemetry项目](https://opentelemetry.io)的联合创始人，也是OpenTelemetry治理委员会的成员。作为OpenTelemetry的社区领导者，他热情地支持和指导社区成员成为积极的贡献者。

**您能介绍一下自己吗？请简要介绍您最初接触可观测性及其与Kubernetes的交集，以及您目前在该领域的工作？**

我从OpenTelemetry成立之初就参与其中，之前从事OpenTracing的工作，目前担任治理委员会成员。我已经在可观测性领域工作了近十年——既是最终用户，试图为我的团队实施它，现在又是贡献者，试图构建下一代可观测性。同样，我在云原生领域也工作了差不多这么久，以前在Kubernetes开始兴起的时候从事平台即服务的工作，所以我对这些技术的融合很感兴趣。

**在我们深入探讨OpenTelemetry之前，您能否阐明Kubernetes可观测性与OpenTelemetry之间的关系？**

OpenTelemetry (OTel) 完全支持Kubernetes的可观测性。OTel完全支持基本的Kubernetes遥测数据，例如用于监控Kubernetes集群性能的资源利用率指标，以及用于自定义应用程序可观测性的工具库。

此外，OpenTelemetry协议(OTLP)与[Prometheus协议](https://thenewstack.io/creating-a-path-for-prometheus-success/)的完全互操作性使用户能够使用OTel利用Prometheus指标。此外，OTel Collector有一个Kubernetes属性处理器，可以添加Kubernetes元数据，这可以用于从Kubernetes API服务器收集指标。Kubernetes集群的追踪和日志也可以使用OpenTelemetry轻松收集和处理。

**在将OpenTelemetry与Kubernetes集成时，您在上下文传播和数据收集方面遇到了哪些挑战？**

将OpenTelemetry与Kubernetes集成的大多数挑战不一定是Kubernetes特有的，尽管在某些方面它们会加剧。最大的挑战无疑是数据管理。[集群](https://thenewstack.io/scaling-to-10000-kubernetes-clusters-without-missing-a-beat/)可以从几十个节点到数万个节点不等，即使是一个小型集群，根据您的工作负载，也会产生大量的指标和日志。上下文传播挑战通常也与工具问题有关，这可能需要多个团队之间的合作和协调才能进行调查。

通常，解决这些挑战的最佳方法是在您开始之前就为它们制定一个计划。围绕要收集哪些重要数据创建现实的目标。确定较小的集群或工作负载来部署OpenTelemetry，而不是试图“烧开大海”并进行大规模更改。

**您能否讨论一下您在大规模Kubernetes环境中扩展OpenTelemetry的方法，尤其是在性能和资源使用方面？**
这是一个复杂的话题，让我们从头开始讨论。资源利用率会根据工作负载、集群类型和大小、收集的信号以及许多其他因素而有所不同。您的目标是在这些因素之间取得平衡，同时在遥测分辨率、遥测可用性和查询性能之间进行权衡。这些权衡通常直接或间接地受到其余可观察性堆栈的影响。让我们以 pod 日志和指标为例。您是通过 Prometheus 公开自定义指标，还是将抓取的日志转换为指标？您需要不同信号之间达到何种程度的相关性？您的日志仅用于调试，还是从中导出面向客户的数据？

所有这些问题都会影响您的收集设置——例如，如果日志遥测的可靠性是最重要的事情，那么您需要运行 sidecar 收集器来抓取日志，然后将这些日志馈送到网关以进行进一步处理。您需要运行单独的日志网关，而不是尝试将日志处理器与指标或跟踪处理器共置。您可能会发现跟踪提供了指标和日志为您提供的绝大部分效用，而服务的资源使用量略有增加。对此并没有硬性规定，因为很大程度上取决于您的应用程序架构和可观察性后端。

**OpenTelemetry 如何与 Kubernetes 堆栈中的其他可观察性工具集成，您遇到了哪些好处或挑战？**

通常，OpenTelemetry 与其他可观察性工具集成良好，尤其是在这些工具支持 OpenTelemetry 协议 (OTLP) 的情况下。您可以使用 Collector 充当每个集群中的“中心枢纽”，从现有的 Prometheus 或 fluentd 部署中收集和规范化数据，或使用 OpenTelemetry 指标作为具有适当适配器的自动缩放器的输入。

我看到的一种流行模式是使用 OpenTelemetry 创建“本地”集群监控堆栈，该堆栈集中所有跨单个集群的遥测数据，然后使用 Collector 的路由功能将关键指标、日志和跟踪数据发送到第三方解决方案。如果您需要完全保真度，您可以通过代理访问“本地”可观察性堆栈。

**您推荐哪些关于使用 OpenTelemetry 检测 Kubernetes 原生应用程序的最佳实践？**

鉴于 OpenTelemetry 建立在一个丰富的分布式上下文层上，确保成功观察您的 k8s 原生应用程序的关键实践是牢记这一点。确保使用跟踪构建服务，无论是使用检测代理还是通过原生检测，以便在整个应用程序中传播上下文。

避免过度依赖自定义应用程序指标——通常，您可以将您感兴趣的数据捕获为跨度属性——这有助于控制成本并确保您的可观察性支出是线性的而不是指数级的。务必利用 Kubernetes 中的新功能，例如 API 服务器和 Kubelet 跟踪，尤其是在您的应用程序与这些 API 交互以进行扩展的情况下。

**您如何在动态 Kubernetes 环境中处理 OpenTelemetry 代理的部署和管理？**

根据您的应用程序的确切需求，您可以选择很多不同的选项。但是，总的来说，您需要考虑两种类型的代理。

第一种是负责从您的代码添加和生成遥测数据的检测代理，第二种是处理和导出遥测数据的收集代理。在 OpenTelemetry 中，前者是我们的任何零代码检测代理，后者是 OpenTelemetry Collector。

检测代理可以通过 OpenTelemetry Operator 最轻松地进行管理，该 Operator 允许您通过部署中的注释创建和分配检测到 pod。值得庆幸的是，Operator 还提供了一个自定义资源来管理 Collector 部署，允许您创建和定义 DaemonSet、StatefulSet、sidecar 部署或其他部署。

典型的 Kubernetes 工作负载可以使用 DaemonSet，确保在每个节点上都可用收集代理，该代理负责抓取本地指标和日志，以及接收调度到该节点的 pod 的数据。通常，对于具有复杂遥测处理的工作负载，收集 sidecar 将与 pod 一起部署，充当数据的本地接收器。
对于需要确保遥测数据尽快离开进程，并且不想处理进程内处理和过滤的额外开销的计划服务或突发服务，这是一个不错的选择。要管理所有这些监控和收集代理，请使用支持 OpenTelemetry Agent Management Protocol ([OpAMP](https://opentelemetry.io/docs/specs/opamp/)) 的控制平面——这是获取或设置配置、监控各种代理的运行状况以及处理更新的标准方法。

**您能否分享一个 Kubernetes/OpenTelemetry 中的可观测性帮助您识别和解决关键问题的具体案例？**

对 Kubernetes 服务进行有效的告警可以大大减少发现导致事件的因素所需的时间。今年早些时候，我们发现数据库中存在一个意外的竞争条件，涉及一个长时间运行的查询，该查询恰好与迁移同时执行。此竞争条件导致表被锁定以进行读取，从而导致整个基础设施中的连接池耗尽。我们的遥测以多种方式识别出了这个问题——我们能够看到失败请求的速率增加了，这触发了自动通知。

这使我们注意到许多 Pod 处于崩溃循环中（因为 Kubernetes 正在扩展以尝试处理重试请求），我们可以很容易地将其与数据库连接池中的错误关联起来。由于 OpenTelemetry 和我们自己的可观测性平台，我们能够发现有问题的数据库集群和我们的数据库迁移之间的关系，因为我们的 CI/CD 也使用 OpenTelemetry 进行监控。总而言之，我们能够在初始异常性能问题出现后的几秒钟内检测到事件，并在几分钟内做出响应，从而减少了停机时间。值得庆幸的是，即使这个数据库对我们的平台至关重要，由于 Kubernetes，我们的客户也只遭受了部分服务降级。

**您能否详细说明最近关于 OpenTelemetry 扩展到持续集成/持续部署的公告？**

OpenTelemetry 的承诺是针对遥测数据制定单一标准，无论云、编程语言或系统类型如何。实际上，我们已经看到用户在 CI/CD 中实施它多年了，并且很高兴看到社区努力改进这些用例的语义约定和上下文传播。这项工作应该会提高互操作性，并增加对 CI/CD 平台中 OpenTelemetry 的支持。

**最后，您能否告诉我们一些关于 OpenTelemetry 未来发展的信息？**

OpenTelemetry 已成为云原生系统中多模式可观测性数据的清晰明确的标准。在不久的将来，该项目将提供对工作负载持续分析的支持，并引入一组新的语义约定，用于结构化事件，以帮助创建前端客户端、生成式 AI 系统、Kubernetes 生命周期信号等的标准遥测数据。

我预计，随着项目越来越稳定和成熟，OpenTelemetry 作为框架、库、云系统和语言标准库的原生部分的采用率只会增加。未来，我相信我们将看到 OpenTelemetry 进一步扩展到新的领域——用户分析、业务事件、开发人员生产力、碳排放和资源成本，仅举几例——并允许在这些领域与底层性能数据之间建立关联，以便解锁新的见解，并帮助开发人员、运营商和业务领导者更好地理解这些因素之间的关系。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)