
<!--
title: 架构师的AI数据栈互操作性指南
cover: https://cdn.thenewstack.io/media/2024/10/3c499b7d-ai-data-stack-interoperability.jpg
-->

AI 的未来是开放的，互操作性是您在任何技术堆栈中保持领先地位的通行证。

> 译自 [The Architect’s Guide to Interoperability in the AI Data Stack](https://thenewstack.io/the-architects-guide-to-interoperability-in-the-ai-data-stack/)，作者 Brenna Buuck。

随着 [人工智能 (AI)](https://thenewstack.io/ai/) 和机器学习在各行各业的不断扩展，数据架构师面临着一个关键挑战：在日益碎片化和专有的生态系统中确保互操作性。[现代 AI 数据栈](https://thenewstack.io/the-architects-guide-to-the-modern-data-stack/) 必须灵活、成本效益高且面向未来，同时避免令人头疼的供应商锁定，这种锁定会扼杀创新并大幅增加预算。

## 互操作性为何重要

在 AI 驱动的世界中，数据至关重要——而且需要大量数据。您今天在数据存储、处理和分析方面做出的选择将直接影响您明天的敏捷性。为互操作性构建架构意味着选择能够跨环境良好运行的工具，减少对任何单个供应商的依赖，并允许您的组织在任何给定时间选择最佳定价或功能集。

以下是一些互操作性应成为您 [AI 数据栈](https://thenewstack.io/the-architects-guide-to-the-genai-tech-stack-10-tools) 中的关键原则的原因。

### 1. 避免供应商锁定

专有系统最初可能看起来很方便，但它们可能会变成一个昂贵的陷阱。互操作系统允许您自由迁移数据，而不会被锁定在一个生态系统中或支付高昂的退出费用。这种灵活性确保您可以利用不断发展的最佳技术。

### 2. 成本优化

使用互操作系统，您可以自由地货比三家。需要更多计算能力？您不会被绑定到特定提供商的定价模型。您可以根据需要切换到更实惠的选项。互操作性使您能够为 AI 栈的每个组件做出最具成本效益的选择。

### 3. 为您的架构做好未来准备

随着 AI 和机器学习工具的快速发展，互操作性确保您的架构能够适应。无论是采用最新的查询引擎还是集成新的机器学习框架，互操作系统都能使您的组织在今天和未来做好 AI 准备。

### 4. 最大限度地提高工具兼容性

互操作系统旨在跨不同的环境、工具和平台运行，从而实现平滑的数据流并减少对复杂迁移的需求。这加快了实验和创新的速度，因为您不会浪费时间让工具协同工作。

## 互操作 AI 数据栈的关键技术

实现互操作性是关于在软件栈中做出战略性决策。以下是一些促进这种灵活性的基本工具。

### 1. 开放式表格格式

开放式表格格式，如 [Apache Iceberg](https://blog.min.io/a-developers-introduction-to-apache-iceberg-using-minio/)、[Apache Hudi](https://blog.min.io/datalakes-with-hudi-and-hms/) 和 [Delta Lake](https://blog.min.io/delta-lake-minio-multi-cloud/)，支持时间旅行、模式演变和分区等高级数据管理功能。这些格式旨在实现最大兼容性，因此您可以在各种工具中使用它们，包括 Dremio、Apache Spark 或 Presto 等 SQL 引擎。Iceberg 的开放结构确保随着新工具和数据库的出现，您可以将它们整合进来，而无需重新架构整个系统。

### 2. 高性能 S3 兼容对象存储

无论您是在本地、公共云还是边缘运行工作负载，[AWS](https://aws.amazon.com/?utm_content=inline+mention) [S3 兼容对象存储](https://min.io/product/s3-compatibility) 都提供了现代 AI 工作负载所需的灵活性。作为一种 [高性能](https://resources.min.io/c/minio-high-performance-object-storage?x=p9k0ng)、可扩展的选项，可以在任何地方部署，S3 兼容性允许组织避免云供应商锁定，同时确保从任何位置或应用程序 [访问数据](https://thenewstack.io/the-architects-guide-to-storage-for-ai)。

### 3. Apache X-Table：多格式自由

[Apache X-Table](https://xtable.apache.org/) 是一个旨在实现开放式表格格式灵活性的项目。它允许您在 Iceberg、Delta Lake 和 Hudi 等开放式表格格式之间切换。这种自由确保随着表格格式的演变或提供新功能，您的架构仍然可以适应，而无需进行重大重构或迁移工作。

### 4. 查询引擎：无需迁移即可查询

互操作性也扩展到查询引擎。[Clickhouse](https://clickhouse.com/docs/en/integrations/minio)、[Dremio](https://blog.min.io/uncover-data-lake-nessie-dremio-iceberg/) 和 [Trino](https://blog.min.io/minio-trino-kubernetes/) 是很好的例子，它们允许您查询来自多个来源的数据，而无需迁移数据。这些工具允许用户连接到各种来源，从云数据仓库（如 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention)）到传统数据库，如 MySQL、[PostgreSQL](https://roadmap.sh/postgresql-dba) 和 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) SQL Server。借助现代查询引擎，您可以在数据驻留的任何地方运行复杂查询，从而避免代价高昂且耗时的迁移。

### 5. 目录，灵活性和性能

像 Polaris 和 Tabular 这样的数据目录提供高性能功能，并且具有现代数据架构所需的灵活性。这些工具旨在与开放式表格格式一起使用，使用户能够高效地管理和查询大型数据集，而不会受到供应商特定限制的约束。这有助于确保您的 AI 模型可以实时访问它们所需的数据，无论数据存储在何处。

## 互操作性现在

构建互操作性不仅仅是为了避免供应商锁定；它是在构建一个弹性、灵活且经济高效的 AI 数据堆栈。通过选择优先考虑开放标准的工具，您可以确保您的组织能够随着新技术的出现而发展和适应，而不会受到传统决策的限制。无论您是采用高性能的 S3 兼容存储、开放式表格格式还是查询引擎，AI 的未来都是开放的——而互操作性是您保持领先地位的通行证。
