Debugging used to be straightforward: A service failed, you checked the logs, followed the stack trace, and fixed the bug. Unfortunately, with AI systems, especially those powered by LLMs and agent workflows, that approach breaks down quickly.

The problem doesn’t just lie in a more complex system. It’s complicated by the fact that failures are no longer deterministic. The system may return a different answer for the same input. A tool might silently fail. Retrieval might return low-quality or noisy context. Nothing overtly “crashes,” but something is clearly wrong.

This tutorial focuses on a practical question: How do we debug a system that doesn’t fail in obvious ways?

To tackle this question, we’ll build a small AI service and, more importantly, instrument it so that we can actually understand what’s happening inside it.

---

## Why debugging AI systems feels different

Traditional debugging relies on three assumptions:

* Inputs lead to predictable outputs
* Failures throw errors
* Logs tell the full story

None of these holds for AI systems.

Instead, we deal with:

* Non-deterministic outputs
* Hidden reasoning steps
* External dependencies (retrieval, APIs, tools)
* Large, dynamic prompts

This means debugging must shift from log-based thinking to observability-driven engineering.

> “Debugging must shift from log-based thinking to observability-driven engineering.”

---

## What we’re building

We’ll create a simple AI question-answering service with:

* Retrieval (vector search + reranking)
* External tool calls
* LLM reasoning
* Structured output validation
* Observability ([tracing + logging](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/) + token estimation)

The focus is not just on building it, but on making it **debuggable**.

### Architecture overview: a debuggable AI system

![Diagram showing the architecture of a debuggable AI system](https://cdn.thenewstack.io/media/2026/05/e68cbcf2-11-1024x835.png)

This architecture highlights a key shift in modern AI Systems: [Observability](https://thenewstack.io/introduction-to-observability/) is a core component rather than an afterthought. Each stage of the workflow, from retrieval to tool execution to model reasoning, is instrumented, enabling engineers to trace decision-making. This makes it possible to debug not just failures but also unexpected behaviors, which are far more common in AI systems than in traditional software.

---

### Step 1: install dependencies

```

bash
pip install fastapi uvicorn \
  langchain langchain-openai langchain-community \
  faiss-cpu rank-bm25 \
  httpx tenacity \
  opentelemetry-api opentelemetry-sdk \
  opentelemetry-instrumentation-fastapi \
  opentelemetry-instrumentation-httpx \
  tiktoken pydantic

```

We explicitly include OpenTelemetry because debugging AI systems without tracing is like flying blind.

---

### Step 2: initialize the model (with production controls)

```

Python
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

Timeouts and retries are not optional. When something fails, you need to know if it’s your system or the model provider.

---

### Step 3: add retrieval (and make it observable)

```

Python
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

Now, retrieval

```

Python
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

#### Debugging insight

If the retrieval is wrong, everything downstream is wrong as well.

Always log what documents were retrieved.

---

```

Python
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

Production AI systems should never allow unrestricted outbound requests from model-generated inputs. Without domain allowlists, agents can become SSRF vectors that can probe internal services, cloud metadata endpoints, or private infrastructure. Restricting outbound access to trusted domains is a minimal production safeguard.

> “Production AI systems should never allow unrestricted outbound requests from model-generated inputs.”

#### Debugging insight

Tool [failures are silent killers](https://thenewstack.io/mastering-deadman-alerts-to-prevent-silent-failures/). Without retries and logging, you won’t know if:

* The tool failed
* The tool returned empty data
* The model ignored the tool

---

### Step 5: token visibility (not exact, but useful)

```

Python
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

Token counting should be treated as an operational estimate, not an exact billing mechanism. Real request cost depends on the full message payloads, retrieved context, tool-call arguments, system prompts, provider-side formatting, and generated output tokens. Even approximate tracking, however, is extremely useful for debugging runaway agents and monitoring cost regressions in production systems.

#### Debugging insight

Unexpected cost spikes often come from:

* large retrieved context
* repeated loops
* oversized prompts

---

### Step 6: build the agent workflow (deterministic)

```

Python
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

#### Debugging insight

We’re sticking to a deterministic flow, so we don’t have to deal with tools or agents acting out on their own.

---

### Step 7: validate output (guardrails)

```

Python
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

#### Debugging insight

Failures here tell you:

* The model ignored instructions
* The output format changed
* Something upstream corrupted the context

---

### Step 8: add observability

```

Python
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

Instrumentation alone does not make traces visible. OpenTelemetry requires a tracer provider, span processor, and exporter to record and emit telemetry data. For local debugging, a console exporter is sufficient. In production systems, traces are typically exported via OTLP collectors to platforms such as Jaeger, Grafana, Tempo, Datadog, or Honeycomb.

#### Add endpoint:

```

Python
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

## What you can now debug

With this setup, you can answer questions like:

**“Why was the answer wrong?”**

* Check retrieved documents

**“Why did the output change?”**

* Compare context and token size

**“Why is latency high?”**

* Trace LLM vs tool vs retrieval

**“Why is the cost increasing?**

* Inspect token estimates and context size

---

## Engineering principle: make AI systems observable

AI systems are not just models. They are pipelines for:

* retrieval
* reasoning
* tools
* validation

Each part can fail independently. You need visibility at every step, or you’re essentially debugging in the dark.

> “Each part can fail independently. You need visibility at every step, or you’re essentially debugging in the dark.”

---

## Production lessons

1. **Logs are not enough**

You need traces that show the full execution path

2. **Retrieval errors look like model errors**

Always inspect the context first

3. **Tool failures are often silent**

Add retries and instrumentation

4. **Token growth is a hidden risk**

Monitor prompt size continuously

5. **Deterministic workflow simplifies debugging**

Fewer moving parts = fewer unknowns

---

## Conclusion

The takeaway here is that, since you’re dealing with a probabilistic system, your debugging tools (and approach) have to change. By introducing things like observability, deterministic workflows, structured validation, and proper tracing, you’re setting yourself up to see where the logic goes sideways (because it will).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/03/6dadf7f1-oladimeji-sowole.jpeg)

Oladimeji Sowole is a member of the Andela Talent Network, a private marketplace for global tech talent.  A Data Scientist and Data Analyst with more than 6 years of professional experience building data visualizations with different tools and predictive models...

Read more from Oladimeji Sowole](https://thenewstack.io/author/oladimeji-sowole/)