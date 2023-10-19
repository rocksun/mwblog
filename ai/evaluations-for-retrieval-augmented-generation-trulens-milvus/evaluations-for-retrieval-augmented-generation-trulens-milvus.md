<!--
# 评估检索增强生成（RAG）：TruLens + Milvus
https://cdn.thenewstack.io/media/2023/10/1fffda46-image5-1024x536.jpg
 -->

译自 [Evaluations for Retrieval Augmented Generation: TruLens + Milvus](https://thenewstack.io/evaluations-for-retrieval-augmented-generation-trulens-milvus/) 。

了解如何构建各种配置和参数的 RAG，包括索引类型、嵌入模型、top k 和 chunk 大小参数。

大型语言模型(LLM)的日益普及，推动了向量搜索技术的兴起，包括专为此设计的向量数据库 Milvus 和 Zilliz Cloud，向量搜索库例如 FAISS，以及与传统数据库集成的向量搜索插件。

越来越多地，向量搜索已成为生成式 AI 在问答应用中的关键企业用例，即所谓的[“检索增强生成（retrieval augmented generation）”或RAG](https://thenewstack.io/discover-the-performance-gain-with-retrieval-augmented-generation/)。这种构建方式使 LLM 可以轻松访问经过验证的知识库，并将其用作语境来回答问题。[Milvus](https://milvus.io/) 是一种高度可扩展的开源向量数据库，[专为此应用而设计](https://thenewstack.io/what-is-milvus-vector-database/)。

## 构建 RAG

在构建高效的 RAG 式 [LLM 应用程序](https://roadmap.sh/guides/introduction-to-llms)时，有许多配置选择可供优化，这些选择可以显着影响检索质量。这些选择包括:

### 构建向量数据库

* 数据选择
* 嵌入模型
* 索引类型

找到高质量、能精确符合应用程序需求的数据非常关键。如果数据不够准确，检索过程就可能返回无关的结果。

选择好数据之后，要考虑使用的嵌入模型，因为它对检索质量有很大影响。即使知识库包含了正确的信息，如果嵌入模型无法对领域内容进行语义理解，检索器也可能给出错误的结果。

上下文相关度是衡量检索质量的一个有用指标，这些选择极大地影响了它。

最后，索引类型可以显著影响语义搜索的效率。这对大型数据集尤其重要；该选择允许您在召回率、速度和资源需求之间进行权衡。Milvus支持多种索引类型，比如平面索引、基于产品量化的索引和基于图的索引。您可以阅读更多关于[不同索引类型](https://milvus.io/docs/index.md)的信息。

### 检索

* 检索到的上下文数量(前 k 个)
* 分块大小

当进行检索时，前 k 个是经常讨论的一个参数，它控制检索到的上下文分块数量。更高的前 k 个提供更高机会检索到所需信息，也增加语言模型融入不相关信息到其回答中的可能性。对简单问题而言，较低的前 k 个通常性能最佳。

分块大小控制每个检索上下文的大小。对更复杂问题而言，较大分块大小可能更有帮助，而简单问题只需要很小一部分信息即可回答，较小分块就足够了。

对这些选择大多数情况，并无一刀切的解决方案。性能可能因数据规模和类型、使用的语言模型、您的应用等而大相径庭。我们需要评估工具来评估这些检索在我们具体用例中的质量。这就是 TruLens 的用武之地。

## TruLens 用于语言模型应用跟踪和评估

TruLens是一个开源库，用于评估和跟踪语言模型应用(如RAG)的性能。通过TruLens，我们还可以利用语言模型本身来评估输出、检索质量等。

构建语言模型应用时，多数人最关心的问题是幻想。RAG 在很大程度上通过为语言模型提供检索上下文来确保准确信息，但无法百分百保证。因此评估对验证应用中[不存在幻想](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)至关重要。TruLens 提供了三项测试：上下文相关度、准确性和答案相关度。让我们逐一查看，以了解它们的益处。

![](https://cdn.thenewstack.io/media/2023/10/4f7f835b-image1a.png)

### 上下文相关度

任何 RAG 应用第一步是检索；为验证检索质量，我们要确保每个上下文块与输入查询相关。这非常关键，因为语言模型将使用该上下文生成答案，所以上下文中的任何不相关信息都可能被编织成幻想。

### 准确性

在检索上下文后，它被语言模型形成答案。语言模型往往偏离提供的事实，对正确的答案进行夸张或扩展。为验证应用的准确性，我们应将回复分为独立语句，并在检索上下文中独立查证每个语句的证据支持。

### 答案相关度

最后，我们的回复仍须有助于回答原始问题。我们可以通过评估最终回复与用户输入的相关度来验证这一点。

## 无幻想 RAG

通过对上述三项达到满意的评估，我们可以对应用的正确性做出细微陈述；它在知识库限度内经验证无幻想。换言之，如果向量数据库仅包含准确信息，则 RAG 提供的答案也准确。

## 具体案例

如前所述，我们的 RAG 许多配置选择可能对幻想有重大影响。为说明这点，我们基于少量城市维基百科文章构建问答 RAG 应用。LlamaIndex 作为该应用的框架。

在 [Google Colab](https://colab.research.google.com/github/truera/trulens/blob/main/trulens_eval/examples/expositional/vector-dbs/milvus/milvus_evals_build_better_rags.ipynb) 中查看此案例。

## 从维基百科加载数据

要构建向量存储，我们首先需要加载数据。这里，我们使用 LlamaIndex 中的数据加载器直接从维基百科加载数据。

```python
from llama_index import WikipediaReader


cities = [
  "Los Angeles", "Houston", "Honolulu", "Tucson", "Mexico City",
  "Cincinnati", "Chicago"
]


wiki_docs = []
for city in cities:
  try:
    doc = WikipediaReader().load_data(pages=[city])
    wiki_docs.extend(doc)
  except Exception as e:
    print(f"Error loading page for city {city}: {e}")
```

## 设置评估器

接下来，我们设置评估器，具体使用前面提到的三项检查上下文相关度、准确性和答案相关度以测试幻想。

TruLens提供一组使用特定模型提供者(如OpenAI、Anthropic或HuggingFace)的提示评估器或反馈功能。

```py
# 初始化基于 OpenAI 的反馈功能集合类:
openai_gpt4 = feedback.OpenAI()
```

设置模型提供者后，我们选择查询语句相关度作为第一个评估。 对于每个评估，我们还使用思维链反馈原因更好地理解。这用反馈功能后缀 `1_with_cot_reason` 表示。

此时，我们还需选择哪些文本传递给反馈功能。TruLens 序列化应用，然后由类 JSON 结构索引。我们使用此索引文本选择。TruLens 提供帮助函数简化此操作:

- `on_input()` 自动找到传给 LlamaIndex 应用的主输入，作为传给反馈功能的第一个文本。
- `TruLlama.select_source_nodes()` 标识 LlamaIndex 检索中使用的源节点。

最后，我们需要将每个上下文相关度聚合为单一分数。本例中，我们使用最大值衡量最相关块的相关度。也可使用其他指标如平均值或最小值。

```
# 问题/语句之间的相关度与每个上下文块。
f_context_relevance = Feedback(openai.qs_relevance_with_cot_reason, name = "Context Relevance").on_input().on(
  TruLlama.select_source_nodes().node.text
).aggregate(np.max)

```

准确性设置类似，聚合略有不同。这里，我们取每个语句的最大准确度分数，然后各语句的平均准确度分数。

```py
grounded = Groundedness(groundedness_provider=openai_gpt4)
f_groundedness = Feedback(grounded.groundedness_measure_with_cot_reason, name = "Groundedness").on(
  TruLlama.select_source_nodes().node.text # context
).on_output().aggregate(grounded.grounded_statements_aggregator)
```

答案相关度是最简单的反馈功能设置，因其仅依赖输入/输出。我们可以使用新的 TruLens 帮助函数 - .on_input_output()。

```py
# 问题与答案整体相关度。
f_qa_relevance = Feedback(openai.relevance_with_cot_reason,
name = "Answer Relevance").on_input_output()
```

## 定义配置空间

现在我们已加载数据和设置评估器，是时候构建我们的 RAG。过程中，我们构建一系列具有不同配置的 RAG，评估每个并选择最佳配置。

如前所述，我们将配置空间限制在 RAG 一些重要选择上。我们在此案例中测试索引类型、嵌入模型、前 k 个和块大小;不过，建议您测试其他配置，如不同距离指标和搜索参数。

## 迭代我们的选择

定义配置空间后，我们用 itertools 尝试每种组合并评估。此外，Milvus 覆盖参数提供了优势，使我们可轻松迭代不同配置，而不需其他向量数据库可能需要的缓慢拆卸和实例化过程。

每次迭代，我们将索引参数选择传给 MilvusVectorStore 和使用存储上下文的应用。我们将嵌入模型传给服务上下文，然后创建索引。

```py
vector_store = MilvusVectorStore(index_params={
  "index_type": index_param,
  "metric_type": "L2"
},
search_params={"nprobe": 20},
overwrite=True)
llm = OpenAI(model="gpt-3.5-turbo")
storage_context = StorageContext.from_defaults(vector_store = vector_store)
service_context = ServiceContext.from_defaults(embed_model = embed_model, llm = llm, chunk_size = chunk_size)
index = VectorStoreIndex.from_documents(wiki_docs,
service_context=service_context,
storage_context=storage_context)
```

然后，我们可用该索引构建查询引擎 —— 定义 `top_k`:

```
query_engine = index.as_query_engine(similarity_top_k = top_k)
```

构建后，我们用 TruLens 包装应用。这里，我们给其易识别名称，将配置记录为应用元数据，并定义反馈功能用于评估。

```py
tru_query_engine = TruLlama(query_engine,
app_id=f"App-{index_param}-{embed_model_name}-{top_k}", 
feedbacks=[f_groundedness, f_qa_relevance, f_context_relevance],
metadata={
  'index_param':index_param,
  'embed_model':embed_model_name,
  'top_k':top_k
})
```

这个 `tru_query_engine` 将像原查询引擎一样运行。

最后，我们使用少量测试提示进行评估，调用应用响应每个提示。由于我们快速连续调用 OpenAI API，Tenacity 可帮助我们通过指数回退避免速率限制问题。

```py
@retry(stop=stop_after_attempt(10), wait=wait_exponential(multiplier=1, min=4, max=10))
def call_tru_query_engine(prompt):
  return tru_query_engine.query(prompt)
  for prompt in test_prompts:
    call_tru_query_engine(prompt)
```

## 结果

**哪种配置表现最佳？**

| 索引类型 | 嵌入模型 | 相似度前 k 个 | 块大小 |
|-|-|-|-|
| IVF Flat | text-embedding-ada-002 | 3 | 200 |

![](https://cdn.thenewstack.io/media/2023/10/378d2b0e-image2a.png)

**哪种配置表现最差？**

这里是更新后的表格:

| 索引类型 | 嵌入模型 | 相似度前 k 个 | 块大小 |
|-|-|-|-|
| IVF Flat | Multilingual MiniLM L12 v2 | 1 | 500 |

![](https://cdn.thenewstack.io/media/2023/10/a9e0b919-image3a.png)

**识别出哪些失败模式？**

我们观察到一种失败模式是检索到错误城市信息。您可以从下面的思维链反馈原因中看到，其中检索到了 Tucson 而不是 Houston 的上下文。

![](https://cdn.thenewstack.io/media/2023/10/65489488-image4a.png)

同样，我们也遇到关于正确城市但与输入问题不相关的上下文被检索的问题。

![](https://cdn.thenewstack.io/media/2023/10/59d315eb-image5a.png)

在这种不相关上下文下，语言模型开始幻想。值得注意的是，幻想不一定与事实上错误；它仅指模型在无证据支持下作答。

![](https://cdn.thenewstack.io/media/2023/10/f6d0af02-image6a.png)

此外，我们还发现不相关答案的例子。

![](https://cdn.thenewstack.io/media/2023/10/2f03d086-image7a.png)

## 理解性能

### 按索引类型

本例中，索引类型对速度、标记使用或评估没有明显影响。这可能因为数据量较小。索引类型对较大语料库可能更重要。

### 按嵌入模型

text-embedding-ada-002 在准确性(平均0.72对比0.60)和答案相关度(平均0.82对比0.62)上优于MiniLM嵌入模型。两者在上下文相关度上表现一致。

这些评分改进可归因于OpenAI嵌入更适合维基百科信息。

### 相似度前 k 个

增加 top k 略微提高最大检索质量(通过上下文相关度测量)。检索更多块，检索器有更多机会获取高质量上下文。

更高的前 k 个也改善了准确性(平均0.71对比0.62)和答案相关度(平均0.76对比0.68)。检索更多上下文块为语言模型提供更多证据提出并支持其结论。

如预期的那样，这些改进以更高令牌使用成本(每个调用平均额外590个令牌)为代价。

### 块大小

增加块大小通过强制包含与输入问题无关的周边文本来降低检索器的准确性。

从积极方面看，更大块大小提供了更多证据进行检查。因此，当语言模型得出结论时，它们更可能得到检索上下文的支持。

最后，增加块大小使每个记录的平均令牌使用增加了400个。

## 用TruLens和Milvus构建更好的RAG

本文中，我们学习使用各种配置和参数(包括索引类型、嵌入模型、前 k 个和块大小)构建 RAG。Milvus 支持大量配置和允许覆盖使这种动态实验成为可能。至关重要的是，我们还使用 TruLens 来跟踪和评估每个实验，识别并解释新的失败模式，并快速找到最佳性能组合。

欲自行尝试，您可以查看开源 [TruLens](https://www.trulens.org/) 并安装开源 [Milvus](https://milvus.io/docs/build_index.md) 或 [Zilliz Cloud](https://zilliz.com/cloud?utm_source=google&utm_medium=cpc&utm_campaign=Brand_Zilliz_Search&utm_content=Zilliz_Cloud_SKAG&utm_term=zilliz%20cloud&utm_campaign=Brand_Zilliz_Search&utm_source=adwords&utm_medium=ppc&hsa_acc=3636806625&hsa_cam=20126268396&hsa_grp=149842899315&hsa_ad=658536737960&hsa_src=g&hsa_tgt=kwd-1798686554316&hsa_kw=zilliz%20cloud&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad=1&gclid=EAIaIQobChMIjJ6a5t6WgQMVjExHAR0v8AzyEAAYASAAEgKG0PD_BwE)。
