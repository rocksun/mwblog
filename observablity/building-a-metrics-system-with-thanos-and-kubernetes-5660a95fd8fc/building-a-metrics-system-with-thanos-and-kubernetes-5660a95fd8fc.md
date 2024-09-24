
<!--
title: 使用Thanos和Kubernetes构建指标系统
cover: https://miro.medium.com/v2/resize:fit:985/1*QobsYEWqhoc_8s3tyB1Jlg.png
-->

指标是任何分布式系统中可观测性的支柱，在 Kubernetes 环境中，Prometheus 通常是……的工具。

> 译自 [Building a Metrics System with Thanos and Kubernetes](https://overcast.blog/building-a-metrics-system-with-thanos-and-kubernetes-5660a95fd8fc)，作者 DavidW。

指标是任何分布式系统中可观测性的基石，在 Kubernetes 环境中，Prometheus 通常是首选工具。

然而，扩展 Prometheus 和保留长期指标数据可能具有挑战性。Thanos 是一个扩展 Prometheus 功能的项目，它提供了可扩展的存储、跨多个 Prometheus 实例的全局查询以及高可用性指标。本文探讨了如何在 Kubernetes 上使用 Thanos 构建一个健壮、可扩展且有弹性的指标系统，涵盖从设置到最佳实践的方方面面。

## Thanos 和 Kubernetes 指标系统到底是什么？

使用 **Thanos 和 Kubernetes** 构建的指标系统就像将您的 Prometheus 监控提升到一个新的水平。Prometheus 非常适合从您的 Kubernetes 集群中抓取和存储指标，但在您需要扩展、长期存储指标或跨多个集群查询时，它会遇到限制。**Thanos** 是一种工具，它建立在 Prometheus 之上，通过提供 **可扩展的存储**、跨集群的 **全局查询** 以及 **高可用性** 来解决这些问题，从而实现故障转移和冗余。

使用 Thanos，您不仅仅是收集指标；您正在构建一个弹性系统，它允许您在分布式环境中存储和访问指标，而无需像以前那样独立管理多个 Prometheus 实例。这使得 Thanos 成为拥有大规模 Kubernetes 部署或希望保留指标以进行长期分析的组织的首选解决方案。

## 我为什么要使用它？

如果您只是运行一个小型 Kubernetes 集群，那么仅使用 Prometheus 可能就足够了。但是，一旦您的集群规模扩大，或者您在不同区域或环境中拥有多个集群，**Prometheus 本身就开始显示出局限性**:

* **指标保留**: Prometheus 不是为长期存储而设计的。您可能希望存储数月或数年的指标，但 Prometheus 只能保留数据有限的时间。
* **高可用性**: Prometheus 不提供内置冗余。如果您的 Prometheus 实例出现故障，您将丢失指标数据，直到它恢复在线。
* **全局查询**: Prometheus 是一个单节点系统，因此不支持跨多个集群的原生查询。

Thanos 通过扩展 Prometheus 的 **云原生功能** 来解决这些问题，这些功能允许您将指标存储在对象存储中（例如，Amazon S3），实时跨多个集群查询，并确保即使组件出现故障也能保证指标可用性。

## 使用 Thanos 和 Kubernetes 构建的指标系统的组件

Thanos 不仅仅是一个工具——它是一套组件，它们协同工作以创建一个功能齐全的指标系统：

* **Thanos Sidecar**: 它与每个 Prometheus 实例一起运行，将指标数据发送到对象存储，并允许 Prometheus 成为更大 Thanos 架构的一部分。
* **Querier**: 此组件聚合来自多个 Prometheus 实例和其他 Thanos 组件的数据，提供指标的统一视图。
* **Store Gateway**: 它从对象存储中检索较旧的指标，从而可以查询超出 Prometheus 本地保留的数据。
* **Compactor**: 通过压缩和降采样存储的指标来减少存储空间，从而提高查询性能和存储效率。
* **Ruler**: 它评估 Prometheus 风格的记录和警报规则，但针对历史数据，从而能够对长期趋势发出警报。

每个组件都在确保您的指标系统随着基础设施的增长而扩展，并且您可以在不管理庞大的 Prometheus 实例的情况下访问长期数据方面发挥作用。

## 在我们开始之前，有一些建议…

* **规划您的存储策略**: 在设置 Thanos 时，请记住，在云中存储大量指标数据可能会很昂贵。明智地选择您的存储提供商和生命周期管理策略（例如，将旧指标移动到更便宜的存储层）。
* **自动化部署**: 使用 Kubernetes 工具（如 Helm）来管理您的 Thanos 和 Prometheus 部署。这将使随着基础设施的增长，扩展和更新系统变得更加容易。
* **监控 Thanos 组件**: 不要只监控您的应用程序——还要为 Thanos 组件的运行状况设置警报。如果您的 Querier 或 Sidecar 出现故障，您需要立即知道。

现在您已经了解了为什么使用 Thanos 和 Kubernetes 构建的指标系统功能强大以及哪些组件使其工作，让我们深入了解设置并让一切运行起来。

## 使用 Kubernetes 部署 Thanos：真实世界教程

本逐步指南将引导您在实际场景中使用 Kubernetes 部署 Thanos。目标是使用 Prometheus 作为核心指标收集器，并使用 Thanos 作为扩展 Prometheus 功能的层，为 Kubernetes 集群建立一个可扩展的长期指标系统。在本教程结束时，您将拥有一个健壮的分布式系统，可以处理长期存储、跨多个 Prometheus 实例查询以及高可用性。

## 第 1 步：在 Kubernetes 上安装 Prometheus

设置指标系统的第一步是在 Kubernetes 集群中启动并运行 Prometheus。如果 Prometheus 尚未安装，您可以使用 **Helm** 快速部署它。

首先添加 Prometheus Chart 的 Helm 存储库：

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

存储库更新后，您可以通过运行以下命令安装 Prometheus：

```
helm install prometheus prometheus-community/prometheus
```

运行此命令后，Helm 将安装 Prometheus 服务器，您可以通过列出正在运行的 Pod 来检查其状态：

```
kubectl get pods -l "app=prometheus"
```

如果 Prometheus 正在运行，您将看到一个或多个名称以 **prometheus** 开头的 Pod。如果 Pod 未运行或卡在错误状态，您可能需要使用以下命令检查日志：

```
kubectl logs <prometheus-pod-name>
```

## 第 2 步：设置 Thanos Sidecar

Thanos Sidecar 对于将 Prometheus 集成到 Thanos 至关重要。它将与 Prometheus 一起运行，将其数据转发到长期存储（例如 Amazon S3）。

在配置 Sidecar 之前，如果您使用的是 Amazon S3，请创建一个新的 S3 存储桶来存储指标：

```
aws s3api create-bucket --bucket my-thanos-bucket --region us-east-1
```

现在，您需要更新 Prometheus 部署以包含 Thanos Sidecar。您将通过将 Thanos 容器添加到现有的 Prometheus 部署中来实现。以下是以 **Prometheus 和 Thanos Sidecar** 为例的部署配置：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: prometheus
        image: prom/prometheus:v2.43.0
        args:
        - "--config.file=/etc/prometheus/prometheus.yml"
        - "--storage.tsdb.path=/prometheus"
        ports:
        - containerPort: 9090
      - name: thanos-sidecar
        image: quay.io/thanos/thanos:v0.32.1
        args:
        - sidecar
        - --tsdb.path=/prometheus
        - --objstore.config-file=/etc/thanos/s3.yaml
        ports:
        - containerPort: 10902
        volumeMounts:
        - name: prometheus-data
          mountPath: /prometheus
        - name: s3-config
          mountPath: /etc/thanos/s3.yaml
          subPath: s3.yaml
        volumes:
        - name: s3-config
          configMap:
            name: s3-config
```

确保您创建了包含存储桶所需 S3 凭据的 **s3.yaml** 文件：

```yaml
type: S3
config:
  bucket: my-thanos-bucket
  endpoint: s3.amazonaws.com
  region: us-east-1
  access_key: YOUR_ACCESS_KEY
  secret_key: YOUR_SECRET_KEY
```

配置完 Sidecar 后，将更改应用到 Kubernetes 集群：

```
kubectl apply -f prometheus-thanos-deployment.yaml
```

这将部署 Prometheus 和 Thanos Sidecar，Sidecar 将开始将 Prometheus 数据发送到 S3 存储桶。

## 第 3 步：部署 Thanos Querier

**Thanos Querier** 允许您跨多个 Prometheus 实例查询数据，从而提供指标的全局视图。当您有多个 Kubernetes 集群或区域并希望拥有统一的指标系统时，这尤其有用。

以下是以 Thanos Querier 为例的部署：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: thanos-querier
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: thanos-querier
        image: quay.io/thanos/thanos:v0.32.1
        args:
        - query
        - --http-address=0.0.0.0:9090
        - --store=dnssrv+_grpc._tcp.thanos-sidecar.default.svc.cluster.local:10901
        - --store=dnssrv+_grpc._tcp.thanos-store.default.svc.cluster.local:10901
        ports:
        - containerPort: 9090
```

在此配置中，Querier 被设置为通过 DNS 服务发现从 Thanos Sidecar 和 Store Gateway 获取数据。Querier 将充当查询指标的集中点。

通过应用 YAML 将 Thanos Querier 部署到您的集群：

```
kubectl apply -f thanos-querier-deployment.yaml
```

要测试 Querier，请将服务端口转发到您的本地机器：

```
kubectl port-forward svc/thanos-querier 9090:9090
```

现在，打开您的浏览器并访问 [http://localhost:9090](http://localhost:9090) 以与 Thanos Querier UI 交互并开始跨 Prometheus 实例查询数据。

## 第 4 步：部署 Thanos Store Gateway

Thanos **Store Gateway** 从 S3 存储桶中检索历史指标。这使您能够查询超出 Prometheus 本身保留限制的数据。

以下是以 Thanos Store Gateway 部署为例的配置：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: thanos-store
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: thanos-store
        image: quay.io/thanos/thanos:v0.32.1
        args:
          - store
          - --data-dir=/data
          - --objstore.config-file=/etc/thanos/s3.yaml
        ports:
          - containerPort: 10901
        volumeMounts:
          - name: data
            mountPath: /data
          - name: s3-config
            mountPath: /etc/thanos/s3.yaml
            subPath: s3.yaml
volumes:
  - name: data
    emptyDir: {}
  - name: s3-config
    configMap:
      name: s3-config
```

将此配置应用于部署 Thanos Store Gateway：

```
kubectl apply -f thanos-store-deployment.yaml
```

Store Gateway 将开始从您的 S3 存储桶中检索较旧的指标，使其可通过 Thanos Querier 查询。

## 第 5 步：验证和测试您的设置

所有 Thanos 组件都运行后，您应该测试整个设置以确保指标正在正确存储和查询。

首先检查所有 Prometheus 和 Thanos Pod 是否正在运行：

```
kubectl get pods
```

如果一切按预期运行，请使用 Thanos Querier UI 执行查询。验证您是否可以从 S3 存储桶中检索最近和历史数据。

您还可以检查 Thanos 组件的日志以确保它们正在正确通信：

```
kubectl logs <thanos-querier-pod-name>
kubectl logs <thanos-store-pod-name>
kubectl logs <thanos-sidecar-pod-name>
```


如果任何组件未按预期工作，这些日志将提供有关问题所在的信息。

## 最佳实践

### 使用 Thanos 和 Kubernetes 的指标系统的最佳实践

在 Kubernetes 上部署 Thanos 是大规模管理指标的强大方法，但为了确保您的设置高效运行并保持成本效益，有一些最佳实践需要遵循。这些不仅会提高性能，还会降低开销并使长期指标保留更易于管理。

### 使用降采样减少查询负载

随着指标数量的增长，查询数据可能会变得缓慢且资源密集。这就是 **降采样** 发挥作用的地方。降采样会聚合较旧的指标，降低其粒度，同时保留随时间推移的重要趋势。通过配置 **Thanos Compactor** 对您的指标进行降采样，您可以显着提高查询性能，降低存储成本，并减轻对象存储的负载。

在典型的 Thanos 设置中，**Compactor** 处理两项任务：将时间序列压缩成更小的块以及对较旧的数据进行降采样。以下是如何配置 Compactor 的示例：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: thanos-compactor
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: thanos-compactor
        image: quay.io/thanos/thanos:v0.32.1
        args:
        - compact
        - --data-dir=/data
        - --objstore.config-file=/etc/thanos/s3.yaml
        - --retention.resolution-raw=30d
        - --retention.resolution-5m=180d
        - --retention.resolution-1h=1y
        volumeMounts:
        - name: data
          mountPath: /data
        - name: s3-config
          mountPath: /etc/thanos/s3.yaml
          subPath: s3.yaml
        volumes:
        - name: data
          emptyDir: {}
        - name: s3-config
          configMap:
            name: s3-config
```

在此配置中，**Compactor** 设置为保留 30 天的原始高分辨率数据，180 天的 5 分钟降采样数据以及 1 年的 1 小时降采样数据。Compactor 会自动创建这些降采样块，使查询历史数据变得更容易，而不会给系统带来负担。

请确保根据您的数据需求和存储容量调整保留期。当您不需要对较旧的指标进行细粒度分析，但仍希望保留长期趋势以进行分析或合规性时，降采样非常理想。

## 利用 Kubernetes 服务发现

Thanos Querier 可以使用 **Kubernetes 服务发现** 自动发现 Prometheus 实例。这简化了扩展或缩减的过程，而无需手动配置新的 Prometheus 实例。Kubernetes 的本机基于 DNS 的服务发现允许 Thanos 在集群中动态发现服务，使系统更灵活，更易于管理。

要在 Thanos Querier 中启用服务发现，您可以修改部署配置，如下所示：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: thanos-querier
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: thanos-querier
        image: quay.io/thanos/thanos:v0.32.1
        args:
        - query
        - --http-address=0.0.0.0:9090
        - --store=dnssrv+_grpc._tcp.prometheus.default.svc.cluster.local:10901
        - --store=dnssrv+_grpc._tcp.thanos-store.default.svc.cluster.local:10901
```

在此设置中，`dnssrv` 地址用于自动发现 Kubernetes 集群中运行的任何 Prometheus 实例和 Thanos Store Gateway。通过利用 Kubernetes 基于 DNS 的服务发现，Thanos 可以动态扩展，而无需在添加新的 Prometheus 实例时进行任何手动配置。

## 保护对象存储访问

当使用 **Amazon S3** 或 **Google Cloud Storage** 等云对象存储来存储您的指标时，保护访问凭据至关重要。您不应该在 YAML 文件中硬编码凭据，而应该使用 **Kubernetes Secrets** 来管理敏感信息，例如您的对象存储访问密钥。

以下是将 S3 凭据安全存储在 Kubernetes Secret 中的方法：

```
kubectl create secret generic s3-credentials \
--from-literal=access_key=YOUR_ACCESS_KEY \
--from-literal=secret_key=YOUR_SECRET_KEY
```

创建 Secret 后，在 Thanos sidecar 或存储配置中引用它：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: thanos-sidecar
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: thanos-sidecar
        image: quay.io/thanos/thanos:v0.32.1
        args:
        - sidecar
        - --tsdb.path=/prometheus
        - --objstore.config-file=/etc/thanos/s3.yaml
        env:
        - name: S3_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: s3-credentials
              key: access_key
        - name: S3_SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: s3-credentials
              key: secret_key
        volumeMounts:
        - name: s3-config
          mountPath: /etc/thanos/s3.yaml
          subPath: s3.yaml
```

通过使用 **Kubernetes Secrets**，您可以确保访问密钥被加密并安全存储，从而降低意外泄露的风险。

## 监控 Thanos 组件

监控 Thanos 组件的运行状况与监控应用程序的运行状况一样重要。如果任何 Thanos 组件（如 Querier、Sidecar 或 Store Gateway）出现故障，可能会影响您的指标系统，导致数据丢失或查询失败。

第一步是设置 **Prometheus 报警规则** 来跟踪 Thanos 组件的状态。例如，您可以使用以下报警规则来监控 Prometheus 中 Thanos 实例的 **up** 状态：

```yaml
groups:
- name: thanos-alerts
  rules:
  - alert: ThanosDown
    expr: up{job="thanos"} == 0
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Thanos instance down"
      description: "The Thanos {{ $labels.instance }} instance is down for more than 5 minutes."
```

如果任何 Thanos 实例在 5 分钟以上处于停机状态，此报警将触发，使您能够快速检测并响应系统中的故障。

您还应该考虑使用 **Grafana** 来可视化 Thanos 组件的性能，并创建仪表板来实时跟踪每个服务的运行状况和性能。

## 优化存储成本

存储大量指标可能会变得很昂贵，尤其是在您长时间保留高分辨率数据的情况下。为了优化成本，请在您的对象存储中使用 **生命周期策略**，自动将较旧的数据移动到更便宜的存储层级，例如 Amazon S3 的 **Glacier** 或 **Google Cloud Nearline Storage**。

例如，在 Amazon S3 中，您可以配置一个生命周期策略，在 90 天后将较旧的数据迁移到 Glacier：

```json
{
  "Rules": [
    {
      "ID": "MoveOlderDataToGlacier",
      "Filter": {
        "Prefix": ""
      },
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        }
      ],
      "NoncurrentVersionTransitions": [],
      "Expiration": {
        "Days": 365
      }
    }
  ]
}
```

应用此策略可确保您只为最近的数据支付高性能存储费用，而较旧的数据将迁移到更便宜、更慢的存储类别。

在 Google Cloud Storage 中，您可以配置类似的生命周期规则，在设定的天数后将对象迁移到 **Nearline** 或 **Coldline** 存储。此策略有助于优化您的存储成本，尤其是在保留大量历史指标数据时。

## 结论

使用 **Thanos** 和 **Kubernetes** 设置指标系统可能感觉是一项艰巨的任务，尤其是在您开始考虑长期存储、高可用性和跨多个集群的全局查询时。但好消息是，它并不一定是一个令人生畏的过程。通过将 Thanos 与 Prometheus 集成，您可以解决 Kubernetes 环境中可观测性方面的一些最大挑战——可扩展性、冗余性和成本管理。

在本指南中，我逐步指导您部署 Prometheus 和 Thanos，配置降采样、保护对象存储访问权限以及使用 Kubernetes 服务发现。这些步骤中的每一个都有助于创建一个更强大、更高效的指标系统，该系统可以随着您的基础设施扩展。这里重要的是保持您的设置灵活，监控组件的运行状况，并随着数据增长优化性能和成本。

现在，我很想听听您的想法！如果您有其他技巧或在部署 Thanos 时遇到任何有趣的挑战，请在下面的评论中留下您的建议。让我们将此资源变成一个协作资源，让每个人都能从中受益。
