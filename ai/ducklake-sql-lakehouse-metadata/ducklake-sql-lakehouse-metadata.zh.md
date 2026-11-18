![在本期The New Stack播客中，DuckLake首席开发者兼DuckLake首席工程师Pedro Holanda讨论了该开源表格式如何降低复杂度、提升性能并使大规模数据管理更加易用。](https://cdn.thenewstack.io/media/2026/11/b52163ee-for-thumbnail-25-1024x576.png)

如果一个普通的SQL数据库就能追踪其文件，数据湖屋能变得多简单？这就是本期 *The New Stack* 播客中探讨的问题。

DuckLake 是由总部位于阿姆斯特丹的 [DuckLabs](https://duckdb.org) 创建的开源表湖屋格式，它通过将表元数据存储在标准SQL数据库中（而不是将清单文件散布在对象存储中），充当了数据管理的交通警察。与传统表格式不同，DuckLake 将湖屋元数据视为关系数据库问题。这些由 Parquet 文件和 SQL 数据库提供支持的高级数据湖功能，降低了传统的湖屋复杂度。

视频

10月，DuckLake 1.1 伴随 [DuckDB 2.0.0 LTS](https://duckdb.org/2026/10/21/announcing-duckdb-200) 一同发布。*The New Stack* 在其阿姆斯特丹总部采访了 DuckLabs 首席 DuckLake 开发者兼首席工程师 [Pedro Holanda](https://www.linkedin.com/in/pdet/)，畅谈此次发布。Holanda 从 DuckDB 还是早期研究原型时就开始为该 [DuckDB 开源项目](https://github.com/duckdb/duckdb)做出贡献，并在访谈中分享了 DuckLake 的完整演变过程。

“这些湖屋格式的存在是为了让人能够更换数据库系统而无需进行迁移，”Holanda 告诉 *The New Stack*。由于其复杂性，“你需要一个数据库系统来追踪哪个表拥有最新版本。”

Holanda 表示，DuckLake 应用了数十年的研究成果，旨在减少文件数量，从而在数据快速增长的时代降低复杂度，同时利用了每个使用数据库系统的人都熟悉 SQL 和架构工作原理这一优势。

“简单性体现在你获取数据的方式上，”Holanda 在谈到 DuckLake 时说道。“你会在某处发起查询。服务器会返回这些答案，并且你确切地知道必须读取哪些 Parquet 文件。因此 Parquet 文件不会改变。改变的只有目录。”

数据湖的维护者通常有许多维护任务要执行。他说，如果你最终产生了很多文件，DuckLake 允许你将它们粘合到一个文件中以减少请求数量。这也可以跨多个快照进行，从而进一步减少文件数量。它还通过使用内联（inlining）和刷新（flushing），解决了流数据湖和湖屋中的“小文件问题”。

Holanda 指出，对于传统数据湖来说，由于有多个数据源同时写入，“你最终会得到如此多的文件，以至于当你不得不查询它时，你必须遍历一堆元数据文件才能弄清楚你需要读取哪些 Parquet 文件，然后你还要读取一堆 Parquet 文件”，这会拖慢所有速度并让开发者感到沮丧。

DuckLake 以速度快、使用简单著称，运行不需要庞大的服务器集群。部分原因在于 Parquet 与 DuckDB 存储非常相似：两者都是列式的，并按行组组织，这使得数据处理步骤保持在最低限度。

“我们在构建 DuckLake 时意识到的一件事是，‘嘿，我们现在有了一个数据库系统，我们有了一个目录；如果我们把数据存储在表上这个激进的想法付诸实践会怎么样？’”他说。“通过 DuckLake，你可以在目录中获得作为表的实际数据表示，我们称之为内联。”

> “通过 DuckLake，你可以在目录中获得作为表的实际数据表示，我们称之为内联。”

在 10 月下旬亚马逊的第三季度财报电话会议上，首席执行官 Andy Jassy 批评了在数据存储和分析引擎之间移动数据的复杂性，特别是随着 AWS 客户的数据生成持续增长。亚马逊以内部使用自家技术闻名，Jassy 将 DuckDB 对这一复杂性问题的解决方案作为 [其收购 DuckLabs](https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/) 的原因。

“随着我们对 DuckLabs 的收购，DuckDB 将成为 AWS 存储和 analytics 的通用 SQL 方言，通过一个快速、简单易用且无处不在的现代 analytics 引擎来简化数据处理，客户将能够编写一次 SQL 查询，然后使用任何 AWS analytics 服务进行执行，”Jassy 说。“在 analytics 领域，客户将首次在查询引擎之间实现零迁移或零可移植性成本。这意义重大，你可以想象它也将如何帮助智能体进行高效查询。”

在独立的 DuckDB 基金会的监督下，DuckDB 和 DuckLake 仍然在 MIT 许可证下保持免费和开源。

总体而言，DuckLake 的最新版本将新功能与 200 多个用于提升质量和稳定性的 bug 修复结合在一起，并且它在 DuckDB 中原生运行。

文章 [DuckLake 1.1 彻底解决AI时代数据湖的荒谬复杂度](https://thenewstack.io/ducklake-sql-lakehouse-metadata/) 最初发布于 [The New Stack](https://thenewstack.io)。