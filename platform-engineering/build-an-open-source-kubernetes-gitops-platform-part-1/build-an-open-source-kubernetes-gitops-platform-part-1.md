
<!--
title: 开源Kubernetes GitOps 平台构建：第一部分
cover: https://cdn.thenewstack.io/media/2025/01/69041ce4-gitops.jpg
-->

使用Kubernetes领域流行的开源工具构建多集群GitOps平台的演练。

> 译自 [Build an Open Source Kubernetes GitOps Platform, Part 1](https://thenewstack.io/build-an-open-source-kubernetes-gitops-platform-part-1/)，作者 John Dietz。

Kubernetes 最近迎来了十周年庆典，其流行的[开源](https://thenewstack.io/open-source/)产品领域已经发展成熟，无论您的平台必须使用什么，都已准备好可靠的开源产品来提供帮助。

一个典型的集群通常包含许多开源工具，因为没有这些工具的 Kubernetes 无法为您的业务增值。这些工具都是令人望而生畏的云原生计算基金会 (CNCF) [全景](https://l.cncf.io/) 中的一部分，它提供了一系列微型产品。有一些工具可以帮助您执行诸如[管理对您服务的访问](https://thenewstack.io/postgres-with-kubernetes-self-managed-or-managed-service/)、创建和更新传输层安全 (TLS) 证书、管理您的域名安全 (DNS) 记录以及确保您的密钥安全同步等操作。这些工具为如何在预生产和生产软件环境中为您的用户构建和交付您的应用程序和基础设施提供了支柱。

本演练是一个使用 Kubernetes 领域流行的开源工具构建多集群 GitOps 平台的综合示例。

## 步骤 1. 选择您的云

您需要做的第一件事是选择您将使用的云。每个云都略有不同，但是如果您专注于云原生架构，Kubernetes 会在很大程度上平衡竞争。大型云服务提供商拥有可靠性优势，而简单的云则展示了成本节约、速度以及更简单的基础设施即代码 (IaC) 和云体验。

通过正确的云原生工具选择，您的云选择的重要性会大大降低。在 Kubernetes 环境中，很容易找到与云无关的产品。Argo、[cert-manager](https://thenewstack.io/how-cert-manager-got-to-500-million-downloads-a-month/)、external-dns 和 CI 运行器在不同的云中都以相同的方式工作。

如果[混合云或多云](https://thenewstack.io/kubernetes-applications-for-multicloud-hybrid-cloud-environs/) 最终成为您故事的一部分，那么在构建平台时，请尽量避免使用特定于云的技术。云教程、蓝图和参考指南可能会试图引导您使用其专有的入口控制器、密钥管理器等，但是 CNCF 全景中通常还有更多可移植的开源替代方案可供选择。最好先进行研究。

## 步骤 2. 选择您的 Git 提供商

很难找到比 GitHub 或[GitLab](https://about.gitlab.com/?utm_content=inline+mention) 更具吸引力的选项。两者都提供可靠的 SaaS 解决方案来托管您的 git 存储库和容器镜像，并且两者都提供自托管选项。您无论选择哪个提供商都不会出错。

对于面向公众的开源代码，我倾向于使用 GitHub。如果您将自托管您的 git 服务器，我倾向于使用 GitLab。如果您没有这些要求，GitHub 通常更受欢迎。在开始之前，您应该问自己的重要问题是：我将来可能会开源什么，以及为什么我可能希望我的源代码[私下托管并从 SaaS](https://thenewstack.io/private-saas-a-new-paradigm/)生态系统中移除？

## 步骤 3. 您的平台域名和 DNS 提供商

如果您还没有关于 DNS 提供商的意见，Cloudflare 是一个不错的选择，尤其是在云未来不明朗的情况下。您可以直接购买和注册域名，或将您现有的域名从您当前的 DNS 注册商指向 Cloudflare 域名服务器。Cloudflare 提供了一些很棒的服务，其配置用户体验非常简单直观。

大多数计划在一个云中保持集中化的用户都使用其云提供商的 DNS 服务。这是一个很好的本能。在 Kubernetes 环境中，cert-manager 和 external-dns 产品对大多数云都具有出色的支持，而这两个产品以及 IaC 通常是唯一需要考虑的 DNS 参与者。

## 步骤 4. 定义您的基础设施即代码

IaC 是您必须为平台生成的第一个代码。IaC 是定义您需要的云资源的代码。它有助于配置您使用的任何软件（如 GitHub 或[DataDog](https://www.datadoghq.com/?utm_content=inline+mention)）的“期望状态”，但这可能会与您对 GitOps 的期望相冲突。当您可以做到时，您的本能应该是让 GitOps 赢得这场战斗。GitOps 只是管理 Kubernetes 上应用程序配置的更好工作流程。

IaC领域只有少数几家领先者。HashiCorp的Terraform在过去十年的大部分时间里一直是IaC的宠儿。一些许可证决策削弱了他们在业界的控制力，使得OpenTofu成为这家基础设施巨头的一个流行分支。

其他流行的选项包括Crossplane，它允许你以Kubernetes原生方式定义你的IaC，以及Pulumi，它允许你使用更流行的开发语言编写你的IaC。

编写IaC时，避免构建IaC单体应用的诱惑。保持你的状态较小，并将事物分解成合理隔离的域。例如，你可以在不同的IaC空间中定义你的云、Git、密钥和用户资源。这可以加快你的IaC执行时间，并减少IaC更改的影响范围。

IaC领域的其他考虑因素包括IaC执行的自动化和治理。Atlantis、Crossplane、Spacelift、Env0和Terraform Cloud都在这个领域做得很好。一旦你建立了你的IaC，你能为你的审计跟踪做的最好的事情就是集中和自动化它的执行。这样安排事情，你的用户就不需要他们自己的权限访问这些资源，因为平台自动化承担了责任。

## 步骤5. 选择你的GitOps引擎

GitOps在许多方面与IaC相似。GitOps允许你定义一个期望状态，然后将其变成实际状态。IaC工具通常通过运行命令来做到这一点，而GitOps则通过自动将Git仓库中某物的期望状态绑定到Kubernetes集群中的实际状态来做到这一点。

在操作上，这意味着要更改集群中的应用程序（例如，应用程序的新版本），你需要通过对包含所有应用程序配置的`gitops`仓库进行更改的拉取请求来更改集群中的实例。这为你的平台的安全性、灾难恢复、操作透明性和配置可重复性提供了显著的优势。

有两个领先的GitOps工具，Argo CD和Flux CD。两者都有活跃的社区，并在Kubernetes领域解决了巨大的问题。它们都是可靠的选择，拥有良好的发布记录、强大的开源治理模型和通过社区进行编码的精神。

我认为Argo CD可能是编写过的最好的软件。我听说Flux CD也是如此。我对这两个项目都充满热情，我喜欢他们的共同目标。

![](https://cdn.thenewstack.io/media/2025/01/210ea526-image1.png)

## 步骤6. 定义你的管理支柱

你必须定义你将在初始控制平面集群或管理集群中使用哪些工具。有很多方法可以做到这一点，但出于实际目的，我将提供一个基于Konstruct方法的示例。

在Konstruct，一个典型的管理集群看起来像这样：

![](https://cdn.thenewstack.io/media/2025/01/7b748ff4-image2-1024x580.png)

管理集群建立了你构建、管理和交付应用程序以及额外基础设施的基础技术。

对于Konstruct的控制平面，我们选择：

* **Argo CD:** 一个GitOps引擎，用于管理Kubernetes中的所有内容以及我们扩展Kubernetes以管理集群外部的所有内容。
* **Atlantis:** 在你的拉取请求中自动化你的Terraform/OpenTofu执行，以提供IaC治理。
* **Crossplane:** 使用GitOps进行IaC操作。
* **vCluster:** 在我们的集群内部创建低成本的隔离集群。

要访问集群服务：

* **ingress-nginx:** 允许外部访问在你的集群中运行的服务。
* **external-dns:** 自动将你的主机名DNS记录指向你的负载均衡器。
* **cert-manager:** 生成和更新为你的服务创建短期TLS证书。
* **Let’s Encrypt issuer:** 为你的服务提供免费的浏览器信任的TLS证书。

对于CI：

* **github-actions-runner-controller:** 一个自托管的GitHub Actions运行器，用于私下运行GitHub CI作业。
* **gitlab-runner:** 一个自托管的运行器，用于私下运行GitLab CI作业。
* **Argo Workflows:** 我们有一套模板，用于构建容器、Helm图表并进行GitOps交付和推广。
* **ChartMuseum:** 一个简单的界面，用于托管由S3支持的Helm图表。

对于用户和密钥：

* **Vault/OpenBao:** 密钥引擎、用户、组和OpenID Connect (OIDC)提供程序，以便平台具有即时的单点登录。
* **External Secrets Operator:** 将你的密钥引擎从Kubernetes中抽象出来，并保持你的密钥同步。
* **Reloader:** 当Kubernetes中的密钥更改时重新启动Pod的操作符。

对于平台门户：

使用GitOps创建物理和虚拟Kubernetes集群，并管理应用程序到这些集群的交付。[kubefirst-pro](https://konstruct.io/kubefirst-pro)
Kubernetes 的吸引力很大程度上源于其厂商无关的架构，这使得这些组件可以互换。您可以使用我们使用的相同工具，也可以从 CNCF 生态系统中选择具有相同功能的替代方案。

## 配置您的云原生平台

恭喜您，您现在已经选择了您的云、DNS 和 Git 提供商。您已经确定了管理平台中所需的各项技术；您知道您的 IaC 和 GitOps 技术将是什么；现在您可以开始为您的组织配置新的开源平台了。

在下一篇文章中，我们将继续介绍从平台创建之日起执行的步骤。我们将逐步介绍平台机器人的创建、GitOps 文件内容的创建、集群配置 IaC 的执行、GitOps 集群引导过程、环境和工作负载集群集群的建立、下游工作负载集群的建模和配置以及您的第一个构建应用程序到新环境的交付。请在第二部分中继续参与这个平台构建之旅。
