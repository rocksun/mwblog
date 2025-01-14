# 基于K8s和Kubevirt的双站点高可用性故障转移新方法

![基于K8s和Kubevirt的双站点高可用性故障转移新方法的特色图片](https://cdn.thenewstack.io/media/2025/01/b8da5e73-main12-1024x614.png)

双数据中心长期以来一直是高可用性系统的重要组成部分。在工厂、医院园区和其他关键任务场所，常见的做法是在第二个服务器机房或校园内位置复制整个核心IT基础设施，并在灾难发生时将应用程序故障转移到第二个机房。

当然，没有人希望大量的昂贵服务器99.9%的时间处于闲置状态，因此，常见的做法也是将IT基础设施虚拟化，从而在两个位置之间创建一个单一的资源池。当一个位置发生故障时，您只需在幸存位置重新启动来自故障位置的工作负载即可。

在过去的20年中，[VMware](https://tanzu.vmware.com?utm_content=inline+mention)虚拟化简化了这一过程。使用扩展的vSAN或具有同步复制的后端存储阵列，您可以跨两个位置设置基础设施，并使其作为一个整体运行。当由于任何原因发生站点故障时，您实际上只损失了VM容量的50%。

**在云原生世界中跨站点部署**

但世界在不断发展。如今，许多组织正积极尝试[减少对VMware的依赖](https://www.spectrocloud.com/webinars/after-vmware-whats-next)以及[博通](https://broadcom-software.security.com/blogs/division/broadcom-software?utm_content=inline+mention)价格上涨后的影响。与此同时，越来越多的应用程序现在是云原生的或至少是容器化的，这意味着合适的替代方案应该为虚拟机和容器提供高可用性平台。

正如我们过去所探讨的，许多企业[正在寻求使用裸机Kubernetes和KubeVirt来提供其新的平台](https://www.spectrocloud.com/blog/production-ready-kubevirt-architecture-for-vms-on-kubernetes)，用于数据中心中的VM和容器工作负载。

但是，我们上面描述的常见用例呢：校园边缘位置的双机房高可用性故障转移方案？

Kubernetes中的几个核心组件基于多数仲裁模型，这意味着您需要奇数个实例才能确保在任何单一故障发生后保持仲裁，并避免“脑裂”错误情况。

但在可能一次性丢失50%基础设施的双机房情况下，不可能维持仲裁。

**评估选项**

如果我们想在成对的数据中心环境中运行KubeVirt以提供高可用性平台，我们需要[解决一些挑战](https://thenewstack.io/three-common-kubernetes-challenges-and-how-to-solve-them/)。

当然，您可以在一个位置运行一个完整的Kubernetes集群，在第二个位置运行另一个Kubernetes集群，并在两个集群之间实现复制。

这绝对不是一个坏的选择，您今天可以使用[Portworx MetroDR](https://portworx.com/services/business-continuity-disaster-recovery/)来实现，它原生支持KubeVirt，如[此处](https://portworx.com/blog/disaster-recovery-for-red-hat-openshift-virtualization/)所述。我个人测试过，它按预期工作。

当然，还有[Portworx](https://portworx.com/?utm_content=inline+mention)本身的成本，如果您想要持续复制，则还需要支付MetroDR的额外费用。这造成了一定的进入门槛，损害了小型部署的经济可行性，尤其是在校园边缘，您可能只需要一台或几台机架式服务器来处理工作负载。

因此，让我们来看看一些替代技术，它们可以在裸机Kubernetes上提供与双站点高可用性解决方案相同的优势，但以更简单的方式来适应小型部署。

**双节点高可用性：从盒子扩展到机房？**

这并非我们第一次寻求解决仲裁问题并在两部分架构中实现高可用性。

我们的[双节点高可用性功能](https://www.spectrocloud.com/blog/two-node-ha-kubernetes-for-edge-computing-cost-savings)专为加油站、商店和餐馆等远端位置而设计。以前，组织面临着艰难的选择：只向数千个站点中的每一个部署一个盒子（成本低，但没有冗余），或者部署一个三节点集群（更好的可用性，但成本是三倍——大规模部署）。

我们构建了一种方法，可以使用两个节点而不是典型的三个节点来部署具有故障转移功能的集群：一个中间选项，提供硬件冗余和33%的成本节省。

Palette双节点高可用性使用[kine](https://github.com/k3s-io/kine)来解决仅使用两个节点运行etcd时相关的仲裁挑战。当一个节点离线时，状态存储仍然可以正常工作。
此功能的一个副作用是，这样的 Kubernetes 集群可以承受 50% 的基础设施损失，这听起来就像双站点 HA 故障转移用例。

我们能否将这种方法扩展到不仅跨两个盒子，还跨两个房间或临近站点提供 HA？

虽然双节点 HA 功能解决了 etcd 挑战，但用户需要仔细选择 Kubernetes 堆栈中剩余的组件，才能承受 50% 的集群节点损失。幸运的是，对于堆栈中大部分较高级别的负载，这并不是真正的问题。

即使应用程序使用基于仲裁的组件，它也可以通过简单地从存活节点上的部署重新启动丢失的 Pod 来从故障中恢复。对于 DaemonSet 来说，这可能更困难，因为来自 DaemonSet 的丢失 Pod 将保持停机状态，直到丢失的节点重新上线。但在大多数情况下，DaemonSet 不需要多数仲裁即可运行。

因此，对于 Kubernetes 本身的核心框架，我们可以通过利用[Spectro Cloud Palette](https://thenewstack.io/virtual-kubernetes-clusters-with-spectro-cloud-palette/)中的双节点 HA 功能，在每个位置运行一个控制平面节点来支持双站点 HA 架构。

此解决方案还支持向[集群添加工作节点以扩展基础设施](https://thenewstack.io/scaling-to-10000-kubernetes-clusters-without-missing-a-beat/)。例如，您可以在每个位置运行四个额外的 Worker 节点，并使用它们为 KubeVirt 提供足够的容量来用于虚拟机应用程序。

**存储难题**
真正的挑战是存储。如果您使用的是外部存储阵列，则需要：

- 某种跨越两个房间/位置的扩展阵列，或；
- 两个阵列，其中以透明的方式实现复制，以便容器存储接口 (CSI) 能够使用另一个阵列在另一侧附加相同的 PersistentVolumeClaim (PVC)。

例如，Dell 的 PowerMax 和 PowerStore 阵列具有 Metro 功能，可以[透明地挂载来自两个已链接阵列的相同卷](https://dell.github.io/csm-docs/docs/replication/high-availability/powerstore-metro/)，这些阵列在后端保持同步。如果您有这样的阵列，那就太好了！它绝对可以使事情更简单。

但假设这不是一个选项，您需要一种更基于软件的存储方法，该方法仍然适用于此双站点环境。让我们看看有哪些选项。

几种软件定义的 Kubernetes 存储解决方案需要多数仲裁才能运行：

由于我们无法从基于仲裁的产品的 50% 节点丢失中恢复，因此所有这些都无法运行。

**我可以获得见证者吗？**
对于 Portworx，您可以选择在第三个位置部署[见证器虚拟机](https://docs.portworx.com/portworx-enterprise/operations/operate-kubernetes/disaster-recovery/px-metro/witness-node-setup)以提供仲裁参与。

但是，见证者需要一个外部 etcd 集群；您不能将其与 Portworx 中的内部键值数据库 (KVDB) 选项一起使用。这意味着还需要在第三个位置为 Portworx 运行 etcd 集群，这增加了对广域网连接的依赖，以保持存储集群的运行。它还需要稍微修改的安装才能在非 MetroDR 模式下运行。

虽然我们已经测试了带有见证器虚拟机的 Portworx（并且它确实有效），但对于大多数用户来说，在近边缘或较小的校园部署中，需要在第三个位置同时拥有自管理的外部 etcd 集群和见证器虚拟机的额外复杂性可能过高。

**使用 Longhorn 和 Piraeus 保持简单**
并非所有解决方案都需要多数仲裁。[Longhorn](https://longhorn.io/)和[Piraeus](https://piraeus.io/)都可以将卷复制到集群中的其他节点，并在中断导致一半基础设施停机时保持存储集群的存活部分在线。

使用`topology.kubernetes.io/zone`标签，我们可以确保副本保留在另一个房间中，以便所有虚拟机都可以在存活的房间中运行。

Longhorn 的功能基于[2021 年新增功能](https://github.com/longhorn/longhorn/blob/master/enhancements/20210216-volume-live-migration.md)，支持使用块模式 PVC 进行实时迁移。当为 Longhorn 存储类设置`migratable: "true"`参数时，您可以创建适合 KubeVirt 并支持实时迁移的块卷模式的 ReadWriteMany (RWX) 卷。

与 Longhorn 中的常规文件系统模式 PVC 相比，卷的性能也更好，这对于为 KubeVirt 虚拟机提供可接受的性能是急需的。但是，社区中的一些人对 Longhorn 的结果好坏参半，通常建议避免使用 RWX 卷。
因此，我们应该仔细研究最后一个选项：Piraeus。这个项目是[Linstor](https://linbit.com/)的免费开源版本，Linstor 是一种基于分布式复制块设备 (DRBD) 的技术，它既简单又高效。与 Longhorn 类似，它支持 RWX 块卷和 KubeVirt 实时迁移。

**在双站点模型中尝试 Piraeus**

**定义堆栈**

出于好奇，我想看看它是否运行良好，我为 Piraeus 创建了一个 CSI [包](https://www.spectrocloud.com/blog/take-the-pain-out-of-deploying-k8s-helm-charts)，将其放入 Palette 集群配置文件中，并使用它部署了一个四节点 KubeVirt 集群：

该集群具有一个双节点高可用性控制平面和每个房间一个 KubeVirt 工作节点：

**使用区域和污点确保隔离**

控制平面节点非常小，不参与 KubeVirt 集群，这意味着辅助存储副本始终从一个工作节点转移到另一个工作节点。但是，如果每个房间有多个工作节点（或可以参与存储集群的更大的控制平面节点），我们可以配置 Piraeus 以确保第二个副本始终位于另一个房间：

```yaml
apiVersion: piraeus.io/v1
kind: LinstorNodeConnection
metadata:
  name: selector
spec:
  selector:
  - matchLabels:
    - key: topology.kubernetes.io/zone
      op: NotSame
```

我们可以通过 Palette 控制每个节点池的标签和污点，因此我们使用它为每个工作程序池设置唯一的区域标签：

![](https://cdn.thenewstack.io/media/2025/01/6208416c-image5a-300x148.png)
图片 1

![](https://cdn.thenewstack.io/media/2025/01/5773239b-image6a-300x146.png)
图片 2

这样，即使每个房间有多个工作节点，它们也永远不会在同一个房间中存储存储副本的两份副本。

从那里，我们可以部署虚拟机，并确保如果一个服务器机房宕机，另一个机房中的虚拟机将继续运行，而故障服务器机房中崩溃的虚拟机将在幸存的一侧重新启动。

**使用 MediK8s 加速故障转移**

当 Kubernetes 节点突然离线时，在其上运行的 Pod 可能会进入永久的终止状态，因为 Kubernetes 不确定如何处理离线节点上的工作负载（更多信息[此处](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#non-graceful-node-shutdown)）。这对于 StatefulSet 和 KubeVirt VM 来说都是有问题的，因为我们希望这些 VM 尽快在幸存节点上重新启动。

为了加快故障转移时间，我们转向[Medik8s](https://www.medik8s.io/)，您将在上面集群配置文件的屏幕截图中看到它。Medik8s 提供自动化逻辑来监控节点健康状况并将`node.kubernetes.io/out-of-service`污点应用于离线节点，这会导致 Kubernetes 清除该节点上处于终止状态的 Pod。然后，调度程序可以立即将工作负载重新调度到集群中的其他节点。

**将双机房架构付诸实践**

一旦我们在集群中部署了双节点高可用性 Kind 存储、Piraeus 存储、KubeVirt 和 Medik8s 堆栈，我们就可以测试高可用性功能。

关闭双机房集群中一半节点后，幸存一侧的 VM 将在三分钟内重新启动。

与 VMware HA 类似，您的传统虚拟化应用程序工作负载可以在站点中断后几分钟内恢复在线。如果您的应用程序需要接近零停机时间，那么您已经拥有可用的 Kubernetes 基础设施，可以迁移到更适合主动/主动设计的云原生架构。

最终结果？如果您正在寻找工厂、医院或其他独立园区位置的高可用性，那么这是一个可行的云原生替代方案，可以替代 vSphere 和 vSAN 的许可成本。

如果您想了解更多关于这项技术的信息，并在其即将发布的 Palette 版本之前抢先体验，[请随时联系我们](https://www.spectrocloud.com/get-started)。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)