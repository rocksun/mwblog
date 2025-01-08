# NoSQL数据库能否符合ACID特性？

![关于NoSQL数据库能否符合ACID特性的特色图片](https://cdn.thenewstack.io/media/2025/01/f77760ab-content-1024x576.jpg)

ACID特性概念传统上与关系型数据库相关联，导致对其在NoSQL系统中适用性的误解。一些知名网站，例如[AWS](https://aws.amazon.com/?utm_content=inline+mention)，断言[NoSQL无法符合ACID特性](https://aws.amazon.com/compare/the-difference-between-acid-and-base-database/)。与这些观点相反，ACID（原子性、一致性、隔离性、持久性）并非关系型数据库所独有，而是事务处理系统的基石。

让我们探讨这些误解以及为什么NoSQL数据库能够——而且经常——遵守ACID特性。

早期的[NoSQL系统](https://thenewstack.io/sql-nosql-and-vectors-oh-my/)优先考虑性能和可用性，经常放松ACID保证，这导致了NoSQL本质上不符合ACID特性的认知。

另一个重要的混淆来源在于对ACID中“C”（一致性）的解释。许多人错误地认为它要求引用完整性约束，而NoSQL数据库通常不支持这一点。然而，ACID的一致性概念更广泛，并不固有地要求引用完整性，允许NoSQL数据库在适当的情况下实现ACID一致性。

**ACID的起源**

原子性、一致性和持久性属性是由Jim Gray在其关于[事务](https://jimgray.azurewebsites.net/papers/theTransactionConcept.pdf?from=https://research.microsoft.com/~gray/papers/theTransactionConcept.pdf&type=path)的开创性论文中提出的。虽然ACID首字母缩略词后来才出现，但基本概念起源于Gray对事务处理的讨论。值得注意的是，Gray对一致性的定义并不依赖于关系型数据库特有的引用完整性约束。相反，它包含一个更广泛的概念：

“事务是对状态的转换，具有原子性（全部或无）、持久性（效果能够在故障后存活）和一致性（正确的转换）的特性。”

Jim Gray和Andreas Reuter后来[这样定义一致性](https://archive.org/details/transactionproce0000gray)：

“事务是对状态的正确转换。作为一个组采取的行动不会违反与状态相关的任何完整性约束。这要求事务是一个正确的程序。”

这突出表明，ACID是一个用于确保事务处理系统（无论是否为关系型）正确性和可靠性的框架。

**事务处理系统：更广泛的背景**

此外，Gray和Reuter[将事务处理系统定义为](https://archive.org/details/transactionproce0000gray)：

“事务处理系统（TP系统）管理与数据库交互以表示和操作现实世界状态的应用程序。它们通常支持分布式、[具有严格可用性和性能要求的异构环境](https://thenewstack.io/heterogeneous-processing-requires-data-parallelization-tools-sycl-and-dpc-are-a-good-start/)。历史上，TP系统开创了诸如容错存储、分布式计算以及最值得注意的是ACID特性等概念。”

甚至在关系型系统之前，例如[IBM](https://www.ibm.com?utm_content=inline+mention)在20世纪70年代的信息管理系统(IMS)，就已经支持ACID事务，远在该首字母缩略词被创造出来之前。

**ACID特性：分层视角**

ACID一致性可以理解为数据库系统内各个层提供的一组保证：

| 层级 | 目的 |
|---|---|
| 查询层 | 支持 |


这些层说明ACID一致性是整个数据库系统协调保证的结果。特别是，这些保证是由查询语言或数据模型层以下的层提供的，这些层可以通过引入更多关于该数据库系统必须确保的完整性约束的概念来增加ACID保证。

**一致性：ACID与CAP**

一个常见的混淆来源是ACID和CAP（一致性、可用性、分区容忍性）中“一致性”一词的双重使用。在ACID中，一致性指的是事务状态转换相对于用户定义约束（例如主键、引用完整性）的正确性。[在CAP中，一致性](https://aerospike.com/blog/implementing-strong-consistency-in-distributed-database-systems/?utm_source=byline&utm_medium=pr&utm_campaign=The%20New%20Stack)表示分布式系统中副本之间的数据一致性。

请注意：

- 在严格串行化隔离级别下运行的符合ACID特性的分布式数据库固有地满足CAP的一致性（线性化）要求。
缺乏CAP一致性（线性化）意味着未能满足ACID的原子性和严格串行化隔离保证。

**BASE与ACID的二分法**

BASE（基本可用，软状态，最终一致性）理念随着NoSQL数据库的出现而出现，以解决Web应用程序的可扩展性需求。早期的NoSQL系统优先考虑可用性和分区容错性，通常会放宽ACID保证。这种区别导致了一种误解，即NoSQL数据库无法实现ACID一致性。

然而，NoSQL系统的发展模糊了这些界限。许多现代NoSQL数据库现在支持：

- 强一致性模型（CAP中的C）
- 具有串行化保证的事务（ACID中的A、I和D）
- 主键等约束的强制执行

**NoSQL系统中的ACID一致性**

一些NoSQL数据库声称具有ACID一致性，并有强大的技术实现作为支撑。但是，请注意，并非所有这些系统都可以在严格的串行化隔离级别运行。例如：

* **DynamoDB:** 根据[AWS](https://aws.amazon.com/dynamodb/features/)，“DynamoDB支持原子性、一致性、隔离性和持久性（ACID）事务，从而能够跨表内和跨表中的多个项目实现复杂的业务逻辑。” 提供具有严格ACID保证的多文档事务。
* **MongoDB:** [https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)
* **Aerospike:** 将在2025年初的8.0服务器版本中发布对严格可串行化ACID事务的支持。
* **Databricks的Delta Lake:** 在分布式对象存储上提供ACID兼容的表存储。

这些例子表明，NoSQL数据库能够并且确实实现了ACID一致性，这使得它们适合于关键任务应用程序。

**结论**

ACID不是关系数据库的遗留物，而是事务处理系统中的一个基础概念。现代NoSQL数据库已经发展到包含ACID保证，挑战了它们天生就是“BASE”的过时说法。随着数据库生态系统的不断创新，必须重新定义我们对ACID的理解，将其视为事务系统的属性，而不管底层数据模型如何。

通过消除这些误解，我们可以更好地理解NoSQL数据库在为各种应用程序提供可靠、一致和可扩展的解决方案方面的能力。

*访问我们的网站，了解更多关于**Aerospike数据库**的信息。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。