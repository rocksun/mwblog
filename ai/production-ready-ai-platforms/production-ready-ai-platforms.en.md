### Starting from square one

Most teams can build an AI prototype. A notebook answers a few prompts, a demo agent calls a tool once, and the room claps. Then reality shows up. Progress is halted by production traffic, noisy inputs, strict SLAs, compliance reviews, and cost pressure. This is where “AI as a feature” becomes “AI as a platform engineering problem.”

The trend is clear: platform teams are treating AI agents as a new execution model that needs shared infrastructure, security boundaries, observability, reliability controls, and governance. One could say it’s eerily similar to what microservices needed a decade ago. And as service meshes mature, they’re increasingly used to enforce zero-trust communication, timeouts, retries, and traffic shaping for AI services, without rewriting app logic.

> “Most teams can build an AI prototype. A notebook answers a few prompts, a demo agent calls a tool once, and the room claps. Then reality shows up.”

This is meant to serve as a guide on how to move from demo to a dependable system by building a small but realistic “AI platform slice.” The end result: a production-ready AI service with retrieval, tooling, guardrails, [observability](https://thenewstack.io/introduction-to-observability/), and deployment hygiene.

### **What you’ll build**

A production-grade AI Research & Decision Support API that:

* Retrieves internal knowledge (vector search + BM25 rerank)
* Fetches external web pages safely (timeouts/retries + parsing)
* Returns structured JSON with sources for trust and audit
* Tracks token/cost signals and emits traces/metrics
* Runs safely under load (bounded agent loops + async concurrency-safe execution)

---

## Step 0: Install the essentials (production-safe)

Pinning matters. “Works on my machine” failures happen when dependency graphs drift. We see this especially with LangChain’s package splits and Pydantic major changes.

```

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

## Step 1: Define robust tool interfaces (timeouts + retries + clean outputs)

Tools should behave like reliable services, complete with: explicit inputs/outputs, bounded time, resilient retries, and safe parsing. Avoid naive HTML parsing.

```

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

Why this matters in production:

* Retries handle transient network failures without “agent hang.”
* Truncation prevents token/cost explosions.
* BeautifulSoup avoids brittle `<title>` splitting.

---

## Step 2: Build retrieval correctly (no “build at import time”)

A common production anti-pattern is rebuilding embeddings and indexes on app startup. It’s slow, expensive, and brittle. There’s a better way: Build once, persist, then load at boot.

```

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

In production, rerankers should avoid rebuilding expensive intermediate structures on every request. By caching the BM25 object using a hashable corpus fingerprint, repeated reranking over the same retrieved document set becomes cheaper and more predictable under load.

How this differs from demo RAG:

* Uses modern imports (`langchain_community`, `langchain_openai`)
* Uses BM25 reranking (more robust than naive lexical matching)
* Caches BM25 indices to avoid rebuilding on repeated queries
* Supports persist/load to avoid expensive startup builds

---

## Step 2.5: Build once offline, load at runtime

Do this as a one-time admin job (or CI job):

```

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

Then your app loads it fast:

```

# app_startup.py
from rag import load_index

index = load_index("./faiss_index")

```

---

## Step 3: Guardrails that reflect production intent

In production, “policy checks” need to be more than naive keyword lists. At a minimum, you should separate:

* Schema validation (is it shaped correctly?)
* Content policy (does it contain secrets/PII patterns?)

This guide pins `pydantic<2` for compatibility, but uses explicit validators instead of type-based constraints to improve readability and maintain forward compatibility with Pydantic v2.

```

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
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")  # email
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

This guide pins `pydantic<2`, so the validation uses `Pydantic v1’s @validator`. If using `Pydantic v2`, replace `@validator` with `@field_validator`.

---

## Step 4: The agent layer (bounded loops + timeouts/retries)

Two key production reminders:

1. Unbounded agent loops are a cost and safety risk.
2. Timeouts and retries are non-optional for reliability.

Bonus tip: Don’t leak internal scratchpad into user-visible messages.

```

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

For production deployments, prefer externalized session state. Windowed in-process memory is acceptable for small examples, but distributed services should store conversation history outside the application process.

> “Engineering production AI systems is less about ‘which model is best’ and more about how the system behaves under stress events like partial outages, drifting data, unpredictable user inputs, and cost constraints.”

---

## Step 5: Async API without killing concurrency

Async web servers often block LangChain agents. Calling them directly inside `async def` will reduce concurrency under load while offloading to a threadpool.

```

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

In production, parsing failures should not disappear silently. Logging a truncated version of the raw model output helps engineers debug malformed responses while avoiding full prompt or internal reasoning leakage. Source merging is also handled explicitly to avoid empty or duplicate provenance entries.

---

## Step 6: Observability (real OpenTelemetry, not vibes)

In production, observability is not optional. You want:

* Traces across API → tools → model calls;
* Latency breakdowns;
* Error budgets’
* And cost/token proxies.

At minimum, it’s important to instrument your FastAPI + HTTP clients:

```

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

Call `setup_otel(app)` in your app startup.

---

## Production checklist (the difference between demo and platform)

Before you call it “production-ready,” verify:

* Version pinning (lockfile/constraints);
* Bounded loops for agents (`max_iterations`);
* Timeouts + retries everywhere (LLM + tools + HTTP);
* Index persistence (no rebuild at import time);
* Source attribution for every retrieved chunk;
* Structured outputs (JSON-only + schema validation);
* Concurrency safety (threadpool offload);
* Telemetry ([traces + metrics + logs](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/));
* Cost controls (token budgets, truncation, caching).

This is how prototypes become platforms, and how platforms survive scale.

---

## Moving beyond prototypes

Engineering production AI systems is less about “which model is best” and more about how the system behaves under stress events like partial outages, drifting data, unpredictable user inputs, and cost constraints.

When you introduce agents and tool use, you’re effectively deploying a [distributed system](https://thenewstack.io/rethinking-system-architecture-the-rise-of-distributed-intelligence-with-ebpf/) that reasons, calls dependencies, and produces business-facing outputs. That demands the same maturity we expect from any critical service: explicit contracts, bounded execution, observability, safe defaults, and controlled rollout.

The good news: You don’t need a giant platform team to start. If you implement the fundamentals in this guide, persisted retrieval, robust tools, validated structured outputs, source attribution, bounded agent loops, async-safe execution, and real telemetry, you’ll have crossed the line from “cool demo” to “operational service.”

From there, scaling a production-ready platform becomes an engineering exercise involving: autoscaling, multi-tenant isolation, policy enforcement at the mesh, and continuous evaluation. This is the path that turns AI from experiments into a reliable enterprise capability.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/03/6dadf7f1-oladimeji-sowole.jpeg)

Oladimeji Sowole is a member of the Andela Talent Network, a private marketplace for global tech talent.  A Data Scientist and Data Analyst with more than 6 years of professional experience building data visualizations with different tools and predictive models...

Read more from Oladimeji Sowole](https://thenewstack.io/author/oladimeji-sowole/)