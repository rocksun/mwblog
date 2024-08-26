# Kubernetes 1.31：防止删除顺序错误导致的持久卷泄漏

[持久卷](/docs/concepts/storage/persistent-volumes/)（简称 PV）与[回收策略](/docs/concepts/storage/persistent-volumes/#reclaim-policy)相关联。回收策略用于确定在删除绑定到 PV 的 PVC 时存储后端需要采取的操作。当回收策略为 `Delete` 时，预期存储后端会释放为 PV 分配的存储资源。本质上，回收策略需要在 PV 删除时得到遵守。在最近的 Kubernetes v1.31 版本中，一项 Beta 功能允许您配置集群以这种方式运行并遵守配置的回收策略。

## 以前的 Kubernetes 版本中回收是如何工作的？

[持久卷声明](/docs/concepts/storage/persistent-volumes/#Introduction)（简称 PVC）是用户对存储的请求。如果找到新创建的 PV 或匹配的 PV，则 PV 和 PVC 被认为是[绑定](/docs/concepts/storage/persistent-volumes/#Binding)的。PV 本身由存储后端分配的卷支持。

通常，如果要删除卷，则预期会删除绑定 PV-PVC 对的 PVC。但是，在删除 PVC 之前删除 PV 没有限制。

首先，我将演示运行旧版 Kubernetes 的集群的行为。

#### 检索绑定到 PV 的 PVC

检索现有的 PVC `example-vanilla-block-pvc`

```
kubectl get pvc example-vanilla-block-pvc
```

以下输出显示了 PVC 及其绑定的 PV；PV 显示在 `VOLUME` 列下：

```
NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS AGE
example-vanilla-block-pvc Bound pvc-6791fdd4-5fad-438e-a7fb-16410363e3da 5Gi RWO example-vanilla-block-sc 19s
```

#### 删除 PV

当我尝试删除绑定 PV 时，kubectl 会话会阻塞，并且 `kubectl` 工具不会将控制权返回给 shell；例如：

```
kubectl delete pv pvc-6791fdd4-5fad-438e-a7fb-16410363e3da
```

```
persistentvolume "pvc-6791fdd4-5fad-438e-a7fb-16410363e3da" deleted
^C
```

#### 检索 PV

```
kubectl get pv pvc-6791fdd4-5fad-438e-a7fb-16410363e3da
```

可以观察到 PV 处于 `Terminating` 状态

```
NAME CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM STORAGECLASS REASON AGE
pvc-6791fdd4-5fad-438e-a7fb-16410363e3da 5Gi RWO Delete Terminating default/example-vanilla-block-pvc example-vanilla-block-sc 2m23s
```

#### 删除 PVC

```
kubectl delete pvc example-vanilla-block-pvc
```

如果 PVC 成功删除，则会看到以下输出：

```
persistentvolumeclaim "example-vanilla-block-pvc" deleted
```

集群中的 PV 对象也会被删除。当尝试检索 PV 时，将观察到 PV 无法找到：

```
kubectl get pv pvc-6791fdd4-5fad-438e-a7fb-16410363e3da
```

```
Error from server (NotFound): persistentvolumes "pvc-6791fdd4-5fad-438e-a7fb-16410363e3da" not found
```

虽然 PV 已删除，但底层存储资源未删除，需要手动删除。

总之，与持久卷关联的回收策略在某些情况下会被忽略。对于 `Bound` PV-PVC 对，PV-PVC 删除的顺序决定了是否遵守 PV 回收策略。如果首先删除 PVC，则会遵守回收策略；但是，如果在删除 PVC 之前删除 PV，则不会执行回收策略。由于这种行为，外部基础设施中的关联存储资产不会被删除。

## Kubernetes v1.31 中的 PV 回收策略

新行为确保在用户尝试手动删除 PV 时，底层存储对象会从后端删除。

#### 如何启用新行为？

要利用新行为，您必须将集群升级到 Kubernetes 的 v1.31 版本，并运行 CSI [外部供应器](https://github.com/kubernetes-csi/external-provisioner) 版本

`5.0.1`
或更高版本。

#### 它如何工作？

对于 CSI 卷，新行为是通过在新的和现有的 PV 上添加一个 [终结器](/docs/concepts/overview/working-with-objects/finalizers/) `external-provisioner.volume.kubernetes.io/finalizer` 来实现的。只有在从后端删除存储后，才会删除终结器。

带有终结器的 PV 示例，请注意终结器列表中的新终结器

```
kubectl get pv pvc-a7b7e3ba-f837-45ba-b243-dec7d8aaed53 -o yaml
```

```
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    pv.kubernetes.io/provisioned-by: csi.vsphere.vmware.com
  creationTimestamp: "2021-11-17T19:28:56Z"
  finalizers:
  - kubernetes.io/pv-protection
  - external-provisioner.volume.kubernetes.io/finalizer
  name: pvc-a7b7e3ba-f837-45ba-b243-dec7d8aaed53
  resourceVersion: "194711"
  uid: 087f14f2-4157-4e95-8a70-8294b039d30e
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 1Gi
  claimRef:
    apiVersion: v1
```
```yaml
kind: PersistentVolumeClaim
name: example-vanilla-block-pvc
namespace: default
resourceVersion: "194677"
uid: a7b7e3ba-f837-45ba-b243-dec7d8aaed53
csi:
  driver: csi.vsphere.vmware.com
  fsType: ext4
  volumeAttributes:
    storage.kubernetes.io/csiProvisionerIdentity: 1637110610497-8081-csi.vsphere.vmware.com
  type: vSphere CNS Block Volume
  volumeHandle: 2dacf297-803f-4ccc-afc7-3d3c3f02051e
  persistentVolumeReclaimPolicy: Delete
  storageClassName: example-vanilla-block-sc
  volumeMode: Filesystem
status:
  phase: Bound
```

[终结器](/docs/concepts/overview/working-with-objects/finalizers/) 阻止此持久卷从集群中删除。如前所述，只有在持久卷成功从存储后端删除后，才会从 PV 对象中删除终结器。要了解有关终结器的更多信息，请参阅 [使用终结器控制删除](/blog/2021/05/14/using-finalizers-to-control-deletion/)。

类似地，终结器 `kubernetes.io/pv-controller` 被添加到动态配置的树内插件卷中。

#### CSI 迁移卷怎么样？
此修复也适用于 CSI 迁移卷。

### 一些注意事项
此修复不适用于静态配置的树内插件卷。

### 参考资料
### 我如何参与？
Kubernetes Slack 频道 [SIG 存储通信渠道](https://github.com/kubernetes/community/blob/master/sig-storage/README.md#contact) 是与 SIG 存储和迁移工作组团队联系的绝佳媒介。

特别感谢以下人员的深刻评论、周到考虑和宝贵贡献：

- Fan Baofa (carlory)
- Jan Šafránek (jsafrane)
- Xing Yang (xing-yang)
- Matthew Wong (wongma7)
如果您有兴趣参与 CSI 或 Kubernetes 存储系统任何部分的设计和开发，请加入 [Kubernetes 存储特别兴趣小组 (SIG)](https://github.com/kubernetes/community/tree/master/sig-storage)。我们正在快速发展，始终欢迎新的贡献者。