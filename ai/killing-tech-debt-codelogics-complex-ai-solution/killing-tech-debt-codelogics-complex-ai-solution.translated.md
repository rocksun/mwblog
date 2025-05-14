# 消除技术债务：CodeLogic 复杂的 AI 解决方案

![Featued image for: Killing Tech Debt: CodeLogic’s Complex AI Solution](https://cdn.thenewstack.io/media/2025/05/ef6452b5-tech-debt-mud-2-1024x576.jpg)

迈阿密 — [Edwin Gnichtel](https://www.linkedin.com/in/ned-gnichtel-12039965/) 见过不少烂摊子——他说的烂摊子指的是遗留应用程序和 IT 系统。

Gnichtel 是 [CodeLogic](https://codelogic.com/) 的 CEO，这是一家软件智能自动化平台，正在部署 AI 来解决技术债务。此前，他是 CodeLogic 的首席技术官，也曾在 [底层软件工程](https://www.technologyandstrategy.com/news/what-is-a-low-level-software-engineer) 领域工作过。

他在周二的 [Infobip Shift Miami](https://shift.infobip.com/us/#hero)（一个专注于 AI 的开发者大会）上告诉听众，情况非常糟糕，难以用图表表示。

“为什么我们有 75,000 个类？”他问道。“这是一个真实系统中的真实数字。顺便说一句，这只是一个系统，它是更大的系统生态系统的一部分。”

## 导致技术债务的开发原因

开发工作中存在许多[技术债务](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/)的原因。他指责 [Agile](https://thenewstack.io/agile-reinvented-a-look-into-the-future/) 通过其无休止地推向生产来增加债务，并补充说，虽然他是 Agile 的支持者，但它对快速交付的关注通过优先考虑功能而非代码质量来加速技术债务。

此外，他指出系统构建在过时的框架之上。另外，现在没有人真正做系统架构了，他补充道。他还指责[对微服务的误解](https://thenewstack.io/how-to-fail-at-microservices/)。

“有多少组织认为，仅仅将他们现有的东西放入容器中，突然间就神奇地将其变成了微服务？”他反问道。

他展示了一个较小应用程序的知识图，该应用程序“仅仅”有 5000 个类、34,000 个方法、300 个表、4700 个 SQL 函数以及无数的边缘连接，形式为类派生和方法到方法的调用。

![A blob of pastel colors that represents an IT application.](https://cdn.thenewstack.io/media/2025/05/3c9d92e6-code_debt_visualization.jpg)

一个小型应用程序的许多依赖关系的图。

“当你得到一个更大的应用程序时，我甚至无法在视觉上表示它，”他说。“[它] 只是屏幕上的一团颜色。”

## AI 在技术债务中的作用

在这种泥泞的混乱中，我们正在添加 AI 生成的代码。

“AI 有可能使情况变得更糟，”他说。“它写在一堆垃圾之上，最终不会带来好的结果。所以我们正在推动技术债务。”

各组织正在处理无休止的代码维护。简而言之，他认为，这不再是人类可以解决的问题。

但也许 AI 可以。

CodeLogic 的方法是首先使用 AI 代理创建一个大型知识图来映射系统的复杂性。

“在许多情况下，只有在执行代码时才能真正看到大量的依赖关系——例如，程序生成的连接对象、某些类型的构造数据库查询，以及各种各样的事情，”他说。

他补充说，执行环境、解释器和构建环境（包括编译器）喜欢注入东西。例如，[Java](https://thenewstack.io/java-modernizes-new-tools-for-ai-and-quantum-age/) 使用 lambda。他说，Lambda 实际上并不存在。他解释说，当你查看字节码时，它只是被转换为类和方法。

“这只是 Java 的想象，”他说。

他补充说，所有这些依赖关系都必须被捕获。CodeLogic 的数据模型位于产品之下，提供差异分析并提供影响信息，以帮助公司了解一切是如何连接的。

## 使用 AI 的复杂解决方案

CodeLogic 对多个模型的使用展示了如何使用 AI 构建复杂的系统。

CodeLogic 一直计划使用机器学习和其他 AI 技术，但他们没有预料到的是，一旦他们堆叠模型、部署 MCP 服务器并使用其他技术来改进[大型语言模型](https://thenewstack.io/what-is-a-large-language-model/)，这些模型会改进得如此之快。

“它使我们能够真正快速地解决这个问题，”他说。

带有 MCP 服务器的 [检索增强生成](https://thenewstack.io/retrieval-augmented-generation-for-llms/) 允许他们与 LLM“对话”，以指向必须审查的代码。影响分析揭示了重写可能影响的所有部分，包括多个“跳跃”之外的部分，例如 REST 端点、API 边界和数据库。
这个过程并非总是直接明了，可能需要重新提示并对照 CodeLogic 系统进行检查，以了解 AI 的认知。他表示，应该对其进行跟踪，以确保它不会破坏依赖关系。还需要人工参与来批准更改。

CodeLogic 创建了一个多图微分分析，可以开始生成所有必需的磁盘集。该分析由一个模型解释，然后生成一个微分集。该微分集由另一个模型解释，该模型生成提示和工单集。

这些可以放入 [JIRA](https://thenewstack.io/why-developers-hate-jira-and-what-atlassian-is-doing-about-it/) 中，以便 AI 可以负责关闭工单。

“归根结底，关键在于它也编写提示，”他说。“这些提示可能非常复杂，然后会被直接推回到生成端的增强型 AI 中，即代码生成端，这使你可以完成所有这些工作。”

最后一部分是帮助开发人员[停止产生技术债务](https://thenewstack.io/stop-technical-debt-before-it-damages-your-company/)。例如，开发人员可以询问 CodeLogic 系统，如果引入特定版本的库会发生什么。

他说：“我们围绕注释语言提供了一些功能，如果你进行了更改，人们会收到通知，并且会受到惩罚。”

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)