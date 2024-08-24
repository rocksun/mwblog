# Kubernetes 1.31: Fine-grained Supplemental Groups Control

This article discusses a new feature in Kubernetes 1.31 that improves the handling of supplemental groups within containers in Pods.

## Motivation: Implicit Group Membership Defined in `/etc/group` of Container Images

While this behavior might not be welcomed by many Kubernetes cluster users/administrators, Kubernetes by default *merges* the group information in the Pod with the information defined in `/etc/group` of the container image.

Let's look at an example, the following Pod specifies `runAsUser=1000`, `runAsGroup=3000`, and `supplementalGroups=4000` in the Pod's security context.

```
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

What is the result of the `id` command inside the `ctr` container?

```
# Create the Pod:
$ kubectl apply -f https://k8s.io/blog/2024-08-22-Fine-grained-SupplementalGroups-control/implicit-groups.yaml
# Verify the Pod's container is running:
$ kubectl get pod implicit-groups
# Check the id command
$ kubectl exec implicit-groups -- id
```

Then, the output should be similar to:

```
uid=1000 gid=3000 groups=3000,4000,50000
```

Where does the group ID `50000` in the supplemental groups (`groups` field) come from, even though `50000` is not defined in the Pod's manifest at all? The answer is the `/etc/group` file in the container image.

Checking the content of `/etc/group` in the container image should show the following:

```
$ kubectl exec implicit-groups -- cat /etc/group
...
user-defined-in-image:x:1000:
group-defined-in-image:x:50000:user-defined-in-image
```

Aha! The container's primary user `1000` belongs to group `50000` in the last entry.

Therefore, the group membership defined in the container image for the container's primary user is *implicitly* merged into the information in the Pod. Note that this is a design decision inherited from Docker by the current CRI implementations, and the community has only recently really revisited it.

### What's the Problem?

The *implicitly* merged group information from the container image can cause some problems, especially when accessing volumes (see [kubernetes/kubernetes#112879](https://issue.k8s.io/112879) for details), because file permissions are controlled by uid/gid in Linux. Even worse, the implicit gids from `/etc/group` cannot be detected/validated by any policy engine, as there is no clue about the implicit group information in the manifest. This can also become a Kubernetes security concern.

## Fine-grained Supplemental Groups Control in Pods: `SupplementaryGroupsPolicy`

To address the above issues, Kubernetes 1.31 introduces a new field `supplementalGroupsPolicy` in the Pod's `.spec.securityContext`.

This field provides a way to control how supplemental groups are calculated for container processes in the Pod. The available policies are:

* **Merge**: This will merge the group membership defined in `/etc/group` for the container's primary user. This policy is applied if not specified (i.e., for backward compatibility).
* **Strict**: It only appends the group IDs specified in the `fsGroup`, `supplementalGroups`, or `runAsGroup` fields as supplemental groups for the container process. This means that any group membership defined in `/etc/group` for the container's primary user will not be merged.

Let's see how the `Strict` policy works.

```
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
# Verify the Pod's container is running:
$ kubectl get pod strict-supplementalgroups-policy
# Check the process identity:
kubectl exec -it strict-supplementalgroups-policy -- id
```

The output should be similar to:

```
uid=1000 gid=3000 groups=3000,4000
```

You can see that the `Strict` policy can exclude group `50000` from the `groups`!

Therefore, ensuring `supplementalGroupsPolicy: Strict` (enforced by some policy mechanism) helps prevent implicit supplemental groups in Pods.

#### Note:

In reality, this is not enough, as a container with enough privileges/capabilities can change its process identity. See the next section for details.

## Attached Process Identity in Pod Status

This feature also exposes the process identity of the first container process attached to the container via `.status.containerStatuses[].user.linux`.
查看隐式组 ID 是否已附加将很有帮助。

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

**注意：**

请注意，`status.containerStatuses[].user.linux` 字段中的值是容器中第一个容器进程的*第一个附加*进程标识。如果容器具有足够的权限来调用与进程标识相关的系统调用（例如 [,](https://man7.org/linux/man-pages/man2/setuid.2.html) `setuid(2)` [或](https://man7.org/linux/man-pages/man2/setgid.2.html) `setgid(2)` [, 等等），容器进程可以更改其标识。因此，](https://man7.org/linux/man-pages/man2/setgroups.2.html) `setgroups(2)` *实际*进程标识将是动态的。

## 功能可用性

要启用 `supplementalGroupsPolicy` 字段，必须使用以下组件：

- Kubernetes：v1.31 或更高版本，并启用 `SupplementalGroupsPolicy` [功能网关](/docs/reference/command-line-tools-reference/feature-gates/)。从 v1.31 开始，该网关被标记为 alpha。
- CRI 运行时：
    - containerd：v2.0 或更高版本
    - CRI-O：v1.31 或更高版本

您可以在节点的 `.status.features.supplementalGroupsPolicy` 字段中查看该功能是否受支持。

```
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

[为 Pod 或容器配置安全上下文](/docs/tasks/configure-pod-container/security-context/)，了解 `supplementalGroupsPolicy` 的更多详细信息
[KEP-3619：细粒度 SupplementalGroups 控制](https://github.com/kubernetes/enhancements/issues/3619)

## 如何参与？

此功能由 SIG Node 社区驱动。请加入我们，与社区联系，分享您对上述功能及其他方面的想法和反馈。我们期待您的参与！