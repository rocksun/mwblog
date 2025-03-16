<!--
title: 无需锁定的向量搜索：为什么开发者喜欢ClickHouse
cover: https://cdn.thenewstack.io/media/2025/03/ffa63a2b-data.jpg
summary: 告别昂贵专有**向量数据库**！**ClickHouse**凭高性能**OLAP**架构，轻松应对**AI**向量搜索。原生支持**Kafka**、**Spark**，无缝集成**Hugging Face**、**LangChain**，构建维基百科搜索引擎，毫秒级响应，告别厂商锁定，**ZSTD**压缩提速，解锁开源**云原生**新姿势！
-->

告别昂贵专有**向量数据库**！**ClickHouse**凭高性能**OLAP**架构，轻松应对**AI**向量搜索。原生支持**Kafka**、**Spark**，无缝集成**Hugging Face**、**LangChain**，构建维基百科搜索引擎，毫秒级响应，告别厂商锁定，**ZSTD**压缩提速，解锁开源**云原生**新姿势！

> 译自：[Vector Search Without the Lock-In: Why Devs Like ClickHouse](https://thenewstack.io/vector-search-without-the-lock-in-why-devs-like-clickhouse/)
> 
> 作者：Lewis DiFelice

如果你所在的开发团队正在参与任何类型的 [AI initiative](https://thenewstack.io/ai/)，你可能会发现自己被推向昂贵的、专有的[向量数据库](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/)。 这样的理由可能听起来很合理：用于向量搜索的专用解决方案*一定*比通用数据库更好。 但这种假设正导致团队陷入代价高昂的供应商锁定局面，然后他们意识到自己正在为可以从开源替代方案中获得的功能支付高昂的价格。

一些开源数据库——开发团队无需大量启动成本或痛苦的锁定周期即可采用的数据库——已经在向量搜索方面表现出色。[Apache Cassandra 5.0](https://www.instaclustr.com/blog/vector-search-in-apache-cassandra-5-0/)、PostgreSQL 和 OpenSearch 都是可靠的选择，但目前有一种新兴的替代方案特别值得开发者关注：[ClickHouse](https://clickhouse.com/)，这是一种开源数据库，它将高性能分析与一些非常令人印象深刻的向量搜索功能相结合。

[ClickHouse 的构建](https://thenewstack.io/clickhouse-rapidly-rivals-other-open-source-databases-in-active-contributors/)从一开始就是为了对大型数据集进行在线分析处理 (OLAP)。 事实证明，这个基础非常适合向量搜索操作，尤其是在大规模情况下。 虽然大多数向量数据库迫使团队为搜索和分析构建单独的基础设施，但 ClickHouse 可以无缝地处理这两者，使其在 AI 工作负载变得更加复杂时更具价值。

## 为什么 ClickHouse 在向量搜索中脱颖而出

ClickHouse 的列式存储架构最初是为分析工作负载而设计的，它也非常适合向量运算。 它可以提供跨海量数据集进行实时相似性搜索所需的性能。 分布式架构可以水平扩展，让你可以将工作负载分布在 CPU 核心和磁盘上，而无需通常与分布式向量数据库相关的复杂性。

但在我看来，它的集成故事让 ClickHouse 特别有吸引力。 它可以[通过对 Apache Kafka 和 Spark 的原生支持直接插入到现有数据管道中](https://www.instaclustr.com/support/documentation/clickhouse/useful-concepts/)，同时还可以与 Hugging Face 和 LangChain 等 AI 工具很好地配合使用。 与专有解决方案不同，你可以直接投入到向量运算中，而无需额外基础设施或许可证。 所有这些都可以在同一高性能架构上开箱即用。

## 使用 ClickHouse 构建维基百科搜索引擎

在深入研究代码之前，让我们先抛开术语：向量搜索的工作原理是将内容（如文本、图像或音频）转换为称为嵌入的数字列表。 将这些想象成坐标，可以标示出不同内容彼此之间的相似程度。 当你构建 AI 应用程序时——尤其是那些需要理解上下文或实时查找相关信息的应用程序——这些嵌入就是你的秘密武器。

让我们通过构建一些有用的东西来了解这在实践中是如何运作的：一个可以使用维基百科文章作为其知识库来回答问题的搜索引擎。

## 快速设置：使用预构建的嵌入快速启动

虽然你可以使用 Hugging Face 或 LangChain 生成自己的嵌入（我建议在生产中使用这种方法），但我将使用预构建的数据集来快速跟踪我们的示例。 Hugging Face 社区已经为数百万篇维基百科文章[创建了嵌入](https://huggingface.co/docs/datasets/en/index)，他们已经免费提供这些嵌入。 这使我们可以专注于核心任务：设置 ClickHouse 以进行向量搜索。

我将[使用一个数据集](https://huggingface.co/datasets/Cohere/wikipedia-22-12-simple-embeddings/tree/refs%2Fconvert%2Fparquet/default/train)，其中包括维基百科文本、嵌入向量和元数据值。 这些嵌入是 768 维向量（本质上是代表每篇文章内容的数字长列表）。 让我们逐步了解如何加载此数据并开始运行搜索。

## 从数据集到可用的搜索引擎：分步指南

首先，让我们检查一下我们正在处理的内容。 该数据集有几个关键列：

- `emb`: 嵌入向量（代表每篇文章的 768 个浮点数数组）
- `text`: 实际的维基百科文章内容
- `title`: 文章标题
- 其他元数据，如浏览量和语言信息

我将使用两个命令在 ClickHouse 中浏览此数据：

- `DESCRIBE`: 了解列结构
- `SELECT`: 查看实际内容

以下是检查我们的数据集的代码：

```
-- Describes the content of the parquet file
DESCRIBE  
url('https://huggingface.co/datasets/Cohere/wikipedia-22-12-simple
embeddings/resolve/refs%2Fconvert%2Fparquet/default/train/0000.parquet',
'Parquet')
SETTINGS enable_url_encoding = 0, max_http_get_redirects = 1; 
 
-- Select lines to get the data in the parquet files 
SELECT *  
FROM  
url('https://huggingface.co/datasets/Cohere/wikipedia-22-12-simple
embeddings/resolve/refs%2Fconvert%2Fparquet/default/train/0000.parquet',
'Parquet')
LIMIT 2 
FORMAT Vertical 
SETTINGS enable_url_encoding = 0, max_http_get_redirects = 1;
```

关于设置的说明：我设置了 `enable_url_encoding = 0`，因为 URL 已经编码，并且设置了 `max_http_get_redirects = 1`，以允许在获取文件时进行一次重定向跳转。

运行这些命令会产生：

![](https://cdn.thenewstack.io/media/2025/03/b9227fef-image1.png)

![](https://cdn.thenewstack.io/media/2025/03/2be0fd16-image2.png)

## 创建向量搜索表

现在我们了解了数据结构，我将创建一个表来存储它。我将使用 ClickHouse 的 [MergeTree](https://clickhouse.com/docs/zh/engines/table-engines/mergetree-family/mergetree) 引擎，该引擎针对向量搜索等分析工作负载进行了优化：

```sql
CREATE TABLE wiki_emb 
( 
 id UInt32, 
   title String, 
   text String, 
      url String, 
      wiki_id UInt32, 
      views UInt32, 
      paragraph_id UInt32, 
     langs  UInt32, 
      emb Array(Float32) 
) 
ENGINE = MergeTree
ORDER BY id;
```

注意：我现在使用 `id` 列作为一个简单的索引。稍后我将介绍性能优化。

## 加载 Wikipedia 数据集

现在，我将使用多个 Parquet 文件中的数据填充该表。首先是一些快速设置：

```sql
SET max_http_get_redirects = 1 
SET enable_url_encoding = 0 
 
INSERT INTO wiki_emb 
SELECT * 
FROM ( 
    SELECT * FROM url('https://huggingface.co/datasets/Cohere/wikipedia-22-12
simple-embeddings/resolve/refs%2Fconvert%2Fparquet/default/train/0000.parquet',
'Parquet')
    UNION ALL 
    SELECT * FROM url('https://huggingface.co/datasets/Cohere/wikipedia-22-12
simple-embeddings/resolve/refs%2Fconvert%2Fparquet/default/train/0001.parquet',
'Parquet')
    UNION ALL 
    SELECT * FROM url('https://huggingface.co/datasets/Cohere/wikipedia-22-12
simple-embeddings/resolve/refs%2Fconvert%2Fparquet/default/train/0002.parquet',
'Parquet')
    UNION ALL 
    SELECT * FROM url('https://huggingface.co/datasets/Cohere/wikipedia-22-12
simple-embeddings/resolve/refs%2Fconvert%2Fparquet/default/train/0003.parquet',
'Parquet')
) AS data_sources;
```

## 优化性能

在开始运行搜索之前，进行一些优化：

1. 首先，我将使用 [ZSTD](https://github.com/facebook/zstd) 压缩嵌入向量，它适用于浮点数：

```sql
ALTER TABLE wiki_emb MODIFY COLUMN emb Array(Float32) CODEC(ZSTD);
```

请注意，虽然像 LZ4 这样的传统压缩方法对于嵌入效果不佳，但 ZSTD 可以显着减少存储空间，而不会影响性能。

2. 为了获得更好的插入性能，始终使用批量插入来减少开销，考虑使用 `file_name` 列来跟踪数据源，如果需要进一步减少存储空间，请研究量化。

## 运行相似向量

现在是有趣的部分 - 实际找到相似的内容。我将把它分成两个步骤，首先使用 Python 将搜索查询转换为向量：

```python
# Install the Cohere Python SDK 
# pip install cohere 
import cohere 
 
# Initialize the Cohere client with your API key 
api_key = 'your-api-key-here' 
co = cohere.Client(api_key) 
 
# Define the text you want to generate embeddings for 
text = " Who created Unix " # Replace with your query   
 
# Generate the embeddings using the multilingual-22-12 model 
response = co.embed( 
    texts=[text], 
    model='multilingual-22-12' 
) 
 
# Extract the embedding from the response 
embedding = response.embeddings[0] 
 
# Print the embedding 
print(embedding) 
 
# Verify the length of the embedding 
 
print(f'Length of embedding: {len(embedding)}') 
Output: 
[0.12451172, 0.20385742, -0.22717285, 0.39697266, -0.04095459 
… 
0.42578125, 0.23034668, 0.39160156, 0.116760254, 0.046661377, 0.1430664] 
Length of embedding: 768
```

请注意，在生产环境中，您通常会使用 LangChain 或类似的框架来处理嵌入生成。为了清楚起见，我在这里展示了基本方法。

## 查找相似文章

一旦我们有了查询嵌入，我们就可以使用 ClickHouse 的内置向量相似度函数来查找最相关的 Wikipedia 文章：

```sql
SELECT 
    title, 
    url, 
    paragraph_id, 
    text, 
    cosineDistance(emb, [Paste the embeddings]) AS distance 
FROM wiki_emb  
ORDER BY distance ASC 
LIMIT 5 
FORMAT Vertical;
```

这里使用了 `cosineDistance`，但 ClickHouse 也支持其他相似性度量，如 `L2Distance`，如果这些更适合您的需求。

该查询按文章与我们的搜索词“Who created Unix”的相似程度对文章进行排名，距离得分越低表示匹配越好。

## 真实性能

在适度的硬件（8 GB 内存，4 个 CPU）上运行此设置，我们获得了令人印象深刻的结果：

- 查询时间：0.633 秒
- 数据集大小：485,859 行
- 无需特殊调整或优化

ClickHouse 的一个特别引人注目的地方在于它处理规模的方式。性能随数据大小呈亚线性扩展，这意味着您不会看到查询时间随着数据集的增长而急剧增加。此外，由于它完全是开源的，您可以保持对数据和基础设施的完全控制。对于已经处理大规模分析工作负载的团队来说，ClickHouse 提供了一种实用的替代方案，可以替代专门的向量数据库，而无需供应商锁定。