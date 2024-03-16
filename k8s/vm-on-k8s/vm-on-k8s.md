
<!--
title: Kubernetes 上的虚拟机：需求和解决方案（2023）
cover: https://arthurchiao.art/assets/img/vm-on-k8s/vm-in-container-solution.png
-->

有些人可能对这个话题感到困惑：**为什么我们仍然需要虚拟机**（来自过去的云计算时代），而在这个云原生时代，我们已经有了容器化平台？此外，为什么我们还要费心在 Kubernetes 上管理虚拟机，而 Kubernetes 是事实上的容器编排平台？

> 译自 [Virtual Machines on Kubernetes: Requirements and Solutions (2023)](https://arthurchiao.github.io/blog/vm-on-k8s/)，作者 None。


## 1. 简介

将虚拟机和容器作为配置方法进行比较是一件复杂的事情，超出了本文的范围。我们只是强调了一些在 Kubernetes 上部署虚拟机的实际原因。

### 1.1. 实用原因

首先，

**并非所有应用程序都可以容器化**。

虚拟机提供了一个完整的操作系统环境和暂存空间（对用户来说是有状态的），而容器最常以无状态的方式使用，并且它们与节点共享相同的内核。不适合容器化的场景：

- 与操作系统紧密耦合或依赖于特定硬件的应用程序；
- 具有复杂显示要求的基于 GUI 的应用程序 -
**例如；**
Windows

其次，具有严格安全要求的应用程序可能不适合容器部署：

- 虚拟机在工作负载之间提供更强的隔离，并更好地控制资源使用；
- OpenStack 中的硬多租户与 Kubernetes 中的软多租户；

第三，并非所有从虚拟机到容器的转换都会带来业务收益。虽然在大多数情况下，从虚拟机迁移到容器可以减少技术债务，但成熟且不太发展的基于虚拟机的堆栈可能无法从这种转换中受益。

综上所述，尽管容器有优势，但在许多情况下虚拟机仍然是必要的。那么问题就变成了：

**是否将它们作为独立平台或传统平台**（如 OpenStack）来维护，还是**使用 Kubernetes 统一管理**——特别是如果你的主要关注点和精力已经放在 Kubernetes 上。

本文探讨了后一种情况：使用 Kubernetes 管理虚拟机以及容器工作负载。

### 1.2 资源配置和编排

在继续之前，让我们简单比较一下两个时代。

#### 1.2.1 云计算时代

在这个时代，重点主要在于 IAAS 级别，其中

**虚拟化在硬件上进行**以提供虚拟 CPU、虚拟网络接口、虚拟磁盘等。

这些虚拟部分最终组装成一台虚拟机 (VM)，就像一台物理机器（刀片服务器）一样供用户使用。

用户通常以如下方式表达他们的需求：

我想要 3 台虚拟机。他们应该，

- 拥有自己的永久 IP 地址（在其整个生命周期中不可变的 IP）。
- 拥有用于暂存空间或有状态数据的持久性磁盘。
- 在 CPU、内存、磁盘等方面可调整大小。
- 在维护或中断期间可恢复（通过冷迁移或热迁移）。

一旦用户登录到机器，他们就可以部署其业务应用程序并在这些虚拟机之上编排其操作。

满足这些需求的平台示例：

- AWS EC2
- OpenStack

这些平台的重点：资源共享、硬多租户、强隔离、安全等。

#### 1.2.2 云原生时代

在云原生时代，编排平台仍然关注

上述需求，但它们在比 IAAS 更高的级别上运行。

它们解决弹性、可扩展性、高可用性、服务负载平衡和模型抽象等问题。

产生的平台通常管理

**无状态工作负载**。

例如，在 Kubernetes 的情况下，用户通常以如下方式表达他们的需求：

我想要一个用于提供静态网站的 nginx 服务，它应该：

- 具有用于访问的唯一入口点（ServiceIP 等）。
- 在 3 个节点上复制 3 个实例（亲和性/反亲和性规则）。
- 请求应进行负载平衡（ServiceIP 到 PodIP 的负载平衡）。
- 行为不当的实例应自动替换为新实例（无状态、健康检查和协调机制）。

### 1.3 总结

牢记上述讨论，让我们来看看一些用于在 Kubernetes 上管理虚拟机工作负载的开源解决方案。

# 2 通过 Kubernetes 管理虚拟机工作负载：解决方案

有两种典型的解决方案，它们都基于 Kubernetes，并且能够管理容器和虚拟机工作负载：

- **容器中的虚拟机**：适用于目前同时维护 OpenStack 和 Kubernetes 的团队。他们可以利用此解决方案向最终用户提供虚拟机，同时逐步淘汰 OpenStack。
- **Kubernetes 原生虚拟机**：适用于希望在 Kubernetes 上统一管理容器和虚拟机工作负载的团队。
**容器内虚拟机**：已经享受了容器生态系统提供的优势和便利，同时希望加强容器工作负载的安全性与隔离方面。

### 2.1 在 Pod 内运行虚拟机：

- kubevirt
  - 图。在容器内运行（全功能）虚拟机，逐步淘汰 OpenStack。
  - 解决方案：kubevirt 等
  - kubevirt 利用 Kubernetes 进行虚拟机配置。
  - 在原生 Kubernetes 之上运行。
  - 引入多个 CRD 和组件来配置虚拟机。
  - 通过将每个虚拟机**嵌入到容器（pod）中**来简化虚拟机配置。
  - 兼容几乎所有 Kubernetes 功能，例如服务负载均衡。

## 2.2 在虚拟机内运行 Pod：

- kata 容器
  - 图。在（轻量级）虚拟机内运行容器，并使用适当的容器运行时。
  - 解决方案：kata 容器等
  - Kata 容器具有轻量级虚拟机包装器，
  - 在轻量级且超快速的虚拟机内部署容器。
  - 使用此外层虚拟机增强容器安全性。
  - 需要专用的容器运行时（但无需更改 Kubernetes）。

# 3 Kubevirt 解决方案概述

在本节中，我们将快速概述 kubevirt 项目。

## 3.1 架构和组件

**高级架构：**

- 图。kubevirt 架构概述

**主要组件：**

- virt-api：kubevirt apiserver，用于接受控制台流式传输等请求；
- virt-controller：协调 kubevirt 对象，如
  **,**
  VirtualMachine
  **(**
  VirtualMachineInstance
  VMI）；
- virt-handler：节点代理（如
  OpenStack 中的 nova-compute），与 Kubernetes 的节点代理
  kubelet 协作；
- virtctl：CLI，例如
  virtctl console <vm>

## 3.2 工作原理

**如何在 Kubernetes 之上的 kubevirt 中创建虚拟机：**

- 图。在 kubevirt 中创建虚拟机的流程。左：kubevirt 添加的步骤；右：在 k8s 中创建 Pod 的原生过程。

您可以看到，**只有附加组件，但没有更改 Kubernetes** 工作流程。

**深入说明：** [在 Kubernetes 中使用 kubevirt 生成虚拟机：深入探讨](/blog/kubevirt-create-vm/)。

## 3.3 节点内部拓扑

节点内组件的内部视图：

- 图。具有两个（KVM）虚拟机的 k8s/kubevirt 节点

## 3.4 技术栈

### 3.4.1 计算

仍然基于
**, 就像 OpenStack 一样。KVM/QEMU/libvirt**

### 3.4.2 网络

与 CNI 机制兼容，可以与 flannel、calico 和 cilium 等流行的网络解决方案无缝协作。

kubevirt 代理在 pod
网络之上进一步创建虚拟机网络。这是必要的，因为虚拟机作为用户空间
进程运行，需要用户空间模拟的网卡（例如 TUN/TAP），而不是 veth 对。

网络是一个大话题，我想为它写一篇专门的博客（如果时间允许）。

### 3.4.3 存储

基于 Kubernetes 存储机制（PV/PVC），以及虚拟机快照、克隆、实时迁移等高级功能，都依赖于这些机制。

还做了一些扩展，例如，containerDisk（将
**嵌入到
虚拟机映像** **) .**
容器映像

# 4 结论

这篇文章讨论了在 Kubernetes 上运行虚拟机的必要性，并对 kubevirt 项目进行了进一步的技术概述。

# 参考文献

- [github.com/kubevirt](https://github.com/kubevirt/kubevirt)
- [github.com/kata-containers](https://github.com/kata-containers/kata-containers)
- [在 Kubernetes 中使用 kubevirt 生成虚拟机：深入探讨 (2023)](/blog/kubevirt-create-vm/)