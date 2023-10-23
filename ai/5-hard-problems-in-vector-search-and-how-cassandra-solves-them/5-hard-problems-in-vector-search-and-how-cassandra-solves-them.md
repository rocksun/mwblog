<!--
# 五个向量搜索难题，以及Cassandra的解决办法
https://cdn.thenewstack.io/media/2023/09/674da981-globalisation-3390877_1280-1024x614.jpg
Feature image by Pete Linforth from Pixabay.
 -->

向量搜索引擎是数据库一个重要的新增功能，它面临着扩展性、垃圾回收、并发性、磁盘利用效率和组合能力等多方面的架构挑战。本文将介绍DataStax如何在Astra DB和Apache Cassandra中添加这些功能。s

译自 [5 Hard Problems in Vector Search， and How Cassandra Solves Them](https://thenewstack.io/5-hard-problems-in-vector-search-and-how-cassandra-solves-them/) 。

向量搜索是生成式AI工具的关键组成部分，因为像[FLARE](https://arxiv.org/abs/2305.06983)这样的检索增强生成(RAG)可以[帮助大语言模型在避免混淆的同时融入最新、定制化的信息](https://hackernoon.com/how-llms-and-vector-search-have-revolutionized-building-ai-applications)。与此同时，向量搜索是一个功能而不是一个独立的产品——您需要查询向量与数据集其他部分的关联，而不仅仅是隔离查询，并且您不应该需要构建管道来同步向量存储中的其他数据。

今年，我们看到向量搜索产品和项目数量爆炸式增长，这使得在众多选择中选取成为一项严峻的工作。在研究可选方案时，您需要考虑以下难题以及解决它们的不同方法。本文将介绍DataStax如何在设计Astra DB和Apache Cassandra的向量搜索实现时解决这些挑战。

## 维度的诅咒

这些难题的核心在于研究人员所说的“[维度的诅咒](https://en.wikipedia.org/wiki/Curse_of_dimensionality)”。这在实践中意味着，在2D或3D空间中仍然可用的算法[，如k-d trees](https://en.wikipedia.org/wiki/K-d_tree)，当向量的维度达到10、100或1000时就会崩溃。结果是，使用高维向量进行精确相似性搜索没有捷径；为了获得对数时间复杂度的结果，我们需要使用近似最近邻(ANN)算法，这带来了以下领域的挑战。

## 问题1: 横向扩展

许多向量搜索算法是为适应单机内存的数据集而设计的，[ann-benchmarks](https://ann-benchmarks.com/)的测试也仅限于此场景。对于学术界处理百万级文档或行数据这可能还行，但这距离真实世界的工作负载要求还有很大差距。

与任何其它领域一样，横向扩展需要复制和分区，以及处理失败复制、网络分区后的修复等子系统。

这对我们来说是一个简单的问题：扩展式复制是Cassandra的强项，将其与Cassandra 5.0中的SAI(存储连接索引 —— 参见[CEP-7](https://cwiki.apache.org/confluence/display/CASSANDRA/CEP-7%3A+Storage+Attached+Index)了解其工作原理，参见[SAI文档](https://docs.datastax.com/en/cql/astra/docs/developing/indexing/sai/sai-overview.html)了解如何使用它)结合，使我们的向量搜索实现几乎零成本地获得了强大的横向扩展能力。

![](https://cdn.thenewstack.io/media/2023/09/ddb066ee-datastax-01.png)

## 问题2: 高效的垃圾回收

这里的“垃圾回收”是指从索引中删除陈旧信息，包括清理已删除的行和处理索引向量值已更改的行。这可能看起来微不足道——在关系数据库世界中，这在40年前就已经成为一个基本解决的问题——但向量索引具有独特性。

关键问题是，我们目前所知提供低延迟搜索和高召回率结果的所有算法都是基于图的。还有许多其他向量索引算法可以使用——[FAISS](https://github.com/facebookresearch/faiss)实现了其中许多——但要么构建太慢，要么搜索太慢，要么召回率太低(有时兼具三者)无法作为通用解决方案。这就是目前我所知生产环境中的向量数据库都使用基于图的索引的原因，最简单的就是HNSW。HNSW(分层导航小世界图)[由Yury Malkov等人在2016年提出](https://arxiv.org/pdf/1603.09320)；这篇论文非常易读，我强烈推荐。关于HNSW的更多内容见下文。

图形索引的挑战在于，当行或文档发生更改时，您不能简单地将旧的(向量关联)节点移除；如果您这样做多次，您的图将不再能够执行其目的，即引导广度优先搜索快速定位包含所有相似向量的底层区域。

所以您需要定期重建索引以执行垃圾回收，但如何安排时间和组织重建呢？如果您每次更改时都重建全部，您将大大增加物理写入量；这称为写入放大。另一方面，如果从不重建则会在查询时额外过滤掉大量陈旧信息，形成“读取放大”。

这是Cassandra多年来一直在研究解决的问题空间。由于SAI索引与主存储生命周期绑定，它们也会参与Cassandra的[压缩](https://cassandra.apache.org/doc/latest/cassandra/operating/compaction/index.html)过程，这以对数方式增加存储单元大小，在读取和写入之间提供更好的平衡。

![](https://cdn.thenewstack.io/media/2023/09/9e2e7048-datastax-02.png)

## 边车: 云应用程序工作负载

DataStax Astra DB 建立在Apache Cassandra之上，为云应用程序工作负载提供一个平台。这意味着以下工作负载:

* **大规模并发** 每秒处理数千到数百万个请求，通常每个只检索几行。这就是为什么即使你能付得起Snowflake的费用，也无法在其上运行Netflix的原因:Snowflake和类似的分析系统只设计为处理每个运行数秒到数分钟甚至更长的几个并发请求。

* **大于内存** 如果您的数据集适合单台机器上的内存，那么使用什么工具都没关系。SQLite、MongoDB、MySQL都可以很好地工作。当情况不是这样时，事情会更具挑战性 —— 坏消息是向量嵌入通常每个几KB，比典型数据库文档大约一个数量级，所以您会相对快速地进入大于内存的规模。

* **应用的核心** 如果您不介意丢失数据，无论是因为数据不重要，还是因为您可以从记录的实际源重建数据，那么同样，使用什么工具都无关紧要。像Cassandra和Astra DB这样的数据库被构建为无论发生什么，都会保持您的数据可用和持久。

## 问题3: 并发性

我之前提到，著名的[ann-benchmarks](https://ann-benchmarks.com/)比较将所有算法限制为单个内核。虽然这营造了公平的比较环境，但它也削弱了那些可以利用过去20年来硬件改进的主要来源(并行计算)的算法的优势。

一个相关的问题是，ann-benchmarks只执行一种类型的操作: 首先构建索引，然后查询索引。处理与搜索交错的更新是可选的——事实上这可能是一种劣势；如果您知道不需要处理更新，您可以做出在人工基准测试上表现良好但不实用的简化假设。

如果您关心能够并发执行多种操作，或者需要在构建后继续更新索引，那么您就需要更深入地了解算法的工作原理和所涉及的权衡取舍。

首先，我所知道的所有通用向量数据库都使用基于图的索引。这是因为您可以在插入第一个向量后立即开始查询图形索引。大多数其他选项要求您在查询索引之前构建完整的索引，或者至少预先扫描数据以学习某些统计属性。

但是，即使在图形索引类别内，实现细节也非常重要。例如，我们最初以为我们可以使用Lucene的HNSW索引实现来节省时间，正如MongoDB、Elastic和Solr所做的那样。但我们很快了解到，Lucene只提供单线程的非并发索引构建。也就是说，您既不能在构建过程中查询它(这本应该是使用该数据结构的主要原因之一!)，也不能允许多线程并发构建。

HNSW论文中建议使用细粒度锁可以解决问题，但我们做得更好，实现了一个非阻塞索引，在[JVector](https://github.com/jbellis/jvector/)中开源。

JVector可以线性扩展到至少32个线程的并发更新。图中x轴和y轴均为对数缩放，显示线程数加倍可以使构建时间减半。

![](https://cdn.thenewstack.io/media/2023/09/670bd674-datastax-03.png)

更重要的是，JVector的非阻塞并发对混合搜索和更新的更实际的工作负载也有益处。这里比较了Astra DB(使用JVector)与Pinecone在不同数据集上的性能。尽管Astra DB在静态数据集上比Pinecone快约10%，但在同时索引新数据的情况下，它的速度要快8到15倍。我们根据Pinecone建议选择了他们提供的最佳Pod配置(Pod类型:p2 和 Pod 大小:x8，每个副本有两个Pod)，以追求更高吞吐量和更低延迟。Pinecone没有透露这对应于哪些物理资源。Astra DB方面，我们选择了默认的按用计费部署模式，不必担心资源选择，因为它是无服务器的。测试使用[NoSQLBench](https://github.com/nosqlbench/)执行。

![](https://cdn.thenewstack.io/media/2023/09/35f2874e-datastax-04.png)

Astra DB在实现更高性能的同时还能保持更高的召回率和精确度([F1值为召回率和精确度的组合](https://en.wikipedia.org/wiki/F-score))。

![](https://cdn.thenewstack.io/media/2023/09/28500f58-datastax-image.jpg)

## 问题4: 有效利用磁盘

我们最初采用[HNSW图形索引算法](https://arxiv.org/abs/1603.09320)，因为它构建索引快、查询快、准确性高，并且易于实现。但是，它有一个众所周知的缺点: 需要大量内存。

HNSW索引由多层组成，其中每一上层节点数约为前一层的10%。这使上层可以充当跳表，允许搜索快速定位包含所有向量的底层区域。

![](https://cdn.thenewstack.io/media/2023/09/a198b699-datastax-06.png)

然而，这种设计意味着(与所有图形索引一样)您不能简单依靠“磁盘缓存就能解决问题”，因为与普通数据库查询不同，图中的每个向量对搜索的相关性几乎相等(上层是一个例外，我们可以并且的确缓存上层)。

Cassandra大部分时间都在等待从磁盘读取向量。

为解决这个问题，我们实现了一种更高级的算法DiskANN，并作为独立的嵌入式向量搜索引擎[JVector](https://github.com/jbellis/jvector)开源(具体来说，JVector实现了DiskANN论文中描述的增量DiskANN算法)。简而言之，DiskANN使用比HNSW更长的单层图边、优化的向量和邻居布局来减少磁盘IOPS，并保持向量的压缩表示在内存中以加速相似性计算。这使Wikipedia工作负载的吞吐量提高了两倍以上。

下图显示了纯嵌入式场景下，不包含客户端/服务器组件的情况下，HNSW与DiskANN的对比。这测量了在Lucene(HNSW)和JVector(DiskANN)下搜索Deep100M数据集的速度。Lucene索引为55GB，包括索引和原始向量。JVector索引为64GB。测试环境为仅有24GB内存的MacBook，约为完整保存索引所需内存的三分之一。

![](https://cdn.thenewstack.io/media/2023/09/bfc355c6-datastax-08.png)

## 问题5: 组合能力

在数据库系统背景下，组合能力指无缝集成各种功能和能力的能力。当讨论集成新类别的功能(如向量搜索)时尤其重要。实际应用除了需要经典的[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)数据库功能，还需要向量搜索。

考虑Astra DB的简单[AI聊天机器人](https://docs.datastax.com/en/astra-serverless/docs/vector-search/chatbot-quickstart.html)应用示例。这是一个关于RAG的最纯粹的应用，它使用向量搜索为大语言模型提供适当的文档，以回答用户的问题。但是，即使是一个简单的演示，它仍需要对Astra DB执行“正常”的非向量查询，来检索对话历史，因为对话历史也必须随每个请求一起发送给大语言模型，以便它可以“记住”之前发生的事。所以关键查询包括:

- 为用户问题找到最相关文档(或文档片段)
- 检索用户对话的最后20条消息

在一个更实际的用例中，我们的一位解决方案工程师最近与一家亚洲公司合作，他们希望为产品目录添加语义搜索，但也希望启用基于词条的匹配。例如，如果用户搜索“红色球阀”，则希望将搜索限制在描述中匹配“红色”词条的产品，不管向量嵌入的语义相似度如何。那么除了经典功能比如会话管理、订单历史、购物车更新等，新的关键查询是：限制产品为包含所有引号内词条的产品，然后在结果中找到与用户查询最相似的。

从这个第二个例子可以清楚看出，应用不仅需要经典查询功能和向量搜索，而且它们经常需要在同一个查询中使用两者。

当前这个领域尚在发展阶段，主流做法是尝试在“普通”数据库中执行经典查询，在向量数据库中执行向量查询，然后当两者同时需要时，以一种特殊方式将它们拼接。这种方式容易出错、低效且昂贵；它的唯一优点是在有更好解决方案之前，可以让它工作。

在Astra DB中，我们在Cassandra SAI之上构建(并开源)了一个更好的解决方案。因为SAI允许创建自定义索引类型，所有的索引都绑定到Cassandra SSTable和压缩生命周期，所以Astra DB可以轻松地允许开发人员无缝混合使用布尔逻辑、基于词条的搜索和向量搜索，而无需管理和同步独立系统的额外开销。这为构建生成式AI应用的开发者提供了更高级的查询功能，可以提高生产力并缩短上市时间。

## 结论

向量搜索引擎是数据库的一个重要新增功能，它面临着扩展性、垃圾回收、并发性、磁盘利用效率和组合能力等多方面的架构挑战。我认为，通过为Astra DB构建向量搜索，我们能够发挥Cassandra的优势，为生成式AI应用开发者提供一流的用户体验。[欲了解更多Astra DB信息](https://www.datastax.com/products/datastax-astra)，请点击此处；如果您想深入了解向量搜索算法，请查看[JVector](https://github.com/jbellis/jvector)。
