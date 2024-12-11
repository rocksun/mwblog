
<!--
title: DIY Kubernetes是混乱的配方
cover: https://cdn.thenewstack.io/media/2024/12/229babb1-pexels-punttim-52608.jpg
-->

企业必须采用集中式策略才能充分发挥 Kubernetes 的潜力。

> 译自 [DIY Kubernetes Is a Recipe for Mayhem](https://thenewstack.io/diy-kubernetes-is-a-recipe-for-mayhem/)，作者 Tobi Knaup。


# 自己动手部署 Kubernetes 是一场灾难的预兆

今天，在2024年末，CTO和其他企业IT领导者将Kubernetes视为必备技术。每个人都知道，现代的基于容器的应用程序具有可移植性、敏捷性和效率——而Kubernetes是普遍接受的、用于大规模部署和管理它们的解决方案。Kubernetes是一个非常流行的开源项目，这意味着低成本和强大的社区支持。

事实上，一个令人惊叹的有帮助的[开源社区](https://kubernetes.io/)是Kubernetes最佳方面之一，使新手能够快速学习该框架。但就像生活中的许多事情一样，某事物的最佳方面也可能导致你陷入困境。

越来越低的入门门槛使得许多企业肆意妄为，从而抵消了Kubernetes的一些关键优势。企业必须采取战略性的、集中的方法来控制分散的Kubernetes实施，并重回正轨。

## Kubernetes 以及更多更多

凭借丰富的教程、指南和社区论坛，Kubernetes的开源社区在帮助初学者快速掌握复杂的新技术方面做得很好。它还开发了新的云原生工具来降低这种复杂性。很快，新用户就会掌握基础概念——Pod、服务、卷、控制器等等——并自豪地启动他们的第一个分布式应用程序。

问题在于，要有效运行Kubernetes，您不仅需要了解框架本身，还需要了解[整个相关的云原生软件生态系统](https://landscape.cncf.io/)——来处理可观察性、日志记录、网络、安全、存储、IAM（身份和访问管理）等基本要素。每个组件都有其学习曲线和发布计划，集成和故障排除也是其中的一部分。

对于旨在提高敏捷性的解决方案来说，这需要大量的维护工作。企业不希望浪费开发人员或管理员的时间去做琐碎的任务，因此他们经常寻求外部帮助来减轻负担。

## 为什么“让云来做”行不通

许多客户选择来自大型云提供商（如[亚马逊](https://aws.amazon.com/?utm_content=inline+mention) EKS或Microsoft AKS）的Kubernetes解决方案。这些解决方案具有单击式Kubernetes配置的优势，后台具有自动更新和扩展功能——并且还提供一系列托管的附加功能。但是，完全依赖任何一个云提供商都有其缺点。

首先也是最明显的是锁定。这些云Kubernetes产品及其云原生组件是专有的云服务。Kubernetes本身之外的服务是由云提供商而不是开源社区开发的，因此使用它们通常意味着客户开发的基于容器的应用程序不再可移植——到其他云或本地Kubernetes实现。

另一个问题是成本。大型云提供商以较低的初始价格提供Kubernetes和相关服务，但随着您添加集群、存储服务、监控等等，总账单会不断增加。还需要集成和自动化这些服务，从而产生需要维护的代码——从而增加了成本和复杂性。如果运营支出达到临界点，那么在学习专有云服务方面的人力资本投资将被浪费，并且切换平台所需的时间、精力和数据迁移成本将是巨大的。

## 偶然陷入DIY混乱

另一个极端是那些选择[开源路线并尝试自行管理](https://thenewstack.io/5-ways-that-open-source-benefits-api-management/)一切的组织。[CNCF（云原生计算基金会）](https://cncf.io/?utm_content=inline+mention)列出了开发人员和DevOps人员需要组装其Kubernetes实现的所有项目。但是，如前所述，从头开始构建和维护该堆栈会消耗许多[开发人员和管理员周期，这些周期本可以更有效地](https://thenewstack.io/bring-purpose-to-api-product-development-with-apiops-cycles/)应用于其他地方。

更糟糕的是，DIY方法通常会导致分割。各个团队被允许自行构建Kubernetes堆栈和工作流程，而没有标准化概念，也没有跨环境的安全策略一致性。在Kubernetes广泛采用被强制执行但缺乏方法的大型组织中，这导致了数千种缺乏互操作性的不同实现。Kubernetes与在其上运行的应用程序纠缠在一起。

这种混乱的局面降低了效率和应用程序的可移植性，并阻碍了Kubernetes未来优势的实现：大规模资源优化。如今，只有那些将整个基础设施建立在高效容器管理之上的公司才能从中受益，他们可以在高峰时段跨平台扩展容器数量，并在非高峰时段缩减规模以释放资源用于批量处理。这是一个诱人的可能性——如果没有统一的Kubernetes管理，这是不可能实现的。

## 迈向集中式解决方案

[企业前进的道路](https://www.nutanix.com/theforecastbynutanix/podcasts/ai-cloud-native-and-hybrid-cloud-work-together)是创建他们自己的集中式云原生工程团队。这个团队必须认识到，Kubernetes及其相关的云原生解决方案将在各种环境中部署——在VM或裸机上的本地环境、多个公有云以及本地环境。该模型应扩展到混合云或多云部署，其中一个Kubernetes应用程序可以为一个平台开发，并在另一个平台上运行。

该团队的目标应该是建立一个标准的云原生堆栈，并提供一键式部署和自动化维护，就像公共Kubernetes提供商所做的那样，但核心是云原生开源项目。这需要选择合适的[云原生工程平台和工具](https://thenewstack.io/kubecon-panel-how-platform-engineering-benefits-developers/)。最重要的选择标准之一是支持[Kubernetes的声明式集群API](https://cluster-api.sigs.k8s.io/)，这简化了跨私有和公有云平台的一致部署。

这种标准化的集中式方法非常适合绿地部署。但是，当企业已经拥有一个混乱不堪的Kubernetes节点网络时，该怎么办？首先，管理层必须明确，这种碎片化的方法不再可接受。然后，集中式团队可以逐步开始重构和迁移现有的Kubernetes应用程序到新的规范堆栈。

一些开发人员或DevOps工程师可能会反对丢弃他们精心构建的一次性堆栈。这就是为什么邀请那些已经在云原生领域获得专业知识的人参与（或加入）集中式云原生工程团队（如果他们愿意）非常重要的原因。最终，开发人员的生产力将得到提高，整个企业将受益于恢复最初让每个人都对Kubernetes感到兴奋的敏捷性和效率。
