
<!--
title: SaaS已死：为何自带云 (BYOC) 才是未来
cover: https://cdn.thenewstack.io/media/2025/03/e58e8532-r-onita-glhgns3gfb0-unsplash-scaled.jpg
summary: SaaS已死？拥抱BYOC！传统SaaS在AI时代面临数据摄取成本高、控制受限等挑战。BYOC让企业在自有云上运行SaaS应用，兼顾便捷与控制，降低成本高达80%。拥抱开源标准，BYOC将颠覆可观测性等领域，迎来计算新纪元！
-->

SaaS已死？拥抱BYOC！传统SaaS在AI时代面临数据摄取成本高、控制受限等挑战。BYOC让企业在自有云上运行SaaS应用，兼顾便捷与控制，降低成本高达80%。拥抱开源标准，BYOC将颠覆可观测性等领域，迎来计算新纪元！

> 译自：[SaaS Is Broken: Why Bring Your Own Cloud (BYOC) Is the Future](https://thenewstack.io/saas-is-broken-why-bring-your-own-cloud-byoc-is-the-future/)
> 
> 作者：Noam Levy

软件即服务 (SaaS) 模式开启了高速产品开发的新纪元。与本地部署的僵化和缓慢不同，SaaS 供应商通过拥有数据托管及其底层基础设施的所有权，提供了一种干净、可靠的体验。然而，就像任何范式转变的苦涩结局一样，世界再次发生了变化。

如今，组织希望保护、控制并了解谁在[处理他们的数据](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/)。这正是传统 SaaS 模式开始崩溃的地方。将大量数据传输给 SaaS 供应商提供了简单性，但代价是成本越来越高，并且失去了数据所有权。

我们不能让自己从 SaaS 的简单性倒退——[以这种方式构建和使用软件](https://thenewstack.io/how-sprinting-slows-you-down-a-better-way-to-build-software/)对于当今的一切来说都太重要了。相反，我们必须找到一种更好的模式，既能保留 SaaS 的优势，又能与市场的发展方向保持一致。我们需要 SaaS 2.0 的崛起。

自带云 (BYOC) 允许客户使用自己的云基础设施和资源来运行 SaaS 应用程序，而不是依赖第三方供应商的基础设施。这种混合方法保留了 SaaS 的便利性和速度，同时保留了自托管解决方案的成本和所有权优势。

## 传统 SaaS 的问题

传统 SaaS 在 AI、可观测性以及任何其他严重依赖数据的领域都面临着两个根本性的挑战：

1. **基于摄取的货币化模式已失效**

* **虚高**：订阅成本与数据摄取量挂钩，公司需要支付只有供应商才知道的隐藏加价。这已将 SaaS 市场推入恶性通货膨胀的状态。
* **不可预测**：数据是动态的。它具有季节性、突发性和不断演变的特性。当供应商根据摄取量收费时，公司很难估算成本，使得预算规划几乎不可能。
* **难以管理**：许多公司浪费大量时间仅仅用于成本管理。他们投入大量精力来识别冗余数据传输并过滤掉有价值的数据以降低成本，即使这些数据可能是有益的。

2. **数据控制和访问限制**

* **安全盲点**：[公司在控制数据](https://thenewstack.io/can-companies-really-self-host-at-scale/)位置和访问方面投入巨资，但使用传统 SaaS，敏感数据很容易驻留在第三方供应商的场所内，超出完全治理范围。
* **合规性问题**：公司的合规性仅与处理其数据的最不合规的第三方供应商一样强大。在 SaaS 时代，敏感数据很容易出现在合规性不如您严格的供应商中。
* **访问受限**：企业无法以他们喜欢的方式使用他们发送给第三方供应商的数据，这对于本地 AI/ML 工作负载以及您想要与数据集成的任何内部工具来说都是一个大问题。

## 什么是 BYOC？

BYOC 允许客户使用自己的云基础设施和资源来运行 SaaS 应用程序，而不是依赖第三方供应商的基础设施。这种混合方法保留了 SaaS 的便利性和速度，同时通过自托管解决方案的控制来平衡成本和所有权。

构建一个易于采用、经济高效且性能良好的 BYOC 堆栈是一项重大的工程挑战。但作为软件供应商，您的客户可以获得许多好处，使其值得付出努力。以下是我们自从向客户提供 BYOC 以来看到的一些主要好处：

1. 那些向 New Relic 和 Datadog 等传统 SaaS 提供商支付数百万美元的公司正在看到前所未有的 [80% 的成本降低](https://www.groundcover.com/customer-stories/cresta-reduces-observability-costs-by-80-by-migrating-to-groundcover)。
2. 因此，他们现在有预算来利用更多的指标、日志和追踪，这意味着可以更好地了解他们以前没有观察到的领域（并且[发现他们原本永远不会发现的问题](https://www.groundcover.com/customer-stories/cloud-security-leader-replaces-datadog-with-groundcover)）。
3. 睡得安稳，因为知道包含敏感数据的可观测性数据（例如日志、指标和追踪）将保留在本地。

## 为什么 BYOC 是 SaaS 的下一个演进

SaaS 为软件消费带来了速度和简单性，而传统的本地部署提供了控制和可预测性。但是，随着公司面临[成本上涨](https://thenewstack.io/hybrid-it-is-emerging-as-the-solution-to-ais-rising-cost/)、合规性挑战以及对数据所有权的需求，一种更平衡的方法正在出现。

BYOC 是 SaaS 的便捷性和本地部署的控制性的整合演变。公司无需将大量数据发送给第三方供应商，而是[可以在其云基础设施中运行 SaaS 应用程序](https://thenewstack.io/why-most-companies-are-struggling-with-infrastructure-as-code/)。这意味着可预测的成本、更好的合规性和量身定制的性能。

我们已经在其他领域看到了这种混合模式的成功。Meta 的 Llama 获得了广泛采用，因为用户可以在其基础设施上运行它。ARM 处理器通过使公司能够根据自己的需求定制芯片而成为全球标准。同样，主要的[云提供商现在提供基于开放标准的托管解决方案](https://thenewstack.io/the-complex-relationship-between-cloud-providers-and-open-source/)，从而在不牺牲 SaaS 体验的前提下为客户提供灵活性。

BYOC 正在证明，公司不必在简单性和控制性之间做出选择。它旨在取两者之长，并使它们协同工作。

## 结论

这是一个激动人心的时代：随着人工智能的兴起，软件的发展速度比以往任何时候都快。我们认为，采用 BYOC、[维护开源](https://thenewstack.io/nivenly-foundation-seeks-equity-for-open-source-maintainers/)标准以及为客户提供无摩擦的工具，将是帮助客户取得成功并迎来计算新纪元的关键。

在 groundcover，我们亲眼目睹了 BYOC 如何改变公司处理可观测性的方式。它使他们能够比以往任何时候都更快地交付和存储更多数据，大幅降低成本，并获得高度定制的体验。正如 BYOC 正在颠覆可观测性市场一样，我们相信它将对其所触及的每个行业产生类似的影响。