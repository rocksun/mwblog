<!--
title: Perses通过声明式仪表盘弥合可观测性差距
cover: https://cdn.thenewstack.io/media/2025/03/4e879205-perses.png
summary: 告别手动低效！云原生时代，Perses 通过 Kubernetes CRD 实现声明式仪表盘，拥抱 GitOps。告别 Grafana JSON，拥抱 Prometheus、Grafana Tempo 等开放标准，实现可移植和大规模协作。CNCF 沙箱项目 Perses，用 DAC 弥合可观测性差距，DevOps 效率 UP！
-->

告别手动低效！云原生时代，Perses 通过 Kubernetes CRD 实现声明式仪表盘，拥抱 GitOps。告别 Grafana JSON，拥抱 Prometheus、Grafana Tempo 等开放标准，实现可移植和大规模协作。CNCF 沙箱项目 Perses，用 DAC 弥合可观测性差距，DevOps 效率 UP！

> 译自：[Perses Closes the Observability Gap with Declarative Dashboards](https://thenewstack.io/perses-closes-the-observability-gap-with-declarative-dashboards/)
> 
> 作者：Nicolas Takashi

在不断发展的 Kubernetes、微服务和 GitOps 环境中，可观测性至关重要。虽然 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)、Prometheus 和 Jaeger 等工具已经标准化了遥测数据的收集和存储，但可视化工具仍然分散。基础设施和应用程序以声明方式进行管理，但[仪表盘](https://thenewstack.io/kubernetes/kubernetes-dashboards/)通常仍然是手动的、不一致的，并且与 [DevOps 工作流程](https://thenewstack.io/devops/)脱节。这种不一致会在依赖一致指标的开发人员、站点可靠性工程师 (SRE) 和业务领导者之间产生摩擦。

## 可观测性仪表盘工具的现状

Grafana 和 Kibana 等已建立的工具擅长可视化，并为许多可观测性供应商铺平了道路。但是，它们通常难以与现代 DevOps 工作流程保持一致。让我们探讨一些已知的挑战。

**手动工作流程和不一致**

许多仪表盘工具依赖于 UI 编辑器或非结构化的 JSON 文件。虽然这种方法提供了灵活性，但它也：

*   **产生配置漂移：** 团队复制仪表盘时会略有差异（例如“prod-latency”与“production-latency”），从而导致事件期间的混乱。
*   **缺乏协作：** 如果没有标准化的规范，开发人员、SRE 和业务团队可能会以不同的方式解释指标。
*   **忽略 GitOps 原则：** 更改很少在 git 中跟踪，这使得审计和回滚变得繁琐。

**部分自动化，完全复杂**

一些工具通过 Terraform 提供程序或 Kubernetes 运算符提供“即代码”工作流程。但是，这些通常是：

*   **不透明：** 基于 JSON 的仪表盘缺乏人类可读性和验证保障。
*   **脆弱：** 在环境（开发/暂存/生产）之间迁移仪表盘通常会破坏查询或数据源。
*   **工具特定：** 专有格式将团队锁定在供应商中，从而使多云策略复杂化。

**缺失的标准**

行业缺乏可移植的、与供应商无关的仪表盘规范。这迫使团队：

*   为每个工具（例如，Grafana、[Datadog](https://www.datadoghq.com/?utm_content=inline+mention) 或 [New Relic](http://newrelic.com/?utm_content=inline+mention)）重新发明模板。
*   在切换供应商时维护脆弱的迁移脚本。
*   牺牲创新以避免返工。

**为什么仪表盘即代码 (DAC) 仍然难以实现**

“即代码”范例改变了基础设施（基础设施即代码，或 IaC）、策略（策略即代码，或 PaC），甚至文档（文档即代码）。但是，仪表盘滞后了，因为现有的解决方案：

*   **优先考虑可视化而不是治理：** 工具侧重于渲染图形，而不是将仪表盘作为协作工件进行管理。
*   **忽略云原生模式：** 很少与自定义资源定义 (CRD)、运算符或 GitOps 工作流程集成。
*   **低估规模：** 手动工作流程在 100 多个微服务下崩溃，在这些微服务中，一致性和自动化是不容商量的。

鉴于所有这些挑战，我想向您介绍 [Perses](https://perses.dev/)，这是一个云原生计算基金会 (CNCF) 沙箱项目，旨在简化云原生环境中的仪表盘创建和管理。让我们探讨一下它是如何应对这些挑战的。

## Perses：一种云原生可视化方法

Perses 将仪表盘重新构想为声明式工件，与现代 DevOps 实践无缝集成。专为云原生生态系统而设计，它提供：

**声明式仪表盘定义**

Perses 使用 Kubernetes CRD 将仪表盘配置存储为代码。这确保了仪表盘是版本控制的、可审计的，并且与 git 中的应用程序清单一起管理。对于已经使用 Argo CD 等 GitOps 工具的团队，Perses 可以无缝集成到现有工作流程中。

**可移植性和灵活性**

与专有仪表盘工具不同，Perses 优先考虑开放标准。其轻量级架构与 Prometheus 和 Grafana Tempo 等流行数据源集成，避免了供应商锁定。开发人员可以通过 npm 包将仪表盘嵌入到内部工具中，而平台团队可以在整个环境中强制执行一致性。

**大规模协作**

Perses 的编程 SDK（Go、Cuelang）使团队能够制作仪表盘模板、重用组件和自动化重复性任务。这对于管理数百个仪表盘的企业尤其有价值，在这些企业中，手动仪表盘维护很快变得难以为继。

**安全和治理**
通过将仪表盘存储在 Kubernetes 命名空间中，Perses 与基于角色的访问控制 (RBAC) 策略保持一致，确保可见性限定在相关团队。由于所有更改都在 git 历史记录中被跟踪，因此合规性审计变得更加简单，从而提供了透明度和责任感。

## 为什么 Perses 在 CNCF 生态系统中脱颖而出

CNCF 长期以来一直支持 Prometheus 和 Grafana 等项目，但 Perses 填补了一个关键空白。它是一个 Kubernetes 原生的仪表盘框架，专为声明式管理和可移植性而构建。它的方法与关键的行业转变保持一致：

- **GitOps 采用：** 将仪表盘视为代码可确保一致性、版本控制以及与现有工作流程的无缝集成。
- **左移可观测性：** 在开发周期中更早地嵌入仪表盘可以提高团队之间的可见性和协作。
- **企业就绪的可扩展性：** 随着组织规模的扩大，他们需要能够强制执行治理而不会增加运营开销的解决方案。

凭借 CNCF 下的沙箱状态，Perses 有望成为社区驱动的标准，就像 OpenTelemetry 统一了整个生态系统中的遥测收集一样。

## 在 KubeCon 了解更多信息

Perses 代表了团队处理可观测性可视化方式的范式转变。拥抱云原生原则和声明式实践消除了传统仪表盘工具的摩擦，确保了一致性、可扩展性和自动化。

要了解 Perses 的实际应用，并了解它如何简化您的可观测性策略，请参加我们在欧洲 KubeCon + CloudNativeCon 上的会议“[无限可能，一致设计：使用 Perses DAC 制作仪表盘](https://kccnceu2025.sched.com/event/1txHy/limitless-possibilities-consistent-design-crafting-dashboards-with-perses-dac-nicolas-takashi-coralogix-antoine-thebaud-amadeus?iframe=no&w=100%25&sidebar=yes&bg=no)”。

*要了解有关 Kubernetes 和云原生生态系统的更多信息，请于 4 月 1 日至 4 日在伦敦参加[欧洲 KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)。*