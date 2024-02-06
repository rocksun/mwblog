<!--
title: 使用talos linux安装Proxmox kubernetes
cover: https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Proxmox-Kubernetes-with-Talos-Linux-780x470.png
-->

就在几天前，我发布了一篇新文章，介绍了在 [VMware vSphere 上安装 Talos Linux](https://www.virtualizationhowto.com/2024/01/talos-linux-kubernetes-vmware-vsphere-installation/) 的方法。Talos 是一个很好的平台，可以稳定地运行 Kubernetes，并将安全性作为首要关注点。我们还可以从在 Proxmox 上运行 Talos Linux 以配置 Kubernetes 集群中受益。让我们以在 Proxmox 中配置 Talos Linux 为例。

> 译自 [Proxmox Kubernetes Install with Talos Linux](https://www.virtualizationhowto.com/2024/01/proxmox-kubernetes-install-with-talos-linux/)。作者 Brandon Lee 是 Virtualizationhowto.com 的高级作者、工程师和所有者，拥有超过二十年的信息技术经验。在为众多《财富》500强公司以及不同行业工作过后，Brandon 在各种 IT 领域积累了丰富的经验，是开源技术的坚定支持者。Brandon 拥有许多行业认证，热爱户外活动，并喜欢与家人共度时光。

## Talos Linux 的优势

Talos 是一个在 Proxmox Kubernetes 或多个虚拟化平台上运行 Kubernetes 的优秀平台。即使你可以运行像 k3s 或 k0s 这样非常小的 Kubernetes 发行版，但仍然需要一个基础[操作系统](https://www.virtualizationhowto.com/2020/01/crypt32-dll-vulnerability-affects-hyper-v-and-windows-operating-systems/)来运行这些容器编排平台。

Talos 是一个集成了 Kubernetes 的小型 Linux 平台，同时也是一个由 API 管理的操作系统。这意味着与其他 Linux 版本不同，它没有 shell 或交互式控制台。

此外，它可以在裸金属上运行，并从 ISO 镜像安装。这是我们将在 Proxmox Kubernetes 中使用 Talos Linux 的方法。

## 在 Proxmox 中安装 Talos Linux

现在让我们看看在 Proxmox 中安装 Talos Linux 的过程。与 [VMware vSphere ](https://www.virtualizationhowto.com/2022/01/create-kubernetes-cluster-with-rancher-and-vmware-vsphere/)不同，我们没有 OVA 部署文件或安装脚本。相反，在 Proxmox 中，我们使用 ISO 安装过程。

请注意以下概述的步骤，以在 Proxmox 中使用 Talos Linux 进行 Kubernetes 安装：

1. 安装 talosctl 命令行工具
2. 下载 Talos Linux ISO 并上传到 Proxmox
3. 为控制平面和工作节点创建虚拟机
4. 在 Proxmox 中启动 Talos [Linux 虚拟机](https://www.virtualizationhowto.com/2021/05/terraform-vsphere-tutorial-linux-virtual-machine-clone/)，并记录控制平面 IP
5. 使用 talosctl 命令生成配置文件
6. 应用控制平面节点配置
7. 引导集群
8. 应用工作节点配置

## 1. 安装 talosctl 命令行工具

你可以在 Linux 工作站或 Windows 的 WSL 安装中[使用以下命令](https://www.virtualizationhowto.com/2019/04/upgrade-to-vmware-vsphere-esxi-6-7-update-2-with-command-line/)轻松安装 talosctl 命令行工具：`curl -sL https://talos.dev/install | sh`

## 2. 下载 Talos Linux ISO 并上传到 Proxmox

在安装了 talosctl 命令行工具之后，要完成的下一个任务之一是下载 Talos Linux ISO 并将其上传到 Proxmox。

您可以从 Github 仓库的官方 releases 链接处下载 Talos Linux ISO 镜像：[Releases · siderolabs/talos · GitHub](https://github.com/siderolabs/talos/releases)。

根据您的架构下载 ISO。对于 Proxmox，我们将[下载](https://www.virtualizationhowto.com/2020/08/host-cannot-download-files-from-vmware-vsphere-lifecycle-manager-patch-store/) metal-amd64.iso 文件。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Download-the-Sidero-meta-ISO-with-Talos.png)

*下载 talos 的 sidero meta iso*

现在，我们将上传该文件到 Proxmox 的镜像库。单击您的本地[存储](https://www.virtualizationhowto.com/2022/09/proxmox-create-iso-storage-location-disk-space-error/)或标记为 ISO 存储的其他存储，并单击 **Upload** 按钮。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Beginning-the-process-to-upload-the-Talos-Linux-ISO-to-your-Proxmox-server.png)

*开始上传 Talos Linux ISO 到 Proxmox 服务器的过程*

选择您上面下载的 metal-amd64.iso 文件，然后再次点击上传按钮。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Select-the-ISO-and-upload-the-file.png)

*选择 ISO 并上传文件*

上传任务成功完成。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/The-upload-ISO-task-completes-successfully.png)

*上传 ISO 任务成功完成*

## 3. 为控制平面和工作节点创建虚拟机

现在，我们已经将 Talos Linux 的 ISO 镜像上传到 [Proxmox 主机](https://www.virtualizationhowto.com/2023/11/upgrade-proxmox-host-to-8-1-tutorial-steps/)，我们可以创建一个新的虚拟机。右键单击要用于创建虚拟机的主机，然后单击 **Create VM**。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Beginning-the-process-to-create-a-new-Proxmox-virtual-machine-for-control-plane.png)

*开始创建用于控制平面的新 proxmox 虚拟机的过程*

它将启动 **Create [Virtual](https://www.virtualizationhowto.com/2023/12/vagrant-boxes-create-virtual-machines-in-seconds-on-virtualbox-hyper-v-and-vmware/) Machine** 向导。（注意切换到 light 模式以使选项更为突出）。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Creating-the-Talos-control-plane-VM.png)

*创建 Talos 控制平面虚拟机*

在 **OS** 屏幕上选择您的 [ISO 镜像文件](https://www.virtualizationhowto.com/2023/11/iventoy-network-boot-of-iso-files-made-easy/)。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Configure-the-control-plane-VM-to-boot-from-the-Talos-Linux-ISO.png)

*配置控制平面虚拟机以从 Talos Linux ISO 引导*

在 **System** 选项卡上保留默认设置。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Control-plane-system-configuration-in-Proxmox.png)

*Proxmox 中的控制平面系统配置*

在这里，我将磁盘大小降低到了10GB。如果需要更大的磁盘，这也是可以的。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Configuring-the-disks-in-Proxmox-for-the-control-plane-node.png)

*在Proxmox中为控制平面节点配置磁盘*

在**CPU**屏幕上根据需要调整 CPU Socket 和 core。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Control-plane-virtual-machine-memory-configuration.png)

*Proxmox控制平面虚拟机的CPU配置*

同样，在内存屏幕上调整**内存**。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Control-plane-virtual-machine-memory-configuration.png)

*控制平面虚拟机内存配置*

在 **Network** 选项卡上选择要用于Talos Linux[虚拟机控制](https://www.virtualizationhowto.com/2023/02/migrate-unifi-controller-from-a-virtual-machine-to-a-docker-container/)平面VM的网络连接。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Proxmox-Kubernetes-control-plane-VM-network-configuration.png)

*Proxmox Kubernetes控制平面VM的网络配置*

在 **Confirm** 屏幕上确认选项。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Confirm-the-Proxmox-control-plane-VM-configuration.png)

*确认Proxmox控制平面VM配置*

## 在Proxmox中创建工作节点虚拟机

我们在一般屏幕上创建了第一个Talos Linux控制平面[虚拟机](https://www.virtualizationhowto.com/2019/01/boot-esxi-virtual-machine-from-passthrough-usb/)。需要注意的是，我使用了与上述控制平面[虚拟机](https://www.virtualizationhowto.com/2019/01/boot-esxi-virtual-machine-from-passthrough-usb/)相同的选项，因此以下截图仅供记录。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Naming-the-new-worker-node-in-Proxmox.png)

*在Proxmox中为新的工作节点命名*

选择Talos Linux的ISO镜像。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Boot-from-the-Talos-ISO-image-for-the-Proxmox-Kubernetes-worker-node.png)

*从Talos ISO镜像引导Proxmox Kubernetes工作节点*

在System屏幕上保留默认设置。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Worker-node-system-configuration-in-Proxmox.png)

*Proxmox Kubernetes Talos工作节点的系统配置*

根据需要调整磁盘大小。不需要太多。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Disk-configuration-for-the-Proxmox-Kubernetes-Talos-worker-node.png)

*Proxmox Kubernetes Talos工作节点的磁盘配置*

配置CPU。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/CPU-configuration-for-the-Proxmox-Kubernetes-Talos-worker-node.png)

*Proxmox Kubernetes Talos工作节点的CPU配置*

配置工作节点内存。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Worker-node-memory-configuration.png)

*工作节点内存配置*

[配置网络](https://www.virtualizationhowto.com/2019/05/configure-network-i-o-control-nioc-with-vsan-vsphere-distributed-switch/)连接。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Worker-node-network-configuration.png)

*工作节点网络配置*

确认配置设置。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Confirm-the-Talos-Linux-worker-node-configuration-for-Proxmox-Kubernetes-cluster.png)

*确认 Talos Linux 工作节点在 Proxmox Kubernetes 集群中的配置*

## 4. 在 Proxmox 中启动 Talos Linux 虚拟机，并记录控制平面 IP

从 Talos ISO 启动您的控制平面虚拟机。您将看到以下画面。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Booting-the-Proxmox-Kubernetes-cluster-Talos-control-plane-node.png)

*启动 Proxmox Kubernetes 集群的 Talos 控制平面节点*

节点将引导到以下画面，并应从 DHCP 服务器获取 IP 地址。请注意您的控制平面节点自动配置的 IP 地址。您将看到节点处于**维护模式**，准备进行引导过程。我们可以从控制节点的控制台获得许多其他信息，包括 Talos 版本、kubelet 状态、Kubernetes 版本等。此外，您甚至可以在屏幕底部看到一些导航选项，按 **F2** 进入**监视模式**，按 **F3** 进入**网络配置**。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Get-the-IP-address-of-the-Proxmox-Kubernetes-cluster-Talos-control-plane.png)

*获取 Proxmox Kubernetes 集群 Talos 控制平面的 IP 地址*

## 5. 使用 talosctl 命令生成配置文件

现在我们已经有了运行 Talos Linux 控制平面节点的 [Proxmox 虚拟机](https://www.virtualizationhowto.com/2023/12/proxmox-vlan-configuration-management-ip-bridge-and-virtual-machines/)的 IP 地址，我们可以生成我们的 Kubernetes 集群所需的机器配置文件。

首先，我们将导出一个环境变量，以便在 talosctl 命令中重用我们的控制平面节点 IP。请用您的 IP 地址替换: `export CONTROL_PLANE_IP=10.1.149.173`。

接下来，我们将使用控制平面节点 IP 生成控制平面节点和工作节点的机器配置文件。

```bash
talosctl gen config talos-proxmox-cluster https://$CONTROL_PLANE_IP:6443
```

如果您想配置机器配置文件存放的输出目录，可以使用以下命令进行设置：

```bash
talosctl gen config talos-proxmox-cluster https://$CONTROL_PLANE_IP:6443 --output-dir _out
```

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Export-the-control-plane-IP-address-and-generate-the-machine-configs.png)

*导出控制平面 IP 地址并生成机器配置*

## 6. 应用控制平面节点配置

现在我们有了配置文件，我们可以开始创建控制平面节点的配置。

```bash
talosctl apply-config --insecure --nodes $CONTROL_PLANE_IP --file controlplane.yaml
```

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Apply-the-control-plane-YAML-file.png)

*应用控制平面 YAML 文件*

如果您连接到 Proxmox 中控制平面[虚拟机](https://www.virtualizationhowto.com/2019/01/boot-esxi-virtual-machine-from-passthrough-usb/)的控制台，您应该开始看到它引导并配置 Kubernetes。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Booting-and-configuring-Kubernetes-on-Talos-control-plane-node.png)

*在 Talos 控制平面节点上引导和配置 Kubernetes*

## 7. 引导集群

在应用了 controlplane.yaml 配置之后，我们需要引导集群以启动 **etcd** 配置。

为了引导集群，我们需要运行一些命令。首先，我们需要设置 TALOSCONFIG、endpoint 和 node，使其指向我们已经启动的控制平面节点。

```bash
export TALOSCONFIG="talosconfig" talosctl config endpoint $CONTROL_PLANE_IP talosctl config node $CONTROL_PLANE_IP
```

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Exporting-the-talosconfig-and-control-plane-address-for-node-and-config.png)

*导出 talosconfig 和控制平面地址以供节点和配置使用*

现在我们可以运行以下命令：

```bash
talos bootstrap
```

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Running-the-talosctl-bootstrap-command.png)

*运行 talosctl bootstrap 命令*

一旦我们引导了集群，最终应该看到所有内容都以绿色 STATUS 全部正常运行。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Control-plane-fully-running-and-bootstrapped.png)

*控制平面完全运行和引导完成*

现在我们应该能够通过 kubectl 看到我们的控制平面正在运行。首先，我们需要检索 kubeconfig 文件：

```bash
talosctl kubeconfig .
```

您还可以将 kubeconfig 文件导出为变量：

```bash
export KUBECONFIG=kubeconfig
```

现在我们可以正常运行 kubectl。

```bash
kubectl get nodes
```

我们看到我们的单个控制平面节点正在运行。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Getting-the-Talos-Kubernetes-nodes-using-kubectl.png)

*使用 kubectl 获取 talos Kubernetes 节点*

## 8. 应用工作节点配置

现在，让我们启动和运行我们的工作节点。在 [Proxmox 中启动](https://www.virtualizationhowto.com/2019/01/boot-esxi-virtual-machine-from-passthrough-usb/)并从 ISO 引导您的工作节点虚拟机。

工作节点的过程与控制平面节点相同。我们将注意到虚拟机上配置的 IP 地址，然后将 **worker.yaml** 配置应用到工作节点。

工作节点引导到维护模式并准备进行配置

让我们将工作节点的 IP 地址导出为变量，然后使用 talosctl 应用 worker.yaml 配置：

```bash
export WORKER_IP=10.1.149.179
talosctl apply-config --insecure --nodes $WORKER_IP --file worker.yaml
```

应用配置：

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Applying-the-worker-node-configuration.png)

*应用工作节点配置*

应用配置后，工作节点被配置完成，我们看到一切都正常运行，工作节点被指定为 node 类型的 **worker**。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Worker-node-fully-provisioned.png)

*工作节点完全配置完成*

现在，我们可以运行另一个 `kubectl get nodes`，并查看我们的控制平面和工作节点都已配置完成，并处于就绪状态以运行 pod。

![](https://www.virtualizationhowto.com/wp-content/uploads/2024/01/Using-kubectl-to-get-both-nodes-and-their-status.png)

*使用 kubectl 获取两个节点及其状态*

## Talos Linux Kubernetes 的常见问题解答

**在运行生产容器时，为什么 Kubernetes 很重要？**

它提供了一个生产容器编排引擎，允许以可伸缩性、性能、兼容性、虚拟化网络以及使用监控解决方案等多方面的优势运行容器。您可以将 Kubernetes 看作容器世界的虚拟化设置，用于调度并允许从故障中恢复。

**什么是 Sidero Metal？**

Sidero Metal 允许在裸金属上运行 Kubernetes。它简化了配置和管理，并确保物理服务器的高效利用。Sidero Metal 与 Talos Linux 的结合使您能够高效且安全地运行 Kubernetes 环境。

**Talos 如何使用 TLS 连接？**

相互 TLS 是 Talos Linux 安全框架的核心特性。此协议确保客户端和服务器相互验证，创建安全的通信通道。在 Kubernetes 环境中，安全数据传输至关重要，相互 TLS 提供了额外的安全层。

**Talos Linux 中的系统服务和管理**

Talos 保持了一个非常精简的安装，仅安装作为 Kubernetes 操作系统所需的内容。重点是通过最小化不必要的组件来减少整体攻击面和漏洞。管理 Talos Linux Kubernetes 集群只能使用 API 进行，而不能使用 SSH 或其他更危险的访问方式。您还可以使用像 Terraform 这样的基础架构即代码解决方案来管理 Talos Linux Kubernetes。

**Talos Linux Kubernetes 在 Proxmox 上易于使用吗？**

通过简单地启动虚拟机来容纳 Talos 安装，将 Talos Linux 与 Proxmox 集成是一项容易完成的任务。您将至少启动 (2) 台虚拟机。一台用于控制平面，另一台是工作节点。

**在使用 Talos 运行 Kubernetes 的好处是什么？**

在 Proxmox 上使用 Talos Linux 运行 Kubernetes 有助于提高安全性、可配置性和自动化水平。它帮助您根据安全最佳实践和其他行业标准配置您的 Kubernetes 集群。

**Talos 如何帮助实现不可变性？**

Talos Linux 的不可变基础架构概念在运行 Kubernetes 时提供了显著的优势。它通过使用基于 API 的配置过程来避免配置驱动，允许将您的集群视为“牛群”而不是“宠物”。

## 完成 Proxmox 上使用 Talos Linux 安装 Kubernetes

Talos Linux 是在许多不同的虚拟化平台上构建 Kubernetes 集群的绝佳平台。Talos Linux 提供了一个非常小、高效和安全的环境来运行您的 Kubernetes 集群。它消除了对 SSH 访问的需求，一切都是通过 API 进行配置。希望这个演示将帮助任何想要在其 Proxmox 家庭实验室环境中快速上手 Talos Linux 的人。
