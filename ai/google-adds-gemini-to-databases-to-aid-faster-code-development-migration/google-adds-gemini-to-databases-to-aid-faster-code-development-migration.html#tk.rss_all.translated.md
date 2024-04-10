## Google Cloud 数据库添加由 Gemini 驱动的功能

Google Cloud 宣布，其数据库产品（包括 Bigtable、Spanner、Memorystore for Redis、Firestore、CloudSQL for MySQL 和 AlloyDB for PostgreSQL）将添加由其专有 [大型语言模型](https://www.infoworld.com/article/3709489/large-language-models-the-foundations-of-generative-ai.html) Gemini 驱动的功能。

目前处于公开预览阶段的 Gemini 驱动的功能包括 [SQL](https://www.infoworld.com/article/3219795/what-is-sql-the-lingua-franca-of-data-analysis.html) 生成和 [AI](https://www.computerworld.com/article/1647870/what-is-artificial-intelligence.html) 协助管理和迁移数据库。

去年，该公司 [在 Spanner 及其数据库迁移服务中添加了 Duet AI，现已更名为 Gemini](https://www.infoworld.com/article/3705374/google-expands-duet-ai-features-across-its-cloud-services.html)。

### SQL 生成

可以通过该公司名为 Database Studio 的 SQL 编辑器访问 SQL 生成功能，该编辑器可在 Google 的 Cloud Console 中找到。

该公司表示，顾名思义，此功能允许开发人员在 Database Studio 中直接使用智能代码协助、代码完成和指导轻松生成、总结和修复 SQL 代码，从而提高生产力，并补充说 Database Studio 同时支持 [MySQL](https://www.infoworld.com/article/2615974/applications-how-to-get-started-with-mysql.html) 和 [PostgreSQL](https://www.infoworld.com/article/3698688/serverless-is-the-future-of-postgresql.html) 方言。

此外，该公司表示，Database Studio 带有一个上下文感知聊天界面，可以输入自然语言，以帮助更快地构建数据库应用程序。

### 使用 Gemini 管理和迁移数据库

为了帮助更好地管理数据库，云服务提供商正在添加一项名为 Database Center 的新功能，该功能将允许操作员从单个窗格管理整个数据库群集。

该公司表示，Database Center 还提供智能仪表盘，以主动评估可用性、数据保护、安全性和合规性态势。

此外，该公司通过基于自然语言的聊天窗口将 Gemini 注入 Database Center，该窗口将允许企业团队与数据库交互并找到更多见解。

该公司表示，聊天窗口还可用于生成与数据库相关问题的故障排除提示。

### AlloyDB AI 获得新功能

除了使用 Gemini 为数据库提供支持外，Google 还为 AlloyDB AI 添加了新功能。

AlloyDB AI [去年推出](https://www.infoworld.com/article/3705374/google-expands-duet-ai-features-across-its-cloud-services.html) 作为其 [AlloyDB for PostgreSQL 数据库服务](https://www.infoworld.com/article/3660548/why-google-cloud-will-battle-aws-azure-in-a-red-hot-postgresql-market.html) 的一部分，是一套集成功能，旨在帮助开发人员使用实时数据构建基于生成式 AI 的应用程序。
**新功能**

* 允许基于生成式 AI 的应用程序使用自然语言查询数据
* 一种新型数据库视图：参数化安全视图

**自然语言查询**

该公司表示，使用自然语言查询数据的能力将允许基于 AI 的应用程序响应企业团队提出的更多问题集。

**参数化安全视图**

另一方面，新型数据库视图——参数化安全视图——允许企业团队根据最终用户的上下文保护数据。

**AlloyDB AI**

AlloyDB AI 可使用 [AlloyDB Omni](https://www.infoworld.com/article/3691825/google-ambushes-on-prem-postgresql-with-alloydb-omni.html) 下载，该产品现已普遍可用。AlloyDB Omni 是 Google Cloud 的 PostgreSQL 兼容数据库服务的可下载版本。

**其他更新**

* 添加类似于去年发布的 Spanner Data Boost 的 Bigtable Data Boost
* 对 Memorystore for Redis 的性能增强