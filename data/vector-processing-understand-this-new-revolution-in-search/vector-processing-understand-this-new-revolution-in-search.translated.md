# 向量处理：了解搜索领域的这场新革命

![Featued image for: Vector Processing: Understand This New Revolution in Search](https://cdn.thenewstack.io/media/2025/01/d364ee52-ato-nyah_macklin-1024x768.jpg)

“向量化一切！”

这是来自[Nyah Macklin](https://github.com/MacklinEngineering)，[Neo4j](https://neo4j.com/company/)高级开发者布道师在[All Things Open 2024](https://thenewstack.io/all-things-open-whats-your-future-as-a-developer/)上关于[向量数据库](https://thenewstack.io/integrating-vector-databases-with-existing-it-infrastructure/)的[演讲](https://2024.allthingsopen.org/sessions/understanding-vector-databases)中的真知灼见。

向量化数据在未来将变得非常重要，尤其是在机器学习和人工智能领域。

向量处理曾经是一个小众概念，如今已成为支持语义搜索、推荐系统和高级聊天机器人等创新应用的最前沿技术。

“向量搜索是一种新兴的信息检索方式，”Percona联合创始人兼技术研究员[Vadim Tkachenko](https://www.linkedin.com/in/vadimtk/)在[他在ATO 2024的会议](https://x.com/Joab_Jackson/status/1850920276243984831)上关于[数据库中的向量搜索](https://www.youtube.com/watch?v=KGGml9pEORM)中表示同意。

## 向量：超越关键词

向量处理的核心在于语义搜索的概念。与依赖于匹配关键词的传统词汇搜索不同，语义搜索深入探讨单词的含义和上下文，旨在理解用户的意图。

它“使我们能够理解单词背后的含义，而不仅仅是单词本身，”Macklin说。

它关乎解读语言的细微之处，认识到同一个词在不同的上下文中可能具有不同的含义。例如，“Apple”在“Apple laptop”中的含义与“apple pie”中的“apple”不同。

语义搜索利用嵌入，即单词、短语甚至整个文档的数值表示来捕捉它们的语义含义。通过将文本（和其他）信息转换为数值向量，语义搜索使计算机能够理解和比较不同内容的含义。

语义搜索是关于查找和评分相关数据，使用上下文和意图。– Nyah Macklin

语义搜索还可以从已知的用户信息中获得更多上下文。用户的搜索历史或位置可以提供更多关于他们意图的线索——例如，“足球”在美国和英国的含义完全不同。

语义搜索结果根据搜索意图进行评分，以便进行比较。相似度分数通常在零到一之间排名，其中一代表最大的相似度。

![Photo of Vadim Tkachenko.](https://cdn.thenewstack.io/media/2025/01/03ae54cf-ato-vadim_tkachenko-300x225.jpg)
Vadim Tkachenko在ATO 2024。

单词或短语的这种数值表示称为嵌入。“河岸”与“储蓄银行”的嵌入不同。

向量处理不仅仅局限于文本和语义搜索。它可以应用于各种数据类型，包括图像、音频和视频。例如，在图像识别中，可以将图像转换为向量，从而进行相似性搜索以查找具有相似内容或特征的图像。

## 向量：语义搜索的基石

向量本质上是一个数字列表，表示大小和方向。此列表中的元素数量定义了它的维度。在机器学习中，通常使用具有数百甚至数千维度的向量来表示复杂的概念和关系。

使用向量进行语义搜索的突破出现在2013年的一篇论文中，“[Efficient Estimation of Word Representations in Vector Space.](https://arxiv.org/abs/1301.3781)” 这篇论文的作者是谷歌的专家Tomas Mikolov、Kai Chen、Greg Corrado和Jeffrey Dean，它提供了一种将句子转换为向量的方法。

研究人员发现，与以往使用训练神经网络的方法相比，向量可以更有效地用于查找大型数据集中的相似之处。

研究人员写道：“我们在计算成本大大降低的情况下观察到精度的大幅提高，即从16亿字的数据集中学习高质量词向量所需时间不到一天。”“此外，我们证明这些向量在我们用于测量句法和语义词相似性的测试集上提供了最先进的性能。”

这篇论文介绍了一种新的模型，称为Word2Vec，它可以有效地将单词和短语转换为密集向量，从而捕捉它们的语义关系。具有相似含义的单词在向量空间中彼此更接近，而不同的单词则相距较远。
![向量嵌入图。](https://cdn.thenewstack.io/media/2025/01/6a2d8b9b-ato24-vectory-tkachenko-percoa-vector_embeddings-02.png)
维基百科图表，通过Vadim Tkachenko的演示说明向量嵌入。


自从论文发表以来，业界围绕这项技术构建了整个产业，[生成式AI](https://thenewstack.io/generative-ai-is-just-the-beginning-heres-why-autonomous-ai-is-next/)。

“向量搜索只是一种查找具有相似特征的相关对象的简单方法，”数据平台提供商[Aiven](https://aiven.io/about)的高级开发者布道者解释说，在她[ATO 2024演示文稿](https://2024.allthingsopen.org/sessions/vector-search-in-modern-databases)中。

“在向量搜索中，我们依靠机器加载模型来帮助我们检测不同事物的特征，无论它们是文本、图像、音频还是其他东西。”

在模型创建的多维空间中，相似的图像往往具有接近的向量，而不相似的图像则具有非常不同的向量。每个实体都有一组坐标，这些坐标可以在不同的实体之间进行比较。

## 向量匹配：在多维空间中搜索
为了有效地利用嵌入进行语义搜索，出现了被称为向量数据库的专用数据库，例如[Pinecone](https://www.pinecone.io/?utm_content=inline+mention)和开源[Milvus](https://milvus.io/)提供的数据库。

向量支持也正在快速添加到传统数据库中。例如，[PostgreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/)用户可以安装[PGVector](https://github.com/pgvector/pgvector)以获得完整的向量支持，包括向量搜索。一个512维向量简单地存储为一个512个数的数组。

![数据库代码。](https://cdn.thenewstack.io/media/2025/01/54d29573-ato24-vectory-tkachenko-percoa-vector_db-01.png)
在PostGreSQL中创建向量表，然后对其运行向量搜索（来自Vadim Tkachenko的演示文稿）。

举例说明了如何使用向量查找电影推荐。

对于这两种类型的数据库，用户查询（“一部有可爱小狗的电影”）都被转换为向量，以便可以将其与数据库中其他电影的“最近邻”进行比较。然后，向量数据库执行相似性搜索以查找其向量最接近查询向量的电影，从而有效地推荐与用户偏好匹配的电影。

## 向量数据库：如此多的向量
这些数据库采用[k近邻](https://www.ibm.com/think/topics/knn) (KNN)和[近似最近邻](https://www.mongodb.com/resources/basics/ann-search) (ANN)等算法来快速识别最接近给定查询向量的向量。

KNN是一种直接的算法，它将查询向量与数据库中的每个其他向量进行比较，根据距离度量识别k个最近邻。虽然对于较小的数据集有效，但对于大型数据集，KNN的计算成本很高。

ANN通过使用索引技术预处理数据并加快搜索速度来解决这一挑战。这些技术，例如IVFFlat和HNSW，创建相关向量的集群或图，允许搜索算法专注于向量空间的特定区域，从而减少所需的比较次数。

第一个选项，**IVFFlat**(具有平面压缩的反向文件)，围绕数据组构建集群，以便用户可以指定要检查的最接近查询的数据块。这是一个仅在输入大部分数据后才构建的索引。

![ivfflat-query](https://cdn.thenewstack.io/media/2025/01/bf58ee98-ato-kutsenko-vector-01-1024x587.png)
使用IVFFlat技术突出显示相关的电影。

第二个选项，**HNSW**(分层可导航小世界)，创建一个具有多层图，最不可能的材料位于外层。指出，这构建成本更高，但运行速度更快。如果要更改大量数据，这也是要使用的索引。

![HNSW图和代码。](https://cdn.thenewstack.io/media/2025/01/91c5c91e-ato-kutsenko-vector-hnsw-02-1024x573.png)
使用HNSW技术突出显示相关的电影。

## 向量处理：未来的搜索
虽然向量处理具有显著优势，但也需要注意一些挑战。结果的准确性很大程度上取决于嵌入的质量和所选择的相似性度量。此外，平衡性能和精度至关重要，尤其是在大型数据集的情况下。选择正确的索引技术并优化搜索参数可以显著影响向量搜索的效率和准确性。
但正如ATO 2024的演讲者所展示的，向量处理正在彻底改变我们与信息交互的方式，使机器能够以更人性化的方式理解和处理数据。

Kutsenko的完整演讲可以在这里观看：

[Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)