
<!--
title: DuckDB：适用于非大数据的进程内Python分析
cover: https://cdn.thenewstack.io/media/2024/05/0ac32b1b-duckdb.png
-->

DuckDB 是一款进程内分析数据库，它可以在无需维护分布式多服务器系统的情况下处理出人意料的大型数据集。最棒的是什么？您可以直接从 Python 应用程序分析数据。

> 译自 [DuckDB: In-Process Python Analytics for Not-Quite-Big Data](https://thenewstack.io/duckdb-in-process-python-analytics-for-not-quite-big-data/)，作者 Joab Jackson。

**匹兹堡** —— 即使分析非常大的数据集，也不总是需要集群。你可以将很多内容打包到运行开源 [DuckDB](https://duckdb.org/) 近进程分析数据库系统的单台服务器中。

这是在 [PyCon](https://us.pycon.org/) 上进行的多次 [演示](https://us.pycon.org/2024/schedule/presentation/132/) 的一个结论，该演示比较了在 [Python](https://thenewstack.io/what-is-python/) 程序员会议上给出的分析解决方案的性能，该会议上周在匹兹堡举行。在那里，他们比较了系统，例如，询问 [Dask](https://www.dask.org/) 系统是否比 [Apache Spark](https://thenewstack.io/context-apache-spark-for-artificial-intelligence-and-ai-2-0/) 的分析速度更快。

但是，如果你可以完全避免设置分布式系统，则可以避免很多维护方面的麻烦。

正如 [Kevin Kho](https://us.pycon.org/2024/speaker/profile/151/) 和 [Han Wang](https://www.linkedin.com/in/han-wang-97272610/) 在 [演示](https://x.com/Joab_Jackson/status/1791908986779824181) 中解释的那样，如果你正确优化，你可以从单台机器中获得很多好处。这就是 DuckDB 的使命。

![](https://cdn.thenewstack.io/media/2024/05/efc645af-ducdb-comparison-1024x768.jpg)

2021 年，H20.ai 在 [一组基准测试](https://h2oai.github.io/db-benchmark/) 中测试了 DuckDB，比较了开源数据科学中流行的各种类似数据库工具的处理速度。

测试人员对 1000 万行和 9 列（约 0.5GB）运行了五个查询。Duck 在短短两秒内完成了任务。对于运行在单台计算机上的数据库来说，这是令人惊讶的。更令人惊讶的是，它在 14 秒内处理了 1 亿行（5GB）。

这些数字令人印象深刻，2023 年，DuckDB 团队返回并 [调整了配置设置并升级了硬件](https://duckdb.org/2023/04/14/h2oai.html)，并将 5GB 的工作负载减少到两秒，而 0.5GB 的工作负载减少到不到一秒。

它甚至在 24 秒内处理了 50GB 的工作负载——通常为 Spark 等分布式系统保留。

在演示中，Lyft 机器学习平台的技术负责人 Wang 说：“这是一个令人震惊的数字。这些改进令人惊叹。”

![](https://cdn.thenewstack.io/media/2024/05/b0ef67e9-duckdb-table.jpg)

*DuckDB 的大数据系统基准，2003 年。*

**结论？** Wang 指出，数量惊人的自称为“大数据”风格的项目不需要 Spark 或其他分布式解决方案：它们可以很好地适应单台服务器。采用这种方法消除了管理分布式系统的大量开销，并将所有数据和代码保留在本地机器上。

## 介绍 DuckDB

[DuckDB](https://duckdb.org/) 正在发生很多事情，它是一个在 2018 年创建的分析型关系近进程 SQL 数据库系统。有两件事立即将它与其他数据平台区分开来。

1. 它将 SQL 与 Python 相结合，为开发人员/分析师提供了一种表达式查询语言，该语言针对应用程序进程本身中的数据执行。
2. 它旨在仅在单台机器上运行。这是一个特性，而不是一个缺陷，因为它消除了在分布式平台上运行数据平台的所有复杂性。

[Alex Monahan](https://x.com/__alexmonahan__?lang=en) 在另一个 Pycon 演示中说：“一旦一个问题对 Pandas 来说有点太大了，你就必须向它抛出一个巨大的分布式系统。这就像用大锤子敲核桃。它不符合人体工程学。”Monham 是 [MotherDuck](https://motherduck.com/about-us/) 的前置软件工程师，该公司提供基于 Duck 的无服务器分析服务。

DuckDB 的两位创建者——[Hannes Mühleisen](https://www.linkedin.com/in/hfmuehleisen/?originalSubdomain=nl)（首席执行官）和 [Mark Raasveldt](https://mytherin.github.io/)（首席技术官）——创立了 [DuckDB Labs](https://duckdblabs.com/)，为该数据库系统提供商业支持，该系统旨在提供快速、易于部署的中型数据分析。

他们从 [能够的小型数据库](https://thenewstack.io/the-origin-story-of-sqlite-the-worlds-most-widely-used-database-software/) 中汲取了相当多的灵感，认为 DuckDB 是列的 SQLite，而不是行的 SQLite。

Duck 具有 Python 风格的界面，还专门为数据科学社区构建。数据将被分析、建模和可视化。数据科学家倾向于不使用数据库，而是依赖 CSV 文件和其他非结构化或半结构化数据源。Duck 允许他们将数据操作直接嵌入到其代码本身中。

这款获得 MIT 许可的开源软件是用 C++ 编写的，因此速度很快。

DuckDB 旨在快速运行，充分利用服务器的所有内核和缓存层次结构。而 SQLite 是一个一次处理一行的基于行的数据库引擎，Duck 一次可以处理 2048 行的整个向量。

它是一个从 Python 安装程序进行的单一二进制安装，可用于多个平台，所有平台均已预编译，因此可以通过命令行或通过客户端库下载并运行。甚至还有一个版本 [在浏览器中运行](https://shell.duckdb.org/)，通过 WebAssembly。

它是一个进程内应用程序，并写入磁盘，这意味着它不受服务器 RAM 的限制，它可以使用整个硬盘驱动器，从而为处理 TB 级数据大小铺平了道路。与客户端-服务器数据库不同，它不依赖于第三方传输机制将数据从服务器传输到客户端。相反，就像 SQLite 一样，应用程序可以作为 Python 调用的一部分提取数据，在同一内存空间内的进程内通信中。

“你直接在它所在的位置读取它，”Monahan 说。

您可以通过多种不同的方式将数据帧本机写入数据库，包括用户定义函数、完整的关联 API、 [Ibis 库](https://duckdb.org/docs/guides/python/ibis.html) 以同时跨多个后端数据源同时写入数据帧，以及 PySpark，但使用不同的导入语句。

## DuckDB 和 Python 如何协同工作

除了命令行之外，它还附带了 15 种语言的客户端。Python 是最流行的，但也有 [Node](https://thenewstack.io/ryan-dahl-from-node-js-and-deno-to-the-modern-jsr-registry/)、JBDC 和 OBDC。它可以读取 CSV、JSON 文件、Apache Iceberg 文件。DuckDB 可以本机读取 Pandas、Polaris 和 Arrow 文件，而无需将数据复制到另一种格式。与大多数仅限 SQL 的数据库系统不同，它在数据被摄取时保留数据的原始数据。

“因此，这可以适应许多工作流，”Monahan 说。

它还可以读取互联网上的文件，包括来自 GitHub（通过 FTP）、Amazon S3、Azure Blob 存储和 Google Cloud Storage 的文件。它可以输出 [TensorFlow](https://thenewstack.io/python-tutorial-use-tensorflow-to-generate-predictive-text/) 和 [Pytorch 张量](https://thenewstack.io/pytorch-lightning-and-the-future-of-open-source-ai/)。

DuckDB 使用一种非常类似 Python 的 SQL 变体，该变体可以本机摄取数据帧。

Monahan 制作了一个示例“Hello World”应用程序来说明：

```
# !pip install duckdb
import duckdb

duckdb.sql("SELECT 42").fetchall()
```

将生成以下输出：

```
[(42,)]
```

该数据库使用 PostgreSQL 作为基础，尽管对 SQL 进行了一些修改，既是为了简化语言，也是为了扩展其功能。

![](https://cdn.thenewstack.io/media/2024/05/15683171-duck-sql-scaled.jpg)

*DuckDB 扩展和简化 SQL 的方式（Alex Monahan 在 Pycon 上的演讲）*

## 大数据已死？

总之，DuckDB 是一个具有革命性意图的快速数据库，即使对于非常大的数据集，它也可以实现单计算机分析。它质疑 [基于大数据的解决方案](https://thenewstack.io/databricks-sees-and-raises-snowflake-with-gen-ai-llmops-more/) 的必要性。

在 2023 年 MotherDuck 博客的一篇广为流传的帖子中，挑衅地题为“ [大数据已死](https://motherduck.com/blog/big-data-is-dead/)”，Jordan Tigani 指出“大多数应用程序不需要处理海量数据”。

他写道：“用于分析工作负载处理的数据量几乎肯定比你想象的要小。”因此，在投入更昂贵的数据仓库或分布式分析系统之前，先考虑一个简单的基于单计算机的分析软件是有意义的。
