<!--
title: 13个鲜为人知的Kubernetes技巧
cover: ./cover.png
-->

Kubernetes 具备完整的生态系统，提供了许多功能，可以显著增强容器化应用程序的管理、可伸缩性和安全性。以下是 13 个技巧，每个都详细说明了技巧解释、使用示例、上下文应用以及注意事项。

> 译自 [13 Kubernetes Tricks You Didn’t Know](https://overcast.blog/13-kubernetes-tricks-you-didnt-know-647de6364472)，作者 DavidW (skyDragon)。

## 1. 使用 PreStop 钩子优雅地关闭 Pod

技巧：PreStop 钩子允许在 Pod 即将终止时在其内部执行特定命令或脚本。这种能力对于确保应用程序优雅地关闭非常关键，可以在必要时保存状态，或执行清理任务以避免数据损坏，并确保平滑重启。

使用示例：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: graceful-shutdown-example
spec:
  containers:
  - name: sample-container
    image: nginx
    lifecycle:
      preStop:
        exec:
          command: ["/bin/sh", "-c", "sleep 30 && nginx -s quit"]
```

这个配置确保 nginx 服务器在关闭之前有 30 秒的时间来完成正在服务的当前请求。

何时使用：在对服务连续性至关重要的环境中实施 PreStop 钩子，以确保在部署、扩展或 Pod 重启期间零或最小的停机时间。

注意事项：Kubernetes 允许 Pod 的终止优雅期。如果 PreStop 钩子脚本执行时间超过这个优雅期，Kubernetes 将强制终止 Pod，可能导致你试图避免的问题。

## 2. 使用 Kubelet 实现自动密钥轮换

技巧：Kubernetes 支持在不重启消耗这些密钥的 Pod 的情况下自动轮换密钥。这个功能对于通过定期更改敏感信息而不影响应用程序可用性来维护安全标准特别有用。

使用示例：假设你在 Kubernetes 中更新了一个密钥。Kubernetes 将在不需要任何干预的情况下更新 Pod 中挂载的密钥，确保应用程序始终具有最新的凭据，而无需手动更新或重新启动。

何时使用：对于需要高水平安全合规性的应用程序，如数据库密码、API 密钥或 TLS 证书等需要频繁进行密钥轮换的情况，此功能是不可或缺的。

注意事项：应用程序必须设计为动态读取更新后的密钥。一些应用程序在启动时缓存密钥，这意味着它们不会识别到更新后的密钥而不重新启动。确保你的应用程序定期检查密钥更新或适当地对变化做出反应。

## 3. 使用短暂容器调试 Pods

巧技：短暂容器提供了一种在运行中的 Pod 上临时附加调试容器的方式，而不改变其原始规范。这对于在生产环境中调试实时问题非常有帮助，因为你不能扰乱服务。

使用示例：

```shell
kubectl alpha debug -it podname --image=busybox --target=containername
```

此命令向现有的 Pod 中添加一个 busybox 容器，允许你执行命令并检查 Pod 的环境，而不改变其运行状态。

何时使用：在诊断实时环境中的问题时，特别是当标准日志和指标提供的信息不足时，请使用短暂容器。这是实时深入分析生产问题的强大工具。

注意事项：由于短暂容器可以访问 Pod 的资源和敏感数据，请谨慎使用，特别是在生产环境中。确保只有授权人员能够部署短暂容器，以避免潜在的安全风险。

## 4. 基于自定义指标的水平 Pod 自动缩放

技巧：水平 Pod 自动缩放器（HPA）可以根据自定义指标扩展你的部署，而不仅仅是标准的 CPU 和内存使用情况。这对于需要根据特定业务指标或性能指标进行扩展的应用程序特别有用，比如队列长度、请求延迟或自定义应用程序指标。

使用示例：

```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: custom-metric-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: your-application
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Pods
    pods:
      metric:
        name: your_custom_metric
      target:
        type: AverageValue
        averageValue: 10
```

此 HPA 配置根据自定义指标 your_custom_metric 的平均值调整你的应用程序的规模。

何时使用：对于传统的基于资源的指标无法准确表示负载的应用程序，或者需要根据业务需求进行精细调整的情况，请使用自定义指标扩展。

注意事项：设置自定义指标涉及与支持自定义指标的指标服务器（如 Prometheus）集成。确保你的指标是负载的可靠指标，以防止过度或不足缩放。

## 5. 使用初始化容器进行设置脚本

技巧：初始化容器在 Pod 中的应用容器之前运行，非常适合需要在应用程序启动之前完成的设置脚本。这可能包括数据库迁移、配置文件创建或等待外部服务可用等任务。初始化容器可以运行一系列设置任务，确保每个步骤在主应用程序容器启动之前都成功完成。

使用示例：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
  - name: myapp-container
    image: myapp
  initContainers:
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'until nslookup myservice; do echo waiting for myservice; sleep 2; done;']
```

此示例使用初始化容器在启动主应用程序容器之前等待名为 myservice 的服务可用。

何时使用：当你的应用程序容器依赖于外部服务或配置在它们启动之前可用时，初始化容器是非常宝贵的。它们确保你的应用程序在环境准备就绪的情况下启动。

注意事项：直到所有初始化容器成功完成，整个 Pod 的启动才会被阻塞。确保初始化容器高效并且能够优雅地处理失败，以防止它们成为瓶颈或导致 Pod 启动失败。

## 6. 用于工作负载特定调度的节点亲和性

技巧：节点亲和性允许你指定规则，限制 Pod 可以被调度到哪些节点上，基于节点上的标签。这对于将工作负载定向到具有特定硬件（如 GPU）、确保数据本地性，或符合合规性和数据主权要求非常有用。

使用示例：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: with-node-affinity
spec:
  containers:
  - name: with-node-affinity
    image: nginx
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
```

这个 Pod 只会被调度到带有标签 disktype=ssd 的节点上。

何时使用：当你的应用程序需要特定节点能力时，或者需要控制工作负载的分布以进行性能优化、法律或监管原因时，请使用节点亲和性。

注意事项：过度使用节点亲和性可能导致集群利用率低下和调度复杂性增加。确保你的集群具有平衡的标签和亲和性分布，以维持资源利用的高效性。

## 7. 用于 Pod 隔离的污点和容忍度

技巧：污点和容忍度共同确保 Pod 不会被调度到不合适的节点上。节点上的污点会排斥不容忍该污点的 Pod。容忍度应用于 Pod，允许它们在被污点的节点上调度。这个机制对于将节点专门用于特定工作负载非常重要，比如 GPU 密集型应用程序，或确保只有特定的 Pod 在带有敏感数据的节点上运行。

使用示例：

```shell
# 对节点应用污点
kubectl taint nodes node1 key=value:NoSchedule

# 具有容忍度的 Pod 规范
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: nginx
  tolerations:
  - key: "key"
    operator: "Equal"
    value: "value"
    effect: "NoSchedule"
```

这个设置确保 mypod 可以被调度到具有特定污点的 node1 上，其他 Pod 无法容忍该污点。

何时使用：在多租户集群中，污点和容忍度特别有用，对于安全性或性能原因，隔离工作负载至关重要。它们也有利于运行需要专用资源的专业工作负载。

注意事项：配置污点和容忍度时要小心，可能会导致调度问题，例如未按预期调度 Pod 或某些节点被闲置。定期审查你的污点和容忍度设置，确保其符合调度需求。

## 8. 用于关键工作负载的 Pod 优先级和抢占

技巧：Kubernetes 允许你为 Pod 分配优先级，较高优先级的 Pod 可以在必要时抢占（驱逐）较低优先级的 Pod。这确保了关键工作负载即使在高度拥挤的集群中也能获得所需的资源。

使用示例：

```yaml
# PriorityClass definition
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "This priority class should be used for XYZ service pods only."

# Pod specification with priorityClassName
apiVersion: v1
kind: Pod
metadata:
  name: high-priority-pod
spec:
  containers:
  - name: high-priority
    image: nginx
  priorityClassName: high-priority
```

这个配置定义了一个高优先级类，并将其分配给一个 Pod，确保它可以抢占其他较低优先级的 Pod。

何时使用：在对你的业务操作至关重要的应用程序中使用 Pod 优先级和抢占，特别是在资源争用普遍的集群中运行时。

注意事项：不当使用可能会导致较不关键应用程序资源匮乏。平衡不同工作负载的需求，并考虑对集群健康和应用程序性能的整体影响。

## 9. 用于动态配置的 ConfigMaps 和 Secrets

技巧：ConfigMaps 和 Secrets 提供了将配置数据注入到 Pod 中的机制。这样可以将配置外部化，使得应用程序更容易配置，无需硬编码配置数据。ConfigMaps 适用于非敏感数据，而 Secrets 则用于敏感数据。

使用示例：

```yaml
# ConfigMap Example
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  config.json: |
    {
      "key": "value",
      "databaseURL": "http://mydatabase.example.com"
    }
```

```yaml
# Pod Spec using ConfigMap
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: myapp-container
      image: myapp
      volumeMounts:
      - name: config-volume
        mountPath: /etc/config
  volumes:
    - name: config-volume
      configMap:
        name: app-config
```

这个配置将 app-config 的内容注入到 Pod 中，使得应用程序可以从 /etc/config/config.json 读取其配置。

何时使用：每当你需要将应用程序的配置或机密数据外部化时，使其更容易管理、更新和维护，而无需重新构建容器镜像时。

注意事项：虽然 ConfigMaps 适用于存储非敏感数据，但避免将其用于任何需要保密的数据。始终使用 Secrets 存储密码、令牌、密钥和其他敏感数据，并注意保护 Secrets 的最佳实践，例如在静态环境中对其进行加密。

## 10. 用于直接容器调试的 Kubectl Debug

技巧：kubectl debug 提供了一种创建临时副本 Pod 并替换其容器为调试版本或添加新的故障排除工具的方式，而不会影响原始 Pod。这在不影响应用程序运行状态的情况下，在实时环境中调试问题非常有用。

使用示例：

```bash
kubectl debug pod/myapp-pod -it --copy-to=myapp-debug --container=myapp-container --image=busybox
```

这个命令创建了 myapp-pod 的副本，并将 myapp-container 替换为用于调试目的的 busybox 镜像。

何时使用：当你需要在生产环境中调试崩溃或行为不符预期的 Pod 时，这个技巧非常宝贵。它允许在最小程度影响服务的情况下进行实时调试。

注意事项：调试 Pod 仍然可能影响整体集群资源分配，并且可能访问敏感数据。确保对调试命令的访问受到严格控制，并在使用后清理调试 Pod。

## 11. 使用请求和限制进行高效资源管理

技巧：Kubernetes 允许您为 Pod 中的每个容器指定 CPU 和内存（RAM）请求和限制。请求保证容器获取指定的资源量，而限制则确保容器绝不会使用超过分配数量的资源。这有助于高效地管理资源分配并防止任何单个应用独占集群资源。

使用示例：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-demo
spec:
  containers:
  - name: demo-container
    image: nginx
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

这个 Pod 规范请求了一定数量的 CPU 和内存给 demo-container，确保它拥有所需的资源以实现最佳性能，同时防止它超出指定的限制。

何时使用：将请求和限制应用于所有容器，以确保可预测的应用程序性能，并避免集群中运行的应用程序之间的资源争用。

注意事项：将限制设置得太低可能会导致 Pod 被终止或无法调度，如果集群无法提供请求的资源。相反，将它们设置得太高可能会导致集群资源的低效利用。根据需要监视应用程序性能并调整请求和限制。

## 12. 用于扩展 Kubernetes 的自定义资源定义（CRDs）

技巧：CRDs 允许您使用自己的 API 对象扩展 Kubernetes，从而创建操作类似于本机 Kubernetes 对象的自定义资源。这对于向集群添加特定于领域的功能、促进自定义操作并与外部系统集成非常有用。

使用示例：

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
  - name: v1
    served: true
    storage: true
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
  shortNames:
  - ct
```

这个 CRD 在集群中定义了一个名为 CronTab 的新资源类型，可以像传统的 cron 作业一样用于调度任务，但具有 Kubernetes 本机管理功能。

何时使用：CRDs 是将 Kubernetes 功能扩展到满足应用程序或服务特定需求的理想选择，例如引入特定于领域的资源类型或与外部服务和 API 集成。

注意事项：设计和管理 CRD 需要对 Kubernetes 内部和 API 机制有很好的理解。设计不良的 CRD 可能会导致性能问题，并且使集群管理变得复杂。请始终确保对 CRD 进行彻底测试，并考虑对集群稳定性和性能的影响。

## 13. Kubernetes API 用于动态交互和自动化

技巧：Kubernetes API 使您能够动态地与集群进行交互，从而可以以编程方式自动化扩展、部署和管理任务。通过利用 API，您可以创建与集群实时交互的脚本或应用程序，实现复杂的自动化和集成方案，超越了静态配置文件和手动命令的可能性。

使用示例：以下是一个基本示例，使用 curl 与 Kubernetes API 交互以获取默认命名空间中 Pod 列表。这假设您拥有一个访问令牌，并且 Kubernetes API 可以在 https://<kubernetes-api-server> 上访问。

```bash
curl -X GET https://<kubernetes-api-server>/api/v1/namespaces/default/pods \
  -H "Authorization: Bearer <your-access-token>" \
  -H 'Accept: application/json'
```

对于更复杂的交互，考虑使用各种编程语言中提供的客户端库，如 Go、Python、Java，它们可以将 HTTP 请求抽象化，并提供更便捷的接口来与 Kubernetes API 进行交互。

何时使用：Kubernetes API 对于开发自定义自动化、动态扩展策略、CI/CD 集成，甚至是扩展 Kubernetes 功能的自定义控制器都非常强大。当您需要将 Kubernetes 操作与外部系统集成或创建自定义部署工作流程时，它尤其有用。

注意事项：直接与 Kubernetes API 交互需要谨慎处理身份验证和授权。确保您的脚本和应用程序遵循最小权限原则，仅请求其所需的权限。此外，在频繁或复杂的查询时要注意 API 服务器的潜在负载，因为这可能会影响集群性能。始终验证和清理 API 客户端的输入，以避免安全漏洞，特别是如果它们与外部系统或用户生成的内容进行交互。

这个技巧使开发人员和运维人员能够根据其独特的操作环境定制 Kubernetes，实现了一种可以显著提高运维效率和灵活性的自动化和集成水平。