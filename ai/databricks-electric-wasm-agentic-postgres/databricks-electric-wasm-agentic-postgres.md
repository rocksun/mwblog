<!--
title: Databricks收购Electric，为每个AI智能体赋予专属Postgres数据库
cover: https://cdn.thenewstack.io/media/2026/08/ef9692c3-andania-humaira-ep5isucpu98-unsplash-scaled.jpg
summary: Databricks宣布收购初创公司Electric，旨在将其基于WASM的Postgres项目PGlite及同步引擎整合进Neon数据库服务。此举是为了应对AI智能体开发中对临时、轻量级数据库的爆发式需求，通过提供高效的数据库分支与同步机制，支持智能体实现类似代码分支的开发流程，从而降低AI应用开发成本。
-->

Databricks宣布收购初创公司Electric，旨在将其基于WASM的Postgres项目PGlite及同步引擎整合进Neon数据库服务。此举是为了应对AI智能体开发中对临时、轻量级数据库的爆发式需求，通过提供高效的数据库分支与同步机制，支持智能体实现类似代码分支的开发流程，从而降低AI应用开发成本。

> 译自：[Databricks acquires Electric to give every AI agent its own Postgres database](https://thenewstack.io/databricks-electric-wasm-agentic-postgres/)
> 
> 作者：Frederic Lardinois

Databricks周二[宣布](https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes)收购Electric，这是一家开发了基于WASM的Postgres项目PGlite以及Electric同步引擎的初创公司，此举正值智能体应用改变开发人员使用数据库方式之际。

Electric团队将加入Neon，这是Databricks去年以约10亿美元收购的无服务器Postgres公司，也是其[Lakebase](https://thenewstack.io/lakebase-is-databricks-fully-managed-postgres-database-for-the-ai-era/)数据库服务的基础。

双方未披露交易条款。

## Databricks收购了什么

[PGlite](https://pglite.dev/)是一个运行在WebAssembly (WASM) 中的完整Postgres数据库。它可以在浏览器、Node.js进程或智能体用于执行代码的沙箱中运行。它支持动态加载扩展，包括Postgres首选的向量扩展pgvector。

据两家公司称，PGlite的每周下载量在过去一年中从100万次增长到1300万次。

## Electric核心的同步引擎

尽管如此，Electric同步引擎才是Databricks对其感兴趣的核心。该引擎维护一个中央Postgres数据库，然后可以与浏览器标签页、移动应用或智能体进行近乎实时的同步。正如Databricks指出的那样，这是Figma或Google Docs的多人协作模型，但应用于Postgres以及使用它的智能体。

Neon团队在[自己的公告](https://neon.com/blog/electric-joins-neon)中指出，“冲突解决、部分复制和重新连接逻辑等复杂问题使得实时同步很难从零开始构建。”这就是为什么Databricks可能选择收购Electric，而不是尝试自己从头构建。

至于Electric的未来，该公司的创始人James Arthur和Valter Balegas[写道](https://electric.ax/blog/2026/08/11/electric-joining-databricks)，“我们之前开源的所有内容都将保持开源。”这涵盖了同步引擎、PGlite、Durable Streams和TanStack DB。

然而，Electric的托管服务并未在交易中保留。“Electric Cloud正在关闭，”创始人们表示。“云用户将需要自行托管或迁移到其他提供商。”

这笔交易也延续了Databricks一系列的数据库收购动作，其中包括Neon本身，以及最近的事务处理初创公司[Mooncake](https://thenewstack.io/mooncake-brings-databricks-rich-transactional-processing/)。

## 一个仅存活10秒的数据库

正如Databricks团队所言，传统的非智能体应用在多个客户端之间共享一个数据库，而该数据库是技术栈中最持久的部分。但智能体工作负载改变了这一点。

在关于智能体开发如何改变数据库的[近期文章](https://www.databricks.com/blog/how-agentic-software-development-will-change-databases)中，Databricks的Ippokratis Pandis、Nikita Shamgunov和Reynold Xin写道，智能体现在在Lakebase上创建的数据库数量大约是人类用户的四倍。他们还强调，平均每个项目现在携带大约10个数据库分支，并且有些项目运行超过500次分支迭代。

对于Lakebase上的某些应用类型，平均数据库计算的存活时间现在不到10秒。

事实证明，智能体喜欢像分支代码一样分支数据库，这是一种Neon[围绕其架构构建](https://thenewstack.io/neon-branching-in-serverless-postgresql/)的模式。

在实践中，一个编程智能体启动一个沙箱，在其中实例化PGlite，针对该数据库进行构建和测试，然后要么丢弃整个内容，要么将结果与（在Databricks的上下文中）Lakebase分支进行同步。由于Lakebase[将存储与计算分离](https://thenewstack.io/new-oltp-postgres-with-separate-compute-and-storage/)并将其数据以Postgres页面格式保存在对象存储中，创建该分支是一个相对廉价的写时复制元数据操作。

“随着编程智能体将创建成本降至零，”Neon团队写道，“应用程序的数量呈爆炸式增长，而且其中大多数都很小。”数据库服务器，即使是扩展到零的无服务器服务器，也为最小可行应用运行成本设定了下限。“如果每个应用都需要固定的最小计算量，你就无法拥有一个丰富的时代，”文章认为。

## “同一理念的两个部分”

值得注意的是，PGlite并非起源于Electric。相反，它最初是Neon联合创始人Stas Kelvich的一个实验，他将Postgres编译为WASM，看看它是否可以在客户端运行。Electric接手了这项工作并将其变成了一个生产级项目。“该代码库成了PGlite的基础，”Arthur和Balegas写道。

正如Databricks的公告所指出的，这现在“重新结合了同一理念的两个部分”。