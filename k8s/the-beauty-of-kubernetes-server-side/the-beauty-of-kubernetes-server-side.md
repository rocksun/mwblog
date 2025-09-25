
<!--
title: Kubernetes SSA：服务器端应用的优雅之道
cover: https://substackcdn.com/image/fetch/$s_!PY0G!,w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9afa0205-f325-403c-afeb-c72ef5c3bf79_1427x542.png
summary: Kubernetes服务端应用(SSA)将资源更新移至API服务器。它通过字段管理解决冲突，实现乐观并发，提升CI/CD流水线和Operator的可靠性，推荐多控制器场景使用。
-->

Kubernetes服务端应用(SSA)将资源更新移至API服务器。它通过字段管理解决冲突，实现乐观并发，提升CI/CD流水线和Operator的可靠性，推荐多控制器场景使用。

> 译自：[The Beauty of Kubernetes Server-Side Apply (SSA)](https://clustersandcoffee.substack.com/p/the-beauty-of-kubernetes-server-side)
> 
> 作者：Annis Souames

任何使用 Kubernetes 的人，可能都执行过 `kubectl apply` 命令来创建集群上的资源或更新它们，或者在更高级的情况下，在构建 operator 时尝试以编程方式创建/更新资源。“apply”操作非常灵活，并在后台抽象了大量内容。例如，`kubectl apply` 命令有两种模式：客户端模式，它多年来一直是 `kubectl` 中的默认模式；以及一种（相对）较新的模式：服务端应用（Server-Side Apply），简称 SSA，它在 2021 年夏天 Kubernetes v1.22 发布时[正式发布](https://kubernetes.io/blog/2021/08/04/kubernetes-1-22-release-announcement/)。

我发现 SSA 是 Kubernetes 中一个经过深思熟虑的精美功能，我们将在本文中深入探讨。我们将讨论它是什么，它是如何工作的，以及它如何为 DevOps 人员和 K8s operator 开发者解决一些重要难题，同时强调一些有趣的理念，例如乐观并发控制。但让我们从基础开始，简要讨论 `kubectl apply` 的默认模式：客户端应用 (CSA)。

当您在现有资源上运行 `kubectl apply` 时，您的机器上默认会发生以下情况（例如运行 `kubectl apply -f …`）：

1. 从 API 服务器获取资源的当前实时版本。
2. 比较三种不同的配置：

   * 您提供的本地文件，这通常被称为*期望状态*，因为我们要求集群移动到新状态。
   * 集群中运行的实时版本，被称为*当前状态*。
   * 存储在实时资源上的 `last-applied-configuration` 注解，它是上次运行 `apply` 时 YAML 的快照，以 JSON 字符串形式存储。
3. 根据这三个来源的比较，使用**三方合并**策略计算一个差异补丁。
4. 将计算出的补丁发送到 Kubernetes API 服务器，然后 API 服务器更新资源，如果资源不存在则创建它。

下图总结了这个三方合并过程：

[![](https://substackcdn.com/image/fetch/$s_!PY0G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9afa0205-f325-403c-afeb-c72ef5c3bf79_1427x542.png)](https://substackcdn.com/image/fetch/$s_!PY0G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9afa0205-f325-403c-afeb-c72ef5c3bf79_1427x542.png)

这是 `kubectl` 多年来默认使用的方法。在资源可以由不同参与者（例如不同用户或控制器）更新的环境中，可能会出现一些问题。我们将在后面简要讨论这些问题，以及服务端应用如何帮助避免这些问题。但是，我们首先介绍 apply 命令的第二种模式：服务端应用（Server-Side Apply），简称 SSA。

服务端应用，自 v1.22 起正式发布，其工作方式不同：不再由 `kubectl` 拉取资源的三个版本并进行比较，而是由一个中心参与者为我们完成所有这些工作：控制平面中的 Kubernetes API 服务器将比较我们指定的新期望版本的资源和集群中运行的当前版本（如果存在）。它还会计算一个*差异*，并在需要时修补资源。

比较和差异计算现在已从我们机器上运行的本地 kubectl 程序转移到集群自身的控制平面，这就是为什么我们称之为服务端应用。下面是这种方法的视觉表示：

[![](https://substackcdn.com/image/fetch/$s_!7yrz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd813a52-32dd-4cf2-a252-6a709af8c39d_1003x480.png)](https://substackcdn.com/image/fetch/$s_!7yrz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd813a52-32dd-4cf2-a252-6a709af8c39d_1003x480.png)

如您所见，`kubectl` 现在充当一个直接的信使。它将您的 YAML 发送到 API 服务器，然后控制平面为我们处理其余部分。要使用此模式，您只需在 `apply` 命令中添加 `--server-side` 标志：

`kubectl apply --server-side -f my-deployment.yaml`

资源可以通过多种方式使用 SSA 进行更新，而不仅仅是使用 `kubectl apply —serverside` 命令。如果您构建 operator 并需要以编程方式更新资源（例如，使用 Kubernetes 客户端 SDK、Kubebuilder 或 Operator Framework），SSA 默认在 k8s API 级别支持 `client.Apply` 方法，您可以通过 PATCH 请求发送该方法。这需要提供一个 `fieldManager` 字符串键来指定哪个参与者负责提供的字段。我们很快将发现什么是托管字段以及 SSA 如何利用它们来处理冲突。

太好了！现在我们了解了 SSA 的工作原理和使用方法，接下来让我们讨论它解决的一些难题。

---

我认为服务端应用在某些方面比客户端应用更出色，主要体现在以下几个方面：

在 Kubernetes Apply 的默认客户端工作流中，如果同一资源之前被另一个参与者（例如控制器、管理员或 CI/CD 流水线）修改过，更新资源可能会导致冲突。这些冲突的发生是因为您运行 `kubectl apply -f …` 时资源拥有的 `resourceVersion` 与刚刚由不同参与者更新的 `resourceVersion` 不同。

SSA 通过在更新期间提供“字段版本控制”机制来简化冲突管理：我们可以指定字段管理器的名称，即负责操作此字段的参与者的 ID，Kubernetes 然后将检查该指定的 ID 是否对应于资源中正确的 `managedFields.manager` 属性。[SSA 文档](https://kubernetes.io/docs/reference/using-api/server-side-apply/#field-management)很好地解释了这一点：

> Server-Side Apply **补丁**请求要求客户端提供其身份作为[字段管理器](https://kubernetes.io/docs/reference/using-api/server-side-apply/#managers)。当使用 Server-Side Apply 时，尝试更改由不同管理器控制的字段将导致请求被拒绝，除非客户端强制覆盖。有关覆盖的详细信息，请参阅[冲突](https://kubernetes.io/docs/reference/using-api/server-side-apply/#conflicts)。
>
> 当两个或更多应用者将一个字段设置为相同的值时，它们共享该字段的所有权。任何后续尝试更改共享字段的值，无论是由哪个应用者进行的，都会导致冲突。共享字段所有者可以通过发送一个不包含该字段的 Server-Side Apply **补丁**请求来放弃对该字段的所有权。

如文档所述，您还可以强制其他参与者覆盖某些字段。

这种行为有一个很好的结果：*乐观并发控制*，我们将在接下来讨论。

采用 SSA 有助于避免 Kubernetes 并发、分布式特性带来的一些问题。我们通常有不同的控制器在集群中并发并行运行。它们可能操作同一资源，导致我们之前讨论的冲突。

为了更好地理解这个问题，想象一下为一种新型资源（CRD）构建控制器。要更新资源，您的控制器执行以下标准“获取-修改-更新”方法：

1. 从集群中获取资源。
2. 更新一些字段。
3. 推送更新，通常通过 `client.Update()` 调用或 PATCH 请求。

然而，在资源可以被其他参与者修改的环境中，这种方法是不安全的。当我们本地获取资源并运行一些逻辑来更新所需字段时，另一个控制器或管理员可能也会在我们之前更新它。这使我们本地拥有资源的过时版本。当我们发送更新请求时，它将导致错误，因为实时资源的版本比我们持有的版本新。

如果您曾经处理过并发编程，这与数据竞争非常相似，其中一个线程更改了一些数据，而另一个线程正在读取它。

数据竞争通常通过同步技术解决，例如使用锁来协调不同的线程。然而，锁定通常是一个开销很大的操作。在 Kubernetes 的上下文中，我们不能真正锁定整个资源直到更新执行完毕。这种锁定和解锁资源的方法在分布式系统中通常被称为*悲观并发控制*。

Kubernetes 中的服务端应用为这个问题提供了一种更好的方法，通常称为*乐观并发控制*。由于服务器现在是单一事实来源，并且所有计算都转移到 API 服务器，它通过避免锁并使用托管字段以及请求中提供的 fieldManager 来控制并发更新，从而实现乐观并发控制。

乐观并发在资源竞争低的分布式系统中效果最佳——也就是说，在这些系统中，竞争性访问共享资源不频繁，因此发生冲突的概率低（但不是零）。在资源竞争高的环境（即，不同参与者频繁访问共享资源）中，使用我们之前讨论的悲观并发会更好，但它会带来性能和复杂性的权衡。

本节我们将讨论 SSA 优势的最后一部分是 CI/CD 流水线，它们经常与部署在集群上的资源进行交互。想象一个设置，其中自动化流水线负责部署应用程序的新版本。它的唯一工作是更新 Deployment 清单中的容器 `image` 字段，以推出最新标签。为简单起见，假设集群中还运行着一个水平 Pod 自动伸缩器（HPA），以便在流量高峰时将您的 Deployment 扩展到多个副本。

使用旧的客户端 `apply`，这个过程出奇地脆弱。流水线的静态 YAML 文件将指定默认的 `replicas` 计数为 2 个 Pod (`replicas: 2`)。现在，如果 HPA 将您的应用程序扩展到 10 个副本以处理流量高峰，下次您的 CI/CD 流水线运行以部署新镜像时，它将使用其本地文件作为期望状态。它将看到集群中的 `replicas` 计数为 10，但其 `last-applied-configuration` 和本地文件都显示为 2。它将在善意的驱动下，尝试在流量高峰期将您的应用程序缩减回 2 个副本，这可能由于两个并发但独立的系统（CI/CD 流水线和 HPA）之间的竞态条件而导致服务中断。

服务端应用通过引入我们之前讨论过的相同字段所有权概念，很好地解决了这个问题。当 CI/CD 流水线使用 `--server-side` 应用其更改时，它**只**声明 `spec.template.spec.containers[0].image` 字段的所有权。同时，水平 Pod 自动伸缩器被注册为 `spec.replicas` 字段的所有者。现在，这两个系统可以**并发地**操作同一资源而**不发生冲突**。流水线可以随意更新镜像标签，HPA 可以自由地上下扩展副本数量。Kubernetes API 服务器理解这些更改由不同参与者管理并安全地合并它们。

如果另一个管理员或不同的流水线*确实*尝试更改镜像标签，SSA 将立即标记一个**冲突**。apply 命令将失败，而不是静默覆盖更改。通过将这些冲突传播回您的 CI/CD 日志，您为 DevOps 工程师创建了一个清晰即时的信号，以调查并解决问题，从而防止意外的生产错误。

到目前为止，我们已经讨论了使用 Server-Side Apply (SSA) 在 Kubernetes 中的几个重要优点。我发现这个功能是一个很好的补充，它优雅地解决了多个问题，特别是对于大型集群。

在我看来，如果您是 operator 或控制器开发者，您绝对应该在资源更新逻辑中使用 SSA。它提供的强大冲突管理非常值得，使您的声明式更新更安全、更可靠。您的 operator 可能会在拥有多个其他控制器的大型集群中使用，如果这是您的工作，最好提供一个高质量、可靠的 operator。

其次，如果您是集群管理员或应用程序开发者，我也建议将 SSA 与 `kubectl apply` 命令一起使用。如果您的集群中有不同的控制器可能更新同一资源，情况尤其如此，因为 SSA 有助于管理冲突并避免我们讨论过的竞态条件。然而，对于没有许多控制器竞争相同资源的小型集群，默认的客户端应用可能仍然足够。

如果您想从**此功能的贡献者之一**那里获得关于为什么要使用 SSA 的另一种观点，我强烈推荐阅读：Google 的 Daniel Smith 撰写的《[Server-side apply is great and you should use it](https://kubernetes.io/blog/2022/10/20/advanced-server-side-apply/)》。