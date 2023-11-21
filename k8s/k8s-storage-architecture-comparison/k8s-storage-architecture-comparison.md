<!--
title: Kubernetes 存储选型：本地vs企业vs容器原生
cover: https://cdn.smartx.com/inc/iomesh/blog/k8s-storage-architecture-comparison.png
 -->

在云计算时代，Kubernetes 已经成为容器编排的首选平台。随着越来越多的企业在 Kubernetes 上运行数据库和中间件，与 Kubernetes 兼容的持久化存储解决方案的需求也在上升。

译自 [Disk vs. Enterprise Storage vs. Kubernetes-Native Storage](https://www.iomesh.com/blog/k8s-storage-architecture-comparison) 。

哪些存储产品适合 Kubernetes，企业可以继续使用本地磁盘和网络存储吗？这些存储解决方案在 Kubernetes 上的表现如何？本文将介绍和对比三种常见的存储选项 - 本地磁盘、企业存储和容器原生存储，分析它们为容器化应用提供存储服务的优劣。

![K8s存储架构比较图](https://cdn.smartx.com/inc/iomesh/blog/K8s-storage-arch-en.png)

## 本地磁盘

直接使用服务器本地磁盘作为 Kubernetes 存储，由于磁盘和应用之间距离近，访问速度快。通过 RAID 可以防止单盘故障导致数据丢失。

但是本地磁盘在可用性、扩展性和资源利用率方面存在明显缺点：

- **无法提供节点级高可用**：物理节点故障时相关应用无法恢复到其他节点，业务系统要增加数据可用性会使整体架构复杂化。
- **无法满足 Kubernetes 的敏捷需求**：存储容量受磁盘空间限制，扩容需要手动添加磁盘、修改 Pod 配置，操作复杂耗时。要提高磁盘可用性还需要部署 RAID，在限定时间和预算内为大量应用提供足够存储空间难度大。
- **运维负担重、资源利用率低**：部署和故障恢复都需大量人工操作。由于无法跨节点共享资源，资源利用率低。

所以本地磁盘仅适合小规模测试或非核心应用数据存储。大规模生产环境中应用困难。

## 企业级存储

通过容器存储接口 (CSI) 将 Kubernetes 与底层存储基础设施集成，来提供持久化存储。该标准使 Kubernetes 可以动态配置不同厂商和型号的存储。根据 GigaOm 的报告 [Key Criteria for Evaluating Kubernetes Data Storage Solutions v4.0](https://gigaom.com/report/key-criteria-for-evaluating-kubernetes-data-storage-solutions/)，这些存储系统主要分为企业存储和容器原生存储两类。

企业存储是指最初面向虚拟化而设计的存储系统，后通过 CSI 插件来支持容器。包括软件定义存储(比如分布式存储)和传统存储(比如集中式存储)。与容器原生存储不同，企业存储不是专门为容器设计，大多来自已有的虚拟化存储。这让企业可以以较少的投入就为 Kubernetes 提供存储。

但是，正如该报告提到，这些系统虽支持 CSI，但与运行其上的新型容器应用架构和时代不同。它们处理容器动态工作负载的能力仍有限。值得注意的是，CNCF 认证的云原生存储同时包括企业存储和容器原生存储。由于两者有明显区别，用户选择和比较时需要谨慎。

### 集中式存储

作为常用的企业存储，相比本地磁盘，集中式存储拥有共享存储池和快照、克隆、灾备等高级功能来提升可用性和资源利用率。但其控制器架构和机架式部署限制了性能和敏捷性。

- 控制器在高并发下容易成为瓶颈；为应对大量并发，需要部署多个存储集群，运维成本激增。
- 以机架式部署时，存储扩容及处理大量动态存储需求的运维难度很大。

### 分布式存储

分布式存储通过在多节点之间分布数据，具有良好的可扩展性和敏捷性。与基于分布式架构的云原生应用集成时，其性能和高可用性优于集中式存储。正如 Gartner 报告 [How Do I Approach Storage Selection and Implementation for Containers and Kubernetes Deployments](https://www.gartner.com/account/signin?method=initialize&TARGET=http%3A%2F%2Fwww.gartner.com%2Fdocument%2F4013517) 提出，容器和 Kubernetes 的存储选择应该“基于可以无限扩展的分布式架构”。

但市面上分布式存储种类繁多，部分产品只是简单重新包装开源方案，其性能、稳定性和 Kubernetes 集成程度往往达不到生产要求。建议重点关注具有自主技术的解决方案，并全面评估其性能、可用性、可靠性、安全性和易用性。

## 容器原生存储

容器原生存储专门面向容器环境设计，与 Kubernetes 高度集成，支持容器级的数据服务和自动化存储管理。相比传统企业存储，其通常更能满足容器化应用的敏捷性和可扩展性需求。

目前，用户可以选择开源的容器原生存储解决方案，如基于 Ceph 的 Rook 和 Longhorn，也可以选择商业的企业级容器原生存储，如 Portworx 和 IOMesh。

两者都可以容器原生方式提供数据服务，但在成本和支持服务方面有区别。一方面，开源解决方案无需采购投入，企业可以在社区帮助下自主应用；另一方面，出现大规模故障时响应不如商业供应商快速。此外，商业解决方案借助更先进的技术，性能和稳定性更优。有关主流容器原生存储性能测试，请参见我们之前的博客 [Kubernetes Storage Capabilities & Performance Analysis: Longhorn, Rook, OpenEBS, Portworx, and IOMesh Compared](https://www.iomesh.com/blog/kubernetes_persistent_storage_comparison)。

## 三种存储选择比较

根据上述分析以及Kubernetes上运行的关键业务(数据服务)对存储服务的基本需求，我们从体系结构、性能、资源共享*、可扩展性、可用性、安全性、易操作性、与Kubernetes集成程度**和成本等多个维度全面比较了本地磁盘、企业存储和Kubernetes原生存储的优势和劣势。

![存储架构比较表](https://cdn.smartx.com/inc/iomesh/blog/three-solutions.png)

> \* 指支持容器跨节点调度和共享存储的能力;
>
> ** 指与 Kubernetes 无缝集成，能充分利用其自动化、标准化等特性的能力。

总体而言，容器原生存储更适合云原生环境。

作为领先的企业级容器原生分布式存储，IOMesh 通过原生 Kubernetes 方式，帮助用户为有状态应用构建弹性、高可靠、高性能的存储池。它降低了采用持久化存储的复杂度，助力企业云原生转型。

欲了解 IOMesh 更多信息，请访问[IOMesh文档](https://docs.iomesh.com/deploy-iomesh-cluster/install-iomesh)中心，也可加入[IOMesh Slack社区](https://iomesh.slack.com/join/shared_invite/zt-pnqohdau-vZnhWMsm0ETSbPA_AJGCRw#/shared-invite/email)获取最新动态和社区支持。

参考资料:

1. [Key Criteria for Evaluating Kubernetes Data Storage Solutions v4.0， GigaOm， 2023](https://research.gigaom.com/report/key-criteria-for-evaluating-kubernetes-data-storage-solutions/)
2. [How Do I Approach Storage Selection and Implementation for Containers and Kubernetes Deployments， Gartner， 2022](https://www.gartner.com/document/4013517)