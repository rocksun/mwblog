
<!--
title: 如何在Kubernetes中以原生方式部署Fluent Bit
cover: https://cdn.thenewstack.io/media/2025/07/3d3bf7a5-deploy-fluentbit-kubernetes-native-crd.jpg
summary: 本文介绍了如何使用 Kubernetes Operator 部署和管理 Fluent Bit，以及如何通过 CRD 进行配置和实现实时配置热加载，简化了日志记录管道的管理和运维工作。
-->

本文介绍了如何使用 Kubernetes Operator 部署和管理 Fluent Bit，以及如何通过 CRD 进行配置和实现实时配置热加载，简化了日志记录管道的管理和运维工作。

> 译自：[How To Deploy Fluent Bit in a Kubernetes-Native Way](https://thenewstack.io/how-to-deploy-fluent-bit-in-a-kubernetes-native-way/)
> 
> 作者：Sharad Regoti

[Fluent Bit](https://fluentbit.io/) 是一个被广泛使用的开源数据收集代理、处理器和转发器，它使你能够从各种来源收集日志、指标和追踪数据，过滤和转换它们，然后将它们转发到多个目的地。

虽然有多种方法可以在 [Kubernetes 中部署 Fluent Bit](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=TNS&utm_medium=sponsored-content)，但在多个集群或团队中管理其生命周期和配置可能成为一项复杂的任务。

这就是 [Fluent Operator](https://github.com/fluent/fluent-operator/tree/master) 的用武之地；它是一种 Kubernetes 原生的方式，可以使用自定义资源定义（CRD）来部署、管理和配置 [Fluent Bit 和 Fluentd](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd)。

本指南探讨了如何使用 Fluent Operator 部署 [Fluent Bit](https://thenewstack.io/whats-driving-fluent-bit-adoption)，为什么使用 Operator 可以简化你的日志记录堆栈，以及如何在不重启 Pod 的情况下进行实时配置更改。

### 前提条件

*   **Kubernetes 集群：** 我将在 Kubernetes 集群中部署 [Fluent Bit](https://chronosphere.io/fluent-bit/?utm_source=TNS&utm_medium=sponsored-content)。我将使用 Docker Desktop，但任何集群都适用。
*   **Elasticsearch：** 我将把日志发送到 Elasticsearch。你可以使用这个 [指南](https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html) 来进行操作。
*   **Kubectl：** 你可以参考 [官方文档](https://kubernetes.io/docs/tasks/tools/#kubectl) 来安装 Kubernetes 命令行工具。
*   **Helm CLI：** 你可以在安装 Helm 时参考 [官方文档](https://helm.sh/docs/intro/install/)。
*   **熟悉 Fluent Bit 概念：** 如果你不熟悉输入、输出、解析器和过滤器等概念，请参考 [官方文档](https://docs.fluentbit.io/manual/concepts/data-pipeline)。

## 什么是 Kubernetes Operator？

Kubernetes Operator 是一种软件扩展，它以 Kubernetes 原生的方式自动管理复杂的应用程序。它利用 CRD 来定义应用程序应如何运行，并确保系统持续与所需状态保持一致。

### 为什么需要 Operator

[Kubernetes](https://chronosphere.io/learn/what-is-kubernetes-and-how-does-it-benefit-observability/?utm_source=TNS&utm_medium=sponsored-content) 提供了基本的原语，例如 Pod 和 StatefulSet，用于部署和管理容器，但它本身并不了解如何管理复杂应用程序的内部逻辑。例如，你可以启动一个数据库 Pod，但 Kubernetes 不知道如何安全地备份它、执行升级或从故障中恢复。

这就是 Operator 的用武之地。它们使用特定领域的智能扩展 Kubernetes，自动执行 Day 1 和 Day 2 的任务，如安装、配置、更新和故障恢复。这会将以前手动、容易出错的工作流程转换为可重复和自我修复的过程。

Operator 对于管理有状态应用程序至关重要，例如数据库、消息代理和遥测管道。如果没有 Operator，管理这些系统需要自定义脚本或手动步骤，这些步骤在动态环境中无法很好地扩展。

Fluent Operator 允许你声明式地配置日志记录堆栈，并让 Operator 处理编排和生命周期管理。

## 什么是 Fluent Operator

Fluent Operator 简化了在 Kubernetes 中部署和配置 [Fluent Bit 和 Fluentd](https://chronosphere.io/learn/fluent-bit-vs-fluentd/?utm_source=TNS&utm_medium=sponsored-content) 的过程。它通过 CRD 公开配置，例如 `ClusterInput`、`ClusterFilter` 和 `ClusterOutput`，它们代表 Fluent Bit 遥测管道的不同阶段。

安装后，Fluent Operator 提供：

*   自动将 Fluent Bit 部署为 DaemonSet。
*   通过 Kubernetes 原生 CRD 进行声明式配置。
*   支持动态配置重新加载，无需重启 Pod。
*   可选的 [Fluentd](https://thenewstack.io/a-guide-to-migrating-from-fluentd-to-fluent-bit) 部署，用于高级日志路由和多租户日志隔离。

这使其成为实践 GitOps 或管理大型多租户 Kubernetes 集群的团队的理想选择。

**注意：** 尽管 Fluent Operator 同时管理 Fluent Bit 和 Fluentd，但本文 [侧重于 Fluent Bit](https://thenewstack.io/fluent-bit-core-concepts/)。

### 主要配置选项

使用 Fluent Operator 部署 Fluent Bit 后，你将使用 CRD 定义日志记录管道。以下是最重要的 CRD 的快速概述：

*   **`FluentBit`**：定义 Fluent Bit DaemonSet 及其配置。
*   **`ClusterFluentBitConfig`**：选择集群级别的输入/过滤器/输出插件，并将最终配置生成到 Secret 中。
*   **`ClusterInput`**：定义日志的来源。例如，你可以配置 Fluent Bit 来追踪容器日志或收集系统日志。
*   **`ClusterParser`**：使用正则表达式、JSON 或自定义格式解析传入的日志。
*   **`ClusterFilter`**：过滤和丰富日志记录。
*   **`ClusterOutput`**：定义将日志发送到哪里，例如 Elasticsearch、Loki 或 Kafka。

有关 Fluent Bit 可用 CRD 的更多信息，请参阅此 [文档](https://github.com/fluent/fluent-operator/tree/master?tab=readme-ov-file#fluent-bit)。

### 如何使用 CRD 配置管道

每个 **`ClusterInput`**、**`ClusterParser`**、**`ClusterFilter`**、**`ClusterMultilineParser`** 和 **`ClusterOutput`** 代表一个 Fluent Bit 配置部分，该部分由 **`ClusterFluentBitConfig`** 通过标签选择器选择。Fluent Operator 监视这些对象，构造最终配置，然后创建一个 Secret 来存储配置，该配置将被挂载到 Fluent Bit DaemonSet 中。整个工作流程如下所示：

[![Fluent Operator 监视这些对象，构造最终配置，然后创建一个 Secret 来存储配置，该配置将被挂载到 Fluent Bit DaemonSet 中。](https://cdn.thenewstack.io/media/2025/07/c6b8b673-fluentbit-workflow.png)](https://cdn.thenewstack.io/media/2025/07/c6b8b673-fluentbit-workflow.png)

来源：Chronosphere。

## 使用 Fluent Operator 部署 Fluent Bit

我将部署一个 Fluent Bit 管道，该管道从 Kubernetes Pod 和 Systemd 收集日志，并将它们发送到 Elasticsearch，如下图所示：

[![部署一个 Fluent Bit 管道，该管道从 Kubernetes Pod 和 Systemd 收集日志，并将它们发送到 Elasticsearch](https://cdn.thenewstack.io/media/2025/07/69030e66-deploy-pipeline.png)](https://cdn.thenewstack.io/media/2025/07/69030e66-deploy-pipeline.png)

来源：Chronosphere。

### 说明

1.  **使用 Helm 安装 Operator。** 请注意，可以通过调整 [values.yaml](https://github.com/fluent/fluent-operator/blob/master/charts/fluent-operator/values.yaml) 文件来修改此 Chart 的行为。

    ```
    export FLUENT_OPERATOR_CONTAINER_RUNTIME="docker" # or "cri-o", "containerd" depending on the container runtime being used (see `values.yaml`)
    
    helm repo add fluent https://fluent.github.io/helm-charts
    helm upgrade --install fluent-operator fluent/fluent-operator \
      --create-namespace \
      --set containerRuntime=${FLUENT_OPERATOR_CONTAINER_RUNTIME}
    ```
2.  **等待 Pod 运行。** 现在，执行以下命令来检查 Pod 的状态。等待 Pod 的状态更改为 `Running`。

    ```
    kubectl get pods
    
    ## Expected Output
    NAME                               READY   STATUS    RESTARTS   AGE
    fluent-bit-5k954                   1/1     Running   0          2s
    fluent-operator-5b55477974-7phj7   1/1     Running   0          11s
    ```
3.  **查看默认配置。** 要列出创建的 Kubernetes 资源，请运行以下命令。这将列出资源类型及其名称。

    ```
    helm get manifest fluent-operator -n default | \
      grep -E '^(kind:|  name:)' | \
      sed 'N;s/\n/ /'
    
    ## Expected Output
    ...
    kind: ClusterFilter   name: kubernetes
    kind: ClusterFilter   name: systemd
    kind: ClusterFluentBitConfig   name: fluent-bit-config
    kind: ClusterInput   name: "docker"
    kind: ClusterInput   name: tail
    kind: FluentBit   name: fluent-bit
    ```
    
    默认情况下，除了设置 Fluent Operator Pod 之外，此 Chart 还会安装和配置 Fluent Bit 以收集 Kubernetes 日志并将其发送到空目标（可以使用 [此标志](https://github.com/fluent/fluent-operator/blob/master/charts/fluent-operator/values.yaml#L9) 禁用此行为）。可以使用以下命令查看此 Chart 生成的默认 Fluent Bit 管道配置。

    ```
    kubectl get secret fluent-bit-config -o jsonpath="{.data.fluent-bit\.conf}" | base64 --decode
    ```
    
    以下是已部署管道的图形表示：

    [![已部署的管道](https://cdn.thenewstack.io/media/2025/07/dd112b0d-deployed-pipeline.png)](https://cdn.thenewstack.io/media/2025/07/dd112b0d-deployed-pipeline.png)

    来源：Chronosphere。
4.  **添加 Elasticsearch 输出。** 要添加 Elasticsearch 输出，请使用 `ClusterOutput` CRD。创建一个 `es-credentials.yaml` 文件，内容如下。此 Kubernetes Secret 包含连接到 Elasticsearch 集群的用户名和密码。

    ```
    apiVersion: v1
    kind: Secret
    metadata:
      name: es-credentials
      namespace: default
    type: Opaque
    data:
      user: <your-base64-encoded-username>
      password: <your-base64-encoded-password>
    ```
    
    接下来，创建一个 `elastic-output.yaml` 文件，内容如下。

    ```
    apiVersion: fluentbit.fluent.io/v1alpha2
    kind: ClusterOutput
    metadata:
      name: es
      labels:
        fluentbit.fluent.io/enabled: "true"
        fluentbit.fluent.io/component: logging
    spec:
      matchRegex: (?:kube|service)\.(.*)
      es:
        host: <elastic-search-host>
        port: 9200
        suppressTypeName: "On"
        httpUser:
          valueFrom:
            secretKeyRef:
              name: es-credentials
              key: user
        httpPassword: 
          valueFrom:
            secretKeyRef:
              name: es-credentials
              key: password
        logstashPrefix: ks-logstash-log
        timeKey: "@timestamp"
    ```
    
    现在应用上述配置。

    ```
    ubectl apply -f es-credentials.yaml
    kubectl apply -f elastic-output.yaml
    ```
5.  **验证 Fluent Bit 配置是否已更新。** 你应该在末尾看到 `es` 插件。

    ```
    kubectl get secret fluent-bit-config -o jsonpath="{.data.fluent-bit\.conf}" | base64 --decode
    
    ## Expected Output
    [Output]
        Name    es
        Match_Regex    (?:kube|service)\.(.*)
        Host    192.168.0.100
    ...
    ```
6.  **验证 Elasticsearch 中的日志。** 注意：我在 Elasticsearch 中创建了模式为 **`ks-logstash-log-*`** 的索引。要在 Kibana 中查看这些日志，你需要创建一个 [数据视图](https://www.elastic.co/docs/explore-analyze/find-and-organize/data-views)。

    [![Elasticsearch GUI](https://cdn.thenewstack.io/media/2025/07/48ae4a56-elastic-indices.png)](https://cdn.thenewstack.io/media/2025/07/48ae4a56-elastic-indices.png)

    来源：Chronosphere。

## 实时/热加载配置

Fluent Operator 的一个重要功能是能够在不重启 Fluent Bit Pod 的情况下重新加载配置。

为了使 Fluent Bit 能够在 Fluent Bit 配置更改时获取并使用最新配置，添加了一个名为 Fluent Bit Watcher 的包装器，以便在检测到 Fluent Bit 配置更改后立即重启 Fluent Bit 进程。

这样，无需重启 Fluent Bit Pod 即可重新加载新配置。以这种方式重新加载 Fluent Bit 配置，因为 Fluent Bit 本身没有内置的重新加载接口。

[![Fluent Bit Pod 工作流程](https://cdn.thenewstack.io/media/2025/07/ef0b141c-hot-reloading-pipeline.png)](https://cdn.thenewstack.io/media/2025/07/ef0b141c-hot-reloading-pipeline.png)

来源：Chronosphere。

### 说明

1.  **检查 Fluent Bit Pod 的 Age。** 要验证 Pod 在配置更改期间是否未重启，请检查 Pod 的 Age。执行以下命令以检查 Pod 的当前 Age。

    ```
    kubectl get pods -l app.kubernetes.io/name=fluent-bit
    
    ## Expected Output
    NAME               READY   STATUS    RESTARTS   AGE
    fluent-bit-5k954   1/1     Running   0          68m
    ```
2.  **进行配置更改。** 要添加另一个 `ClusterOutput` CRD，请创建一个 `es-hot-reload.yaml` 文件，内容如下。这与之前的 CRD 类似，但我在此配置中将 `logstashPrefix` 从 `ks-logstash-log` 更改为 `new-ks-logstash-log`。

    ```
    apiVersion: fluentbit.fluent.io/v1alpha2
    kind: ClusterOutput
    metadata:
      name: es-hot-reload
      labels:
        fluentbit.fluent.io/enabled: "true"
        fluentbit.fluent.io/component: logging
    spec:
      matchRegex: (?:kube|service)\.(.*)
      es:
        host: <elastic-search-host>
        port: 9200
        suppressTypeName: "On"
        httpUser:
          valueFrom:
            secretKeyRef:
              name: es-credentials
              key: user
        httpPassword: 
          valueFrom:
            secretKeyRef:
              name: es-credentials
              key: password
        logstashPrefix: new-ks-logstash-log
        timeKey: "@timestamp"
    ```
    
    现在，应用上述配置。
3.  **验证 Pod 时间。** 你应该看到 Pod 没有重启，并且其 Age 保持相对不变。

    ```
    kubectl get pods -l app.kubernetes.io/name=fluent-bit
    
    ## Expected Output
    NAME               READY   STATUS    RESTARTS   AGE
    fluent-bit-5k954   1/1     Running   0          68m
    ```
4.  ****验证 Fluent Bit 配置已使用最新的输出进行更新。****

    ```
    kubectl get secret fluent-bit-config -o jsonpath="{.data.fluent-bit\.conf}" | base64 --decode
    ```
5.  **验证 Elasticsearch 中的日志。** 注意：我仅在 Elasticsearch 中创建了模式为 **`new-ks-logstash-log-*`** 的索引。要在 Kibana 中查看这些日志，你需要创建一个 [数据视图](https://www.elastic.co/docs/explore-analyze/find-and-organize/data-views)。

## 结论

你可以利用 Fluent Operator 以可扩展的 Kubernetes 原生方式管理 Fluent Bit 部署。

Fluent Operator 使用 CRD 简化了复杂日志记录管道的配置，同时支持动态更新，而无需重启 Pod。无论你是在单个集群中还是在多个环境中运行，Fluent Operator 都可以简化可观测性并减少运营开销。

如果你想了解更多信息或有疑问，请加入下一次虚拟 [Fluent Bit 办公时间](https://www.meetup.com/fluent-community-meeting/events) 或加入 [Fluent Bit Slack](https://www.launchpass.com/fluent-all)。