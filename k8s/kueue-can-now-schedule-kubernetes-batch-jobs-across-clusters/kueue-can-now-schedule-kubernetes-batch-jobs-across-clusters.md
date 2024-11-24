
<!--
title: Kueue现在可以跨集群调度Kubernetes批处理作业
cover: https://cdn.thenewstack.io/media/2024/11/59ad16fe-kueue.png
-->

“MultiKueue”测试版多集群作业调度功能允许管理员将工作负载放置在远程集群上。

> 译自 [Kueue Can Now Schedule Kubernetes Batch Jobs Across Clusters](https://thenewstack.io/kueue-can-now-schedule-kubernetes-batch-jobs-across-clusters/)，作者 Joab Jackson。

来自 Kubernetes [批处理工作组](https://github.com/kubernetes/community/blob/master/wg-batch/README.md) 的一个批处理调度器现在能够在外部集群上调度工作负载，这有望简化运营管理，并可能扩大可用计算资源的范围，这对于具有计算密集型 AI 工作负载的组织来说无疑是一个非常需要的特性。

这项名为 [MultiKueue](https://kueue.sigs.k8s.io/docs/concepts/multikueue/) 的新 Beta 功能在上周的 [KubeCon+CloudNativeCon 北美峰会](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 主题演讲中由 [CERN](https://home.cern/science/computing) 的平台工程实验室工程师 Ricardo Rocha  巧妙地演示，他对 [大型计算工作负载](https://thenewstack.io/how-cern-accelerates-with-kubernetes-helm-prometheus-and-coredns/) 并不陌生。

他表示，此类软件可以在帮助“管理非常复杂的基础设施，包括跨多个管理域的多个集群”方面大有帮助。


## 什么是 Kueue？

[Kueue](https://kueue.sigs.k8s.io/) 是一个 Apache 2 许可下的 [开源项目](https://github.com/kubernetes-sigs/kueue)，它是一个 Kubernetes [资源配额管理器](https://kueue.sigs.k8s.io/docs/overview/)，为 Kubernetes 集群提供了一个工作负载队列，该队列可以是弹性的，也可以是异构的。

它决定何时 [创建 Pod](https://kueue.sigs.k8s.io/docs/concepts#admission) 以启动作业，以及何时停止作业并删除其 Pod。它还可以抢占作业。这套 API 提供了用于设置配额和策略的语言，以便在租户之间公平共享。

![](https://cdn.thenewstack.io/media/2024/11/6f076d43-kueue-theory-of-operation.svg)

*摘自 [Kueue 概述](https://kueue.sigs.k8s.io/docs/overview/) 页面。*

不同类型的计算资源，例如 GPU 或基于竞价型实例的虚拟机，被描述为“ResourceFlavors”或对象，然后可以使用这些对象来适应资源的工作负载，并且 [也作为对象捕获](https://www.youtube.com/watch?v=HWTNCTaKZ_o)。

Kueue 可以安装在任何 vanilla Kubernetes 集群之上。它建立在现有的 Kubernetes 自动缩放、Pod 到节点调度和作业生命周期管理技术之上。

## 使用 MultiKueue 进行 Kubernetes 调度

Kubernetes 本身会以随机顺序调度队列中的多个作业。它还会调度部分工作负载，考虑到需要执行的工作负载类型，这可能会出现问题。

Kueue 执行全有或全无调度。工作负载会排队，并且只有在有足够的资源时才会完整运行。

其他的全有或全无调度工具包括 [Apache YuniKorn](https://yunikorn.apache.org/) 和 [Volcano](https://volcano.sh/en/)。

但 Kueue 的优势还在于它支持不同团队的多个队列。每个研究团队都可以在自己的命名空间中获得集群的专用部分，而 Kueue 提供了在每个团队的部分未被使用时临时共享的功能。

在主题演讲中，Google 的软件工程师 Marcin Wielgus 指出，考虑到 AI 处理作业的规模和运行它们所需的 GPU 的相对稀缺性，这种排队可能非常有价值。

借助 MultiKueue，Kueue 不仅可以管理本地集群，还可以管理来自外部云提供商和 [其他高性能计算](https://link.springer.com/article/10.1007/s41781-020-00052-w) (HPC) 中心的集群。

可以将作业提交到控制集群，该集群会在多个可用集群中的一个中搜索主集群，并在找到足够的容量时放置作业。

如果作业需要 GPU，则在工作负载描述中指定该限制，因此 Kueue 将知道仅将该作业放置在具有足够 GPU 的节点上。


## 远近集群

目前，MultiKueue 是 Kueue v.9 中默认启用的 Beta 功能。

CERN 是一个认真考虑整合 MultiQueue 的组织。

欧洲核研究组织 CERN（代表“Conseil Européen pour la Recherche Nucléaire”）目前正在设计其下一个粒子加速器。目前，该研究机构每年产生 100PB 的数据，但随着新的粒子加速器的到来，这个数字可能会增长 10 倍或更多。

Rocha 是一个工程团队的成员，该团队正在研究构建一个系统，以便针对多个资源 [调度作业](https://arxiv.org/abs/2309.06782)，这些资源可以是内部资源、公共云提供商，也可以是通过 CERN 的 [全球 LHC 计算网格](https://home.cern/science/computing/grid)（一个遍布全球的 [HPC 超级计算机](https://thenewstack.io/xs-colossus-supercomputer-changes-the-sc500-performance-game/) 网络）提供的资源。

这样一个系统将用于使用参数优化的批处理作业，并与现有调度程序（例如 Slurm 和 KubeFlow）协同工作，通过 Kueue 入口点集中管理。

Rocha 演示了该项目如何与 MultiKueue 协同工作。在仪表板中，Rocha 展示了一些活动集群，一个在内部，一个位于德国。

这些集群的所有作业都已排队并出现在主集群中。Rocha 启动的一个作业对于本地集群来说太大了，Kueue 自动在具有可用计算资源的远程集群上启动了它。

“我们的想法是提交作业，而不用关心它们在哪里运行，”Rocha 说。
