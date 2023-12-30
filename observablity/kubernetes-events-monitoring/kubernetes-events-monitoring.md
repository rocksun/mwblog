<!--
title: 使用OpenTelemetry实现Kubernetes事件监控
cover: ./kubernetes-events-monitoring-cov.png
-->

在 Kubernetes 中，事件是提供对集群内状态变化洞察的对象。进行 Kubernetes 事件监控对于实时洞察 Kubernetes 集群的运行状态至关重要。它使管理员能够快速识别并响应问题，优化资源分配，并确保其容器化应用程序的平稳高效运行。

> 译自 [Kubernetes Events Monitoring with OpenTelemetry | Complete Tutorial](https://signoz.io/blog/kubernetes-events-monitoring)。作者 Dejan Lukić。

在本教程中，我们涵盖:

- 什么是 Kubernetes 事件？
- 为什么 Kubernetes 事件监控很重要？
- 使用 OpenTelemetry 收集 Kubernetes 事件
- 事件
- 对象
- 先决条件
- 设置 OpenTelemetry collector 
- 使用 Signoz 仪表板进行监控
- 结论

如果您想直接开始实施，请从[先决条件](https://signoz.io/blog/kubernetes-events-monitoring#prerequisites)部分开始。

分析 Kubernetes 集群中特定事件是可观测性的关键组成部分，为更快的问题解决提供了对集群事件之间关联的深入洞察。

这个教程将演示如何使用OpenTelemetry Collector收集Kubernetes事件并将它们转发到SigNoz。

但在此之前，让我们更深入地了解一下Kubernetes事件以及监控它们为何如此重要。

## 什么是 Kubernetes 事件？

Kubernetes 事件是提供有关集群内活动更新的通知，例如 pod 的启动或崩溃。它们提供了对变更和操作的历史视图，有助于跟踪和解决问题。

这些事件是系统就重要操作或问题进行通信的手段，对于维护 Kubernetes 设置的健康和效率至关重要。

Kubernetes 事件的类型：

- Failed事件：指示 Kubernetes 中的意外问题。
- Evicted事件：指 pods 被强制从节点中移除的情况。
- Failed Scheduling事件：发生在 Kubernetes 无法调度任务时。
- Volume事件：与 Kubernetes 中的存储问题相关。
- Node事件：指与节点相关的通知或警报。例如，节点就绪、节点故障等。

## 为什么监控 Kubernetes 事件很重要？

监控 Kubernetes 事件对于保持对集群活动的实时了解至关重要。这些事件充当详细日志，标记变更、pod 生命周期事件和错误。通过监控这些事件，您可以随时了解集群内的状态和活动。

监控 Kubernetes 事件对以下几个关键原因至关重要：

- **运维可靠性**：它实时洞察容器化应用的健康和性能，确保操作平稳。
  - 检测失败的部署和资源分配问题。
  - 通过主动解决问题降低停机时间。
- **安全与合规性**：事件监控对于识别安全漏洞并保持符合法规标准至关重要。
  - 实时检测可疑活动。
  - 生成符合法规标准的审计跟踪。
- **战略决策制定**：随时间分析事件模式有助于资源优化和扩展决策。
  - 通过预防性解决性能瓶颈来提高用户体验。
  - 促使对资源管理和扩展做出明智的决策。

## 使用 OpenTelemetry 收集 Kubernetes 事件

OpenTelemetry 是一组 API、SDK、库和集成，旨在标准化遥测数据（日志、度量和跟踪）的生成、收集和管理。它由云原生计算基金会支持，是可观测性领域的主要开源项目。

通过 OpenTelemetry 收集的数据是与供应商无关的，可以发送到您选择的任何后端。在本教程中，我们将 Kubernetes 事件发送到 [SigNoz](https://signoz.io/)，这是一个 OpenTelemetry 原生的 APM。

OpenTelemetry 充当中间人，收集有关 pod 活动、错误和资源使用的数据。这些收集到的信息帮助您了解集群内部发生了什么，从而更轻松地排除问题并保持系统平稳运行。

OpenTelemetry 提供了 OpenTelemetry Collector，可用作具有许多灵活配置的遥测处理系统，用于收集和管理遥测数据。我们将使用 OpenTelemetry Collector 来收集 Kubernetes 事件并将其发送到 SigNoz。

## OpenTelemetry Collector 如何收集数据？

receiver是数据进入 OpenTelemetry Collector 的方式。receiver通过顶层的 `receivers` 标签在 YAML 中进行配置。至少必须有一个启用的receiver，以使配置被视为有效。

以下是 otlp receiver的示例：

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:
```

OTLP receiver可以通过 gRPC 或 HTTP 使用 [OTLP](https://github.com/open-telemetry/opentelemetry-proto/blob/main/docs/specification.md) 格式接收数据。您可以通过 YAML 文件启用高级配置。

以下是 otlp receiver 的示例配置：

```yaml
receivers:
  otlp:
    protocols:
      http:
        endpoint: "localhost:4318"
        cors:
          allowed_origins:
            - http://test.com
            # Origins can have wildcards with *, use * by itself to match any origin.
            - https://*.example.com
          allowed_headers:
            - Example-Header
          max_age: 7200
```

您可以在[此处](https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/otlpreceiver/README.md)找到有关高级配置的更多详细信息。

配置receiver后，必须启用它。receiver通过服务部分内的pipeline启用。pipeline包括一组receiver、processor和exporter。

以下是一个pipeline配置示例：

```yaml
service:
  pipelines:
    metrics:
      receivers: [otlp, prometheus]
      exporters: [otlp, prometheus]
    traces:
      receivers: [otlp, jaeger]
      processors: [batch]
      exporters: [otlp, zipkin]
```

为了收集 Kubernetes 事件，OpenTelemetry Collector 提供了 [k8seventsreceiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/k8seventsreceiver)。

每个 OpenTelemetry receiver都收集其指定的一部分度量、日志和/或跟踪。在这种情况下，Kubernetes 事件receiver仅收集日志。以下是由 Kubernetes 事件receiver收集的日志，分为两组：事件和对象。

## 事件

receiver收集的事件数据：

| 度量名称 | 描述 | 度量 |
| -------- | ---- | ---- |
| 事件原因 | 事件的原因 | k8s.event.reason |
| 事件操作 | 给定的事件操作 | k8s.event.action |
| 事件开始时间 | 事件的开始时间 | k8s.event.start_time |
| 事件名称 | 事件的名称 | k8s.event.name |
| 事件唯一标识符 | 事件的唯一标识符 | k8s.event.uid |
| 事件计数 | 事件的总计数 | k8s.event.count |

## 对象

receiver收集的对象数据：

| 度量名称 | 描述 | 度量 |
| -------- | ---- | ---- |
| 对象类型 | K8s 对象的类型 | k8s.object.kind |
| 对象名称 | 对象的名称 | k8s.object.name |
| 对象唯一标识符 | 对象的唯一标识符 | k8s.object.uid |
| 对象字段路径 | 对象的字段路径 | k8s.object.fieldpath |
| 对象 API 版本 | 对象的 API 版本 | k8s.object.api_version |
| 对象资源版本 | 对象的资源版本 | k8s.object.resource_version |

## 先决条件

在开始之前，您需要：

- 一个 [SigNoz Cloud](https://signoz.io/teams/) 账户。
- 在本地安装 [kubectl](https://kubernetes.io/docs/reference/kubectl/)。
- 部署了 Kubernetes 集群。

## 设置 OpenTelemetry Collector

现在，您将使用 `k8seventsreceiver` 和一个 OTLP exporter来设置 OpenTelemetry Collector。

[了解有关 Kubernetes 和 OpenTelemetry collector ](https://signoz.io/docs/tutorial/kubernetes-infra-metrics/)的更多信息，访问 SigNoz。

### 步骤 1：使用 OTEL 选项创建配置映射

创建一个带有 `otelcontribcol` 配置的 ConfigMap。将 `<YOUR SIGNOZ REGION>` 替换为您 SigNoz 云区域的值，同时将 `<YOUR SIGNOZ ACCESS TOKEN>` 替换为仪表板中找到的令牌。

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otelcontribcol
  labels:
    app: otelcontribcol
data:
  config.yaml: |
    receivers:
      k8s_events:
        namespaces: [default, my_namespace, platform]
    exporters:
      otlp:
        endpoint: https://ingest.<YOUR SIGNOZ REGION>.signoz.cloud:443
        tls:
          insecure: false
        timeout: 20s # Adjust the timeout value as needed
        headers:
          "signoz-access-token": <YOUR SIGNOZ ACCESS TOKEN>

    service:
      pipelines:
        logs:
          receivers: [k8s_events]
          exporters: [otlp]
```

通过运行以下命令应用配置映射：

```bash
$ kubectl apply -f configuration-map.yaml
```

### 步骤 2：创建服务账户

创建collector 应使用的服务账户。

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  labels:
    app: otelcontribcol
  name: otelcontribcol
```

通过运行以下命令将服务账户应用到集群：

```bash
$ kubectl apply -f service-account.yaml
```

### 步骤 3：为基于角色的访问控制 (RBAC) 创建 Cluster Role

使用下面的命令创建具有所需权限的 `ClusterRole`，并创建一个 `ClusterRoleBinding` 将该角色授予上面创建的服务账户。

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otelcontribcol
  labels:
    app: otelcontribcol
rules:
- apiGroups: [""]
  resources:
  - events
  - namespaces
  - namespaces/status
  - nodes
  - nodes/spec
  - pods
  - pods/status
  - replicationcontrollers
  - replicationcontrollers/status
  - resourcequotas
  - services
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources:
  - daemonsets
  - deployments
  - replicasets
  - statefulsets
  verbs: ["get", "list", "watch"]
- apiGroups: ["extensions"]
  resources:
  - daemonsets
  - deployments
  - replicasets
  verbs: ["get", "list", "watch"]
- apiGroups: ["batch"]
  resources:
  - jobs
  - cronjobs
  verbs: ["get", "list", "watch"]
- apiGroups: ["autoscaling"]
  resources:
  - horizontalpodautoscalers
  verbs: ["get", "list", "watch"]
```

通过运行以下命令将 ClusterRole 应用到集群：

```bash
$ kubectl apply -f cluster-role.yaml
```

### 步骤 4：创建部署清单

创建一个 [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment) 以部署collector 。


```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otelcontribcol
  labels:
    app: otelcontribcol
spec:
  replicas: 1
  selector:
    matchLabels:
      app: otelcontribcol
  template:
    metadata:
      labels:
        app: otelcontribcol
    spec:
      serviceAccountName: otelcontribcol
      containers:
      - name: otelcontribcol
        image: signoz/otelcontribcol:latest
        args: ["--config", "/etc/config/config.yaml"]
        volumeMounts:
        - name: config
          mountPath: /etc/config
      imagePullPolicy: IfNotPresent
      volumes:
      - name: config
        configMap:
          name: otelcontribcol
```

通过运行以下命令将清单应用到集群：

```bash
$ kubectl apply -f deployment.yaml
```

## 在 Signoz 仪表板上进行监控

部署 OpenTelemetry Collector 后，您可以在 SigNoz 中访问日志选项卡，查看 Kubernetes 事件的日志。

![](https://signoz.io/img/blog/2023/12/kubernetes-events-monitoring-logs-tab.webp)

在 SigNoz Logs 选项卡中监视 Kubernetes 事件的日志。

您还可以通过以下步骤从日志创建仪表板：

1. 转到 SigNoz Cloud。
2. 在左侧面板上，选择“Dashboards”。
3. 按下“+ New Dashboard”。
4. 按下“Import JSON”。
5. 粘贴来自以下 [GitHub 存储库](https://github.com/SigNoz/dashboards/blob/main/k8s-events-receiver.json)的 JSON。JSON 包含所有面板及其布局顺序。
6. 按下“Load JSON”。

现在，您已经有了一个包含receiver发送的大多数度量标的仪表板，其中包括一些时间序列图，以提高视觉体验。

![](https://signoz.io/img/blog/2023/12/kubernetes-events-monitoring-metrics.webp)

*Kubernetes 事件监控仪表板*

## 结论

在本教程中，您安装了OpenTelemetry Collector来收集Kubernetes事件，并将收集到的数据发送到SigNoz进行监控和警报。

请访问我们的OpenTelemetry Collector[完整指南](https://signoz.io/blog/opentelemetry-collector-complete-guide/)，以深入了解它。OpenTelemetry正在悄悄地成为开源可观察性的世界标准，通过使用它，您可以获得诸如所有遥测信号的单一标准、无供应商锁定等优势。

SigNoz是一个开源的[OpenTelemetry本地APM](https://signoz.io/blog/opentelemetry-apm/)，可用作您所有可观察性需求的单一后端。