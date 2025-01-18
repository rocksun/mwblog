
<!--
title: 如何使用OpenAI自动分类PostgreSQL中的数据
cover: https://miro.medium.com/v2/da:true/resize:fit:1200/0*aqvy9nSam8zLhloV
-->

数据分类是一项至关重要但极具挑战性的任务。学习如何使用开源扩展和OpenAI模型在PostgreSQL中实现自动化。

> 译自 [How to Automate Data Classification in PostgreSQL With OpenAI](https://medium.com/timescale/how-to-automate-data-classification-in-postgresql-with-openai-ff14f9066de9)，作者 Team Timescale。

企业从各种来源接收大量数据，包括客户互动、交易、支持查询、产品评论等等。这使得数据分类成为一项至关重要的任务。然而，对非结构化数据（例如客户评论和支持互动）进行分类一直具有挑战性。大型语言模型 (LLM) 的出现简化了这一过程。

在本教程中，我们将探讨如何使用开源扩展 pgai 和 pgvector 直接在 PostgreSQL 中自动化数据分类。如果您已经在 PostgreSQL 中拥有数据，或者想要构建不依赖于额外向量数据库或框架的分类系统，这种方法尤其有用。

🔖 要了解有关将非结构化数据转换为结构化数据的更多信息，请查看以下资源：
- [PostgreSQL 中的结构化、半结构化和非结构化数据](https://www.timescale.com/learn/structured-vs-semi-structured-vs-unstructured-data-in-postgresql)
- [使用开源工具解析所有数据：非结构化数据和 Pgai](https://timescale.ghost.io/blog/parsing-all-the-data-with-open-source-tools-unstructured-and-pgai/)

## 在 PostgreSQL 中自动化数据分类：工具

首先，让我们快速了解一下 pgvector 和 pgai，这两个我们将与 PostgreSQL 一起使用的开源扩展。我们还将了解 OpenAI 模型如何帮助完成此过程。

### Pgvector：将 PostgreSQL 打造为向量数据库

[Pgvector](https://github.com/pgvector/pgvector) 是一个功能强大的开源 PostgreSQL 扩展，它为数据库带来了向量处理功能，并允许您直接在表中存储、查询和管理高维向量。它可用于使用 PostgreSQL 构建语义搜索、推荐系统和数据分类算法。

### OpenAI 模型简介

OpenAI 提供一系列先进的语言模型，这些模型会随着技术的进步而更新。在撰写本文时，旗舰模型 GPT-4o 和 GPT-4o Mini 是最新的模型。这些模型是多模态的，能够处理文本和图像输入，同时产生文本输出，并且其架构旨在以高精度和速度处理复杂的多步骤任务。

GPT-4o 是阵容中最先进的模型，其上下文窗口最多可达 128,000 个 token，使其能够在长时间的对话或文档中保持广泛的上下文感知。该模型比之前的迭代（例如 GPT-4 Turbo）更快且更具成本效益。

对于需要更轻量级解决方案的开发者，GPT-4o Mini 是一个较小的模型，也是 OpenAI 最便宜的模型。它的智能高于 GPT-3.5-Turbo，但速度更快、成本更低，并且适用于轻量级任务。

上一代模型 GPT-4 Turbo 和 GPT-3.5 Turbo 仍然可用。GPT-4 Turbo 还包括视觉功能，支持 JSON 模式和函数调用，用于处理涉及文本和图像的任务。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aMO1IBF8Cix5s9WvZoXnng.png)

### 什么是 pgai？

[Pgai 是 PostgreSQL 的一个开源扩展](https://github.com/timescale/pgai) ，它将 AI 驱动的功能直接带入您的数据库。您可以使用 pgai 与机器学习模型交互并在 PostgreSQL 中构建 AI 工作流，从而使您能够创建 AI 驱动的系统，而无需离开数据库环境。

当 pgai 与 pgvector 和 OpenAI 结合使用时，其真正的强大功能就会显现出来。您可以使用 pgai 利用通过 pgvector 存储在 PostgreSQL 中的向量数据，并调用 OpenAI 方法来自动对这些数据进行分类。这种组合允许您在 PostgreSQL 中构建一个完全自动化的数据分类管道。

## 设置

首先，您需要一个安装了 pgvector 和 pgai 扩展的 PostgreSQL 工作安装。您可以[手动](https://github.com/timescale/pgai/tree/main?tab=readme-ov-file&ref=timescale.com#install-from-source)安装它们，或者使用预构建的 Docker [容器](https://github.com/timescale/pgai/tree/main?tab=readme-ov-file&ref=timescale.com#use-a-pre-built-docker-container)。或者，您可以简单地使用[Timescale Cloud](https://console.cloud.timescale.com/?ref=timescale.com) 获取一个预安装了 pgai 和 pgvector 的免费 PostgreSQL 云实例。

登录或在 Timescale Cloud 上创建一个帐户，选择您的服务类型、区域和计算能力，然后单击“创建服务”。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Dq0WIHBpV7WSxXlp)

创建服务后，您将收到连接字符串、用户名、密码、数据库名称和端口。您还可以下载数据库配置。

让我们将 PostgreSQL 数据库连接字符串保存为环境变量。

```bash
$ export PG_CONNECTION_STRING="your_postgresql_connection_string"
```

您还需要 OpenAI API 密钥。前往[platform.openai.com](http://platform.openai.com/) 获取一个。获取后，也将其保存在环境变量中。

```bash
$ export OPENAI_API_KEY="{API_KEY}"
```

现在您可以使用 `psql` 以如下方式连接：

```sql
PGOPTIONS="-c ai.openai_api_key=$OPENAI_API_KEY" psql -d $PG_CONNECTION_STRING
```

您可以激活pgai和pgvector扩展：

```sql
CREATE EXTENSION IF NOT EXISTS ai CASCADE;
CREATE EXTENSION IF NOT EXISTS vector CASCADE;
```

让我们检查一下pgai和pgvector扩展是否已在PostgreSQL数据库中启用，运行以下命令：

```sql
tsdb=> \dx
                                                    List of installed extensions
        Name         | Version |   Schema   |                                      Description
---------------------+---------+------------+---------------------------------------------------------------------------------------
 ai                  | 0.4.0   | ai         | helper functions for ai workflows
 pg_stat_statements  | 1.10    | public     | track planning and execution statistics of all SQL statements executed
 plpgsql             | 1.0     | pg_catalog | PL/pgSQL procedural language
 plpython3u          | 1.0     | pg_catalog | PL/Python3U untrusted procedural language
 timescaledb         | 2.17.2  | public     | Enables scalable inserts and complex queries for time-series data (Community Edition)
 timescaledb_toolkit | 1.18.0  | public     | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
 vector              | 0.8.0   | public     | vector data type and ivfflat and hnsw access methods
(7 rows)
```

让我们也检查一下OpenAI函数调用是否有效。您可以通过以下方式测试：

```sql
SELECT *
FROM ai.openai_list_models()
ORDER BY created DESC;
```

此代码应返回所有可用的OpenAI模型列表：

```
id | created | owned_by
-----------------------------+------------------------+-----------------
chatgpt-4o-latest | 2024-08-13 02:12:11+00 | system
gpt-4o-2024-08-06 | 2024-08-04 23:38:39+00 | system
gpt-4o-mini | 2024-07-16 23:32:21+00 | system
gpt-4o-mini-2024-07-18 | 2024-07-16 23:31:57+00 | system
gpt-4o-2024-05-13 | 2024-05-10 19:08:52+00 | system
gpt-4o | 2024-05-10 18:50:49+00 | system
gpt-4-turbo-2024-04-09 | 2024-04-08 18:41:17+00 | system
gpt-4-turbo | 2024-04-05 23:57:21+00 | system
gpt-3.5-turbo-0125 | 2024-01-23 22:19:18+00 | system
gpt-4-turbo-preview | 2024-01-23 19:22:57+00 | system
gpt-4-0125-preview | 2024-01-23 19:20:12+00 | system
…
```

我们现在可以继续教程步骤。

## 使用Pgai在PostgreSQL中执行数据分类

在本教程中，我们将从产品评论列表开始。然后，我们将使用pgai和pgvector扩展，利用OpenAI API将评论分类为正面、负面或中性类别。您可以使用类似的方法执行任何其他数据分类任务。

让我们首先创建一个`product_reviews`表，其中包含一些示例数据。

### 创建`product_reviews`表

以下SQL命令创建一个名为`product_reviews`的表，用于存储产品的客户评论。该表包括客户ID、评论日期、产品名称、简短评论和详细评论的列。

```sql
-- Create the `product_reviews` table
CREATE TABLE product_reviews (
    -- Unique identifier for each customer
    customer_id INT NOT NULL PRIMARY KEY,
    -- Timestamp with timezone for the review date
    date TIMESTAMPTZ,
    -- Name of the product being reviewed                    
    product TEXT,
    -- A brief summary of the review                        
    short_review TEXT,
    -- The detailed review text                   
    review TEXT                          
);
```

让我们通过运行以下命令来确认`product_reviews`表已成功创建：

```sql
\dt
```

输出：

```
List of relations
 Schema |      Name       | Type  |  Owner  
--------+-----------------+-------+----------
 public | product_reviews | table | postgres
(1 row)
```

### 插入示例产品评论

让我们插入笔记本电脑、手机和平板电脑等产品的示例评论。

```sql
-- Insert sample data into `product_reviews` table
INSERT INTO product_reviews (customer_id, date, product, short_review, review) VALUES
(1, '2022-01-01', 'laptop', 'Great!', 'Great laptop, very fast and reliable.'),
(2, '2022-01-02', 'laptop', 'Good', 'Good laptop, but the battery life could be better.'),
(3, '2022-01-03', 'laptop', 'Worst ever', 'This is the worst laptop I have ever used.'),
(4, '2022-01-04', 'laptop', 'Not bad', 'Not bad, but the screen is a bit small.'),
(5, '2022-01-05', 'phone', 'Excellent', 'Excellent phone, great camera and battery life.'),
(6, '2022-01-06', 'phone', 'Decent', 'Decent phone, but the screen is not as good as I expected.'),
(7, '2022-01-07', 'phone', 'Poor', 'Poor phone, battery life is terrible and camera quality is not good.'),
(8, '2022-01-08', 'tablet', 'Awesome', 'Awesome tablet, very fast and responsive.'),
(9, '2022-01-09', 'tablet', 'Satisfactory', 'Satisfactory tablet, but the screen resolution could be better.'),
(10, '2022-01-10', 'tablet', 'Disappointing', 'Disappointing tablet, slow performance and battery drains quickly.');
```

### 创建`product_reviews_classification`表

接下来，我们将创建`product_reviews_classification`表来存储数据分类结果，包括客户ID和评论类型。您可以使用以下SQL命令创建表。

```sql
-- Create the `product_reviews_classification` table
CREATE TABLE product_reviews_classification (
    -- Unique identifier for each customer
    customer_id INT NOT NULL PRIMARY KEY,
    -- The classification type of the review (e.g., Positive, Negative, Neutral)
    review_type TEXT                     
);
```

### 对产品评论进行分类并将其插入`product_reviews_classification`表

为了将产品评论分类为正面、负面或中性类别，我们将使用 OpenAI API。我们将使用 pgai 扩展提供的 SQL 中的`openai_chat_complete`函数来执行数据分类任务。

在 SQL 命令中，我们将执行三个关键步骤。

**步骤 1：使用结构化模板格式化评论**

第一步，我们将原始评论格式化为结构化文本格式。我们可以使用 SQL 中的`format`函数来实现，该函数将`short_review`和`review`字段组合成一个一致的模板。

**步骤 2：使用 OpenAI 对评论进行分类并对结果进行分类**

接下来，我们将获取格式化的评论并调用 OpenAI 的 API 将其分类为`positive`、`negative`或`neutral`。如果分类属于这三个预期类别之一，我们将保留它；否则，我们将默认评论为`neutral`。

**步骤 3：将分类后的评论插入`product_reviews_classification`表**

最后，我们将分类后的评论数据插入`product_reviews_classification`表。

以下是执行分类任务的三步 SQL 命令。

```sql
-- Step 1: Format reviews with a structured template
WITH formatted_reviews AS (
    SELECT
        customer_id,
        format(
            E'%s %s\nshort_review: %s\nreview: %s\n\t',
            short_review, review, short_review, review
        ) AS product_final_review
    FROM product_reviews
),

-- Step 2: Classify reviews using OpenAI and categorize the results
classified_reviews AS (
    SELECT
        customer_id,
        CASE
            WHEN result IN ('positive', 'negative', 'neutral') THEN result
            ELSE 'neutral'
        END AS review_type
    FROM (
        SELECT
            customer_id,
            ai.openai_chat_complete(
                'gpt-4o',
                jsonb_build_array(
                    jsonb_build_object(
                        'role', 'system',
                        'content', 'You are an assistant that classifies product reviews into positive, negative, or neutral categories. You can only output one of these three categories: positive, negative, or neutral.'
                    ),
                    jsonb_build_object(
                        'role', 'user',
                        'content',
                        concat(
                            E'Classify the following product review into positive, negative, or neutral categories. You cannot output anything except "positive", "negative", "neutral":\n\n',
                            string_agg(x.product_final_review, E'\n\n')
                        )
                    )
                )
            )->'choices'->0->'message'->>'content' AS result
        FROM formatted_reviews x
        GROUP BY customer_id
    ) subquery
)

-- Step 3: Insert classified reviews into the `product_reviews_classification` table
INSERT INTO product_reviews_classification (customer_id, review_type)
SELECT customer_id, review_type
FROM classified_reviews
;
```

在`openai_chat_complete`函数中，我们将使用“gpt-4o”模型。

首先，让我们通过运行以下命令确认产品评论是否已分类并插入到`product_reviews_classification`表中：

```sql
SELECT * FROM product_reviews_classification;
```

输出：

```
customer_id | review_type
-------------+-------------
4 | neutral
10 | negative
6 | neutral
2 | neutral
9 | neutral
3 | negative
5 | positive
7 | negative
1 | positive
8 | positive
(10 rows)
```

我们可以通过执行简单的 SQL 连接来验证我们的结果。

```sql
-- Join the `product_reviews` and `product_reviews_classification` tables
SELECT
    pr.customer_id,
    pr.review,
    prc.review_type
FROM
    product_reviews pr
JOIN
    product_reviews_classification prc
ON
    pr.customer_id = prc.customer_id;
```

输出：

```
customer_id |                                review                                | review_type
-------------+----------------------------------------------------------------------+-------------
           4 | Not bad, but the screen is a bit small.                              | neutral
          10 | Disappointing tablet, slow performance and battery drains quickly.   | negative
           6 | Decent phone, but the screen is not as good as I expected.           | neutral
           2 | Good laptop, but the battery life could be better.                   | neutral
           9 | Satisfactory tablet, but the screen resolution could be better.      | neutral
           3 | This is the worst laptop I have ever used.                           | negative
           5 | Excellent phone, great camera and battery life.                      | positive
           7 | Poor phone, battery life is terrible and camera quality is not good. | negative
           1 | Great laptop, very fast and reliable.                                | positive
           8 | Awesome tablet, very fast and responsive.                            | positive
(10 rows)
```

太棒了！我们已经成功地使用 pgai 的`openai_chat_complete`函数按类型对产品评论进行了分类。

## 使用触发器自动化数据分类任务

接下来，我们将创建一个触发器来自动化数据分类任务。为此，我们首先需要将数据分类的 SQL 命令封装到一个 PostgreSQL 函数中，该函数将由触发器调用。

### 步骤 1：将数据分类任务封装到函数中

```sql
CREATE OR REPLACE FUNCTION classify_and_insert_review() RETURNS TRIGGER AS $$
BEGIN
    -- Step 1: Format the new review with a structured template
    WITH formatted_reviews AS (
        SELECT
            NEW.customer_id AS customer_id,
            format(
                E'%s %s\nshort_review: %s\nreview: %s\n\t',
                NEW.short_review, NEW.review, NEW.short_review, NEW.review
            ) AS product_final_review
    ),

    -- Step 2: Classify the review using OpenAI and categorize the results
    classified_reviews AS (
        SELECT
            customer_id,
            CASE
                WHEN result IN ('positive', 'negative', 'neutral') THEN result
                ELSE 'neutral'
            END AS review_type
        FROM (
            SELECT
                customer_id,
                ai.openai_chat_complete(
                    'gpt-4o',
                    jsonb_build_array(
                        jsonb_build_object(
                            'role', 'system',
                            'content', 'You are an assistant that classifies product reviews into positive, negative, or neutral categories. You can only output one of these three categories: positive, negative, or neutral.'
                        ),
                        jsonb_build_object(
                            'role', 'user',
                            'content',
                            format(
                                E'Classify the following product review into positive, negative, or neutral categories. You cannot output anything except "positive", "negative", "neutral":\n\n%s',
                                product_final_review
                            )
                        )
                    )
                )->'choices'->0->'message'->>'content' AS result
            FROM formatted_reviews
        ) subquery
    )

    -- Step 3: Insert classified review into the product_reviews_classification table
    INSERT INTO product_reviews_classification (customer_id, review_type)
    SELECT customer_id, review_type FROM classified_reviews;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

这将创建该函数 `classify_and_insert_review()`.

### 步骤 2：创建触发器

接下来，我们创建一个触发器，每当向product_reviews表中插入新行时，该触发器就会调用上述函数。

```sql
CREATE TRIGGER classify_review_trigger
AFTER INSERT ON product_reviews
FOR EACH ROW
EXECUTE FUNCTION classify_and_insert_review();
```

一旦创建了这个触发器，每当向product_reviews表中插入新行时，classify_and_insert_review()函数就会被执行。

## 下一步

在本教程中，我们完成了一个简单的分类任务，演示了如何使用 OpenAI 和 pgai 在 PostgreSQL 中进行自动数据分类。我们使用 pgai 扩展与 OpenAI API 进行交互，将产品评论分类为正面、负面或中性类别。然后，我们创建了一个触发器来自动化分类。

要开始使用 PostgreSQL 和 OpenAI 自动化数据分类，请查看 Timescale Cloud 的 AI 堆栈。它包括一套完整的开源 PostgreSQL 扩展——pgvector、pgai、pgai Vectorizer 和 pgvectorscale——这将简化你的 AI 工作流程，无需管理多个系统的开销。今天就使用 Timescale Cloud 上的免费 PostgreSQL 数据库构建更智能、更高效的 AI 解决方案。

如果你想本地构建，你可以在各自的仓库（欢迎 GitHub⭐点赞！）中找到 pgai、pgai Vectorizer 和 pgvectorscale 的安装说明。这里有一个使用 Llama 3 和 Ollama 的示例教程，为你提供指导。