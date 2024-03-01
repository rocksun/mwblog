<!--
title: Kubernetes Pod Disruption Budget实用指南
cover: https://teckbootcamps.com/wp-content/uploads/2024/01/Copy-of-kube-1.png
-->

管理**Kubernetes**集群在保持一致的可用性和对故障的韧性方面存在困难。虽然使用副本可以确保存在多个应用程序实例，但并不能保证应用程序运行时的不间断。

> 译自 [Kubernetes Pod Disruption Budget: The Practical Guide 2024](https://teckbootcamps.com/pod-disruption-budget-the-practical-guide/)，作者 Mohamed BEN HASSINE 。

这就是Pod Disruption Budget（Pod中断预算，PDB）变得至关重要的地方。PDB是Kubernetes内的一个功能，通过对应用程序可以处理的中断数量制定规定，有助于维持应用程序的稳定性。

本文深入探讨了PDB的具体内容，包括其定义、如何创建、最佳使用案例以及其重要性的基本原因。

## 什么是“Pod Disruption（Pod中断）”？

Pod中断指的是当Pod被有意地从节点中删除或驱逐时发生的情况。这可能出于各种原因，包括：

- 节点维护（如操作系统升级或硬件升级）。
- Kubernetes集群升级。
- 自动缩放。
- 由于节点资源约束而重新调度Pod。

在Kubernetes中，有两种类型的中断：

- 自愿中断：这些是可以控制和计划的中断。预计它们将遵守您定义的Pod Disruption Budget（PDB）。
- 非自愿中断：这些是无法预测或控制的意外中断，例如节点上的硬件故障或内核崩溃。重要的是要注意，这些类型的中断不会遵守PDB设置的约束。

## 什么是“Pod Disruption Budget”？

现在我们已经了解了Pod中断是什么，让我们深入探讨一下旨在帮助我们管理它的工具。简单来说，Pod Disruption Budget（PDB）使您能够控制应在任何给定时刻可访问的副本数。在为应用程序配置PDB时，您可以指定以下内容之一：

- Pod必须始终可用的最小副本数（称为最小可用）。
- 可用的副本数的最大数量（称为最大不可用）。

在实际操作中，这意味着，例如，如果您的应用程序有5个副本，并且您设置了一个PDB，要求最少可用的副本数为2个，则只要有两个副本正常运行，PDB就不会影响您的应用程序。

但是，如果副本数少于2个，某些Kubernetes操作将被暂停。例如，如果由于缩容过程导致副本少于2个，那么您的集群的缩容将被暂停。

## 使用“Pod Disruption Budget”的要求？

为了使用Pod Disruption Budget（PDB），要求很简单：

- Kubernetes版本：确保您的Kubernetes版本为1.21或更高。
- Pod标记：要创建和应用PDB，您需要指定应该生效的Pods。因此，相应地标记您的Pods，以便简单地识别应该应用PDB的Pods。此标记有助于精确应用Pod Disruption Budget。

## 如何创建Pod Disruption Budget？

我们将讨论创建Pod Disruption Budget（PDB）对象的各种方法。

### Kubectl Create

要快速将Pod Disruption Budget（PDB）应用于特定工作负载，请执行以下kubectl命令：

```bash
kubectl create poddisruptionbudget my-app-pdb --min-available=1 \
--selector=app=my-super-app
```

让我们分解一下：

- **poddisruptionbudget**：这是我们要创建的Kubernetes API资源类型，代表“Pod Disruption Budget”资源。或者，您可以使用简称“pdb”。
- **my-app-pdb**：这是专门为应用程序“super-critical-app”创建的PDB资源的名称。
- **--min-available**=1：此标志确保我们的应用程序始终可用的最小副本数为1个，设置中断的阈值。
- **--selector**=app=my-super-app：此标志用于指定应该应用PDB的Pods。在本例中，它指定了PDB适用于具有标签“app=super-critical-app”的Pods。

### YAML定义

另一种创建Pod Disruption Budget（PDB）对象的方法是使用YAML文件定义其配置。

让我们看一个在前一节中讨论的相同PDB的示例，特别是利用minAvailable参数。

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-app-pdb
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: my-super-app
```

执行kubectl apply -f <YAML_FILE>将生成相同的Pod Disruption Budget（PDB）。现在，让我们探讨使用maxUnavailable参数的示例。

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-app-pdb
spec:
  maxUnavailable: 0
  selector:
    matchLabels:
      app: my-super-app
```

### Helm Chart

以下是如何在Helm Chart中定义PDB的示例：

```yaml
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
 name: "{{ .Release.Name }}-pdb"
spec:
 minAvailable: 2
 selector:
 matchLabels:
 app: "{{ .Release.Name }}"
```

在此示例中，Pod Disruption Budget（PDB）被配置为在自愿中断期间保持两个标记为app: {{ .Release.Name }}的Pods的最小数量。

当执行可能使应用程序不可用的操作时，Kubernetes努力遵守PDB准则。例如，它将尝试以避免违反PDB的方式将Pods分配给节点。

重要的是要认识到，PDB不能确保可用Pod的数量或百分比保持恒定。在发生意外中断或集群资源不足以在节点故障后调度新的Pod时，可用Pod的计数可能会低于指定的阈值。

将PDB集成到您的Helm Chart中时，确认选择器字段中的标签与您打算保护的Pods的标签对齐至关重要。

## 验证PDB已创建并应用

让我们首先列出我们的Pod Disruption Budget（PDB）对象。我们期望看到一个，特别是在前面的部分中创建的那一个，名称为“app-pdb”。

```bash
$ kubectl get pdb

NAME        MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
my-app-pdb         1              0                      0     
```

目前的配置规定最少1个副本。鉴于我们使用默认设置1个副本，因此最大可允许的不可用性限制为1（任何更多，应用程序将停止运行）。


## 如何测试Kubernetes PDB？

要真正掌握Pod Disruption Budgets（PDB）的有效性，最具见解的方法是在各种场景下积极测试它，其中其作用是保护应用程序不会少于指定数量的副本。

## Kubernetes节点排空

我们将首先执行节点排空，不仅仅是任何节点，而是特别是我们的应用程序副本当前正在运行的节点。节点排空涉及在将节点标记为“cordoned”后重新定位所有Pod，表示该节点上不能再调度新的Pod。

假设我们执行了命令

```bash
kubectl get po -o wide | grep -i my-super-app 
```

我们确定节点名称为“teckbootcamps-node”，让我们继续排空该节点。

```bash
$ kubectl drain teckbootcamps-node --ignore-daemonsets

node/teckbootcamps-node cordoned
```

这是一个积极的开始。最初，我们观察到我们的节点已被封闭，表示不会将新的工作负载分配给它。让我们继续检查后续输出以获取更多见解。

```
evicting pod default/last-app
evicting pod default/my-super-app
evicting pod default/funny-app
```

有趣。值得注意的是，节点上的所有Pod都被安排进行驱逐。但是，重要的是不要误以为这表明了PDB无法正常工作。

这只是对其预期操作的通知。让我们继续查看接下来发生的事情。

```
evicting pod default/my-super-app
error when evicting pods/"my-super-app" -n "default" (will retry after 5s): Cannot evict pod as it would violate the pod's disruption budget.
evicting pod default/jkog-cc8457d4-pkhzs
error when evicting pods/"my-super-app" -n "default" (will retry after 5s): Cannot evict pod as it would violate the pod's disruption budget.
```

PDB来拯救！ Kubernetes在驱逐目标Pod（我们最近创建的PDB中指定的Pod）时遇到了障碍。

它评估配置的PDB并推断出，疏散此Pod将导致可用的Pod数量从1减少到0，低于minAvailable=1定义的阈值。

## Kubernetes节点池升级

让我们在不同的工作流程中测试PDB-具体来说，在Google云平台（GCP）上的GKE集群中升级节点池，并且节点池只有一个节点和最小可用设置为1。通常，在这样的过程中，将节点标记为封闭以防止在其上调度新的工作负载。

随后，应用排空操作以将工作负载转移到具有更新的Kubernetes版本的新节点。在理论上，PDB应该介入，因为此场景意味着将Pod从一个节点驱逐到另一个节点时副本数减少为0。让我们在这种情况下检查其性能。

使用gcloud CLI

```bash
gcloud container clusters upgrade CLUSTER_NAME --node-pool=NODE_POOL_NAME --cluster-version VERSION
```

结果如何？没有升级！好吧，不完全是。最初，您的工作负载不会转移到新节点，实际上仍然作为旧节点上的唯一占用者（假设其他工作负载没有PDB）。但是，请注意您从GCP收到的这条有趣的消息。

## Pod Disruption Budget（PDB）是确保应用程序持续运行的最佳解决方案吗？

简而言之，不是。Pod Disruption Budget（PDB）并非是确保应用程序不间断运行的一劳永逸的解决方案。从技术上讲，它并不是绝对可靠的，有时需要额外的方法来保证应用程序的连续和正确运行。让我们探讨一些例子。

考虑一个简单的情景：您有一个名为“my-cool-app”的Pod，有一个副本，并且应用了PDB，其中minAvailable=1，表示应始终有一个运行中的副本，不允许对Pod进行中断。

现在，如果您运行kubectl delete po my-cool-app，您认为会发生什么？如果您的答案是“它会被删除”，那么您是正确的。PDB不会阻止Pod被删除，因为这种直接删除被视为管理员发起的管理操作，而不是由Kubernetes服务自己管理。因此，在管理员直接删除Pod时，PDB不会产生影响。

## Kubernetes PDB的缺陷

旨在确保应用程序持续运行的PDB可能会阻碍某些操作。例如，如果您尝试排空一个节点，PDB可能会阻止该操作，导致节点上的应用程序无法被驱逐，因为受到了PDB的限制。尽管PDB的目的是保持应用程序的不间断运行，但如果计划不当，它可能会干扰现有的流程。

虽然PDB并不完全阻止某些操作，但它可能会引入延迟。考虑一下在GCP的GKE节点池中升级Kubernetes版本的示例。最初，PDB可能会延迟节点排空，但最终，该操作会进行，尽管延迟了一个小时。因此，虽然PDB不会阻止应用程序的停机，但它确实延迟了节点池升级过程。

PDB的影响还延伸到集群的缩减能力。如果不同的应用程序在两个节点上运行，并且Kubernetes可以将它们合并到单个节点以进行缩减，PDB将阻止此操作以避免中断。然而，这种保护是以维护应用程序可靠性而产生更高的集群费用为代价的。

## 结论

总之，我们探讨了“Pod中断”的概念及其对应的“Pod中断预算”（PDB）。我们讨论了实施PDB的先决条件，并深入探讨了创建它的各种方法，包括使用kubectl create、YAML定义和Helm Chart。还介绍了验证过程，以确保成功创建和应用PDB。

然后，我们继续在实际场景中测试PDB，例如Kubernetes节点排空和节点池升级。尽管PDB是维护应用程序可用性的宝贵工具，但重要的是要认识到，它可能不是连续运行的最终解决方案，并且我们强调了在Kubernetes环境中使用时可能遇到的一些问题。