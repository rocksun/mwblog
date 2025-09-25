<!--
title: 十大Kubernetes部署错误：成因、解决与避坑秘籍
cover: https://cdn.thenewstack.io/media/2025/09/e4e5b71b-kubernetes.png
summary: Kubernetes 部署错误常见，多因配置或资源。文章详解 10 常见错误与故障排除，并强调自动化、资源限制及可观测性，旨在预防问题。
-->

Kubernetes 部署错误常见，多因配置或资源。文章详解 10 常见错误与故障排除，并强调自动化、资源限制及可观测性，旨在预防问题。

> 译自：[Top 10 Kubernetes Deployment Errors: Causes and Fixes (And Tips)](https://thenewstack.io/top-10-kubernetes-deployment-errors-causes-and-fixes-and-tips/)
> 
> 作者：Sunny Yadav

当您的 [Kubernetes](https://thenewstack.io/kubernetes/) 部署失败时，可能会感觉像大海捞针。一个小小的错误——一个字段缺失、镜像名称拼写错误或内存不足——都可能使一切停滞。您可能会惊讶地发现，配置错误是高达 80% 的 Kubernetes 安全和稳定性问题的根本原因。

了解 Kubernetes 部署错误发生的原因以及如何准确地排除故障。无论您是处理 CrashLoopBackOff、卡住的 Pod 还是 YAML 问题，我们都将深入探讨 10 个常见问题，并提供简单的方法来在未来预防它们。

## **接下来**

* Kubernetes 部署错误为何发生：3 个主要原因
* 10 大 Kubernetes 部署错误及其故障排除方法
* 通用故障排除框架
* 预防未来错误的专业技巧
* 总结：在 Kubernetes 部署问题发生前做好准备

## **Kubernetes 部署错误为何发生：3 个主要原因**

Kubernetes 帮助您在[容器](https://thenewstack.io/introduction-to-containers/)中运行应用程序，但即使是设置中的小错误也可能导致大问题。大多数问题发生是因为配置不正确或您的集群没有足够的资源。让我们看看部署失败的几个常见原因。

### **声明式配置出错**

Kubernetes 使用 [YAML 文件](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)来定义您的应用程序应有的样子。这被称为声明式配置。但如果该文件中有哪怕一个小错误——例如拼写错误、错误的缩进或字段缺失——您的应用程序将无法正确部署。

此外，有时文件是有效的 YAML 但对 Kubernetes 无效。例如，您可能忘记设置副本数量或指向尚不存在的服务。这些小错误可能难以发现，但一旦发现就容易修复。

### **镜像和资源限制**

您的容器镜像就是 Kubernetes 运行的应用程序。如果镜像名称错误或镜像未推送到注册表，Kubernetes 就无法拉取它，您的应用程序也无法启动。另一个常见问题是没有为您的 [Pod](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/) 设置足够的 CPU 或内存。如果 Pod 请求的资源多于可用资源，Kubernetes 可能会延迟它或使其处于“Pending”状态。

### **节点和集群级别问题**

有时问题不在于您的应用程序——而在于集群本身。如果节点已满、离线或出现问题，您的应用程序可能没有地方运行。集群的网络或存储设置也可能存在问题。例如，Pod 可能无法连接到其他服务，或者如果存储不可用，它可能会崩溃。

## **10 大 Kubernetes 部署错误及其故障排除方法**

当 [Kubernetes 部署](https://thenewstack.io/a-look-at-kubernetes-deployment/)出现问题时，一开始可能会感到困惑。但许多错误是常见的，并且有明确的原因。以下是您可能会遇到的 10 个最常见的错误以及如何修复它们。

### **1. CrashLoopBackOff**

此错误意味着 Pod 启动后立即崩溃，然后反复尝试重新启动。这通常发生在容器内的应用程序启动后立即失败时。

**故障排除方法：**

*   运行 *kubectl logs <pod-name>* 查看应用程序崩溃的原因。
*   检查您的启动命令或环境变量。
*   确保任何所需的文件、服务或依赖项都可用。

### **2. ImagePullBackOff / ErrImagePull**

当 Kubernetes 无法下载您的容器镜像时，会显示这些错误。这可能是因为镜像名称错误、注册表需要登录或镜像不存在。

**故障排除方法：**

*   检查 YAML 文件中的镜像名称和标签。
*   确保镜像已推送到容器注册表。
*   如果是私有注册表，请添加有效的镜像拉取密钥。

### **3. OOMKilled**

OOM 代表内存不足（out of memory）。此错误意味着您的容器使用的内存超出允许范围，并被系统终止。

**故障排除方法：**

*   增加部署文件中的内存限制。
*   优化您的应用程序以减少内存使用。
*   使用 *kubectl describe pod <pod-name>* 检查内存限制和使用情况。

### **4. CreateContainerConfigError**

此错误意味着 Pod 设置中的某些内容有误。这可能是一个错误的 Secret、ConfigMap 或 Volume。

**故障排除方法：**

*   使用 *kubectl describe pod <pod-name>* 查看详细错误消息。
*   检查 Secret、ConfigMap 或 Volume 是否在 [YAML](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) 中被引用。
*   确保路径和键是正确的。

### **5. NodeNotReady**

此错误意味着集群中的节点不可用于运行 Pod。它可能已关闭或断开连接。

**故障排除方法：**

*   使用 *kubectl get nodes* 检查节点状态。
*   查看 *kubectl describe node <node-name>* 获取更多信息。
*   根据问题重启或修复节点。

### **6. Pod Stuck in Pending**

处于“Pending”状态的 Pod 尚未启动。这通常意味着资源不足（CPU 或内存）或卷不可用。

**故障排除方法：**

*   运行 *kubectl describe pod <pod-name>* 找出它处于 Pending 状态的原因。
*   检查您的集群是否有足够的可用资源。
*   确保存储卷或节点选择器是正确的。

### **7. FailedScheduling**

此错误意味着 Kubernetes 找不到符合您的 Pod 要求的节点。这通常与资源限制或调度规则有关。

**故障排除方法：**

*   使用 *kubectl describe pod <pod-name>* 查看调度详情。
*   减少 Pod 规格中的 CPU 或内存请求。
*   检查您是否使用了可能阻止调度的任何节点选择器或污点。

### **8. ContainerCannotRun**

这意味着容器根本未能启动。这可能是因为入口点命令错误或容器没有所需的权限。

**故障排除方法：**

*   使用 *kubectl logs <pod-name>* 或 describe pod 查看错误。
*   确保 YAML 中的命令和参数是正确的。
*   检查是否存在文件缺失、权限损坏或所需的访问权限。

### **9. Exit Code 1 / 125**

这些退出代码表示您的应用程序在启动后立即失败。代码 1 通常表示一般错误。代码 125 可能意味着容器命令在应用程序运行之前就失败了。

**故障排除方法：**

*   使用 *kubectl logs <pod-name>* 查看错误输出。
*   仔细检查您的入口命令、环境变量和依赖项。
*   尝试使用 docker run 在本地运行镜像进行测试。

### **10. Pods in Init / Waiting Loop**

有时 Pod 会长时间停留在“Init”或“Waiting”状态。这发生在 Init 容器或主容器无法正常启动时。

**故障排除方法：**

*   使用 *kubectl describe pod <pod-name>* 检查是什么阻碍了进程。
*   确保 Init 容器成功完成。
*   检查镜像名称、卷挂载和启动脚本。

## **通用故障排除框架**

当 Kubernetes 出现问题时，遵循按部就班的方法会有所帮助。不要猜测，而是使用 Kubernetes 内置的工具来找出发生了什么。

这是一个简单的框架，可以指导您进行故障排除：

| 步骤 | 作用 | 工具或命令 |
| --- | --- | --- |
| **kubectl describe** | 查看 Pod 状态、事件和错误消息 | *kubectl describe pod <pod-name>* |
| **检查事件和日志** | 了解 Kubernetes 的行为和应用程序行为 | *kubectl get events, kubectl logs* |
| **试运行 (Dry run)** | 在 YAML 错误影响*集群*之前捕获它们 | *kubectl apply –dry-run=client* |
| **资源监控** | 识别内存/CPU 问题 | *kubectl top pod* 或仪表板工具 |
| **健康探针** | 确保应用程序正常运行并准备好接收流量 | YAML 中的存活探针和就绪探针 |

### 从 `kubectl describe` 开始

*kubectl describe* 命令提供了 Pod、节点或其他资源正在发生的事情的完整细分。它显示了当前状态、任何错误消息和相关事件。这应该是您获取问题线索的第一站。

### **检查事件和日志**

事件告诉您 Kubernetes 一直在尝试做什么，例如调度 Pod 或拉取镜像。日志显示您的应用程序或容器实际在做什么。使用 *kubectl get events* 获取全局视图，使用 *kubectl logs <pod-name>* 查看容器内部。

### **使用试运行 (Dry Run) 验证 YAML**

YAML 文件中的小拼写错误或错误的格式可能会导致大问题。在应用配置之前，使用 *kubectl apply –dry-run=client -f <file>.yaml* 来检查您的配置。这有助于在不更改集群任何内容的情况下尽早发现错误。

### **监控资源使用情况**

使用 *kubectl top* 或指标仪表板等工具检查您的 Pod 正在使用的 [CPU 和内存](https://thenewstack.io/how-to-choose-the-right-cloud-cpu-for-your-workload/)量。如果 Pod 没有足够的资源——或者请求过多——它们可能会崩溃、卡住或被系统终止。

### **使用探针和健康检查**

存活探针和就绪探针帮助 Kubernetes 了解您的应用程序何时健康并准备好提供流量。如果这些探针缺失或设置不正确，Pod 可能会频繁重启或在准备好之前接收流量。添加适当的健康检查使您的应用程序更稳定。

## **预防未来错误的专业技巧**

一旦您修复了常见的 Kubernetes 问题，下一步就是阻止它们再次发生。一些聪明习惯对于保持部署顺畅无忧大有裨益。

### **自动化静态分析和验证**

在部署之前，使用工具检查您的 YAML 文件是否存在错误。静态分析器可以捕获缺失的字段、错误的格式或无效的值。在您的 [CI/CD 流水线](https://thenewstack.io/kubernetes-ci-cd-pipelines-explained/)中自动化此步骤有助于您在问题影响生产之前尽早发现它们。

**YAML 静态分析和验证的有用工具：**

*   Kubeval
*   kube-linter
*   Datree
*   kubectl –dry-run

### **明智地使用资源请求和限制**

始终为您的容器设置 CPU 和内存请求和限制。这有助于 Kubernetes 正确调度您的 Pod，并保护您的集群免受单个 Pod 使用过多资源的影响。但不要猜测——从小处着手，并根据实际使用情况进行调整。

**设置资源请求和限制的技巧：**

*   从小的默认值开始（例如，100m CPU，128Mi 内存），并监控使用情况。
*   使用 *kubectl top pod* 或指标仪表板查看实际资源消耗。
*   设置请求（最低需求）和限制（最大允许）。
*   避免将限制设置得过低，因为它可能导致您的应用程序崩溃或重启。

### **实施可观测性工具**

添加工具，让您实时查看集群中发生的事情。仪表板和监控解决方案可以帮助您更快地发现问题，并更容易理解整体性能。

**Kubernetes 流行的可观测性工具：**

*   [Prometheus](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/) + Grafana
*   Kube-state-metrics
*   用于日志聚合的 Loki
*   用于追踪的 Jaeger
*   Datadog、[New Relic](https://thenewstack.io/new-relics-intelligent-observability-platform-is-ambitious/) 或 Dynatrace 用于一体化监控

## **总结：在 Kubernetes 部署问题发生前做好准备**

Kubernetes 中的部署错误可能会拖慢您的团队，浪费资源并导致不必要的停机。这就是为什么理解常见问题——以及如何修复或预防它们——对于任何使用容器和集群的人来说都是一项非常有价值的技能。

通过使用尽早发现问题的工具、设置智能资源限制并密切关注您的环境，您可以在问题开始之前避免大多数麻烦。而当需要清理旧的或损坏的部署时，以正确的方式进行同样重要。

在我们的指南 [如何在 Kubernetes 中移除部署](https://thenewstack.io/remove-deployment-in-kubernetes/) 中了解如何安全地从集群中移除部署。

**主要资源**

- https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
- https://lumigo.io/kubernetes-troubleshooting/kubernetes-imagepullbackoff/
- https://lumigo.io/kubernetes-troubleshooting/kubernetes-oomkilled-error-how-to-fix-and-tips-for-preventing-it/
- https://sysdig.com/blog/kubernetes-createcontainerconfigerror-createcontainererror/
- https://lumigo.io/kubernetes-troubleshooting/kubernetes-node-not-ready-error-and-how-to-fix-it/
- https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/
- https://www.kubernet.dev/resolving-kubernetes-failedscheduling-errors-a-comprehensive-guide/
- https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/
- https://komodor.com/learn/exit-codes-in-containers-and-kubernetes-the-complete-guide/
- https://kubernetes.io/docs/tasks/debug/debug-application/debug-init-containers/