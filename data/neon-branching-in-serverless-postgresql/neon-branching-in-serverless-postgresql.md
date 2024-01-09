<!--
title: 无服务器PostgreSQL中的分支机制
cover: https://cdn.thenewstack.io/media/2024/01/114b8dd9-screenshot-2024-01-06-at-10.37.53 am-1024x452.png
-->

分支机制为用户提供了生产数据库的完整副本，用户可以在副本上进行各种实验或测试，而不会影响到主分支上的生产数据库。这种分支机制非常有利于开发和测试工作的进行。

> 译自 [Neon: Branching in Serverless PostgreSQL](https://thenewstack.io/neon-branching-in-serverless-postgresql/)，作者 Susan Hall 是The New Stack的赞助商编辑。她的工作是帮助赞助商为其提供的内容获得尽可能广泛的读者群。她从The New Stack的早期就开始为该网站撰稿，也为其他网站撰稿......

尽管 git 仓库中广泛使用分支，但根据无服务器 PostgreSQL 多云提供商 [Neon](https://neon.tech/) 的联合创始人兼首席执行官 [Nikita Shamgunov](https://www.linkedin.com/in/nikitashamgunov/) 所言，分支从未真正适合数据库。

尽管通过大量艰苦工作，Neon 已经实现了分支，但他说分支的出现是从一个基础设施特性发展成为一个开发者工作流工具。

“在 Postgres 现有的架构中......实现分支是一个非常困难的特性。它需要新一代的架构和存储架构，才能实现分支，因为分支的关键特性是写时复制。例如 git 就有这一特性，当你创建一个分支时，基本上只是移动了一些指针。这就为你在一个独立的分支中获取了数据的完整隔离副本。”

它需要文件系统和数据库引擎的紧密集成。

“我们现有的文件系统不会关心上面运行的是什么，对吗？它们不知道在文件系统上面运行的是数据库还是其他应用程序，并在创建分支时保留所有事务语义，使它对当前在生产环境中运行的系统不可检测。在这种存储之上做到这一点，是一个非常困难的事情。”

## 在沙盒中获得数据的副本。

由于 Postgres 最底层与文件系统之间的 API 相对较小，Neon 拦截并重定向从本地文件系统的读写调用，以使任何 RPC 调用进入其云原生存储。其专门为 Postgres 定制构建的存储层在节点集群间重新分布数据，提供近乎无限的容量，并通过将较少使用的数据移动到低成本层面节省成本。

从虚拟的角度来看，它是数据的副本，但从物理的角度来看，它是写时复制，这不会使所需的存储空间加倍，而是用作更改指向数据的指针的一种方法。

“从物理上来说，它只是一个指针......指向同一页面的指针。只有在页面被修改时，我们才会创建额外的物理页面。这就是写时复制的工作方式。而由于它位于存储子系统中，在 Postgres 本身内部构建它是非常困难的，几乎不可能的。它运行在文件系统之上，而 Postgres 对文件系统没有影响力。” Shamgunov 解释道。

[分支](https://neon.tech/docs/introduction/branching)为用户提供了生产数据的完整副本，但这是一个沙盒环境，用户可以在其中进行实验，而不会影响到主分支。

您可以创建一个分支，其中包含当前时间或较早时间的所有数据。Neon 保留项目分支的七天历史作为预写日志(WAL)记录，实现基于时间点的恢复功能。

“这是一种非常安全的开发软件的方式。它给你一种类似于git的信心，可以随心所欲地处理你的分支，因为你始终可以从主分支、生产分支重置它。当特性开发完成时，你可以将更改推送到主分支。”他说。

它使用户能够:

- 瞬间备份数据库
- 在一次性的测试专用分支中运行测试
- 安全地在生产环境中尝试自动化数据库迁移
- 隔离地运行分析或机器学习工作负载

或者，如果你决定放弃你所做的一切，由于它是无服务器的，这不会产生任何成本。 无服务器意味着开发人员不必担心调整应用程序资源的大小，他们只需添加一个指向数据库的连接字符串。 并且通过按消耗计费，Neon可以缩减到零。

该公司在其云服务上免费提供一个项目，最多10个分支，每个分支3GB存储和1GB RAM的共享计算实例。

12月，它宣布了[分支重置](https://neon.tech/blog/announcing-branch-reset)功能，该功能使您可以使用主分支的最新模式和数据保持分支更新。 它的作用类似于git工作流中的`git reset-hard parent`。 需要注意的是，它可能会覆盖分支中的一些工作。

它还为Neon Pro计划的用户引入了[IP允许功能](https://neon.tech/blog/restrict-access-to-your-neon-database-with-ip-allow)，为数据添加了另一层安全保护。它使您可以限制对分支的访问，只允许您指定的IP地址。您可以创建一个默认应用于所有分支的IP白名单，也可以仅将其应用于项目的主分支。

## 向量也支持

虽然Postgres已有35多年的历史，但它[仍然很受欢迎](https://thenewstack.io/from-a-fan-on-the-ascendance-of-postgresql/)。根据[Stack Overflow 2023开发者调查](https://survey.stackoverflow.co/2023/)，它是45.5%的开发者[选择的数据库](https://thenewstack.io/postgresql-takes-a-new-turn/)，而MySQL为41%。不过，它在[DB-Engines上的排名仅为第4](https://db-engines.com/en/ranking)，而MySQL排第2。

之前与创立实时数据分析平台[SingleStore](https://thenewstack.io/singlestore-offers-fast-vector-processing-for-real-time-ai/)(MemSQL)的Shamgunov于2022年与[Postgres资深人士](https://github.com/kelvich)[Heikki Linnakangas](https://www.linkedin.com/in/heikki-linnakangas-6b58bb203/)和[Stas Kelvich](https://github.com/kelvich)共同创立了Neon。云提供商Vercel于5月[宣布与Neon建立合作关系](https://thenewstack.io/vercel-offers-postgres-redis-options-for-frontend-developers/)，与在线集成开发环境[Replit](https://replit.com/)的类似合作正在推动Neon的增长。

它在8月宣布完成了4600万美元的B轮融资，使其总融资达到1.04亿美元。

该公司还积极参与了Postgres相似性搜索扩展[pgvector](https://github.com/pgvector/pgvector)的开发。例如，Linnakangas对项目做出了几项贡献，以提高性能，Shamgunov说。作为Postgres提供商，该公司的观点是不需要单独的向量数据库。

与此同时，与[Postgres边缘平台pgEdge一样](https://thenewstack.io/extension-pgvector-makes-pgedge-a-distributed-vector-database/)，Neon也超越了pgvector所提供的功能，使用其自主研发的称为[pg_embedding](https://github.com/neondatabase/pg_embedding)的向量扩展的额外算法集来帮助进一步提高准确性。它使用Postgres和分层可导航小世界算法提供向量相似性搜索，以逼近最近邻搜索。

它的[逻辑复制也处于测试阶段](https://neon.tech/blog/change-data-capture-with-serverless-postgres)。
