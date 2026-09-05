**When enterprise AI applications scale, they inevitably hit a wall**. For many engineering teams, this wall is initially diagnosed as a billing issue, a monthly API invoice that has grown out of control. However, viewing token consumption purely as a financial metric fundamentally misunderstands how LLMs operate in production. Token optimization, unlike its other optimization cousins, is not an accounting exercise; it’s a distributed systems and hardware utilization challenge.

> “Token optimization, unlike its other optimization cousins, is not an accounting exercise; it’s a distributed systems and hardware utilization challenge.”

In this guide, we explore, through the lens of Concierge (a latency-sensitive, synchronous [customer support agent](https://thenewstack.io/openai-presence-enterprise-agents/)) and Pathfinder (an asynchronous, multi-step autonomous CI debugging agent), how these systems fell victim to autoregressive bottlenecks as they grew, and how we fixed these issues.

## What you’re actually paying for

A token is not a word: treating it like one will break your budgeting “models.” Every major [LLM provider tokenizes](https://thenewstack.io/what-is-an-llm-token-beginner-friendly-guide-for-developers/) text using byte-pair encoding (BPE), breaking words into subword units. While common words stay intact, rarer words or punctuation split into fragments. As a rule of thumb, 1 token = 4 characters, or 0.75 words in standard English prose.

When budgeting for production, you must account for the structural pricing spread; providers bill input tokens and output tokens at different rates. Output tokens are typically 4-5X more expensive than input tokens.

As a baseline, assume a mid-tier frontier model runs roughly $3 per million input tokens and $15 per million output tokens.

## The quadratic history tax

LLM provider APIs are completely stateless; to make an LLM behave as if it remembers past events, you must resend the entire history of the session and input with every single API call.

This means that a model’s own previous outputs are continuously re-billed to you as inputs on subsequent steps. This triggers a compounding cost that impacts both *Concierge* and *Pathfinder,* though their curves scale differently.

Let *S* be the static system context (instructions and schemas), *u* be the incoming data per step, and r be the model’s response payload. The input cost for every given turn k is

![Formula defining the input cost for every given turn.](https://cdn.thenewstack.io/media/2026/09/c6d6eb93-image2.png)

When you sum this across a complete execution run of *N* steps, the total input token volume compounds quadratically.

![Formula for the total input cost, i.e. the sum of input costs of every given turn in an execution run of N steps.](https://cdn.thenewstack.io/media/2026/09/ed5c2910-image3-1024x88.png)

This `O(N^2)` accumulation of history is the exact mechanism that causes the explosion in cost and latency.

|  |  |  |
| --- | --- | --- |
| **Variable** | **Concierge (Chat system)** | **Pathfinder (Autonomous agent)** |
| Static context (S) | 3,100 tokens (Full returns/shipping policies and brand guidelines) | 1,200 tokens (Tool definitions, system constraints, CI environment data) |
| Incoming data (u) | 80 tokens (Short customer chat replies) | 900 tokens (Massive raw text payloads: log excerpts, file reads, shell outputs) |
| Response payload (r) | 220 tokens (Polite customer-facing answers) | 300 tokens (Internal monologue + JSON Tool Arguments) |
| Step multiplier (N) | 10 turns (Average support thread length) | 15 steps (Average agent troubleshooting loop length) |

When we calculate the total input tokens consumed by a single session using the quadratic formula

* **Concierge**: Consumed 45,300 tokens per 10-turn ticket
* **Pathfinder**: Consumed 150,000 tokens per 15-step turn

Because Pathfinder’s step increment was 4X larger than Concierge, its token cost curve was drastically steeper. If Pathfinder were to get stuck in an infinite tool-use loop and hit 30 steps, a single run could consume **570,000 tokens**.

## The solution

### Fixing the individual call

**Prompt hygiene:** Hardcoding static reference documentation into the system prompt means you pay to parse identical text on every turn. So we stripped static text from the prompt and switched to dynamic injection.

For Concierge, we implemented a RAG step to fetch only the 2-3 policy snippets relevant to the ticket. The prompt dropped from 3,100 tokens to 380. A 60% reduction for a 10-turn thread.

For Pathfinder, we applied automated prompt compression using *LLMLingua-2* to compress verbose CI log files before sending them to the model. By filtering out non-essential log lines, we reduced the size of incoming tool observations by 3X without sacrificing debugging accuracy.

```

from llmlingua import PromptCompressor

compressor = PromptCompressor(
model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
use_llmlingua2=True
)

try:
compressed_result = compressor.compress_prompt(
raw_ci_log_text,
rate=0.33,
force_tokens=["Error", "Exception", "Failed", "Traceback", "FATAL"]
)
# Pass high-density payload to the frontier model
compact_prompt = compressed_result["compressed_prompt"]
except Exception as e:
print(f"Compression failed, falling back to raw log text: {e}")
# Graceful degradation: pass the raw (or truncated) log if compression fails
compact_prompt = raw_ci_log_text

```

**Eliminating the retry**: Relying on open-ended prose instructions “return JSON” caused malformation. When parsing failed, the system initiated a synchronous retry, sending the entire accumulated context as if it were a new attempt. We replaced the entire natural language formatting request with strict structural contracts via forced schema validation.

In both Concierge and Pathfinder, we converted the output format to a strict pydantic schema for tool-calling mode and tool-execution payloads. Malformed outputs across both systems dropped to under 0.5%, eliminating tail latency spikes caused by cascading queues.

```

# Unified Schema Enforcement for Concierge Responses &amp; Pathfinder Tool Execution
from pydantic import BaseModel
from typing import Literal

class TicketResponse(BaseModel):
    reply: str
    category: Literal["shipping", "returns", "billing", "product", "other"]
    escalate: bool
    confidence: float

# The API is structurally locked into emitting validated JSON matching the schema
response = client.messages.create(
    model="claude-opus-4",
    system=SYSTEM_PROMPT,
    messages=messages,
    tools=[
    {
    "name": "respond_to_ticket",
    "description": "Formulate a response and classify the support ticket.",
    "input_schema": TicketResponse.model_json_schema()
    }
    ],
    tool_choice={"type": "tool", "name": "respond_to_ticket"},
)

```

**Output token bounding:** Models naturally generate verbose reasoning chains and conversational filler, inflating expensive output tokens. Where the LLM provider exposes logit bias, you can directly suppress every token outside the valid set at decode time; where it doesn’t, constrained decoding libraries (Outlines, Guidance) or a forced tool call with an enum-typed schema will get you the same guarantee.

```

class ClassifyOnly(BaseModel):
    category: Literal["shipping", "returns", "billing", "product", "other"]
    priority: Literal["low", "medium", "high", "urgent"]

```

### State management

The stateless nature of the models meant we had to parse the static prompt prefix and historical steps on every turn. We introduced explicit cache breakpoints to allow the inference engine to reuse the states of static blocks. We altered both Concierge and Pathfinder to flag stable, historical segments for caching. Under standard vendor pricing, cache reads are discounted by 90%. *It is important to check with your vendor on whether caching is enabled.*

```

# Caching the stable history prefix for a multi-turn session
response = client.messages.create(
    model="claude-sonnet-4",
    max_tokens=4096,
    system=[{
        "type": "text",
        "text": SYSTEM_PROMPT,
        "cache_control": {"type": "ephemeral"} # Cache hits drop prefix costs by 90%
    }],
    tools=TOOL_SCHEMAS,
    messages=session_history + [{"role": "user", "content": current_step_input}],
)

```

For a 10-turn Concierge chat, this dropped input costs by ~70%. For a 15-step Pathfinder trajectory, it resulted in a 76% cost reduction.

### Semantic caching

Duplicate queries across separate sessions were triggering redundant frontier model invocations. We implemented a vector similarity cache layer upstream of the LLM using Redis. Our Concierge service analysis showed that 34% of customer support tickets were semantic duplicates of common FAQs.

Intercepting these requests reduced latency to sub-50ms for hits. Because of the nature of CI pipeline logs, we have not yet found a suitable cache for Pathfinder’s inputs.

```

import os
import json
import redis
from redis.commands.search.query import Query

# Configure connection via environment variable for environment portability
redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379")
r = redis.Redis.from_url(redis_url)

def get_cached_response(tenant_id, query_text, threshold=0.92):
    try:
results = r.ft(f"cache_idx:{tenant_id}").search( # scoped by tenant -- see below
Query("*=>[KNN 1 @vector $vec AS score]").sort_by("score").dialect(2),
query_params={"vec": query_vec.tobytes()},
)
except redis.RedisError as e:
print(f"Redis cache error: {e}")
return None # Fail-open: gracefully fall back to a cache miss)
  query_vec = embed(query_text) # small, fast bi-encoder -- not the frontier model

try:
results = r.ft(f"cache_idx:{tenant_id}").search( # scoped by tenant -- see below
Query("*=>[KNN 1 @vector $vec AS score]").sort_by("score").dialect(2),
query_params={"vec": query_vec.tobytes()},
)
except redis.RedisError as e:
print(f"Redis cache error: {e}")
return None # Fail-open: gracefully fall back to a cache miss

```

Semantic caching could be a security problem, because if you choose a global cache, Customer A’s account-specific answer could get served to Customer B because their phrasing embeddings are close enough. To mitigate this, we split the cache into two tiers: a global cache for tenant-agnostic content, and a per-tenant, per-user namespace keyed with the tenant ID baked into the prefix itself for anything touching account state.

Cache poisoning is another risk: we only write to the cache from responses that passed schema validation and the injection-pattern classifier, we stamp every cache entry with its source traceId, and we encourage routine purging of unknown caches.

### Context compaction

Uncapped conversation or agent trajectories allowed N to grow continuously, expanding the cost curve and causing latency degradation. We capped N by implementing a sliding window that summarizes historical context via a small, ultra-cheap model. For Concierge, we kept the last 3 turns verbatim while condensing older turns into a rolling metadata block.

For Pathfinder, when the debugging steps exceeded 4 runs, we trimmed and summarized the oldest tool execution outputs into a compact chronological timeline, transforming the open-ended quadratic cost explosion into a predictable, bounded window.

```

def compact_session_history(history_steps: List[Dict[str, Any]], keep_recent: int = 3) ->     List[Dict[str, Any]];
    """Flattens older history into a cheap summary block, preserving recent context."""
    if len(history_steps) &lt;= keep_recent:
        return history_steps
    old_steps = history_steps[:-keep_recent]
    recent_steps = history_steps[-keep_recent:]
    
# Compress the old history using a fast, low-cost utility model
try:
historical_summary = summarize_with_utility_model(old_steps)
# Note: Anthropic prohibits 'system' roles in the messages array.
# Using 'assistant' ensures cross-provider compatibility.
return [{"role": "assistant", "content": f"[System Context: Summary of prior steps: {historical_summary}]"}] + recent_steps
except Exception as e:
print(f"History compression failed: {e}")
# Fallback: Return the uncompressed history to gracefully degrade
return history_steps

```

### Model cascading

Directing every single operation to an expensive frontier model represents massive overprovisioning for mundane tasks. We integrated LiteLLM as an internal routing gateway to implement model cascading, routing every request to the lowest-cost model capable of completing the task.

> “Directing every single operation to an expensive frontier model represents massive overprovisioning for mundane tasks.”

```

# litellm_config.yaml
model_list:
  - model_name: fast-path
    litellm_params:
      model: openai/mistral-support-ft
      api_base: http://vllm-internal:8000/v1
  - model_name: frontier-path
    litellm_params:
      model: anthropic/claude-opus-4

```

Simple, repetitive tasks are routed to a lower model, which offloads 70% of Concierge chats from the frontier model. For Pathfinder, we broke the agent loop down into separate sub-tasks: high-level planning, tool selection, and code-patch synthesis remained with the frontier model, while mechanical, text-heavy operations, such as log parsing, regex extraction, and error-string formatting, were offloaded to the lower models. This hybrid orchestration reduced Pathfinder’s token costs by more than 50%.

## What’s next

The transformation of Concierge and Pathfinder proves a fundamental truth about production AI. You cannot achieve scale by simply relying on the natural language capabilities of a frontier model. You must engineer the system around it. By shifting your focus from naive token reduction to maximizing system resource utilization, we reclaimed absolute control over the infrastructure.

> “Efficiency in the era of gen AI is not defined by how cheaply you can operate but by how densely you can pack information.”

Efficiency in the [era of gen AI](https://thenewstack.io/gitlab-ai-agents-jevons-paradox/) is not defined by how cheaply you can operate but by how densely you can pack information, how quickly you can serve it, and how reliably you can parse the output. The architectural decisions detailed here represent more than just a token optimization strategy; they are a required foundation for building high-throughput, battle-tested, and resilient AI systems at scale.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/65126d72-borisheadshot-1-600x600.png)

Boris Chabeda is a systems engineer focused on the intersection of high-concurrency infrastructure and intelligent automation. His work centers on architecting resilient environments that bridge the gap between experimental development and production-grade reliability. By integrating specialized languages and agentic frameworks,...

Read more from Boris Chabeda](https://thenewstack.io/author/boris-chabeda/)