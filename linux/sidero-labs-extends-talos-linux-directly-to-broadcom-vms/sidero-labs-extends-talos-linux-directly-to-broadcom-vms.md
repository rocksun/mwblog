<!--
title: Sidero Labs：Talos Linux原生直达博通VM
cover: https://cdn.thenewstack.io/media/2025/12/078dfdf3-getty-images-onqeqiif4ny-unsplash.jpg
summary: Sidero Labs的Talos Linux专为Kubernetes设计。Omni SaaS现支持在VMware vSphere中自动配置Talos节点，实现集群动态扩展与缩减。Talos Linux倾向裸机，但也满足VMware客户需求。
-->

Sidero Labs的Talos Linux专为Kubernetes设计。Omni SaaS现支持在VMware vSphere中自动配置Talos节点，实现集群动态扩展与缩减。Talos Linux倾向裸机，但也满足VMware客户需求。

> 译自：[Sidero Labs Extends Talos Linux Directly to Broadcom VMs](https://thenewstack.io/sidero-labs-extends-talos-linux-directly-to-broadcom-vms/)
> 
> 作者：B. Cameron Gain

亚特兰大 — [Sidero Labs](https://www.siderolabs.com/?utm_content=inline+mention) 的 Talos [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 旨在为管理异构 [Kubernetes](https://thenewstack.io/kubernetes/) 和其他部署的高成本和复杂性提供替代方案。它是一个专为 Kubernetes 设计的轻量级但高度可扩展的操作系统。

在许多方面，它与 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 Linux OpenShift、[SUSE Rancher](https://thenewstack.io/suse-upgrades-its-rancher-kubernetes-management-family/) 及其他 Kubernetes 发行版的功能相反。在所有这些发行版中，Kubernetes 都安装在通用操作系统之上并运行。Sidero Labs 及其开源的 Talos Linux 认为，这个整个基础不仅是不必要的，而且是一种负担，特别是在私有云和边缘用例中。

它还可以支持虚拟机 (VM)，尽管在 Kubernetes 上运行的 VM 仍然有限，而且在 Broadcom 的 vSphere 情况下，需要变通方法才能将其与 Talos Linux 集成。

但现在，Sidero Labs 基于 Talos Linux 构建的软件即服务 (SaaS) Omni 可以用于 [在 vSphere 中自动配置 Talos 节点](https://github.com/siderolabs/omni-infra-provider-vsphere)。

“Talos 一直在所有虚拟机上运行良好，”Sidero Labs 首席执行官 Steve Francis 在 [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 期间告诉我。“新功能是 Omni 上用于 Broadcom [VMware](https://www.vmware.com/?utm_content=inline+mention) 的基础设施提供商——这意味着 Omni 可以在 VMware 基础设施上创建虚拟机，从而创建集群、扩展它们等等。”

系统与操作系统的集成是一个有趣的发展，例如当项目包含或集成不同的操作系统时。然而，正在讨论的与 [虚拟机](https://thenewstack.io/the-challenges-of-uniting-vms-and-containers-on-a-single-platform/) 相关的具体工作是在内部构建的，与 VMware 无关。

“我们的许多客户仍在虚拟机上运行。他们中的许多人正在使用 VMware 作为基础设施，未来三年肯定如此，”Francis 说。“我们的客户希望有一种方法，可以轻松地在 VMware 上扩展和缩减集群。他们需要这种能力，而无需前往他们的 VMware 配置组静态创建新的虚拟机。作为解决方案，我们为 Omni 编写了一个配置器，Omni 是我们的多集群管理 SaaS。”

Omni SaaS 允许用户插入基础设施提供商。如果集群需要扩展，它将在您的 VMware 基础设施上动态创建虚拟机。它可以在需要达到扩展约束的次数内执行此操作，并且可以缩减并销毁这些机器。这基本上使得在 VMware 基础设施上扩展和缩减集群变得完全透明。

“配置系统支持虚拟机基础设施。它支持 Kubernetes，并且也具有裸机类似的功能。我们现在也为 Oxide 的超融合基础设施提供了类似的功能。”

## 裸机与虚拟机和 Talos Linux

现在几乎所有东西，绝大多数基础设施、容器和基础设施，都在虚拟机上。然而，在 Sidero Labs 的客户群中，许多客户运行裸机。配置系统将与在裸机上运行的容器一起工作。有一个用于裸机的基础设施提供商，它可以使用智能平台管理接口 (IPMI) 或 Redfish 等方法实际打开机器。

“我们的理念是，直接在裸机上运行 Kubernetes 比在虚拟机中运行更好，”Francis 说。“如果你确实需要使用虚拟机，那么 VMware 提供商就派上用场了。Talos Linux 操作系统更倾向于裸机。”

之所以构建 VMware 的虚拟提供商，是因为人们在他们的 VMware 基础设施上投入了大量资金来运行大量虚拟机。希望采用 Talos Linux 的团队经常面临的限制是“我们只能获得虚拟机。”