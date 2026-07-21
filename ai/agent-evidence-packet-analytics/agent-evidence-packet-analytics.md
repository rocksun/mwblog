<!--
title: 为什么每个AI代理的决策都需要一张“凭证”？
cover: https://cdn.thenewstack.io/media/2026/07/78b12e3d-aakash-dhage-q_d2ilpbmjg-unsplash.jpg
summary: 文章指出，仅靠检索数据无法支持AI代理做出准确决策。AI需要基于结构化的证据包进行分析，包含查询定义、数据时效、已知偏差及反向验证，从而实现决策的可审计性与可复现性，确保AI分析结果的可信度。
-->

文章指出，仅靠检索数据无法支持AI代理做出准确决策。AI需要基于结构化的证据包进行分析，包含查询定义、数据时效、已知偏差及反向验证，从而实现决策的可审计性与可复现性，确保AI分析结果的可信度。

> 译自：[Why every AI agent decision needs a receipt](https://thenewstack.io/agent-evidence-packet-analytics/)
> 
> 作者：Manveer Chawla

当定价引擎部署了更新后的折扣规则30分钟后，转化率警报被触发。分析平台在相关时间窗口内存储了数百万条结账事件。AI代理检索了50条显示购物车放弃的会话日志，并报告了一个可能的定价回归问题。

但仅靠检索无法回答关键问题。转化率是在所有买家群体中确实下降了，还是样本偏向于某个特定地区？价格敏感的客户群体是否受到了不成比例的影响？页面加载时间是否在同一时间激增，从而导致这变成了一个性能问题而非定价问题？

AI代理找到了相关记录，但它并未衡量观测群体是如何变化的。

## 检索功能的局限性

检索定位的是候选证据：匹配查询的日志行、会话记录和文档。而分析则是衡量一个群体。它计算比率、比较时间窗口、跨维度聚合，并量化变化。

> “AI代理找到了相关记录，但它并未衡量观测群体是如何变化的。”

如果一个AI代理读取了50条放弃日志，并得出“定价变更导致了流失”的结论，它就跳过了关键步骤：你必须验证部署后转化率确实下降了，比较受影响和未受影响的客户群体，并测试技术指标是否显示出相同的偏移。

对于那些需要对快速变化的实时系统进行推理的AI代理而言，决定性的上下文往往[无法被检索](https://thenewstack.io/retrieval-ai-agent-architecture/)或提前准备。它必须根据当前数据进行计算。

## 证据包应该包含什么

如果分析层要为[LLM提供服务](https://thenewstack.io/introduction-to-vllm-a-high-performance-llm-serving-engine/)，它们之间的接口就需要一个契约。最简单的版本就是SQL查询本身：返回查询结果的同时返回查询语句，以便有人可以重新运行它。

但仅凭SQL无法告诉AI代理数据是否完整、计算是否为近似值，或者是否测试了其他竞争性的解释。如果响应中包含了所有这些信息会怎样？

一种方法是使用“有界证据包”：一种结构化的响应，它携带测量结果以及解释、质疑或重新执行该测量所需的一切信息。

`as_of`（截至时间）时间戳告诉AI代理查询运行的时间。按来源划分的`ingest_watermarks`（摄入水位线）告诉它每个地区或管道底层数据的更新程度。`known_gaps`（已知差距）字段明确了覆盖范围的不完整性，而不是让AI代理去假设覆盖是完整的。

如果欧盟的结账事件延迟了90秒，这一事实应该包含在数据包中，而不是埋在运行手册里。锚定到摄入时间的`data_cutoff`（数据截止）子句使得结果即使在后期事件到达后，依然具有可审计性和可复现性。

证据包还应该引用版本化的指标定义和参数化查询模板，而不仅仅是一个查询ID或哈希值。当AI代理报告结账转化率下降了22%时，审查者需要看到是哪种计算得出了这个数字，基于哪个群体，以及使用了哪些参数。

这些标识符应指向持久注册表中的不可变版本，并且引用的定义应与数据包一起保留或缓存，以供事故处理时使用。

许多分析计算使用近似算法，如t-digest百分位数和HyperLogLog基数。两者都是合理的，但AI代理不应将近似结果呈现为精确结果。一个说明方法并标记近似值的`calculation`（计算）字段可以保持这种可见性。

孤立的单个指标容易导致选择性偏见，因此数据包应包含反向验证：根据各自基准测试的相关指标。如果转化率下降的同时平均订单价值上升，且页面加载时间保持不变，这将削弱网站性能假设，并将调查方向指向特定客户群体的价格敏感度。

深入的会话ID有助于人工调查人员，但证据包需要明确说明这些示例会话只是为了说明聚合结果，它们不能证明该结果。

针对结账转化场景，这看起来可能如下所示：

```json
{
  "observation": {
    "metric": "checkout.conversion_rate",
    "unit": "percent",
    "current_value": 3.28,
    "baseline_value": 4.21,
    "change": { "relative_pct": -22.1, "absolute_percentage_points": -0.93 }
  },
  "baseline_definition": {
    "description": "Mean conversion rate for the same 30-minute interval",
    "lookback": "previous 7 days"
  },
  "scope": { "service": "pricing-engine", "deployment": "pricing-2026-06-15.1" },
  "time_window": { "start": "2026-06-15T10:15:00Z", "end": "2026-06-15T10:45:00Z" },
  "as_of": "2026-06-15T10:46:03Z",
  "ingest_watermarks": { "default": "2026-06-15T10:45:58Z", "eu-west-1": "2026-06-15T10:44:31Z" },
  "known_gaps": [{ "region": "eu-west-1", "detail": "checkout events delayed ~90s" }],
  "data_cutoff": "ingested_at <= 2026-06-15T10:45:58Z",
  "metric_definition": { "id": "checkout-conversion-v2.1", "registry_uri": "https://metrics.internal/defs/checkout-conversion-v2.1" },
  "query": {
    "template": { "id": "post-deployment-conversion-v1", "registry_uri": "https://metrics.internal/queries/post-deployment-conversion-v1" },
    "parameters": { "deployment": "pricing-2026-06-15.1", "window_start": "2026-06-15T10:15:00Z", "window_end": "2026-06-15T10:45:00Z", "data_cutoff": "2026-06-15T10:45:58Z" },
    "query_id": "query-b8d4e2f7"
  },
  "coverage": { "sessions_observed": 142380, "sampling_policy": "unsampled" },
  "calculation": { "method": "exact count ratio", "approximate": false },
  "drilldown_examples": ["session-a91f", "session-d47c", "session-02eb"],
  "segment_breakdown": [
    { "segment": "discount-sensitive buyers", "segment_definition": "segment-discount-sensitive-v1", "current_value": 2.41, "baseline_value": 3.62, "unit": "percent", "change": { "relative_pct": -33.4, "absolute_percentage_points": -1.21 } }
  ],
  "counterchecks": [
    { "metric": "avg_order_value", "current_value": 87.40, "baseline_value": 72.15, "unit": "usd", "materiality_threshold_pct": 10, "result": "above baseline" },
    { "metric": "page_load_time_p95", "current_value": 1.82, "baseline_value": 1.79, "unit": "seconds", "materiality_threshold_pct": 15, "result": "within baseline" }
  ]
}
```

## 将数据库观测与AI代理的解释分开

证据包的可靠性取决于产生它的系统。

对于既定指标，治理层应公开[批准的定义和受控查询路径](https://clickhouse.com/blog/visa-conversational-agents)。AI代理选择模板并提供参数。查询引擎使用只读凭据和资源限制执行，然后通过应用结构化响应模式的证据适配器返回结果。

> “证据包的可靠性取决于产生它的系统。”

对于不可预见的调查，在带有SQL验证、审计日志和严格成本限制的只读副本上进行的受控探索路径，可以[支持临时分析和任意SQL，而无需开放无限制的访问权限](https://clickhouse.com/blog/announcing-managed-clickstack-mcp-server)。

这种分离使得数据库的观测和模型的解释可以清晰地分开。数据库本身不产生结论，它产生可审计、可重现的观测结果。LLM负责解释这些观测结果并推荐行动。

策略门控或人工审查者随后可以检查证据包，重新运行查询，并决定该解释是否成立。没有这种分离，AI代理的置信度将与系统的确定性变得无法区分。

## 支持AI代理的证据工作负载

支持受控的AI代理分析改变了工作负载特征。每次AI代理交互都可能触发数十个并发查询，因为它在探索数据集并对可能的并行假设进行推理。一个用户的简单问题会变成一阵分析查询爆发，这种并发性的转变正在[重新绘制数据库需要处理的内容](https://clickhouse.com/blog/ai-redrawing-database-market)。

![图表展示了现代BI工作负载的本质变化及其对数据仓库的影响](https://cdn.thenewstack.io/media/2026/07/9aea591f-image-1024x376.png)

> “有用的AI代理不是那个能消费最多数据的代理。而是那个系统能够确切展示它测量了什么、如何测量以及还有什么不确定性的代理。”

## 是什么让AI代理值得信赖

有用的AI代理不是那个能消费最多数据的代理。而是那个系统能够确切展示它测量了什么、如何测量以及还有什么不确定性的代理。从证据契约开始。可信度始于AI代理所接收内容的[可审计性](https://thenewstack.io/agentic-ai-observability-auditing/)。