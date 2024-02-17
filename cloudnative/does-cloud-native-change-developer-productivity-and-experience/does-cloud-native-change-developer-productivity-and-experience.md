<!--
title: 云原生改变了开发者的生产力和体验？
cover: https://cdn.thenewstack.io/media/2024/02/3aafa6b7-clouds-1024x649.jpg
-->

管理层必须谨慎选择正确的平台、工具、流程和生产力指标，全力支持开发者，以获得最佳成果。

> 译自 [Does Cloud Native Change Developer Productivity and Experience?](https://thenewstack.io/does-cloud-native-change-developer-productivity-and-experience/)，作者 Jason Bloomberg 是一位领先的 IT 行业分析师、作家、主题演讲者，并且是企业技术和数字化转型多个颠覆性趋势的全球公认专家。他是数字化转型分析公司 Intellyx 的创始人和总裁。

在这一系列文章的第一篇中，我讨论了云原生平台工程的[三个悖论](https://yylives.cc/2024/01/21/the-3-paradoxes-of-cloud-native-platform-engineering/): 如何不经意地通过测量开发者生产力而降低它；平台工程工作如何通过过于规范化而适得其反；以及云原生开发者如何同时关注单个微服务和 Pod 和集群的行为。

在这个第二篇文章中，我的同事 Eric Newcomer 深入探讨了平台工程师在[为云原生开发者构建内部开发者平台(IDP)](https://thenewstack.io/why-platform-engineering-is-different-for-cloud-native-apps/)时面临的挑战。他总结道，成功需要正确的组织结构和治理，适度的纪律以及 IDP 中正确的平台工具组合 - 特别是，面向开发、部署和支持微服务的小型自治团队定制的数据[可观测性工具](https://thenewstack.io/observability-in-2024-more-opentelemetry-less-confusion/)。

这两篇文章贯穿了两个主线。第一个是[开发者生产力](https://chronosphere.io/learn/a-starting-guide-to-measuring-developer-productivity/) - 单个开发者和团队在给定时间内可以完成多少工作。同样重要的第二个主线是开发者体验或 DX。DX 是对开发者可以有效利用可用的工具和平台完成工作的能力，以及士气和整体工作满意度的测量。

向开发者投入的挑战越多，持续产出高质量工作的难度就越大。与此同时，在这种情况下增加生产力的压力可能会对开发者体验产生有害影响，这种情况肯定会适得其反。

云原生是提出这些挑战的一个领域。在[云原生大规模部署的背景下构建微服务](https://chronosphere.io/learn/comparing-monolith-and-microservice-architectures-for-software-delivery/)是困难和复杂的。那么，组织应该如何在云原生计划中平衡开发者生产力和 DX?理想情况下，如何同时改善两者?

## 为何云原生开发如此富有挑战性

[云原生开发](https://thenewstack.io/cloud-native/)以[微服务](https://thenewstack.io/microservices/microservices-101/)开始。尽管微服务有许多定义(许多根本不“微”)，但一个流行的定义是“简约、内聚的执行单元”。

“简约”意味着尽可能小，但不要更小 - “微”的部分。“内聚”是良好软件的一个众所周知的特性，意味着每个微服务做好一件事。

“执行单元”是指微服务在容器中运行时包含执行所需的运行时组件 - 这与早期基于 XML 的 Web 服务端点形成了有意的对比，后者需要企业服务总线(或其他像 servlet 引擎等技术)来提供执行上下文。

此外，在更广泛的[云原生架构](https://chronosphere.io/learn/what-is-cloud-native-architecture/)背景下，微服务需要额外的考虑。它们在 pod 内自动扩展，因此开发人员必须将其设计为无状态的。因此，使用微服务管理状态需要特殊小心才能获得动态扩展的好处。

为了保持生产力，云原生开发者必须与 DevOps 团队合作，全时关注每个微服务的所有这些属性，并牢记每个微服务在更广泛的云原生架构环境中的功能。

换句话说，云原生开发是困难和复杂的 - 这些挑战很容易影响开发者的生产力和体验。

## 在充满挑战的开发中保持良好的体验

好消息是: 开发者喜欢挑战。他们中的大多数选择这个职业是因为固有的满足感可以解决困难的难题。当一段特别棘手的代码最终按预期运行时，没有比这更令人振奋的了。

然而，有一条细线，在有趣和充实的挑战与如此困难的问题之间，解决问题就像自打脑袋。对许多开发者来说，云原生开发更像是后者。

开发者的生产力和体验都依赖于将这个等式转向开发者所喜爱的那种挑战。IDP 可以提供帮助，因为它为开发者提供了一套推荐的工具，但拥有正确的工具至关重要。

在 IDP 中可以找到的所有工具中，最有助于提高生产力和体验的[可观测性工具](https://chronosphere.io/learn/3-key-differences-of-open-source-observability-tools-vs-proprietary-observability-tools/)。只要开发者拥有解决问题所需的信息，困难的问题就没有关系 - Chronosphere 等可观测性工具提供了这些信息。

Chronosphere 不仅为开发者提供了专门的可观测性，还专注于观察云原生环境。

特别是，[Chronosphere Lens](https://chronosphere.io/learn/empower-developer-effectiveness-in-the-cloud-native-age-with-chronosphere-lens/) 通过动态生成面向服务的视图，支持开发者主动探索和对系统行为进行故障排除，超越了原始遥测数据。

## Intellyx 的看法 

当管理层过于关注开发者生产力时，开发者体验可能会受到影响，从而损害士气，并且生产力方面产生适得其反的效果。管理层需要用轻巧的手法来避免这个问题，特别是在云原生中。

云原生环境可能变得如此动态和嘈杂，以至于生产力和开发者体验都会下降。管理层必须特别注意，通过正确的平台、工具、流程和生产力指标来支持其开发者，利用[平台工程](https://chronosphere.io/learn/sre-vs-devops-successful-platform-engineering-needs-both/)创建和管理 IDP，以促进最佳结果，尽管云原生开发本身复杂。

毕竟，云原生开发的复杂性本身并不是问题。复杂性无疑带来了挑战，但开发者总是喜欢挑战。复杂性加上可视性的缺乏会带来沮丧，降低生产力和体验。

例如，有了 Chronosphere 和 Google Cloud 等适当的可观测性，开发者就有很大机会来处理云原生固有的复杂性，按时按预算交付质量软件，同时保持生产力和体验。
