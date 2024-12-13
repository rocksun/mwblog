
<!--
title: Kubernetes中消除未利用资源
cover: ./cover.png
-->

Kubernetes中未使用的资源不仅仅是预算项目——它们也是效率、可扩展性和性能的隐形杀手。

> 译自 [Eliminating Unutilized Resources in Kubernetes](https://overcast.blog/eliminating-unutilized-resources-in-kubernetes-7a36c05b1d63)，作者 DavidW。

Kubernetes 中未使用的资源不仅仅是预算项目——它们是效率、可扩展性和性能的隐形杀手。

浪费的 CPU 周期、空闲内存和未充分利用的节点都会累积起来，增加成本，同时降低集群处理实际工作负载的能力。如果您大规模使用过 Kubernetes，您就会知道这些低效率如何演变成真正的运维难题。

如今，随着 [Scaleops](https://scaleops.com/) 等新型智能自动化工具的兴起，您可以相当快速且轻松地检测、修复和防止未使用的资源，包括“[无法驱逐的工作负载](https://scaleops.com/blog/scaleops-pod-placement-optimizing-unevictable-workloads/)”，例如 PDB、配置错误的 Safe-to-Evict 注解和“裸 Pod”。自动化此过程可同时最大限度地减少资源浪费和人工工作。

### 什么是 Kubernetes 中未使用的资源？

未使用的资源是指剩余的空闲但已保留的计算、内存或存储容量，这通常是由于配置不当或工作负载放置不当造成的。这些低效率以各种方式出现：

- Pod 使用的资源远少于其请求的资源。
- 由于无法驱逐的工作负载，节点处于空闲状态。
- 资源配置过多的集群浪费宝贵的云资源。

# 为什么未使用的资源比以往任何时候都更重要

每个空闲的 CPU 内核或未使用的 GB 内存都代表着金钱的浪费。除了成本之外，资源低效率还会影响可扩展性，使集群变得臃肿，无法有效响应不断变化的工作负载。

随着集群规模的扩大，这些低效率会加剧，将可控的问题变成运维危机。解决未使用的资源不仅仅是为了节省资金——它还关乎释放 Kubernetes 设置的全部潜力。

### 为什么会发生这种情况？

Kubernetes 的灵活性是有代价的：复杂性。虽然它为团队提供了精确管理资源的工具，但要实现最佳利用率，需要深入了解资源请求、限制、调度策略和自动缩放机制。

一些 [常见原因](https://scaleops.com/blog/scaleops-pod-placement-optimizing-unevictable-workloads/) 包括：

- 配置错误的 **Pod Disruption Budgets (PDB)**，阻止 Pod 被驱逐。
- 过度使用 `safe-to-evict: false` 注解。
- 缺乏管理控制器的裸 Pod，使其无法驱逐。
- 保守的资源请求远远超过实际使用情况。

### 解决未使用的资源的关键挑战

1. **可见性**：如果没有强大的监控，未使用的资源可能会在成本飙升或性能下降之前不被注意到。
2. **无法驱逐的工作负载**：PDB 和关键注释通常会阻止自动缩放器优化资源。
3. **人工工作**：识别、分析和修复低效率需要大量时间和专业知识，从而分散了其他工程工作的重点。
4. **可扩展性**：集群越大，就越难以手动微调数百或数千个节点上的资源分配。

### 实现解决方案

像 [ScaleOps](https://scaleops.com/) 这样的现代工具可以自动化繁重的工作。

通过 **检测** 低效率、智能地 **重新调度** **工作负载** 并 **持续** **监控** 资源浪费，像 ScaleOps 这样的工具弥合了 Kubernetes 的原始功能与实际可用性之间的差距。

借助智能算法和直观的仪表板，ScaleOps 和其他现代工具可以优化资源使用，而无需不断进行手动调整，并获得最佳结果。

### 你将学到什么

在本指南中，我们将分解：

- Kubernetes 中未使用的资源是什么，以及为什么它们至关重要。
- 未使用资源的主要原因，包括“无法驱逐的工作负载”。
- 包括 ScaleOps 在内的用于自动化资源优化的工具和策略。
- 在集群中管理资源效率的最佳实践和陷阱。

让我们深入研究并解决正在消耗 Kubernetes 集群效率的低效率问题。

## 了解 Kubernetes 中未使用的资源

在 Kubernetes 中有效使用资源对于保持成本效益、可扩展性和性能至关重要。但是，各种因素都可能导致资源被分配但未被充分利用，从而导致资源空闲并增加成本。让我们探讨一下未使用的资源是什么，它们为什么会发生以及如何有效地解决它们。

## 什么是未使用的 Kubernetes 资源？

未使用的资源是指分配给 Kubernetes 集群中的节点或 Pod 但未被应用程序或工作负载积极使用的 CPU、内存或存储部分。这些空闲资源通常是由于：
**资源过度配置:** 分配超过所需资源。**调度不当:** 工作负载在节点上的分布不均。**自动伸缩器限制:** 由于特定的 Pod 配置或约束，无法调整或缩减节点。

# 发生原因

**保守的资源请求:** 开发人员通常会高估资源需求以避免中断，导致 Pod 使用的 CPU 或内存远低于其分配量。**受限的工作负载迁移性:** 某些工作负载（例如关键系统 Pod）配置为保留在特定节点上。**不平衡的调度:** Kubernetes 的默认调度可能会由于 bin-packing 算法不足而导致某些节点资源过载，而其他节点空闲。**节点级约束:** 集群自动伸缩器和其他工具无法驱逐标记为不可驱逐的 Pod，导致节点资源利用率不足。

# 检测未利用资源

使用 **Prometheus** 和 **Grafana** 等工具监控集群指标，以识别请求资源使用量与实际资源使用量之间的差异。例如，以下 PromQL 查询显示 Pod 的 CPU 使用率：

`rate(container_cpu_usage_seconds_total[5m])`

将其与 `kube_pod_container_resource_requests` 结合使用，以比较请求的资源使用量与实际资源使用量：

`kube_pod_container_resource_requests{resource="cpu"}`

这些指标可以突出显示资源过度配置的 Pod 或资源利用率不足的节点。

# 未利用资源的类型

## 通用资源利用率不足

当分配的资源（CPU、内存）未被 Pod 完全使用时，就会发生通用资源利用率不足。这通常源于过于保守的资源请求和不匹配的扩展策略。

## 发生原因

**峰值开销:** 开发人员根据潜在的峰值使用量而不是实际平均使用量来配置资源。**静态资源分配:** 针对需求随时间变化的工作负载设置固定的资源限制。

## 如何检测

使用监控工具比较实际使用量与请求量，检查 **资源利用率比率** 是否较低：

`kubectl top pods`

此命令显示每个 Pod 当前的 CPU 和内存消耗，从而可以轻松识别资源利用率不足的 Pod。

## 示例：资源过度分配的 Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: over-provisioned-app
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app-container
        image: app-image:v1
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "1"
            memory: "2Gi"
```

如果每个 Pod 的实际使用量约为 `200m` CPU 和 `512Mi` 内存，则此 Deployment 会浪费超过一半的已分配资源。

## 常用案例

**预生产环境**: 资源过度配置以模拟峰值负载。**突发工作负载**: 使用量出现零星峰值的应用程序通常会导致资源过度配置。

# 不可驱逐的工作负载

不可驱逐的工作负载是指 Kubernetes 无法重新调度或删除的 Pod，这使其成为自动伸缩器效率的重要障碍。去除或防止它们很容易[使用合适的工具](https://scaleops.com/blog/scaleops-pod-placement-optimizing-unevictable-workloads/)，但手动操作可能会成为持续的难题。

## 不可驱逐工作负载的主要因素

**1. Pod Disruption 预算 (PDB)**

PDB 定义在中断期间必须保持运行的最小副本数。这可以防止关键工作负载被驱逐，但可能会阻碍节点扩展。

**PDB 配置示例**：

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-app-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: my-app
```

此配置确保始终运行两个副本，但在缩减节点规模时可能会阻止驱逐操作，导致某些节点资源利用率不足。

**2. 可安全驱逐的注释**

标记为 `safe-to-evict: false` 的 Pod 在节点扩展或 bin-packing 操作期间无法被删除或重新调度。

**注释示例**：

```yaml
metadata:
  annotations:
    cluster-autoscaler.kubernetes.io/safe-to-evict: "false"
```

**3. 裸 Pod**

直接创建而无需控制器（例如，Deployment、ReplicaSet）的 Pod 缺乏重新调度或扩展所需的自动化功能。

**裸 Pod 示例**：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: standalone-pod
spec:
  containers:
  - name: app-container
    image: app-image:v1
```

这些 Pod 会阻止节点缩减规模，导致资源空闲。

# 如何解决不可驱逐的工作负载

在我们开始之前，我的建议是使用智能专用工具自动化此过程，我最喜欢的是 [Scaleops](https://scaleops.com/)。

我更喜欢选择此类工具的原因很简单：

- 安装 10 分钟后（无需更改代码/配置），您将看到未利用资源减少 95% 以上，并且不会再次出现。
- 它可以自动执行，无需任何手动操作。
- 它可以持续地自动检测、修复和防止未利用资源。安装后即可忽略。

## Kubernetes VPA：优缺点和最佳实践
探索 Kubernetes VPA 的优缺点和最佳实践，包括其工作原理、关键指标、配置和用法……

scaleops.com

但是，您也可以选择手动执行此操作，并反复执行，无论出于何种原因迫使您这样做。如果您这样做，以下是一些可以帮助您的步骤：

## 1. 调整 Pod Disruption Budgets

查看并更新 PDB 以尽可能允许更大的驱逐灵活性：

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: updated-pdb
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      app: my-app
```

## 2. 谨慎使用 Safe-to-Evict

仅对关键工作负载应用 `safe-to-evict` 批注。

## 3. 用控制器替换裸 Pod

使用 Deployment 或 StatefulSets 等控制器部署工作负载，以确保正确的管理和可扩展性。

**以前裸 Pod 的示例部署**：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: managed-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app-container
        image: app-image:v1
```

这确保 Kubernetes 可以有效地扩展和重新调度工作负载。

通过解决普遍的资源利用不足和不可驱逐的工作负载，Kubernetes 集群可以更高效地运行，降低成本并提高可扩展性。通过定期审核和自动化工具积极主动地维护最佳资源利用率。

# 检测、修复和防止未利用资源

## 为什么检测和防止未利用资源？

未利用的资源会导致：

* **成本增加**：空闲资源会增加云账单。
* **性能下降**：资源碎片会影响工作负载效率。
* **可扩展性受限**：低效的集群难以处理扩展需求。

## 智能自动化工具如何提供帮助

ScaleOps 等工具提供了一种针对资源低效的自动化解决方案：

* **检测**：通过全面的集群分析识别未充分利用的节点、不可驱逐的 Pod 和资源分配问题。
* **修复**：应用智能调度算法来重新分配工作负载，而不会违反 PDB 或 safe-to-evict 规则。
* **预防**：持续监控集群，确保将不可驱逐的工作负载降至最低，并有效利用资源。

以下是 ScaleOps 如何优化不可驱逐的工作负载：

```yaml
# ScaleOps 优化示例
apiVersion: scaleops/v1
kind: PodOptimization
metadata:
  name: optimize-workloads
spec:
  policies:
  - type: "reschedule"
    targets:
    - labelSelector: "safe-to-evict: false"
    action: "optimize-placement"
```

此配置识别不可驱逐的 Pod 并优化其放置位置，以实现更好的资源分配。

# 手动方法来检测和修复 Kubernetes 中未利用的资源

虽然像 ScaleOps 这样的自动化工具简化了未利用资源的检测和纠正，但手动方法提供了灵活性和直接控制。使用 Kubernetes 原生工具和命令，您可以分析资源使用情况并解决集群中的低效问题。

# 检测未利用资源

## 使用 `kubectl top`

识别未充分利用的 Pod

`kubectl top` 命令检索集群中 Pod 和节点的资源使用情况指标，例如 CPU 和内存。要识别未充分利用的 Pod：

`kubectl top pods --all-namespaces`

此命令显示所有正在运行的 Pod 的当前资源使用情况。将报告的值与 Pod 配置中定义的资源请求进行比较。例如，仅使用 `100m` CPU 但请求 `500m` CPU 的 Pod 表示过度配置。

# 分析节点的资源低效

要分析节点及其利用率水平，请运行：

`kubectl top nodes`

此命令显示节点上的总 CPU 和内存使用情况。始终利用率低的节点可能具有不可驱逐的工作负载或不平衡的调度。

# 将资源请求与实际使用情况进行比较

使用 Prometheus 指标比较请求的和实际的使用情况。对于 CPU 利用率，以下 PromQL 查询很有用：

`rate(container_cpu_usage_seconds_total[5m])`

将其与请求的资源进行比较：

`kube_pod_container_resource_requests{resource="cpu"}`

此比较突出显示分配的资源多于其消耗的 Pod。

# 修复过度配置的资源

# 调整资源请求和限制

过度配置的 Pod 会浪费本可以分配到其他地方的资源。要解决此问题，请更新未充分利用的 Pod 的资源请求和限制。例如：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource-optimized-app
spec:
  replicas: 2
  template:
    spec:
      containers:
      - name: app-container
        image: app-image:v1
        resources:
          requests:
            cpu: "250m"
            memory: "512Mi"
          limits:
            cpu: "500m"
            memory: "1Gi"
```

此更新使资源请求与观察到的使用情况保持一致，从而减少浪费，同时保持性能。

# 解决不可驱逐的工作负载

## 查看和修改 Pod Disruption Budgets (PDB)
Pod Disruption Budgets (PDB) may prevent evictions, leading to idle resources. List all PDBs in the cluster:

```bash
kubectl get pdb --all-namespaces
```
Check the `minAvailable` or `maxUnavailable` values. For example:

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: app-pdb
spec:
  minAvailable: 3
  selector:
    matchLabels:
      app: critical-app
```
If the `minAvailable` value is too high, adjust it to allow more flexibility during scaling:

```yaml
spec:
  minAvailable: 2
```

## Removing Safe-to-Evict Annotations
Safe-to-evict annotations prevent the autoscaler from evicting Pods. To find Pods with this annotation:

```bash
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.metadata.annotations."cluster-autoscaler.kubernetes.io/safe-to-evict" == "false") | .metadata.name'
```
Once identified, edit the Pod configuration to remove the annotation:

```bash
kubectl edit pod <pod-name>
```
Delete the following annotation:

```yaml
metadata:
  annotations:
    cluster-autoscaler.kubernetes.io/safe-to-evict: "false"
```

## Converting Bare Pods to Managed Workloads
Bare Pods (lacking a controller) prevent node scaling. Convert them to managed workloads, such as Deployments. Export the Pod configuration:

```bash
kubectl get pod naked-pod -o yaml > naked-pod.yaml
```
Modify the YAML to create a Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: managed-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: naked-pod
  template:
    metadata:
      labels:
        app: naked-pod
    spec:
      containers:
      - name: app-container
        image: app-image:v1
```
Apply the updated configuration and delete the original bare Pod:

```bash
kubectl apply -f managed-app.yaml
kubectl delete pod naked-pod
```

## Continuous Monitoring and Optimization
Regular monitoring is key to preventing the recurrence of underutilized resources. Use tools like Prometheus and Grafana to set up dashboards and alerts for resource usage metrics. Monitor the difference between requested and actual usage to proactively adjust resource allocation. This proactive approach ensures the cluster remains optimized and cost-effective.

# Best Practices for Managing Underutilized Resources
When not using intelligent automation solutions and operating entirely manually, ensure:

**Regularly audit PDBs**
Ensure PDB configurations allow necessary evictions during scaling or maintenance. Avoid overly strict policies that lock Pods in place.  **Use safe-to-evict annotations judiciously**
Restrict the use of `safe-to-evict: false` to truly critical workloads. Overuse limits the autoscaler's optimization capabilities. **Deploy workloads using controllers**
Avoid bare Pods by deploying workloads using controllers like Deployments, ReplicaSets, or StatefulSets. This ensures proper management and eviction when needed. **Adopt automated resource management tools**
Leverage tools like ScaleOps to automatically detect and optimize underutilized resources. **Continuously monitor resource usage**
Implement robust monitoring to track resource utilization and identify inefficiencies in real-time.

# Pitfalls to Watch Out For
When not using intelligent automation solutions and operating entirely manually, be aware of:

**Restrictive PDBs**
Incorrectly configured PDBs can prevent autoscaler operation, leading to idle resources. **Overuse of un-evictable annotations**
Marking too many Pods as un-evictable hinders autoscaling efforts and increases costs. **Ignoring bare Pods**
Failure to effectively manage bare Pods prevents node scaling and wastes resources. **Inconsistent resource monitoring**
Clusters without regular audits or monitoring may accumulate inefficiencies over time. **Lack of automation**
Relying on manual processes to manage cluster resources can lead to errors and delays.

# Conclusion
Effective resource management is crucial for maintaining a scalable and cost-effective Kubernetes cluster. By understanding and addressing underutilized resources, engineering teams can save significant costs and improve performance.

We discussed:

- Types of underutilized resources, including un-evictable workloads.
- The challenges of manually detecting and remediating these issues.
- How tools like ScaleOps automate optimization, improve visibility, and simplify resource management.

Start by checking your cluster for inefficiencies using Kubernetes native tools, or delve into automated solutions like ScaleOps for a more streamlined process. If you face similar challenges or have tips to share, let us know in the comments below.

Thank you for reading!

# Learn More
## Kubernetes VPA: Advantages, Disadvantages, and Best Practices
### Explore the advantages, disadvantages, and best practices of Kubernetes VPA, including how it works, key metrics, configuration, and usage…
scaleops.com

## Kubernetes Pod Right-Sizing: A Practical Guide
### Effective resource allocation is crucial for optimizing the cost and performance of applications running in…
overcast.blog