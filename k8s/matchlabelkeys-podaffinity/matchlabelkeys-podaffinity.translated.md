# Kubernetes 1.31：PodAffinity 中的 MatchLabelKeys 升级至 Beta 版

Kubernetes 1.29 引入了新的字段 `MatchLabelKeys` 和 `MismatchLabelKeys`，用于 PodAffinity 和 PodAntiAffinity。

在 Kubernetes 1.31 中，此功能升级至 Beta 版，相应的特性门控 (`MatchLabelKeysInPodAffinity`) 默认启用。

`MatchLabelKeys`
- 增强滚动更新的灵活调度
在工作负载（例如 Deployment）的滚动更新期间，集群中可能同时存在多个版本的 Pod。
但是，调度器无法根据 PodAffinity 或 PodAntiAffinity 中指定的 `LabelSelector` 区分旧版本和新版本。因此，它将根据 Pod 的版本进行共同定位或分散。

这会导致次优的调度结果，例如：

- 新版本 Pod 与旧版本 Pod 共同定位（PodAffinity），这些旧版本 Pod 最终将在滚动更新后被删除。
- 旧版本 Pod 分布在所有可用拓扑中，阻止新版本 Pod 由于 PodAntiAffinity 找不到节点。
`MatchLabelKeys` 是 Pod 标签键的集合，可以解决此问题。
调度器从新 Pod 的标签中查找这些键的值，并将它们与 `LabelSelector` 结合起来，以便 PodAffinity 匹配标签中具有相同键值对的 Pod。
通过在 `MatchLabelKeys` 中使用标签 [pod-template-hash](/docs/concepts/workloads/controllers/deployment/#pod-template-hash-label)，可以确保仅评估相同版本的 Pod 的 PodAffinity 或 PodAntiAffinity。

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: application-server
  ...
affinity:
  podAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchExpressions:
        - key: app
          operator: In
          values:
          - database
      topologyKey: topology.kubernetes.io/zone
      matchLabelKeys:
      - pod-template-hash
```
上面的 matchLabelKeys 将在 Pod 中被翻译为：

```
kind: Pod
metadata:
  name: application-server
  labels:
    pod-template-hash: xyz
  ...
affinity:
  podAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchExpressions:
        - key: app
          operator: In
          values:
          - database
        - key: pod-template-hash # 从 matchLabelKeys 添加；只有来自相同副本集的 Pod 才会匹配此亲和性。
          operator: In
          values:
          - xyz
      topologyKey: topology.kubernetes.io/zone
      matchLabelKeys:
      - pod-template-hash
```
`MismatchLabelKeys`
- 服务隔离
`MismatchLabelKeys` 是 Pod 标签键的集合，类似于 `MatchLabelKeys`，它从新 Pod 的标签中查找这些键的值，并将它们与 `LabelSelector` 合并为 `key notin (value)`，以便 PodAffinity *不* 匹配标签中具有相同键值对的 Pod。
假设每个租户的所有 Pod 都通过控制器或 Helm 等清单管理工具获得 `tenant` 标签。

虽然在编写每个工作负载的清单时 `tenant` 标签的值未知，但集群管理员希望为租户隔离实现独占的 1:1 租户到域的放置。

`MismatchLabelKeys` 适用于此用例；
通过使用变异 Webhook 全局应用以下亲和性，集群管理员可以确保来自同一租户的 Pod 独占地位于同一域上，这意味着来自其他租户的 Pod 不会位于同一域上。
```
affinity:
  podAffinity: # 确保此租户的 Pod 落在同一个节点池中
    requiredDuringSchedulingIgnoredDuringExecution:
    - matchLabelKeys:
      - tenant
      topologyKey: node-pool
  podAntiAffinity: # 确保只有来自此租户的 Pod 落在同一个节点池中
    requiredDuringSchedulingIgnoredDuringExecution:
    - mismatchLabelKeys:
      - tenant
      labelSelector:
        matchExpressions:
        - key: tenant
          operator: Exists
      topologyKey: node-pool
```
上面的 matchLabelKeys 和 mismatchLabelKeys 将被翻译为：

```
kind: Pod
metadata:
  name: application-server
  labels:
    tenant: service-a
  spec:
    affinity:
      podAffinity: # 确保此租户的 Pod 落在同一个节点池中
        requiredDuringSchedulingIgnoredDuringExecution:
        - matchLabelKeys:
          - tenant
          topologyKey: node-pool
          labelSelector:
            matchExpressions:
            - key: tenant
              operator: In
              values:
              - service-a
      podAntiAffinity: # 确保只有来自此租户的 Pod 落在同一个节点池中
        requiredDuringSchedulingIgnoredDuringExecution:
        - mismatchLabelKeys:
          - tenant
          labelSelector:
            matchExpressions:
            - key: tenant
              operator: Exists
            - key: tenant
              operator: NotIn
              values:
              - service-a
          topologyKey: node-pool
```
## 参与进来
这些功能由 Kubernetes [SIG Scheduling](https://github.com/kubernetes/community/tree/master/sig-scheduling) 管理。

请加入我们并分享您的反馈。我们期待您的来信！

## 如何了解更多？
[PodAffinity 的官方文档](/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) [KEP-3633：在 PodAffinity 和 PodAntiAffinity 中引入 MatchLabelKeys 和 MismatchLabelKeys](https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/3633-matchlabelkeys-to-podaffinity/README.md#story-2)