
<!--
title: 虚拟化和容器：强强联合
cover: https://cdn.thenewstack.io/media/2024/03/3227501a-chocolates.jpg
-->

随着虚拟机和虚拟化技术的不断发展，似乎这项技术注定会被淘汰。但与企业计算中的大多数事物一样，旧技术并不会轻易消失。

> 译自 [Virtualization and Containers: Better Together](https://thenewstack.io/virtualization-and-containers-better-together/)，作者 Alex Handy。

改变总是令人望而生畏。当企业虚拟化在 2000 年代初开始抬头时，它迫使管理员和架构师摆脱单机思维的资源规划。现在，得益于[虚拟化](https://thenewstack.io/the-new-age-of-virtualization/)，每台机器都可以成为多台机器。大型服务器可以在一台设备上托管一百台虚拟机，从而推动服务器整合和降低成本。

当那些相同的管理员和架构师需要了解和采用 Linux 容器时，这种资源整合的趋势仍在继续。随之而来的是可部署资产的极大简化，将其精简到更小的规模，并消除了大量的依赖项和操作系统冗余。

在从虚拟机和虚拟化中走出来之后，似乎这项技术注定要像过去单服务器应用程序一样被废弃。但与企业计算中的大多数事物一样，旧技术不会轻易消失，它仍然存在，并且[通常“运行业务”。](https://thenewstack.io/what-workloads-do-businesses-run-on-kubernetes/)

## 协同工作

[Fabian Deutsch](https://github.com/fabiand) 是红帽的高级工程经理，也是 [KubeVirt 项目](https://kubevirt.io/) 的维护者，该项目最初旨在 [将虚拟机引入 Kubernetes](https://thenewstack.io/the-future-of-vms-on-kubernetes-building-on-kubevirt/)。自该项目于 2016 年启动以来，这便一直是他工作的重点，如今他为这个 Kubernetes 子项目取得的进展感到自豪，现在该项目完全专注于在云原生计算基金会 (CNCF) 中毕业。[今天发布的红帽 OpenShift 4.15](https://www.redhat.com/en/blog/unveiling-red-hat-openshift-415) 将 KubeVirt 作为 OpenShift 虚拟化的基础。

该项目的首要目标是为虚拟机提供一流的云原生支持。

“我们[采用了 Kubernetes 的理念和 API](https://thenewstack.io/databases-and-kubernetes-adopting-a-distributed-mindset/) 将其融入其中，让虚拟机受益于丰富的 CNCF 生态系统，”Deutsch 说。“我们加倍投入这个生态系统和许多其他项目也已采用的云原生 API。KubeVirt 最大的优势在于它几乎以原生方式与 Kubernetes 平台相结合，因此可以与许多基于 Kubernetes 的项目（例如 Prometheus、Tekton、CRIO 或 Argo CD）一起使用。在 [Argo CD](https://argo-cd.readthedocs.io/en/stable/) 的情况下，我们添加了一些胶水，让 Argo CD 可以像处理容器一样处理虚拟机。”

在 CNCF 沙箱中待了三年，并在 [CNCF 孵化器](https://www.cncf.io/projects/) 中待了近三年后，Deutsch 自豪地表示 KubeVirt 即将毕业。Deutsch 说，虽然仍有工作要做才能实现这一目标，但最终用户现在应该知道 KubeVirt 已经成熟且功能丰富。高盛萨克斯代表（KubeVirt 用户）将在本周的 KubeCon EU 上的主题演讲中谈论他们的经验。

## 一切都很熟悉

KubeVirt 基于 KVM，因此它与过去二十年来在开源虚拟化的各个领域中使用的所有熟悉的工具和虚拟化技术相同。KubeVirt 沿用了以前 KVM 用户熟悉的基本概念、性能和客户机操作系统兼容性。主要区别在于用户可以通过他们选择的 Kubernetes 平台（例如 [OpenShift 虚拟化](https://www.redhat.com/en/resources/15-reasons-adopt-openshift-virtualization-ebook)）对其进行配置，这是该平台本身提供的功能（例如 RBAC、身份管理存储和网络抽象）。

这为 KubeVirt 带来了两个结果：首先，熟悉 KVM 的现有虚拟化用户可以期待 KubeVirt 像在正常的独立虚拟化情况下一样运行他们现有的虚拟机。其次，由于它与 Kubernetes 集成，因此用于管道（Tekton）、用于持续部署（Argo CD）和用于网络（Istio）等 CNCF 项目通常也几乎可以自然地与虚拟机一起工作。

根据 Deutsch 的说法，这为用户带来了许多好处。

改变是困难的。如果运营商决定迁移到新平台，需要牢记一个问题：当我进行这项重大投资以迁移到新平台时，我是否希望维持现状，还是希望让自己处于能够从大型生态系统中受益并拥有一个允许我及我的最终用户不断发展的位置。这意味着改变运营商的工作方式或最终用户在平台上部署应用程序的方式。运营商和容器是运营商自动化其工作的机会，也是最终用户以不同且更有效的方式交付应用程序的手段，”他说。

还有其他好处，因为它更高效或更快，或者新员工希望以容器而不是虚拟机的方式交付，因为这更容易。他们有新工具、新 IDE、新软件，而为最终用户提供这些计算能力的平台所有者现在可以通过 Kubernetes 构建的自服务来实现这一点。拥有一个现代灵活的自服务平台也有助于招聘和留住人才。

虽然当今的 KubeVirt 中提供了许多传统的虚拟化功能，但 KubeVirt 中仍有新功能不断涌现，并且随着用户群几乎每天都在扩大，对该平台有了新的需求。

借助[BootC](https://github.com/containers/bootc)，我们现在有了可引导容器。我们统一了交付容器和虚拟机的路径。虽然当今已经有了如此多的协同作用，但这并不是终点，”他说。

未来计划扩展到更好的文档。随着更多工作负载迁移到 KubeVirt，对更广泛支持的需求不断增加，而这正是团队现在的重点，Deutsch 说。

我们想要的一件大事是毕业。我们需要在 KubeVirt 中解决一些流程和政府事务。在过去几年中添加了如此多的功能后，我们需要对 KubeVirt 的其他方面给予更多关注，”他说。

目标必须是将其设置为在未来五年内取得成功。我们对“硬功能”给予了大量关注——与 Kubernetes 冲突的更传统的功能，例如热插拔。我们最终确定了 CPU 和内存热插拔，并且我们还正在扩展与 OVN Kubernetes 的合作以获得更好的网络解决方案。

我们花时间构建了 KubeVirt，”Deutsch 说。“我们不想操之过急。我们尝试在 Kubernetes 之上构建最佳解决方案，并以正确的方式与 Kubernetes 集成。KubeVirt 不再是一个年轻的项目，但现在是尝试它的最佳时机。我们已经成熟了。
