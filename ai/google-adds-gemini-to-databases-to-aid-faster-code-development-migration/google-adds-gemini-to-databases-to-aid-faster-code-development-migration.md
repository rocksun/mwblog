
<!--
title: Google添加Gemini到数据库，加快代码开发和迁移
cover: ./cover.png
-->

预计 Gemini 在 Google Cloud 数据库产品中的可用性将帮助开发者比去年集成的 Duet AI 更快地编写代码和迁移。

> 译自 [Google adds Gemini to databases to aid faster code development, migration](https://www.infoworld.com/article/3715160/google-adds-gemini-to-databases-to-aid-faster-code-development-migration.html)，作者 Anirban Ghoshal。

Google Cloud 宣布，其数据库产品（包括 Bigtable、Spanner、Memorystore for Redis、Firestore、CloudSQL for MySQL 和 AlloyDB for PostgreSQL）将添加由其专有[大型语言模型](https://www.infoworld.com/article/3709489/large-language-models-the-foundations-of-generative-ai.html) Gemini 驱动的功能。

目前处于公开预览阶段的 Gemini 驱动的功能包括 [SQL](https://www.infoworld.com/article/3219795/what-is-sql-the-lingua-franca-of-data-analysis.html) 生成和 [AI](https://www.computerworld.com/article/1647870/what-is-artificial-intelligence.html) 协助管理和迁移数据库。

去年，该公司 [在 Spanner 及其数据库迁移服务中添加了 Duet AI，现已成为 Gemini](https://www.infoworld.com/article/3705374/google-expands-duet-ai-features-across-its-cloud-services.html)。

可以通过该公司名为 Database Studio 的 SQL 编辑器访问 SQL 生成功能，该编辑器可在 Google 的 Cloud Console 中找到。

该公司表示，顾名思义，此功能允许开发人员在 Database Studio 中直接使用智能代码协助、代码完成和指导轻松生成、总结和修复 SQL 代码，从而提高生产力，并补充说 Database Studio 同时支持 [MySQL](https://www.infoworld.com/article/2615974/applications-how-to-get-started-with-mysql.html) 和 [PostgreSQL](https://www.infoworld.com/article/3698688/serverless-is-the-future-of-postgresql.html) 方言。

此外，该公司表示，Database Studio 带有一个上下文感知聊天界面，可以输入自然语言，以帮助更快地构建数据库应用程序。

分析师称，谷歌并不是将 SQL 代码生成添加到其功能列表中的唯一数据库提供商。

“在生成式 AI 的协助下进行 SQL 代码生成已成为过去一年生成式 AI 手到擒来的成果之一，”dbInsight 的首席分析师 Tony Baer 说道。

“新一代生成式 AI 数据库代码助手最终应该具备相较于迎合通用语言的助手而言的关键优势，即专属于数据库，因此它们可以读取数据库的元数据，不仅形成，还能优化 SQL 代码，” Baer 解释道。

### 使用 Gemini 管理和迁移数据库

为了帮助更好地管理数据库，云服务提供商正在添加一项名为 Database Center 的新功能，该功能将允许操作员从单个窗格管理整个数据库群集。

该公司表示，Database Center 还提供智能仪表盘，以主动评估可用性、数据保护、安全性和合规性态势。

此外，该公司通过基于自然语言的聊天窗口将 Gemini 注入 Database Center，该窗口将允许企业团队与数据库交互并找到更多见解。

该公司表示，聊天窗口还可用于生成与数据库相关问题的故障排除提示。

Baer 说，谷歌有了通过单一窗格来管理多个数据库的想法，其灵感来自 Oracle。Baer 说，虽然 Oracle 提供了对同一数据库（这是多模态的）的多个实例的功能，但 Google 将该功能扩展到了异类数据库集合。

“拥有集中控制意味着企业可以对其安全、数据访问和服务级别协议 (SLA) 的策略保持一致。首席分析师解释说，这是朝着我们期望从云端获得的简化迈出的重要一步。

谷歌还将其 Gemini 扩展到其数据库迁移服务，该服务之前支持 Duet AI。

该公司表示，Gemini 改进的功能将使该服务变得更好，并补充说，Gemini 可以帮助将数据库驻留代码（例如存储过程、函数）转换为 PostgreSQL 方言。

此外，由 Gemini 驱动的数据库迁移还重点说明了使用并排比较方言以及代码的详细解释和建议来解释代码翻译。

该公司表示，专注于解释代码的计划旨在帮助升级和重新培训 SQL 开发人员的技能。

### AlloyDB AI 获得新功能

除了使用 Gemini 为数据库提供支持外，Google 还为 AlloyDB AI 添加了新功能。

去年作为 [AlloyDB for PostgreSQL](https://www.infoworld.com/article/3660548/why-google-cloud-will-battle-aws-azure-in-a-red-hot-postgresql-market.html) 数据库服务的一部分[推出](https://www.infoworld.com/article/3705374/google-expands-duet-ai-features-across-its-cloud-services.html)的 AlloyDB AI 是一套集成功能，旨在帮助开发者利用实时数据构建基于生成式 AI 的应用程序。

新功能包括允许基于生成式 AI 的应用程序使用自然语言查询数据以及一种新型数据库视图。

该公司表示，启用自然语言查询数据功能将允许基于 AI 的应用程序响应企业团队提出的更多问题集。

另一方面，新型数据库视图（参数化安全视图）允许企业团队根据最终用户的上下文保护数据。AlloyDB AI 可以使用现已全面提供的 AlloyDB Omni 下载。

AlloyDB Omni 是 Google Cloud 的 PostgreSQL 兼容数据库服务的可下载版本。

其他更新包括添加 Bigtable Data Boost（类似于去年发布的 Spanner Data Boost）以及对 Memorystore for Redis 的性能增强。