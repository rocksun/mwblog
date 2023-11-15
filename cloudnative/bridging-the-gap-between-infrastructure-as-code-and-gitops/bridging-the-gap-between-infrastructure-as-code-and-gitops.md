<!-- 
# 弥合基础设施即代码和GitOps的鸿沟
https://cdn.thenewstack.io/media/2023/11/d4ce1a52-jeremiah-ross-wpndkbutztm-unsplash-1-1024x683.jpeg

 -->

如何将Terraform、Crossplane和Atlantis巧妙地组合使用，发挥每项技术的优势，同时保留实施严格日常管理的灵活性。

> 作者John Dietz是Kubefirst的联合创始人。他在IT领域担任领导职务超过20年，涵盖测试、性能、开发、数据、DevOps、平台架构和云工程等多个方面。他在将《今日美国》转移到云端方面发挥了关键作用，并自2017年以来一直在帮助公司采用Kubernetes技术。译自 [Bridging the Gap Between Infrastructure as Code and GitOps](https://thenewstack.io/bridging-the-gap-between-infrastructure-as-code-and-gitops/) 。

基础设施即代码是过去十年计算领域最伟大的进步之一。它[建立了一种新的规范](https://thenewstack.io/infrastructure-as-code-evolution-and-practice/)，将软件团队中已经深入人心的变更流程扩展到了运行软件的基础设施上。提出变更请求，进行代码审查，批准，然后应用变更。

我们的团队一直在努力为我们的[即时Kubernetes平台](https://docs.kubefirst.io/)提供基础设施管理的自动化支持，包括初期设置(第一天)和日常管理(第二天)。挑战在于，第一天和第二天的基础设施即代码需求可能因您对第二天工作流程所需的基础设施治理管控的要求不同而大不相同。您是否可以让基础设施即代码工具决定您的Kubernetes集群需要被销毁，或者您需要人工参与这个决定过程？

几个月前，我们在一个研究工作中发现了一种非常巧妙的技术组合，可以同时发挥Terraform、Crossplane和Atlantis的优势，而且保留了根据您的组织要求实施严格日常治理的灵活性。

## 我们的任务：向大众提供免费的IaC自动化解决方案

因为我们正在努力为大众提供一个自动化的基础设施即代码解决方案，所以我们需要非常谨慎地考虑为您的内部开发者平台选择哪些基础设施即代码技术。我们会根据流行度、免费层价值、开源许可状态、稳定性、可扩展性、易用性、文档完备度、易维护性以及与平台其他组件的配合程度来衡量各个组件。

Terraform、Atlantis和Crossplane这三个技术多年来引起了我们极大的兴趣，因为它们各自解决了基础设施即代码自动化的不同方面。让我们简要讨论每项技术，并突出它们的优势和局限性。

## Hashicorp Terraform - 命令行IaC

[Terraform](https://developer.hashicorp.com/terraform)已经成为企业基础设施即代码的事实标准。我们多年来一直非常喜爱Terraform。它有一个稳定的产品，使用简单的语言，拥有繁荣的供应商中立的provider市场，可以[让您配置任何东西](https://thenewstack.io/terraform-cloud-now-offers-less-code-and-no-code-options/)：云服务，用户，机密，git仓库等等。

Terraform是一个命令行工具，它在一组用HCL语言编写的文件中运行，这些文件表示您期望的基础设施状态。当您运行`terraform plan`时，它会将期望状态与实际状态进行对比，并告诉您如果应用这些更改会发生什么。当您运行`terraform apply`时，它会执行实际更改，或者告诉您为什么无法更改。

因为Terraform是一个命令行工具，许多组织将它当作一个命令行工具在使用，这一点不足为奇。云工程师可以直接从他们的本地机器向云基础设施应用更改。而站点可靠性工程师和平台团队则对这种不透明的设置方式感到担忧，因为当您知道是谁在什么时间对应用了什么更改，他们的流程会变得简单得多，所以黑箱的命令行工具并不理想。这在凌晨被报警惊醒时尤其如此。

优点：

- 无与伦比的供应商支持 - 几乎万物都有Terraform提供商
- 稳定且可靠
- 命令行工具意味着您不需要预先存在的基础设施就可以运行它，这对从零开始非常有帮助

缺点：

- 将Terraform作为GitOps流程的一部分运行需要在流程中停止，或者从自定义的pod中执行Terraform
- 没有内置的控制平面来自动执行计划/应用(除非您支付SaaS产品费用)

## Atlantis - Terraform工作流自动化

多年来，[Atlantis](https://www.runatlantis.io/)一直是我们首选的将Terraform变更过程与软件团队的自然工作流程集成的技术。大多数人会将他们的Terraform代码保存在git仓库中，所以当您想要更改基础设施即代码时，您会打开一个拉取请求，请求审批，然后应用更改。

Atlantis会挂钩到这个流程中，这样当拉取请求被打开时，Terraform计划就会自动运行并直接在拉取请求中作为评论反馈计划结果。

如果您在审查后确定了计划，可以直接在拉取请求中评论atlantis apply，Atlantis将尝试应用Terraform更改并报告结果，如果成功则自动关闭和合并拉取请求。

我们在Kubernetes中以拥有所管理资源权限的[service account](https://github.com/kubefirst/gitops-template/blob/v2.3.5/aws-github/terraform/aws/eks/main.tf#L348-L364)身份运行Atlantis。通过这种设置，您可以允许开发者为基础设施即代码做出贡献，而不需要实际授予他们自行应用更改的权限。

优点：

- 提供Terraform计划和应用的可见性
- 提供所有基础设施更改的集中审计日志
- 开发者可以在他们熟悉的git中工作
- 开发者无需云端访问权限即可为基础设施做出贡献

缺点：

- 仅适用于Terraform的IaC

## Crossplane - 完美适合GitOps的IaC

我们是一家彻头彻尾的[GitOps公司](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/)。Kubernetes空间中可能没有比将Kubernetes集群绑定到git仓库中的期望状态更大的力量了。您可以定义所需的基础设施状态，然后您的GitOps引擎将会使其变为现实，或者告诉您为何无法实现。

[Crossplane](https://www.crossplane.io/)的目的与Terraform非常相似——它们都有一个开放的供应商中立的provider市场，都提供非常有价值的自管理免费层，并且在您定义好所需状态后，Crossplane会尝试应用这些状态。

但是，Crossplane的执行机制与Terraform非常不同。它不是一个命令行工具，而是一个在Kubernetes内运行的控制平面。您通常也不会在Crossplane中编写代码；它要求您在自定义资源定义中声明所需状态。当您使用GitOps同步流程编排复杂的云资源置备操作时，这种方式非常有优势，因为您可以将基础设施即代码步骤纳入GitOps编排中，而不会中断GitOps流程。

在Kubefirst中创建新集群时，GitOps就是我们在集群中安装所有应用程序的方式，所有的这些编排都定义在我们的`gitops`仓库中。下面是一个[示例](https://github.com/kubefirst/gitops-template/tree/v2.3.5/aws-github/templates/mgmt)，展示了我们上游模板仓库中的样子。在每个YAML文件中，您会看到这样一个注解：

```
  annotations:
    argocd.argoproj.io/sync-wave: '20'
```

这个注解定义了将会在哪个同步流程中应用这个GitOps配置，并允许我们控制安装顺序，例如先安装Vault，然后再安装`external-secrets-operator`。

优点：

- 适合GitOps的技术可以更无缝、自动地创建/销毁基础设施即代码资源
- 如果Terraform的新的商业源许可证对您的组织有问题，则可以选择替代的提供商

缺点：

- Provider 支持还不如Terraform全面(因为它比较新)，但是您可以从Terraform Provider创建Crossplane Provider，这为我们提供了一条值得信赖的发展道路
- 需要Kubernetes集群来运行，这在创建初始Kubernetes基础设施时有问题

## IaC自动化治理

当GitOps符合您的治理理念时，它非常出色；当不符合时，它可能会有些危险。

![](https://cdn.thenewstack.io/media/2023/11/477575c6-image1-e1699972785614.png)

对于应用程序，GitOps显然是一个强大的进步。想要新版本的应用程序？只需在GitOps仓库中的文件设置为新版本，当它进入主分支时，那就是您的应用程序版本。想要旧版本回来？只需在GitOps仓库中的文件重新设置为旧版本，它就会变成您的应用程序版本。

这对于应用程序是一个伟大的工作流程，它极大地简化了在Kubernetes中的资产管理，并显著改善了您的灾难恢复准备。但是正如我们前面讨论的，Kubernetes不仅可以管理应用程序，现在我们也在讨论基础设施。

IaC可以以经典的三步计划-审查-应用的命令行工具形式运行，也可以以两步审查-应用的控制平面工具形式运行，它们在不同的场景下都很有用。例如，对于生产集群，您可能不希望您的GitOps引擎在没有人工审批的情况下决定删除您的生产集群。

对于以提供平台为业的平台工程团队来说，在平台配置操作中结合使用GitOps和Crossplane是非常棒的。基本上，您可以根据需要在GitOps流程编排中随时运行基础设施即代码，而无需进行笨拙的检查步骤。但是，如果这是一个刚刚配置的生产集群，是否应该将其管理为GitOps或者采用更严格的治理，比如Atlantis提供的？

思考实验：本文的其余部分将描述一个将Atlantis与拉取请求集成的美好场景。相反，您也可以考虑基于[类似Kyverno这样的策略引擎](https://www.youtube.com/watch?v=hsf58XJD3j4&themeRefresh=1)和一些自定义资源在GitOps仓库中管理Crossplane基础设施即代码资源及其删除策略，声明生产集群不可被删除。

## 第一天GitOps，第二天治理

我们最近发现可以使用Crossplane的Terraform提供程序在Crossplane中运行Terraform。这使您可以利用GitOps在配置新集群基础设施时的正确位置运行Terraform。但是，在此之后，您可能不再希望集群由GitOps管理，而是将治理转移到Atlantis，以便从那时起人工审查计划。

当您在Crossplane资源上[设置](https://docs.crossplane.io/latest/concepts/managed-resources/#deletionpolicy)`deletionPolicy:Orphan`时，它会建议Crossplane在从GitOps中删除对象时不要删除实际基础设施。因此，如果您将资源孤立，等待它在ArgoCD中同步，然后可以从GitOps流程中删除Terraform，基础设施将保持不变。

接下来，您可以通过拉取请求将与Crossplane相同的Terraform复制到Atlantis管理的目录中，计划将显示没有更改(假设您保留相同的状态存储)。当您应用这个无操作变更时，拉取请求将被合并，之后Terraform将由Atlantis管理。

这种技术为您的平台团队在第一天提供了他们渴望的GitOps速度和功能，同时为您的组织在第二天及以后提供所需的治理和控制。

## 在Kubefirst上探索Crossplane包装的Terraform

Kubefirst[最近宣布](https://kubefirst.io/blog/release2-3/)了即时GitOps开源平台的集群生命周期管理功能。使用一个简单的`kubefirst launch up`命令，您可以获得一个配置应用程序，它可以创建一个多集群生态系统，这些GitOps集群无缝绑定到所有热门的云原生开源工具，并且都是免费的。

默认情况下，安装kubefirst时，您将获得四个新集群：`management`、`development`、`staging`和`production`。 management集群将托管您的Atlantis实例、Crossplane控制平面和一个kubefirst UI，后者可以在您的GitOps仓库中生成集群定义。 其余三个集群则会基于这些提交构建，您可以创建任意多的集群。templates目录定义了集群的创建方式，您可以根据需要调整其组件。

您的GitOps仓库中还将有一个Terraform目录，其中定义了由Atlantis管理的Terraform入口点。如果您使用拉取请求更改任何目录，您将在拉取请求中看到Terraform计划被触发，您可以在拉取请求中评论`atlantis apply`来应用计划。

看看您是否可以配置一组kubefirst集群，并将开发集群的Crossplane工作区孤立出来。 然后按照前面描述的细节，将其转移到Atlantis的管理下。 这是使用GitOps配置复杂基础设施的非常强大的方式。 在生产集群上，您可以将控制权交还给人工进行第二天的严格日常运维治理。

如果您遇到任何问题，我们有一个拥有数百名工程师的[社区](https://kubefirst.io/slack)，他们都渴望使用最流行的云原生开源工具进行协作。 我们的免费平台是全面的、可移植的、可扩展的和开源的。 您可以自由修改我们的任何意见。 我们欢迎贡献者，并希望通过我们的用户界面赢得您的青睐。 在我们为所有支持的云和基于模板的GitOps方法收集反馈的同时，我们的专业版是完全免费的。 我们期待您加入我们的使命。
