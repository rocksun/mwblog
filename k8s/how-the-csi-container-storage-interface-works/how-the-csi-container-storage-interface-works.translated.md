## 社论

这篇博文由客座作者撰写，[Steven Sklar](https://www.linkedin.com/in/steven-sklar-1ab7103/) 来自 [QuestDB](https://questdb.com/)。它最初出现在他的私人博客 [sklar.rocks](https://sklar.rocks/how-container-storage-interface-works/) 上。我们感谢他对 Kubernetes 生态系统的贡献，并感谢他允许我们重新发布他的文章。Steven，你太棒了！🔥

如果你在 Kubernetes 中使用持久化存储，你可能已经看到有关如何从 [树内迁移到 CSI 卷](https://kubernetes.io/blog/2022/09/26/storage-in-tree-to-csi-migration-status-update-1.25/) 的文章，但还不确定这到底是怎么回事？或者，你可能正在尝试调试一个卡住的 VolumeAttachment，它不会从节点卸载，从而阻碍了你的重要 StatefulSet 滚动更新？清晰地了解容器存储接口（简称 CSI）是什么以及它是如何工作的，将让你在处理 Kubernetes 中的持久化数据时充满信心，让你能够回答这些问题以及更多问题！

## 容器存储接口 (CSI)

容器存储接口是一个 API 规范，使开发人员能够构建自定义驱动程序，用于处理容器化工作负载中的卷的供应、附加和挂载。只要驱动程序正确实现了 CSI API 规范，就可以在任何受支持的容器编排系统（如 Kubernetes）中使用它。这将持久化存储开发工作与核心集群管理工具分离，从而允许在云原生生态系统中快速开发和迭代存储驱动程序。

在 Kubernetes 中，CSI 已用更灵活的存储介质管理方式取代了传统的树内卷。以前，为了利用新的存储类型，必须升级整个集群的 Kubernetes 版本，才能访问新存储类型的新 PersistentVolume API 字段。但现在，借助 [大量的独立 CSI 驱动程序](https://kubernetes-csi.github.io/docs/drivers.html)，只要有相应的驱动程序，你就可以立即向集群添加任何类型的底层存储。

但是，如果现有驱动程序无法提供你需要的功能，而你又想构建一个新的自定义驱动程序，该怎么办？也许你担心从树内迁移到 CSI 卷的后果？或者，你只是想了解更多有关持久化存储如何在 Kubernetes 中工作的信息？那么，你来对地方了！本文将介绍 CSI 是什么，并详细说明它如何在 Kubernetes 中实现。

## 它是贯穿始终的 API

与 Kubernetes 生态系统中的许多事物一样，容器存储接口实际上只是一个 API 规范。在 [container-storage-interface/spec](https://github.com/container-storage-interface/spec) GitHub 仓库中，你可以找到此规范的 2 个不同版本：

- [protobuf 文件](https://github.com/container-storage-interface/spec/blob/master/csi.proto)，它使用 gRPC 术语定义 API 架构
- [markdown 文件](https://github.com/container-storage-interface/spec/blob/master/spec.md)，它描述了整体系统架构，并详细介绍了每个 API 调用

我将在本节中讨论的内容是该 markdown 文件的缩写版本，同时借用仓库本身中的一些漂亮的 ASCII 图！

### 架构

CSI 驱动程序有 2 个组件，节点插件和控制器插件。控制器插件负责高级卷管理；创建、删除、附加、分离、快照和还原物理（或虚拟化）卷。如果你使用的是为云提供商构建的驱动程序（如 AWS 上的 EBS），则驱动程序的控制器插件会与 AWS HTTPS API 通信以执行这些操作。对于其他存储类型，如 NFS、EXSI、ZFS 等，驱动程序会以该 API 接受的任何格式将这些请求发送到底层存储的 API 端点。

**社论：**对于 simplyblock 也是如此。Simplyblock 的 CSI 驱动程序实现了所有必要的，以及以下描述的调用，使其成为 Amazon EBS 的完美替代品。如果你想了解更多，请阅读：[为什么选择 Simplyblock](https://www.simplyblock.io/why-simplyblock)。

另一方面，节点插件负责在卷附加到节点后挂载和供应卷。这些低级操作通常需要特权访问，因此节点插件安装在集群数据平面中的每个节点上，无论卷可以在哪里挂载。

节点插件还负责将磁盘使用情况等指标报告回容器编排系统（规范中称为“CO”）。正如你可能已经猜到的，我将在本文中使用 Kubernetes 作为 CO！但使该规范如此强大的原因在于，只要它遵守 API 指南设定的契约，任何容器编排系统（例如 Nomad）都可以使用它。

规范文档提供了一些可能的部署模式，让我们从最常见的模式开始。
**CO “主”主机**

```
+-------------------------------------------+
|                                           |
| +------------+ +------------+ |
| | CO | gRPC | 控制器 | |
| | +-----------> 插件 | |
| +------------+ +------------+ |
|                                           |
+-------------------------------------------+
```

**CO “节点”主机**

```
+-------------------------------------------+
|                                           |
| +------------+ +------------+ |
| | CO | gRPC | 节点 | |
| | +-----------> 插件 | |
| +------------+ +------------+ |
|                                           |
+-------------------------------------------+
```

由于控制器插件涉及更高级别的卷操作，因此它不需要在集群数据平面的主机上运行。例如，在 AWS 中，控制器会调用 AWS API，如 `ec2:CreateVolume`、`ec2:AttachVolume` 或 `ec2:CreateSnapshot` 来管理 EBS 卷。只要调用者通过 AWS 认证，这些函数就可以在任何地方运行。CO 所需的全部功能就是能够通过 gRPC 向插件发送消息。因此，在此架构中，控制器插件在集群控制平面的“主”主机上运行。

另一方面，节点插件必须在集群数据平面的主机上运行。一旦控制器插件完成其工作，将卷附加到节点供工作负载使用，节点插件（在该节点上运行）将通过将卷挂载到众所周知的路径并选择性地对其进行格式化来接管。此时，CO 可以自由地将该路径用作卷挂载，以便创建新的容器化进程；因此，该挂载上的所有数据都将存储在由控制器插件附加的基础卷上。需要注意的是，容器编排器（而非控制器插件）负责让节点插件知道它应该执行挂载。

### 卷生命周期

该规范提供了一个基本卷操作流程图，也以酷炫的 ASCII 图的形式提供：

```
CreateVolume +------------+ DeleteVolume
+------------->| 已创建 +--------------+
| +---+----^---+ |
| 控制器 | | 控制器 v
+++ 发布 | | 取消发布 +++
|X| 卷 | | 卷 | |
+-+ +---v----+---+ +-+
| 节点就绪 |
+---+----^---+
节点 | | 节点
发布 | | 取消发布
卷 | | 卷
+---v----+---+
| 已发布 |
+------------+
```

挂载卷是一个同步过程：每一步都需要前一步成功运行。例如，如果卷不存在，我们怎么可能将它附加到节点？

在发布（挂载）卷以供工作负载使用时，节点插件首先要求控制器插件已成功在它可以访问的目录中发布卷。在实践中，这通常意味着控制器插件已创建卷并将其附加到节点。现在卷已附加，是节点插件发挥作用的时候了。此时，节点插件可以在其设备路径访问卷，以创建文件系统并将其挂载到目录。一旦挂载，卷即被视为已发布，并且可以供容器化进程使用。这结束了 CSI 挂载工作流。

继续 AWS 示例，当控制器插件发布卷时，它会调用 `ec2:CreateVolume`，然后调用 `ec2:AttachVolume`。这两个 API 调用通过创建 EBS 卷并将其附加到特定实例来分配基础存储。一旦卷附加到 EC2 实例，节点插件就可以自由地对其进行格式化并在其主机的文件系统上创建一个挂载点。

以下是上述卷生命周期图的注释版本，这次在流程图中包含了 AWS 调用。

```
CreateVolume +------------+ DeleteVolume
+------------->| 已创建 +--------------+
| +---+----^---+ |
| 控制器 | | 控制器 v
+++ 发布 | | 取消发布 +++
|X| 卷 | | 卷 | |
+-+ | | +-+
| |
<ec2:CreateVolume> | | <ec2:DeleteVolume>
| |
<ec2:AttachVolume> | | <ec2:DetachVolume>
| |
+---v----+---+
| 节点就绪 |
+---+----^---+
节点 | | 节点
发布 | | 取消发布
卷 | | 卷
+---v----+---+
| 已发布 |
+------------+
```

如果控制器要删除卷，它必须首先等待节点插件安全地卸载卷，以保留数据和系统完整性。否则，如果在卸载卷之前强制将其从节点分离，我们可能会遇到数据损坏等问题。一旦卷被节点插件安全地取消发布（卸载），控制器插件将调用 `ec2:DetachVolume` 以将其从节点分离，最后调用 `ec2:DeleteVolume` 以将其删除，假设您不想在其他地方重复使用该卷。

CSI 强大的原因在于它没有规定如何发布卷。只要您的驱动程序正确实现了 CSI 规范中定义的必需 API 方法，它将与 CSI 兼容，并且可以扩展到在 Kubernetes 和 Nomad 等 CO 中使用。

## 在 Kubernetes 中运行 CSI 驱动程序
**为什么控制器和节点插件本身就是插件？**

容器编排器如何调用它们，它们插入到哪里？

答案取决于你使用的容器编排器。由于我比较熟悉 Kubernetes，我将使用它来演示 CSI 驱动程序如何与 CO 交互。

### 部署模型

由于负责低级卷操作的节点插件必须在数据平面中的每个节点上运行，因此通常使用 DaemonSet 安装它。如果你有异构节点，并且只想将插件部署到其中的一部分，则可以使用节点选择器、亲和性或反亲和性来控制哪些节点接收节点插件 Pod。由于节点插件需要 root 访问权限才能修改主机卷和挂载，因此这些 Pod 将在特权模式下运行。在此模式下，节点插件可以跳出其容器的安全上下文，在执行挂载和配置操作时访问底层节点的文件系统。如果没有这些提升的权限，节点插件只能在其自己的容器化命名空间内操作，而没有它在节点上配置卷所需的系统级访问权限。

控制器插件通常在部署中运行，因为它处理诸如卷和快照之类的更高级别基元，这些基元不需要对群集中每个节点的文件系统进行访问。同样，让我们考虑一下我之前使用的 AWS 示例。如果控制器插件只是进行 AWS API 调用来管理卷和快照，为什么它需要访问节点的根文件系统？大多数控制器插件都是无状态且高可用的，这两者都适用于部署模型。控制器也不需要在特权上下文中运行。

### 事件驱动的 Sidecar 模式

既然我们知道了 CSI 插件如何在典型群集中部署，现在是时候关注 Kubernetes 如何调用每个插件来执行与 CSI 相关的操作了。一系列 Sidecar 容器（已向 Kubernetes API 服务器注册以对群集中的不同事件做出反应）与每个控制器和节点插件一起部署。在某种程度上，这类似于典型的 Kubernetes 控制器模式，其中控制器对群集状态的变化做出反应，并尝试将当前群集状态与所需状态协调一致。

目前有 6 个不同的 Sidecar 与每个 CSI 驱动程序一起工作，以执行特定的与卷相关的操作。每个 Sidecar 向 Kubernetes API 服务器注册自身，并监视特定资源类型的更改。一旦 Sidecar 检测到必须对其执行的操作的更改，它就会使用 CSI 规范中的一个或多个 API 调用调用相关插件来执行所需的。

#### 控制器插件 Sidecar

以下是与控制器插件一起运行的 Sidecar 表：

| Sidecar 名称 | 监视的 K8s 资源 | 调用的 CSI API 端点 |
|---|---|---|
| external-provisioner | PersistentVolumeClaim | CreateVolume、DeleteVolume |
| external-attacher | VolumeAttachment | Controller(Un)PublishVolume |
| external-snapshotter | VolumeSnapshot（内容） | CreateSnapshot、DeleteSnapshot |
| external-resizer | PersistentVolumeClaim | ControllerExpandVolume |

这些 Sidecar 如何协同工作？我们使用有状态集的示例进行演示。在此示例中，我们动态配置 PersistentVolume（PV），而不是将 PersistentVolumeClaim（PVC）映射到现有 PV。我们从使用 VolumeClaimTemplate 创建新的有状态集开始。

```yaml
apiVersion: apps/v1
kind: StatefulSet
spec:
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "my-storage-class"
      resources:
        requests:
          storage: 1Gi
```

创建此有状态集将根据上述模板触发创建新的 PVC。创建 PVC 后，Kubernetes API 将通知 external-provisioner Sidecar 创建了此新资源。然后，external-provisioner 将通过 gRPC 向其相邻的控制器插件发送 CreateVolume 消息。在此，CSI 驱动程序的控制器插件通过处理传入的 gRPC 消息并根据其自定义逻辑创建新卷来接管。在 AWS EBS 驱动程序中，这将是 ec2:CreateVolume 调用。

此时，控制流移动到内置的 PersistentVolume 控制器，该控制器将创建匹配的 PV 并将其绑定到 PVC。这允许调度有状态集的底层 Pod 并将其分配给节点。

在这里，external-attacher Sidecar 接管。它将收到新 PV 的通知，并调用控制器插件的 ControllerPublishVolume 端点，将卷挂载到有状态集的已分配节点。这相当于 AWS 中的 ec2:AttachVolume。

此时，我们有一个 EBS 卷挂载到 EC2 实例，所有这些都基于有状态集、PersistentVolumeClaim 和 AWS EBS CSI 控制器插件的工作。
## 节点插件 Sidecar

与节点插件一起部署的唯一 Sidecar 是 `node-driver-registrar`。此 Sidecar 作为 DaemonSet 的一部分运行，将节点插件注册到节点的 kubelet 中。在注册过程中，节点插件将通知 kubelet 它能够使用其所属的 CSI 驱动程序挂载卷。然后，kubelet 本身将一直等到 Pod 被调度到其对应的节点，此时它负责通过 gRPC 向节点插件发出相关的 CSI 调用（PublishVolume）。

## 通用 Sidecar

在容器和节点插件 Pod 中还运行一个 livenessprobe Sidecar，它监视 CSI 驱动程序的运行状况并向 Kubernetes Liveness Probe 机制报告。

### 通过套接字通信

这些 Sidecar 如何与控制器和节点插件通信？通过共享套接字上的 gRPC！因此，每个 Sidecar 和插件都包含一个指向单个 Unix 套接字的卷挂载。

![CSI 控制器部署](https://static.wixstatic.com/media/a7fbb2_b28b2514decc445496cd94a637a159a9~mv2.png/v1/fill/w_49,h_20,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_auto/a7fbb2_b28b2514decc445496cd94a637a159a9~mv2.png)

此图表突出了 CSI 驱动程序的可插拔特性。要将一个驱动程序替换为另一个驱动程序，您只需将 CSI 驱动程序容器换成另一个容器，并确保它正在侦听 Sidecar 向其发送 gRPC 消息的 Unix 套接字。由于所有驱动程序都宣传自己的不同功能并通过共享 CSI API 契约进行通信，因此它实际上是一个即插即用解决方案。

## 结论

在本文中，我只介绍了容器存储接口规范和在 Kubernetes 中实现的高级概念。虽然希望它能更清楚地了解安装 CSI 驱动程序后会发生什么，但编写一个驱动程序需要对节点的操作系统和驱动程序正在实现的基础存储机制有大量的底层知识。幸运的是，CSI 驱动程序适用于各种云提供商和分布式存储解决方案，因此您很可能可以找到一个已经满足您要求的 CSI 驱动程序。但是，如果您的特定驱动程序行为不当，了解其底层原理总是会有帮助。

如果您对本文感兴趣并想了解更多相关主题，请 [告诉我](https://sklar.rocks/contact/me/)！我总是很乐意回答有关 CSI 驱动程序、Kubernetes 运营商和许多其他 DevOps 相关主题的问题。