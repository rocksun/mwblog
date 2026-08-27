<!--
title: “你可以租用一个功能，但你无法租用一个基础”：MotherDuck为何收购为其数据流水线提供动力的初创公司？
cover: https://cdn.thenewstack.io/media/2026/08/bae3f574-barsrsind-qtln4bddnce-unsplash-scaled.jpg
summary: 数据仓库公司MotherDuck收购了初创公司Tower，旨在强化其AI驱动的数据流水线运营能力。MotherDuck认为，关键基础设施不应仅靠租用，必须将其核心执行层整合至自家产品中，从而更好地支持AI代理构建、调度和管理数据任务。
-->

数据仓库公司MotherDuck收购了初创公司Tower，旨在强化其AI驱动的数据流水线运营能力。MotherDuck认为，关键基础设施不应仅靠租用，必须将其核心执行层整合至自家产品中，从而更好地支持AI代理构建、调度和管理数据任务。

> 译自：[“You can rent a feature, but you can’t rent a foundation”: why MotherDuck bought the startup already powering its data pipelines](https://thenewstack.io/motherduck-tower-acquisition-python/)
> 
> 作者：Paul Sawers

当您所依赖的技术属于他人时，您会怎么做？当然是收购其背后的初创公司。这正是数据仓库公司 [MotherDuck](https://motherduck.com/) 对 [Tower](https://www.tower.dev/) 所做的事情。Tower 是一家数据基础设施初创公司，其技术此前已为 MotherDuck 的 AI 构建的数据流水线提供支持。

这笔交易于周二宣布，是 MotherDuck 四年历史上的首次收购。随着 MotherDuck 进一步推动可以构建和操作数据流水线的 AI 代理，此次收购将 Tower 的技术和团队纳入旗下。

## Tower 展翅高飞

Tower 由前 Snowflake 工程师 Serhii Sokolenko（首席执行官）和 Brad Heller（首席技术官）于 2024 年末在德国创立。他们的理念是：一旦开发人员或 AI 助手编写了数据流水线的代码，仍然需要有人对其进行打包、部署到适当的基础设施中、连接凭据并进行维护——Sokolenko 在[三月份](https://thenewstack.io/tower-python-data-pipelines/)告诉 *The New Stack*，这项枯燥的工作构成了数据工程的“最后一英里”。

本质上，Tower 是 Python 流水线的托管运行时——它打包代码、部署代码并使其在生产环境中保持运行。它还提供在运行时之上构建的工具，例如基于浏览器的 AI 代理 [Tower Control](https://control.tower.dev/)，允许用户用简单的语言描述他们想要的流水线。

![使用 Tower Control，用户可以用简单的语言描述他们想要的流水线。](https://cdn.thenewstack.io/media/2026/08/15286e2c-gigf1.gif)

*使用 Tower Control，用户可以用简单的语言描述他们想要的流水线。*

Control 可以生成代码，将其部署为 Tower 应用程序并运行它——有效地将过程从提示（Prompt）转化为生产，而开发人员无需亲自设置底层的运行时。

![Control 可以生成代码，并将其部署为 Tower 应用程序。](https://cdn.thenewstack.io/media/2026/08/b86ca8af-gigf2.gif)

*Control 可以生成代码，并将其部署为 Tower 应用程序。*

MotherDuck 本身是一个基于开源数据库 [DuckDB](https://duckdb.org/) 的无服务器数据仓库，由前 Google BigQuery 工程负责人 Jordan Tigani 于 2022 年创立。该公司 [自成立以来](https://techcrunch.com/2023/09/20/database-startup-motherduck-lands-52-5m-to-grow-its-duckdb-based-platform/) 已 [融资](https://motherduck.com/blog/announcing-series-seed-and-a/) 约 1 亿美元。

MotherDuck 的 [最初理念](https://thenewstack.io/motherducks-hybrid-query-execution-enhances-real-time-data-analytics/) 侧重于速度和本地计算：查询可以在笔记本电脑上通过 DuckDB 运行，也可以在 MotherDuck 的云端运行，或者两者结合——这与 Snowflake、Databricks 和 BigQuery 的“云优先”模型有所不同。最近，MotherDuck [扩展了](https://thenewstack.io/motherduck-duckdb-mcp-collaboration/) 这种方法以支持 AI 代理，使用 MCP 让代理能够直接与数据交互。六月份推出的 [Flights](https://motherduck.com/blog/flights-agent-native-ingest/) 功能使事情有了更具操作性的转变，该功能通过同一个 MCP 服务器公开了一个通用 Python 运行时，让代理能够创建、运行和调度数据流水线。

事实证明，Tower 正是支撑 Flights 的关键基础设施。

## “我们几乎一夜之间成了他们最大的客户”

Tower 与 MotherDuck 的合作实际上早于 Flights。Tigani 表示，MotherDuck 最初一直在寻找一种第三方工具，可以推荐给客户作为将数据导入其仓库的更简单方法。但随后 AI 的进步改变了公司认为需要解决的问题的本质。

> “当 AI 突然开始能够解决数据问题时，我们意识到我们对问题的思考方式错了。”

“当 AI 突然开始能够解决数据问题时，我们意识到我们对问题的思考方式错了，”Tigani 告诉 *The New Stack*。“Claude 可以通过编写连接器来帮助人们移动数据，从而解决我们试图解决的问题，但它无法做到的是沙箱化（sandboxing）和调度。”

这导致 MotherDuck 需要一个地方来安全地执行这些代理生成的代码、管理凭据并按计划运行作业。碰巧的是，Tower 已经提供了这些功能。

“它完美地解决了我们的问题，让我们在短短几周内就发布了 Flights，”Tigani 补充道。

对于 MotherDuck 来说，Tower 提供了缺失的执行层；对于 Tower 来说，这种认识转化为一种重要的客户关系。“我们几乎一夜之间成了他们最大的客户，从那时起，我们的团队就一直在合作交付产品，”Tigani 说。

如此早就关注 Tower 也让 MotherDuck 有机会在决定是否自己构建类似产品之前测试该技术及其背后的团队。Tigani 表示，最终的考量归结为 MotherDuck 能以多快的速度将想要的功能交付到客户手中。

“自己构建总是很有诱惑力，但在尝试了 Tower 之后，我们很快意识到，为了让我们底层的基础设施真正发挥作用，我们需要解决一堆问题，而 Tower 几乎就是我们需要的一切，”他说。

最终，Tower 在 MotherDuck 想要构建的东西中变得越重要，彻底拥有该技术的理由就越充分。Tigani 认为，一旦 Tower 开始执行在 MotherDuck 内部创建和调度的作业，客户必然会要求 MotherDuck 对该运行时的安全性、可靠性和行为负责。

“我在我工作过的每一家基础设施公司都重学过一条规则：你可以租用一个功能，但你无法租用一个基础，”Tigani 说。“当 MotherDuck 内部的一个代理构建了一个作业并对其进行调度时，执行该作业的东西就是我们的产品——无论上面印着什么标志。”

> “我在我工作过的每一家基础设施公司都重学过一条规则：你可以租用一个功能，但你无法租用一个基础。”

MotherDuck 现在希望利用该技术实现的一个例子包括将 Flights 与 [Dives](https://motherduck.com/docs/key-tasks/dives/) 结合起来，这是它在 [二月份发布](https://motherduck.com/blog/duck-dive-and-answer/) 的一种 AI 生成的数据可视化功能。Tower 可以为通过 Flights 运行的作业生成稳定的 URL，从而有效地允许这些作业充当 Dive 或其他前端可以调用的数据 API。

Tigani 举了一个显示用户推荐的应用程序的例子。Dive 可以生成查看这些推荐的界面，而 Flight 可以处理创建或修改它们的请求。Flight 可以限制和验证用户被允许做出的更改，而不是给前端提供对底层数据的广泛写入权限。

“当你把它们放在一起时，你就可以构建丰富的应用程序，”Tigani 说。

## Tower 的下一个篇章

所有这些都给 Tower 客户提出了一个显而易见的问题。这家初创公司推销的一部分是，开发人员可以使用其运行时而不必将自己绑定到特定的数据平台，而现在 Tower 本身属于其中一个平台。

Tower 联合创始人兼首席执行官 Serhii Sokolenko 认为，MotherDuck 代表了与行业内大型云数据平台不同的“家”。他的观点是，Tower 可以更深入地集成，而不必围绕在 AI 代理出现之前很久就建立的架构进行调整。

“加入超大规模云服务商（hyperscaler）通常意味着要适应其遗留架构，”Sokolenko 告诉 *The New Stack*。“加入 MotherDuck 让我们能够帮助塑造数据和 AI 基础设施的发展方向。”

> “加入超大规模云服务商通常意味着要适应其遗留架构。”

不过，仍然存在权衡。Tower 正在放弃作为数据库不可知论者（database-agnostic）所带来的部分广度，以换取围绕一个平台进行更具体的构建——这是一种赌注，即更紧密的集成最终将产生比远程支持许多系统更好的体验。

“通过将 Tower 的 Python 计算专门集中在 MotherDuck 上，我们正在用广泛的基础连接换取深度、原生的执行，”他说。

Sokolenko 的论点是，“锁定（lock-in）”问题随之转移到了下一层。Tower 现在可能与 MotherDuck 绑定得更紧密，但他表示，由于 MotherDuck 本身是建立在 DuckDB 之上的，底层的数据仍然是开放和可移植的。其目标是在不将数据本身困在专有系统内的情况下，让运行时、代理和仓库更紧密地结合在一起。

这也解释了为什么 MotherDuck 的混合执行模型吸引了 Tower。DuckDB 允许工作在本地计算和云计算之间移动，Sokolenko 认为这与 Tower 自身的方向高度一致。

“这直接符合 Tower 的愿景——允许业务用户和代理无缝地从本地数据探索转向云端生产执行，”他说。

对于 Tower 的现有客户，眼前的未来意味着向 MotherDuck 迁移。Sokolenko 表示，Tower 客户已经在与 MotherDuck 讨论迁移路径，而之前使用过 Tower 的人将被邀请尝试 MotherDuck 及其更广泛的代理数据功能。

Tigani 证实，MotherDuck 正在努力将现有 Tower 客户迁移到 Flights，尽管他承认这两个产品并不完全相同。“存在一些差异，我们正在努力弥合差距，使过渡更加无缝，”他说。

与此同时，Tower 的技术将被更深入地整合到 MotherDuck 本身中。今天，MotherDuck 有两个独立的沙箱化、按需运行时：由 Tower 支持的 Flights，以及它的无服务器 DuckDB 实例 [Ducklings](https://motherduck.com/docs/about-motherduck/billing/duckling-sizes/)。Tigani 表示，计划最终将两者合并，结合 Ducklings 的近乎即时启动与 Tower 作业提供的更强大的沙箱化能力。

## 驾驭代理浪潮

MotherDuck 绝不是唯一一家推动数据代理超越回答问题范畴的公司。Databricks 的 [Genie Code](https://www.databricks.com/blog/introducing-genie-code) 可以在 Databricks 内部生成并运行代码、构建流水线和调试故障。与此同时，Snowflake 也一直在 [以 CoCo 等](https://www.snowflake.com/en/news/press-releases/snowflake-unveils-cortex-code-an-ai-coding-agent-that-drastically-increases-productivity-by-understanding-your-enterprise-data-context/) 为代表的 AI 编码代理方向发展，而 [较新的 CoCo Automations](https://docs.snowflake.com/en/release-notes/2026/other/2026-08-21-cortex-code-automations-preview) 可以在 Snowflake 管理的沙箱内调度无人值守的代理运行。

细节各不相同，但两者都指向了数据行业的更广泛转变：为 AI 代理提供基础设施，以对数据采取行动并操作其周围的系统，而不仅仅是查询现有的内容。

> “AI 使构建我们五到十年前无法想象的有用功能成为可能。平台是数据资产中最复杂的部分，因此仓库供应商很有优势处于任何新模式的核心位置。”

Tigani 预见这种情况已经有一段时间了。今年早些时候，[他概述了](https://motherduck.com/blog/water-town-agent-swarm-data-stack/) 一个未来，数据工程日益成为一个代理监督问题，代理处理诸如构建和修复流水线以及响应模式和数据质量变化等任务，而人类监督它们的工作。他还 [曾将](https://motherduck.com/blog/future-casting-the-modern-data-stack/) LLM 的进步比作数据公司必须学习驾驭的浪潮。

“我喜欢这样思考——数据平台供应商正在应对新的机会，以改善客户的生活，”Tigani 说。“AI 使构建我们五到十年前无法想象的有用功能成为可能。平台是数据资产中最复杂的部分，因此仓库供应商很有优势处于任何新模式的核心位置。对 Tower 的收购为我们提供了一个部署、跟踪和调度数据代理的平台，这应该能让我们处于驾驭这股浪潮的有利位置。”