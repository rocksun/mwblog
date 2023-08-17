# 构建 Kubernetes 集群 — 选择工作节点大小

TL;DR: 在创建Kubernetes集群时，您可能首先要问的一个问题是：“我应该使用哪种类型的工作节点，以及应该有多少个？”

翻译自 [Architecting Kubernetes clusters — choosing a worker node size](https://learnk8s.io/kubernetes-node-size) 。

![](https://learnk8s.io/a/23c83c8632770bc29860b854504a0926.svg)

当您创建一个 Kubernetes 集群时，您可能首先会问的一个问题是："我应该使用什么类型的工作节点，以及需要多少个？"

*如果您正在构建一个本地集群，您应该订购一些最新一代的高性能服务器，还是使用您数据中心中闲置的几台旧机器？*

或者，如果您使用像 Google Kubernetes Engine（GKE） 这样的托管 Kubernetes 服务，您应该使用八个 n1-standard-1 实例还是两个 n1-standard-4 实例来实现所需的计算容量？

目录：

- 集群容量
- Kubernetes 工作节点中的保留资源
- 工作节点中的资源分配和效率
- 韧性和复制
- 扩展增量和提前时间
- 拉取容器镜像
- Kubelet 和扩展 Kubernetes API
- 节点和集群限制
- 存储
- 总结和结论

## 集群容量

在一般情况下，Kubernetes 集群可以被看作是将一组单独的节点抽象为一个大的“超级节点”。

这个超级节点的总计算容量（CPU 和内存）是所有组成节点容量的总和。

有多种实现方式。

例如，想象您需要一个总容量为 8 个 CPU 核心和 32GB 内存的集群。

以下是设计集群的两种可能方式中的两种：

![小型节点与大型节点在 Kubernetes 集群中的应用](https://learnk8s.io/a/c642b260295b87df85d97a6e8c20be48.svg)

这两种选项都会产生具有相同容量的集群，但左侧的选项使用了四个较小的节点，而右侧的选项使用了两个较大的节点。

哪个更好呢？

让我们从回顾如何在工作节点中分配资源开始。

## Kubernetes 工作节点中的保留资源

Kubernetes 集群中的每个工作节点都是运行 kubelet（Kubernetes Agent）的计算单元。

kubelet 是一个连接到控制平面并将节点的当前状态与集群的状态同步的二进制文件。

例如，当 Kubernetes 调度程序将一个 Pod 分配给特定节点时，它不会发送消息给kubelet。

相反，[它会写一个 Binding 对象并将其存储在 etcd 中](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#scheduling-cycle-binding-cycle)。

kubelet 定期检查集群的状态，一旦注意到一个新的 Pod 分配给其节点，就会开始下载 Pod 规范并创建它。

kubelet 通常部署为 SystemD 服务，并作为操作系统的一部分运行。

Kubelet、SystemD 和操作系统都需要 CPU 和内存等资源来正常工作。

**因此，工作节点的所有资源都并不是都可以用于运行 Pod 。**

CPU 和内存资源通常分配如下：

- 操作系统。
- Kubelet。
- Pods。
- 驱逐阈值。

![](https://learnk8s.io/a/d627f4247a50662c83a2a40703a8b693.svg)

您可能会想知道每个资源分配给了其中的哪些。

虽然这些往往是可配置的，但大多数情况下，CPU 通常在以下分配中被保留：

- 第一个核心的 6％。
- 第二个核心的 1％（最多2个核心）。
- 接下来两个核心的 0.5％（最多4个核心）。
- 四个核心以上的任何核心的 0.25％。

至于内存，可能如下：

- 小于 1 GB 的机器的 255 MiB 内存。
- 前 4GB 内存的 25％。
- 接下来 4GB 内存的 20％（最多 8GB）。
- 接下来 8GB 内存的 10％（最多 16GB）。
- 接下来 112GB 内存的 6％（最多 128GB）。
- 128GB 以上的任何内存的 2％。

最后，驱逐阈值通常为 100MB。

*什么是驱逐阈值？*

这是内存使用的阈值 - 如果节点越过该阈值，kubelet 会开始驱逐 Pod ，因为当前节点内存不足。

举个例子。

对于一个具有 8GB 和 2 个 vCPU 的实例，可用资源如下：

1. 70m vCPU 和 1.8GB 供 kubelet 和操作系统使用（通常捆绑在一起）。
2. 100MB 的驱逐阈值。
3. 剩余的 6.1GB 内存和 1930 毫核可以用于 Pods。

只有总内存的 75％ 用于运行工作负载。

![](https://learnk8s.io/a/3de0f4647a4b0d71b196d4e394aa5451.svg)

*不仅如此。*

您的节点可能需要在每个节点上运行一些 Pod（例如 DaemonSets）以正常运行，这些 Pod 也会消耗内存和 CPU。

示例包括 Kube-proxy、像 Fluentd 或 Fluent Bit 这样的日志代理、NodeLocal DNSCache 或 CSI 驱动程序。

**这是您无论节点大小如何都必须支付的固定成本。**

![](https://learnk8s.io/a/e77f8c687be1e38bd35470e177e4290a.svg)

考虑到这一点，让我们来看看“少量大节点”和“多个小节点”这两种截然不同的扩展方向的优缺点。

> 请注意，“节点”在本文中始终指的是工作节点。控制平面节点的数量和大小的选择是一个完全不同的话题。

## 资源分配和工作节点效率

随着较大实例，kubelet 保留的资源减少。

让我们来看两种极端情况。

您想要为 request 为 0.3 vCPU 和 2GB 内存的应用程序部署七个副本。

1. 在第一种情况下，您为部署所有副本而提供了一个单一的工作节点。
2. 在第二种情况下，您在每个节点上部署一个副本。

> 为了简单起见，我们假设在这些节点上没有运行 DaemonSets。

七个副本所需的总资源是 2.1 vCPU和 14GB 内存（即 7 x 300m = 2.1 vCPU 和 7 x 2GB = 14GB）。

4 个 vCPU 和 16GB 实例能够运行这些工作负载？

让我们计算一下保留的 CPU：

```
6% of the first core        = 60m +
1% of the second core       = 10m +
0.5% of the remaining cores = 10m
---------------------------------
total                       = 80m
```

可用于运行 Pod 的 CPU 为 3.9 个虚拟 CPU（即 4000m - 80m）——远远足够。

接下来，我们来检查为 kubelet 保留的内存：

```
25% of the first 4GB of memory = 1GB
20% of the following 4GB of memory  = 0.8GB
10% of the following 8GB of memory  = 0.8GB
--------------------------------------
total                          = 2.8GB
```

Pod 可用的总内存为 16GB - （2.8GB + 0.1GB）——其中 0.1GB 考虑了 100MB 的驱逐阈值。

最后，Pod 可使用的内存最多为 13.1GB 。

![在拥有 2 vCPU 和 16GB 内存的 Kubernetes 节点上的资源分配](https://learnk8s.io/a/c72727b60ee6387d73c40004f9003561.svg)

**不幸的是，这不够用（即 7 个副本需要 14GB 内存，但你只有 13.1 GB），你应该配置一个具有更多内存的计算单元来部署工作负载。**

如果你使用云提供商，下一个可用的计算单元增量是 4 vCPU 和 32GB 内存。

![拥有 2 vCPU 和 16GB 内存的节点不足以运行七个副本](https://learnk8s.io/a/c1be9a8de0824f6e5abcba5371bb9b4e.svg)


太好了！

现在，让我们看看另一种情况，即我们尝试找到适合单个副本的最小实例，该副本的请求为 0.3 vCPU 和 2GB 内存。

**我们尝试使用具有 1 vCPU 和 4GB 内存的实例类型。**

kubelet 保留的 CPU 总计为 6% 或 60m，Pod 可用的 CPU 为 940m。

由于该应用程序仅需要 300m 的CPU，这是足够的。

kubelet保留的内存为 25% 或 1GB，再加上额外的 0.1GB 的驱逐阈值。

Pod 可用的总内存为 2.9GB；由于该应用程序仅需要 2GB，这个值足够了。

很棒！

![在拥有 2 vCPU 和 16GB 内存的 Kubernetes 节点上的资源分配](https://learnk8s.io/a/f97ca286843a3ff5ee0fbc9a55630829.svg)

现在，让我们比较这两种设置。

第一个集群的总资源只是一个单一节点—— 4 vCPU 和 32 GB。

第二个集群有 7 个实例，每个实例有 1 vCPU 和 4GB 内存（总计 7 vCPU 和 28 GB 内存）。

在第一个示例中，Kubernetes 保留了 2.9GB 的内存和 80m 的 CPU。

在第二个示例中，保留了 7.7GB（1.1GB x 7 个实例）的内存和 360m 的 CPU（60m x 7 个实例）。

**你已经注意到在配置较大的节点时资源的利用效率更高。**

![在单个节点的集群和多个节点的集群之间比较资源分配](https://learnk8s.io/a/23885fd9cefd09159d3bab9618a55aae.svg)

*但是还不仅仅是这样。*

较大的实例仍然有空间可以运行更多的副本——但是有多少呢？

* 保留的内存为 3.66GB（3.56GB kubelet + 0.1GB 的驱逐阈值），Pod 可用的总内存为 28.44GB。
* 保留的 CPU 仍然是 80m，Pod 可以使用 3920m。

在这一点上，你可以通过以下的除法找到内存和 CPU 的最大副本数量：

```
Total CPU   3920 /
Pod CPU      300
------------------
Max Pod       13.1
```

你可以针对内存重复上述的计算：

```
Total memory  28.44 /
Pod memory     2
---------------------
Max Pod       14.22
```

但是，让我们观察一下当你再次扩展部署时会发生什么——这次是到 17 个副本（即多 2 个副本）。

以上的数字表明，在 4 vCPU 和 32GB 的工作节点上，你在内存之前耗尽了 CPU ，最多可以托管 13 个副本。

![计算 2 vCPU 和 32GB 工作节点的 Pod 容量](https://learnk8s.io/a/8166b554c895b638a68d2ef76475f943.svg)

那么第二种情况呢？

还有扩展的空间吗？

实际上没有。

**虽然这些实例仍然具有更多的 CPU，但在部署第一个 Pod 之后，它们只有 0.9GB 的可用内存。**

![计算1 vCPU和4GB工作节点的Pod容量](https://learnk8s.io/a/2e379971f411f7ca2908ebed0798c020.svg)

总之，较大的节点不仅能更好地利用资源，还可以减少资源的碎片化，并提高效率。

这是否意味着你应该总是配置更大的实例？

让我们看看另一种极端情况：当一个节点意外丢失时会发生什么？

## 弹性和复制

少量的节点可能会限制您的应用程序的有效复制程度。

例如，如果您有一个高可用性应用程序，由 5 个副本组成，但只有两个节点，则有效复制程度将减少到 2 个。

这是因为这五个副本只能分布在两个节点上，如果其中一个节点失败，可能会同时使多个副本停机。

![拥有两个节点和五个副本的集群的复制因子为两个](https://learnk8s.io/a/4db4fb1e1af84fcbcec51b23f9b9e77f.svg)

另一方面，如果您至少有五个节点，每个副本都可以在单独的节点上运行，如果一个节点失败，最多只会影响一个副本。

**因此，如果您具有高可用性要求，可能需要在集群中拥有一定数量的最小节点数。**

![拥有五个节点和五个副本的集群的复制因子为五个](https://learnk8s.io/a/4b0ddbe420f754323537c3bde7f938e2.svg)

您还应该考虑节点的大小。

当较大的节点丢失时，一些副本最终会被重新调度到其他节点。

如果节点较小且仅托管了少量工作负载，则调度程序只会重新分配少量 Pod 。

尽管调度程序不太可能出现任何限制，但重新部署许多副本可能会触发集群自动缩放器。

而且根据您的设置，这可能会导致进一步的减速。

让我们探讨一下为什么会这样。

## 扩展增量和引导时间

您可以[使用水平扩展器（即增加副本数）和集群自动缩放器（即增加节点数）的组合来扩展在 Kubernetes 上部署的应用程序](https://learnk8s.io/kubernetes-autoscaling-strategies)。

*假设您的集群已达到总容量，那么节点大小如何影响您的自动缩放？*

首先，您应该知道集群[自动缩放器在触发自动缩放时不会考虑内存或 CPU 的可用性](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#should-i-use-a-cpu-usage-based-node-autoscaler-with-kubernetes)。

换句话说，完全利用的集群不会触发集群自动缩放器。

相反，当 Pod 由于资源不足而无法调度时，集群自动缩放器会创建更多节点。

此时，自动缩放器调用云提供商 API ，为该集群提供更多的节点。


![](https://learnk8s.io/a/a26ee4d5052d327089d62b6da143f914.svg)
*(1) 当Pod由于资源不足而等待时，集群自动缩放器提供新的节点。*

![](https://learnk8s.io/a/6a29222a3225ebb38f4e758210ca85b5.svg)
*(2)当Pod由于资源不足而等待时，集群自动缩放器提供新的节点。*

**不幸的是，通常情况下，提供节点是很慢的。**

创建一个新的虚拟机可能需要几分钟的时间。

在较大或较小的节点上，是否可以更改提供时间？

不可以，无论实例大小如何，通常时间都是恒定的。

**而且，集群自动缩放器不限于一次添加一个节点；它可能一次性添加多个节点。**

我们来看一个示例。

有两个集群：

1. 第一个集群有一个拥有 4 vCPU 和 32GB 的单个节点。
2. 第二个集群有 13 个拥有 1 vCPU 和 4GB 的节点。

部署一个需要 0.3 vCPU 和 2GB 内存的应用程序，然后将其扩展到 13 个副本。

这两个设置都已达到总容量——它们没有额外的空间供 Pod 使用。

![一个节点一个Pod和所有Pod放入单个节点](https://learnk8s.io/a/f9fd8d7bfbc21dbf4e2f34d68489d1f7.svg)

当部署扩展到 15 个副本（即多 2 个副本）时会发生什么？

在这两个集群中，集群自动缩放器检测到额外的 Pod 由于资源不足而无法调度，然后进行以下操作：

1. 为第一个集群提供一个额外的拥有 4 vCPU 和 32GB 的节点。
2. 为第二个集群提供两个拥有 1 vCPU 和 4GB 的节点。

由于在不同实例上提供节点没有时间差异，所以这两种情况下的节点将同时可用。

![](https://learnk8s.io/a/ab3adead1eea7f1615bff64488318317.svg)

无论如何，你能发现另一个区别吗？

第一个集群还有空间可以容纳更多的 Pod ，因为总容量为 13 个。

相反，第二个集群仍然已满。

你可以说较小的增量更高效且更便宜，因为你只添加所需的内容。

![Kubernetes 节点中的自动扩展增量比较](https://learnk8s.io/a/4b5b12047d321e34a6c2455677fd99a0.svg)

但是，让我们观察一下当你再次扩展部署时会发生什么——这次是到 17 个副本（即多 2 个副本）。

* 第一个集群在现有节点上创建了两个额外的Pod。
* 第二个集群已达到容量上限。Pod处于待定状态，触发集群自动缩放器。最终，将提供两个额外的工作节点。

![Kubernetes节点中自动扩展增量的权衡](https://learnk8s.io/a/be78be3cd35dc7387e2352c4630c5ae9.svg)

**在第一个集群中，扩展几乎是瞬时的。**

而在第二个集群中，你必须等待节点被提供，然后 Pod 才能提供服务。

换句话说，在前一种情况下，扩展速度更快，在后一种情况下，扩展需要更长时间。

**通常情况下，由于提供时间在几分钟范围内，您应该谨慎考虑是否频繁触发集群自动缩放器，以避免产生更长的 Pod 引导时间。**

换句话说，如果您可以接受（可能）未充分利用资源，那么在较大节点上可以更快地进行扩展。

*但是事情并没有结束。*

拉取容器映像也会影响您可以多快地扩展工作负载，而这与集群中的节点数量有关。

## 拉取容器映像

在 Kubernetes 中创建一个 Pod 时，其定义会存储在 etcd 中。

kubelet 的工作是检测到 Pod 分配给其节点，并创建它。

kubelet将会：

* 从控制平面下载定义。
* [调用容器运行时接口（CRI）来创建 Pod 沙箱。 CRI 调用容器网络接口（CNI）以将 Pod 连接到网络。](https://learnk8s.io/kubernetes-network-packets#how-linux-network-namespaces-work-in-a-pod)
* 调用容器存储接口（CSI）以挂载任何容器卷。

在这些步骤结束时，Pod 已经运行，kubelet 可以继续检查存活性和就绪性探针，并将新 Pod 的状态更新到控制平面。

![Kubelet和CRI、CSI以及CNI接口](https://learnk8s.io/a/b321498cc64bfd4bc424abd7a8a8f461.svg)

**需要注意的是，当 CRI 在 Pod 中创建容器时，它必须首先下载容器映像。**

除非容器映像已在当前节点上缓存，否则需要下载。

我们来看一下这如何影响在两个集群中进行扩展：

1. 第一个集群有一个拥有 4 vCPU 和 32GB 的单个节点。
2. 第二个集群有 13 个拥有 1 vCPU 和 4GB 的节点。

让我们部署一个需要 0.3 vCPU 和 2GB 内存的应用程序的 13 个副本。

该应用程序使用[基于 OpenJDK 的](https://hub.docker.com/_/openjdk)容器映像，重量为 1GB（基本映像本身为775MB）。

这对这两个集群有什么影响？

* 在第一个集群中，容器运行时仅下载一次映像并运行13个副本。
* 在第二个集群中，每个容器运行时都会下载和运行映像。

在第一种情况下，只会下载 1GB。

![容器运行时只下载一次容器映像并运行 13 个副本](https://learnk8s.io/a/352ea906f7800c90ed71deea01eac4f1.svg)

然而，在第二种情况下，您将下载 13GB 的容器映像。

由于下载需要时间，第二个集群在创建副本方面要比第一个集群慢。

它还使用更多的带宽并进行更多的请求（即至少为每个映像层进行一次请求，共 13 次），这使得它更容易受到网络故障的影响。

![每个13个容器运行时下载一个映像](https://learnk8s.io/a/d4dfe6e68938734993dd6b5bd2498e7b.svg)

需要注意的是，这个问题会随着集群自动缩放器而加剧。

如果您的节点较小：

* 集群自动缩放器一次提供多个节点。
* 一旦准备就绪，每个节点开始下载容器映像。
* 最后，Pod 被创建。

当您提供较大的节点时，映像可能已缓存在节点上，Pod 可以立即启动。


![想象一下，有一个拥有8个节点的集群，每个节点一个副本。](https://learnk8s.io/a/c77ad0aa9e0afa24e57788948ee1b12c.svg)
*想象一下，有一个包含8个节点的集群，每个节点上有一个副本。*

![](https://learnk8s.io/a/d3b49aee1e2a56dfe0509c3874c308a8.svg)
*集群已满；将副本扩展到16个会触发集群自动缩放器。*

![](https://learnk8s.io/a/6b09aa74b75b631b7be55c492d80c084.svg)
*一旦节点被配置，容器运行时会下载容器镜像。*

![](https://learnk8s.io/a/4f053af905c5ceb1f89c9a70dcabebd9.svg)
*最后，在节点上创建了Pod。*

那么，您是否应该始终提供较大的节点？

不一定。

您可以通过[容器注册表代理](https://github.com/rpardini/docker-registry-proxy)来减轻节点下载相同容器映像的问题。

在这种情况下，仍然会下载映像，但是从当前网络中的本地注册表下载。

或者您可以使用诸如 [Spegel](https://github.com/XenitAB/spegel) 之类的工具预热节点的缓存。

使用 Spegel ，节点是可以广告和共享容器映像层的对等体。

在另一种情况下，容器映像从其他工作节点下载，Pod 几乎可以立即启动。

但是，容器带宽不是您必须控制的唯一带宽。

## Kubelet 和扩展 Kubernetes API

kubelet 旨在从控制平面中提取信息。

因此，定期间隔内，kubelet 会向 Kubernetes API 发出请求，以检查集群的状态。

*但是，控制平面是否发送指令给 kubelet？*

拉模型更容易扩展，因为：

* 控制平面不必将消息推送到每个工作节点。
* 节点可以独立地以自己的速度查询API服务器。
* 控制平面不必保持与kubelet的连接开放。

> 请注意，也有明显的例外。诸如 kubectl logs 和 kubectl exec 之类的命令需要控制平面连接到 kubelet（即推模型）。

但是 Kubelet 不仅仅查询信息。

它还向 master 平面报告信息。

例如，[kubelet 每隔十秒向集群报告节点状态](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#:~:text=%2D%2Dnode%2Dstatus%2Dupdate%2Dfrequency)。

此外，kubelet 在就绪探针失败（以及应从服务中删除 Pod 端点）时通知控制平面。

并且 kubelet 将容器指标的状态及时更新到控制平面。

换句话说，kubelet 向控制平面发出多个请求（即从控制平面和到控制平面的双向请求）以保持节点正常运行。

在 Kubernetes 1.26 及更早版本中，[kubelet 每秒最多可以发出 5 个请求（在 Kubernetes >1.27 中，这一限制已放宽](https://kubernetes.io/blog/2023/05/15/speed-up-pod-startup/#raised-default-api-query-per-second-limits-for-kubelet)）。

那么，假设您的 kubelet 运行在满负荷状态下（即每秒 5 个请求），当您运行几个较小的节点与运行单个较大的节点时，会发生什么？

我们来看看我们的两个集群：

1. 第一个集群有一个拥有 4 vCPU 和 32GB 的单个节点。
2. 第二个集群有13个拥有 1 vCPU 和 4GB 的节点。

第一个集群生成每秒 5 个请求。

![单个kubelet每秒发出5个请求](https://learnk8s.io/a/cb5baa1a4b290bff10e3f693fb5fce97.svg)

第二个集群每秒发出 65 个请求（即 13 x 5）。

![13 个kubelet每秒发出 5 个请求](https://learnk8s.io/a/106f96256da416271d46d757e912c983.svg)

当您在运行较多较小的节点的集群中运行集群自动缩放器时，您应该将 API 服务器的扩展到适应更频繁的请求。

反过来，这通常意味着在较大的实例上运行控制平面或运行多个控制平面。

## 节点和集群限制

Kubernetes 集群的节点数量是否有限制？

[Kubernetes 设计支持最多 5000 个节点。](https://kubernetes.io/docs/setup/best-practices/cluster-large/)

但是，这不是一个硬性约束，正如 Google 团队所演示的，[您可以在 15,000 个节点上运行 GKE 集群](https://cloud.google.com/blog/products/containers-kubernetes/google-kubernetes-engine-clusters-can-have-up-to-15000-nodes)。

对于大多数用例来说，5000 个节点已经是一个很大的数字，可能不会影响您对较大或较小节点的决策。

相反，您可以在集群中运行的最大 Pod 数量可能会促使您重新考虑集群架构。

那么，在 Kubernetes 节点中可以运行多少个 Pod ？

大多数云提供商允许在每个节点上运行 110 到 250 个Pod。

如果您自己创建集群，[那么默认值是 110](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/#:~:text=Default%3A%20%22promiscuous%2Dbridge%22-,maxPods,-int32)。

在大多数情况下，这个数字不是 kubelet 的限制，而是云提供商在风险双预订 IP 地址的情况下的限制。

为了理解这意味着什么，让我们退一步，看看集群网络是如何构建的。

在大多数情况下，每个工作节点被分配一个子网，其中包含 256 个地址（例如 10.0.1.0/24 ）。

![每个工作节点都有一个分配的子网](https://learnk8s.io/a/cc3274f66d411c87546f1eb88a42511d.svg)

其中[两个是受限](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/)的，您可以使用 254 个用于运行您的 Pod。

考虑一个情况，您在同一个节点上有 254 个 Pod。

您再创建一个 Pod，但用尽了可用的 IP 地址，因此它保持处于挂起状态。

为了解决这个问题，您决定将副本数减少到 253。

挂起的 Pod 是否在集群中被创建？

很可能不会。

当您删除 Pod 时，其状态变为 "Terminating" 。

kubelet 发送 SIGTERM 信号给 Pod（如果存在的话，还调用 preStop 生命周期钩子），并等待容器正常关闭。

如果容器在 30 秒内未终止，kubelet 会发送 SIGKILL 信号给容器，并强制终止进程。

在此期间，Pod 仍然没有释放 IP 地址，流量仍然可以到达它。

当 Pod 最终被删除时，IP 地址被释放。

![](https://learnk8s.io/a/01b4a22bf8aa92a7998540f6ac1516e0.svg)
*当 Pod 被删除时，kubelet 会收到更改通知。*

![](https://learnk8s.io/a/ba13194ea5b9ef63597e8fb059355887.svg)
*如果 Pod 具有 preStop 钩子，首先会调用它。然后，kubelet 发送 SIGTERM 信号给容器。*

![](https://learnk8s.io/a/eaba36dda660dd289189979c3b6ce3c4.svg)
*默认情况下，进程有30秒的时间退出，包括preStop钩子。如果进程在这之前没有退出，kubelet会发送SIGKILL信号并强制终止进程。*

![](https://learnk8s.io/a/c05c50cd03dba4465b38b95a016b3712.svg)
*kubelet 通知控制平面成功删除了 Pod。IP 地址最终被释放。*

此时，挂起的 Pod 可以被创建，并被分配与上一个 Pod 相同的 IP 地址。

这是一个好主意吗？

嗯，没有其他可用的 IP 地址 —— 所以您别无选择。

![](https://learnk8s.io/a/e038d5441bbab5e27bff91fa567517e0.svg)
*想象一下，您的节点正在使用所有可用的IP地址。*

![](https://learnk8s.io/a/f0bdd2ddeb962d9e3303965eef0006d3.svg)
*当一个Pod被删除时，IP地址不会立即释放。您必须等待正常关闭。*

![](https://learnk8s.io/a/362ab748b014147011e2a723ae8fa71b.svg)
*一旦Pod被删除，IP地址就可以被重新使用。*

这会有什么后果？

还记得我们提到过 Pod 应该正常关闭并处理所有待处理的请求吗？

好吧，如果 Pod 被突然终止（即没有正常关闭），并且 IP 地址立即被分配给另一个 Pod ，所有现有的应用程序和 Kubernetes 组件可能仍然不会意识到这种变化。

结果，一些现有的流量可能会错误地发送到新的 Pod ，因为它具有与旧的 Pod 相同的 IP 地址。

![](https://learnk8s.io/a/7b2d466a8559f46f477801ae2ca257fd.svg)
*入口控制器将流量路由到一个IP地址。*

![](https://learnk8s.io/a/a785b7150b052e5f5f6906c17c7312b8.svg)
*如果IP地址在不等待正常关闭的情况下被重新分配并用于一个新的Pod，入口控制器可能仍然会将流量路由到该IP地址。*

为了避免这个问题，您可以分配较少的 IP 地址（例如 110），并将其余的 IP 地址用作缓冲区。

这样，您可以相当确定相同的 IP 地址不会立即被重新使用。

## 存储

计算单元对可以附加的磁盘数量有限制。

例如，在 Azure 上，具有 2 个 vCPU 和 8GB 内存的 Standard_D2_v5 最多可以附加 4 个数据磁盘。

如果您希望将一个 StatefulSet 部署到使用 Standard_D2_v5 实例类型的工作节点上，您将无法创建超过四个副本。

这是因为 StatefulSet 中的每个副本都附加了一个磁盘。

一旦创建第五个副本，Pod 将保持挂起状态，因为持久卷声明无法绑定到持久卷。

那为什么不行？

因为每个持久卷都是一个附加的磁盘，您只能为该实例有 4 个持久卷。

那么，您的选择是什么？

您可以配置一个更大的实例。

或者您可以使用不同的 subPath 字段重新使用相同的磁盘。

让我们来看一个例子。

以下持久卷需要一个具有 16GB 空间的磁盘：

* pvc.yaml

```yaml 

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared
spec:
  storageClassName: default
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 16Gi
```

如果您将此资源提交到集群，您将看到创建了一个持久卷，并将其绑定。

```bash
kubectl get pv,pvc
```

持久卷与持久卷声明之间是一对一的关系，因此您将无法有更多的持久卷声明来使用同一个磁盘。

如果您想在 Pod 中使用该声明，可以这样做：

* deployment-1.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app1
spec:
  selector:
    matchLabels:
      name: app1
  template:
    metadata:
      labels:
        name: app1
    spec:
      volumes:
        - name: pv-storage
          persistentVolumeClaim:
            claimName: shared
      containers:
        - name: main
          image: busybox
          volumeMounts:
            - mountPath: '/data'
              name: pv-storage
```

您可以有另一个使用相同持久卷声明的部署：

* deployment-1.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app2
spec:
  selector:
    matchLabels:
      name: app2
  template:
    metadata:
      labels:
        name: app2
    spec:
      volumes:
        - name: pv-storage
          persistentVolumeClaim:
            claimName: shared
      containers:
        - name: main
          image: busybox
          volumeMounts:
            - mountPath: '/data'
              name: pv-storage
```

然而，使用这个配置，两个 Pod 将在同一个文件夹中写入数据。

您可以让它们在子目录中工作，使用 subPath 来解决这个问题。

```yaml
deployment-1.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app2
spec:
  selector:
    matchLabels:
      name: app2
  template:
    metadata:
      labels:
        name: app2
    spec:
      volumes:
        - name: pv-storage
          persistentVolumeClaim:
            claimName: shared
      containers:
        - name: main


          image: busybox
          volumeMounts:
            - mountPath: '/data'
              name: pv-storage
              subPath: app2
```

这些部署将在以下路径上写入数据：

* /data/app1 对于第一个部署和
* /data/app2 对于第二个。

这个解决方法不是一个完美的解决方案，有一些局限性：

* 所有部署都必须记住使用 subPath。
* 如果您需要写入卷，您应该选择一个可以从多个节点访问的 Read-Write-Many 卷，这些卷通常难以配置。

此外，对于一个 StatefulSet ，相同的解决方法也不适用，因为这将为每个副本创建一个全新的持久卷声明（和持久卷）。

## 总结和结论

那么，在集群中应该使用少量大节点还是许多小节点呢？

这取决于您在集群中部署的工作负载。

例如，如果您的应用程序需要 10GB 内存，使用 16GB 内存的实例等同于"运行较小的节点"。

对于只需要 64MB 内存的应用程序，相同的实例可能被认为是"大"的，因为您可以容纳多个实例。

那么，对于具有不同资源需求的各种工作负载的混合呢？

在 Kubernetes 中，没有规定所有节点必须具有相同的大小。

您完全可以在集群中使用不同大小的节点组合。

这可能使您能够权衡两种方法的利弊。

虽然您可能会通过试错来找到答案，但我们还建立了一个工具来帮助您进行这个过程。

[Kubernetes 实例计算器](https://learnk8s.io/kubernetes-instance-calculator)可以让您探索适用于给定工作负载的最佳实例类型。

确保您试一试。