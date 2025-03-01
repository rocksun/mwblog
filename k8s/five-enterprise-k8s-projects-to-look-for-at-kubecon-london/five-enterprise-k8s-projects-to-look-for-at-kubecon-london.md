
<!--
title: KubeCon伦敦值得关注的五个企业级K8s项目
cover: https://cdn.thenewstack.io/media/2025/02/32396366-kubecon123.png
-->

> 译自：[Five Enterprise K8s Projects To Look For at KubeCon London](https://thenewstack.io/five-enterprise-k8s-projects-to-look-for-at-kubecon-london/)
> 作者：Ant Newman

尽管有大量的讨论，但仍有很多具有颠覆性意义却容易被忽视的开源项目。以下五个项目值得关注。

如果您打算参加今年四月在伦敦举行的[KubeCon欧洲大会](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)，您去的目的很可能不是为了品尝美食。您是奔着会议而来，特别是想深入了解云原生生态系统最新创新的脉搏。

当您访问日程安排页面来制定行程时，很容易感到不知所措。有超过300场演讲可供选择（从超过2500份提交中经过严格筛选）。

尽管演讲数量巨大，但仍有许多令人惊叹、至关重要、具有变革意义的开源项目拥有[蓬勃发展的贡献者和用户社区](https://www.cncf.io/blog/2025/01/29/2024-year-in-review-of-cncf-and-top-30-open-source-project-velocity/)，但在活动议程上的报道却很少或根本没有。

有些项目比较成熟；有些项目比较新，但它们在今年云原生计算基金会（[CNCF](https://cncf.io/?utm_content=inline+mention)）KubeCon EU日程安排中并没有扮演重要的角色。

- 对于每场OpenTelemetry或Prometheus的演讲（两者之间共有35场以上），只有一场[vCluster](https://thenewstack.io/kubernetes-gets-back-to-scaling-with-virtual-clusters/)演讲。
- 对于每场eBPF或Kubeflow的会议（两者之间共有22场），只有一场[Kairos](https://thenewstack.io/livin-kubernetes-on-the-immutable-edge-with-kairos-project/)会议。
- 您还将找不到关于备份工具[Velero](https://thenewstack.io/how-to-make-up-for-kubernetes-disaster-recovery-shortfalls/)、可持续性工具[kube-green](https://thenewstack.io/an-open-source-journey-to-greener-cloud-native-environments/)、网络超级工具[Multus](https://thenewstack.io/how-to-navigate-multiple-networks-for-kubernetes-workloads/)、数据存储Kine或裸机供应器[MAAS](https://thenewstack.io/provision-bare-metal-kubernetes-with-the-cluster-api/)的任何信息。一点都没有。

因此，让我们花一点时间来关注几个项目，作为Kubernetes的企业采用者，您需要了解这些项目。

## 1. Cluster API

Cluster API，或者简称CAPI，绝对属于“成熟”阵营；它始于2018年。它是多集群Kubernetes背后的驱动力，使您可以声明式地配置和管理集群，就像Kubernetes声明式地配置和管理其自身资源一样。Cluster API是可扩展的；存在许多CAPI提供程序，使您可以管理不同云和其他基础设施环境中的集群。

CAPI很重要，因为我们生活在一个多集群、多环境的世界中——当然，我们需要一种方法来提升自己并在集群之间进行编排。而CAPI以一种开源的方式实现了这一点，这完全符合K8s及其API驱动的、声明式的、可扩展的方法。

您今天可以在Spectro Cloud的Palette、[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) OpenShift、[VMware Tanzu](https://tanzu.vmware.com?utm_content=inline+mention)和许多其他产品中找到CAPI。它无疑正在对企业Kubernetes产生影响。并且它正在积极维护，在过去的几周内刚刚发布了新版本。但是，只有3700颗GitHub星，它并不完全处于聚光灯下。

有关Cluster API的详细信息，请[阅读我们的博文](https://www.spectrocloud.com/blog/cluster-api-and-kubernetes-cluster-management)。

在KubeCon上，您会发现只有几场演讲提到了CAPI。我们会将[New Relic的这场演讲](https://sched.co/1txDE)列入我们的日程安排。

## 2. KubeVirt

KubeVirt是将虚拟机工作负载引入Kubernetes集群的最流行的解决方案。作为一个项目，它已经运行了八年多，但最近随着企业寻求摆脱专有供应商价格上涨的策略，其开发和采用率有所提高。

虽然KubeVirt可能还不是家喻户晓的名字，但它已经获得了超过5000颗GitHub星，并被Nvidia、Cloudflare和一些我们不允许透露的大型企业使用。在贡献者方面，它也有一些非常强大的力量，包括Red Hat，您会发现它以某种方式烘焙到各种K8s管理平台中。

如果您致力于云原生，并且正在寻找虚拟机的归宿——就像数千家大大小小的企业一样——您需要了解KubeVirt。

在KubeCon上，您会发现只有三场演讲提到了它。我们推荐[Red Hat和Nvidia的这场演讲](https://sched.co/1td18)。同时，我们建议您[阅读这篇博文](https://www.spectrocloud.com/blog/production-ready-kubevirt-architecture-for-vms-on-kubernetes)。

## 3. vCluster
vCluster 允许您创建“虚拟集群”——看起来和感觉都像一个成熟的 Kubernetes 集群的环境，但运行在单个主机集群中。vCluster 可以在几秒钟内启动和销毁，并且开销非常小。它们也真正彼此隔离。

这些特性解决了一些 Kubernetes 的实际问题。vCluster 非常适合临时开发环境，因为它们不会让您的工程师等待半个小时才能使集群达到就绪状态，因此您不会在测试完成后仍让 vCluster 保持运行状态。隔离功能解决了命名空间的令人沮丧的弱点，例如资源名称跨越所有命名空间。

一些厂商甚至认为您不再需要多个集群，您可以只运行一个大型集群并使用虚拟集群进行分割。我们并不完全相信这种说法（我们的研究表明[集群数量呈上升趋势](https://info.spectrocloud.com/2024-state-of-production-kubernetes)），但我们确实相信 vCluster 对于某些用例非常有用，尤其是在您向开发团队提供 Kubernetes 作为服务 (KaaS) 时。

自从 Loft Labs 创建 vCluster 以来，它已获得 8,000 个 GitHub 星标，但您只能找到[KubeCon 上的一个演讲](https://sched.co/1tx9S)，来自 Loft。

同时，请阅读我们存档中的这篇[经典博文](https://www.spectrocloud.com/blog/virtual-kubernetes-clusters-with-palette-virtual-clusters)以开始使用。

## 4. Kairos

Kairos 是一个用于构建可定制可引导镜像的软件工厂，主要用于边缘计算环境。您可以放入您首选的操作系统和 Kubernetes 发行版，并获得安全、不可变的镜像——使其成为许多边缘用例成功的关键基础。

虽然它只有 1,200 个 GitHub 星标，但贡献者正在构建诸如可信启动之类的先进功能，并且 Kairos 已经在欧洲铁路等苛刻的环境中使用。

2024 年，Kairos 成为 CNCF 沙箱项目，使其备受关注。但是，如果您前往 KubeCon，则必须前往项目展馆才能与团队会面或观看周二的[五分钟闪电演讲](https://sched.co/1tcuw)。

您可能想[查看这篇博文以了解背景](https://www.spectrocloud.com/blog/livin-kubernetes-on-the-immutable-edge-with-kairos-project)。

## 5. LocalAI

在过去的几次 KubeCon 上，您都会看到关于 AI 的演讲，在伦敦，AI/机器学习 (ML) 轨道上有 25 场演讲。

我们知道 K8s 人们正在以各种方式拥抱 AI，包括使用诸如[K8SGPT](https://sched.co/1tx86)之类的集群操作助手，但我们也知道这是一个了解安全和隐私并喜欢一些 #selfhosted 和 #homelab 行动的社区。

因此，令人惊讶的是没有看到任何演讲（从标题中可以看出）关注如何在集群中运行 AI 模型以进行本地推理。无论是出于隐私原因还是远端边缘部署，在许多用例中，您都不能将数据发送到云或中央数据中心进行分析。

这就是 LocalAI 针对的用例，这是一个拥有超过 30,000 个 GitHub 星标的热门项目。它提供了一个与 OpenAI API 规范兼容的即插即用 REST API。您可以看到它[如何在本文中为 K8SGPT 等工具解锁价值](https://www.spectrocloud.com/blog/k8sgpt-localai-unlock-kubernetes-superpowers-for-free)。

## 拥抱多样性

云原生生态系统的广度一直是其杀手级优势和其致命弱点。我们的[2024 年生产 Kubernetes 状态研究](https://info.spectrocloud.com/2024-state-of-production-kubernetes) 发现，浏览生态系统是企业采用者的首要挑战。

因此，让我们利用 KubeCon 的机会，从讨论常见项目的拥挤主题演讲中抽身出来，将注意力转向我们试图解决的挑战以及为解决这些挑战而构建的创新项目。

让我们尽我们所能支持这些项目，不仅通过贡献代码或资金的常规途径，还通过选择不带偏见的平台并简化创新采用的方式。这种选择的理念是我们 Palette 平台背后的指导原则之一。[请查看。](https://www.spectrocloud.com/integrations-and-environments)
