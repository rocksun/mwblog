
<!--
title: 查询图数据库的新ISO标准GQL
cover: https://cdn.thenewstack.io/media/2024/04/dba5470c-map.png
-->

国际标准化组织 (ISO) 已发布一项用于查询图表的国际标准，称为图查询语言 (ISO/IEC 39075:2024)。

> 译自 [GQL: A New ISO Standard for Querying Graph Databases](https://thenewstack.io/gql-a-new-iso-standard-for-querying-graph-databases/)，作者 Joab Jackson。

图数据库现已正式成为计算机科学领域的一流实体。

国际标准化组织 (ISO) 发布了用于查询图表的国际标准，称为[图查询语言(Graph Query Language)](https://www.iso.org/standard/76120.html)（ISO/IEC 39075:2024）。

这是 ISO 自 1987 年批准 [SQL](https://thenewstack.io/how-to-write-sql-queries/) 以来发布的第一种数据库查询语言。标准机构花了五年多时间对细节进行分类。

[Neo4j](https://thenewstack.io/neo4j-funding-shows-graph-databases-gained-acceptance/) 的首席技术官 [Philip Rathle](https://www.linkedin.com/in/prathle/) 在接受 TNS 采访时表示：“没有什么是像国际正式标准这样的，它与 SQL 来自同一组织，是 SQL 的兄弟，可以为 GQL 的主流价值大肆宣传。”

[ISO/IEC 联合技术委员会 1/AG 1](https://www.linkedin.com/company/jtc1news/) 的通信负责人 [Tony Holland](https://www.linkedin.com/in/tonyhollanduk/) 在一份声明中表示：“该版本标志着查询语言历史上的新篇章，彻底改变了我们与互连数据交互并利用其力量的方式。”“GQL 代表了数据查询和操作方面的重要一步，提供了一种用于导航复杂图结构的统一且富有表现力的语言。”

除了 Neo4J 的专业知识外，来自 [HypergraphDB](https://hypergraphdb.org/)、[Redis Labs](https://redis.com/?utm_content=inline+mention)、[TigerGraph](https://thenewstack.io/tigergraph-graph-dbs-to-become-a-must-have-in-2022/)、[Oracle](https://developer.oracle.com/?utm_content=inline+mention) 和德国波恩大学的工程师 [也参与了该项目](https://www.gqlstandards.org/existing-languages)。

![](https://cdn.thenewstack.io/media/2024/04/bd89fc7a-graph-visualization-example-1024x825-1.png)

*图数据库的可视化（由 Neo4J 提供）*

## 标准化的优势

全球标准机构批准该语言，就像它对 SQL 本身所做的那样，确保了它的稳定性，鼓励用户和工具供应商进一步投资该技术。

图计算的基础是[属性图](https://neo4j.com/blog/gql-international-standard/)，它在描述动态变化的数据方面更胜一筹。

图数据库已[广泛使用了几十年](https://thenewstack.io/neo4j-biggest-break-in-data-journalism/)，直到最近，该形式才引起了人们对成为[关键组件](https://www.gartner.com/en/articles/understand-and-exploit-gen-ai-with-gartner-s-new-impact-radar)的新兴趣[大型语言模型](https://thenewstack.io/how-to-cure-llm-weaknesses-with-vector-databases/)的[生成式 AI 应用程序](https://thenewstack.io/will-generative-ai-kill-devsecops/)。图模型可以可视化复杂、相互连接的系统。

Rathle 解释说，LLM 的缺点在于它们在某种程度上是黑匣子。“无法理解语言模型背后的推理。它只是遵循神经网络并做自己的事情，”他说。知识图可以作为外部存储器，一种可视化 LLM 如何构建其世界观的方式。

Rathle 说：“因此，我可以追踪图并了解它为何得出该答案。”

Rathle 说，图数据库还广泛用于医疗保健公司进行药物发现，以及飞机和其他制造商将其用作可视化复杂系统设计的一种方式。“你拥有所有这些级联依赖关系，并且该计算在图中非常有效，”Rathle 说。

## GQL 中有什么？

GQL 标准长达 600 多页，引用了 400 多篇论文。

组件包括：

- 仅图数据类型（顶点、边、路径）
- 标量数据类型
- 标量类型的运算、函数和谓词
- 事务模型
- 安全模型
- 图模式匹配
- 图类型，用于约束图的内容

[GQL](https://www.gqlstandards.org/home) 基于 [Cypher](https://neo4j.com/product/cypher-graph-query-language)——以及它的开源变体 [OpenCypher](https://opencypher.org/)——这是最流行的图数据库系统之一 [Neo4j](https://neo4j.com/) 的查询语言。

GQL 的核心语法与 Cypher 基本相同，MATCH … RETURN 语句的工作方式相同。查询：

```
MATCH (movie:Movie)
RETURN movie.title
```

将[返回数据库中具有“Movie”标签的所有节点](https://neo4j.com/docs/cypher-manual/current/clauses/match/)。

```
Table 2. Result
movie.title
"Wall Street"
 
"The American President"
 
Rows: 2
```

GQL 还使用相同的基本表达式、线性组合和 Cypher 的其他方面。

例如，这个来自 Neo4J 的示例查询显示了在 22:37 停靠在 Denmark Hill 的交通服务的下个停靠站：

```
MATCH (n:Station {name: 'Denmark Hill'})&lt;-[:CALLS_AT]-
(s:Stop WHERE s.departs = time('22:37'))-[:NEXT]-&gt;
(:Stop)-[:CALLS_AT]-&gt;(d:Station)
RETURN d.name AS nextCallingPoint
```

结果为…

```
Table 4. Result
nextCallingPoint
"Clapham High Street"
```

不过，Cypher 和 GQL 之间存在一些[基本差异](https://neo4j.com/blog/cypher-path-gql/)。

GQL 将使用关键字 `INSERT` 向图中添加节点或关系，而 Cypher 使用 `CREATE`。`FOR` 语句取代了 Cypher 的 `UNWIND`。

其他[图查询语言](https://www.nebula-graph.io/posts/graph-query-languages-you-should-know)包括[NebulaGraph](https://www.nebula-graph.io/) 的 NQL，[Apache Tinkerpop 的 Gremlin](https://thenewstack.io/tinkerpop-growing-graph-database-popularity/)，[RDF 的 SPARQL](https://www.w3.org/TR/rdf11-concepts/) 以及 [ArangoDB](https://arangodb.com/) 的 AQL 。还有 [GraphQL 语言](https://thenewstack.io/graphql-growth-explodes-but-so-do-problems-federated-graphs-solve/)，这是一种面向图的查询语言，用于构建 API。

从现有的图查询语言升级的路径应该相当容易，至少如果这些实现基于 Cypher 的话。据 Rathlee 称，至少有十几个不同的图数据库系统建立在 OpenCypher 之上，包括来自 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 的流行的 [Neptune](https://aws.amazon.com/neptune)。
