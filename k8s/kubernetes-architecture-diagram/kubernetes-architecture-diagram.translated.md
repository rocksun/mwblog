**你知道 Kubernetes 架构图是什么吗？** **kubectl、微服务、无服务器计算、Kubernetes 监控、AWS、容器、Fluentd、pod、节点或扩展**呢？ 这些是你可能听说过的基本计算术语，但你是否完全掌握了它们是如何协同工作的？
即使你熟悉这些概念，你是否真正理解它们的实际应用？ 如果你理解，请继续阅读，你将加深你的知识。 如果不理解，请坐下来，让我来为你分解。

我们将要**从头开始解构 Kubernetes**，探索 **Kubernetes 架构图、真实世界的例子、核心组件和实际用例**。 到最后，你不仅会理解 Kubernetes 是什么，还会理解如何有效地使用它。 准备好深入了解前所未有的**可扩展性、编排和容器化部署**。

[什么是 Kubernetes 集群架构？](#h-what-is-kubernetes-cluster-architecture)
[Kubernetes 架构图有哪些好处？](#h-what-are-the-benefits-of-kubernetes-architecture-diagram)
[使用 Kubernetes 架构图是否需要容器？](#h-do-you-need-containers-to-work-with-kubernetes-architecture-diagram)
[Kubernetes 架构图如何工作](#h-how-does-kubernetes-architecture-diagram-works)
[Kubernetes 控制平面和节点架构详解](#h-kubernetes-control-plane-and-node-architecture-explained)
[Kubernetes 概念、工具和部署](#h-kubernetes-concepts-tools-and-deployment) - Kubernetes 架构图
[常见问题解答](#h-kubernetes-architecture-diagram-faq)

## 什么是 Kubernetes 集群架构？

**Kubernetes 集群架构是指包含主控制平面和一个或多个工作节点系统的结构**。 或者，如果你使用 Kubernetes 自我管理的服务器，如 kubeadmn、kops 等，它甚至可能更多。

这两种实例都可以在云、虚拟机甚至物理设备中。 然而，当涉及到像 Azure AKS、GCP GKE 和 AWS EKS 这样的托管 Kubernetes 架构图环境时，控制平面由指定的云提供商管理。

当大型企业希望执行关键任务时，他们会使用 Kubernetes，这是一个用于容器管理的开源系统，也是满足他们需求的完美解决方案。

### 为什么要使用 Kubernetes？

- 在需要时扩展应用程序
- 管理容器集群
- 优化容器下方底层硬件的使用
- 启用应用程序组件，以便它们可以在需要时重新启动并在系统中移动
- 现有容器化应用程序中的变更管理

### Kubernetes 2025 的新功能是什么？

**AI/ML 编排**：Kubernetes 现在原生支持用于机器学习工作流的 GPU/TPU 调度，**Kubeflow 2.0**等工具简化了 MLOps 管道。
**边缘原生 Kubernetes**：**K3s**和**MicroK8s**等轻量级发行版主导了边缘部署，从而可以在 IoT 和 5G 网络中进行实时处理。
**无服务器演进**：**Knative**和**OpenFunction**现在是自动扩展到零的标准，从而降低了事件驱动型应用程序的成本。
**可持续性功能**：Kubernetes 引入了节能调度，优先考虑由可再生能源供电的节点。

![kubernetes 可以做什么？](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
![kubernetes 可以做什么？](https://images.clickittech.com/2020/wp-content/uploads/2022/04/13202311/Diagram-52-1024x802.jpg)

除了其基本框架功能外，Kubernetes 在其他方面也很有用。 它允许用户从各种选项中进行选择，例如语言、日志记录和监控工具、应用程序框架类型，以及用户可能需要的许多其他有价值的工具。

Kubernetes 本身不是[平台即服务](https://cloud.google.com/learn/what-is-paas) (PaaS)，但你可以将其用作完整的 PaaS 起始基础。

自从 Kubernetes 出现在市场上以来，它已成为一种流行的工具，也是当今最成功的开源平台之一。

## Kubernetes 架构图有哪些好处？

![k8s 优势](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
![k8s 优势](https://images.clickittech.com/2020/wp-content/uploads/2022/04/13202323/Diagram-54-1024x803.jpg)

**我们需要 Kubernetes 仅仅是因为它允许我们有效地将工作负载分配到所有可用资源中，而且它还允许我们优化基础设施成本。**

### 可扩展性

在 Kubernetes 中部署的所有应用程序都称为微服务，它们由许多容器组成，这些容器进一步分组为 pod 系列。 从这里，每个容器在逻辑上都设计为执行一项单一任务。

阅读有关[微服务优势](https://www.clickittech.com/devops/microservices-benefits/)的完整博客。

### 高可用性
几乎所有的容器编排引擎都可以提供应用程序的可用性。然而，Kubernetes 的高可用性架构旨在实现基础设施和应用程序的可用性。它还通过利用复制控制器、Pet Set 和副本集来确保应用程序前端的高可用性。

Kubernetes（高可用性）还支持基础设施的可用性，包括各种存储后端。这些包括块存储设备，如 [Amazon Elastic Block Store](https://aws.amazon.com/es/ebs/) (EBS)、Google Compute Engine 永久磁盘等。

### 可移植性

Kubernetes 的设计在操作系统、容器运行时、云平台、PaaS 和处理器架构方面提供了多种选择。此外，您可以在不同的 Linux 发行版（如 CentOs、Debian、Fedora、CoreOS、Ubuntu 和 Red Hat Linux）上配置 Kubernetes 集群。

您可以基于 KVM、libvirt 和 vSphere 将其部署在本地或虚拟环境中。

Kubernetes 的 Serverless 架构可以在 [Google Cloud](https://www.clickittech.com/google-cloud-consulting/)、Azure 和 [AWS](https://www.clickittech.com/aws-managed-services/) 等云平台上运行。不过，如果您混合和匹配跨云提供商或本地的集群，您也可以创建混合云。

### 自动装箱

Kubernetes 将自动打包您的应用程序，并根据所有可用资源和要求创建容器调度，而不会牺牲可用性。因此，Kubernetes 将在尽力而为和关键工作负载之间取得平衡，以节省未使用的资源并确保完全利用。

### 负载均衡和服务发现

Kubernetes 提供了关于网络和通信的安心，因为它会自动为容器分配 IP 地址。此外，对于一组容器，它提供了一个单一的 DNS 名称，该名称将在集群内进行负载均衡。

### 存储编排

Kubernetes 架构图允许您选择要挂载的系统存储。您可以选择公共云提供商，如 AWS、GCP，甚至本地存储。此外，您可以使用共享网络存储系统，如 iSCSI、NFS 等。

### 自我修复

Kubernetes 能够自动重启所有在执行期间失败的容器。此外，它将杀死所有未响应用户先前定义的健康检查的容器。最后，如果节点死亡，它将重新调度并替换所有其他可用节点中的所有失败容器。

### 密钥和配置管理

Kubernetes 可以帮助您更新和部署密钥和应用程序配置，而无需重建您的镜像并在堆栈配置中暴露密钥。

### 批量执行

除了管理服务外，Kubernetes 还可以处理您的批量和 CI 工作负载，如果需要，它将替换失败的容器

### 水平扩展

Kubernetes 只需要一个命令来扩展容器，但它也可以使用 CLI 缩小它们。您可以通过 Kubernetes UI 中找到的仪表板执行扩展。

### 自动回滚和发布

Kubernetes 可以逐步推出对您的应用程序或其配置的更新和更改。如果出现问题，Kubernetes 可以并且将会回滚更改。

这些是 Kubernetes 架构图的一些最关键的优势，但这并不是 Kubernetes 提供的全部。因此，让我们更深入地了解 Kubernetes 更有吸引力的方面及其实际用例。

![why use k8s blog](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

![why use k8s blog](https://images.clickittech.com/2020/wp-content/uploads/2022/04/13202258/CTA-blog_Mesa-de-trabajo-1-copia-176-1024x410.png)

### 在本地运行 Kubernetes

当企业在他们的数据中心而不是替代方案（公共云提供商）中实施 Kubernetes 架构图时，这变成了一件大事。这些几个重要因素对于公司决定实施本地 Kubernetes 策略至关重要，这很自然：

### 业务策略

每个企业都有特定的业务策略要求，例如需要在指定的地理位置准确运行工作负载。考虑到特定的策略需求，您会明白为什么企业可能难以利用公共云。

此外，如果提到的企业对其竞争对手有严格的业务策略，一些公司可能不接受来自各种公共云提供商的报价。

### 避免锁定

许多企业希望避免使用来自一个云提供商的服务，因为他们可能希望在多个云中部署他们的应用程序。这包括本地（私有）云。因此，企业将降低由于特定云提供商的问题而造成的永久性影响的风险。

此外，这使公司能够与云提供商协商更好的价格。

### 成本
在大规模应用中，在公有云中运行应用程序的成本可能很高，而成本效益可能是使用本地 Kubernetes 最重要的原因。

此外，如果您的应用程序依赖于处理和摄取大量数据，那么您可能需要支付高昂的费用才能在公有云环境中运行它们。

另一方面，由于现有数据中心的存在，利用“内部”Kubernetes 将显著降低运营成本。

### 数据隐私与合规性

一些组织对数据隐私和合规性问题有明确的规定。例如，如果公司的服务嵌套在特定的公有云中，这些规则可能会阻止公司为不同世界区域的客户提供服务。

您将有效地将您的应用程序现代化为具有您自己的数据中心的云原生格式。如果您选择本地 Kubernetes，您将显著改变您的业务。像这样的有效策略将帮助您节省大量资金，同时无疑会提高基础设施的利用率。

您可以下载我们的幻灯片 [企业和公司为什么要采用 Kubernetes？](https://clickittech.com/resource/slides/devops/Why-adopt-kubernetes.pdf)

## 您需要容器来使用 Kubernetes 架构图吗？

**是的，想要使用 Kubernetes 架构的公司会大规模地使用容器**，因为他们不使用一两个容器。而是使用几十个甚至 100 个容器，以确保高可用性并平衡流量负载。
随着流量的激增，**扩展容器**对于处理每秒不断增长的请求数量至关重要。相反，**缩减**可以在低需求期间优化资源使用并降低成本。

但这里有一个挑战：**手动容器管理既繁琐、耗时又效率低下**。这就提出了一个重要的问题：**所有这些手动工作都值得吗？** 答案在于**自动化**。

这就是**容器编排工具**的用武之地，而 **Kubernetes 在市场上处于领先地位**。凭借其**强大的自动伸缩能力**，Kubernetes 可以根据实时流量需求动态调整容器数量，从而节省大量的人工劳动。

它的主导地位不仅仅在于功能，**Google 创建了 Kubernetes**，使其成为当今最**值得信赖、可扩展且被广泛采用**的容器管理解决方案之一。

## Kubernetes 架构图如何工作

Kubernetes 架构图的组件是节点（机器集合）和控制平面。现在，让我们更深入地了解这些组件。

![kubernetes architecture diagram](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
![kubernetes architecture diagram](https://images.clickittech.com/2020/wp-content/uploads/2022/04/13202329/Diagram-55-1024x858.jpg)

### Kubernetes 架构图中的 Master 节点角色

**Master 节点是所有管理任务的起点**，其职责是管理 Kubernetes 架构图。
集群中可以有多个 master 节点，并且需要检查容错，因为更多的 master 节点会将系统置于称为“高可用性”的模式。

但是，一个 master 节点是执行所有任务的主节点。

### Kubernetes Master 节点组件

#### Kubernetes API 服务器

- master 节点内的 API 服务器是执行所有管理任务的地方。
- REST 命令随后会发送到 API 服务器以处理和验证请求。
- 集群的最终状态将根据请求存储在分布式键值上。

#### 调度器

- 此组件将任务调度到指定的从属节点。此外，每个从属节点将存储有关资源使用情况的信息。
- 调度器将以服务和 Pod 的形式调度所有工作。
- 在调度任务之前，调度器将考虑服务质量要求、亲和性、反亲和性、数据局部性等。

#### 控制管理器

- 控制管理器是一个控制器，一个用于调整 Kubernetes 集群的守护进程。
- Kubernetes 集群的目的是管理各种非终止控制循环。
- 此组件还执行其他操作，例如节点垃圾回收、事件垃圾回收和级联删除垃圾回收。此外，它还具有生命周期功能，例如命名空间创建。
- 本质上，控制器会监视托管对象的所需状态，但它也使用 API 服务器来监视和管理其当前状态。如果未满足对象的所需状态，则控制循环将通过采取特定步骤来实现此目标，从而确保当前状态和所需状态级别一致。

#### ETCD

- 此组件分发一个键值存储，最终使用集群状态。
- 您可以从外部配置 ETCD，也可以使其成为 Kubernetes Master 的一部分。
“Go”编程语言是人们用来编写 ETCD 的语言。在 Kubernetes 中，您可以存储配置详细信息，如 Secrets、ConfigMaps、子网等，并存储集群状态。

### Pod

Pod 是由一个或多个容器控制的单个应用程序。一个 Pod 包含一个唯一的网络 ID、应用程序容器和存储资源，以确定它将如何运行容器。

### Service

Pod 很容易发生变化。因此，Kubernetes 不能保证一个物理 Pod 将保持活动状态（如果复制控制器结束并以新的 Pod 开始）。

相反，Service 将显示一组逻辑 Pod，但它也将扮演网关的角色。这意味着您不必跟踪构成 Service 的 Pod，因为 Pod 可以向 Service 发送请求。

### NameSpace

是一个虚拟集群，可在跨多个项目的多个用户的环境中使用。值得一提的是，一个物理集群可以同时运行多个虚拟集群。

命名空间中的资源必须是唯一的，并且它们不会被授予对另一个命名空间的访问权限。此外，可以为命名空间分配资源配额，因此您可以避免过度消耗物理集群中的总体资源。

### Volume

在 Kubernetes 中，Volume 将应用于整个 Pod。因此，它将挂载在指定 Pod 中的所有容器上。即使容器重新启动，Kubernetes 也可以保证所有数据都将被保存。但是，如果 Pod 被杀死，Volume 也会消失。一个 Pod 可以有多个不同类型的 Volume。

### Deployment

Deployment 描述了 Pod 的所需状态或副本集，通常在 yaml 文件中。控制器将缓慢更新环境，直到当前状态和预期状态匹配，如 Deployment 文件中所指定的那样。此环境更新包括删除或创建副本。

yaml 文件为每个 Pod 定义了两个副本。但是，当只有一个副本正在运行时，yaml 文件定义也将创建另一个副本。因此，重要的是要知道，当 Deployment 管理副本时，不应直接操作它们。请改用新的实现。

### Kubernetes 高级架构图

在谈论高级别时，Kubernetes 架构图由几个部分组成，如控制平面（主节点）、几个 Kubelet（集群节点）和 ETCD（分布式存储系统，有助于保持一致的集群状态）。

![hire our accountable devops team](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
![hire our accountable devops team](https://images.clickittech.com/2020/wp-content/uploads/2022/04/13202303/CTA_Mesa-de-trabajo-1-copia-148-1024x321.png)

## Kubernetes 控制平面和节点架构详解

控制平面是一个特定的系统，它永久管理对象状态，帮助匹配系统对象的实际状态和所需状态，并响应集群内的任何变化。

控制平面由三个基本组件组成——kube-scheduler、kube-apiserver 和 kube-controller-manager。这些组件将通过单个主节点运行，甚至可以在多个主节点中复制（高可用性）。

### Kube-Scheduler

- 一个组件会监视新创建的没有分配节点的 Pod，并选择它们将运行的节点。
- 调度决策基于几个因素：数据局部性、工作负载间干扰、软件/硬件/策略约束、资源需求（个体和集体）、亲和性和反亲和性规范以及截止日期。

### Kube-Apiserver

- kube-apiserver 组件充当 API 服务器的中心实现组件。此外，它通过部署其他实例（水平扩展）进行扩展。可以运行多个实例并在它们之间平衡流量。
- API 服务器公开 Kubernetes API，它是 Kubernetes 控制平面的前端组件。

### Kube-Controller-Manager

即使每个控制器都是一个孤立的进程，您也可以将多个控制器合并到一个二进制文件中，但它将作为一个进程运行，以降低复杂性。

以下是一些控制器类型：

**节点控制器**——在节点关闭时发出通知并做出响应。
**Job 控制器**——监视 Job 对象（一次性任务）并创建完成任务的 Pod。
**Endpoints 控制器**——填充 Endpoints 对象（合并 Pod 和 Service）。
**Token 控制器和服务帐户**——创建新命名空间所需的默认帐户和 API 访问令牌。

### 工作节点架构

工作节点通过 Pod 运行应用程序，主节点控制 Pod。Pod 计划在物理服务器（从节点）上运行。因此，当您想从外部环境访问应用程序时，您必须连接到这些节点。

#### 工作节点组件

**容器运行时**

- 工作节点需要一个容器运行时来管理和运行容器的生命周期。
- Docker 经常被误认为是容器运行时，但它实际上是一个以这种方式利用容器的平台。

**Kubelet**

- Kubelet 与 Master Node 通信并在工作节点上执行。它通过 API 服务器获取 Pod 规范。此外，它还会执行健康且活跃运行的 Pod 中描述的相关容器。

**cAdvisor**

- cAdvisor 分析在指定节点上运行的每个容器的网络使用情况、文件、CPU 和内存的所有指标。您应该找到一个好的监控工具，因为 cAdvisor 不提供长期存储解决方案。
- 您无需采取特定步骤来安装 cAdvisor，因为它集成了 kubelet 二进制文件。

**Kubelet 快速工作流程图**

一个更实用的解决方案是向您展示 Kubelet 工作流程的图示，以便您更好地理解它的工作原理。您将在下面看到 Kubelet 工作流程的详细但快速的演示。

![kubelet workflow diagram](https://images.clickittech.com/2020/wp-content/uploads/2022/04/13202316/Diagram-53-1024x828.jpg)

**Kube-proxy**

- Kube-proxy 在每个节点上运行，并且与每个主机子网单独工作，以确保外部方可以访问所有服务。
- 它还充当位于工作节点上的任何服务的负载均衡器和网络代理。此外，kube-proxy 将管理 UDP 和 TCP 数据包的网络路由。
- 网络代理在每个工作节点上运行，并跟踪每个服务终结点的 API 服务器（删除/创建）。
- 为了使 kube-proxy 能够访问服务终结点，它会创建不同的路由。

## Kubernetes 概念、工具和部署

### ETCD

深入了解 Kubernetes 架构图总是很有趣的，并且 **ETCD 是一个出色的 Kubernetes 架构**示例的关键要素。Kubernetes 将所有集群状态信息存储在 ETCD 中，并且被称为控制平面的唯一有状态元素。

**ETCD 具有高度一致性，使其能够成为锚点协调点**。此外，由于 Raft 共识算法，ETCD 具有高可用性。
ETCD 的另一个出色功能是它可以将更改流式传输到客户端。这有助于所有 Kubernetes 集群组件保持同步。

### Kubectl

这是 Kubernetes 的命令行工具，可帮助您运行命令。此外，**Kubectl 有助于管理和检查集群资源、查看日志和应用程序部署。**

Kubectl 允许用户控制执行任何 Kubernetes 操作的访问权限。从更技术的角度来看，kubectl 是 Kubernetes API 的客户端。

### Kubernetes 网络

“每个 Pod 一个 IP”模型是 Kubernetes 的运作方式。这意味着每个 Pod 都分配有一个 IP 地址。此外，单个 Pod 中的容器将共享相同的 IP 地址和网络命名空间。

通常，CNI 将使用覆盖网络，通过利用 VXLAN（流量封装）来隐藏 Pod 的底层网络。此外，它可以利用其他完全路由的解决方案。无论它使用哪种解决方案，集群范围的 Pod 网络都是 Pod 将进行通信的地方，CNI 提供商管理此通信。

Pod 中没有限制，因此容器可以在彼此之间进行通信，因为在 Pod 中时，容器共享相同的 IP 地址和网络命名空间。这意味着容器的通信是通过 localhost 完成的。其次，由于 Pod IP 地址，Pod 之间的通信是可能的。

### Kubernetes 中的存储

Kubernetes 基于卷的概念；本质上，卷是一个可能包含 Pod 可以访问的某些数据的目录。但是，特定卷类型的使用决定了其内容，选择支持此目录的介质，以及此目录最初是如何形成的。

Pod 中的任何容器都能够使用同一 Pod 中的存储。最初，存储将在 Pod 重新启动时继续存在，但是 Pod 删除后会发生什么取决于存储类型。

各种可用的选项将允许您将块存储和文件存储挂载到 Pod，最受欢迎的选项是云存储服务，如 gcePersistentDisk 和 AWS EBS。或者，物理存储（如 iSCSI、Flocker、NFS、CephFS 和 glusterFS）也是可选的。

最后，StorageClasses 是一个抽象层，允许您查看底层存储的质量差异。此外，运营商使用 StorageClasses 来描述不同的存储类型，这为存储提供了基于来自每个 Pod 的所有传入声明的动态配置。

![kubernetes on aws blog](https://images.clickittech.com/2020/wp-content/uploads/2022/04/13202336/CTA-blog_Mesa-de-trabajo-1-copia-177-1024x410.png)

### Kubernetes Supervisord
管理和创建进程是supervisord主要的功能。然而，这些进程的起点是其配置文件中的数据。如果你想知道supervisord是如何做到这一点的，答案很简单——它创建子进程。

只要子进程处于活动状态，Supervisord就会管理它创建的每个子进程。这就是为什么supervisord被称为其子进程的“父进程”。

## Fluentd

[Fluentd](https://www.fluentd.org/) 是一个流行的开源数据收集器，你可以在你的 Kubernetes 节点上设置它。设置完成后，你将快速转换和过滤日志数据，并跟踪容器日志文件。通过这样做，你可以将它们传送到 Elasticsearch 集群，用于索引和存储数据。

**JSON 统一日志记录** – Fluentd 将尽可能地将数据结构化为 JSON。这对于处理日志数据非常重要，因为 Fluentd 会统一它们。处理日志数据包括过滤、收集、跨多个目标和来源的日志输出以及缓冲。

**可插拔架构** – 由于 Fluentd 具有灵活的插件系统，社区能够扩展功能。此外，这些插件将连接多个数据输出和数据源。Fluentd 插件非常有用，因为它们可以更好地简化日志使用。

**内置可靠性** – 由于此数据收集器使用基于文件的缓冲并支持内存，因此它可以防止你在节点间丢失有价值的数据。此外，你可以将其设置为高可用性，但请记住，它在应对困难的故障转移方面也表现出色。

**所需最低资源** – 这个开源收集器占用最少的系统资源，因为它是由 Ruby 和 C 语言组合编写的。

## Kubernetes 部署

Deployment 为 Kubernetes 提供了修改或创建携带容器化应用程序的 Pod 实例的指令。部署可以实现许多目标，例如在受控环境中启用更新代码的推出、扩展副本 Pod 数量，以及在需要回滚的情况下将代码回滚到之前的部署版本。

### 部署优势

Kubernetes 部署给我们带来的最有意义的好处是关于各种重复功能（扩展、更新生产中的应用程序、部署）的自动化系统。

此外，自动 Pod 实例启动机制让您高枕无忧，因为现在您可以放心，您的实例将按预期运行，并且在集群中的所有节点上运行。从本质上讲，您拥有的自动化程度越高，效果就越好。即使您的部署速度更快，您也会遇到更少的错误。OpenShift 可以在 Kubernetes 集群内外实现自动化；这是 [OpenShift vs Kubernetes](https://www.clickittech.com/devops/openshift-vs-kubernetes/) 之间的完整比较。

由于对节点和 Pod 进行持续的健康和性能监控，Kubernetes 部署可以绕过已关闭的节点，甚至可以替换失败的 Pod。通过这样做，部署控制器可以轻松地替换 Pod，以确保所有重要应用程序的无缝工作。

![let us help you to push your startup](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

![let us help you to push your startup](https://images.clickittech.com/2020/wp-content/uploads/2022/04/13202307/CTA_Mesa-de-trabajo-1-copia-149-1024x321.png)

Kubernetes 架构图最初不容易理解，但是当您理解后，您的工作生活将会变得更加轻松。

我们已经了解到，Kubernetes 被证明是扩展、支持各种解耦的有状态和无状态工作负载以及提供自动回滚和推出的绝佳解决方案。不过，它也是一个出色的平台，可让您编排应用程序（基于容器）。

今天，我们一起学习了很多信息。我希望您现在对 Kubernetes、它是什么以及它的工作方式有了更好的理解。如果您想了解我们尚未讨论的任何内容，请联系我们，我们团队的专业人员将帮助您解决任何问题。

此博客也可在 [DZone](https://dzone.com/articles/kubernetes-architecture-diagram) 上找到。不要忘记在那里关注我们

## Kubernetes 架构图常见问题解答

**什么是 Kubernetes 集群？** Kubernetes 集群是已定义的节点集。Kubernetes 架构图中的节点用于运行容器化应用程序。与虚拟机相比，Kubernetes 集群架构中的集群更灵活、更轻量级，可轻松管理、移动和开发应用程序。
**什么是 Kubernetes 构造？**

Kubernetes 构造至关重要，因为它们为您的容器化应用程序注入了活力。说到构造，一个很棒的 Kubernetes 架构示例是 deployment，因为此构造控制着 pod 的销毁和创建。

**Docker 和 Kubernetes 之间的主要区别是什么？**

Docker 和 Kubernetes 之间的主要区别包括 Kubernetes 跨集群运行，而 Docker 在一个节点上运行。另一个本质区别是，您可以在没有 Kubernetes 的情况下使用 Docker，但要使 Kubernetes 架构工作，您需要一个容器运行时来进行编排。

**什么是 Kubernetes 控制平面？**

Kubernetes 控制平面是 Kubernetes 架构图的大脑。控制平面做出所有决策，并通过 kubelet 与数据平面（主体）进行通信。

**为初学者解释 Kubernetes 架构的主要组件是什么？**

Kubernetes 架构围绕两个主要部分构建：**控制平面**和**工作节点**。

控制平面管理集群的整体状态，包括关键组件，如处理通信的 **API Server**、存储所有配置数据的 **etcd**、将 pod 分配给节点的 **Scheduler** 以及确保集群保持所需状态的 **Controller Manager**。**工作节点**是应用程序运行的地方，包含诸如管理容器的 **Kubelet**、处理网络的 **Kube-Proxy** 以及运行容器的**容器运行时**（例如，Docker）等组件。这些元素共同确保 Kubernetes 可以高效地管理和扩展容器化应用程序。

**Kubernetes 如何处理 pod 和服务之间的网络连接？**

Kubernetes 通过为每个 pod 分配唯一的 IP 地址来处理网络连接，从而允许 pod 之间直接通信，即使跨节点也是如此。

它使用**服务**为 pod 组提供稳定的访问点，包括 **ClusterIP**、**NodePort** 和 **LoadBalancer**。

Kubernetes 还包括一个内部 **DNS** 服务，使 pod 能够使用 DNS 名称而不是 IP 地址来查找服务，从而确保无缝通信和负载平衡。