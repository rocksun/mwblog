![在 AWS 收购 DuckLabs 以及 DuckDB 2.0.0（迄今为止最大规模的功能更新）发布之后，DuckDB 正迈入一个新时代。在本期《The New Stack》播客中，DuckLabs 开发者布道师 Gábor Szárnyas 探讨了这款高性能分析型数据库如何演进，以支持 AI 智能体、实现更快的查询以及更灵活的数据处理。](https://cdn.thenewstack.io/media/2026/11/90305fd8-thumbnail-23-1024x576.png)

DuckDB 一直是一款无需配置的数据库：将其导入代码即可开始查询。DuckDB 2.0 已于 10 月发布，现在它可以作为服务器运行，供其他机器连接。DuckLabs 的 [Gábor Szárnyas](https://www.linkedin.com/in/szarnyasg/) 将此称为该版本的重磅特性。

由于该特性连同全新的存储格式和全新的 SQL 解析器，标志着 DuckDB 工作方式的重大转变，团队决定将此次最新升级定为一个主版本（major release）。在 *The New Stack* 播客中，[Szárnyas](https://www.linkedin.com/in/szarnyasg/) 解释了版本变化、早期用户在 2.0.1 错误修复版本发布前给团队带来的启发，以及如何规划生产环境升级。

视频

代号为 Cinnamon Teal 的 DuckDB 2.0 是这款分析型数据库迄今为止规模最大的功能发布，距离 1.0.0 版本发布已过去两年多。

我们在位于阿姆斯特丹的 DuckLabs 总部见到了公司开发者关系负责人 Szárnyas。DuckDB 2.0 能够作为服务器运行，并以更快的速度查询数据。

“其他特性还包括一个可扩展的 SQL 解析器，它在今年早些时候还处于实验阶段，但现在已成为默认开启的功能。理想情况下这不会破坏任何现有功能，但仍有可能带来影响，”Szárnyas 表示，“我们还希望通过此次发布以及向更多网络化操作转型的整体方案来体现这一点，将 [Quack 远程协议](https://duckdb.org/quack/)作为一等公民内置于 DuckDB 中。”

使用 DuckDB 2.0 创建的数据库文件无法被早期版本打开，不过 2.0 仍可读写现有的数据库文件，且这些旧文件依然能被旧版本读取。对于生产系统，Szárnyas 重申了数据库领域的常见经验法则：“永远不要在生产环境中迁移到 .0 版本。”他表示，根据团队的风险承受能力，2.0.1 或 2.0.2 才是适合将生产环境迁移过去的版本。团队目前正在开发 2.0.1，专注于错误修复、小幅性能调优以及用户反馈。

DuckDB 2.0.0 已经内置了专门的[智能体模式](https://duckdb.org/docs/2.0/clients/cli/agent_mode)，这使得 AI 编程智能体更容易理解报错并自行修正 SQL 查询，从而在不浪费 Token 的情况下更快获得更好的结果。

> “AI 并不真的在乎这些。大语言模型不介意文本格式是否糟糕，或者标点符号是否完美。”

“针对 AI 智能体，我们只需以无空格的紧凑模式输出简单的 Markdown 表格。AI 并不真的在乎这些。大语言模型不介意文本格式是否糟糕，或者标点符号是否完美，”Szárnyas 说，这使得 DuckDB 能够“将这些表格压缩到原始大小的 60% 到 70% 左右，而智能体阅读起来同样清晰”。

智能体模式不设隐藏截断，提供以 JSON 结构化的机器可读错误，并配有防止失控查询的护栏，同时支持 Claude Code、Codex 和 Cursor 等编程智能体。

继亚马逊于 8 月宣布收购 DuckLabs 后，AWS [分享了其如何在内部使用这款进程内分析引擎](https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/)，包括用于在 S3 Tables 中执行查询。AWS 技术副总裁 Mai-Lan Tomsen Bukovec 表示，AWS 使用集成并优化了 DuckDB 的自研 Quick 查询引擎，已处理了超过 25 亿次查询。她写道，DuckDB 帮助 Amazon Quick 将平均查询延迟降低了 30%。

DuckDB 还将成为 AWS 存储与分析服务的通用 SQL 方言。在 10 月的第三季度财报电话会议上，亚马逊 CEO Andy Jassy 指出，这将通过“一种快速、易用且无处不在的现代分析引擎”来简化数据处理，“客户只需编写一次 SQL 查询，即可使用任何 AWS 分析服务来执行”。这包括查询引擎之间零迁移或零移植成本，Jassy 表示这还将有助于 AI 智能体高效地查询数据。

文章《[DuckDB 2.0 转向客户端-服务器架构，并为编程智能体新增智能体模式](https://thenewstack.io/duckdb-storage-compatibility-agents/)》首发于 [The New Stack](https://thenewstack.io)。