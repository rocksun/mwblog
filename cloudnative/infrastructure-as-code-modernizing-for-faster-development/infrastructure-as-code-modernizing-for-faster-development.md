# 基础设施即代码：实现现代化以加快开发速度

翻译自 [Infrastructure as Code: Modernizing for Faster Development](https://thenewstack.io/infrastructure-as-code-modernizing-for-faster-development/) 。

在 6 月 15 日专门针对 IaC 的虚拟用户大会 PulumiUp 之前，演讲者将讨论他们的组织如何实现更快的应用程序开发以及应对遗留系统的挑战。

![](https://cdn.thenewstack.io/media/2023/06/c9d1dc52-infrastructure-highways-2-1024x576.jpg)
*图片由 Unsplash 的 Abraham Barrera 提供。*

在 Matt Stephenson 在 Starburst Data 工作之前，他曾经在 Square 工作。在那里，他学到了一些关于使用传统基础设施即代码 （IaC） 的惨痛教训。

“我们构建了一个完整的系统，与 Terraform 和 Helm 进行了大量编排，并与我们自己的一些后端服务集成，” Starburst 的高级首席软件工程师 Stephenson 告诉 The New Stack 。

这不是一个他记忆犹新的项目：“必须构建和维护该服务的经历让我看到了行业中可用的服务，因为不必再次构建它。

他说，问题不在于 Terraform 本身，而在于“执行 Terraform 的所有代码，管理 Terraform 本身的输入和输出的所有代码。

传统 IaC 可能会给工程团队的生活带来许多挑战。其中：

* 定义配置时，遵循所需的约定和标准可能会变得更加复杂，并且复杂性会随着扩展而增加。
* 因此，配置偏移很常见，并可能导致不合规和服务中断。（一般来说，错误配置是[安全漏洞](https://thenewstack.io/bridgecrew-all-these-misconfigured-terraform-modules-are-a-security-issue/)的主要原因。)
* 必要的集成和功能并不总是可用于特定用例。
* 传统 IaC 可能会带来巨大的维护需求，并且很难招聘和留住具有这些技能的工程师。

“许多传统的基础设施即代码产品都有自己的语言，它们有自己的环境，你必须成为它们的专家才能有效地处理它们，”斯蒂芬森说。“或者你必须得到某种支持，才能使用其中之一。

在 Starburst Data ，他负责监督公司 Galaxy 产品的架构，这是一个托管数据湖分析平台。他的团队逐渐将传统的 IaC 换成了 Pulumi ， Pulumi 是一个开源的 IaC 产品，允许用任何编程语言构建基础设施。

Stephenson 将在 6 月 15 日举行的虚拟用户大会 [PulumiUp](https://www.pulumi.com/pulumi-up/) 上发表演讲，该会议致力于基础设施即代码、它如何实现更快的应用程序开发以及用户如何应对遗留系统的挑战。

他说，在会议上，他将谈论 Pulumi 的自动化 API 。“这对我们来说是一个很大的驱动力，能够编排我们所有的 Pulumi 堆栈，而不必编写我们过去必须编写的整个服务。”

## 为整个团队赋能

根据 Stephenson 的说法， Pulumi 与传统的 IaC 解决方案的一个差异是：“它基于人们在大学学习或加入行业后很快学习的编程语言”。

Pulumi 允许开发人员使用通用语言构建基础设施，包括任何 Java 语言（Java、Scala、Clojure、Groovy、Kotlin）; .NET （C#， F#， PowerShell）;Node.js （ JavaScript， TypeScript）;Go，Python 甚至 YAML 。这有助于使配置基础结构成为工程团队中更多成员可以执行的操作。

Stephenson 说，在使用 Pulumi 之前，“主要是更高级的工程师参与设置所有基础设施和代码环境。如今，我们有不同技能水平的人在其中工作。

他说，现在，即使是他组织中没有基础设施或站点可靠性工程背景的人，“当他们进行产品开发时，他们能够进入并进行所需的更改。他们真的不必担心聘请专家来获得他们想要的事情。

因此，Stephenson 补充说，为团队雇用特定于 IaC 的专家的需求减少了，更多的人有能力处理问题。

“如果发生涉及基础设施的事件，很多时候人们可以进行所需的更改，以执行我们的[持续交付 pipeline](https://thenewstack.io/ci-cd/) 并解决问题。”

## 寻求灵活性

华盛顿信托银行聘请的第一位 DevOps 工程师 Dennis Sauvé 也将在 PulumiUP 上发表演讲，谈论他的公司从完全本地系统迁移到 Microsoft Azure 云上运行的经验 - IaC ，主要用 TypeScript 编写，由 Pulumi 提供。

在聘请 Sauvé 之前，该银行决定启动云服务，以推进客户协作工具等创新，该工具将允许华盛顿信托的客户经理直接与客户交谈。它已经确定 Azure 的通信服务将帮助它更轻松地构建该应用程序， Sauvé 告诉 The New Stack 。

但该银行还希望未来可能构建的应用程序以及可能部署这些应用程序的云具有灵活性。

Sauvé 说， Pulumi 提供了这种灵活性和他的团队所需的选择。“你可以选择你的云提供商。然后，一旦您拥有云提供商，您就可以选择要构建该堆栈的语言，并且他们支持它。

“因此，我们高枕无忧，不仅要更改编写基础设施即代码的语言，还可以更改云提供商。我们可以去[亚马逊网络服务]或谷歌云，我们可以随身携带很多东西。因此，在考虑不同的提供商时，这是一个巨大的奖励。

## 节省时间和辛劳

Sauvé 说， Pulumi 对华盛顿信托银行的最大好处之一是它使他的团队能够节省时间和辛劳。他和他的开发团队一直在创建用于创建资源的最佳实践模板。

与开发人员和运营工程师之间可能存在的来回不同，“开发人员现在可以转到我们的基础设施包，找到他们想要构建的资源，选择该资源并设置它以进行部署。它确实加快了开发和测试环境的速度。

他补充说，不仅如此，Pulumi 已经成为一种标准化工具，确保在整个组织中以相同的方式创建资源。

然而，他补充说，迁移到云端和 Pulumi 并非没有困难。值得注意的是，原生的 Typescript 包从文件大小的角度来看，“只是一个资源使用稍微累赘的巨大包，但它在生产中起作用”。

他指出，Pulumi 将很快发布 TypeScript 软件包的下一代版本，该软件包“应该非常精简并解决一些性能问题”。

Stephenson 承认，从传统的 IaC 转移一开始可能会对团队造成一些干扰。（“总有人真的把帽子挂在房间里的专家身上，比如 Terraform ，”他指出。

但从长远来看，他说，它赋予了组织中更广泛的人权力。他指着一位大学毕业后不久就加入 Starburst Data 的同事：“现在他处于高级水平；他基本上让自己提升了两次级别，因为他在所有事情上都处于领先地位。Pulumi 是他真正挖掘的东西之一。

Stephenson 从其他公司听到了类似的故事。“你最终会遇到可能会反击的人，但归根结底，有很多人表现出色，成为下一个摇滚明星，因为做出了这样的转变。

To learn more about Infrastructure as Code (and see presentations by Stephenson, Sauvé and other experts), register for June 15’s virtual event, PulumiUP.
要了解有关基础设施即代码的更多信息（并查看 Stephenson、Sauvé 和其他专家的演讲），请[注册参加 6 月 15 日的虚拟活动 PulumiUP](https://www.pulumi.com/pulumi-up/)。

![](https://cdn.thenewstack.io/media/2023/06/7f0f48a8-pulumiup-copy.png)
