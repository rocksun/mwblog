<!--
title: 开始Kubernetes的10个最佳实践
cover: ./cover.png
-->

Kubernetes已成为容器编排的事实标准，为部署、管理和扩展容器化应用程序提供了强大的平台。作为开发人员，理解Kubernetes最佳实践对于确保平稳的部署、高效的运维和增强的安全性至关重要。在本博文中，我们将探讨15个每个开发人员都应该了解的Kubernetes最佳实践，以及代码片段和YAML示例。

> 译自 [10 Kubernetes Best Practices to Get You Started](https://collabnix.com/10-kubernetes-best-practices-to-get-you-started/)，作者 Karan Singh 。

## 1. 使用Kubernetes原生资源

Kubernetes提供了丰富的原生资源，如Pod、Deployment、Service和Volume，用于管理容器化应用程序。重要的是要使用这些原生资源，而不是创建自定义脚本或变通方法。原生资源旨在与Kubernetes无缝配合，提供更好的可管理性、可扩展性和安全性。

例如，这是一个简单Pod定义的YAML示例：

```yaml
apiVersion: v1 
kind: Pod 
metadata: 
  name: my-pod 
spec: 
  containers: 
  - name: my-container 
    image: my-image:tag 
    ports: 
    - containerPort: 80
```

## 2. 遵循单一职责原则

每个容器化应用程序都应该有一个单一的责任，这意味着它应该只执行一个任务或功能。避免将多个服务或应用程序捆绑到单个容器中，因为这会使管理和扩展变得更加复杂。相反，为应用程序的每个组件使用单独的容器或Pod。

以下是一个多容器应用程序的Pod定义示例，其中有专门的前端和后端容器：

```yaml
apiVersion: v1 
kind: Pod 
metadata: 
  name: my-app 
spec: 
  containers: 
  - name: frontend 
    image: frontend-image:tag 
    ports: 
    - containerPort: 80 
  - name: backend 
    image: backend-image:tag 
    ports: 
    - containerPort: 8080
```

## 3. 定义资源限制和请求

资源限制和请求允许您为容器分配适当数量的资源，防止资源争用并确保最佳性能。根据应用程序的需求和集群中可用的资源来定义资源限制和请求。

以下是一个具有资源限制和请求的Pod定义示例：

```yaml
apiVersion: v1 
kind: Pod 
metadata: 
  name: my-pod 
spec: 
  containers: 
  - name: my-container 
    image: my-image:tag 
    resources: 
      limits: 
        cpu: "1" 
        memory: "1Gi" 
      requests: 
        cpu: "0.5" 
        memory: "500Mi"
```

## 4. 使用标签（Label）和注释（Annotation）

标签和注释允许您将元数据附加到您的Kubernetes对象上，提供了一种组织、过滤和管理资源的方式。使用标签为您的资源添加有意义的信息，例如应用程序名称、环境、版本等。使用注释添加额外的信息，例如配置细节或文档链接。

以下是一个带有标签和注释的Pod定义示例：

```yaml
apiVersion: v1 
kind: Pod 
metadata: 
  name: my-pod 
  labels: 
    app: my-app 
    environment: production 
  annotations: 
    config: "https://my-config.com" 
spec: 
  containers: 
  - name: my-container 
    image: my-image:tag
```

## 5. 使用ReplicaSets或Deployments实现可扩展性

为了确保高可用性和可扩展性，应使用ReplicaSets或Deployments来替代直接创建Pods。ReplicaSets和Deployments允许您为应用程序定义所需的副本数量，并根据需求自动进行水平扩展或缩减。

以下是用于扩展应用程序的Deployment定义示例：

```yaml
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  name: my-deployment 
spec: 
  replicas: 3 
  selector: 
    matchLabels: 
      app: my-app 
  template: 
    metadata: 
      labels: 
        app: my-app 
    spec: 
      containers: 
      - name: my-container 
        image: my-image:tag 
        ports: 
        - containerPort: 80
```

## 6. 使用命名空间进行资源隔离

命名空间允许您在集群内创建逻辑分区，提供资源隔离和访问控制。使用命名空间根据项目、团队或环境对资源进行分组，并避免将默认命名空间用于您的应用程序。这有助于防止资源名称冲突，并提供更好的组织和安全性。

以下是一个带有命名空间的Pod定义示例：

```yaml
apiVersion: v1 
kind: Pod 
metadata: 
  name: my-pod 
  namespace: my-namespace 
spec: 
  containers: 
  - name: my-container 
    image: my-image:tag 
    ports: 
    - containerPort: 80
```

## 7. 使用RBAC进行访问控制

基于角色的访问控制（RBAC）允许您为Kubernetes集群内的用户和组定义细粒度的访问控制规则。使用RBAC限制对敏感资源和操作的访问，并仅向用户和组授予必要的权限。避免将默认的cluster-admin角色用于普通用户或服务，以减少未经授权的访问风险。

以下是一个RBAC角色定义示例：

```yaml
apiVersion: rbac.authorization.k8s.io/v1 
kind: Role 
metadata: 
  name: my-role 
rules: 
- apiGroups: [""] 
  resources: ["pods"] 
  verbs: ["get", "list", "create", "update", "delete"]
```

## 8. 使用Secrets存储敏感数据

避免在容器镜像或Kubernetes清单中以明文形式存储敏感数据，例如密码、API密钥或证书。相反，使用Kubernetes Secrets安全地存储敏感数据，并在应用程序清单中引用它们。Secrets已加密，并可独立管理，提供了一种更安全的处理敏感数据的方式。

以下是一个秘密定义的示例：

```yaml
apiVersion: v1 
kind: Secret 
metadata: 
  name: my-secret 
type: Opaque 
data: 
  username: dXNlcm5hbWU= 
  password: cGFzc3dvcmQ=
```

## 9. 使用健康检查

健康检查允许您确保您的容器正常运行并准备好提供流量服务。使用就绪探针检查您的容器是否准备好接收流量，并使用存活探针检查您的容器是否仍然正确运行。正确使用健康检查有助于Kubernetes检测和从故障中恢复，确保您的应用程序具有高可用性。

以下是一个带有健康检查的Pod定义示例：

```yaml
apiVersion: v1 
kind: Pod 
metadata: 
  name: my-pod 
spec: 
  containers: 
  - name: my-container 
    image: my-image:tag 
    ports: 
    - containerPort: 80 
    readinessProbe: 
      httpGet: 
        path: /health 
        port: 80 
      initialDelaySeconds: 5 
      periodSeconds: 10 
    livenessProbe: 
      httpGet: 
        path: /health 
        port: 80 
      initialDelaySeconds: 10 
      periodSeconds: 30
```

## 10. 使用滚动更新进行部署

在更新应用程序时，使用部署的滚动更新来确保零停机和平稳更新。滚动更新允许您逐渐更新您的应用程序，一次一个副本，同时保持所需数量的副本始终运行。这有助于最小化中断，并确保您的应用程序在更新期间保持可用。

以下是一个具有滚动更新的部署定义示例：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: my-image:tag
        ports:
        - containerPort: 80
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
```

## 12. 使用持久卷和持久卷声明

使用持久卷（PV）和持久卷声明（PVC）在集群中持久存储数据。PV 是代表物理存储资源的集群范围资源，而 PVC 用于从 PV 请求特定量的存储。通过使用 PV 和 PVC，即使容器或 pod 被重新调度到不同的节点，也可以确保应用程序数据得到保留。

以下是持久卷声明的示例定义：

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

## 13. 使用标签和注解进行元数据管理

使用标签和注解将元数据附加到 Kubernetes 对象，例如 pod、服务和卷。标签用于标识和过滤对象，而注解用于向对象附加任意元数据。使用标签和注解为您的对象提供有意义的元数据，例如应用程序名称、版本号或环境名称，有助于过滤、查询和调试。

以下是带有标签和注解的 pod 定义示例：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: my-app
  annotations:
    version: v1.0.0
spec:
  containers:
  - name: my-container
    image: my-image:tag
    ports:
    - containerPort: 80
```

## 14. 监控和观察您的集群

监控和观察您的 Kubernetes 集群对于确保应用程序的健康和性能至关重要。使用诸如 Prometheus、Grafana 或 Kubernetes 本地监控解决方案（如 Kubernetes Metrics Server）之类的工具来收集和分析集群的指标，例如 CPU 使用情况、内存使用情况和网络流量。设置警报和通知以主动监视您的集群，并在出现任何问题时及时接收通知。

以下是使用 Prometheus 和 Grafana 监控您的集群的示例：

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: my-service-monitor
spec:
  selector:
    matchLabels:
      app: my-app
  endpoints:
  - port: metrics
    path: /metrics
    interval: 30s
```

## 15. 使用 RBAC 进行访问控制

实施基于角色的访问控制（RBAC）以控制对您的 Kubernetes 资源的访问，并确保只有授权用户具有对集群执行操作的权限。使用 ClusterRoles 和 ClusterRoleBindings 定义角色和绑定，授予特定用户、组或服务帐户特定的权限。限制过度宽松的角色使用，并遵循最小权限原则以最小化安全风险。

以下是 ClusterRole 和 ClusterRoleBinding 定义示例：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: my-cluster-role
rules:
- apiGroups: ["", "extensions", "apps"]
  resources: ["pods", "deployments"]
  verbs: ["get", "list", "watch", "create", "update", "delete"]
- apiGroups: [""]
  resources: ["services"]
  verbs: ["get", "list", "watch"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-cluster-role-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: my-cluster-role
subjects:
- kind: User
  name: john.doe
  apiGroup: rbac.authorization.k8s.io
```

## 结论

Kubernetes 是一个强大且复杂的容器编排平台，需要正确配置和管理才能确保应用程序的顺利运行。通过遵循这 15 条 Kubernetes 最佳实践，您可以优化 Kubernetes 集群的性能、可靠性和安全性，并简化应用程序的部署和管理流程。

请记住始终遵循 Kubernetes 文档，并及时了解最新的最佳实践和安全建议。定期审查和审核您的 Kubernetes 配置，以识别和解决任何潜在的安全风险或性能瓶颈。此外，利用监控和可观察性工具主动监视您的集群，并迅速响应可能出现的任何问题。

通过遵循这些最佳实践，您可以确保您的 Kubernetes 部署在生产环境中高效、可靠和安全，并且您的应用程序能够顺利运行。祝您在 Kubernetes 编码中顺利愉快！
