# 向量数据库基础：HNSW

![向量数据库基础：HNSW](/blog/content/images/size/w2000/2024/08/A-Beginner-s-Guide-to-Vector-Embeddings--1--copy.png)

在机器学习和人工智能系统中，向量数据库是存储和搜索海量数据的必备工具。[想象一下地图上的点](https://www.timescale.com/learn/postgresql-extensions-pgvector?ref=timescale.com)，每个点都有其独特的坐标。在数据库的语境中，这些“坐标”帮助我们快速准确地找到所需的信息。

[Pgvector](https://github.com/pgvector/pgvector?ref=timescale.com) 是 PostgreSQL 的一个扩展，允许在数据库中存储和检索向量数据。它支持 HNSW（分层可导航小世界）索引，这使得对高维向量数据进行快速近似最近邻搜索成为可能。HNSW 索引至关重要，因为它们可以高效地找到相似的向量，而无需扫描整个数据集。这在处理大量高维向量数据时非常有用，因为扫描所有向量会变得很慢。

本文的主要目的是解释 HNSW 索引，重点介绍它们为何优于旧方法以及如何将它们与 pgvector 一起使用。我们针对任何使用向量数据库、开发 AI 应用程序或对现代数据搜索感兴趣的人定制了本指南。我们还将简要介绍这项技术如何与 TimescaleDB 集成，并展示它如何增强现实世界应用程序中大规模数据管理功能。

## Pgvector 上的 HNSW 索引

Pgvector 引入分层可导航小世界索引，是其高效管理向量数据库能力的绝佳补充。这种方法源于 Malkov 和 Yashunin 的[基础工作](https://arxiv.org/abs/1603.09320?ref=timescale.com)，在近似最近邻搜索 (ANN) 领域开辟了新天地，提供了一种新颖的基于图的框架。

该框架对于高维数据尤其重要，因为传统索引由于每个维度增加带来的复杂性呈指数级增长，难以保持效率。

### 探索近似最近邻搜索 (ANN)

近似最近邻搜索 (ANN) 是一种计算问题，其重点是在数据集中找到与给定查询点最接近的数据点。与精确最近邻搜索不同，ANN 允许在搜索精度和计算效率之间进行权衡，承认在高维空间中，精确匹配在计算时间和资源方面可能过高。

ANN 可以分为三个主要类别，每个类别都由其基础数据结构定义：树、哈希和图。树以层次结构组织数据，允许在每个节点进行二元决策以导航到查询点附近。哈希将数据点转换为低维空间中的代码，将相似的项分组到同一个桶中，以便更快地检索。

图（HNSW 使用的）创建了一个点网络，其中边根据相似性度量连接邻居。在这些方法中，HNSW 由于使用多层图结构而脱颖而出，该结构有效地解决了“维数灾难”问题——这个问题会影响高维数据空间，使传统搜索方法效率低下，通常不可行。

HNSW 的分层图方法使它能够进行近似搜索，而不是追求精确匹配，从而显着减少计算开销，而不会大幅降低精度。

这种方法承认处理高维数据的固有局限性，强调实用性和性能而非完美。它巧妙地通过其层次结构层逐步缩小搜索区域来导航数据空间，确保搜索保持快速和相关。

### 区分 HNSW 和 IVF

当将 HNSW 与倒排文件 (IVF) 索引方法进行比较时，HNSW 的一个突出特点是它能够适应动态数据集——它可以高效地管理插入和删除，而无需完全重建索引。这种动态特性对于不断发展的应用程序至关重要，这些应用程序需要索引与它所代表的数据一样灵活。虽然 IVF 索引在使用中功能强大，但它们通常需要完全重建才能适应新数据或删除旧数据，这可能很耗时，并会阻碍实时搜索功能。HNSW 的设计绕过了这种限制，为数据不断变化的数据库提供了更可持续的解决方案。

## HNSW 如何工作？

要了解 HNSW 算法的工作原理，需要仔细研究其原理、它从跳跃列表中获得的灵感以及它如何引入长边来克服传统图索引挑战。

### HNSW 的原理
# HNSW 利用图结构来组织数据，以反映数据点之间固有的相似性，形成可导航的小世界网络。指导这种结构的原则是最小化图中任意两点之间的路径长度，确保每个点都可以通过少量跳跃从任何其他点到达。这是通过将数据组织成多个层来实现的，每个后续层都提供了对数据的更精细的视图。

## 受跳跃列表启发

跳跃列表是一种用于存储排序项目列表的数据结构，它具有高效的搜索、插入和删除操作，它启发了 HNSW 的分层设计。在跳跃列表中，元素被组织成层，较高的层提供快捷方式，以便快速遍历列表。

类似地，HNSW 构建了多层图，其中顶层包含较少的节点，充当快速导航数据空间的高速公路，在深入更密集的较低层进行细粒度搜索之前，将搜索引导到更接近目标的位置。

## 引入“长”边

在 HNSW 的上下文中，“长”边是指图的顶层中的连接，这些连接跨越数据空间中的大距离，绕过许多中间节点。这些边对于实现小世界属性至关重要，允许快速跳跃整个图。

当搜索查询从顶层向下移动到底层时，边的长度会减小，搜索区域变得越来越局部化，从而能够以最小的计算开销精确识别最近的邻居。

## 解决传统图索引挑战

传统的图索引技术通常难以应对维数灾难，在高维空间中，数据点之间的距离变得不那么有意义。这使得有效地组织和搜索数据变得具有挑战性。它们还存在可扩展性差和难以更新索引的问题，因为新的数据点被添加或删除。

HNSW 通过其多层分层方法解决了这些问题。它允许通过在每一层减少维数并动态调整图的结构来实现高效搜索，而无需完全重建。

这种设计提高了高维空间中的搜索效率，并支持增量更新，使 HNSW 特别适合数据点频繁变化的动态数据集。

![表示 HNSW 分层结构的图表](https://www.timescale.com/blog/content/images/2024/08/Untitled-design--4-.png)

总之，HNSW 优化了组织和搜索高维数据的策略，利用了可导航的小世界网络和跳跃列表的原理，引入了长边以促进快速导航。这种结构显着克服了传统图索引技术的局限性，为近似最近邻搜索提供了一种可扩展、动态且高效的解决方案。

## 如何创建 HNSW？

创建 HNSW 索引涉及几个步骤，重点是构建分层结构，使用其多层方法构建图，以及实现的实际方面。

### 构建分层结构

HNSW 的分层结构从根本上来说是一组分层图，每个图都以不同的抽象程度表示数据集。顶层具有最少的节点，充当搜索查询的入口点，便于快速遍历数据空间。每个后续层都增加了密度，添加了更多细节，直到到达底层，其中包含所有数据点。

**初始化**: 从空结构开始。图最初没有节点，第一个插入的节点成为顶层的唯一成员。**层分配**: 对于每个新的数据点，确定其在层次结构中的最大层 l。这通常使用概率方法完成，例如抛硬币或从几何分布中抽取，以确保节点数量的预期值随着层高度的增加而减少。**连接节点**: 将新节点插入到其分配的最大层中的每一层。在每一层中，将节点连接到其最近的邻居。节点在每一层中具有的连接数或边数可以是固定的或可变的，受参数的影响，例如图的所需稀疏度或密度。

![表示如何构建分层结构的图表](https://www.timescale.com/blog/content/images/2024/08/HNSW-vector-database-basics_building-structure.png)

*构建分层结构*

### 图构建

图构建使用数据点填充分层结构，并根据相似性或接近度建立连接。
**查找邻居**: 识别当前层中插入的新节点的最近邻居。这可能涉及搜索整个图或使用启发式方法来限制搜索空间。最初，搜索从随机选择的节点或随着图增长而更新的指定入口点开始。**更新连接**: 一旦识别出层中的最近邻居，就会建立新节点的连接。这可能需要更新邻居的连接，以确保图保持可导航且小世界属性得以保留。**层下降**: 对节点最大层以下的每一层重复此过程，随着图变得更密集，细化对最近邻居的搜索。这种迭代方法确保每个节点都以最佳方式放置在层次结构中，从而保持高效的导航。

![表示图构建过程的图表](https://www.timescale.com/blog/content/images/2024/08/HNSW-vector-database-basics_graph-construction.png)

### 实现

HNSW 的实际实现可能因具体用例和性能要求而异。但是，一些常见的考虑因素包括：

**语言和库选择**: 实现可以用各种编程语言创建。C++ 经常被选择，因为它在高级可用性和对内存和性能的低级控制之间取得了平衡。像 `nmslib` 和 `faiss` 这样的库可以提供优化后的数据结构和算法，以提高性能。**内存管理**: 尤其对于大型数据集，高效的内存使用至关重要。这涉及为存储节点和边选择适当的数据结构以及管理层次结构。**并行化**: 为了加快构建和查询过程，HNSW 实现可以利用并行计算技术。这包括并行化最近邻居的搜索和节点的插入，以及管理可能出现的并发问题。

在实现 HNSW 时，对这些领域的关注可以显著影响索引的性能和可扩展性，使其适用于高维空间中搜索和数据检索的广泛应用。

## HNSW 方法：优点和挑战

HNSW 索引算法带来了几个优点和挑战。了解这些可以帮助有效地利用 HNSW 进行向量数据库管理和搜索应用程序。

### 优点

**文档齐全**: HNSW 的一个重要优势是其强大的文档和支持其方法的大量研究。这个强大的基础有助于开发人员和研究人员了解、实现和优化算法以用于各种应用程序。**向量数据库中的首选索引**: HNSW 已成为众多向量数据库引擎的首选索引。它在高维向量空间搜索操作中的效率使其成为 AI、机器学习和类似领域中非常受欢迎的工具，在这些领域中，根据向量相似性快速检索信息至关重要。**可配置以实现高召回率和速度**: HNSW 提供出色的可配置性，允许对其进行调整以实现高召回率（检索最相关结果的能力），而不会显著影响搜索速度。这种平衡在搜索结果的准确性至关重要且需要快速获得结果的场景中特别有价值。

### 挑战

**内存密集型**: HNSW 的性能在很大程度上依赖于将索引完全存储在内存中。虽然有利于速度，但这种架构选择使 HNSW 更适合具有大量可用 RAM 的系统。随着数据集的增长，尤其是达到数千万个高维向量时，内存需求可能会成为限制因素。**随内存扩展，而不是磁盘**: 与有效利用磁盘空间的其他数据存储和索引方法不同，HNSW 的设计要求整个索引适合可用内存。这种特性可能会在为大型数据集扩展系统或在内存资源受限的环境中带来挑战。

## 在 Pgvector 中创建 HNSW 索引

将 HNSW 集成到您的项目中以实现高效的向量搜索功能可能出奇地简单，尤其是在使用像 AI 和向量这样的工具时[ Timescale Cloud](https://www.timescale.com/ai/?ref=timescale.com) 以及它在 SQL 和 Python 环境中的支持。

使用 Timescale Cloud，开发人员可以访问[ pgvector, pgvectorscale 和 pgai](https://www.timescale.com/blog/making-postgresql-a-better-ai-database/)—将 PostgreSQL 变成易于使用且高性能的向量数据库的扩展，以及完全托管的云数据库体验。

以下是如何在每个上下文中使用一行代码利用 HNSW，使您的向量数据库更强大、搜索效率更高，无论是在我们的云平台上还是使用开源版本。

### 使用 pgvector 在 Timescale 上使用 SQL 创建 HNSW 索引

```sql
CREATE EXTENSION IF NOT EXISTS pgvector;
CREATE TABLE my_table (
  id SERIAL PRIMARY KEY,
  embedding vector(128),
  ...
);
CREATE INDEX ON my_table USING ivfflat (embedding vector_hnsw_ip);
```
TimescaleDB is an extension of PostgreSQL designed to handle time-series data, events, and analytics. It also extends its capabilities to support vector operations through the pgvector extension. Implementing HNSW indexing for your vector data within a PostgreSQL database can significantly boost search performance.

Here's how to create an HNSW index for an embedding column of your table in SQL:

```sql
CREATE INDEX document_embedding_idx ON document_embedding USING hnsw(embedding vector_cosine_ops);
```

This command creates an HNSW index named `document_embedding_idx` for the `embedding` column of the `document_embedding` table, using [cosine similarity operations](https://en.wikipedia.org/wiki/Cosine_similarity?ref=timescale.com) (`vector_cosine_ops`). This index leverages the speed and accuracy of the HNSW algorithm to facilitate efficient nearest neighbor searches.

### Utilizing HNSW with the Timescale Library in Python
For those working within a Python environment, the Timescale Python library simplifies applying HNSW indexing to your vector data.

Here's how to create an HNSW index using the library:

```python
vec.create_embedding_index(client.HNSWIndex())
```

This line of code instructs the library to create an HNSW index on the vector data managed by the `vec` object.

For finer control over the indexing process, including adjusting algorithm parameters for better performance, you can specify additional options, such as:

```python
vec.create_embedding_index(client.HNSWIndex(m=16, ef_construction=64, ef_search=10))
```

This expanded example sets the `m`, `ef_construction`, and `ef_search` parameters to customize the HNSW index. Here, `m` controls the maximum number of connections for each element in the index, `ef_construction` adjusts the size of the dynamic list used during index construction for better accuracy, while `ef_search` influences the search time precision.

## Overcoming HNSW's Limitations
While HNSW is a preferred index in vector databases, its memory-intensive nature can be a hurdle for developers handling large datasets. This is where [pgvectorscale](https://github.com/timescale/pgvectorscale/?ref=timescale.com) shines, offering high performance without consuming disk space and memory.

By [adding StreamingDiskANN indexing to pgvector](https://www.timescale.com/blog/how-we-made-postgresql-as-fast-as-pinecone-for-vector-data/), pgvectorscale overcomes the limitations of in-memory indexes like HNSW. It stores parts of the index on disk, making it more cost-effective to run and scale as your vector workload grows. As SSDs are significantly cheaper than RAM, this drastically reduces the cost of storing and searching large amounts of vectors.
Pgvectorscale also supports streaming filtering, enabling accurate retrieval even when applying auxiliary filters during similarity searches. It adds Statistical Binary Quantization (SBQ) to pgvector, improving the accuracy of traditional quantization methods.

The result is an index that consumes less disk space and memory, leading to improved search performance and accuracy. [And all of this is a quarter of the cost of dedicated databases like Pinecone](https://www.timescale.com/blog/pgvector-vs-pinecone/).

The combination of [pgai](https://github.com/timescale/pgai?ref=timescale.com) (bringing AI workflows to PostgreSQL) with pgvectorscale and pgvector empowers developers to continue using the PostgreSQL they know and love, transforming it into a high-performance platform for vector workloads and building AI applications. [Learn how to get started today](https://www.timescale.com/ai?ref=timescale.com).

## Conclusion
In this article, we explored HNSW indexing, which enhances the efficiency and accuracy of ANNS in high-dimensional data spaces. Starting with its operational principles, we saw how HNSW excels in performance and flexibility.

By breaking down the process of building an HNSW index and highlighting its advantages and limitations, we aimed to provide a comprehensive understanding of its impact on vector database management. HNSW indexing offers a perfect blend of speed, precision, and ease of use, making it a preferred index for numerous applications, including AI, machine learning, and more.

Despite its memory-intensive nature and challenges in scaling large datasets, HNSW's strengths in facilitating fast and accurate searches are undeniable. For those ready to integrate HNSW into their projects, whether through SQL commands or the Python-based Timescale library, the process is both straightforward and powerful. With just a single line of code, you can unlock the potential of your vector data, enhancing the search capabilities of your applications.

Working with expanding datasets? [Install the pgvectorscale PostgreSQL extension](https://github.com/timescale/pgvectorscale/?ref=timescale.com) and start building more scalable AI applications with higher-performance embedding search and cost-effective storage.