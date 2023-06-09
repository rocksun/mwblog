# 寻找 k3OS 替代方案？为边缘 K8s 选择容器操作系统

翻译自 [Looking for a k3OS Alternative? Choosing a Container OS for Edge K8s](https://thenewstack.io/looking-for-a-k3os-alternative-choosing-a-container-os-for-edge-k8s/) 。

6 个主要的容器操作系统的比较，它们通常会与轻量级的 Kubernetes 发行版(如K3S)配对使用。

![](https://cdn.thenewstack.io/media/2023/03/f51a1245-key2.jpg)
*Dall-e 2 的艺术 “Unsecure Kubernetes”*

作为系统管理员，您知道部署和维护 Linux 发行版可能会很痛苦。

即使出现了基础设施即代码（IaC）范式，如 Terraform ， Linux 系统也经常由于增量更新而处于不同的状态（“snowflakes”）。

## 容器操作系统：为容器和 Kubernetes 构建

今天，我们需要针对使用 Kubernetes 的容器化云原生工作负载优化我们的 Linux 发行版。这意味着保持基本操作系统稳定可预期，这样顶部的集群可以具有相同的可靠性、性能和安全性运作，并优化内核以及 K8s 需要的依赖关系和服务。

如果您采用针对 Kubernetes 优化的容器操作系统，则可以避免这种努力。容器操作系统通常在资源有限时部署，尤其是在边缘计算环境中。这就是为什么它们通常是轻量级的，并与轻量级（低于 100 兆字节）的 Kubernetes 发行版（如 K3S）配对。

## 让我们比较一下六种主要的容器操作系统

在本文中，我们将帮助您找到适用于 Kubernetes 的最佳操作系统。我们将介绍：

* CoreOS，云原生操作系统的先驱
* Flatcar Container Linux，继任者
* K3OS，轻量级
* Bottlerocket，亚马逊的
* Talos，CNCF 认证的 installer
* Kairos，工厂

## CoreOS，云原生操作系统的先驱

可以说，第一个容器操作系统是 CoreOS 。 CoreOS 团队在 2013 年发布了第一个版本，甚至在 Kubernetes 创建之前。 CoreOS Linux 具有许多安全功能，例如自动更新和只读文件系统。这种类型的操作系统被认为是“不可变的”。CoreOS还包括一个漏洞扫描程序和一个容器防火墙。

2018 年，红帽公司收购了 CoreOS ，这导致 Kinvolk 团队创建了 Flatcar Container Linux 作为开源的替代产品。

## Flatcar Container Linux，继任者

与 CoreOS Linux 一样， Flatcar 是不可变的。它在初始启动过程中是可配置的，任何进一步的修改都不会持久。只有特定目录中的用户数据在重新启动后仍然存在。

除了不可变且易于使用外， Flatcar 还具有令人兴奋的功能，例如自动系统更新和主动/被动分区功能，使可扩展性变得容易。

值得一提的是，ISO 映像在部署到裸金属服务器时是可下载的，这使得 Flatcar 非常适合 Kubernetes 边缘的情况。

然而，它缺乏开箱即用的自动化方法来构建 Kubernetes 集群，也不提供任何用于管理集群生命周期的 Kubernetes 原生框架。在我们看来，它属于 DIY 的范畴，其中包含容器 OS 的管理，但 Kubernetes 层完全脱离。

对于任何希望管理严肃的 Kubernetes 部署的人来说，我们需要继续寻找。

## K3OS，轻量级

K3OS 是由 Rancher Labs 专门为 K3 S集群设计的轻量级不可变操作系统。它只包含为 Kubernetes 集群提供支持的基本组件。k3OS 和 K3S 的轻量级带来了许多好处，例如减少攻击面、缩短启动时间和更精简的文件系统，这使其成为边缘用例的候选者。

### Kubernetes Native

此外，一旦集群运行，您就可以使用 Kubernetes API 轻松升级它。事实上，k3OS 与 Rancher 系统升级控制器的集成提供了一个 Kubernetes 原生解决方案，通过扩展 Kubernetes API 来升级节点。它使 k3OS 节点能够利用自己的 Kubernetes 集群功能从最新的 GitHub 版本自动升级。这使它成为一个真正的 Kubernetes 原生进程。

然而，自定义 k3OS 镜像和自动化其随 Kubernetes 集群部署的配置非常的复杂。此外,没有Kubernetes原生的方法来生成这些镜像或轻松部署到公有云。

###  一个死项目？

虽然这些功能可能是该项目的一些有趣的后续步骤，但最新的 k3OS 版本于 2021 年 10 月[发布](https://github.com/rancher/k3os/releases)，并且没有解决任何 GitHub 问题。随着 k3OS 的开发显然已经死亡，用户现在正在寻找其他替代方案（[此处](https://github.com/rancher/k3os/issues/846)为其他评论示例），很难推荐在当今的任何生产环境中使用 k3OS 。

下一步是什么？

## Bottlerocket，亚马逊的

Bottlerocket 是另一个基于 Linux 的开源操作系统，专为在 Kubernetes 集群上安全运行容器化工作负载而设计。

### 非常适合 AWS 忠诚者

亚马逊网络服务 （AWS） 于 2020 年创建了 Bottlerocket，它已与各种 AWS 服务集成，例如弹性 Kubernetes 服务 （EKS）、弹性容器服务 （ECS）、Fargate、EC2 实例、Graviton2 和 Amazon Inspector。因此，虽然您可以在各种环境中运行Bottlerocket，但它主要针对 AWS 公共云。

虽然在 AWS 云或 VMware vSphere 中部署很容易，但在裸机服务器或边缘环境中配置 Bottlerocket 要困难得多。（您可以在[此处](https://github.com/bottlerocket-os/bottlerocket/blob/develop/PROVISIONING-METAL.md)找到完整指南）。在 VMware vSphere 中， Bottlerocket 只能作为工作节点运行，这也是一个不便。这意味着现有的控制平面节点必须已经就位，您必须单独配置该节点。

该系统只能通过 API 进行配置，并具有安全的带外访问方法。只能通过管理或控制容器访问 Bottlerocket ，这些容器是必须在单独的容器实例中安装的额外组件。没有 SSH 服务，甚至没有 shell 。

### Kube Native

Bottlerocket Kubernetes operator 负责系统更新，而镜像则由 TUF（更新框架）保护。这是一个完全 Kubernetes 原生的工作流程，遵循与 Rancher 系统升级控制器相同的原则。现有镜像将被替换为新镜像，并且在引导过程中发生故障时具有回滚功能。

此外，Bottlerocket 支持多个“变体”，对应于一组支持的集成和功能，例如 Kubernetes，ECS，Nvidia GPU 等等。

也可以从精选的变体中构建自己的 Bottlerocket 镜像，而不是直接下载工件。这需要 Rust 和 Docker BuildKit 。最后，值得注意的是，在撰写本文时没有包含 K3S 的变体。

## Talos，CNCF 认证的 Installer

Talos 是一个极简主义的 Linux 发行版，从头开始设计用于运行 Kubernetes。

它的主要目的是将 Kubernetes 原则引入操作系统层。它引入了一种实时管理操作系统和 Kubernetes 本机组件的声明性方法，允许以简化和高效的方式来处理操作并浏览整个系统的生命周期。它由 Sidero Labs 于 2018 年发布（预发布），完全开源。

### 对 CAPI 友好的容器操作系统

Talos 完全删除了 SSH 和控制台访问权限，转而支持 API 管理。您可以在任何超大规模云、裸金属服务器和虚拟化系统中部署 Talos。该工具还提供了一种通过执行命令 talosctl cluster create 来使用 Docker 运行时部署本地 Talos 集群的简单方法。

它还包括集群 API （CAPI） 提供程序、群集 API 引导提供程序 Talos 或 CABPT。它的作用是为计算机生成引导程序配置，并将更新的资源与 CAPI 进行协调。控制平面配置有一个单独的提供程序，即集群 API 控制平面提供程序 Talos （CACPPT）。

### 用于生命周期管理的强大 CLI

`talostctl` 命令行界面允许您与 Talos 节点和 Kubernetes 集群进行交互，而无需任何终端或 SSH 连接。它利用 API 和 Kubernetes CRD 。这为所有 Kubernetes 基础设施组件实现了无摩擦的生命周期管理。

Talos 通过 `talosctl` CLI 和声明性输入为您提供各种操作。例如，您可以通过运行`talosctl upgrade-k8s --to 1.26.1` 以有序的方式升级整个集群，其中 1.26.1 是更新的 Kubernetes 版本。

### 强大的安全功能

Talos 在快速构建安全的 Kubernetes 集群方面非常高效。Talos 支持磁盘加密、NVIDIA GPU 和 Fabric Manager ，并允许您管理公钥基础设施 （PKI） 的生命周期。在边缘运行 Talos 时，磁盘加密非常有用。它可以在磁盘丢失或被盗的情况下保护数据。但是，它并非旨在防止对计算机（包括驱动器）进行物理访问的攻击。

它还提供内置管理功能，以促进集群生命周期管理。

例如，它依靠浮动虚拟 IP 部署高度可用的 Kubernetes 集群，而无需任何外部负载均衡器，并允许通过公共互联网上的 Wireguard 对等发现进行安全连接。如果节点发生故障，剩余的控制平面节点之一将获得 VIP 的所有权。

此外，集群在集群初始化期间会自动引导，并且可以轻松扩展和缩小控制平面。

### 轻量级，但自以为是

系统占用空间非常小，具有 80MB 的 SquashFS 镜像大小。这大大减少了群集的攻击面。但是，Talos 自以为是的方法也意味着它有一些缺点和局限性：

* 虽然减少的 OS 大小弥补了总体占用空间的差异，但它不支持 K3S 。
* 镜像自定义仅限于内核模块和根文件系统内容。
* 随着内核占用空间的减少，支持的硬件和特定内核功能的列表也会减少。
* 系统管理的某些方面比传统的 Kubernetes 环境更复杂。

因此， Talos 非常适用于在灵活性与安全的现成发行版之间权衡可以接受的特定场景。

## Kairos，工厂

在过去的几年里，Kubernetes 中出现了一个有趣的模式。它需要使用 Kubernetes 作为可扩展的 API 来添加自动化功能。

例如，Cluster API 允许通过使集群逻辑组件成为 Kubernetes 中的一等公民来部署 Kubernetes 集群。因此，从现有的 Kubernetes 集群中，您可以引导一个新的 Kubernetes 集群，并在部署后委派其管理。

Kairos 也遵循同样的原则。它允许您通过扩展 Kubernetes API 来构建和自定义不可变的操作系统镜像和 Kubernetes 集群。它通过监视 Kairos 自定义资源的自定义控制器提供这些功能。控制器根据对这些资源执行的 CRUD 操作采取适当的操作。

### 构建您选择的操作系统的工厂

Kairos 提供的不仅仅是一个容器专用的操作系统， Kairos 充当一个 Kubernetes “工厂”，生产 K3S 集群，这些集群由您选择的不可变操作系统支撑。与前面描述的其他解决方案相反， Kairos 是一个元发行版，这意味着它能够将任何现有的 Linux 发行版转换为不可变的操作系统。

它不是自以为是的，而是可以灵活地使用您选择的操作系统。选择发行版后， Kairos 会发布一个不可变的工件，您可以将其部署为支持 Kubernetes 集群的完整操作系统。

### OCI 注册表简化 ISO 镜像构建

唯一的要求是该系统的 OCI 兼容的容器镜像。Kairos 依赖开放容器计划(OCI)容器注册表来从容器镜像构建全功能的 OS 。这简化了 OS 构建和更新过程，因为它是通过使用 Dockerfile 和容器运行时实现的。另外， Kairos 还为每次发布提供预构建的镜像。

Kairos 通过 ISO 镜像提供结果工件，该镜像可以通过多种选项制作：Kubernetes自定义资源定义(CRDs)、 Preboot 执行环境(PXE)启动或手动将 ISO 镜像挂载到目标服务器上。

Kairos 的另一个关键功能是 [AuroraBoot](https://github.com/kairos-io/AuroraBoot) 。它允许您通过与动态主机配置协议(DHCP)服务器合作直接从网络引导 Kairos 镜像。当前， Aurora 以 Docker 容器的形式运行，但很快将以 Kubernetes Pod 的形式提供。有了 Aurora ，您需要的仅仅是指定要部署为 Kubernetes 集群 OS 的容器镜像以及 cloud-init 配置的配置文件。

### 自协调集群引导

Kairos 原生支持 Kubernetes。更具体地说，它提供了 K3S 集群，使其成为 Kubernetes 边缘用例的完美选择。

在这种情况下，Kairos 还能够自协调 Kubernetes 集群的引导程序，而无需任何中央服务器。这意味着它可以按需部署高可用性 （HA） Kubernetes 集群，除了所需数量的控制平面节点和 kube-vip 使用的虚拟 IP 之外，不需要其他设置。将此方法与 Aurora 结合使用，您可以瞬间通过网络自动部署 HA 集群。选举过程定义了每个节点的角色，并完全通过共享账本进行分配。

因此，无论您是要部署单节点集群，还是要部署具有多个控制平面节点的大型 HA 集群，该过程都是相同的。因此，它大大减少了集群构建，同时还允许更好的可扩展性。

### 高安全性

在安全性方面，Kairos 可以选择使用本地受信任的平台模块 （TPM） 芯片提供磁盘加密。支持多种场景：

* 加密密钥可以存储在 TPM 芯片中
* 使用 TPM 密钥对加密后，可以使用外部服务器存储用户数据分区的加密密码
* 可以使用密钥管理(KMS)服务器存储密码并在 TPM 挑战之后将其返回给节点

最后，Kairos 使用与 cloud-init 兼容的云配置格式简化了功能配置。它为动态配置提供模板化功能，简化自动化以及与 CI/CD 管道的集成。

Kairos 最初是为 Kubernetes 边缘操作创建的，但它也是在数据中心的裸金属或虚拟服务器上运行 Kubernetes 集群的绝佳选择。

它的多功能性和基础 Linux 发行版的选择使 Kairos 成为受某些供应商和操作系统约束但仍希望大规模利用容器专用操作系统，不变性和自动化的企业客户的理想解决方案。

## 为什么需要容器操作系统

Kubernetes 是一个复杂的分布式系统，你不能在糟糕的基础上构建集群。虽然 Kubernetes 通常被认为是“云操作系统”，但它本身并不是一个操作系统。它需要一个通过不变性和专业化提供强大而稳定的支持的操作系统。

不可变性强制实施声明性驱动的状态，该状态支持所有现代基础结构工具，消除雪花并带来更好的性能可预测性和更高的可伸缩性。

对于边缘用例，大多数操作都是远程执行的，本地几乎没有或没有合格的人员。因此，像原子更新、易回滚、限制可写文件系统和额外安全性等功能至关重要。所有这些都通过采用不可变的容器操作系统实现。

## 操作系统的选择对您重要吗？

在我们在本文中比较的解决方案中，只有 Kairos 允许您将任何 Linux 操作系统转换为不可变的操作系统。如果您想继续使用自己喜欢的发行版，这可能是首选项。

或者，您可以从一些提供开箱即用不变性的精选操作系统中进行选择。我们描述的大多数解决方案都是自以为是的，有其优点和缺点。

## 不要忘记大规模多集群的管理平面

容器专用的不可变操作系统只是拼图的一部分。当您在不同位置（尤其是在边缘）部署多个集群时，您还需要一个中央管理平面来帮助实现标准化、易于部署和操作。

Spectro Cloud 的 Palette Edge 建立在 Kairos 之上，并增加了中央管理功能。它为集群配置文件提供了一个额外的抽象层，允许您创建标准化的 Kubernetes 集群配置，并在关联所需的边缘计算机时部署到任何地方。

但不要信我的话！您可以[免费试用 Palette Edge](https://www.spectrocloud.com/free-tier/) ，并将其与本文提到的其他解决方案进行比较，或者[查看文档](https://docs.spectrocloud.com/clusters/edge/native)。 