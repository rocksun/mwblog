
<!--
title: Kubernetes故障排除手册
cover: https://miro.medium.com/v2/resize:fit:1200/1*gUfOtR-2j22T3yNXtYI0rQ.png
-->

调试 Kubernetes 应用程序就像在迷宫中导航。由于其分布式特性和众多组件，在 Kubernetes 中识别和解决问题需要一套强大的工具和技术。

> 译自 [The Kubernetes Troubleshooting Handbook](https://itnext.io/the-kubernetes-troubleshooting-handbook-7596a1fdf2ff)，作者 Piotr。

在本博文中，我们将探讨各种技术和工具，以帮助您进行 Kubernetes 故障排除和调试。无论您是经验丰富的 Kubernetes 用户还是刚入门，本指南都将为您提供有关高效调试实践的宝贵见解。

虽然在本博文中，我尽力根据我的经验汇编有用的建议，但权威的真相来源始终是[官方 Kubernetes 文档](https://kubernetes.io/docs/home/)。

## 分析 Pod 生命周期事件

了解 Pod 的生命周期对于调试和维护在 Kubernetes 中运行的应用程序至关重要。每个 Pod 都要经历从创建到终止的几个阶段，分析这些事件可以帮助您识别和解决问题。

### Pod 生命周期阶段

Kubernetes 中的 Pod 会经历以下阶段：

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*cxZIFOhlnbOwfm78IKXt0g.png)

**使用 `kubectl get` 和 `kubectl describe`**


要分析 Pod 的生命周期事件，您可以使用 `kubectl get` 和 `kubectl describe` 命令。

`kubectl get` 命令提供 Pod 状态的高级概述：

```
kubectl get pods
```

输出：

```
NAME READY STATUS RESTARTS AGE
web-server-pod 1/1 Running 0 5m
db-server-pod 1/1 Pending 0 2m
cache-server-pod 1/1 Completed 1 10m
```

此输出显示每个 Pod 的当前状态，这可以帮助您识别需要进一步调查的 Pod。

`kubectl describe` 命令提供有关 Pod 的详细信息，包括其生命周期事件：

```
kubectl describe pod <pod-name>
```

输出片段：

```
Name:           web-server-pod
Namespace:      default
Node:           node-1/192.168.1.1
Start Time:     Mon, 01 Jan 2024 10:00:00 GMT
Labels:         app=web-server
Status:         Running
IP:             10.244.0.2
Containers:
  web-container:
    Container ID:   docker://abcdef123456
    Image:          nginx:latest
    State:          Running
      Started:      Mon, 01 Jan 2024 10:01:00 GMT
    Ready:          True
    Restart Count:  0
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  10m   default-scheduler  Successfully assigned default/web-server-pod to node-1
  Normal  Pulled     9m    kubelet, node-1    Container image "nginx:latest" already present on machine
  Normal  Created    9m    kubelet, node-1    Created container web-container
  Normal  Started    9m    kubelet, node-1    Started container web-container
```

### 分析 Pod 事件

`kubectl describe` 输出中的 `Events` 部分提供了 Pod 发生的重大事件的按时间顺序排列的日志。这些事件可以帮助您了解生命周期转换并识别诸如以下问题：

- **调度延迟**：调度 Pod 的延迟可能表明资源限制或调度程序问题。
- **镜像拉取错误**：拉取容器镜像失败可能表明网络问题或容器注册表问题。
- **容器崩溃**：通过检查导致崩溃的事件，可以诊断重复的容器崩溃。

## Kubernetes 事件和审计日志

Kubernetes 生成集群范围的 `kind: Event` 我们可以使用它来快速了解集群中发生的事情。

 另一方面，审计日志 `kind: Policy` 对于确保集群的合规性和安全性很有用。它们可以显示登录尝试、Pod 权限提升等等。

### Kubernetes 事件

Kubernetes 事件提供集群内重大事件的时间线，例如 Pod 调度、容器重启和错误。它们有助于了解状态转换并识别问题的根本原因。

查看事件

要查看集群中的事件，请使用 `kubectl get events` 命令：

```
kubectl get events
```

输出示例：

```
LAST SEEN TYPE REASON OBJECT MESSAGE
12s Normal Scheduled pod/web-server-pod Successfully assigned default/web-server-pod to node-1
10s Normal Pulling pod/web-server-pod Pulling image "nginx:latest"
8s Normal Created pod/web-server-pod Created container web-container
7s Normal Started pod/web-server-pod Started container web-container
5s Warning BackOff pod/db-server-pod Back-off restarting failed container
```

过滤事件

您可以过滤事件以关注特定命名空间、资源类型或时间段。例如，要查看与特定 Pod 相关的事件：

```
kubectl get events --field-selector involvedObject.name=web-server-pod
```

描述资源

`kubectl describe` 命令在其输出中包含事件，提供有关特定资源及其事件历史记录的详细信息：

```
kubectl describe pod web-server-pod
```

输出片段：

```
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  10m   default-scheduler  Successfully assigned default/web-server-pod to node-1
  Normal  Pulled     9m    kubelet, node-1    Container image "nginx:latest" already present on machine
  Normal  Created    9m    kubelet, node-1    Created container web-container
  Normal  Started    9m    kubelet, node-1    Started container web-container
```

### Kubernetes 审计日志

审计日志提供了对所有发送到 Kubernetes API 服务器的 API 请求的详细记录，包括用户、执行的操作和结果。它们对于安全审计和合规性至关重要。

**启用审计日志**

要启用审计日志，请使用适当的标志和审计策略配置 API 服务器。以下是一个审计策略配置示例：

```yaml
# audit-policy.yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Metadata
  resources:
  - group: ""
    resources: ["pods"]
- level: RequestResponse
  users: ["admin"]
  verbs: ["update", "patch"]
  resources:
  - group: ""
    resources: ["configmaps"]
```

**配置 API 服务器**

在启动 API 服务器时指定审计策略文件和日志文件位置：

```bash
kube-apiserver --audit-policy-file=/etc/kubernetes/audit-policy.yaml --audit-log-path=/var/log/kubernetes/audit.log
```

**查看审计日志**

审计日志通常写入文件。您可以使用标准日志分析工具来查看和过滤日志。以下是一个审计日志条目的示例：

```json
{
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Metadata",
    "auditID": "12345",
    "stage": "ResponseComplete",
    "requestURI": "/api/v1/namespaces/default/pods",
    "verb": "create",
    "user": {
        "username": "admin",
        "groups": ["system:masters"]
    },
    "sourceIPs": ["192.168.1.1"],
    "objectRef": {
        "resource": "pods",
        "namespace": "default",
        "name": "web-server-pod"
    },
    "responseStatus": {
        "metadata": {},
        "code": 201
    },
    "requestReceivedTimestamp": "2024-01-01T12:00:00Z",
    "stageTimestamp": "2024-01-01T12:00:01Z"
}
```

## Kubernetes 仪表盘

Kubernetes 仪表盘是一个基于 Web 的 UI，提供了一种简单的方法来管理和排查 Kubernetes 集群。它允许您可视化集群资源、部署应用程序并执行各种管理任务。

### 安装 Kubernetes 仪表盘

有关安装和访问仪表盘的详细信息，请参阅 [kubernetes 文档](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)。

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*sD0LKJ3JeGZ-2AQT7HjdSg.png)

### 使用仪表盘

仪表盘提供各种功能来帮助管理和排查 Kubernetes 集群：

1. **集群概述**: 查看集群的总体状态，包括节点、命名空间和资源使用情况。
2. **工作负载**: 监控和管理工作负载，例如部署、副本集、有状态集和守护进程集。
3. **服务和入口**: 管理服务和入口资源以控制网络流量。
4. **配置和存储**: 管理配置映射、密钥、持久卷声明和其他存储资源。
5. **日志和事件**: 查看日志和事件以进行故障排除和审计。

## 监控资源使用情况

监控资源使用情况有助于您了解应用程序如何消耗资源并确定优化机会。

监控工具

* **kubectl top**: 提供实时资源使用指标。
* **Prometheus**: 收集和存储指标以进行详细分析。
* **Grafana**: 可视化指标并提供用于监控的仪表盘。

使用 kubectl top

`kubectl top` 命令显示了 Pod 和节点的当前 CPU 和内存使用情况。

```bash
kubectl top pods
kubectl top nodes
```

示例输出：

```
NAME        CPU(cores)   MEMORY(bytes)
my-app-pod  100m         120Mi
```

## 使用 kubectl logs

在调试 Kubernetes 应用程序时，`kubectl logs` 是我们武器库中最基本工具之一。此命令有助于从 Pod 中的特定容器中检索日志，使您能够有效地诊断和解决问题。

### 基本用法

检索 Pod 日志的最简单方法是使用 `kubectl logs` 命令，后跟 Pod 名称和命名空间。以下是一个在 `default` 命名空间中运行的 Pod 的基本示例：

```bash
kubectl logs <pod-name>
```

此命令从指定 Pod 中的第一个容器中获取日志。如果您的 Pod 包含多个容器，您还需要指定容器名称：

```bash
kubectl logs <pod-name> -c <container-name>
```

### 使用 `-f` 标志实时获取日志

要实时流式传输日志，类似于 Linux 中的 `tail -f`，请使用 `-f` 标志：

```bash
kubectl logs -f <pod-name>
```

这对于在应用程序运行时监控日志并观察实时进程的输出特别有用。

> 有一些项目增强了日志尾随功能，例如 [stern]。

### 检索以前的日志

如果 Pod 已重新启动，您可以使用 `--previous` 标志查看先前实例的日志：

```bash
kubectl logs <pod-name> --previous
```

这有助于通过检查故障之前的日志来了解导致 Pod 重新启动的原因。

### 使用标签过滤日志

您还可以使用 `kubectl` 以及 `jq` 来过滤与特定标签匹配的 Pod 的日志，以进行高级过滤：

```bash
kubectl get pods -l <label-selector> -o json | jq -r '.items[] | .metadata.name' | xargs -I {} kubectl logs {}
```

将 `<label-selector>` 替换为您的特定标签，例如 `app=myapp`。

### 与其他工具结合使用

您可以将 `kubectl logs` 与其他 Linux 命令结合使用，以增强您的调试过程。例如，要在日志中搜索特定错误消息，可以使用 `grep`：

```
kubectl logs web-server-pod | grep "Error"
```

对于实时日志中的连续搜索：

```
kubectl logs -f web-server-pod | grep --line-buffered "Error"
```

### 实用技巧

**日志轮换和保留**： 确保您的应用程序处理日志轮换，以防止日志占用过多的磁盘空间。

**结构化日志记录**： 使用结构化日志记录（例如 JSON 格式），以便使用 `jq` 等工具更轻松地解析和分析日志。

**集中式日志记录**： 考虑设置集中式日志记录系统（例如 Elasticsearch、Fluentd 和 Kibana - EFK 堆栈）来聚合和搜索来自所有 Kubernetes Pod 的日志。

## 使用 kubectl exec 进行交互式故障排除

`kubectl exec` 允许我们直接在正在运行的容器内执行命令。这对于交互式故障排除特别有用，可以检查容器的环境、运行诊断命令并执行实时修复。

### 基本用法

`kubectl exec` 的基本语法如下：

```
kubectl exec <pod-name> -- <command>
```

要在 Pod 中的特定容器中执行命令，请使用 `-c` 标志。请注意，这将执行命令并立即退出容器。

```
kubectl exec <pod-name> -c <container-name> -- <command>
```

### 运行交互式 Shell

`kubectl exec` 最常见的用途之一是在容器内打开交互式 Shell 会话。这允许您以交互方式运行多个命令。以下是如何操作：

```
kubectl exec -it <pod-name> -- /bin/bash
```

对于使用 `sh` 而不是 `bash` 的容器：

```
kubectl exec -it <pod-name> -- /bin/sh
```

### 示例：检查环境变量

要检查容器内的环境变量，可以使用 `env` 命令：

```
kubectl exec <pod-name> -- env
```

如果您需要检查特定容器中的环境变量：

```
kubectl exec <pod-name> -c <container-name> -- env
```

### 示例：检查配置文件

假设您需要检查容器内的配置文件。您可以使用 `cat` 或容器内可用的任何文本编辑器：

```
kubectl exec <pod-name> -- cat /path/to/config/file
```

对于特定容器：

```
kubectl exec <pod-name> -c <container-name> -- cat /path/to/config/file
```

### 将文件复制到容器和从容器复制文件

如果您在容器中没有需要的二进制文件，可以使用 `kubectl cp` 轻松地将文件复制到容器和从容器复制文件。例如，要将文件从本地机器复制到容器：

```
kubectl cp /local/path/to/file <pod-name>:/container/path/to/file
```

要将文件从容器复制到本地机器：

```
kubectl cp <pod-name>:/container/path/to/file /local/path/to/file
```

### 实用技巧

**使用 `-i` 和 `-t` 标志**： `-i` 标志使会话交互，`-t` 标志分配一个伪终端。`-it` 一起启用完全交互式会话。

**以特定用户身份运行**： 如果需要，使用 `--user` 标志以特定用户身份在容器内执行命令。
```
kubectl exec --user=<username> -it <pod-name> -- /bin/bash
```

**安全注意事项**： 在使用提升的权限运行 `kubectl exec` 时要谨慎。确保您已实施适当的 RBAC（基于角色的访问控制）策略，以防止未经授权的访问。

## 使用 `kubectl debug` 进行节点级调试

大多数调试技术都集中在应用程序级别，但是也可以使用 `kubectl debug node` 命令调试特定 Kubernetes 节点。

节点级调试对于诊断影响 Kubernetes 节点本身的问题至关重要，例如资源耗尽、配置错误或硬件故障。

这样，**调试 Pod 可以访问节点的根文件系统，该文件系统在 Pod 中以 `/*` 形式挂载。**

**创建调试会话**：

使用 `kubectl debug` 命令在节点上启动调试会话。此命令会在指定的节点上创建一个运行调试容器的 Pod。

```
kubectl debug node/<node-name> -it --image=busybox
```

将 `<node-name>` 替换为要调试的节点的名称。`-it` 标志打开交互式终端，`--image=busybox` 指定用于调试容器的镜像。

> 有关更多详细信息，请参阅 [Kubernetes 官方文档关于节点级调试](https://kubernetes.io/docs/tasks/debug/debug-cluster/kubectl-node-debug/)。


## 使用调试容器进行应用程序级调试

对于更复杂的问题，请考虑使用预装工具的调试容器。有很多好的 Docker 镜像包含用于调试的工具和脚本，其中一个我推荐的是 [https://github.com/nicolaka/netshoot](https://github.com/nicolaka/netshoot)。可以使用以下命令快速创建它：

```
kubectl run tmp-shell --rm -i --tty --image nicolaka/netshoot
```

示例：使用调试容器作为 sidecar

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
   name: nginx-netshoot
   labels:
       app: nginx-netshoot
spec:
replicas: 1
selector:
   matchLabels:
       app: nginx-netshoot
template:
   metadata:
   labels:
       app: nginx-netshoot
   spec:
       containers:
       - name: nginx
       image: nginx:1.14.2
       ports:
           - containerPort: 80
       - name: netshoot
       image: nicolaka/netshoot
       command: ["/bin/bash"]
       args: ["-c", "while true; do ping localhost; sleep 60;done"]
```

应用配置：

```
kubectl apply -f debug-pod.yaml
```


### 实用技巧

**设置重启策略**：确保您的 Pod 规范具有适当的重启策略以处理不同的故障场景。

**自动化监控**：使用 Prometheus 和 Alertmanager 设置对关键问题的自动化监控和警报，例如 `CrashLoopBackOff`。

## 用于调试的临时容器

[临时容器](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#ephemeral-container) 是临时的，专门用于调试目的。它们对于运行诊断工具和命令很有用，而不会影响正在运行的应用程序。本章将探讨如何在 Kubernetes 中创建和使用临时 Pod 以进行交互式故障排除。

### 为什么使用临时 Pod？

- **隔离**：在隔离的环境中进行调试可以防止意外更改正在运行的应用程序。
- **工具可用性**：允许使用应用程序容器中可能不存在的专用工具。
- **临时性**：这些 Pod 可以根据需要轻松创建和销毁，而不会对集群造成残留影响。

### 创建临时 Pod

在 Kubernetes 中创建临时 Pod 有多种方法。一种常见的方法是使用 `kubectl run` 命令。

示例：创建临时 Pod

**使用 kubectl run**：

```
kubectl debug mypod -it --image=nicolaka/netshoot
```


此命令使用 `netshoot` 镜像创建一个调试 Pod 并打开一个交互式 shell。

### 使用临时 Pod 的实用技巧

**工具可用性**：确保调试容器镜像包含所有必要的故障排除工具，例如 `curl`、`netcat`、`nslookup`、`df`、`top` 等。

**安全注意事项**：在创建临时 Pod 时要注意安全。确保它们具有有限的访问权限，并且仅由授权人员使用。

### 示例：使用自定义调试容器进行高级调试

让我们逐步了解如何使用自定义调试容器进行高级调试任务。

**使用自定义调试容器创建临时 Pod**：

```
kubectl debug -it redis5 --image=nicolaka/netshoot

Defaulting debug container name to debugger-v4hfv.
If you don't see a command prompt, try pressing enter.
                    dP            dP                           dP
                    88            88                           88
88d888b. .d8888b. d8888P .d8888b. 88d888b. .d8888b. .d8888b. d8888P
88'  `88 88ooood8   88   Y8ooooo. 88'  `88 88'  `88 88'  `88   88
88    88 88.  ...   88         88 88    88 88.  .88 88.  .88   88
dP    dP `88888P'   dP   `88888P' dP    dP `88888P' `88888P'   dP

Welcome to Netshoot! (github.com/nicolaka/netshoot)
Version: 0.13





 redis5  ~ 
```


**运行诊断命令**：

在调试容器中，我们可以运行各种命令。

```
# Check DNS resolution
nslookup kubernetes.default.svc.cluster.local

Server:         10.96.0.10
Address:        10.96.0.10#53

Name:   kubernetes.default.svc.cluster.local
Address: 10.96.0.1
```


## 处理 DNS 和网络问题

现在我们将介绍两种常见的故障排除场景；DNS 问题和有状态 Pod 调试。让我们看看我们在实践中学到了什么。

### 常见的网络问题

- **DNS 解析失败**：无法将服务名称解析为 IP 地址。
- **服务不可达**：集群内无法访问服务。
- **Pod 通信问题**：Pod 无法相互通信。
- **网络策略配置错误**：错误的网络策略阻止了流量。

### 用于故障排除的工具和命令

- **kubectl exec**：在容器中运行命令以诊断网络问题。
- **nslookup**：检查 DNS 解析。
- **ping**：测试 Pod 和服务之间的连接。
- **curl**：验证 HTTP 连接和响应。
- **traceroute**：跟踪数据包到达目的地的路径。

### 示例：诊断 DNS 解析问题

让我们逐步了解如何诊断名为 `my-app-pod` 的 Pod 尝试访问服务 `my-db-service` 时出现的 DNS 解析问题。

**检查 DNS 解析**：

```
kubectl exec -it my-app-pod -- nslookup my-db-service
```


或者，我们可以使用调试 Pod 或临时容器。

指示问题的输出：

```
Server: 10.96.0.10
Address:10.96.0.10#53
** server can't find my-db-service: NXDOMAIN
```

**检查 CoreDNS 日志**：

检查 CoreDNS Pod 的日志以识别任何 DNS 解析问题。

```
kubectl logs -l k8s-app=kube-dns -n kube-system
```

查找指示 DNS 解析失败的错误或警告。

**验证服务和端点**：

确保服务和端点存在并已正确配置。

```
kubectl get svc my-db-service
kubectl get endpoints my-db-service

NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
my-db-serviceClusterIP   10.96.0.11   <none>        5432/TCP   1h

NAME         ENDPOINTS            AGE
my-db-service10.244.0.5:5432      1h
```

**重启 CoreDNS Pod**：
重启 CoreDNS Pod 以解决潜在的瞬态问题。

```kubectl rollout restart deployment coredns -n kube-system```
**再次验证 DNS 解析**：
解决问题后，再次验证 DNS 解析：

```
kubectl exec -it my-app-pod -- nslookup my-db-service
```

预期输出：

```
Server: 10.96.0.10
Address:10.96.0.10#53

Name:   my-db-service.default.svc.cluster.local
Address:10.96.0.11
```
### 实用技巧

**使用网络调试容器**： 使用 `nicolaka/netshoot` 等网络调试容器进行全面的网络故障排除。

```
kubectl run netshoot --rm -it --image nicolaka/netshoot -- /bin/bash
```

**监控网络指标**： 使用 Prometheus 和 Grafana 监控网络指标并为网络问题设置警报。

**实施冗余**： 配置冗余 DNS 服务器和故障转移机制以提高网络可靠性。

## 调试有状态应用程序

Kubernetes 中的有状态应用程序需要针对调试进行特殊考虑，因为它们依赖于持久性存储和跨重启的一致状态。本节将探讨处理和调试有状态应用程序特有问题的方法。

### 什么是有状态应用程序？

有状态应用程序在会话和重启之间维护状态信息，通常使用持久性存储。示例包括数据库、消息队列和其他需要数据持久性的应用程序。

### 有状态应用程序中的常见问题

- **持久性存储问题**： PVC 或 PV 问题会导致数据丢失或不可用。
- **Pod 启动失败**： 由于状态依赖关系，Pod 初始化期间发生错误。
- **网络分区**： 影响有状态 Pod 之间通信的网络问题。
- **数据一致性问题**： 跨副本或重启的数据不一致。

### 示例：调试 MySQL StatefulSet

让我们逐步调试名为 `my-mysql` 的 MySQL StatefulSet 。

**检查 StatefulSet**：

```
kubectl describe statefulset my-mysql
```

输出片段：

```
Name:           my-mysql
Namespace:      default
Selector:       app=my-mysql
Replicas:       3 desired | 3 total
...
Events:
  Type    Reason            Age   From                    Message
  ----    ------            ----  ----                    -------
  Normal  SuccessfulCreate  1m    statefulset-controller  create Pod my-mysql-0 in StatefulSet my-mysql successful
  Normal  SuccessfulCreate  1m    statefulset-controller  create Pod my-mysql-1 in StatefulSet my-mysql successful
  Normal  SuccessfulCreate  1m    statefulset-controller  create Pod my-mysql-2 in StatefulSet my-mysql successful
```

**检查持久卷声明**：

```
kubectl get pvc
kubectl describe pvc data-my-mysql-0
```

输出片段：

```
Name: data-my-mysql-0
Namespace: default
Status: Bound
Volume: pvc-1234abcd-56ef-78gh-90ij-klmnopqrstuv
...
```

**检查 Pod 日志**：

```
kubectl logs my-mysql-0
```


输出片段：

```
2024-01-01T00:00:00.000000Z 0 [Note] mysqld (mysqld 8.0.23) starting as process 1 ...`
2024-01-01T00:00:00.000000Z 1 [ERROR] InnoDB: Unable to lock ./ibdata1 error: 11
```

**在 Pod 中执行命令**：

```
kubectl exec -it my-mysql-0 -- /bin/sh
```

在 Pod 内：

```
# Check mounted volumes
df -h
# Verify MySQL data directory
ls -l /var/lib/mysql
# Check MySQL status
mysqladmin -u root -p status
```

**检查网络连接**：

```
kubectl exec -it my-mysql-0 -- ping my-mysql-1.my-mysql.default.svc.cluster.local
```

输出片段：

```
PING my-mysql-1.my-mysql.default.svc.cluster.local (10.244.0.6): 56 data bytes
64 bytes from 10.244.0.6: icmp_seq=0 ttl=64 time=0.047 ms
```

## 高级调试技术

Kubernetes 中的高级调试技术涉及使用专门的工具和策略来诊断和解决复杂问题。本章将介绍跟踪工具和远程调试。

### 使用 Jaeger 进行分析

[Jaeger](https://www.jaegertracing.io/) 是一种开源的端到端分布式跟踪工具，可帮助监控和调试复杂分布式系统中的事务。使用 Jaeger 进行分析可以提供有关微服务性能的见解，并帮助识别延迟问题。

您可以在 Kubernetes 集群中使用 Jaeger Operator 或 Helm 安装 Jaeger。

```
helm repo add jaegertracing https://jaegertracing.github.io/helm-charts
helm repo update
helm install jaeger jaegertracing/jaeger
```

应用程序插装：

确保您的应用程序已配置为将跟踪数据发送到 Jaeger。这通常涉及在您的应用程序代码中添加 Jaeger 客户端库，并将其配置为向 Jaeger 后端报告。

Go 应用程序示例：

```
import (
    "github.com/opentracing/opentracing-go"
    "github.com/uber/jaeger-client-go"
    "github.com/uber/jaeger-client-go/config"
)
func initJaeger(service string) (opentracing.Tracer, io.Closer) {
    cfg := config.Configuration{
        ServiceName: service,
        Sampler: &config.SamplerConfig{
            Type:  "const",
            Param: 1,
        },
        Reporter: &config.ReporterConfig{
            LogSpans:           true,
            LocalAgentHostPort: "jaeger-agent.default.svc.cluster.local:6831",
        },
    }
    tracer, closer, _ := cfg.NewTracer()
    opentracing.SetGlobalTracer(tracer)
    return tracer, closer
}
```

访问 Jaeger UI 查看和分析跟踪。

```
kubectl port-forward svc/jaeger-query 16686:16686
```

在浏览器中打开 `http://localhost:16686`。

### 使用 mirrord 进行远程调试

Mirrord 是一款开源工具，它允许通过在 Kubernetes 集群和远程基础设施的上下文中运行本地进程来进行 Kubernetes 服务的远程调试。

### 设置 mirrord

`curl -fsSL https://raw.githubusercontent.com/metalbear-co/mirrord/main/scripts/install.sh | bash`

**连接到您的集群**：

启动 mirrord 会话以将您的本地环境连接到您的 Kubernetes 集群。

```
mirrord connect
```

**交换部署**：

使用 mirrord 将集群中的部署替换为您的本地服务。

```
mirrord exec --target-namespace devops-team --target deployment/foo-app-deployment nodemon server.js
```

此命令将来自 Kubernetes 集群的流量、环境变量和文件操作重定向到您的本地机器，允许您像在本地运行一样调试服务。

设置 mirrord 会话后，您可以使用您喜欢的调试工具和 IDE 来调试在本地机器上运行的服务。

- **设置断点**： 使用您的 IDE 设置断点并单步执行代码。
- **检查变量**： 检查变量和应用程序状态以识别问题。
- **进行更改**： 进行代码更改并立即查看效果，而无需重新部署到集群。

有关使用 mirrord 进行调试的详细示例和更多信息，请阅读[这篇博文](https://itnext.io/why-fast-feedback-loops-matter-when-working-with-kubernetes-abc123)。

## 其他工具

除了核心 Kubernetes 命令和开源工具之外，还有其他一些工具可以增强您在各个类别中的故障排除功能。以下是一些值得注意的工具：


| 名称 | 类别 | 描述 |
|------|------|------|
| Komodor | 故障排查 | 为Kubernetes提供全面的实时洞察、变更跟踪和根本原因分析。 |
| Robusta | 事件响应 | 自动化事件响应平台,与Kubernetes集成,以增强可观察性和故障排查能力。 |
| Sysdig | 监控与安全 | 云原生可视化和安全平台,提供对容器性能、安全性和合规性的深入洞察。 |


## 结束语

调试 Kubernetes 应用程序可能是一项复杂且具有挑战性的任务，但使用正确的工具和技术，它会变得更加容易管理。

请记住，有效的调试不仅仅是解决出现的错误，还包括主动监控、高效的资源管理以及对应用程序架构和依赖项的深刻理解。

通过实施本指南中概述的策略和最佳实践，您可以构建一个强大的调试框架，使您能够快速识别、诊断和解决问题，确保 Kubernetes 部署的顺利运行。

感谢您抽出时间阅读这篇文章。希望您觉得它有趣且信息丰富。