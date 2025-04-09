
<!--
title: VMware最终赶上Kubernetes了吗？
cover: https://cdn.thenewstack.io/media/2025/04/9df4f152-vmware-caught-kubernetes.jpg
summary: VMware借Broadcom收购，发力云原生！VMware Cloud Foundation (VCF) 成为虚拟机和容器的统一平台，集成vSphere Kubernetes Service (VKS)，支持多集群管理。通过YAML配置，简化AI应用部署，内置安全功能，打造最安全的Kubernetes平台，目标直指AWS EKS、Azure AKS和Google GKE！
-->

VMware借Broadcom收购，发力云原生！VMware Cloud Foundation (VCF) 成为虚拟机和容器的统一平台，集成vSphere Kubernetes Service (VKS)，支持多集群管理。通过YAML配置，简化AI应用部署，内置安全功能，打造最安全的Kubernetes平台，目标直指AWS EKS、Azure AKS和Google GKE！

> 译自：[Has VMware Finally Caught Up With Kubernetes?](https://thenewstack.io/has-vmware-finally-caught-up-with-kubernetes/)
> 
> 作者：B Cameron Gain

自从容器成为“热门事物”以来，VMware 一直是领先的 Kubernetes 管理和基础设施服务提供商之一，也是过去十年中 [Kubernetes](https://thenewstack.io/kubernetes/) 项目的三大贡献者之一。但这还不够。

在 2023 年被 Broadcom 收购之前，VMware 的大部分 Kubernetes 知识产权 (IP) 并未被客户充分利用。VMware 肯定有很多东西可以提供，但它没有一个通用平台，使处于 Kubernetes 旅程不同阶段的公司能够满足他们对虚拟机 (VM) 和 Kubernetes 容器的所有需求。

但这已经得到了纠正；现在，VMware Cloud Foundation (VCF) 成为虚拟机和容器的[单一平台](https://thenewstack.io/vmwares-private-cloud-shift-under-broadcom/)，具有多集群管理和许多其他云原生环境的功能等诸多增强功能。

## 聚焦的催化剂

Broadcom 的收购是 VMware 将整个私有云堆栈和服务集成到 VCF 中的一个[催化剂](https://thenewstack.io/vmwares-private-cloud-shift-under-broadcom/)。虽然 VMware 之前在 VCF 堆栈中拥有许多基础设施和管理组件，但 Broadcom 帮助带来了急需的关注——以及支持组织全面满足 Kubernetes 运行时和统一管理需求的能力。Kubernetes 运行时许可证已包含在 VCF 许可证中，因此无需额外许可证。

“Broadcom 模式强调了解客户需求——客户在哪里，以及他们需要什么才能在平台上取得成功。VMware 一直拥有强大的 IP 和尖端技术，但在收购之前，其中大部分并未得到充分利用，尤其是对于较新的基于容器的工作负载，”Broadcom VCF 部门 Kubernetes 产品管理负责人 [Timothy Carr](https://www.linkedin.com/in/timmycarr/) 在一次采访中告诉我。“此次收购明确了这种区别。它使 VMware 能够识别有价值的领域，识别新应用程序的发展方向，并确定需要做些什么才能保持竞争力并提供类似公共云的敏捷性。”

通过 VCF 实现 Kubernetes 卓越性的转变主要涉及 Kubernetes 运行时——vSphere Kubernetes Service (VKS)，以前称为 [Tanzu](https://tanzu.vmware.com?utm_content=inline+mention) Kubernetes Grid——及其著名的虚拟机和支持基础设施的更深入集成。

TechTarget 旗下 Enterprise Strategy Group 的分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 表示：“这是 VMware 回归基础，它需要这样做才能说服客户 VCF 是一个可以并行运行容器和虚拟机的可行平台。“VMware 仍然拥有一项巨大的资产：一大批与 vSphere 一起成长的管理员。向这些 VMware 人员展示一条清晰的道路，让他们成为应用程序现代化故事的一部分，对于说服企业尝试在 [VCF] 上使用 Kubernetes 至关重要。”

## 深度和广度

![VCF 是运行虚拟机和容器的单一平台。](https://cdn.thenewstack.io/media/2025/04/f817653a-vmwarecloudfoundation.png)

*VCF 是运行虚拟机和容器的单一平台。（来源：VCF）*

VCF 对 Kubernetes 支持的一个关键组成部分是其 VMware vSphere Supervisor。Supervisor 充当平台和控制平面，可以在其上配置一套强大的基础设施和云服务，包括 Kubernetes 集群服务。这些服务包括 VKS（Kubernetes 运行时）、多集群管理、VM 服务、vSphere Pod、网络服务、存储和备份服务、身份和访问控制服务、镜像注册表以及许多其他功能。

Carr 说：“以前，虚拟机、容器和网络服务的多个不同 API 分布在不同的区域。“新方法的优势在于 Kubernetes 和虚拟机 API 与单一操作模型的集成。这为两种工作负载简化了流程。”

例如，如果您需要构建和运行 AI 应用程序，则必须准备一个带有 Nvidia GPU 运算符的 Kubernetes 集群。此外，数据科学家需要一个可以访问 GPU 资源的工作站。“现在可以使用 YAML 配置来编排所有这些，并由现有的企业 VMware 基础设施工作流程来操作，从而使环境更加强大，”Carr 说。
“最终，该平台现在支持交付各种类型的应用程序——无论是基于虚拟机、基于 Kubernetes 还是两者兼而有之。Kubernetes 提供的可扩展性使这些功能类似于云基础设施，从而提高了整体效率和灵活性，”他继续说道。

Volk表示，将 Kubernetes 集成到 VCF 中的确已经“走了很长一段路”，从最初专注于自下而上编写部署和管理任务的脚本的方法。“VCF 已经发展到提供一种更具声明性，因此更一致和可扩展的方法，这对于运行云原生应用程序是必要的，”Volk 说。

## Kubernetes 现在更新了

VMware 的工程师表示，他们已经打破了过去，优先发布最新版本的 Kubernetes，目标是在上游版本发布后的两个月内完成。Carr 说，这有助于确保与超大规模企业使用的最新版本保持一致。

Carr 说，目标是在 VCF 上创建一个深度集成的 Kubernetes 产品，就像超大规模企业所做的那样。“[AWS](https://aws.amazon.com/?utm_content=inline+mention) 拥有 EKS——AWS Kubernetes 集成度最高的版本。Azure 上的 AKS 和 [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) 上的 GKE 也是如此，”Carr 说。“我们通过 VKS 在 VCF 基础设施上实现了相同级别的集成，并且已经在朝着这个目标取得更多进展。”

此外，Carr 声称，内置的安全功能使其成为迄今为止在该公司基础设施上运行的最安全的 Kubernetes 平台。这是“其他供应商无法完全复制的。我们将继续利用这一优势，因为它在 VCF 上构建了最好的 Kubernetes 堆栈，”Carr 说。

“最后，重要的是要注意，这不仅仅是关于 Kubernetes——一切都建立在该公司的虚拟化平台之上，该平台已经成功运营了 20 多年。”

借助 VCF，VMware 提供了一个单一平台，该平台具有内置的 Kubernetes 运行时和一个经过 [CNCF](https://cncf.io/?utm_content=inline+mention) 认证的 Kubernetes 发行版，供组织在同一基础设施上运行现代容器化应用程序和传统 VM。VCF 旨在简化 Kubernetes 的部署和管理，同时统一计算、存储、网络和安全性——VMware 表示这可以降低总拥有成本和运营复杂性。在博通收购之后，VMware 正在将 VCF 吹捧为一项主要产品。首席信息官和任何参与 DevOps 运营的人员都应该至少认真考虑将其作为标准化平台。