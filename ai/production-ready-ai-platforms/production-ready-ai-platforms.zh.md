### 从零开始

大多数团队都能构建 AI 原型。一个 Notebook 跑通几个提示词，一个 Demo 代理调用一次工具，全场欢呼。接着现实就给了重重一击。生产环境的流量、嘈杂的输入、严格的 SLA、合规性审查以及成本压力让进度停滞不前。这就是“将 AI 作为功能”转变为“将 AI 作为一个平台工程问题”的转折点。

趋势显而易见：平台团队正将 AI 代理视为一种新的执行模型，需要共享的基础设施、安全边界、可观测性、可靠性控制和治理。可以说，这与十年前微服务所需的条件惊人地相似。随着服务网格的成熟，它们越来越多地被用于在不重写应用逻辑的情况下，为 AI 服务强制执行零信任通信、超时、重试和流量整形。

> “大多数团队都能构建 AI 原型。一个 Notebook 跑通几个提示词，一个 Demo 代理调用一次工具，全场欢呼。接着现实就给了重重一击。”

本指南旨在指导如何通过构建一个微小但现实的“AI 平台切片”，将 Demo 转化为可靠的系统。最终结果：一个具备检索、工具调用、护栏、[可观测性](https://thenewstack.io/introduction-to-observability/)和部署规范的生产级 AI 服务。

### **你将构建的内容**

一个生产级的 AI 研究与决策支持 API，具备以下功能：

* 检索内部知识（向量搜索 + BM25 重排序）
* 安全地抓取外部网页（超时/重试 + 解析）
* 返回带有来源的结构化 JSON，以实现信任和审计
* 跟踪 Token/成本信号并发出追踪/指标
* 在负载下安全运行（有界代理循环 + 异步并发安全执行）

---

## 步骤 0：安装必备组件（生产安全型）

版本锁定至关重要。当依赖图发生漂移时，就会出现“在我的机器上能运行”的故障。我们特别在 LangChain 的包拆分和 Pydantic 的重大变更中看到了这一点。

```python

pip install fastapi uvicorn \
  rank-bm25 \
  langchain langchain-openai langchain-community \
  openai tiktoken faiss-cpu \
  "pydantic&lt;2" python-dotenv httpx tenacity beautifulsoup4 \
  opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp \
  opentelemetry-instrumentation-fastapi \
  opentelemetry-instrumentation-httpx

```

---

## 步骤 1：定义鲁棒的工具接口（超时 + 重试 + 干净的输出）

工具的表现应像可靠的服务，具备：明确的输入/输出、有界的时间、弹性重试和安全解析。避免平庸的 HTML 解析。

```python

# tools.py
from __future__ import annotations

import os
import httpx
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential
from pydantic import BaseModel, Field


class WebResult(BaseModel):
    url: str
    title: str | None = None
    text: str = Field(..., description="Extracted page text (truncated).")
    source: str | None = Field(None, description="Optional source identifier.")


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=8))
async def http_get(url: str, timeout_s: int = 10) -> str:
    async with httpx.AsyncClient(timeout=timeout_s, follow_redirects=True) as client:
        r = await client.get(url)
        r.raise_for_status()
        return r.text



MAX_WEB_TEXT_CHARS = int(os.getenv("MAX_WEB_TEXT_CHARS", 8000))
async def web_fetch(url: str) -> WebResult:
    raw = await http_get(url)
    soup = BeautifulSoup(raw, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else None
    # Extract visible text and truncate to protect token cost.
    text = " ".join(soup.get_text(separator=" ").split())
    text = text[:MAX_WEB_TEXT_CHARS]

    return WebResult(url=url, title=title, text=text, source=url)

```

为什么这在生产中很重要：

* 重试处理瞬时网络故障，避免“代理挂起”。
* 截断防止 Token/成本爆炸。
* BeautifulSoup 避免了脆弱的 `<title>` 分割。

---

## 步骤 2：正确构建检索（不要“在导入时构建”）

一个常见的生产反模式是在应用启动时重建嵌入和索引。这很慢、昂贵且脆弱。有一个更好的方法：构建一次，持久化，然后在启动时加载。

```python

# rag.py
from __future__ import annotations

import os
import re
from typing import List, Optional, Tuple

from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from functools import lru_cache
from rank_bm25 import BM25Okapi


_STOPWORDS = {
    "a","an","the","and","or","but","if","then","else","to","of","in","on","for","with",
    "as","at","by","from","is","are","was","were","be","been","it","this","that","these",
    "those","you","your","we","our","they","their","i","me","my"
}
_TOKEN_RE = re.compile(r"[a-z0-9]+")

def _tokenize(text: str) -> List[str]:
    tokens = _TOKEN_RE.findall(text.lower())
    return [t for t in tokens if t not in _STOPWORDS and len(t) > 1]


def make_embeddings(openai_api_key: Optional[str] = None) -> OpenAIEmbeddings:
    key = openai_api_key or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY must be set for embeddings.")
    return OpenAIEmbeddings(openai_api_key=key)


def build_index(pages: List[Tuple[str, str]], openai_api_key: Optional[str] = None) -> FAISS:
    emb = make_embeddings(openai_api_key=openai_api_key)
    docs = [Document(page_content=txt, metadata={"source": src}) for src, txt in pages]
    return FAISS.from_documents(docs, emb)


def save_index(index: FAISS, path: str) -> None:
    index.save_local(path)


def load_index(path: str, openai_api_key: Optional[str] = None) -> FAISS:
    emb = make_embeddings(openai_api_key=openai_api_key)
    return FAISS.load_local(path, emb, allow_dangerous_deserialization=True)


def retrieve(index: FAISS, query: str, k: int = 5) -> List[Document]:
    return index.similarity_search(query, k=k)



@lru_cache(maxsize=256)
def _build_bm25(corpus_key: tuple) -> BM25Okapi:
    """
    Build and cache BM25 indexes for repeated document corpora.
    corpus_key must be hashable, so we use tuple-of-tuples.
    """
    return BM25Okapi([list(tokens) for tokens in corpus_key])


def rerank_bm25(query: str, docs: List[Document], top_n: int = 3) -> List[Document]:
    """
    Rerank retrieved documents using BM25.

    The BM25 index is cached by corpus fingerprint to avoid rebuilding
    the same lexical index repeatedly under load.
    """
    if not docs:
        return []

    corpus_tokens = tuple(tuple(_tokenize(d.page_content)) for d in docs)
    bm25 = _build_bm25(corpus_tokens)

    query_tokens = _tokenize(query)
    scores = bm25.get_scores(query_tokens)

    ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
    return [doc for _, doc in ranked[:top_n]]

```

在生产环境中，重排序器应避免在每次请求时重建昂贵的中间结构。通过使用可哈希的语料库指纹缓存 BM25 对象，在负载下对同一检索文档集进行重复重排序会变得更便宜且更具可预测性。

这与 Demo RAG 的区别：

* 使用现代导入路径（`langchain_community`, `langchain_openai`）
* 使用 BM25 重排序（比单纯的词法匹配更鲁棒）
* 缓存 BM25 索引以避免在重复查询时重建
* 支持持久化/加载，以避免昂贵的启动构建

---

## 步骤 2.5：离线构建一次，运行时加载

将其作为一次性的管理员任务（或 CI 任务）执行：

```python

# build_index_once.py
from rag import build_index, save_index

PAGES = [
    ("policy_handbook", "…your internal policy text…"),
    ("runbook_incidents", "…your oncall runbooks…"),
]
index = build_index(PAGES)
save_index(index, "./faiss_index")
print("Saved FAISS index.")

```

然后你的应用就能快速加载：

```python

# app_startup.py
from rag import load_index

index = load_index("./faiss_index")

```

---

## 步骤 3：反映生产意图的护栏

在生产环境中，“策略检查”不仅仅是单纯的关键词列表。至少，你应该区分：

* 模式验证（形状是否正确？）
* 内容策略（是否包含敏感信息/PII 模式？）

本指南锁定 `pydantic<2` 以确保兼容性，但使用显式验证器而非基于类型的约束，以提高可读性并保持与 Pydantic v2 的前向兼容性。

```python

# guardrails.py
import re
from pydantic import BaseModel, ValidationError, validator

class FinalAnswer(BaseModel):
    answer: str
    sources: list[str] = []
    cost_tokens: int

    @validator("answer")
    def validate_answer_text(cls, v: str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("answer must not be empty")

        if len(v) > 2000:
            raise ValueError("answer exceeds 2000 characters")

        return v

    @validator("cost_tokens")
    def validate_cost_tokens(cls, v: int) -> int:
        if v &lt; 0:
            raise ValueError("cost_tokens must be non-negative")
        return v


# Minimal pattern-based checks; expand or replace with DLP tooling in production.
_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),                      # API-key-like
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),                    # SSN-like
    re.compile(r"\b(?:\d[ -]*?){13,16}\b"),                  # card-like sequence
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-{2,}")  # email
]

def policy_check(text: str) -> None:
    for pat in _PATTERNS:
        if pat.search(text):
            raise ValueError("Policy violation: potential sensitive data detected.")


def validate_answer(payload: dict) -> FinalAnswer:
    try:
        obj = FinalAnswer(**payload)
    except ValidationError as e:
        raise ValueError(f"Schema validation failed: {e}") from e

    policy_check(obj.answer)
    return obj

```

本指南锁定了 `pydantic<2`，因此验证使用了 `Pydantic v1 的 @validator`。如果使用 `Pydantic v2`，请将 `@validator` 替换为 `@field_validator`。

---

## 步骤 4：代理层（有界循环 + 超时/重试）

两个关键的生产提示：

1. 无界代理循环存在成本和安全风险。
2. 超时和重试对于可靠性来说是必选项。

额外提示：不要将内部暂存盘（scratchpad）泄露到用户可见的消息中。

```python

# agent_setup.py
import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY must be set.")

llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
    temperature=0,
    openai_api_key=api_key,
    request_timeout=30,
    max_retries=2,
)


# Safer than unbounded ConversationBufferMemory:
# keeps only the last 10 turns to avoid silent token growth.
memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=10
)

def fetch_internal_summary(query: str) -> str:
    # placeholder for internal systems (DB/logs/tickets)
    return f"Internal summary for: {query}"

tools = [
    Tool(
        name="InternalData",
        func=fetch_internal_summary,
        description="Fetch internal operational context (tickets/runbooks/metrics summaries)."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=False,
    max_iterations=5,
    early_stopping_method="generate",
)

```

对于生产部署，优先选择外部化的会话状态。对于小型示例，窗口化的进程内内存是可以接受的，但分布式服务应将会话历史记录存储在应用程序进程之外。

> “工程化生产 AI 系统与其说在于‘哪个模型最好’，不如说在于系统在压力事件（如局部停机、数据漂移、不可预测的用户输入和成本约束）下的表现如何。”

---

## 步骤 5：不牺牲并发性的异步 API

异步 Web 服务器经常会被 LangChain 代理阻塞。直接在 `async def` 中调用它们会在负载下降低并发性，应将其卸载到线程池。

```python

# api.py
import json
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.concurrency import run_in_threadpool
from agent_setup import agent
from guardrails import validate_answer
from rag import retrieve, rerank_bm25
from tools import web_fetch

logger = logging.getLogger(__name__)
app = FastAPI()

class AskRequest(BaseModel):
    question: str
    use_web: bool = False

@app.post("/ask")
async def ask(payload: AskRequest):
    # 1) Retrieve once per request, not every agent step.
    from app_startup import index

    hits = retrieve(index, payload.question, k=6)
    top_docs = rerank_bm25(payload.question, hits, top_n=3)

    # Include source attribution for trust, debugging, and compliance.
    context = [
        {
            "text": d.page_content[:1200],
            "source": d.metadata.get("source")
        }
        for d in top_docs
    ]
    sources = [c["source"] for c in context if c.get("source")]
    # 2) Optionally fetch external information with bounded tool behavior.
    if payload.use_web:
        # In production, use a domain allowlist instead of arbitrary URLs.
        web = await web_fetch("https://example.com")
        sources.append(web.url)
        context.append({"text": web.text[:1200], "source": web.url})
    # 3) Ask the agent using a threadpool because agent.run is blocking.
    prompt = (
        "Use the following context to answer. "
        "Return JSON only with keys: answer, sources, cost_tokens.\n\n"
        f"CONTEXT: {context}\n\n"
        f"QUESTION: {payload.question}"
    )
    raw = await run_in_threadpool(agent.run, prompt)
    # 4) Parse/validate and fail closed.
    try:
        payload_json = json.loads(raw)
    except Exception as e:
        logger.warning(
            "Agent output parse failed: %s | raw=%s",
            e,
            raw[:200] if isinstance(raw, str) else str(raw)[:200]
        )
        payload_json = {
            "answer": "Unable to produce valid structured output.",
            "sources": sources,
            "cost_tokens": 0
        }
    # Merge sources explicitly, filtering out None and empty strings.
    seen = set()
    merged_sources = []

    for source in payload_json.get("sources", []) + sources:
        if source and source not in seen:
            seen.add(source)
            merged_sources.append(source)

    payload_json["sources"] = merged_sources
    payload_json["cost_tokens"] = int(payload_json.get("cost_tokens", 0))

    obj = validate_answer(payload_json)
    return obj.dict()

```

在生产环境中，解析失败不应默默消失。记录模型原始输出的截断版本有助于工程师调试格式错误的响应，同时避免完整的提示词或内部推理泄露。来源合并也经过显式处理，以避免空条目或重复项。

---

## 步骤 6：可观测性（真正的 OpenTelemetry，而非靠氛围编程）

在生产环境中，可观测性不是可选项。你需要：

* 跨越 API → 工具 → 模型调用的追踪；
* 延迟细分；
* 错误预算；
* 以及成本/Token 代理。

至少，对你的 FastAPI + HTTP 客户端进行检测非常重要：

```python

# otel.py
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry import trace

def setup_otel(app):
    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter())
    )
    FastAPIInstrumentor.instrument_app(app)
    HTTPXClientInstrumentor().instrument()

```

在应用启动时调用 `setup_otel(app)`。

---

## 生产检查清单（Demo 与平台之间的区别）

在称之为“生产就绪”之前，请验证：

* 版本锁定（Lockfile/约束）；
* 代理的有界循环（`max_iterations`）；
* 处处可见的超时 + 重试（LLM + 工具 + HTTP）；
* 索引持久化（不在导入时重建）；
* 每个检索块的来源归属；
* 结构化输出（仅 JSON + 模式验证）；
* 并发安全（线程池卸载）；
* 遥测（[追踪 + 指标 + 日志](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/)）；
* 成本控制（Token 预算、截断、缓存）。

这就是原型如何转变为平台，以及平台如何在大规模环境下生存。

---

## 超越原型阶段

工程化生产 AI 系统与其说在于“哪个模型最好”，不如说在于系统在压力事件（如局部停机、数据漂移、不可预测的用户输入和成本约束）下的表现如何。

当你引入代理和工具使用时，你实际上是在部署一个能推理、调用依赖并产生面向业务输出的[分布式系统](https://thenewstack.io/rethinking-system-architecture-the-rise-of-distributed-intelligence-with-ebpf/)。这要求具备我们对任何关键服务所期望的成熟度：显式契约、有界执行、可观测性、安全默认值和受控发布。

好消息是：你不需要一个庞大的平台团队就能开始。如果你实施了本指南中的基本原则——持久化检索、鲁棒的工具、经过验证的结构化输出、来源归属、有界代理循环、异步安全执行和真正的遥测——你就已经跨越了从“酷炫 Demo”到“运营服务”的界限。

从那里开始，扩展生产就绪平台就变成了一项工程练习，涉及：自动扩展、多租户隔离、网格侧的策略强制执行以及持续评估。这是将 AI 从实验转变为可靠企业能力的必经之路。