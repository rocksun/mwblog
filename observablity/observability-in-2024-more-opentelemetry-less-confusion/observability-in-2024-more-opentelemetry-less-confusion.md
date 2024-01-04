<!--
title: 可观测性2024：更多OpenTelemetry，更少困惑
cover: https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1-1024x576.png
-->

可观测性无疑已成为应对数据爆炸带来混乱的关键。但数据激增本身也制造了另一种混乱。

> 译自 [Observability in 2024: More OpenTelemetry， Less Confusion](https://thenewstack.io/observability-in-2024-more-opentelemetry-less-confusion/)，作者 B. Cameron Gain 是 ReveCom Media 的创始人兼首席分析师。他对计算机的痴迷始于 20 世纪 80 年代初，当时他破解了太空侵略者游戏机，这样就可以整天花 25 美分在当地的视频游戏厅玩游戏。然后...

这对许多IT团队来说，如果不是大多数，都是充满混乱和挑战的一年。在各种挑战中，不断上升的云成本和优化云支出的压力尤为突出。节省成本的策略大多被委派给[DevOps来实施](https://thenewstack.io/breaking-down-the-wall-in-devops/)。

与此同时，[需要管理](https://thenewstack.io/grappling-with-observability-data-management/)和监控的数据爆炸性增长，尤其是那些继续扩张的组织，这往往产生了涵盖多云和内部部署环境的数据管理和监控需求。

可观测性可以说在2023年崛起为伟大的救世主，对于导航由数据爆炸引起的混乱至关重要。然而，随着数据激增，可观测性本身也制造了潜在的混乱。

日志、追踪和指标等遥测数据的涌入，构成了与降低云成本、优化冗余以及在 IT 问题发生之前预测和解决业务问题相关的决策基础，但生成的大量遥测数据本身就制造了更多需要管理的复杂性。

尽管你总可以使用 Grafana 面板来帮助[将这些数据合并到一个控制台中](https://thenewstack.io/why-dynatrace-says-ai-is-the-answer-for-single-panel-observability-for-cloud-native/)，但对能够帮助细调所需的数据类型并将其汇集到单一接口中的解决方案的需求，在 2023 年成为一个特别关键的需求。

[Dotan Horovits](https://www.linkedin.com/today/author/horovits)，Logz.io 的首席开发者倡导者和[云原生计算基金会(CNCF)](https://cncf.io/?utm_content=inline-mention)的云原生大使说:"今年也见证了强大的经济压力，这使得成本效益成为所有人关注的焦点。"关于可观测性花费过多的高调报道进一步凸显了需要创新的解决方案来提高信噪比以及更灵活的定价方案的需求。

好消息是 2023 年的主要趋势涉及标准化的兴起，特别是随着开放遥测作为实现各种可观测性工具和流程的通用标准而取得的进展。这有助于通过创建一个标准来汇集各种可观测性工具到一个单一界面(通常是一个 Grafana 控制台)来驯服遥测数据野兽。

安全顶然仍是一个持续的关切，但开源带来了希望。例如，eBPF 已经确立为[安全实践中可观测性](https://thenewstack.io/3-observability-best-practices-for-cloud-native-app-security/)的支柱。

此外，人工智能和机器学习(ML)的兴起，包括[大语言模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)(LLM)，旨在理解可观测性数据爆炸。2024 年，希望机器[能在解析可观测性数据方面发挥更可靠的作用](https://thenewstack.io/games-data-play-the-sql-murder-mystery/)，减轻人工分析的负担。

## 太多?

得益于 OpenTelemetry 和其他新兴最佳实践的进步，新的工具和调整，2023 年标志着一个[由开源发展主导](https://thenewstack.io/open-source-developers-are-securitys-new-front-line/)的可观测性变得更易于访问的一年。

可观测性已经超越了其与监控相关的传统职责，用于发现错误和解决故障，现在它的影响力延伸到了不同的接口、工具，并展示了增强的开放性和兼容性，从而越来越多地进行预测。

这些预测可以涉及在故障发生之前预测故障、成本变化、资源使用情况和其他变量，这些变量在以前肯定会更难预测，主要依赖试错法。

的确，就在今年较早时候的 KubeCon 2023 + CloudNativeCon 上，OpenTelemetry 的一个关键发展就是它现在支持三个核心的可观测信号:日志、指标和追踪，[企业管理协会(EMA)](https://www.enterprisemanagement.com/)的分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 表示。“这意味着组织现在可以使用单个代理来收集其日益分布式和因此复杂的微服务应用程序宇宙中的可观测数据。”

“这可能大大简化了当今可观测性中最重要的痛点之一: instrumentation。开发人员现在可以从 OpenTelemetry 不断增强的自动检测 instrumentation 中受益，不再需要为特定的可观测平台 instrumentation 他们的代码。”Volk 说。

然而，由于工具激增带来的选择自由也产生了自己的挑战。

“虽然我同意可观测性已经对各种工具更加开放，但这也成为一个挑战，带来了工具泛滥和数据粉碎，这在今年对组织提出了重大挑战。组织不再为获取正确的数据而苦恼，而是在于数据爆炸难以‘大海捞针’，这不仅存储成本高，也越来越难分析有价值的信息。” Horovits 说。

“因此，可观测性实践正在向上移动到堆栈，从关注收集日志、指标和其他信号，到从数据中提取见解，横跨基础设施和应用程序，横跨信号类型、来源和格式。为了解决这个需求，可观测性工具和供应商正在转向整体的可观测性解决方案，并加大对数据分析后端功能的投入。”

的确，[OpenTelemetry 的支持和采用](https://thenewstack.io/opentelemetry-and-observability-looking-forward/)应该继续保持强劲的增长轨迹。

我们看到终端用户和可观测性供应商中的采用量在增加，这进一步推动了专有和开源遥测发送和抓取代理的淘汰。我预计随着日志部分已经达到正式发布，意味着该项目现在已经在可观测性的三大支柱(即日志，指标和追踪)上普遍可用，这种趋势将会加速。Horovits说:“展望‘三大支柱’以外，今年的焦点转移到了持续分析这一新的遥测信号上。该项目也正在将其从后端中心的起源扩展到支持客户端遥测和真实用户监控用例。”

[CI/CD](https://thenewstack.io/how-to-observe-your-ci-cd-pipelines-with-opentelemetry/) 体现了这一转变，开发阶段揭示了关键指标、日志和追踪，以几年前难以想象的方式提供了可观测性，这要归功于 OpenTelemetry 提供的工具化和其他流程与工具。值得注意的是，广泛使用的 DORA 指标现在已经成为评估开发者生产力的组成部分。

Horovits说: “缺乏 CI/CD 可观测性会导致变更引入生产的导致时间不必要地过长，这是衡量一个提交进入生产需要多少时间的一个关键 DORA 指标。今天的 CI/CD 工具发出各种遥测数据，无论是日志、指标还是追踪数据，以[报告发布流水线状态](https://thenewstack.io/leaky-data-pipelines-uncovering-the-hidden-security-risks/)。自然地，我们要用与监控生产环境相同的可观测性栈来监控软件发布流水线。比如 Prometheus、OpenSearch 和 Jaeger 等开源工具可以用于可视化流水线事件、指标和序列，以诊断不稳定的测试、有缺陷的构建或构建环境中的问题。”

但是，CI/CD 可观测性的工作仍有待做。

Horovits说: “尽管许多 CI/CD 工具会发出遥测数据，但它们并没有遵循任何特定的标准、规范或语义约定。这使得使用可观测性工具来监控这些流水线变得很困难。”

## 安全性、可观测性以及 eBPF

安全性显然仍然是一个巨大的问题，尤其是对于高度分布式和复杂的 Kubernetes 结构，这导致 2[023 年攻击事件的增加](https://thenewstack.io/kubernetes-security-in-2023-adoption-soars-security-lags/)，进而导致了更多的罚款和对那些被认为负有责任的人的解雇。这一不幸的趋势预计将在 2024 年继续。扩展的伯克利包过滤器(eBPF)的有效性在2023年表现出了很大的希望，它构成了[开源安全](https://thenewstack.io/the-new-stack-context-two-views-of-open-source-security/)工具的基础，为帮助预防攻击提供了可观察性。

[eBPF](https://thenewstack.io/what-is-ebpf/) 的效力主要源自其计算效率，因为它与 Linux 内核紧密相连。然而，将 eBPF 仅仅归类为基于 Linux 内核的工具会产生误导，因为它的影响延伸到整个堆栈，影响应用它的应用程序。使用 eBPF 的有效平台应该能够赋权 DevOps 团队[监控 Kubernetes 集群中应该运行的内容](https://thenewstack.io/using-prometheus-to-monitor-kubernetes-clusters-running-cloud-foundry/)，并在违反策略或检测到安全威胁时提供可操作的结果。

开源继续引领安全性的道路。2023 年闪亮的两个开源 eBPF 安全可观测性工具是 [KubeScape](https://www.armosec.io/kubescape/) 和 [Cilium](https://cilium.io/)。Kubernetes 安全提供商 ARMO 通过覆盖 Kubernetes 应用程序及其更新的生命周期，为可观测性提供了一个窗口。

这包括 IDE、CI/CD 流水线和集群，用于风险分析、安全性、合规性、配置错误扫描和镜像扫描。开源产品还包括网络策略和安全策略等加固建议。Kubescape 与 DevOps 团队[使用该平台](https://thenewstack.io/why-you-should-run-your-platform-team-like-a-product-team/)所需的工具清单集成，如软件物料清单(SBOM)、签名扫描和策略控制。它在开发周期开始时启动扫描，跨越 CI/CD，贯穿部署和集群管理过程。

Cilium通过eBPF提供了额外的功能，以帮助保护在Docker和Kubernetes上部署的运行时之间的[网络连接](https://thenewstack.io/a-use-case-to-secure-kubernetes-network-connections/)，以及其他环境，包括裸机和虚拟机。创建Cilium并将其捐赠给CNCF的[Isovalent](https://thenewstack.io/isovalent-open-sources-tetragon-ebpf-based-observability-platform/)及其贡献者也在并行开发Cilium的功能，通过Cilium的子项目Hubble和Tetragon分别提供网络可观测性和网络安全功能。

Cilium主要提供容器网络接口(CNI)实现，这通常是Kubernetes网络栈的核心组件，[ARMO](https://thenewstack.io/armo-misconfiguration-is-number-1-kubernetes-security-risk/)的CTO和联合创始人[Benyamin Hirschberg](https://il.linkedin.com/in/ben-hirschberg-66141890)说。 

由于Cilium能够为[加强容器间流量的Kubernetes集群提供更好的性能](https://thenewstack.io/loft-labs-vcluster-provides-secure-multitenant-kubernetes-clusters/)，“该项目确实在网络策略之上改进了其安全性能，网络策略已经存在多年。” Hirschberg说，“安全可观测性是Cilium的一个重大新发展，表明用户正在这个领域寻求解决方案。”

[开源社区](https://thenewstack.io/scaling-open-source-community-by-getting-closer-to-users/)倾向于解决短期问题，并为像Cilium这样的项目实现全新的功能，如Tetrago提供动力，Tetrago本质上是一个类似Falco的运行时威胁检测代理。

Hirschberg 说，Kubescape 结合了 eBPF 数据流，以全面了解集群的安全态势。通过结合 eBPF 在内核级别提供的对网络流量的可见性，它将实时系统行为添加到漏洞和配置错误等额外发现中。

“这提供了对可达漏洞、可以在不破坏应用程序的情况下修复的配置错误、攻击路径检测甚至建议最佳网络策略和 seccomp 配置文件的视图。” Hirschberg 说。

## 机器时间

可观测性[可以用来](https://thenewstack.io/how-the-opentelemetry-collector-scales-observability/)收集洞察力改进业务决策，并减轻对 IT 预算的日益严格审查，从而降低云成本。但是，正确的工具对于理解这种遥测数据激增至关重要。不用说，可观测性可以说在 2023 年崛起为伟大的救世主，对于导航由数据爆炸引起的混乱至关重要。然而，随着数据的激增，可观测性本身也制造了自己的潜在混乱。大语言模型和 AI 已经开始发挥可能是革命性的作用。在 2023 年，我们看到了 AI 应用程序将介入的初始迹象，这可能标志着可观测性的终极形态。这些流程和 AI 可以以人类无法实现的方式进行计算分析。

这主要表现在两方面。首先，有了好的可观测性工具，大量遥测数据可以被解析、分类和层级化，让人类可以理解并用于做出业务决策、资源分配和其他决定。同时，AI可以评估大量的遥测数据，根据元遥测[数据做出决策，最终自动化决策过程](https://thenewstack.io/dr-torq-data-processing-at-the-edge-with-linux-awk/)。尽管假设人类会进行最终检查，至少在初始阶段是这样。

另一方面涉及 AI 以无代码、低代码的方式发起命令，使用通用语言来描述可观测性结论和期望的洞察。在大语言模型的帮助下，AI 接管了这个过程。虽然这些工具尚未出现，但关于它们的讨论在 2023 年很普遍。因此，AI 对 2024 年的可观测性的涌入，承诺将是迷人的。

“大语言模型将成为 DevOps 团队、安全工程师和 SRE(网站可靠性工程师)的‘伙伴’，持续关注传入的数据，提出预防性优化的建议，并帮助快速解决问题，最大限度地减少业务影响。大语言模型有分析难以置信的大量复杂的运营数据的绝佳能力，这些数据来自 DevOps、IT 和业务，因此可以帮助我们人类根据几乎完整的上下文确定优先级。”Volk 说。“大语言模型还将为我们提供自动化越来越多管理任务所需的代码，让人类可以专注于为这些自动化设置策略护栏。”

Volk 说，能够分析日志、指标和跟踪的单一数据流使数据分析更具力量来检测那些“未知的未知”。

Torsten 说:“大语言模型特别‘欣赏’OpenTelemetry 统一处理所有可观测数据所提供的额外上下文。”“在 2024 年，我们可以期待更具体、更可操作的洞察，降低错过相关趋势或异常的风险。”
