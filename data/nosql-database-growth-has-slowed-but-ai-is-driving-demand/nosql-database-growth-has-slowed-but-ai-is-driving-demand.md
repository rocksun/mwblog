
<!--
title: NoSQL 数据库增长放缓，但人工智能正在推动需求
cover: https://cdn.thenewstack.io/media/2024/07/5a65fb92-pawel-czerwinski-weizaiwlk1k-unsplash.jpg
-->

与向量数据库相比，NoSQL 数据库的增长最近有所下降。然而，NoSQL 供应商认为他们的产品最适合 AI。

> 译自 [NoSQL Database Growth Has Slowed, but AI Is Driving Demand](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/)，作者 Richard MacManus。

四年前，我写过一篇关于 [NoSQL 数据库快速增长](https://thenewstack.io/redis-in-the-age-of-ai/) 的文章——很大程度上是因为它们与人工智能 (AI) 和机器学习 (ML) 的兼容性。但那是 *在* [生成式 AI 热潮开始](https://thenewstack.io/top-5-internet-technologies-of-2022/) 之前，OpenAI 在 2022 年 11 月发布了 ChatGPT。

那么，ChatGPT 出现后，NoSQL 数据库发生了什么变化？在 [向量数据库](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/) 的新时代，NoSQL 数据库系统——如文档存储 (MongoDB)、键值存储 (Redis) 和宽列存储 (Cassandra)——还在增长吗？

回到 2020 年，为了说明 NoSQL 数据库系统的增长，我使用了以下来自 [DB-Engines](https://db-engines.com/en/ranking_categories) 的图表：

![](https://cdn.thenewstack.io/media/2020/05/54662c9c-db-engines1.png)

该图表显示了从 2013 年到 2020 年，MongoDB、Redis 和 Cassandra 等系统的陡峭上升轨迹（尽管在这段时期结束时，所有三者都略有下降）。与 Oracle 和 MySQL 等传统关系型数据库的平坦——最终下降——曲线相比，NoSQL 的增长曲线非常显著。

以下是 DB-Engines 在过去 36 个月（3 年）内的最新流行度图表：

![](https://cdn.thenewstack.io/media/2024/07/3571b88d-dbengines-36mth_9july2024.png)

需要注意的是，该图表衡量的是流行度增长（而不是实际用户），我们可以看到，向量数据库自 2021 年以来自然经历了增长爆发——尽管它似乎在去年年底达到顶峰。与此同时，文档存储和键值存储略有下降。

但是，如果我们查看 2013 年的图表，我们可以看到向量数据库的增长还没有达到文档存储和键值存储的峰值（让我们忽略宽列存储图表，因为自 2020 年我的帖子以来，它的数据集似乎在 DB-Engines 上发生了变化）。

![](https://cdn.thenewstack.io/media/2024/07/32c44fd7-dbengines-since2013_9july2024.png)

此外，尽管增长率略有下降，但 NoSQL 数据库系统仍然是开发人员最受欢迎的选择之一。下图显示了过去两年中排名前十的数据库系统变化很小，前六名（包括排名第五的 MongoDB 和排名第六的 Redis）保持不变。我们还看到，前四名数据库系统都是关系型数据库；并且用户数量明显多于 MongoDB 和 Redis。

![](https://cdn.thenewstack.io/media/2024/07/6e9366a9-db-engines-ranking_july2024.png)

## NoSQL 和生成式 AI

当 [Redis](https://redis.com/?utm_content=inline+mention) 在今年早些时候宣布有争议的 [许可证变更](https://redis.io/blog/redis-adopts-dual-source-available-licensing/) 时，Linux 基金会几乎立即宣布支持 Redis 的开源分支，[名为 Valkey](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)。Redis 公司的立场是，大型云提供商拥有不公平的市场优势，新的许可证是其试图让他们付费的方式。MongoDB 在 2018 年也采取了类似的措施，收紧了其许可证的限制。

关于 Redis 新许可证的争论，我将留给其他人，但我确实想强调 [一篇博客文章](https://redis.io/blog/the-future-of-redis/)，Redis 在宣布后的第二天发布了这篇文章。这篇文章名为“Redis 的未来”，重点关注 Redis 的 AI 用途。“我们始终走在 GenAI 浪潮的前沿，”首席执行官 Rowan Trollope 和首席技术官 Yiftach Shoolman 写道，并补充说，“我们是最早认识到数据库中需要向量搜索功能的公司之一，甚至在 ChatGPT 和 LLM 成为家喻户晓的名字之前。”

这篇文章详细介绍了名为 Redis CoPilot 的 AI 驱动的助手的计划（[现在已可用](https://redis.io/chat)），“允许开发人员使用语言直接与他们的数据交互，并将这些数据转换为代码。”它还打算通过利用产品量化并进一步利用最新的硬件和 GPU 进步来提高向量处理性能，使 Redis “对于 RAG 用例更具成本效益”。

至于 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)，它也针对生成式 AI 用例。在最近发表在 The New Stack 上的一篇文章中，开发人员关系团队负责人 Rick Houlihan 明确地 [将它的解决方案与 PostgreSQL](https://thenewstack.io/benchmarking-postgresql-vs-mongodb-for-genai/) 进行了比较，PostgreSQL 是一个流行的开源关系型数据库系统。Houlihan 认为，像 PostgreSQL 这样的系统并非为 AI 所要求的工作负载类型而设计：

“考虑到 RDBMS 在处理宽行和大数据属性时众所周知的性能限制，这些测试表明像 PostgreSQL 这样的平台难以处理生成式 AI 工作负载所需的丰富、复杂文档数据，也就不足为奇了。”

毫不奇怪，他得出结论，使用文档数据库（如 MongoDB）“比使用并非为这些工作负载设计的工具提供更好的性能”。

为了维护 PostgreSQL 的声誉，为 Postgres 提供 AI 相关功能的托管服务提供商并不缺乏。今年早些时候，[我采访了一家名为 Tembo 的“Postgres 作为平台”公司](https://thenewstack.io/how-devs-can-use-postgres-extensions-including-for-ai-apps/)，该公司看到了对 AI 扩展的巨大需求。“Postgres 有一个名为 pgvector 的扩展，”Tembo 首席技术官 Samay Sharma 告诉我。“因此，它允许您将一个名为向量的简单数据类型添加到您现有的表中。因此，即使您有现有的数据行，您也可以添加一个向量数据类型——它是一个转换后的嵌入。”

## AI 数据供应充足

当然，现在每家数据库公司都声称其可以很好地与 AI 结合使用。就在上个月，[Oracle](https://developer.oracle.com/?utm_content=inline+mention) 发布了其 Oracle APEX 低代码开发平台的[AI 驱动更新](https://thenewstack.io/from-english-to-sql-oracle-apex-ai-bridges-the-language-gap/)，该公司表示，该更新使非开发人员能够在不到两分钟的时间内执行向量查询，而无需了解 SQL。

在 AI 方面，目前的需求并不缺乏——所有数据库公司和项目，无论是 SQL 还是 NoSQL，都从中受益。