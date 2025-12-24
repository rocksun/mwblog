*这是 [Janakiram MSV](https://thenewstack.io/author/janakiram/) 撰写、Spectro Cloud 赞助的新电子书 [《在Kubernetes上运行虚拟机：企业迁移的实用路线图》](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) 第三章的摘录。*

*从探讨云原生环境中虚拟机（VM）的架构和生命周期，到组建跨职能迁移团队和选择合适的工具，这本 [现可免费下载](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) 的免费书籍帮助企业领导者自信地驾驭这场世代性变革。*

---

建立生产就绪的 KubeVirt 平台需要在网络、存储和安全方面进行仔细规划。每个领域都建立在 Kubernetes 的基础上，同时增加了 VM 特定的功能和要求。

## 存储架构

KubeVirt 利用 Kubernetes 原生存储概念进行 VM 磁盘管理。VM 使用持久卷声明（PVC）来请求存储，而不是使用传统数据存储。存储特性，例如性能配置文件和访问模式，通过 StorageClass 对象定义，这些对象通过容器存储接口（CSI）驱动程序连接到底层存储系统。

实时迁移需要多个节点可以同时访问的存储。这通常涉及使用 StorageClass 对象，通过网络文件系统（NFS）、CephFS 或分布式存储系统等技术提供 ReadWriteMany (RWX) 卷。对于数据库等高性能工作负载，PVC 可以配置 volumeMode 为 Block，直接为 VM 提供裸块设备，以实现最佳输入/输出（I/O）性能。

当底层 CSI 驱动程序提供这些功能时，KubeVirt 还支持存储操作，例如克隆和快照。这使得创建现有磁盘的 VM 模板或对运行系统进行时间点备份等工作流成为可能。

## 网络配置

VM 默认使用伪装绑定连接到 Kubernetes pod 网络，这提供了到集群网络的网络地址转换 (NAT) 访问。这种方法将 VM 与现有的 Kubernetes 网络和服 务发现机制无缝集成。

更复杂的网络场景需要额外的工具。Multus 作为容器网络接口（CNI）元插件，使 pod 及其包含的 VM 能够同时连接到多个网络。此功能支持将 VM 通过桥接网络连接到特定虚拟局域网（VLAN）或通过单根 I/O 虚拟化（SR-IOV）直通设备提供高性能连接等用例。

CNI 插件的选择对可用的网络功能有显著影响。不同的 CNI 实现提供不同级别的功能，以满足高级网络要求，包括网络分段、流量整形和性能优化。

## 安全框架

KubeVirt 继承了 Kubernetes 的安全模型，并将其扩展到 VM 工作负载。命名空间提供主要的隔离边界，将相关的 VM 和容器分组，同时控制它们对集群资源的访问。这种方法创建了逻辑分离，类似于将 VM 组织到文件夹或资源池中。

基于角色的访问控制（RBAC）定义了 VM 管理的精细权限。RBAC 策略指定哪些用户或服务帐户可以在特定命名空间内创建、删除、修改或访问 VM。这使得在不同团队或项目之间能够细粒度地委派管理职责。

网络策略控制 VM 和其他集群工作负载之间的流量。这些策略提供基本的网络分段功能，尽管它们的有效性完全取决于 CNI 插件的实现。一些 CNI 解决方案提供比其他解决方案更高级的策略执行和监控功能。

Pod 安全标准和准入控制器可以像容器化应用程序一样对 VM 工作负载强制执行安全策略。这包括对特权操作、资源限制和安全上下文的限制，这些限制管理 VM 在集群内的运行方式。

## 集成考量

通过 KubeVirt 进行的 VM 管理继承了 Kubernetes 平台的诸多优势。资源管理使用与容器相同的配额和限制系统。网络策略在 VM 和 pod 之间保持一致。存储管理遵循标准的 Kubernetes 模式，利用持久卷和存储类。

声明式模型意味着 VM 配置可以通过标准 DevOps 实践进行版本控制、审查和部署。团队可以将用于容器化应用程序的相同 GitOps 工作流应用于其 VM 基础设施，从而使不同工作负载类型的操作保持一致。

VM 和容器工作负载在单一平台上的融合为统一的管理方法创造了机会。存储策略可以一致地应用于两种工作负载类型。网络分段策略可以将 VM 和 pod 纳入相同的策略框架。安全控制受益于集中管理和一致的执行机制。

然而，这种集成也需要仔细规划，以确保在更广泛的 Kubernetes 操作模型中充分解决 VM 特定的要求，例如实时迁移、控制台访问以及与旧版应用程序的兼容性。

---

要了解更多信息，请立即下载 [《在Kubernetes上运行虚拟机：企业迁移的实用路线图》](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)！

[!["在Kubernetes上运行虚拟机" 封面图片](https://cdn.thenewstack.io/media/2025/11/87847543-spectro-ebook-hero-image.png)](https://cdn.thenewstack.io/media/2025/11/87847543-spectro-ebook-hero-image.png)