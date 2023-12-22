<!--
title:  虚拟化的新时代
cover: https://cdn.thenewstack.io/media/2023/12/1956fb37-cncf_kccnc-na_kubevirt-announcement_featured-1024x576.png
-->

KubeVirt允许运维团队在Kubernetes API背后的容器中运行嵌套的KVM虚拟机，标志着虚拟化领域的转变。我们获得了关于1.1版本的更新。

> 译自 [The New Age of Virtualization](https://thenewstack.io/the-new-age-of-virtualization/)，作者 Alex Williams 是The New Stack的创始人和出版商。他是一位资深技术记者，曾在TechCrunch，SiliconAngle以及现在被称为ReadWrite的地方工作。Alex自上世纪80年代末就开始从事新闻工作，最初在...

虚拟机的概念已经存在一段时间，你可以这样说。但 Kubernetes 最初并没有虚拟机的概念。而现在，通过一个称为 KubeVirt 的新功能，它实现了虚拟机的支持。在某种程度上，这代表了虚拟化的新时代。

KubeVirt允许运维团队在容器中嵌套运行KVM虚拟机，并在Kubernetes API的背后运行。这意味着Kubernetes API现在包含了虚拟机的概念。对于在本地运行并需要虚拟机的应用程序来说，现在基于虚拟机的工作负载可以在位于API背后的集群中运行。

这是有道理的。虚拟机是物理基础设施的一个重要组成部分。但是在云原生环境中也同样适用，为什么不呢？

从历史上看，考虑到一些应用可能很容易被容器化，而其他技术可能不容易，这在权衡考虑与之相关的复杂性时曾经是一个更深层次的问题。一些人希望摆脱传统的虚拟化环境，[转向云端](https://thenewstack.io/messaging-connectivity-in-a-hybrid-kubernetes-cloud-environment/)。然而，他们的应用程序可能不允许或需要大量投资才能将其容器化。

虚拟化的新时代意味着虚拟机可以在不担心底层基础设施的情况下运行应用程序。它打开了许多机会和用例。迁移传统应用程序变得更加容易。它们无需容器化，这降低了完全容器化这些传统应用程序所带来的成本。

其他机会包括在相同环境中运行虚拟机和Kubernetes，在资源上进行削减，利用Kubernetes提供的动态资源，访问GPU，并支持ARM。

在KubeCon芝加哥峰会上，Red Hat的[Vladik Romanovsky](https://www.linkedin.com/in/vromanovsky/)和Nvidia的[Ryan Hallisey](https://www.linkedin.com/in/ryan-hallisey-b680b279/)与The New Stack的Alex Williams共同讨论了[Kubevirt 1.1](https://www.cncf.io/blog/2023/11/07/announcing-kubevirt-v1-1/)的发布情况，该版本已于KubeCon发布。 Kubevirt 1.0于7月份发布。

在1.1版本中，社区推出了内存热插拔和vCPU热插拔等功能。

“这些对于虚拟化领域并不是新功能，”Red Hat的高级首席软件工程师Romanovsky表示。“我们之前一直想实现这些功能，但由于各种限制，我们一直无法实现。平台不够稳定。”

Kubernetes和云原生方法对一些人来说可能似乎不太熟悉，但是，Hallisey，Nvidia的高级软件工程师和技术负责人表示，这应该是一个可以管理的跨越。

“当你看到[Kubernetes生态系统](https://thenewstack.io/kubernetes/)和[云原生环境](https://thenewstack.io/cloud-native/)的范式时，适应就会发生，” Hallisey说。“这其中有一些学习曲线，了解这些东西，但最终当你掌握它们时，你会发现自己又回到了熟悉的领域。相同的概念仍然适用。这些功能现在只是通过不同的方式暴露出来。”

