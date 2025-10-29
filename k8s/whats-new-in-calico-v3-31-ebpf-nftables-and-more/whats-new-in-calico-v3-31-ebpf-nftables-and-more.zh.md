我们很高兴地宣布发布 Calico v3.31，🎉 它带来了一系列新功能和改进。

快速浏览一下，以下是此版本中的主要更新和改进：

*   [Calico NFTables 数据平面现已正式发布](#calico-nftables)
*   [Calico eBPF 数据平面增强功能](#calico-ebpf)
    *   **简化安装：** 新模板默认使用 `eBPF`，通过 `kubeProxyManagement` 字段自动禁用 `kube-proxy`，并添加 `bpfNetworkBootstrap` 用于自动 API 端点检测。
    *   **可配置的 cgroupv2 路径：** 支持不可变操作系统（例如 Talos）。
*   [Calico Whisker（可观测性堆栈）](#calico-whisker)
    *   Calico v3.31 中改进了用户界面和性能。
    *   新的策略追踪类别：**已强制执行** vs **待处理**。
    *   内存使用量更低，IPv6 修复，以及更高效的流传输。
*   [网络与 QoS](#networking)
    *   跨所有数据平面新增带宽和数据包速率 QoS 控制。
    *   DiffServ (`DSCP`) 支持：通过标记数据包来优先处理流量（例如，VoIP 使用 `EF`）。
    *   引入新的 `QoSPolicy` API 用于声明式流量控制。
*   [封装与路由](#encapsulation)
    *   **技术预览：** Felix 现在直接处理封装路由（`IP-in-IP`，`no-encap`）—— 无需 BIRD！
*   [NAT 控制](#nat-control)
    *   新增 `natOutgoingExclusions` 配置用于精细的 NAT 管理。
    *   在 `IPPoolsOnly` 或 `IPPoolsAndHostIPs` 之间选择以获得灵活性。
*   [BGP 增强功能](#bgp)
    *   支持每个对等体自定义本地 ASN，从而实现 `eBGP` 和高级路由反射器设置。
*   [性能与可用性](#performance)
    *   更快的 IP 地址管理启动。
    *   降低内存使用量并改进选择器索引。
    *   新增 `calicoctl validate` 命令，用于离线和在 CI/CD 管道中验证 Calico 资源。
    *   `AutoHostEndpoint` 现在同时支持 `InterfaceCIDRs` 和 `InterfaceSelectors`。

## Calico NFTables 现已正式发布 (GA)！

VIDEO

我们很高兴地宣布 Calico 的 `NFTables` 数据平面现已正式发布！随着越来越多的 Linux 发行版选择 `NFTables` 作为首选的 netfilter 工具，很明显 `NFTables` 正在成为云原生网络中 `IPTables` 的继任者。

Calico 用户已经通过 Calico v3.29 的技术预览版测试并采用了 `NFTables` 数据平面，在此版本中，我们正式发布 `nftables` 数据平面。与它的前身 `iptables` 相比，`NFTables` 通过简化 Linux 内核中网络变更的编程方式，显著提高了效率和性能，帮助您以更低的开销大规模运行 Kubernetes 网络和安全。

![kube-proxy ipvs vs nftables 延迟]()![kube-proxy ipvs vs nftables 延迟](https://www.tigera.io/app/uploads/2025/10/kube-proxy-ipvs-vs-nftables-latency-blog.png)

## Calico eBPF 数据平面

Calico v3.31 使安装更简单、更自动化。新的安装模板默认使用 `eBPF` 数据平面，通过 `kubeProxyManagement` 设置自动禁用 `kube-proxy`，并使用 `bpfNetworkBootstrap` 自动检测 API 服务器端点。它还支持动态 `cgroupv2` 路径，提高了与 `Talos Linux` 等不可变操作系统的兼容性。如果您想了解分步教程，请观看以下视频：

VIDEO

### 基于 eBPF 的安装资源

VIDEO

借助 Calico v3.31，在基于 kubeadm 的 Kubernetes 集群上使用 Calico Operator 安装 `eBPF` 数据平面变得无缝。它不再需要任何手动步骤。只需使用新的 `eBPF` 安装模板即可。

*   📄 `eBPF` 模板：新的安装模板现在默认使用 `eBPF` 作为数据平面，减少了手动配置。
*   🔑 新的安装选项：现在可以直接使用 `eBPF` 数据平面进行安装，更加简单：

1.  **`kubeProxyManagement`：** 自动禁用 `kube-proxy`，因为 Calico `eBPF` 完全替代了它。
2.  **`bpfNetworkBootstrap`：** 在安装 Calico 之前 `kube-proxy` 存在的环境中，Calico 会学习 `kubernetes` 服务端点并将这些端点自动编程到 `eBPF` 数据平面中，从而无需手动配置。

这简化了安装/迁移过程，并确保 Calico 的 `eBPF` 数据平面以最少的手动步骤进行优化配置。

```
spec:
  calicoNetwork:
    bpfNetworkBootstrap: Enabled
    kubeProxyManagement: Enabled
...
```

### 可配置的 cgroupv2 路径

VIDEO

不可变 Linux 发行版越来越受欢迎，每个发行版都有自己管理系统资源和存储的方式。在 Calico v3.31 中，我们添加了一个新的 Felix 配置字段：

*   **`cgroupV2Path`：** 允许您指定自定义的 cgroup 挂载路径，从而提高 `eBPF` 与 `Talos Linux` 等不可变操作系统的兼容性。

这确保了 Calico 的 `eBPF` 数据平面在各种现代操作系统环境中平稳运行，使采用更容易、更可靠。

```
apiVersion: crd.projectcalico.org/v1
kind: FelixConfiguration
metadata:
 name: default
spec:
 cgroupV2Path: "/sys/fs/cgroup"
```

## Calico Whisker（Calico 可观测性堆栈）

VIDEO

Whisker 在我们的社区中迅速受到喜爱，用户喜欢其直观的用户界面。在 Calico v3.31 中，我们更进一步，改进了策略追踪的用户界面，降低了内存使用，修复了 IPv6 绑定问题，并实现了 Goldmane 中更高效的流传输。现在，针对每个流评估的策略明确分为两类：

*   **已强制执行**：当前处于活动状态并影响流量流的策略。
*   **待处理**：如果一个流匹配一个暂存的网络策略，那么待处理行将由如果该暂存网络策略被强制执行时，可以应用于该流的所有策略填充。这些策略将会在所有暂存策略被强制执行时，对匹配该流的任何新连接强制执行。

## 网络

### Calico 带宽管理服务质量 (QoS)

VIDEO

Linux 多个数据平面（`eBPF`、`IPTables` 和 `NFTables`）现在提供新的带宽和数据包速率 QoS 突发和峰值速率控制。

这些改进使得操作员在 OpenStack 和 Kubernetes 环境中管理流量 QoS 时能够进行更精细的控制和更快的响应。

```
annotations:
   # Bandwidth peakrate and minburst
   qos.projectcalico.org/ingressPeakrate: "1000000"   # in bits per second
   qos.projectcalico.org/egressPeakrate: "500000"     # in bits per second
   qos.projectcalico.org/ingressMinburst: "1500"      # defaults to MTU if lower
   qos.projectcalico.org/egressMinburst: "1500"

   # Packet rate limits with burst
   qos.projectcalico.org/ingressPackets: "1000"       # packets per second
   qos.projectcalico.org/egressPackets: "800"         # packets per second
   qos.projectcalico.org/ingressPktBurst: "200"       # burst packets
   qos.projectcalico.org/egressPktBurst: "200"
```

## 流量分类

在 Calico v3.31 中，我们通过对工作负载和 `hostendpoints` 支持差分服务 (`DiffServ`) 来扩展服务质量 (QoS) 功能。

这一增强功能允许您对离开集群的流量进行分类和优先级排序，确保即使流量离开集群，关键流量也能获得优先处理。

通过在 Calico `hostendpoint` 上设置 `qos.projectcalico.org/dscp` 注解，Calico 可以对出站数据包应用适当的 DSCP 标记。这就像给您的数据包贴上 VIP 徽章，无需排队——直接进入支持 QoS 的网络的快速通道。

此更新引入了一种新的 DSCP 类型，支持数字值（0–63）和常见字符串值，以及相应的数据平面逻辑，以在多个数据平面中强制执行 DSCP 标记。由于 DSCP 嵌入在 6 位 IP 数据包头中，您的网络中的下游设备可以使用这些标记进行转发和优先级排序，从而更容易将 Kubernetes 工作负载集成到现有的支持 QoS 的环境中。

### 工作原理

*   DSCP 支持数字值（0–63）和字符串名称（AF11、EF、CS5）。
*   新的 `QoSPolicy` API 用于 Kubernetes 原生流量控制。
*   通过数据平面使用 `iptables` 或 `nftables` 强制执行。

### 重要性

*   优先处理关键工作负载：视频或交易等对延迟敏感的流量会获得加速处理。
*   简化配置：在清单中声明性地设置 QoS，而不是手动配置 DSCP。
*   面向未来：可跨 `iptables` 和 `nftables` 数据平面工作。

```
apiVersion: projectcalico.org/v3
kind: HostEndpoint
metadata:
  name: hep-with-dscp
  annotations:
    qos.projectcalico.org/dscp: "cs5"

```

**影响可视化：**

*   🟢 视频/语音流量 → 使用 EF 优先处理
*   🔵 API 流量 → 标记为 AF21
*   ⚪ 批处理作业 → 默认 BE

## Felix 直接编程的封装路由

封装对 Calico 来说并不新鲜，但在 v3.31 中，Felix 接管了 IP-in-IP 和无封装路由的职责。此前，BIRD 通过 BGP 处理这些。将其转移到 Felix 可以简化操作，减少依赖，并加快大型集群中的实时升级。

```
apiVersion: crd.projectcalico.org/v1
kind: FelixConfiguration
metadata:
 name: default
spec:
 programClusterRoutes: Enabled

```

## 对 natOutgoing 的精细控制（社区贡献！）

Calico v3.31 引入了对 NAT 出站流量的更精细控制。此前，启用 `natOutgoing` 会对所有离开 IPPool 的流量进行 SNAT，包括本地集群流量。现在，Felix 引入了 `natOutgoingExclusions`：

*   **IPPoolsOnly**（默认）：只有离开 IPPool 的流量才会被 SNAT。
*   **IPPoolsAndHostIPs**：离开 IPPool 的流量和流向集群主机的流量都会被 SNAT。

示例补丁命令：

```
kubectl patch felixconfiguration --type=merge default -p='{"spec":{"natOutgoingExclusions":"IPPoolsAndHostIPs"}}'

```

## BGP 增强功能

此前，Calico 对所有 BGP 会话都使用节点的全局 ASN。现在，您可以针对每个对等体进行覆盖，从而解锁与外部路由器的 eBGP 和路由反射器设计等场景。

```
kind: BGPPeer
apiVersion: projectcalico.org/v3
metadata:
  name: asn_override
spec:
  asNumber: 64516
  localASNumber: 65002

```

## 性能与可用性

*   **更快的 IPAM：** 高效的服务器端过滤加速了大型集群（1000+ 块）中的 IP 分配。
*   **并行启动：** Felix 现在并行加载 BPF 程序，减少了启动延迟。
*   **内存优化：** 对资源标签键/值进行去重，以减少大规模部署时的内存使用。
*   **安全与合规：** TLS 密码现在可根据企业需求进行配置。
*   **性能改进：** 选择器索引去重、并行 BPF 程序加载、降低内存使用量。
*   **`calicoctl validate`：** 在本地验证输入，无需应用更改。
*   **AutoHostEndpoint：** 支持 `InterfaceSelectors` 和新的 `InterfaceCIDRs` 选项以精确匹配节点 IP。

请查阅我们[发布说明](https://docs.projectcalico.org/release-notes/v3.31)中 OpenStack 和 OpenShift 的完整改进列表。

[点击此处](https://demo.arcade.software/SZ028sCkdnwA8SF1Idlq?embed)在您的浏览器中体验 Calico v3.31 Whisker UI 改进。