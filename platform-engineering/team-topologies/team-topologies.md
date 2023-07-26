# 团队拓扑（Team Topologies）

翻译自 [Martin Fowler](https://martinfowler.com/) 大师的 [TeamTopologies](https://martinfowler.com/bliki/TeamTopologies.html) 。

任何大型软件项目，比如为大公司开发的软件体系，都需要很多人的参与。而一旦有很多人，就需要考虑如何将他们分成有效的团队。形成[以业务能力为中心](https://martinfowler.com/bliki/BusinessCapabilityCentric.html)的团队有助于软件项目对客户需求作出响应，但所需技能的范围常常使得这样的团队难以应付。[Team Topologies](https://www.amazon.com/gp/product/1942788819/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1942788819&linkCode=as2&tag=martinfowlerc-20) 是由 Matthew Skelton 和 Manuel Pais 开发的描述软件开发团队组织的模型。它定义了四种团队形式和三种团队交互模式。该模型鼓励健康的交互方式，使以业务能力为中心的团队在提供有价值的软件时能够蓬勃发展。

该框架中的主要团队类型是**流程对齐团队（stream-aligned team）**，这是一个以[业务能力为中心](https://martinfowler.com/bliki/BusinessCapabilityCentric.html)的团队，负责一个业务能力的软件。这些团队运行时间较长，将自己的努力视为提供增强业务能力的[软件产品](https://martinfowler.com/articles/products-over-projects.html)。

每个流程对齐团队都是全栈和全生命周期团队：负责前端、后端、数据库、业务分析、功能优先级、用户体验、测试、部署、监控——整个软件开发过程的全部方面。他们以[结果为导向](https://martinfowler.com/bliki/OutcomeOriented.html)，专注于业务成果，而不是以[活动为导向](https://martinfowler.com/bliki/ActivityOriented.html)，专注于特定功能，比如业务分析、测试或数据库。但是团队也不应该太大，理想情况下，每个团队应该是一个[“两个披萨”的团队](https://martinfowler.com/bliki/TwoPizzaTeam.html)。一个大型组织将拥有许多这样的团队，虽然它们需要支持不同的业务能力，但它们有共同的需求，比如数据存储、网络通信和可观测性。

像这样的小团队需要找到方法来减少认知负担，以便他们可以专注于支持业务需求，而不是（例如）数据存储问题。实现这一目标的一个重要部分是建立在一个能够处理这些非核心问题的平台上。对于许多团队来说，这个平台可以是一个广泛可用的第三方平台，比如用于数据库支持的 Ruby on Rails 。但是对于许多产品来说，并没有单一的现成平台可供使用，一个团队将不得不找到并整合几个平台。在一个较大的组织中，他们将不得不访问一系列内部服务并遵循企业标准。

这个问题可以通过为组织构建一个内部平台来解决。这样的平台可以整合第三方服务、几乎完整的平台以及内部服务。《Team Topologies》将构建这样一个平台的团队（很不富有创意但很明智）划分为**平台团队**。

较小的组织可以与一个单一的平台团队合作，该团队为外部提供的产品集提供了一个薄薄的层。然而，较大的平台需要比“两个披萨”团队更多的人。因此，作者们开始描述由许多平台团队组成的平台组合。

平台的一个重要特点是它被设计成在大多数情况下以自助方式使用。流程对齐团队仍然负责其产品的运营，并在使用平台时直接与平台团队进行简单的协作，而不期望进行复杂的合作。在《Team Topologies》框架中，这种交互模式被称为 **X-as-a-Service** 模式，其中平台作为流程对齐团队的服务。

然而，平台团队需要将它们的服务构建为产品本身，并深入了解客户的需求。这通常需要使用另一种交互模式，即协作模式，在构建该服务时进行更密切的合作。协作模式是一种更为密集的合作方式，并应被视为一种临时方法，直到平台足够成熟，可以转入 **X-as-a-Service** 模式。

到目前为止，这个模型没有表现出特别创新的东西。将组织分解为业务对齐团队和技术支持团队的做法早已是企业软件的老生常谈。近年来，很多作者都强调了让这些业务能力团队负责全栈和全生命周期的重要性。对我来说，《Team Topologies》的亮点是专注于问题，即让业务对齐团队在全栈和全生命周期的情况下，往往面临过多的认知负担，这与构建小而敏捷的团队的愿望相冲突。平台的关键好处在于它减少了这种认知负担。

> 《Team Topologies》的一个关键洞察是平台的主要好处，也就是减轻流程对齐团队的认知负担。

这一洞察具有深远的影响。首先，它改变了平台团队对平台的看法。减轻客户团队的认知负担导致不同的设计决策和产品路线图，与主要用于标准化或降低成本的平台截然不同。除此之外，这一洞察还使《Team Topologies》进一步发展，通过确定另外两种团队类型。

有些能力需要专家，他们可以花费大量时间和精力来掌握对许多流程对齐团队都很重要的主题。与作为流程对齐团队成员时可能的情况相比，安全专家可能会花更多的时间研究安全问题并与更广泛的安全社区进行交流。这些专家聚集在“**使能团队**”中，他们的角色是在其他团队内部培养相关技能，以便这些团队保持独立，更好地拥有和发展自己的服务。为了实现这一目标，使能团队主要使用《Team Topologies》中的第三种交互模式。**促进模式**涉及一种辅导角色，使能团队的目标不是编写和确保符合标准，而是教育和辅导同事，使流程对齐团队变得更加自治。

流程对齐团队负责为其客户提供的所有价值流，但有时我们会发现流程对齐团队的某些工作非常复杂，需要一个专门的团队来专注处理，从而形成第四种类型的团队：**复杂子系统团队**。复杂子系统团队的目标是减轻使用该复杂子系统的流程对齐团队的认知负担。即使只有一个客户团队使用该子系统，这也是一种值得的分工。通常，复杂子系统团队努力以 X-as-a-Service 模式与其客户进行交互，但在短期内可能需要使用协作模式。

![](https://martinfowler.com/bliki/images/team-topologies/diagram.png)
《Team Topologies》包括一组图形符号来说明团队及其关系。这里展示的图形符号[与书中使用的图形符号](https://github.com/TeamTopologies/Team-Shape-Templates)有所不同。[最近的一篇文章](https://teamtopologies.com/key-concepts-content/team-interaction-modeling-with-team-topologies)详细介绍了如何使用这些图表。

《Team Topologies》明确地承认了[康威定律](https://martinfowler.com/bliki/ConwaysLaw.html)的影响。它鼓励的团队组织方式考虑到人与软件组织之间的相互作用。《Team Topologies》的支持者希望其团队结构能够塑造软件架构未来的发展方向，使其能够与业务需求相适应，具有响应性并且解耦。

George Box 曾经巧妙地说过：“所有的模型都是错误的，但有些是有用的。”因此，《Team Topologies》是错误的：复杂的组织结构不能简单地归结为只有四种团队和三种交互方式。但是，正是这些限制使得模型变得有用。《Team Topologies》是一种工具，它推动人们将自己的组织发展成为一种更有效的运营方式，使流程对齐团队通过减轻认知负担来最大化其流程。

## 致谢

Andrew Thal, Andy Birds, Chris Ford, Deepak Paramasivam, Heiko Gerin, Kief Morris, Matteo Vaccari, Matthew Foster, Pavlo Kerestey, Peter Gillard-Moss, Prashanth Ramakrishnan 和 Sandeep Jagtap 在我们的内部邮件列表上讨论了这篇文章的初稿，并提供了宝贵的反馈意见。

Matthew Skelton 和 Manuel Pais 友善地对本文提供了详细的评论，包括分享自书籍出版以来的一些最新思考。

## 进一步阅读

关于《Team Topologies》框架的最佳介绍是同名[书籍](https://www.amazon.com/gp/product/1942788819/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1942788819&linkCode=as2&tag=martinfowlerc-20)，该书于 2019 年出版。作者们还维护着[《Team Topologies》](https://teamtopologies.com/)网站，并提供教育和培训服务。他们最近发表的关于[团队交互建模](https://teamtopologies.com/key-concepts-content/team-interaction-modeling-with-team-topologies)的文章是一个很好的入门，介绍了《Team Topologies》元模型如何用于构建和演化组织的模型。[1]

《Team Topologies》的许多内容都基于认知负荷的概念。作者们在 Tech Beacon 上[探讨了认知负荷](https://techbeacon.com/app-dev-testing/forget-monoliths-vs-microservices-cognitive-load-what-matters)。Jo Pearce 则进一步阐述了认知负荷在[软件开发中的应用](https://12devsofxmas.co.uk/2015/12/day-3-managing-cognitive-load-for-team-learning/)。

《Team Topologies》中的模型与我在本网站上发表的关于软件团队组织的思考相契合。你可以在[“ team organization ”标签](https://martinfowler.com/tags/team%20organization.html)下找到这些内容。

## 注释

1：为了在建模术语上更为严谨，我会说《Team Topologies》通常作为一个**元模型**。如果我使用《Team Topologies》来构建一个航空公司软件开发组织的模型，那么该模型将根据《Team Topologies》的术语对航空公司的团队进行分类。然后我会说，《Team Topologies》模型是我对航空公司模型的一个元模型。