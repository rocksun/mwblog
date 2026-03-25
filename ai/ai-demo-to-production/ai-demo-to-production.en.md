Building an AI demo is easy. Shipping an AI system that runs reliably in production, day after day, under load, within budget, and with observability, is hard. Many teams discover this gap only *after* their impressive proof-of-concept collapses when exposed to real users, real data, and real operational constraints.

> “Building an AI demo is easy. Shipping an AI system that runs reliably in production… is hard.”

Production AI systems are more than models. They are distributed systems that must handle failures, control costs, evolve safely, and integrate with existing infrastructure. This guide shows the core architectural patterns behind production-grade AI systems, along with a simplified reference implementation.

You’ll learn how to:

* Structure an AI service for production
* Use modern LLM orchestration
* Add retrieval, guardrails, and cost awareness
* Deploy in a scalable, observable way

## Why AI breaks in production

Most AI demos fail in production for the same reasons:

* No clear separation between reasoning, retrieval, and execution
* Lack of observability (you don’t know what the model is doing)
* No cost controls or token limits
* Tight coupling between model logic and application logic
* No deployment strategy beyond “run this script”

Production AI systems must be treated like any other critical service: they must be versioned, monitored, and scalable to achieve resilience.

## Reference architecture

A production AI system typically includes:

1. API layer: FastAPI or similar
2. LLM orchestration layer: LangChain
3. Knowledge layer: Vector database (FAISS, Qdrant, Pinecone)
4. Tooling layer: APIs, databases, services
5. Guardrails: schema validation, policy checks
6. Observability: logs, metrics, traces
7. Infrastructure: containers, Kubernetes, IaC

We’ll implement a simplified, but realistic version of this stack in this guide.

## Step 1: Install dependencies

```

pip install fastapi uvicorn \
  langchain langchain-openai langchain-community \
  pydantic faiss-cpu tiktoken
```

Key points:

* `langchain-openai` is required for OpenAI models
* `langchain-community` provides vector stores and utilities

## Step 2: Initialize the LLM

```

import os
from langchain_openai import ChatOpenAI

openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY must be set")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    openai_api_key=openai_api_key
)
```

### Why this matters

* Explicit API-key validation [prevents silent failures](https://thenewstack.io/mastering-deadman-alerts-to-prevent-silent-failures/)
* `'gpt-4o-mini' is often a cost-efficient choice for production workloads that need strong latency and price-performance, though model selection should be validated against your accuracy and budget targets.`

## Step 3: Build a knowledge layer (vector store)

Production AI systems commonly use retrieval-augmented generation (RAG) to ground responses in real data.

```

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

embeddings = OpenAIEmbeddings(
model="text-embedding-3-small",
openai_api_key=openai_api_key
)

docs = &#91;
    Document(page_content="All customer data must be encrypted at rest."),
    Document(page_content="Refunds require manager approval above $500."),
]

vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
```

This enables:

* Enterprise knowledge grounding
* Reduced risk of hallucination
* Faster updates compared to retraining models

## Step 4: Expose retrieval as a tool

Agentic systems work best when retrieval is treated as a tool rather than hard-coded logic.

```

from langchain.tools import Tool

def retrieve_policy(query: str) -&gt; str:
    docs = retriever.invoke(query)
    return "\n".join(d.page_content for d in docs)

tools = &#91;
    Tool(
        name="PolicyRetriever",
        func=retrieve_policy,
        description="Retrieve internal company policies."
    )
]
```

This separation allows:

* Tool auditing
* Permission control
* Safe expansion later

## Step 5: Manage conversation state explicitly

```

from typing import Dict, List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

# Demo-only in-memory store.
# In production, replace with Redis, Postgres, DynamoDB, etc.
conversation_store: Dict&#91;str, List&#91;BaseMessage]] = {}

def load_history(session_id: str) -&gt; List&#91;BaseMessage]:
    return conversation_store.get(session_id, &#91;])

def append_user_message(session_id: str, content: str) -&gt; None:
    history = conversation_store.setdefault(session_id, &#91;])
    history.append(HumanMessage(content=content))

def append_ai_message(session_id: str, content: str) -&gt; None:
    history = conversation_store.setdefault(session_id, &#91;])
    history.append(AIMessage(content=content))
```

Memory is essential in production for:

* Conversational coherence
* User experience
* Stateful workflows

## Step 6: Initialize the agent (production-safe)

```

from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(&#91;
("system", "You are a helpful assistant that uses tools when needed."),
("human", "{input}"),
("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)
```

Once initialized, this agent can:

* Plan steps
* Call tools when needed
* Produce grounded responses

## Step 7: Validate and sanitize AI responses

Production systems should never return raw LLM output directly to users. Instead, responses should be validated, sanitized, and converted into a predictable schema before leaving the service boundary. This ensures downstream systems receive structured, reliable data and prevents malformed outputs from propagating through the system.

```

``` python
from pydantic import BaseModel, Field
from typing import List

class AgentResponse(BaseModel):
answer: str = Field(description="Direct answer to the user")
sources: List&#91;str] = Field(default_factory=list, description="Supporting sources")

structured_llm = llm.with_structured_output(AgentResponse)

result = structured_llm.invoke(
"Answer the user question and include any relevant source identifiers."
)
```
```

> “Production AI systems should never return raw LLM output directly to users. Instead, responses should be validated, sanitized, and converted into a predictable schema.”

Guardrails help reduce several classes of runtime issues, including:

* Unexpected output shapes
* Schema violations
* Some downstream parsing failures

However, guardrails alone are not sufficient to prevent prompt injection or unsafe tool execution. Production systems should also implement additional controls such as tool allowlists, authorization checks, input filtering, and human review for high-risk actions.

## Step 8: Wrap everything in a FastAPI service

```

``` python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Production AI Service")

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_agent(payload: Query):
try:
result = agent_executor.invoke({"input": payload.question})
return {"answer": result&#91;"output"]}
except Exception:
raise HTTPException(status_code=500, detail="Internal server error")
```
```

Why this matters:

* Decouples AI logic from clients
* Enables scaling, auth, rate-limiting
* Fits cleanly into microservice architectures

Run locally:

`uvicorn main:app --host 0.0.0.0 --port 8080`

## Step 9: Add cost awareness (often ignored)

Cost control is an important element of production AI.

```

``` python
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o-mini")

def estimate_tokens(messages: list&#91;dict]) -&gt; int:
    """
    Rough token estimate for a list of chat messages.

    Note: This is only an approximation. Real request cost depends on
    system prompts, retrieved context, tool call arguments, and
    generated output tokens returned by the model provider.
    """
    total_tokens = 0

    for message in messages:
        content = message.get("content", "")
        total_tokens += len(encoder.encode(content))

    return total_tokens
```
```

In production:

* Log tokens per request
* Set per-user or per-endpoint budgets
* Route cheap models for routine tasks

## Step 10: Observability basics

At minimum, log:

* Inputs
* Tool calls
* Token usage
* Errors

```

``` python
import logging
logging.basicConfig(level=logging.INFO)

def log_event(event: str, data: dict):
    logging.info({"event": event, **data})
```
```

In mature systems, integrate:

* OpenTelemetry
* Prometheus/Grafana
* Centralised log storage

## Step 11: Containerize for deployment

`Before containerising, create a requirements.txt file that matches the packages used in the guide.`

```

``` requirements.txt
fastapi
uvicorn
langchain
langchain-openai
langchain-community
pydantic
faiss-cpu
tiktoken
```
```

```

FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD &#91;"uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

This enables:

* Consistent environments
* Kubernetes deployment
* CI/CD pipelines

## Step 12: Scale with Kubernetes (conceptual)

In production, deploy:

* Multiple replicas
* Horizontal Pod Autoscaling
* Secrets via environment variables
* Resource limits for cost control

AI systems scale unpredictably. Kubernetes handles that complexity by design.

## Key production lessons

1. AI systems are [distributed](https://thenewstack.io/rethinking-system-architecture-the-rise-of-distributed-intelligence-with-ebpf/) systems
2. Observability can’t be optional
3. Cost must be controlled, not hoped for
4. Guardrails are necessary to protect both users and systems
5. Infrastructure matters as much as models

## A refreshed approach to production AI

[Moving AI from demos to production requires](https://thenewstack.io/ai-prototype-to-production-postgres/) better systems and a complete abandonment of hype.

Reliable AI systems require thoughtful architecture, clear separation of concerns, and production discipline. By combining modern LLM orchestration, retrieval, guardrails, observability, and cloud-native deployment, teams can build AI services that are not only impressive but dependable and resilient through production.

The organizations that win will treat AI as production software, engineered with the same rigour as any mission-critical system.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/03/6dadf7f1-oladimeji-sowole.jpeg)

Oladimeji Sowole is a member of the Andela Talent Network, a private marketplace for global tech talent.  A Data Scientist and Data Analyst with more than 6 years of professional experience building data visualizations with different tools and predictive models...

Read more from Oladimeji Sowole](https://thenewstack.io/author/oladimeji-sowole/)