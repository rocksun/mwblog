没有什么比在可观测性仪表板显示完美绿色且延迟低于100ms时，却收到企业客户发来的邮件，指责你的AI在向用户撒谎更让人恐惧的了。

六个月前，我的团队为一家金融科技客户交付了一个检索增强生成（RAG）模型。我们的任务是创建一个能够摄取数千份高度非结构化PDF财务报告的系统，从中提取关键数据、计算嵌入（embeddings），并将所有内容存储在向量数据库中，以驱动内部问答聊天机器人。

起初，系统运行得非常完美。

然后，聊天机器人开始回答有关公司2022年业绩的查询，引用的却是2018年的数据。机器人甚至将客户竞争对手赚取的收入归结为其子公司名下。最可怕的是，系统确实[正确地从向量数据库中检索到了信息](https://thenewstack.io/writer-coms-graph-based-rag-alternative-to-vector-retrieval/)。

这不是RAG管道的错，而是因为错误的自主摄取引擎导致我们用垃圾数据毒害了自己的数据库。

以下是对如何构建一个看起来可靠却只会产生垃圾的系统的复盘。

## 发生了什么：摄取幻觉

我们的摄取工作流程遵循标准的AI管道。一旦PDF被放入S3存储桶，摄取过程就会触发提取代理运行。提取代理（在广泛使用的前沿LLM的帮助下）负责从文档中提取文本块，并返回相应的元数据：`document_type`（文档类型）、`fiscal_year`（财年）、`company_entity`（公司实体）和JSON格式的`summary`（摘要）。

这些元数据值随后被附加到文本块中，并发送到向量存储进行嵌入。

我们的错误在于将概率提取过程视为确定性过程。这意味着当LLM无法识别扫描模糊的PDF中难以辨认的财年时，它并没有抛出异常，而是做了LLM倾向于做的事：猜。在这种情况下，它对财年的猜测是“2024”。

> “我们的错误在于将概率提取过程视为确定性过程。”

由于我们将幻觉与提取的文本一起嵌入，很明显，我们创建了针对[不存在文档的高速搜索](https://thenewstack.io/build-rag-document-search/)。

## 为什么令人惊讶：作为法官的LLM失效了

AI回音室非常推崇“LLM作为法官”的概念。普遍的智慧认为，如果你不信任LLM的输出，只需在它前面再放一个LLM来复核工作即可。

我们正是这样实现的。在数据被添加到向量数据库之前，二级“验证器代理”会根据原始文本对提取的JSON进行评估。

那么，为什么幻觉还是漏过去了呢？因为我们严重低估了**LLM的谄媚（Syllcophancy）**。

当我们查看日志时，我们发现验证器代理始终同意提取代理的意见。如果提取器输出`{"fiscal_year": 2024}`，验证器会扫描文本，找不到年份，但它没有拒绝该有效负载，而是在内部合理化道：“*好吧，第一个模型肯定看到了我漏掉的东西。*”

事实证明，使用概率模型来监督另一个概率模型并不能提供防火墙，只会产生确认偏误循环。

## 什么不起作用：“提示工程”陷阱

我们的第一反应是可以通过提示工程（prompt engineering）来解决这个工程问题。

> “事实证明，使用概率模型来监督另一个概率模型并不能提供防火墙，只会产生确认偏误循环。”

我们对验证器代理的系统提示进行了几次热修复：

* *“不要产生幻觉”*
* *“如果你不能100%确定元数据，请输出NULL”*
* *“你是一名严谨的财务审计师，猜测会导致严重惩罚。”*

不出所料，我们的尝试彻底失败了。LLM变得过于防御性，它不再提取有效的条目，而是开始拒绝完全正确的数据。此外，由于包含了推理步骤，我们的API费用增加了40%。

认为数学矩阵会遵循严格的架构，这是我们思维上的懒惰。

## 什么最终奏效了：代码优于提示

很明显，我们需要从验证过程中移除所有决策权限。数据管道依赖于固定的数据契约，而不是概率。

我们用基于Pydantic的确定性Python组件和我们已经在使用的关系数据库替换了验证器LLM。我们强制LLM输出它认为最可能的答案，但我们将它的输出视为来自HTML表单的用户输入。

1. **严格的Pydantic接地**。简单的Pydantic检查只能确保年份在2000年到当前年份之间。但这并不能[阻止LLM为2018年的文档虚构出](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)“2024年”。为了解决这个问题，我们要求使用正则接地检查（regex grounding check）确保`fiscal_year`在原始文本中实际存在。

```python
import re
from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime

class ExtractedMetadata(BaseModel):
    raw_text: str = Field(exclude=True) # Keep out of final DB payload
    company_entity: str
    fiscal_year: Optional[int]
    
  model_validator(mode='after')
def ground_year_in_text(self) -> "ExtractedMetadata":
if self.fiscal_year is not None:
# Step 1: Bounds Check (Catch impossible years)
current_year = datetime.now().year
if not (2000 <= self.fiscal_year <= current_year):
raise ValueError(f"Year {self.fiscal_year} is out of bounds.")

# Step 2: Grounding Check (Catch plausible hallucinations)
# Find all 4-digit numbers in the raw text that look like recent years
years_in_text = [int(y) for y in re.findall(r'\b(20\d{2})\b', self.raw_text)]

if self.fiscal_year not in years_in_text:
raise ValueError(
f"Hallucination detected: {self.fiscal_year} does not exist in source text."
)
return self
```

2. **确定性交叉引用**。关于`company_entity`字段，我们决定不再完全信任LLM的拼写。我们参考LLM的建议，并针对我们硬编码的SQL数据库中客户的真实实体进行了模糊字符串匹配。

这里棘手的工程点在于，我们需要避免用实际的竞争对手分析来塞满死信队列（DLQ）。换句话说，如果相关文档分析的是“Acme Corp”（我们客户的竞争对手），我们绝不希望模糊字符串匹配器错误地将其解释为“Alpha Corp”并扔进DLQ。那么，我们是怎么做的呢？我们让LLM添加一个`is_competitor`布尔标志。如果是客户实体，它需要与SQL数据库匹配度至少达到95%；否则，它将被丢弃到DLQ。

3. **默认隔离**。我们重新设计了管道架构，使得提取队列中的任何内容都不会直接放入向量数据库。所有内容都被移动到一个中间的PostgreSQL表中。只有那些满足Pydantic接地要求的数据才会被嵌入。

## 我会做出的不同选择

如果今天让我从零开始构建，我的基本哲学将完全不同：**永远不要将原本可以通过简单的`IF`语句、正则表达式规则或标准数据库约束解决的任务交给LLM。**

整个行业正深受生成式AI的“金锤”综合征之苦。我们将关键的数据完整性检查委托给了旨在进行创意叙事的系统。

**最终总结**：概率系统需要确定性的边界。

我们重新设计了管道架构。没有提取数据直接进入向量数据库。所有数据必须临时暂存在PostgreSQL表中。嵌入操作仅针对那些成功满足Pydantic接地约束和数据库验证检查的有效载荷。

> “最终总结：概率系统需要确定性的边界。”

你可以允许LLM提取、分析和总结信息。然而，每当需要将数据作为事实依据写入存储时，它必须通过更严格的、传统工程化的障碍。用新的Pydantic接地和SQL检查替换我们的“验证器代理”，立即切断了数据中毒，将我们的API费用减少了50%，并使我们能够创造出企业客户可以信任的AI产品。