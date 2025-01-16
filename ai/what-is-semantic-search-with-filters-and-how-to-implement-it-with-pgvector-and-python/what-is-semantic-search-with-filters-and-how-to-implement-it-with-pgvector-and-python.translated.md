在新窗口中打开 打开外部网站 在新窗口中打开外部网站

类别：所有文章

2025年1月15日

作者：Timescale团队

如果您正在使用搜索驱动的应用程序，在大量非结构化数据中找到所需内容可能会感觉像大海捞针。传统上，使用BM25等算法的关键词搜索一直是首选解决方案，但说实话——它常常达不到目标。为什么？因为它专注于匹配精确的词语，而不是理解其背后的实际上下文或含义。这就是**语义搜索**发挥作用的地方。语义搜索通过使用向量嵌入来捕捉词语的含义和上下文，从而提供更智能、更相关的结果。

更棒的是：当您向语义搜索添加过滤器时，您可以*微调*这些结果。想要按位置、类别或自定义字段缩小范围？很容易。过滤器允许您对数据进行切片和切块，以精确找到您要查找的内容。

在本指南中，我们将向您展示如何通过在PostgreSQL数据库中设置带有过滤器的语义搜索来增强您的搜索功能。我们将使用诸如[pgvector](https://www.timescale.com/learn/postgresql-extensions-pgvector)（用于存储和查询向量嵌入）之类的工具，

让我们开始吧！

语义搜索允许您*去除噪音*，超越基本的关键词匹配。它不仅仅查找精确的词语匹配，而是捕捉查询背后的*意图*和*上下文*。如何做到？通过使用[向量嵌入](https://www.timescale.com/blog/a-beginners-guide-to-vector-embeddings)—高维数值表示，将数据的本质打包成机器可以理解的格式。

它是这样工作的：您的数据被转换为向量表示。如果您正在处理文档，它通常会被分解成更小的块，每个块都被映射为高维向量空间中的一个唯一点。在这个空间中，具有相似含义的数据彼此更靠近。这意味着当您搜索时，系统会根据含义检索结果，而不仅仅是您键入的词语。

语义搜索使用余弦相似度或欧几里得距离等相似性度量来确定这些向量点有多接近。这些度量计算查询向量与潜在匹配之间的“距离”，帮助您找到最相关的结果。

为了提高速度，尤其是在大型数据集的情况下，近似最近邻搜索 (ANN) 或分层可导航小世界 (HNSW) 等算法发挥了作用。它们使查找相似向量变得快速有效，使您的搜索保持相关性和闪电般的速度。

在搜索应用程序中，过滤器是使结果更相关和更有用的武器。语义搜索在基于含义查找结果方面做得很好，但是当您添加过滤器时，您可以真正专注于重要内容。过滤器允许您根据特定条件（例如位置、类别、日期或自定义字段）缩小结果范围，以便用户获得他们想要的确切内容。

假设您正在构建产品搜索。语义搜索可能会调出与用户描述匹配的项目，但过滤器可以细化这些结果，仅显示某些品牌、价格范围或库存项目。语理解和基于属性的过滤相结合，有助于您创建高度定向且可操作的搜索算法。

从技术角度来看，过滤器通过限制搜索发生的向量空间来工作。算法不是扫描所有内容，而是只查看满足您条件的向量。结果？搜索速度更快，更相关。

当您实现带有过滤器的语义搜索时，您可能会遇到处理大型数据集或复杂过滤条件的情况。选择正确的索引方法是保持搜索速度和准确性的关键。您会遇到两个突出的选项：**分层可导航小世界** (HNSW) 算法，一种流行的索引算法，以及

HNSW 是一种基于图的算法，旨在进行高效的近似最近邻搜索。它的工作原理是构建一个多层图，其中每个节点代表一个数据点，边根据节点的邻近性连接节点。这种结构允许快速遍历和检索相似的向量。

优势：

* **高召回率：**HNSW 提供高召回率，确保检索最相关的向量。
* **快速查询时间：**图结构能够进行快速搜索，这对于实时应用程序非常有益。

局限性：

* **内存密集型：**HNSW 需要大量的内存存储，这对于大型数据集来说可能是一个限制。
* **过滤搜索挑战：**应用基于属性的过滤器效率可能较低，因为可能需要遍历整个图来强制执行过滤器，从而导致查询时间增加。

要了解有关[HNSW 算法的更多信息，请查看](https://www.timescale.com/blog/vector-database-basics-hnsw)我们的深入探讨。
StreamingDiskANN is an advanced indexing method introduced in pgvectorscale. It addresses some key limitations of HNSW and is significantly faster.

Compared to HNSW, the advantages for filtering searches are:

**Efficient Filtering:** StreamingDiskANN supports streaming filters, enabling accurate retrieval even when applying auxiliary filters during similarity search.  **Disk-Based Storage:** Unlike the memory-intensive HNSW, StreamingDiskANN stores parts of the index on disk. This reduces RAM dependency and makes it more cost-effective to run and scale as vector workloads grow.
In other words, HNSW offers high recall and fast queries, but it is very memory-intensive and struggles with filtering searches. StreamingDiskANN, on the other hand, provides a scalable and cost-effective solution with enhanced filtering capabilities, making it ideal for large datasets requiring complex filtering semantic search. You can read more about StreamingDiskANN and pgvectorscale capabilities in [this blog post](https://www.timescale.com/blog/how-we-made-postgresql-as-fast-as-pinecone-for-vector-data).

In the 2024 Stack Overflow Developer Survey, [PostgreSQL](https://survey.stackoverflow.co/2024/technology/#1-databases) was ranked as the most loved database for the second year in a row. DB-Engines also considers...

This tutorial will demonstrate how to easily build a semantic search with filtering using PostgreSQL and Python. Let's get started.

First, you need a PostgreSQL environment with the necessary extensions installed. You can install them [manually](https://github.com/timescale/pgai/tree/main?tab=readme-ov-file&ref=timescale.com#install-from-source) or use a pre-built Docker image.

Run the following command to pull the TimescaleDB image:

```bash
docker pull timescale/timescaledb-ha:pg16
```
This image comes pre-installed with the extensions in the default PostgreSQL database. Now, run the container:

```bash
docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb-ha:pg16
```
Now, you can connect to your PostgreSQL instance using the following command:

```bash
psql -d "postgres://<username>:<password>@<host>:<port>/<database-name>"
```
The default `username` and `database-name` are both `postgres`. Use the password you set when running the Docker container.

Now, enable the extensions:

```sql
CREATE EXTENSION IF NOT EXISTS ai CASCADE;
CREATE EXTENSION IF NOT EXISTS vectorscale CASCADE;
```
The `CASCADE` option will automatically install [pgvector](https://github.com/pgvector/pgvector) and...

`\dx`
You should get output similar to this, showing the ai, vector, and vectorscale extensions installed:

```
postgres=# \dx
List of installed extensions
Name | Version | Schema | Description
---------------------+---------+------------+---------------------------------------------------------------------------------------
ai | 0.6.0 | ai | helper functions for ai workflows
plpgsql | 1.0 | pg_catalog | PL/pgSQL procedural language
plpython3u | 1.0 | pg_catalog | PL/Python3U untrusted procedural language
timescaledb | 2.17.2 | public | Enables scalable inserts and complex queries for time-series data (Community Edition)
timescaledb_toolkit | 1.19.0 | public | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
vector | 0.8.0 | public | vector data type and ivfflat and hnsw access methods
vectorscale | 0.5.1 | public | pgvectorscale: Advanced indexing for vector data
(7 rows)
```
This tutorial uses OpenAI's [GPT 4o](https://platform.openai.com/docs/models#gpt-4o) model as the LLM. However, you can also choose other models...

Go to [platform.openai.com](http://platform.openai.com) to get your OpenAI API key. Once you have the key, create a

`.env`
file and set the API key as an environment variable.  Also, add the database connection string.
```
OPENAI_API_KEY="your_secret_openai_api_key"
DB_URL="postgres://postgres:password@127.0.0.1:5432/postgres"
```
Create a Python virtual environment, install JupyterLab and launch it.

```bash
$ pip install jupyterlab
$ jupyter lab
```
Now you can install the required libraries:

```bash
!pip install psycopg2-binary
!pip install python-dotenv
```
Since we are using a local Docker-based installation, we should also install the [pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md) Python...

```bash
!pip install pgai
```
You should now run the vectorizer worker so that it can generate embeddings later. You can do this:

```bash
$ pgai vectorizer worker -d "postgres://postgres:password@127.0.0.1:5432/postgres"
```
Now, let's check if you can successfully connect to OpenAI and retrieve the list of all available models:

```python
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
DB_URL = os.environ["DB_URL"]
import psycopg2
with psycopg2.connect(DB_URL) as conn:
    with conn.cursor() as cur:
        # pass the API key as a parameter to the query. don't use string manipulations

```
```python
cur.execute("SELECT * FROM ai.openai_list_models(api_key=>%s) ORDER BY created DESC", (OPENAI_API_KEY,))
records = cur.fetchall()
print(records)
```

如果您的设置正常工作，这将返回可用 OpenAI 模型的列表。

本教程将使用一个[酒店评论数据集](https://www.kaggle.com/datasets/pratiyushsingh/timescale-synthetic-hotel-reviews)。每条评论包括评论全文、物业类型、位置、评论者位置、评分、卧室和浴室数量以及评论日期。有些评论是积极的，而另一些是消极的。

以下是我们的数据集示例。为简洁起见，我们只显示了七行：

```json
[
  {
    "review_text": "The hotel was a haven of comfort and luxury. Impeccably clean rooms, friendly staff, and a prime location made our stay unforgettable. The delicious breakfast spread was an added bonus. Highly recommend this gem!",
    "date": "2025-01-01",
    "category": "hotels",
    "name": "Yates, Gonzalez and Mack",
    "rating_score": 5,
    "location": {
      "city": "Cooktown",
      "country": "Canada"
    },
    "customer_location": {
      "city": "South Staceyburgh",
      "country": "Bahamas"
    },
    "bedrooms": 3,
    "bathrooms": 1
  },
  {
    "review_text": "This hotel is exceptional! The rooms are pristine and beautifully decorated. Staff are incredibly welcoming and attentive. The amenities, including the luxurious pool and spa, are top-notch. An unforgettable stay with stunning views and a delightful atmosphere. Highly recommend!",
    "date": "2025-01-02",
    "category": "hotels",
    "name": "Hill-Hatfield",
    "rating_score": 3,
    "location": {
      "city": "Rachelland",
      "country": "Benin"
    },
    "customer_location": {
      "city": "Dorothyview",
      "country": "Cayman Islands"
    },
    "bedrooms": 3,
    "bathrooms": 2
  },
  {
    "review_text": "The room was filthy, with stained sheets and a persistently foul odor. Staff was rude and unresponsive to complaints. The so-called \"breakfast\" was inedible. Worst hotel experience I've ever had. Not recommended at all.",
    "date": "2025-01-06",
    "category": "hotels",
    "name": "Rocha, Robinson and Ellis",
    "rating_score": 1,
    "location": {
      "city": "Holmesstad",
      "country": "Benin"
    },
    "customer_location": {
      "city": "New Joshua",
      "country": "Senegal"
    },
    "bedrooms": 2,
    "bathrooms": 3
  },
  {
    "review_text": "The hostel offers a convenient location with friendly staff and basic amenities. Rooms are clean but can be cramped. Communal areas are lively, though sometimes noisy. Good for budget travelers seeking a social atmosphere.",
    "date": "2025-01-11",
    "category": "hostels",
    "name": "Lane-Kidd",
    "rating_score": 2,
    "location": {
      "city": "North Sarahton",
      "country": "Portugal"
    },
    "customer_location": {
      "city": "Port Manuelburgh",
      "country": "Philippines"
    },
    "bedrooms": 5,
    "bathrooms": 3
  },
  {
    "review_text": "The hotel was a nightmare—musty room, stained sheets, and a bathroom that screamed for cleaning. Unhelpful staff and paper-thin walls made sleep impossible. The only thing five-star about this place is the regret. Don't stay here.",
    "date": "2025-01-11",
    "category": "hotels",
    "name": "Love Group",
    "rating_score": 5,
    "location": {
      "city": "Mackville",
      "country": "New Zealand"
    },
    "customer_location": {
      "city": "East Cole",
      "country": "Pitcairn Islands"
    },
    "bedrooms": 5,
    "bathrooms": 2
  },
  {
    "review_text": "These apartments are fantastic! The spacious, modern design and top-notch amenities create a luxurious living experience. The friendly staff and well-maintained facilities make it a pleasure to call this place home. Highly recommended!",
    "date": "2025-01-05",
    "category": "apartments",
    "name": "Jordan LLC",
    "rating_score": 1,
    "location": {
      "city": "Lake Meganview",
      "country": "Nepal"
    },
    "customer_location": {
      "city": "Williebury",
      "country": "Mexico"
    },
    "bedrooms": 5,
    "bathrooms": 2
  },
  {
    "review_text": "I had an amazing stay at the downtown hostel! The staff was incredibly friendly and helpful, the rooms were clean and cozy, and the communal areas were perfect for meeting fellow travelers. Highly recommend!",
    "date": "2025-01-08",
    "category": "hostels",
    "name": "Torres-Branch",
    "rating_score": 2,
    "location": {
      "city": "Davidsonchester",
      "country": "Romania"
    },
    "customer_location": {
      "city": "Wallaceberg",
      "country": "Chile"
    },
    "bedrooms": 5,
    "bathrooms": 2
  }
]
```

让我们首先创建一个名为`hotel_reviews`的表：

```python
conn = psycopg2.connect(DB_URL)
conn.autocommit = True
with conn.cursor() as cur:
    cur.execute('''
CREATE TABLE IF NOT EXISTS hotel_reviews (
id BIGINT PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
review_text TEXT,
embedding vector(1536),
category TEXT,
rating_score INTEGER,
location_city TEXT,
location_country TEXT,
customer_city TEXT,
customer_country TEXT,
name TEXT,
date DATE,
bedrooms INTEGER,
bathrooms INTEGER
);
''')
```

每个表列对应于我们评论数据中的一个属性。现在，让我们插入我们的数据集并在过程中创建嵌入。方法如下：

```python
with conn.cursor() as cur:
    for review in hotel_reviews:
```
```python
print("插入评论：")
print(review)
cur.execute('''
INSERT INTO hotel_reviews (
    review_text, category, rating_score,
    location_city, location_country,
    customer_city, customer_country, name,
    date, bedrooms, bathrooms
)
VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
''', (
    review['review_text'],
    review['category'],
    review['rating_score'],
    review['location']['city'],
    review['location']['country'],
    review['customer_location']['city'],
    review['customer_location']['country'],
    review['name'],
    review['date'],
    review['bedrooms'],
    review['bathrooms']
))
```

[Pgai 向量化器](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md) 可直接在 PostgreSQL 中自动创建和维护向量嵌入。它允许您

```python
with conn.cursor() as cur:
    cur.execute('''
SELECT ai.create_vectorizer(
    'Reviews'::regclass,
    destination => 'hotel_reviews_embeddings',
    embedding => ai.embedding_openai('text-embedding-3-small', 1536),
    chunking => ai.chunking_recursive_character_text_splitter('review_text'),
    formatting => ai.formatting_python_template('$chunk - Category: $category'),
    indexing => ai.indexing_hsnw(min_rows => 50000, opclass => 'vector_l2_ops')
);
''')
```

向量化器使用 OpenAI 的模型自动从`review_text`列生成嵌入。嵌入存储在单独的表中（`hotel_reviews_embeddings_store`），并自动创建一个视图（`hotel_reviews_embeddings`）以将原始数据与其嵌入连接起来，从而方便查询和使用嵌入数据。在上面的代码中，我们还创建了一个分层可导航小世界 (HSNW) 索引以加快相似性搜索速度。对于更大的数据集，[StreamingDiskANN](https://www.timescale.com/blog/pgvector-is-now-as-fast-as-pinecone-at-75-less-cost) 是推荐的方法。创建向量化器时，您可以按以下方式设置：

```python
with conn.cursor() as cur:
    cur.execute('''
SELECT ai.create_vectorizer(
    'Reviews'::regclass,
    destination => 'hotel_reviews_embeddings',
    embedding => ai.embedding_openai('text-embedding-3-small', 1536),
    chunking => ai.chunking_recursive_character_text_splitter('review_text'),
    formatting => ai.formatting_python_template('$chunk - Category: $category'),
    indexing => ai.indexing_diskann(min_rows => 100000, storage_layout => 'memory_optimized')
);
''')
```

现在，我们将创建一个函数来执行带有过滤器的语义搜索。以下是函数的代码：

```python
def semantic_search(query_text, category=None, min_rating=None, max_rating=None,
                    min_bedrooms=None, max_bedrooms=None,
                    min_bathrooms=None, max_bathrooms=None,
                    location_city=None, location_country=None, limit=5):
    """
    使用可选的评分、房间和位置过滤器执行语义搜索
    """
    with conn.cursor() as cur:
        # 使用过滤器构建 SQL 查询
        sql = '''
WITH query_embedding AS (
    SELECT ai.openai_embed('text-embedding-3-small', %s, api_key=>%s) as embedding
)
SELECT review_text, category, rating_score,
       location_city, location_country,
       bedrooms, bathrooms,
       embedding <=> (SELECT embedding FROM query_embedding) as distance
FROM hotel_reviews
WHERE 1=1
'''
        params = [query_text, OPENAI_API_KEY]
        if category:
            sql += ' AND category = %s'
            params.append(category)
        if min_rating:
            sql += ' AND rating_score >= %s'
            params.append(min_rating)
        if max_rating:
            sql += ' AND rating_score <= %s'
            params.append(max_rating)
        if min_bedrooms:
            sql += ' AND bedrooms >= %s'
            params.append(min_bedrooms)
        if max_bedrooms:
            sql += ' AND bedrooms <= %s'
            params.append(max_bedrooms)
        if min_bathrooms:
            sql += ' AND bathrooms >= %s'
            params.append(min_bathrooms)
        if max_bathrooms:
            sql += ' AND bathrooms <= %s'
            params.append(max_bathrooms)
        if location_city:
            sql += ' AND location_city = %s'
            params.append(location_city)
        if location_country:
            sql += ' AND location_country = %s'
            params.append(location_country)
        sql += ' ORDER BY embedding <-> (SELECT embedding FROM query_embedding) LIMIT %s'
        params.append(limit)
        cur.execute(sql, params)
        results = cur.fetchall()
        return [
            {
                'review_text': r[0],
                'category': r[1],
                'rating_score': r[2],
                'location_city': r[3],
                'location_country': r[4],
                'bedrooms': r[5],
                'bathrooms': r[6],
                'similarity_score': 1 - r[7]  # 将距离转换为相似度
            }
            for r in results
        ]

```

```python
results = semantic_search(
    "private pool",
    category="villas",
    limit=3
)
for i, result in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(f"Review: {result['review_text']}")
    print(f"Category: {result['category']}")
```

```python
print(f"评分: {result['rating_score']}")
print(f"位置: {result['location_city']}, {result['location_country']}")
print(f"房间: {result['bedrooms']} 寝室, {result['bathrooms']} 浴室")
print(f"相似度评分: {result['similarity_score']:.2f}")
```

```
结果 1:
评论: 这座别墅是宁静的绝美绿洲，拥有令人叹为观止的景色、优雅的内饰和宁静的私人泳池。它是奢华与舒适的完美融合，提供难忘的美丽与放松之旅。
类别: 别墅
评分: 4
位置: 新克雷格, 圣诞岛
房间: 3 寝室, 1 浴室
相似度评分: 0.39

结果 2:
评论: 这座别墅是天堂！令人惊叹的景色、奢华的设施和无可挑剔的服务。无边泳池和茂盛的花园营造了宁静的休憩之所。非常适合放松和恢复活力。对于任何寻求难忘休憩的人来说，它都是真正的瑰宝！
类别: 别墅
评分: 2
位置: 阿什利港 haven, 留尼汪
房间: 3 寝室, 3 浴室
相似度评分: 0.35

结果 3:
评论: 别墅散发着奢华和宁静的气息，拥有令人惊叹的海景、豪华的内饰和私人无边泳池。无可挑剔的服务和茂盛的花园使这里成为梦幻般的度假胜地。真正的天堂度假胜地！
类别: 别墅
评分: 5
位置: 霍夫曼堡, 南非
房间: 5 寝室, 3 浴室
相似度评分: 0.35
```

就是这样！我们已经成功地在 PostgreSQL 中使用 pgai 和 pgvector 扩展实现了带有过滤器的语义搜索。此外，我们还利用 pgvectorscale 的 StreamingDiskANN 索引来实现高性能的嵌入式搜索和存储效率。

我们刚刚构建了一个功能强大的带有过滤功能的 PostgreSQL 语义搜索引擎，它结合了 pgai 和 pgvector 的简单性和 pgvectorscale 的性能提升。

立即开始构建您自己的带过滤器的语义搜索！有关 [Timescale 的 AI 堆栈](https://www.timescale.com/ai) 的更多信息，请浏览

以下是一些相关的博文和指南，可帮助您扩展知识并了解有关语义搜索及其他内容的更多信息：

* 使用 OpenAI 和 PostgreSQL 在 10 分钟内完成语义搜索
* 在 PostgreSQL 中结合语义搜索和全文搜索（使用 Cohere、Pgvector 和 Pgai）
* 使用 Pgvector 和 JavaScript 实现过滤的语义搜索
* 使用 Pgvector 和 Cohere 的 PostgreSQL 混合搜索
* 我们如何使 PostgreSQL 的向量数据速度与 Pinecone 一样快

最初发布日期

2025年1月15日

pgai

3.3k

pgvectorscale

1.5k