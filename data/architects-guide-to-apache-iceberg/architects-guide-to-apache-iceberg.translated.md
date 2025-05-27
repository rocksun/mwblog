# Apache Iceberg 架构师指南

![Featued image for: Architect’s Guide to Apache Iceberg](https://cdn.thenewstack.io/media/2025/05/01095a00-iceberg-1024x576.jpg)

[Apache Iceberg](https://iceberg.apache.org/) 1.9.0 版本于 4 月 28 日发布，它带来了一系列更新，不仅仅是扩展了其功能集。它们预示着更大的变化：[Delta Lake](https://blog.min.io/delta-lake-minio-multi-cloud/?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog) 和 [Iceberg](https://blog.min.io/the-definitive-guide-to-lakehouse-architecture-with-iceberg-and-aistor/?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog) 之间的差距正在缩小。曾经是 Delta Lake 独有的功能，如具有沿袭的行级操作、快速半结构化数据处理，现在在 Iceberg 中也可用了。[Iceberg](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/) 现在支持更容易地从 Delta Lake 迁移，这清楚地表明它们不再是竞争对手，而是一个继承战利品的胜利者。

让我们来探讨一下 Iceberg 1.9.0 中的新功能，它如何反映 Delta Lake 的历史优势，以及这种融合对 Lake house 的未来意味着什么。

## Iceberg 和 Delta 之间的原始差异

最初，Iceberg 和 Delta Lake 做了[不同的架构选择](https://thenewstack.io/architects-guide-to-a-reference-architecture-for-an-ai-ml-data-lake/)。

Delta Lake 早期优先考虑性能，围绕 Parquet 和 Spark 进行了紧密优化，并采用了事务日志模型。另一方面，Iceberg 专注于长期数据组织——例如构建与格式无关的表规范、引入基于快照的版本控制以及定义分层元数据层次结构。Delta 使用平面事务日志；Iceberg 使用清单树。Delta 需要 Parquet；Iceberg 支持多种格式，如 Avro、Orc，当然还有 Parquet。这些区别赋予了每个项目独特的优势。

然而，随着 Iceberg 1.9.0 的发布，情况发生了变化。[Iceberg 正在缩小性能差距](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/)，同时保持架构清晰性。Delta 正在添加兼容性层。曾经的差异化因素现在变成了共享能力。

## Iceberg 1.9.0：新功能

### 增强的行级操作

Iceberg 1.9.0 允许等值删除和行沿袭跟踪共存。这一进步使得能够基于指定条件精确删除行，并为插入或更新的行分配唯一的行 ID，从而促进准确的数据版本控制和审计。

Delta Lake 长期以来一直支持这种行级变更和沿袭跟踪。Iceberg 现在也具备了这种能力，缩小了两者之间的功能差距。

### Delta Lake 到 Iceberg 的迁移

Iceberg 提供了一种通过 `iceberg-delta-lake` 模块从 Delta Lake 迁移的结构化方法。该模块提供了 `snapshotDeltaLakeTable` 操作，允许创建引用现有 Delta Lake 表的数据文件的 Iceberg 表，而无需数据重复。它还支持在迁移期间维护事务历史记录，从而确保数据操作的连续性。

结果是一种更直接、更高效的从 Delta 迁移到 Iceberg 的方式，并且清楚地表明 Iceberg 正在成为主要的开放表格式。

### Variant 数据类型支持

Iceberg 1.9.0 引入了一个 `variant` 逻辑类型，用于以二进制格式存储半结构化数据（如 JSON）。这避免了解析和将 JSON 存储为字符串的性能开销。

这个想法直接来自 Delta Lake，后者引入了相同的功能，以将查询性能提高到[基准测试场景中的八倍](https://www.databricks.com/blog/introducing-open-variant-data-type-delta-lake-and-apache-spark)。Iceberg 采用此功能使其成为具有半结构化数据（如涉及日志和事件）的低延迟工作负载的可行选择。

### 原生地理空间支持

Iceberg 1.9.0 添加了一个新的 `geometry` 逻辑类型，从而可以高效地存储和查询空间数据集。主要功能包括：

- 支持 Well-Known Binary (WKB) 编码。
- 默认坐标参考系 (CRS) 设置为 OGC:CRS84。
- 对 XY、XYZ、XYM 和 XYZM 坐标格式的多维支持。
- 可选的空间统计信息，如边界框，以提高查询性能和空间索引。

此地理空间模型与 GeoParquet 规范保持一致，从而确保与开放数据标准的兼容性。这是 Iceberg（以及数据社区）围绕通用标准发展的一个例子。

### REST Catalog：更适合企业

REST catalog 身份验证的改进包括：

- 支持可插拔的身份验证处理程序。
- 更清晰的身份验证和请求逻辑分离。
- 扩展了对企业身份系统的测试。

这是生产级部署的基础性更新，这些部署使用 Iceberg REST 目录进行多引擎或多租户环境，这是企业数据湖仓部署中非常[常见的用例](https://blog.min.io/the_way_of_the_cloud/?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog)。

### 弃用旧版本：Hadoop 2 和 Spark 3.3 已删除

已删除对 Hadoop 2 和 Spark 3.3 的支持。这不仅仅是清理工作：这是一个信号。如果您仍然受限于旧的 Hadoop 基础设施，那么现在是规划您的[退出](https://min.io/solutions/hdfs-migration?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog)的时候了。Iceberg 正在朝着现代运行时、云原生存储和横向扩展计算的方向发展。

### 其他值得关注的点

**分区统计信息 API：** 公开分区级别的元数据，以实现更好的规划和修剪。

**纳秒时间戳支持：** 扩展了 Parquet 后端的精度。

**InternalData API：** 改进了 Spark、Flink 和 Trino 等引擎的集成路径。

您可以在[此处](https://github.com/apache/iceberg/releases/tag/apache-iceberg-1.9.0)找到完整的发行说明。

## 融合对每个人都有好处

长期以来，Delta Lake 一直是 Databricks 用户的默认选择。但自从 [Databricks 收购了 Tabular](https://blog.min.io/modern-data-architectures-with-iceberg-and-tabular/?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog)（由 Iceberg 的创建者创立的目录公司）以来，开放表格式的未来看起来更加统一。

Iceberg 正在获得使 Delta Lake 受欢迎的性能和可用性功能，同时忠于其[架构清晰性](https://thenewstack.io/the-architects-guide-a-modern-data-lake-reference-architecture/)：独立的目录支持、规范驱动的演进和开放性。Delta Lake 正在开始公开 REST 接口和兼容性层，例如 [UniForm](https://docs.databricks.com/aws/en/delta/uniform)。

这就是融合。这对每个在湖仓之上构建的人都有好处。围绕标准进行组织降低了团队采用或迁移湖仓的认知和运营开销。这意味着数据工程师、架构师、分析师和 AI 工程师不必重新学习工具、平台或功能。当事情按照您期望的方式工作时，一切都会变得更容易。

## 为什么存储很重要

如果存储跟不上，其他一切都无关紧要。

Iceberg 依赖于快速扫描、快速元数据操作和高吞吐量。

现代对象存储专为此而设计。它运行在商用硬件上，并部署到私有云、数据中心、托管设施或边缘位置，同时以最少的硬件提供最佳性能。私有云 Iceberg 部署的经济性是无与伦比的：没有出口费用或 GET 和 PUT 的成本意味着您可以根据需要尽可能快地扩展，而无需担心高昂的云账单。更不用说最安全的部署仍然是那些在气隙部署中的部署。

存储不是堆栈中令人兴奋的部分，但如果它太慢、太昂贵或不够安全，其他一切都会崩溃。

## 前进的道路

Delta Lake 和 Iceberg 的融合不是关于一个战胜另一个。而是关于生态系统的成熟。随着两个项目都在不断发展以采纳彼此的优势，真正的赢家是用户。团队现在可以根据架构契合度和运营目标选择工具，而不仅仅是功能清单或供应商对齐。

这种转变推动行业朝着更大的互操作性、更开放的标准和更简单的决策发展。它降低了转换成本，鼓励了最佳实践，并使团队能够专注于构建可靠、高性能的数据系统，而不是在格式孤岛中导航。

这就是进步。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)