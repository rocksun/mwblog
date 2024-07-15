# 使用此新的开源扩展，使 Pgvector 比 Pinecone 更快且便宜 75%

![使用此新的开源扩展，使 Pgvector 比 Pinecone 更快且便宜 75% 的特色图片](https://cdn.thenewstack.io/media/2024/07/65712007-1.cover_image_postgresql-vs-pinecone-1024x585.jpg)

我经常听到开发人员在构建 AI 应用程序时问：“我需要一个[独立的向量数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)吗？还是我可以使用我已有的通用数据库？”

虽然像[PostgreSQL](https://thenewstack.io/postgresql-takes-a-new-turn/)这样的通用数据库因其熟悉度和[pgvector](https://github.com/pgvector/pgvector)等扩展而越来越受欢迎，用于向量存储和搜索，但选择使用专用向量数据库（如[Pinecone](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/)）的一个理由是其性能更好。其推理如下：专用向量数据库具有专门为存储和搜索大量向量数据而构建的数据结构和算法，因此与具有附加向量支持的通用数据库相比，它们提供了更好的性能和可扩展性。

我在[Timescale](https://www.timescale.com)（PostgreSQL 云数据库公司）的团队构建了[pgvectorscale](https://github.com/timescale/pgvectorscale/)，旨在使 PostgreSQL 成为更好的 AI 数据库，并挑战 PostgreSQL 和 pgvector 对于工作负载而言性能不佳的观念。Pgvectorscale 将专门用于大规模向量搜索和存储的数据结构和算法作为扩展引入 PostgreSQL，帮助提供与专用向量数据库（如 Pinecone）相当甚至更好的性能。

## Pgvectorscale：在 PostgreSQL 上针对大型向量工作负载实现高性能、经济高效的扩展

[Pgvectorscale](https://github.com/timescale/pgvectorscale/?ref=timescale.com) 是一个开源 PostgreSQL 扩展，它建立在 pgvector 之上，能够实现更高的性能和可扩展性（继续阅读以了解实际数字）。使用 pgvector 和 pgvectorscale，开发人员可以构建更可扩展的 AI 应用程序，从更高性能的嵌入搜索和经济高效的存储中受益。

Pgvectorscale 在[开源 PostgreSQL 许可证](https://github.com/timescale/pgvectorscale/blob/main/LICENSE?ref=timescale.com)下获得许可，它通过利用 pgvector 数据类型和距离函数来补充 pgvector，进一步丰富了 PostgreSQL 生态系统，用于构建 AI 应用程序。虽然 pgvector 是用 C 编写的，但 pgvectorscale 扩展是用 Rust 编写的，为社区提供了一种新的途径来为 PostgreSQL 中的向量支持做出贡献。

Pgvectorscale 在 pgvector 的基础上进行了两项关键创新：

**StreamingDiskANN 向量搜索索引：**StreamingDiskANN 克服了内存中索引（如 HNSW（分层可导航小世界））的局限性，通过将索引的一部分存储在磁盘上，使其在向量工作负载增长时更经济高效地运行和扩展。受微软研究的启发，然后由 Timescale AI 研究人员改进，pgvectorscale 的 StreamingDiskANN 索引优化了 pgvector 数据，以实现低延迟、高吞吐量搜索，而不会牺牲高精度。将索引存储在磁盘上的能力极大地降低了存储和搜索大量向量数据的成本，因为 SSD 比 RAM 便宜得多。

**统计二进制量化 (SBQ)：**由 Timescale 的研究人员开发，这种技术通过提高使用量化来减少向量存储所需空间时的精度来改进标准二进制量化技术。

## Pgvector 与 Pinecone：pgvectorscale 的性能影响

让我们简要介绍一下 pgvectorscale 帮助 PostgreSQL 获得与专用向量数据库（如 Pinecone）相当甚至更好的性能的说法。

为了测试 pgvectorscale 的性能影响，我们将 PostgreSQL 与 pgvector 和 pgvectorscale 的性能与 Pinecone（被广泛认为是专用向量数据库的市场领导者）进行了比较，使用了一个包含 5000 万个 Cohere 嵌入（每个嵌入 768 维）的数据集进行[基准测试](https://www.timescale.com/blog/pgvector-vs-pinecone/)。

带有 pgvector 和 pgvectorscale 的 PostgreSQL 在 99% 的召回率下，以 28 倍的 p95 延迟和 16 倍的查询吞吐量，优于 Pinecone 的存储优化索引 (s1)，用于近似最近邻查询。

此外，带有 pgvectorscale 的 PostgreSQL 在相同数据集上，在 90% 的召回率下，实现了比 Pinecone 的性能优化索引 (p2) 低 1.4 倍的 p95 延迟和高 1.5 倍的查询吞吐量。p2 pod 索引是 Pinecone 建议您在需要最佳性能时使用的索引，令我们惊讶的是，pgvectorscale 仍然帮助 PostgreSQL 超越了它！
这种令人印象深刻的性能，加上 PostgreSQL 可信赖的可靠性和 [持续的演进](https://www.timescale.com/blog/making-postgresql-a-better-ai-database)，清楚地表明：使用 pgvector 和 pgvectorscale 在 PostgreSQL 上构建是开发人员创建高性能、可扩展 AI 应用程序的明智之选。

成本效益同样引人注目。使用 pgvector 和 pgvectorscale 自托管 PostgreSQL 比 Pinecone 便宜 75-79%。在 AWS EC2 上自托管 PostgreSQL 每月约花费 835 美元，而 Pinecone 的存储优化索引 (s1) 每月花费 3,241 美元，性能优化索引 (p2) 每月花费 3,889 美元。

这一结果反驳了 [说法](https://www.pinecone.io/blog/pinecone-vs-pgvector/?ref=timescale.com)，即 PostgreSQL 和 pgvector 易于上手，但对于 AI 应用程序来说不可扩展或性能不佳。借助 pgvectorscale，构建 GenAI 应用程序的开发人员可以享受为向量搜索量身定制的性能，而无需放弃功能齐全的 PostgreSQL 数据库和生态系统的优势。

这些优势很多。选择独立的向量数据库意味着您将失去通用数据库中存在的所有数据类型、事务语义和操作功能，而这些功能通常对于部署生产应用程序是必需的。PostgreSQL 还提供了丰富的工具和生态系统——例如用于查询统计信息的 pg_stat_statements、用于调试慢速查询的 EXPLAIN 计划，以及用于 AI 数据堆栈中所有其他技术的众多连接器、库和驱动程序。

如果您想详细了解 pgvectorscale 的性能，这里有一个 [技术](https://www.timescale.com/blog/how-we-made-postgresql-as-fast-as-pinecone-for-vector-data/)解释，说明 StreamingDiskANN 和统计二进制量化是如何工作的。本 [pgvector 与 Pinecone 比较博客文章](https://www.timescale.com/blog/pgvector-vs-pinecone) 中还详细介绍了基准测试方法和结果。

## PostgreSQL 作为 AI 应用程序的基础
数据库对于构建 AI 应用程序至关重要，**我认为未来所有应用程序都将是 AI 应用程序。**利用 LLM 的 AI 应用程序的兴起也意味着开发人员对数据库的要求更高。好消息是，PostgreSQL 凭借其丰富的生态系统和社区，正在不断发展以满足不断变化的开发人员需求。

我相信 PostgreSQL——凭借其丰富的生态系统、多种数据类型支持和经过实战检验的可靠性——是未来数据的基石。我曾听到过一个简洁的表达：“PostgreSQL 用于一切”。未来，一切都会融入 AI。

在 Timescale，我们相信 [PostgreSQL 是未来数据的基石](https://www.timescale.com/blog/postgres-for-everything/)。PostgreSQL 生态系统的强大之处在于它成为专业开发人员和一般开发人员最喜欢的数据库。

![](https://cdn.thenewstack.io/media/2024/07/933ebf28-4.postgres-for-everything_so-2023-1.png)
根据 2023 年 Stack Overflow 开发者调查，PostgreSQL 是专业开发人员和一般开发人员中最受欢迎的数据库选择。

**我认为 PostgreSQL 是未来 AI 应用程序的理想基础。**pgvector、pgvectorscale 和 [pgai](https://github.com/timescale/pgai) 等扩展降低了在 AI 应用程序中采用和扩展 PostgreSQL 的门槛——无论是搜索、RAG 还是代理——因为它们消除了采用独立向量数据库的需要，并简化了数据架构。

随着 PostgreSQL for AI 生态系统的不断发展，我希望更多开发人员能够用 PostgreSQL 在其 AI 数据堆栈中取代复杂、脆弱的数据架构（处理多个数据库），从而获得坚如磐石的基础、多功能扩展和简单易用的优势。

## 立即使用 PostgreSQL 构建您的 AI 应用程序
[Pgvector](https://github.com/pgvector/pgvector)、[pgvectorscale](https://github.com/timescale/pgvectorscale/) 和 [pgai](https://github.com/timescale/pgai) 都是根据 [PostgreSQL 许可证](https://github.com/timescale/pgvectorscale/blob/main/LICENSE?ref=timescale.com) 开源的，您可以立即在您的 AI 项目中使用它们。
您可以在 Github（上面链接）上找到安装说明。如果您正在寻找托管数据库，您可以在 [Timescale 的云 PostgreSQL 平台](https://console.cloud.timescale.com/signup) 上访问所有三个扩展。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)