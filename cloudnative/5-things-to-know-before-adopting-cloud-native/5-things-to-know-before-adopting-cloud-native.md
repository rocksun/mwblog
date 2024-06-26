# 采用云原生技术前需了解的五个要点

如果没有适当的规划和工具，企业可能面临着数据量大、成本高、停机时间长、工程效率降低以及客户不满等风险。

翻译自 [5 Things to Know Before Adopting Cloud Native](https://thenewstack.io/5-things-to-know-before-adopting-cloud-native/) 。

![](https://cdn.thenewstack.io/media/2023/08/5df696ca-cloud-1024x380.jpg)
*图片来自 Shutterstock 的 guruXOX*

> 这是一个四部分系列的第一部分。
>
> 云原生的采用并不是一个简单的搬迁和迁移过程。在跨足这一步骤之前，有许多需要学习和考虑的内容，以确保云原生环境能够满足业务和技术需求。对于那些在现代化过程中处于早期阶段的企业来说，这可能意味着需要了解各种云原生术语、好处、风险，以及云原生可观测性对于成功的重要性。
> 
> 为了提供帮助，我们创建了一个围绕“入门云原生”的四部分指南。这些文章旨在教育并帮助概述云原生架构的内容和原因。
>
> 第一部分首先涵盖了云原生的基本要素，以及与传统架构的区别，以及与 DevOps 方法论的关联。

## 审视云原生及其对当今业务的必要性

对于企业的生存来说，可靠的[云原生环境](https://thenewstack.io/cloud-native/)至关重要。转向现代的[微服务](https://thenewstack.io/microservices/)和基于容器的架构承诺提供速度、效率、可用性以及更快创新的能力，这些是企业在一个新一代的云原生公司正在吸引渴望获得新功能、快速交易和始终可用服务的客户时所需要的关键优势。

再加上经济不确定性和企业之间的竞争压力飙升：在线零售商网站的简单搜索延迟可能会使一个忠实的客户和令人垂涎的收入流失给更具创新和可靠性的竞争对手。

随着灵活机构的竞争加剧、全球经济的不确定性以及要求高、苛刻的客户，转向现代的、云原生的技术堆栈和最佳实践比以往任何时候都更为重要，它可以提供：

* 高度可用和更可靠的服务。云原生的最佳实践使您能够构建更具弹性的产品和服务。
* 更多的灵活性和互操作性。云原生环境不仅更具可移植性，而且还能够动态地按需进行扩展和缩减。
* 更快的速度和更高的效率。工程师可以更快地进行迭代，以应对不断增加的客户期望。

但需要注意的是，云原生并不容易。采用云原生技术带来的好处是不可忽视的，Gartner 预测到 2027 年将有 90% 的公司采用云原生。但是，从传统环境向现代环境的转变也面临着挑战：如果从传统向云原生的转型缺乏适当的规划和工具，企业可能面临着空前的数据量、增加的成本、停机时间、降低的工程生产力，以及客户的不满。

## 什么是云原生？

大多数组织面临的挑战是如何灵活地开发和部署新应用程序，以满足不断变化的业务需求。越来越多地，云原生是构建和部署新应用程序的首选架构。云原生方法为业务和开发人员都带来了好处。

与单体应用程序开发相比，云原生应用程序或服务与明确描述的依赖关系松散耦合。因此：

* 应用程序和进程以[软件容器](https://thenewstack.io/containers/)作为隔离单元运行。
* 独立服务和资源由中央编排过程管理，以改善资源利用率并降低维护成本。
* 企业获得了一个高度动态的系统，由相互协作提供业务价值的独立进程组成。

从根本上说，云原生架构利用微服务和容器，在公共或私有云平台上作为首选的部署基础架构。

* **微服务**提供了松散耦合的应用程序架构，支持高度分布式模式的部署。此外，微服务支持一个不断增长的解决方案生态系统，可以补充或扩展云平台。
* **容器**很重要，因为开发、部署和维护应用程序需要大量持续的工作。容器提供了一种将进程和应用程序捆绑和运行的方法。它们具有可移植性和易于扩展的特点。它们可以在应用程序的整个生命周期中使用，从开发到测试再到生产。它们还允许将大型应用程序分解为较小的组件，并作为微服务呈现给其他应用程序。
* **Kubernetes**（也称为 K8s）是最受欢迎的用于编排容器的开源平台。一旦工程师配置了所需的基础架构状态，[Kubernetes 使用自动化将该状态与其平台同步](https://thenewstack.io/kubermatic-kubernetes-platform-beats-complexity-through-automation/)。组织可以在裸金属、虚拟机、公共云、私有云和混合云上运行Kubernetes与容器。

## 云原生与 DevOps 的关联

云原生是两种变革的交汇点。一种是围绕微服务和容器的软件和技术架构，另一种是组织变革，即 DevOps 。DevOps 是一种实践，打破了开发团队和中央 IT 运维团队之间的壁垒，编写软件的工程师也负责运行它。在云原生时代，这一点至关重要，因为分布式系统如此复杂，操作必须由构建它们的团队来运行。

通过[云原生和 DevOps](https://thenewstack.io/cloud-native/doing-devops-the-cloud-native-way/)，小团队可以独立地开展具体项目的工作，这些项目可以轻松地合并成综合应用程序。他们可以更快地工作，而不需要承担作为更大团队一部分运作的所有麻烦。亚马逊执行主席杰夫·贝佐斯认为，这种小团队的方法是如此有益，他将两片比萨饼团队的概念普及了出去，这是两片比萨饼可以喂饱的人数。根据这一理论，团队越小，成员之间的协作就越好。这种协作非常重要，因为软件发布的速度比以往任何时候都要快得多。

云原生和 DevOps 共同使组织能够快速创建和频繁更新应用程序，以满足不断变化的业务机会。它们有助于满足期望（并要求）应用程序具有高可用性、响应能力，并随着新技术的出现而不断整合的利益相关者和用户群体。

## 单体架构曾经有其时代和地位

我们刚刚讨论了[微服务架构](https://thenewstack.io/microservices/what-is-microservices-architecture/)是在组织中部署一组分布式但相互依赖的服务的有结构方式。与过去的一些应用程序开发方法相比，它们是具有改变性质的，允许开发团队独立工作，并以云原生规模运作。

相比之下，单体架构中的应用程序所有元素都紧密集成在一起。对一个元素进行简单的更改，比如需要支持新的前端，就需要进行这种更改，然后重新编译整个应用程序。通常有以下三个优点：

* **开发简单**：许多开发工具支持单体应用程序的创建。
* **部署简单**：将单个文件或目录部署到您的运行时。
* **扩展简单**：通过在某种负载均衡器后面运行多个副本来轻松地扩展应用程序。

![](https://cdn.thenewstack.io/media/2023/08/e131b035-image1a-e1691410870594.jpg)

## 单体模型

单体模型更加传统，当然也有一些优点，但会减缓需要在快速、可靠、创新的应用程序开发方面进行扩展和竞争的企业。以下是组织在使用单体模型时面临的主要问题：

* **可扩展性** - 个别组件不容易扩展。
* **灵活性** - 单体受到已在系统中使用的技术的限制，通常不可在新环境中移植（跨云）。
* **可靠性** - 模块错误可能会影响应用程序的可用性。模块错误可能会影响应用程序的可用性。
* **部署** - 当发生变更时，需要重新部署整个单体。
* **开发速度** - 在涉及大型单体应用程序时，开发更加复杂且较慢。

## 关于云原生的最后一句话

过去几年的教训告诉我们，速度和敏捷性是数字化转型组织成功的基础。能够满足业务线、客户和内部用户不断变化的需求的组织，将能够成功地应对艰难时期。

采用[云原生架构有助于确保可以快速创建新应用程序](https://thenewstack.io/architectural-considerations-for-creating-cloud-native-applications/)，并及时更新现有应用程序，以整合新技术或随着时间的推移进行的需求变更。

在下一篇文章中，我们将讨论云原生架构的好处以及它如何赋予现代业务力量。
