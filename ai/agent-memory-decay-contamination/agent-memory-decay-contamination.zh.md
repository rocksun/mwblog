几个月前，我在评估一个表现异常的客户支持智能体。一位用户在周一咨询了计费问题，解决到一半中断了，周三回来继续。然而，周三的对话完全从零开始。智能体根本不知道用户是谁、之前的具体问题是什么、已经尝试过哪些方案，或者曾承诺过什么。

团队为这个智能体构建了坚实的基础：操作端点的幂等键、多步骤流程的工作流状态机、涉及计费的事务性写入。确保正确性的基础设施已经就位，但他们缺少的是一种让智能体召回并推理自身历史的能力，即让它知道：两天前，它曾向这位用户承诺过一笔尚未发放的退款。

这就是我想讨论的问题。不是那些优秀系统工程已经解决的智能体可靠性问题，而是更高、更难的一层：智能体“记忆”的能力。

## 首先，记忆不是什么

太多关于[智能体记忆架构](https://thenewstack.io/ai-agent-memory-architecture/)的讨论都跑偏了，因为人们对这个词的用法各不相同。让我先澄清三点。

**记忆不是幂等性。** 如果你的智能体因为同一个请求两次触发端点而执行了两次相同的动作，修复方案是幂等键。智能体不需要记忆，系统需要识别重复。**记忆不是工作流状态。** 如果你的智能体处于流程中途，修复方案是记录当前步骤并限制合法转换的状态机。**记忆不是事务一致性。** 如果两个智能体准备操作同一份数据，修复方案是数据库级的隔离。

这三者都是必要的，但它们都不是记忆。它们能保证单个动作的正确性，却不能赋予智能体历史感。

## 记忆究竟是什么

我认为智能体记忆由五种必须协同工作的能力组成。持久化存储只是其中之一，也是最容易实现的一个，而其他能力正是大多数生产环境智能体的短板。

*   **持久化（Persistence）：** 智能体的历史记录在会话结束、进程重启和部署后依然存在。通过写入数据库即可解决。
*   **筛选（Selection）：** 智能体决定哪些内容值得记住。永久存储每一场对话的每一个 Token 既昂贵又会适得其反，这会在召回时稀释信号。
*   **压缩（Compression）：** 原始历史被总结为有用的信息。两小时的对话变成一段文字加结构化事实。没有压缩，检索成本会随交互时间线性增长。
*   **衰减与遗忘（Decay and forgetting）：** 旧记忆的重要性低于新记忆，有些记忆则应当被遗忘。如果没有衰减，陈旧信息与新鲜信息的权重相同，这正是 RAG 流水线误导你的方式，也是我[上一篇文章的主题](https://thenewstack.io/rag-pipeline-hybrid-search/)。
*   **防污染（Contamination prevention）：** 错误的记忆比没有记忆更糟。错误的事实一旦存储，就会污染未来的每一次决策。真正的记忆系统会标记不确定的记忆，在它们被矛盾时降级，并在证明错误时将其隔离。

大多数关于智能体记忆的讨论都将这五点简化为第一点。他们争论该用哪个数据库存储智能体状态，并认为问题已解决。但没有筛选的持久化会导致智能体变慢；没有压缩会导致成本激增；没有衰减会导致智能体自信地犯错；没有防污染则会让智能体随着时间推移变得越来越笨。这五者缺一不可，而底层基座决定了你能构建什么样的架构。

> “没有筛选的持久化会导致智能体变慢；没有压缩会导致成本激增；没有衰减会导致智能体自信地犯错；没有防污染则会让智能体变得越来越笨。”

## 一个实用的分类法

记忆是有结构的。借鉴认知科学为我提供了一套词汇，用于诊断[智能体架构在何处失效](https://thenewstack.io/serverless-cloud-architecture-is-failing-modern-ai-agents/)。

*   **工作记忆（Working memory）** 是上下文窗口：当前任务、当前轮次。快速但短暂。这是目前大多数智能体拥有并容易与通用记忆混淆的部分。
*   **情节记忆（Episodic memory）** 是特定过去交互的历史，带有丰富的元数据：人物、事件、时间及结果。
*   **语义记忆（Semantic memory）** 是提取出的知识。例如：“该客户偏好早班机”、“财务 API 返回的金额以分为单位”。它是通过含义而非时间来查询的。
*   **程序记忆（Procedural memory）** 是习得的行为：哪些工具序列比其他的更有效。目前几乎没有人将其应用于生产环境。这是另一篇文章的主题。

工作记忆是一个提示词字符串。情节记忆需要结构化的时间序列查询。语义记忆[需要向量搜索](https://thenewstack.io/why-developers-need-vector-search/)。本文接下来的部分将聚焦于情节记忆和语义记忆，这也是生产环境真正的差距所在。

## 为什么单一用途的存储难担大任

大多数团队首先想到的是 Redis。快速、熟悉，非常适合工作记忆。问题在于键值存储只提供一种访问模式：按键获取。这在情节召回中会失效，因为情节召回需要的查询类似于：“过去 30 天内我为该地区用户发放的所有成功退款”。这是一个关系型查询，而不是简单的键查找。

团队想到的第二件事是向量数据库。嵌入过去的交互，按相似度搜索。这对语义记忆很有用，但在情节召回中表现不佳，因为情节召回通常需要精确的谓词：特定的用户、特定的时间窗口、特定的结果。当你需要 WHERE 子句时，余弦相似度帮不上忙。而且向量存储通常无法与你的应用程序数据进行关联（Join），这意味着智能体无法在了解用户背景的情况下推理记忆。

此外还有污染处理问题。当发现一个记忆是错误的时候，你需要更新或废弃它。在向量存储中，这意味着重新索引；在键值存储中，是大规模缓存失效；而在支持向量的关系型数据库中，这只是一个 UPDATE。记忆系统的生死取决于错误记忆被清理的可靠程度。

## 模式设计与诚恳的告诫

这是一个在单一数据库中处理情节和语义记忆层的参考模式（Schema）。

```sql

-- Episodic memory: what happened, with outcomes
CREATE TABLE episodic_memory (
  id           BIGINT PRIMARY KEY AUTO_INCREMENT,
  agent_id     VARCHAR(64) NOT NULL,
  user_id      BIGINT NOT NULL,
  session_id   BIGINT NOT NULL,
  action_type  VARCHAR(100) NOT NULL,
  summary      TEXT,           -- compressed form
  raw_payload  JSON,           -- full detail, kept for audit
  outcome      ENUM('success','failure','pending'),
  confidence   FLOAT DEFAULT 1.0,
  superseded_by BIGINT NULL,   -- contamination invalidation
  created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  embedding    VECTOR(1536),
  INDEX idx_agent_user_time (agent_id, user_id, created_at),
  INDEX idx_embedding USING HNSW (embedding)
);
-- Semantic memory: distilled knowledge, with decay metadata
CREATE TABLE semantic_memory (
  id           BIGINT PRIMARY KEY AUTO_INCREMENT,
  agent_id     VARCHAR(64) NOT NULL,
  user_id      BIGINT,
  fact         TEXT NOT NULL,
  confidence   FLOAT DEFAULT 1.0,
  source_count INT DEFAULT 1,
  last_confirmed_at DATETIME NOT NULL,
  contradicted_at   DATETIME NULL,
  created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  embedding    VECTOR(1536),
  INDEX idx_embedding USING HNSW (embedding)
);

```

相比一年前我写的简单模式，这里增加了几个细节：

*   **同时包含 `summary` 和 `raw_payload` 列。** 压缩不是可选的。智能体在召回时读取 `summary`；`raw_payload` 保留用于审计和重新总结。
*   **`confidence` 和 `superseded_by`。** 记忆不是不可变的。`superseded_by` 是针对污染的软删除指针。当记忆 A 被记忆 B 反驳时，A 指向 B 并在召回中被排除。原始记录不会被删除，因为审计很重要。
*   **`source_count` 和 `last_confirmed_at`。** 经过十次交互证实的实相比证实一次的事实更可靠。两年前最后证实的事实权重应低于昨天证实的。这些数据会喂给召回时应用的衰减函数，而不是在写入时应用。

**数据保留，权重改变。** 这是贯穿上述内容的核心原则。记忆记录不应被重写或删除，而应被标记、衰减或取代。

## 体现真实记忆行为的召回查询

有了这个模式，召回查询可以表达比“查找相似内容”更复杂的行为。这包括通过新鲜度和置信度加权的相似度衡量，同时排除被污染的记忆。

```sql

-- Semantic recall with decay and contamination filtering
SELECT fact,
       confidence
       * EXP(-DATEDIFF(NOW(), last_confirmed_at) / 90.0) AS effective_weight,
       VEC_COSINE_DISTANCE(embedding, @task_vec) AS distance
FROM semantic_memory
WHERE (user_id = @user_id OR user_id IS NULL)
  AND contradicted_at IS NULL
  AND VEC_COSINE_DISTANCE(embedding, @task_vec) < 0.30
ORDER BY distance, effective_weight DESC
LIMIT 10;

```

衰减项 `EXP(-days/90)` 的半衰期约为 60 天。客户偏好衰减较慢，库存事实衰减较快。一个真正的记忆系统会针对每种记忆类型调整此参数。

这些查询在做真正的记忆处理。它们不只是检索行，而是在建模置信度如何衰减、污染如何传播、时效性如何与相关性相互作用。数据库是底座，智能存在于查询中，而非数据行中。

## 更新记忆：乐观与悲观模式

记忆并非一次性写入的。随着新证据的出现，置信度会更新，记忆会被取代。由于这些更新可能并发发生，我们需要深思熟虑地进行并发控制。有两种常见模式，其区别很重要，因为它们经常被混淆。

悲观锁先获取锁并在操作期间一直持有。在预期存在冲突且操作简短时使用：

```sql

-- Pessimistic: lock the row, then update
BEGIN;

SELECT confidence, source_count
FROM semantic_memory
WHERE id = @memory_id
FOR UPDATE;

-- Application computes new confidence

UPDATE semantic_memory
SET confidence = @new_confidence,
    source_count = source_count + 1,
    last_confirmed_at = NOW()
WHERE id = @memory_id;

COMMIT;

```

乐观并发控制采用不同的方法。读取时不加锁；相反，你会记录所读行的版本，并在写入时断言版本未发生变化。如果已变，则更新失败，应用程序重试。在冲突罕见且读者远多于写者时使用：

```sql

-- Optimistic: read with version, write conditionally

SELECT confidence, source_count, version
FROM semantic_memory
WHERE id = @memory_id;

UPDATE semantic_memory
SET confidence = @new_confidence,
    source_count = source_count + 1,
    last_confirmed_at = NOW(),
    version = version + 1
WHERE id = @memory_id
  AND version = @read_version;

-- If 0 rows affected, another transaction won the race; retry.

```

两者都是有效的。来自人工审核者的记忆更新（频率低、谨慎度高）适合悲观锁。来自跨数百万条记录的后台总结任务的记忆更新（频率高、冲突低）适合乐观并发。在一个事务中草率地混用它们（在刚刚锁定的行上同时使用 `FOR UPDATE` 和版本检查）是做无用功，说明你对提交的模型感到困惑。

重点不在于使用哪一个，而在于数据库同时支持两者，它们都符合 ACID 正确性，并且智能体不需要在应用代码中实现这些逻辑。

## 状态持久化不是记忆，但记忆需要它

最后，让我说明一个在大多数架构讨论中被忽视的区别。

我在本文大部分内容中描述的是一个状态与知识持久层。它是底座。就其本身而言，它不是完整意义上的记忆。记忆是当一个智能系统善用该底座时发生的事情：选择记住什么、总结保留什么、衡量新旧、识别曾经相信的错误，并在正确的时刻提取正确的记忆。底座本身不做这些事，智能体去做。但如果没有一个支持这些行为的底座，智能体就无法做到这些。

> “底座本身不做这些事，智能体去做。但如果没有一个支持这些行为的底座，智能体就无法做到这些。”

对于任何正在构建生产级智能体的团队，我问的问题不是“用哪个向量数据库”或“是否该用 Redis”，而是你底下的底座是否支持你在未来 12 个月内所需的全部记忆行为。持久化是基础，但还需要：针对情节历史的结构化查询、基于压缩总结的向量召回、读取时计算的置信度衰减、作为一等公民的污染失效处理、同时支持悲观和乐观并发，以及随着[智能体集群增长](https://thenewstack.io/cloud-native-and-open-source-help-scale-agentic-ai-workflows/)的水平扩展能力。

这就是我们在演进 [**TiDB**](https://www.pingcap.com/) 以支持智能体负载时的思考方向。不是做一个“顺便能写 SQL 的向量数据库”，也不是做一个“强行挂载向量功能的关系型数据库”，而是一个能处理真实记忆系统所需的所有存储模式，并具备分布式 SQL 的一致性和扩展特性的底座。模式设计是容易的部分，底座所赋能的模式才是智能体真正记忆的寄托。

工作负载是全新的，但原则始终如一。