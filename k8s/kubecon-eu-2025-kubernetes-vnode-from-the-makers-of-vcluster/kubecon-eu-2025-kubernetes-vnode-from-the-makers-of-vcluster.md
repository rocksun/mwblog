<!--
title: Kubernetes vNode，来自vCluster的创造者
cover: https://cdn.thenewstack.io/media/2025/04/a607bf27-vnode.png
summary: KubeCon爆款预定！LoftLabs推出vNode，为Kubernetes节点级隔离放大招！区别于vCluster，vNode主打商业化，轻量级运行时隔离Workload，安全增强！对比Kata Containers、GVisor，vNode性能更优，与DaemonSet集成，Helm Chart一键安装，特权容器也能Hold住！云原生多租户的福音！
-->

KubeCon爆款预定！LoftLabs推出vNode，为Kubernetes节点级隔离放大招！区别于vCluster，vNode主打商业化，轻量级运行时隔离Workload，安全增强！对比Kata Containers、GVisor，vNode性能更优，与DaemonSet集成，Helm Chart一键安装，特权容器也能Hold住！云原生多租户的福音！

> 译自：[KubeCon Europe: Kubernetes vNode, From the Makers of vCluster](https://thenewstack.io/kubecon-eu-2025-kubernetes-vnode-from-the-makers-of-vcluster/)
> 
> 作者：Joab Jackson

在伦敦举行的 [KubeCon + CloudNativeCon 欧洲 2025](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) 的 Kubernetes 管理员应该在本周参观 S281 展位的 [LoftLabs](https://www.loft.sh/company/about)，以了解该公司最新的技术 [Kubernetes vNodes](https://www.loft.sh/blog/vnode-kubernetes-node-isolation-multi-tenancy)。

vNode 是一种在 Kubernetes 集群中隔离单个节点的工具，它延续了该公司在 2021 年推出的一项名为 [vCluster](https://thenewstack.io/loft-labs-vcluster-provides-secure-multitenant-kubernetes-clusters/) 的开源技术，该技术虚拟化 Kubernetes 控制平面，以简化多租户、提高安全性和更有效地利用资源。

该公司声称，vNode 是一种轻量级运行时，它在此过程中迈出了下一步，在节点级别提供隔离，以便更好地共享集群，同时保持工作负载之间的强大隔离。

该软件将面向需要安全多租户和[特权容器访问](https://thenewstack.io/kubecon-eu-2025-edera-protect-offers-a-secure-container/)的企业 IT 团队，并且它与所有主要的 Kubernetes 云提供商和符合标准的独立 Kubernetes 集群集成。

[Lukas Gentele](https://www.linkedin.com/in/gentele/) 在接受 TNS 采访时指出，与 [vCluster](https://thenewstack.io/vcluster-to-the-rescue/) 不同，vNode 不会开源，而是会保留为商业产品。

## 隔离挑战

最初，[多租户](https://www.f5.com/glossary/multi-tenant-cloud-architecture)并不是 [Kubernetes 设计者](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)的 [当务之急](https://www.ibm.com/think/topics/kubernetes-history)，他们认为容器编排器的用例主要是由单个团队用来管理自己的集群。

尽管如此，[Kubernetes 多租户](https://kubernetes.io/docs/concepts/security/multi-tenancy/)（其中多个参与者可以共享一个集群）已成为一种重要的运营模式，因为企业和云提供商都为不同且有时相互竞争的客户提供 Kubernetes 服务。

![Multi-tenancy diagram](https://cdn.thenewstack.io/media/2025/04/48f288c5-multi-tenancy.png)

*Courtesy of Kubernetes.io*

## 仅靠命名空间无法解决问题

Gentele 解释说，[命名空间](https://thenewstack.io/what-are-linux-namespaces-and-how-are-they-used/) 通过 vCluster 等技术帮助驯服了 [Kubernetes](https://thenewstack.io/kubernetes/) 控制平面，但对于隔离集群中的单个节点没有太大帮助。

Kubernetes 的设计目的不是为了分离节点，也不是为了在节点级别隔离 I/O 和带宽等资源。来自不同命名空间的 Pod 在同一节点上运行，它们彼此之间没有隔离，也不会免受嘈杂邻居或其他占用过多资源的 Pod 的负面影响。在节点级别管理所有这些问题令人头疼。

将租户放入他们自己单独的节点确实提供了强大的隔离，但就资源分配而言，这可能很昂贵，因为并非所有资源都可能在每个节点中使用。

已经有不同的方法来解决这个问题，例如 [Kata Containers](https://thenewstack.io/the-road-to-kata-containers-2-0/)、Google 的 [GVisor](https://thenewstack.io/google-launches-gvisor-an-open-source-sandboxed-container-runtime/) 和 [Docker](https://www.docker.com/?utm_content=inline+mention) 的 [Sysbox](https://github.com/nestybox/sysbox)。

Gentele 解释说，每种方法都有其缺点。

![](https://cdn.thenewstack.io/media/2025/04/9d76da0b-vnode-02.png)

[Kata Containers](https://katacontainers.io/)（通常称为“微型 VM”）带有自己的独立内核，并且可能具有很高的开销。它们也不能与每个云提供商一起使用。

Google [gVisor](https://gvisor.dev/) 通过系统调用过滤流量，这会降低性能，并且主要限于 Google Cloud。Sysbox 的工作方式与 vNode 最为相似，主要用于 [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/)。

## vNode 方式

[vNode](https://www.vnode.com/) 是如何工作的？它是一个位于 Kubernetes 控制平面和底层工作节点之间的运行时。在那里，它在共享物理节点内的轻量级虚拟化层中隔离工作负载。
在一段[视频](https://youtu.be/woqIVrnbGuE)中，LoftLabs 演示了一个具有特权的 workload pod 执行到具有特权的 pod 中，仍然可以访问该 pod 上的其他资源，例如 Kubelet 或 CoreDNS，从而使它们容易受到[容器逃逸](https://thenewstack.io/leaky-vessels-vulnerability-sinks-container-security/)攻击。

要安装 vNode，用户需要配置一个 Helm chart，以便在集群的每个节点上安装一个 vNode [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)，这将自动将具有特权的 pod 放入虚拟节点中（提醒 containerd 运行时不要运行此 pod）。因此，从 pod 本身逃逸的攻击者仍然被隔离在 vNode 中，而不是在主机节点上横冲直撞。

这种方法在保持严格边界的同时，保持了资源效率并提供了高性能。用户可以为不同的团队、项目和应用程序划分节点，而无需求助于虚拟机。

![vNode 比较图](https://cdn.thenewstack.io/media/2025/04/1de9e1a0-vnode-03.webp)

*图片由 LoftLabs 提供。*

## vCluster 集成

虽然虚拟集群提供了工作负载隔离，但它们仍然可以共享底层节点。使用 vNode 可确保即使租户工作负载共享同一集群，它们仍然保持隔离。

LoftLabs 表示，通过结合使用 vCluster 和 vNode，客户将能够在保持强大隔离的同时，平衡共享资源的成本效益。

除了演示 vNode 之外，LoftLabs 的展位还将展示 vCluster 本身的一些新功能，包括新的快照和恢复功能以及更强大的 [Rancher Labs 集成](https://thenewstack.io/suse-upgrades-its-rancher-kubernetes-management-family/)。