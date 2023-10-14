<!--
# 现代数据技术栈指南
https://cdn.thenewstack.io/media/2023/10/756d37d7-library-stacks-1024x683.jpg

 -->

现代数据技术栈将继续发展变化，但仍然需要大规模性、高性能、数据可访问性、模块化和灵活性。

译自 [The Architect’s Guide to the Modern Data Stack](https://thenewstack.io/the-architects-guide-to-the-modern-data-stack/) 。

尽管对现代数据技术栈的精确定义可能难以捉摸，但有一点是明确的：它并非是传统的、单一的被过去的巨头偏爱的方式。现代数据技术栈是一系列专门化工具的动态组合，每个工具在数据处理的一个具体方面都有出众表现。它是一个模块化的、可变形的生态系统，适应技术的流动性和业务需求的不断变化。

尽管存在这种流动性，或者也许正因为这种流动性，现代数据技术栈确实有一些明确的特点。它是[云原生](https://thenewstack.io/cloud-native/)的、模块化的、高性能的、兼容 RESTful API、实现了计算与[存储](https://thenewstack.io/storage/)的分离，并且是开放的。让我们更详细地看一下这些特点:

- **云原生**:云原生工具提供了无与伦比的扩展性，使组织能够无缝地处理和分析海量的数据集，同时在不同的云环境下保持高性能。无论是公有云还是私有云，现代数据技术栈都是多云兼容的，确保灵活性并避免供应商锁定。
- **模块化**:现代数据技术栈提供了许多专门针对特定数据任务进行优化的工具。这种模块化允许组织搭建定制的数据基础设施，以满足其独特的需求，在快速发展的数据环境中提高敏捷性和适应性。
- **高性能**:性能是现代数据技术栈的核心。其组件都是为了高性能而设计的，使组织能够高效地处理和分析数据。
- **兼容 RESTful API**:采用 RESTful API 标准进行通信，使技术栈中的组件之间能够顺畅地标准化交流，促进互操作性，并将技术栈分解为可管理的组件来创建微服务。这个的一个例子就是 [S3 API](https://min.io/product/s3-compatibility) 在技术栈中的无所不在。
- **计算与存储分离**:[将计算和存储分离](https://blog.min.io/a-developers-introduction-to-apache-iceberg-using-minio/)是现代数据技术栈的基本架构原则。这种分离允许组织独立扩展其计算资源和存储容量，优化成本效益和性能。它还可以实现动态的资源分配，确保计算能力与特定的工作负载相匹配。
- **开放**:现代数据技术栈通过采用开源解决方案和[开放的表格式](https://blog.min.io/a-developers-introduction-to-apache-iceberg-using-minio/)，支持开放性，消除了专有的数据孤岛和供应商锁定。这种对开放性的承诺促进了在广泛的平台和工具间的协作、创新和数据可访问性，增强了技术栈的适应性和包容性。

## 现代数据技术栈的形态

想象现代数据技术栈是一个交响乐团，每个器乐演奏自己的部分，同时遵循指挥家 Kubernetes 的指挥，共同创建和谐的数据体验。虽然演奏者可能更迭，但组成部分保持不变：数据集成、存储、转换、数据可观测性、数据发现、数据可视化、数据分析以及机器学习和人工智能。让我们深入探讨每个领域。

![](https://cdn.thenewstack.io/media/2023/10/209698c4-image1a-e1696949838245.jpg)

### 存储

对象存储在现代数据技术栈中发挥着重要作用。对象存储提供可扩展、高性能和灵活的存储解决方案，以处理日益增长的数据量。对象存储增强了技术栈的敏捷性，因为最优秀的对象存储可以部署在不同的基础设施上，这凸显了软件定义存储的重要性。

存储日益在技术栈的其他组件之间进行无缝集成，并作为[数据湖架构](https://min.io/solutions/modern-data-lakes-lakehouses)的支柱发挥积极作用。像使用 MinIO 和 [Iceberg](https://blog.min.io/lakehouse-architecture-iceberg-minio/)、[Hudi](https://blog.min.io/streaming-data-lakes-hudi-minio/) 以及 [Delta Lake](https://blog.min.io/delta-lake-minio-multi-cloud/) 搭建的数据湖，完美契合这种使用场景。

### 数据集成

摄取是连接不同数据源的桥梁。现代[数据集成](https://min.io/product/integrations)工具内化灵活性和开放性理念。它们不会在专有数据存储里囤积数据，而是促进数据可访问性，不管数据所在位置。无论公有云、私有云、裸机基础设施还是边缘节点，数据集成工具消除过去将数据隔离的障碍。

这一领域一个值得关注的参与者是 [Apache NiFi](https://nifi.apache.org/)，这是一个开源的数据集成工具，可以轻松编排数据流。它与对象存储兼容，确保数据可以在不同环境间无缝流动。[Airflow](https://blog.min.io/apache-airflow-minio/) 是这个领域另一个明显选手。Airflow 是一个开源平台，用于编排、调度和监控复杂的数据工作流，使管理和自动化数据相关任务更简单。

过去涉及实际数据移动的集成模式在很大程度上被就地集成的概念取代。这一范式转变不仅改变了我们管理数据的方式，还代表我们对数据自由、可访问性和敏捷性方法的根本转变。现代数据技术栈中的数据属于您，而不属于专有系统。获得利益的必须是您和组织，而不是销售过时关系数据库的跨国公司。

### 转换

虽然转换和数据集成应用有些重叠，但重要的是注意像 [Apache Spark](https://blog.min.io/spark-minio-kubernetes/) 和 [DBT](https://www.getdbt.com/) 这样高度专业化的转换工具的存在。这些工具服务于不同目的，允许[数据工程师和分析师](https://roadmap.sh/ai-data-scientist)在下游应用使用前修改和优化数据。以对象存储作为数据的源和目标，这些工具确保转换过程中数据保持[一致](https://blog.min.io/the-new-metrics-of-object-storage/)、可访问和可靠。

### 数据可观测性

确保数据可靠性和质量在现代数据技术栈中至关重要。数据可观测性工具充当警惕的守护者，提供数据管道运行状况和行为的见解。这些工具不仅可以监控，还可以检测异常，帮助维护数据完整性。

[Prometheus](https://blog.min.io/opentelemetry-flask-prometheus-metrics/) 是一种流行的可观测性工具，它让您能深入了解数据基础设施，为现代数据技术栈的标准 [S3 兼容性](https://min.io/docs/minio/linux/operations/monitoring/collect-minio-metrics-using-prometheus.html)提供必要的可观测性。虽然 [Grafana](https://min.io/docs/minio/container/operations/monitoring/grafana.html) 通常与基础设施和应用监控相关，但也可以扩展以监控数据管道。

### 数据发现

像 Apache Atlas 和 [Collibra](https://cdn.collibra.com/Community/Documentation/2022.09/Collibra-DIC-Edge-Guide-2022.09.pdf) 这样的工具提供在整个组织发现和编录数据资产的手段。与对象存储仓库集成确保所有数据(无论位置)都可以被发现和使用。

### 数据可视化

数据可视化工具将原始数据转化为有意义的、可操作的洞察。它们让用户可以制作吸引人的故事、发现模式并做出基于数据的决策。这些工具依赖可访问性，确保每个人都可以使用数据，不仅仅是[数据科学家或分析师](https://roadmap.sh/ai-data-scientist)。这里我们再次看到 RESTful API 广泛用于连接技术栈中的数据。

Tableau、Power BI、Looker 和 [Apache SuperSet](https://blog.min.io/how-to-druid-superset-minio/) 等工具在这一类别中领先，提供对任何位置数据的洞察。

### 数据分析

对象存储是在线分析处理 (OLAP) 分析数据库的[主要存储](https://blog.min.io/databases-for-object-storage/)。这种前瞻性方法被分析巨头如 [Snowflake](https://min.io/solutions/snowflake)、[SQL Server](https://min.io/solutions/sqlserver) 和 [Teradata](https://min.io/resources/docs/Teradata-solution-brief.pdf) 采用，它依赖可查询表的概念，消除数据迁移需求，允许这些高性能数据库将精力集中在查询性能而不是存储上。这种趋势遵循下一步逻辑，即更小、更轻量级的分析引擎，如完全摒弃存储仅依赖内存处理以进一步加速数据分析工作负载的 [DuckDB](https://blog.min.io/duckdb-and-minio-for-a-modern-data-stack/)。

追求对象存储规模性、性能和成本效益优势的云原生分析平台正在彻底改变企业从数据中提取价值的方式。这不仅是技术变革，对于希望在当今数据驱动世界保持竞争力的组织来说，是战略需求。

### 机器学习和 AI

现在，[机器学习(ML)和 AI](https://thenewstack.io/ai/) 在现代数据技术栈中比以往任何时候都更加重要，驱动颠覆性洞察和决策能力。像 [TensorFlow](https://blog.min.io/hyper-scale-machine-learning-with-minio-and-tensorflow/) 和 PyTorch 这样的 ML 框架占据中心舞台，展示它们与高性能对象存储集成时的扩展能力。这种强大协同不仅可以加速 ML 模型的训练和推理阶段，还可以增强 AI 驱动应用的敏捷性，允许组织利用数据潜力进行[异常检测](https://blog.min.io/anomaly-detection-from-log-files-the-performance-at-scale-use-case/)、自然语言处理、[计算机视觉](https://blog.min.io/object-detection-minio-yolo/)等。在这个数据驱动创新时代，MI 和 AI 已成为必不可少的支柱，重塑行业，为那些愿意开拓由强大对象存储提供支持的智能自动化和数据驱动决策新前沿的企业开启新的可能性。

## 总结

这些现代数据技术栈的竞争者并非企业架构师的最终选择。我们遗漏了很多，也有很多尚未探索，但读者应该注意其中的类别。现代数据技术栈将继续发展，采用新的工具和技术。但是，其对规模、性能、数据可访问性、模块化和灵活性的需求将保持不变。

在 MinIO，我们将这些原则视为工程优先的原则。事实上，我们认为自己更像是数据公司，而不是存储公司。我们致力于成为整个数据乐团的一部分，支持大规模组件以及即兴创作。

保持探索、保持创新，开发数据的无限潜力。现代数据技术栈是您的交响曲，而您是作曲家。如果您对现代数据技术栈的内容有任何疑问或想法，欢迎通过 [Slack](https://minio.slack.com/ssb/redirect) 或发送电子邮件至 hello@min.io 与我们联系。