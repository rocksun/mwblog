[Prefect](https://www.prefect.io/) 以其同名的开源数据流水线和工作流编排工具而闻名，该公司近日[宣布](https://www.prefect.io/prefect-acquires-dagster)收购 [Dagster](https://dagster.io/)。Dagster 与 Prefect 本身一样，是 [Apache Airflow](https://thenewstack.io/apache-airflow-3-0-from-data-pipelines-to-ai-inference/) 最重要的替代方案之一。

该交易尚未正式完成，它将两家最成熟的 Airflow 挑战者合并为一家公司。开源编排工具 Dagster 和全托管云产品 [Dagster+](https://dagster.io/lp/dagster-plus-trial) 将保留其现有的名称、定价和产品路线图，约 40 名 Dagster 团队成员将作为交易的一部分加入 Prefect。

在周一发表的 [LinkedIn 文章](https://www.linkedin.com/feed/update/urn:li:activity:7482460618369753088/)中，Prefect 创始人兼首席执行官 Jeremiah Lowin 解释说，此次收购是对 AI 代理可靠运行所需各种组件的押注：明确定义的目标，以及在自身决策将任务引向未脚本化路径时进行临时调整的灵活性。

据 Lowin 所述，Dagster 通过定义和跟踪结果来处理目标设定方面的工作；Prefect 通过运行工作本身来处理临时调整；而 [FastMCP](https://gofastmcp.com/)（Prefect 用于将代理连接到外部系统的自有工具）则控制代理在执行过程中被允许触达的范围。

> “现代编排领域有了新的重心。”

对于 Lowin 来说，这次收购的核心在于规模化。

“现代编排领域有了新的重心，” Lowin 写道。

## 合二为一

这一“规模化”的举措距离 Prefect 和 Dagster 开始竞争已过去七年，当时两者作为 Airflow 的挑战者崭露头角，而 Airflow 是大多数团队用于调度和运行数据流水线的默认工具。

Prefect 致力于简化生产环境下的工作流编排，并提高其可靠性，以服务 Python 开发者。Dagster 则专注于使数据流水线更易于定义、理解和验证，更强调流水线应该产生什么结果，而不是仅仅运行一系列任务。

> “多年来，Prefect 和 Dagster 互相提高了彼此及我们这一领域的门槛。这种竞争产生了两个出色的产品，以及数据生态系统中最强大的两个开源社区。”

“多年来，Prefect 和 Dagster 互相提高了彼此及我们这一领域的门槛，” Lowin 写道，“这种竞争产生了两个出色的产品，以及数据生态系统中最强大的两个开源社区。”

这两家公司为运行流水线而构建的优势，现在正被扩展以覆盖更广阔的领域，Prefect 押注这些同样的优势正是 AI 代理工作负载未来所需要的。

## AI 的转型

两家公司在一段时间内一直在围绕 AI 代理进行重新定位。早在 2024 年，[Prefect 3.0 的发布明确聚焦于](https://www.prefect.io/blog/introducing-prefect-3-0)支持代理工作流。一年后，[Dagster 推出了 Components](https://dagster.io/blog/accelerate-data-pipeline-development-with-dagster-components)，这被宣传为一种使用基于 YAML 的可重用构建块而不是手写 Python 来构建流水线的方法。不久之后，[Dagster 通过 Compass 更进一步](https://dagster.io/blog/introducing-compass)，这是一个让分析师通过 Slack 发送自然语言提示而不是编写 SQL 来查询数据的工具。

然而，这些都无法与 Prefect 通过 FastMCP 构建的影响力相提并论。该框架与模型上下文协议 (Model Context Protocol, MCP) 协同工作，这是 Anthropic 在 [2024 年底发布](https://www.anthropic.com/news/model-context-protocol)的开放标准，它允许 [AI 模型发现](https://thenewstack.io/why-the-model-context-protocol-won/)并调用外部工具和数据，使开发者能够通过编写简单的 Python 函数而不是直接手写协议来构建 MCP 服务器。Prefect 在 MCP 启动的 [同一个月就推出了 FastMCP](https://jlowin.dev/blog/introducing-fastmcp)，Anthropic 后来将其采纳为 MCP 的[官方 Python SDK](https://pypi.org/project/mcp/)。

这两家公司的演变促成了此次极具战略意义的收购，但对于那些自早期以来一直引导 Dagster 的人来说，这笔交易产生了深远影响。Nick Schrock 是 Dagster 的创始人，他于 2022 年从[首席执行官转任首席技术官](https://dagster.io/blog/pete-hunt-path-to-elementl-part2)，为 Pete Hunt 让位。在官方的[收购公告](https://www.businesswire.com/news/home/20260713065285/en/Prefect-Acquires-Dagster-Uniting-the-Two-Leading-Modern-Orchestrators)中，他与 Hunt 一起被提到，将“担任 Prefect 的战略顾问”，同时继续“活跃在开源社区中”。

然而，Schrock 在周一发表的[个人博客文章](https://dagster.io/blog/prefect-is-acquiring-dagster)读起来更像是与 Dagster 的彻底决裂。

“我想分享的是，我将离开这个项目和公司，” Schrock 写道。

Schrock 的离职为 Dagster 的一个章节画上了句号。然而，此次收购本身却开启了另一个篇章，Prefect 押注两家公司多年来为数据编排所发展的理念，在 AI 代理进入生产环境时将证明其价值。