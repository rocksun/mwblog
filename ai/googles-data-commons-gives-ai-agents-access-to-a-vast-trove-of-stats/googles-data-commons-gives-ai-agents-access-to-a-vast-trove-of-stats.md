<!--
title: 谷歌Data Commons：AI智能体的数据宝库
cover: https://cdn.thenewstack.io/media/2025/09/8a4e910d-kai-wenzel-06mhffyv6yy-unsplash-scaled.jpg
summary: 谷歌Data Commons推出模型上下文协议(MCP)服务器，赋能AI代理用海量公共数据回答复杂查询，减少幻觉。与ONE Campaign合作，简化全球发展数据访问。
-->

谷歌Data Commons推出模型上下文协议(MCP)服务器，赋能AI代理用海量公共数据回答复杂查询，减少幻觉。与ONE Campaign合作，简化全球发展数据访问。

> 译自：[Google’s Data Commons Gives AI Agents Access to a Vast Trove Of Stats](https://thenewstack.io/googles-data-commons-gives-ai-agents-access-to-a-vast-trove-of-stats/)
> 
> 作者：Frederic Lardinois

[Data Commons](https://datacommons.org/) 可能是谷歌鲜为人知的计划之一，但该项目收集了广泛主题和地理范围的[公共数据集](https://datacommons.org/data/agriculture)（以及查询和可视化这些数据的工具），当你寻找权威数据源来丰富你的应用程序或专有数据集时，它会非常方便。但在AI的新时代，Data Commons也有了新的用例，包括用真实世界的统计信息来增强大型语言模型（LLM），以减少AI代理在回答事实性问题时的幻觉。

为了让开发者更容易地将这些海量数据引入他们的代理，Data Commons 今天推出了其模型上下文协议（Model Context Protocol）服务器，而无需直接与 Data Commons API 交互。

“要从传统数据库编译一份可靠的报告，用户需要跨数据集工作并手动提取数据，”谷歌在今天的公告中解释道。“然而，代理能够理解复杂的查询，并能快速获取和编译所需数据。”

## 入门

谷歌为其自有的 [Gemini CLI](https://github.com/datacommonsorg/agent-toolkit/blob/main/docs/quickstart.md) 和 [代理开发工具包](https://github.com/datacommonsorg/agent-toolkit) 提供了 Data Commons MCP 服务器入门教程，以及针对 [Google Collab 用户](https://colab.research.google.com/github/datacommonsorg/agent-toolkit/blob/main/notebooks/datacommons_mcp_tools_with_custom_agent.ipynb) 的说明。不过，由于它是一个标准的 MCP 服务器，将其集成到任何代理工作流程中应该没有任何障碍。

谷歌表示，有了这个，代理将能够回答诸如“比较金砖国家（BRICS nations）的预期寿命、经济不平等和GDP增长”以及“生成一份关于美国各县收入与糖尿病之间关系的简明报告”等问题。

## Data Commons MCP 的实际应用：与 ONE Campaign 合作

为了试用 MCP 服务器，谷歌与 [ONE Campaign](https://www.one.org/us/) 合作，这是一个非营利组织，旨在“汇集基层活动家、尖端数据分析、值得信赖的使者和数十年的专业知识，以建立政治资本并推动政策和投资，从而创造一个更具韧性、更公平的未来。” 两个组织共同构建了 [ONE Data](https://data.one.org/) 平台，该平台结合了 ONE 的全球发展数据和 Data Commons 中的公共数据集。谷歌和 ONE 随后在该平台之上构建了一个代理，允许任何人快速地用自然语言搜索这些数据源。

“迫切需要加强发展中国家的卫生系统，但寻找关于卫生筹资的可靠数据是一个重大挑战——真正是在大海捞针，”该公司指出。“信息分散在数千个不同的信息孤岛中，埋藏在不同的报告格式里，由技术术语组织，并存储在几个独立的数据库中。现在，例如，如果你想识别哪些国家面临捐助者削减资金的风险，你可以快速搜索那些最依赖外部卫生资金的国家，因此这些国家最容易受到援助减少或债务冲击的影响。”