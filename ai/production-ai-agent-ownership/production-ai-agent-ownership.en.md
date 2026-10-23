At 2:07 a.m., an AI agent starts failing.

The application is still running, but requests are timing out because a downstream API is returning errors. The agent has already retried twice, using more tokens than usual, and its response time has roughly doubled.

The first question should not be:

```

	“Which model should we use?”

```

It should be:

```

	“Who owns this system right now?”

```

That question is easy to overlook when [building AI agents](https://thenewstack.io/how-to-build-ai-agents-with-lifelong-learning/). Teams often pour effort into prompts, retrieval, tools, and model selection, but production ownership determines whether an agent becomes a dependable service or another source of operational risk.

> “Teams often pour effort into prompts, retrieval, tools, and model selection, but production ownership determines whether an agent becomes a dependable service or another source of operational risk.”

A production agent needs an owner, boundaries, telemetry, failure policies, escalation paths, and a clear distinction between what the system may automate and what requires human intervention.

![Diagram showing the workflow loop involved with an agent dealing with a user request.](https://cdn.thenewstack.io/media/2026/10/c3d0706d-image-1024x406.png)

A production agent should not have a direct path from reasoning to action. Each tool invocation should pass through explicit controls, remain observable, and have a defined [path to human intervention](https://thenewstack.io/ai-sre-agent-autonomy-phases/).

Here’s a practical way to build those controls.

---

## Step 1: Treat the agent as a production service

An agent should have the same operational identity as any other production service.

Start by defining its ownership metadata.

```

Python
from pydantic import BaseModel


class AgentService(BaseModel):
    name: str
    owner_team: str
    service_tier: str
    escalation_channel: str


agent_service = AgentService(
    name="incident-command-agent",
    owner_team="platform-engineering",
    service_tier="critical",
    escalation_channel="#platform-oncall",
)

```

This may look simple, but it changes the conversation.

The agent is no longer an experiment running somewhere in a Python process. It is a service with an accountable team and an escalation path.

> “The agent is no longer an experiment running somewhere in a Python process. It is a service with an accountable team and an escalation path.”

You can later attach the same metadata to logs, traces, dashboards, alerts, and deployment records.

---

## Step 2: Define what the agent is allowed to do

Ownership also means being clear about what an agent is allowed to do.

An agent that can only read telemetry carries far less risk than one that can restart production services, change infrastructure, or deploy code.

That’s why I prefer an explicit tool allowlist, which limits the agent to the actions you’ve deliberately granted it.

```

Python
ALLOWED_TOOLS = {
    "get_service_health",
    "get_recent_deployments",
    "search_runbooks",
    "summarize_incident",
}


class ToolAuthorizationError(Exception):
    """Raised when an agent attempts to use an unapproved tool."""


def authorize_tool(tool_name: str) -> None:
    if tool_name not in ALLOWED_TOOLS:
        raise ToolAuthorizationError(
            f"Tool '{tool_name}' is not authorized."
        )

```

The guiding principle is **deny by default**.

Adding a new capability should be an intentional engineering decision, not something that happens because a tool became available to the agent.

For destructive operations, authorisation should be even stricter. A production restart or deployment should require authenticated human approval, not the agent’s own judgment.

---

## Step 3: Put budgets around agent execution

An agent that can reason indefinitely is difficult to operate.

Every production workflow should have limits around execution time, model calls, tool calls, and ideally token consumption.

```

Python
import os


class ExecutionBudget:
    def __init__(
        self,
        max_steps: int | None = None,
        max_tools: int | None = None,
    ):
        self.steps = 0
        self.tool_calls = 0

        self.max_steps = (
            max_steps
            if max_steps is not None
            else int(os.getenv("MAX_AGENT_STEPS", "5"))
        )

        self.max_tools = (
            max_tools
            if max_tools is not None
            else int(os.getenv("MAX_TOOL_CALLS", "8"))
        )

        if self.max_steps <= 0 or self.max_tools <= 0:
            raise ValueError(
                "Execution budget limits must be positive."
            )

    def check_step(self) -> None:
        if self.steps >= self.max_steps:
            raise RuntimeError(
                "Agent step budget exceeded."
            )

        self.steps += 1

    def check_tool_call(self) -> None:
        if self.tool_calls >= self.max_tools:
            raise RuntimeError(
                "Agent tool-call budget exceeded."
            )

        self.tool_calls += 1

```

Execution limits should be configurable rather than buried in application code. By passing these limits through the constructor, engineers can assign different budgets to different agents without changing global settings. A diagnostic agent might need only three steps, while a more complex research workflow may require considerably more. When no limits are supplied, the class falls back to environment variables. What matters is that every workflow has a defined ceiling, and that the same budget is enforced throughout its execution.

---

## Step 4: Make model calls observable

An owner cannot operate what they cannot see.

At minimum, record:

* request latency;
* model used;
* success/failure;
* tool calls;
* token usage where available;
* correlation or request ID;
* escalation events.

A simple wrapper provides a useful boundary.

```

Python
import logging
import time
import uuid

logger = logging.getLogger(__name__)


def invoke_model(model, messages):
    request_id = str(uuid.uuid4())
    started = time.perf_counter()

    # Extract the model name across different provider libraries.
    model_name = (
        getattr(model, "model_name", None)
        or getattr(model, "model", None)
        or "unknown_model"
    )

    try:
        response = model.invoke(messages)

        elapsed = time.perf_counter() - started

        logger.info(
            "agent_model_call_success",
            extra={
                "request_id": request_id,
                "model": model_name,
                "latency_seconds": round(elapsed, 3),
            },
        )

        return response

    except Exception:
        elapsed = time.perf_counter() - started

        logger.exception(
            "agent_model_call_failed",
            extra={
                "request_id": request_id,
                "model": model_name,
                "latency_seconds": round(elapsed, 3),
            },
        )

        raise

```

The request ID becomes especially valuable when an incident involves several services.

An engineer should be able to move from an alert to the agent request and then to the underlying model and tool calls.

In production, supplement this logging layer with [distributed tracing and metrics](https://thenewstack.io/agent-traces-application-data/) for a more complete view of system behaviour and performance.

---

## Step 5: Separate failure from escalation

A failed model call does not necessarily mean the entire service should fail.

Likewise, a successful model call does not mean the agent’s recommendation should execute automatically.

These are different decisions.

```

Python
def handle_agent_failure(error: Exception) -> dict:
    logger.error(
        "Agent execution failed; escalating to human.",
        exc_info=(
            type(error),
            error,
            error.__traceback__,
        ),
    )

    return {
        "status": "escalated",
        "message": (
            "The AI agent could not complete the operation. "
            "Human intervention is required."
        ),
        "error_type": type(error).__name__,
    }

```

This distinction matters during a real incident.

The agent might go down, but the engineering team should still be able to respond using the underlying workflows and runbooks. That is what graceful degradation looks like in practice.

---

## Step 6: Make high-risk actions human-gated

One of the most useful patterns for enterprise agents is separating **recommendation** from **execution**.

For example:

```

Telemetry
    ↓
AI Agent
    ↓
Diagnosis
    ↓
Recommended Action
    ↓
Risk Check
    ↓
Human Approval
    ↓
Production Change

```

The agent might recommend:

```

	“Increase the database connection pool.”

```

But it shouldn’t push that change to production just because the model generated the recommendation.

Here’s what a simple approval boundary looks like:

```

Python
def execute_action(
    action: str,
    approved_by: str | None,
) -> dict:
    if not approved_by:
        return {
            "status": "awaiting_approval",
            "action": action,
        }

    return {
        "status": "approved",
        "action": action,
        "approved_by": approved_by,
    }

```

A real system needs a more sophisticated implementation, but the architectural boundary is what matters.

> “The agent can own reasoning without owning authorisation.”

The agent can own reasoning without owning authorisation.

---

## Step 7: Give the agent a health check

A production agent needs a health endpoint just like any other service.

With FastAPI:

```

`Python
import os

import httpx
from fastapi import FastAPI, Response, status

app = FastAPI()

SERVICE_NAME = "incident-command-agent"


@app.get("/health/live")
async def liveness():
    """Check whether the application process is responsive."""
    return {
        "status": "alive",
        "service": SERVICE_NAME,
    }


async def check_provider() -> bool:
    """Check a configured provider health endpoint."""
    health_url = os.getenv("MODEL_PROVIDER_HEALTH_URL")

    if not health_url:
        return False

    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            result = await client.get(health_url)
            return result.status_code == 200
    except httpx.RequestError:
        return False


@app.get("/health/ready")
async def readiness(response: Response):
    """Check whether required dependencies are available."""
    if not await check_provider():
        response.status_code = (
            status.HTTP_503_SERVICE_UNAVAILABLE
        )
        return {
            "status": "unhealthy",
            "reason": "Model provider unavailable",
        }

    return {
        "status": "ready",
        "service": SERVICE_NAME,
    }

```

Liveness and readiness serve different purposes. The liveness endpoint confirms that the application process is responsive, while readiness checks whether the service can handle requests based on the availability of its required dependencies.

In this example, the readiness endpoint checks a configured model-provider health URL and returns HTTP 503 when the check fails. The check is deliberately lightweight and time-limited to avoid introducing unnecessary delays or costs. In production, teams should adapt it to their provider’s supported health-check mechanism and other critical dependencies, such as a vector database or configuration service.

Keeping these checks separate lets orchestration platforms such as Kubernetes distinguish between an application that needs restarting and one that can’t serve traffic temporarily.

---

## Step 8: Fail closed when safety controls break

One of the worst failure modes is letting an agent keep running after its safety mechanisms go down.

For example:

```

Python
def run_controlled_agent(
    tool_name: str,
    model,
    messages,
    budget: ExecutionBudget,
):
    try:
        authorize_tool(tool_name)

        # Reuse the budget across agent steps and tool calls.
        budget.check_step()
        budget.check_tool_call()

        return invoke_model(
            model,
            messages,
        )

    except ToolAuthorizationError:
        logger.exception(
            "Agent authorisation check failed."
        )

        return {
            "status": "blocked",
            "message": (
                "The requested operation is not authorised."
            ),
        }

    except RuntimeError:
        logger.exception(
            "Agent execution budget exceeded."
        )

        return {
            "status": "escalated",
            "message": (
                "The agent exceeded its execution budget. "
                "Human investigation is required."
            ),
        }

    except Exception as exc:
        return handle_agent_failure(exc)

```

Notice that different failures produce different outcomes. An authorisation failure should block the requested operation, while an exhausted execution budget should trigger escalation rather than another retry. A temporary model failure, meanwhile, should follow the system’s defined failure-handling policy.

Another important detail: the execution budget must persist throughout the agent’s workflow. Creating a new budget for every invocation would reset its counters, allowing repeated calls to bypass the intended limits. Instead, create the budget once and pass it into each successive invocation, as shown below.

```

Python
# Create one budget for the entire agent workflow.
budget = ExecutionBudget(
    max_steps=5,
    max_tools=8,
)

# Reuse the same budget across successive invocations.
for tool_name in planned_tools:
    result = run_controlled_agent(
        tool_name=tool_name,
        model=model,
        messages=messages,
        budget=budget,
    )

    if isinstance(result, dict) and result.get(
        "status"
    ) in {"blocked", "escalated"}:
        break

```

With the same budget shared across invocations, each counted step and tool call contributes to the workflow’s overall limit. Once that limit is reached, the agent stops rather than continuing with a fresh budget. These controls only work if they remain effective throughout execution, especially when an agent encounters repeated failures.

---

## Step 9: Define the 2 a.m. runbook

This is where operational ownership becomes real.

Suppose the agent starts failing at 2 a.m.

The on-call engineer should be able to answer five questions quickly:

1. **Is the agent itself healthy?**
2. **Is the model provider healthy?**
3. **Are retrieval or tool dependencies failing?**
4. **Has the agent exceeded its normal cost or latency envelope?**
5. **What happens if we disable it?**

The last question matters most.

Every production AI system should have a clear degradation path.

For an incident-response agent, that might mean:

```

AI Agent unavailable
        ↓
Incident still created
        ↓
Telemetry remains available
        ↓
Standard runbook activated
        ↓
Human engineer continues investigation

```

The AI system should speed up operations, not become something the organisation can’t operate without.

---

## So, who owns the agent?

The answer should never simply be:

Production ownership needs to be explicit.

Someone owns:

* deployment;
* infrastructure;
* model configuration;
* tool permissions;
* monitoring;
* incident response;
* cost;
* security;
* rollback;
* the decision to disable the agent.

That doesn’t mean one person has to handle everything. It means everyone knows their role well enough that, when an incident hits, the team isn’t wasting time figuring out who should take charge.

---

## The real test of an AI agent

The easiest time to operate an AI agent is during business hours when everything is working.

The real test comes at 2 a.m.

A production-ready agent should have an owner who can be paged, an execution budget that prevents runaway behaviour, observability that explains what happened, authorisation boundaries that constrain what it can do, and a fallback that allows engineers to continue without it.

The goal isn’t to take humans out of the loop.

> “A production-ready agent should have an owner who can be paged, an execution budget, observability that explains what happened, authorisation boundaries, and a fallback that allows engineers to continue without it.”

It’s to make it clear where the agent’s responsibility ends and where a human needs to step in.

Because when something goes wrong at 2 a.m., the question isn’t whether the model was smart enough.

It’s whether the system was designed well enough that the person on call knows what happened, what the agent did, and what to do next.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/03/6dadf7f1-oladimeji-sowole.jpeg)

Oladimeji Sowole is a member of the Andela Talent Network, a private marketplace for global tech talent.  A Data Scientist and Data Analyst with more than 6 years of professional experience building data visualizations with different tools and predictive models...

Read more from Oladimeji Sowole](https://thenewstack.io/author/oladimeji-sowole/)