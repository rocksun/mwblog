<!--
title: 不止Terraform：如何扩展DevOps
cover: https://cdn.thenewstack.io/media/2024/02/b5261c11-stairway-1024x576.jpg
-->

这是我们在旅程中学习的教训，以克服DevOps的挑战，为后续的扩展奠定基础。

> 译自 [Beyond Terraform: How We Scaled DevOps](https://thenewstack.io/beyond-terraform-how-we-scaled-devops/)，作者 Malcolm Edgar 是Drop Bio Health的首席技术官，这是一家通过血液生物标志物和生活方式分析在家提供健康跟踪的公司。他之前曾担任金融科技公司Avoka Technologies的首席技术官，并获得了一项加密方法专利。

这是两部分文章的第一部分。

成为一个新兴科技公司的首席技术官，有点像在玩杂耍火把。保持敏捷、快速和安全的责任往往会压垮小型团队，尤其是因为云开发的复杂性。在2023年，我的公司[Drop Bio Health](https://www.dropbiohealth.com/)通过血液生物标志物和生活方式分析在家提供健康跟踪，决定简化云开发以专注于核心产品价值开发。

我一直在重新考虑我们的[DevOps方法，以提高团队效率](https://thenewstack.io/best-practices-for-adopting-a-devops-culture/)、增加我们的部署频率并进一步加强安全协议。这里是我们在这次旅程中学到的教训的故事，以克服DevOps的挑战并为可扩展增长建立自己。

## Terraform实验: 一个让我们花费时间和注意力的绕路

与许多团队一样，我们首先与[AWS](https://aws.amazon.com/?utm_content=inline-mention)云开发工具包(CDK)一起走上了Terraform之路，希望它能成为我们云基础设施问题的灵丹妙药。然而，这次旅程引入了许多意想不到的DevOps复杂性，不仅消耗了我们团队不可持续的时间，而且分散了我们对[核心产品开发](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/)的注意力。  

Terraform的声明性性质意味着一切，包括资源及其配置，都必须明确定义。随着我们的架构的增长，代码行也在增长 - 运行到成千上万行。这个庞大的代码库变得越来越难以管理。

此外，维护一个仅用于基础设施的专用项目意味着我们发现自己在两个主要项目之间来回切换: 一个专注于我们的应用程序，另一个仅针对基础设施。这种分工在我们的团队内[制造了不必要的隔阂](https://thenewstack.io/top-challenges-to-creating-high-performing-engineering-teams/)，并对确保我们的应用程序和基础设施更改保持同步提出了挑战。

测试Terraform也提出了其独特的一系列挑战。鉴于其面向配置的性质和缺乏直接的测试框架，测试更像是模式匹配而不是常规的逻辑验证。因此，调试更多地是侦探工作而不是解决问题。

随着我们的Terraform代码库的扩展，很明显需要分割来进行管理。然而，这种看似谨慎的决定，将配置拆分到多个文件和目录中，使追踪依赖关系和整体理解变得更加困难。回顾起来，我们进入Terraform世界的旅程，虽然开始是很乐观的，但逐渐变成了复杂性的泥沼。我们需要一个变化，这样我们就可以把更多宝贵的时间和资源花在我们的业务目标上，而不是手动的DevOps任务上。

## 进入: 基础设施自动化

虽然我们正在努力抵消这些复杂性，但市场正在以惊人的速度发展，任何延误都可能意味着错失机会。在这种环境下，管理开发和运维的压力开始给我们的团队带来负担。

我开始看新的基础设施方法，寻找自动化来解决我们在基础设施即代码工具(如CDK和Terraform)面临的挑战。最新的从代码中的基础设施创新非常适合帮助我们的小团队快速高效地进行工作。我们使用[Nitric](https://nitric.io/)(请查看[GitHub上的开源项目](https://github.com/nitrictech/nitric))，它根据我们的代码自动提供所需的基础设施，并提供意见鲜明的最佳实践来帮助我们以高效和自信的方式进行云部署。

我们的基础设施和部署流程要简单得多，使我们的团队可以自由地专注于开发我们的核心业务功能并按需部署。Nitric提供的自动化意味着我们可以扩展DevOps，同时绕过Terraform的常见挑战。 

作为Nitric实施的一部分，我们也重新审视了我们的应用程序架构。这导致了一些关于可扩展性、安全性和成本的改进(AWS托管成本降低60%)。在第二部分中，我将分享我们学到的架构课程和我们取得的成果。

您也可以在[这篇文章](https://nitric.io/case-studies/dropbio)中了解有关我们在这个项目中的成功的更多信息。
