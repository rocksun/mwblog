
<!--
title: cert-manager月下载量达5亿的历程
cover: https://cdn.thenewstack.io/media/2024/12/7228606c-kccnc-na-24_matt-barker_ashley-davis_featured.png
-->

据The New Stack Makers的本期节目介绍，这个开源证书生命周期管理工具最初是作为求职者测试项目启动的。

> 译自 [How cert-manager Got to 500 Million Downloads a Month](https://thenewstack.io/how-cert-manager-got-to-500-million-downloads-a-month/)，作者 Heather Joslyn。

盐湖城——科技行业的招聘面试以让求职者经历重重考验而臭名昭著。但几年前，在初创公司 Jetstack，一个给求职者出的工程挑战变成了一个开源成功案例——[cert-manager](https://cert-manager.io/)。

Jetstack 早期就参与了[Kubernetes 的蓬勃发展](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)，旨在帮助其他组织使用 K8s 和容器。但 Jetstack 联合创始人 在《The New Stack Makers》系列节目的“On the Road”环节中回忆道：“因为我们起步很早，这已经是将近十年前的事了，当时 Kubernetes 周围几乎没有什么东西，我们不得不采取艰难的方式。”该节目在[KubeCon + CloudNativeCon 北美大会](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)录制。

Barker 说，附加组件很大程度上需要从头开始构建。同时，他说，客户要求一种在[Kubernetes](https://roadmap.sh/kubernetes)内部或与 Kubernetes 一起轻松管理证书的方法。

Barker 说，在招聘第一位工程师时，“我们想，现在每个人都在使用[Let’s Encrypt](https://letsencrypt.org/)。为什么我们不创建一个小的面试挑战，让这位未来的工程师在 Kubernetes 内部自动化 Let’s Encrypt 呢？

“我们让他在周五完成。他周一带着一个可运行的原型回来了，他说，我把它叫做 kube-lego：Kubernetes Let’s Encrypt Go 二进制文件，这就是它的作用。我和我的联合创始人互相看了一眼，心想，哇，他是怎么做到的？这太不可思议了。所以我们显然录用了他。”

不仅如此，kube-lego 还成为了 cert-manager，一个开源项目，在 9 月份毕业于[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)。

在本期 Makers 节目中，Barker（现在是[Venafi（一家 CyberArk 公司）](https://venafi.com/)（收购了 Jetstack）的副总裁兼全球工作负载身份架构主管）和他的同事 Davis（Venafi 的软件工程师）讲述了 cert-manager 如何从一个面试难题发展成为 CNCF 毕业项目的故事。

据 CNCF 11 月份发布的数据显示，该项目现在为[Red Hat OpenShift](https://www.openshift.com/try?utm_content=inline+mention) 用户以及 Kubernetes 用户管理证书，[每月下载量超过 5 亿次](https://www.cncf.io/announcements/2024/11/12/cloud-native-computing-foundation-announces-cert-manager-graduatio)。

## CNCF 如何帮助 cert-manager

Cert-manager 成为 CNCF 毕业项目的历程始于四年前，当时[它被捐赠给了该基金会](https://thenewstack.io/jetstacks-certificate-management-project-joins-the-cncf-sandbox-of-cloud-native-technologies/)，Barker 说这是一个“自然而然”的过程。

他说，该项目被设计成与证书颁发机构无关（或 CA 无关），并重新命名为 cert-manager。“然后接力棒传给了另一位工程师 ，他从那时起就开始发展它。它成为了执行特定生命周期管理的事实上的标准。”

Barker 说，一个指向 CNCF 管理的标志是围绕 cert-manager 已经壮大的社区。“我们收到了社区的积极反馈，”他说。“我们有很多贡献者；许多公司为 cert-manager 构建了连接器。因此，它周围已经存在一个非常强大的生态系统。”

Davis 说，CNCF 帮助维护者应对流行项目的一个长期挑战：“对于这样一个庞大的使用该项目的社区，不可避免地会对如何处理事情产生不同的意见。

“例如，如果我们发现某些东西可能被称为安全漏洞，但它并不是世界上最关键的事情。我们是否应该为此做出重大更改？我们是否应该中断其他人的工作流程来修复问题并确保它不会成为问题，或者我们是否应该接受它，记录它，然后继续前进？对此没有明确的答案。在这么多人参与这些讨论的情况下，达成共识可能很难。但通常情况下，我们都能达成共识。”

## cert-manager 的毕业后计划

现在 cert-manager 已经达到毕业状态，它还有很多计划要在路线图上实现。首先，Davis 说，有很多子项目。
其中包括[trust-manager](https://github.com/cert-manager/trust-manager)，根据其[GitHub](https://github.com/)文档，“这是一个小型Kubernetes操作符，旨在帮助减少管理集群中TLS信任捆绑包的开销”。它有一个证书签名请求（CSR），并与[Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/)服务网格集成。

Davis说：“我们在这些子项目中做的很多新东西和新工作都是为了解决与证书管理相关的其他问题。”“因此，[该]管理器可以签发这些证书，并获得您需要的证书。”

Barker表示，从更大的角度来看，他专注于解决在企业规模运行cert-manager的团队面临的问题。“Cert-manager已经成为堆栈的一部分。它已经成为既成事实，我们开始看到公司现在像对待云操作系统一样采用和部署Kubernetes，”他说。“因此，如果不是在使用Kubernetes的云原生技术上，你还会在哪里构建你的下一个应用程序呢？因此也就包括了cert-manager。”

这意味着，当然，要关注混合云、多云和边缘用例。他说，随着部署变得越来越复杂，“管理和运行起来会非常痛苦。这就是我在思考如何帮助那些企业用户简化这个过程。”

路线图上的另一个项目：帮助安全专业人员快速了解一个以开发人员速度和工作流程为理念构建的项目。

“现在，我们正在做的事情，并且花费大量时间去做的事情，就是教育安全团队了解使用cert-manager对组织的影响，以及如何正确地控制它、管理它，以及如何获取和发现所有这些证书和所有这些cert-manager实例。匹配开发人员方面发生的所有速度，但同时也要保证InfoSec团队可以应用的安全措施。”

查看完整剧集，了解更多关于cert-manager的信息，包括如何参与贡献。
