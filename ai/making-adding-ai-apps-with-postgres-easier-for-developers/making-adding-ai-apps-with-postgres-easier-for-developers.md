
<!--
title: 让开发者更轻松地使用Postgres添加AI应用
cover: ./cover.png
-->

借助 Timescale 的 AI 工具套件，您可以创建和管理向量嵌入以及关系数据，而无需外部工具或额外的基础设施。

> 译自 [Making Adding AI Apps with Postgres Easier for Developers](https://thenewstack.io/making-adding-ai-apps-with-postgres-easier-for-developers/)，作者 Susan Hall。

随着 AI 和[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms)的兴起，被要求创建 AI 应用程序的开发者可能会感到自己被带入了一个陌生的领域。开源 PostgreSQL 数据库供应商 [Timescale](https://www.timescale.com/go/best-postgres-db) 对此的解决方案是一套工具，旨在帮助没有 AI 背景的开发者构建企业级应用程序。

其 [pgai 工具套件](https://github.com/timescale/pgai) 的最新成员是 [pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md)，它将整个嵌入过程集成到 [Postgres](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/) 中，允许开发者在关系数据 alongside 创建、存储和管理向量嵌入，而无需外部工具或额外的基础设施。

所有工具都构建于 [pgvector](https://github.com/pgvector/pgvector) 之上，这是一个支持在 Postgres 中进行向量搜索的开源扩展。

虽然许多 Postgres 供应商在竞相提供 AI 功能的过程中[添加了 pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/)，但 Timescale 认为这不足以帮助刚接触 AI 的开发者入门。

“如果你想想谁在真正构建 AI 应用程序，实际上是软件开发者，应用程序开发者，”Timescale 的 AI 和开发者产品负责人 Avthar Sewrathan 解释道。虽然他们有构建生产系统的经验，但他们可能没有 AI 和 ML 背景，而这些传统上是数据科学家或研究工程师的领域，但他们不一定是全栈工程师或后端工程师。

“Vectorizer 真正处理的是，‘好吧，我们在 Postgres 中拥有向量搜索功能，但是你如何开始呢？然后，一旦你创建了嵌入，你如何才能真正拥有一个生产应用程序，以及随之而来的需求是什么？’” 他说道。

## 自动创建嵌入

为了总结 pgai Vectorizer，他解释说：“它通过一个 SQL 查询将嵌入创建置于自动驾驶状态，并且所有操作都在 Postgres 中进行。[它自动化]了从源数据创建嵌入的过程，并允许团队基本上设置好之后就不用管了。

随着新数据添加到他们的表中，嵌入将自动创建，并且他们避免了所有关于数据同步和确保嵌入扩展的问题，因为一切都在后台自动同步，从而减少了开发团队原本需要自己完成的工作。”

他说，客户越来越多地询问与 AI 相关的操作任务，这使其成为一个日益受到关注的领域。

使用 pgai Vectorizer，开发者可以：

* 在他们熟悉的同一 PostgreSQL 数据库平台上管理 AI 应用程序的所有数据——向量、元数据、事件数据。
* 自动实时同步数据更改到向量嵌入。
* 无需更改代码或创建自定义数据管道即可轻松切换嵌入模型，以便进行快速测试和实验。
* 跟踪模型版本并在推出期间确保向后兼容性，以实现平滑过渡。

“pgai Vectorizer 是一款颠覆性产品。它承诺简化我们的整个 AI 工作流程，从嵌入创建到实时同步，使我们能够更快、更高效地交付 AI 应用程序，”MarketReader 的首席技术官 Web Begole 说道。“通过将所有内容直接集成到 PostgreSQL 中，pgai Vectorizer 消除了对外部工具和专业知识的需求，使我们的团队更容易专注于创新而不是基础设施。”


> “如果你想构建一个生产级应用程序，实际上需要克服非常棘手的工程挑战。”  
>
> —Timescale 的 AI 产品负责人 Avthar Sewrathan

Sewrathan 指出了 pgai Vectorizer 可以为开发者替代的四项任务：

- **构建 ETL 管道** ——接收源文档或图像，协调对 OpenAI 或其他模型的调用并创建实际嵌入。
- **分块和格式化** ——“在创建嵌入之前，你需要将[数据]转换为正确的格式，并将其大小调整为适合嵌入模型的标记限制。所以这是我们帮你完成的另一项任务。你只需用一行代码进行配置，然后它就会在后台自动运行，”Sewrathan 说。
- **扩展和管理嵌入创建管道** ——“大多数开发人员可以用半小时编写一个[Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/)嵌入创建脚本，但要拥有一个能够实际扩展并处理 OpenAI 速率限制、在创建数十万个嵌入时处理排队的脚本，这就是我们的系统开箱即用的功能。它取代了这些用于更新和同步的排队系统。”
- **同步** ——“当你构建 AI 应用程序时，你必须编写代码来检查，‘好的，在我的向量数据库中，这些嵌入已创建。’[但是]我的关系数据库中是否有正确的元数据？或者，例如，假设你的关系数据库中有新文档，你需要检查是否创建了相应的向量。这种代码执行我所说的同步，比如检查陈旧性，”Sewrathan 说。你可以保证你的嵌入是最新的，如果不是，你会收到通知。

Sewrathan 说：“我认为当今业界看到的很多情况是，数据库添加了向量搜索功能来取代向量数据库，并认为这足以使它们成为构建 AI 应用程序的重要组成部分。但我们认识到——在过去一年半多的时间里，我们与数百名开发人员进行了交谈，我们一直在构建这个项目——我们发现向量搜索只是构建 AI 系统的一部分。”

他说：“如果你想构建一个生产级应用程序，实际上需要克服非常棘手的工程挑战。因此，我们的整个论点是，就 pgai 而言，我们能否为开发人员提供一套工具，不仅可以解决向量搜索问题，还可以扩展你的 AI 系统，解决嵌入创建、更新、数据同步、嵌入陈旧性以及在数据库内部[访问]模型的能力。”


## 最初只是 pgai

去年 6 月推出第一个工具时，该公司在一篇博文中表示：“简而言之，我们构建 pgai 是为了帮助[让更多 PostgreSQL 开发人员成为 AI 工程师](https://www.timescale.com/blog/pgai-giving-postgresql-developers-ai-engineering-superpowers/)。”

[pgai](https://github.com/timescale/pgai?tab=readme-ov-file) 是 Postgres artificial intelligence 的缩写，旨在简化使用 PostgreSQL 构建语义搜索、检索增强生成 (RAG) 和其他 AI 应用程序的过程。

> “简而言之，我们构建 pgai 是为了帮助让更多 PostgreSQL 开发人员成为 AI 工程师。”  
>
> ——Timescale 博文

“pgai 通过将嵌入存储在 pgvector 数据类型中，并使用 Python 和 PL/Python 在 PostgreSQL 数据库中与模型 API 交互来补充 pgvector，”其 GitHub 页面解释道。它可以在现有关系数据上执行分类、摘要和数据增强任务。它直接在数据库中创建嵌入，跳过了将它们保存到数据库的任务。

pgai 和 pgai Vectorizer 最初仅支持 [OpenAI](https://github.com/timescale/pgai/blob/main/docs/openai.md)，现在支持 [Ollama](https://github.com/timescale/pgai/blob/main/docs/ollama.md)、[Anthropic](https://github.com/timescale/pgai/blob/main/docs/anthropic.md) 和 [Cohere](https://github.com/timescale/pgai/blob/main/docs/cohere.md)。该公司已宣布计划支持更多模型，包括 Claud 和 Hugging Face。

## 改进的扩展性

同样在 6 月推出的 [pgvectorscale](https://github.com/timescale/pgvectorscale) 旨在处理[大规模、高性能的 AI 用例](https://www.timescale.com/blog/pgvector-is-now-as-fast-as-pinecone-at-75-less-cost/)。

“Pgvectorscale 将用于大规模向量搜索和存储的专用数据结构和算法作为扩展引入 PostgreSQL，帮助提供与 [Pinecone](https://www.pinecone.io/?utm_content=inline+mention) 等专用向量数据库相当甚至更优的性能，”该公司表示。

它添加了一个受 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 的 [DiskANN](https://github.com/microsoft/DiskANN) 算法启发的 StreamingDiskANN 向量搜索索引，通过将部分索引存储在磁盘上来解决 HNSW（分层可导航小世界）等内存索引的局限性。由于固态硬盘比 RAM 便宜得多，因此将索引存储在磁盘上可以节省大量成本。
它还开发了统计二进制量化 (SBQ)，以在采用[标准二进制量化技术](https://jkatz05.com/post/postgres/pgvector-scalar-binary-quantization/)压缩以节省存储空间的同时提高准确性。

虽然 pgvector 是用 C 编写的，但 pgvectorscale 是用 [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) 使用 [PGRX 框架](https://github.com/pgcentralfoundation/pgrx) 开发的，从而为另一个快速增长的社区增加了访问权限。

## 全开源

这种压缩意味着更低的基礎設施成本，但 Sewrathan 也指出了其他成本节约。

“我们认为你实际上可以运行更少的自定义代码，这节省了大量的工程时间，实际上允许更小的团队来完成这项工作。[以前你可能需要] 10 个开发人员；现在你只需要两三个，因为很多事情都是自动化的，并且通过 Vectorizer 为你开箱即用，”他说。

Sewrathan 在[The New Stack 的一篇文章](https://thenewstack.io/make-pgvector-faster-than-pinecone-and-75-cheaper-with-this-new-open-source-extension/)中还提到了它的基准测试，将它的 pgvector 版本与 Pinecone 进行了比较，得出的结论是，Postgres 扩展不仅成本低得多，而且比独立的向量数据库更快。

Sewrathan  称赞流行的[久经考验的 PostgreSQL](https://thenewstack.io/from-a-fan-on-the-ascendance-of-postgresql/)，写道：

“选择一个独立的向量数据库将意味着你将失去通用数据库中存在的全系列数据类型、事务语义和操作特性，而这些特性通常是部署生产应用程序所必需的。”

pgai 工具是开源的，但 Timescale 也将其作为完全托管的数据库服务的一部分提供。
