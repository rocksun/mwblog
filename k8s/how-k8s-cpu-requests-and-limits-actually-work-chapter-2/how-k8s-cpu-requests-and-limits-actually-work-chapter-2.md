
<!--
title: K8s CPU Request和Limit实际工作原理 — 第二章
cover: https://cdn.thenewstack.io/media/2024/11/9453c09f-wizard.jpg
-->

深入探讨 CPU，探索 CPU 资源Request和Limit如何在 Linux 操作系统层面发挥作用。

> 译自 [How K8s CPU Requests and Limits Actually Work — Chapter 2](https://thenewstack.io/how-k8s-cpu-requests-and-limits-actually-work-chapter-2/)，作者 Reid Vandewiele。

阅读[第一章: Kubernetes Request和Limit的实际工作原理](https://thenewstack.io/how-kubernetes-requests-and-limits-really-work/)。

深入理解 Kubernetes 资源管理神秘的内部工作原理会让你感觉像个巫师。正如本系列上一篇文章中详述的那样，成为 Kubernetes 资源管理的巫师需要对 Kubernetes 中资源管理的运作方式有一个端到端的上下文理解，包括从用户抽象到 Linux 内核级别的技术实现的所有内容。

在第 1 章中，我们详细介绍了如何使用 Pod 规范和节点状态来匹配挂起的 Pod 和可用节点。一旦匹配成功，节点就需要运行 Pod。第 2 章继续深入探讨 CPU，着手回答 CPU 资源请求和限制如何在 Linux 操作系统级别发挥作用的问题，以及这对于预期、预测或保证 CPU 资源结果意味着什么。

## 旅程继续

在我们深入探讨Request和Limit如何影响正在运行的容器的细节之前，我们必须先介绍 pod 如何被调度到节点。关于资源，最重要的几点是，pod 是根据它们的资源Request大小和节点报告的容量大小分配到节点的，并且节点的“满载”完全基于Request，与资源使用情况或资源Limit无关。

为了重新开始，假设在你的 Kubernetes pod 规范中，你Request了 250 毫核 CPU 来运行你的容器。现在，该 pod 已被调度到一个节点状态报告为 1,930m 可分配 CPU 容量的节点上运行。接下来会发生什么？

必须发生一些事情才能将这个抽象的Request（250m CPU）以及任何Limit转换为围绕正在运行的进程的一组具体分配或约束。这是必要的，因为 Kubernetes 不是操作系统，它只是一个编排器。将由 Linux（作为实际的操作系统）来强制执行与资源相关的设置。但 Linux 不理解Request和Limit的抽象概念。需要进行转换来配置负责实际执行的 OS 子系统。

大多数 Kubernetes 资源抽象都是由 kubelet 和容器运行时使用 Linux 控制组 (cgroups) 和控制组设置来实现的。

我们现在只关注 CPU。对于 CPU 资源，相关的 cgroup 设置是：

| Kubernetes 抽象 | 转换为… | Cgroup 设置 (v1) | Cgroup 设置 (v2) |
|---|---|---|---|
| CPU Request |  ———–> | `cpu.shares` | `cpu.weight` |
| CPU Limit |  ———–> | `cpu.cfs_quota_us`<br>`cpu.cfs_period_us` | `cpu.max` |

理解这种从 Kubernetes 资源抽象到可强制执行的 Linux 内核 cgroup 参数（或其他可配置项）的转换的怪癖，可以真正提高你预测行为、调试问题和智能地为你的工作负载配置资源设置的能力。

*注意：cgroup API 有两个常用版本。为简单起见，本文的其余部分将仅引用 cgroup v2 设置名称。使用 v1 实现的功能等效。*

## CPU 资源很复杂

信不信由你，控制、分配和保留进程 CPU 时间的底层内核工具的工作方式并不像“请给 nginx 250 毫核，谢谢”那么简单易懂。

我知道，这很令人震惊。🤯

本文没有时间也没有篇幅深入探讨 Linux 完全公平调度器 (CFS) 的血腥细节。我不会告诉你 Kubernetes 将如何为给定Request值在给定节点上设置 `cpu.weight` 的精确值。这些文章已经存在，而且它们很吸引人。如果你感兴趣，我强烈建议你深入研究。这是一个[很好的例子](https://linuxera.org/cpu-memory-management-kubernetes-cgroupsv2/)。

不过，我将尽力构建一个在 Kubernetes 工作负载资源设置决策中很有用的概念模型。考虑到这一目标，最关键的基础知识是：

1. Kubernetes 使用的每个 CPU cgroup 控件都与 Linux 的完全公平调度器 (CFS) 相关。
2. CFS 是一个比例进程调度器。假设我们不干预，可以将 CFS 视为希望为每个可运行进程提供相等的 CPU 时间。
3. 当 Kubernetes 设置 `cpu.weight` （Request）时，这就是对比例尺的干预。如果一个可运行进程的权重是另一个进程的两倍，CFS 将为权重两倍的进程提供两倍的 CPU 时间。
4. 当 Kubernetes 设置 `cpu.max` (Limit)时，…
（Limit），这并不会改变进程在可运行时的比例优先级。它可能会导致进程周期性地进入超时状态——就像一个任性的孩子——在此期间，进程将不会获得任何 CPU 时间。

这有什么意义吗？不是很明白？好的。让我们逐段分析一下。首先，“施加影响”是什么意思，然后“将进程置于超时”是什么意思。

## CPU Request – 施加影响

Linux 的 CFS 可能会默认给每个可运行的进程分配相同数量的 CPU 时间，但这并不是 Kubernetes 想要的。

Kubernetes 的目标是根据用户在容器的 CPU 资源Request中指定的比例，优先为每个容器的进程分配 CPU 时间。

简单来说，在单核节点（1,000m 容量）上。CPU Request为 200m 的容器应优先获得 ⅕（五分之一）的可用 CPU 周期；CPU Request为 250m 的容器应优先获得 ¼（四分之一）的周期；CPU Request为 500m 的容器应优先获得 ½（二分之一）的周期。

如果节点容量发生变化，这些比例也会发生变化。在双核节点（2,000m 容量）上，相同的 500m Request意味着该容器应优先获得节点可用 CPU 周期的 ¼（四分之一）。双核节点上有更多可用的 CPU 周期，因此应优先运行此容器的部分更小。

为了将 CPU Request转换为可由 `cpu.weight` cgroup 控制实现的内容，Kubernetes 将毫核值转换为与容量成比例的权重值。这些值具体是多少？这是一个很好的问题。

由于 `cpu.weight` 值本身是相互成比例的，因此没有神奇的值可以设置为 `cpu.weight` 来保证静态的 CPU 时间量。任何单个进程的比例优先级取决于其相对于其他正在运行进程的权重。

要从像 ⅕、¼ 和 ½ 这样的比例分数中获得整数权重，您可以计算一个公分母，并使用它来获得比例整数 `cpu.weight` 值。

| 整体比例 | 公分母 | 比例整数权重 |
|---|---|---|
| 1/5 | 4/20 | 4 |
| 1/4 | 5/20 | 5 |
| 1/2 | 10/20 | 10 |

这个模型在概念上与 Kubernetes 的做法类似。由于 pod 调度和节点“满载”的实现方式，Kubernetes 确保为容器计算的分数值总和永远不会超过 1，因此 cgroup 的 CPU 优先级永远不会低于其Request与容量的比例。

这是对 Kubernetes 如何处理 CPU Request的一个有效但过于简化的概念理解。我们可以对这个级别的行为进行一个非常有趣的观察。

![](https://cdn.thenewstack.io/media/2024/11/a939e1fe-observation-1024x385.jpg)


## 特性：可突增 Pod

节点上通常会有一些瞬时空闲 CPU 容量，这些容量并没有因为某个特定容器的 CPU Request而被保证分配给它。这种情况发生在以下情况下：

1. 节点尚未“满载”，因此其部分容量尚未保证分配给任何特定容器。
2. 容器已Request CPU 资源，但目前未使用它们。

当这种情况发生时，可突增 pod 如何工作？假设多个 pod 和容器正在争夺 CPU 突增容量。哪些容器将获得额外的 CPU 时间，以及它们将获得多少 CPU 时间？

一个迂腐但正确的工程答案是：这取决于情况，因为我们还没有真正讨论服务质量 (QoS) 类和 cgroup 层次结构 🤓。

Cgroup 层次结构是另一个我无法在这个高级概述中详细阐述的主题，但我将尝试对其进行足够近似的讲解，以至少分享一个关于可突增 pod 和容器行为的有趣观察。

下图说明了 Kubernetes 如何为 QoS 类和 pod 设置 cgroup 层次结构，以及示例 `cpu.weight` 值。值得注意的是 `burstable.slice` 和 `besteffort.slice` QoS 组及其在层次结构中的位置。

![](https://cdn.thenewstack.io/media/2024/11/e14ff171-image13-1024x433.png)

理解此图的要点：

* Cgroup 以层次结构配置。它们像洋葱一样具有层级。
* 在每一层，cgroup 根据其 `cpu.weight` 分配 CPU 时间，与同级节点成比例。
* 分配给某一层 cgroup 的 CPU 时间可以进一步细分给下一层中该 cgroup 的子级。子分配的方式相同：每个子级使用其 `cpu.weight`（与其兄弟节点）竞争分配给父 cgroup 的 CPU 时间的一部分。

因此，在 Kubernetes 如何设置这些组以及根据上图所示的上下文中：

* 保证 QoS 的 pod 彼此竞争，一个可突增的巨型父级和一个尽力而为的微型父级。
* 如果即使只有一个可突增 QoS 容器需要 CPU 时间，它也会获得比保证 QoS 或尽力而为 QoS 的 pod 多得多的可用“额外”周期，这是由于分配给可突增巨型父级的比例权重所致。
- 即使节点上的每个 BestEffort 容器都需要 CPU 时间，它们组合的 `cpu.weight` 与 Guaranteed 和 Burstable QoS 容器竞争时，总量也永远不会超过 BestEffort 微型父级分配的权重 1。

这种实现方式会产生一些细微的行为差异，但最有趣的可能是以下情况：

![](https://cdn.thenewstack.io/media/2024/11/564e24b0-key-observation_-ch.-2.2-1024x567.png)

对于没有最低性能要求或敏感度的 BestEffort 工作负载来说，这种突发优先级行为可能是非常理想的。然而，当工作负载有任何最低要求时，这种不公平的 CPU 突发容量分配可能会出乎意料或造成问题。

可以通过以下两种方式之一避免意外的 CPU 饥饿风险：

1. 确保最低 CPU 分配的最可靠方法是让工作负载Request它。为每个需要的容器设置 CPU Request，并将它们设置为正确的值。（什么是正确的值？[好问题](https://thenewstack.io/stop-setting-cpu-and-memory-requests-in-kubernetes/)。）
2. 另一种可能更复杂的缓解策略可能是尝试使用 CPU Limit来抑制最有可能的恶意行为者或贪婪的 CPU 消耗者的 CPU 使用。

Limit方法一开始可能看起来很诱人，但业界已逐渐达成共识，即不要对通用工作负载模板使用 CPU Limit，而是依赖Request方法。正如我们将在下一节中看到的那样，CPU Limit本身也存在一些缺点和性能陷阱。

## CPU Limit：对进程设置超时

当您为容器定义 Kubernetes CPU Limit时，容器运行时会将其转换为容器 cgroup 上的 `cpu.max` 值，并且容器的进程将受到 CFS 带宽控制机制的约束。

理解 CFS 带宽控制的关键概念：

1. 带宽控制基于时间段。
2. CPU 配额（如果已分配）是根据每个时间段授予的运行时间（微秒）设置的。
3. 一旦 CFS 记账系统确定某个进程已消耗其某个时间段的所有配额，该进程就会受到Limit。受到Limit时，该进程实际上会暂停。
4. 在每个时间段的开始，配额会刷新，并且受Limit的进程会再次变为可运行状态。

`cpu.max` 是通过设置 `MAX PERIOD` 字符串来配置的，其中 `MAX` 是组在每个“PERIOD”（µs）中可以运行的微秒数。

它可以更深入。这个基础是理解 Kubernetes 中的 CPU Limit和Limit的最低要求。如果您想真正深入研究，有很多很棒的文章剖析了其他 CFS 带宽控制，以及与运行时记账系统的工作方式相关的特定边缘情况。

简而言之，以下是促使业界避免Limit并尝试从正确设置的 CPU Request/`cpu.weight` 获得保证的原因。

假设您有一个应用程序需要 120 毫秒的 CPU 时间来处理一个Request。为了简单起见，我们假设配额周期为 100 毫秒（Kubernetes 的默认值），CPU Limit为 400m。根据我们的 100 毫秒配额周期，400m = 4/10 = 2/5 = 每个周期的 0.4，或每个 100 毫秒周期中的 40 毫秒。由于 `cpu.max` 使用微秒，因此在设置的字面值中会有更多零，因此它会在那里变成 40000 100000，但我们可以在讨论中继续使用 40 毫秒和 100 毫秒。


|**Limit演示场景**||
|---|---|
| Kubernetes CPU Limit | 400m |
| cpu.max 的值 | 40000 100000 |
| 每个Request所需的运行时间 | 120ms |

下图显示了即使节点上没有其他进程运行，此应用程序的一个Request的延迟也可能发生的情况。

![](https://cdn.thenewstack.io/media/2024/11/006dc451-image12-1024x367.png)

虽然这可以说是Limit的预期用途，但在单独查看应用程序时，这里存在潜在的错失机会。如果在处理此Request时没有其他进程争用 CPU 时间，则Limit会引入 115 毫秒的可避免延迟。在此期间，CPU 没有用于任何其他用途。

Limit总是会对应用程序施加约束，从而影响延迟。Limit是面向约束的，那么您为什么通常要引入这种孤立的约束？

答案：通常，您不会。

人们通常凭直觉认为Limit与公平性有关，并确保每个工作负载都能获得分配的时间。但正如我们所了解到的，这实际上并非如此。Limit本身并不是运行时间的保证。运行时间分配保证来自 CPU Request，而不是Limit。Limit的唯一作用是防止单个应用程序利用节点上的额外 CPU 时间（如果有的话）。

![](https://cdn.thenewstack.io/media/2024/11/6b4c4d35-key-observation_-ch.-2.3-1024x488.png)

## 旅程继续：深入探讨内存

CPU 和 CFS cgroup 设置完成后，接下来该讨论内存了。内存Request和Limit如何转换为 Linux 进程设置？比例模型是否会以与 CPU 相同的方式应用于内存？当节点上出现内存争用时会发生什么，原因是什么，Request和Limit如何影响结果？

掌握了 Kubernetes 的 cgroups 基础知识后，我们将在第 3 章重置、调整并将注意力转向 Linux 内存资源实现细节。
