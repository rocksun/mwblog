
<!--
title: Pulumi 模式与实践平台 (P3)：面向大型组织的参考架构
cover: https://www.pulumi.com/blog/pulumi-patterns-and-practices/meta.png
-->

Pulumi 模式与实践平台 (P3) 是一个基于 Pulumi 的内部平台的参考架构，用于在大型环境中进行基础设施管理和安全部署。

> 译自 [Pulumi Patterns and Practices Platform (P3): A reference architecture for large-scale organizations](https://www.pulumi.com/blog/pulumi-patterns-and-practices/)，作者 None。

基础设施管理一直都是一件有趣的事情，直到你发现自己在 AWS 控制台中滚动浏览 1000 多个资源。更糟糕的是，当一个不靠谱的产品团队想要使用 Azure，而你的数据团队想要使用 GCP 时，你将在 Azure 中进行 ARM 摔跤，并看着你的规模经济向错误的方向倾斜，因为你正在将 CloudFormation 模板复制粘贴到另一个 git 仓库中。这。需要。成为。一个。平台！

在那一刻的不知所措中，你会被推销，每周都会收到培养邮件，并被告知你所有的问题都将通过实施 IDP（内部开发平台，就好像你以前从未见过这个首字母缩略词一样）来解决。一个需要花费大量资金和时间来实施的 IDP，超出了默认设置。一个实际上只解决你一半问题的 IDP。你的内部团队提供构建一些东西，感觉更像是将随机代码片段焊接在一起，形成一个由垃圾场废料制成的抽象的现成品雕塑，已经过时 5 年了。这项投资将在多久后变得无用，你必须重新开始？

这太令人筋疲力尽了。如果市场上有一个好的解决方案，你就不必阅读这篇文章。所以让我们谈谈你真正需要什么，以及 Pulumi 如何提供帮助。

## 有效的内部开发平台

有很多 [列表文章](https://en.wikipedia.org/wiki/Listicle) 声称权威地告诉你内部开发平台的 5 个、7 个或 11 个基本组成部分。就我个人而言，我相信我们的客户会告诉我们，以下就是他们所说的需求：

- **一致性**：为混乱带来秩序。随着你的公司和基础设施的增长，保持一致性变得越来越复杂。你可能已经建立了想要复制的设计模式，但你没有办法在当前工具中对这些实践进行编码。有很多可重复使用的代码块的复制粘贴，但没有办法应用 [DRY 原则](https://www.youtube.com/watch?v=5xw04T20lto&t=7s)或将重要部分模块化/模板化（提示：所有部分都很重要！）。
- **可重复性**：可重复的行为，谁知道呢？如果你运行两次部署，每次都会得到相同的结果吗？如果你复制生产环境来创建测试环境，它们实际上是相同的吗？让它们变得相同需要多少额外的工作？每次运行 AI 工作负载时，你都会获得相同版本的训练数据集吗？谁知道呢。缺乏可重复性会减慢开发速度，使调试更加困难，并使我们刚刚讨论过的重用更难实现。
- **可见性**：当你的节点数量和用户数量开始超过大约 50-100 个资源（计算或人类）时，你很快就会遇到可见性问题。很难掌握正在发生的事情，你有多少资源，它们在哪里，以及它们花费了多少。任何声称能够管理 1000 个或更多节点的系统都必须具有深度集成的分析、仪表板、图表，并且能够搜索，涵盖所有云、所有用户和所有类型的资源。
- **安全性和合规性**：良好的围栏造就良好的邻居。RBAC、策略即代码、出色的密钥管理、与现有身份提供者的集成。这些是你构建可以依赖的安全和策略护栏所需要的。没有它们？这只是一桶装满炸药的责任，等待着火花。
- **可审计性**：发生了什么以及谁做的？这就像一场高风险的[线索](https://en.wikipedia.org/wiki/Cluedo)游戏。你能多快地找出谁运行了那个糟糕的部署？是*芥末上校*在*图书馆*用*烛台*吗？还是 Blake 这个新来的前端开发人员在 AWS 中拥有过于广泛的权限？能够快速回答这些问题。快速，就像几分钟，而不是几小时或几天。而且它可能发生在 6 个月前。哎哟。
- **开发人员体验**：在理想的世界中，开发人员驱动自己的 DevOps。平台团队提供自助服务工具和简化的工作流程，允许你的工程师配置新的资源，这样你的团队就不必这样做。而且你知道，如果开发人员不喜欢用户体验，他们根本不会使用它，并且会发明自己的工具。你将有 ROGUE 系统需要追踪，并在冗长乏味的过度技术性会议中进行争论。这不是你想要的。我们需要让开发人员保持快乐，以防止这种情况发生。

## 模式与实践平台参考架构的整体视图

Pulumi 拥有广泛的 [产品和功能](https://www.pulumi.com/product/) 来满足这些需求。我们的工具从一开始就以集成为设计理念，它们可以很好地协调，为运营团队和开发团队提供流畅简化的工作流程。

我们有一个想法，可以将所有 Pulumi 产品整合在一起，为安全、基础设施管理和部署提供一个全面的内部平台。如果你愿意，可以称之为 [内部开发平台工程师平台](https://www.pulumi.com/what-is/what-is-platform-engineering/) (IPfDPE)。我们称之为多年来一直努力构建的愿景的实现。

**Pulumi 模式和实践平台 (P3)** 是一个参考架构，我们将通过本系列文章对其进行描述并提供代码。我们将深入探讨不仅可以使用我们的工具做什么，还可以如何使用它们，并提供参考实现的代码，您可以使用它来启动该过程。

以下是一个快速概述，让您了解我们将如何在 Pulumi 模式和实践平台 (P3) 中解决这些需求。

### 一致性

Pulumi 可以通过将设计模式编码到可重用的 *组件资源* 中，以及通过构建自定义*提供无代码或低代码方式来启动新项目。模板有助于更快地启动项目，并确保一致的代码结构、策略合规性和最佳实践。*

除此之外，由于 Pulumi 是 [多云](https://www.pulumi.com/blog/deploy-to-multiple-regions/)（AWS、Azure、Google Cloud 等）和 [多语言](https://www.pulumi.com/blog/pulumiup-pulumi-packages-multi-language-components/)（JavaScript、Python、Go、C#、Java），因此您可以在所有环境和所有开发团队中享受相同的一致性，无论他们偏好的语言或所需的云工具。

一致性的另一个核心方面是 *漂移检测*。Pulumi 会自动检测并修复与存储在 Pulumi Cloud 中的预期状态偏离的云资源。这项技术比布洛芬更能消除开发人员造成的头痛。

### 可重复性

自 2010 年以来，科学家们一直认为我们正处于一场危机之中——一场 *可重复性危机*——我们无法轻松地重复实验以验证已发布的结果。同样，软件行业也正在进入自己的可重复性危机，尤其是在 AI 训练工作流程方面，越来越难以重新创建关键的构建和生产环境。[Pulumi 堆栈](https://www.pulumi.com/learn/building-with-pulumi/understanding-stacks/) 使得跨多个环境管理配置和状态变得非常容易，并且使[在 Pulumi 中复制部署](https://www.pulumi.com/blog/simple-reproducible-kubernetes-deployments/)成为几个基本操作的问题。

您可以使用 Pulumi 程序来捕获 *所有* AI 训练工作负载所需的资源，包括诸如[版本化数据](https://www.pulumi.com/ai/answers/xig35anR7ibjAP5MhHDyxC/time-travel-queries-on-snowflake-dynamic-tables)使用具有时间旅行功能的动态表[Snowflake](https://www.pulumi.com/case-studies/snowflake/)。这意味着您可以确保您的部署不仅将在您需要的基础设施上，而且每次都将拥有确切的版本数据，这对于 A/B 测试和调试您的模型至关重要。

### 可见性
Pulumi 管理下的每个资源都可以在 [Pulumi Insights](https://www.pulumi.com/product/pulumi-insights/) 中看到。从这个单一窗格界面，您可以搜索所有云环境中的资源。[Pulumi Copilot](https://www.pulumi.com/product/copilot/) 提供最先进的 AI 聊天界面，可以提出复杂的问题并立即获得结果。Pulumi Insight 的分析使您能够识别资源使用中的异常或趋势，并深入了解成本、安全性和合规性问题。

![图：使用 Pulumi Insights 搜索任何资源](https://www.pulumi.com/uploads/pulumi-insights-search.gif)

*图：使用 Pulumi Insights 搜索任何资源*

### 安全性和合规性

在现代术语中，当您说 DevOps 时，您指的是 DevSecOps。Pulumi 旨在默认安全。Pulumi Cloud 提供完整的 [基于角色的访问控制 (RBAC) 功能](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/)，包括与 [GitHub 团队](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/#github-based-teams) 和 [基于 SAML 的 SSO](https://www.pulumi.com/docs/pulumi-cloud/access-management/saml/) 的深度集成，以及 [Pulumi ESC](https://www.pulumi.com/product/esc/) 提供的托管密钥和灵活定义的安全环境，以及 [Pulumi Crossguard](https://www.pulumi.com/crossguard/) 提供的策略即代码。最重要的是，所有这些功能都深度集成到整个平台中，创建了一个严密的系统，拥有您管理安全和访问所需的所有护栏。

### 可审计性

用户在 Pulumi 中执行的每个操作都可以通过 [审计日志](https://www.pulumi.com/docs/pulumi-cloud/audit-logs/) 进行跟踪，该日志可以在 Pulumi Cloud 主页仪表板中通过两次点击进行搜索。审计日志可以通过一次点击按用户进行筛选。创建审计日志的自动备份是一个 [一流的功能](https://www.pulumi.com/docs/pulumi-cloud/audit-logs/#automated-export)。您永远不必担心在有人询问系统中发生的事件时快速响应。此外，每个部署和更新都有日志直接从 Pulumi Cloud 应用程序可见，无论它是如何启动的。

![图：在 Pulumi Cloud 中查看审计日志](https://www.pulumi.com/images/docs/guides/self-hosted/auditlogs.png)

*图：在 Pulumi Cloud 中查看审计日志*

### 开发人员体验

也许 Pulumi 最引人注目的方面是开发人员体验。[开发人员喜欢 Pulumi](https://www.pulumi.com/testimonials/)，因为他们可以使用自己喜欢的工具。通用编程语言、可视化 IDE、命令行工具以及具有 API 驱动架构的产品是开发人员想要的，也是 Pulumi 大量提供的。

有了 Pulumi 模板和自定义内部组件资源，[开发人员可以驱动自己的 DevOps](https://www.pulumi.com/blog/software-developer-experience-devex-devx-devops-culture/#how-does-devex-intersect-with-devops)，直接配置自己的基础设施资源并管理自己的部署，减少平台团队的瓶颈。产品工程团队可以通过简化的工作流程进行自助服务，该工作流程默认情况下符合公司政策。在他们最喜欢的编程语言的代码深处，您的开发人员甚至不会知道他们正在遵循公司规则。

![图：使用 C# 在 VS Code 中编写 Pulumi 程序](https://www.pulumi.com/blog/pulumi-patterns-and-practices/pulumi-ide.png)

*图：使用 C# 在 VS Code 中编写 Pulumi 程序*

### 更多内容即将推出

因此，既然我们已经说明了如何将 Pulumi 应用于满足大型组织最迫切的需求，希望您会意识到我们在此介绍的 Pulumi 模式和实践平台 (P3) 参考架构不仅仅是基础设施即代码。P3 是一个由 Pulumi 提供支持的团队平台，您的开发人员门户不仅仅是软件目录，而是在所有云环境中完全可用的控制平面。

敬请关注以下系列文章，我们将使用 Pulumi 为功能齐全的内部开发人员平台 (IDP 或 IPfDPE，如果您愿意) 实现 P3 参考架构。也就是说，您可能已经投资了一些流行的云原生工具，例如 [Backstage](https://www.pulumi.com/blog/pulumi-in-a-cloud-native-world/#the-kebap-stack-reference-architecture) 或 [Kubernetes](https://www.pulumi.com/blog/kubernetes-4-0-even-more-kubernetes-native/)。Pulumi 与其他工具配合良好，您会很高兴看到 [如何使用 Pulumi 来弥补](https://www.pulumi.com/blog/pulumi-in-a-cloud-native-world) [CNCF](https://www.cncf.io/) 生态系统中的差距。

如果您已经准备好在这篇介绍之后开始使用 Pulumi，请随时 [创建帐户](https://www.pulumi.com/signup/) 并按照我们的 [入门](https://www.pulumi.com/docs/get-started/) 指南进行操作，看看简单的用例有多容易，并开始想象相同的开发人员体验如何扩展到您的整个组织。

要了解更多信息，您可以观看以下视频，它提供了有关 Pulumi 工作原理的高级概述：
