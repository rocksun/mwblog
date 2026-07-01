[JetBrains](https://www.jetbrains.com/)，即 IntelliJ IDEA IDE 背后的捷克开发工具公司，于[周一宣布](https://blog.jetbrains.com/idea/2026/06/kotlin-notebook-sunset/)将停止维护 [Kotlin Notebook](https://kotlinlang.org/docs/kotlin-notebook-overview.html)，这是他们于 2023 年 7 月首次推出的交互式编程插件。

从 [IntelliJ IDEA 2026.2](https://blog.jetbrains.com/idea/2026/05/intellij-idea-2026-2-eap/) 开始，该插件将从 IDE 中解绑，并以 Apache 2.0 许可证的形式移交给开源社区——这也是其源代码首次公开。JetBrains 将不会发布 2026.3 及更高版本的兼容版本，这意味着接手该项目的开发者将面临断层的兼容性问题。

> “Kotlin Notebook 的采用率未达到我们预期的水平。”

在项目发布近三年后，JetBrains JVM 生态系统负责人 [Marco Behler](https://www.linkedin.com/in/marco-behler-4b4b8a171/) 表示，该插件基本未能找到目标受众。“Kotlin Notebook 的采用率没有达到我们预期的水平，”Behler 写道。

他还指出，开发者的工作方式发生了更广泛的变革，而 AI 正是其中的主角。

“AI 工具改变了开发者探索代码、原型设计和迭代的方式，许多最初推动 Notebook 普及的工作流也随之演变，”他说道。

> “AI 工具改变了开发者探索代码、原型设计和迭代的方式。”

微软在 2 月采取了几乎相同的行动，当时它[低调宣布](https://github.com/dotnet/interactive/issues/4163)将弃用 Polyglot Notebooks——即其允许在 Jupyter 格式内运行 C# 及其他语言的 VS Code 扩展——且几乎只提前了一个月通知。在该插件被微软下架之前，其[安装量已超过](https://www.devclass.com/databases/2026/02/14/microsoft-deprecates-polyglot-notebooks-developers-react/4091167) 180 万次，评分为四星，微软当时引导用户转向“下一代 AI 驱动的编程体验”。

## Python 问题

尽管“AI 替代”的观点可能存在一定道理，但背后可能有一个更简单的解释：Notebook 是 Python 原生的习惯，并且一直如此。

[Jupyter](https://jupyter.org/) 格式（支撑 Kotlin Notebook 和 Polyglot Notebooks 的开放标准）[起源于 Python 和数据科学领域](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)。其内核协议是一种定义 Notebook 前端如何与语言运行时通信的开放规范，其设计本身与具体语言无关，这使得 JetBrains 和 Microsoft 在其基础上构建变得相对简单。但让 Notebook 真正发挥作用的工作文化——探索性分析、内联可视化、将结果作为动态文档共享——本质上属于使用 Python 的数据科学家，而非使用 Kotlin 或 C# 的应用程序开发人员。

JetBrains 试图将这种文化引入 IntelliJ 的 Kotlin 开发者群体中。微软也试图为其 C# 和 .NET 社区做同样的事情。然而，两个社区都没有像 Python 开发者采用 Jupyter 那样去采用它，而两家公司似乎都将 AI 作为退出的借口。

## Jupyter 的地位：并未被撼动

Jupyter Notebook 的使用率似乎依然十分强劲。根据 GitHub [最新的 Octoverse 报告](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)，包含 Jupyter Notebook 的仓库数量同比增长了 75%，从 140 万增长到 242 万。另一个数据点是：Jupyter Notebook 在带有 AI 标签的仓库中的使用率几乎翻了一番，拥有超过 40 万个活跃项目——这证明了它作为原型设计和运行 AI 实验首选环境的地位。

Google [Colab](https://en.wikipedia.org/wiki/Google_Colab) 的情况则完全不同。自 2017 年以来，Colab 从一开始就构建为面向数据科学家和机器学习研究人员的 Python 首选环境，它从未遇到过导致 Kotlin Notebook 和 Polyglot Notebooks 失败的受众问题——它一直服务于那些将 Notebook 作为日常工具的群体。Google [几年来](https://blog.google/innovation-and-ai/technology/developers-tools/google-colab-ai-coding-features/)一直在为 Colab 添加 AI 功能，并于 2025 年 6 月推出了完整的“[AI 优先](https://developers.googleblog.com/new-ai-first-google-colab-now-available-to-everyone/)”版本。其核心逻辑是将 Agent 能力直接集成到 Notebook 中，而不是将 AI 视为放弃它的理由。

对于 JetBrains 而言，Kotlin Notebook 的下线是其更大规模调整的一部分。正如 *The New Stack* [此前撰文](https://thenewstack.io/ide-vs-desktop-agent/)所言，传统 IDE 正受到 AI 原生编程工具的现实压力，这些工具越来越多地通过对话和 Agent 编排来处理任务，而不是依靠菜单和按键。6 月初，[JetBrains 开源了 Mellum2](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/)，这是一个为本地部署而构建的 120 亿参数编程模型——这是当前 AI 编程工具市场中的一次自信之举。在同一个月内砍掉一个利基插件并开源一个前沿模型，说明了 JetBrains 认为自己的未来所在——而那并不是说服 Kotlin 开发者像数据科学家一样工作。