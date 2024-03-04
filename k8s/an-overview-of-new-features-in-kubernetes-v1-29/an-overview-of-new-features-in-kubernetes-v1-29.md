
<!--
title: Kubernetes v1.29新功能概述
cover: http://teckbootcamps.com/wp-content/uploads/2024/02/crd-1.png
-->

Kubernetes v1.29 是 2023 年的第三个主要版本更新，也是今年的最后一个主要版本，包含 49 个主要更新。

> 译自 [An overview of new features in Kubernetes v1.29](https://teckbootcamps.com/an-overview-of-new-features-in-kubernetes-v1-29/)，作者 Mohamed BEN HASSINE。

今年发布的第一个版本 v1.27 接近 60 个项目，第二个版本 v1.28 有 46 个项目。尽管 Kubernetes 已经发布了近 10 年，但 Kubernetes 仍然非常活跃！

此版本中有 19 项增强功能进入 Alpha 阶段，19 项将升级到 Beta 阶段，11 项将升级到稳定版本。

可以看出，仍有许多新功能正在逐步引入。

## 基于 CEL 的 CRD 规则验证正式达到 GA

对于所有在 Kubernetes 上开发的朋友来说，此功能应该非常重要。因为在大多数情况下，我们使用 CRD 在 Kubernetes 中实现功能扩展。

在通过 CRD 实现功能扩展时，为了提供更好的用户体验和更可靠的输入验证，有必要支持验证。

CRD 目前原生支持两种类型的验证功能：

- 基于 CRD 结构定义的检查
- OpenAPIv3 验证规则

例如：

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.13.0
  name: kongplugins.configuration.konghq.com
spec:
  group: configuration.konghq.com
  names:
    categories:
    - kong-ingress-controller
    kind: KongPlugin
    listKind: KongPluginList
    plural: kongplugins
    shortNames:
    - kp
    singular: kongplugin
  scope: Namespaced
  versions:
  - name: v1
    schema:
      openAPIV3Schema:
        description: KongPlugin is the Schema for the kongplugins API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object. Servers should convert recognized schemas to the latest
              internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          protocols:
            description: Protocols configures plugin to run on requests received on
              specific protocols.
            items:
              description: KongProtocol is a valid Kong protocol. This alias is necessary
                to deal with https://github.com/kubernetes-sigs/controller-tools/issues/342
              enum:
              - http
              - https
              - grpc
              - grpcs
              - tcp
              - tls
              - udp
            type: string
          type: array
          type: object
          ...
    x-kubernetes-validations:
    - message: Using both config and configFrom fields is not allowed.
      rule: '!(has(self.config) && has(self.configFrom))'
    - message: Using both configFrom and configPatches fields is not allowed.
      rule: '!(has(self.configFrom) && has(self.configPatches))'
    - message: The plugin field is immutable
      rule: self.plugin == oldSelf.plugin
```

在上面的示例中，定义了一个名为 KongPluginIn 的自定义资源，其中
openAPIV3Schema定义了 OpenAPI 架构的验证规则。

但是，这些内置规则可以实现的效果相对有限。如果你想实现更丰富的验证规则/功能，可以使用：

- Admission Webhook
- 使用自定义验证器

然而，

**无论是 Admission webhook 还是自定义验证器，它们都与 CRD 本身分离，这也将增加开发 CRD 和后续维护成本的难度。**

为了解决这些问题，Kubernetes 社区为 CRD 引入了基于 CEL（通用表达式语言）的验证规则。该规则可以直接在 CRD 声明文件中编写，而无需使用任何准入 webhook 或自定义验证器，极大简化了 CRD 的开发和维护成本。

在 Kubernetes v1.29 版本中，基于 CEL 的 CRD 验证能力达到 GA。你只需要使用 `x-kubernetes-validations` 定义验证规则即可。

它足够轻量和安全，可以直接在 kube-apiserver 中运行。我们来看一个例子：

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.13.0
  name: kongplugins.configuration.konghq.com
spec:
  group: configuration.konghq.com
  scope: Namespaced
  versions:
  - name: v1
    schema:
      openAPIV3Schema:
        description: KongPlugin is the Schema for the kongplugins API.
        properties:
          plugin:
            ...
        x-kubernetes-validations:
        - message: Using both config and configFrom fields is not allowed.
          rule: '!(has(self.config) && has(self.configFrom))'
        - message: The plugin field is immutable
          rule: self.plugin == oldSelf.plugin
```

比如，在这句话中 `self.plugin == oldSelf.plugin`，`self` 和 `oldSelf` 分别表示变更前后资源对象。一旦 `plugin` 字段的内容被定义，就不允许再被修改。

此外，CEL 还具有非常丰富的特性，可以通过在线 Playground [https://playcel.undistro.io/](https://playcel.undistro.io/) 体验。

正如我前面提到的，这个特性已经推出两年多了。它在 Kubernetes v1.25 中达到 Beta 并默认启用，现在终于达到 GA。

此外，Kubernetes Gateway API 项目正在删除其所有的Admission webhook，并使用基于 CEL 的规则进行验证。这可能是目前社区中最大的一个用例。

## 为动态和静态分配保留 NodePort 端口范围达到稳定

在 Kubernetes 中，本机 Service 对象包含 NodePort 类型，用于将集群内的服务暴露给外部实体。目前，创建新的 NodePort 并指定固定端口会带来一定的风险。指定的端口可能已经被分配，从而导致冲突和 Service 创建失败。

此 Kubernetes 增强提案 (KEP) 建议为 NodePort 类型的 Service 引入可选范围的动态和静态保留，为端口配置提供两种方法：

1. **自动随机生成**：Kubernetes 将根据预定义的规则自动生成端口。
2. **手动设置**：用户可以根据自己的需求手动设置端口。

例如，kube-apiserver 可以使用 `--service-node-port-range` 标志控制 NodePort 可以使用的端口范围，默认范围为 30000-32767。此 KEP 中提出的计算公式如下：

```
Static Band Start=Min(Max($min,$node-range-size/$step),$max)
```

其中：

- Service Node Port 范围：30000-32767
- 范围大小：32767 – 30000 = 2767
- 带宽偏移：Min(Max(16,2767/32),128)=Min(86,128)=86
- 静态带宽开始：30000
- 静态带宽结束：30086

按照此计算，30000-30086 被认为是静态段，而其余端口被认为是动态段。

实现此方法可以降低使用固定端口创建 NodePort 类型的 Service 时发生冲突的风险，从而提高整体集群稳定性。

```bash
 ┌─────────────┬─────────────────────────────────────────────┐
 │   static    │                    dynamic                  │
 └─────────────┴─────────────────────────────────────────────┘

 ◄────────────► ◄────────────────────────────────────────────►
30000        30086                                          32767

```

当用户希望自己指定 NodePort 端口时，如果所选端口落在上文概述的静态范围内，则不太可能发生冲突。

首先，此特性是 Kubernetes 的一个内部方面，对于大多数场景，一个简单的原则就足够了：“在手动选择 NodePort 时，尽量选择前面提到的静态范围内的端口。”如果用户指定的端口位于动态范围内并且尚未被分配，则创建过程也将成功。

此计算方法源自 KEP-3070，用于将 ClusterIP 分配给 Service，确保在 Kubernetes 生态系统中进行端口分配时采用简化且有效的方法。

## Sidecar 容器特性达到 Beta 并默认启用

Sidecar 作为辅助容器，增强了主容器的功能。虽然在服务网格场景中广泛使用，但许多用户也在非服务网格上下文中部署它们，例如用于日志记录、监控和各种其他目的。

在使用 Sidecar 的场景中，过去曾出现过问题。一个值得注意的问题是 Sidecar 容器缺乏生命周期管理。

例如，当一个 Pod 被删除时，Sidecar 容器缺乏适当的生命周期管理会导致这些服务和主容器的生命周期之间出现同步不匹配，从而对服务可靠性产生不利影响。

此 Kubernetes 增强提案 (KEP) 通过将 Sidecar 容器定义为 Pod 规范中 init 容器的一部分来解决这些挑战。

此外，KEP 规定 Sidecar 容器应遵守“始终重新启动”策略。通过将 Sidecar 纳入具有始终如一重新启动策略的 init 容器，此提案旨在增强 Sidecar 容器的生命周期管理，从而在服务网格和非服务网格场景中促进更好的同步和可靠性。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mohamedbenhassine-pod
spec:
  initContainers:
  - name: log
    image: mohamedbenhassine/fluentbit
    restartPolicy: Always
    ...
```

在 Kubernetes v1.29 中，这项功能将默认启用，Sidecar 容器的停止顺序将按照它们启动的相反顺序进行。

这确保了主容器首先停止，并且还方便控制所有容器的组件生命周期。

## PreStop Hook 引入了睡眠操作（Alpha）

此 KEP 也很有趣，主要是为了简化最常见的要求之一。

许多应用程序 Pod 在关闭时需要断开连接，以避免影响用户流量。因此，PreStop 通常设置为在关闭之前执行一些相关处理或等待。

但是，当前的 PreStop Hook 仅支持两种类型：exec 和 httpGet。

此 KEP 旨在实现本机睡眠操作，例如：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  template:
    spec:
      containers:
      - name: nginx
        image: nginx:1.25.3
        lifecycle:
          preStop:
            sleep:
              seconds: 5
        readinessProbe:
          httpGet:
            path: /
            port: 80
```

这可能非常简单。在引入此 KEP 之前，需要将其设置为类似于 exec sh -c "sleep 5" 的内容，这需要将此命令包含在容器中 sleep。

但是，此功能目前处于 Alpha 阶段，是否可以最终达到 GA 取决于社区的反馈。

## 改进服务帐户令牌绑定机制（Alpha）

在 Kubernetes 中，服务帐户令牌是确保安全性的不可或缺的一部分。它们用于对集群中的各个工作负载进行身份验证并防止未经授权的访问。

Kubernetes v1.29 进一步加强了这些令牌的安全保护：现在每个服务帐户只能与特定的 Pod 实例关联，并且在泄露后无法被滥用。此方法有效地捆绑了服务帐户和 Pod 生命周期，极大地降低了攻击者使用被盗令牌进行攻击的可能性。

在 v1.29 中，kube-apiserver 具有以下相关的功能门控来控制相关功能。当然，除了 KEP-4193 之外，此版本还推广了 KEP-2799，该版本减少了基于秘密的服务帐户令牌的数量。这有助于缩短令牌的有效期并尽可能减少攻击面。

```bash
LegacyServiceAccountTokenCleanUp=true|false (BETA - default=true)
ServiceAccountTokenJTI=true|false (ALPHA - default=false)
ServiceAccountTokenNodeBinding=true|false (ALPHA - default=false)
ServiceAccountTokenNodeBindingValidation=true|false (ALPHA - default=false)
ServiceAccountTokenPodNodeInfo=true|false (ALPHA - default=false)
```

## Kubelet 资源指标达到 GA

这是一个历史悠久的 KEP。从最初的提案到 GA，花了 5 年的时间，在此期间发生了许多有趣的事情。这次涉及的主要部分是以下指标：

* container_cpu_usage_seconds_total
* container_memory_working_set_bytes
* container_start_time_seconds
* node_cpu_usage_seconds_total
* node_memory_working_set_bytes
* pod_cpu_usage_seconds_total
* pod_memory_working_set_bytes
* resource_scrape_error

以下是示例的输出：

```
# HELP container_cpu_usage_seconds_total [STABLE] Cumulative cpu time consumed by the container in core-seconds
# TYPE container_cpu_usage_seconds_total counter
container_cpu_usage_seconds_total{container="coredns",namespace="kube-system",pod="coredns-55968cc89d-bhhbx"} 0.195744 1691361886865
# HELP container_memory_working_set_bytes [STABLE] Current working set of the container in bytes
# TYPE container_memory_working_set_bytes gauge
container_memory_working_set_bytes{container="coredns",namespace="kube-system",pod="coredns-55968cc89d-bhhbx"} 1.675264e+07 1691361886865
# HELP container_start_time_seconds [STABLE] Start time of the container since unix epoch in seconds
# TYPE container_start_time_seconds gauge
```


## Kubernetes组件健康状况服务水平指标（SLIs）达到了GA（一般可用）状态。

这个 KEP 的主要目的是允许每个组件暴露自己的健康状态，以便可以基于其健康状态的SLI来计算集群的SLO。

很久以前，在Kubernetes中有一个ComponentStatus，它可以用来查看集群中组件的状态。但正如下面所示，在v1.19中已经被有效地弃用了。

```bash
mohamedbenhassine@k8s-test:~$ kubectl  get cs
Warning: v1 ComponentStatus is deprecated in v1.19+
NAME                 STATUS    MESSAGE   ERROR
scheduler            Healthy   ok        
etcd-0               Healthy   ok        
controller-manager   Healthy   ok 

```

我们希望使用这个KEP来使用每个组件的健康状态作为SLI，收集和聚合它，并计算集群的SLO。然后可以提供一个SLA。（对于对它们之间的关系感兴趣的朋友可以搜索相关内容）

下面是一个示例的输出：

```bash
test@mohamedbenhassine:/$ kubectl get --raw "/metrics/slis"
# HELP kubernetes_healthcheck [STABLE] This metric records the result of a single healthcheck.
# TYPE kubernetes_healthcheck gauge
kubernetes_healthcheck{name="etcd",type="healthz"} 1
kubernetes_healthcheck{name="etcd",type="livez"} 1
kubernetes_healthcheck{name="etcd",type="readyz"} 1
kubernetes_healthcheck{name="etcd-readiness",type="readyz"} 1
kubernetes_healthcheck{name="informer-sync",type="readyz"} 1
kubernetes_healthcheck{name="ping",type="healthz"} 1
kubernetes_healthcheck{name="ping",type="livez"} 1
kubernetes_healthcheck{name="ping",type="readyz"} 1
```

## ReadWriteOncePod 持久卷访问模式升级为稳定状态

在以前的版本中，ReadWriteOnce访问模式允许在共享节点上的多个pod同时读取和写入相同的卷。

随着Kubernetes 1.29的发布，ReadWriteOncePod特性被引入为稳定版本的新增功能。这确保了一个独占于整个集群的pod拥有对持久卷索赔（PVC）的独占读取或写入权限。

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOncePod
  storageClassName: standard
  resources:
    requests:
      storage: 5Gi
```

## 使用matchLabelKeys定义Pod亲和性或反亲和性

这个新的alpha特性通过引入matchLabelKeys增强了PodAffinity/PodAntiAffinity。这个新增功能确保了在滚动更新期间进行更精确的计算，从而基于指定的标签键更好地控制pod的调度。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: teckbootcamps-deployment
spec:
  template:
    spec:
      affinity:
        podAffinity:
          matchLabelKeys:
            - app-2024
```

## KMS v2加密已升级为稳定状态

在Kubernetes版本1.29中，Key Management Service（KMS）v2的稳定性得到了增强。这个更新带来了改进的性能、密钥轮换功能、健康检查和增强的可观察性。这些进步有助于在Kubernetes环境中安全地对API数据进行静态加密。

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: encrypted
provisioner: kubernetes.io/aws-ebs
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

## 移除与云服务提供商的内置集成（KEP-2395）

在Kubernetes 1.29中，默认配置涉及在没有内置与云服务提供商的集成的情况下运行。用户可以灵活地启用外部云控制器管理器，或通过使用相关的功能开关恢复到传统的集成。

```bash
kubeadm init --cloud-provider=external
```

## Kubernetes 1.29上的已知问题

Evented PLEG此功能在v1.27中升级为Beta版，但在测试新版本时发现了许多问题，因此它现在默认情况下已禁用，并将在社区修复后再次启用。

**建议在v1.29中首先关闭此功能**

## 其他Kubernetes 1.29特性

- KEP-2495: PV/PVC ReadWriteOncePod达到GA状态
- [NodeExpandSecret](https://github.com/kubernetes/enhancements/issues/3107)特性达到GA状态
- kube-proxy现在具有一个新的nftables后端