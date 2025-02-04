
<!--
title: 向量数据库为何将在AI时代长盛不衰
cover: https://cdn.thenewstack.io/media/2025/01/e9ed1c3b-why-vector-databases-are-here-stay-ai-age.jpg
-->

了解向量数据库，特别是多模态数据库，为何成为 AI 驱动架构中如此流行的组件。

> 译自 [Why Vector Databases Are Here to Stay in the AI Age](https://thenewstack.io/why-vector-databases-are-here-to-stay-in-the-ai-age/)，作者 Gerald Venzl。

向量数据库是人工智能驱动架构中的重要组成部分，随着主流人工智能和大型语言模型 (LLM) 的兴起，其受欢迎程度日益提高。

简单来说，[向量数据库](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/)是允许存储和检索向量的数据库。向量是LLM的关键组成部分，它对模型训练所用的数据进行抽象和推理。

然而，向量数据库作为*数据库*，不仅仅可以存储和检索向量。它们还提供内置的近似最近邻 (ANN) 算法，可以直接在数据库中实现向量相似性搜索功能。

## 向量数据库的类型

使用数据库管理新型数据有两种常见方法：单用途和多模型。向量也不例外。

单用途数据库已经产生了许多专注于向量存储、搜索和检索的向量数据库；但是，它们无法管理任何其他类型的数据。它们是为单一目的而构建的，因此得名*单用途数据库*。这方面的例子包括Chroma、[Pinecone](https://www.pinecone.io/?utm_content=inline+mention)和Weaviate。

多模型数据库方法将向量存储、搜索和检索功能添加到现有的数据库技术中。这允许在同一数据库中管理向量以及[其他类型的数据](https://thenewstack.io/what-data-type-should-you-use-for-storing-monetary-values_2/)。这方面的例子包括[PostgreSQL](https://roadmap.sh/postgresql-dba)、[MySQL](https://thenewstack.io/a-cheat-sheet-to-database-access-control-mysql/)和[Oracle Database](https://www.oracle.com/database/)。

## 使用向量数据库的好处

无论使用哪种方法，将向量存储在数据库中意味着在将LLM应用于现有数据时，不需要重复创建向量。此外，将向量存储在数据库中，而不是文件系统中的文件中，可以实现对它们的智能管理。例如，向量可以在数据库中进行索引、压缩和分区。

除了向量相似性搜索之外，向量数据库还可以用于多种其他场景，例如推荐引擎、目标检测和语义搜索。一些向量数据库还允许您导入和存储预训练的LLM，并通过这些LLM直接在数据库中生成传入数据的向量。这通常可以减轻对LLM中间层的需求。

向量数据库通常也是人工智能驱动架构中实现[检索增强生成 (RAG)](https://thenewstack.io/using-sql-powered-rag-to-better-analyze-database-data-with-genai/) 的重要组成部分，它通过提供特定领域的知识来微调LLM的响应。

## 多模型数据库的人工智能优势

然而，多模型方法可以实现其他重要场景，这些场景可以启动公司的AI之旅。因为多模型方法将向量功能添加到现有技术中，所以您通常只需要将现有系统升级到支持新向量功能的版本即可。这种优势不容忽视，因为它意味着您不必从头开始学习新的技术技能，不必安装新系统，也不必定义从现有来源到新系统的任何数据管道。

此外，多模型数据库可以结合传统的分析（通常通过SQL）实现向量相似性搜索。这意味着向量相似性搜索可以成为更大的[SQL查询](https://thenewstack.io/how-to-write-sql-queries)的一部分，并包含所有现有数据。

下面的示例显示了检索最符合感兴趣买家的预算和偏好位置的待售房屋的前10个最佳匹配项。它结合了向量相似性搜索来检索看起来像用户提供的图片中的房屋：

```sql
SELECT picture, price, location 
FROM houses_for_sale 
WHERE price <= (SELECT budget FROM buyers WHERE buyer_id = :app_user_id) 
  AND location IN (SELECT preferred_location FROM buyer_locations WHERE buyer_id = :app_user_id) 
ORDER BY VECTOR_DISTANCE (picture_vector, VECTOR_EMBEDDING(houses_llm USING :app_input_picture)) 
FETCH FIRST 10 ROWS ONLY;
```

查询的第一部分是一个常规的关系型SQL查询。它从`houses_for_sale`表中选择所有房屋的图片、价格和位置，其中售价小于或等于买家的预算，并且位置与买家的偏好位置之一匹配。然后，它根据用户提供的图片与`houses_for_sale`中房屋图片的相似度对结果进行排序。
表。这就是向量相似性搜索的用武之地。`ORDER BY` 部分无需直接比较图片，而是执行以下操作：

1. 通过导入的名为 `houses_llm` 的 LLM 使用 `VECTOR_EMBEDDING()` 函数生成用户提供的房屋图片的向量。
2. 获取生成的向量，并使用 `VECTOR_DISTANCE()` 函数计算其与存储的待售房屋图片向量的相似度或距离。
3. 然后根据这些向量的相似度对结果进行排序，首先返回最相似的结果。
4. 最后，它只返回前 10 个最相似向量的匹配项，例如，与用户提供的图片最相似的房屋。

使用多模态数据库方法也意味着熟悉 SQL 的用户无需深入了解 LLM 和向量生成即可执行向量相似性搜索。Oracle 数据库将多模态方法更进一步，采用融合数据库方法，不仅提供多模态功能，还使用户能够将数据库中可用的相同安全策略、压缩、信息生命周期管理 (ILM)、性能加速和其他功能应用于向量。

## 向量数据库长盛不衰

由于向量数据库使得存储、管理和检索向量变得如此容易，并且在多模态向量数据库的情况下，允许将向量相似性搜索与现有数据和分析相结合，因此它们已成为 AI 驱动架构中的一个流行组件。向量数据库不仅加速了公司利用 AI 的进程，而且简化了这一进程。
