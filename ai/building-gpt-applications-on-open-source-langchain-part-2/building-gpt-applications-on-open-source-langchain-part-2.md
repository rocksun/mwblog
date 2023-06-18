# 在开源 LangChain 上构建 GPT 应用程序，第 2 部分

翻译自 [Building GPT Applications on Open Source LangChain, Part 2](https://thenewstack.io/building-gpt-applications-on-open-source-langchain-part-2/) 。查看原文可以看到更多的相关链接。

我们将使用快速崛起的 LLM 应用框架来给出一个实际的例子，展示如何使用 GPT 来帮助回答 PDF 文档中的问题。

![](https://cdn.thenewstack.io/media/2023/06/24ce4fb6-shutterstock_2-1024x512.jpg)

这是两篇文章中的第二篇。

在[前一篇文章](http://yylives.cc/2023/06/08/building-gpt-applications-on-open-source-stack-langchain/)中，我们讨论了在使用开源技术栈（如 LangChain ）构建 GPT 应用时，开发者需要考虑的三个因素。现在，让我们使用 LangChain 来给出一个实际的例子，我们希望能够存储和分析 PDF 文档。

我们将获取一个 PDF 文档，将其分成较小的部分，将文档的文本和其向量表示（嵌入*）保存在数据库系统中，然后进行查询。我们还将使用 GPT 来帮助回答问题。

*在 GPT 中，嵌入（embedding）是一个词语或短语的数值表示。[向量](https://thenewstack.io/vector-databases-what-devs-need-to-know-about-how-they-work/)以一种[机器学习模型](https://roadmap.sh/guides/free-resources-to-learn-llms)能理解的方式表示词语和短语的语义含义。

## 创建 SingleStoreDB 账号

首先，注册一个免费的 SingleStoreDB Cloud 账户。登录后，在左侧导航栏中选择 **CLOUD > Create new workspace group** 。接下来，选择 **Create Workspace** 并按照向导进行操作。以下是本示例的推荐设置：

* **Create Workspace Group**
* **Workspace Group Name**: LangChain Demo Group
* **Cloud Provider**: AWS
* **Region**: US East 1 (N. Virginia)


点击 **Next** ：

* **Create Workspace**
* **Workspace Name**: langchain-demo
* **Size**: S-00

点击 **Create Workspace** 。

一旦 workspace 创建并可用，从左侧导航栏中选择 **DEVELOP > SQL Editor** 来创建一个新的数据库，如下所示：

```sql
CREATE DATABASE IF NOT EXISTS pdf_db;
```

## 创建 Notebook

从左侧导航栏中选择 **DEVELOP > Notebooks** 。在网页的右上角，选择 **New Notebook > New Notebook** ，如下图所示（图1）。

![](https://cdn.thenewstack.io/media/2023/06/972a7af8-image2.png)

我们将笔记本称为 **langchain_demo** 。从可用选项中选择 **Blank** notebook 模板。

我们还将使用 notebook 上方的下拉菜单选择 **Connection** 和 **Database** ，如图 2 所示。

![](https://cdn.thenewstack.io/media/2023/06/299ba78e-image1.png)
*图2. Connection 和 Database*

## 填写 Notebook

首先，我们将导入一些库：

```python
!pip install langchain --quiet
!pip install openai --quiet
!pip install pdf2image --quiet
!pip install tabulate --quiet
!pip install tiktoken --quiet
!pip install unstructured --quiet
```

接下来，我们将读取一个 PDF 文档。这是 Neal Leavitt 撰写的一篇文章，标题为“面向对象数据库到底发生了什么？”面向对象数据库（OODB）是在 20 世纪 80 年代末和 90 年代初出现的一项新兴技术。我们将通过在右上方选择 **Edit Firewall** 选项来将 `leavcom.com` 添加到防火墙。一旦地址被添加到防火墙，我们将读取 PDF 文件：

```python
from langchain.document_loaders import OnlinePDFLoader
loader = OnlinePDFLoader("http://leavcom.com/pdf/DBpdf.pdf")
data = loader.load()
```

我们可以使用 LangChain 的 OnlinePDFLoader ，这使得阅读 PDF 文件更容易。

接下来，我们将获得有关文档的一些数据：

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

print (f"You have {len(data)} document(s) in your data")
print (f"There are {len(data[0].page_content)} characters in your document")
```

输出应为：

```
You have 1 document(s) in your data
There are 13040 characters in your document
```

现在，我们将文档拆分为包含 2000 个字符的页面，从而获得七页：

```python
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000, chunk_overlap = 0)
texts = text_splitter.split_documents(data)

print (f"You have {len(texts)} pages")
```

接下来，我们将创建一个表来存储文本和嵌入。我们可以直接使用 `%%sql magic` 命令来做到这一点：

```sql
%%sql

USE pdf_db;
DROP TABLE IF EXISTS pdf_docs;
CREATE TABLE IF NOT EXISTS pdf_docs (
    id INT PRIMARY KEY,
    text TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
    embedding BLOB
);
```

要使用 Python 代码连接到我们的数据库，我们可以使用内置的 `connection_url` ，如下所示：

```python
from sqlalchemy import *
db_connection = create_engine(connection_url)
```

我们将设置我们的 OpenAI API 密钥：

```python
import openai
openai.api_key = "OpenAI API Key"
```

并使用 LangChain 的 `OpenAIEmbeddings` ：

```python
from langchain.embeddings import OpenAIEmbeddings
embedder = OpenAIEmbeddings(openai_api_key = openai.api_key)
```

现在我们已经准备好获取向量嵌入并将它们存储在数据库系统中：

```python
db_connection.execute("TRUNCATE TABLE pdf_docs")

for i, document in enumerate(texts):
    text_content = document.page_content

    embedding = embedder.embed_documents([text_content])[0]

    stmt = """
        INSERT INTO pdf_docs (
            id,
            text,
            embedding
        )
        VALUES (
            %s,
            %s,
            JSON_ARRAY_PACK_F32(%s)
        )
    """
```

我们 TRUNCATE 表以确保我们从一个空表开始。然后我们遍历文本页面，从 OpenAI 获取嵌入，并将文本和嵌入存储在数据库表中。

我们现在可以问一个问题，如下所示：

```python
query_text = "Will object-oriented databases be commercially successful?"

query_embedding = embedder.embed_documents([query_text])[0]

stmt = """
    SELECT
        text,
        DOT_PRODUCT_F32(JSON_ARRAY_PACK_F32(%s), embedding) AS score
    FROM pdf_docs
    ORDER BY score DESC
    LIMIT 1
"""

results = db_connection.execute(stmt, str(query_embedding))

for row in results:
    print(row[0])
```

在这里，我们将问题转换为向量嵌入，执行 `DOT_PRODUCT` 并仅返回最高分值。

最后，我们可以根据前面的问题使用 GPT 来提供答案：

```python
prompt = f"The user asked: {query_text}. The most similar text from the document is: {row[0]}"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)
```

下面是一些示例输出：

*Based on the information provided in the document, it seems that object-oriented databases are not expected to be commercially successful in the near future. While they are gaining some popularity in niche markets such as CAD and telecommunications, relational databases continue to dominate the market and are expected to do so for the foreseeable future. IDC predicts that the growth rate for relational databases will be significantly higher than that of OO databases through 2004. However, OO databases still have their place in certain niche markets.*

## 总结

在这个例子中，我们看到了 LangChain 在应用程序开发过程中的优势。我们还看到了如何轻松地将文档从一种格式转换为另一种格式，将内容存储在数据库系统中，生成向量嵌入，并对存储在数据库系统中的数据提出问题。如果我们有兴趣对数据执行其他查询操作，我们还可以充分利用 SQL 的强大功能。

我将在 6 月 22 日主持一个研讨会，并将介绍如何使用 LangChain 构建一个 ChatGPT 应用程序。希望你能参加。在[这里](https://www.singlestore.com/resources/webinar-langchain-lift-off-launch-your-open-source-gpt-apps-today-2023-06/?utm_campaign=singlestore-for-ai&utm_medium=osm&utm_source=newstack)进行报名。
