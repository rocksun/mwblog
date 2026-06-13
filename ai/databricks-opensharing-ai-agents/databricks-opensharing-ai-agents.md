<!--
title: Databricks希望通过OpenSharing解决AI智能体技能的“邮件共享”难题
cover: https://cdn.thenewstack.io/media/2026/06/474bf001-masantocreative-dxi3fpqbkuy-unsplash-scaled.jpg
summary: Databricks发布了OpenSharing协议，作为Delta Sharing的升级版，它支持跨组织安全共享AI模型、智能体技能及非结构化数据。该协议现已成为Linux Foundation的独立项目，旨在打破供应商锁定，解决AI资产共享中低效的邮件传输问题，并支持Apache Iceberg及多种本地存储厂商。
-->

Databricks发布了OpenSharing协议，作为Delta Sharing的升级版，它支持跨组织安全共享AI模型、智能体技能及非结构化数据。该协议现已成为Linux Foundation的独立项目，旨在打破供应商锁定，解决AI资产共享中低效的邮件传输问题，并支持Apache Iceberg及多种本地存储厂商。

> 译自：[Databricks wants to kill the "email me a file" problem for AI agent skills](https://thenewstack.io/databricks-opensharing-ai-agents/)
> 
> 作者：Frederic Lardinois

[Databricks](https://www.databricks.com/) 于周三发布了 OpenSharing，这是其开源 [Delta Sharing](https://github.com/delta-io/delta-sharing) 协议的继任者。

这一升级版协议增加了对 [Apache Iceberg](https://iceberg.apache.org/) REST Catalog 客户端的支持，并将本地存储供应商纳入生态系统，首批合作伙伴包括 [Everpure](https://www.everpuredata.com/)（原 Pure Storage）、[MinIO](https://www.min.io/) 和 [Qumulo](https://qumulo.com/)。

此外，OpenSharing 现在是一个独立的 [Linux Foundation](https://www.linuxfoundation.org/) 项目，并将 Delta Sharing 的零拷贝共享能力从表格扩展到了智能体技能、AI 模型和非结构化数据。

目前，智能体堆栈的大多数层级已达成共识：

OpenSharing 通过提供一种帮助组织安全共享数据和 AI 资产的协议，在此堆栈基础上进行了构建。

## 从 Delta Sharing 到 OpenSharing

Databricks 在 [2021 年推出了 Delta Sharing](https://www.databricks.com/company/newsroom/press-releases/databricks-unveils-delta-sharing-the-worlds-first-open-protocol-for-real-time-secure-data-sharing-and-collaboration-between-organizations)，作为 Databricks 开源表格式 [Delta Lake](https://delta.io/) 的子项目。当时，它被标榜为第一个用于跨组织安全数据共享的开放协议。该公司表示，自那时起，它已成为应用最广泛的开放数据共享协议，拥有数千家客户和合作伙伴，包括 Amadeus、Atlassian、LSEG、SAP、Stripe 和 The Trade Desk。

正如 Databricks 联合创始人兼 CTO Matei Zaharia 在今天的公告中所言：“Delta Sharing 证明了业界会选择开放而非供应商锁定。”

值得注意的是，对于现有的 Delta Sharing 用户，一切都不会改变。当前的 Delta Sharing 部署将继续运行。OpenSharing 在不引入破坏性变更的情况下，增加了新的资产类型、接收者和来源。

## 不要再通过邮件发送智能体技能

[Akram Chetibi](https://www.linkedin.com/in/akram-chetibi-752763b/) 是 Databricks 负责生态系统和合作伙伴集成的产品团队负责人。他在接受 *The New Stack* 独家采访时表示，智能体技能是目前需求量最大的新资产类型，其次是 AI 模型。

在 2023 年底加入 Databricks 之前，Chetibi 曾是 [AWS Data Exchange](https://aws.amazon.com/data-exchange/) 的创始产品经理，并帮助启动了 [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 业务。

“目前还没有一种简单的方法来共享智能体技能，”Chetibi 说道。“如果我今天让你跟我共享一个智能体技能，你会怎么做？……你会给我发一封包含文件的电子邮件。但如果我想要更新，我该如何获取？你得再给我发一封包含新文件的邮件。”

Databricks 将 OpenSharing 称为第一个用于安全共享 AI 资产的、供应商中立的开放协议。目前的替代方案要么是定制化集成，要么是单厂商市场，例如 Salesforce 的 [AgentExchange](https://www.salesforce.com/agentforce/agentexchange/)，或是 AWS 和 Microsoft 市场内的智能体商店。

有了 OpenSharing，提供商只需发布一次技能或模型，任何合作伙伴都可以通过标准的 API 进行发现、授权和访问，并实现源端的零拷贝访问。

值得注意的是，该协议并不会规定技能或模型必须是什么样子。

## 协议的工作原理

Chetibi 表示，无论资产类型如何，外部协作的需求始终如一。“他们需要一种能够跨云、跨区域、跨平台工作的方案，并且他们需要通常所说的零拷贝或实时共享，”他说。

通用对象模型沿用了 Delta Sharing 的设计。提供商将资产打包成一个“共享（share）”。该共享包含模式（schema），而现在的模式可以容纳表格、AI 模型或智能体技能。

底层的机制因资产类型而异。结构化数据采用 Parquet 格式，可以通过用于单个分区的签名 URL 进行共享，并通过兼容 Delta 或 Iceberg 的 API 暴露，并具备变更数据馈送（change data feed）等功能。非结构化数据和 AI 资产的工作方式是通过以云中立的方式为底层存储提供云令牌（cloud tokens）。

该协议涵盖了跨管理边界的外部只读共享；内部治理不在本次公告范围内，不过 Chetibi 表示在该领域“敬请期待”。

## 另一个 API：Iceberg

OpenSharing 现在也支持 Apache Iceberg API。Iceberg 已成为共享分析表格的事实标准，与 Parquet 互补。但 Chetibi 认为，“格式的重要性正变得越来越低——归根结底，它们都像带有某些元数据的 Parquet。”

Delta Sharing 已经拥有适用于 Apache Spark、Power BI、Excel 和 Python 的连接器，甚至 Snowflake 也将其作为接收端提供支持。通过增加 Iceberg API，任何支持该 API 的工具都成为了提供商可以触达的另一个目的地。

Databricks 在这一方向上已经推进了一段时间。它在 2024 年以[据报道 20 亿美元的价格](https://techcrunch.com/2024/08/14/databricks-reportedly-paid-2-billion-in-tabular-acquisition/)收购了由 Apache Iceberg 创建者成立的 Tabular，并在 Iceberg v4 规范中推动 [Delta 与 Iceberg 之间的元数据融合](https://www.snowflake.com/en/blog/engineering/iceberg-summit-2026-recap-v4-spec/)。

与此同时，Snowflake [将其共享扩展到了](https://www.snowflake.com/en/blog/data-sharing-open-table-formats/)跨云和跨区域的 Iceberg 和 Delta 表，并声称其共享生态系统的规模是竞争对手的 2.5 倍。两家公司现在都将各自的共享策略描述为“开放”。但 Databricks 提供的是一种其他人可以实现的协议，而 Snowflake 的共享则运行在其自己的平台上。

## 将协议引入本地环境（On-prem）

Everpure（前身为 Pure Storage，于二月[重塑品牌](https://www.sdxcentral.com/news/pure-storage-relaunches-as-everpure-pivoting-to-ai-focused-data-management/)）、MinIO 和 Qumulo 在发布时提供了托管的 OpenSharing 服务，Cohesity、Commvault、Hewlett Packard Enterprise、NetApp、Nutanix、Rubrik 和 VAST Data 也计划跟进。

存储供应商自行运行 OpenSharing 服务器，因此客户无需自行搭建。

> “这是一个真正开放的协议，它得到了许多非 Databricks 平台的广泛使用和支持。”

“一旦这些合作伙伴在本地托管服务器，你就可以使用与连接任何其他云或平台相同的协议轻松地连接到它，”Chetibi 说。

Chetibi 表示，首先需要完成两件事：协议需要支持非结构化数据和 AI 资产，因为本地资产不仅仅是表格；此外，Databricks 希望由存储提供商而不是客户来操作服务器。

## 开放治理

继 Delta Lake 和 Unity Catalog 之后，OpenSharing 也成为了 Databricks 在 Linux Foundation 旗下的项目。Databricks 在 [2024 年 6 月将上述项目捐赠给了 LF AI & Data](https://lfaidata.foundation/blog/2024/06/20/welcoming-unity-catalog-to-the-lf-ai-data-foundation-a-milestone-in-open-data-and-ai-governance/)。

“我们不希望它仅仅是 Databricks 的东西——这是一个真正开放的协议，它得到了许多非 Databricks 平台的广泛使用和支持，”Chetibi 说道。