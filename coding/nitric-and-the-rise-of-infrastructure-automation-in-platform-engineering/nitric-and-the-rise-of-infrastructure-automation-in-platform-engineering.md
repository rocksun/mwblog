# Nitric 和基础设施自动化在平台工程中的崛起

在一个充斥着低代码的世界中，基础设施自动化的“少代码”目标在平台工程领域变得更加流行。

翻译自 [Nitric and the Rise of Infrastructure Automation in Platform Engineering](https://thenewstack.io/nitric-and-the-rise-of-infrastructure-automation-in-platform-engineering/) 。

![](https://cdn.thenewstack.io/media/2023/08/6fcbfc14-nitric-1024x683.png)

如果您构建了一个内部开发者平台（IDP），您是选择采用低代码并雇低成本工程师，还是为高性能工程师打造呢？这引发了与 [Nitric](https://nitric.io/?utm_content=inline-mention) 的工程副总裁 [Rak Siva](https://www.linkedin.com/in/rak-siva-b9360816a/) 的讨论，我们讨论了低代码和[平台工程](https://thenewstack.io/platform-engineering/)的交集，特别是对于自助创业初创公司而言。

是的，现在已经是 2023 年，科技行业的每个人都在努力在更少的资源下做更多的事情。但初创公司不得不考虑[从 A 轮融资到 B 轮融资需要花费更长的时间](https://news.crunchbase.com/venture/startups-raise-series-a-series-b/)。此外，包括[网络安全](https://thenewstack.io/how-to-get-started-filling-3-4-million-cybersecurity-jobs/)和 [DevOps 工程师](https://www.venturi-group.com/blog/2022/04/why-are-devops-engineers-so-hard-to-hire?source=google.com)在内的许多岗位，无论经济环境如何，都很难填补，并且仍然保持着较高的薪水。

现在比以往任何时候都更需要让应用开发人员更快地为最终用户提供价值。

平台工程，这门关注减少开发人员和运维工程师的繁重工作的社会技术学科，实际上提出了一个非常有说服力的方案来实现所有这些目标。此外，在这个缺乏人手的[技术裁员时期](https://thenewstack.io/fear-and-layoffs-how-to-cope-with-techs-uncertain-times/)，这也是一种避免[开发人员过度劳累](https://thenewstack.io/this-cant-be-normal-the-tech-industry-after-a-year-of-burnout/)的方式。

在内部开发平台（IDP）中利用低代码开发，或者仅通过基础设施自动化实现更少的代码，比以往任何时候都更重要。并且，由于平台预算正受到削减，与其他方面一样，将一些复杂性抽象出来，以减轻过度紧张的平台工程师的负担，也是一个不错的主意。

## 低代码平台 vs. 较少代码平台

首先，为了讨论的需要，从 IT 部门的视角，对一些基本定义进行说明：

* [什么是无代码开发？](https://thenewstack.io/what-everyone-gets-wrong-about-no-code/)当重复发生某些事情时，工程师不编写代码，比如 Webflow、Airtable 和 Bubble，这对于原型和网站特别有用。
* [什么是低代码开发？](https://thenewstack.io/using-low-code-tools-in-enterprise-application-development/)通常会构建图形用户体验来解决单一任务，Siva 指出这对原型制作很有用。低代码示例包括 BigQuery、Tableau 和 Looker 7。
* 什么是基础设施自动化？使用框架和抽象来通过较少的代码执行最佳实践。通常位于内部开发者门户后面，开发人员仍然可以选择不遵循这些[黄金路径](https://thenewstack.io/new-to-platform-engineering-try-a-thin-self-service-layer/)。基础设施自动化最终应导致工程师编写较少的代码。

这三者都声称可以帮助开发人员以更少的资源做更多的事情。但正如 TNS 的 Richard Gall 所写，[低代码可能意味着开发人员需要付出更多的工作](https://thenewstack.io/does-low-code-mean-more-work-or-more-freedom-for-developers/)。此外，普渡大学的最新研究发现，尽管“令人恼人地可信”，[ChatGPT 的代码回答在 52% 的时间里是错误的](https://arxiv.org/abs/2308.02312)。的确，低代码可能只适合进行实验，或者可能需要使用 [Kubiya DevOps 的会话 AI](https://thenewstack.io/kubiya-launches-first-generative-ai-for-platform-engineering/) 等工具对内部领域需求和工作流进行培训。

对于公民开发者（即在技术业务方面工作的人员），无代码开发可能很有趣。但是对于 IT 群体而言，Siva 担心这会带来技术锁定和“承诺不兑现”。他认为低代码工具通常是特定于品牌的，而较少和低代码开发工具通常更加中立，如云无关。

此外，开发团队可以以不同的方式与平台互动。一些团队可能会采用低到无代码的便利路线来处理运营任务，同时希望对最终用户有差异化影响的步骤有更多的控制。

内部开发者平台应该像汽车经销商一样，不同的应用团队选择不同的车辆，都具有相同的品牌、基本安全性、可观察性和网络性能。每个团队都应该能够查看底层情况，了解发生了什么，但运营团队将决定哪些团队可以自动执行哪些操作，哪些团队可以采用手动方式。如果他们进行了平台团队明确不支持的操作，他们可能会自行承担风险。

正如 Syntasso 的 Abigail Bangser 所说，内部开发者平台应该处理多个团队共享的非差异性但并不重要的重复性工作。因此，开发人员如何进行差异性工作可能会因公司而异。

## Nitric 云感知应用框架

例如，[Nitric](https://nitric.io/?utm_content=logo-sponsorpage&utm_source=thenewstack&utm_medium=website&utm_campaign=platform) 是一个“云感知”的开源框架，Siva解释说，它通过事件、队列、文档存储和存储桶等操作自动执行运行时的代码。他说：“我们直接从您的代码中推断基础架构，并为您自动进行配置。”

Nitric 属于较少代码的范畴，至少在较小的规模上，它可以替代 Kubernetes 编排。“如果您不使用 Nitric，您将手动编写单独的 Terraform 或任何基础架构即代码（IaC）项目，”Siva 说。Nitric 建立在 IaC 的 Pulumi 和一些 Terraform 之上，以便为云部署的最佳实践提供自动化框架。

“我之所以说‘较少的代码’，是因为在抽象出某些内容时，您基本上是采用了[最佳]实践，并使它们可复制，”Siva 解释说。“在一天结束时，最终用户编写的代码较少，因为他们正在利用您的抽象，因此他们的代码库中的重复性被剥离。”

Nitric 基于三大主要云提供商的观察到的模式——谷歌云、Azure云和[亚马逊Web服务（AWS）](https://aws.amazon.com/?utm_content=inline-mention)。每个提供商都有托管服务，包括 API 网关、计算、文档存储、存储桶以及用于事件和队列的 Pub/Sub，它们的功能是相同的。这些功能通常通过基础架构即代码（IaC），如 [Pulumi](https://www.pulumi.com/?utm_content=inline-mention) 和 [HashiCorp](https://www.hashicorp.com/?utm_content=inline-mention) 的 Terraform ，组合在一起。然后，Nitric 是在这些 IaC 的基础上构建的，允许开发人员部署到云中的存储桶，规则和策略由您的运营或 DevOps 团队设置。

托管服务被认为是组织优化其云使用和成本的最佳实践——在全球计算短缺的情况下，这更加重要。云成本仍然是[环境影响](https://thenewstack.io/want-to-save-the-world-start-by-cutting-your-cloud-costs/)的主要代理人——效率更高、托管代码的碳足迹更小。

同样更具计算效率的是，Nitric 允许开发人员在模拟云的本地运行时体验中运行其代码，因此开发人员可以编写和迭代他们的代码，而无需在准备好投入生产之前将其容器化并部署到云中。

## 平台工具必须具有可扩展性

随着代码堆栈的复杂性不断增加，软件开发人员的角色也变得越来越复杂。这一情况又因较小的团队不得不用更少的资源做更多的事情而变得更加糟糕。突然之间，开发人员可能需要了解现代软件堆栈的七个层次，包括 Kubernetes 、网络、可观察性、存储、安全性以及部署到云中。这使得他们分心，远离了他们的主要目标，即更快地为最终用户提供价值。

如今的 DevOps 成功是关于抽象，而不是阻碍和分散注意力。是护栏，而不是大门。这就是为什么成功的平台工程必须管理基本问题，同时仍然具有高度的可扩展性。内部开发者平台和周围的工具应该能够使开发团队更快地移动，而不是创建人为的障碍。在需要的地方，像请购票证这样的策略应该决定何时打开或关闭大门。

Nitric 开源框架一开始是非常有主见的，Siva 承认：“第一个版本，我们知道需要什么，所以我们将代表您进行配置，”但是任何运维团队都可以分支它，按照文档上的说明来扩展或完全更改提供者，从而更改与之相关的资源，以及如何将该存储桶部署到每个云。

例如，Nitric 的开箱即用版本部署为以无服务器方式运行的容器化 lambda 。但是，您可以修改底层的 Pulumi 代码，将提供者更改为作为 AWS 的 EC2 实例运行。

平台工程使得 DevOps 组织可以继续像一个整体一样运行，但是在开发人员和运维任务之间重新设置了一些障碍，因此开发人员不需要了解完整的堆栈。

“实际上，我们在分离关注点。开发人员说：我想在云中的某个地方运行这个执行上下文——我关心的只是它能运行，” Siva 说。“但基础设施团队可以确定如何在云中运行它，以及为实现这一目标而配置了哪些资源。通过进行这种分离，我们实际上允许人们构建自己的平台——如果他们想要的话。”

尽管在平台工程领域是一个框架，但 Nitric 专注于基础设施团队使用较少的代码来获得更多的控制。Siva说：“它使他们能够始终以相同的方式部署相同的资源，无论哪个开发团队请求它。”而且，由于并不是所有的应用团队都是一样的，“我们根据每次部署提供配置，以确定是否应该为您提供高 CPU 、低 CPU 或配置，您可以在 Nitric 中定义这些配置。”

运维工作的减少通常也意味着开发工作的减少。

“您会发现，开发团队实际上最终会参与到基础设施的供应中，无论是通过支持工单还是战斗室或其他方式，因为他们的东西在运行时通常不会工作，”他说。通过正确的平台工具，“他们不需要真正担心基础设施，因为它保证能够工作”，因为平台团队使他们“能够始终以相同的方式部署相同的资源，无论哪个开发团队请求它。”

## 平台工具是否可以成为 DevOps 工程师的临时解决方案？

对于刚刚开始 DevOps 之旅的自助创业初创公司，平台工程至关重要，但可能找不到或无法承担现在雇佣 DevOps 人员。

“我们正在消除创业公司所需的低级别或重复性活动，但是当真正建立了规模并且实际上实现了增长时，他们将需要一个运维人员，” Siva 说。“但是那个运维人员不会把时间浪费在琐碎的活动上。他们将把时间花在为组织提供有价值的活动上。”

在面对 DevOps 人才短缺的情况下，这在所有规模的公司中也可能是个案，开发人员不得不进行补偿并承担两个工作——他们的常规工作和运维工作，后者对他们来说成为了非差异性的重复性工作。这不仅使团队少了一个运维工作者，还少了一个开发人员。正确的平台工具链可以减轻这两种能力的负担。

对于 Nitric 框架，Siva 说：“我不认为这是消除运维团队的工具。我们希望赋予运维团队权力，并阻止他们复制和粘贴 Terraform 或执行重复性任务，让他们专注于更重要的事情，比如确保应用程序使用正确的工具，准备好进行扩展，并得到维护和运行。”

最后，较少的代码平台工程选项也可以帮助平台团队，通过抽象出 CI/CD 和基础架构供应。平台团队的演变可以从运维重点转向更多的开发人员体验，他们可以专注于为内部客户（包括软件开发和运维团队）提供业务价值驱动力。

[![免费电子书：平台工程：您现在需要了解的内容](https://cdn.thenewstack.io/media/2023/08/7dfbd08f-free-platform-engineering-book.png)](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/)