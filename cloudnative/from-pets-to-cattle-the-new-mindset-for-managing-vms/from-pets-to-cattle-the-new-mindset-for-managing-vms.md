<!--
title: 从“宠物”到“牲畜”：虚拟机管理新思维
cover: https://cdn.thenewstack.io/media/2026/01/6b66a48d-from-pets-to-cattle-vm-management-scaled.jpg
summary: 文章介绍KubeVirt将VM迁移至Kubernetes的实践指南，重点在于操作模式转变、团队能力建设，并应对文化抵制，实现自动化云原生管理。
-->

文章介绍KubeVirt将VM迁移至Kubernetes的实践指南，重点在于操作模式转变、团队能力建设，并应对文化抵制，实现自动化云原生管理。

> 译自：[From Pets to Cattle: The New Mindset for Managing VMs](https://thenewstack.io/from-pets-to-cattle-the-new-mindset-for-managing-vms/)
> 
> 作者：Janakiram MSV

*本文节选自[“运行Kubernetes上的虚拟机：企业迁移的实用路线图”](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)一书的第四章，该书由知名研究分析师和技术专家[Janakiram MSV](https://thenewstack.io/author/janakiram/)撰写，并由Spectro Cloud赞助。*

*该书为正在探索将虚拟机 (VM) 迁移到Kubernetes的云原生组织提供了实用的路线图。在涵盖将VM迁移到Kubernetes的各种选项的同时，本书重点关注KubeVirt，这是一个[云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention)项目。Janakiram在[本书介绍](https://thenewstack.io/migrating-vms-to-kubernetes-a-roadmap-for-cloud-native-enterprises)中解释说，该项目“提供了一种标准化方式，使用与容器化工作负载相同的API、工具和操作实践来运行VM”。*

*从探索云原生环境中VM的架构和生命周期，到组建跨职能的迁移团队和选择合适的工具，这本[现已开放下载](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)的免费书籍，帮助企业领导者充满信心地应对这场划时代的转变。*

---

使用KubeVirt将虚拟机 (VM) 工作负载迁移到[Kubernetes](https://thenewstack.io/kubernetes/)，需要团队改变部署和管理应用程序的方式。虽然底层基础设施技术发生变化，但更显著的影响通常在于调整操作实践和团队工作流程，以有效地与云原生工具配合。

本章探讨了迁移规划的实际方面，包括评估组织准备情况、建立正确的团队能力，以及管理从以VM为中心的操作到Kubernetes原生方法的过渡。

## 理解操作转变

已经为容器化应用程序运行Kubernetes的组织已经建立了云原生实践。然而，将这些实践扩展到VM工作负载，通常会暴露出传统操作和云原生操作交叉点的差距。

根据Spectro Cloud的“2024年生产Kubernetes状态”研究，VM的采用一直是限制Kubernetes采用的一个重要障碍。研究发现，“继续将VM与容器一起使用”和“对变革的文化抵制”仍然是影响组织如何进行平台采用的关键因素。

VM管理和Kubernetes原生实践之间的操作差异带来了具体的挑战。传统的VM操作通常涉及基于GUI的工具、票据驱动的配置和仔细的变更管理流程。Kubernetes操作则强调声明式配置、自动化部署和快速迭代周期。

考虑这两种方法之间资源请求的差异：

* 在传统的VM环境中，开发人员通常通过服务台系统提交新虚拟机的请求。基础设施团队审查规范，从标准模板配置VM，并在可能需要数天或数周的审批流程后提供访问权限。
* 在Kubernetes环境中，开发人员修改YAML文件中的资源规范，将更改提交到版本控制，并观察自动化系统在几分钟内部署新的配置。这种转变不仅仅意味着速度的提高：它改变了决策者、资源分配方式以及操作专业知识的所在地。

习惯于VM操作的团队可能会觉得Kubernetes方法最初令人不安。开发人员自主性的增加和集中控制的减少可能会让人感觉失去了监管。然而，一旦团队调整了流程，这种转变通常会带来更高的敏捷性和更有效的资源利用。

## 应用程序部署模式

将VM工作负载迁移到Kubernetes还会影响应用程序的部署和管理方式。传统的VM部署通常将虚拟机视为长期存在的基础设施，承载应用程序数月或数年。团队仔细配置操作系统、安装依赖项，并为每个工作负载调整特定的性能设置。

KubeVirt提供了另一种方法，其中VM在生命周期管理方面更像容器。虽然VM内部的应用程序可能保持不变，但VM本身可以被视为[牛而不是宠物](https://thenewstack.io/how-to-treat-your-kubernetes-clusters-like-cattle-not-pets)。这使得自动化替换、滚动更新和动态扩展等实践成为可能，这些在容器化环境中很常见。

这种转变要求团队重新考虑如何处理VM配置、应用程序部署和操作维护。基础设施即代码 (IaC) 实践变得更加重要，因为VM规范是在版本控制的清单中定义的，而不是通过手动配置过程。

这种过渡还影响了团队如何处理监控、日志记录和故障排除。Kubernetes原生工具为可观测性和自动化提供了新功能，但团队需要学习这些工具如何应用于KubeVirt下运行的VM工作负载。