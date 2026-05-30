调试过去非常直截了当：服务失败，检查日志，追踪堆栈信息，然后修复 Bug。不幸的是，对于 AI 系统，尤其是那些由 LLM 和智能体（Agent）工作流驱动的系统，这种方法很快就会失效。

问题不仅在于系统变得更加复杂。更复杂的是，失败不再是确定性的。系统可能会针对相同的输入返回不同的答案。工具可能会默默失败。检索可能会返回低质量或嘈杂的上下文。没有发生明显的“崩溃”，但显然有什么地方不对劲。

本教程专注于一个实际问题：我们该如何调试一个不会以显式方式失败的系统？

为了解决这个问题，我们将构建一个小型 AI 服务，更重要的是，对其进行检测，以便我们能够真正理解其内部发生的事情。

---

## 为什么调试 AI 系统感觉如此不同

传统调试依赖于三个假设：

* 输入能带来可预测的输出
* 失败会抛出错误
* 日志能说明全部情况

这些对于 AI 系统都不成立。

相反，我们要应对的是：

* 非确定性的输出
* 隐藏的推理步骤
* 外部依赖项（检索、API、工具）
* 庞大且动态的提示词

这意味着调试必须从基于日志的思维转变为可观测性驱动的工程。

> “调试必须从基于日志的思维转变为可观测性驱动的工程。”

---

## 我们要构建什么

我们将创建一个简单的 AI 问答服务，包含：

* 检索（向量搜索 + 重排）
* 外部工具调用
* LLM 推理
* 结构化输出校验
* 可观测性（[追踪 + 日志](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/) + Token 估算）

重点不仅在于构建它，还在于使其**可调试**。

### 架构概述：一个可调试的 AI 系统

![展示可调试 AI 系统架构的图表](https://cdn.thenewstack.io/media/2026/05/e68cbcf2-11-1024x835.png)

这一架构突出了现代 AI 系统的一个关键转变：[可观测性](https://thenewstack.io/introduction-to-observability/)是一个核心组件，而不是事后的想法。从检索、工具执行到模型推理，工作流的每个阶段都经过了检测，使工程师能够追踪决策过程。这使得调试不仅限于失败，还能调试意外行为，这在 AI 系统中比在传统软件中要常见得多。

---

### 步骤 1：安装依赖

```bash
pip install fastapi uvicorn \
  langchain langchain-openai langchain-community \
  faiss-cpu rank-bm25 \
  httpx tenacity \
  opentelemetry-api opentelemetry-sdk \
  opentelemetry-instrumentation-fastapi \
  opentelemetry-instrumentation-httpx \
  tiktoken pydantic
```

我们明确包含了 OpenTelemetry，因为在没有追踪的情况下调试 AI 系统就像盲飞。

---

### 步骤 2：初始化模型（带生产控制）

```Python
import os
from langchain_openai import ChatOpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY must be set")

llm = ChatOpenAI(
model="gpt-4o-mini",
temperature=0,
model_kwargs={"response_format": {"type":     "json_object"}},
openai_api_key=api_key,
request_timeout=30, 
max_retries=2
)
```

超时和重试不是可选的。当某些内容失败时，你需要知道是你的系统出了问题，还是模型提供商的问题。

---

### 步骤 3：添加检索（并使其可观测）

```Python
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

docs = [
    Document(page_content="Observability helps debug AI systems."),
    Document(page_content="Retrieval quality impacts model output."),
    Document(page_content="Tracing reveals hidden execution paths.")
]

embeddings = OpenAIEmbeddings()
index = FAISS.from_documents(docs, embeddings)
```

现在，检索

```Python
from rank_bm25 import BM25Okapi

def retrieve(query: str):
    results = index.similarity_search(query, k=5)

    # Add lexical reranking
    corpus = [doc.page_content.split() for doc in results]
    bm25 = BM25Okapi(corpus)
    scores = bm25.get_scores(query.split())

    ranked = sorted(zip(scores, results), reverse=True)

    return [
        {
            "text": doc.page_content,
            "source": doc.metadata.get("source", "internal")
        }
        for _, doc in ranked[:3]
    ]
```

#### 调试洞察

如果检索出错，下游的所有内容也都会出错。

务必记录检索到了哪些文档。

---

```Python
from urllib.parse import urlparse
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

# Restrict outbound requests to trusted domains only.
ALLOWED_DOMAINS = {
    "api.trusted-source.com",
    "documentation.org"
}

@retry(
    stop=stop_after_attempt(2),
    wait=wait_exponential(min=1, max=4)
)
async def fetch_external(url: str):

    parsed_url = urlparse(url)

    # Prevent SSRF and internal network probing.
    if parsed_url.netloc not in ALLOWED_DOMAINS:
        raise ValueError(
            f"URL domain '{parsed_url.netloc}' is not allowed."
        )

    async with httpx.AsyncClient(
        timeout=10,
        follow_redirects=False
    ) as client:

        response = await client.get(url)
        response.raise_for_status()

    # Truncate response to control token usage.
    return response.text[:3000]
```

生产环境中的 AI 系统绝不应该允许来自模型生成输入的无限制出站请求。如果没有域名白名单，智能体可能会成为 SSRF（服务端请求伪造）攻击媒介，从而探测内部服务、云元数据端点或私有基础设施。限制对受信任域名的出站访问是一项最低限度的生产安全保障。

> “生产环境中的 AI 系统绝不应该允许来自模型生成输入的无限制出站请求。”

#### 调试洞察

工具[失败是无形杀手](https://thenewstack.io/mastering-deadman-alerts-to-prevent-silent-failures/)。如果没有重试和日志记录，你将无法得知：

* 工具是否失败
* 工具是否返回了空数据
* 模型是否忽略了该工具

---

### 步骤 5：Token 可见性（不精确，但有用）

```Python
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o-mini")

def estimate_tokens(messages):
    """
    Approximate token usage for OpenAI-style chat payloads.

    Note:
    This is still an estimate. Real usage depends on:
    - system prompts
    - retrieved context
    - tool call arguments
    - provider-specific formatting
    - output tokens
    """

    # Approximate overhead used by OpenAI chat formatting.
    tokens_per_message = 3
    tokens_per_name = 1

    total = 0

    for message in messages:

        total += tokens_per_message

        for key, value in message.items():

            if isinstance(value, str):
                total += len(encoder.encode(value))

            if key == "name":
                total += tokens_per_name

    # Assistant reply priming tokens.
    total += 3

    return total
```

Token 计数应该被视为一种运营估算，而不是精确的计费机制。实际的请求成本取决于完整的消息负载、检索到的上下文、工具调用参数、系统提示词、提供商端的格式化以及生成的输出 Token。然而，即使是近似的追踪，对于调试失控的智能体和监控生产系统中的成本退化也极其有用。

#### 调试洞察

意想不到的成本激增通常来自：

* 庞大的检索上下文
* 重复循环
* 过大的提示词

---

### 步骤 6：构建智能体工作流（确定性）

```Python
def run_workflow(question: str):

    # Step 1: Retrieve
    context = retrieve(question)

    context_text = "\n".join([c["text"] for c in context])

    messages = [
        {"role": "system", "content": "Answer clearly using the provided context."},
        {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {question}"}
    ]

    tokens = estimate_tokens(messages)

    response = llm.invoke(messages)

    return {
        "raw_output": response.content,
        "sources": [c["source"] for c in context],
        "token_estimate": tokens
    }
```

#### 调试洞察

我们坚持使用确定性工作流，因此不需要处理工具或智能体自行其是的情况。

---

### 步骤 7：验证输出（护栏）

```Python
from pydantic import BaseModel

class OutputSchema(BaseModel):
    answer: str
    sources: list[str]
    token_estimate: int

import json

def validate_output(raw):

    try:
        parsed = json.loads(raw["raw_output"])
    except Exception:
        parsed = {
            "answer": raw["raw_output"],
            "sources": raw["sources"],
            "token_estimate": raw["token_estimate"]
        }

    validated = OutputSchema(**parsed)
    return validated.dict()
```

#### 调试洞察

这里的失败会告诉你：

* 模型忽略了指令
* 输出格式发生了变化
* 上游的某些环节损坏了上下文

---

### 步骤 8：添加可观测性

```Python
from fastapi import FastAPI

from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import (
    HTTPXClientInstrumentor,
)

# Configure tracer provider.
provider = TracerProvider()

# For local debugging:
# export traces to console.
#
# In production, prefer:
# OTLPSpanExporter -> OpenTelemetry Collector -> Jaeger/Grafana/etc.
processor = BatchSpanProcessor(ConsoleSpanExporter())

provider.add_span_processor(processor)

trace.set_tracer_provider(provider)

# Create application.
app = FastAPI()

# Instrument FastAPI and outbound HTTP calls.
FastAPIInstrumentor.instrument_app(app)

HTTPXClientInstrumentor().instrument()
```

仅靠检测并不能让追踪可视化。OpenTelemetry 需要追踪器提供商（Tracer Provider）、Span 处理器（Span Processor）和导出器（Exporter）来记录和发送遥测数据。对于本地调试，控制台导出器就足够了。在生产系统中，追踪数据通常通过 OTLP 收集器导出到 Jaeger、Grafana、Tempo、Datadog 或 Honeycomb 等平台。

#### 添加端点：

```Python
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask(q: Query):

    result = await run_in_threadpool(run_workflow, q.question)

    output = validate_output(result)

    return output
```

---

## 你现在可以调试什么

通过这种设置，你可以回答以下问题：

**“为什么答案是错的？”**

* 检查检索到的文档

**“为什么输出改变了？”**

* 对比上下文和 Token 大小

**“为什么延迟这么高？”**

* 追踪 LLM vs 工具 vs 检索

**“为什么成本在增加？”**

* 检查 Token 估算和上下文大小

---

## 工程原则：让 AI 系统可观测

AI 系统不仅仅是模型。它们是包含以下环节的管道：

* 检索
* 推理
* 工具
* 验证

每个部分都可能独立失效。你需要在每一步都具备可见性，否则你基本上是在黑暗中进行调试。

> “每个部分都可能独立失效。你需要在每一步都具备可见性，否则你基本上是在黑暗中进行调试。”

---

## 生产经验

1. **仅有日志是不够的**

你需要能够显示完整执行路径的追踪（Traces）

2. **检索错误看起来就像模型错误**

务必先检查上下文

3. **工具失败通常是无声的**

增加重试和检测

4. **Token 增长是一个隐藏的风险**

持续监控提示词大小

5. **确定性工作流可以简化调试**

更少的活动部件 = 更少的未知因素

---

## 结论

这里的核心结论是，由于你面对的是一个概率性系统，你的调试工具（和方法）必须发生改变。通过引入可观测性、确定性工作流、结构化验证和适当的追踪，你可以做好准备，在逻辑走偏时能够看清问题所在（因为逻辑总会走偏）。