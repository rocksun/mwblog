
<!--
title: 掌握Kubernetes Pod故障排除：高级策略和方案
cover: https://cdn.sanity.io/images/rhzn5s2f/production/e43ddff88e75e373ce94de0bf9436333ed554f5e-1200x627.jpg?w=1230&fit=max&auto=format
-->

Kubernetes（K8s）部署通常会带来各种角度的挑战，包括 pod、服务、ingress、无响应集群、控制平面和高可用性设置。Kubernetes [pod](/kubernetes-glossary/pod) 是 Kubernetes 生态系统中最小的可部署单元，封装了一个或多个共享资源和网络的容器。Pod 旨在运行应用程序或进程的单个实例，并根据需要创建和处置。Pod 对于在 K8s 环境中扩展、更新和维护应用程序至关重要。

> 译自 [Master Kubernetes Pods: Advanced Troubleshooting Strategies](https://www.getambassador.io/blog/kubernetes-pods-troubleshooting-advanced-strategies)，作者 None。

本文探讨了 Kubernetes pod 面临的挑战以及要采取的故障排除步骤。运行 Kubernetes pod 时遇到的部分错误消息包括：

- ImagePullBackoff
- ErrImagePull
- InvalidImageName
- CrashLoopBackOff

有时，您甚至不会遇到列出的错误，但仍会发现您的 pod 失败。首先，需要注意的是，在调试任何 Kubernetes 资源时，您都应该了解 [API 参考](https://kubernetes.io/docs/reference/)。它解释了如何定义各种 Kubernetes API 以及 pod/部署中的多个对象如何工作。文档在 [Kubernetes 网站](https://kubernetes.io/docs/reference/)上的 API 参考中定义得很明确。在这种情况下，在调试 pod 时，从 API 参考中选择 pod 对象以详细了解 pod 的工作原理。它定义了进入 pod 的字段，即版本、类型、元数据、规范和状态。Kubernetes 还提供了一个[作弊小炒](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)，其中包含所需命令的指南。

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
➜ ~ kubectl create deploy nginx --image=nginxdeployment.apps/nginx created
```

Pod 正在运行后，获取 pod 名称：

```
➜ ~ kubectl get pods
NAME READY STATUS RESTARTS AGE
nginx-8f458dc5b-hcrsh 1/1 Running 0 100s
```

复制正在运行的 pod 的名称并获取有关它的更多信息：

```
➜ ~ kubectl describe pod nginx-8f458dc5b-hcrsh
Name:             nginx-8f458dc5b-hcrsh
hable:NoExecute op=Exists for 300s
Events:
 Type    Reason     Age    From               Message
 ----    ------     ----   ----               -------
 Normal  Scheduled  2m43s  default-scheduler  Successfully assigned default/nginx-8f458dc5b-hcrsh to k8s-troubleshooting-control-plane
 Normal  Pulling    2m43s  kubelet            Pulling image "nginx"
 Normal  Pulled     100s   kubelet            Successfully pulled image "nginx" in 1m2.220189835s
 Normal  Created    100s   kubelet            Created container nginx
 Normal  Started    100s   kubelet            Started container nginx
```

镜像已成功拉取。您的 Kubernetes pod 正在运行，没有错误。

要演示 ImagePullBackoff，请编辑部署 YAML 文件并指定一个不存在的镜像：

```
➜ kubectl edit deploy nginx
 containers:
 -image: nginxdoestexist
  imagePullPolicy: Always
  name: nginx
```

新 pod 未成功部署

```
➜ ~ kubectl get pods
NAME READY STATUS RESTARTS AGE
nginx-5b847fdb95-mx4pq 0/1 ErrImagePull 0 3m40s
nginx-8f458dc5b-hcrsh 1/1 Running 0 38m
```

显示 ImagePullBackoff 错误

```
➜  ~ kubectl describe pod nginx-6f46cbfbcb-c92bl
Events:
 Type     Reason     Age                From               Message
 ----     ------     ----               ----               -------
 Normal   Scheduled  88s                default-scheduler  Successfully assigned default/nginx-6f46cbfbcb-c92bl to k8s-troubleshooting-control-plane
 Normal   Pulling    40s (x3 over 88s)  kubelet            Pulling image "nginxdoesntexist"
 Warning  Failed     37s (x3 over 85s)  kubelet            Failed to pull image "nginxdoesntexist": rpc error: code = Unknown desc = failed to pull and unpack image "docker.io/library/nginxdoesntexist:latest": failed to resolve reference "docker.io/library/nginxdoesntexist:latest": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
 Warning  Failed     37s (x3 over 85s)  kubelet            Error: ErrImagePull
 Normal   BackOff    11s (x4 over 85s)  kubelet            Back-off pulling image "nginxdoesntexist"
 Warning  Failed     11s (x4 over 85s)  kubelet            Error: ImagePullBackOff
```

## Kubernetes Pod 错误 - 已拉取镜像但 Pod 处于 pending 状态。

每当你在生产环境中运行 K8s 时，K8s 管理员会根据集群内运行的命名空间的要求为每个命名空间分配资源配额。命名空间用于在集群内进行逻辑分离。

当资源配额中的规范不满足 Pod 中应用程序的最低要求时，就会抛出“Image pulled, but the pod is still pending”错误。在以下示例中，创建一个名为 payments 的命名空间：

```
➜ ~ kubectl create ns payments

namespace/payments created
```

使用相关规范创建资源配额

```
➜  ~ cat resourcequota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
 name: compute-resources
spec:
 hard:
   requests.cpu: "1"
   requests.memory: 1Gi
   limits.cpu: "2"
   limits.memory: 4Gi
```

将资源配额分配给命名空间 payments

```
➜ ~ kubectl apply -f resourcequota.yaml -n paymentsresourcequota/compute-resources created
```

已创建资源配额/compute-resources

在具有资源配额限制的命名空间内创建新部署：

```
kubectl create deploy nginx --image=nginx -n paymentsdeployment.apps/nginx created
```

尽管已成功创建部署，但没有 Pod 存在：

```
➜ ~ kubectl get pods -n payments

No resources found in payments namespace
```

已创建部署，但是没有处于准备状态的 Pod，没有更新的 Pod，也没有可用的 Pod：

```
➜  ~ kubectl get deploy -n payments
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx   0/1     0            0           7m4s
```

要进一步调试，请描述 nginx 部署。Pod 创建失败：

```
➜  ~ kubectl describe deploy nginx -n payments
Name:                   nginx
Namespace:              payments
CreationTimestamp:      Wed, 24 May 2023 21:37:55 +0300
Labels:                 app=nginx
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=nginx
Replicas:               1 desired | 0 updated | 0 total | 0 available | 1 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
 Labels:  app=nginx
 Containers:
  nginx:
   Image:        nginx
   Port:         <none>
   Host Port:    <none>
   Environment:  <none>
   Mounts:       <none>
 Volumes:        <none>
Conditions:
 Type             Status  Reason
 ----             ------  ------
 Available        False   MinimumReplicasUnavailable
 ReplicaFailure   True    FailedCreate
 Progressing      False   ProgressDeadlineExceeded
OldReplicaSets:    <none>
NewReplicaSet:     nginx-8f458dc5b (0/1 replicas created)
Events:
 Type    Reason             Age   From                   Message
 ----    ------             ----  ----                   -------
 Normal  ScalingReplicaSet  10m   deployment-controller  Scaled up replica set nginx-8f458dc5b to 1
```

从 Kubernetes 事件进行的进一步分析显示 Pod 创建所需的内存不足。

```
➜ ~ kubectl get events --sort-by=/metadata.creationTimestamp
```

当你的镜像已成功拉取，并且你的容器已创建，但你的运行时配置失败时，就会发生此错误。例如，如果你有一个正在尝试写入不存在的文件夹或没有写入该文件夹的权限的正在工作的 Python 应用程序。最初，应用程序会执行，然后遇到错误。如果你的应用程序逻辑中出现 panic ，则容器将停止。容器将进入 CrashLoopBackOff。最终，你观察到部署没有 Pod，即存在一个 Pod，但它没有运行并抛出 CrashLoopbackoff 错误。

## 存活和就绪探测失败

存活（Liveness）探测检测 Pod 是否已进入损坏状态且无法再提供流量。Kubernetes 将为您重新启动 Pod。就绪（readiness ）探测检查您的应用程序是否已准备好处理流量。就绪探测确保您的应用程序从配置映射中提取所有必需的配置并启动其线程。只有完成此过程后，您的应用程序才准备好接收流量。如果您的应用程序在此过程中遇到错误，它也会进入 CrashLoopBackoff。

## 开始故障排除！

本文概述了 Kubernetes Pod 的故障排除技术。它解决了在部署 Pod 时遇到的常见错误，并提供了解决这些错误的实用解决方案。它还深入了解了在理解 Kubernetes 工作原理和有效识别和解决问题时至关重要的参考页面和备忘单。通过遵循本文中提供的指导，读者可以提高他们的故障排除技能，并简化其 Kubernetes Pod 的部署和管理。