<!--
title: SimKube模拟Kubernetes集群
cover: https://cdn.thenewstack.io/media/2023/12/a68b856a-david_morrison-acrl-kubecon-1024x768.jpg
-->

SimKube可在模拟/开发集群重现Kubernetes生产集群的追踪，用于故障排除和参数测试。

> 译自 [Simulate Kubernetes Cluster Behavior with SimKube](https://thenewstack.io/simulate-kubernetes-cluster-behavior-with-simkube/)，作者 Joab Jackson 是 The New Stack 的高级编辑，负责报道云原生计算和系统操作。他报道 IT 基础设施和开发 25 多年，包括在 IDG 和 Government Computer News 的任期。在那之前，他...... 

Kubernetes 很复杂，一旦投入生产，调试成本很高。如果有一种方法可以在实际运行云服务提供商账单之前，以逼真的方式测试新的 Kubernetes 部署，那该多好？

[SimKube](https://github.com/acrlabs/simkube) 就是为了提供这种能力而诞生的。它可以在实际集群上记录一些行为，然后在模拟集群上回放这些行为，以便能够对其进行详细检查。从长远来看，这种技术不仅可以进行模拟回放，甚至可以帮助用户尝试不同的场景。

它是Applied Computing Research Labs的创始人 [David Morrison](https://www.linkedin.com/in/david-morrison-9419b110/) 的设想的结晶，该实验室是一个专注于建模、调度和优化分布式系统的研究与开发公司。他在今年早些时候在芝加哥举行的 [KubeCon + CloudNativeCon 北美大会](https://thenewstack.io/kubecon-2023-managing-pets-cattle-and-starfish/)上介绍了 SimKube 以及对这种技术的需求。

尽管 SimKube 在功能上已经成熟，但它仍处于早期开发阶段。随着 Kubernetes 被越来越多地用在生产环境中，像 SimKube 这样的行为分析和监控工具将变得非常必要，不仅可以重播有问题的场景，还可以设计和尝试新的场景，Morrison 认为。

建立一个集群或者启动一个节点的平均时间是多少？我们可以比较两个不同的模拟来看哪一个更有效率吗？

“能够回答这些问题非常重要，我认为在 Kubernetes 生态系统中，我们现在缺乏这种工具。” Morrison 说。

## 想象一下可能性

令人欣喜地是，Morrison描绘了 Kubernetes 仿真工具可以在各种场景下的使用方式。

一个明显的使用案例是故障排除: 集群可能会出现故障，但根本原因不明。管理员可以在自己的笔记本电脑上重播发生故障时的事件追踪。当潜在的修复方案制定好时，可以先在模拟集群上测试。

它也可以用来预防潜在问题。

负责所有通向集群的管道的 CI/CD 工程师可能想确保用户不会在新的 Kubernetes 配置中引入任何[回归](https://thenewstack.io/kubernetes-races-to-fix-regressions-introduced-by-recent-security-patches/)。他们可以通过要求在入门过程中运行模拟来实现这一点。

仿真软件也可以成为从 Kubernetes 部署中获取最大价值的有力盟友。

Kubernetes [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/) 有许多旋钮可以调整，在为节点分配工作负载设置优先级方面，尽管它让人猜测最佳调度是什么。想象一下在笔记本电脑上运行不同的场景，使用真实的生产数据，并看到哪种配置效果最好的一些数字。您甚至可以将运维数据馈送到机器学习机器进行“超参数”调优。

在调度方面，Kubernetes 的批处理一直是一个特殊的挑战，因为它没有强大的批处理原语可用。但随着机器学习运维的出现，大规模批处理作业变得越来越普遍，它必须处理大规模的语言模型或扩散模型工作负载。这导致了诸如 [Volcano](https://github.com/volcano-sh/volcano) 之类的替代调度程序的出现，它也可以在做出承诺之前进行轻松测试。

## 见识 SimKube

SimKube 由 Morrison 创建，[主要用 Rust 编写](https://thenewstack.io/rust-is-surging-ahead-in-webassembly-for-now/)，是一组 6 个工具，用于模拟 Kubernetes 调度和自动扩展行为。

命令行实用程序 sk-ctrl 提供了从生产集群导出运维数据并在模拟集群上重播该数据的方法，从而模拟相同的行为。

![放大](https://cdn.thenewstack.io/media/2023/12/5ca7e4d3-sk-overview-1024x628.png)

*SimKube 的工作原理。*

放置在生产环境中，sk-tracer 从 API 服务器收集数据。它可以监视并创建资源和 pod 在集群上弹起或下降的时间线(称为 trace)，并记录发生的任何预定义的特殊事件。如果您有一个自定义控制器，它也可以监视它。

在用户请求时，sk-tracer 会将追踪保存到文件中。追踪对象本身大部分是时间线对象(序列化为类 JSON 的二进制格式)。

当用户希望重新运行追踪时，sk-driver 会下载追踪对象，并通过模拟集群(在开发环境或笔记本电脑上运行的 [KIND](https://kind.sigs.k8s.io/))上的 API 服务器运行它。

## 虚拟节点

提供模拟集群虚构部分的是 sk-vnode 和 sk-cloudprov。sk-vnode 基本上是一个假装是节点的虚拟 Kubelet。当被 ping 时，它会响应一个状态，但里面没有容器。

“您可以在本地笔记本电脑上启动成百上千个这些东西。它真的很轻量级，”Morrison 热情地说。

为了模拟您的生产集群，您可以使用 kubectl 导出生产配置文件，使用节点定义来设置相同的模拟节点。

您可以像部署常规集群一样部署模拟集群，使用 Kubernetes [集群自动扩展器](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/clusterapi/README.md)。该软件使用户能够在所有主要云服务提供商中供应和取消供应节点，尽管它还提供了通过自定义接口执行此操作的能力。Morrison 构建了 sk-cloudprov 来模拟基于 gRPC 的云服务提供商，尽管在现实中，它只是将请求分发给 sk-vnodes，而 sk-vnodes 则在模拟集群上部署虚拟节点。

## 假想追踪

目前，您可以在 SimKube 上重播结果，并在 [Grafana 和 Prometheus](https://thenewstack.io/why-grafana-needs-opentelemetry/) 上再次观看它的展开，

但是除了重新运行实际事件的追踪外，该技术还可以为回答假设场景奠定基础。可以修改追踪对象，甚至可以从头开始创建。可以在模拟集群中应用假设追踪，来回答诸如“如果我们有一个扩展到 10，000 个 pod 的部署，会怎样？”这样的问题。

“这可能是一个非常强大的事情，”Morrison说。

## 更多 Kubernetes 模拟

![](https://cdn.thenewstack.io/media/cbf9f47c-kwok.svg)

*KWOK 是 Kubernetes Without Kubelet 的缩写。*

SimKube 不是这个城市里唯一的 Kubernetes 模拟器。在 KubeCon 上，苹果的两名研究人员还[讨论了一个类似的项目](https://www.youtube.com/watch?v=3YH_2vqWAzQ&t=925s)，名为 [KWOK](https://kwok.sigs.k8s.io/)，即 Kubernetes Without Kubelet 的缩写。

KWOK“是一个工具包，可以在几秒钟内建立一个具有数千个节点的集群。在场景下，所有节点都被模拟为像真实节点一样行为，因此整体方法采用了非常低的资源占用，您可以轻松地在笔记本电脑上运行”，文档如是解释。

[Kubemark](https://github.com/kubernetes/kubernetes/tree/master/test/kubemark)、[Virtual Kubelet](https://virtual-kubelet.io/) 和 [KCP](https://www.kcp.io/)(Kubernetes 控制平面)是沿这条线的其他工作。

“所以这里有大量重复的工作。让我们停止重复所有这些东西，专注于一件事”，Morrison说，并补充说他希望 SimKube 可以成为这项工作的一部分。
