<!--
title: Kubernetes v1.35：Kubelet 配置目录插槽功能正式 GA
cover: https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/k8s-v1.35.png
summary: Kubernetes v1.35发布Kubelet配置目录插槽功能(GA)。它通过--config-dir简化了大型集群配置管理，允许合并多个文件，实现灵活定制。
-->

Kubernetes v1.35发布Kubelet配置目录插槽功能(GA)。它通过--config-dir简化了大型集群配置管理，允许合并多个文件，实现灵活定制。

> 译自：[Kubernetes v1.35: Kubelet Configuration Drop-in Directory Graduates to GA](https://kubernetes.io/blog/2025/12/22/kubernetes-v1-35-kubelet-config-drop-in-directory-ga/)
> 
> 作者：Sohan Kunkerkar (Red Hat)

随着 Kubernetes v1.35 版本的发布，Kubelet 配置目录插槽（drop-in directory）功能已正式可用。
这项新稳定的功能简化了在大型、异构集群中管理 Kubelet 配置的复杂性。

在 v1.35 中，Kubelet 命令行参数 `--config-dir` 已达到生产就绪状态并获得全面支持，
允许您指定一个包含 Kubelet 配置插槽文件的目录。
该目录中的所有文件将自动与您的主 Kubelet 配置合并。
这使得集群管理员能够为 Kubelet 维护一个统一的*基础配置*，同时为不同的节点组或用例实现有针对性的自定义，而无需复杂的工具或手动配置管理。

## 问题：大规模管理 Kubelet 配置

随着 Kubernetes 集群变得越来越大和复杂，它们通常包含具有不同硬件能力、工作负载要求和操作约束的异构节点池。这种多样性要求不同节点组之间有不同的 Kubelet 配置——然而，大规模管理这些多样化的配置变得越来越具有挑战性。由此带来了几个痛点：

*   **配置漂移**：不同节点可能存在细微的配置差异，导致行为不一致
*   **节点组定制**：GPU 节点、边缘节点和标准计算节点通常需要不同的 Kubelet 设置
*   **操作开销**：为每种节点类型维护独立的、完整的配置文件容易出错且难以审计
*   **变更管理**：在异构节点池中推出配置更改需要仔细协调

在 Kubernetes 中添加此支持之前，集群管理员必须在为所有节点使用单一整体配置文件、手动维护多个完整配置文件或依赖独立工具之间做出选择。每种方法都有其缺点。
此次功能晋升到稳定版为集群管理员提供了一个完全受支持的第四种方法来解决这一挑战。

## 示例用例

### 管理异构节点池

考虑一个包含多种节点类型的集群：标准计算节点、高容量节点（例如带有 GPU 或大内存的节点）以及具有特殊要求的边缘节点。

#### 基础配置

文件：`00-base.conf`

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
clusterDNS:
  - "10.96.0.10"
clusterDomain: cluster.local

```

#### 高容量节点覆盖

文件：`50-high-capacity-nodes.conf`

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
maxPods: 50
systemReserved:
  memory: "4Gi"
  cpu: "1000m"

```

#### 边缘节点覆盖

文件：`50-edge-nodes.conf`（边缘计算通常容量较低）

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
evictionHard:
  memory.available: "500Mi"
  nodefs.available: "5%"

```

通过这种结构，高容量节点应用基础配置和容量特定的覆盖配置，而边缘节点则应用带有边缘特定设置的基础配置。

### 渐进式配置发布

在发布配置更改时，您可以：

1.  添加一个带有高数字前缀的新插槽文件（例如 `99-new-feature.conf`）
2.  在部分节点上测试更改
3.  逐步推广到更多节点
4.  一旦稳定，将更改合并到基础配置中

## 查看合并后的配置

由于配置现在分散在多个文件中，您可以使用 Kubelet 的 `/configz` 端点检查最终合并的配置：

```
# Start kubectl proxy
kubectl proxy

# In another terminal, fetch the merged configuration
# Change the '<node-name>' placeholder before running the curl command
curl -X GET http://127.0.0.1:8001/api/v1/nodes/<node-name>/proxy/configz | jq .

```

这显示了 Kubelet 在所有合并应用后实际使用的配置。
合并后的配置还包括通过 Kubelet 命令行参数指定的任何配置设置。

有关详细的设置说明、配置示例和合并行为，请参阅[官方文档](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#configuration-drop-in-directory)。

## 最佳实践

使用 Kubelet 配置插槽目录时：

1.  **逐步测试配置**：在新插槽配置在全集群范围内推广之前，始终在部分节点上进行测试，以最大程度地降低风险
2.  **版本控制您的插槽文件**：将您的插槽配置文件与您的基础设施即代码一起存储在版本控制中（或生成这些配置的源配置中），以跟踪更改并方便回滚
3.  **使用数字前缀实现可预测的顺序**：使用数字前缀（例如 `00-`、`50-`、`90-`）命名文件，以明确控制合并顺序，并使配置分层对其他管理员清晰可见
4.  **注意临时文件**：一些文本编辑器在编辑时会自动在同一目录中创建备份文件（例如 `.bak`、`.swp` 或带有 `~` 后缀的文件）。确保这些临时文件或备份文件不会留在配置目录中，因为它们可能会被 Kubelet 处理

## 致谢

此功能是通过 [SIG Node](https://github.com/kubernetes/community/tree/master/sig-node) 的协作努力开发的。特别感谢所有贡献者，他们在此功能从 v1.28 的 Alpha 版，经 v1.30 的 Beta 版，到 v1.35 的 GA 版的整个历程中，帮助设计、实现、测试和文档化此功能。

要提供对此功能的反馈，请加入 [Kubernetes 节点特别兴趣小组](https://github.com/kubernetes/community/tree/master/sig-node)，参与 [公共 Slack 频道](http://slack.k8s.io/)（#sig-node）的讨论，或在 [GitHub](https://github.com/kubernetes/kubernetes/issues) 上提交问题。

## 参与其中

如果您对 Kubelet 配置管理有任何反馈或问题，或者想分享您使用此功能的经验，欢迎加入讨论：

SIG Node 期待听到您在生产环境中使用此功能的经验！