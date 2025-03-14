
<!--
title: 轻松扩展至10,000个Kubernetes集群
cover: https://cdn.thenewstack.io/media/2024/10/8fb30933-datacenter2.jpg
-->

客户询问Spectro Cloud其Palette平台能否处理其海量规模。该公司着手对此进行测试。

> 译自 [Scaling to 10,000 Kubernetes Clusters Without Missing a Beat](https://thenewstack.io/scaling-to-10000-kubernetes-clusters-without-missing-a-beat/)，作者 Romain Decker。

谈到Kubernetes的扩展，我们自然会想到在集群内进行向上或向下扩展，无论是手动操作还是使用众多自动缩放器类型之一（顺便说一句，我们[有一篇博文对此进行了介绍](https://www.spectrocloud.com/blog/kubernetes-autoscaling-patterns-hpa-vpa-and-keda)）。

但还有一种越来越常见的扩展方式：扩展您拥有的集群数量。

我们的年度研究发现，使用[Kubernetes](https://thenewstack.io/kubernetes/)的典型企业现在拥有超过20个集群；6%的企业拥有超过100个集群。

而且数量肯定不止几百个。据[这份CNCF案例研究](https://www.cncf.io/case-studies/mercedes-benz/)显示，众所周知，梅赛德斯-奔驰在2023年运行了近1000个Kubernetes集群。

[边缘用例](https://thenewstack.io/the-challenge-of-scaling-the-intelligent-edge/)使数量更高：我们的一个客户Dentsply Sirona在[数千家牙科诊所](https://kccnceu2024.sched.com/event/1YeS4)中使用Kubernetes。
[选择运行大量集群的原因有很多](https://www.spectrocloud.com/blog/why-you-need-kubernetes-multi-cluster-management)——不仅仅是将开发/测试与生产环境分开，还包括支持多云Kubernetes策略、多区域部署和应用程序隔离（爆炸半径），以及安全和合规性需求。

## 大量集群……新的瓶颈？

如果您运行数十、数百或数千个Kubernetes集群，您可能已经采用了[Kubernetes管理平台](https://www.spectrocloud.com/blog/what-is-an-enterprise-kubernetes-management-platform)来集中和自动化集群的部署和操作方式。

而这正是事情变得非常有趣的地方，因为大多数Kubernetes管理平台根本就不是为有效扩展而设计的。

![](https://cdn.thenewstack.io/media/2024/10/c6aad8b6-image1-1024x1024.png)

一旦超过40或50个集群，管理平台本身就会成为瓶颈。在每秒的API调用和新指令的负载下，其性能会下降。

最终会出现错误、超时以及Web界面和API无响应的情况。平台本身可能会出现停机，导致您不得不争分夺秒地扩展其资源或恢复它——与此同时，您将无法构建新集群或对现有集群进行更改。

我们是怎么知道的？因为我们的客户多次向我们展示并告诉我们，当他们与供应商完成最初的概念验证后，事情很快就会崩溃。在某些情况下，我们自己也测试了这些平台，并发现它们在负载下难以运行。

## 供应商怎么说？

这些平台供应商（如果他们承认这个限制的话）通常提供的指导是运行管理平台的多个实例，例如每个区域、每个环境或每组集群一个实例。

例如，Kubermatic建议[建议](https://docs.kubermatic.com/kubermatic/v2.26/architecture/)“对于大规模部署，建议使用多个专用种子集群，而不是在单个集群中运行KKP主组件和种子组件”。

在[冗长的扩展指南](https://ranchermanager.docs.rancher.com/reference-guides/best-practices/rancher-server/tuning-and-best-practices-for-rancher-at-scale)中，Rancher指出了其“上游集群”的计算瓶颈：“扩展Rancher时，一个典型的瓶颈是上游（本地）Kubernetes集群中的资源增长。上游集群包含所有下游集群的信息。许多应用于下游集群的操作会在上游集群中创建新对象，并需要上游集群中运行的处理程序进行计算。”

我们认为，这种架构上的变通方法违背了集中式管理平台的初衷。当您拥有多个管理服务器时，您将不再拥有单一视图体验，更不用说您引入的复杂性了。当您达到边缘规模时，这根本不可行。

## 10,000个集群。我们能胜任吗？

最近，一位客户向我们提出了一个挑战：他们目前的管理平台供应商（顺便说一句，并非我们刚才提到的两个供应商之一）难以扩展到几百个集群。

这是一个问题，因为客户希望将边缘Kubernetes部署到10,000个零售场所。

由于之前有过不好的经验，他们问我们：Palette真的能像我们需要的这样扩展吗？

## 第一个要素：正确的架构

Palette 的架构专门针对这种超大规模场景而设计。我们采用了一种[去中心化架构](https://www.spectrocloud.com/product/decentralized-architecture)，将计算负担放在每个本地集群中运行的智能代理上，而不是依赖单一的管理平面来执行工作。

Palette 管理平面的主要多租户 SaaS 部署已经轻松运行超过 1400 个集群（许多客户拥有自己的专用实例或自行托管 Palette 软件，因此他们自然不计入主实例的总压力测试）。

但这距离 10000 个目标还有很长的路要走。我们如何证明 Palette 可以扩展到这种程度？

## 隆重介绍 Spectro Cloud 的性能实践

![](https://cdn.thenewstack.io/media/2024/10/2523782e-image3-1024x485.png)

性能和可扩展性对我们至关重要，因此我们大力投资建立了性能实践：一套流程，使我们能够在负载下分析系统行为，从而能够突破 Palette 的性能极限，持续优化，然后验证积极的影响。

这样，客户可以充满信心地进行扩展，因为我们的最大数字不仅仅是美好的愿望或营销夸大其词。

我们还使用性能测试来提高产品效率，并验证系统在不同负载条件下的可靠性和稳定性。通过模拟现实场景和对系统进行大规模压力测试，我们可以识别和解决潜在的瓶颈，确保平台即使在高峰使用期间也能保持稳定和响应迅速。

为了应对客户提出的 10000 个集群的挑战，我们启动了一个新的性能测试模拟。

我们建立了一个专用的 Palette SaaS 实例，与我们的客户使用的实例相同。这一点很重要：我们没有为了性能而调整管理平面，Palette 也不知道它正在接受测试。我们没有操纵实验。

接下来，我们需要 10000 个三节点集群，以及至少 30000 台机器来构成我们的边缘 Kubernetes 主机并运行本地 Palette 代理。

不幸的是，我们的 CFO 不会批准购买一仓库的新服务器，因此我们创建了一个合成环境。为此，我们创建了两个框架。

- **一个内部开发的性能测试框架，** 一个具有端点的 API 服务，用于在配置的环境中创建租户、项目、边缘主机和集群。它精确地模拟了完整的集群生命周期，并执行真实代理将对 Palette 发出的所有 API 调用，发送有关事件、机器健康状况、心跳和包状态的数据。
- **一个基于[K6](https://k6.io/)的负载生成和指标捕获框架，** 并进行了额外的自定义开发和扩展。这将生成负载、捕获指标和测试负载规范所需的测试数据。我们可以指定并发虚拟用户的数量以及许多其他选项，并查看对 Palette 物理资源和性能的影响。

框架中的所有内容都是可配置的，允许我们测试和验证许多场景，并且总体而言，模拟代理的行为与安装在生产集群中的真实[Palette 边缘和集群代理](https://thenewstack.io/virtual-kubernetes-clusters-with-spectro-cloud-palette/)完全相同。

![如果在 PowerPoint 中疯狂操作，这就是 1000 个边缘节点的样子。](https://cdn.thenewstack.io/media/2024/10/47e0ecf1-image4-1024x599.png)

*如果在 PowerPoint 中疯狂操作，这就是 1000 个边缘节点的样子。*

使用此设置，我们逐步增加模拟数量，直到模拟 10000 个集群和 36000 个边缘节点，所有这些都由单个 Palette 实例管理，并可从单个用户界面访问。

我们的测试套件监控 Palette 组件的稳定性、API（也为我们的 UI 提供支持）的响应速度以及执行标准操作时 UI 体验的性能。在测试过程的每个步骤中，我们的工程和质量保证团队也进行了人工验证。

## 以优异的成绩通过

结果非常清晰。UI 和 API 保持响应迅速。我们没有遇到性能下降、不稳定、停机、奇怪的错误或瓶颈。

事实上，我们没有看到任何迹象表明我们甚至接近 Palette 在 10000 个集群时的扩展限制。我们只停在那里，因为那是客户为我们设定的目标。

从下面的屏幕截图可以看出，为了达到这个规模，我们不必投入大量的硬件。我们的 Mongo 数据库服务器是具有 16 个内核的 CPU，内存为 64 GB。

![](https://cdn.thenewstack.io/media/2024/10/680d95ff-image2-1024x754.png)

观看下面的视频，快速了解 Palette 界面的实时、未经编辑的浏览过程，您可以在其中看到我们导航集群、过滤、深入分析、切换项目以及执行其他正常操作，并且具有完全的响应能力。

## 你明年将运行多少个集群？

如果您的 Kubernetes 环境有可能扩展到数百或数千个集群，那么您肯定会在使用多集群管理平台——并且您现在需要考虑该平台是否能够与您一起扩展。

Palette 从第一天起就针对极大规模进行了架构设计，并且我们建立了强大的性能实践，使我们能够快速测试任何场景并持续优化我们的平台。

因此，当我们回到客户那里，现场演示 Palette 运行 10k 个三节点集群，毫不费力时，他们都惊呆了。

因此，如果您考虑规模问题，请让我们接受考验。[请求演示](https://www.spectrocloud.com/get-started)，告诉我们您有多少个集群，我们将演示 Palette 支持您的集群环境。
