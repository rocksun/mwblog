
<!--
title: Kubernetes 中的 OOM Killer：优化技巧
cover: https://www.causely.io/wp-content/uploads/2024/08/preventing-oom-kills-1024x576.png
-->

Kubernetes 中的内存不足 (OOM) 杀手：如何优化容器内存管理并保持应用程序稳定性

> 译自 [OOM Killer in Kubernetes: Optimization Tips](https://www.causely.io/blog/kubernetes-oom-killer-tips/)，作者 Karina Babcock。


在 Kubernetes 上大规模运行容器化应用程序需要仔细的资源管理。一个非常复杂但常见的挑战是防止内存不足 (OOM) 杀死，当容器的内存消耗超过其分配的限制时就会发生这种情况。这种由 Kubernetes 内核的 OOM 杀手进行的粗暴终止会破坏应用程序的稳定性，并可能影响应用程序的可用性和整个环境的健康状况。

在本文中，我们将探讨 OOM 杀死可能发生的原因，并提供应对和防止它们的策略。

在深入研究之前，值得注意的是，OOM 杀死是一种症状，可能有多种根本原因。对于组织来说，实施一个能够快速准确地解决根本原因分析问题的系统非常重要，这样可靠性工程团队就可以快速响应，并有可能从一开始就防止这些事件发生。

## 深入了解 OOM 杀死

[Kubernetes](https://www.causely.io/resources/glossary-cloud-native-technologies/) 中的内存不足 (OOM) 杀死发生在容器超过其内存限制时，导致 Kubernetes 内核的 OOM 杀手终止容器。这会影响应用程序的稳定性，需要立即关注。

以下几个因素可能会在您的 Kubernetes 环境中触发 OOM 杀死：

* **内存限制超过**：这是最常见的原因。如果容器持续超过其指定的内存上限，OOM 杀手就会介入以防止系统崩溃。
* **内存泄漏**：应用程序可能会随着时间的推移而出现内存泄漏，它们分配内存但无法正确释放。这种隐藏的、意外的增长最终会导致 OOM 杀死。
* **资源过度承诺**：将太多资源密集型 Pod 共同放置在一个节点上会导致可用内存耗尽。当组合的内存使用量超过容量时，OOM 杀手就会启动。
* **突发工作负载**：具有尖峰工作负载的应用程序可能会经历突然的内存激增，从而突破其限制，触发 OOM 杀死。

例如，一个出现内存泄漏代码错误的 Web 服务器可能会逐渐消耗越来越多的内存，直到 OOM 杀手介入以防止崩溃。

另一种情况可能是当 Kubernetes 集群通过在单个节点上调度太多 Pod 来过度承诺资源时。OOM 杀手可能需要介入以释放内存并确保系统稳定性。

## OOM 杀死的破坏性影响：为什么它们很重要

OOM 杀死通常不会发生。它们会对您的应用程序和集群的整体健康状况造成一系列负面影响，例如：

* **应用程序停机**：当容器被 OOM 杀死时，它会突然终止，导致应用程序立即停机。用户可能会遇到服务中断和停机。
* **数据丢失**：依赖内存中数据或有状态会话的应用程序在 OOM 杀死期间可能会丢失关键信息。
* **性能下降**：频繁的 OOM 杀死会导致容器反复重启。这种持续的波动会降低应用程序的整体性能和用户体验。
* **服务中断**：应用程序通常相互交互。一个容器中的 OOM 杀死可能会中断服务间通信，导致级联故障和更广泛的服务中断。

如果运行关键数据库服务的容器遇到 OOM 杀死，可能会导致数据丢失和损坏。这会导致依赖数据库获取信息的其它容器的服务中断，从而导致整个应用程序生态系统出现级联故障。

## 应对 OOM 杀死

有一些不同的策略可以用来应对 OOM 杀死，以尝试运行一个内存高效的 Kubernetes 环境。

### 设置适当的资源请求和限制

例如，您可以在 Kubernetes 部署中为特定容器设置 200Mi 的内存请求和 300Mi 的内存限制。请求确保容器至少获得 200Mi 的内存，而限制将其限制在 300Mi 以防止过度消耗。

```yaml
resources:
  requests:
    memory: "200Mi"
  limits:
    memory: "300Mi"
```

虽然这可能会缓解潜在的内存使用问题，但这是一个非常手动化的过程，并且根本没有处理我们使用 Kubernetes 可以实现的动态特性。它也不能解决源问题，源问题可能是触发内存泄漏或 GC 进程失败的代码级问题。

### 转向自动扩展

利用 [自动扩展](https://www.causely.io/resources/glossary-cloud-native-technologies/) 功能是资源分配的核心动态选项。有两种自动扩展方法：

- **垂直 Pod 自动伸缩 (VPA):** [VPA](https://kubernetes.io/docs/concepts/workloads/autoscaling/) 根据实时内存使用模式动态调整资源限制。这确保容器拥有足够的内存来运行，但避免过度配置。
- **水平 Pod 自动伸缩 (HPA):** [HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) 根据内存使用情况向上或向下扩展运行应用程序的 Pod 数量。这将内存使用情况分布在多个 Pod 上，防止任何单个 Pod 超出其限制。以下 HPA 配置显示了根据内存使用情况进行扩展的示例：

```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

### 监控内存使用情况

主动监控是关键。例如，您可以配置 [Prometheus](https://www.causely.io/resources/glossary-cloud-native-technologies/) 每 15 秒从您的 Kubernetes Pod 中抓取内存指标，并设置 [Grafana](https://grafana.com/) 仪表板以可视化内存使用趋势。此外，您可以在 Prometheus 中创建警报，以便在内存使用量超过某个阈值时触发通知。

### 优化应用程序内存使用情况

不要低估代码优化的力量。解决应用程序中的内存泄漏，并实施内存高效的数据结构以最大程度地减少内存消耗。

### Pod 中断预算 (PDB)

在部署更新时，[PDB](https://www.causely.io/resources/glossary-cloud-native-technologies/) 确保即使在推出期间，也保持最少的 Pod 可用。这减轻了在部署期间广泛发生 OOM 杀死的风险。以下是一个 PDB 配置示例，有助于确保最小的 Pod 可用性。

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-app-pdb
spec:
  minAvailable: 80%
  selector:
    matchLabels:
      app: my-app
```

### 管理节点资源

您可以应用节点选择器以确保内存密集型 Pod 仅调度到具有至少 8GB 内存的节点上。此外，您可以使用污点和容忍度将具有高内存容量的特定节点专门用于内存密集型应用程序，从而防止由于资源限制而导致的 OOM 杀死。

```yaml
nodeSelector:
  disktype: ssd
tolerations:
- key: "key"
  operator: "Equal"
  value: "value"
  effect: "NoSchedule"
```

### 使用 QoS 类别

Kubernetes 提供服务质量 ([QoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)) 类别，这些类别优先考虑对关键应用程序的资源分配。将最高 QoS 类别分配给最不能容忍 OOM 杀死的应用程序。以下是一个带有 QoS 参数的资源配置示例：

```yaml
resources:
  requests:
    memory: "1Gi"
    cpu: "500m"
  limits:
    memory: "1Gi"
    cpu: "500m"
```

这些只是一些可能有助于防止 OOM 杀死的策略。挑战在于它们发生的频率以及发生时对应用程序的风险。

可以想象，在 Kubernetes 环境中，不可能手动管理资源利用率并保证容器化应用程序的稳定性和性能。

## 手动阈值 = 僵化和风险

这些技术可以帮助降低 OOM 杀死的风险。但是，问题并没有完全解决。通过设置手动阈值和限制，您将消除 Kubernetes 的许多动态优势。

解决 OOM 杀死问题的更理想方法是使用自适应的动态资源分配。即使您在初始部署时正确地分配了资源，也会有许多因素会改变应用程序消耗资源的方式。还存在风险，因为应用程序和资源问题不仅会影响一个 Pod 或一个容器。资源问题可能会波及集群的各个部分，并降低其他正在运行的应用程序和服务的性能。

## 哪种策略最有效地防止 OOM 杀死？

垂直 Pod 自动伸缩 (VPA) 和水平 Pod 自动伸缩 (HPA) 是用于管理 Kubernetes 容器中资源限制的常用策略。VPA 根据实时内存使用模式调整资源限制，而 HPA 根据内存使用情况扩展 Pod。

使用 Prometheus 等工具进行监控可能有助于解决内存使用趋势问题。优化应用程序内存使用情况并非易事，因为确定是基础设施还是代码导致问题尤其具有挑战性。

Pod Disruption Budgets (PDB) 可以帮助确保在部署期间始终保持最少数量的 Pod 可用，而节点选择器和污点则可以用于管理节点资源。服务质量 (QoS) 类别会优先为关键应用程序分配资源。

有一点是肯定的：OOM 杀死是使用传统监控工具和方法管理的常见且代价高昂的挑战。

在 [Causely](https://www.causely.io/)，我们专注于应用因果推理软件来帮助组织保持应用程序的健康和弹性。通过自动化根本原因分析，可以立即解决诸如 OOM 杀死之类的问题，并避免新版本或应用程序更改的意外后果。
