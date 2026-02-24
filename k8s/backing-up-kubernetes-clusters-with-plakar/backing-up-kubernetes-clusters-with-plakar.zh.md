**TL;DR:**

> 我们为 Plakar 构建了一个 Kubernetes 集成，它在三个层面备份集群：etcd（灾难恢复）、manifests（细粒度恢复和检查）以及持久卷（通过 CSI 快照）。这实现了全面的集群恢复、细粒度恢复以及跨环境的数据可移植性。

---

在加入 [Linux 基金会和 CNCF](https://plakar.io/posts/2026-01-07/plakar-joins-the-linux-foundation-and-cloud-native-computing-foundation/) 后，
我们开始参加一些活动，比如在巴黎举行的 Cloud Native Days 和即将到来的阿姆斯特丹 KubeConf。
虽然我们已经提供了大量的集成，但我们觉得不能空手参加这些活动；
我们必须宣布并展示一些新东西——比如 Kubernetes 集成。

![](/posts/2026-02-18/backing-up-kubernetes-clusters-with-plakar/cnd-booth.png)
从左到右：Omar、Julien、Antoine 和 Gilles 在我们的 Cloud Native Days 展位。

在过去几年里，我使用 Kubernetes 做了很多工作，但主要是
作为用户，并且在特定环境中：严格遵循
GitOps 流程，使用托管 Kubernetes，并且几乎不使用任何
PVC，因为所有数据
都存储在托管数据库或存储桶中。

因此，这对我来说也是一个深入研究 Kubernetes
Golang API 以及
CSI 支持驱动器工作原理的机会。

## 安装 k8s 集成

在撰写本文时，etcd 和 k8s 集成已提交到公共仓库，并且**仅适用于 Plakar v1.1.0-beta**。

要测试它们，您首先需要安装我们最新版本的 Plakar 测试版：

```
$ go install github.com/PlakarKorp/plakar@v1.1.0-beta.4

```

这对于本文中的命令成功执行是必需的！

## 使用 etcd 进行灾难恢复

为了提供一个完整的解决方案，我决定从多个层面来处理备份
策略。最低层是**确保 etcd 的安全**。

[etcd](https://etcd.io) 是一个用于分布式系统的分布式键值存储。
它通常被用作 Kubernetes 集群中的单一事实来源。

在正常情况下，*etcd* 可以抵抗其
集群节点的部分中断，但如果太多节点发生故障，它可能无法
恢复。考虑到这一部分的关键性，制定一个健全的灾难恢复策略非常重要。

为此，我们刚刚发布了 [etcd
集成](https://github.com/PlakarKorp/integration-etcd) 的第一个版本：备份 etcd 现在就像这样简单：

```
$ plakar pkg add etcd
$ plakar backup etcd://node1:2379

```

不幸的是，由于 *etcd* 恢复的工作方式，很难以
细粒度的方式进行恢复，因此这确实是应对大规模集群中断的
最后一道防线。

为了更细粒度地检查或恢复集群状态，我们
需要处理 manifests。

## 保存 manifests

第二层是备份 manifests：
它们代表**集群中在给定时间点的所有工作负载**，
以及关于其当前状态的额外元数据。

在此层，可以更容易地浏览备份内容、
调查快照之间的差异或以细粒度方式恢复
资源：

*   恢复整个集群配置
*   仅恢复一个命名空间
*   甚至恢复单个 Deployment。

这是 [Kubernetes 集成](https://github.com/PlakarKorp/integration-k8s) 所做的一部分：
它获取集群上所有 manifests 和资源，以便用 Plakar 进行归档。

```
$ plakar pkg add k8s
$ plakar backup k8s://localhost:8001

```

备份中状态元数据的存在也解锁了其他
用途：例如，除了现有的监控工具之外，
通过 UI 轻松浏览集群在特定时间（可用的节点、
部署的状态等）发生的情况，这有助于调查事件。

## 数据呢？

即使 Kubernetes 最初并非为有状态工作负载而设计，
但在实践中，将持久卷附加到 Pod 是很常见的，
这些也需要得到保护。

[Kubernetes 集成](https://github.com/PlakarKorp/integration-k8s) 的另一个主要工作是
提供一种备份和恢复持久卷内容的方法。
顺便说一句，这也是我实现起来最复杂的部分。

我非常感谢 Mathieu 和 Gilles 在此过程中对我的帮助，
在我遇到困难时提供支持，并残酷地简化了设计，
使集成更易于开发和使用——也更强大。独自工作时，
很容易陷入编写“聪明”代码的诱惑，最终这些代码变得
相当复杂且难以使用。

我们从 CSI 支持的 PVC 开始，因为它们代表了 Kubernetes 集群中持久存储的事实标准。

```
$ plakar pkg add k8s
$ plakar backup k8s+csi://localhost:8001/prod/my-pvc

```

该集成的工作原理是：首先创建给定 PVC 的快照。然后，当快照准备就绪时，
将其挂载到一个运行小型帮助程序（运行我们的文件系统导入器）的 Pod 中。
Plakar 连接到它并摄取数据。最后，PVC 快照从
Kubernetes 集群中删除。

恢复工作方式类似，只是不创建快照。

Plakar 提供的一个强大功能是它可以混合搭配连接器，
例如，可以将 *etcd*
快照恢复到 Kubernetes 集群中的持久卷，或者将数据从
PVC 移动到 S3 存储桶。
潜力无限！

## 总结

未来是继续测试该集成在不同
Kubernetes 分发版和提供商中的表现，并扩展
对非 CSI 卷的支持。如果您正在运行 Kubernetes 集群，
无论是本地部署还是托管，请务必尝试一下，并告诉我们您的想法！