*这篇文章摘自 Janakiram MSV 即将出版的 TNS 电子书《[在 Kubernetes 上运行虚拟机：企业迁移的实践路线图](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)》。立即预注册，以便在本月晚些时候发布时抢先阅读此书。*

多年来，企业 IT 格局一直在经历着根本性的变革。各行各业的组织都在采纳云原生技术，拥抱容器，并使其应用程序交付实践现代化。这种转变不仅仅是技术变革，它反映了一种新的软件构建和运营方法，优先考虑敏捷性、可扩展性和弹性。

Kubernetes 已成为这场变革的基础。[Google](https://cloud.google.com/?utm_content=inline+mention) 内部的容器编排系统，如今已成为现代应用程序的通用控制平面。各组织正在以 [Kubernetes](https://thenewstack.io/kubernetes/) 为标准——不仅用于新的云原生应用程序，还将其作为所有工作负载（包括在虚拟机 (VM) 中运行的传统应用程序）的主要平台。

最近的市场事件加速了这一演进。[Broadcom](https://www.vmware.com/?utm_content=inline+mention) 于 2023 年收购 [VMware](https://tanzu.vmware.com?utm_content=inline+mention) 创造了一个关键时刻，将渐进式的现代化进程转变为一项紧迫的业务优先事项。向[订阅许可、产品捆绑和大幅涨价](https://thenewstack.io/vmware-users-adjust-to-broadcom-subscription-licensing/)的转变，迫使许多组织加快了其云原生采纳时间表。

然而，这种紧迫性也创造了一个机会。已经投资于 Kubernetes 的组织现在有了充分的业务理由，可以将其基础设施整合到一个单一的开放平台上。

## 虚拟机挑战

尽管容器化势头强劲，但大多数企业仍然运行着数千台虚拟机。这些工作负载代表着数十年的应用程序开发，并且通常包含无法轻易重写或替换的关键业务系统。传统应用程序、具有特定操作系统 (OS) 要求的商业软件以及复杂的单体系统都要求基于 VM 的部署模型。

这给 Kubernetes 采用者带来了根本性的挑战。如何在标准化云原生基础设施的同时，维护您的业务所依赖的虚拟机？

> 如何在标准化云原生基础设施的同时，维护您的业务所依赖的虚拟机？

传统方法迫使组织维护独立的基础设施堆栈：VM 工作负载在管理程序平台上运行，而容器化应用程序在 Kubernetes 集群上运行。这种划分会带来操作复杂性、工具重复以及资源利用效率低下。由于每个堆栈都需要独特的技能组合，因此不同的团队需要管理和运营这些环境。

## KubeVirt 解决方案

[KubeVirt](https://thenewstack.io/open-source-kubevirt-vm-management-with-kubernetes-is-a-work-in-progress/) 通过扩展 Kubernetes 来编排虚拟机和容器，从而解决了这一挑战。作为 [云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 项目，KubeVirt 提供了一种标准化方式，可以使用与容器化工作负载相同的 API、工具和操作实践来运行 VM。

这种方法实现了真正意义上的基础设施整合。团队可以通过一个单一的控制平面来管理 VM 和容器，使用一致的安全策略、网络配置和资源管理实践。结果是操作简化，资源利用效率更高。

KubeVirt 还提供了一条实用的迁移路径。组织可以将现有 VM 迁移到其 Kubernetes 平台，而无需更改应用程序。这种“提升和转移”（lift and shift）方法能够立即实现基础设施整合，从而为将应用程序现代化作为独立计划留出时间。

[![在 Kubernetes 上运行虚拟机：企业迁移的实践路线图](https://cdn.thenewstack.io/media/2025/10/8a2207e3-runningvirtualmachinesonkubernetesapracticalroadmapforenterprisemigrations.png)](https://cdn.thenewstack.io/media/2025/10/8a2207e3-runningvirtualmachinesonkubernetesapracticalroadmapforenterprisemigrations.png)

## 您将学到什么

即将出版的电子书《**[在 Kubernetes 上运行虚拟机：企业迁移的实践路线图](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)**》将为使用 KubeVirt 在 Kubernetes 上实现 VM 管理提供全面的指导。它涵盖了成功采用所需的技术、流程和组织考量。

### 技术基础

本书探讨了 KubeVirt 的架构和核心组件，解释了虚拟机概念如何转化为 Kubernetes 资源。您将学习 Kubernetes 生态系统中的 VM 生命周期管理、网络、存储和安全性。

### 人员与流程转型

成功的实施不仅仅需要技术部署。本书探讨了从传统 VM 运营到云原生实践的文化转变。这包括从基于图形用户界面 (GUI) 的管理，演变为使用[基础设施即代码](https://thenewstack.io/introduction-to-infrastructure-as-code/) (IaC) 和 GitOps 方法的声明式、代码驱动方法。

这种转型遵循[人员、流程和技术框架](https://web.archive.org/web/20151122232441/http://www.boozallen.com/media/file/People-Process-Technology-Enterprise2.pdf)。它需要提升团队技能、建立新的操作实践并实施合适的技术解决方案。

### 迁移策略

本书涵盖了实用的迁移方法，从简单的 VM 重宿主到更高级的重平台策略。它探讨了原生的 Kubernetes 工具和能够大规模自动化迁移过程的专业迁移平台。

### 卓越运营

除了初始迁移之外，本书还探讨了统一环境中的持续运营。这包括监控、优化、安全性以及利用更广泛的 Kubernetes 生态系统来实现高级功能。

## 前进之路

已经致力于 Kubernetes 的组织能够很好地扩展其平台以处理 VM 工作负载。这种方法在现有投资的基础上，同时简化了基础设施管理。

这一旅程需要仔细规划和执行，才能带来显著效益。统一的基础设施可降低操作复杂性，提高资源效率，并为持续现代化奠定基础。

本书将作为您的指南，贯穿从初始规划到长期运营的整个过程。它提供了在 Kubernetes 上成功实施 VM 管理并实现基础设施整合全部优势所需的实践知识。

云原生未来不仅仅关乎容器：它关乎创建一个统一、高效且敏捷的平台，能够处理您的所有工作负载。KubeVirt 使这个未来在今天成为可能。

**详细了解由 Spectro Cloud 支持的《[在 Kubernetes 上运行虚拟机：企业迁移的实践路线图](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)》，并注册成为首批获取我们最新电子书的读者之一。**