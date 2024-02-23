<!--
title: 关于Kubernetes的预测已经错了
cover: https://cdn.thenewstack.io/media/2024/02/db012df2-predictions-1024x576.jpg
-->

为什么解决 Kubernetes 复杂性问题如此难以捉摸？

> 译自 [Kubernetes Predictions Were Wrong](https://thenewstack.io/kubernetes-predictions-were-wrong/)，作者 Steve Fenton 是 Octopus Deploy 的一位 Octonaut，一位 DORA 社区指导者，拥有20多年软件交付经验的六届微软MVP。

2020年，人们预测Kubernetes会在一年内消失。他们认为会有人创建一个服务，可以减少相邻的选择，并使Kubernetes成为默认的简单选择。每个人都会使用Kubernetes，但很少有人会在底层工作。

我今早检查了一下，它还在这里——底层也都还在。那么，为什么解决[Kubernetes复杂性问题](https://thenewstack.io/why-is-everyone-ignoring-the-day-2-kubernetes-problem/)的办法仍然如此难寻呢？

## 一个充满选择的生态系统

单独来看，Kubernetes不是特别复杂，但广泛的工具、选项和决策组成了它周围的生态系统。您可以在任何地方运行Kubernetes，从本地机器到云端。您可以在单个低功耗机器或成千上万的超大规模节点上运行。您可以使用它来运行一个单体应用或成千上万的微服务。

并没有一种固执己见的Kubernetes使用方式。它被设计得非常灵活。这意味着您可以做出所有决定。您选择精确[配置Kubernetes](https://roadmap.sh/kubernetes)的方式以及使用哪些辅助工具。 

当人们说复杂时，他们谈论的不是Kubernetes本身的复杂性，而是您需要做出的大量决定才能开始使用它。

这还没有考虑软件本身。如果您刚用Go编写了一个在容器中运行的微服务，在Kubernetes中运行它非常简单。如果您有一个遗留的单体应用，它的假设是它将在虚拟机上运行，那么进行大量的工作来弯曲它以便在容器中运行。

难怪当面对如此多的选择时，负责交付解决业务问题的软件的开发人员在信息过载时会觉得压力山大，特别是当综合考虑容器、基础设施自动化和容器注册表的不同选择时，各种文件格式和约定的使用使问题更加复杂。

如果您想骑自行车上班，选择一辆自行车需要大量的研究，所以想象一下分别购买车架、车轮、把手、刹车和变速器。一些骑手会想要这种程度的控制，但当您的工作只是到达目的地时，这种情况就会压倒一切。

## 认知超载和平台团队

Kubernetes会平静地实用化并有效消失的同时也运行我们所有工作负载的观点没有实现。没有人设法为Kubernetes创建一条固执己见的路径，这条路径将关注所有这些选择。

这个简单原因是，神话般的唯一真理之道对大多数应用程序和服务都不起作用。如果不考虑应用程序和组织的上下文，就无法创建一个简单的路径。

这就是为什么平台工程得到了推动。虽然创建一个行业范围内的简化选择之路的可能性不大，但在一个组织内创建这样的路径是完全可行的。

一个最小可行的平台可以是一个列出预设决策并为每个配置文件提供标准示例的维基页面。这可能会发展成一个面向开发人员的门面，允许他们沿着一个简单的维度指定他们需要的内容，例如“大小”，而平台会处理旗标背后的细节。

平台应该提供简化的方法来做正确的事情，同时允许专家开发人员在标准方法不合适时[剥离层层包装](https://thenewstack.io/cloud-native/the-cloud-native-landscape-the-application-definition-and-development-layer/)。

## 减少选项而不限制团队

[Kubernetes不存在单一固执己见路径的事实](https://thenewstack.io/different-approaches-for-building-stateful-kubernetes-applications/)突显了应用程序和组织的上下文因素的重要性。虽然创建一个通用的简化方法不实际，但[平台工程是减少](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/)路上需要做出的许多决定的一种方法，特别是当这些决定并不关键时。

尽管存在感知的复杂性问题，但Kubernetes没有任何减缓增长的迹象。显然，好处超过了采用的痛苦。那么，想象一下，如果采用Kubernetes及其相关移动部件变得更容易，会发生什么？

平台团队可以是在尊重本地上下文的同时创建一个固执己见的Kubernetes设置的关键因素。也许预测没有错误，只是延迟了。

要进一步了解Kubernetes和云原生生态系统，请加入我们3月19日至22日在巴黎举行的KubeCon + CloudNativeCon Europe。