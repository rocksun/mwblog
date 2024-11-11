
<!--
title: Kubernetes Request和Limit的真正工作原理
cover: https://cdn.thenewstack.io/media/2024/11/db6c17c5-wizard2.png
-->

Kubernetes 资源管理技术内部运作的向导之旅 — 第 1 章。

> 译自 [How Kubernetes Requests and Limits Really Work](https://thenewstack.io/how-kubernetes-requests-and-limits-really-work/)，作者 Reid Vandewiele。

*“任何足够先进的技术都与魔法无异。”*  **— Arthur C. Clarke**

[Kubernetes](https://thenewstack.io/kubernetes/) 无疑是一个优雅、精致、设计良好的开源企业软件大厦。它广为人知。即便如此，这个强大的平台工具的内部机制仍然笼罩在神秘之中。友好的抽象，例如 CPU 和内存的“[资源Request](https://thenewstack.io/understanding-kubernetes-resource-types/)”，隐藏了大量相互关联的进程——精确且优化的调度算法、将友好抽象巧妙转换为神秘内核特性的方法，以及可能令人惊讶的数学运算量——所有这些共同作用，产生了用户表达意图的实际体现。

在典型的软件开发或 IT 基础架构团队中，大多数团队成员[永远没有理由或需要深入研究 Kubernetes 的细节](https://thenewstack.io/stop-setting-cpu-and-memory-requests-in-kubernetes/)，以真正深入理解他们的 YAML 清单是如何变成运行现实的。

即使只了解一点它的实际工作原理，其他人也可能会将你新获得的知识误认为是魔法。

在 [StormForge](https://stormforge.io/)，我与一个[复杂子系统团队](https://www.atlassian.com/devops/frameworks/team-topologies#:~:text=3.%20Complicated%2Dsubsystem%20team)（巫师？）合作，他们完全专注于 Kubernetes 一个非常具体、经常被误认为是良性的元素：资源管理。但这篇文章不是关于我做什么的；而是关于我学到了什么。

这是由四部分组成的系列文章的第 1 章，它将揭开 Kubernetes Request和Limit实际工作原理的神秘面纱。在整个系列中，我将引导你走上成为 Kubernetes Request和Limit巫师的道路。

当你读到第 4 章的结尾时，你应该具备以下能力：

- 对 Kubernetes 中资源管理的实现方式有一个上下文相关的端到端总结性理解。
- 清楚地了解 Kubernetes 资源抽象的优点和缺点。
- 接触（就像晒黑一样）Request和Limit在 Linux 内核级别的技术实现细节。
- 提高预测和调试由于设置不当的Request或Limit而导致的怪癖和不良结果的能力。
- 一本简洁的高级 Key Observations™ 手册，即使在你没有深入思考 kubelet、kube-scheduler、cgroup 或 OOM Killer 的工作原理时，也能帮助你做出关于Request和Limit的经验管理决策。

让我们开始吧。

## 宏观视角：透视镜中的层次

要真正理解Request和Limit的实际作用，而不是其抽象的细节，列出与这些输入相关的每个子系统会很有帮助。

* **Pod 规范 (kube-api)**：用户的原始资源Request和Limit值保存在 pod 规范中。
* **节点状态 (kubelet)**：Kubelet 将静态容量信息作为每个节点状态的一部分进行报告。
* **Pod 调度 (kube-scheduler)**：调度程序在决定将待处理 pod 调度到哪些节点上运行时，会考虑节点容量信息、正在运行的 pod Request和待处理的 pod Request。
* **CPU 的容器配置（容器运行时）**：Kubelet 和容器运行时（例如，containerd）将根据作为 CPU Request和Limit给出的值设置 cgroup 参数。
* **内存的容器配置（容器运行时）**：与 CPU 类似，kubelet 和容器运行时将为每个容器和进程设置 cgroup 和其他参数，这次是基于作为内存Request和Limit给出的值。
* **节点压力和驱逐 (kubelet)**：Kubelet 定期评估节点的整体资源状况。如果它注意到过多的资源压力，它可能会采取行动（例如，驱逐一个或多个 pod）来尝试缓解问题。

我们将在旅程中的某个地方深入研究这些层。

## Pod 规范

这一层很小，但它仍然是一个层，因为它很重要。

每个 pod 都需要资源（尽管 BestEffort [QoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) pod 除外）。规范只是[期望状态](https://github.com/open-gitops/documents/blob/v1.0.0/GLOSSARY.md#desired-state)，因此除了记录期望状态之外，这一层实际上什么也不会发生。但是，它不应该被轻视。容器所需的资源以及应该设置的Limit都从这里开始。

pod 规范有很多内容，但现在我们只关心其中的一部分。一个有用的咒语可以用来详细检查资源设置（对于一个相当任意的单个 pod 的选择），它可以由 `kubectl` 和 `jq` 组成，如下所示：

## 节点状态

Pod 需要资源。节点拥有资源。Pod 规约记录了 Pod 需要的资源，而节点状态记录了节点拥有的资源。这使得节点状态成为 Pod/节点资源匹配系统的对应输入。在任何 Pod 运行操作发生之前，Pod 规约和节点状态都需要被了解和定义。

随着 Pod 在节点上不断地被调度和取消调度，您可能会认为节点报告的资源会不断变化。但事实并非如此。每个节点报告的只是一个简单的、静态的、可分配的容量。这个数字永远不会改变，无论节点上运行了多少个 Pod。它不是已分配的资源，而只是节点理论上可以分配的资源。

在接下来的几个例子中，我们将展示一个示例节点的状态信息。为了保持一致性，我们将在此处按名称选择一个节点并记住它。

```bash
% export NODE=$(kubectl get node -o name | cut -d / -f 2 | head -1)
```

现在考虑以下命令。此调用可用于显示节点状态的示例，用于可分配的 CPU 和内存。就像 Pod 规约一样，节点状态中有很多内容，但我们希望去除所有无关信息，目前只关注资源信息。

```bash
% kubectl get node "$NODE" -o json \
  | jq '.status | {capacity, allocatable}
        | [ to_entries[] | .value |= {cpu, memory} ]
        | from_entries'

{
  "capacity": {
    "cpu": "2",
    "memory": "3859240Ki"
  },
  "allocatable": {
    "cpu": "1930m",
    "memory": "3169064Ki"
  }
}
```

容量是节点资源的原始度量；可分配容量是 Kubernetes 认为可用于运行 Pod 的部分。

## Pod 调度

在 Kubernetes API 中创建 Pod 后，必须将其调度到节点上运行。它需要匹配。我们探讨的前两层——Pod 规约和节点状态——在调度过程中结合在一起。

kube-scheduler 的工作是选择一个特定节点来运行 Pod，其决策的很大一部分将基于任何给定 Pod Request的资源在候选节点上是否可用。

在调度阶段，资源抽象仍然完全完整，但只有一半重要：`requests`。

![](https://cdn.thenewstack.io/media/2024/11/ab1486a6-image11s-1024x428.jpg)

`limits` 在稍后才有意义，但在这里没有意义。在决定将新 Pod 调度到哪个节点运行时，`limits` 会被完全忽略。

为了确定一个节点是否有可用于新 Pod 的资源，kube-scheduler 只需将节点上已运行的所有 Pod 的 `requests` 相加，然后从节点的可分配容量中减去该数字。如果 Pod 的 `requests` 较小，则节点上有空间运行它。如果 Pod 的 `requests` 较高，则没有空间。

请务必注意，物理资源利用率与此决策无关。理论上，节点的 CPU 可能会熔化成渣，并且分配了它的每个字节内存，但如果其 Pod 的 `requests` 加起来不等于它报告的可分配数量，kube-scheduler 将很乐意为其提供更多 Pod 来运行。

相反，如果节点的 CPU 实际上处于空闲状态且内存使用量很小，调度程序仍可能认为它已满。资源不必实际使用——只需Request——就可以使节点在此目的上逻辑上已满。

## 节点“满载”

确定节点的满载程度不会直接报告，并且每当您或其他东西需要它时都必须重新计算。幸运的是，如果您想知道它，`kubectl` 将此计算内置到其 `describe` 节点输出中。

对于实际的向导，请考虑以下 `kubectl` 和 `awk` 的神秘合成。

```bash
% kubectl describe node "$NODE" \
  | awk '/Name:/{print "\n"$1, $2} /Allocated/{p=1} /storage/{p=0} p'

Name: ip-10-16-200-217.ec2.internal
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests      Limits
  --------           --------      ------
  cpu                1351m (70%)   3840m (198%)
  memory             1889Mi (61%)  12068Mi (389%)
```


分配的 1351m CPU 数量将是此节点上运行的 Pod 中所有容器的 CPU `requests` 的总和。如果您想自己进行粗略的计算，可以使用 CLI 工具进行近似计算。首先获取调度到该节点上的所有未终止的 Pod：

```bash
% kubectl get pods --all-namespaces --field-selector \
  status.phase!=Terminated,status.phase!=Succeeded,status.phase!=Failed,spec.nodeName="$NODE"

NAMESPACE          NAME                        READY   STATUS    RESTARTS   AGE
amazon-guardduty   aws-guardduty-agent-gnfzz   1/1     Running   0          5h15m
kube-system        aws-node-5lcqm              2/2     Running   0          5h15m
kube-system        ebs-csi-node-t8nqh          3/3     Running   0          5h15m
...
```

然后，将 Pod 列表输出为 JSON，并添加一个 `jq` 脚本来收集所有 `requests`（例如，CPU `requests`）并对其求和。

```bash
% kubectl get pods --all-namespaces -o json --field-selector \
  status.phase!=Terminated,status.phase!=Succeeded,status.phase!=Failed,spec.nodeName="$NODE" \
  | jq '[ .items[].spec.containers[].resources.requests.cpu // "0"
          | if endswith("m")
            then (rtrimstr("m") | tonumber / 1000)
            else (tonumber) end
        ] | add * 1000 | round | "\(.)m"'

"1351m"
```

该数字应与 `kubectl describe` 显示的数字匹配，这表明 `kubectl` 和 kube-scheduler 如何获得这些数字。

在我们更多地转向理论之前，文章的实际部分中还有一个 `kubectl` + `jq` 咒语。以下命令旨在演示节点上还有多少 CPU 可用，因此 Pod 可以（理论上）发出多大的 CPU `request`，并且仍然可以调度在此处运行。

```bash
% { kubectl get node "$NODE" -o json; \
    kubectl get pods --all-namespaces -o json --field-selector \
      status.phase!=Terminated,status.phase!=Succeeded,status.phase!=Failed,spec.nodeName="$NODE"; } \
  | jq -s '( .[0].status.allocatable.cpu
             | if endswith("m")
               then (rtrimstr("m") | tonumber / 1000)
               else (tonumber) end
           ) as $allocatable
           | ( [ .[1].items[].spec.containers[].resources.requests.cpu // "0"
                 | if endswith("m")
                   then (rtrimstr("m") | tonumber / 1000)
                   else (tonumber) end
               ] | add
             ) as $allocated
           | ($allocatable - $allocated) * 1000 | round
           | "\(.)m is available"'

"579m is available"
```

最终，这些命令所做的就是演示这种简单的关系：

![](https://cdn.thenewstack.io/media/2024/11/87eeac88-image8-1024x95.png)

**关键观察**

节点根据资源 `requests` 变为“满载”并且无法接受其他工作负载。节点上实际使用的 CPU 或内存与此节点是否可以处理更多 Pod 的决定无关。

如果您希望节点“满载”意味着其实际的 CPU 和内存资源正在被有效地使用，则需要确保 CPU 和内存 `requests` 与实际使用情况相匹配。

`limits` 与节点是否“满载”无关，并且在此阶段完全被忽略。

## 旅程继续：深入探讨 CPU

将 pod 分配给节点后（我确信这是天作之合），该节点需要将 pod 的每个容器作为 Linux 进程运行。不过，Linux 对 Kubernetes 资源抽象一无所知。资源 Request 和 Limit 如何在 Linux 操作系统级别发挥作用？该实现对于基于 Pod 规范和节点状态的预期、预测或保证结果意味着什么？

随着 Kubernetes 调度的出现，我们将在第 2 章中深入研究 Linux CPU 资源实现细节。