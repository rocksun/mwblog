
<!--
title: Kubernetes 集群存在大量的计算和内存过度配置
cover: http://www.nextplatform.com/wp-content/uploads/2020/02/ab_container-port-scaled.jpg
-->

自 Google 向开源社区发布 Kubernetes 的十年以来，它已成为编排和管理的领先平台

> 译自 [Kubernetes Clusters Have Massive Overprovisioning Of Compute And Memory](https://www.nextplatform.com/2024/03/04/kubernetes-clusters-have-massive-overprovisioning-of-compute-and-memory/)，作者 Jeffrey Burt。

自 Google 向开源社区发布 [Kubernetes](https://www.nextplatform.com/2022/03/15/teaching-kubernetes-to-do-fractions-and-multiplication-on-gpus/) 十年来，它已成为编排和管理软件容器和微服务的首选平台，同时击败了 Docker Swarm 和 Mesosphere 等竞争对手。（还记得它们吗？十年后，你将不会记得。）

构建软件堆栈的公司采用了 Kubernetes 来创建自己的容器平台，例如 Red Hat 的 OpenShift 和 VMware 的 Tanzu，几乎每个云服务提供商都在其众多服务下方提供 Kubernetes，并且速度非常快。

如今，根据云原生计算基金会的数据，超过 560 万开发人员使用 Kubernetes，它占据了容器编排工具领域的 92% 份额。Kubernetes 非常强大。Cast AI 的联合创始人兼首席产品官 Laurent Gil 表示，Cast AI 是一家初创公司，其基于人工智能的自动化平台旨在帮助组织优化其 Kubernetes 使用，Kubernetes 和容器对于软件开发人员和 DevOps 工程师在日益分布和加速的 IT 世界中至关重要。

“将 Kubernetes 视为一个出色的工具箱，”Gil 告诉 *The Next Platform*。“我们过去拥有单体应用程序。Kubernetes 的好处是你可以将应用程序分解成更小的部分，好处在于某些部分可以复制，因此你可以轻松扩展。想象一下你是 Netflix——他们实际上使用了 Kubernetes——并且有数百万人同时涌入并观看。如果你使用 Kubernetes，你可以无限复制这些容器，以便处理这种流量。容器非常适合这种情况。你可以扩展它。它几乎就是以这种方式设计的。”

也就是说，开发人员在云中使用 Kubernetes 时会遇到挑战，其中一个关键挑战是为应用程序配置 CPU 和内存。去年，这家成立五年的公司考察了开发人员和 DevOps 人员预测 Kubernetes 应用程序所需的 IT 资源量的能力，发现结果并不好。

Gil 表示，开发人员通常请求的计算和内存远多于他们实际需要的，导致大量超支。2022 年，请求的 CPU 和配置的 CPU 之间存在很大的差距——37%，该公司发现去年这一差距进一步扩大至 43%。这是基于开发人员的想法的超额配置量。

“这意味着在一年内，浪费实际上增加了，而不是减少了，”他说。“现在应该已经很清楚了。如果你需要两个 CPU，只需配置两个。不要配置三个。但它比去年更糟。”

## 平均 CPU 使用率为 13%

Cast AI 研究人员还考察了开发人员实际使用了多少配置的 CPU。平均而言，该数字为 13%。他们希望了解在更大的集群中这些数字是否更好，但在拥有 1,000 个或更多 CPU 的集群中，CPU 利用率仅达到 17%。

拥有 30,000 个或更多 CPU 的集群达到了 44% 的利用率，但仅占他们考察的系统的 1%。

所有这些都表明 CPU 大量超额配置，大部分计算能力处于闲置状态。

“我预期结果不会很好，但我没想到会这么糟糕，”他说。“平均而言，你超额配置了 8 倍。真正使用的那一个。在 100 台机器中——CPU 是 Kubernetes 中最昂贵的组件——你只使用了 13 台。平均而言，你没有使用其余的。如果你有 100 台机器，它们都被使用了，但每台只使用了 13%。Kubernetes 就像房间里的气体。它会填满空间。如果你有一个在该机器上运行的应用程序，它们都会被使用。它们只会以 13% 的利用率被使用。”

![](https://www.nextplatform.com/wp-content/uploads/2024/03/cast-ai-aws-spot-pricing.jpg)

对于 [2024 Kubernetes 成本基准报告](https://cast.ai/kubernetes-cost-benchmark/)，Cast AI 考察了在去年 1 月 1 日至 12 月 31 日期间在 AWS、Azure 和 Google Cloud Platform 上运行的 4,000 个集群，然后使用供应商的平台对其进行了优化。他们排除了 CPU 少于 50 个的集群以进行分析。

考察的另一个领域：各个云托管 Kubernetes 平台上的利用率。在 AWS 上的 Elastic Kubernetes Services (EKS) 和 Microsoft Azure 上的 Kubernetes Service (AKS) 上，利用率徘徊在 11% 左右，而在 Google Cloud 的 Google Kubernetes Engine (GKE) 上，利用率更好，为 17%。GKE 上的集群往往比其他两个集群更大，并且该服务提供自定义实例。

谷歌是 Kubernetes 的源头，它可能拥有精通的用户，并且可以这样翻译，“Gil 说。“但你知道吗？坦率地说，即使是 17% 也不算好。它仍然是超额配置的五倍以上。想想看：你去找你的 CTO，你说，‘你知道吗？你可以将你的云成本降低五倍，因为你实际上不需要那么多。’”

## 内存利用率并没有好多少

Cast AI 还研究了内存使用情况，注意到平均而言，内存使用率为 20%。然而，内存比 CPU 便宜，因此如果 CPU 利用率更高会更好，Gil 说。但事实并非如此。

“人们更多地关注内存，从本质上讲，随着他们更多地关注，他们做得更好，”他说。“他们更多地关注内存，因为当容器内存不足时，容器会停止并重新启动。CPU 是弹性的。你可以从 0% 到 80%。它总是有空间。内存，你不能超过 100。如果你超过 100，它就会崩溃。它被称为‘内存不足。OOM’。这是 DevOps 和 Kubernetes 最害怕的问题。他们更多地关注内存，因此它略好一些，但平均而言仍然是五倍太多。”

云平台之间没有太大差异，Azure 的内存利用率最高，为 22%，其次是 AWS 的 20% 和 Google Cloud 的 18%。

研究人员在报告中写道，随着企业准备增加对云服务的支出，他们需要解决这一利用率问题。今年全球最终用户在公共云服务上的支出
[预计将达到 6788 亿美元](https://www.gartner.com/en/newsroom/press-releases/11-13-2023-gartner-forecasts-worldwide-public-cloud-end-user-spending-to-reach-679-billion-in-20240)，比 2023 年的 5636 亿美元增长 20.4%。

即使是 AWS 在其最受欢迎的美国地区的 Spot 实例定价，在 2022 年 8 月至 2023 年期间也平均上涨了 23%。

十年前，许多积极进军云计算的组织惊讶地发现成本开始累积，这些成本与数据主权和监管问题一起成为过去几年数据回流背后的主要驱动力。Gil 说，提高资源利用率会有所帮助。

## 将人从等式中剔除

他说，问题在于确定所需的资源仍然是一个高度手动化的过程。开发人员不知道他们的应用程序或集群需要什么，因为他们还没有看到它的规模。Gil 说，很难猜测微服务需要什么资源，并补充说，随着 Kubernetes 变得更加复杂，这并不会变得更容易。

“我们称这是一个非线性问题，你必须实时调整许多小变量，每个变量都会影响其他变量，”他说。“这不仅仅是你只使用了其中的 10%，而是你可能没有使用正确的变量。这就是人类过度配置的原因。他们知道这是不对的。但出于某种原因，他们不知道该怎么做。”

越来越多的供应商提供自动化工具和平台来改善云中的资源优化。阵容包括像
[思科系统](https://www.nextplatform.com/2022/03/24/cisco-rolls-out-new-systems-as-it-pushes-its-own-kubernetes-stack/) 这样的老牌厂商，以及 AppDynamics、Nutanix、Apptio、VMware 和 Flexera。Cast AI 吹嘘其平台使用 AI 技术可以为组织节省 50% 或更多的云成本。2023 年 11 月，该公司获得了财务支持，[筹集了 3500 万美元](https://cast.ai/press-release/series-b-announcement/) 的 B 轮融资，使筹集的总金额达到 7300 万美元。
