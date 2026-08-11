您的团队已使用 [KubeVirt](https://kubevirt.io/) 将虚拟机迁移至 Kubernetes。工作负载运行良好，团队信心倍增。然而，有人提出了一个问题：我们能将虚拟机实时热迁移到另一个集群吗？

灾难恢复、集群升级、容量再平衡——这些需求接踵而至。KubeVirt 的答案看似简单：v1.6 版本中引入的分布式热迁移功能应该可以解决这个问题。

但您的网络团队给出的答案则复杂得多。虚拟机在目标集群上通常需要保留其原始 IP 和 MAC 地址。这意味着需要在站点间扩展二层域。在传统基础设施中，这意味着配置新的 VLAN、交换机配置，甚至可能涉及更换硬件。需要变更窗口。需要申请工单。需要数周时间。

> “在传统基础设施中，这意味着配置新的 VLAN、交换机配置，甚至可能涉及更换硬件。需要变更窗口。需要申请工单。需要数周时间。”

迁移技术本身并不是问题。阻碍迁移的往往是网络。

![图片展示了四个目标：扩展二层网络、网络间路由、减少广播/未知单播/组播 (BUM) 流量，以及无缝工作负载移动性。](https://cdn.thenewstack.io/media/2026/08/415e061e-image-1024x572.png)

## 为什么网络是难点

跨集群热迁移有两个标准 Kubernetes 网络无法解决的网络需求。

首先是 **扩展二层域 (Stretched L2 domain)**。虚拟机必须以相同的 MAC 和 IP 地址出现在目标集群的同一广播域中。否则，每次迁移都意味着 IP 重新分配、DNS 更新和连接中断。有状态应用（如使用同步复制的 PostgreSQL 集群，或具有持久 TCP 会话的消息队列）在没有人工干预的情况下无法承受 IP 变更。

其次是 **专用迁移通道**。迁移需要实时传输数 GB 的内存状态。如果通过承载应用流量的同一网络进行传输，会造成拥塞、不可预测的延迟，且无法独立监控不同流量类型。

![展示 VXLAN 网络覆盖的图表。](https://cdn.thenewstack.io/media/2026/08/6fa0c32a-image-1024x572.png)

在传统的虚拟化平台中，这些问题通过专用的 [迁移 VLAN 和专有虚拟](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) 交换机构造来解决：它们通常与硬件耦合、厂商绑定，且往往按 CPU 插槽收费。开源方案需要作为覆盖网络 (Overlay) 运行，能够以声明式方式管理，且无需干预物理网络。

EVPN/VXLAN 正好提供了这一功能。[OpenPERouter](https://github.com/openperouter/openperouter) 将其转化为 Kubernetes 原生资源。

## 作为 Kubernetes CRD 的 EVPN

OpenPERouter 通过三个自定义资源定义 (CRD) 管理 EVPN 配置。`Underlay` CR 在每个 Kubernetes 集群与其机架顶部交换机之间建立 BGP 对等关系。`L2VNI` CR 创建一个二层覆盖网络，由 VXLAN 段实现，并由 VNI 编号识别且作用于 VRF。最后，`L3VNI` CR 实现了不同子网间的 IP 路由，并将您的集群连接到外部网络。

应用网络在 VRF “red” 中使用 VNI 110：

```

apiVersion: openpe.openperouter.github.io/v1alpha1
kind: L2VNI
metadata:
  name: application-net
  namespace: openperouter-system
spec:
  vni: 110
  vrf: red
  hostmaster:
    type: linux-bridge
    linuxBridge:
      autoCreate: true
  l2gatewayips: ["192.170.10.1/24"]

```

两个集群获取相同的 `L2VNI` 资源，且任一集群上的虚拟机均可在 192.170.1.0/24 子网共享二层邻接关系。集群 A 上 IP 为 192.170.1.3 的虚拟机可以访问集群 B 上 IP 为 192.170.1.30 的虚拟机，就像它们在同一台交换机上一样。

迁移网络是第二个 `L2VNI`。它使用完全相同的模式，但 VNI 不同：

```

apiVersion: openpe.openperouter.github.io/v1alpha1
kind: L2VNI
metadata:
  name: migration-net
  namespace: openperouter-system
spec:
  vni: 666
  vrf: rouge
  hostmaster:
    type: linux-bridge
    linuxBridge:
      autoCreate: true
  l2gatewayips: ["192.170.10.1/24"]

```

迁移网络只需要在 L2VNI CR 中设置唯一的 VNI 和 VRF（在本例中为 `666` 和 `rouge`），迁移流量便可与应用网络隔离。此覆盖网络运行在站点间现有的 IP 连接之上。VXLAN 隧道端点甚至不需要在同一个网络段上。只要站点间存在 IP 可达性（可以跨越任意跳数路由），覆盖网络即可收敛。

> “两个 CRD 定义了曾经需要网络团队介入和变更窗口才能完成的工作。”

## 操作迁移

在网络架构就绪后，这是 [运维人员在第二天](https://thenewstack.io/kubernetes-1-35-features-that-change-day-2-operations/) 当虚拟机需要移动时实际所做的操作。

**跨集群 IP [管理](https://thenewstack.io/how-amazon-eks-auto-mode-simplifies-kubernetes-cluster-management-part-1/)** 需要一种无需中心化协调即可防止冲突的 IPAM 策略。示例使用了 [Whereabouts](https://github.com/k8snetworkplumbingwg/whereabouts) 并辅以排除范围，这意味着每个集群的 Network Attachment Definition 覆盖相同的 192.170.10.0/24 子网，但排除了另一个集群的地址范围。集群 A 从低地址范围分配，集群 B 从高地址范围分配。但 Whereabouts 只是设计选择而非强制要求；任何能够跨集群划分范围的 IPAM 提供程序均可使用。

**迁移本身**涉及三个资源：

目标虚拟机必须由用户在集群 B 上配置 `runStrategy: WaitAsReceiver`——使用相同的 MAC 地址、相同的 IP 配置，保持空闲状态直到接收到传入的迁移。

随后，集群 B 上的 `VirtualMachineInstanceMigration` 接收器声明就绪：

```

apiVersion: kubevirt.io/v1
kind: VirtualMachineInstanceMigration
metadata:
  name: vmim-target
spec:
  receive:
    migrationID: cross-cluster-demo
  vmiName: vm-1

```

集群 A 上的匹配发送器指向接收器的迁移 IP（从接收器的 `.status.synchronizationAddresses` 获取）并启动传输。

```

apiVersion: kubevirt.io/v1
kind: VirtualMachineInstanceMigration
metadata:
  name: migration-source
spec:
  sendTo:
    connectURL: "&lt;receiver VMI migration .status.synchronizationAddresses[0]>:9185"
    migrationID: cross-cluster-demo
  vmiName: vm-1
EOF

```

在底层，迁移流量流经 VNI 666，与 VNI 110 隔离。虚拟机在保持身份完整的情况下被复制到集群 B。EVPN 更新跨架构的 MAC/IP 通告——发送至该虚拟机的流量开始到达新集群。无需 DNS 变更，无需 IP 重新分配，无需连接重置。

## 责任归属

这里的真正转变是运营层面的，而不仅仅是技术层面的。BGP EVPN 的配置（即覆盖网络、VRF 和 VNI）从网络团队的领域转移到了 Kubernetes 管理员手中。

> “运营模式从‘请求物理网络变更并等待’转变为‘应用一个 CR，覆盖网络即可收敛’。”

网络团队仍负责底层设施：路由器端点和链路的 IP 寻址、物理连接以及站点间的路由。这一点没有改变。但一旦底层设施就绪，其上的一切——扩展二层域、专用迁移网络、VRF 隔离——都由管理集群的同一平台团队通过 Kubernetes CRD 进行声明。无需向网络团队提交工单以添加 VLAN。无需变更窗口来将广播域扩展到新站点。

下表重点展示了与传统虚拟化技术栈相比，运营职责的转变：

| | **网络管理员角色** | **Kubernetes 管理员角色** |
| --- | --- | --- |
| **传统虚拟化** | 为每次虚拟机移动管理物理交换机、VLAN 和硬件配置。 | 依赖网络团队提交工单和手动变更窗口。 |
| **KubeVirt + OpenPERouter** | 设置基础 IP 连接、路由器端点和链路。 | 通过 K8s CRD 声明式管理覆盖网络、BGP/EVPN 配置和虚拟机移动性。 |

运营模式从“请求物理网络变更并等待”转变为“应用一个 CR，覆盖网络即可收敛”。平台团队以管理 Kubernetes 中其他一切事物的方式管理虚拟机移动性：声明式、版本控制、可审计。

## 开始使用

网络不应成为虚拟机无法跨集群移动的原因。通过 Kubernetes CRD 管理的 EVPN 覆盖网络，为多集群 KubeVirt 部署提供了传统平台所具备的虚拟机移动性，且无需依赖物理网络或绑定特定的许可模式。

有关分步指南，请参阅 [集群间的扩展二层网络](https://kubevirt.io/2025/Stretched-layer2-network-between-clusters.html) 和 [用于跨集群热迁移的专用迁移网络](https://kubevirt.io/2025/Dedicated-migration-network-for-cross-cluster-live-migration.html)。现成的配置文件可在 [OpenPERouter 示例](https://github.com/openperouter/openperouter/tree/main/examples/evpn/multi-cluster/) 中找到。

**注意：** KubeVirt 是 CNCF 孵化项目，于 2019 年 9 月被接纳，并于 2022 年 4 月进入孵化成熟阶段。文中提到的分布式热迁移功能自 v1.6（2025 年 7 月）版本起可用，并在 v1.8（2026 年 3 月）版本中保持稳定。`}
} Leveraging extra-cluster live migration, KubeVirt, and EVPN. The article highlights that traditional L2 network constraints hinder VM mobility, requiring tedious manual network changes. By utilizing OpenPERouter to implement EVPN/VXLAN via Kubernetes CRDs, platform teams gain the ability to manage stretched L2 domains and dedicated migration paths declaratively. This shift enables seamless cross-cluster VM migrations without needing external network team involvement, enhancing operational agility. 
,alternative_title1: Breaking Physical Limits: How to Enable KubeVirt VM Cross-Cluster Live Migration with EVPN,alternative_title2: The Cross-Cluster Migration Challenge: Why KubeVirt Needs EVPN Support,alternative_title3: From Manual Tickets to Automated Delivery: How EVPN Empowers KubeVirt VM Mobility,translated_content: ## 为什么您的 KubeVirt 虚拟机无法跨集群迁移——以及 EVPN 如何解决它

您的团队已使用 [KubeVirt](https://kubevirt.io/) 将虚拟机迁移至 Kubernetes。工作负载运行良好，团队信心倍增。然而，有人提出了一个问题：我们能将虚拟机实时热迁移到另一个集群吗？

灾难恢复、集群升级、容量再平衡——这些需求接踵而至。KubeVirt 的答案看似简单：v1.6 版本中引入的去中心化热迁移功能应该可以解决这个问题。

但您的网络团队给出的答案则复杂得多。虚拟机在目标集群上通常需要保留其原始 IP 和 MAC 地址。这意味着需要在站点间扩展二层域。在传统基础设施中，这意味着配置新的 VLAN、交换机配置，甚至可能涉及更换硬件。需要变更窗口。需要申请工单。需要数周时间。

> “在传统基础设施中，这意味着配置新的 VLAN、交换机配置，甚至可能涉及更换硬件。需要变更窗口。需要申请工单。需要数周时间。”

迁移技术本身并不是问题。阻碍迁移的往往是网络。

![图片展示了四个目标：扩展二层网络、网络间路由、减少广播/未知单播/组播 (BUM) 流量，以及无缝工作负载移动性。](https://cdn.thenewstack.io/media/2026/08/415e061e-image-1024x572.png)

## 为什么网络是难点

跨集群热迁移有两个标准 Kubernetes 网络无法解决的网络需求。

首先是 **扩展二层域 (Stretched L2 domain)**。虚拟机必须以相同的 MAC 和 IP 地址出现在目标集群的同一广播域中。否则，每次迁移都意味着 IP 重新分配、DNS 更新和连接中断。有状态应用（如使用同步复制的 PostgreSQL 集群，或具有持久 TCP 会话的消息队列）在没有人工干预的情况下无法承受 IP 变更。

其次是 **专用迁移通道**。迁移需要实时传输数 GB 的内存状态。如果通过承载应用流量的同一网络进行传输，会造成拥塞、不可预测的延迟，且无法独立监控不同流量类型。

![展示 VXLAN 网络覆盖的图表。](https://cdn.thenewstack.io/media/2026/08/6fa0c32a-image-1024x572.png)

在传统的虚拟化平台中，这些问题通过专用的 [迁移 VLAN 和专有虚拟](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) 交换机构造来解决：它们通常与硬件耦合、厂商绑定，且往往按 CPU 插槽收费。开源方案需要作为覆盖网络 (Overlay) 运行，能够以声明式方式管理，且无需干预物理网络。

EVPN/VXLAN 正好提供了这一功能。[OpenPERouter](https://github.com/openperouter/openperouter) 将其转化为 Kubernetes 原生资源。

## 作为 Kubernetes CRD 的 EVPN

OpenPERouter 通过三个自定义资源定义 (CRD) 管理 EVPN 配置。`Underlay` CR 在每个 Kubernetes 集群与其机架顶部交换机之间建立 BGP 对等关系。`L2VNI` CR 创建一个二层覆盖网络，由 VXLAN 段实现，并由 VNI 编号识别且作用于 VRF。最后，`L3VNI` CR 实现了不同子网间的 IP 路由，并将您的集群连接到外部网络。

应用网络在 VRF “red” 中使用 VNI 110：

```
apiVersion: openpe.openperouter.github.io/v1alpha1
kind: L2VNI
metadata:
  name: application-net
  namespace: openperouter-system
spec:
  vni: 110
  vrf: red
  hostmaster:
    type: linux-bridge
    linuxBridge:
      autoCreate: true
  l2gatewayips: ["192.170.10.1/24"]
```

两个集群获取相同的 `L2VNI` 资源，且任一集群上的虚拟机均可在 192.170.1.0/24 子网共享二层邻接关系。集群 A 上 IP 为 192.170.1.3 的虚拟机可以访问集群 B 上 IP 为 192.170.1.30 的虚拟机，就像它们在同一台交换机上一样。

迁移网络是第二个 `L2VNI`。它使用完全相同的模式，但 VNI 不同：

```
apiVersion: openpe.openperouter.github.io/v1alpha1
kind: L2VNI
metadata:
  name: migration-net
  namespace: openperouter-system
spec:
  vni: 666
  vrf: rouge
  hostmaster:
    type: linux-bridge
    linuxBridge:
      autoCreate: true
  l2gatewayips: ["192.170.10.1/24"]
```

迁移网络只需要在 L2VNI CR 中设置唯一的 VNI 和 VRF（在本例中为 `666` 和 `rouge`），迁移流量便可与应用网络隔离。此覆盖网络运行在站点间现有的 IP 连接之上。VXLAN 隧道端点甚至不需要在同一个网络段上。只要站点间存在 IP 可达性（可以跨越任意跳数路由），覆盖网络即可收敛。

> “两个 CRD 定义了曾经需要网络团队介入和变更窗口才能完成的工作。”

## 操作迁移

在网络架构就绪后，这是 [运维人员在第二天](https://thenewstack.io/kubernetes-1-35-features-that-change-day-2-operations/) 当虚拟机需要移动时实际所做的操作。

**跨集群 IP [管理](https://thenewstack.io/how-amazon-eks-auto-mode-simplifies-kubernetes-cluster-management-part-1/)** 需要一种无需中心化协调即可防止冲突的 IPAM 策略。示例使用了 [Whereabouts](https://github.com/k8snetworkplumbingwg/whereabouts) 并辅以排除范围，这意味着每个集群的 Network Attachment Definition 覆盖相同的 192.170.10.0/24 子网，但排除了另一个集群的地址范围。集群 A 从低地址范围分配，集群 B 从高地址范围分配。但 Whereabouts 只是设计选择而非强制要求；任何能够跨集群划分范围的 IPAM 提供程序均可使用。

**迁移本身**涉及三个资源：

目标虚拟机必须由用户在集群 B 上配置 `runStrategy: WaitAsReceiver`——使用相同的 MAC 地址、相同的 IP 配置，保持空闲状态直到接收到传入的迁移。

随后，集群 B 上的 `VirtualMachineInstanceMigration` 接收器声明就绪：

```
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstanceMigration
metadata:
  name: vmim-target
spec:
  receive:
    migrationID: cross-cluster-demo
  vmiName: vm-1
```

集群 A 上的匹配发送器指向接收器的迁移 IP（从接收器的 `.status.synchronizationAddresses` 获取）并启动传输。

```
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstanceMigration
metadata:
  name: migration-source
spec:
  sendTo:
    connectURL: "<receiver VMI migration .status.synchronizationAddresses[0]>:9185"
    migrationID: cross-cluster-demo
  vmiName: vm-1
EOF
```

在底层，迁移流量流经 VNI 666，与 VNI 110 隔离。虚拟机在保持身份完整的情况下被复制到集群 B。EVPN 更新跨架构的 MAC/IP 通告——发送至该虚拟机的流量开始到达新集群。无需 DNS 变更，无需 IP 重新分配，无需连接重置。

## 责任归属

这里的真正转变是运营层面的，而不仅仅是技术层面的。BGP EVPN 的配置（即覆盖网络、VRF 和 VNI）从网络团队的领域转移到了 Kubernetes 管理员手中。

> “运营模式从‘请求物理网络变更并等待’转变为‘应用一个 CR，覆盖网络即可收敛’。”

网络团队仍负责底层设施：路由器端点和链路的 IP 寻址、物理连接以及站点间的路由。这一点没有改变。但一旦底层设施就绪，其上的一切——扩展二层域、专用迁移网络、VRF 隔离——都由管理集群的同一平台团队通过 Kubernetes CRD 进行声明。无需向网络团队提交工单以添加 VLAN。无需变更窗口来将广播域扩展到新站点。

下表重点展示了与传统虚拟化技术栈相比，运营职责的转变：

| | **网络管理员角色** | **Kubernetes 管理员角色** |
| --- | --- | --- |
| **传统虚拟化** | 为每次虚拟机移动管理物理交换机、VLAN 和硬件配置。 | 依赖网络团队提交工单和手动变更窗口。 |
| **KubeVirt + OpenPERouter** | 设置基础 IP 连接、路由器端点和链路。 | 通过 K8s CRD 声明式管理覆盖网络、BGP/EVPN 配置和虚拟机移动性。 |

运营模式从“请求物理网络变更并等待”转变为“应用一个 CR，覆盖网络即可收敛”。平台团队以管理 Kubernetes 中其他一切事物的方式管理虚拟机移动性：声明式、版本控制、可审计。

## 开始使用

网络不应成为虚拟机无法跨集群移动的原因。通过 Kubernetes CRD 管理的 EVPN 覆盖网络，为多集群 KubeVirt 部署提供了传统平台所具备的虚拟机移动性，且无需依赖物理网络或绑定特定的许可模式。

有关分步指南，请参阅 [集群间的扩展二层网络](https://kubevirt.io/2025/Stretched-layer2-network-between-clusters.html) 和 [用于跨集群热迁移的专用迁移网络](https://kubevirt.io/2025/Dedicated-migration-network-for-cross-cluster-live-migration.html)。现成的配置文件可在 [OpenPERouter 示例](https://github.com/openperouter/openperouter/tree/main/examples/evpn/multi-cluster/) 中找到。

**注意：** KubeVirt 是 CNCF 孵化项目，于 2019 年 9 月被接纳，并于 2022 年 4 月进入孵化成熟阶段。文中提到的去中心化热迁移功能自 v1.6（2025 年 7 月）版本起可用，并在 v1.8（2026 年 3 月）版本中保持稳定。
,title: 为什么您的 KubeVirt 虚拟机无法跨集群迁移？EVPN 解决方案详解,summary: 本文分析了 KubeVirt 跨集群热迁移面临的网络障碍，包括二层网络延伸及专用迁移通道需求。文章提出利用 OpenPERouter 将 EVPN 技术引入 Kubernetes，通过声明式 CRD 管理网络，帮助平台团队消除对传统物理网络变更的依赖，实现虚拟机无缝移动。}
