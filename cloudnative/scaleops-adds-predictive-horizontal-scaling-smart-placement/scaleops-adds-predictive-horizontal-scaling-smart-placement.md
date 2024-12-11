
<!--
title: ScaleOps 添加预测式水平扩展和智能部署
cover: https://cdn.thenewstack.io/media/2024/12/a4fa2d88-toggles.jpg
-->

利用AI，系统可以学习容器的正常行为，并预测流量高峰的出现时间，从而实时自动扩展。

> 译自 [ScaleOps Adds Predictive Horizontal Scaling, Smart Placement](https://thenewstack.io/scaleops-adds-predictive-horizontal-scaling-smart-placement/)，作者 Susan Hall。

以色列初创公司ScaleOps在其产品中增加了水平扩展和其他功能，以[在运行时动态分配容器资源](https://thenewstack.io/scaleops-dynamically-right-sizes-containers-at-runtime/)。

其预测式水平Pod自动伸缩功能使用AI预测应用程序负载以实时扩展。

“如今的问题之一是，一旦需要为应用程序进行水平扩展，并且需要更多副本以处理负载，问题在于应用程序进行水平扩展需要很长时间……我们预测并提前扩展，然后当负载真正到来时，您已经拥有了运行所需的副本数量，它们可以处理不断变化的需求，”ScaleOps联合创始人兼首席执行官Yodar Shafrir在一次采访中表示。

该公司表示，通过提供具有[集群和每个应用程序需求的整体视图](https://thenewstack.io/why-kubernetes-cluster-management-needs-to-be-easier-for-developers/)的上下文感知平台，它可以消除开发团队和DevOps团队之间关于实时资源分配的摩擦。

“我们意识到市场上没有人解决这个问题；他们只是提供可见性并让人们意识到这个问题。资源分配过程仍然完全中断，”Shafrir在公告中表示。

该系统使用AI和机器学习，可以从前一周或前一个月确定[容器](https://thenewstack.io/containers/)的正常行为，并预测流量峰值何时发生以及相应地进行扩展。

它与其他自动伸缩器集成，例如开源[Karpenter](https://thenewstack.io/how-aws-supports-open-source-work-in-the-kubernetes-universe/)、集群自动伸缩器、水平Pod自动伸缩器(HPA)或[Keda](https://thenewstack.io/kubernetes-autoscaling-keda-moves-into-cncf-incubation/)，以确定每个工作负载的最佳副本数量。

它还宣布了智能Pod部署功能，该功能通过考虑应用程序约束和集群状态来优化资源分配，从而减少所需的活动节点数量。

“如今在集群中运行的一些Pod有一些限制[这]可能会阻止节点缩容。通常，这适用于无法抢占且无法容忍节点缩容的工作负载，”Shafrir解释道。

“那么公司会怎么做呢？他们添加注释来告诉Kubernetes集群永远不要缩容Pod当前正在运行的节点。我们了解每个应用程序的需求和所有限制，并且我们也拥有整个集群的整体视图，因此我们确保所有具有此限制的Pod都将调度到相同的节点上。这样，这些节点将保持静态，并且无法缩容，但集群的其余部分将更加动态，然后您可以在需要时缩容节点。”

该公司认为，实时预测式扩展和智能Pod部署相结合可以为组织节省50%的云成本并提高应用程序性能。

第三个新功能是一组仪表板，可帮助工程团队快速分析和了解问题的根本原因，然后相应地管理工作负载。

ScaleOps可在任何Kubernetes环境中运行，包括主要的云平台，如[AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure和[Google](https://cloud.google.com/?utm_content=inline+mention) Cloud，以及本地和隔离服务器。

ScaleOps成立于2022年，总部位于特拉维夫，最近宣布获得B轮融资5800万美元，使公司总融资额达到8000万美元。

“今天，我们主要关注生产和预发布用例，我们将扩展到传统资源，包括网络、存储、GPU，以及我们今天正在使用的计算和内存，”Shafrir表示。
