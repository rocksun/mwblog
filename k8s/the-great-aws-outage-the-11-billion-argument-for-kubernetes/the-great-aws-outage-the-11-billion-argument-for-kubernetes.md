
<!--
title: AWS惊天大宕机：110亿天价警示，力推Kubernetes！
cover: https://cdn.thenewstack.io/media/2025/10/063031b0-kubernetes.jpg
summary: 文章回顾2025年AWS大规模中断，强调单一云脆弱性。多云虽好但复杂，Kubernetes作为抽象层提供真正的可移植性和弹性，并提升开发者生产力。
-->

文章回顾2025年AWS大规模中断，强调单一云脆弱性。多云虽好但复杂，Kubernetes作为抽象层提供真正的可移植性和弹性，并提升开发者生产力。

> 译自：[The Great AWS Outage: The $11 Billion Argument for Kubernetes](https://thenewstack.io/the-great-aws-outage-the-11-billion-argument-for-kubernetes/)
> 
> 作者：Arjun Iyer

嗯，那真是糟糕的一周。

如果你在科技行业，你肯定知道我说的是哪一周。那是2025年10月声势浩大的 [AWS](https://aws.amazon.com/?utm_content=inline+mention) us-east-1 大规模中断。当警报开始响起时，你在哪里？

我正在进行演示，突然，一切都停止工作了。我们的应用程序、我们的认证、我们的 CI/CD 流水线，全都失效了。那是一个数字鬼城。八个小时里，互联网的很大一部分——从流媒体服务和电子商务网站，到令人恐惧的金融和医疗保健平台——就这么凭空消失了。

随后的几天和几周里，事后分析报告纷纷出炉。[Tom’s Guide](https://www.tomsguide.com/news/live/amazon-outage-october-2025) 等出版物记录了这次巨大的、连锁性的影响，而 [福布斯](https://www.forbes.com/sites/christerholloman/2025/10/20/aws-outage-billions-lost-multi-cloud-is-wall-streets-solution/) 则一直在统计损失。目前的估计是多少？超过110亿美元的收入损失和市值蒸发。

一百一十亿。美元。

跟风指责 AWS 很容易。但老实说，在这种规模下进行工程设计是极其困难的。故障总会发生。

现在尘埃落定，我们需要问自己一个真正令人不安的问题：我们为何如此脆弱？

## **单一云的诱惑**

十年来，公共云一直是一个令人难以置信的加速器。我们用资本支出换取了运营支出，作为回报，我们获得了按需计算、存储以及丰富的托管服务生态系统。这是一笔划算的交易。

但我们也变得安逸了。我们围绕一个提供商的专有 API 构建了我们的整个系统和业务。我们基于 DynamoDB 构建，使用 Lambda 作为函数，并通过身份和访问管理 (IAM) 将一切连接起来。它速度快，功能强大，但也像一颗定时炸弹。

十月的大规模中断不仅仅是一次服务故障；它是控制平面的故障。当身份服务崩溃时，整个纸牌屋都倒塌了。它暴露了我们思维中的根本缺陷：我们在一个单一的、巨大的故障点之上构建了极其弹性的应用程序。

福布斯文章指出，华尔街现在最喜欢用的词是“多云”。他们没错。例如，那些在 AWS 和 Google Cloud Platform (GCP) 上拥有 active-active 设置的公司，当时发推文说的是“我们正在经历一些小问题”，而不是“我们彻底瘫痪了”。

但对我们大多数人来说，“直接上多云”是一个糟糕、简单且极其昂贵的建议。

## **为什么“多云”是一个陷阱（通常情况下）**

如果你对这次中断的应对之策是让你的团队也学习 [Google](https://cloud.google.com/?utm_content=inline+mention) 的 IAM、Azure 的 Active Directory 以及他们所有不同的托管数据库服务的细节……祝你好运。

真正的多云很难。它不仅仅是在两个地方运行几台虚拟机 (VMs)。它还包括：

*   **不同的 API：** 在 AWS 中配置负载均衡器的方式与在 GCP 中完全不同。
*   **不同的服务：** 并非每个托管服务都有 1:1 的对应物。你最终会为最低的共同点构建，或者更糟的是，构建两个（或三个）完全独立的堆栈。
*   **不同的工具：** 你的 `boto3` 脚本在 Azure 中毫无用处。你的整个 CI/CD 和可观测性堆栈可能需要复制或重新架构。

这种方法不仅使你的基础设施成本翻倍；它还使你的认知负荷翻倍。你需要在两个完全陌生的生态系统中交付功能、管理可靠性并解决问题。

多年来，这种复杂性是获得真正弹性的门槛。我们大多数人理所当然地选择不支付。

但是，如果这个门槛成本突然降为零呢？如果我们一直因为其他原因而采用的平台，恰恰就是关键所在呢？

## **Kubernetes 作为伟大的抽象层**

这就是 Kubernetes (K8s) 改变游戏规则的地方。

对于许多人来说，K8s 只是一个“容器编排器”。它是你用来运行微服务的工具。但这种描述是只见树木不见森林。

Kubernetes 是一个为你的整个应用程序提供的一致的、云无关的 API。

想想看。无论你将其提交到运行在 Elastic Kubernetes Service (AWS)、Google Kubernetes Engine 还是 Azure Kubernetes Service 上的集群，Kubernetes 的 `Deployment.yaml` 都看起来一模一样。一个 `Service` 对象抽象了底层的云负载均衡器。一个 `PersistentVolumeClaim` 抽象了底层的存储类（Amazon Elastic Block Store、Google Persistent Disk 等）。

K8s 是我们一直缺少的那一层抽象。它是云的“操作系统”。

当你的应用程序只“讲”Kubernetes 时，你就不再受限于云提供商的专有 API。你被锁定在一个无处不在的开源标准中。

这使得多云的梦想成为切实的现实：

1.  **真正的可移植性：** 容器镜像就是容器镜像。你的应用程序，以容器形式打包，将在你的笔记本电脑、AWS us-east-1 集群和 GCP europe-west-2 集群中完全一致地运行。
2.  **基础设施即数据：** 你的应用程序的整个期望状态只是一组 YAML 或 JSON 文件。将你的 Argo CD 或 Flux (GitOps) 流水线指向一个新区域——或一个不同云上的新空集群——轻而易举。
3.  **联邦与故障转移：** 借助现代工具，你可以将一组集群作为一个逻辑单元进行管理。服务网格（如 [Linkerd 或 Istio](https://thenewstack.io/using-istio-or-linkerd-to-unlock-ephemeral-environments/)）可以自动将流量从故障区域或云提供商处路由开，通常无需人工干预。

采用 Kubernetes 不仅仅是为了容器编排。这是一个战略性的商业决策，旨在赎回你的自由。它能让你节省数十亿美元，不仅是通过在中断中幸存下来，更是因为无需构建和维护 N 个不同版本的平台。

## **超越弹性：真正的胜利是速度**

这是大多数“多云”思想文章所遗漏的部分。仅仅为了灾难恢复而关注 Kubernetes，就像买了一辆 F1 赛车去买菜一样。

Kubernetes 真正的日常魔力在于它对开发者生产力的提升。

我们生活在一个全新的、AI 原生的世界中。我们有副驾驶和智能体生成大量的代码。软件的 [瓶颈](https://thenewstack.io/why-staging-is-a-bottleneck-for-microservice-testing/) 不再是编写代码；而是测试和验证它*.*

你如何确保你的 AI 生成的（或初级开发人员生成的）更改不会破坏它需要与之通信的 50 个其他 [微服务](https://thenewstack.io/introduction-to-microservices/) 之一？

旧方法是拥有一个 [共享的预演环境](https://thenewstack.io/smart-ephemeral-environments-share-more-copy-less/)。一个单一的、脆弱的、总是损坏的“上帝”环境，每个人都害怕触碰。它是一个永久的瓶颈。但是，如果使用得当，Kubernetes 可以成为一个速度增压器。

凭借其原生的命名空间、资源配额和网络策略等概念，[Kubernetes](https://thenewstack.io/kubernetes/) 是一个出色的多租户平台。这种多租户能力解锁了一种比简单地为每个 [拉取请求](https://thenewstack.io/shifting-testing-left-the-request-isolation-solution/) 启动完整、独立的堆栈副本远更为强大和可扩展的模型——这种策略在拥有数十或数百个微服务时会迅速变得不可行。

设想这种更先进的方法：

*   开发人员针对单个微服务打开一个拉取请求 (PR)。
*   一个 [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) 流水线立即启动那个已更改的服务。
*   利用服务网格（如 Linkerd 或 Istio）和上下文感知路由，该 [平台创建一个“虚拟”测试](https://thenewstack.io/boost-microservices-testing-quality-with-platform-engineering/) 环境。
*   当开发人员或自动化端到端测试向此环境发送请求时（例如，通过添加一个特殊的 HTTP 头），网格会智能地路由该请求。
*   对已更改服务的请求将转到新版本。对所有其他（未更改）服务的请求则路由到稳定的、共享的基线堆栈。
*   开发人员获得了针对完整堆栈的高保真、隔离测试，但没有了复制它的巨大开销。
*   一旦 PR 合并，只有那个单一的、轻量级的命名空间被销毁。

这是 CI/CD 的圣杯。它让团队有信心每天合并和部署 50 多次。而且，在传统的基于 VM 的架构上，这在财务或技术上都根本不可行。

## **不要只关注上次中断，为未来十年做好准备**

AWS 中断事件是关于集中性脆弱性的一次痛苦而昂贵的教训。是的，Kubernetes 是实现华尔街现在所要求的跨区域和多云弹性的技术解决方案。

但这仅仅是个开始。

不要仅仅为了在下一次提供商中断中幸存下来而采用 K8s。采用它来构建一个能够应对自身开发流程中瓶颈的平台。采用它，让你的团队能够更快、更安全、更有信心地交付产品。

这是令我兴奋的愿景。在 Signadot，我们认为 Kubernetes 是开发者生产力的终极基础——一个能让每位开发者按需获得一个隔离的、高保真测试环境的平台，即使在这个不断快速变化的 AI 驱动的新世界中也是如此。（你可以在 [我们的文档](https://www.signadot.com/docs/overview/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=tns+platform) 中了解更多关于这种方法的信息。）

软件的未来是快速、分布式和复杂的。不要再在一个提供商的沙滩上建造城堡了。是时候在磐石上建造了。