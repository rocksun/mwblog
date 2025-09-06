在之前的[文章](https://thenewstack.io/gpu-orchestration-in-kubernetes-device-plugin-or-gpu-operator/)中，我介绍了设备插件和 GPU Operator，以便将底层加速基础设施暴露给 Kubernetes 工作负载。在本文中，我将介绍 [Kubernetes](https://thenewstack.io/kubernetes/) 的一项新兴特性，称为[动态资源分配](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) (DRA)，它使 GPU 编排更加高效。

传统的 Kubernetes 资源管理是围绕简单的可计数资源（如 CPU 和内存）设计的。这种模型在通用计算方面表现良好，但在 GPU 和专用 AI 加速器等专用硬件方面却举步维艰。

Kubernetes 1.8 中引入的设备插件框架试图弥补这一差距，但受到基本架构限制。设备插件只能报告可用设备的数量，而没有关于其特定属性或功能的任何信息。每个设备都完全分配给单个容器，无法共享或进行部分分配。

## 设备插件架构的局限性

Kubernetes 中的设备插件框架存在若干架构限制，这些限制阻碍了高效的硬件利用率和管理。其基于整数的资源模型将设备视为可互换的计数，无法捕获 GPU 型号、内存大小或性能属性的差异。

这迫使运营商依赖[节点标签和 nodeSelectors](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/)，从而导致脆弱的基础设施耦合和运营复杂性。该框架还禁止设备共享，这意味着即使单个容器仅使用其容量的一小部分，也可能垄断高端 GPU，从而导致普遍的利用率不足。

它进一步缺乏参数化，从而阻止工作负载使用 [Multi-Instance GPU](https://www.nvidia.com/en-in/technologies/multi-instance-gpu/) (MIG) 配置文件或功率限制等设置来动态配置设备，从而使高级配置成为供应商特定的且不可移植的。

调度程序盲目运行，不知道设备拓扑或集群范围的资源，从而导致效率低下的放置决策，从而降低了分布式工作负载的性能。健康状况监控非常基本，通常会让 Pod 卡在发生故障的设备上，除非外部控制器进行干预。最后，设备插件通常以具有广泛主机访问权限的特权 [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) 运行，从而造成严重的安全风险。

总而言之，这些缺陷暴露了该框架的简单设计与现代加速器、存储设备和网络接口的复杂异构性质之间的根本不一致，使其不足以满足下一代 Kubernetes 工作负载的需求。

## 了解 DRA 架构

DRA 架构代表了 Kubernetes 管理专用资源方式的完全重新设计。DRA 的核心是在 `resource.k8s.io` API 组中引入了几个新的 API 对象，这些对象协同工作以实现动态分配。

**ResourceClaim** 对象描述了对特定资源的需求，并通过[通用表达式语言](https://cel.dev/) (CEL) 过滤器表达详细的要求。声明可能请求具有至少 16GB 内存和特定计算能力的 GPU。这些声明可以手动创建以用于共享资源，也可以通过 **ResourceClaimTemplates** 自动为每个 pod 生成。ResourceClaim 的生命周期跟踪整个分配过程，从初始请求到绑定到最终清理。

**DeviceClass** 对象定义了设备类别，并包含平台管理员在安装 DRA 驱动程序时创建的选择标准。这些类使用 CEL 表达式根据设备的属性来过滤设备。用于高性能计算或运行 AI 工作负载的 DeviceClass 可能仅选择具有特定内存配置和计算架构的 GPU。DeviceClass 对象中的结构化参数使调度程序能够了解设备需求，而无需不透明的供应商特定配置。

**ResourceSlice** 对象由 DRA 驱动程序发布，以宣传每个节点上可用的资源。这些切片包含详细的设备属性，包括内存容量、架构版本和供应商特定的功能。调度程序使用此信息将 pod 需求与可用资源进行匹配。与设备插件的静态报告不同，ResourceSlice 会在设备可用性发生变化时提供动态更新。

## 受存储启发的范式转变

为了解决设备插件框架的深层局限性，Kubernetes 引入了动态资源分配。DRA 代表了专用硬件管理方式的根本性范式转变，它借鉴了使用 [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PV) 和 [PersistentVolumeClaims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PVC) 进行动态存储配置的成熟且易于理解的模型。

这种类比为工程师提供了一个强大的思维模型。DRA 中的 DeviceClass 类似于 StorageClass，用于定义可用资源的类型。ResourceClaim 类似于 PVC，表示用户对该资源实例的请求。这种方法将对资源的请求与其底层实现分离，从而提供了极大的灵活性。

下表比较了 DRA 的关键组件及其存储对应组件，并确定了与每个组件关联的主要用户角色。

| 概念 | 动态资源分配 (DRA) | 受影响的 DRA 角色 | 存储原语 | 受影响的存储角色 |
| --- | --- | --- | --- | --- |
| 定义可用资源的“类型”或“类” | DeviceClass | 集群管理员、设备所有者 | StorageClass | 集群管理员、存储专家 |
| 用户对资源实例的请求 | ResourceClaim, ResourceClaimTemplate | 工作负载运营商 | PersistentVolumeClaim (PVC) | 开发人员、工作负载运营商 |
| 表示集群中实际可用的资源 | ResourceSlice | DRA 驱动程序（设备所有者） | PersistentVolume (PV) | 集群管理员、存储专家 |

## DRA 如何改变资源分配工作流程

DRA 的技术工作流程展示了其优于传统方法的优势。当用户创建具有 ResourceClaim 要求的 pod 时，调度程序会立即开始通过 DynamicResources 插件分析这些声明。调度程序查询整个集群中的 ResourceSlice，以识别与 CEL 选择标准匹配的设备。复杂的表达式可以同时评估多个属性，例如同时要求最小内存和特定的架构特征。

一旦确定了合适的设备，调度程序将根据整体集群优化目标选择最佳的节点和设备组合。分配详细信息将直接写入 ResourceClaim 状态，从而无需外部驱动程序参与调度决策。与设备插件相比，这种方法使调度程序能够并行处理多个 pod 的资源分配，从而显着提高了吞吐量。

[![流程图](https://cdn.thenewstack.io/media/2025/08/5857ef9b-dra-arch-833x1024.png)](https://cdn.thenewstack.io/media/2025/08/5857ef9b-dra-arch-833x1024.png)

在 pod 绑定到节点后，kubelet 的 DRA 管理器将接管本地资源管理。它在适当的 DRA 驱动程序插件上调用 NodePrepareResources gRPC 方法。驱动程序准备硬件设备并生成容器设备接口规范，该规范配置容器对资源的访问。当 pod 终止时，kubelet 会调用 NodeUnprepareResources 以进行清理并释放资源以供将来分配。

DRA 驱动程序遵循一种双组件架构，该架构将控制平面和节点级操作分开。控制器组件集中运行并管理 ResourceSlice 的创建和更新。它监视 ResourceClaim 的更改并处理资源生命周期管理。kubelet 插件组件作为 DaemonSet 在每个节点上运行，并实现 gRPC 接口以进行设备准备和清理。与单片设备插件方法相比，这种分离实现了更好的可伸缩性和更清晰的架构边界。

## 当前的局限性和未来的发展轨迹

DRA 目前处于 Beta 状态，并且有多个功能门控制着不同的功能。核心 DynamicResourceAllocation 功能门自 [Kubernetes 1.32](https://thenewstack.io/kubernetes-1-32-aces-api-conformance-testing/) 起可用。其他 Alpha 功能包括用于动态重新配置的可分区设备、用于管理控制的设备污点和容忍度，以及用于回退设备选择的优先级列表。这些功能正在积极开发和测试中，以准备正式发布。

DRA 的完全成熟仍然存在一些技术挑战。在连接之前不可见的网络连接资源需要额外的开发。实现 DRA 驱动程序的复杂性高于传统设备插件，这为供应商带来了学习曲线。ResourceSlice 对象可能会因大量的设备清单而面临扩展挑战。社区正在通过增强的测试和性能优化来积极解决这些局限性。

刚刚发布的 [Kubernetes 1.34](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/) 包括几项重要的增强功能。DRA 扩展资源桥将实现从现有设备插件的无缝迁移。设备绑定条件将提供基于优先级的就绪性检查。可消耗容量功能将支持更复杂的共享模型。原生健康状况监控会将设备状态直接集成到 Kubernetes 资源模型中。

## 过渡到 DRA

组织应开始评估 DRA，以满足其专用工作负载的需求。运行 AI 和机器学习 (ML) 工作负载的平台团队将立即从 GPU 共享和动态分配功能中受益。高性能计算环境可以利用 DRA 来满足复杂的拓扑要求和跨设备依赖性。网络功能虚拟化部署可以使用 DRA 进行复杂的网络资源管理。

从设备插件迁移到 DRA 需要仔细的规划，但可以带来显着的长期利益。组织应建立具有 DRA Beta 功能的测试环境，以获得运营经验。开发团队需要接受有关结构化参数模型和基于 CEL 的设备选择的培训。应评估供应商关系，以确保关键硬件资源的 DRA 驱动程序可用性。

动态资源分配代表了 Kubernetes 中专用硬件管理的未来。该技术解决了多年来限制资源利用率和工作负载灵活性的根本局限性。凭借强大的生态系统支持和明确的正式发布途径，DRA 有望成为在云原生环境中管理 GPU、加速器和其他专用资源的标准方法。现在开始进行采用计划的组织将能够很好地利用这些功能，因为它们会逐渐成熟并达到生产就绪状态。