# Elasticsearch 很好，但向量数据库才是未来

![Featued image for: Elasticsearch Was Great, But Vector Databases Are the Future](https://cdn.thenewstack.io/media/2024/11/dfd4cd38-similarity-1024x574.png)

几十年来，关键词匹配（也称为全文搜索），例如 Elasticsearch，一直是企业搜索和推荐引擎等信息检索系统的默认选择。

随着人工智能驱动的搜索技术的进步，人们正在转向[语义搜索](https://zilliz.com/glossary/semantic-search?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)，使系统能够理解用户查询的含义和意图。嵌入模型和[向量数据库](https://zilliz.com/learn/what-is-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)已成为这种转变的核心。

语义搜索通过将数据表示为向量嵌入来超越关键词匹配，从而更细致地理解搜索意图，并改变从[检索增强生成](https://zilliz.com/learn/Retrieval-Augmented-Generation?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns) (RAG)到[多模态搜索](https://milvus.io/docs/multimodal_rag_with_milvus.md#Multimodal-Search-with-Generative-Reranker?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)的各种应用。

实际上，有效的信息检索系统既需要语义理解，也需要精确的关键词匹配。例如，用户期望搜索结果显示与其[搜索查询相关的概念，同时也要尊重查询中使用的文字](https://thenewstack.io/taming-text-search-with-the-power-of-regular-expressions/)，例如特殊术语和名称，并返回精确匹配的结果。

由稠密向量驱动的语义搜索有助于理解含义（例如知道“汽车”和“轿车”相同），而[传统的全文搜索](https://zilliz.com/learn/evolution-of-search-from-traditional-keyword-matching-to-vector-search-and-genai?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)则提供用户期望的精确结果（例如查找“Python 3.9”的精确匹配）。因此，许多组织正在采用混合搜索方法，结合两种方法的优势，在灵活的语义相关性和可预测的精确关键词匹配之间取得平衡。

**混合搜索的挑战**

实现混合搜索的一种常见方法是使用专用向量数据库，例如开源的[Milvus](https://zilliz.com/what-is-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)，用于高效且可扩展的语义搜索，以及像Elasticsearch或OpenSearch这样的传统搜索引擎用于全文搜索。

虽然这种方法可以产生良好的结果，但它也引入了一层新的复杂性。管理两个不同的搜索系统意味着要处理单独的基础设施、配置和维护任务，这会增加运营负担，并增加潜在集成问题的可能性。

统一的混合搜索解决方案将带来许多好处：

* **减少基础设施维护：**管理一个系统而不是两个系统，可以大大降低运营复杂性，节省时间和资源。这也意味着减少上下文切换和掌握两套不同 API 的认知负担。
* **整合数据管理：**统一的表结构允许您同时存储[稠密](https://zilliz.com/learn/sparse-and-dense-embeddings?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)（基于向量）和[稀疏](https://zilliz.com/learn/sparse-and-dense-embeddings#Sparse-versus-dense-embeddings-a-summary?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)（基于关键词）数据以及共享的元数据标签。使用两个独立的系统需要为双方都存储两次元数据标签才能进行元数据过滤。
* **简化查询：**单个请求可以执行语义和全文搜索任务，无需对单独的系统进行两次 API 调用。
* **增强的安全性和访问控制：**统一的方法可以实现[更直接和强大的安全管理](https://thenewstack.io/managing-cloud-security-risk-posture-through-a-full-stack-approach/)，因为所有访问控制都可以在向量数据库中集中管理，从而增强安全合规性和一致性。

**统一向量方法如何简化混合搜索**
在语义搜索中，[机器学习模型](https://zilliz.com/ai-models?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)将文本“嵌入”为点，即[稠密向量](https://zilliz.com/learn/dense-vector-in-ai-maximize-data-potential-in-machine-learning?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)，在高维空间中基于其含义表示。语义相似的文本在该空间中彼此更接近。“苹果”和“水果”在这个空间中可能比“苹果”和“汽车”更接近。这允许我们仅通过使用[近似最近邻 (ANN)](https://zilliz.com/glossary/anns?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)算法计算每个点之间的距离来快速找到语义相关的文本。

此方法也可应用于全文搜索，方法是将文档和查询编码为稀疏向量。在稀疏向量中，每个维度代表一个词项，其值表示该词项在文档中的重要程度。

文档中不存在的词项的值为零。由于任何给定文档通常只使用词汇表中所有可能词项的一小部分，因此大多数词项不会出现在文档中。这意味着生成的向量是稀疏的——它们的大多数值都为零。例如，在通常用于[评估信息检索](https://thenewstack.io/researchers-use-machine-learning-to-supercharge-data-retrieval/)任务的MS-MARCO数据集中，虽然大约有900万个文档和一百万个唯一词项，但搜索系统通常将这个大型集合划分为较小的片段以方便管理。

即使在段落级别，词汇表中也有数十万个词项，每个文档通常包含少于100个词项，这意味着每个向量的值超过99%为零。这种极端的稀疏性对我们有效存储和处理这些向量的方式具有重要意义。

这种稀疏模式可以用来优化搜索性能，同时保持准确性。最初为稠密向量设计的向量数据库可以适应有效地处理这些稀疏向量。例如，开源向量数据库Milvus刚刚发布了使用Sparse-BM25的原生全文搜索支持，Sparse-BM25是Elasticsearch和其他全文搜索系统使用的[BM25算法](https://zilliz.com/learn/mastering-bm25-a-deep-dive-into-the-algorithm-and-application-in-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)的稀疏向量实现。Sparse-BM25通过以下方式为全文搜索解锁基于近似的优化：

**高效的检索算法和数据剪枝：**通过应用基于启发式的剪枝来丢弃段索引中稀疏向量值最低的文档，并忽略搜索查询中的低值稀疏向量，向量数据库可以显著减小索引大小并优化性能，同时将质量损失降到最低。**解锁进一步的性能优化：**将词频表示为稀疏向量而不是反向索引，可以实现额外的基于向量的优化。这些包括：- 图索引用于比暴力扫描更有效的搜索。
[乘积量化 (PQ) / 标量量化 (SQ)](https://zilliz.com/learn/scalar-quantization-and-product-quantization?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)进一步减少内存占用。
除了这些优化之外，Sparse-BM25实现还继承了高性能向量数据库Milvus的几个系统级优势：

**高效的底层实现和内存管理：**Milvus中的核心[向量索引引擎](https://thenewstack.io/what-is-milvus-vector-database/)是用C++实现的，比基于Java的系统（如Elasticsearch）提供了更有效的内存管理。仅此一项就通过节省与基于JVM的方法相比的千兆字节来减少内存占用。**支持MMap：**与Elasticsearch在内存和磁盘中都使用页面缓存进行索引存储类似，Milvus支持[内存映射 (MMap)](https://zilliz.com/blog/milvus-introduced-mmap-for-redefined-data-management-increased-storage-capability?utm_source=vendor&utm_medium=referral&utm_campaign=2024-11-11_blog_elasticsearch-limits_tns)来扩展索引超过可用内存时的内存容量。
**传统搜索堆栈在向量搜索方面的不足**
Elasticsearch 是基于传统的倒排索引构建的，这使得优化其整体架构以进行密集向量搜索从根本上变得困难。其影响是显而易见的：即使只有 100 万个向量，Elasticsearch 也需要 200 毫秒（在完全托管的 Elastic Cloud 上测试）才能返回搜索结果，而 Milvus 在完全托管的 Zilliz Cloud 上则需要 6 毫秒——性能差异超过 30 倍。

每秒查询数 (QPS) 的吞吐量也有 3 倍的差异，其中 Zilliz Cloud 上性能最高的实例运行速度为 6,000 QPS，而 Elastic Cloud 最多为 1,900 QPS。此外，Zilliz Cloud 加载向量数据和构建索引的速度比 Elastic Cloud 快 15 倍。

这种性能差距随着规模的扩大而扩大，Elasticsearch 的 Java/JVM 实现难以与基于 C++/Go 的向量数据库的扩展性相匹配。此外，Elasticsearch 缺乏关键的向量搜索功能，例如基于磁盘的索引 (DiskAnn、MMap)、优化的元数据过滤和范围搜索。

**结论**

以 Milvus 为例的向量数据库，有望超越 Elasticsearch，成为混合搜索的统一解决方案。通过将密集向量搜索与优化的稀疏向量技术相结合，向量数据库提供了卓越的性能、可扩展性和效率。

这种统一的方法简化了基础设施，减少了内存占用，并增强了搜索功能，使其成为高级搜索需求的未来。因此，向量数据库提供了一个全面的解决方案，可以无缝地结合语义搜索和全文搜索，性能优于 Elasticsearch 等传统搜索系统。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。