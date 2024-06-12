# 使用高级 SQL 向量查询增强您的 RAG 应用程序

![增强您的 RAG 应用程序的高级 SQL 向量查询的特色图片](https://cdn.thenewstack.io/media/2024/06/8988455f-advancedsqlqueries-1024x574.png)

[检索增强生成 (RAG)](https://myscale.com/blog/understanding-retrieval-augmented-generation-what-is-rag-why-it-matters/#what-is-rag-and-how-does-it-work) 彻底改变了我们与数据交互的方式，在相似性搜索中提供了无与伦比的性能。它擅长根据简单查询检索相关信息。但是，RAG 在处理更复杂的任务（例如基于时间的查询或复杂的关联数据库查询）时常常力不从心。这是因为 RAG 主要设计用于使用来自外部来源的相关信息进行增强文本生成，而不是执行基于条件的精确检索。[这些限制](https://thenewstack.io/5-bottlenecks-impacting-rag-pipeline-efficiency-in-production/) 限制了它在需要精确和条件数据检索的场景中的应用。

我们的高级 RAG 模型基于 SQL [向量数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)，将有效管理各种查询类型。它不仅可以处理简单的相似性搜索，还擅长基于时间的查询和复杂的关联查询。

让我们讨论一下如何使用 [MyScale](https://myscale.com/) 和 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 创建 AI 助手来克服这些 RAG 限制，从而提高数据检索过程的准确性和效率。我们将抓取 Hacker News 的最新故事，同时指导您完成该过程，以演示如何使用高级 SQL 向量查询增强您的 RAG 应用程序。

## 工具和技术

我们将使用多种工具，包括 MyScaleDB、OpenAI、LangChain、[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 和 HackerNews API 来开发此有用应用程序。

- [MyScaleDB](https://myscale.com/)：MyScale 是一个 SQL 向量数据库，可以高效地存储和处理结构化和非结构化数据。
- [OpenAI](https://openai.com/)：我们将使用 OpenAI 的聊天模型生成文本到 SQL 查询。
- LangChain：LangChain 将帮助构建工作流并与 MyScale 和 OpenAI 无缝集成。
- [Hugging Face](https://huggingface.co/)：我们将使用 Hugging Face 的嵌入模型获取文本嵌入，这些嵌入将存储在 MyScale 中以供进一步分析。
- [HackerNews](https://github.com/HackerNews/API)API：此 API 将从 HackerNews 获取实时数据以进行处理和分析。

## 准备

### 设置环境

在开始编写代码之前，我们必须确保安装了所有必需的库和依赖项。您可以使用以下方法安装它们：

```
pip install -r requirements.txt
```

此 `pip` 命令应安装此项目中所需的所有依赖项。

### 导入库并定义辅助函数

首先，我们将导入必要的库并定义用于从 Hacker News 获取和处理数据的辅助函数。

```python
import pandas as pd
import requests
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def get_story_ids():
    # ...

def get_story_details(story_id):
    # ...

def get_comments(story_id):
    # ...

def convert_comments_to_string(comments):
    # ...
```

这些函数获取故事 ID，获取特定项目的详细信息，递归获取评论并将评论转换为单个字符串。

### 获取和处理故事

接下来，我们从 Hacker News 获取最新和最热门的故事，并处理它们以提取相关数据。

```python
# 获取最新和最热门的故事
stories = get_story_ids()

# 处理故事以提取相关信息
processed_stories = []
for story_id in stories:
    story_details = get_story_details(story_id)
    comments = get_comments(story_id)
    comments_string = convert_comments_to_string(comments)
    processed_stories.append({
        "title": story_details["title"],
        "url": story_details["url"],
        "score": story_details["score"],
        "time": story_details["time"],
        "author": story_details["author"],
        "comments": comments_string
    })
```

我们使用上述定义的辅助函数从 Hacker News 获取最新和最热门的故事。我们处理获取的故事以提取相关信息，如标题、URL、分数、时间、作者和评论。我们还将评论列表转换为单个字符串。

## 初始化用于嵌入的 Hugging Face 模型

我们现在将使用预训练模型为故事标题和评论生成嵌入。此步骤对于创建 RAG 系统至关重要。

```python
# 加载预训练模型
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")
```

我们将使用 Hugging Face transformers 库加载用于生成嵌入的预训练模型，并为故事标题和评论生成嵌入。

### 处理长评论

为了处理超出模型最大令牌长度的长评论，我们将它们拆分为可管理的部分。

```python
def split_long_comments(comment):
    # ...
```

此函数将长评论拆分为适合模型最大令牌长度的部分。

### 处理故事以进行嵌入

最后，我们将处理每个故事以生成标题和评论的嵌入，并创建一个最终的 Pandas DataFrame。

```python
# 处理故事以生成嵌入
processed_stories_with_embeddings = []
for story in processed_stories:
    title_embedding = model(tokenizer(story["title"], return_tensors="pt")).pooler_output
    comments_embedding = model(tokenizer(story["comments"], return_tensors="pt")).pooler_output
    processed_stories_with_embeddings.append({
        "title": story["title"],
        "url": story["url"],
        "score": story["score"],
        "time": story["time"],
        "author": story["author"],
        "title_embedding": title_embedding,
        "comments_embedding": comments_embedding
    })

# 创建最终的 DataFrame
df = pd.DataFrame(processed_stories_with_embeddings)
```

在此步骤中，我们处理每个故事以生成标题和评论的嵌入，在必要时处理长评论，并使用所有处理后的数据创建一个最终的 DataFrame。

## 连接到 MyScaleDB 并创建表

MyScaleDB 是一个高级 SQL 向量数据库，它通过以下方式增强了 RAG 应用程序：

- **高效的向量存储和检索：**MyScaleDB 可以高效地存储和检索向量，从而实现快速和准确的相似性搜索。
- **SQL 接口：**MyScaleDB 提供了一个熟悉的 SQL 接口，使开发人员可以轻松地使用 SQL 查询来执行复杂的数据检索。
- **可扩展性和高可用性：**MyScaleDB 是可扩展的，可以处理大量数据，并且具有高可用性，以确保应用程序的持续运行。

要连接到 MyScaleDB 并创建表，请执行以下步骤：

```sql
# 连接到 MyScaleDB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydb"
)

# 创建表
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE stories (
        id INT NOT NULL AUTO_INCREMENT,
        title TEXT,
        url TEXT,
        score INT,
        time DATETIME,
        author TEXT,
        title_embedding BINARY(128),
        comments_embedding BINARY(128),
        PRIMARY KEY (id)
    )
""")

# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()
```

通过这些步骤，我们连接到 MyScaleDB 并创建了一个名为 `stories` 的表，该表将存储处理后的故事数据，包括标题和评论嵌入。
### 高效处理复杂查询

[高效处理复杂查询](https://myscale.com/blog/complex-queries-with-sql-in-vector-databases/) 和相似性搜索，例如 [全文搜索](https://myscale.com/blog/text-search-and-hybrid-search-in-myscale/) 和 [过滤向量搜索](https://myscale.com/blog/optimizing-filtered-vector-search/)。

我们将使用 clickhouse-connect 连接到 MyScaleDB，并创建一个表来存储抓取的故事。

此代码导入 clickhouse-connect 库，并使用提供的凭据建立与 MyScaleDB 的连接。如果存在，它将删除现有的表 default.posts，并使用指定架构创建一个新表。

**注意：** MyScaleDB 为 500 万个向量的向量存储提供了一个免费的 pod。因此，你可以在你的 RAG 应用程序中开始使用 MyScaleDB，而无需任何初始付款。

### 插入数据和创建向量索引

现在，我们将处理后的数据插入 MyScaleDB 表，并创建一个索引以实现高效的数据检索。

此代码将数据批量插入 default.posts 表中，以高效管理大量数据。向量索引在 Title_Embedding 列上创建。

### 设置查询生成提示模板

我们将设置一个提示模板，将自然语言查询转换为 MyScaleDB SQL 查询。

此代码设置了一个提示模板，指导 LLM 根据输入问题生成正确的 MyScaleDB 查询。

### 设置查询参数

我们将设置查询生成的 parameters。

此代码设置要检索的 top 结果数 (top_k)，定义表信息 (table_info)，并为问题设置一个空输入字符串 (input)。

## 设置模型

在此步骤中，我们将设置 OpenAI 模型，以将用户输入转换为 SQL 查询。

### 将文本转换为 SQL

此方法首先根据用户输入和表信息生成一个最终提示，然后使用 OpenAI 模型将文本转换为 SQL 向量查询。

在此步骤之后，我们将获得如下查询：

```sql
SELECT * FROM default.posts
WHERE DISTANCE(Title_Embedding, Embeddings('AI domain')) < 0.5
ORDER BY DISTANCE(Title_Embedding, Embeddings('AI domain'))
LIMIT 10;
```

但 MyScaleDB DISTANCE 预期 DISTANCE(column, array)。因此，我们需要将 Embeddings('AI domain') 部分转换为向量嵌入。

## 处理和替换查询字符串中的嵌入

此方法将用于将 Embeddings(“Extracted keywords”) 替换为 float32 数组。

此方法将查询作为 input，如果查询字符串中存在任何 Embeddings 方法，则返回更新后的查询。

## 执行查询

最后，我们将执行查询以从向量数据库中检索相关故事。

此外，你可以获取模型返回的查询，提取指定列并使用它们来获取列，如上所示。然后可以将这些结果传递回聊天模型，创建一个完整的 AI 聊天助手。这样，助手可以动态地使用直接从结果中提取的相关数据来响应用户查询，确保无缝且交互式的体验。

## 结论

简单的 RAG 由于专注于直接相似性搜索而用途有限。但是，当与 MyScaleDB、LangChain 等高级工具结合使用时，RAG 应用程序不仅可以满足大规模大数据管理的需求，还可以超越这些需求。它们可以处理更广泛的查询，包括基于时间和复杂的关联查询，从而显著提高当前系统的性能和效率。

如果你有任何建议，请通过 [X/Twitter](https://x.com/MyScaleDB) 或 [Discord](https://discord.com/invite/D2qpkqc4Jq) 联系我们。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。