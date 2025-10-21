<!--
title: Kubernetes：从集市联邦到AI新纪元
cover: https://cdn.thenewstack.io/media/2025/10/88cf1887-bazaar.jpg
summary: Kubernetes已发展十年，形成“集市的联邦”模式。通过SIGs和WGs协作，它成为一个强大、开放且供应商中立的平台，为AI时代做好准备。
-->

Kubernetes已发展十年，形成“集市的联邦”模式。通过SIGs和WGs协作，它成为一个强大、开放且供应商中立的平台，为AI时代做好准备。

> 译自：[Kubernetes: From a Federation of Bazaars to the AI Frontier](https://thenewstack.io/kubernetes-from-a-federation-of-bazaars-to-the-ai-frontier/)
> 
> 作者：Antonio Ojea

回顾过去，很难相信 Kubernetes 项目已经存在十多年了。这让我想起 [Eric S. Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymond) 的旧文章《[大教堂与集市](https://www.oreilly.com/library/view/the-cathedral/0596001088/)》，以及我们过去是如何看待开源的。你要么拥有“大教堂”，由少数开发人员根据一个总体规划建造；要么拥有“集市”，一个混乱但充满活力的创意市场。

那么，Kubernetes 属于哪一种呢？在深入研究其代码库和社区多年之后，我可以说它两者都不是。[Kubernetes](https://thenewstack.io/kubernetes-an-overview/) 是一种新事物：一个集市的联邦。在这里，成千上万热情洋溢的人的工作不是由自上而下的架构师指导，而是由共同的愿景和信任专家发挥最佳水平的结构所引导。这就是我们的秘诀。这也是我们发展如此之快的原因，也是我们现在准备好迎接下一个巨大挑战的原因：成为 [AI](https://thenewstack.io/ai-for-developers-how-can-programmers-use-artificial-intelligence/) 的首选平台。

## **集市的联邦**

你可能会认为这种规模的项目依赖于僵化的自上而下规划，但真正的魔力发生在我们 的[特别兴趣小组（SIGs）](https://github.com/kubernetes/community/blob/master/committee-steering/governance/sig-governance.md)内部。以 SIG-Network、SIG-Node 和 SIG-API-Machinery 为例——这些专注的小组汇集了来自全行业的专家，他们撸起袖子，在各自的特定领域应对严峻挑战。

当然，这些 SIG 并非孤立运作；它们持续进行沟通。[SIG Architecture](https://github.com/kubernetes/community/tree/master/sig-architecture) 是一个自然的论坛，用于讨论跨 SIG 的技术问题，以确保项目保持一个有凝聚力的整体。对于跨越多个 SIG 的特别复杂和模糊的问题，我们组建[工作组](https://github.com/kubernetes/community/blob/master/committee-steering/governance/wg-governance.md)。这些临时小组汇集了来自不同 SIG 的专家，专注于解决一个特定的、具有挑战性的问题，并在任务完成后解散。

所有这些技术工作都建立在一个稳定、支持性的基础之上。这就是项目治理的作用所在。[指导委员会](https://github.com/kubernetes/community/tree/master/committee-steering) 的职责不是发布技术指令；而是确保项目的整体健康，调解争议并保护我们的社区价值观。尽管 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention)（CNCF）为我们的工作提供了一个中立的归宿，但真正的创新源于这种由 SIG 和工作组组成的协作互联网络。

## **十年的演进**

过去十年中，所有这些合作确实取得了丰硕成果。我们的首要任务只是让容器编排在大规模环境下可靠运行。如今，我们拥有一个经过实战检验的平台，它解决了数千用户和数十亿容器的实际问题。

坚实的基础正是 Kubernetes 非常适合 AI 的原因。运行大规模 AI 和机器学习（ML）工作负载会将基础设施的每个部分推向极限。我们的社区模式非常适合为应对这一挑战而发展平台：

## **可移植性和供应商中立性**

随着 Kubernetes 成为 AI 的标准，我们面临碎片化的风险，这会破坏使 Kubernetes 如此出色的“随处运行”承诺。那将把我们带回我们都曾努力摆脱的供应商锁定困境。

这正是我们社区免疫系统发挥作用的地方。[K8s AI 合规性计划](https://github.com/cncf/ai-conformance) 是一项积极的、由社区主导的倡议，旨在防止这种情况发生。它是我们的集市联邦共同创建一套通用标准。目标是定义一个经过认证的基线，说明什么是“AI 就绪”的 Kubernetes 集群。这确保了你今天构建的 AI 应用程序明天可以在任何符合标准的 Kubernetes 发行版上运行，无论是在本地还是在任何云中。这是我们确保平台保持公共利益，而不是成为一堆封闭花园的方式。

## **下一个十年**

[Kubernetes 对 AI 时代的准备](https://thenewstack.io/kubecon-europe-how-google-will-evolve-kubernetes-in-ai-era/)并非偶然。它是十年开放协作、激烈辩论和共同所有权的直接成果。它证明了一种成功融合了个人贡献者的热情和全行业公司战略投资的模式。

在 [Google](https://cloud.google.com/?utm_content=inline+mention)，我们非常自豪能从一开始就参与这一旅程，并继续成为上游项目的主要贡献者。但 Kubernetes 的力量源于其多样性。它是我们所有努力的总和。

**Kubernetes/Kubernetes 顶级企业贡献者（历史总计）**

| **排名** | **公司** | **总贡献数（过去十年）** |
| --- | --- | --- |
| 1 | Google | 1,334,974 |
| 2 | [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) | 527,045 |
| 3 | [VMware](https://tanzu.vmware.com?utm_content=inline+mention) | 361,508 |
| 4 | Microsoft | 246,836 |
| 5 | IBM | 114,501 |

*来源：CNCF DevStats，Kubernetes 项目，截至 2025 年 9 月。*

我们共同构建的平台不仅仅是代码。它是一个强大、开放且不断发展的[下一代智能应用程序](https://thenewstack.io/whats-next-in-building-better-generative-ai-applications/)的基础。我迫不及待地想看到未来 10 年我们能在此基础上构建什么。