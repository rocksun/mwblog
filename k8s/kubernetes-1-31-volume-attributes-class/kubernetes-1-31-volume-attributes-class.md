
<!--
title: Kubernetes 1.31：用于卷修改的VolumeAttributesClass Beta
cover: ./cover.png
-->

Kubernetes 中的卷一直以来都由两个属性描述：存储类和容量。存储类是卷的不可变属性，而容量可以通过卷调整大小动态更改。这使得具有卷的工作负载的垂直扩展变得复杂。虽然云提供商和存储供应商通常提供允许指定 IO 服务质量（性能）参数（如 IOPS 或吞吐量）并在工作负载运行时对其进行调整的卷，但 Kubernetes 没有允许更改它们的 API。

> 译自 [Kubernetes 1.31: VolumeAttributesClass for Volume Modification Beta](https://kubernetes.io/blog/2024/08/15/kubernetes-1-31-volume-attributes-class/)，作者 Sunny Song Matthew Cary。

Kubernetes 中的卷一直以来都由两个属性来描述：存储类和容量。存储类是卷的不可变属性，而容量可以使用[卷调整大小](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)动态更改。

这使得具有卷的工作负载的垂直扩展变得复杂。虽然云提供商和存储供应商通常提供的卷允许指定 IO 服务质量（性能）参数（如 IOPS 或吞吐量）并随着工作负载的运行对其进行调整，但 Kubernetes 没有允许更改它们的 API。

我们很高兴地宣布，自 Kubernetes 1.29 起处于 alpha 阶段的 [VolumeAttributesClass KEP](https://github.com/kubernetes/enhancements/blob/master/keps/sig-storage/3751-volume-attributes-class/README.md) 将在 1.31 中进入测试阶段。这提供了一个通用的、Kubernetes 原生的 API，用于修改卷参数，如预配置的 IO。

与 Kubernetes 中的所有新卷功能一样，此 API 是通过[容器存储接口 (CSI)](https://kubernetes-csi.github.io/docs/)实现的。除了 VolumeAttributesClass 功能门控之外，您的配置器特定的 CSI 驱动程序必须支持新的 ModifyVolume API，它是此功能的 CSI 端。

有关所有详细信息，请参阅[完整文档](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/)。这里我们展示了常见的工作流程。

## 动态修改卷属性

`VolumeAttributesClass` 是一种集群范围的资源，用于指定配置器特定的属性。这些是由集群管理员以与存储类相同的方式创建的。例如，可以为具有更多或更少预配置 IO 的卷创建一系列金、银和铜卷属性类。

```yaml
apiVersion: storage.k8s.io/v1alpha1
kind: VolumeAttributesClass
metadata:
  name: silver
driverName: your-csi-driver
parameters:
  provisioned-iops: "500"
  provisioned-throughput: "50MiB/s"
---
apiVersion: storage.k8s.io/v1alpha1
kind: VolumeAttributesClass
metadata:
  name: gold
driverName: your-csi-driver
parameters:
  provisioned-iops: "10000"
  provisioned-throughput: "500MiB/s"
```

属性类以与存储类几乎相同的方式添加到 PVC 中。

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pv-claim
spec:
  storageClassName: any-storage-class
  volumeAttributesClassName: silver
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 64Gi
```

与存储类不同，卷属性类可以更改：

```
kubectl patch pvc test-pv-claim -p '{"spec": {"volumeAttributesClassName": "gold"}}'
```

Kubernetes 将与 CSI 驱动程序一起更新卷的属性。PVC 的状态将跟踪当前和所需的属性类。PV 资源也将使用新的卷属性类进行更新，该类将设置为 PV 当前活动的属性。

## Beta 版的限制

作为一项测试功能，仍有一些功能计划用于 GA，但尚未出现。最大的是配额支持，有关详细信息，请参阅 [KEP](https://github.com/kubernetes/enhancements/blob/master/keps/sig-storage/3751-volume-attributes-class/README.md) 以及 [sig-storage](https://github.com/kubernetes/community/tree/master/sig-storage) 中的讨论。

有关 CSI 驱动程序中对此功能的支持的最新信息，请参阅 [Kubernetes CSI 驱动程序列表](https://kubernetes-csi.github.io/docs/drivers.html)。