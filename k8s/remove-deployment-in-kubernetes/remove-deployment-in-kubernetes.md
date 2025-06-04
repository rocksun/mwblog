<!--
title: 如何在 Kubernetes 中删除 Deployment：方法、步骤和工具
cover: https://cdn.thenewstack.io/media/2025/05/26a7059e-remove-kubernetes-deployment-2.jpg
summary: K8s删除Deployment，用kubectl delete或helm uninstall，别忘清理PVC。kubectl apply --prune可删除不再定义的资源，ttlSecondsAfterFinished清理Job。Finalizers卡住？手动移除需谨慎！GitOps流程更安全，Argo CD级联删除很方便。缩减副本为0可暂停Deployment。
-->

K8s删除`Deployment`，用`kubectl delete`或`helm uninstall`，别忘清理`PVC`。`kubectl apply --prune`可删除不再定义的资源，`ttlSecondsAfterFinished`清理`Job`。`Finalizers`卡住？手动移除需谨慎！`GitOps`流程更安全，`Argo CD`级联删除很方便。缩减副本为0可暂停`Deployment`。

> 译自：[How To Remove a Deployment in Kubernetes: Methods, Steps and Tools](https://thenewstack.io/remove-deployment-in-kubernetes/)
> 
> 作者：Sunny Yadav

**要点**：

*   要删除 Deployment 及其关联的资源，请使用：
    `kubectl delete deployment <deployment-name> -n <namespace>`
*   删除 Deployment 不会删除关联的 PVC 或 PV。您必须显式删除这些资源以防止孤立卷：
    `kubectl delete pvc <pvc-name> -n <namespace>`
*   使用
    `kubectl apply --prune`
    删除清单中不再定义的资源。为 Job 设置 ttlSecondsAfterFinished 或配置 CronJob 历史记录限制以自动清理已完成的工作负载。

Kubernetes 集群经常积累孤立资源，例如 ReplicaSet、PersistentVolume 和 ConfigMap。删除工作负载后，这些资源会长期存在。结果是什么？浪费存储空间、意外成本和性能下降。

在没有结构化流程的情况下运行临时的 kubectl delete 命令可能会留下悬挂的 Pod 或卡住的 Finalizer。它可能会将一个简单的拆卸变成一个耗时的故障排除会话。此外，运维人员经常报告说，随着集群规模和复杂性的增加，这些手动清理会引入不稳定性和运维负担。

那么，有没有一种方法可以在 Kubernetes 中删除 Deployment，而不会发生所有这些情况？有的！了解如何正确删除 [Kubernetes](https://thenewstack.io/kubernetes/) 中的 Deployment，以保持集群的精简、可预测性，并为下一次部署做好准备。

## 应该删除还是缩减？

| 操作 | 理想使用场景 | 优势 |
|------|------------|-----|
| 缩容 | 非高峰期。维护窗口期。调试会话。 | 保留版本历史和配置以便快速恢复，避免重新应用清单文件。 |
| 删除 | 应用程序永久退役。完全移除工作负载。 | 清理所有资源，确保没有陈旧对象残留。 |

## 前提条件和工具：在 K8s 中删除 Deployment

在删除或缩减 Deployment 之前，请确保您已准备好正确的工具，并且具有访问 [Kubernetes 集群](https://thenewstack.io/is-cluster-api-really-the-future-of-kubernetes-deployment/) 的必要权限。这将确保您可以安全地执行操作，避免配置错误，并在出现问题时轻松回滚。

以下是您需要的：

*   **kubectl**：用于与集群交互的主要命令行工具。
*   [命令行界面 (CLI)](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/)已安装：
*   **已配置的 kubeconfig**：您的本地 kubeconfig 文件应指向正确的集群上下文和命名空间。
*   **集群级权限**：[基于角色的访问控制 (RBAC)](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/) 或允许您获取、列出、缩放和删除 Deployment 的集群角色绑定。
*   **YAML 清单或 Helm Chart**：Deployment 对象的定义，供参考或重新部署。
*   **备份或版本控制**：您的清单记录（例如 git）或快照工具，以防您需要回滚。
*   **监控和日志记录工具（可选但推荐）**：像 [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/)、Grafana 或 EFK/ELK 这样的系统，用于观察更改的影响。

## 删除 Kubernetes 中 Deployment 的 4 种方法

以下是在 Kubernetes 中拆除 Deployment 的四种常用方法。选择最适合您的 [CI/CD 流程](https://thenewstack.io/ci-cd/) 和运维要求的方法。

### 1. `kubectl delete deployment` 命令

使用内置 CLI 进行一次性删除：

```
kubectl delete deployment <deployment-name> [-n <namespace>]
```

此 API 调用会向下级联以删除 Deployment 对象、其 ReplicaSet 和所有关联的 [Pod](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/)。
这是一个快速分解：

*   `kubectl delete`
    ：这是用于删除资源的命令。
*   `deployment`
    ：它指定要删除的资源类型。
*   `<deployment-name>`
    ：这是您要删除的 Deployment 的实际名称所在的位置。
*   `[-n <namespace>]`
这是一个可选标志，用于指定 Deployment 所在的命名空间。如果省略此项，kubectl 将假定为当前或默认命名空间。
因此，如果要删除默认命名空间中名为 my-app 的 Deployment，可以运行：`kubectl delete deployment my-app`

如果它位于名为 staging 的命名空间中，则可以运行：`kubectl delete deployment my-app -n staging`

### 2. 通过 Manifest 删除 (`kubectl delete -f`)

通过将 kubectl 指向它们，将其绑定到你的 Git 支持的 manifest 或本地 YAML 文件：

```
kubectl delete -f path/to/deployment.yaml
```

以下是它的工作原理：

*   `kubectl delete`: 用于删除资源的命令。
*   `-f`: 此标志告诉 kubectl 从指定的文件中读取资源配置。
*   `path/to/deployment.yaml`: 这是你的 manifest 文件的路径，该文件可以定义 Deployment 或任何其他 Kubernetes 资源。kubectl 将读取此文件并删除其中定义的所有资源。

此方法支持目录 (`-f dir/`) 和标签选择器 (`-l key=value`)，使你可以精细地控制要删除的资源。

### 3. 删除 Helm 管理的 Deployment (`helm uninstall`)

当你使用 [Helm](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/) 部署应用程序时，请使用 Helm CLI 卸载它们。这可以确保更彻底地删除作为 Helm 版本一部分的所有资源。

```
helm uninstall <release-name> [-n <namespace>]
```

以下是它的工作原理：

*   `helm uninstall`: 这是卸载版本的 Helm 命令。
*   `<release-name>`: 这是你在安装 Helm 版本时为其指定的名称。
*   `[-n <namespace>]`: 此可选标志指定 Helm 版本部署到的命名空间。如果省略，Helm 将假定为默认命名空间。

例如，如果你在默认命名空间中安装了一个名为 my-chart 的版本，则可以运行：`helm uninstall my-chart`

如果它位于名为 operations 的命名空间中，则可以运行：`helm uninstall my-chart -n operations`

### 4. GitOps 删除（Pull-Request 工作流程）

在 GitOps 中，你的 Git 存储库是事实来源 - 删除通过代码更改进行：

*   删除 Git 分支中的 Deployment YAML（或将其注释掉）。
*   针对你的主分支打开一个 pull request。
*   在审查后合并，并让你的 GitOps 控制器（例如 [Argo CD and Flux](https://thenewstack.io/argo-cd-and-flux-are-cncf-grads-but-what-now/)）协调并删除资源。

这种方法提供了完整的审计跟踪，并与现有的基于 PR 的审查和批准集成。此外，Argo CD 的级联选项使你可以选择是仅删除 Application 对象，还是同时删除所有子资源。

## 如何在 Kubernetes 中删除 Deployment：5 个简单步骤

以下是一个简洁的逐步演练，用于安全地从 Kubernetes 集群中删除 Deployment。你将学习如何查明 Deployment，选择性地暂停它，删除它，验证所有 Pod 和 ReplicaSet 是否消失，最后清理任何剩余资源。

### 1. 识别目标 Deployment

首先，列出你的 Deployment，以确认你要删除的工作负载的确切名称和命名空间。

使用此命令：

```
kubectl get deployments --all-namespaces
```

此命令显示每个 Deployment，以及其命名空间、所需的副本和当前状态。使用 `-n <namespace>` 标志将输出范围缩小到特定命名空间。

### 2. 将副本缩放到零（可选）

如果你希望在删除之前暂停应用程序，请使用以下命令将其副本计数缩减为零：

```
kubectl scale deployment <deployment-name> --replicas=0 -n <namespace>
```

缩放到零会停止所有 Pod，而不会删除 Deployment 对象，从而保留其 manifest 和 rollout 历史记录，以便快速恢复。这在维护窗口或调试会话期间特别有用。

### 3. 执行删除命令

准备好完全拆卸后，请一次性删除 Deployment 对象及其子对象：

```
kubectl delete deployment <deployment-name> -n <namespace>
```

默认情况下，Kubernetes 垃圾回收会将删除操作级联到关联的 ReplicaSet 和 Pod，从而确保它们与 Deployment 一起删除。如果需要调整宽限期或强制删除，可以添加 `--grace-period=<seconds>` 或 `--force` 之类的标志。

### 4. 验证 ReplicaSet 和 Pod 是否已消失

删除后，确认没有与 Deployment 相关的 ReplicaSet 或 Pod 剩余。以下是你可以使用的命令：

成功的删除不会返回匹配的资源。如果仍然看到条目，请重新运行删除命令或调查 finalizers。检查这些可以确保你不会留下占用资源的孤立工作负载。

### 5. 清理关联的资源（Services、PVC、ConfigMaps、Secrets）

Deployment 通常会创建链接的 Services、PersistentVolumeClaims (PVC)、ConfigMaps 或 Secrets，这些资源可能不会自动删除。显式删除它们：
或者，通过标签选择器一次性删除目标资源组：

```
kubectl delete all,configmap,secret -l app=<deployment-label> -n <namespace>
```

清理这些工件可以防止过时的配置和存储声明在集群中残留。定期审计和删除孤立资源可以保持集群的整洁并优化资源使用。

## 背后的原理是什么？

当你删除或缩减 Deployment 时，Kubernetes 不会简单地删除资源，而是会协调一系列清理和关闭流程，以保持集群的完整性并防止资源泄漏。以下是它的工作原理。

### 控制器垃圾回收

Kubernetes 使用垃圾回收控制器来删除依赖资源，当它们的拥有对象被删除时，类似于图书馆系统在用户帐户关闭时自动撤回借阅的书籍。

每个资源都带有一个 ownerReference，将其与其父对象联系起来，因此当你删除 Deployment 时，它的 ReplicaSet 和 Pod 就会变成“孤儿”，然后垃圾回收器会对其进行垃圾回收。

你可以选择：

- 前台级联删除，Kubernetes 首先删除所有依赖项，然后才删除父项
- 后台级联删除，父项立即消失，依赖项异步清理

### 优雅终止和 Finalizers

当你删除 Pod 时，Kubernetes 会通过设置 .metadata.deletionTimestamp 将其标记为终止。

在此终止期间：

- kubelet 向容器的主进程发送 SIGTERM 信号，并运行任何配置的 preStop 钩子，让你的应用程序有机会关闭连接和刷新缓冲区。
- 如果[容器](https://thenewstack.io/containers/)未在 terminationGracePeriodSeconds 内终止，Kubernetes 会升级到 SIGKILL，强制关闭以避免无限期挂起。

只有在删除所有 finalizers 后，Kubernetes 才会完成删除，从而保证卸载依赖卷、通知外部系统以及执行任何操作员定义的清理逻辑。

## 删除 Deployment 时的挑战（以及修复方法）

以下是删除 Deployment 时最常遇到的问题，以及具体的补救措施，可让你在不影响维护窗口的情况下摆脱困境。

### 1. 无法退出的终止 Pod

有时，你发出删除或缩减命令，但 Pod 仍停留在 Terminating 状态。可以把它想象成客人在你宣布结束时间后拒绝离开派对。

常见原因和修复方法包括：

- **残留的 finalizers**：等待清理钩子的 Pod 将无法完成终止，直到删除 finalizers 或其控制器完成工作。
- **卡住的卷挂载**：如果 PVC 或 CSI 驱动程序挂起，Kubernetes 无法卸载和终止 Pod。在节点上重新启动 kubelet 通常可以释放挂载。
- **失败的活跃度/就绪度探测**：配置错误的健康检查可能会阻止正常关闭。验证你的探测 URL 和超时。
- **强制删除**：作为最后的手段，使用`kubectl delete pod <name> --grace-period=0 --force`立即发送 SIGKILL。
- **使用 Runbook 进行调查**：在升级之前，请按照结构化步骤操作，例如检查 finalizers、检查节点连接或重新启动 kubelet。

### 2. 卡住的 Finalizers 阻止删除

Finalizers 就像 Kubernetes 对象上的“在完成清理之前不要拆除”标签。如果控制器未能删除它们，资源将永远保持在 Terminating 状态。你通常会在[命名空间](https://thenewstack.io/what-are-linux-namespaces-and-how-are-they-used/)、CRD 或 PVC 上看到这种情况。

要解除阻止：

- 使用以下命令识别卡住的资源：

  `kubectl get <resource> <name> -o jsonpath='{.metadata.finalizers}'`
- 通过修补对象来编辑 finalizers：

  `kubectl patch <resource> <name> -p '{"metadata":{"finalizers":[]}}' --type=merge`
- 除非作为紧急解决方法，否则避免手动删除 finalizer - 删除 finalizer 会绕过预期的清理逻辑，这可能会损坏外部系统。
- 通过确保你的控制器正确处理其 finalizers 来防止再次发生。例如，使用在其代码中实现清理的操作员。

### 3. 孤立的持久卷

当你删除 Deployment 时，它的 PVC 和底层 PV 可能会残留，就像废弃的存储柜仍在累积租金一样。如果不加以检查，它们会浪费空间并增加成本。

要检测和删除它们：

- 列出未绑定的 PV -

  `kubectl get pv --field-selector=status.phase=Released`
  显示不再被任何 Pod 声明的 PV。
- 使用脚本或 Kor 等工具自动清理，这些工具扫描处于 Released 或 Failed 阶段的 PV，并在批准后删除它们。
- 使用标签选择器来定位特定于应用程序的卷：

  `kubectl delete pv -l app=myapp`
- 在你的监控堆栈中集成警报 - Prometheus，[Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/) - 以通知你非 Bound 状态下不断增长的 PV 计数。
- 在你的生命周期中使用钩子
[Helm chart](https://thenewstack.io/the-super-helm-chart-to-deploy-or-not-to-deploy/) 或 GitOps 流水线可在应用程序关闭时自动删除 PVC 和 PV。

## 自动化清理

对 Kubernetes 资源进行干净、自动化的关闭可以节省时间，并防止声明状态与实际集群之间出现偏差。

通过结合级联删除、修剪以及 Jobs 和 [CronJobs](https://thenewstack.io/with-automated-backups-cron-jobs-may-not-work-in-your-favor/) 的内置 TTL 机制，您可以确保未使用或过时的资源在无需手动干预的情况下消失。以下是每种方法的操作步骤。

### 使用 `--cascade` 和 `--prune` 标志

Kubernetes 提供了控制如何删除或修剪资源及其依赖项的标志。

以下是删除时 `--cascade` 提供的功能：

- 前台删除 (`--cascade=foreground`) 阻止删除父对象，直到其所有依赖项都首先被删除。
- 后台删除 (`--cascade=background`) 立即删除父对象，并让垃圾收集器异步清理依赖项。
- 使用 `kubectl delete deployment my-deploy --cascade=foreground` 来强制执行有序清理，或使用 `--cascade=background` 以从 CLI 获得更快的返回。

在修剪方面，它允许 kubectl 应用删除当前清单中不再定义的资源，使您的集群与 git 或本地配置保持同步。

要启用，请运行 `kubectl apply -f ./manifests --prune -l app=myapp`。从 Kubernetes 1.27 开始，新的基于 ApplySet 的修剪 (`--applyset`) 通过显式跟踪资源集来提高安全性和性能。

### ttlAfterFinished 和 CronJobs

Kubernetes 提供了内置功能来自动清理已完成的 Jobs，例如。

- Jobs 的 ttlSecondsAfterFinished，允许您将 `.spec.ttlSecondsAfterFinished: <seconds>` 添加到 Job 清单中，以便在计时器过期后，TTL-after-finished 控制器删除它（及其依赖项）。此功能自 v1.23 起已正式发布，并遵循 finalizers，确保安全关闭。
- CronJobs 的历史记录限制，您可以在 CronJob 规范中使用 `.spec.successfulJobsHistoryLimit` 和 `.spec.failedJobsHistoryLimit` 仅保留固定数量的旧 Job 对象。此外，将历史记录限制与 ttlSecondsAfterFinished 结合使用，可以为计划的工作负载生成全面的生命周期策略。

## 常见问题 (FAQ)

以下是关于删除 Kubernetes 中 Deployment 的最常见问题的答案。

### 我可以恢复已删除的 Deployment 吗？

Kubernetes 没有为 kubectl delete deployment 提供原生的“撤消”功能。一旦您删除了 Deployment，其对象和历史记录将从 etcd 中删除。要恢复，您必须重新应用原始清单或来自版本控制的 Helm chart，或者从删除之前拍摄的 etcd 或 Velero 备份中恢复。

### 删除会删除相关的 PVC 吗？

默认情况下，删除 Deployment 不会删除其 PersistentVolumeClaims (PVC) 或底层 PersistentVolumes (PV)。PVC 是单独的 API 对象，必须显式删除，例如 `kubectl delete pvc <name>`，如果您想释放存储空间。

### 哪个更好：删除 vs. 暂停/停止？

删除 (`kubectl delete deployment`) 永久删除 Deployment 对象、其 ReplicaSets、Pods 和元数据。将其用于完全关闭。暂停 (`kubectl rollout pause deployment/<name>`) 停止 Deployment 的控制器协调，但保持 Deployment、ReplicaSets 和 Pods 不变。它非常适合批量更新或维护。

## 如何在 Kubernetes 中删除 Deployment：结论

在 Kubernetes 中删除 Deployment 不仅仅是发出删除命令。它还包括为您的用例选择正确的方法，确保您拥有必要的工具和权限，并了解在幕后运行的清理过程。无论您选择缩减还是彻底删除，分步删除指南都有助于您避免孤立资源并保持集群卫生。

使用 `--cascade` 和 `--prune` 等标志自动化清理，并利用 ttlSecondsAfterFinished 等 Jobs 功能，确保您的集群与您声明的状态保持同步，而无需手动干预。通过应用这些最佳实践，您可以保持 Kubernetes 环境的精简、可靠，并为下一个工作负载做好准备。

了解[如何从头开始构建 Kubernetes Operator](https://thenewstack.io/how-to-build-a-kubernetes-operator-from-scratch/)，以自动化复杂的应用程序生命周期任务。