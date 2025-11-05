
<!--
title: 冗余的救赎：云宕机冲击能否化解？
cover: https://cdn.thenewstack.io/media/2025/10/df99b3e5-sophia-shi-y0efzg2_ku8-unsplash-scaled.jpg
summary: AWS宕机事件凸显服务互联性。全面冗余因复杂性难以实现，引入新挑战。组织需增强可见性，绘制依赖图谱，以提高数字韧性，快速应对中断。
-->

AWS宕机事件凸显服务互联性。全面冗余因复杂性难以实现，引入新挑战。组织需增强可见性，绘制依赖图谱，以提高数字韧性，快速应对中断。

> 译自：[The Promise of Redundancy: Can the Impact of a Cloud Outage Be Avoided?](https://thenewstack.io/the-promise-of-redundancy-can-the-impact-of-a-cloud-outage-be-avoided/)
> 
> 作者：Joe Vaccaro

[10月20日的AWS宕机事件](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/)有力地提醒了我们当今应用程序和服务的互联程度。从银行到流媒体，从医疗保健到物流，各种规模和行业的组织都依赖于公共云和其他第三方服务的复杂网络。正如我们所见，一次中断可以迅速级联，不仅影响一家公司，还会影响整个行业和数百万终端用户。

面对这种中断，我们自然会问：为什么没有更多公司能够建立有效的冗余来保护自己免受此类中断的影响？答案在于复杂性。

## **现代应用程序背后的隐性复杂性**

客户和员工所期望的无缝数字体验，是由密集的基础设施和服务组件网络驱动的，这些组件通常来自第三方。现代应用程序依赖于无数底层服务，包括云平台、托管数据库、无服务器功能和外部API，这些服务本身可能又依赖于相同的[云提供商或类似的外部依赖项](https://thenewstack.io/cloud-dependencies-need-to-stop-f-ing-us-when-they-go-down/)。这种错综复杂的网络使得构建完全冗余的系统在[操作上和经济上都充满挑战](https://thenewstack.io/building-reliable-ai-requires-a-lot-of-boring-engineering/)。

即使有工程化的故障转移，例如切换到另一个云提供商区域，这些策略也远非简单明了。每个额外的冗余层都会引入其自身的[依赖项和管理](https://thenewstack.io/unlocking-the-power-of-automatic-dependency-management/)挑战。

## **完全冗余是不可能的**

对于那些已经部署了部分冗余的组织来说，知道何时调用故障转移是一个困难的权衡。冗余可以通过多种方式架构：维护多个独立的故障区域，其中实例和工作负载[分布在不同的云](https://thenewstack.io/why-developers-need-to-care-about-distributed-cloud-computing/)提供商（多云）之间；或者采用主动-主动架构，其中工作负载并行运行，如果其中一个变得不可用，服务仍能维持。例如，一个电子商务平台可能会在同一[云提供商的](https://thenewstack.io/how-to-ensure-cloud-native-architectures-are-resilient-and-secure/)两个不同区域复制其关键数据库和应用程序服务器，以确保在一个区域发生故障时服务的连续性。

然而，故障转移和补救措施本身可能具有破坏性，并且需要时间来执行。数据一致性、会话状态同步和DNS传播延迟都可能在转换期间引入复杂性并导致潜在的服务降级。在某些情况下，如果辅助环境没有完全更新，或者它与主环境共享隐藏的依赖项，故障转移可能会产生新的问题。

做出正确决策取决于理解故障的范围（局部或广泛）、持续时间（临时或长期）、底层依赖项的行为以及对用户和业务成果的实际影响。如果没有这种洞察力，补救措施可能会延迟，甚至通过中断用户或加剧技术挑战来使情况恶化。

## **可见性和依赖项映射的必要性**

为应对这些挑战，组织应优先提高对其所依赖环境的可见性，无论是自行管理还是由第三方提供。映射应用程序和服务依赖项对于[发现隐藏风险](https://thenewstack.io/leaky-data-pipelines-uncovering-the-hidden-security-risks/)（例如未知的单点故障）以及制定冗余策略至关重要。在发生故障期间，实时了解每个依赖项的运行状况以及终端用户受到的影响，对于做出快速、明智的决策至关重要。

提供商的状态[更新可能会延迟或过于笼统](https://thenewstack.io/linkerd-service-mesh-update-addresses-more-demanding-user-base/)，无法解决特定公司的情况。直接了解服务行为和用户影响使组织能够清晰沟通并果断行动，最大程度地减少业务中断。

## **数字韧性的作用**

云提供商的宕机事件提醒我们，韧性不仅取决于智能架构，还取决于整个服务的智能和可见性。随着组织继续采用云、SaaS以及现在的AI工作负载（这些架构通常会增加依赖项的复杂性），我们必须认识到，每种技术都带来了巨大的机遇和新型风险。

应对宕机事件和其他中断的能力，不仅取决于冗余（冗余永远无法做到完美），还取决于组织在压力下有效观察、理解和响应其环境的能力。这种环境意识需要端到端可见性，使其成为数字韧性的基石。