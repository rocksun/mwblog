<!--
title: KubeVirt架构全解析：CRD、控制器与守护进程
cover: https://cdn.thenewstack.io/media/2025/12/2a4cacb6-kubevirt-architecture-spectrocloud.jpg
summary: KubeVirt将传统虚拟机与容器在Kubernetes上连接，扩展K8s API实现VM原生管理。通过CRD、控制器、守护进程等组件，它提供统一平台，助力企业向云原生转型。
-->

KubeVirt将传统虚拟机与容器在Kubernetes上连接，扩展K8s API实现VM原生管理。通过CRD、控制器、守护进程等组件，它提供统一平台，助力企业向云原生转型。

> 译自：[KubeVirt’s Architecture: CRDs, Controllers and Daemons](https://thenewstack.io/kubevirts-architecture-crds-controllers-and-daemons/)
> 
> 作者：Janakiram MSV

*本文节选自知名研究分析师和技术专家 Janakiram MSV 撰写、Spectro Cloud 赞助的新电子书《[在 Kubernetes 上运行虚拟机：企业迁移的实用路线图](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)》第三章。* *这本免费电子书[现已开放下载](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)，从探索云原生环境中虚拟机的架构和生命周期，到组建跨职能迁移团队和选择合适的工具，帮助企业领导者自信地驾驭这场百年一遇的转型。*

---

## KubeVirt 基础：连接虚拟机和容器

随着组织逐步摆脱传统虚拟化，[KubeVirt](https://thenewstack.io/open-source-kubevirt-vm-management-with-kubernetes-is-a-work-in-progress/) 不仅作为一种工具，更作为一项基础技术出现，使得分阶段、务实地迁移到 Kubernetes 成为可能。它充当了一座桥梁，使传统虚拟机和现代容器能够在单一、统一的平台：[Kubernetes](https://thenewstack.io/kubernetes/) 上共存。

理解 KubeVirt 的架构和功能是利用它来降低迁移风险、整合基础设施并加速迈向云原生运营模式的第一步。

本章将探讨基础设施评估所需的关键技术基础、实际限制和真实世界实施模式。

## 架构概览：KubeVirt 如何扩展 Kubernetes

KubeVirt 的设计理念非常直接，并牢固地建立在 Kubernetes 已然擅长的方面。KubeVirt 没有为虚拟机创建一个新的并行编排系统，而是扩展了久负盛名的 Kubernetes API 和控制平面，使其能够将虚拟机作为原生资源进行管理。它有效地将调度、网络和存储等核心功能直接委托给 Kubernetes，同时在之上分层增加了虚拟化所需的特定逻辑。

[![KubeVirt Architecture Stack](https://cdn.thenewstack.io/media/2025/12/96b4a2db-kubevirt-architecture-stack.png)](https://cdn.thenewstack.io/media/2025/12/96b4a2db-kubevirt-architecture-stack.png)

KubeVirt 为 Kubernetes 增加了虚拟化能力。

从本质上讲，KubeVirt 虚拟机只是一个在标准 Kubernetes Pod 内运行的进程。这种方法允许虚拟机和容器在同一工作节点上并排运行，通过相同的网络进行通信，并使用相同的存储资源，所有这些都通过一个统一的界面进行管理。

为此，KubeVirt 在集群中引入了三种主要类型的组件：

1.  **自定义资源定义 (CRDs)：** 这些是 Kubernetes API 的扩展，用于定义新的对象类型。KubeVirt 添加了多个 CRD，其中最著名的是 VirtualMachine 和 VirtualMachineInstance (VMI)。这使得管理员能够像定义任何其他 Kubernetes 对象（如 Pod）一样，使用声明式 YAML 清单来定义 VirtualMachine。
2.  **控制器：** 这些是集群范围的组件，包含管理新 CRD 的业务逻辑。它们作为 Pod 运行并监视 Kubernetes API 的变化。
3.  **守护进程：** 这些是节点特定的代理，以 DaemonSet 的形式部署，负责管理集群中每个工作节点上的虚拟机生命周期。

## 关键组件及其作用

KubeVirt 组件之间的相互作用在 Kubernetes 内部创建了一个无缝的虚拟化层。虽然操作员可以安装所有必要的组件，但理解这些组件的各自作用对于故障排除和有效管理至关重要。

*   **VirtualMachine 和 VMI：** 这是用户交互的两个主要 CRD。VirtualMachine 对象代表虚拟机的持久期望状态。它可以在启动和停止时保留其配置和数据。VirtualMachineInstance 代表该 VirtualMachine 的实际运行实例。VMI 更具临时性，仅在 VirtualMachine 对象处于运行状态时才存在，并与承载它的 Pod 紧密耦合。

*   **virt-api 服务器：** 它作为所有虚拟化流程的 HTTP API 入口点，充当 VMI CRD 操作的接口。它验证、处理并将 VMI 和 VirtualMachine 资源定义持久化到 Kubernetes 中，从而允许 KubeVirt 控制平面的其余部分做出反应。

*   **virt-控制器：** 这是中央的、集群范围的控制器。其主要任务是监视新的 VMI 对象的创建。当定义了 VMI 时，virt-控制器会创建一个对应的 Pod，该 Pod 最终将托管 VirtualMachine 进程。它处理高级操作并协调复杂的动作，例如实时迁移。

*   **virt-处理程序：** 这是一个 DaemonSet，意味着每个工作节点上都运行一个实例。它充当节点特定的代理。当虚拟机的 Pod 被调度到其节点上时，virt-处理程序就会接管。它与 Pod 内部的 virt-启动器通信，执行所有必要的操作，以在该特定主机上启动、停止和管理虚拟机进程。

*   **virt-启动器：** 对于每个运行中的虚拟机，都有一个专用的 Pod，该 Pod 中的主容器运行 virt-启动器组件。此组件是链中的最后环节。它接收来自 virt-处理程序的指令，并使用本地 `libvirtd` 实例启动和管理构成虚拟机的实际 [QEMU](https://github.com/qemu/qemu)/基于内核的虚拟机 ([KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine)) 进程。它还通过捕获来自 Kubernetes 的信号并将其传递给虚拟机进程来确保平稳关机。

*   **libvirtd：** 这是一个运行在 virt-启动器容器内的虚拟机管理守护进程。它向 QEMU/KVM 公开一个控制接口，处理虚拟机生命周期命令，例如启动、停止、暂停、恢复和迁移。它通过提供稳定的 API 抽象了与 QEMU 直接交互的复杂性。

*   **QEMU：** 这是一个由 virt-启动器容器内的 `libvirtd` 调用、运行在用户空间的模拟器和虚拟化器。QEMU 模拟虚拟机的硬件环境，并通过 KVM（如果可用）进行硬件加速来执行客户操作系统。它处理设备仿真、I/O 操作和 CPU 虚拟化。

[![Kubevirt Services Architecture](https://cdn.thenewstack.io/media/2025/12/9a01675d-kubevirt-services-architecture.png)](https://cdn.thenewstack.io/media/2025/12/9a01675d-kubevirt-services-architecture.png)

额外控制器和守护进程的通信和存储。