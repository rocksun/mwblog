
<!--
title: Kubernetes 1.31：细粒度SupplementalGroups控制
cover: ./cover.png
-->

本文讨论了 Kubernetes 1.31 中的一项新功能，该功能改进了 Pod 中容器内补充组（supplementary groups）的处理方式。

> 译自 [Kubernetes 1.31: Fine-grained SupplementalGroups control](https://kubernetes.io/blog/2024/08/22/fine-grained-supplementalgroups-control/)，作者 Shingo Omura。

## 动机：容器镜像中 /etc/group 中定义的隐式组成员资格

虽然这种行为可能不受许多 Kubernetes 集群用户/管理员的欢迎，但 Kubernetes 默认情况下会将 Pod 中的组信息与容器镜像中 /etc/group 中定义的信息合并。

让我们看一个例子，下面的 Pod 在 Pod 的安全上下文中指定了 runAsUser=1000、runAsGroup=3000 和 supplementalGroups=4000。

**implicit-groups.yaml**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: implicit-groups
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    supplementalGroups: [4000]
  containers:
  - name: ctr
    image: registry.k8s.io/e2e-test-images/agnhost:2.45
    command: [ "sh", "-c", "sleep 1h" ]
    securityContext:
      allowPrivilegeEscalation: false
```

在 ctr 容器中 id 命令的结果是什么？

```
# Create the Pod:
$ kubectl apply -f https://k8s.io/blog/2024-08-22-Fine-grained-SupplementalGroups-control/implicit-groups.yaml

# Verify that the Pod's Container is running:
$ kubectl get pod implicit-groups

# Check the id command
$ kubectl exec implicit-groups -- id
```

然后，输出类似以下形式：

```
uid=1000 gid=3000 groups=3000,4000,50000
```

辅助组（组字段）中的组 ID 50000 从何而来，即使 50000 在 Pod 清单中完全没有定义？答案是容器镜像中的 /etc/group 文件。

检查容器镜像中 /etc/group 的内容应该会显示以下内容：

```
$ kubectl exec implicit-groups -- cat /etc/group
...
user-defined-in-image:x:1000:
group-defined-in-image:x:50000:user-defined-in-image
```

啊哈！容器的主要用户 1000 在上一个条目中属于组 50000。

因此，容器镜像中定义的容器主要用户的 /etc/group 中的分组成员资格隐式合并到了 Pod 中的信息。请注意，这是一个设计决策，当前 CRI 实现从 Docker 继承而来，社区在现在之前从未真正重新考虑过它。

### 这是怎么了？

容器镜像中从 `/etc/group` 中隐式合并的组信息可能会引起一些关注，特别是在访问卷时(请参见[kubernetes/kubernetes#112879](https://issue.k8s.io/112879)了解详情)，因为文件权限由Linux中的uid/gid控制。更糟糕的是，/etc/group中的隐式gid不能被任何策略引擎检测/验证，因为清单中没有隐式组信息的线索。这还可能对Kubernetes安全性构成威胁。

## 在 Pod 中对精细的 SupplementalGroups 进行控制：SupplementaryGroupsPolicy

为了解决上述问题，Kubernetes 1.31 在 Pod 的 .spec.securityContext 中引入了新的 supplementalGroupsPolicy 字段。

此字段提供了一种方法来控制如何计算 Pod 中容器进程的附加组。以下是可用策略：

* Merge：将为容器的主用户在 /etc/group 中定义的组成员关系合并。如果不指定，将应用此策略（即向后兼容行为）。
* Strict：它仅将 fsGroup、supplementalGroups 或 runAsGroup 字段中指定的组 ID 附加为容器进程的补充组。这意味着不会合并为容器主用户在 /etc/group 中定义的组成员关系。

让我们来看看 Strict 策略如何发挥作用。

**strict-supplementalgroups-policy.yaml**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: strict-supplementalgroups-policy
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    supplementalGroups: [4000]
    supplementalGroupsPolicy: Strict
  containers:
  - name: ctr
    image: registry.k8s.io/e2e-test-images/agnhost:2.45
    command: [ "sh", "-c", "sleep 1h" ]
    securityContext:
      allowPrivilegeEscalation: false
```

```
# Create the Pod:
$ kubectl apply -f https://k8s.io/blog/2024-08-22-Fine-grained-SupplementalGroups-control/strict-supplementalgroups-policy.yaml

# Verify that the Pod's Container is running:
$ kubectl get pod strict-supplementalgroups-policy

# Check the process identity:
kubectl exec -it strict-supplementalgroups-policy -- id
```

该输出应类似于此：

```
uid=1000 gid=3000 groups=3000,4000
```

可以看到严格策略将组 50000 从组中排除！

因此，确保 supplementalGroupsPolicy: Strict（由一些策略机制强制实施）有助于防止 Pod 中的隐式补充组。

> 注意：实际上，这个还不够，因为拥有足够权限/能力的容器可以更改其进程的身份。有关详细信息，请参阅下一节。

## 附加的 Pod 状态中处理身份

此功能还会通过 .status.containerStatuses[].user.linux 字段公开附加到容器的第一个容器进程的进程身份。这有助于查看是否附加了隐式组 ID。

```
...
status:
containerStatuses:
- name: ctr
  user:
    linux:
      gid: 3000
      supplementalGroups:
      - 3000
      - 4000
      uid: 1000
...
```

> **注意**：请注意，`status.containerStatuses[].user.linux` 字段中的值是容器中第一个容器进程的*第一个附加*进程标识。如果容器具有足够的权限来调用与进程标识相关的系统调用（例如 [,](https://man7.org/linux/man-pages/man2/setuid.2.html) `setuid(2)` [或](https://man7.org/linux/man-pages/man2/setgid.2.html) `setgid(2)` [, 等等），容器进程可以更改其标识。因此，](https://man7.org/linux/man-pages/man2/setgroups.2.html) `setgroups(2)` *实际*进程标识将是动态的。

## 功能可用性

要启用 `supplementalGroupsPolicy` 字段，必须使用以下组件：

- Kubernetes：v1.31 或更高版本，并启用 `SupplementalGroupsPolicy` [功能网关](/docs/reference/command-line-tools-reference/feature-gates/)。从 v1.31 开始，该网关被标记为 alpha。
- CRI 运行时：
    - containerd：v2.0 或更高版本
    - CRI-O：v1.31 或更高版本

您可以在节点的 `.status.features.supplementalGroupsPolicy` 字段中查看该功能是否受支持。

```yaml
apiVersion: v1
kind: Node
...
status:
  features:
    supplementalGroupsPolicy: true
```

## 接下来的步骤？

Kubernetes SIG Node 希望 - 并期望 - 该功能将在 Kubernetes 的未来版本中升级到 beta 以及最终的通用可用性 (GA)，以便用户不再需要手动启用功能网关。

`Merge` 策略在未指定 `supplementalGroupsPolicy` 时应用，以确保向后兼容性。

## 如何了解更多？

- [为 Pod 或容器配置安全上下文](/docs/tasks/configure-pod-container/security-context/)，了解 `supplementalGroupsPolicy` 的更多详细信息
- [KEP-3619：细粒度 SupplementalGroups 控制](https://github.com/kubernetes/enhancements/issues/3619)

## 如何参与？

此功能由 SIG Node 社区驱动。请加入我们，与社区联系，分享您对上述功能及其他方面的想法和反馈。我们期待您的参与！