# 采用基础设施即代码的演练

翻译自 [A Walkthrough of Adopting Infrastructure as Code](https://thenewstack.io/a-walkthrough-of-adopting-infrastructure-as-code/) 。

首先介绍如何入门，然后深入探讨一些高级用例，展示你可以从中实现的功能。

![](https://cdn.thenewstack.io/media/2023/06/137b2633-shutterstock_10-1024x745.jpg)
*这是一个由三部分组成的系列中的第二部分。*

跟随这个系列的第一篇文章《任何编程语言的基础设施即代码》，这个演练将展示如何开始并使用基础设施即代码。我们所展示的一切都将使用 Pulumi 的免费和开源的基础设施即代码 SDK 完成，你可以[在这里下载](https://www.pulumi.com/docs/get-started/install/)。你也可以在这里注册 Pulumi Cloud。在讨论如何入门的基础知识后，我们将深入探讨一些高级应用案例，以展示你可以从那里做些什么。

## 迁移到基础设施即代码

当选择基础设施即代码工具时，最初有一个重大决策：是全新的基础设施，还是采用现有基础设施？在后一种情况下，也许你之前点击进入 AWS 控制台进行了一些实验，但现在准备使用基础设施即代码。或者，你可能最初使用的是 Terraform，现在想要迁移到 Pulumi。无论哪种情况，都无法避免。这是一个较为棘手的情况。

在某些情况下，最好的方法是直接丢弃该基础设施，从头开始构建。或者，你可以先专注于系统中的“新”部分，与现有基础设施进行整合，直到你确信是时候进行迁移。然而，在许多情况下，这是不可行的：也许你实际上已经有了一个关键任务的服务，需要将其纳入[基础设施即代码](https://thenewstack.io/a-brief-devops-history-the-roots-of-infrastructure-as-code/)的管理之下。好消息是，[Pulumi](https://thenewstack.io/pulumi-new-features-for-infrastructure-as-code-automation/) 提供了从现有工具（如 Terraform、AWS CloudFormation/CDK、Azure Resource Manager（ARM）、Kubernetes YAML 等）迁移的工具，将现有基础设施无缝地纳入 Pulumi 的管理范围，而不会造成任何中断。用户指南“[迁移到 Pulumi](https://www.pulumi.com/docs/guides/adopting/)”将详细介绍这个过程。

## 开始使用基础设施即代码

假设我们从新的基础设施开始，即使你从迁移开始，大部分概念仍然相关。

### 云基础设施资源：架构和拓扑

通常情况下，我们会根据我们独特的场景来规划一种特定的云架构。也许我们正在创建一个容器化应用程序，一个机器学习流水线，或者启动一个 Kubernetes 集群。在所有这些情况下，首先需要了解组成我们架构的云资源。在 Pulumi 中，这些资源是你将编写代码来操作的可编程对象。

云基础设施的世界有点令人生畏。Pulumi 支持超过100个云平台。AWS 有超过 200 个服务，其中包含超过 1,000 个单独的资源和超过 30 万个可配置属性。Pulumi 是一个多云工具，但“多云”并不意味着“最低公共分母”。相反， Pulumi 以原始、未经过修改的形式提供了所有这些云、资源和属性。这样做的好处是你可以随时利用这些云的全部功能。缺点是你需要了解这些云以及如何正确使用它们。因此，你可能很快就会发现自己需要一个起点，而不是一个空白页面。

[Pulumi 模板](https://www.pulumi.com/templates/)是一个很好的入门方式。它们代表了一打最常见的应用程序和基础设施架构在最流行的云平台上。这些模板旨在足够简单，以便一眼就能理解，但又足够完整，以便在实践中有用。其中包括在 AWS、Azure 和 Google Cloud 上跨容器化服务、无服务器应用程序、静态网站、虚拟机和 Kubernetes 集群等常见的 Kubernetes 工作负载。每个模板都会生成一个完整可工作的项目，你可以用来测试或作为自定义架构的起点。

[Pulumi Examples](https://github.com/pulumi/examples)是一个开源的集合，包含超过 300 个完全可工作的示例，涵盖更多的云平台和服务。如果在模板中没有找到合适的起点，很有可能在这里找到你所需的架构的近似解决方案。如果找不到，[Pulumi Registry](https://www.pulumi.com/registry/) 中有超过 100,000 个单独的 API 示例，例如[这个示例，演示了如何使用复制功能创建一个新的 Snowflake 数据库](https://www.pulumi.com/registry/packages/snowflake/api-docs/database/#example-usage)。虽然这些示例和模板并不总是那么完整，但它们也可以作为很好的起点，并为你创建额外的代码提供了极好的参考材料。

让我们快速看一下几个代表常见应用架构的示例。

### 架构 1：容器化服务

在这个示例中，我们构建并发布一个运行 NGINX Web 服务器的 Docker 镜像到一个私有容器 registry ，然后在一个负载均衡的服务中运行该镜像。负载均衡器确保我们可以在后端根据工作负载的增加轻松扩展副本数量，而不会从根本上改变客户端的访问方式。根据我们选择的云平台的不同，实现这个目标的方式也会有所不同，所需的详细资源也会有所不同。

如果我们选择的云平台是 AWS，我们将需要一个 Elastic Container Service (ECS) 集群和注册表，以及一个 Fargate 服务和应用程序负载均衡器。这样可以使我们的服务可以通过互联网访问：

![](https://cdn.thenewstack.io/media/2023/06/598dec04-image1a.png)

在[这里](https://www.pulumi.com/templates/container-service/aws/)查看 AWS 的模板。

另一方面，如果我们选择 Google Cloud，我们可以使用 Google Kubernetes Engine (GKE) 或 Google Cloud Run。在这个示例中，我们使用 Cloud Run 和内置的存储库，因为这些服务通常在刚开始时使用起来更容易:

![](https://cdn.thenewstack.io/media/2023/06/27faef52-image2a.png)

无论是哪种情况，在部署完基础设施后，我们将拥有一个完全可运行的微服务环境，其中一个负载均衡的服务正在运行 NGINX Web 服务器。基础设施即代码工具将为我们提供一个可访问互联网的负载均衡器的 URL ，以便我们可以浏览到它。

在[这里](https://www.pulumi.com/templates/kubernetes/gcp/)查看 GCP 的模板。

### 架构 2：无服务器应用

在这个示例中，我们将创建一个无服务器应用程序。与容器不同，容器在各个云平台上的表现比较一致（主要得益于 Docker 和 Kubernetes 等技术），而无服务器的工作方式在不同的云平台上差异很大。

对于 Azure，我们需要创建一个 Azure Blob 存储容器来托管我们的代码，上传无服务器函数包，并配置一个 Azure Function 应用程序，使我们的函数能够通过 HTTPS 访问：

![](https://cdn.thenewstack.io/media/2023/06/30947269-image3a.png)

在[这里](https://www.pulumi.com/templates/serverless-application/azure/)查看 Azure 的模板。

对于 AWS，尽管架构在本质上非常相似，但细节上有很大的差异。我们将使用 Amazon API Gateway 和 Lambda 结合在一起，使我们的函数可以通过 HTTPS 访问：

在这两种情况下，在部署完基础设施后，我们会获得一个用于访问的 Web URL。这个示例很好地提醒我们，每个云平台在细节上都非常不同。基础设施即代码并不一定会屏蔽这些细节，尽管可能可以构建一些抽象层来实现，这既是一种优势，也是你需要探索的问题。

![](https://cdn.thenewstack.io/media/2023/06/99a1923a-image4a.png)

[这里](https://www.pulumi.com/templates/serverless-application/aws/)是 AWS 的模板。

### 架构 3：Kubernetes 集群

在最后一个示例中，让我们转换思路，将重点放在比应用程序本身更“基础”的基础设施上。这是平台工程师可能更关心的事情，而不是专注于构建和发布服务的后端系统工程师。在这个具体案例中，我们将在 AWS 和 Azure 中创建一个托管的 Kubernetes 集群。

对于 Azure 的 Kubernetes 服务 (AKS)，该服务的设计相当庞大。因此，我们可以简单地启动一个带有相关网络基础设施的托管集群：

![](https://cdn.thenewstack.io/media/2023/06/fc21577e-image5a.png)

[这里](https://www.pulumi.com/templates/kubernetes/azure/)是 Azure 的模板。

另一方面，对于 AWS 的 Elastic Kubernetes Service (EKS)，该服务本身的设置相当复杂，涉及许多组件。这包括控制平面本身、工作节点组、自动扩缩组、AWS 容器网络接口插件来管理 Pod 网络等等：

![](https://cdn.thenewstack.io/media/2023/06/1550d812-image6a.png)

[这里](https://www.pulumi.com/templates/kubernetes/aws/)是 EKS 的模板。

您可以在这里看到不同云提供商的等效云服务之间的巨大差异，以及 AWS 更加“构建模块”风格的实现方式。这也是基础设施即代码能够捆绑最佳实践以便重复使用的绝佳示例。它使用了 [Pulumi 的 EKS Package](https://www.pulumi.com/registry/packages/eks/)，以标准方式配置了上述所有内容，这样当您刚开始时就不需要弄清楚每一个细节。

无论是哪种情况，我们最终都会得到一个完全托管的 Kubernetes 集群，工具会生成一个 kubeconfig 文件，可以立即在集群上部署或查看。

## 基础设施项目和堆栈

所有这些示例都有一个共同点：基础设施即代码程序的任务是声明个别资源对象、它们的属性以及它们之间的关系。无论是什么场景、云平台还是选择的编程语言，这都是正确的。一旦程序完成了这个任务，基础设施即代码工具就会处理剩下的事情。

声明所有这些的代码是 Pulumi 称之为**项目**的东西，每个经过配置和准备部署的项目实例，也就是每个“环境”，被称为**堆栈**。

![](https://cdn.thenewstack.io/media/2023/06/129d0389-image7.png)

每个项目可以有多个正在运行的堆栈。这对于管理开发者堆栈（例如每个团队成员一个堆栈）、暂存环境和生产环境非常有用。在扩展全球服务时，拥有多个生产环境是很常见的。而使用短暂的堆栈也越来越常见，例如通过创建临时堆栈来运行拉取请求期间的预提交测试，以便对假设的部署进行测试。

Pulumi CLI 提供了创建这两种堆栈的便利方式。pulumi new 命令创建一个新的项目：

```shell
$ pulumi new
```

它会提示您选择项目布局、名称和其他相关设置。一个项目只是一个名称、程序和相关元数据，并且是后续堆栈的父级。

new 命令还会创建一个起始堆栈，通常称为 dev，用于在开始新项目时进行早期开发。但是，可以使用 pulumi stack 命令创建和管理其他堆栈：

```shell
$ pulumi stack init   # 为此项目创建一个新堆栈
$ pulumi stack ls     # 列出此项目中的堆栈
$ pulumi stack select # 切换当前正在使用的堆栈
$ pulumi stack rm     # 删除堆栈
```

在项目级别定义的所有内容都会在所有堆栈之间共享，包括代码本身。这很好，因为通常我们希望所有环境彼此保持一致。但显然，有时我们希望某些元素有意地有所不同。也许我们想将不同的堆栈部署到不同的区域，在开发堆栈中使用比生产环境更小或更少的虚拟机以降低云成本等等。

这就是 Pulumi **配置**的用途。使用配置，您可以轻松地在一个堆栈与另一个堆栈之间为特定设置设置不同的值，然后程序可以相应地改变其行为。这使您可以通过默认方式保持项目的大部分已声明基础设施在堆栈之间的一致性，但在需要时可以显式地进行更改。

```shell
$ pulumi config set aws:region us-west-2
```

然而，配置并不止于此。我们的某些配置可能涉及使用敏感信息，例如 Stripe 访问密钥、数据库密码或其他类型的秘密令牌。尽管 Pulumi 使用传输中和休息时的安全加密来安全处理所有状态，但我们绝不希望这些设置以明文形式显示在任何地方。这就是 Pulumi 密钥系统的用武之地，它提供了内置的加密和安全存储，用于存储这些设置。

```shell
$ pulumi config set dbPassword --secret [redacted]
```

最后，Pulumi 提供了工具，根据您自己的要求管理项目和堆栈，类似于 Git 可以用于许多不同的源代码控制哲学，如单体仓库。有关所涉及的权衡的描述，请参阅[“组织项目和堆栈”用户指南](https://www.pulumi.com/docs/guides/organizing-projects-stacks/)或 [IaC 推荐最佳实践博客系列](https://www.pulumi.com/blog/iac-recommended-practices-structuring-pulumi-projects/)。对于复杂的系统，我们可能希望在基础设施的不同部分之间区分关注点，这意味着一个堆栈可以依赖于另一个堆栈。

例如，可以有一个基本的网络和安全层、一个数据堆栈和一个 Kubernetes 集群，它们从较低层次消耗信息，但是可以单独进行配置，而上面的应用程序则依赖于上述所有元素的不同组合。

每个堆栈是一个安全性和部署并发性的单位。通过以这种方式分层堆栈，我们可以让不同的团队成员相互独立地工作，确保我们的基础设施的最安全和最可靠的部分受到保护，并且只是普遍地让团队的不同部分以不相互影响的方式更快地前进。支持这一点的功能被称为“堆栈引用”，您可以在文档中[了解有关如何使用它们的更多信息](https://www.pulumi.com/docs/intro/concepts/stack/#stackreferences)。

## 进行部署

当我们将所有事物连接起来——一个项目、其代码包含所需的云资源拓扑声明，以及至少一个堆栈——现在是时候实际运行它了。由于我们的代码是用普通的编程语言编写的，很容易认为我们只需直接运行它。（事实上，稍后我们将看到，使用 Automation API，我们确实可以这样做。）然而，基础设施即代码是特殊的，由于其声明性质，我们将使用 Pulumi CLI 来运行它，以确保采用声明性的基础设施即代码工作流程。

`pulumi up` 命令是实现这一工作流程的关键：

```shell
$ pulumi up
```

up 命令评估我们的程序，生成所需状态的资源图，并向我们提供即将发生的部署的预览。（如果我们想作为独立步骤运行预览，可以显式运行 `pulumi preview` 命令。）该预览将显示任何创建、更新或删除的操作，以及有关部署的有趣元数据。第一次部署到堆栈时，只会进行创建操作，但之后我们将看到从上一次 up 操作到下一次 up 操作所发生的所有更改的详细差异，包括属性级别的差异。这些更改可能是由于代码更改或配置更新引起的。

让我们看看所有这些的实际操作。首先，我们将创建一个新的堆栈，在 AWS 上运行一个负载均衡的服务（尽管是 AWS，但无论我们选择的云是什么，相同的工作流程都适用）：

```shell
$ pulumi new container-aws-typescript
```

现在让我们检查生成的代码：

![](https://cdn.thenewstack.io/media/2023/06/39b0d7a7-image8.png)

如果我们部署这个代码，我们将看到完整的资源图和最后的负载均衡服务：

![](https://cdn.thenewstack.io/media/2023/06/1cbdb6e7-image9.png)

这就是初始部署的样子。现在让我们为我们的应用程序创建一个数据库，并将其扩展到三个副本，只是为了好玩。我们首先进行代码更改：

然后再次运行 `pulumi up`。请注意，这次它会显示我们的更改差异，甚至包括已更改的单个属性以及新增的内容：

![](https://cdn.thenewstack.io/media/2023/06/49d040f2-image10.png)

请注意，由于了解资源之间的依赖关系，基础设施即代码工具可以并行运行许多操作。您会看到在更新过程中显示了时间。配置云基础设施可能是一个耗时的过程，但由于并行性，Pulumi不仅知道以什么顺序运行各种操作，还可以尽可能快地完成。

当一切都完成后，我们可以销毁我们的堆栈，这将删除其中的所有基础设施：

```shell
$ pulumi destroy
```

这显然是一个危险但必要的操作。Pulumi 具有两个功能可帮助避免错误。首先，保护资源会要求执行额外的步骤才能删除它，其次，“保留删除”选项会在逻辑资源从 Pulumi 堆栈中移除后仍保留物理资源。对于那些可能造成灾难性破坏的关键和宝贵资源（如数据库），最好使用这些选项——宁愿安全，也不要后悔！

在本系列的第 3 部分中，也是最后一部分，我们将讨论高级的基础设施即代码用例，以及如何使用 Pulumi Cloud 来开发可编程的云基础设施并在大规模上管理云基础设施。我们将使用 Pulumi Cloud ，可以在[此处](https://app.pulumi.com/signup)找到它。