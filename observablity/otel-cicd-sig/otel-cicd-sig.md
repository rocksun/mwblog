
<!--
title: OpenTelemetry正在扩展到CI/CD可观测性
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
summary: OpenTelemetry 扩展至 CI/CD 可观测性！新版语义约定 v1.27.0 纳入 CI/CD 属性，标准化遥测数据。通过 CI/CD SIG 协作，对齐 SLSA 规范，实现 VCS 版本追踪和供应链安全。未来将聚焦指标约定、原型构建和 OTEP #258 实施，欢迎加入 CNCF Slack `#cicd-o11y` 频道共建。
-->

OpenTelemetry 扩展至 CI/CD 可观测性！新版语义约定 v1.27.0 纳入 CI/CD 属性，标准化遥测数据。通过 CI/CD SIG 协作，对齐 SLSA 规范，实现 VCS 版本追踪和供应链安全。未来将聚焦指标约定、原型构建和 OTEP #258 实施，欢迎加入 CNCF Slack `#cicd-o11y` 频道共建。

> 译自：[OpenTelemetry Is Expanding Into CI/CD Observability](https://opentelemetry.io/blog/2025/otel-cicd-sig/)
> 
> 作者：OpenTelemetry Authors; Docs CC BY

多年来，我们一直在讨论需要一种通用的“语言”来报告和观察 CI/CD 管道，最终，我们看到了这种语言的第一个“词”进入可观测性的“词典”——[OpenTelemetry 开放规范](/docs/specs/otel/)。随着 OpenTelemetry 最新发布的 [语义约定](/docs/specs/semconv/) v1.27.0，您可以找到 [用于报告 CI/CD 管道的指定属性](/docs/specs/semconv/attributes-registry/cicd/)。

这是 [OpenTelemetry 中 CI/CD 可观测性特别兴趣小组 (SIG)](https://github.com/open-telemetry/community/blob/main/projects/ci-cd.md) 努力工作的结果。当我们完成第一阶段的核心里程碑时，我们认为现在是与世界分享它的好时机。

## 工程师需要了解 CI/CD 管道的可观测性

[CI/CD 可观测性](https://medium.com/@horovits/fcc6c10c4987) 对于确保软件高效且可靠地发布到生产环境至关重要。 良好运行的 CI/CD 管道通过缩短 [变更前置时间 DORA 指标](https://horovits.medium.com/improving-devops-performance-with-dora-metrics-918b9604f8e2) 并能够快速识别和解决损坏或不稳定的流程，从而直接影响业务成果。 通过将可观测性集成到 CI/CD 工作流程中，团队可以实时监控管道的健康状况和性能，从而深入了解瓶颈和需要改进的领域。 利用用于监控生产环境的相同成熟工具，组织可以扩展其可观测性能力以包括发布周期，从而培养软件交付的整体方法。 无论是开源工具还是专有工具，在为 CI/CD 管道选择可观测性工具链时，都无需重新发明轮子。

## 标准化的必要性

然而，CI/CD 工具的多样化格局给实现一致的端到端可观测性带来了挑战。 由于每个工具都有自己的方式、格式和语义约定来报告管道执行状态，因此工具链中的碎片化可能会阻碍无缝监控。 在工具之间迁移变得很痛苦，因为它需要重新实现现有的仪表板、报告和警报。

当您需要以统一的方式监控发布管道中涉及的多个工具时，事情会变得更具挑战性。 这就是 [开放标准和规范变得至关重要的地方](https://horovits.medium.com/the-rise-of-open-standards-in-observability-highlights-from-kubecon-13694e732c97)。 它们创建了一种通用的统一语言，一种与工具和供应商无关的语言，从而可以在不同的工具之间实现有凝聚力的可观测性，并使团队能够保持对其 CI/CD 管道性能的清晰而全面的视图。

标准化的需求与创建上述语义约定相关，即用于报告管道中发生的事情的语言。 标准化对于通过系统传播此报告的方式也是必需的，例如在管道执行期间生成进程时。 这促使我们推广使用环境变量进行进程之间的上下文和 baggage 传播的标准化，这是最近批准和合并的另一个重要里程碑。

## OpenTelemetry：CI/CD 可观测性规范的天然家园

这种认识促使我们寻找正确的方法来创建规范。 OpenTelemetry 正在成为遥测生成和收集的标准。 OpenTelemetry 规范的任务正是解决这个问题：为遥测创建一个通用的、统一的且与供应商无关的规范。 并且它对云原生计算基金会 (CNCF) 的支持确保了它保持开放和供应商中立。 作为 OpenTelemetry 的长期倡导者，将其扩展到涵盖这个重要的 DevOps 用例是理所当然的。

我们从几年前的 [OpenTelemetry 扩展提案 (OTEP #223)](https://github.com/open-telemetry/oteps/pull/223) 开始，提出了我们扩展 OpenTelemetry 以涵盖 CI/CD 可观测性用例的想法。 与此同时，我们在 CNCF Slack 上开设了一个 Slack 频道，以聚集志同道合的爱好者，并开始集思广益，了解它应该是什么样子。 Slack 频道不断发展，我们很快发现这个问题在许多组织中都很常见。

根据技术监督委员会和 CNCF 内其他人的反馈，我们采取了要求授权的途径，即在 OpenTelemetry 的语义约定 SIG（简称 SIG SemConv）下为该主题启动一个专门的工作组。 在他们的祝福下，我们 [启动了正式的 CI/CD 可观测性 SIG](https://github.com/open-telemetry/community/blob/main/projects/ci-cd.md)，以正式确定我们之前的 Slack 小组讨论和目标。
## OpenTelemetry 的 CI/CD 可观测性 SIG

自 2023 年 11 月以来，该 SIG 一直积极与多家公司和开源项目的专家合作，致力于制定 CI/CD 可观测性语义标准。在成立之初，我们决定将重点放在 2024 年的几个关键领域：

- CI/CD 系统的一组通用属性。
- 开发原型，包括整体和特定于信号的属性。
- 继续推进将环境变量作为上下文传播器添加到 OpenTelemetry 规范的提案 (OTEP #258)。
- 一种将 OpenTelemetry 约定与 [CDEvents](https://cdevents.dev/docs/) 和 [Eiffel](https://eiffel-community.github.io/) 连接起来的策略。

起初，我们的 SIG 每周一在更大的语义约定工作组会议期间举行会议。这为我们提供了一个很好的机会来确定方向，因为我们研究和讨论了如何完成路线图上的目标。这也使我们能够了解更大的 OpenTelemetry 社区的许多成员，征求对我们设计的反馈，并获得有关如何进行的指导。OpenTelemetry 语义约定工作组一直非常支持 CI/CD 倡议。

在完成并发布其初始里程碑（见下文）后，我们的 SIG 获得了自己的 [专用会议时段](https://github.com/open-telemetry/community/pull/2293)，在 [OpenTelemetry 日历](https://github.com/open-telemetry/community#calendar) 上，每周四太平洋时间 06:00 举行。该小组在这里聚在一起讨论当前和未来的工作，然后再提交给周一举行的更大的语义约定会议。我们非常期待社区的持续支持和参与，因为我们将继续推动这一关键的标准化领域。

## CI/CD 是最新 OpenTelemetry 语义约定的一部分

经过数月的迭代和反馈，[第一组语义约定已合并](https://github.com/open-telemetry/semantic-conventions/pull/1075) 到 v1.27.0 版本中。此更改为 `CICD`、`artifacts`、`VCS`、`test` 和 `deployment` 命名空间下的 CI/CD 引入了第一组基础语义。这是 CI/CD 可观测性 SIG 和整个行业的一个重要里程碑。这为我们小组所有其他目标的开始形成和实现奠定了基础。

但这实际上意味着什么？它提供什么价值？让我们考虑两个命名空间的真实示例。

### 跟踪来自版本控制系统 (VCS) 的发布修订

[版本控制系统 (VCS) 属性](/docs/specs/semconv/attributes-registry/vcs/) 涵盖了 VCS 中常见的多个领域，例如引用和更改（拉取/合并请求）。`vcs.repository.ref.revision` 属性是一个关键的元数据。由于 GitHub 和 GitLab 等版本控制系统会发出事件，因此它们现在可以具有此语义兼容的属性。这意味着在集成代码、发布代码并将其部署到环境时，系统可以包含此属性，并更轻松地跨边界跟踪代码修订。如果部署失败，您可以快速查看代码的修订版本并将其追溯到有问题的版本。此属性实际上也是 [DORA 指标](https://dora.dev/guides/dora-metrics-four-keys/) 的关键元数据，因为您可以计算变更前置时间和失败部署恢复时间。

### 用于供应链安全的工件，与 SLSA 规范对齐

[工件属性命名空间](/docs/specs/semconv/attributes-registry/artifact/) 在其首次实现中具有多个属性。此命名空间中的一组关键属性涵盖了与 [SLSA](https://slsa.dev/spec/v1.0/about) 模型紧密对齐的 [证明](https://slsa.dev/attestation-model)。这实际上是可观测性和软件供应链安全之间首次建立直接联系。考虑以下由 SLSA 定义的 [供应链威胁模型](https://slsa.dev/spec/v1.0/threats)：

这些用于工件和证明的新属性有助于实时观察上图中建模的事件序列。实际上，今天存在的约定以及将来添加的约定可以使用可观测性语义实现核心软件交付能力（如安全性和平台工程）之间的互操作性。

## CI/CD 可观测性工作组的下一步是什么

如前所述，我们达到的第一个主要里程碑是合并 OTEP，用于使用新属性扩展语义约定，该属性现在是 OpenTelemetry 语义约定最新版本的一部分。

第二个重要的里程碑是 [OTEP #258](https://github.com/open-telemetry/oteps/pull/258)，用于环境变量上下文传播，该提案已获得批准并合并。此 OTEP 为编写规范奠定了基础。

由于我们在最初的里程碑上取得了进展，因此我们更新了[CI/CD 可观测性 SIG 2024 年剩余时间的里程碑](https://github.com/open-telemetry/community/blob/main/projects/ci-cd.md)。我们的目标是在年底前尽可能完成已定义的里程碑。值得注意的是，我们专注于：

* 添加[版本控制系统的指标约定](https://github.com/open-telemetry/semantic-conventions/pull/1383)。
* 在 CICD 系统中构建跟踪原型（例如，ArgoCD、GitHub、GitLab、Jenkins）。
* 准备好[OTEP #258](https://github.com/open-telemetry/oteps/pull/258)以供实施，并添加到规范中。
* 向注册表添加更多属性，涵盖更多领域。
    * Software outage incidents
    * System attributes around CI/CD runners
* 开始处理跟踪和事件（日志）信号的具体细节，为其他规范之间的互操作性搭建桥梁。
* 采纳[实体和资源 OTEP](https://github.com/open-telemetry/oteps/pull/264)的变更。
* [启用供应商特定的扩展](https://github.com/open-telemetry/semantic-conventions/issues/1193)。
* 语义采纳的开源社区拓展策略。

到目前为止，所有提到的都只是开始！我们在[CICD 项目看板](https://github.com/orgs/open-telemetry/projects/79)上定义了很多工作，并且我们有正在进行的工作！我们将继续迭代为 2024 年剩余时间设定的上述里程碑。以下是一些需要注意的事项。

* 版本控制系统指标——DORA 的领先指标
* 来自 GitHub Actions 和审计日志的跟踪
* 特别感谢以下人员使该组件成为可能：
    * Tyler Helmuth – Honeycomb
    * Andrzej Stencel – Elastic
    * Curtis Robert – Splunk
    * Justin Voss
    * Kristof Kowalski – Anz Bank
    * Mike Sarahan – Nvidia
* GitHub Receiver 组件的相应版本，但在 GitLab 中实现

还有更多！

## 扩展 OpenTelemetry 需要集体的力量

哇，要做的事情真多！可以肯定的是，这个 SIG 将持续到 2024 年以后，并贯穿 2025 年。标准很难制定，但至关重要。而且，我们有一些很棒的人员参与了 SIG 并为这些标准做出了贡献！你可能会问是谁？

首先，我们要感谢 OpenTelemetry 领导委员会的关键成员，他们大力支持了我们迄今为止所做的工作，并将继续这样做。

在 OpenTelemetry 技术委员会中，我们有两位核心赞助商，分别是来自 Lightstep 的 Carlos Alberto 和来自 Google 的 Josh Suereth。Carlos 和 Josh 都非常支持 CICD 工作，真正指导我们完成成功所需的流程和细节。

在 OpenTelemetry 管理委员会中，来自 Microsoft 的 Trask Stalnaker 一直是一位杰出的盟友，而来自 Skyscanner 的 Daniel Blanco 现在担任我们的联络员。Trask 和 Daniel 在支持 SIG 并使我们能够在 OpenTelemetry 社区中拥有自己的会议方面发挥了重要作用。

除了这些人之外，我们还收到了以下关键人物的大量反馈、支持和贡献：

*   Yuri Shkuro – Jaeger 的创建者，OpenTelemetry 的联合创始人
*   Andrea Frittoli – Tekton CD 维护者，CDEvents 联合创建者，IBM
*   Emil Bäckmark – CDEvents 和 Eiffel 维护者，Ericsson
*   Magnus Bäck – Eiffel, Axis Communications
*   Liudmila Molkova – Microsoft
*   Christopher Kamphaus – Jemmic, Jenkins
*   Giordano Ricci – Grafana Labs
*   Giovanni Liva – Dynatrace, Keptn
*   Ivan Calvo – Elastic, Jenkins
*   Armin Ruech – Dynatrace
*   Michael Safyan – Google
*   Robb Kidd – Honeycomb
*   Pablo Chacin – Grafana Labs
*   Alexandra Konrad – Elastic
*   Alexander Wert – Elastic
*   Joao Grassi – Dynatrace
*   DJ Gregor – Discover

说了很多名字！我们非常感谢所有支持这项计划并帮助其实现的人！构建行业范围的标准需要大量的思考能力和时间。难题很难解决，但这些人已经迎接了挑战，使可观测性和 CICD 系统的世界变得更好、更具互操作性！

## 加入工作组讨论并产生影响

想了解更多？想参与塑造 CI/CD 可观测性吗？

我们邀请开发人员和从业者参与讨论，贡献想法，并帮助塑造 CI/CD 可观测性和 OpenTelemetry 语义约定的未来。讨论在 CNCF Slack 的 `#cicd-o11y` 频道中进行，您可以参与本文中提到的任何 GitHub issue，并加入 CICD SIG 每周四太平洋时间 06:00 举行的[每周例会](https://calendar.google.com/calendar?cid=Z29vZ2xlLmNvbV9iNzllM2U5MGo3YmJzYTJuMnA1YW41bGY2MEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)。