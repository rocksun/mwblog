Nowadays, most of us interact with frontier AI models in a structured way, even if we do not always think about it that way. Most systems already sit on top of a protocol, often created by the model providers themselves. [OpenAI and Anthropic](https://thenewstack.io/ai-agent-harness-pricing-split/), for example, each provide APIs to communicate with their inference systems.

In practice, one approach is to use an OpenAI-compatible API that can serve a multi-turn agent. We can point the official OpenAI SDK at a compatible inference endpoint, hold a conversation with the agent, and use the same interface across turns.

These systems are built in a specific, clever way that lets them scale. When traffic grows or subagents spawn, these systems need to be scaled so that we, as engineers, can make necessary adjustments without users noticing. For example, we may scale a single-replica system to three replicas behind a load balancer when we need additional traffic support, while still retaining the proper conversation context and previous turns.

> “The microservices principles everyone stopped talking about five years ago turn out to be exactly what agent traffic needs.”

We will look at what happens under bursts of AI traffic.

Many of the questions we need to ask ourselves before developing these systems were already addressed by the 2010s-era microservices literature. We will show how to rebuild an agent-friendly API from those principles, backing it with [Oracle AI Database Free](https://www.oracle.com/database/free/?source=:ex:pw:::::TNS_SAFA_A&SC=:ex:pw:::::TNS_SAFA_A&pcode=), and measure what changes.

## Why agent traffic is different from web traffic

**Key insight:** The load shape is different, and that difference is exactly what a stateful design struggles to absorb.

Four properties separate an agent client from a browser:

1. **Conversations are long and stateful, but requests are not.** A 40-turn agent loop results in 40 independent HTTP requests. Nothing in the protocol ties them to one server. Each tool call is stateless at the HTTP layer: the endpoint receives individual requests and responses over time, so the application needs to determine which conversation a request belongs to and where its state lives.
2. **Tool calls fan out unpredictably.** One chat request may trigger zero downstream calls, or six, one of which hits a vector index and takes 400 milliseconds. Because model outputs and tool-section paths can vary, even the same input may trigger a different sequence and number of tool calls.
3. **Agents retry aggressively.** AI agents are usually wrapped in an agent harness with its own control loop, error handling, and retry policy. When a timeout or error occurs, the system may receive a rapid sequence of retries from the same workload. This is useful for resilience, but it can also amplify pressure on a dependency that is already struggling.
4. **Load is bursty and machine-paced.** There is little or no think time between turns. While an AI agent is operating, it can generate a continuous burst of work, constrained mainly by the hardware and concurrency limits around it.

Point 1 is the one that people usually understand: a browser session survives on one server thanks to stickiness and human think time. An agent can issue many requests in rapid succession, and without durable shared state, requests distributed across replicas can lose the context they need, creating friction for the user.

## The first version everyone builds

Here is the whole failure, in one endpoint:

```

SESSIONS: dict[str, list] = {}
SLOTS = asyncio.Semaphore(int(os.environ.get("CONCURRENCY", "32")))  # one pool

@app.post("/v1/chat/completions")
async def chat(req: Request):
    body = await req.json()
    sid = req.headers.get("x-session-id") or body.get("user")
    async with SLOTS:                                 # everything shares it
        history = SESSIONS.setdefault(sid, [])
        history.append({"role": "user", "content": body["messages"][-1]["content"]})
        if body.get("tools"):
            await TOOLS[body["tools"][0]["function"]["name"]]()   # inline, in-path
        ...

```

This is a correct, working, minimal OpenAI-compatible API. The decorator establishes that the following function runs asynchronously when the endpoint is invoked.

This minimal endpoint passes all tests but has a fundamental flaw. Can you spot it?

In our POC benchmark, we drove 200 conversations of four turns each, sending every turn to the next available replica in rotation—the kind of distribution you can see when the stickiness parameter is not configured appropriately:

| Deployment | Turns | Context lost | Loss rate |
| --- | --- | --- | --- |
| Monolithic, **1 machine** | 800 | 0 | **0.0%** |
| Monolithic, **3 machines** | 800 | 600 | **75.0%** |
| Decomposed, 1 machine | 800 | 0 | 0.0% |
| Decomposed, 3 machines | 800 | 0 | **0.0%** |

Take a look at the monolithic deployment with one machine versus three. The design is not broken; it is conditionally correct.  The condition is that every turn reaches the same machine, which is exactly the condition you give up when you scale.

> “The failure is silent. The model still answers, but it may answer without the right context because the request landed on another machine that does not have the previous chat history.”

The failure is silent. The model still answers, but it may answer without the right context because the request landed on another machine that does not have the previous chat history. Observability may still show HTTP 200 responses, yet the system is not behaving correctly from the user’s perspective. That is the difference we need to account for [when designing APIs](https://thenewstack.io/why-databases-need-apis/) for AI applications.

## Returning to the principles

**Key insight:** Nothing in the fix is new. It is Lewis and Fowler’s [microservices characteristics](https://martinfowler.com/articles/microservices.html) (2014) and Michael Nygard’s bulkhead pattern from *Release It!*, applied to a request shape that did not exist when they were written.

There are three principles that do the heavy lifting:

**Statelessness:** Conversation state moves out of the process and into a shared store. Any replica can serve any turn of any conversation. This single change lets the previous endpoint scale across replicas without relying on process-local conversation state: we don’t need to send the full chat history back and forth on every request if the agent can retrieve what it needs from a centralized place.

**Bulkheads (a.k.a. isolation):** The idea is to isolate different parts of the [system to prevent cascading failures](https://thenewstack.io/acm-vibe-coding-ai-agent/). In this case, we isolate by *dependency*, not globally.

**Smart endpoints, dumb pipes:** The OpenAI chat-completions protocol is an unusually useful transport layer: relatively small, stable, already supported by many agent frameworks, and familiar to AI developers. We put the intelligence—routing, budgeting, memory engineering, context engineering, tool-calling policies—on top of it, rather than inside it. Keep the pipe simple.

## The POC: four services, one protocol

![Image showing the architecture of monoliths and gateways + services](https://cdn.thenewstack.io/media/2026/10/e309ac0a-image.png)

*Architecture*

The decomposed stack splits along failure-domain lines, not along nouns:

* **gateway** — speaks the OpenAI protocol, holds nothing, and scales horizontally
* **memory** — owns conversation state and the tool audit trail; nothing else may hold a message list
* **tools** — executes tools in its own process, with its own concurrency budget and timeout
* **Oracle AI Database Free** — the shared substrate under all of it

As the architecture shows, the point is to isolate as much as possible while keeping each component focused on one job. That can make the components easier to evolve independently. It also gives us room to set separate concurrency budgets, timeouts, and other configuration parameters for each dependency.

You can implement this with semaphores: they let us control access to shared resources, which is exactly what we need.

```

CHAT_SLOTS = asyncio.Semaphore(int(os.environ.get("CHAT_CONCURRENCY", "24")))
TOOL_SLOTS = asyncio.Semaphore(int(os.environ.get("GW_TOOL_CONCURRENCY", "8")))

```

And because the protocol is unchanged, the official SDK can communicate with this OpenAI-compatible endpoint without changes to the SDK itself:

```

from openai import OpenAI
c = OpenAI(base_url="http://127.0.0.1:8110/v1", api_key="")

c.models.list()          # ['agent-gateway/router-v1']
r1 = c.chat.completions.create(model="agent-gateway/router-v1",
        messages=[{"role": "user", "content": "hello"}], user="demo-1")
r2 = c.chat.completions.create(model="agent-gateway/router-v1",
        messages=[{"role": "user", "content": "and again"}], user="demo-1")
# r1 -> "turn 1"   r2 -> "turn 3"   (state survived, on a different replica)

```

As the gateway writes to the memory component independently—and with concurrency controlled by the semaphores—the design avoids relying on local file system state across replicas.

## Are bulkheads worth it?

A bulkhead isolates different components of our application to prevent failures from propagating across them. For example, we can separate the tool-calling path from the standard chat-completion path.

Imagine we have a system that correctly partitions components and separates tool-calling requests from standard chat completions, as shown here:

![Image comparing bulkhead request times](https://cdn.thenewstack.io/media/2026/10/b9d9bc85-image.png)

*Bulkhead comparison from our POC*

Both stacks get 32 admission slots per replica. The monolithic approach spends them from one request pool. The gateway splits them: 24 for plain chat, eight for tool-bearing requests. The benchmark drives 120 chat requests per second while 300 concurrent callers hammer a 400-millisecond tool.

> “Without bulkheads, a user making a standard chat request can end up waiting behind slow tool calls because every request is competing for the same pool.”

Without bulkheads, a user making a standard chat request can end up waiting behind slow tool calls because every request is competing for the same pool. With isolation, tool pressure remains can be isolated from the standard chat pool, helping preserve capacity for standard chat traffic.

## Where Oracle AI Database Free fits in

**Key insight:** “Database per service” is the one microservices principle you may not want to apply uniformly in an AI application.

The advice that was prevalent in 2014 was to give every service its own datastore, because the coupling cost of a shared schema exceeded the coordination cost of eventual consistency.

For agents, that calculus can invert, because a single agent turn writes four things that must agree:

* the conversation state
* the tool invocation record (and order)
* the semantic, episodic and workflow memory facts extracted from the turn
* the idempotency ledger entry that stops a retry re-executing a paid tool

If you decide to split these across data stores—one in Postgres, one in a vector store, and another in Redis—you get a consistency problem that the application now has to manage. Databases have been solving transactional consistency for decades, so this architecture can use database transaction capabilities to manage these related writes together.

Keeping them in one database makes it one transaction commit:

```

CREATE TABLE agent_sessions (
  session_id   VARCHAR2(64) PRIMARY KEY,
  messages     JSON NOT NULL,                 -- native JSON, not a CLOB you parse
  version      NUMBER DEFAULT 1 NOT NULL,     -- optimistic concurrency
  updated_at   TIMESTAMP WITH TIME ZONE DEFAULT SYSTIMESTAMP NOT NULL
);

CREATE TABLE agent_memory (
  memory_id    VARCHAR2(64) PRIMARY KEY,
  session_id   VARCHAR2(64),
  content      CLOB NOT NULL,
  embedding    VECTOR(1024, FLOAT32)          -- same row, same transaction
);

CREATE VECTOR INDEX ix_memory_vec ON agent_memory (embedding)
  ORGANIZATION NEIGHBOR PARTITIONS DISTANCE COSINE WITH TARGET ACCURACY 95;

```

Relational, JSON and vector data in one engine, one transaction, one backup, one set of credentials. [Oracle AI Database Hybrid Vector Search](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/understand-hybrid-vector-indexes.html?source=:ex:pw:::::TNS_SAFA_B&SC=:ex:pw:::::TNS_SAFA_B&pcode=) lets a retrieval query retrieve what it needs, join the tool history and rank by cosine distance in a single statement—instead of joining in Python across three systems, which may otherwise require application-level coordination across multiple systems.

Another thing the database does for horizontally scaled APIs is help coordinate concurrent turns. Two replicas serving turns of the same conversation is normal, not exceptional. SELECT … FOR UPDATE plus a version column can serialize conflicting updates and implement retry handling, rather than letting competing updates overwrite conversation state.

## The counterintuitive part: decompose compute, converge data

Everyone reaches for microservices to scale AI applications, but applying the principle uniformly can create consistency challenges across the agent’s memory, audit log, and vector index.

> “The useful split is asymmetric: decompose the compute, converge the data.”

The useful split is asymmetric: decompose the compute, converge the data.

The 2014 principles still hold. We just need to adapt them to the new era of AI agents.

*Ready to try the architecture? Download* [*Oracle AI Database Free*](https://www.oracle.com/database/free/?source=:ex:pw:::::TNS_SAFA_A&SC=:ex:pw:::::TNS_SAFA_A&pcode=)*, install the* [*Oracle AI Agent Memory Python package*](https://pypi.org/project/oracleagentmemory/)*, and follow the local quickstart to add persistent state and durable memory to your agent API. For more examples, visit the* [*Oracle AI Developer Hub*](https://github.com/oracle-devrel/oracle-ai-developer-hub)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/46f3e9e2-nacho-profile-pic.jpeg)

Nacho Martínez — Data Scientist Advocate at Oracle, Developer Relations. I build open-source tools and demos that bring developers closer to the Oracle stack and Oracle AI Database. Find me on GitHub at @jasperan.

Read more from Nacho Martínez](https://thenewstack.io/author/nacho-martinez/)