Recently, a crucial RAG pipeline used by one of our corporate clients began hallucinating about financial numbers without notifying us of any errors or failures. Our dashboards displayed the system’s health in green; all tests went well. However, the system confidently recommended to its users that they invest in certain stocks because their earnings would rise significantly. Unfortunately, that report was completely fictional.

It took us three extremely painful days to pinpoint the cause of the issue: a small change to a prompt template caused the LLM to ignore the context altogether and rely solely on its pre-trained weights.

This experience surfaced how incredibly unfriendly modern AI systems are to conventional debugging methods.

If you face any issues with classic software, you know exactly where in code something goes wrong: you have a line number, an error message, a stack trace, and perhaps even a *NullReferenceException*.

> “There is no console.logging your way out of a probabilistic error, and no breakpoints to debug neural networks’ internal state.”

If you run into problems with an AI-powered solution, you will not find any bugs there, and the system still works flawlessly. Instead, it produces an outright fabrication, skips a critical part of the reasoning, picks up an irrelevant source, and builds a perfect argument based on false information. There is no *console.logging* your way out of a probabilistic error, and no breakpoints to debug neural networks’ internal state.

To make it through the age of Generative AI, we need a new way to conceptualize debugging.

## The paradigm shift: deterministic vs. probabilistic bugs

To understand why our current tooling fails, we must first understand how the nature of the bugs has changed.

|  |  |  |
| --- | --- | --- |
| **Feature** | **Traditional debugging** | **Gen AI debugging** |
| **Failure mode** | Binary (Pass/Fail, Crash, Exception) | Gradients of wrong (Hallucination, Drift, Omission) |
| **Root cause** | Logical flaw, syntax error, bad state | Poor retrieval, ambiguous prompt, model drift |
| **Reproducibilty** | High (Given exact inputs, outputs match) | Low (Same inputs can yield different outputs) |
| **Primary tool** | Breakpoints, Stack Traces, Unit Tests | Execution Traces, Evals, Payload Logging |

> “In traditional software, a bug is a flaw in the instructions. In Generative AI, a bug is a flaw in the contextual environment.”

In traditional software, a bug is a flaw in the instructions. In Generative AI, a bug is a flaw in the contextual environment you provided to the model. If you treat an LLM failure like a logic bug, you will waste hours rewriting wrapper code when the real issue is a poorly chunked PDF in your vector database.

## Modern approach to debugging and monitoring of generative AI systems

The systems that make it past the production gate will view AI systems not as some magical function call but rather as an I/O-bounded external subsystem with all its randomness and unpredictability. Let’s take a look at how modern engineers solve the challenge of probabilistic code debugging.

### Stop stepping, go asynchronous

During the [multi-step agent workflow](https://thenewstack.io/groundcover-ai-observability-agents/) (e.g., Query → Retrieve → Tool Call → Synthesize), any malfunction that happens during synthesis is most likely because of faulty retrieval three steps back.

Stepping through your code won’t help here; instead, you should create trace graphs. All interactions require capturing the whole payload. And since LLM calls are network-bound and take seconds to resolve, your tracing needs to be done asynchronously to avoid blocking your event loop.

Below is an example of how you could wrap your system into modern asynchronous tracing without breaking a FastAPI application while emitting well-structured JSON to `stdout` for further consumption by Datadog, CloudWatch, or OpenTelemetry.

```

Python
import time
import json
import logging
from string import Template 
from typing import Callable, Dict, Any, List

# Configure structured logging for production ingestion
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def trace_llm_execution(
    step_name: str, 
    async_llm_callable: Callable, 
    prompt_template: str, 
    context: List[str], 
    user_query: str
) -> Dict[str, Any]:
    
# 1. Use string.Template for safer hydration to avoid KeyError on user input containing '{}'
template = Template(prompt_template)
hydrated_prompt = template.safe_substitute(
context="\n".join(context),
query=user_query
) 
    
    start_time = time.perf_counter()
    error = None
    raw_response = None
    
    try:
        # 2. Await the probabilistic call to keep the thread unblocked
        raw_response = await async_llm_callable(hydrated_prompt)
    except Exception as e:
        error = str(e)
        
    latency_ms = round((time.perf_counter() - start_time) * 1000, 2)
    
    # 3. Create an immutable artifact of the exact state
    trace_artifact = {
        "event": "llm_trace",
        "step": step_name,
        "latency_ms": latency_ms,
        "hydrated_prompt": hydrated_prompt, # Crucial: What did the model actually see?
        "raw_context_chunks": context,      # Crucial: Did the DB return garbage?
        "raw_response": raw_response,
        "error": error
    }
    
    # 4. Emit to stdout for observability platforms
    logger.info(json.dumps(trace_artifact))
        
    if error:
        raise RuntimeError(f"Step {step_name} failed: {error}")
        
    return raw_response

```

By dumping structured traces to standard output, you allow your observability stack to index the exact `hydrated_prompt`. If the output is wrong, you don’t guess; you query your logs. 90% of the time, the bug is right there: the model was fed [the wrong context](https://thenewstack.io/context-rot-enterprise-ai-llms/).

### Differentiate “context bugs” from “reasoning bugs”

Once the AI pipeline starts hallucinating, developers rush to correct the prompt. This is a lazy approach. You need first to determine where the problem comes from:

**Context bug**: The vector database returns irrelevant chunks. The answer was wrong because the model was starved of proper context (Solutions: tune your embeddings and chunk sizes, hybrid BM25 retrieval)

**Reasoning bug**: The vector database returned the most relevant chunks, but the model either did not use them properly, misunderstood them, or suffered from format drift. (Solution: upgrade the model, lower the temperature, use few-shot examples)

Yelling at the LLM to obey system prompts (“YOU MUST ONLY USE THE CONTEXT!!!”) and trying to fix a reasoning bug this way will never work out.

### Modern data type schema validation with Pydantic

Your enterprise system will not do without validation. You won’t get away with the manual regexes and `json.loads()`. The probabilistic output needs to conform to a schema. For Python, Pydantic solves this issue elegantly.

```

Python
import time
import json
import logging
from typing import Callable, Dict, Any, List

# Configure structured logging for production ingestion
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def trace_llm_execution(
    step_name: str, 
    async_llm_callable: Callable, 
    prompt_template: str, 
    context: List[str], 
    user_query: str
) -> Dict[str, Any]:
    
    # 1. Hydrate the prompt exactly as the model will see it
    hydrated_prompt = prompt_template.format(
        context="\n".join(context), 
        query=user_query
    )
    
    start_time = time.perf_counter()
    error = None
    raw_response = None
    
    try:
        # 2. Await the probabilistic call to keep the thread unblocked
        raw_response = await async_llm_callable(hydrated_prompt)
    except Exception as e:
        error = str(e)
        
    latency_ms = round((time.perf_counter() - start_time) * 1000, 2)
    
    # 3. Create an immutable artifact of the exact state
    trace_artifact = {
        "event": "llm_trace",
        "step": step_name,
        "latency_ms": latency_ms,
        "hydrated_prompt": hydrated_prompt, # Crucial: What did the model actually see?
        "raw_context_chunks": context,      # Crucial: Did the DB return garbage?
        "raw_response": raw_response,
        "error": error
    }
    
  # 4. Emit to stdout; use default=str to handle non-serializable objects (like Exceptions)
logger.info(json.dumps(trace_artifact, default=str)) 
        
    if error:
        raise RuntimeError(f"Step {step_name} failed: {error}")
        
    return raw_response

```

### Automated evals via “LLM-as-a-Judge”

Since GenAI does not support string equality assertion tests for outputs, unit testing needs to shift its approach.

Where previously you crafted brittle assertions, now you rely on a lightweight and cheap model (GPT-4o-mini, Gemini 1.5 Flash, or Claude 3 Haiku), which will then judge your primary model’s output against a rigorous criterion.

One example of an evaluation prompt is passing the answer and the source to the judge model prompt, which says, “Rate this answer on a scale of 1-5 solely based on whether it mentions the following context.” You can thus continually monitor hallucination rates in your [CI/CD process](https://thenewstack.io/introduction-to-ci-cd/).

## Engineering is the art of reigning in chaos

While the early generation of AI tools was almost magical because we experimented with them on paper, enterprise software does not operate on the principles of magic; it works on the principles of observability, predictability, and clear boundaries.

> “While the early generation of AI tools was almost magical, enterprise software does not operate on the principles of magic; it works on the principles of observability, predictability, and clear boundaries.”

The current challenge in debugging code is not that the code has become more complex or harder to understand. The problem is the environment in which the code runs, which becomes unpredictable. By turning our attention away from breakpoints towards creating asynchronous traces, strictly validating schemas with Pydantic, and automatically running evaluators, we can demystify AI and return it to software engineering.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.