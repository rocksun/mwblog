
<!--
title: 深入探索列式数据库：是什么让它们脱颖而出
cover: https://cdn.thenewstack.io/media/2025/02/c6ba388a-tom-podmore-70ru5lg28me-unsplash-scaled.jpg
-->

如果您是一名数据从业者，了解这些内部原理可以帮助您优化性能。

> 译自 [Deep Dive into Columnar Databases: What Makes Them Shine](https://thenewstack.io/deep-dive-into-columnar-databases-what-makes-them-shine/)，作者 Gaurav Ramesh。

列式存储已成为数据工程和分析领域的一个颠覆者。与传统的行式数据库相比，它提供了显著的性能优势。

以列存储数据的想法并不新鲜。它最早由 GP Copeland 和 SN Khoshafian 在 1985 年全面提出。他们的论文 *“[A Decomposition Storage Model (DSM)](https://dl.acm.org/doi/10.1145/971699.318923),”* 提出以二元关系存储数据，将每个属性值与记录的标识符配对。这种方法按列而不是按行组织数据，为涉及属性子集的查询提供了简单性和检索性能优势。但是，它总体上需要更多的存储空间。

研究人员于 [1999 年开始开发 MonetDB](http://sites.computer.org/debull/A12mar/monetdb.pdf)，并于 2004 年将其作为开源项目发布。它成为首批采用列式架构进行分析工作负载并展示其有效性的系统之一。在 2000 年代中期开发的 [C-Store](https://dl.acm.org/doi/10.5555/1083592.1083658) 标志着另一个重要的里程碑。它引入了先进的概念，这些概念现在已成为现代列式存储系统中的标准。

在 2000 年代后期和 2010 年代初期，该领域的发展加速，[Apache Parquet](https://parquet.apache.org/) 等项目（受 [Google 的 Dremel 论文](https://research.google/pubs/dremel-interactive-analysis-of-web-scale-datasets-2/) 的影响）将列式存储引入了 Hadoop 生态系统。

## 核心概念：列式存储与行式存储

传统的行式[数据库将单个行的所有数据存储在一起](https://thenewstack.io/how-open-source-and-time-series-data-fit-together/)。一行表示您要建模的实体。从这个角度来看，对于这篇文章，可以将面向文档的[数据库（如 MongoDB）](https://thenewstack.io/how-to-plan-your-mongodb-upgrade/) 视为行式数据库，因为它将整个文档（实体）存储在一起，类似于行式数据库。相比之下，列式数据存储将数据组织成列，每列包含所有行中单个属性的值。这种看似简单的更改对性能产生了深远的影响。

**查询处理中的谓词和投影**

在讨论事务和分析系统时，需要理解两个关键概念：

- **谓词**是您用来过滤所需实体（行）的条件（将它们视为 SQL 查询中的 `WHERE` 子句）。
- **投影**是您在响应中需要的字段（列）（将它们视为在 `SELECT` 语句中定义的名称）。

如果您将[数据视为垂直堆叠的行列表](https://thenewstack.io/the-architects-guide-to-the-modern-data-stack/)，则谓词会水平切片，而投影会垂直切片。

事务查询通常依赖于谓词来过滤行，投影跨越整行（例如，`SELECT * FROM orders WHERE user_id = 1234`）。相比之下，分析查询中的投影涉及被查询实体的一小部分字段（例如，`SELECT user_id, name, num_orders FROM user_aggregates WHERE user_id = 1234`）。

考虑一个包含 50 列和数百万行的表。在行式系统中，如果您只需要三列，数据库仍然必须读取每行的所有 50 列。使用列式存储，仅访问三个相关的列，从而大大减少了 I/O 开销，即[在分析中处理的数据量](https://thenewstack.io/clickhouse-optimizing-real-time-data-analysis-with-online-analytical-processing/)查询。

**支持列式存储的关键技术**

以列存储数据[可以实现各种优化，从而显著提高查询性能](https://thenewstack.io/enhancing-the-flexibility-of-sparks-physical-plan-to-enable-execution-on-various-native-engines/)。这是一个思维模型：将查询执行视为一个[通过各个阶段传递数据的管道](https://thenewstack.io/leaky-data-pipelines-uncovering-the-hidden-security-risks/)，并在每个步骤中对其进行转换。数据越小，成本越低，管道速度越快。

[减少数据](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/)您可以使用多种方法：

- **高效的数据表示**（数据压缩，列式压缩）
- **提前过滤数据**（列裁剪，谓词下推）
- **尽可能晚地扩展数据**（直接对压缩数据进行操作，延迟物化）
- **更快的数据处理**（向量化执行，优化连接）

这些技术是相互关联的，并且相互依赖以获得最大的性能提升。

**数据压缩和列式压缩**

列式存储实现了高压缩率，因为单个列中的数据类型相同并且表现出相似的模式。诸如**字典编码、运行长度编码 (RLE)、位打包和增量编码**等技术通常用于现代列式存储中。

例如，在跟踪用户流量来源的 Web 分析数据库中，*source*列通常具有一小组唯一值。 这允许：

*   **字典编码**：将整数值分配给字符串值（例如，email = 1，Twitter = 2）。
*   **运行长度编码 (RLE)**：如果连续条目具有相同的值，则将其存储为（值，计数）。
*   **位打包**：如果只存在几个唯一值，则每个值使用较少的位而不是完整的整数。

**列裁剪**

列裁剪消除了查询执行中不必要的列。 考虑以下查询：

```sql
SELECT first_name, last_name, email, phone FROM users WHERE num_orders > 10
```

如果表有 100 列，但查询只需要 5 列，则列裁剪可将 I/O 开销降低 95%。

**谓词下推**

谓词下推在查询执行管道中尽早地过滤数据。 通过使用**区域图**（跟踪存储块内最小值/最大值的元数据），数据库可以跳过不符合过滤条件的整个块。

例如，在查询中：

```sql
SELECT name FROM users WHERE age > 30 AND city = 'New York'
```

列式数据库可以首先根据元数据过滤块，然后再扫描单个行，从而减少不必要的处理。

**直接对压缩数据进行操作**

列式数据库可以直接对压缩数据执行操作，从而最大限度地降低 I/O 成本。 考虑以下查询：

```sql
SELECT sum(salary) FROM employees WHERE department = 1002
```

使用字典编码和 RLE，只有相关数据在最后一步被读取和扩展，从而显着提高性能。

**延迟物化**

延迟物化会延迟加载不必要的列，直到需要时才加载。 在查询中：

```sql
SELECT name FROM users WHERE age > 30 AND city = 'New York'
```

最初只处理 age 和 city，name 列在最后阶段加载。

**向量化处理**

SIMD（单指令多数据）允许处理器并行地对多个值执行操作。 考虑：

```
SELECT sum(price) FROM sales WHERE user_id = 1234
```

SIMD 不是逐行评估 user_id，而是一次比较 256 个值，从而显着提高速度。

**高效的连接实现**

列式数据库实现了高级连接技术，例如使用 Bloom 过滤器的半连接。 这些结构允许数据库有效地检查数据集中是否存在某个值，从而减少不必要的比较。

例如，在连接中：

```sql
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.id WHERE c.region = 'EMEA'
```

为有效客户构建 Bloom 过滤器，允许数据库快速丢弃不相关的订单。

## 结论

列式数据存储提供：

*   通过压缩实现**存储效率**
*   通过列裁剪和谓词下推实现**减少 I/O**
*   使用向量化处理和优化连接实现**更快的执行速度**

它们广泛用于 Web 分析、商业智能、机器学习基础设施和实时分析。

如果您是数据从业者，了解这些内部原理可以帮助您优化性能。 如果您是工程负责人，这些技术将帮助您评估权衡并为您的组织做出战略决策。