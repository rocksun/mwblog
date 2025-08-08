
<!--
title: 平台工程遇阻：为何基础设施至关重要
cover: https://cdn.thenewstack.io/media/2025/07/91f798ab-jakub-zerdzicki-agkspo5oiyg-unsplash-scaled.jpg
summary: 平台工程正朝着基础设施平台工程(IPE)演进，IPE关注构建云原生环境的自助、可扩展且具成本效益的基础设施平台。实施IPE的关键步骤包括审核平台、转变设计、定义策略及采用Kubernetes原生工具。
-->

平台工程正朝着基础设施平台工程(IPE)演进，IPE关注构建云原生环境的自助、可扩展且具成本效益的基础设施平台。实施IPE的关键步骤包括审核平台、转变设计、定义策略及采用Kubernetes原生工具。

> 译自：[Platform Engineering Is Failing — Here's Why Infrastructure Comes First](https://thenewstack.io/platform-engineering-is-failing-heres-why-infrastructure-comes-first/)
> 
> 作者：Lukas Gentele

我们现在已经进入平台工程应用的几年，它已被广泛接受为组织加速软件开发和过渡到现代软件方法的最佳方式。Gartner 预计，到 2026 年，大约[80% 的组织将拥有专门的平台工程团队](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering)。

然而，尽管受到了极大的关注，并且取得了一些显著的成功，但许多组织发现，他们最初的平台工程工作并没有达到他们的期望。这并不是因为[平台工程方法是错误的](https://thenewstack.io/youre-doing-platform-engineering-wrong-probably/)，而是因为平台团队的关注范围过于狭窄。

## 为什么平台工程团队会忽视基础设施基础

对于大多数组织来说，平台工程是一项重要的事业。你可能想从一张白纸开始，但你的组织可能拥有多个开发团队，他们的关注点差异很大，而且在硬件、软件和工具方面也有大量的投资。以下是平台团队常犯的四个错误领域。

**对基础设施的关注不足**：许多团队将其精力集中在内部开发者平台（IDP）上。这是有道理的，因为那是[开发者花费所有时间的地方](https://thenewstack.io/why-traditional-logging-and-observability-waste-developer-time/)，但是由于对 IDP 的过度关注，底层基础设施变成了事后才考虑的问题。当基础薄弱时，整个建筑都会摇摇欲坠。

**未能平衡开发者体验 (DX) 与成本：** 对于刚起步的平台团队来说，DX 和开发者生产力往往是优先考虑的。但是，如果你的成本无法持续，你的平台最终将会受到损害，尤其是在你快速增长的情况下。

例如，Ada 最初尝试让[每个人共享两个开发集群](https://www.vcluster.com/case-studies/ada-cx)，但发现开发者们在互相覆盖彼此的工作。该公司最初考虑给每个开发者自己的集群，但意识到这将太昂贵，而且开发者难以管理。

**安全、合规性和治理是事后才考虑的：** 鉴于当今的监管环境和日益增长的网络威胁，安全、合规性和治理至关重要，需要从一开始就构建到你的平台中。在事后才添加它们，你将永远在追赶，并承担更大的风险。

**未能使平台架构与未来需求保持一致：** 通常，平台[团队最终会创建通用平台来支持](https://thenewstack.io/how-team-topologies-supports-platform-engineering/)各种架构，包括遗留架构和现代架构，这并非他们自己的过错。随着越来越多的工作负载[迁移到 Kubernetes](https://thenewstack.io/how-to-jump-start-your-stalled-kubernetes-migration/)，这些平台变得越来越低效。

## 基础设施平台工程：超越开发者工具的演变

像任何新学科一样，[平台工程也在不断发展](https://thenewstack.io/platform-engineering-is-devops-evolved-new-report-shows/)。各组织正在扩展平台工程的概念，以明确包含基础设施[平台工程 (IPE)，从而摆脱对 DX 和 IDE 的过度关注](https://thenewstack.io/the-pillars-of-platform-engineering-part-5-orchestration/)。

IPE 专注于构建专为云原生环境量身定制的自助服务、可扩展且具有成本效益的基础设施平台。与主要旨在简化开发者工作流程和抽象基础设施复杂性的方法不同，IPE 明确关注提供可扩展的、策略驱动的和具有成本意识的 [Kubernetes 基础设施，从而使你的团队能够高效地运营](https://thenewstack.io/understanding-the-kubernetes-operator-pattern/)。IPE 解决了上面概述的问题。

**将基础设施作为头等大事：** 通过 IPE，你优先考虑底层基础设施，确保从一开始就构建多租户、隔离、成本效益和治理。

**效率和生产力：** IPE 优化了基础设施效率，减少了浪费，并确保了具有成本意识的扩展。

**策略驱动和安全设计：** 安全、合规性和治理已集成到平台中，从而实现了安全的共享基础设施，该基础设施消除了[运营瓶颈，同时控制了](https://thenewstack.io/chaos-to-control-3-steps-for-automating-incident-management/)成本。

**专为 Kubernetes 原生工作负载而构建：** IPE 专为过渡到 Kubernetes 的组织的动态环境、临时工作负载和多云策略而定制。

## 基础设施平台工程实施入门

好消息是，许多组织可以从他们今天所处的位置迁移到 IPE，而无需从头开始。这就像抬起房子，在下面建造一个新的坚实的基础。

如果你的团队已经采用了 [Kubernetes 并且对现有成本](https://thenewstack.io/how-to-gain-visibility-into-kubernetes-cost-allocation/)、工作负载和故障具有合理的可见性，那么你应该有资格开始使用。关键是识别当前平台中的结构性弱点，以确定在哪里应用 IPE 原则。以下路线图提供了一个有用的起点。

| IPE 入门：实用路线图 | |
| --- | --- |
| 步骤 1： | 审核你的平台，找出成本、治理和基础设施故障点。 |
| 步骤 2： | 转变平台设计，将基础设施视为一种产品。 |
| 步骤 3： | 从第一天起就定义策略即代码和成本指标。 |
| 步骤 4： | 采用 Kubernetes 原生工具（虚拟 Kubernetes、分层多租户等） |

如果你的组织将受益于 IPE，请问问自己，你当前的平台团队是否已准备好执行此路线图，并考虑添加或引入基础设施专家来提供帮助。