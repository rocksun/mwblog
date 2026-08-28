<!--
title: 为什么基础RAG在多跳推理中表现不佳（以及GraphRAG如何解决它）
cover: https://cdn.thenewstack.io/media/2026/08/ea391b28-rick-rothenberg-vojwkhu64fc-unsplash.jpg
summary: 文章探讨了基础RAG系统在处理多跳推理和全局摘要时的局限性，指出其单纯依赖语义相似度的缺陷。通过引入GraphRAG，结合知识图谱的结构化关系与向量搜索，能有效解决复杂关联查询，并提供了基于Python和Neo4j的实战部署方案与工程注意事项。
-->

文章探讨了基础RAG系统在处理多跳推理和全局摘要时的局限性，指出其单纯依赖语义相似度的缺陷。通过引入GraphRAG，结合知识图谱的结构化关系与向量搜索，能有效解决复杂关联查询，并提供了基于Python和Neo4j的实战部署方案与工程注意事项。

> 译自：[Why basic RAG fails at multi-hop reasoning (and how GraphRAG fixes it)](https://thenewstack.io/graphrag-multi-hop-reasoning-python/)
> 
> 作者：Emmanuel Akita

当前的AI工程设计中，LLM（大语言模型）的构建方法过于简单化了。按照回音室效应的观点，解决LLM幻觉问题很简单：只需设计一个标准的检索增强生成（RAG）系统，将PDF文档拆分为1,000个token的块，对其进行嵌入（Embedding），存入向量数据库，然后执行余弦相似度搜索即可。

这在实际部署之前一切看起来都很完美……

部署后，企业很快就会发现，仅使用分块文本进行检索无法很好地处理复杂问题。标准RAG假设语义相似度意味着相关性，但事实并非总是如此。当用户提出一个需要通过“概念C”连接“概念A”和“概念B”的“多跳”问题时，标准RAG往往失效，因为这些概念通常不会同时出现在同一个文本块中。RAG在全局摘要任务（例如“我们所有合规报告中讨论的主要风险因素是什么？”）上也表现得很差。

> “标准RAG假设语义相似度意味着相关性，但事实并非总是如此。”

如果您正在为企业系统设计AI，您需要结构化推理。分块文本本身没问题，但不要随机分块。您真正需要的是GraphRAG。

GraphRAG结合了知识图谱的结构化知识和向量搜索的语义能力，提供了一种强大的组合方案。本教程将解释您当前的流程为何失败，并帮助您使用Python实现GraphRAG工作流。

## 朴素向量搜索的局限性

现在，让我们打破“向量嵌入将拯救一切”这一简单误区！

假设您有一个存储在[向量数据库](https://thenewstack.io/silent-llm-hallucination-loop/)中的企业合同数据集。

* **块 1**：“Acme Corp 在 2022 年收购了 BetaTech。”
* **块 2**：“Sarah Connor 于 2023 年被任命为 BetaTech 的 CEO。”

**查询**：“谁领导了被 Acme Corp 收购的那家公司？”

朴素向量搜索会嵌入查询并找到最接近的块。不可避免的是，它会找到与“Acme Corp”和“领导力”高度相似的块，但“块 2”会被忽略，因为“Sarah Connor”和“BetaTech 的 CEO”在语义上与“Acme Corp”毫无关联。

常规RAG方法缺乏不同实体之间的结构化关系。要回答多跳查询，您需要理解 `(“Acme Corp”) - [ACQUIRED]` -> `(BetaTech)` 这种关系，以及 `(“Sarah Connor”) - [LEADS] -> (BetaTech)` 这种关系。

这就是 GraphRAG 的用武之地。

## 进入 GraphRAG

GraphRAG 需要 LLM 在摄入步骤处理文档，提取节点（实体）和边（关系），从而从您的文本块中创建知识图谱。

与传统方法中查询由孤立的文本字符串组成不同，在 GraphRAG 中，我们首先通过向量搜索确定起始节点，然后遍历图的关系，获取高度相关的子图，以便进行[LLM 推理](https://thenewstack.io/how-diffusion-based-llm-ai-speeds-up-reasoning/)。

最近，Neo4j 的 [neo4j-graphrag](https://github.com/neo4j/neo4j-graphrag) 等框架使得这种架构变得普及。我们将使用该框架构建一个稳健的流水线，执行数据摄入、模式强制（schema enforcement）和图遍历。

## 实践实现：使用 Python 构建 GraphRAG

我们将构建一个[能够摄入非结构化文本数据](https://thenewstack.io/data-pipelines-serve-ai/)、构建知识图谱并通过动态 Cipher 遍历查询图的流水线。

### 第一步：安装依赖

您需要一个可用的 Neo4j 数据库（本地或云端）以及以下软件包：

```bash
pip install neo4j neo4j-graphrag openai python-dotenv
```

### 第二步：初始化连接与生产环境防护

生产级的流水线需要妥善的凭据管理和弹性机制。

GraphRAG 的摄入在 LLM API 请求方面非常昂贵。如果不配置速率限制处理程序，您的流水线在处理第一个真实文档时就会出现 `RateLimitError`。

```python
import os
from neo4j import GraphDatabase
from neo4j_graphrag.llm import OpenAILLM
from neo4j_graphrag.embeddings import OpenAIEmbeddings 
from neo4j_graphrag.utils.rate_limit import RetryRateLimitHandler

# 初始化 Neo4j 驱动
neo4j_uri = os.environ.get("NEO4J_URI")
neo4j_user = os.environ.get("NEO4J_USERNAME")
neo4j_password = os.environ.get("NEO4J_PASSWORD")

if not all([neo4j_uri, neo4j_user, neo4j_password]):
    raise ValueError("缺少必要的 Neo4j 环境变量 (NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)。")

driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
driver.verify_connectivity() 

# 使用严格速率限制初始化 LLM，以应对繁重的提取任务
llm = OpenAILLM(
    model_name="gpt-4o",
    model_params={"temperature": 0},
    rate_limit_handler=RetryRateLimitHandler(max_attempts=5, min_wait=2.0)
)
embedder = OpenAIEmbeddings(model="text-embedding-3-small")
```

### 第三步：在知识图谱构建器中强制执行模式

非结构化的图不过是一个杂乱无章的数据库。一旦您不提供适当的模式（schema），您的 LLM 就会产生幻觉，随意定义实体标签，导致“Acme Corp”、“Acme Corporation”和“Ame”等重复节点。我们将预先构建架构并将其输入到流水线中。

> “非结构化的图不过是一个杂乱无章的数据库。”

```python
from neo4j_graphrag.experimental.pipeline.kg_builder import SimpleKGPipeline

# 定义明确的模式以防止提取过程中出现 LLM 幻觉
schema = {
    "node_types": ["Organization", "Person", "Technology"],
    "relationship_types": ["ACQUIRED", "LEADS", "DEVELOPS"],
    "patterns": [
        ("Organization", "ACQUIRED", "Organization"),
        ("Person", "LEADS", "Organization")
    ]
}

# 定义强制执行该模式的流水线
kg_builder = SimpleKGPipeline(
    llm=llm,
    driver=driver,
    embedder=embedder,
    schema=schema
)

sample_text = """
Acme Corp 在 2022 年收购了 BetaTech。 
2023 年，Sarah Connor 被任命为 BetaTech 的 CEO，以推动 AI 计划。
"""

import asyncio

# 执行提取和图填充
asyncio.run(kg_builder.run_async(text=sample_text)) 
```

*工程备注：在底层，该流水线仍然使用 `FixedSizeSplitter` 分割您的文本。不同之处在于，它在保存之前会利用 LLM 从这些块中提取语义架构。*

### 第四步：向量 Cipher 检索器

多跳推理正是在这里实现的。普通的向量检索器只能提供节点。为了跨图遍历，我们使用 `VectorCypherRetriever`。我们将嵌入查询，确定语义入口点，最后对所有 1 跳连接的邻居执行 Cipher 查询。

```python
from neo4j_graphrag.retrievers import VectorCypherRetriever

# 定义遍历逻辑：查找向量匹配项，然后扩展 1 跳以获取关系
traversal_query = """
MATCH (node)[r](neighbor)
RETURN "Entity: " + coalesce(node.id, '') + " (Info: " + coalesce(node.text, '') + ") | " +
"Relationship: " + type(r) + " | " +
"Neighbor: " + coalesce(neighbor.id, '') + " (Info: " + coalesce(neighbor.text, '') + ")" AS text,
score
""" 

# 初始化 VectorCypherRetriever 以启用实际的 GraphRAG
retriever = VectorCypherRetriever(
    driver=driver,
    index_name="entity_vector_index",
    embedder=embedder,
    retrieval_query=traversal_query
)

query = "谁领导了被 Acme Corp 收购的那家公司？"

# 根据查询检索连接的上下文
retrieved_context = retriever.search(query_text=query, top_k=3)

print(retrieved_context)
```

检索到的上下文包括 BetaTech、它被 Acme Corp 收购的事实，以及 Sarah Connor 领导它的事实，因为我们提供了用于检索关系的特定模式。LLM 现在拥有了提供准确回答所需的所有事实。

## 经验教训：工程师在采用 GraphRAG 前必须了解的事项

如果您想升级您的 RAG 系统，请考虑以下权衡：

1. **摄入成本高**：传统 RAG 成本较低，因为嵌入模型很便宜。在 GraphRAG 中摄入每个文档块，您需要像 GPT-4o 这样的 LLM 来提取实体。请谨慎过滤您的企业数据。
2. **模式设计非选配**：如第三步所示，不要忽视数据建模。模式是区分高效检索引擎和混乱节点集的关键。
3. **可观测性更优**：要调试朴素 RAG，您需要检查巨大的浮点数组；而要调试 GraphRAG，您只需查看 Neo4j 仪表板以查看节点即可。很容易就能看出 LLM 是否产生了幻觉。

标准的向量搜索是一个非常强大的解决方案，但将其视为企业 AI 的“一刀切”式方案是一种投机取巧。现实世界的用例需要明确的数据建模和确定性的搜索能力。

> “标准的向量搜索是一个非常强大的解决方案，但将其视为企业 AI 的‘一刀切’式方案是一种投机取巧。”

GraphRAG 在设计上需要更强的意图性、遵循严格的准则以及更高的前期计算投入。然而，回报是巨大的：GraphRAG 让您拥有了做真正有价值事情的能力——对数据进行多跳推理，这正是企业所渴望的。"}