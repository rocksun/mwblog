# 为解决 Kubernetes 蔓延问题，尝试“自下而上”的 Kubernetes

![Featued image for: To Solve Kubernetes Sprawl, Try Kubernetes ‘All the Way Down’](https://cdn.thenewstack.io/media/2024/10/6133b087-kubernetes-solve-itself-turtles-1024x576.jpg)

在某个时刻，某些技术会有效地“获胜”并成为默认的普遍标准。我们已经多次看到这种情况，但最突出的两个是 TCP/IP+以太网和 Linux。最近，[Kubernetes 成为交付应用程序负载的事实标准](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/) 已经变得很明显。

[Kubernetes](https://roadmap.sh/kubernetes) 用于交付云原生应用程序、传统单体应用程序、虚拟化以及几乎所有其他内容。之所以会这样，是因为与之前的 TCP/IP+以太网和 Linux 一样，Kubernetes 是一个“只需运行”的 80-90% 解决方案，用于交付和管理应用程序负载。现在，随着 Kubernetes 在企业内部和外部变得越来越流行，我们看到 Kubernetes 集群的“蔓延”现象越来越严重。就像之前的路由器/交换机、服务器和虚拟机 (VM) 蔓延一样，组织必须采取措施才能成功地大规模管理 Kubernetes。解决方案？答案是……Kubernetes。

## 首先，一些背景信息

乍一看可能并不明显，但 TCP/IP+以太网最初并不是今天这样普遍的标准。在 20 世纪 80 年代中期，[思科](http://cisco.com/?utm_content=inline+mention) 系统是[第一家推出多协议路由器的公司](https://web.archive.org/web/20070707180833/http://newsroom.cisco.com/dlls/2004/hd_061404.html)。当时，互联网骨干网仍然由美国政府，即国家科学基金会 (NSF) 运营。许多企业园区使用不同的 L2/L3 协议，包括 AppleTalk、[SNA](https://en.wikipedia.org/wiki/Systems_Network_Architecture)、[DECnet](https://en.wikipedia.org/wiki/DECnet)、[Banyan Vines](https://en.wikipedia.org/wiki/Banyan_VINES)、令牌环、IPX/SPX (Novell) 等。后来，许多其他 L1/L2 协议问世，例如 20 世纪 90 年代的光纤分布式数据接口 (FDDI) 和异步传输模式 (ATM)。

然而，如今，TCP/IP 和以太网的组合已经一次又一次地获胜，因为它们是开放标准，易于获取，通常避免锁定，并解决了 80-90% 的网络问题。这使得任何精通该组合的人都可以从一个解决方案（例如，校园网络）转向另一个解决方案（例如，互联网骨干网网络）。

Linux 的历史类似。它不是第一个在 x86 平台上运行的 UNIX 变体；这一荣誉属于 SCO/[微软](https://news.microsoft.com/?utm_content=inline+mention) Xenix。多年来，它一直不如早期的 UNIX SVR4 版本（如 Solaris 和 AIX），这些版本拥有更好的支持、对称多处理以及更多优势。然而，与 TCP/IP+以太网一样，Linux 随着时间的推移一次又一次地获胜，它是一个开放标准，易于获取，可以避免供应商锁定，并有效地解决了从树莓派到大型高性能计算 (HPC) 集群的任何解决方案的 80%-90% 的操作系统问题。现在，世界上大多数数据中心都运行在 Linux 上。

## 这就引出了 Kubernetes

很长一段时间以来，Kubernetes 已经有效地赢得了应用程序部署之战。它最初是针对大规模应用程序的云原生解决方案，但随着时间的推移，它变得足够通用，现在经常用于传统应用程序、虚拟化以及几乎所有负载。它可以在树莓派、Microsoft Windows、大型 HPC 集群或任何地方运行。

重要的是，它具有简洁且可扩展的架构，以及对运营商和开发人员都友好的[API](https://thenewstack.io/the-power-of-k8s-api-solutions-revolutionizing-industries/)。它提供了一个抽象层，您可以在开发时在笔记本电脑上运行，与在生产环境中运行时相同。

Kubernetes 并不是第一个尝试构建应用程序平台的尝试。WebLogic 和 WebSphere 早于它出现；它们只支持[Java](https://thenewstack.io/java/) 应用程序，但具有类似的意图：使应用程序的打包和部署更容易。虚拟化也可以被认为具有类似的意图。然而，在过去 10 年中，Kubernetes 一次又一次地获胜，以至于现在您在 Kubernetes *之上* 运行[VM](https://github.com/kubevirt/kubevirt)、[WebLogic](https://oracle.github.io/weblogic-kubernetes-operator/) 或 WebSphere！
Kubernetes 已发展成为应用负载部署的事实标准。就像之前的 TCP/IP+以太网和 Linux 一样，它解决了 80%-90% 的应用打包、部署和运维问题。它是一个开放标准，易于获取，并允许您避免供应商锁定。也许最重要的是，它拥有一个内置的架构，可以帮助运维，允许滚动升级，为您的负载（Pod）提供清晰的分层方式，提供可扩展的 API 等等。我们对此非常了解。我们是第一个将 [OpenStack](https://www.openstack.org/) 的控制平面放在 Kubernetes 上，并使用 Mirantis OpenStack on Kubernetes (MOSK) 的公司。我们很早就知道 Kubernetes 最终会获胜——虽然有时 [复杂](https://thenewstack.io/tackling-the-complexities-of-kubernetes-fleet-management/)，但使用它的好处实在太大了。

## Kubernetes 无处不在
这让我们回到了问题的核心：现在 Kubernetes 已经获胜，我们如何管理无休止的 Kubernetes 集群洪流？大多数大型企业都在各个地方使用它：[AWS](https://aws.amazon.com/?utm_content=inline+mention) EKS、[Google](https://cloud.google.com/?utm_content=inline+mention) GKE、Microsoft AKS、Mirantis MKE、通用 Kubernetes 等等等等。无论是在本地还是在公有云上，K8s 无处不在，并且像杂草一样不断增长。解决方案是什么？

当然，是 Kubernetes！它确实是“[乌龟——或者 Kubernetes——无处不在](https://en.wikipedia.org/wiki/Turtles_all_the_way_down)！”

很明显，管理 Kubernetes 蔓延的最佳方法是使用 Kubernetes 作为控制平面来管理其他 Kubernetes 集群。Kubernetes 可以成为管理您的“薄层”Kubernetes 的自然“控制点”，支持各种容器和虚拟化工作负载，并抽象基础设施。

例如，[k0smotron](https://github.com/k0sproject/k0smotron) 将控制平面（管理集群或控制节点）和数据平面（管理集群或工作节点）分开。这为您的 Kubernetes 集群提供了一个单一的控制点，以提高可扩展性，分离关注点（例如，分别升级您的控制平面和数据平面）以及跨不同提供商管理集群（即与基础设施选项无关）。这允许使用 Kubernetes 集群来实现“混合多云”的圣杯。换句话说，您不再关心您的集群位于何处，因为您是从同一个控制点管理它们。

## Kubernetes 是 Kubernetes 的解决方案
当我提到“控制点”时，这意味着在任何 IT 系统中，通常都有一个自然的控制点来与该系统交互并管理它。例如，对于 Amazon Web Services，AWS API/UI 是管理该系统的自然控制点。对于 Java 应用程序，自然控制点是 JVM。大多数系统都有一个控制点，即使它们的控制平面和数据平面是合并的。

现代控制点的独特之处在于它们几乎总是具有 API。传统控制点不太可能具有支持 API 的控制点。在这个现代的无处不在的自动化时代，所有控制点都必须具有 API。

这就是 Kubernetes 能够独特地管理自身的原因。借助 Cluster API (CAPI) 及其提供商，我们可以使用 Kubernetes 来管理 Kubernetes，因为作为控制点，它可以管理其他控制点。Cluster API 包括 Amazon (CAP-A)、Azure (CAP-Z)、[VMware](https://tanzu.vmware.com?utm_content=inline+mention) (CAP-V)、裸机和 [更多](https://cluster-api.sigs.k8s.io/reference/providers) 的“提供商”。

这意味着所有必要的工具都已准备就绪，可以使用 Kubernetes 来“解决自身”。解决 Kubernetes 蔓延的答案 *就是* Kubernetes 本身。作为开放标准，Kubernetes 是跨本地和云集群管理的明显解决方案。早期的控制平面工作，例如 k0smotron，已经证明了总体方向，但现在是时候将其提升到一个新的水平，并兑现“Kubernetes 无处不在”的承诺。

*要了解更多关于 Kubernetes 和云原生生态系统的信息，请加入我们参加 **KubeCon + CloudNativeCon 北美**，于 2024 年 11 月 12 日至 15 日在犹他州盐湖城举行。*
[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)