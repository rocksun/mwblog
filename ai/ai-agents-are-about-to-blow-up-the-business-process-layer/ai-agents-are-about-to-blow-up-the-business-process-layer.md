
<!--
title: AI智能体即将颠覆业务流程层
cover: https://cdn.thenewstack.io/media/2025/01/7ae5f9a7-sparks.png
-->

主动式AI“自动化系统”将把静态的业务运营转变为动态的、上下文感知的、自主系统。

> 译自 [AI Agents Are About To Blow Up the Business Process Layer](https://thenewstack.io/ai-agents-are-about-to-blow-up-the-business-process-layer/)，作者 Ed Anuff。

人们想到生成式AI时，许多人认为它作为“参与系统”的一部分——客户服务代理、供应链管理工具或智能交互和搜索组织的PDF和其他专有数据的方式。

这是准确的看法：在未来一两年内，通过[利用大型语言模型（LLM）](https://www.datastax.com/guides/what-is-a-large-language-model?utm_medium=byline&utm_source=thenewstack&utm_campaign=agentic-ai&utm_content=)智能创建内容的应用程序将仍然是企业的首要[AI重点](https://thenewstack.io/ai/)。

但请考虑这一点：大多数企业编写的代码都位于业务流程中——例如库存规划之类的系统，它们位于参与层和更严格的记录系统（组织的数据等）之间。GenAI将如何使该层受益？组织如何利用这项普及的技术改进其业务流程？

![A classic enterprise architecture](https://cdn.thenewstack.io/media/2025/01/9c44e2c3-image1.png)

*典型的企业架构。*

智能AI是答案。虽然AI智能体被设计用来执行特定任务或自动化特定且经常重复的任务（例如更新您的日历），但它们通常需要人工输入。智能AI完全关乎自主性（想想自动驾驶汽车），它采用代理系统不断适应动态环境并独立创建、执行和优化结果。

当智能AI应用于业务流程工作流时，它可以将脆弱的、静态的业务流程替换为动态的、上下文感知的自动化系统。

让我们来看看为什么将AI智能体集成到企业架构中标志着组织处理自动化和业务流程方式的变革性飞跃，以及支持这些自动化系统需要什么样的平台。

## 智能体目前正在做什么

当您向智能体提供上下文时，智能体将该[上下文提供给LLM](https://thenewstack.io/llm/)并要求其完成并响应它。AI智能体还可以使用功能代表用户完成任务。这些AI智能体可以执行由指令和从上下文中获得的信息指导的几个关键功能：

- **工具使用**: 智能体使用外部函数、API或工具来扩展其功能并执行特定任务。这可能包括调用预定义函数或与外部服务交互（例如使用cURL发出网络请求或访问RESTful API）以获取上下文或执行超出其固有功能的操作。
- **决策**: 智能体评估可用信息并选择最合适的行动来实现其目标。这包括分析上下文、权衡可能的结果并选择符合预期目标的行动方案。
- **规划**: 智能体制定一系列行动或策略以实现特定目标。
- **推理**: 智能体分析可用的上下文，得出结论，预测行动的结果，并就达到预期结果的最佳步骤做出明智的决定。

这些后一种功能——决策、规划和推理——通常涉及多个智能体共同努力实现目标。智能体可以试图改进生成的代码的正确性，讨论智能决策是否存在偏差，或者规划使用其他[智能功能](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/)来完成任务。

## 编排智能网络

为代理网络提供支持的模型本质上是无状态函数，它们将上下文作为输入并输出响应，因此需要某种框架来编排它们。部分编排可能是简单的改进（例如，让模型请求更多信息）。这听起来可能类似于[检索增强生成 (RAG)](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_medium=byline&utm_source=thenewstack&utm_campaign=agentic-ai&utm_content=)——它确实如此，因为RAG本质上是代理架构的简化形式：它为模型提供了一个访问附加信息的单一工具，通常来自向量数据库。

但是多智能体模型框架更进一步：它们代理对附加信息的请求，或提供旨在馈送到另一个智能体以进行改进的响应。

![Frameworks enable agents to work in concert.](https://cdn.thenewstack.io/media/2025/01/cbae4a70-image2-1024x484.png)

*框架使智能体能够协同工作。*

例如，一个代理可以编写一些Python代码，然后另一个代理审查它。或者一个代理可以表达一个目标或想法，然后第二个代理的工作可以是将该目标或想法分解成一系列任务，或者审查该想法以发现第一个代理可以审查的问题，然后改进该想法。你的结果会越来越好。

## 好吧，但是我该如何构建代理式AI？

在不久的将来，许多软件工程师将成为代理式流程的作者。他们将通过混合和匹配组件——模型、用户输入、目标——和关键业务服务来构建这些流程。

这些组件的一个例子是库存管理系统中的库存。如果你将该系统连接到一个可以帮助在节假日优化库存水平的代理会怎样？在另一个已经进行了一些历史库存水平分析的代理的帮助下，你可以确保有足够的库存来满足季节性需求，但在节后高峰期后留下少量库存。这可能会让狂热的圣诞节后促销购物者失望，但它也有助于防止零售商亏本销售商品。

但是开发人员将如何构建这些系统呢？

代理式流程当然可以用代码表达，但将其可视化为“代理式流程”也有帮助——一个代理的输出成为另一个代理的输入，依此类推。现在可用的工具已经在简化构建代理式系统方面提供了很多价值。其中一个解决方案是[Langflow](https://www.datastax.com/products/langflow?utm_medium=byline&utm_source=thenewstack&utm_campaign=agentic-ai&utm_content=), 一个用于[创建代理式AI应用程序](https://thenewstack.io/datastax-aims-to-simplify-building-ai-apps-with-ragstack/)和复杂AI工作流程的可视化低代码构建器，可以通过拖放不同的组件来实现，无需大量编码。

![代理式“流程”有助于自动化业务流程。](https://cdn.thenewstack.io/media/2025/01/7bcd77f4-image3-1024x442.png)

*代理式“流程”有助于自动化业务流程。*

Langflow使开发人员能够将任何东西定义为工具，包括提示、数据源、模型、API、工具或任何其他代理等组件。我们最近看到对使用代理构建“流程”的需求显著增加，因为开发人员正在创建许多包含多个代理功能的应用程序。代理是开发人员最常插入Langflow流程的组件类型。

## 总结：从副驾驶到驾驶员

代理式工作流程[将企业数据整合在一起](https://thenewstack.io/bringing-ai-to-the-data-center/), AI和API，形成自动化系统，使领域专家能够扩展其能力，并通过AI使企业更好地运作。将AI代理集成到企业架构中标志着组织处理自动化和业务流程方式的巨大飞跃。这些由LLM和代理框架赋能的代理，通过在流程、工作流程和代码之间无缝运行，超越了传统的界限。

![AI如何改变企业架构](https://cdn.thenewstack.io/media/2025/01/a64863a4-image4-1024x381.png)

*AI如何改变企业架构。*

采用代理式工作流程有望提高业务运营的效率、可扩展性和响应能力。它们将管理整个工作流程，以更大的适应性处理复杂的任务，并通过提供更个性化和及时的互动来改善客户体验。随着自动化嵌入企业系统，AI副驾驶将升级为驾驶员，采用代理式AI的组织将能够更好地进行创新、竞争和创造价值。
