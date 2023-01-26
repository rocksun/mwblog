# 平台工程师：开发人员是您的客户

本文翻译自 [Platform Engineers: Developers Are Your Customers](https://tanzu.vmware.com/content/analyst-reports/innovation-insight-for-internal-developer-portals?utm_source=cote&utm_campaign=devrel&utm_content=TNSdevcustomers)。

您的平台如何适应您组织的实践、需求和文化将使平台工程团队变得有价值。

![](https://cdn.thenewstack.io/media/2023/01/92013d04-developers-1024x683.jpg)

如果您是一个构建平台工程团队的组织，那么该团队的新客户就是应用程序开发人员。这似乎是显而易见的，但它与基础设施建设者考虑的通常的工作方式有着巨大的不同。[交付服务](https://www.techtarget.com/searchitoperations/definition/IT-service-delivery-information-technology-service-delivery)和将平台作为产品进行管理有着非常显著的区别。

虽然平台已经存在了几十年，但将平台视为产品的概念源于 DevOps 社区，例如 Netflix 的工具组、SRE 原理、Pivo​​tal（现为 VMware Tanzu）的实践、“[Team Topologies](https://www.youtube.com/watch?v=IISozt7zc9I)”、Thoughtworks 等等，还有许多其他的。

通过研究多年来构建和运行这些平台的平台工程团队，我们发现采用最成功的组织是那些转向产品思维并将其内部开发人员团队视为客户的组织。在我们了解产品管理平台意味着什么之前，让我们从什么是平台开始。

## 产品：平台

平台是开发人员用来构建和运行其应用程序的框架、中间件、工具和实践。 Thoughtworks 的 Evan Bottcher 在 2018 年更[准确地定义了粘合层](https://martinfowler.com/articles/talk-about-platforms.html)：

“数字平台是自助服务 API、工具、服务、知识和支持的基础，它们被安排为引人注目的内部产品。自主交付团队可以利用该平台以更快的节奏交付产品功能，同时减少协调。”

您可以将其视为基础设施层之上的一切，无论该基础设施是基础设施即服务 (IaaS)、裸机、虚拟化还是 Kubernetes。在云原生商店中，Kubernetes 提供了闪烁的光标，有时也称为“拨号音”，平台就是你堆放在 Kubernetes 上面的所有东西，这样开发人员就可以开始编码，你可以开始在生产环境中运行他们的应用程序。

在过去的一年里，[内部开发人员门户 (IDP)](https://tanzu.vmware.com/content/analyst-reports/innovation-insight-for-internal-developer-portals?utm_source=cote&utm_campaign=devrel&utm_content=TNSdevcustomers) 已被添加到被认为是“平台”的组件中。 IDP 的定义各不相同（Gartner 在[定义它方面做得很好](https://tanzu.vmware.com/content/analyst-reports/innovation-insight-for-internal-developer-portals?utm_source=cote&utm_campaign=devrel&utm_content=TNSdevcustomers)），但我们认为它是多年来所有[老式应用程序生命周期](https://youtu.be/izHE64nBFeY)所一直缺失的管理内容。

它是开发人员用来支持内部采购、发现其他可用团队和 API、跟踪他们自己的应用程序和文档的内部网，顾名思义，它是组织需要的所有信息辐射器和单一管理平台的门户框架。

目前，Spotify 的开源项目 Backstage 是构建 IDP 的非常有趣的基础。 Backstage 被证明是一种很好的方法来标准化 IDP 的外观，同时为自定义留出足够的空间。

它的目的是帮助大公司的开发人员更好地相互合作，它表明了这一点。我们在 [VMware Tanzu Application Platform 中拥有良好的使用体验](https://www.youtube.com/watch?v=GAzKCQO8Vt0)。

平台的无供应商图表并不多（我很高兴向您展示 VMware 的图表！），但是来自 CNCF 工作组的这张定义“平台”的图表非常好：

![](https://cdn.thenewstack.io/media/2023/01/6a568c9d-image2.png)

因此，可以快速了解什么是平台。

## 客户：开发人员

在过去的 10 年里，我们吸取了很多平台工程经验。平台成功的最重要教训是了解您的客户是谁。在平台的情况下，这些客户就是开发人员。

第一步是了解您的客户需要什么：他们的目标是什么、他们的工作方式、[他们遇到的问题](https://tanzu.vmware.com/content/analyst-reports/forrester-vmware-executive-checklist-for-devex?utm_source=cote&utm_campaign=devrel&utm_content=TNSdevcustomers)以及什么对他们有效。也就是说，您想开始为他们的开发人员体验建立一个想法和品味。此外，您需要了解什么对组织和其他利益相关者（通常是安全、治理和 FinOps 人员）有价值。

这里的“你”是产品经理，在一些平台团队中也被称为“产品负责人”。值得庆幸的是，产品管理是一个非常成熟、有据可查的角色，其流程我们可以适应。 Syntasso 的 Paula Kennedy 是平台即产品方法的早期支持者之一，她总结了[平台产品经理的工作](https://youtu.be/jJSo3kdflpA?t=1020)：

产品经理可以帮助定义产品策略。他们可以帮助制定产品路线图。他们可以管理准备交付的特性 backlog ，并通过数据驱动的决策和验证假设帮助确定这些功能的优先级。

产品经理决定平台中包含哪些功能和服务以及何时实现它们。为此，产品经理会与开发人员和组织中的其他人讨论、研究并了解在生产过程中需要什么。

产品经理不断地平衡几件事，其中包括：

1. 开发者需要解决哪些有价值的问题？
1. 使用平台中的功能解决这些问题的最佳方法是什么？
1. 应该如何实施功能以满足整个组织的需求，而不仅仅是个别开发人员？
1. 识别风险及其补救措施

所有这一切不仅是通过直觉完成的，而且还遵循经过验证的设计方法，通过数据驱动的研究和测试来完成。

## 去开发者所在的地方

如果他们还没有[使用像 Cloud Foundry 这样的平台](https://www.vmware.com/explore/video-library/video-landing.html?sessionid=1655951656875001wz8N&videoId=6315283627112)，我们与之交谈的大多数基础设施团队都专注于构建基于 Kubernetes 的平台。这些团队通常遵循相同的方法，也就是所谓的服务交付方法。

具有服务交付意识的团队收集性能和容量需求，了解未来几年将在集群上运行多少工作负载、安全和生产需求等。然后他们构建了“kool korporate Kubernetes kloud”并或多或少地完成了。他们已经提供了服务，现在只需确保其可用性即可。

现在，开发人员可以来获取他们想要的所有 Kubernetes——或者在他们的配额允许的范围内获取。这种方法更像是一种项目思维方式，而不是产品思维方式，因此它为我们提供了一种思考如何对平台进行产品管理的好方法。

这种以项目为导向的方法的问题在于，开发人员需要的不仅仅是 Kubernetes 闪烁的光标；他们需要持续的帮助来弄清楚他们在 Kubernetes 之上需要什么工具。而且，您很有可能无法提前预测该技术栈如何满足您组织的独特需求。您需要发现和发展它，检验理论……也就是说，对其进行产品管理。

为此，您应该从开发人员开始，了解他们每天都在做什么。有两个常见的事情可以开始：规划生产路径和改进开发人员使用引导。

生产路径基于[价值流图](https://tanzu.vmware.com/developer/practices/value-stream-map/?utm_source=cote&utm_campaign=devrel&utm_content=TNSdevcustomers)，该图绘制了从构思到设计、编码、部署以及让使用软件的人员交付价值所需的所有活动。这是一个假设的例子：

![](https://cdn.thenewstack.io/media/2023/01/af8edbf8-image1.png)

请务必与实际用户一起验证此旅程地图！理解这个价值流图将使平台团队持续了解他们的客户，即使不是每项活动都是平台团队的责任。

映射此路径后，您可以开始寻找要解决的问题。其中许多问题将消除浪费，通常是通过删除不必要的步骤、改善不同团队之间的协作（通常称为“左移”）以及自动化沿途的流程。

另一个常见的起点是开发人员参与流程。在今年的[一项调查中](https://tanzu.vmware.com/content/analyst-reports/forrester-vmware-executive-checklist-for-devex?utm_source=cote&utm_campaign=devrel&utm_content=TNSdevcustomers)，大型组织中大约 50% 的经理表示他们对开发人员的引导时间不满意。因此，例如，您可能会确定开发人员从头开始使用您的平台需要多长时间。

另一个版本可能是衡量新开发人员贡献有意义的代码需要多长时间才能走完[黄金路径](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/)。我建议通过运行定期的调查[来查找和跟踪消除开发人员的苦力活](https://tanzu.vmware.com/content/white-papers/developer-toil-the-hidden-tech-debt?utm_source=cote&utm_campaign=devrel&utm_content=TNSdevcustomers)，将会非常有用。

当您从开发人员开始时，您可以更好地管理平台中的产品。这不仅是选择最适合的功能，而且还优先考虑你如何度过你的时间。

> 开发人员通常想要最新最好的东西——任何看起来既酷又有用的东西。但是，即使是 100 名左右的开发人员之间的差异已经很大了，更不用说 25,000 名，这会损害整个组织。

如果你从底层开始，例如只使用 Kubernetes，你可能会构建出超出需要的东西，你可能会错过添加一个适合你的 Java 开发人员（或任何类型）的服务网格，而且你肯定不会能够学习和调整您使用的工具和内部开发人员门户方法。

以下是平台团队解决的常见问题和功能的一些示例：

- 标准化构建流水线并自动生成[物料清单](https://tanzu.vmware.com/software-bill-of-materials?utm_source=cote&utm_campaign=devrel&utm_content=TNSdevcustomers)以确保合规性和安全性
- 自动启动开发人员环境
- 建立和改进内部协作工具，例如内部开发人员门户
- 寻找打包和配置新应用程序以在平台上运行或减少修改应用程序以在平台上运行所需时间的方法
- 修改引导门户以添加更多自助服务特性
- 额外的支持服务（或“中间件”），例如 MySQL、RabbitMQ 或 Spring Cloud 服务
- 用于横切关注点的标准工具包，如安全、日志记录、metrics 和负载平衡
- 与其他企业系统集成，尤其是您的内部系统
- 具有不同服务级别目标 (SLO) 和生产特性、行业法规和云主权支持的平台的多个变体

这些团队所做的最困难的事情之一是平衡开发人员的需求与组织范围的标准。开发人员通常想要最新最好的东西——无论是编程语言、部署方法（还记得 Docker 什么时候是什么奇怪的东西吗？还是虚拟化？）、新工具和框架……任何看起来既酷又有用的东西。但是，即使是 100 名左右的开发人员之间的差异已经很大了，更不用说 25,000 名，这会损害整个组织——例如局部优化还有其他等等。

> 有价值的是您平台的所有定制，这些定制可以提高开发人员的工作效率。

这是我们希望产品管理能够处理的问题。当您像对待客户一样对待开发人员时，您会更渴望为他们提供他们想要的东西，并投入额外的工作以使其可持续发展。

相反，如果您只是提供一组预先确定的服务，虽然您可能并不打算这样做，但更容易滑入“只使用已批准的企业架构”。我认为将 Java 应用程序服务器的简化为 Spring、JBoss 和 Rails，开发人员转向 Docker，以及 WS-* 和企业服务总线之类的失宠表明集中式平台存在这个问题，这些平台未能将开发人员视为客户。

## 超越闪烁的光标

问题是，您将最终得到一个与上图类似的平台。但这不会是您平台中最有价值的部分。您的平台如何适应组织的实践、需求甚至文化（在 DevOps 意义上）将使平台工程团队变得有价值。

当您从开发人员开始时，您会发现平台工程团队可以解决的最具影响力的问题。它不会是成本管理、安全甚至多云全球控制平面魔法。所有这些都是必需的，但实际上，它们是商品、工业标准功能，或者很快就会成为这样。

有价值的是您平台的所有定制，这些定制可以提高开发人员的工作效率。以及构建它们的顺序。产品经理所做的很大一部分工作是确定所有事情的优先级，并确保专注于在最短的时间内增加最大的价值。

从平台即产品的角度思考并将产品管理落实到位是组织中良好平台工程的关键，尤其是大型组织。第一步：最好找个产品经理。