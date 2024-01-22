<!--
title: Milvus 2023：开源向量数据库年度回顾
cover: https://cdn.thenewstack.io/media/2024/01/b3816dc5-data-1024x576.png
-->

随着新年的到来，现在是回顾整个向量数据库行业的好时机，特别关注开源项目Milvus。

> 译自 [Milvus in 2023: Open Source Vector Database Year in Review](https://thenewstack.io/milvus-in-2023-open-source-vector-database-year-in-review/)，作者 James Luan 是Zilliz的工程副总裁。拥有康奈尔大学计算机工程硕士学位的他，在Oracle、Hedvig和阿里云等公司拥有丰富的数据库工程师经验。

去年标志着人工智能（AI）的一个重要转折点。[大语言模型](https://zilliz.com/glossary/large-language-models-(llms)?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)（LLMs）已经成为焦点，因其卓越的自然语言处理能力而得到广泛认可。这一激增的流行度显著扩展了机器学习应用的可能性，使开发人员能够构建更智能和交互式的应用程序。

在这场革命中，[向量数据库](https://zilliz.com/learn/what-is-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)已经成为一个关键组成部分，[充当LLMs](https://roadmap.sh/guides/free-resources-to-learn-llms)的长期记忆。[检索增强生成](https://zilliz.com/use-cases/llm-retrieval-augmented-generation?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)（RAG）模型的崛起，智能代理和多模态检索应用程序的出现展示了向量数据库在增强多模态数据检索效率、减少LLMs中的幻觉并补充领域知识方面的巨大潜力。

LLM的发展也催生了嵌入技术的重大进展。根据Hugging Face上的[Massive Text Embedding Benchmark（MTEB）排行榜](https://huggingface.co/spaces/mteb/leaderboard)，领先的嵌入模型如UAE、VoyageAI、CohereV3和Bge都是在2023年发布的。这些进展加强了各种向量搜索技术（如Milvus）的向量检索效果，为AI应用提供了更精确和高效的数据处理能力。

然而，随着向量数据库的日益普及，关于专业化解决方案的必要性引起了争论。许多新创企业进入了向量数据库领域。许多传统的关系型和NoSQL数据库已经开始将向量视为重要的数据类型，并声称能够在各种情况下替代专业的向量数据库。

随着我们步入2024年，现在是回顾整个向量数据库行业的好时机，特别关注开源 Milvus。

## Milvus 在 2023 年的表现：数字不会说谎

[Milvus](https://zilliz.com/what-is-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns) 于 2019 年首次推出，开创了向量数据库的概念，并始终保持着高可靠性、可扩展性、搜索质量和性能的声誉。在 2023 年，Milvus 取得了令人瞩目的成果，并经历了重大变革，主要是由 LLMs 的迅猛发展和人工智能生成内容（AIGC）应用的蓬勃发展驱动的。以下是一些最能代表 Milvus 在 2023 年取得进展的关键数字。

### 滚动升级期间零停机

对于那些对向量数据库还不熟悉的人，它们的主要关注点集中在功能上，而不是运营维护。许多应用程序开发者在向量数据库的稳定性上付出的关注较少，因为他们的应用程序通常处于早期探索阶段。然而，如果你的 AIGC 应用程序旨在在生产环境中部署并实现最佳用户体验，稳定性就变得不可或缺。

Milvus 不仅注重功能，还通过在 Milvus 从版本 2.2.3 开始添加滚动升级来提高运营稳定性。经过持续的优化，这个功能可以确保在升级过程中零停机，而不中断业务流程。

### 生产环境中的3倍性能提升

提升向量搜索性能应该是向量数据库的主要目标。许多向量搜索解决方案选择基于适应[分层可导航小世界（HNSW）](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)算法，以快速进入市场。不幸的是，这意味着它们在实际生产环境中面临着重大挑战，特别是在高度筛选的搜索（超过90%）和频繁数据删除的情况下。

Milvus 专注于在任何开发阶段，特别是在生产环境中优化性能，在搜索性能方面取得了三倍的提升，尤其是在筛选搜索和流式插入/搜索情境中。

我们还推出了 [VectorDBBench](https://github.com/zilliztech/VectorDBBench)，一个开源的基准测试工具，以便开发人员可以在不同条件下评估向量数据库。与传统的评估方法不同，VectorDBBench 使用真实世界的数据进行评估，包括超大数据集或与实际嵌入模型数据类似的数据，为用户提供更深入的信息，以进行明智的决策。

### 在 Beir 数据集上提高了5%的召回率

虽然[密集嵌入](https://zilliz.com/learn/sparse-and-dense-embeddings?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)在向量搜索中证明是有效的，但在搜索姓名、物体、缩写和短查询上，它们必须赶上步伐。为了应对它们的局限性，Milvus引入了一种混合查询方法，将密集嵌入与稀疏嵌入集成在一起，以提高搜索结果的质量。这种带有重新排名模型的混合解决方案导致了在 [Beir 数据集](https://paperswithcode.com/dataset/beir)上召回率提高了5%，经我们的测试验证。

Milvus还推出了一种专为稀疏嵌入定制的基于图的检索解决方案，超越了传统搜索算法如 WAND 的性能。

在 [2023 年的 NeurIPS BigANN](https://big-ann-benchmarks.com/neurips23.html) 竞赛中，Zilliz 工程师 Zihao Wang 展示了 [Pyanns](https://big-ann-benchmarks.com/neurips23.html#winners)，这是一种搜索算法，明显优于稀疏嵌入搜索轨道中的其他参赛作品。这是我们为生产环境开发的稀疏嵌入搜索算法的前身。

### 大型数据集上节省了 10 倍的内存

在 2023 年，检索增强生成（RAG）是向量数据库最流行的用例。然而，[RAG 应用程序](https://thenewstack.io/discover-the-performance-gain-with-retrieval-augmented-generation/)中向量数据量的增加对这些应用程序提出了存储挑战。当转换后的向量的体积超过原始文档块的体积时，这个挑战尤为明显，潜在地升高内存使用成本。例如，将文档分成块后，从一个 500 令牌块（约 1kb）转换的 1536 维 float32 向量（约 3kb）的大小大于 500 令牌块。

Milvus 是第一个支持基于磁盘的索引的开源向量数据库，实现了5倍的内存节省。截至2023年底，[Milvus 2.3.4](https://milvus.io/docs/release_notes.md#v234?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns) 引入了使用内存映射文件（[MMap](https://zilliz.com/blog/milvus-introduced-mmap-for-redefined-data-management-increased-storage-capability?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)）将标量和向量数据/索引加载到磁盘的功能。与传统的内存索引相比，这一进步使内存使用减少了10倍以上。

### 20个 Milvus 版本发布

在2023年，我们发布了20个版本，这证明了300多名社区开发者的奉献精神，以及我们在开发中秉持用户驱动的承诺。

举例来说，Milvus 2.2.9 引入了[动态模式](https://zilliz.com/blog/what-is-dynamic-schema?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)，标志着从优先考虑性能转向增强可用性的重要转变。[Milvus 2.3](https://milvus.io/blog/unveiling-milvus-2-3-milestone-release-offering-support-for-gpu-arm64-cdc-and-other-features.md?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns) 引入了关键功能，如 upsert、[范围搜索](https://zilliz.com/blog/unlock-advanced-recommendation-engines-with-milvus-new-range-search?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)、余弦度量等，所有这些都是由我们用户社区的特定需求和反馈驱动的。

### 单一集群中百万租户

实现[多租户](https://thenewstack.io/avoiding-the-pitfalls-of-multitenancy-in-kubernetes/)对于开发 RAG 系统、AI 代理和其他 LLM 应用程序至关重要，满足了用户对数据隔离的增强需求。对于业务到客户（B2C）的企业，租户数量可能激增到百万级别，使得对用户数据进行物理隔离变得不切实际（例如，在关系数据库中创建数百万个表是不太可能的）。Milvus 引入了分区键功能，允许根据分区键进行高效、逻辑上的隔离和数据过滤，这在大规模情境下非常方便。

相反，习惯处理数以万计租户的企业对涉及物理资源隔离的更微妙策略受益匪浅。最新的 Milvus 2.3.4 带来了增强的内存管理、协程处理和 CPU 优化，使得在单个集群内创建数以万计的表更加容易。这一增强还通过提高效率和控制，满足了 B2B 企业的需求。

### 1000 万次 Docker 镜像拉取

随着 2023 年接近尾声，Milvus 已经达到了 [1000 万次 Docker 镜像下载](https://hub.docker.com/r/milvusdb/milvus)。这一成就表明开发者对 Milvus 的兴趣增加，突显了它在向量数据库领域日益重要的地位。作为一个云原生向量数据库，Milvus 与 Kubernetes 和更广泛的容器生态系统无缝集成。

### 单一集合中的 100 亿实体

虽然可扩展性目前可能没有夺取人们在 AI 现象中的注意力，但它在其长期成功中扮演着关键角色。Milvus 向量数据库可以轻松扩展，以容纳数十亿的向量数据。Milvus 帮助一位 LLM 客户存储、处理和检索了惊人的 100 亿数据点，这仅仅是 Milvus 处理海量数据的能力的一个例子。

## 超越数字: 对向量数据库的新见解

除了数字里程碑外，2023 年还为我们提供了有关向量搜索技术微妙细节和不断演变动力的宝贵见解。

### LLM 应用仍处于早期阶段

回顾移动互联网繁荣的早期，许多开发者创建了简单的应用，如手电筒或天气预报，最终被整合到智能手机操作系统中。去年，大多数人工智能原生应用，如 AutoGPT，在 GitHub 上迅速获得了 100,000 颗星，虽然没有提供实际价值，但代表了有意义的实验。对于向量数据库应用程序，当前的用例可能只是人工智能原生转型的第一波浪潮。

### 向量数据库朝着多样化方向发展

类似于数据库演变为在线事务处理（OLTP）、在线分析处理（OLAP）和NoSQL等类别，向量数据库显示出明显的多样化趋势。脱离对在线服务的传统关注，离线分析获得了显著的推动。这一转变的另一个显著实例是2023年推出的开源语义缓存 [GPTCache](https://zilliz.com/blog/building-llm-apps-100x-faster-responses-drastic-cost-reduction-using-gptcache?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)。它通过存储和检索语言模型生成的响应，提升了基于GPT的应用的效率和速度。

### 向量操作变得更加复杂

在支持[近似最近邻（ANN）](https://zilliz.com/glossary/anns?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)搜索的同时是向量数据库的一个定义特征，但这并不是孤立存在的。仅仅保持最近邻搜索就足以将数据库归类为向量或人工智能原生数据库的普遍观念，过于简化了向量操作的复杂性。在基本的混合标量过滤和向量搜索能力之外，专为人工智能原生应用定制的数据库应支持更复杂的语义能力，如神经网络（NN）过滤、K最近邻（KNN）连接和聚类查询。

### 弹性可扩展性对于人工智能原生应用至关重要。

人工智能应用的指数增长，例如 ChatGPT 在两个月内积累了超过1亿月活跃用户，可能超过了先前的任何业务轨迹。一旦企业实现增长的步伐，迅速从100万扩展到10亿数据点变得至关重要。人工智能应用开发者受益于由LLM提供商设定的按需付费服务模型，从而大大降低了运营成本。同样，存储与此定价模型一致的数据对开发者有利，使他们能够更多关注核心业务。

与语言模型（LLMs）和其他各种技术系统不同，向量数据库以有状态的方式运作，需要持久性数据存储。因此，在选择向量数据库时，优先考虑弹性和可扩展性至关重要，以确保与不断演变的人工智能应用的动态需求保持一致。

### 在向量数据库中进行机器学习可以取得非凡的成果

在2023年，我们在AI4DB（面向数据库的人工智能）项目中的大量投资取得了显著的成功。作为我们努力的一部分，我们向 [Zilliz Cloud](https://zilliz.com/cloud?utm_source=vendor&utm_medium=referral&utm_campaign=2023-01-10_blog_2023-milvus_tns)（完全托管的 Milvus 解决方案）引入了两个关键功能：1）AutoIndex，一种基于机器学习的自动参数调整索引，以及2）基于数据聚类的数据分区策略。这两者在显著增强 Zilliz Cloud 的搜索性能方面发挥了关键作用。

### 开源 vs 闭源

像 OpenAI 的 GPT 系列和 Claude 等领先的闭源LLMs使开源社区在计算和数据资源上处于不利地位。

然而，在向量数据库领域，开源最终将成为用户的首选。选择开源带来了许多优势，包括更多样化的用例、加速的迭代和培育更健壮的生态系统。

此外，数据库系统非常复杂，不能承受通常与LLMs相关联的不透明性。用户在选择最合理的数据库使用方法之前必须充分了解数据库。而且，开源所蕴含的透明度使用户能够根据其需求定制数据库。

## 结语与新的开始

看到2023年创立的许多人工智能初创公司的创新，真是令人兴奋。这让我想起我最初进入VectorDB开发领域的原因。在2024年，所有这些创新应用将真正获得推动，吸引的不仅仅是资金，还有真正付费的客户，这将为这些开发人员带来不同的需求。

我们对未来一年中在向量数据库中看到更多多样化的应用和系统设计充满期待和兴奋。

让我们在2024年创造非凡的成就！
