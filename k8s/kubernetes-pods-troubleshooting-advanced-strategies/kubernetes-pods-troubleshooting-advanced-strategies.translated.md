# 掌握 Kubernetes Pod 故障排除：高级策略和解决方案

![](https://cdn.sanity.io/images/rhzn5s2f/production/e43ddff88e75e373ce94de0bf9436333ed554f5e-1200x627.jpg?w=1450&fit=max&auto=format)

## 先决条件

- [Kubernetes Pod 错误 - ImagePullBackoff](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__617bec3157e1)
- [Kubernetes Pod 错误 - 已拉取镜像，但 pod 处于待处理状态。](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__739dc6a05bde)
- [存活探测和就绪探测失败](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__bb3376ad6f37)
- [开始故障排除！](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__88ceac778110)

## Kubernetes（K8s）部署的挑战

Kubernetes（K8s）部署通常会带来各种角度的挑战，包括 pod、服务、入口、无响应集群、控制平面和高可用性设置。Kubernetes [pod](/kubernetes-glossary/pod) 是 Kubernetes 生态系统中最小的可部署单元，封装了一个或多个共享资源和网络的容器。Pod 旨在运行应用程序或进程的单个实例，并根据需要创建和处置。Pod 对于在 K8s 环境中扩展、更新和维护应用程序至关重要。

## Kubernetes Pod 故障排除

本文探讨了 Kubernetes pod 面临的挑战以及要采取的故障排除步骤。运行 Kubernetes pod 时遇到的部分错误消息包括：

- ImagePullBackoff
- ErrImagePull
- InvalidImageName
- CrashLoopBackOff

有时，您甚至不会遇到列出的错误，但仍会发现您的 pod 失败。首先，需要注意的是，在调试任何 Kubernetes 资源时，您都应该了解 [API 参考](https://kubernetes.io/docs/reference/)。它解释了如何定义各种 Kubernetes API 以及 pod/部署中的多个对象如何工作。文档在 [Kubernetes 网站](https://kubernetes.io/docs/reference/) 上的 API 参考中定义得很明确。在这种情况下，在调试 pod 时，从 API 参考中选择 pod 对象以详细了解 pod 的工作原理。它定义了进入 pod 的字段，即版本、类型、元数据、规范和状态。Kubernetes 还提供了一个 [备忘单](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)，其中包含所需命令的指南。

## 先决条件

本文假设读者具备以下条件：

- 已安装 [Kind](https://github.com/kubernetes-sigs/kind) 以进行场景演示
- 对 Kubernetes 架构有中级了解
- [Kubectl](https://kubernetes.io/docs/reference/kubectl/) 命令行工具

## Kubernetes Pod 错误 - ImagePullBackoff

该错误显示有三个不同的原因：

- 无效镜像
- 无效标签
- 无效权限

当您没有有关镜像的正确信息时，就会出现这些情况。您可能也没有从其存储库（私有存储库）中提取镜像的权限。为了在下面的示例中演示这一点，我们创建了一个 nginx 部署：

```
â ~ kubectl create deploy nginx --image=nginxdeployment.apps/nginx created
```

Pod 正在运行后，获取 pod 名称：

```
â ~ kubectl get pods
NAME READY STATUS RESTARTS AGE
nginx-8f458dc5b-hcrsh 1/1 Running 0 100s
```

复制正在运行的 pod 的名称并获取有关它的更多信息：

```
â ~ kubectl describe pod nginx-8f458dc5b-hcrsh
Name: nginx-8f458dc5b-hcrsh
Namespace: default
Priority: 0
Node: k8s-troubleshooting-control-plane
Start Time: Thu, 23 Jun 2022 12:33:12 +0000
Labels: app=nginx
Annotations: kubectl.kubernetes.io/last-applied-configuration:
  {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"app":"nginx"},"name":"nginx","namespace":"default"},"spec":{"selector":{"matchLabels":{"app":"nginx"}},"template":{"metadata":{"labels":{"app":"nginx"}},"spec":{"containers":[{"image":"nginxdeployment.apps/nginx","imagePullPolicy":"Always","name":"nginx"}]}}}}
Status: Running
IP: 10.244.0.10
IPs: 10.244.0.10
Controlled By: ReplicaSet/nginx-8f458dc5b
Containers:
  nginx:
    Container ID: docker://7505024832225349120
    Image: nginxdeployment.apps/nginx
    Image ID: docker-pullable://nginxdeployment.apps/nginx@sha256:0123456789abcdef0123456789abcdef0123456789abcdef
    Port: 80/TCP
    Host Port: 0/TCP
    State: Running
      Started: Thu, 23 Jun 2022 12:33:13 +0000
    Ready: True
    Restart Count: 0
    Liveness: http-get http://:80/ delay=1s timeout=1s period=10s #success=1 #failure=3
    Readiness: http-get http://:80/ delay=1s timeout=1s period=10s #success=1 #failure=3
    Environment: <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-2999 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  default-token-2999:
    Type: Secret (a volume populated by a Secret)
    SecretName: default-token-2999
    Optional: false
Events:
  Type    Reason     Age   From               Message
  ----    ------     ---   ----               -------
  Normal  Scheduled  2m43s  default-scheduler  Successfully assigned default/nginx-8f458dc5b-hcrsh to k8s-troubleshooting-control-plane
  Normal  Pulling    2m43s  kubelet            Pulling image "nginx"
  Normal  Pulled    100s   kubelet            Successfully pulled image "nginx" in 1m2.220189835s
  Normal  Created    100s   kubelet            Created container nginx
  Normal  Started    100s   kubelet            Started container nginx
```

镜像已成功拉取。您的 Kubernetes pod 正在运行，没有错误。

要演示 ImagePullBackoff，请编辑部署 YAML 文件并指定一个不存在的镜像：

```
â kubectl edit deploy nginx
```

```
containers:
- image: nginxdoestexist
  imagePullPolicy: Always
  name: nginx
```

新 pod 未成功部署

```
â ~ kubectl get pods
NAME READY STATUS RESTARTS AGE
nginx-5b847fdb95-mx4pq 0/1 ErrImagePull 0 3m40s
nginx-8f458dc5b-hcrsh 1/1 Running 0 38m
```

显示 ImagePullBackoff 错误
**Kubernetes Pod 错误 - 已拉取镜像，但 Pod 处于待处理状态**

每当你在生产环境中运行 K8s 时，K8s 管理员会根据集群内运行的命名空间的要求为每个命名空间分配资源配额。命名空间用于在集群内进行逻辑分离。

当资源配额中的规范不满足 Pod 中应用程序的最低要求时，就会抛出“已拉取镜像，但 Pod 仍处于待处理状态”错误。在以下示例中，创建一个名为 payments 的命名空间：

```
kubectl create ns payments
```

已创建命名空间/payments

使用相关规范创建资源配额

```
cat resourcequota.yamlapiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    requests.cpu: "1"
    requests.memory: 1G
    limits.cpu: "2"
    limits.memory: 4Gi
```

将资源配额分配给命名空间 payments

```
kubectl apply -f resourcequota.yaml -n payments
```

已创建资源配额/compute-resources

在具有资源配额限制的命名空间内创建新部署：

```
kubectl create deploy nginx --image=nginx -n payments
```

已创建部署。apps/nginx

尽管已成功创建部署，但没有 Pod 存在：

```
kubectl get pods -n payments
```

在 payments 命名空间中未找到任何资源。

已创建部署，但没有 Pod 处于就绪状态，没有 Pod 为最新状态，也没有 Pod 可用：

```
kubectl get deploy -n payments
```

| 名称 | 就绪 | 最新 | 可用 | 年龄 |
|---|---|---|---|---|
| nginx | 0/1 | 0 | 0 | 7m4s |

要进一步调试，请描述 nginx 部署。Pod 创建失败：

```
kubectl describe deploy nginx -n payments
```

名称：nginx
命名空间：payments
创建时间戳：2023 年 5 月 24 日星期三 21:37:55 +0300
标签：app=nginx
注释：deployment.kubernetes.io/revision: 1
选择器：app=nginx
副本：1 个所需 | 0 个已更新 | 0 个总计 | 0 个可用 | 1 个不可用
策略类型：滚动更新
MinReadySeconds：0
滚动更新策略：25% 最大不可用，25% 最大激增
Pod 模板：
标签：app=nginx
容器：nginx：
镜像：nginx
端口：<无>
主机端口：<无>
环境：<无>
挂载：<无>
卷：<无>
条件：
| 类型 | 状态 | 原因 |
|---|---|---|
| 可用 | False | MinimumReplicasUnavailable |
| 副本故障 | True | FailedCreate |
| 正在进行 | False | ProgressDeadlineExceeded |
旧副本集：<无>
新副本集：nginx-8f458dc5b（已创建 0/1 个副本）
事件：
| 类型 | 原因 | 时间 | 来源 | 消息 |
|---|---|---|---|---|
| 正常 | 缩放副本集 | 10m | deployment-controller | 已将副本集 nginx-8f458dc5b 扩展到 1 |

从 Kubernetes 事件进行的进一步分析显示 Pod 创建所需的内存不足。

```
kubectl get events --sort-by=/metadata.creationTimestamp
```

**Kubernetes Pod 错误 - CrashLoopBackOff**

当你的镜像已成功拉取，并且你的容器已创建，但你的运行时配置失败时，就会发生此错误。例如，如果你有一个正在尝试写入不存在的文件夹或没有写入该文件夹的权限的正在工作的 Python 应用程序。最初，应用程序会执行，然后遇到错误。如果你的应用程序逻辑中出现恐慌，则容器将停止。容器将进入 CrashLoopBackOff。最终，你观察到部署没有 Pod，即存在一个 Pod，但它没有运行并抛出 CrashLoopbackoff 错误。

**存活和就绪探测失败**
**存活探测和就绪探测**

* **存活探测**检测 Pod 是否已进入损坏状态且无法再提供流量。Kubernetes 将为您重新启动 Pod。
* **就绪探测**检查您的应用程序是否已准备好处理流量。就绪探测确保您的应用程序从配置映射中提取所有必需的配置并启动其线程。只有完成此过程后，您的应用程序才准备好接收流量。如果您的应用程序在此过程中遇到错误，它也会进入 CrashLoopBackoff。

## 开始故障排除！

本文概述了 Kubernetes Pod 的故障排除技术。它解决了在部署 Pod 时遇到的常见错误，并提供了解决这些错误的实用解决方案。它还深入了解了在理解 Kubernetes 工作原理和有效识别和解决问题时至关重要的参考页面和备忘单。通过遵循本文中提供的指导，读者可以提高他们的故障排除技能，并简化其 Kubernetes Pod 的部署和管理。