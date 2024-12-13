
<!--
title: 您的内部开发者平台缺少编排功能吗？
cover: https://cdn.thenewstack.io/media/2024/12/208b7e37-daniel-bryant-kubernetes-day-uk.png
-->

开发者门户自上而下运作。Terraform 和 Kubernetes 的团队自下而上构建。那么，从中间向外运作的平台工程策略呢？

> 译自 [Is Your Internal Developer Platform Missing Orchestration?](https://thenewstack.io/is-your-internal-developer-platform-missing-orchestration/)，作者 Jennifer Riggins。

[平台工程](https://thenewstack.io/platform-engineering/)在过去几年中迅速兴起，成为解决[DevOps 缺陷](https://thenewstack.io/platform-engineering-wont-kill-the-devops-star/)的方案。技术蔓延和云原生复杂性使得开发人员不堪重负，运维工程师也因重复性任务过多而感到沮丧。

一个[内部开发者平台 (IDP)](https://thenewstack.io/internal-developer-portal-what-it-is-and-why-you-need-one/)就像建筑物上的脚手架。它是一个在不同层面为不同需求提供的支撑结构，虽然任何人都可以看到下面的情况，但它有助于让建设者——无论是建筑还是软件的建设者——专注于手头的工作。

平台工程填补了应用程序开发和运营基础设施管理之间的技术堆栈空白。正如Syntasso产品营销主管所称的，这个“缺失的中层”是管理平台生命周期所必需的。

越来越多的组织正在承担平台工程项目。但一些团队报告了喜忧参半的结果——一些迹象表明炒作浪潮正在消退。

到 2026 年，Gartner 分析师预测[80% 的组织将拥有平台工程项目](https://thenewstack.io/platform-engineering-is-for-everyone/)——但该公司也报告说，平台工程已从其炒作的巅峰跌入“幻灭的低谷”。

“当我们陷入‘幻灭的低谷’时，我们开始学习东西，”Bryant 在 10 月在伦敦举行的 [Kubernetes 社区日英国](https://community.cncf.io/events/details/cncf-kcd-uk-presents-kubernetes-community-days-uk-london-2024/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 上的一次演讲中说道。“你开始听到恐怖故事和战斗故事——我在 DevOps 中经历过，在微服务中也经历过。我们向下走的时候学到了很多东西。

“但是，如果你正在构建平台，那么实现第二天成功将会有点艰难，”他补充道。

我们已经从最近的[2024 年加速 DevOps 状态](https://dora.dev/research/2024/dora-report/)（也称为[DORA 报告](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/)）的结果中看到了这一点。虽然个人和团队感觉生产力更高，组织的软件交付和运营绩效有所提高，但吞吐量下降了 8%，变更稳定性下降了 14%——所有这些都是由于采用了[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)。

有没有更好的方法来构建 IDP？Bryant 谈到了平台协调器（由现有工具组成，而不是构建您自己的平台即服务）的潜力，它能够使开发人员更快、更高效、更安全地构建。

## 你如何构建平台？

在过去 20 年的技术生涯中，Bryant 发现了构建平台的三个不同模式，每个模式都有不同的目标：

- 自上而下的平台：专注于应用程序开发人员，通常以内部开发者门户的形式交付，最常使用[Backstage](https://thenewstack.io/spotifys-backstage-a-strategic-guide/)构建。
- 自中而外的平台：专注于平台工程，包括一切即服务、流程自动化、大规模管理和[平台即产品](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/)。
- 自下而上的平台：专注于运营或基础设施，例如 Terraform、[Kubernetes](https://roadmap.sh/kubernetes)、[Apache Mesos](https://thenewstack.io/apache-mesos-narrowly-avoids-a-move-to-the-attic-for-now/)或[Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/)，以及 DevOps 原则“你构建它，你运行它”。

### 自上而下或 Backstage 方法

自上而下的方法专注于应用程序开发人员体验。这些是 Spotify 工程师在创建用于构建内部开发者门户的[Backstage 开源框架](https://github.com/backstage/backstage)时制定的黄金路径。

“Backstage 无处不在。它抓住了时代精神，对吧？开始使用非常棒，”Bryant 说。但它“在第二天体验上可能更具挑战性”。

现代平台工程策略的一个目标应该是降低开发人员的认知负担——不要让开发人员学习新东西。自上而下的平台方法的风险通常在于必须学习TypeScript才能使用Backstage的开源版本。

Bryant将这种方法比作圣诞节收到一只小狗——一开始看起来很棒，但后来你必须照顾它并清理它的排泄物。

他说，挑战在于，像Backstage这样的门户通常只是一个“薄薄的外观”，它调用一系列基础设施API。这对引导来说很棒，但它使升级和维护变得非常困难，这就是为什么会有Backstage即服务公司和内部Backstage团队出现的原因。

“如果你之前什么都没有——你有很多微服务，你的东西到处都是，[而且]你不知道你的资产里有什么，那么它就有极好的开发者体验，”Bryant说。“Backstage和其他门户网站都是高度可定制的。但我们确实看到的一种反模式是，每个人都说，‘我可以为此编写一个插件’，然后他们意识到它是TypeScript，他们就不太热衷了。”

他说，Backstage具有出色的服务目录和技术文档，但它并没有涵盖平台的所有需求。采用不同的平台方法，门户可以充当Bryant所说的“应用程序编排”，它只关注在软件开发生命周期中提供有用的、可搜索的界面。

### 自下而上或运维方法

基础设施即代码是构建自下而上且以运维为中心的平台的方式。

“这就是Terraform或Crossplane是我的平台的地方，”Bryant说。“我可以通过HashiCorp配置语言、cron作业、GitOps管道来编排我的所有基础设施。它是高度自动化的，这对快速体验来说很棒。”

然而，随着技术蔓延，这变得越来越困难，这使得自动化和编排越来越困难。这可能会创建一个快速发展的平台客户的双速组织，而非客户则停留在遗留软件上。

此外，Bryant说，基础设施抽象永远不会完美，它们会泄漏给开发人员，开发人员至少必须了解一些关于Kubernetes和其他增加认知负担的运维复杂性。

“并非每个工程师都想这样做，”Bryant说。“有些人只想要：这是我的应用程序。让它运行。”

### 中间外或编排方法

最后，Bryant为结合了更高抽象级别工具和流程的中间外平台策略进行了论证。

在这个新兴的三层堆栈中，首先是应用程序开发，代码编写、交付和运行都在这里进行。

中间是平台编排层，Bryant说，平台、开发人员体验和站点可靠性工程师专注于设计、启用和优化。从事这部分工作的人（直到最近才缺失）专注于内部开发人员平台生命周期和平台API。

然后，所有内容都位于基础设施编排和组合层，DevOps和平台工程师在这里进行规划、构建和维护。

“一旦你理解了这三层，你就可以考虑领域边界，”Bryant说。“你可以考虑API。你可以考虑耦合和内聚，”这允许技术领导层决定权衡。“这就是我们构建可扩展平台的方式，以实现速度、安全性和效率。”

他举例说明了服务于此中间编排层的产品：

* Crossplane Compositions
* Cloud Native Operational Excellence (CNOE), 一个构建内部开发人员平台的开源框架
* Humanitec Resource Definition
* Kratix Promises, by Syntasso
* Argo Custom Resource Definition
* Flux Custom Resource Definition

## 提供平台开发者体验

平台工程师的成功归结于真正考虑您的内部用户体验 (UX)——开发者体验或 DevEx。

“你现在正在构建一个产品，因此，UX 至关重要，”Bryant 说。
他引用了 Spotify Backstage 的产品经理的观点，阐述了这种方法应该包含的内容：将基本的软件设计原则——API优先、领域边界和面向对象设计——应用于平台。

在这个策略中，你隐藏信息，以便每一层都清楚它应该做什么。然后，遵循渐进式披露的概念，Bryant 说——这“是关于让系统易于上手，但也能完成困难任务”——随着你的内部客户对平台越来越熟悉或需要完成更困难的任务，你可以根据需要披露其他功能。

这样，你就不会一开始就吓到你的开发者客户——因为有了平台工程，你的平台仍然可以选择使用。

每个开发者用户群都会略有不同，但 Bryant 认为，平台团队应该专注于服务三个方面：

- 用户界面
- 命令行界面
- API

然后，努力优化自动化。

“业务需求会发生变化，用户期望会扩大，而 API 是平台的核心，”他说，并提供了可以实现他所说的正确抽象级别的特定 API：

- 开放应用模型：[OAM](https://oam.dev/), [Score](https://score.dev/)。
- [Kratix Promise Workflows](https://docs.kratix.io/main/reference/promises/workflows)。
- [KubeBuilder](https://book.kubebuilder.io/)。
- Crossplane。
- [Massdriver](https://www.massdriver.cloud/)。
- Terraform。

“这些都不是好坏之分。这都是权衡取舍，”Bryant 说，他认为 OAM 和 Score 更侧重于开发者，而 Massdriver 更侧重于实现。

## 寻找合适的平台技术栈

平台工程策略的下一步是选择技术栈，通常由各种最佳工具组成。

Bryant 突出了一些常见的平台自动化栈，从更不那么武断到更武断：

- BACK 栈：Backstage、Argo、Crossplane、Kyverno
- CNOE 框架
- Kubefirst，
- 使用其他云原生计算基金会技术构建你自己的。

无论你选择什么，他都说，确保在这个中间层有明确的界限。然后，平台 API 将定义你的开发者如何与平台组件、服务和跨平台生命周期的流程进行交互。

## 采用平台即产品的思维模式

“当你将你的平台视为产品时，真正的魔力就出现了，”Bryant 在他的演示文稿中说。“你实际上是在为用户的需求而构建，真正理解人们想要什么并满足这些需求，”Bryant 说。

用户输入对于成功构建你的平台至关重要。“如果你正在构建一个平台来提高速度、减少缺陷、扩展规模，那么你必须对你在构建什么有一个更清晰的认识，”他说，并快速沟通以获得内部开发者客户的反馈。

然后，与所有产品管理一样，关键是设定目标和 DevEx 指标。这包括领先指标，例如：

- 采用率
- 入职时间
- 到第 n 个拉取请求的时间

以及滞后指标，例如：

- 应用保留率
- 减少的事件和近失事件
- 投资回报率，通常以节省的时间来衡量。

任何形式的平台工程指标都需要将定量的快速成功与长期的业务目标和定性的开发者体验结合起来。

## 附加阅读推荐

为了理解和实现平台工程成功所需的组织动态，Bryant 推荐了[两本必读](https://www.syntasso.io/post/top-five-platform-engineering-books-for-2024)之书：

- “[Enabling Microservice Success](https://www.oreilly.com/library/view/enabling-microservice-success/9781098130787/)” by [Sarah Wells](https://thenewstack.io/setting-microservices-up-for-success-real-world-advice/)
- “[Team Topologies](https://thenewstack.io/how-team-topologies-supports-platform-engineering/)” by [Matthew Skelton](https://thenewstack.io/setting-microservices-up-for-success-real-world-advice/) 和 [Manuel Pais](https://www.linkedin.com/in/manuelpais)

我们还想补充我们自己的免费电子书：“[Platform Engineering: What You Need to Know Now](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/)”。
