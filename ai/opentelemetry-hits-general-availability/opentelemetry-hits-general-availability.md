<!--
title: 成为云计算遥测标准后，OpenTelemetry 迈入 AI 基础设施时代
cover: https://cdn.thenewstack.io/media/2026/05/612c2996-ubaid-e-alyafizi-rirrvhm-7ea-unsplash-scaled.jpg
summary: CNCF宣布开源可观测性框架OpenTelemetry正式毕业。该项目通过标准化数据打破厂商锁定，且在AI时代正加速演进为AI工作负载与智能体的重要基础设施。
-->

CNCF宣布开源可观测性框架OpenTelemetry正式毕业。该项目通过标准化数据打破厂商锁定，且在AI时代正加速演进为AI工作负载与智能体的重要基础设施。

> 译自：[After becoming cloud computing’s telemetry standard, OpenTelemetry graduates into the AI infrastructure era](https://thenewstack.io/opentelemetry-hits-general-availability/)
> 
> 作者：Paul Sawers

云原生计算基金会（[CNCF](https://www.cncf.io/)）周四宣布 [OpenTelemetry](https://opentelemetry.io/) 正式毕业。这是一个[开源可观测性框架](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)，已成为云原生计算中应用最广泛的基础设施之一。

这一里程碑标志着该项目在经历七年崛起后达到了顶峰。该项目[始于 2019 年](https://opensource.microsoft.com/blog/2019/05/23/announcing-opentelemetry-cncf-merged-opencensus-opentracing/)，由两个竞争的可观测性项目合并而成：一个是 CNCF 支持的分布式追踪标准 [OpenTracing](https://opentracing.io/)，另一个是最初由谷歌发起并得到微软等公司支持的遥测项目 [OpenCensus](https://opencensus.io/)。

如今，OpenTelemetry 被广泛用于在分布式软件系统中收集和导出遥测数据——包括追踪（traces）、指标（metrics）和日志（logs）。“毕业”代表了 CNCF 对开源项目的最高成熟度认证，标志着治理的稳定性、生产环境的采用以及长期的可持续性。该基金会表示，OpenTelemetry 目前已成为 CNCF 生态系统中“发展速度最快”的项目之一，仅次于 Kubernetes，拥有超过 12,000 名贡献者，吸引了 2,000 多家公司的参与。

对于许多开发人员和基础设施团队来说，OpenTelemetry 多年来已经发挥了基石基础设施的作用，这让它的正式毕业显得有些姗姗来迟。CNCF 首席技术官 [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/) 告诉 *The New Stack*，基金会的毕业流程故意设计得很慢，以便为那些有望成为长期行业标准的项目提供保障。

> “毕业的目标是向企业提供确定性，让他们确信自己正构建在一个中立且坚固的骨干之上。”

“我们的毕业流程并不求快；它通常需要多年的努力来构建稳定性、安全性和弹性的治理，以确保整个行业长期、可持续的创新，”Aniszczyk 说道。“对于像 OpenTelemetry 这样关键的项目，我们需要确认它是现代技术栈中一个永久的、中立于厂商的组件，而不是依赖于任何单一的商业利益。毕业的目标是向企业提供确定性，让他们确信自己正构建在一个中立且坚固的骨干之上。”

## 成为通用基础设施

现代软件系统产生的遥测数据已经超出了许多组织实际所能管理的范围。随着云环境横跨公共基础设施、私有数据中心、Kubernetes 集群以及——越来越多——由 AI 生成的服务，可观测性团队正在努力应对不断上升的复杂性和[不断攀升的数据成本](https://thenewstack.io/why-observability-bills-grow/)。OpenTelemetry 厂商中立的定位有助于推动行业的广泛采用——目前主要的云提供商和可观测性厂商，包括 Microsoft Azure、AWS、Google Cloud、Datadog、Grafana Labs、Splunk 和 New Relic，都以各种形式对其提供了支持。

在历史上，这些厂商通常依赖专有的代理（agent）、SDK 和遥测管道，这使得组织很难在平台之间进行迁移。OpenTelemetry 帮助标准化了跨编程语言和基础设施环境的检测工作，使得遥测数据能够更容易地在监控和分析系统之间流动。

Aniszczyk 指出，2019 年 OpenTracing 和 OpenCensus 的合并有助于防止可观测性市场的碎片化，同时通过削弱专有遥测技术的锁定，改变了厂商的商业竞争方式。

> “在 OpenTelemetry 出现之前，厂商在专有代理/收集器和数据格式上进行竞争，这往往导致客户被锁定。”

“在 OpenTelemetry 出现之前，厂商在专有代理/收集器和数据格式上进行竞争，这往往导致客户被锁定，”他说道。“如今，竞争在下一层白热化：在提供高信号洞察、出色的 AI 驱动分析和高性价比解决方案的基础之上，提供优质的开发人员和用户体验。”

Grafana Labs 首席技术官 [Tom Wilkie](https://uk.linkedin.com/in/tomwilkie) 在 2026 年初接受 *The New Stack* 采访时也[认为](https://thenewstack.io/can-opentelemetry-save-observability-in-2026/)，OpenTelemetry 通过标准化跨平台的检测，帮助瓦解了传统可观测性带来的锁定。

“团队不再需要拼凑特定厂商的 SDK，新的可观测性玩家也可以更容易地进入市场，因为代码检测不再是护城河，”Wilkie 说道。

然而，OpenTelemetry 的快速增长也给一些采用者带来了运维上的烦恼。在[一份 2025 年的提案](https://opentelemetry.io/blog/2025/stability-proposal-announcement/)中，该项目治理委员会概述了未来的稳定性提升工作，并承认 OpenTelemetry 的“复杂性和缺乏稳定性”给“生产部署制造了障碍”，列举的问题包括破坏性的配置更改、大型部署中的性能回退，以及跨数百或数千个服务协调升级的困难。

在 2025 年 12 月接受 *The New Stack* 采访时，可观测性初创公司 MyDecisive.ai 的创始人 [Ari Zilka](https://www.linkedin.com/in/arizilka/) [表示，一些企业](https://thenewstack.io/from-group-science-project-to-enterprise-service-rethinking-opentelemetry/)实际上已将 OpenTelemetry 变成了一项“团体运动”，大型组织通常会指派整个内部团队来管理遥测基础设施和收集器的部署。

这些担忧反映了多年来在可观测性市场上一直存在的更广泛的挫败感。运行大型分布式系统的组织通常会收集海量的日志、追踪和指标，在此过程中产生巨额的监控账单。

当然，OpenTelemetry 自身并不能解决可观测性的经济学问题，但它的标准化努力有助于为那些试图与老牌平台竞争的[新兴可观测性厂商](https://thenewstack.io/opentelemetry-opens-the-door-for-observability-startups/)降低门槛。

## 基础设施压力

该项目的毕业恰逢 AI 生成的软件和自治基础设施系统开始给可观测性工具带来额外的压力。AI 编码系统生成服务、部署、API 调用和基础设施变更的速度，要比传统软件开发周期快得多。  
Aniszczyk 表示，AI 智能体（agent）和自治系统的兴起正在对现代基础设施提出新的要求，而遥测技术正在成为监控和协调这些系统的核心机制。

> “向 AI 智能体和自治系统的转变，是当今基础设施面临的最重要的单一进化压力。”

“向 AI 智能体和自治系统的转变，是当今基础设施面临的最重要的单一进化压力，”他说道。“我们认为 OpenTelemetry 已经超越了传统的可观测性框架——它现在正成为 AI 工作负载和模型的基石。这意味着其规模要扩大到全新的数量级，在这些数量级中，遥测是 AI 智能体源源不断的感觉输入。”

CNCF 表示，不断增长的 AI 工作负载正在帮助推动整个生态系统中 OpenTelemetry 采用率的上升。根据 [npm 下载数据](https://npmx.dev/package/@opentelemetry/api)，该项目的 JavaScript API 包月下载量从 2025 年 4 月的约 7500 万次飙升至 2026 年 4 月的超过 2 亿次，创下了历史新高。该项目的 [Python API 包](https://pypistats.org/packages/opentelemetry-api)在同一时期也创下了历史最高的下载量。

可观测性初创公司 [OllyGarden](https://ollygarden.com/) 的联合创始人 [Juraci Paixão Kröhling](https://www.linkedin.com/in/jpkroehling/) 表示，许多组织发现 AI 系统引入了长期以来与分布式云基础设施相关的同样的运维和可靠性问题。

“随着各组织竞相将生成式 AI 工作负载投入生产环境，他们发现生成式 AI 系统其实就是分布式系统，并伴随着所有随之而来的延迟、可靠性和成本问题，”Kröhling 在一份声明中表示。“OpenTelemetry 为这些团队提供了一种通用语言，用以检测智能体、模型及其周边服务，而不会被任何单一厂商所锁定。”