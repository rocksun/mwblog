# Kubernetes 内存请求和限制的实际工作原理

![Featued image for: How Kubernetes Memory Requests and Limits Actually Work](https://cdn.thenewstack.io/media/2024/11/55418f14-image25.png)

**另请阅读：**

* **第一章：** [Kubernetes 请求和限制的实际工作原理](https://thenewstack.io/how-kubernetes-requests-and-limits-really-work/)
* **第二章：** [Kubernetes CPU 请求和限制的实际工作原理](https://thenewstack.io/how-k8s-cpu-requests-and-limits-actually-work-chapter-2/)
* **第四章：** [K8s 驱逐机制：资源管理出错](https://thenewstack.io/how-k8s-eviction-works-resource-management-gone-wrong/)

深入理解 Kubernetes 资源管理的神秘内部机制，会让你感觉像个巫师。正如本系列第一篇文章中详细介绍的那样，成为 Kubernetes 资源管理的巫师，需要对 Kubernetes 中的资源管理功能有一个端到端的上下文理解，包括从其用户抽象到 Linux 内核级别的技术实现等一切内容。

在本系列第一章中，我们详细介绍了如何使用 pod 规范和节点状态来匹配待处理的 pod 和可用的节点。在第二章中，我们深入探讨了如何将[请求和限制](https://thenewstack.io/kubernetes-requests-and-limits-demystified/)转换为 Linux cgroup 的 CPU 设置，以及这对性能和可靠性结果意味着什么。

第三章将继续深入探讨内存，目标是揭示内存请求和限制在 Linux 层面变成了什么，理解这种转换是如何执行的，以及它在预测、预测或保证内存资源结果方面意味着什么。

## 旅程继续

Kubernetes pod 的调度完全基于它们的请求。节点的“满负荷”是基于请求的，忽略使用情况和限制。Cgroup 用于对进程施加约束和好处，并且它们具有层次结构。Kubernetes 使用从 Kubepods => (QoS level)? => pod => container 的层次结构设置 cgroup。基于 CPU 请求和限制的转换，每个 cgroup 都获得 `cpu.weight` 和/或 `cpu.max` 设置的值。最快捷的回顾。🏁

现在让我们重置，转向并专注于内存。

根据我们了解的 CPU 请求和限制的实现方式，cgroup 看起来确实很重要。Kubernetes 在 cgroup 方面为内存提供了哪些功能？

对于内存资源：

这里似乎缺少一些东西。没有与内存请求[对应的 cgroup 设置](https://thenewstack.io/stop-setting-cpu-and-memory-requests-in-kubernetes/)抽象。我们上次了解到，CPU 请求是一种保证，如果进程需要那么多 CPU，它就能得到。Kubernetes 能否用内存匹配这种保证，并确保工作负载请求的任何内存都能得到？

*注意：目前常用的 cgroup API 有两个版本。为了简单起见，本文其余部分仅指 cgroup v2 设置名称。使用 v1 实现具有功能上等效的结果*

## 内存是成败的关键

关于内存资源，需要提前知道的一件关键事情是，内存不是可压缩的资源，这与 CPU 不同。

CPU 时间可以被暂停或延迟而不会终止进程，尽管这样做可能会影响性能。内存并非如此。你要么得到它，要么得不到。没有尝试，也没有延迟。如果一个进程需要更多内存，要么会分配更多内存，要么进程会被终止。是的，Kubernetes 会重新启动它，但损害可能已经造成。

因此，避免不足似乎很重要。

## 内存限制

我们将首先深入探讨内存限制的工作原理，因为对于内存来说，限制比请求更简单。

当你在 Kubernetes 中设置内存限制时，它从根本上来说是一个字节值，容器运行时所做的全部工作就是将该数字直接插入容器 cgroup 的 `memory.max` 控制中。就是这样。

如果 cgroup 的内存使用量超过该限制，OOMKiller 将会将其清除。超过限制的容器（进程/进程）将被清除，并且清除将仅限于该容器。在清除过程中，不会损害其他容器。就这么简单。

另一个有助于简化此清除过程的 cgroup 设置是 `memory.oom_group`。

“容器”是一个 cgroup，一个 cgroup 可以运行多个进程。OOMKiller 从技术上讲不需要杀死容器的所有进程；它理论上可以只杀死一个或杀死多个。

在最近的 Kubernetes 版本中，每个容器 cgroup 的 `memory.oom_group` cgroup v2 控制都设置为 true（或技术上的“1”）。这避免了在超过限制时 OOMKiller 将执行的操作的歧义：容器中的所有进程都将被杀死。

## Cgroup 和内存请求
Kubernetes 不会根据内存请求设置任何 cgroup 控制。

考虑到 CPU 请求具有如此优雅和受保护的分配结果，这可能会让人感到失望。

在撰写本文时，存在一个 cgroup v2 控制，Kubernetes 理论上可以使用它来基于容器的请求建立基线内存保护：但是，Kubernetes 没有使用此设置。[memory.low](https://facebookmicrosites.github.io/cgroup2/docs/memory-controller.html)

虽然 cgroup 在根据 Kubernetes CPU 请求保证 CPU 时间方面非常有效，但在 Kubernetes 内存请求方面，它们并没有被用于任何用途。我们必须从其他地方寻找 Kubernetes 为尝试保护（或偏好）在内存开始紧张且 OOMKiller 开始调用时使用少于其请求的内存的进程所做的工作。

## 警惕 OOMKiller
如果我们讨论的是内存耗尽时会发生什么，我们需要确保我们已经对被称为 OOMKiller 的 Linux 神话怪物建立了一个水平集。

OOMKiller 是一个 [Linux 内核](https://thenewstack.io/linux-kernel-6-12-prepped-for-superior-scheduling-real-time-ops/) 功能，当节点内存不足时调用。当尝试使用内存的进程导致页面错误但没有可用的物理内存时，它会被触发。在 OOMKiller 离开之前，它将选择至少一个进程终止，释放该进程一直在使用的内存。

OOMKiller 选择的进程可能与触发页面错误的进程相同，也可能不同。鉴于不能保证页面错误进程将是死亡的进程，我们如何确定 OOMKiller 将选择哪个进程作为其受害者？

OOMKiller 决策的细节以及如何影响它，是 Kubernetes 如何尝试保护和保护“行为良好”的容器进程（那些使用小于或等于其请求的内存的进程）的基础。

## 准备一些数学计算
Kubernetes 为容器内存制定的第一个保护措施是，与 CPU 一样，如果正在运行的容器内存请求的总和超过节点的可分配内存，Kubernetes 不会在节点上运行任何新的 Pod。节点上将始终有足够的内存让每个容器使用与其请求一样多的内存。这不是直接保护，而是一种逻辑保护：如果所有容器使用的内存都小于或等于其请求的内存量，则不应调用 OOMKiller。

但我们都知道确保容器的内存使用量保持在或低于其内存请求是多么困难。如果一个或多个容器消耗的内存超过请求的内存，则 OOMKiller 可能会出现。

以下是预测在这种情况下哪些 Kubernetes 容器进程将被 OOMKilled 的方法。

### OOM 分数
现代 OOMKiller 使用相当简单的算法来选择它将终止哪些进程。每个进程都会根据进程使用的内存量获得一个 `oom_score`。使用更多内存的进程会获得更高的分数。当 OOMKiller 开始调用时，分数最高的进程将首先被终止。

分数高 🏆，损失大 ☠️。

Linux 允许用户——以及 Kubernetes——通过设置一个 `oom_score_adj` 数字来影响进程的 `oom_score`，该数字的范围从 -1000 到 1000。Kubelet 为其启动的每个容器进程设置一个 `oom_score_adj`，并使用巧妙的数学方法来确保（以合理的确定性）使用超过其请求的内存的容器将始终在行为良好的容器（使用少于其请求的容器）之前终止。它设置的内容已 [记录](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#node-out-of-memory-behavior)。该数学方法如何帮助我们有点模糊，因此这里有一个扩展的解释。

BestEffort Pod 的 `oom_score_adj` 为 1000，这基本上是“请杀死我”的代码。成为 OOMKilling 的首选是有道理的；在 Pod 调度期间不会考虑它们，因此如果出现任何问题，它们应该被清除。

另一方面，所有 Guaranteed QoS 容器上设置的 `oom_score_adj` 为 -997，相当于来自系统 OOMKiller 的近乎无敌。在 Guaranteed QoS 容器之前，几乎所有其他内容都将被杀死。这也是有道理的，因为 Guaranteed QoS 容器在超过其自身请求时总是会被立即杀死，而不管系统容量如何；系统 OOMKiller 不需要针对它们。

对于 Burstable QoS，这个等式的效果，它的工作原理以及它在保护行为良好的进程方面的可靠性，如果不真正了解 `oom_score` 和 `oom_score_adj` 的确切工作原理，就很难确定。最后，可以公平地说，`oom_score_adj`
使用此公式设置的值非常有效，可以确保使用超过请求内存的突发型容器在任何使用较少内存的突发型容器之前被终止。

### 为什么？

OOM 分数范围为 0 到 2000，基于进程使用了多少节点内存。`oom_score_adj` 值可以强制对进程进行评分，就好像它始终使用了超出实际使用量的额外百分比的节点内存。例如：

- 值为 250 将导致对进程进行评分，就好像它使用了相当于节点容量 25% 的额外内存。
- 值为 1000（最大值）将导致对进程进行评分，就好像它使用了相当于节点容量 100% 的额外内存。

对于我们这些数学爱好者，计算细节如下所示。

*有趣的小知识：由于应用了缩放因子，使用少量内存的新进程的实际 OOM 分数为 666。如果您的系统上有许多进程的*oom_score*为 666，请不要担心：这完全正常，不是世界末日的预兆。*

回想一下，对于突发型 Pod，Kubernetes 将 `oom_score_adj` 设置为

![](https://cdn.thenewstack.io/media/2024/11/a609ca9c-codecogsequation-300x41.png)

公式

这是什么作用？

举个简单的例子：如果容器请求节点内存容量的 3%，Kubernetes 将 `oom_score_adj` 值设置为 97% (970)。如果容器请求节点容量的 32%，Kubernetes 将 `oom_score_adj` 值设置为 68% (680)。

简而言之，此 `oom_score_adj` 设置计算会规范化所有突发型容器的评分内存等效值，这样如果每个容器都*正好*使用它请求的内存，则每个容器将具有*正好*相同的 `oom_score`。

下图以节点容量的百分比（而不是字节）来说明内存请求和 OOM 分数点，以演示 `oom_score` 规范化方案的工作原理。

任何使用超过其请求内存的突发型容器，无论该容器的大小如何，其 `oom_score` 都将大于此规范化的“完全请求使用量”值。因此，任何使用超过其请求内存的容器的 `oom_score` 都将高于所有使用小于或等于其内存请求的容器。

下图演示了一个小型容器，它使用了相对较少的内存，但仍然超过了它的请求，它将获得比突发型 QoS 类中任何其他容器更高的 `oom_score`。

此 `oom_score_adj` 技巧不如 `memory.low` 等 cgroup 控制那样简洁易懂，其精度受 `oom_score_adj` 设置分辨率的限制；但是，就保护容器免受系统 OOMKiller 的影响而言，这是一个相当合理的实现，只要它们的内存使用量在请求值范围内。

很高兴知道 Kubernetes 在进程使用少于请求的内存时做得很好。但是，在结束之前，记住我们开始的内容很重要：内存竞争是生死攸关的情况。在需要终止某个进程时做出合理的决定来终止哪个进程是很好的，但理想情况下，我们希望避免一开始就必须做出这样的决定。

## 旅途继续：节点压力驱逐

实现 CPU 和内存请求和限制在很大程度上是一项预先设置的任务，由 kubelet 和容器运行时执行，将资源抽象中的数字转换为 cgroup 和 Linux 进程设置。Linux 本身负责运行时强制执行，而 Kubernetes（编排器）则退居二线。

不过，Kubelet 并没有完全退出游戏。当 Linux 似乎难以应对时，Kubelet 将重新出现并尝试帮助解决问题。我们将在下一章中了解其工作原理，并在本系列的下一章（也是最后一章）中总结我们所做的所有关键观察结果。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)