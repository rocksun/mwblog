
<!--
title: 微软构建AutoGen Studio用于AI代理原型设计
cover: https://cdn.thenewstack.io/media/2024/08/5102500e-valeria-nikitina-mlvfsxdrtdq-unsplash.jpg
-->

微软的新低代码工具简化了 AI 代理的创建，承诺在仍处于积极研究阶段的同时彻底改变多代理工作流的开发。

> 译自 [Microsoft Builds AutoGen Studio for AI Agent Prototyping](https://thenewstack.io/microsoft-builds-autogen-studio-for-ai-agent-prototyping/)，作者 Darryl K Taft。

[微软](https://news.microsoft.com/?utm_content=inline+mention) 研究院推出了 [AutoGen Studio](https://microsoft.github.io/autogen/docs/autogen-studio/getting-started/), 这是一款新的 [低代码](https://thenewstack.io/confessions-of-a-low-code-convert/) 接口，旨在彻底改变开发人员原型设计 AI 代理的方式。

该公司表示，该工具建立在开源 [AutoGen](https://microsoft.github.io/autogen) 框架之上，旨在简化创建和管理多代理工作流的复杂过程。

[Elvis Saravia](https://www.linkedin.com/in/omarsar/?originalSubdomain=bz)，[分布式人工智能研究所 (DAIR.AI)](https://www.dair-institute.org/) 的 [机器学习](https://thenewstack.io/how-machine-learning-works-an-overview/) 和 [自然语言处理](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/) 研究员，[在 X 上发布了有关该技术的帖子](https://x.com/omarsar0/status/1829163090715529358?t=uu8tJUUbu4BSYWvZtzeb5g&s=03)（以前称为 Twitter）。

Intellyx 分析师 [Jason Bloomberg](https://www.linkedin.com/in/jasonbloomberg?originalSubdomain=nl) 表示：“‘代理’一词指的是一个独立于其环境中其他软件的自主软件，它实现特定的业务目标。”“然而，它们究竟有多自主以及它们实际做什么，取决于你问谁。”

## 为开发人员提供低代码解决方案

AutoGen Studio 提供了一种用户友好的 AI 代理开发方法，允许开发人员快速原型设计 AI 代理，用专门的技能增强代理，将代理组合成复杂的工作流，并与代理交互以完成各种任务。

Omdia 分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 表示：“这是微软的一个非常酷的项目，实际上已经 [酝酿了几个月](https://github.com/microsoft/autogen/tree/main/samples/apps/autogen-studio)。”“基本上，它运行在微软的 LLM 编排框架 AutoGen 之上，并且确实加快了企业从业者构建 GenAI 结果的原型设计过程——不仅仅是代理，而是任何他们可能想要对 LLM 运行方式进行一些控制的结果。”

该工具提供 Web 接口和 [Python](https://thenewstack.io/python/) API，使开发人员能够使用基于 JSON 的规范来表示支持 LLM 的代理。这种灵活性满足了各种开发偏好和技能水平。

Shimmin 说：“它实际上是对你从其他代理框架（如 [LangGraph](https://thenewstack.io/develop-a-master-ai-agent-with-langgraph-in-python/) 和 [CrewAI](https://www.crewai.com/)）获得的功能的一个很好的图形补充。”“对于在 Azure AI 之上构建的开发人员来说，这个工具加上框架可以帮助他们从 PoC 过渡到生产，而不会遇到很多麻烦，并且还有一些额外的优势，比如插入 [Microsoft [Azure] Purview](https://www.microsoft.com/en-us/security/business/risk-management/microsoft-purview-data-governance/) 等工具，以更好地保护 AI 数据。”

## 简化开发的关键功能

AutoGen Studio 包含一些旨在简化开发过程的功能，例如用于指定代理工作流的直观的拖放式 UI；交互式评估和调试功能；以及可重用代理组件库。

这些功能建立在无代码多代理开发工具的四个核心设计原则之上，尽管微软尚未详细披露这些原则。

## 正在进行的工作

虽然 AutoGen Studio 代表着 AI 代理开发的重大进步，但微软指出，它是一个仍在开发中的研究项目，可能永远不会成为独立的产品。该公司包含以下警告：“AutoGen Studio 目前正在积极开发中，我们正在快速迭代。请注意，我们可能会在未来几周的版本中引入重大更改……”

然而，底层的 AutoGen 框架已经在各个行业找到了应用，包括：

- 广告
- 客户支持
- 网络安全
- 数据分析
- 教育
- 金融
- 软件工程

## 巨大的潜力

这种广泛的适用性突出了 AutoGen Studio 在各个领域的潜在影响。

Bloomberg 表示：“AI 代理可以在组织的云原生策略中发挥重要作用，因为每个代理都可以无状态地运行在容器中。”“因此，每个代理平台都有能力自动扩展代理，根据需要部署尽可能多的相同代理来应对任何情况。”

此外，基于生成式 AI 的代理正在迅速取代机器人流程自动化 (RPA) 机器人——但彭博社告诉 The New Stack，故事还有更多内容。“这些技术正在逐渐取代 RPA，以及业务流程自动化、低代码/无代码平台、规则引擎、数据集成技术等等。”

微软鼓励开发人员将 AutoGen Studio 用于原型设计和演示目的，而不是作为生产就绪的应用程序。对于需要身份验证和高级安全等功能的已部署应用程序，建议开发人员直接在 AutoGen 框架上构建。

随着 AI 不断发展并重塑各个行业，像 AutoGen Studio 这样的工具将在民主化 AI 开发和促进多代理系统创新方面发挥至关重要的作用。
