## Kubernetes 十周年：裸机基础设施上的 Talos

今年，Kubernetes 随着 v1.30.0 版本的发布迎来了其十周年纪念日，巩固了其作为首选云平台的地位。EKS、GKS 和 AKS 等自管理 Kubernetes 集群占集群总数的 73%，其余 27% 为自管理，如 [Dynatrace](https://assets.dynatrace.com/en/docs/wp/bae3218-wp-kubernetes-in-the-wild-en.pdf?_ga=2.202268564.403052509.1714528198-1455211400.1714528198) 所述。

过去十年是公有云时代，但由于成本不断上升，一些企业正试图通过混合云找到平衡。根据 [VMware](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/docs/vmware-ebook-state-of-kubernetes.pdf) 的说法，大约 76% 的组织现在利用多个云，即公有云和私有云的组合。Kubernetes 允许我们在所选硬件上构建多云和私有云层，并且以经济高效的方式构建，而无需承诺使用某个特定云。

尽管 Kubernetes 的采用率不断提高，但人们仍然关注成本效率、可靠性和安全性。从 Kubernetes 虚拟机过渡到裸机基础设施可通过消除管理程序层、简化故障排除流程和最大化应用程序的资源可用性来提供性能优势。裸机设置使组织能够完全控制硬件组件，从而针对特定工作负载进行定制优化。通过正确的工程实践和 Kubernetes 的集成，组织可以实现与公有云产品同等的功能。

从历史上看，由于操作复杂性，特别是在管理集群生命周期方面，在裸机上运行 Kubernetes 构成了挑战。然而，这些障碍已随着 **Talos** 的引入而被克服，我们将在本文中进一步探讨。

## Talos 简介

Talos 是一个非常精简的操作系统，用 Golang 编写。Talos 被设计为一个特定于操作系统的操作系统，用于维护 Kubernetes 集群。为了使 Kubernetes 基础设施更可靠，我们需要确保每个节点运行相同版本的操作系统。Talos 可以通过添加 Talos 构建在其上的不可变理念来帮助我们保持 Kubernetes 基础设施的可靠性和一致性。

Talos 始终作为 SquashFS 映像运行，SquashFS 映像是 Linux 中的只读文件系统。Talos SquashFS 映像的总大小约为 80M。Talos 故意省略了 systemd、GNU 实用程序、控制台包、bash 或 SSH 二进制文件等组件，以最大程度地减少攻击面并降低安全漏洞的可能性。相反，它依赖于一个用于管理系统操作的现代 API。

Talos 仅包含所需内容。相反，所有内容都由一个现代 API 管理。Talos 非常注重不可变基础设施理念。

## 什么是不可变基础设施？

不可变基础设施一旦系统部署，你将无法对其进行任何更改；此概念称为不可变基础设施。如果在不可变基础设施中需要进行更改，则会创建一个具有所需修改的新基础设施，而不是更改现有基础设施。拥有不可变的基础设施使登台、预生产和生产环境更加一致。在裸机 k8s 基础设施上保持节点之间的一致性是最重要的。在这种类型的基础设施中，我们的应用程序与操作系统紧密耦合，这是不可变系统的缺点。

## 使用 Talos 的好处

- Talos 在整个系统中保持一致性，并避免任何配置更改。Talos 将此称为“可预测性”。
- Talos 旨在使 Kubernetes 基础设施完全不可变，从而增强可靠性、安全性和一致性。这使得 Talos 成为运行 Kubernetes 的裸机服务器的理想选择。
- Talos 被设计为不可变的，因此它在 RAM 上运行，而不是在磁盘上运行。由于 Talos 是 SquashFS 映像，因此它具有较少的写入点，这些写入点本质上是短暂的。
- Talos 具有高度安全性。
- Talos 是一个非常轻量级的操作系统，大约有 12 个二进制文件，全部用于运行 Kubernetes。
- Talos 是 API 驱动的。
- Talos 遵循 KSPP（内核自保护项目）给出的建议 - [KSPP 文档](https://docs.kernel.org/security/self-protection.html)

## 用例

Talos 非常适合自管理 Kubernetes 集群，但 [CIVO](https://www.civo.com/docs/faq#why-does-civo-use-talos-linux) 等平台提供使用 Talos 部署 Kubernetes 集群的支持。以下是使用 Talos 运行 Kubernetes 的一些用例。

**边缘应用程序：**
## Kubernetes for Edge Devices

Kubernetes is one of the best choices available for managing large numbers of edge devices. Not only is Kubernetes designed for container orchestration, but it can also effectively manage edge devices. To ensure our edge applications are reliable and secure, having a secure and reliable Kubernetes environment is crucial. Talos is a great fit for edge devices due to its security and reliability, as well as its immutable philosophy.

### Kubernetes on Bare Metal

Using Kubernetes on bare metal removes unnecessary abstractions, giving our applications full control over the hardware. Talos stands out as an excellent choice for deploying Kubernetes on bare metal servers. It removes unnecessary configuration and troubleshooting, making it easy to deploy Kubernetes on bare metal.

### AI and Machine Learning Workloads

Kubernetes has proven to be an ideal platform for testing and training new machine learning models, with the ability to seamlessly deploy to larger scale environments. Maintaining consistency in deployment is crucial to ensuring secure and stable model deployments. Talos plays a key role in this by providing a consistent environment to reliably scale models as needed.

## Architecture and Design

The Talos architecture consists of many different components that have defined gRPC interfaces. All communication between Talos components happens over gRPC.

### Talos Filesystem Partitions

- EFI: Stores EFI boot data.
- BIOS: Used for GRUB second stage boot.
- Boot: Used for the bootloader, stores initramfs and kernel data.
- Meta: Stores metadata about the Talos node.
- State: Stores machine configuration.
- Ephemeral: Mounted at /var, used for storing temporary data.

Talos has a 3-layer filesystem:

- rootfs: This is the core layer with a read-only squashfs. The squashfs is then mounted into memory as a loop device.
- tmpfs: This filesystem is used for runtime specific needs.
- system: Needed for internal operations.

For example, Talos will write to /system/etc/hosts, which is then bind mounted to /etc/hosts. Talos does not make /etc writable, but rather only specific parts of /etc. /system is recreated entirely on every boot. To maintain persistence across boots, Talos creates overlay filesystems. /var is owned by Kubernetes. This directory is used by etcd to write data. This data is only deleted when the machine is upgraded or reset, to avoid this we add the "--preserve" option when upgrading.

### Components

talosctl is a CLI tool used to interact with all the components in Talos. It is similar to how we interact with the kube-api using kubectl. Similarly, talosctl is used to interact with apid.

**apid:** Talos is API driven, apid is responsible for providing gRPC endpoints to interact with different components. apid is present on every node, including the control plane.
- **machined:** It is responsible for handling API requests from apid, and does resource and controller management.
- **trustd:** It is a daemon that is used to establish trust across the system. It is used to establish trust between nodes.
- **udevd:** It is used to setup necessary links in /dev.

### Controllers and Resources

- **Resources:** These are similar to resources in Kubernetes, resources have different types and contain metadata like namespace, type, etc. Resources can be uniquely identified by their namespace. The MachineConfig resource reflects the current machine configuration.
- **Controllers:** In Talos, controllers run as threads. A controller can manage multiple resource types, each resource type can have a large number of resources. To avoid conflicts, only one controller is responsible for managing a particular resource type in a namespace. Talos stores the resource types that a controller is defined for in the meta namespace.

## Demo

In this article, we are showcasing the functionality using Docker as we do not have bare metal available. Subscribe to our blog as we plan to share how to run Talos on bare metal in a future post. We will learn how to create a Kubernetes cluster using Docker.

### Setting Up Docker and Talos Cluster

### Prerequisites

Before proceeding, make sure you have the following installed:

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- talosctl
*Note: The talosctl and Talos OS ISO image versions should be the same. For more information, check the releases.*

### Mac

```bash
brew install siderolabs/tap/talosctl
```

### Linux

```bash
wget https://github.com/siderolabs/talos/releases/download/v1.7.0/talosctl-linux-amd64
chmod +x talosctl-linux-amd64
./talosctl-linux-amd64
sudo mv ./talosctl-linux-amd64 /usr/local/bin
```

Let's install a three-node cluster using docker and talosctl. The following command will create a 3 node cluster (control plane, worker node 1, worker node 2).

```bash
talosctl cluster create --workers 2
```

Let's check the number of nodes created and the OS information

```bash
kubectl get nodes -o wide
```
## kubectl get node talos-default-worker-1 -o json | jq -r '.status.nodeInfo.osImage'

```bash
# 让我们清理并删除集群
talosctl cluster destroy
```

## 结论

Talos 在管理 Kubernetes 环境中发挥着至关重要的作用。它的简单性极大地简化了 Kubernetes 集群的配置。Talos 的不可变理念极大地增强了基础设施的安全性与一致性。

## 常见问题解答

### Talos 与 k3s

Talos 与 k3s 之间没有直接比较。但是，在考虑部署 Kubernetes 集群时，k3s 需要一个操作系统，并且具有其他依赖项，这些依赖项根据底层操作系统而异。而 Talos 的重点是使用其不可变理念运行 Kubernetes 集群，从而保持其安全性和可靠性。Talos 使 Kubernetes 部署变得更加简单。

### Talos 包含哪些二进制文件？

- Talos 中的 `init` 二进制文件负责运行 kubelet 和容器运行时。
- Containerd 是 Talos 中的运行时，以及 runc。
- Modprobe 用于为某些二进制文件加载模块。模块可以添加到 Talos，或者我们可以使用 [Image Factory](https://factory.talos.dev/) 中预先构建的模块。
- 对于卷管理，使用 lvm。
- udevd 用于从内核收集消息并将其传递给其他系统。
- xfs_repair 等二进制文件用于修复 XFS 文件系统。

### Talos 是否免费？

Talos 是一个免费且开源的操作系统，受 Mozilla 公共许可证版本 2.0 约束，允许商业使用。在 [Talos Github 存储库](https://github.com/siderolabs/talos) 中查看更多信息。

### 为什么要使用 Talos？

Talos 使 Kubernetes 环境更加安全可靠。众所周知，Talos 适用于 Kubernetes 等分布式系统，如果您希望您的 Kubernetes 环境更加安全可靠，则应该使用 Talos。

### 我们可以在裸机上运行 Talos 吗？

如果您希望在裸机上配置 Kubernetes，Talos 是理想的选择。敬请关注，了解如何在裸机上部署 Talos，订阅我们的帖子或直接联系我们以进一步讨论此事。

### 谁为 Talos 提供额外支持？

[Sidero Labs](https://www.siderolabs.com/)
- CloudRaft 用于实施和支持。
[联系我们](/contact-us) 以进一步讨论。