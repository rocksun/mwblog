<!--
title: SQL与Python：数据世界的亦敌亦友
cover: https://cdn.thenewstack.io/media/2025/10/987a9f29-python.jpg
summary: SQL在2025年榜单跃升至第四位，因其声明性、高效处理数据。它与Python互补，AI可通过Python生成SQL。SQL将持续作为结构化数据标准接口，与AI深度融合。
-->

SQL在2025年榜单跃升至第四位，因其声明性、高效处理数据。它与Python互补，AI可通过Python生成SQL。SQL将持续作为结构化数据标准接口，与AI深度融合。

> 译自：[SQL vs. Python: Frenemies of the Data World](https://thenewstack.io/sql-vs-python-frenemies-of-the-data-world/)
> 
> 作者：Ivan Novick

每年，[IEEE Spectrum 顶级编程语言](https://spectrum.ieee.org/top-programming-languages-2025)排行榜真实反映了全球软件生态系统中至关重要的内容。在 2025 年的榜单中，SQL 从 2024 年的第 9 位跃升至第 4 位，仅次于 Python、Java 和 C++。考虑到 SQL 的“高龄”及其专业领域，这一排名引人注目。

在此背景下，数据揭示了一个更深层次的故事：几十年来，在创新浪潮中，SQL 作为企业分析的支柱始终屹立不倒，在表示和大规模查询数据方面效率无与伦比。[我曾撰文阐述为何 SQL 是 AI 的理想搭档](https://thenewstack.io/why-ai-and-sql-go-together-like-peanut-butter-and-jelly/)，并相信 SQL 人气惊人的跃升进一步证实了 SQL 和 [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/) 的互补性。这种互补性常常被误解，而实际上它们对于当今数据密集型 AI 工作负载都必不可少。

## **SQL 的起源**

SQL 创建于 20 世纪 70 年代，源于 Edgar Codd 对关系数据库的构想及其对关系代数和集合论的数学形式化。与指令执行**如何**完成任务的过程式和函数式语言不同，SQL 是声明性的；它指定你想要**什么**，而将路径的确定留给引擎。这种基于集合的抽象已经持续应用了几十年，支持从小型数据集到管理数十亿行的系统，因为它植根于关系代数和集合论。

SQL 已经超越了每一次硬件更新和编程趋势。它最初在大型机上运行，后来适应了 UNIX 服务器、分布式系统，现在又驱动着云 SaaS 数据库引擎。SQL 引擎已用 C、C++、Java 和其他语言实现，并针对多核 CPU、GPU 和 [NVMe 存储](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/)进行了优化。SQL 接口保持标准化，使用户免受复杂性影响，而底层实现则持续演进。

## **SQL 与过程式和函数式思维模式的对比**

SQL 与 [Java](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/)、[C++](https://thenewstack.io/introduction-to-c-programming-language/) 和 Python 等过程式语言之间的区别不仅仅是语法。过程式和函数式语言依赖显式控制流、循环、条件分支和函数调用来一次一个元素地处理数据。相比之下，SQL 一次性操作整组行。SQL 不是编写循环来扫描列表并求和，而是对列使用聚合函数 (SUM)。SQL 不是使用嵌套的 `if` 语句，而是应用 `WHERE` 子句来过滤子集。连接通过描述关系如何连接来取代手动指针追踪或映射查找。这种转变意味着，虽然过程式代码指定如何计算，但 SQL 指定需要什么结果，将决定使用索引、执行哈希连接还是跨多个 CPU 并行处理的任务留给了数据库优化器。

## **Python：互补而非竞争**

Python 在榜单中排名第一，其成功很大程度上归功于数据科学和机器学习。它易于学习、灵活，并得到丰富的数值计算和机器学习 (ML) 库生态系统的支持。但 Python 和 SQL 并非竞争对手；它们互为补充。SQL 处理结构化存储、过滤、连接和大规模聚合；Python 提供编排、统计建模和自定义逻辑。

分析师可能会编写 SQL 查询来提取数百万条销售记录，然后转向使用 pandas 或 NumPy 的 Python 进行可视化或统计测试。数据工程师使用 Airflow 或 Prefect 将 SQL 步骤嵌入到基于 Python 的工作流中，确保在下游转换之前高效进行数据库处理。一些数据库引擎甚至支持直接在 SQL 中嵌入 Python 函数，允许数据整理和自定义逻辑在靠近数据的地方执行，而无需将数据移出引擎。

## **AI 到 Python 到 SQL 的制胜之道**

Python 还可以以模板化的方式编写许多 SQL 查询。例如，你可能希望创建 50 个不同的 SQL 语句，以在 50 个不同的表或数据集上执行类似的任务。一个简单的 Python 查询可以轻松生成并运行 50 个 SQL 语句。

现在，在当今世界，AI 可以编写 Python 脚本。因此，通过对话式界面，AI 生成 Python，然后 Python 生成 SQL。

示例：“生成一个 Python 脚本，该脚本生成并运行一个 SQL 查询到人口表，并对人口统计数据进行平均。数据存储在 50 个表中，每个美国州一个表，因此生成 50 个这样的查询，并在 Python 脚本的末尾总结数据。”

因此，AI 生成 Python，Python 生成 SQL，形成一个和谐的链条。

## **SQL 的未来是什么？**

SQL 在 2025 年的持续相关性反映了其作为处理结构化数据的标准接口的作用。尽管硬件、编程范式和数据平台发生了变化，SQL 仍保持稳定，因为它植根于关系代数和集合论。未来趋势指向 SQL 与向量和 AI 工作负载的更广泛集成，以及用于数据库内函数的嵌入式过程语言（如 Python）。

SQL 不太可能被取代，而是将继续作为传统关系数据库、分布式数据仓库和混合数据平台等异构系统之间的通用层。它的未来由其实用性决定：SQL 仍然是查询和管理数据的标准化、广泛采用的方法，并且随着新引擎和基础设施的出现，它将继续在其中得到实现。