# 使用 OpenAI CLIP、Claude Sonnet 3.5 和 pgvector 构建 AI 图像库

![使用 OpenAI CLIP、Claude Sonnet 3.5 和 pgvector 构建 AI 图像库](/blog/content/images/size/w2000/2024/09/Advanced-RAG-application-with-claude-sonnet-3-5-and-pgvector--1-.png)

Anthropic 是人工智能 (AI) 研究领域的一家巨头，主要专注于安全和道德的人工智能系统，它推出了另一个家族成员，**Claude Sonnet 3.5**。对于许多人来说，Claude 家族的最新成员凭借其智能、速度和成本效益，迅速取代了 GPT-4o 成为默认的大型语言模型 (LLM)，树立了新的行业标准。Sonnet 3.5 不仅用途广泛，而且可靠性也使其在开发人员中广受好评。

这些大型语言模型可以理解和处理各种模态，例如图像、文本和音频，使它们能够为从多模态搜索引擎到先进的 AI 驱动的创意工具等各种未来应用提供支持。[ 在之前的一篇文章中](https://www.timescale.com/blog/retrieval-augmented-generation-with-claude-sonnet-3-5-and-pgvector)，您了解了如何使用 Claude Sonnet 3.5 和 pgvector 构建一个简单的检索增强生成 (RAG) 应用程序。

在本文中，我们将提高挑战级别，创建一个**AI 图像库**，让您搜索图像并提出问题。我们将使用相同的工具构建一个 RAG 应用程序：带有 pgvector 的 PostgreSQL 作为向量数据库，以及 Claude Sonnet 3.5 作为 LLM。

[RAG 不仅仅是向量搜索](https://www.timescale.com/blog/rag-is-more-than-just-vector-search/).

## RAG 概述

RAG，即检索增强生成，是一种 AI 框架，通过将生成式语言模型与传统的信息检索系统相结合来增强生成式语言模型。

RAG 采用两个主要步骤：

1. **检索和预处理**: 强大的搜索算法查询外部数据源，检索到的信息会经过预处理，例如分词和去除停用词。

2. **生成**: 预处理后的数据被整合到 LLM 中，丰富其上下文，从而实现更准确、信息丰富和引人入胜的响应。

让我们深入了解我们将用于 RAG 应用程序的工具的详细信息。

## 工具详细信息

对于 RAG 应用程序，我们将使用带有 pgvector 的 PostgreSQL 作为我们的向量数据库，Claude Sonnet 3.5 将作为我们的 LLM。让我们讨论它们是什么以及它们的功能。

### Pgvector

从 PostgreSQL 16 开始，原生向量支持不可用，但**pgvector**通过允许您在 PostgreSQL 中存储和搜索向量数据来弥补了这一差距。这个开源扩展允许 PostgreSQL 执行通常与向量数据库相关的任务，包括：

**高级搜索**: Pgvector 允许将数据存储为向量，支持各种最近邻搜索算法，例如 L2、内积和余弦距离，用于精确和近似搜索。这些算法使根据您的查询有效地找到相似和相关的内容成为可能。**多功能应用**: 它可以根据各种属性找到类似的项目，例如图像、文档或产品，从而增强各种领域的搜索功能。**与 PostgreSQL 功能集成**: pgvector 与 PostgreSQL 的标准功能无缝集成，包括：，这确保了事务完整性。__ACID 兼容性__**时间点恢复**, 这允许恢复到特定时刻。，便于组合来自多个表的數據。`JOIN`
支持

### Claude Sonnet 3.5

Anthropic 的 Claude Sonnet 3.5 在各种评估中优于竞争对手和 Claude 3 Opus，同时与 Claude 3 Sonnet 的速度和成本相匹配。以下是 Claude Sonnet 3.5 LLM 的一些关键功能：

**速度**: 它比 Claude 3 Opus 快两倍。**成本**: 它按百万个 token 定价，比 Opus 低五倍。**性能**:- Claude Sonnet 3.5 在研究生级推理 (GPQA)、本科生级知识 (MMLU) 和编码能力 (HumanEval) 方面表现出色。
- 它优于竞争对手模型，例如 OpenAI 的 GPT-4o 和 Google 的 Gemini 1.5 Pro。
**用户体验**:- 开发人员报告编码任务的生产力提高了 3-4 倍。
- 该模型以其自然直观的交互方式而受到赞赏。
**可用性**:- 免费访问 Claude.ai 和 Claude iOS 应用程序
- Claude Pro 和 Team 计划订阅者享有更高的速率限制
- 可通过 Anthropic API、Amazon Bedrock 和 Google Cloud 的 Vertex AI 获取
- 也提供 Web 应用程序访问
**输入上下文窗口**: 支持高达 200,000 个 token**最大输出 token**: 每次请求最多可生成 4,096 个 token

![Claude 3.5 Sonnet 的成本和智能展示](https://www.timescale.com/blog/content/images/2024/09/Retrieval-Augmented-Generation-With-Claude-Sonnet-3.5-and-Pgvector_claude-models-1.png)

__Claude 3.5 Sonnet__

## 高级 RAG 实现
```python
from sentence_transformers import SentenceTransformer

# 加载 CLIP 模型
model = SentenceTransformer('clip-ViT-B-32')

# 编码图片
image_embeddings = model.encode(destination_filepaths)
```
```python
from PIL import Image
# 加载 CLIP 模型
img_model = SentenceTransformer("clip-ViT-B-32")
# 编码图像：
img_emb = model.encode([Image.open(filepath) for filepath in destination_filepaths])
img_emb = img_emb.tolist()
```

### 创建表格并插入数据
我们将创建 `image_gallery` 表来存储我们的图像及其嵌入。通常，图像不会直接存储在数据库中；而是存储对包含图像的文件系统的引用。我们将采用相同的方式。该表将包含以下列：

**Id**: 充当主键，用于唯一标识每一行。**Path**: 存储图像的文件路径，类型为 `TEXT`。
**Embedding**: 存储图像嵌入，类型为 `VECTOR`。`VECTOR` 的大小设置为 512，即用于图像表示的嵌入的维度。
```python
cursor.execute(document_table)
conn.commit()
```
以下代码构建了一个 **SQL** `INSERT` 语句，用于将图像文件路径及其嵌入添加到 `image_gallery` 表中。它通过交错文件路径和嵌入来准备参数，然后执行语句并将事务提交到数据库。

```python
sql = 'INSERT INTO image_gallery (path, embedding) VALUES ' + ', '.join(['(%s, %s)' for _ in img_emb])
params = list(itertools.chain(*zip(destination_filepaths, img_emb)))
cursor.execute(sql, params)
conn.commit()
```
创建 ivfflat 索引，就像之前一样：
```python
ivfflat = """CREATE INDEX ON image_gallery USING ivfflat (embedding vector_cosine_ops)"""
cursor.execute(ivfflat)
conn.commit()
```
### 图像搜索
以下代码根据文本查询执行图像搜索。它定义了一个名为 `image_search` 的函数，该函数将查询编码为嵌入。然后，它在 `image_gallery` 表中搜索前五个最接近的图像嵌入，并返回其文件路径。

```python
def image_search(conn, query):
    query_embeddings = img_model.encode(query).tolist()
    with conn.cursor() as cur:
        cur.execute('SELECT path FROM image_gallery ORDER BY embedding <=> %s::vector LIMIT 5', (query_embeddings))
        return cur.fetchall()
query = ["What is my grandpa holding"]
print(image_search(conn, query))
```
这是从函数中检索到的图像：

![一位老人拿着一个小木柜](https://www.timescale.com/blog/content/images/2024/09/Advanced-RAG-With-Pgvector-and-Claude-Sonnet-3.5_image.png)
现在，让我们向 Claude 模型询问更多关于图像的信息。

### 结合 LLM 和搜索
您可以将以下代码分解为以下部分：

**检索相关图像：**
- 调用 `image_search` 以根据文本查询获取相关图像 - 将图像编码为 base64 字符串
**增强查询：**
- 创建一个查询字符串，其中包含文本查询和有关图像的上下文
**查询 Claude 模型：**
- 向 Claude 模型发送一个请求，其中包含增强的查询和编码的图像。
- 请求模型描述图像
**返回结果：**
- 返回相关图像的文件路径和模型的响应
**示例用法：**
- 使用示例查询执行 `rag_function` - 使用 matplotlib 显示检索到的图像
以下是代码：

```python
def Smart_gallery(conn, client, model_name, query):
    relevant_images = image_search(conn, query)
    image_media_type = "image/jpeg"
    with open(relevant_images[0][0], "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        image_data =encoded_string.decode('utf-8')
    full_query = (f"Context: The following are relevant pictures for the given query.\n"
    f"Based on the image, explain what is the picture about:\n"
    f"Question: {query[0]}")
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image_media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Describe this image."
                    }
                ],
            }
        ],
    )
    return relevant_images[0][0], message.content
# 示例用法：
query = ["What is my grandpa holding"]
image, text = Smart_gallery(conn, client, "claude-3-5-sonnet-20240620", query)
plt.imshow(Image.open(image))
print(text)
```
以下是检索到的图像和查询结果：

![一位老人拿着一个小木柜](https://www.timescale.com/blog/content/images/2024/09/Advanced-RAG-With-Pgvector-and-Claude-Sonnet-3.5_image-1.png)
该模型通过计算图像搜索检索到的结果的嵌入距离和文本，并进行分析后，提供了结果。`>>> 图像显示一位头发花白、留着白胡子的老人，手里拿着一个看起来像是手工制作的木制橱柜或小型结构。他穿着灰色 T 恤，里面是白色长袖衬衫。他手中的木制品看起来像是玩具屋、宠物围栏或装饰性储物柜。它有雕刻的小门和小窗，看起来像房子。这位老人似乎是在家中，背景中可以看到窗帘。他的表情表明他可能正在检查或展示这件木制品，可能是他自己制作的。`

万事俱备！感谢 pgvector 和 Claude Sonnet 3.5，我们成功地完成了 AI 驱动的图像库。

## 结论

受增强型检索增强生成 (RAG) 与 LLM 能力的启发，我们开发了一个 AI 图像搜索库。该系统根据文本查询检索类似图像，并将它们用作 Sonnet 3.5 的上下文。

为了将图像和文本链接起来，我们使用 CLIP 模型生成嵌入，然后使用 pgvector 将其存储在 PostgreSQL 中。我们执行了相似性搜索以检索图像路径，然后将其提供给 Sonnet 3.5 用于上下文。

Timescale 可以帮助您更快、更高效地构建 AI 应用程序。使用 [Timescale Cloud](https://www.timescale.com/ai?ref=timescale.com)，开发人员可以访问 pgvector、pgvectorscale 和 pgai——这些扩展将 PostgreSQL 变成易于使用且高性能的向量数据库，以及完全托管的云数据库体验。

pgai 和 pgvectorscale 都是根据 PostgreSQL 许可证开源的。要安装它们，请查看 [pgai](https://github.com/timescale/pgai?ref=timescale.com) 和

[GitHub 仓库 (⭐s 欢迎！)。您可以在 Timescale Cloud PostgreSQL 平台上的任何数据库服务上访问 pgai 和 pgvectorscale。](https://github.com/timescale/pgvectorscale?ref=timescale.com)
__pgvectorscale__[.](http://console.cloud.timescale.com/signup?ref=timescale.com)
__立即使用 Timescale Cloud 构建您的 AI 应用程序__