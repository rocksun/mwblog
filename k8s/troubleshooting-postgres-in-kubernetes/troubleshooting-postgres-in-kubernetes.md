<!--
title: Kubernetes中PostgreSQL的故障诊断
cover: ./cover.png
-->

在 Crunchy Data 担任解决方案架构师的角色中，我帮助客户使用 [Crunchy Postgres for Kubernetes](https://www.crunchydata.com/products/crunchy-postgresql-for-kubernetes)（CPK）快速上手。在 Kubernetes 中安装和管理 Postgres 集群从未如此简单。然而，有时事情不会按计划进行，我注意到一些 Kubernetes 安装可能出现问题的主要领域。今天，我想逐步介绍一些人们在尝试在 Kubernetes 中运行 Postgres 时经常遇到的常见问题，并提供一些基本的故障排除思路以便入门。当然，您的问题可能不在这里，但如果您只是想诊断安装失败或群集故障，这是我首选的入门故障排除清单。

> 译自 [Kubernetes Troubleshooting Postgres in Kubernetes](https://www.crunchydata.com/blog/troubleshooting-postgres-in-kubernetes)。作者 Bob Pacheco 。

## 事物的顺序：CRD、Operator、Cluster、Pod

让我们从对事物是如何安装以及由谁安装的基本理解开始。您可以利用这些知识来确定在安装过程中未出现您期望的内容时首先查看何处。

**自定义资源定义（CRD）**：CPK Operator 需要一个自定义资源定义（CRD）。每个 Operator 可以拥有多个 CRD。我们最新的 Operator 版本，5.5，包含了 3 个 CRD 示例，其中之一是 postgres-operator.crunchydata.com_postgresclusters.yaml。用户将所有 CRD 文件应用于 Kubernetes 集群。在安装 Operator 之前，必须先安装 CRD。

**Operator**：用户通过应用 manager.yaml 文件来安装 CPK Operator，该文件描述了一种 [kind:Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) 的 Kubernetes 对象。这将创建 Deployment，而 Deployment 又会创建 Operator Pod。Operator 本身是运行在 Pod 中的容器。

**Postgres Cluster**：CPK Postgres Cluster 通常由用户应用包含 PostgresCluster.spec 描述的 postgres.yaml 文件创建，该文件描述了一种 [kind:PostgresCluster](https://access.crunchydata.com/documentation/postgres-operator/latest/references/crd/5.5.x/postgrescluster) 的 Kubernetes 对象。

**Pods**：StatefulSets 和 Deployments 创建它们所描述的各个 Pods。Operator 为每个 Postgres Pod 和 pgBackRest repo 主机 Pod（如果适用）创建一个 StatefulSet。还会为 pgBouncer Pods（如果适用）创建 Deployments。如果缺少某个 Pod，请查看拥有该 Pod 的 Deployment 或 StatefulSet 的描述。如果缺少 Deployment 或 StatefulSet，通常可以在 CPK Operator 日志中找到原因。

## 镜像拉取

接下来，让我们看一下镜像拉取问题。有两个主要原因会导致镜像拉取错误。1 - 您没有权限连接到镜像仓库或拉取所请求的镜像。或者 2 - 请求的镜像不在镜像仓库中。

### 权限示例

尝试部署 CPK Operator。

```bash
kubectl apply -n postgres-operator -k install/default --server-side
```

我发现出现了 ImagePullBackOff 错误。

```bash
kubectl -n postgres-operator get pods
NAME                     READY   STATUS           RESTARTS   AGE
pgo-5694b9545c-ggz7g    0/1     ImagePullBackOff   0          27s
```

在 Kubernetes 中，当 Pod 无法启动时，首先要做的是运行 describe 命令查看 Pod 的详细信息，尤其是输出底部的事件。

```bash
kubectl -n postgres-operator describe pod pgo-5694b9545c-ggz7g
...
Events:
  Type     Reason   Age   From     Message
  ----     ------   ----  ----     -------
  Normal   Pulling  6m9s  kubelet  Pulling image "registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.5.0-0"
  Warning  Failed   6m9s  kubelet  Failed to pull image "registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.5.0-0": rpc error: code = Unknown desc = failed to pull and unpack image "registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.5.0-0": failed to resolve reference "registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.5.0-0": failed to authorize: failed to fetch anonymous token: unexpected status from GET request to <https://access.crunchydata.com/api/v1/auth/jwt/container/token/?scope=repository%3Acrunchydata%2Fpostgres-operator%3Apull&service=crunchy-container-registry:> 403 Forbidden
```
查看事件，我们发现尝试从 Crunchy Data 镜像仓库拉取 `crunchydata/postgres-operator:ubi8-5.5.0-0` Pod。在下一个事件条目中看到：`403 Forbidden`。这意味着我们没有权限从此镜像仓库拉取此 Pod。

#### 添加拉取凭据

为了解决问题，我们将创建一个拉取凭据并将其添加到deployment中。您可以在 CPK 文档中找到有关为私有镜像仓库创建拉取凭据的更多信息。

按照文档创建了镜像拉取凭据并将其添加到deployment中。我们应用了这个更改并删除了失败的 Pod。现在我们看到 Pod 被重新创建，并且成功拉取了镜像。

```bash
kubectl apply -n postgres-operator -k install/default --server-side

kubectl -n postgres-operator delete pod pgo-5694b9545c-xnpjg
pod "pgo-5694b9545c-xnpjg" deleted

kubectl -n postgres-operator get pods
NAME                   READY   STATUS    RESTARTS   AGE
pgo-5694b9545c-xnpjg  1/1     Running   0          23s
```

### 镜像不在镜像仓库中的示例

我们再次尝试部署 Operator，发现出现了 ImagePullBackOff 错误。

```bash
kubectl -n postgres-operator get pods
NAME                   READY   STATUS           RESTARTS   AGE
pgo-6bfc9554b7-6h4jd  0/1     ImagePullBackOff   0          22s
```

就像之前一样，我们将 describe Pod 并查看事件以确定发生这种情况的原因：

```bash
kubectl -n postgres-operator describe pod pgo-6bfc9554b7-6h4jd

...
Events:
  Type     Reason   Age   From     Message
  ----     ------   ----  ----     -------
...
  Normal   Pulling  4m30s  kubelet  Pulling image "registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.50.0-0"
  Warning  Failed   4m30s  kubelet  Failed to pull image "registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.50.0-0": rpc error: code = NotFound desc = failed to pull and unpack image "registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.50.0-0": failed to resolve reference "registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.50.0-0": registry.crunchydata.com/crunchydata/postgres-operator:ubi8-5.50.0-0: not found
```

这次我们尝试从 Crunchy Data 镜像仓库拉取 `crunchydata/postgres-operator:ubi8-5.50.0-0` 镜像。然而，未找到该镜像。仔细检查 CPK Operator kustomization.yaml 文件中列出的镜像后，我们发现有一个拼写错误。我们的标签应为 ubi8-5.5.0-0，而不是 ubi8-5.50.0-0。

```yaml
images:
  - name: postgres-operator
    newName: registry.crunchydata.com/crunchydata/postgres-operator
    newTag: ubi8-5.50.0-0
```

#### 更改标签名

我们对文件进行了更正并应用了更改。Pod 将自动使用正确的镜像标签重新创建。

```bash
kubectl apply -n postgres-operator -k install/default --server-side

kubectl -n postgres-operator get pods
NAME                   READY   STATUS    RESTARTS   AGE
pgo-6bfc9554b7-6h4jd  1/1     Running   0          96s
```

通过使用 Kubernetes 的 describe pod 功能，我们能够查看我们为何遇到镜像拉取错误，并轻松纠正它们。

## 资源分配

在排除失败的 Kubernetes 安装问题时，另一个重要的地方是查看资源分配，确保 Pod 具有必要的 CPU 和内存。我在安装时经常看到的最常见问题包括：

- 请求超过了可用的 Kubernetes 节点上的资源。
- 资源请求不足以支持 Pod 中运行的容器的正常操作。

### 资源请求超出可用范围

在这个 postgres.yaml 文件中，我们为我们的 Postgres Pod 设置了一些资源请求和限制。我们请求了 5 个 CPU，并设置了每个 Postgres Pod 的 CPU 限制为 10 个。

```yaml
instances:
  - name: pgha1
    replicas: 2
    resources:
      limits:
        cpu: 10000m
        memory: 256Mi
      requests:
        cpu: 5000m
        memory: 100Mi
```

当我们创建 Postgres 集群并查看 Pod 时，我们发现它们处于挂起状态。

```bash
kubectl apply -n postgres-operator -k high-availability
postgrescluster.postgres-operator.crunchydata.com/hippo-ha created
```

```bash
kubectl -n postgres-operator get pods
NAME                                 READY   STATUS    RESTARTS   AGE
hippo-ha-pgbouncer-7c467748d-tl4pn   2/2     Running   0          103s
hippo-ha-pgbouncer-7c467748d-v6s4d   2/2     Running   0          103s
hippo-ha-pgha1-bzrb-0                0/5     Pending   0          103s
hippo-ha-pgha1-z7nl-0                0/5     Pending   0          103s
hippo-ha-repo-host-0                 2/2     Running   0          103s
pgo-6ccdb8b5b-m2zsc                  1/1     Running   0          48m
```

让我们 describe 其中一个挂起的 Pod 并查看事件：

```bash
kubectl -n postgres-operator describe pod hippo-ha-pgha1-bzrb-0
Name:             hippo-ha-pgha1-bzrb-0
Namespace:        postgres-operator
...
Events:
  Type     Reason             Age                    From                Message
  ----     ------             ----                   ----                -------
  Warning  FailedScheduling   3m41s (x2 over 3m43s)  default-scheduler   0/2 nodes are available: 2 Insufficient cpu. preemption: 0/2 nodes are available: 2 No preemption victims found for incoming pod..
```

我们注意到可用的 CPU 不足以满足我们的请求。因此，我们减少了资源请求和限制，然后再次尝试。

```yaml
instances:
  - name: pgha1
    replicas: 2
    resources:
      limits:
        cpu: 1000m
        memory: 256Mi
      requests:
        cpu: 500m
        memory: 100Mi
```

```bash
kubectl apply -n postgres-operator -k high-availability
postgrescluster.postgres-operator.crunchydata.com/hippo-ha created
```

```bash
kubectl -n postgres-operator get pods
NAME                                 READY   STATUS    RESTARTS   AGE
hippo-ha-backup-jb8t-tgdtx           1/1     Running   0          13s
hippo-ha-pgbouncer-7c467748d-s8wq6   2/2     Running   0          34s
hippo-ha-pgbouncer-7c467748d-zhcmf   2/2     Running   0          34s
hippo-ha-pgha1-hmrq-0                5/5     Running   0          35s
hippo-ha-pgha1-xxtf-0                5/5     Running   0          35s
hippo-ha-repo-host-0                 2/2     Running   0          35s
pgo-6ccdb8b5b-m2zsc                  1/1     Running   0          124m
```

现在我们看到所有的 Pod 都按预期运行。

### 资源Request不足

如果我们没有分配足够的资源会发生什么呢？在这里，我们将 CPU request 和 limit 设置得非常低。我们请求 5m CPU，并将每个 Postgres Pod 的限制设置为 10m CPU。

```yaml
instances:
  - name: pgha1
    replicas: 2
    resources:
      limits:
        cpu: 10m
        memory: 256Mi
      requests:
        cpu: 5m
        memory: 100Mi
```

```bash
kubectl apply -n postgres-operator -k high-availability
postgrescluster.postgres-operator.crunchydata.com/hippo-ha created
```

```bash

kubectl -n postgres-operator get pods
NAME                                 READY   STATUS    RESTARTS      AGE
hippo-ha-pgbouncer-7c467748d-hnf5k   2/2     Running   0             93s
hippo-ha-pgbouncer-7c467748d-q28t9   2/2     Running   0             93s
hippo-ha-pgha1-r2qs-0                4/5     Running   2 (11s ago)   93s
hippo-ha-pgha1-x2ft-0                4/5     Running   2 (8s ago)    93s
hippo-ha-repo-host-0                 2/2     Running   0             93s
pgo-6ccdb8b5b-m2zsc                  1/1     Running   0             136m
```

我们注意到我们的 Postgres Pod 只显示了 4/5 个容器正在运行，且在创建 90 秒后已经重新启动了两次。这清楚地表明出现了问题。让我们查看 Postgres 容器的日志，了解发生了什么。

```bash
kubectl -n postgres-operator logs hippo-ha-pgha1-r2qs-0 -c database
```

我们没有得到任何日志。这表明 Postgres 容器没有启动。现在我们将调整 CPU request 和 limit 为更合理的值，然后再次尝试。通常我不会低于 500m。

```yaml
instances:
  - name: pgha1
    replicas: 2
    resources:
      limits:
        cpu: 1000m
        memory: 256Mi
      requests:
        cpu: 500m
        memory: 100Mi
```

```bash
kubectl apply -n postgres-operator -k high-availability
postgrescluster.postgres-operator.crunchydata.com/hippo-ha created
```

现在我们看到我们的集群正常运行，所有预期的容器都在运行。

```bash
kubectl -n postgres-operator get pods
NAME                              READY   STATUS    RESTARTS   AGE
hippo-ha-backup-pv9n-tr7mh       1/1     Running   0          6s
hippo-ha-pgbouncer-7c467748d-45jj9   2/2   Running   0          33s
hippo-ha-pgbouncer-7c467748d-lqfz2   2/2   Running   0          33s
hippo-ha-pgha1-8kh2-0             5/5     Running   0          34s
hippo-ha-pgha1-v4t5-0             5/5     Running   0          34s
hippo-ha-repo-host-0              2/2     Running   0          33s
pgo-6ccdb8b5b-m2zsc               1/1     Running   0          147m
```

## 存储分配

最后，让我们看一下在为我们的 pods 分配存储时可能遇到的一些常见问题。关于在安装时分配存储的问题，有一些最常见的问题：

- 不正确的资源请求
- 不受支持的存储类

### 不正确的资源请求示例

这是我们要为 postgres.yaml 中的 Postgres 集群 pods 分配的存储的示例：

```yaml
dataVolumeClaimSpec:
  accessModes:
  - 'ReadWriteOnce'
  resources:
    requests:
      storage: 1GB
```

当我们尝试应用清单时，我们在命令行上看到了这个输出：

```bash
k apply -n postgres-operator -k high-availability
The PostgresCluster "hippo-ha" is invalid: spec.instances[0].dataVolumeClaimSpec.resources.requests.storage: Invalid value: "1GB": spec.instances[0].dataVolumeClaimSpec.resources.requests.storage in body should match '^(\\+|-)?(([0-9]+(\\.[0-9]*)?)|(\\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\\+|-)?(([0-9]+(\\.[0-9]*)?)|(\\.[0-9]+))))?
```

"1GB" 的值是无效的。错误消息告诉您错误在清单的 `spec.instances[0].dataVolumeClaimSpec.resources.requests.storage` 部分。消息甚至提供了用于验证的正则表达式。

我们输入有效值 `1Gi` 后，成功部署了我们的 Postgres 集群。请记住，千兆字节必须用 Gi 描述，而兆字节则用 Mi。有关更多语法细节，请参阅 [Kubernetes 文档](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes)。

```yaml
dataVolumeClaimSpec:
  accessModes:
  - 'ReadWriteOnce'
  resources:
    requests:
      storage: 1Gi
  affinity:
```

```bash
kubectl -n postgres-operator get pods
NAME                              READY   STATUS    RESTARTS   AGE
hippo-ha-backup-ngg5-56z7z       1/1     Running   0          10s
hippo-ha-pgbouncer-7c467748d-4q887   2/2   Running   0          35s
hippo-ha-pgbouncer-7c467748d-lc2sr   2/2   Running   0          35s
hippo-ha-pgha1-w9vc-0             5/5     Running   0          35s
hippo-ha-pgha1-zhx8-0             5/5     Running   0          35s
hippo-ha-repo-host-0              2/2     Running   0          35s
pgo-6ccdb8b5b-vzzkp               1/1     Running   0          12m
```

### 不正确的存储类名示例

我们想要为我们的 Postgres 集群 pods 指定一个特定的存储类：

```yaml
dataVolumeClaimSpec:
  storageClassName: foo
  accessModes:
  - 'ReadWriteOnce'
  resources:
    requests:
      storage: 1Gi
```

当我们应用清单时，我们发现我们的 Postgres pods 被卡在 "pending" 状态。

```bash
kubectl -n postgres-operator get pods
NAME                              READY   STATUS    RESTARTS   AGE
hippo-ha-pgbouncer-7c467748d-jxxpf   2/2   Running   0          3m42s
hippo-ha-pgbouncer-7c467748d-wdtvq   2/2   Running   0          3m42s
hippo-ha-pgha1-79gr-0             0/5     Pending   0          3m42s
hippo-ha-pgha1-xv2t-0             0/5     Pending   0          3m42s
hippo-ha-repo-host-0              2/2     Running   0          3m42s
pgo-6ccdb8b5b-vzzkp               1/1     Running   0          24m
```

此时我们不清楚为什么 pods 处于 pending 状态。让我们describe其中一个并查看事件，看看是否能获取更多信息。

```bash
kubectl -n postgres-operator describe pod hippo-ha-pgha1-79gr-0
Name: hippo-ha-pgha1-79gr-0
Namespace: postgres-operator
...
Events:
  Type    Reason            Age    From               Message
  ----    ------            ----   ----               -------
  Normal  NotTriggerScaleUp  31s    (x32 over 5m34s)  cluster-autoscaler pod didn't trigger scale-up:
  Warning FailedScheduling  13s    (x6 over 5m36s)   default-scheduler 0/2 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling..
```

在 describe 的事件中，我们看到 pod 具有未绑定的即时 PersistentVolumeClaims。这是什么意思？这意味着 Kubernetes 无法满足我们的存储需求，因此它保持未绑定状态。如果我们检查 dataVolumeClaimSpec，我们看到我们设置了三个特定的值：

```yaml
dataVolumeClaimSpec:
  storageClassName: foo
  accessModes:
  - 'ReadWriteOnce'
  resources:
    requests:
      storage: 1Gi
```

我们查看 Kubernetes 提供程序中可用的存储类。在这种情况下，我们正在部署在 GKE 上。我们看到我们有 3 个可用的存储类：

![](https://imagedelivery.net/lPM0ntuwQfh8VQgJRu0mFg/79f28a80-978a-4281-3894-ed71a9c5ac00/public)

我们删除失败的集群部署：

```bash
kubectl delete -n postgres-operator -k high-availability postgrescluster.postgres-operator.crunchydata.com "hippo-ha"
```

更新清单中的 storageClassName 为受支持的存储类并应用它。

```yaml
dataVolumeClaimSpec:
  storageClassName: standard-rwo
  accessModes:
  - 'ReadWriteOnce'
  resources:
    requests:
      storage: 1Gi
```

```bash
kubectl apply -n postgres-operator -k high-availability configmap/db-init-sql created postgrescluster.postgres-operator.crunchydata.com/hippo-ha created
```

现在我们看到所有的 pods 都已经正常运行。

```bash
kubectl -n postgres-operator get pods
NAME                                READY   STATUS    RESTARTS   AGE
hippo-ha-backup-jstq-c8n67         1/1     Running   0          6s
hippo-ha-pgbouncer-7c467748d-5smt9 2/2     Running   0          31s
hippo-ha-pgbouncer-7c467748d-6vb7t 2/2     Running   0          31s
hippo-ha-pgha1-9s2g-0               5/5     Running   0          32s
hippo-ha-pgha1-drmv-0               5/5     Running   0          32s
hippo-ha-repo-host-0                2/2     Running   0          32s
pgo-6ccdb8b5b-vzzkp                 1/1     Running   0          44m
```

## 我们成功了！

在这篇博客中，我们成功地识别、诊断和纠正了在 Kubernetes 中安装 Postgres 时可能出现的常见问题。我们学会了如何使用 Kubernetes 的 describe 函数来获取信息，帮助我们诊断遇到的问题。这里学到的经验不仅适用于 Postgres。如果清单不正确或未分配适当的资源，这些问题可能发生在 Kubernetes 中运行的任何应用程序上。恭喜！您现在拥有解决常见安装问题所需的知识。
