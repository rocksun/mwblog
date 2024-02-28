<!--
title: TsFile：一种IoT时间序列数据的标准格式
cover: https://cdn.thenewstack.io/media/2024/02/c0118649-turbine-1024x576.jpg
-->

这种列存储文件格式专为物联网的独特需求而设计，旨在减少网络传输和云计算资源的消耗。

> 译自 [TsFile: A Standard Format for IoT Time Series Data](https://thenewstack.io/tsfile-a-standard-format-for-iot-time-series-data/)，作者 Susan Hall。

TsFile 项目已经达到 1.0 版本，提交者们正努力使其成为 Apache 软件基金会内的一个独立项目。

TsFile 是一种为时间序列数据设计的列存储文件格式，具有先进的压缩技术以最小化存储空间，高吞吐量的读写能力，并与 [Apache 项目](https://thenewstack.io/apache-streaming-projects-exploratory-guide/) Spark 和 Flink 等处理和分析工具深度集成。

随着工业物联网的发展，例如单个风力涡轮机产生了[大量的数据](https://thenewstack.io/data/)。

根据[该项目的 GitHub 页面](https://github.com/thulab/tsfile)，“特别是当物联网进入工业互联网时，智能设备产生的数据量比面向消费者的物联网多出一到两个数量级”，获取可操作的见解变得更加复杂。

它表示 TsFile 旨在支持“高达每秒数千万数据点的高吞吐量摄取，仅用于修正低质量数据的稀疏更新；紧凑的数据打包和对长期历史数据的深度压缩；传统顺序和条件查询，复杂的探索性查询，信号处理，数据挖掘和机器学习。”

## IoTDB 中的底层格式

TsFile 是 [Apache IoTDB 时序数据库](https://sxsong.github.io/doc/23sigmod-iotdb.pdf)的底层存储文件格式。IoTDB 代表着中国清华大学软件学院超过十年的研究工作。它于 2020 年成为 Apache 软件基金会的[顶级项目](https://thenewstack.io/iotdb-provides-data-management-for-industrial-edge-it/)。

“在 TsFile 出现之前，时间序列数据缺乏标准文件格式，导致数据收集和处理复杂化。” 项目委员会发言人 Pengcheng Zheng 在一封电子邮件中说道。

“有了 TsFile，用户可以在 IoTDB 中执行可移植的数据卸载和加载，使底层数据的管理和迁移更加灵活。即使没有数据库，用户也可以直接使用 SDK 从 TsFile 中读取数据，实现一些轻量级的数据读写场景。”

![](https://cdn.thenewstack.io/media/2024/02/f425ef9d-screenshot-2024-02-24-at-10.44.09%E2%80%AFam.png)

用户可以将数据写入端设备或网关中的 TsFile，然后将其发送到云端到 IoTDB 或其他统一管理系统。它本身不是数据库，而是一种通过压缩和高效存储来减少云端网络传输和计算资源消耗的格式。

TsFile 可以存储来自单个设备或多个设备的时间序列。虽然来自多个设备的数据存储在 TsFile 中，但每个设备都有独立的存储引擎，因此在物理上与传统数据库中一样是隔离的。数据按时间维度索引以加速查询性能，实现快速过滤和检索时间序列数据。

在 IoTDB 中，它支持在线事务处理（OLTP）和在线分析处理（OLAP），无需将数据重新加载到不同的存储中。

## 使用更少的云资源

物联网原生数据模型将设备和传感器的时间序列数据组织成适应延迟数据到达的日志结构合并树，适用于写入密集型工作负载。对于短暂的延迟，数据首先缓存在 MemTables 中，然后再刷新到 TsFiles 中。

TsFile 允许用户直接写入数据，无论是否预先定义了模式、是否使用了过滤器，而[新版本增加了对更多数据类型和算法的支持](https://dlcdn.apache.org/tsfile/1.0.0/RELEASE_NOTES.md)。

尽管最初是用 Java 编写的，但据 Zheng 称，TsFile 在多种语言中的实现需求正在增长，例如 C++、Go 和 Rust。其用户通常在需要高效数据存储、快速访问和分析至关重要的场景中工作，如物联网、智能控制系统、金融分析和日志分析。

他指出，TsFile 以其专注于时间序列数据独特需求的特点而脱颖而出。

“过去，公司通常会以各种用户定义的文件格式编写时间序列数据，缺乏统一性，或者使用通用的列式文件格式，如 [Apache 项目] [Parquet](https://parquet.apache.org/) 和 [ORC](https://orc.apache.org/)，这使得没有标准的数据收集和处理变得复杂。”

“TsFile 提供了诸如深度压缩长期历史数据、高吞吐量和处理罕见更新等优势。它与 IoTDB 和其他系统的集成能力进一步突显了其优势。用户可以在嵌入式设备或网关上写入 TsFile 数据，然后直接将 TsFile 传输到云端，无需进行传统的 ETL [提取、转换、加载] 过程。通过这种方式，[云端的网络传输和计算资源需求](https://thenewstack.io/the-right-sizing-problem-in-cloud-computing-and-how-to-solve-it/)得到了降低。”

未来，委员会希望使 TsFile 成为一个独立的项目，拥有自己的 SDK 和更易于使用的文档，增加对更多语言的支持，在 TsFile 中集成更多编码和[压缩方法](https://dbdb.io/db/iotdb)，并提供更多工具，如可视化、解析和修复工具。

“然而，这些计划并非不可撤销，因为我们是按照 Apache 的方式进行合作，每次讨论新见解都可能有助于修改和优化，” Zheng 先生说。

Susan Hall 是 The New Stack 的赞助编辑。她的工作是帮助赞助商使其贡献的内容获得尽可能广泛的读者群。她从 The New Stack 的早期就开始撰写文章，以及其他网站...
阅读更多关于 Susan Hall 的内容
