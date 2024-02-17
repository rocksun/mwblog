<!--
title: 可组合架构与微服务：哪个更优？
cover: https://cdn.thenewstack.io/media/2024/02/fb188674-microservices-vs-composable-architecture-1024x576.jpg
-->

两种软件开发架构都有各自的优缺点。下面是如何决定可组合架构还是微服务架构哪种更适合你的方法。

> 译自 [Composable Architectures vs. Microservices: Which Is Best?](https://thenewstack.io/composable-architectures-vs-microservices-which-is-best/)，作者 Michel Murabito 是Mia-Platform的开发者倡导者，拥有超过18年的软件开发经验。

[单体架构](https://mia-platform.eu/blog/monolith-to-microservices/)几十年来一直是软件开发的基石。尽管其简单易开发的特点，但随着应用程序复杂度的增加，传统架构往往会遇到性能瓶颈和可扩展性挑战。[微服务](https://mia-platform.eu/blog/microservices/)很快成为一种解决方案，通过提供性能优化、灵活性和容错性来应对这些挑战。从行业巨头如 [Atlassian](https://www.atlassian.com/software-development/practices/microservices) 和 [Netflix](https://thenewstack.io/how-culture-impacts-technology-choice-a-review-of-netflixs-use-of-microservices/) 成功从单体技术迁移的经验中我们可以学到的一课是，速度、敏捷性和可扩展性在当今市场上获胜。

[可组合架构](https://mia-platform.eu/blog/composable-architecture/)作为一种与软件开发不断发展的需求相契合的补充方法已经出现。这种设计方法在科技行业引起了很多关注，在2021年，[Gartner预测](https://www.gartner.com/en/newsroom/press-releases/2021-10-18-gartner-identifies-the-top-strategic-technology-trends-for-2022)采用可组合方法的公司将能够比竞争对手更快地实现新功能，提高了80%。

尽管可组合架构可以增强企业的敏捷性、可扩展性和适应性，但许多IT和DevOps团队想知道这对微服务意味着什么。他们关心这些方法之间的关系、相似之处和差异，以及可组合架构是否会让微服务变得过时。

## 可组合架构：模块化系统的崛起

可组合架构是一种模块化的软件设计和开发方法，构建了灵活、可重用和适应性强的软件架构。它涉及将庞大的、单体平台分解为小型、专业化、可重用和独立的组件。这种架构模式包括一系列可插拔的模块化组件，如微服务、[打包的业务能力（PBC）](https://mia-platform.eu/blog/packaged-business-capabilities-pbc/)、无头架构和API-优先开发，这些组件可以无缝地替换、组装和配置，以满足业务需求。

在可组合应用中，[每个组件](https://mia-platform.eu/blog/creating-composable-software-components/)都是独立开发的，使用最适合应用功能和目的的技术。这使企业能够构建可以迅速适应业务需求的定制化解决方案。

由于这种架构模式基于[API-优先](https://thenewstack.io/api-first-development-architecting-applications-with-intention/)原则，信息在服务和系统之间共享，无需了解底层技术。这种方法提供了一系列好处，包括：

- 它帮助团队轻松快速地扩展规模，充分利用增长机会获得竞争优势。
- 它使维护和系统更新变得更容易，因为模块化组件可以单独修改和替换，减少认知负担。
- 它通过允许团队重复使用和重新利用现有组件来满足不断变化的需求和要求，加快了开发过程。
- 它允许添加新的API和工具以支持增长，而不必担心它们是否能很好地配合使用。
- 它使组织能够跟上数字渠道的业务趋势，同时提供一致的体验，提高客户满意度。

在电子商务应用和网站开发中，可组合方法已经得到了显著的普及，为开发人员、客户和零售商增强了数字体验，像[Shopify](https://www.shopify.com/ng/enterprise/composable-commerce)和[Amazon](https://docs.aws.amazon.com/wellarchitected/latest/government-lens/consider-composable-architecture-and-reusability.html)这样的行业领军者正充分利用其优势。

## 微服务：仍然强大的经过验证的方法

微服务架构仍然被用于开发、部署和扩展简化的模块化软件解决方案，这些解决方案可以被其他应用程序重复使用。它包括一组较小的独立组件或服务，每个组件负责特定的业务功能。

微服务是与传统的单体架构有重大差异的，传统架构中，用户界面和后端通常紧密耦合，设计为作为单一功能一起工作。微服务架构是一种分散化的方法，允许团队开发、维护和持续改进单个服务，而不会中断整个应用程序。这些技术通常利用[API](https://thenewstack.io/api-management/)来外部公开信息，以实现与外部服务、应用程序和系统的无缝集成。

微服务架构非常适合具有多个功能组件的复杂系统，许多大型科技公司，包括[eBay](https://www.slideshare.net/tcng3716/ebay-architecture?next_slideshow=1)、[X](https://thenewstack.io/how-airbnb-and-twitter-cut-back-on-microservice-complexities/)（以前被称为Twitter）和[Netflix](https://www.techaheadcorp.com/blog/design-of-microservices-architecture-at-netflix/)，已将其传统的单体应用程序迁移到了小型、独立的、专业化的应用程序。在2023年，[Stack Overflow的开发者调查](https://survey.stackoverflow.co/2023/)报告称，49%的开发者正在其组织中使用微服务。

微服务为软件开发组织提供了明显的好处，例如：

- 增强了故障隔离，并确保单个模块的失败对较大的应用程序影响最小。
- 提供了灵活性，可以根据需要添加、替换或移除单个微服务，同时尝试新的技术堆栈。
- 使团队能够采用小型且频繁的发布，利用CI/CD自动化开发、测试和发布过程。
- 将软件组件隔离，以便进行性能和健康监控。

然而，与每一项新兴技术一样，使用微服务也有其缺点。大量独立的服务引入了复杂性，可能会使得管理每个服务变得艰巨。DevOps和运维团队也可能会遇到分布式跟踪的挑战。多个服务之间的通信还会产生操作开销，使系统设计变得复杂。

## 可组合架构与微服务架构的关系

可组合设计系统是一种软件开发的微服务方法，允许将各个组件组合和重新配置以满足系统开发中的特定要求。可组合架构通常包含比微服务架构更广泛的组件范围和潜在的更大的服务。另一方面，微服务可以与API一起使用来创建可组合技术。这样，微服务可以是可组合架构的一种具体实现。微服务通常关注小型、具体的业务能力，而可组合架构更为广泛。

两者都涉及可互换和可重复使用的组件，以增强灵活性和适应性。此外，两者都鼓励使用技术无关的组件，以使开发团队能够自主工作。

## 胜者？可组合架构还是微服务？

选择哪种方法最适合您的用例需要考虑很多因素。两者都提供独特的好处，并且对于现代技术设计和开发都是必不可少的，但两者也都面临挑战。

可组合架构为软件生命周期带来了敏捷性、模块化、可重用性和快速开发，但也引入了一些问题。这种动态灵活的方法使得监控、预测和验证组件之间的交互变得困难。随着组件数量的增加，有必要不过分专注于集成，而是保持对架构最终目的的关注。从安全角度来看，可组合架构也可能带来挑战，因为每个组件可能具有不同的[安全要求](https://www.nmg-international.com/post/how-secure-are-composable-architectures)和漏洞。组织必须从设计阶段开始考虑这些问题，并实施系统来减轻随着挑战出现而产生的问题。

微服务方法也是如此。虽然它被认为是与分布式系统和管理独立服务的团队合作的极佳选择，但微服务也带来了复杂性。然而，由于组件较小，通常更容易减轻和解决这些复杂性。

在选择方法之前，了解其影响至关重要。考虑它将如何影响产品开发和部署、对市场变化的适应能力以及业务结果。此外，考虑它在交付出超越市场预期的卓越客户体验方面的作用，这对于在市场上取得成功至关重要。

## 在多范式景观中的架构未来

随着[应用架构](https://mia-platform.eu/blog/application-architecture/)不断演变，企业正在寻求最能推动业务灵活性和敏捷性的方法、概念和技术。Gartner预测，[70%的大中型](https://www.youtube.com/watch?v=4GzJFw54AxY)组织很快将把可组合性视为关键的成功标准，可组合方法可能会使新功能的实施速度提高80%，潜在地缩短上市时间。这表明，可组合架构将在企业软件架构的未来中发挥重要作用。

[可组合商业](https://mia-platform.eu/blog/composable-commerce-for-omnichannel-strategies/)、[数字体验平台（DXP）](https://www.sitecore.com/knowledge-center/digital-marketing-resources/what-is-a-composable-dxp)和客户数据平台可以赋予创新力，民主化发展，提高治理能力，并持续提供价值。

需要注意的是，可组合架构并不意味着微服务的终结，因为微服务是可组合技术的重要组成部分。此外，随着微服务和其他基于组件的架构变得更加普遍，可组合架构将继续演进。

## 总结

没有一种适用于所有情况的软件架构。在选择时，要考虑每种方法的优势、能力和挑战将如何影响您的业务目标。

可组合性是一种强大的架构设计模式，改变了我们对应用程序开发的方式。其模块化的特性承诺了可伸缩性、可靠性和敏捷的应用程序开发，缩短了上市时间，提供了运营独立性，实现了成本节约，改善了客户体验，节省了时间。

同样地，微服务方法将复杂系统分解为更小、更专业的服务，代表着不同的业务功能。它为软件开发生命周期带来了更快的创新、高度的可伸缩性、改善的弹性、持续交付和故障隔离。

要更深入地了解可组合架构以及如何将您的业务转变为可组合企业，请深入阅读我们的可组合企业白皮书。
