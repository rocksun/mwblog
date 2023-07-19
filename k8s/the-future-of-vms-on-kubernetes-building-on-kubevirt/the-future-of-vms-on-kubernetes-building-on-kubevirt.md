# 虚拟机在 Kubernetes 上的未来：基于 KubeVirt 构建

Palette 虚拟机编排器使虚拟机成为您的集群中的一级公民。

翻译自 [The Future of VMs on Kubernetes: Building on KubeVirt](https://thenewstack.io/the-future-of-vms-on-kubernetes-building-on-kubevirt/) 。

![](https://cdn.thenewstack.io/media/2023/07/d3aa4ab2-palette1-1024x684.jpg)
*来自 Shutterstock 的图片*

还记得虚拟化曾经是炙手可热的新技术吗？二十年前，我在一家小型托管公司负责架设和部署物理服务器，那时我第一次接触到虚拟化。

看着 vMotion 实时迁移工作负载在物理主机之间转移的过程，对我来说是一个"啊哈"时刻，我知道虚拟化将改变整个生态系统。

也许因此，我在 VMware 担任架构师多年并不足为奇。

十年后，当我第一次接触容器和 Docker 时，我有了类似的"啊哈"时刻，看到这一突破对我的开发同事意味着什么。随后的几年里，显而易见的是Kubernetes是这种范式转变的自然延伸。

我相信，阅读这篇文章的许多人也经历过类似的觉醒。

尽管有二十年的创新历程，现实总是会将我们拉回现实。在企业领域，事实是我们并没有[完全过渡到](https://thenewstack.io/the-hidden-pain-of-diy-on-premises-k8s-based-software-distribution/)云原生应用或云原生基础设施。

## 数百万台虚拟机将继续存在

尽管容器化应用越来越受欢迎，但在企业中仍然存在着数百万个基于虚拟机的应用程序。一种新的技术浪潮并不总是会淘汰其前身。

也许几十年后，每个企业的工作负载都会被重构为[容器化](https://thenewstack.io/containers/)微服务，但有些工作负载可能永远不会被重构，例如它们的代码过于复杂或太旧。

因此，我们面临一个非常现实的问题：在企业中如何让虚拟化和容器共存？

我们有几个选择：

* **保持完全分离**：大多数企业目前运行独立的虚拟机和容器基础设施。当然，这是低效且有风险的：它需要不同的硬件、多个团队、一套策略、访问控制、网络和存储配置，以及许多其他内容。
* **将容器引入虚拟化基础设施**：您可以在虚拟化基础设施中运行容器。但这是一个深层嵌套的环境，意味着效率低且复杂。很难进行扩展，通常需要专有解决方案才能实现。
* **将虚拟机引入 Kubernetes 基础设施**：如果 Kubernetes 是您基础设施的未来，这是一种更可持续的方法。Kubernetes 已通过 Kubernetes API 展现出提供高度可靠、可扩展和可扩展的平台的能力，并具有声明性管理的优势。

实际上，有一种解决方案可以实现这第三种选择：KubeVirt。

## KubeVirt：在 Kubernetes 集群中使虚拟机成为一级公民

[KubeVirt](https://kubevirt.io/) 是一个 Cloud Native Computing Foundation（CNCF） 的孵化项目，巧合的是，它在上周刚刚[发布了 1.0 版本](https://kubevirt.io/2023/KubeVirt-v1-has-landed.html)。

利用基于内核的虚拟机（KVM）超级监视程序本身就是可以容器化的 Linux 进程这一事实， KubeVirt 使基于 KVM 的虚拟机工作负载可以在 Kubernetes 中以 Pods 的形式进行管理。

这意味着您可以将虚拟机引入现代的基于Kubernetes的云原生环境，而无需立即重构您的应用程序。

### KubeVirt 的实现原理

KubeVirt 将 K8s 风格的 API 和清单引入其中，通过简单的资源驱动虚拟机的配置和管理，并提供标准的虚拟机操作（虚拟机的生命周期、电源操作、克隆、快照等）。

![](https://cdn.thenewstack.io/media/2023/07/4543bbae-image1a-e1689610922174.png)
*来源：https://kubevirt.io/user-guide/architecture*

需要虚拟化服务的用户与虚拟化 API 进行交互（见下图），该 API 再与 Kubernetes 集群进行通信以调度所请求的虚拟机实例（VMI）。

调度、网络和存储都由 Kubernetes 委派处理，而 KubeVirt 提供虚拟化功能。

KubeVirt 提供以下三个功能以提供虚拟机管理能力：

* Kubernetes API 中添加的新自定义资源定义（CRD）
* 与这些新类型相关联的用于整个集群逻辑的额外控制器
* 与新类型相关联的节点特定逻辑的额外守护程序

![](https://cdn.thenewstack.io/media/2023/07/9dfc97c9-image2a-e1689610963544.png)

由于虚拟机作为 Pod 在 Kubernetes 中运行，它们享有以下优点：

* 与 Kubernetes 资源相同的声明性模型。
* 与 Kubernetes 网络插件相同，以实现虚拟机与集群中的其他 Pod 或服务之间的通信。
* 存储选项，包括持久卷，为虚拟机提供数据持久性。
* Kubernetes 内置的高可用性和调度功能：虚拟机可以在多个节点上调度以实现负载均衡、亲和性和反亲和性规则等。

与 Kubernetes 生态系统集成：KubeVirt 与其他 Kubernetes 生态系统工具和功能无缝集成，例如 Kubernetes 基于角色的访问控制（RBAC）用于访问控制、监控和日志记录解决方案，以及服务网格技术等。

## KubeVirt 的现实应用：有何障碍？

KubeVirt 听起来很令人兴奋，不是吗？您可以将虚拟机像处理其他容器一样。

然而，实现这一目标并不是易事。

### 安装KubeVirt：手动配置

KubeVirt 是开源的，所以您今天就可以下载和安装它。

但是手动安装过程可能很耗时，并且您可能会遇到与所有必要组件集成和兼容性的挑战。

首先，您需要运行 Kubernetes 集群，然后在该集群上执行以下操作：

* 安装 KubeVirt operator （用于管理KubeVirt资源）
* 部署 KubeVirt 自定义资源定义（CRDs）
* 部署 KubeVir t组件（Pods、服务和配置）

您需要为每个集群都这样做。虽然基本安装允许您创建简单的虚拟机，但更高级的功能，例如实时迁移、克隆或快照，需要您部署和配置额外的组件（快照控制器、容器化数据导入器等）。

### 裸金属的挑战

我们上面提到过“嵌套”基础设施的低效性。虽然在其他虚拟机或公共云实例上嵌套运行 KubeVirt 在技术上是可能的，但它需要软件仿真，这会对您的工作负载产生性能影响。

相反，将 KubeVirt 运行在裸金属 Kubernetes 上是很有意义的，但传统上并不容易。在裸金属服务器上搭建环境、部署操作系统并对其进行管理、在上面部署 Kubernetes ——这个过程可能很复杂，尤其在大规模部署时更是如此。

### 运维：具有挑战性的用户体验

当涉及到第二天的运维时，KubeVirt 需要用户进行大量的手动操作。让我们来看几个例子：

首先，KubeVirt 默认不提供用户界面：全部都是命令行界面（CLI）或 API 。这对于习惯于操作 Kubernetes 和容器的集群管理员来说可能完全没问题，但对于习惯于从图形用户界面（GUI）进行操作的虚拟化管理员来说可能会带来挑战。

甚至像启动或停止虚拟机这样简单的操作都需要修改虚拟机清单或使用 `virtctl` 命令行。

![](https://cdn.thenewstack.io/media/2023/07/79cb2946-image3a-e1689611005457.png)

另一个例子是实时迁移：要将虚拟机实时迁移到另一节点，您必须创建一个 `VirtualMachineInstanceMigration` 资源来告诉 KubeVirt 要做什么。

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstanceMigration
metadata:
  name: live-migrate-webapp01
  namespace: default
spec:
  vmiName: webapp01
```

如果您在大规模部署中每天执行许多此类操作，并在多个集群之间执行，那么这将需要相当大的工作量。编写脚本或自动化可以解决问题，但这本身增加了学习曲线并增加了设置成本。

## 介绍 Palette 虚拟机编排器

我们看到了一个机会，利用 KubeVirt 提供的所有优势，解决所有这些问题，并为在 Kubernetes 上运行虚拟机提供真正的企业级解决方案。

今天，我们正式宣布：让我们来见识一下虚拟机编排器（VMO），它是我们 Palette Kubernetes 管理平台 4.0 版本中的新功能。

VMO是一个免费功能，利用KubeVirt使虚拟机（VMs）和Kubernetes容器可以轻松地从单一统一平台进行管理。

以下是VMO的亮点。

简化的设置过程
如果您对Palette还不熟悉，一个使它与众不同的事物是集群配置文件的概念。这是预先配置和可重复使用的蓝图，记录了集群堆栈的每一层，从基础操作系统到上层的应用程序，您可以通过几次点击部署到集群中。

我们为VMO构建了一个附加包，其中包含我们之前提到的所有KubeVirt组件，以及更多内容，包括：

快照控制器，为虚拟机和相关卷提供快照功能
容器化数据导入器（CDI），用于将持久卷声明（PVC）作为虚拟机的磁盘（作为数据卷）使用的功能。
Multus，提供虚拟局域网（VLAN）网络访问虚拟机
开箱即用的Grafana仪表板，为您的虚拟机提供监控


Palette不仅可以为您构建集群，还可以将VM管理功能预配置到该集群中，得益于Cluster Profile。这样做将大大减少手动配置的工作量。

此外，Palette的多集群分散式架构使得将VMO功能轻松地交付给多个集群，而无需手动启用。

简化的裸金属体验
我们之前谈到了在裸金属上运行KubeVirt的重要性，以及在为Kubernetes配置和管理裸金属服务器时的难度。

幸运的是，Palette旨在简化在各种环境中部署Kubernetes集群的方式，其中包括裸金属。

有许多方式可以为裸金属服务器提供编排服务，其中一个最受欢迎的方式是Canonical MAAS，它允许您像管理私有云一样管理物理机器的配置和生命周期。

我们非常喜欢MAAS，因此我们在VMO包中包含了Canonical MAAS和我们的MAAS提供程序用于Cluster API，以自动化部署OS和Kubernetes在裸金属硬件上。这样，新的Kubernetes裸金属集群的部署将变得与云端一样简单。

当然，如果您不想使用MAAS，可以使用您自己的裸金属提供商。

强大的管理功能和直观的界面
一旦一切就绪，Palette的始终可用的声明性管理将保持整个集群的状态与设计一致，并通过自动化协调循环来消除配置漂移。这也适用于虚拟机工作负载。

虽然DIY KubeVirt在虚拟化世界中可能会让您对

一些功能感到不满意，但Palette提供了许多开箱即用的功能。

其中包括虚拟机实时迁移、动态资源再平衡和维护模式（用于修复或替换主机机器）、以及从用户界面（UI）声明新的VLAN。您还可以使用Prometheus和Grafana对集群、节点和虚拟机进行开箱即用的监控。

虽然DIY KubeVirt中，平台运营商（也就是您）必须选择、安装和配置一个开源解决方案来获得用户界面，但Palette已经具备以下界面：



虚拟机的未来
正如您所了解的，我们对Palette 4.0和虚拟机编排器功能的发布感到非常兴奋。

我们构建在KubeVirt开源基础之上，并为企业提供了更简单、更强大的体验。

结果呢？已经致力于在应用现代化旅程中采用Kubernetes并已投入Kubernetes技能和工具的组织将从一个单一平台中管理容器和虚拟机中受益。

这不仅仅是一种暂时的过渡阶段，用于重构的应用程序，而且还适用于混合部署（共享虚拟机和容器的应用程序）以及将永远托管在虚拟机中的工作负载。即使虚拟化已经存在近25年，虚拟机当然还没有完结。