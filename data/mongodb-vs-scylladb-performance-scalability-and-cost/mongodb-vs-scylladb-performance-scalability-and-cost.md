<!--
title: MongoDB vs ScyllaDB: 性能、扩展性和成本对比
cover: https://cdn.thenewstack.io/media/2024/01/89978df9-wrestling-1024x789.jpg
-->

我们对这两种数据库进行了深入的基准测试研究，应用了超过133项测量指标进行全面比较。以下是测试结果。

> 译自 [MongoDB vs. ScyllaDB: Performance, Scalability and Cost](https://thenewstack.io/mongodb-vs-scylladb-performance-scalability-and-cost/)，作者 Daniel Seybold。

我们之前比较了两个重要的 NoSQL 数据库的[技术特点](https://thenewstack.io/mongodb-vs-scylladb-a-comparison-of-database-architectures/): 市场领先的通用 NoSQL 数据库 MongoDB，以及以性能为导向的竞争者 ScyllaDB。MongoDB 和 ScyllaDB 都承诺提供高可用性、高性能和可扩展的架构。但它们实现这些目标的方式与您起初可能想象的差异要大得多。

为了量化这些架构差异的性能影响，我们进行了深入的基准测试研究，应用了 133 多项性能测量结果来测试性能和可扩展性。本文分享了高级结果。

总结:ScyllaDB 最适合操作 TB 级数据集并需要高吞吐量(超过 50 kOps)的应用，同时为读写操作提供可预测的低延迟。

## 关于此基准测试

NoSQL 数据库格局不断发展。在过去 15 年中，在选择高性能和可扩展的 NoSQL 数据库时，它已经引入了许多选择和权衡。我们最近对 MongoDB 和 ScyllaDB 进行了基准测试，以获得它们在不同工作负载下的性能、性价比和可扩展性能力的详细情况。

为了创建工作负载，我们使用了 Yahoo! 云服务基准 [YCSB](https://github.com/brianfrankcooper/YCSB)，这是一个开源和行业标准的基准测试工具。数据库基准测试通常被认为不透明，并且是将苹果与梨进行比较。为了解决这些挑战，此基准比较基于 [benchANT](https://benchant.com/) 科学验证的基准测试即服务平台。该平台确保了可重现的基准测试过程(更多详情，请参阅关于 [Mowgli](https://dl.acm.org/doi/pdf/10.1145/3297663.3310303) 和 [benchANT](https://dl.acm.org/doi/abs/10.1145/3491086.3492473) 的相关研究论文)，该过程遵循了[数据库基准测试](https://dl.acm.org/doi/pdf/10.1145/3209950.3209955)的建立指南。

此基准测试项目由 [benchANT](https://benchant.com/) 进行，并由 ScyllaDB 赞助，以提供两种数据库技术的公平、透明和可重现的比较。为此，所有基准测试均在数据库供应商的 DBaaS 产品上进行，即 MongoDB Atlas 和 ScyllaDB Cloud，以确保可比较的准备生产的数据库部署。此外，所应用的基准测试工具是标准的 YCSB 基准测试，所有应用的配置选项都公开了。

DBaaS 集群范围从 3 到 18 个节点，这些节点按照三个可比较定价的扩展规模进行分类。基准测试研究包括三种工作负载类型，涵盖了从 250GB 到 10TB 的数据集大小的读密集、读更新和写密集应用程序域。我们总共比较了 133 项性能指标，范围从吞吐量(每成本)到延迟再到可扩展性。ScyllaDB 在 133 项测量中有 132 项超过了 MongoDB:

- 对于所有应用的工作负载，与 MongoDB 相比，ScyllaDB 提供了更高的吞吐量(高达 20 倍)。
- ScyllaDB 为几乎所有场景的插入、读取和写入操作实现了低于 10 毫秒的 P99 延迟。相比之下，MongoDB 只为某些读取操作实现了低于 10 毫秒的 P99 延迟，而 MongoDB 的插入和更新延迟比 ScyllaDB 高出 68 倍。
- ScyllaDB 实现了接近线性的可扩展性，而 MongoDB 显示出效率较低的水平可扩展性。
- 价格性能比明确显示了 ScyllaDB 的巨大优势，根据工作负载和数据集大小，其价格性能比可高出 19 倍。

为了确保结果的完全透明性和可重现性，所有基准测试结果都公开在 [GitHub](https://github.com/benchANT/mongodb-vs-scylladb) 上。这些数据包含原始性能测量以及诸如 DBaaS 实例详细信息和用于运行 YCSB 实例的 VM 详细信息等附加元数据。即使没有 benchANT 平台，您也可以自行重现结果。

## MongoDB 与 ScyllaDB 基准测试结果概述

完整的基准测试涵盖了三种工作负载: 社交、缓存和传感器。

- **社交**工作负载基于 YCSB 工作负载 B。它创建了一个读密集型工作负载，95% 的读取操作和 5% 的更新操作。我们使用该工作负载的两种形式，它们在请求分布模式方面有所不同，即均匀分布和热点分布。这些工作负载针对小型数据库扩展大小(数据集为 500GB)和中型扩展大小(数据集为 1TB)执行。
- **缓存**工作负载基于 YCSB 工作负载 A。它创建了一个读更新工作负载，50% 的读取操作和 50% 的更新操作。该工作负载以两种版本执行，它们在请求分布模式方面有所不同，即均匀分布和热点分布。该工作负载针对小型数据库扩展大小(数据集为 500GB)、中型扩展大小(数据集为 1TB)和大型扩展大小(数据集为 10TB)执行。
- **传感器**工作负载基于 YCSB 及其默认数据模型，但操作分布为 90% 的插入操作和 10% 的读取操作，模拟真实的物联网(IoT)应用程序。该工作负载使用最新的请求分布模式执行。该工作负载针对小型数据库扩展规模(数据集为 250GB)和中型扩展规模(数据集为 500GB)执行。

以下摘要部分总结了 MongoDB 和 ScyllaDB 在不同工作负载和数据库集群大小方面的关键比较结果。详细的所有工作负载和配置结果描述在[扩展的基准测试报告](https://benchant.com/blog/mongodb-vs-scylladb-benchmark)中提供。

### 性能比较摘要: MongoDB vs ScyllaDB

对于**社交工作负载**，ScyllaDB 的吞吐量更高，延迟更低，优于 MongoDB 在社交工作负载的所有测量配置。

![放大](https://cdn.thenewstack.io/media/2024/01/bbbcbfde-image1a.png)

- ScyllaDB 提供了高达 12 倍的吞吐量。
- 与 MongoDB 相比，ScyllaDB 的更新延迟明显更低(低至 47 倍)。
- ScyllaDB 的读取延迟也较低，低至 5 倍。

对于**缓存工作负载**，ScyllaDB 的吞吐量更高，延迟更低，优于 MongoDB 在缓存工作负载的所有测量配置。

![放大](https://cdn.thenewstack.io/media/2024/01/5cc7cc9c-image2a.png)

- 即使是一个小的三节点 ScyllaDB 集群也优于一个大的 18 节点 MongoDB 集群。
- 随着数据大小的增长，ScyllaDB 提供了持续增长的吞吐量，最高可达 20 倍。
- 与 MongoDB 相比，ScyllaDB 的更新延迟明显更好(低至 68 倍)。
- 对于所有扩展大小和请求分布，ScyllaDB 的读取延迟也较低，低至 2.8 倍。

对于**传感器工作负载**，ScyllaDB 的吞吐量更高，延迟更低，优于 MongoDB 在传感器工作负载的结果，除了在小规模扩展下的读取延迟。

![放大](https://cdn.thenewstack.io/media/2024/01/8892478c-image3a.png)

- 随着数据大小的增长，ScyllaDB 提供了持续增长的吞吐量，最高可达 19 倍。
- 与 MongoDB 相比，ScyllaDB 提供了更低的(低至 20 倍)更新延迟结果。
- MongoDB 在小规模扩展下提供更低的读取延迟，但 ScyllaDB 在中型规模扩展下提供更低的读取延迟。

### 可扩展性比较摘要: MongoDB vs ScyllaDB

对于**社交工作负载**，ScyllaDB 实现了近线性的可扩展性，吞吐量可扩展性为理论上可能的 400% 的 386%。MongoDB 实现了均匀分布 420%(理论上可能的 600%)和热点分布 342%(理论上可能的 600%)的扩展因子。

![放大](https://cdn.thenewstack.io/media/2024/01/fd9f99f4-image4a.png)

![放大](https://cdn.thenewstack.io/media/2024/01/7a97f424-image5a.png)

对于**缓存工作负载**，ScyllaDB 在所有测试中实现了近线性可扩展性。MongoDB 实现了理论上可能的 600% 的 340%，和理论上可能的 2400% 的 900%。

![放大](https://cdn.thenewstack.io/media/2024/01/2650855d-image6a.png)

![放大](https://cdn.thenewstack.io/media/2024/01/2803d44f-image7a.png)

对于**传感器工作负载**，ScyllaDB 实现了近线性可扩展性，吞吐量可扩展性为理论上可能的 400% 的 393%。MongoDB 实现了理论上可能的 600% 的 262% 的吞吐量可扩展性因子。

![放大](https://cdn.thenewstack.io/media/2024/01/d7506e5a-image8a.png)

![](https://cdn.thenewstack.io/media/2024/01/9643079c-image9a.png)

### 价格性能结果摘要: MongoDB vs ScyllaDB

对于**社交工作负载**，与 MongoDB Atlas 相比，ScyllaDB 为小规模扩展提供了 5 倍的操作/美元，为中型规模扩展提供了 5.7 倍的操作/美元。 对于热点分布，ScyllaDB 为小规模扩展提供了 9 倍的操作/美元，为中型规模扩展提供了 12.7 倍的操作/美元。

![放大](https://cdn.thenewstack.io/media/2024/01/32935d2e-image10.png)

对于**缓存工作负载**，与 MongoDB Atlas 相比，ScyllaDB 为小规模扩展提供了 12 至 16 倍的操作/美元，为中大规模扩展提供了 18-20 倍的操作/美元。

![放大](https://cdn.thenewstack.io/media/2024/01/d0ede298-image11a.png)

对于**传感器工作负载**，与 MongoDB Atlas 相比，ScyllaDB 提供了 6 至 11 倍的操作/美元。在缓存和传感器工作负载中，MongoDB 能够随着实例/集群大小的增长扩展吞吐量，但保留的操作/美元正在减少。

![放大](https://cdn.thenewstack.io/media/2024/01/590fd049-image12a.png)

## 技术要点: 缓存工作负载，12 小时运行

除了默认的 30 分钟基准测试运行外，我们还为統一分布的大规模扩展选择了长时间 12 小时运行基准测试。

对于 MongoDB，我们选择了确定的 8 个 YCSB 实例，每个 YCSB 实例有 100 个线程，并以均匀分布运行缓存工作负载 12 个小时，目标吞吐量为每秒 40 kOps。

吞吐量结果显示，MongoDB 按预期持续提供 40 kOps/s。

![放大](https://cdn.thenewstack.io/media/2024/01/83de2232-image13a.png)

12 小时内的 P99 读取延迟显示了延迟峰值达到 20 毫秒和 30 毫秒，并且在运行 4 小时后出现尖峰增加。平均而言，12 小时运行的 P99 读取延迟为 8.7 毫秒;对于常规的 30 分钟运行，它是 5.7 毫秒。

12 小时内的 P99 更新延迟在整个 12 小时内呈现尖峰模式，峰值延迟为 400 毫秒。平均而言，12 小时运行的 P99 更新延迟为 163.8 毫秒，而对于常规的 30 分钟运行，它是 35.7 毫秒。

![放大](https://cdn.thenewstack.io/media/2024/01/0ab6d699-image14.png)

![放大](https://cdn.thenewstack.io/media/2024/01/5603f1dc-image15.png)

对于 ScyllaDB，我们选择了确定的 16 个 YCSB 实例，每个 YCSB 实例有 200 个线程，并以均匀分布运行缓存工作负载 12 小时，目标吞吐量为每秒 500 kOps。

吞吐量结果显示，ScyllaDB 按预期持续提供 500 kOps/s。

![放大](https://cdn.thenewstack.io/media/2024/01/55eef29c-image16a.png)

12 小时内的 P99 读取延迟保持恒定在 10 毫秒以下，除了一个 12 毫秒的峰值。平均而言，12 小时运行的 P99 读取延迟为 7.8 毫秒。

12 小时内的 P99 更新延迟在整个 12 小时内呈现稳定模式，平均 P99 延迟为 3.9 毫秒。

![放大](https://cdn.thenewstack.io/media/2024/01/06e0c710-image17a.png)

![](https://cdn.thenewstack.io/media/2024/01/3eec4f94-image18a.png)


## 技术要点: 缓存工作负载，插入性能

除了三种定义的工作负载外，我们还在 MongoDB 和 ScyllaDB 中测量了小规模扩展(500 GB)、中型规模扩展(1 TB)和大规模扩展(10 TB)的纯插入性能。需要强调的是，对于 MongoDB 启用了批量插入，而对于 ScyllaDB 则没有(因为 YCSB 不支持它用于 ScyllaDB)。

以下结果显示，对于小规模扩展，实现的插入吞吐量在可比级别。然而，对于更大的数据集，ScyllaDB 在中型基准测试中实现了 3 倍更高的插入吞吐量。但对于大规模基准测试，MongoDB 无法摄入完整的 10 TB 数据，导致仅插入 5 TB 数据(更多详细信息，请参阅吞吐量结果)。然而，ScyllaDB 的性能比 MongoDB 高出 5 倍。

![放大](https://cdn.thenewstack.io/media/2024/01/75730d53-image19a.png)

## 技术要点: 缓存工作负载，客户端一致性性能影响

除了标准基准配置外，我们还以较弱的一致性设置运行了均匀分布的缓存工作负载。即，我们允许 MongoDB 从辅助节点读取(readPreference=secondarypreferred)，对于 ScyllaDB，我们将 readConsistency 设置为 ONE。

结果显示吞吐量有预期的增加: ScyllaDB 增加 23%，MongoDB 增加 14%。与社交工作负载的客户端一致性影响相比，此吞吐量增加较低，因为缓存工作负载仅为 50% 的读取工作负载，仅读取性能受益于应用的较弱读取一致性设置。通过应用较弱的写入一致性设置，也可以进一步增加整体吞吐量。

![放大](https://cdn.thenewstack.io/media/2024/01/8f6a1055-image20.png)

## 结论: 性能、成本和可扩展性

完整的基准测试包括 133 项性能和可扩展性测量，用于比较 MongoDB 与 ScyllaDB。结果显示，ScyllaDB 在 133 项测量中的 132 项上优于 MongoDB。

对于所有应用的工作负载，即缓存、社交和传感器，ScyllaDB 提供了更高的吞吐量(高达 20 倍)和更好的吞吐量可扩展性结果，与 MongoDB 相比。关于延迟结果，ScyllaDB 为几乎所有场景的插入、读取和更新操作实现了低于 10 毫秒的 P99 延迟。相反，MongoDB 仅对某些读取操作实现了低于 10 毫秒的 P99 延迟，而插入和更新延迟与 ScyllaDB 相比高出 68 倍。这些结果验证了 ScyllaDB 的分布式体系结构能够在规模上提供可预测的性能(如 benchANT 技术比较中所解释)的说法。

可扩展性结果显示，两种数据库技术随着工作负载的增长而水平扩展。然而，ScyllaDB 实现了近乎线性的可扩展性，而 MongoDB 显示出效率较低的水平可扩展性。在一定程度上，根据 ScyllaDB 的多主分布式体系结构，其结果在某种程度上是可以预期的，而近线性可扩展性仍然是一个杰出的结果。此外，由于不同的分布式体系结构(如 benchANT 技术比较中所解释)，MongoDB 的可扩展性效率较低的结果也在预期之中。

就价格性能而言，结果显示 ScyllaDB 具有明显的优势，根据工作负载和数据集大小，其价格性能比可高达 19 倍。因此，要实现与 ScyllaDB 相当的性能，需要一个规模更大、成本更高的 MongoDB Atlas 集群。

总结来说，这个基准测试研究表明，ScyllaDB为操作TB级数据集并需要高吞吐量(超过50kOps)以及对读写操作具有可预测的低延迟的应用程序提供了一个伟大的解决方案。这项研究没有考虑高级数据模型(如时间序列或向量)或复杂操作类型(聚合或扫描)的性能影响，这些将在未来的基准测试研究中考虑。但从当前的结果来看，在选择数据库技术之前进行深入的基准测试将帮助您选择一个显著降低成本并防止未来性能问题的数据库。

有关完整的设置和配置细节、每个工作负载的额外结果以及技术要点的讨论，请参阅[完整的基准测试报告](https://benchant.com/blog/mongodb-vs-scylladb-benchmark)。