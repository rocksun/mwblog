# 如何使用Forklift将您的虚拟机迁移到KubeVirt

![Featued image for: 如何使用Forklift将您的虚拟机迁移到KubeVirt](https://cdn.thenewstack.io/media/2025/01/77fcecf2-migration-1024x576.jpg)

随着越来越多的公司迁移到云端，他们遇到了一个问题：许多大型的、遗留的、虚拟化的工作负载无法轻松地重构为云原生，组织选择将它们作为虚拟机继续运行，同时慢慢地为新的应用程序引入容器和Kubernetes。简而言之，虚拟机仍然存在。

但很少有人提到如何将虚拟化工作负载迁移到Kubernetes集群——当您可能有数百或数千个虚拟化工作负载时，这一点非常重要。

让我们探讨一下将[虚拟机迁移](https://thenewstack.io/the-future-of-vms-on-kubernetes-building-on-kubevirt/)到Kubernetes集群真正需要什么，一些开源项目如何帮助自动化迁移的部分过程，以及Spectro Cloud的新虚拟机迁移助手如何使这个过程变得简单易行，即使您还不是Kubernetes专家。

## 非常手动的方式：virt-v2v

首先，让我们以最困难的方式来做，看看我们如何手动将虚拟机从VMware vSphere迁移到启用KubeVirt的K8s集群。

### 客户机转换

在底层，[KubeVirt运行虚拟机](https://thenewstack.io/the-future-of-vms-on-kubernetes-building-on-kubevirt/)使用基于内核的虚拟机 (KVM)，这是一种Linux原生的一类虚拟机管理程序。因此，作为迁移的开始，我们需要将我们的VMware虚拟机转换为与KVM兼容。有一些工具可以用来完成这个任务。我们将看看virt-v2v，这是一个开源工具，用于将客户机操作系统从许多专有虚拟机管理程序转换为KVM。

首先，我们需要在跳板主机上安装virt-v2v。Virt-v2v可以通过大多数包管理器获得。我们需要确保我们的跳板主机可以访问我们的vCenter和目标Kubernetes集群。

接下来，我们需要访问目标机器。Virt-v2v支持本地文件路径，以及通过网络直接访问虚拟机磁盘。在此阶段，我们应该关闭虚拟机以防止数据丢失或损坏。最好使用快照备份磁盘。

当我们的跳板主机设置好后，我们希望迁移的虚拟机已关闭，并且磁盘可访问。我们现在可以开始转换过程了。

转换过程完成后，我们可以检查工作目录，查看转换后的磁盘是否可用。除了转换磁盘外，此过程还删除了VMware Guest Tools（不再需要它们）并安装了VirtIO驱动程序，这对于虚拟机在迁移后正常运行至关重要。

现在我们的虚拟机磁盘已转换为RAW格式（一种KVM友好的格式），我们需要一种[方法将其在Kubernetes集群中可用](https://thenewstack.io/cluster-api-offers-a-way-to-manage-multiple-kubernetes-deployments/)。

### 磁盘导入

容器通常被认为是短暂的。因此，考虑到虚拟机在设计上是在电源循环之间持久存在的，所以在Kubernetes中运行虚拟机的想法似乎有些奇怪。但是，使用K8s的基元，例如DataVolumes (PVs)和PersistantVolumeClaims (PVCs)，我们可以持久化虚拟机磁盘，即使虚拟机已关闭。

首先，我们需要确保[容器化数据导入器 (CDI)](https://github.com/kubevirt/containerized-data-importer)已在我们的KubeVirt集群中配置。CDI是一个用于Kubernetes的持久存储[管理附加组件](https://thenewstack.io/managing-kubernetes-clusters-for-platform-engineers/)，主要用于提供一种声明式的方法来为Kubevirt虚拟机在PVC上构建虚拟机磁盘。

接下来，使用virtctl（一个用于与Kubernetes集群中的虚拟机交互的KubeVirt CLI），我们可以开始数据导入，使用CDI将我们的磁盘导入集群。通过选择上传到DataVolume，CDI将根据集群的默认StorageClass自动配置具有适当设置的PVC。

数据上传完成后，我们的虚拟机磁盘就可以绑定到pod了。

### 虚拟机模板

现在磁盘已导入，我们可以定义虚拟机的外观。这是通过名为VirtualMachine的自定义资源 (CR) 完成的。在这里，我们可以定义诸如资源请求和附加磁盘等内容。要附加我们导入的磁盘，我们将在磁盘和卷部分引用它。

最后，我们可以将此VirtualMachine安装到我们的KubeVirt集群中。现在，使用virtctl，我们可以启动我们的虚拟机。瞧！我们已经成功地将VMware vSphere虚拟机迁移到Kubernetes集群中。

现在可以使用virtctl访问正在运行的虚拟机，或者通过访问Palette中的虚拟机编排器 (VMO) 仪表板来访问。
简单吧？现在，对每台机器、每个主机、每个数据中心都这样做。（这可能会变得很混乱。）

## 更省力的方式：Forklift
围绕 virt-v2v 出现了一些更高抽象的工具，可以帮助自动化大规模转换和迁移——无需 Bash。像 [Forklift](https://github.com/kubev2v/forklift) 这样的项目旨在提供一种 Kubernetes 原生方式，将多台机器从 VMware 迁移到 KubeVirt。Forklift 通过引入一个控制器来实现这一点，该控制器协调多个自定义资源以协调迁移。

首先，我们需要一个已配置 KubeVirt 的正在运行的 Kubernetes 集群。接下来，我们可以安装 Forklift。这包括部署组件，例如 Operator Lifecycle Manager (OLM)、Certificate Manager、Forklift Operator、Forklift Controller 和几个支持操作符来处理验证。一旦安装了相关的自定义资源定义 (CRD) 并部署了操作符，我们就可以开始设置迁移了。

### 自定义资源
Forklift 使用六个 Kubernetes CR 来执行迁移：

* **Provider**: VM 平台的表示。这可以是 vCenter（源）或 KubeVirt（目标——我们的目标集群）。提供程序包含诸如源 URL 和包含凭据的密钥的引用等信息。
* **Host**: 对特定 ESXi 主机的可选引用。这可以通过绕过 vCenter 并直接从虚拟机管理程序访问磁盘来帮助加快迁移速度。
* **Storage map**: 将 vCenter 存储映射到 Kubernetes 存储类的途径。
* **Network map**: 将 vCenter 网络配置映射到 Kubernetes 网络的途径。
* **Plan**: 将所有与迁移相关的数据整合在一起的核心资源。它引用提供程序、主机和映射，并详细说明应迁移的所有虚拟机。
* **Migration**: 代表正在运行或已完成的计划。

这些资源中的大多数都依赖于来自 vCenter 或 ESXi 的信息。例如，我们需要[知道我们的虚拟机正在使用哪些网络和存储设备](https://thenewstack.io/honey-i-secured-your-boot-edge-trusted-boot-with-kairos/)，以及虚拟机的 ID。这可以使用 VMware 的 govc 等工具查询。

此外，还使用多个密钥和 ConfigMap 来配置提供程序和计划的某些方面。所有这些都应与六个自定义资源一起创建。

### 运行迁移
要开始迁移，请将所有自定义资源及其伴随的配置安装到 Kubernetes 集群中。一旦它们都协调完毕并进入“就绪”状态，迁移就会开始，迁移 CR 转变为“执行”状态就标志着迁移的开始。您可以使用 kubectl 等工具监控迁移进度。

迁移过程大致可以概述如下：

* **磁盘分配**: 创建 PV 和 PVC。
* **镜像转换**: 创建一个 pod 来运行 virt-v2v 进程。
* **磁盘传输**: 使用 CDI 上传转换后的镜像。
* **虚拟机创建**: 在集群中安装 VirtualMachine 清单。

一旦计划达到“成功”状态，迁移就完成了，并且在目标命名空间中创建了一个虚拟机。

## VM 迁移助手方式
拥有一个控制器来为您协调迁移非常方便。但是，管理计划、获取和填写虚拟机元数据以及手动处理存储和网络映射既繁琐又容易出错。

在大规模情况下，填写这么多的 YAML 会让你感觉仍然是在完全手动进行迁移。如果您来自 vCenter 的 UI 并且刚刚进入 Kubernetes 的世界，您可能正在寻找更熟悉的界面。这就是 VM 迁移助手。

基于 Forklift 的核心功能，Spectro Cloud Palette 的 VM 迁移助手是一个基于 Web 的 UI，用于规划、配置、管理和运行迁移。

无论您是想迁移几台还是几百台虚拟机（单个计划最多 500 台！），迁移助手 UI 都可以处理设置和部署 CR、ConfigMap 和密钥的复杂性，因此您可以专注于更重要的任务：规划大规模基础设施迁移。

### 使用助手
在您的 Palette 管理的集群中安装了 VM 迁移助手包后，您可以在浏览器中访问 UI。

系统将指导您配置提供程序，为您处理验证，并透明地显示任何问题。一旦您的提供程序部署并准备就绪，您就可以开始设置您的计划了。

使用提供程序，VM 迁移助手会获取源环境中的所有虚拟机。您可以过滤、排序和检查虚拟机以轻松构建计划。关于虚拟机潜在问题的警告——例如名称不符合 RFC 1123 或禁用了更改块跟踪——清晰可见，以帮助您做出明智的决策。
选择好所有所需的虚拟机后，系统会显示存储和网络映射选项。系统预先配置了合理的默认值，但如果需要自定义配置，可以手动添加其他映射。还可以指定目标命名空间。

创建计划时，所有必要的自定义资源都会在集群上创建。几秒钟后，计划将进入“就绪”状态，这意味着可以启动它。在计划概述中，您可以通过选择用于迁移的自定义源网络或添加挂钩（一种在迁移之前或之后对虚拟机执行操作的方法）来进一步自定义计划。

启动后，您可以在UI中监控迁移进度，其中包括计划中每个虚拟机的分步细分。您还可以监控迁移统计信息并检查与迁移相关的任何资源。


### 温迁移
到目前为止，我们一直在讨论冷迁移，其中源虚拟机始终处于关闭状态。这些迁移在技术上更简单，但需要更多停机时间。温迁移提供了一种替代方案，使用快照。

可以使用VM迁移助手执行温迁移。要开始，请按照与冷迁移相同的方式设置计划。在计划概述屏幕上，切换“温迁移”开关以将迁移标记为温迁移。迁移开始时，您的源虚拟机将继续运行。将定期拍摄磁盘快照并导入到Kubernetes集群。然后，您可以安排“切换”——虚拟机将短暂关闭的时刻，以及自上次快照以来任何新数据都将被传输。最后，一旦传输完成，虚拟机将在Kubernetes集群中启动。

通过在虚拟机仍在运行时传输大部分磁盘数据，温迁移有助于最大限度地减少停机时间，并允许异步执行迁移的冗长部分。

当然，温迁移也带来自身的一系列挑战。由于在一次迁移过程中可能需要进行多次数据传输，并且切换阶段仍然需要一些停机时间，因此应仔细规划迁移以确保最小的停机时间并减少对主机网络的压力。迁移后数据的验证对于验证在切换时刻没有发生数据丢失或损坏至关重要。


### 导入OVA
开放虚拟设备 (OVA) 是一种流行的虚拟机打包格式。它是一个单一的、可移植的存档，包含虚拟机的完整定义和内容。

在传统的VMware数据中心中，可以快速导入OVA以部署新的虚拟机。OVA通常不仅包含VM规范，还包含在其上运行的应用程序。这些应用程序通常需要在机器首次启动时从VMware Tools守护程序获得的OVF XML配置。

VMware有一套工具来促进这一点，但是当来宾操作系统被转换时，这些工具将被移除，因为它们通常不需要基于KVM的机器。这意味着应用程序不仅无法访问环境，而且您作为管理员甚至无法访问设置环境。

由于OVA在管理虚拟化工作负载中起着关键作用，而OVF环境是难题的关键部分，因此我们必须解决这个问题并构建一个解决方法。

当您创建OVA提供程序时，VM迁移助手将解析源中存在的所有OVA。将提取所需的OVF环境变量。创建计划时，您将有机会配置任何需要设置环境变量的虚拟机。变量将作为磁盘附加到虚拟机，并在其启动后立即提供给导入的设备。


## 更大难题的重要组成部分
完整的VMware到K8s迁移比我们今天讨论的要复杂得多。它涉及仔细的规划、维护多个并行环境、配置网络和入口以确保您的用户不会以任何方式受到干扰等等。

它还需要以缓慢而受控的方式进行，并且可能需要数月甚至数年时间，具体取决于要移动的工作负载的大小。不幸的是，这意味着组织需要很长时间才能完全改变其基础设施。

鉴于像基础设施迁移这样的大型任务的所有复杂性，您需要尽可能多的帮助。我们已经编制了一些[网络研讨会](https://www.spectrocloud.com/webinars/the-new-home-for-your-vms-kubernetes)、[博客](https://www.spectrocloud.com/blog/the-future-of-vms-on-kubernetes-building-on-kubevirt)和[参考架构](https://www.spectrocloud.com/resources/collateral/vmo-architecture-pdf)来帮助促进迁移。
手动VM迁移方法可以作为一到两台机器的概念验证，但随着规模的增长，您需要使用Forklift或VM Migration Assistant等更自动化的工具。

要了解有关VM Migration Assistant的更多信息，请[查看我们的文档](https://docs.spectrocloud.com/vm-management/vm-migration-assistant/)，并务必与我们的专家[预约演示](https://www.spectrocloud.com/get-started)，看看我们如何提供帮助。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。