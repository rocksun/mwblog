<!--
title: 能让 Kubernetes “隐身”吗？揭秘 AWS 为何将其视为使命
cover: https://cdn.thenewstack.io/media/2026/04/44a50300-thumbnail-4.png
summary: AWS EKS 首席产品经理 Jesse Butler 探讨了如何通过 Karpenter 等项目简化 Kubernetes，使其像 Linux 一样成为不可见的基础设施，并强调了社区维护者对云原生生态的重要性。
-->

AWS EKS 首席产品经理 Jesse Butler 探讨了如何通过 Karpenter 等项目简化 Kubernetes，使其像 Linux 一样成为不可见的基础设施，并强调了社区维护者对云原生生态的重要性。

> 译自：[Can you make Kubernetes invisible? Here's why AWS is on a mission to do it.](https://thenewstack.io/aws-kubernetes-invisible-simplicity/)
> 
> 作者：Adrian Bridgwater

在本期 *The New Stack Makers* 中，我们采访了 [AWS Elastic Kubernetes Service](https://aws.amazon.com/eks/) 的首席产品经理 [Jesse Butler](https://www.linkedin.com/in/jesse-butler/?skipRedirect=true)。

凭借在 Karpenter、Kro 和 Cedar 等多个关键云原生计算基金会（CNCF）项目中的深度参与，Butler 在阿姆斯特丹举办的 KubeCon + CloudNativeCon 欧洲 2026 大会上阐述了他对更高效云原生计算的愿景。

VIDEO

Butler 于 2020 年加入 AWS，他表示任期内的使命一直是让 Kubernetes 变得更易于使用。凭借他在 Unix 领域的背景，他坚定地相信开源软件开发及其让技术大众化的能力。

谈到开源领域的现状，Butler 同意在开放平台中“商业化成分是恰当的”，但归根结底，一切都取决于社区驱动的活动以及维护者和提交者的工作。

## 制定行业规范

“这确实是 CNCF 做得非常出色的地方之一，它帮助制定、标准化并汇聚了这个社区，使其成为一个正式的、受治理的实体。但公司也可以发挥非常重要的作用；仅仅因为一个团队在 [GitHub](https://thenewstack.io/github-launches-its-coding-agent/) 中解决了一些问题，并不意味着它对每个人都可行，因此需要一种流动的融合，让我们看到开源技术与专有核心基础创新之间的综合体，”Butler 说道。

Butler 承认软件工程师和厂商共同协作开发未完成的软件产品的价值，他提醒我们，通常是 CNCF 的成员组织对项目进行必要的打磨，使其达到可用的状态。

“但只要想想这里的规模，我的意思是，CNCF 几乎是地球上曾存在过的最大的软件工程项目，它也是更广泛的 Linux 基金会的一部分，”Butler 说。“我的感触是，并不是每个组织都想以同样的方式做出贡献，但这就是开源的核心精神，即选择的自由。如果我们长期想要摆脱这些支柱式的、专有的堆栈，这就是应该拥抱的正确方法论。”

> CNCF 几乎是地球上曾存在过的最大的软件工程项目，它也是更广泛的 Linux 基金会的一部分。

## 容器化：理所当然的选择

谈到行业近年来的进展，Butler 表示他在 AWS 的团队非常欢迎 Kubernetes 让开发人员能够实现大规模编排的能力。目前大约有 [80% 的企业在生产环境中深度使用 Kubernetes](https://www.cncf.io/reports/cncf-annual-survey-2024/)，开源生态系统已完全接受了这项技术，但复杂性依然无处不在。

这一现实显然促使 Butler 将他在 KubeCon 欧洲 2026 的演讲题目定为“从复杂到清晰，让 Kubernetes 变得不可见”。他的意图是将其与 Linux 进行类比，他说 Linux “基本已经退居幕后”，成为了一种被公认的公用事业。他认为我们可以通过多种方式解决复杂性挑战，从抽象服务到将功能合并或整合为更易于消费的模块。

## Karpenter、Kro 和 Cedar

在介绍他在 Karpenter、Kro 和 Cedar 项目上的工作时，Butler 解释了 Karpenter 如何处理节点生命周期管理。他说，这个项目揭示了一个启示：最佳的自动扩缩容方法是实时配置节点。这意味着工程师不必担心自动扩缩容，这就是 [Karpenter](https://github.com/aws/karpenter-provider-aws) 的工作方式。该技术根据工作负载压力运行：当开发人员调度任务且没有可用节点时，它会检查指定的配置，创建一个节点，然后将其加入集群。

谈到项目 [Kro](https://github.com/kubernetes-sigs/kro)（Kubernetes 资源编排器）时，Butler 自嘲是“机场休息室里发牢骚的老头”，抱怨自己不得不编写自定义控制器来将集群中的资源粘合在一起。

“在那次飞行中，我编写了现在 Kro 的第一个实例，并在集群中的组合和资源编排方面采取了一些非常新颖的方法，并立即意识到这是整个生态系统都能受益的东西，”Butler 说道。

最后是 [Cedar，一种开源策略语言](https://www.cedarpolicy.com/en)和评估引擎，由 AWS 捐赠给了 CNCF。该技术处理细粒度的授权控制，且并非 Kubernetes 特有，因此适用于各种云原生策略任务。

## 开源无处不在

“总的来说，我必须说维护者需要更多的关爱。当这些人在修复容器调试问题时，没有人是想以此发财的，对吧？开源现在无处不在，从你的笔记本电脑、智能手机到你的飞机座位，但这么多技术背后的人并不是为了荣誉而做这些，所以我们必须照顾好这个生态系统，”乐观的 Butler 补充道。

随着简化 Kubernetes 并持续维护 CNCF 项目开放性的动力不断增强，Butler 的结语分量十足。展望未来，他希望智能体自动化（Agentic Automation）与人类创造力的结合，能让世界各地的用户拥有更好的开源软件。