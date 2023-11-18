<!--
title:  基于Milvus和Python的电影推荐系统开发
cover: https://cdn.thenewstack.io/media/2023/11/8e2f603d-movie-recommender-engine-1024x565.jpg
-->

用开源工具帮用户发现兴趣电影。

译自 [Create a Movie Recommendation Engine with Milvus and Python](https://thenewstack.io/create-a-movie-recommendation-engine-with-milvus-and-python/)，作者 Gourav Singh Bais。


推荐系统或推荐引擎是旨在预测和推荐用户可能感兴趣的产品、服务和内容(如电影、书籍、音乐或新闻文章)的信息过滤系统。

存在各种类型的推荐系统，例如[协同过滤](https://realpython.com/build-recommendation-engine-collaborative-filtering/)、[基于内容的过滤](https://www.turing.com/kb/content-based-filtering-in-recommender-systems)、[混合推荐系统](https://analyticsindiamag.com/a-guide-to-building-hybrid-recommendation-systems-for-beginners/)和[基于向量的推荐系统](https://medium.com/vector-database/building-personal-recommender-systems-with-milvus-and-paddlepaddle-808567e3d65e)。基于向量的系统使用向量空间来查找(推荐)数据库中最接近的项目。存储这些向量有多种方法，最高效的方法之一是使用 [Milvus](https://milvus.io/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-11-08_blog_milvus-movie-recommender_tns) 开源[向量数据库](https://thenewstack.io/using-a-vector-database-to-search-white-house-speeches/)。该数据库高度灵活、快速且可靠，支持快速添加、删除、更新数万亿字节的向量并进行近实时搜索。

本文介绍了如何使用 [Milvus](https://zilliz.com/what-is-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2023-11-08_blog_milvus-movie-recommender_tns) 和 [Python](https://zilliz.com/product/integrations/python) 构建电影推荐器。该系统将使用 SentenceTransformers 将文本[信息转换](https://www.sbert.net/)为向量，并将这些向量存储在 Milvus 中。Milvus 使用户能够根据他们提供的文本信息在数据库中搜索电影。

您可以在 [GitHub 上的 Milvus Bootcamp 仓库](https://github.com/milvus-io/bootcamp)中找到本教程的代码，还有一个 [Jupyter 笔记本](https://github.com/milvus-io/bootcamp/blob/master/solutions/nlp/recommender_system/recommender_system.ipynb)。

## 搭建环境

对于本文，您需要安装以下要求:

- Python 3.x
- Python 包管理器(PIP)安装包
- Jupyter 笔记本编写代码
- Docker
- 至少 32GB RAM 的系统或 Zilliz Cloud 帐户

Python 要求

您还需要安装一组将在本教程中需要的库。使用 PIP 安装库:

```
$ python -m pip install pymilvus pandas sentence_transformers Kaggle
```

向量数据存储(Milvus)

您将使用 Milvus 向量数据库来存储您将使用电影描述生成的嵌入。数据集相对较大，至少对于在个人电脑上运行的服务器而言。所以您可能想使用 Zilliz Cloud 实例来存储这些向量。

如果您更喜欢保留本地实例，可以下载 docker-compose 配置并运行它:

```
$ wget https://github.com/milvus-io/milvus/releases/download/v2.3.0/milvus-standalone-docker-compose.yml -O docker-compose.yml
$ docker-compose up -d
```

您现在已经具备了使用 Milvus 构建电影推荐系统的所有要求。

数据收集和预处理  

对于这个项目，您将使用来自 Kaggle 的电影数据集，其中包含 45，000 部电影的元数据。您可以直接下载这个数据集，或者使用 Kaggle API 通过 Python 下载数据集。要通过 Python 完成此操作，您需要从 Kaggle.com 的个人资料部分下载 kaggle.json 文件，并将其放在 API 可以找到的位置。

接下来，设置一些 Kaggle 身份验证的环境变量。为此，您可以打开 Jupyter 笔记本并编写以下代码行:

```
%env KAGGLE_USERNAME=username
%env KAGGLE_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%env TOKENIZERS_PARALLELISM=true 
```

完成后，您可以使用 Kaggle 的 Python 依赖项从 Kaggle 下载数据集:

```python
# import kaggle dependency
import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('rounakbanik/the-movies-dataset'， path='dataset'， unzip=True)
```

下载数据集后，您可以使用 pandas 的 read_csv() 方法读取数据集:

```python 
# import pandas
import pandas as pd

# read csv data  
movies = pd.read_csv('dataset/movies_metadata.csv'， low_memory=False)

# check shape of data
movies.shape
```

数据库记录和列

图片显示您有 45，466 条记录，有 24 列元数据。使用以下命令检查所有这些元数据列:

```
# check column names
movies.columns
```

数据集列  

有许多您不需要创建推荐系统的列。您可以使用以下命令过滤所需的列:

```python
# filter required columns
trimmed_movies = movies[["id"， "title"， "overview"， "release_date"， "genres"]]

trimmed_movies.head(5)
```

必需的列

此外，数据中的一些字段缺失，因此删除那些行以产生干净的数据集:

```python
unclean_movies_dict = trimmed_movies.to_dict('records')
print('{} movies'.format(len(unclean_movies_dict)))

movies_dict = []
for movie in unclean_movies_dict:
    if movie["overview"] == movie["overview"] and movie["release_date"] == movie["release_date"] and movie["genres"] == movie["genres"] and movie["title"] == movie["title"]:
        movies_dict.append(movie)
```

连接 Milvus  

现在您已经具有所有所需的列，连接到 Milvus 开始上传数据。要连接到 Milvus 云实例，您需要统一资源标识符 (URI) 和令牌，您可以从 Zilliz Cloud 控制台下载它们。

Zilliz Cloud 控制台

获取 URI 和 API 密钥后，可以使用 PyMilvus 中的 connect() 方法连接到 Milvus 服务器:

```python
# import milvus dependency
from pymilvus import *

# connect to milvus
milvus_uri="YOUR_URI"
token="YOUR_API_TOKEN"

connections.connect("default"， uri=milvus_uri， token=token)

print("Connected!")
```

为电影生成嵌入

现在是计算电影数据集中文本数据的嵌入的时候了。首先，创建一个集合对象，它将存储电影 ID 和文本数据的嵌入。还要创建一个索引字段，以提高搜索效率:

```python
COLLECTION_NAME = 'film_vectors'
PARTITION_NAME = 'Movie'

# Here's our record schema  
"""
"title": Film title，
"overview": description，  
"release_date": film release date，
"genres": film generes，
"embedding": embedding
"""

id = FieldSchema(name='title'， dtype=DataType.VARCHAR， max_length=500， is_primary=True)
field = FieldSchema(name='embedding'， dtype=DataType.FLOAT_VECTOR， dim=384)

schema = CollectionSchema(fields=[id， field]， description="movie recommender: film vectors"， enable_dynamic_field=True)

if utility.has_collection(COLLECTION_NAME):
  # drop the same collection created before    
  collection = Collection(COLLECTION_NAME)
  collection.drop()
  
collection = Collection(name=COLLECTION_NAME， schema=schema)
print("Collection created.")

index_params = {
  "index_type": "IVF_FLAT"，
  "metric_type": "L2"，
  "params": {"nlist": 128}，    
}

collection.create_index(field_name="embedding"， index_params=index_params)
collection.load()
print("Collection indexed!")
```

现在您有一个索引集合，可以为文本生成嵌入的函数。尽管概览是生成嵌入的主要列，但您也将使用流派和发布日期信息以及概述来使数据更具逻辑性。  

要生成嵌入，请使用 SentenceTransformer:

```python
from sentence_transformers import SentenceTransformer
import ast

# function to extract the text from genre column
def build_genres(data):
  genres = data['genres']
  genre_list = ""
  entries = ast.literal_eval(genres)
  genres = ""
  for entry in entries:
    genre_list = genre_list + entry["name"] + "， "
  genres += genre_list
  genres = "".join(genres.rsplit("，"， 1))
  return genres

# create an object of SentenceTransformer   
transformer = SentenceTransformer('all-MiniLM-L6-v2')

# function to generate embeddings
def embed_movie(data):
  embed = "{} Released on {}. Genres are {}.".format(data["overview"]， data["release_date"]， build_genres(data))
  embeddings = transformer.encode(embed)
  return embeddings  
```

该函数使用 build_genres() 方法清理流派列并从中获取文本。然后它创建一个 SentenceTransformer 对象来帮助从文本生成嵌入。最后，它使用 encode() 方法使用概述、发布日期和流派特征生成嵌入。

将嵌入发送到 Milvus  

现在您可以使用 embed_movie() 方法创建嵌入。这个数据集太大，不适合在一次插入语句中发送到 Milvus，但是每次发送一行数据会产生不必要的网络流量并增加太多时间。所以，创建数据行的批次(例如 5，000 行)发送到 Milvus:

```python
# Loop counter for batching and showing progress
j = 0
batch = []

for movie_dict in movies_dict:
  try:
    movie_dict["embedding"] = embed_movie(movie_dict)
    batch.append(movie_dict)
    j += 1
    if j % 5 == 0:
      print("Embedded {} records".format(j))
      collection.insert(batch)
      print("Batch insert completed")
      batch=[]
  except Exception as e:
    print("Error inserting record {}".format(e))
    pprint(batch)
    break
    
collection.insert(movie_dict)    
print("Final batch completed")
print("Finished with {} embeddings".format(j)) 
```

注意:您可以根据个人需求和偏好调整批量大小。 此外，一些电影的 ID 无法转换为整数会失败。您可以通过架构更改或验证其格式来解决此问题。

将嵌入发送到 Milvus

使用 Milvus 推荐新电影

现在您可以利用 Milvus 的近实时向量搜索功能来获取符合观众标准的电影的近似匹配。为此，创建两个不同的函数:

embed_search():您需要一个转换器将用户的搜索字符串转换为嵌入。该函数获取查看者的标准，并将其传递给您用来填充 Milvus 的相同转换器。

search_for_movies():此函数执行实际的向量搜索，并使用其他函数提供支持。

```python
# load collection memory before search
collection.load()

# Set search parameters   
topK = 5
SEARCH_PARAM = {
  "metric_type":"L2"，
  "params":{"nprobe": 20}，    
}

# convert search string to embeddings
def embed_search(search_string):
  search_embeddings = transformer.encode(search_string)
  return search_embeddings

# search similar embeddings for user's query
def search_for_movies(search_string):
  user_vector = embed_search(search_string)
  return collection.search([user_vector]，"embedding"，param=SEARCH_PARAM， limit=topK， expr=None， output_fields=['title'， 'overview'])
```

上述代码定义了参数 topK 用于获取前五个相似向量，metric_type 为 L2(欧几里德平方)计算两个向量之间的距离，nprobe 表示要搜索的集群单元数量。它还实现了不同的函数来获取用户查询(推荐)的相似向量。

最后，使用 search_for_movies() 函数根据用户的搜索词条推荐电影:

```python
from pprint import pprint

search_string = "A comedy from the 1990s set in a hospital. The main characters are in their 20s and are trying to stop a vampire."
results = search_for_movies(search_string)

# check results for hits
for hits in iter(results):
  for hit in hits:
    print(hit.entity.get('title'))
    print(hit.entity.get('overview'))
    print("-------------------------------") 
```

电影推荐输出

通过使用 Milvus 的向量搜索功能，代码根据用户的查询推荐前五部相似的电影。就是这样:您现在已经