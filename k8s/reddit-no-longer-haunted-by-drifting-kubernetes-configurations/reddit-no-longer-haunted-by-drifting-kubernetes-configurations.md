
<!--
title: Reddit不再受漂移的Kubernetes配置困扰
cover: https://cdn.thenewstack.io/media/2025/01/ec2bcf77-reddit.png
-->

三年前，Reddit的基础设施工程师团队大部分时间都在忙于灭火。以下是他们如何开发平台抽象来简化操作并重新掌控局面的。

> 译自 [Reddit No Longer Haunted by Drifting Kubernetes Configurations](https://thenewstack.io/reddit-no-longer-haunted-by-drifting-kubernetes-configurations/)，作者 Joab Jackson。

当Reddit于2022年3月13日宕机时，它粗暴地提醒该公司需要以不同的方式管理其基础设施。

臭名昭著的[“圆周率日”全站宕机](https://www.reddit.com/r/RedditEng/comments/11xx5o0/you_broke_reddit_the_piday_outage/)，巧合的是，[持续了314分钟](https://thenewstack.io/how-the-world-celebrated-pi-day/)，源于从[Kubernetes 1.23升级到1.24](https://thenewstack.io/kubernetes-1-24-drops-dockershim-makes-space-for-stateful-workloads/)的集群范围升级，这导致了一些细微的不可预测行为，迫使基础设施团队进行回滚，这本身就是一个高风险操作。

即便如此，公司工程师也知道需要改变运营方式。

这个广受欢迎的社交新闻论坛正在扩展其服务器堆栈以跨多个区域工作，以提高可靠性，目标是在全球范围内提供服务。围绕广告投放和机器学习的其他举措也带来了自身的挑战。此外，公司高管正在准备IPO。

公司需要一个新的平台抽象，Reddit基础设施团队的高级软件工程师提到。随着公司的发展，他们需要新的平台抽象才能继续高效地运营。

和Reddit软件工程师一起，在最近的KubeCon+CloudNativeCon北美会议上，基础设施团队介绍了如何创建一个新的平台抽象，以便在规划上领先，并摆脱反应式、灭火模式。

“从技术上讲，我们能够用更少的人解决更具挑战性的问题，”说。“由于我们在过去几年中投入了大量资金，这使得我们能够投入更多专门的工程时间来主动解决问题，而不是被动地灭火。”

## 神秘的命名空间

2022年，该公司运行着20个Kubernetes驱动的生产集群。基础设施团队有92名工程师，远少于公司部署的706名应用工程师。他们的工作大部分是帮助应用工程师。

一个问题是命名空间的创建。在Reddit中，每个在Kubernetes上运行的应用程序都需要一个[命名空间](https://thenewstack.io/leveraging-namespaces-for-cost-optimization-with-kubernetes/)，这可以通过[Helm chart](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/)或[Kustomize manifest](https://github.com/kubernetes-sigs/kustomize)指定。应用程序开发者并不是编写这些规范的专家。

这导致了大量的复制粘贴。结果，错误潜入其中，并不总是被审阅者发现。审查过程为应用程序审查过程增加了额外24小时。

由于时区差异，仅仅为了获得命名空间，可能需要将近整整一周的时间。而且糟糕的配置设置仍然渗透到整个[持续集成](https://thenewstack.io/ci-cd/)过程中，这可能导致停机。

Reddit对命名空间的管理并不一致。“我们无法判断命名空间的来源，也不知道它是否正在被使用，”说。正因为如此，公司制定了一条规则，不删除任何命名空间，因为工程师无法判断某个命名空间是否仍在某个地方被使用。

所有过时的命名空间——随着公司将其单体应用程序迁移到微服务，其中有很多——仍然占用Kubernetes资源。

## 手工打造的集群和“闹鬼”的基础设施

与此同时，基础设施团队也有其自身的挑战。

工程师需要30多个小时才能启动一个集群，包括100多个步骤，包括配置网络、配置硬件或选择云供应商、安装控制平面以及添加可观察性和自动缩放工具。

此外，集群的原地升级非常危险，正如圆周率日所说明的那样，而且根本没有停用集群的流程。仍在工作的集群的配置已经发生漂移，并以未记录的方式变得定制化。

停用集群相当于“昂贵的考古学搜寻，以找到所有必须停用的不同基础设施”，说。

> “这是一个自我强化的低效循环”——Reddit的Harvey Xia

“任何工程师都很难自信地推断集群的行为方式，或者它实际的行为方式，这使得所有生命周期操作都极其危险，”Xia说。

因此，基础设施团队的大部分时间都花在了维持一切正常运行和修复故障上。

Xia说，这种“被动式、救火式的心态”使得很难“设想、规划或构建更可持续的未来”。

## Reddit 为什么选择 K8s 控制器而不是 IaC

抽象通过将用户的关注点与底层实现分离来隐藏复杂性。根据 Xia 的定义，平台是由开发人员可以构建的组合工具组成的生态系统。它遵循公司开发人员的最佳实践。

Reddit 决定通过一组由 Kubernetes 控制流程支持的声明式 API 来实现平台。接口定义为自定义资源。期望状态是规范，观察到的状态通过状态报告。

自定义资源驱动 Kubernetes 控制器，这些控制器通过将活动状态更改为期望状态来实现其 API。

工程师最初考虑过[Infrastructure as Code](https://thenewstack.io/infrastructure-as-code/) 工具，但随后改用基于 Kubernetes 控制器的工具。

使用标准 IaC，很难表示任意的业务逻辑，这是构建 Reddit 基础设施的主要要求。

“我无法模拟一个工作流程，在这个工作流程中，我从证书颁发机构配置 TLS 证书，将其卸载到 Amazon 证书管理器，并将其附加到负载均衡器，”Xia 说。标准 IaC 平台也不是动态的。您不能依赖 IaC 来更新失效的证书。

![](https://cdn.thenewstack.io/media/2025/01/3d614d20-kubecon-reddit-infra-01.png)

相比之下，Kubernetes 控制器将确保当前状态始终处于或至少始终朝着期望状态移动。这将包括所有生命周期操作。

## 脑和工作负载集群

如今，Reddit 基础设施工程师花费在管理集群上的时间更少了。他们有一组 API 可以通过“单一窗口”管理多个集群。

![](https://cdn.thenewstack.io/media/2025/01/dad96262-kubecon-reddit-infra-02.png)

公司有两种类型的集群。一个是控制集群，可以认为是操作的大脑。它为其他易于替换的“工作负载”集群生成配置。

“我们开始将这些集群视为牲畜，而不是宠物，”Thukral 说。

这样，集群具有明确定义的属性，所有适用的配置更新都会自动流入该集群。可以执行多集群操作。

每个工作负载集群都有其自己的自定义资源，其中包含其操作阶段（测试、生产或暂存）、地理位置和后端云供应商等属性的标签。这为多集群 API 控制奠定了基础。联合控制器通过 K8s 标签选择器管理集群。

集群目标是动态的。如果启动新的测试集群，它会自动加入测试命名空间。

“这为我们的工程师节省了大量时间，”Xia 说。

这种方法也有一些潜在的缺点。首先，编排集群是单点故障。但是该系统的设计使得即使无法更新工作集群，它们也可以继续运行和自我修复。限制可以启动的集群类型也会限制可以构建的集群种类，从而使它们更容易管理。

[FluxCD](https://thenewstack.io/deploy-stateful-workloads-on-kubernetes-with-ondat-and-fluxcd/) 用于将源配置与集群同步。[Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/) 用于将 Kubernetes API 桥接到云供应商资源。而[Cluster API](https://thenewstack.io/is-cluster-api-really-the-future-of-kubernetes-deployment/) 提供了管理 Kubernetes 控制平面的 API。

Reddit 公司自己的自定义资源对这些资源或基础原语进行了中介，允许公司根据需要交换实现。

命名空间的创建也变得更容易了。现在，Reddit 应用开发人员无需学习 Helm 或 Kustomize，只需创建一个名为 Reddit Namespace 的自定义资源，并将其定向到一组集群即可。对于用户而言，基于角色的访问控制 (RBAC) 简化为两个选项：操作员或读取器状态。

## 没有阿喀琉斯之踵

为了帮助基础设施工程师更轻松地创建控制器和操作器，Reddit 构建了[Achilles SDK](https://github.com/reddit/achilles-sdk)，它构建在 Kubernetes 控制器运行时之上。

![](https://cdn.thenewstack.io/media/2025/01/a4e111d3-kubecon-reddit-infra-03.png)

Thukral 说，这个 SDK 将整个协调循环表示为一个有限状态机。目前，这是由单个函数处理的，这可能会变得相当笨拙。Thukral 说，用 Achilles 构建的集群比在 Terraform 下组装的相同集群所需的步骤少得多。

阿喀琉斯（Achilles）会自动跟踪所有子资源和状态条件。

“我们希望让我们的基础设施工程师能够专注于构建业务逻辑，而无需成为Kubernetes专家，”Thukral说。

## 结果

Reddit 仍在构建新基础设施的过程中，不过该公司已经看到了成果，工程师们自豪地表示。

该平台的可扩展性大大增强：再也不用为命名空间的编写和管理而头疼。在安全性和应用堆栈的简化方面也取得了进步。

如今，搭建一个新的集群大约需要两个小时。升级可以在一个小时内完成。多亏了 Achilles，一个控制器的创建和测试可以在不到两周的时间内完成，“对我们来说这是一个巨大的成功”，Thukral 说。

该公司年初时在生产环境中拥有4个Kubernetes控制器，截至KubeCon，公司已有12个。这些控制器管理着基础设施的诸多方面，包括Kubernetes Ingress堆栈、AWS网络、Redis、Cassandra、HashiCorp Vault以及Kubernetes本身。

“对平台抽象的投资已经得到了回报，”夏说，“自助服务接口已经取代了我们以前大部分的专属服务流程。许多繁重的内部工作流程已被自动化所取代。”

在这次演讲中，Xia 还提供了一些关于何时自动化工作流程的建议。

第一步：一切都必须可编程。他说，该平台使工程师能够专注于那些“我们想要花时间解决的有影响力的问题”。

您可以在此处查看整个演讲：[https://youtu.be/ruto5Sak-jI](https://youtu.be/ruto5Sak-jI)。