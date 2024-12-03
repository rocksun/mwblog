# DevOps为何倒退以及我们如何解决

![Featued image for: Why DevOps Is Backward and How We Can Solve It](https://cdn.thenewstack.io/media/2024/11/e030a842-devops-1024x586.png)

即使在科技领域，书面语言也能出人意料地影响我们对技术应用方式的理解。

将开发和运维合并的概念[已经存在](https://platformengineering.org/talks-library/devops-is-dead-long-live-platform-engineering)了[大约15年](https://blog.mindgrub.com/the-rise-and-fall-of-devops)。缩写为常用的术语“[DevOps](https://thenewstack.io/devops/)”，它已被广泛用于描述大多数已建立的软件开发、部署和支持。近年来，加入了“安全”（sec），DevSecOps现在代表了软件应该如何开发。

但现实是应用程序开发是首要的。只有在代码编写完成后，团队才会[完全定义基础设施、安全要求和流程](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/)，以使应用程序顺利投放市场并运行。然后是完善的架构，之后是结构良好的[CI/CD管道](https://thenewstack.io/ci-cd/)，新的功能和错误修复可以无缝地编写和部署。但我们并不生活在那个理想的世界中。

## DevOps还是OpDev？

也许“DevOps”这个词比“OpDev”更朗朗上口，但可以说，由于开发是首要的，运维将会紧随其后。但是，如果我们仔细观察，大多数公司实际上都在运行“OpDev”管道，即使他们没有意识到这是如何在组织内部产生的。

每次开发人员导入云提供商的软件开发工具包（SDK）或通过命令行（CLI）访问资源时，开发人员都获得了[构建运维基础设施以完成任务的机会](https://platformengineering.org/talks-library/devops-is-dead-long-live-platform-engineering)。身份验证？数据库需求？无服务器函数？这些都至少以编程方式提供给开发团队。

除非是一家发展迅速且不太严格的初创公司（我们可以讨论为什么即使在这里也不是一个好主意），否则安全和运维团队需要评估源代码中请求的资源，并在代码编写后构建一个管理框架来提供该基础设施。

在上面讨论的理想世界中，如果合并的团队在开发开始之前都同意了一套明确的需求和项目架构，这可能不是问题，但即使是最好的计划也无法经受住第一次考验。我们甚至不要谈论代码更改请求（PR）、功能添加和重构对架构造成的麻烦。

如果没有非常严格的CI/CD管道和（通常）许多团队成员维护基础设施的安全性和成本效益，运维将是一项西西弗斯式的任务，最重要的是它很慢。

## 解决问题

因此，我们需要一种更好的方法来处理基础设施，而不会将运维团队变成消防员而不是合作的团队成员。相应地，我们希望使开发人员能够不受严格规则集的限制进行构建，同时保留敏捷的特性和快速的开发速度。

[这个问题有一些不同的解决方案](https://cd.foundation/state-of-cicd-2024/)。最明确的方法是抽象掉基础设施以及常见的开发方法，并用一种全新的语言替换它们。
一个全面的解决方案是一种通用的[编程语言](https://thenewstack.io/programming-languages/)，旨在开发整个云应用程序，包括其基础设施和应用程序代码。虽然这解决了所有问题，但这对于大多数团队来说都是一项巨大的工作。绝大多数开发人员都熟悉一套完善的语言，或者正在使用用遗留语言编写的现有代码库。

更现实且易于操作的方法，例如[Nitric](https://nitric.io?utm_content=inline+mention)，将平台即服务 SDK 从代码库中抽象出来，并将开发人员的基础设施需求替换为一个工具库，无论最终代码部署在哪里，都可以完全相同地引用这些工具。运维团队可以轻松地在集中位置维护所需的 infra 模式，从而减少在代码 PR 后解决问题的需要。
也许我们需要另一个术语来描述[这个流程](https://circleci.com/blog/platform-engineering-devops-at-scale)，比如[平台工程](https://platformengineering.org/talks-library/devops-is-dead-long-live-platform-engineering)，或者我们可以保留现有的DevOps术语。但无论使用什么语言，我们都需要重新思考我们提供给开发人员用于基础设施的工具：将架构流程中的运维部分与应用程序开发放在相同的时间框架内。

使用基于HCL和Pulumi标准的[新的后端框架工具](https://nitric.io/blog/nitric-is-terraform)，这些标准已被绝大多数开发人员使用，这是一种 surprisingly simple 的方法，可以解决许多问题，包括与现有漏洞扫描工具和流程的干净集成。并且随着现代编码AI工具的发展，重构遗留代码库以集成标准基础设施后端也变得越来越容易。

DevOps 仍然落后吗？更有可能的是，它以其原始形式仍然活跃。它只需要一种更好的方法让开发人员和运维人员一起工作。DevOps万岁。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。