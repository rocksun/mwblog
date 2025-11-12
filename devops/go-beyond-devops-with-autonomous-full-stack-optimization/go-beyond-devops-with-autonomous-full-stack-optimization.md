<!--
title: 超越DevOps：全栈自主优化，开启智能运维新篇章
cover: https://cdn.thenewstack.io/media/2025/11/ea2bebb6-beyond-devops-autonomous-full-stack-optimization.jpg
summary: 云端过度配置普遍存在，源于开发者为可靠性过度配置及配置复杂性。Akamas提供AI驱动的全栈优化方案，弥合团队协作差距，实现持续自动化优化，提升效率与可靠性。
-->

云端过度配置普遍存在，源于开发者为可靠性过度配置及配置复杂性。Akamas提供AI驱动的全栈优化方案，弥合团队协作差距，实现持续自动化优化，提升效率与可靠性。

> 译自：[Go Beyond DevOps With Autonomous Full-Stack Optimization](https://thenewstack.io/go-beyond-devops-with-autonomous-full-stack-optimization/)
> 
> 作者：Charles Humble

在本地数据中心时代，采购周期以月计，[过度配置](https://thenewstack.io/how-to-avoid-overprovisioning-java-resources/)是一种合乎逻辑的风险管理策略——它司空见惯，以至于没有人会多想。

理论上，公共云提供商提供的弹性实用计算的兴起应该让我们摆脱了过度配置，但[情况并非如此](https://thenewstack.io/automation-can-solve-resource-overprovisioning-in-kubernetes/)。我曾合作过的公司通常过度配置至少50%，即使在云端也是如此。[僵尸服务器](https://thenewstack.io/zombie-resources-eat-up-your-cloud-budget/)（曾经完成有益工作但现在已不再使用）比比皆是。

## 云端过度配置为何在弹性计算下依然存在

自动化优化平台供应商 [Akamas](https://akamas.io/?utm_content=inline+mention) 的首席运营官 Enrico Bruschini 认为他知道为何过度配置仍然是一个如此大的问题。

“DevOps革命和平台团队的兴起让开发者负责。开发者不想在半夜被叫醒，也不想被指责以不可靠的方式配置应用程序。所以他们要求过度配置，”他在一次采访中说。

“我们看到两个相关趋势：嵌套在堆栈每一层的配置参数数量不断增加，以及发布周期缩短。这使得任何人越来越难研究出正确的配置是什么。根据不断变化的需求持续调整，简直不可思议，”Bruschini 解释道。

正确[调优像Java虚拟机 (JVM) 这样的运行时确实非常困难](https://akamas.io/events/java-on-kubernetes-lessons-in-performance-engineering-with-akamas-and-microsoft/)，而且长期以来，调优JVM需要专业知识，而这些知识通常只掌握在典型组织中的少数开发者手中。结果可能是大量的配置复制粘贴。

“团队中会有人举手说，‘我非常了解Kubernetes、JVM或Node.js；让我看看，’”Bruschini 说。“他们会进去，调整一些东西，然后在接下来的几年里，就会有一个每个人都在复制粘贴的‘超级英雄配置’。它变成了一个静态蓝图，导致应用程序在设计上配置不佳。

“你可以随意过度配置，但如果你没有调优你的运行时配置，你只是在扩大低效率——如果你使用Kubernetes [Horizontal Pod Autoscaler (HPA)](https://thenewstack.io/reduce-kubernetes-costs-using-autoscaling-mechanisms/)，情况也同样适用，”他说。

## DevOps文化 vs. 可靠性和成本优化

这不仅仅是昂贵。从[环境角度](https://thenewstack.io/ebooks/cloud-infrastructure/developers-guide-to-cloud-infrastructure-efficiency-and-sustainability-2/)来看，过度配置的硬件也是不好的，并且构成可靠性风险。Bruschini 认为，由于不同团队的不同动机及其各自的可见性，问题变得更加复杂。

“我们反复观察到客户的平台团队、SRE [站点可靠性工程] 团队和开发团队之间存在裂痕，”他说。“平台团队优化成本，并热衷于直接配置其平台。SRE团队旨在降低风险。但这两个团队的触及范围都有限。他们可以触及基础设施层和他们构建的平台，但他们几乎无法触及工作负载和运行时配置，比如JVM堆大小、垃圾收集器选择等等；那是应用程序团队的职责。”

Bruschini 指的是信息孤岛——这正是DevOps试图根除的东西。困难在于，人类会自然而然地围绕明确的激励机制形成群体。ClearBank 担任技术产品负责人的经验丰富的平台团队负责人 Russell Miles 认为，这意味着：“打破信息孤岛不仅需要精力和意愿，而且需要持续投入以确保它们保持分解状态。”

## FinOps和可持续性反馈循环

Miles 表示，围绕成本和适用性的挑战需要被视为DevOps文化的延伸，而不是冲突。DevOps的反馈循环是根据观察、判断、决策、行动 (OODA) 循环建模的，这是一种由军事战略家 John Boyd 开发的四阶段决策模型。

“DevOps文化强调反馈循环和持续改进，”Miles 在采访中说。“但它在某些组织中做得不太好的地方是平衡可持续性和成本等反馈循环。”

> 围绕成本和适用性的挑战需要被视为 DevOps 文化的延伸，而不是冲突。

Miles 解释说，FinOps和可持续性反馈循环通常极其不成熟，即使在那些理解其价值的组织中也是如此。在平台团队的赋能下，ClearBank 引入了诸如“每笔支付交易的碳足迹”等指标。

“我们在做出决策时可以看到碳减排，并将其与业务挂钩，”Miles 说。然而，这仍处于早期阶段。“在ClearBank，我们已经看到你通常首先发展OODA循环中的‘O’（观察、判断）阶段，所以如果一个工具能为开发者提供‘决策’和‘行动’部分，那将是非常棒的。”

## 弥合运行时优化差距

现有许多工具可以帮助开发者优化代码，但 Bruschini 认为市场存在空白，需要一种工具来帮助进行协调的全栈优化，以提高可靠性、性能并降低成本。这一观察促成了 Akamas 平台的诞生，该平台目前有两个模块：[Akamas Offline](https://akamas.io/offline-optimization/) 和 [Akamas Insights](https://akamas.io/insights/)。

Akamas Offline 旨在在负载测试结束后执行供应商所谓的优化研究。要使用它，您首先定义优化目标、任何服务水平协议 (SLA) 和其他边界，然后通过生成流量的负载测试来运行研究。

“该工具将提供不同迭代的配置，并附带解释说明原因，以及所有必要的配置，您可以获取并应用，”Bruschini 说。

Akamas Insights 于今年早些时候推出测试版，现已普遍可用，它是一款AI驱动的软件即服务 (SaaS) 解决方案，旨在帮助组织轻松地将开发者、SRE 和平台工程师团结在一个共同目标周围：提供可靠、高效的服务。这是通过提供可直接应用的工作负载、运行时和Kubernetes配置，根据生产环境调优整个堆栈来实现的。

“我们聚焦于分散在整个堆栈中的众多优化机会，”Bruschini 说。“Insights模块的诞生是与许多公司交流后发现他们对优化机会所在之处一无所知的结果，”他补充道。

Akamas Insights 使用现有的可观测性数据，这意味着无需安装额外的代理。该供应商正在为每个可观测性工具单独构建集成。目前，[Datadog](https://www.datadoghq.com/?utm_content=inline+mention)、[Dynatrace](https://www.dynatrace.com/?utm_content=inline+mention) 和 [Prometheus](https://thenewstack.io/prometheus-and-opentelemetry-just-couldnt-get-along/) 均受支持，并计划与其他可观测性工具集成。

## 两阶段演进：从赋能到自动化

该供应商的长期愿景是两阶段演进，Bruschini 将其描述为“首先赋能团队，然后自动化并减少他们的工作量。”

“我们从赋能开始，因为我们厌倦了看到SRE或平台团队追着应用程序团队在各层之间正确配置事物，”他说。

“SRE现在可以轻松发现不可靠的应用程序，并从Akamas发起一个PR [pull request]，其中包含所有推荐的更改。开发者可以审查并批准PR，在保持控制的同时，轻松优化整个堆栈。”

然后，随着团队获得信心，他们可以允许Akamas自动化该过程，直到“优化成为原生平台能力：自动化、持续、因此轻松且始终安全。”

Bruschini 相信他可以将持续、实时、AI驱动的优化应用于Akamas客户的生产环境。这项技术正在为这一现实做好准备，Kubernetes原地Pod大小调整是朝着这个方向迈出的一步。

## 弥合云效率日益扩大的差距

随着大型企业努力应对快速交付、可靠性和成本优化等相互竞争的压力，过度配置问题没有自行解决的迹象。随着AI编程助手加速开发周期和性能工程角色逐渐淡出，应用程序交付速度与运行时效率之间的差距持续扩大。

像Akamas这样的工具认识到，优化不再是事后考虑，也不能依赖偶尔的“超级英雄配置”——它必须是自动化、持续的，因此是轻松且始终安全的。

Bruschini 关于持续AI驱动优化的愿景是否会成为行业标准仍有待观察。但有一件事是清楚的：随意过度配置云资源、僵尸服务器以及所有相关问题的时代不能无限期地持续下去。