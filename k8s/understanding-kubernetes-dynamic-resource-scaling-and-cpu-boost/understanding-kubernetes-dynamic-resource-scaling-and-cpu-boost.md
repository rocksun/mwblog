<!--
title: 更快的Kubernetes工作负载启动时间与Kube Startup CPU Boost
cover: ./cover.png
-->

当应用程序的资源需求发生变化时，在 Kubernetes 1.27 中，通过 in-place 资源调整可以调整 Pod 资源而无需重新启动容器。

> 译自 [](https://cloud.google.com/blog/products/containers-kubernetes/understanding-kubernetes-dynamic-resource-scaling-and-cpu-boost)，作者 。

尽管 Kubernetes 具有许多自动化功能，但运行容器化应用程序仍然面临一些挑战。其中之一是需要定义应用程序所需的资源。这些通常是 CPU 和内存，但也可能包括本地存储。Kubernetes 提供了一种在 [Pod 模板](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates)中为应用程序配置资源的方式。

```yaml
metadata:
  labels:
    app.kubernetes.io/name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.25.3
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```

但是，如果应用程序的资源需求随时间变化呢？一个选择是配置更大的请求以满足峰值资源需求。这不是一种最佳方法，会导致资源利用不足。它还会产生不必要的基础设施成本，因为并非所有时间都在使用。

## Java 虚拟机资源使用模式

Java 应用程序通常需要随时间而变化的不同资源。Java 是一种动态的、解释型语言，基于“一次编写，到处运行”的原则。它通过生成通用字节码而不是特定架构的机器码来实现这一点，需要 Java 虚拟机（JVM）来运行应用程序。JVM 在启动时通常需要更多的资源，而在运行时则需要更少。这是因为在初始类加载或优化时存在密集的计算操作。由于 JVM 利用了多线程，分配更多的 CPU 资源通常可以减少启动时间。

## 容器化 Java 应用程序

容器已成为在云中部署和运行应用程序的事实标准。容器平台通过设计提供可移植性，因此在容器中运行时 JVM 的可移植性并不实用。将工作负载移至云并运行容器的公司通常寻求其工作负载的弹性。在需要时动态扩展和收缩的能力也意味着支付更少的资源使用费用。容器化 JVM 应用程序的长启动时间使得利用云中容器运行时的弹性特性成为问题。

一种可能的解决方案是提前将 Java 代码编译成本地机器代码。这使得 Java 应用程序可以在没有 JVM 的情况下运行，并提供更快的启动和更好的性能。例如，GraalVM 是一个支持这种构建方式的 Java 开发工具包。然而，使用这种方法会带来其他挑战，通常需要应用程序现代化的努力。因此，如果容器平台能够根据需要动态分配计算资源，公司更愿意使用 JVM。

## Kubernetes 中的动态资源调整和 CPU Boost

Kubernetes 1.27 版引入了一项名为[ in-place resource resize](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha/) 的新功能，允许您在不重新启动容器的情况下调整 Pod 资源。为了启用此功能，Pod 容器中的资源字段现在允许对 CPU 和内存资源进行变更。该功能仍处于 alpha 阶段。

受益于 in-place resource resize 的解决方案之一是 [Kube Startup CPU Boost](https://github.com/google/kube-startup-cpu-boost)，这是一个 Kubernetes operator ，用于增加 Pod 的 CPU 资源。资源更新发生在集群将 Pod 调度到节点之前。一旦容器准备就绪，operator 将更新其资源为原始值。由于 in-place resource resize 功能，此操作不会强制 Pod 重新启动。

Kube Startup CPU Boost 是开源的。它旨在解决启动过程中需要额外资源的应用程序用例。这些用例不限于容器化的 JVM 应用程序。

安装 Kube Startup CPU Boost 可以使用以下命令完成。作为先决条件，集群需要启用 [InPlacePodVerticalScaling](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha/#how-to-use-this-feature) 功能开关。

```bash
kubectl apply -f https://github.com/google/kube-startup-cpu-boost/releases/latest/download/manifests.yaml
```

安装完成后，您可以为应用程序配置 CPU 提升。让我们首先部署一个示例 Java 应用程序，并检查其在没有提升的情况下的启动时间。为此，您可以使用具有以下特性的演示应用程序：

- 使用 Spring Boot 3 框架创建
- 在 REST 端点上公开数据
- 使用 Spring Data 和 Java Persistence API 从数据库中获取数据
- 在使用 Java 17 的容器中运行，并作为 "fat jar" 执行
- 使用 1 个核心的 CPU 请求和限制

```bash
git clone https://github.com/google/kube-startup-cpu-boost
cd kube-startup-cpu-boost/demo-app
kubectl create ns demo
kubectl kustomize | kubectl apply -f -
```

以下命令将从日志中检查 Spring 应用程序的启动时间。在我们的案例中，在具有 e2-standard4 节点的 GKE 集群上，平均为 18 秒。

```bash
kubectl logs deploy/spring-rest-jpa -n demo | grep \"Started DemoApplication\"
```

让我们重复相同的操作，但这次使用启动 CPU 提升配置。将容器 CPU 请求和限制增加 100%（到 2 个核心），直到 Pod 达到 Ready 状态。为此，请在您应用程序的命名空间中应用以下配置。

```yaml
apiVersion: autoscaling.x-k8s.io/v1alpha1
kind: StartupCPUBoost
metadata:
  name: boost-001
  namespace: demo
spec:
  selector:
    matchExpressions:
      - key: app.kubernetes.io/name
        operator: In
        values: ["spring-demo-app"]
  resourcePolicy:
    containerPolicies:
      - containerName: spring-demo-app
        percentageIncrease:
          value: 100
  durationPolicy:
    podCondition:
      type: Ready
      status: "True"
```

接下来，删除先前的部署并重新创建。

```bash
kubectl delete deploy/spring-demo-app -n demo
kubectl kustomize | kubectl apply -f -
```

这次启动 CPU 提升会增加容器的 CPU 资源。使用与之前相同的命令来检查应用程序的启动时间，我们在测试中看到了 9 秒的启动时间，大约快了两倍。

```bash
kubectl logs deploy/spring-demo-app -n demo | grep \"Started DemoApplication\"
```

在幕后发生了什么？

![](https://storage.googleapis.com/gweb-cloudblog-publish/images/01._kube-startup-cpu-boost.max-1000x1000.png)

Kube Startup CPU Boost 使用 [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks) 来增加容器资源。该 webhook 接收新 Pod 的 admission 请求。它查询 Boost Manager 组件以获取匹配的提升配置。一旦找到，它会按照配置增加 CPU 资源请求和限制。一旦 Pod 达到所需状态，管理器会将容器资源更新为其原始值 - 所有这些都不需要重新启动 Pod，这要归功于 [Kubernetes 中的 in-place POD 调整](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha/)功能。

## 注意事项和限制

管理员在规划集群容量和选择节点配置时应考虑此解决方案。如果容量不足，集群将无法调度提升的 Pod。为了实现更快的启动速度，为节点安全地腾出额外的 CPU 资源是速度和成本之间的权衡。由于 in-place 调整功能，这些资源将在短时间内可用于其他应用程序。与运行超配的 Pod 相比，这使得总体开销更小。

使用集群自动缩放器的用户在使用此解决方案时也应谨慎。不建议与积极优化利用率的自动缩放器一起使用。由于提升管理器减少了 Pod 的初始资源，自动缩放器可能会将节点视为未充分利用。这可能会触发缩减动作，并将 Pod 重新调度到不同的节点。

## 摘要

在文章中，我们描述了 Pod 和容器的 Kubernetes 资源管理。对于需要不同资源的应用程序而言，该过程可能并不理想。其中一个示例是在容器中运行的 JVM 中的 Java 应用程序，它在启动阶段需要更多的 CPU 资源，而一旦运行则需要更少。为了保证这一点，您需要以膨胀的 CPU 资源请求来运行 Pod，以满足峰值需求。但是，仅设置更高的资源限制是不够的，因为它们的可用性随时间变化。

新的 [Kubernetes in-place POD](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha/) 调整功能旨在解决这个问题，而 [Kube Startup CPU Boost](https://github.com/google/kube-startup-cpu-boost) 解决方案演示了如何利用这一新功能。这是针对在启动阶段需要额外 CPU 资源的应用程序的有针对性解决方案。一旦应用程序启动运行，CPU 资源就会减少，由于 in-place 资源调整，这个操作不会重新启动 Pod。
