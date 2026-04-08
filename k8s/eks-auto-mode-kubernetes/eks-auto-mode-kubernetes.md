<!--
title: Amazon EKS Auto Mode 旨在终结 Kubernetes 繁琐运维：逐个节点实现自动化
cover: https://cdn.thenewstack.io/media/2026/04/0116e405-thumbnail-47.png
summary: Amazon EKS 产品经理 Alex Kestner 介绍了 EKS Auto Mode。该模式通过接管节点生命周期和基础设施运维，减少平台团队的重复性繁琐工作，实现自动化的成本优化与扩展。
-->

Amazon EKS 产品经理 Alex Kestner 介绍了 EKS Auto Mode。该模式通过接管节点生命周期和基础设施运维，减少平台团队的重复性繁琐工作，实现自动化的成本优化与扩展。

> 译自：[Amazon EKS Auto Mode wants to end Kubernetes toil — one node at a time](https://thenewstack.io/eks-auto-mode-kubernetes/)
> 
> 作者：Adrian Bridgwater

在本期 [*The New Stack Makers*](https://thenewstack.io/podcasts/) 中，我们采访了 Amazon Web Services（AWS）Amazon Elastic Kubernetes Service（Amazon EKS）的首席产品经理 Alex Kestner。Kestner 解释了 Amazon EKS Auto Mode（自动模式）如何融入 AWS 的超大规模云厂商技术栈，以及他在与云原生计算基金会（CNCF）互动中的角色。这次讨论是在阿姆斯特丹举行的 [2026 年 KubeCon + CloudNativeCon 欧洲站](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 期间进行的。

## 固有能力，固有复杂性

Kestner 首先直面了一个令人不快的事实：他承认 Kubernetes 面临的挑战在于，由于它功能极其强大，任何拥有如此强悍实力的工具集都会带有一定的复杂性。而更受欢迎的消息是，通过 Amazon EKS，AWS 可以为客户承担“很大一部分无差异的繁重工作”。

但复杂性为何会出现？是因为扩展挑战、服务互连，还是因为与遗留系统的一些冗余连接？

> 大多数困难来自于那些消耗平台团队时间的日常任务，使他们无法为业务交付真正的价值。

“坦率地说，大多数困难来自于那些消耗[平台团队](https://thenewstack.io/caught-in-the-middle-the-new-role-of-platform-teams/)时间的日常任务，使他们无法为业务交付真正的价值，”Kestner 解释道，“这些事情阻碍了开发者，而他们本应致力于在应用程序中创造独特且差异化的价值，从而实现更快的交付和更好的用户服务。

“你可以联想到那些重复且持续的运营任务，例如处理集群中节点的生命周期，确保它们是安全的、最新的，并为性能和成本选择了正确的实例类型。为了确保集群中所有协助运行的软件保持一致且是最新的，这些任务是必需的。这样我们才能让工作负载在那个[集群](https://thenewstack.io/part-2-access-aws-services-through-a-kubernetes-dual-stack-cluster/)中得到最合适的适配。”

## 基础设施繁琐工作的克星

为了应对这一系列软件工程责任，Amazon EKS Auto Mode 旨在解决生产环境中的“基础设施繁琐工作”。该技术最初在 [AWS re:Invent 2024](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-eks-auto-mode/) 上推出，它解决了节点执行和行为中的共性问题，涵盖了从启动到[使用后退役节点](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/)的整个节点生命周期。

“从根本上说，自动模式旨在承担我们看到的平台团队所做的许多无差异的繁重工作，目的只是为了获得我们在 Kubernetes 和整个 CNCF 中看到的这个不可思议的生态系统所带来的好处，”Kestner 说道。

深入了解 Amazon EKS Auto Mode 的机制，我们可以看到，对于一个在生产环境中真正有用的 Kubernetes 集群，需要运行一些关键的运营软件元素，以帮助它与各种其他[基础设施原语](https://thenewstack.io/matt-biilmann-and-netlifys-quest-to-simplify-the-frontend/)进行交互，或者在 Amazon EKS 的情况下，与其他 AWS 服务进行交互。AWS 承担了这些元素的责任并在集群外运行它们；通过这样做，公司减轻了通常由云原生开发者承担的部分维护负担。

同样值得注意的是与 AWS EC2 团队合作开展的工作。其成果是 [Amazon EC2 Managed Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html)（Amazon EC2 托管实例），该公司将其定位为一种在 Amazon EC2 上运行计算工作负载的简化方式，并将实例的运营控制权委托给云服务提供商。每当 Amazon EKS Auto Mode 启动进入 Kubernetes 集群时，它都会使用 EC2 托管实例。

## 终结不可预测的工作负载？

AWS 做了大量细致的工作，但这里提供的运营减负是否预示着 Kubernetes 中不可预测工作负载的终结？合规性、安全性、虚拟化管理和整体云浪费现在会减少吗？Kestner 澄清说，不一定，但这主要是由于现代云原生部署的多样化地形。

“虽然我们不一定能影响客户用例的多样性，但 Amazon EKS Auto Mode 旨在为扩展和成本优化提供一个非常面向应用程序的视角……这总是会对容量规划有所帮助，”Kestner 说，“自动模式是建立在一系列开源标准和产品之上的，其中之一是 [Karpenter 项目](https://karpenter.sh/)，它致力于根据特定的工作负载需求来调整计算资源的规模。

“因此，这意味着客户可以让他们的工作负载指定所需的基础设施类型并定义其计算需求，而这一切基本上都是在后台完成的。自动模式随后会去寻找最优化且最具成本效益的基础设施来满足这些需求。”

我们在 Amazon EKS Auto Mode 中看到的并不完全是容量规划难题的终结，但它是朝着正确方向迈出的一步。随着今年 KubeCon + CloudNativeCon 欧洲站上的厂商讨论如此直接地集中在宣称拥有适合 AI 时代的云原生基础设施方案，针对平台团队的基础运营支持技术在未来一段时间内仍将至关重要。