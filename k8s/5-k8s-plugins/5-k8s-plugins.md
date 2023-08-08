# 五个能让你的生活变得更轻松的 kubectl 插件

我已经使用 Kubernetes 五年了，但直到最近才开始使用插件来增强我的 kubectl 命令。我将向您展示五个插件，这些插件帮助我避免重复的任务，使集群管理更简单，应对事故响应更轻松。本文介绍的所有插件都可以使用 Krew 进行安装。

![](https://alicegg.tech/assets/2023-08-08-k8s-plugins/lego.jpg)
*[Photo by Iker Urteaga](https://unsplash.com/@iurte?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)*

## Mac 用户注意事项

如果您使用的是 ARM 架构的 Mac，在使用 Krew 安装插件时，我提到的大多数插件可能会显示无法安装。这通常是因为插件作者没有发布 mac-arm64 构建。但您可以通过覆盖 KREW_ARCH 环境变量来安装 mac-amd64 构建，这同样有效。例如：

```bash
KREW_ARCH=amd64 kubectl krew install janitor
```

## Tail

通过 `kubectl logs -f` 记录 pod 的日志始终是了解正在运行的 pod 在做什么的好方法。可惜的是，我从未设法记住如何让它同时记录多个 pod 的日志。tail 插件通过为我们提供一组辅助函数来解决这个问题，从而轻松地流式传输一组 pod 的日志。例如，它可以检索由 Job 创建的所有 pod 的日志，或者附加到 Service 的所有 pod 的日志：

```bash
❯ k tail --job=logging-job
default/logging-job-xtx4s[busybox-container]: My log

❯ k tail --svc=mikochi
default/mikochi-69d47757f6-9nds7[mikochi]: [GIN] 2023/07/27 - 12:31:16 | 200 |     496.098µs |       10.42.0.1 | GET      "/api/refresh"
default/mikochi-69d47757f6-9nds7[mikochi]: [GIN] 2023/07/27 - 12:31:16 | 200 |   10.347273ms |       10.42.0.1 | GET      "/api/browse/"
default/mikochi-69d47757f6-9nds7[mikochi]: [GIN] 2023/07/27 - 12:31:16 | 200 |    9.598031ms |       10.42.0.1 | GET      "/api/browse/"
default/mikochi-69d47757f6-9nds7[mikochi]: [GIN] 2023/07/27 - 12:31:19 | 200 |     193.686µs |       10.42.0.1 | GET      "/ready"
```

## Janitor

Janitor 是一个 kubectl 插件，允许您列出处于问题状态的资源。它不需要使用 grep 命令，而是为您提供了命令，用于自动列出不健康、未准备好或未调度的 Pod、失败的 Job、挂起的 PVC 以及未声明的 PV。在检查集群期间发生事故时，这对于直接指向您正在处理的问题非常有帮助。

```bash
❯ k janitor pods status
STATUS             COUNT
Running            4
Error              6
ImagePullBackOff   1

❯ k janitor pods unhealthy
NAME                 STATUS             AGE
failing-job-ln7rf    Error              4m40s
failing-job-vbfqd    Error              4m33s
failing-job2-kmxqm   Error              4m30s
failing-job-cjbt6    Error              4m27s
failing-job2-grwcn   Error              4m23s
failing-job2-s842x   Error              4m17s
my-container         ImagePullBackOff   17m

❯ k janitor jobs failed
NAME           REASON                 MESSAGE                                       AGE
failing-job    BackoffLimitExceeded   Job has reached the specified backoff limit   4m46s
failing-job2   BackoffLimitExceeded   Job has reached the specified backoff limit   4m36s
```

## Neat

Neat 是一个简单的实用程序，用于从命令输出中删除生成的字段。您只需将 `kubectl get` 的输出导入 `kubectl neat` 中即可使用。这使输出更易读，并且如果您想保存 yaml 以创建新资源，这非常方便。

```bash
❯ k get pod -o yaml mikochi-69d47757f6-9nds7
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: "2023-07-21T12:30:58Z"
  generateName: mikochi-69d47757f6-
  labels:
    app.kubernetes.io/instance: mikochi
    app.kubernetes.io/name: mikochi
    pod-template-hash: 69d47757f6
  name: mikochi-69d47757f6-9nds7
  namespace: default
.......

❯ k get pod -o yaml mikochi-69d47757f6-9nds7 | k neat
apiVersion: v1
kind: Pod
metadata:
  labels:
    app.kubernetes.io/instance: mikochi
    app.kubernetes.io/name: mikochi
    pod-template-hash: 69d47757f6
  name: mikochi-69d47757f6-9nds7
  namespace: default
.......
```

## View-secret

由于 Secret 内部的数据是经过 base64 编码的，所以阅读它们通常需要使用 `kubectl get`、`jq` 和 `base64 -d` 命令的组合。view-secret 插件旨在简化此过程，允许您直接读取和解密 secrets 中的值。

```bash
❯ k view-secret mikochi username
[CENSORED]

❯ k view-secret mikochi password
[ALSO CENSORED]
```

## Node-shell

如果您想直接访问一个节点，在事故期间找到节点 IP，使用正确的 RSA 密钥进行 SSH 等操作可能会浪费宝贵的时间。但是通过使用 nsenter，可以从（特权）容器中获取 root shell。node-shell 插件利用此功能，在单个 kubectl 命令中让您访问节点：

```bash
❯ k node-shell my-node
spawning "nsenter-qco8qi" on "my-node"
如果您看不到命令提示符，请尝试按下 Enter 键。
root@my-node:/# cat /etc/rancher/k3s/k3s.yaml
apiVersion: v1
clusters:
- cluster:
.......
```