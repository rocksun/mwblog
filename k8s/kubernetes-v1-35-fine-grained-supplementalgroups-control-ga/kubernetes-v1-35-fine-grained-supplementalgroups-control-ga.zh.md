# Kubernetes v1.35：细粒度补充组控制正式发布 (GA)

作者：**Shingo Omura (LY Corporation)** |
2025年12月23日，星期二

代表 Kubernetes SIG Node，我们很高兴地宣布，Kubernetes v1.35 中*细粒度补充组控制*已正式发布 (GA)！

新的 Pod 字段 `supplementalGroupsPolicy` 作为可选的 Alpha 功能在 Kubernetes v1.31 中引入，随后在 v1.33 中升级为 Beta 版。
现在，该功能已普遍可用。
此功能允许您对 Linux 容器中的补充组实现更精确的控制，从而增强安全态势，尤其是在访问卷时。
此外，它还增强了容器中 UID/GID 详细信息的透明度，提供改进的安全监督。

如果您计划将集群从 v1.32 或更早版本升级，请注意自 Beta 版 (v1.33) 以来引入了一些行为破坏性更改。
有关更多详细信息，请参阅上一篇关于升级到 Beta 版的博客文章中的 [Beta 版中引入的行为变更](/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/#the-behavioral-changes-introduced-in-beta) 和 [升级注意事项](/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/#upgrade-consideration) 章节。

## 动机：容器镜像中 `/etc/group` 定义的隐式组成员身份

尽管大多数 Kubernetes 集群管理员/用户可能没有意识到这一点，但默认情况下，Kubernetes 会将 Pod 中的组信息与容器镜像中 `/etc/group` 文件中定义的信息进行*合并*。

例如；一个 Pod 清单，在其安全上下文中指定了 `spec.securityContext.runAsUser: 1000`、`spec.securityContext.runAsGroup: 3000` 和 `spec.securityContext.supplementalGroups: 4000`。

```
apiVersion: v1
kind: Pod
metadata:
  name: implicit-groups-example
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    supplementalGroups: [4000]
  containers:
  - name: example-container
    image: registry.k8s.io/e2e-test-images/agnhost:2.45
    command: [ "sh", "-c", "sleep 1h" ]
    securityContext:
      allowPrivilegeEscalation: false

```

`example-container` 容器中 `id` 命令的结果是什么？输出应类似于此：

```
uid=1000 gid=3000 groups=3000,4000,50000

```

补充组（`groups` 字段）中的组 ID `50000` 从何而来，即使 `50000` 根本没有在 Pod 清单中定义？答案是容器镜像中的 `/etc/group` 文件。

检查容器镜像中 `/etc/group` 的内容，包含以下类似内容：

```
user-defined-in-image:x:1000:
group-defined-in-image:x:50000:user-defined-in-image

```

这表明容器的主要用户 `1000` 属于最后一个条目中的组 `50000`。

因此，容器镜像中 `/etc/group` 文件为容器主要用户定义的组成员身份会*隐式地*合并到 Pod 中的信息。请注意，这是当前 CRI 实现从 Docker 继承的设计决策，社区直到现在才真正重新考虑它。

### 有什么问题？

容器镜像中 `/etc/group` 文件中*隐式*合并的组信息带来了安全风险。这些隐式 GID 无法被策略引擎检测或验证，因为在 Pod 清单中没有它们的记录。这可能导致意外的访问控制问题，特别是在访问卷时（详见 [kubernetes/kubernetes#112879](https://issue.k8s.io/112879)），因为 Linux 中的文件权限由 UID/GID 控制。

## Pod 中的细粒度补充组控制：`supplementaryGroupsPolicy`

为了解决这个问题，Pod 的 `.spec.securityContext` 现在包含 `supplementalGroupsPolicy` 字段。

此字段允许您控制 Kubernetes 如何计算 Pod 中容器进程的补充组。可用的策略有：

*   *Merge*：将合并为容器主要用户在 `/etc/group` 中定义的组成员身份。如果未指定，将应用此策略（即为了向后兼容，保持现有行为）。
*   *Strict*：只有在 `fsGroup`、`supplementalGroups` 或 `runAsGroup` 中指定的组 ID 才会作为补充组附加到容器进程。为容器主要用户在 `/etc/group` 中定义的组成员身份将被忽略。

我将解释 `Strict` 策略是如何工作的。以下 Pod 清单指定了 `supplementalGroupsPolicy: Strict`：

```
apiVersion: v1
kind: Pod
metadata:
  name: strict-supplementalgroups-policy-example
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    supplementalGroups: [4000]
    supplementalGroupsPolicy: Strict
  containers:
  - name: example-container
    image: registry.k8s.io/e2e-test-images/agnhost:2.45
    command: [ "sh", "-c", "sleep 1h" ]
    securityContext:
      allowPrivilegeEscalation: false

```

`example-container` 容器中 `id` 命令的结果应类似于此：

```
uid=1000 gid=3000 groups=3000,4000

```

您可以看到 `Strict` 策略可以从 `groups` 中排除组 `50000`！

因此，确保 `supplementalGroupsPolicy: Strict`（由某些策略机制强制执行）有助于防止 Pod 中的隐式补充组。

#### 注意：

具有足够权限的容器可以更改其进程身份。
`supplementalGroupsPolicy` 只影响初始进程身份。

继续阅读了解更多详情。

## Pod 状态中附加的进程身份

此功能还通过 `.status.containerStatuses[].user.linux` 字段公开附加到容器第一个进程的进程身份。这将有助于查看是否附加了隐式组 ID。

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

#### 注意：

请注意，`status.containerStatuses[].user.linux` 字段中的值是附加到容器中第一个进程的*初始*进程身份。如果容器具有足够的权限来调用与进程身份相关的系统调用（例如 [`setuid(2)`](https://man7.org/linux/man-pages/man2/setuid.2.html)、[`setgid(2)`](https://man7.org/linux/man-pages/man2/setgid.2.html) 或 [`setgroups(2)`](https://man7.org/linux/man-pages/man2/setgroups.2.html) 等），容器进程可以更改其身份。因此，*实际*进程身份将是动态的。

有几种方法可以限制容器中的这些权限。我们建议以下作为简单解决方案：

此外，kubelet 无法查看 NRI 插件或容器运行时内部工作原理。配置节点或特权工作负载的集群管理员，在获得本地管理员权限后，可能会更改任何 Pod 的补充组。然而，这超出了 Kubernetes 的控制范围，不应成为安全强化的节点所关注的问题。

## `Strict` 策略需要最新的容器运行时

高级容器运行时（例如 containerd、CRI-O）在计算将附加到容器的补充组 ID 方面起着关键作用。因此，`supplementalGroupsPolicy: Strict` 需要支持此功能的 CRI 运行时。
旧行为（`supplementalGroupsPolicy: Merge`）可以与不支持此功能的 CRI 运行时一起工作，因为此策略完全向后兼容。

以下是一些支持此功能的 CRI 运行时以及您需要运行的版本：

*   containerd: v2.0 或更高版本
*   CRI-O: v1.31 或更高版本

而且，您可以在 Node 的 `.status.features.supplementalGroupsPolicy` 字段中查看是否支持该功能。请注意，此字段不同于 [KEP-5328: 节点声明功能（原节点能力）](https://github.com/kubernetes/enhancements/issues/5328) 中引入的 `status.declaredFeatures`。

```
apiVersion: v1
kind: Node
...
status:
  features:
    supplementalGroupsPolicy: true

```

随着容器运行时普遍支持此功能，各种安全策略可能会开始强制执行更安全的 `Strict` 行为。最佳实践是确保您的 Pod 为此强制执行做好准备，并且所有补充组都在 Pod 规范中透明声明，而不是在镜像中。

## 参与其中

此增强功能由 [SIG Node](https://github.com/kubernetes/community/tree/master/sig-node) 社区推动。
请加入我们，与社区联系，并分享您对上述功能及其他方面的想法和反馈。我们期待您的来信！

## 如何了解更多？