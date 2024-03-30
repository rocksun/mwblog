
<!--
title: 架构师指南：现代数据湖参考架构
cover: https://cdn.thenewstack.io/media/2024/03/0089ca4c-modern-data-lake-architecture.jpg
-->

现代数据湖将数据湖的灵活性与数据仓库的结构相结合，同时为两者提供可扩展性和性能。

> 译自 [The Architect’s Guide: A Modern Data Lake Reference Architecture](https://thenewstack.io/the-architects-guide-a-modern-data-lake-reference-architecture/)，作者 Keith Pijanowski。

旨在最大化其数据资产的企业正在采用可扩展、灵活且统一的数据存储和分析方法。这种趋势是由负责构建与不断变化的业务需求相一致的基础架构的企业架构师推动的。现代数据湖架构通过将数据湖的可扩展性和灵活性与数据仓库的结构和性能优化相结合来满足这一需求。这篇文章提供了一个参考架构，用于理解和实施现代数据湖。

## 什么是现代数据湖？

现代数据湖一半是数据仓库，一半是数据湖，并且对所有内容都使用[对象存储](https://thenewstack.io/the-architects-guide-to-using-ai-ml-with-object-storage/)。这听起来可能像一个营销策略——将两种产品放在一个包中并称之为新产品——但本文中介绍的数据仓库比传统数据仓库更好。它使用对象存储，因此在可扩展性和性能方面提供了对象存储的所有优势。采用这种方法的组织只需为其所需内容付费（由对象存储的可扩展性实现），并通过为其底层对象存储配备通过高端网络连接的 NVMe 驱动器来实现性能。

以这种方式使用对象存储是由于开放表格式 (OTF) 的兴起，例如 Apache Iceberg、Apache Hudi 和 Delta Lake。一旦实施这些规范，就可以无缝地将对象存储用作数据仓库的基本存储解决方案。它们还提供传统数据仓库中可能不存在的功能，包括快照（也称为时间旅行）、模式演进、分区、分区演进和零拷贝分支。

但现代数据湖不仅仅是一个花哨的数据仓库，因为它还包含一个用于非结构化数据的数据湖。OTF 还提供与数据湖中外部数据的集成，这允许在需要时将外部数据用作 SQL 表。或者，可以使用高速处理引擎和熟悉的 SQL 命令转换外部数据并将其路由到数据仓库。

因此，现代数据湖不仅仅是将数据仓库和数据湖打包在一起并使用不同名称。它们共同提供的价值高于传统数据仓库或独立数据湖中的价值。

## 概念架构

分层是一种展示现代数据湖所需的组件和服务的一种便捷方式。分层提供了一种清晰的方式来对提供类似功能的服务进行分组。它还允许建立一个层次结构，消费者在顶部，数据源（及其原始数据）在底部。现代数据湖从上到下的层包括：

- **消费层**：包含高级用户用于分析数据所使用的工具。还包含将以编程方式访问现代数据湖的应用程序和 AI/ML 工作负载。
- **语义层**：用于数据发现和治理的可选元数据层。
- **处理层**：此层包含查询现代数据湖所需的计算集群。它还包含用于分布式模型训练的计算集群。可以使用存储层在数据湖和数据仓库之间进行集成，在处理层中进行复杂转换。
- **存储层**：对象存储是现代数据湖的[主要存储服务](https://thenewstack.io/the-architects-guide-to-using-ai-ml-with-object-storage/)；但是，机器学习操作 (MLOps) 工具可能需要其他存储服务，例如关系数据库。如果您正在追求生成式 AI，您将需要一个向量数据库。
- **摄取层**：包含接收数据所需的服務。高级摄取可以根据计划检索数据。现代数据湖应支持各种协议。它还应支持以流和批次形式到达的数据。可以在摄取层中进行简单和复杂的数据转换。
- **数据源**：数据源层在技术上不是现代数据湖解决方案的一部分，但本文中包含它，因为构建良好的现代数据湖必须支持具有不同数据发送功能的各种数据源。

下图直观地描绘了这些层以及实现这些层可能需要的功能。这是一个端到端架构，其中平台的核心是一个现代数据湖。此图还显示了摄取、转换、发现、管理和使用数据所需的组件。它还描绘了支持依赖于现代数据湖的重要用例所需的工具，例如 MLOps 存储、向量数据库和机器学习集群。

![](https://cdn.thenewstack.io/media/2024/03/d8b4f3fa-modern-data-lake-reference-architecture.png)

*来源：[Modern Data Lake Reference Architecture](https://resources.min.io/c/modern-datalake-reference-architecture?x=P9k0ng&lx=exvNTw&utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)*

存储层和处理层是现代数据湖的核心。这两层还包含用于构建数据基础设施的最快发展的技术：使用开放表格式构建的数据仓库、高速对象存储和向量数据库。

## 存储层

![](https://cdn.thenewstack.io/media/2024/03/2db06eeb-modern-data-lake-object-storage.png)

*来源：[Modern Data Lake Reference Architecture](https://resources.min.io/c/modern-datalake-reference-architecture?x=P9k0ng&lx=exvNTw&utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)*

数据存储层是所有其他层所依赖的基础。其目的是可靠地存储数据并有效地提供数据。它包含用于现代数据湖的数据湖和数据仓库侧的单独对象存储服务。

![](https://cdn.thenewstack.io/media/2024/03/96bbb379-modern-data-lake-storage-bucket.png)

*来源：[Modern Data Lake Reference Architecture](https://resources.min.io/c/modern-datalake-reference-architecture?x=P9k0ng&lx=exvNTw&utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)*

如果需要，可以使用 [存储桶](https://thenewstack.io/how-to-create-an-object-storage-bucket-with-minio-object-storage/) 将这两个对象存储服务合并到对象存储的一个物理实例中，以将数据仓库存储与数据湖存储分开。但是，如果你的使用层和数据管道将在这两个存储服务上放置不同的工作负载，请考虑将它们分开并安装在不同的硬件上。

例如，常见的数据流是让所有新数据都进入数据湖。然后可以将其转换并摄取到数据仓库中，在那里它可以被其他应用程序使用并用于数据科学和数据分析。在此数据流中，现代数据湖会给你的数据仓库带来更多负载，因此你将希望在高端硬件（存储设备、存储集群和网络）上运行它。

外部表功能允许数据仓库和处理引擎将数据湖中的对象读作 SQL 表。如果数据湖用作原始数据的着陆区，那么此功能以及数据仓库的 SQL 功能可用于在将原始数据插入数据仓库之前对其进行转换。或者，外部表可以“按原样”使用，并与数据仓库中的其他表和资源联接，而无需离开数据湖。此模式可以通过将数据保存在一个地方同时使其可供外部服务使用，从而帮助节省迁移成本并克服一些数据安全问题。

你还可以使用此参考架构来追求 AI/ML 策略，但这超出了本文的范围。我们的 [AI/ML 现代数据湖参考架构](https://resources.min.io/c/ai-ml-within-a-modern-datalake?x=P9k0ng&lx=exvNTw) 提供了有关构建 AI 数据基础设施的信息。

## 处理层

处理层包含现代数据湖支持的所有工作负载所需的计算。在较高的层面上，计算有两种类型：数据仓库的处理引擎和分布式机器学习的集群。

![](https://cdn.thenewstack.io/media/2024/03/adce1948-modern-data-lake-processing-layer.png)

*来源：[Modern Data Lake Reference Architecture](https://resources.min.io/c/modern-datalake-reference-architecture?x=P9k0ng&lx=exvNTw&utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)*

数据仓库处理引擎支持针对数据仓库存储中的数据分布式执行 SQL 命令。摄取过程中的转换也可能需要处理层的计算能力。例如，在某些数据仓库中，你可能希望使用奖章架构；在其他数据仓库中，你可能选择使用具有维度表的星形模式。这些设计通常需要在摄取期间对原始数据进行大量的提取、转换和加载 (ETL)。

现代数据湖中的数据仓库将计算与存储分离。因此，如果需要，可以为单个数据仓库数据存储存在多个处理引擎。（这不同于传统的关系数据库，其中计算和存储紧密耦合，并且每个存储设备都有一个计算资源。）

可能的处理层设计是为使用层中的每个实体设置一个处理引擎。例如，为商业智能 (BI) 使用处理集群，为数据分析使用单独的集群，为数据科学使用另一个集群。每个处理引擎都将查询相同的数据仓库存储服务，但是由于每个团队都有自己专用的集群，因此它们不会相互竞争计算。如果 BI 团队正在运行计算密集型月末报告，它们不会干扰运行每日报告的另一个团队。

![](https://cdn.thenewstack.io/media/2024/03/1736a42b-modern-data-lake-processing-storage-layers.png)

*来源：[Modern Data Lake Reference Architecture](https://resources.min.io/c/modern-datalake-reference-architecture?x=P9k0ng&lx=exvNTw&utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)*

机器学习模型，尤其是大型语言模型，如果以分布式方式进行训练，可以更快地进行训练。机器学习集群支持分布式训练。分布式训练应与 MLOps 工具集成，用于实验跟踪和检查点。

## 总结

本文介绍了现代数据湖的高级参考架构，并探讨了其核心组件。目标是为组织提供一个战略蓝图，以便构建一个平台，该平台可以有效地管理其庞大且多样化的数据集并从中提取价值。

现代数据湖结合了基于 OTF 的数据仓库和灵活数据湖的优势，提供了一个统一且可扩展的解决方案，用于存储、处理和分析数据。如果您想更深入地了解这些概念，请通过 [hello@min.io](mailto:hello@min.io) 联系 Min.io 团队。
