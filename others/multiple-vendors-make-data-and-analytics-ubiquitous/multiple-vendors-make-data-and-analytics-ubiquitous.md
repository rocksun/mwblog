# 多个供应商使数据和分析无处不在

翻译自 [Multiple Vendors Make Data and Analytics Ubiquitous](https://thenewstack.io/multiple-vendors-make-data-and-analytics-ubiquitous/) 。

来自八家不同公司的消息显示，分析、数据管理、流数据和人工智能越来越多地混合在一起，都在云端。

![](https://cdn.thenewstack.io/media/2022/03/e0cb02e1-board-862112__340-e1678887435842.webp)

在过去的几周里，分析领域的许多新旧主要参与者发布了大量新闻。他们共同指出了该行业在 2023 年第一季度结束时的一些重要趋势。尽管分析领域可能很复杂，但人们开始觉得重要的想法和标准正在自我肯定并获得广泛采用。

数据湖技术的重要性和标准化程度的提高、人工智能和机器学习的持续重要性、在云中进行分析的额外动力、数据集成的持续相关性以及将分析技术嵌入主流生产力和开发人员工具中，所有这些都发挥着重要作用新闻中的作用。因此，让我们来看看过去几周来自八家不同供应商的公告，并分析它们对行业的意义。

## 冰山一角

为了说明这些趋势，让我们从数据湖和湖屋的世界开始，开源 Apache Parquet 文件格式及其衍生产品，如 Apache Iceberg 和 Delta Lake，继续获得发展势头。在 3 月 1 日的 Subsurface 活动中，数据湖/湖屋播放器 Dremio 宣布了对 Iceberg 表格式支持的多项增强。其中包括使用新支持的 SQL 命令 COPY INTO 将数据复制到 Iceberg 表中的能力；支持将多个文件合并为一个文件，使用 Dremio Sonar 中的新 OPTIMIZE 命令（现在也将联合更多数据源）；并添加了一个新的 ROLLBACK 命令以将表返回到以前的特定时间或快照 ID。所有这些功能似乎使 Iceberg 与竞争性 Delta Lake 格式中的类似功能相提并论，Delta Lake 格式最初由 Databricks 开发，但现在是一种在 Linux 基金会赞助下管理的开源技术。

正如我提到的，Delta Lake 和 Iceberg 本质上都是 Parquet 格式的衍生产品（尽管 Iceberg 在技术上也可以将其功能带到其他格式），这仅说明了 Parquet 在数据湖世界中的重要性。但看起来它在图数据库世界中也变得越来越重要。图数据库竞争者 TigerGraph 同样在 3 月 1 日宣布，它正在增加对 Parquet 的普遍支持，并提供以该格式摄取数据的能力。 TigerGraph 还在共享可视化图仪表板上添加协作编辑和查看功能，该公司正在增强其图数据科学包，通过 NodePiece 提供更好的图嵌入，并通过 pyTigerGraph 添加对自己的打包算法的支持。

巧合的是，TigerGraph 本周刚刚发布了一个基准测试，显然是在 VLDB Endowment 的支持下，重点关注图形分析的规模和图形结构数据的商业智能。在基准测试中，TigerGraph 在 AWS EC2 部署中承担了 108 TB 的工作负载，据该公司称，该部署在包含 2179 亿个顶点和 1.6 万亿条边的图形上处理 OLAP 样式的查询。 TigerGraph 表示基准测试的 108TB 数据量是“之前世界纪录的 3 倍”。虽然以健康的怀疑态度考虑所有基准测试总是明智的，但这里清楚的是，图技术正在处理越来越大的数据量，并被用于分析和运营工作负载，所有这些都在云端。

## AI, 哦

这个与图数据的交集并不是本月人工智能在通用分析领域展示其实力的唯一地方。例如，Databricks 于 3 月 7 日宣布了一项新的机器学习模型服务功能。该产品专门设计用于在 Databricks Lakehouse 平台上执行的主流分析环境中集成 ML 模型创建、维护和服务。它不仅负责模型部署和批量评分/推理，而且还设置必要的 API 端点，以便轻松进行实时交互式评分，包括流数据场景。 Databricks ML 服务还与 Databricks 平台的一部分技术集成了一段时间：Unity Catalog 和 Feature Store（在推理时自动执行特征查找），以及 MLflow 实验管理。

说到 Databricks，它是 SAP 于 3 月 8 日宣布将在其 Datasphere 服务的背景下与之合作的四家重要公司之一，这是对所谓的 SAP Data Warehouse Cloud 的改进版本。现有的 DWC 客户将自动看到新的 Datasphere 功能，无需迁移。

除了在数据 Lakehouse 方面与 Databricks 合作之外，SAP 还与 DataRobot 合作进行人工智能领域的合作，与 Confluent 合作提供更多的流数据处理功能，以及与 Collibra 合作进行数据治理。这些令人印象深刻的跨行业合作伙伴关系的目标是，用 SAP 自己的话来说，“丰富 SAP Datasphere 并允许组织创建一个统一的数据架构，无论数据存储在何处，都能安全地结合 SAP 和非 SAP 数据。”这种伙伴关系也是双向的。例如，借助 Databricks，客户将能够将 Lakehouse 数据带入 Datasphere，也能够将 SAP 数据（包括来自 ERP 实施、Concur 和 Ariba 的数据）带入 Databricks 环境。这是非常企业化的东西；相应地，SAP 还与多家全球系统集成商合作，包括 Accenture、Deloitte、Capgemini、EY、IBM 和 PWC。

## 云中的数据集成：即用即付，先行合并

虽然“云”一词可能来自 SAP 的产品名称，但云在分析中的中心地位怎么强调都不为过。正如经验丰富的 SAP 在数据治理和管理领域与 Collibra 合作一样，另一个企业数据管理巨头 Informatica 也宣布了自己的新云计划。 2 月 28 日，该公司推出了 Cloud Data Integration (CDI) Free 和 CDI Paygo。 CDI Free 以去年推出的 Data Loader 产品 Informatica 为基础，增加了来自 SAP 经典堆栈的工业级数据集成功能。每月最多可免费使用 2000 万行 ELT（提取、加载和转换）或 10 个 ETL（提取、转换和加载）处理小时，以先到者为准。之后，CDI Paygo（即“随用随付”）允许客户处理更多数据，并在基于使用的定价模型下进行计费。

在过去的几周里，Informatica 并不是唯一一家上新闻的云数据集成公司。在 Informatica 分享新闻的同一天，该领域的另一家公司 Talend 宣布，它正在为云作业管理添加 AI 驱动的自动化，改进数据源连接，以及用于监控数据质量的额外数据可观测性功能。最近，姊妹公司 Qlik 宣布将收购 Talend。由于两家公司均由私募股权公司 Thoma Bravo 所有，因此这笔交易似乎很可能会完成。与此同时，Qlik 已经在其产品组合中拥有重要的数据集成技术，因此我们必须拭目以待，看看 Talend 新宣布的功能将如何发挥作用。

## 云数据和数据市场

紧随其后的是 Rockset，这是一个基于开源 RocksDB 项目的实时分析数据库。 Rockset 可以摄取关系数据和流数据，将其保存在专有存储中，然后使用积极的索引策略来承担数据仓库和数据虚拟化工作负载的组合。 3 月 1 日，该公司宣布了基于多集群架构的新工作负载隔离功能，该功能有助于将流数据摄取与低延迟查询工作负载隔离开来，从而使每个工作负载都可以独立扩展，并且据该公司称，无需多个数据库副本。 Rockset 将自己描述为云原生，将自己添加到供应商名单中，这些供应商越来越多地将云和分析视为永久混合。

当然，出于数据丰富的目的，云中的分析可以从基于云的外部数据馈送中受益匪浅。这就是为什么著名的数据目录提供商 Alation 于 2 月 22 日宣布推出 Alation 数据市场。除了数据治理之外，Alation 对数据目录的看法一直是使数据可发现、可访问，并且在某种意义上，对等- 审查（在企业内）。同样的精神似乎导致了数据市场的引入，这样外部数据就可以像公司数据一样访问。

## 微软 Add-Ins 丰富

使数据更易于访问的另一种方法是使其在核心数据目录和分析界面之外以及在其他应用程序内部可用。这就是 Alation 在 Alation Anywhere 中额外宣布支持 Microsoft Teams 的背后原因，它现在可以在 Microsoft Teams 聊天中发现和查询数据集（加入对 Slack 和 Tableau 的现有支持）。除了以前支持的 Google 表格之外，还有 Alation Connected Sheets，现在可以从 Microsoft Excel 访问目录中的数据。集成紧密且非常有价值——您可以在此处查看 Teams/Alation Anywhere 技术的演示。 Alation 还和我分享了 Google Sheets 上的 Connected Sheets 的演示，确实令人印象深刻。

最后，Teams 和 Excel 并不是唯一获得第三方分析集成的 Microsoft 工具，Alation 也不是唯一这样做的公司。事实证明，Databricks 也参与其中。由于开发人员是 Databricks 的核心支持者，该公司决定将 Microsoft 的 Visual Studio Code 用于其集成，为广受欢迎的多平台（和免费）开发人员工具创建一个插件。从本质上讲，该插件使 VS Code 成为 Databricks 的一流客户端，为开发人员提供了一个超越 Databricks notebook 界面的选项，用于处理他们 lakehouse 中的数据，以及他们已经构建或正在构建的 ML 模型。

## 这是什么意思呢？

开源表格格式越来越受欢迎和采用。在高性能场景中，图数据越来越多地用于分析。机器学习和流数据在主流分析环境中越来越普遍，并且集成得越来越紧密。像 SAP 这样的巨头正在更多环境中共享更多数据。数据集成变得越来越便宜和容易。丰富的数据更容易获得，也更容易与公司数据混合。这一切都发生在云端，每个人都可以使用他们最喜欢的工具进行分析，即使它们是 Slack 或 Teams 等协作平台，Excel 或 Google Sheets 等电子表格，或者 VS Code 等开发人员工具。

分析正变得越来越面向云，越来越普遍，越来越嵌入在平台上，而不是专门或什至主要关注分析。这意味着分析在采用和部署方面正在增长，但随着它深入各种技术平台，它也在“消失”。这似乎是一个悖论，但实际上非常合乎逻辑：最有效的基础架构以不引人注意的方式运行，以至于您甚至都不知道它在那里，让您无需绕行或提前计划即可使用它。这就是当今分析领域正在发生的事情，来自 Alation、Databricks、Dremio、Informatica、Rockset、SAP、Talend 和 TigerGraph 的所有新闻都证实了这一点。