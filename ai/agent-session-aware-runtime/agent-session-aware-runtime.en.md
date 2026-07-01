**Over the past few months**, four AI giants quietly rebuilt the same thing at once: AWS, Microsoft, Google, and Anthropic each shipped agent runtime updates that point to the same architectural shift.

Microsoft rebuilt its Foundry-hosted agents in April around per-session isolation. Anthropic’s [Managed Agents](https://www.anthropic.com/engineering/managed-agents) virtualize the agent into a session, a harness, and a sandbox. AWS routes each session to its own microVM, and Google isolates agent code execution in a dedicated sandbox. The common pattern is not another model feature or developer tool. It is a move from request-level load balancing to session-aware execution.

This matters because enterprise agents are not ordinary API calls. They are long-running, stateful, tool-using processes that often run code influenced by user input. At its core, the agent runtime is becoming a control plane for state, identity, isolation, and lifecycle, and the unit it schedules has moved from the individual request to the agent session. The convergence across four platforms suggests session-aware execution is becoming a baseline requirement for production-grade agents.

## The traditional cloud scaling model

To appreciate why this matters, it helps to start with what the traditional model got right. [NGINX](https://www.nginx.com/) and HAProxy tiers typically sit in front of a pool of workers and route each incoming request to the next available backend. The state is deliberately kept elsewhere, in Redis or a database, so any worker can serve any request. That externalization of state is what enables elastic scaling, fault tolerance, and infrastructure replacement without disrupting the application. Sticky sessions were available, but enterprises treated them as an exception for stateful applications rather than the default.

![](https://cdn.thenewstack.io/media/2026/06/a6e2d290-model-a-load-balancer-1024x753.png)

The model rests on two assumptions: that requests do not depend on one another and that any backend can serve any request. For web APIs and microservices, those assumptions held for nearly two decades and enabled the scaling of the largest systems ever built. Agents challenge both at once, which is why conventional load balancing alone is no longer sufficient.

## Why agents break the model

Agents pose two distinct challenges: preserving conversational state across turns and enforcing a security boundary strong enough to withstand untrusted code. Only the first can be addressed by routing alone.

## Why can the agent state not be pooled?

Imagine an enterprise support agent processing a refund. It reads the order, calls a tool, and then waits for the model. The next turn asks a clarifying question. If that turn is routed to a different replica without access to the prior context, the agent loses the state it needs to finish the workflow.

> The load balancer starts to behave less like a traffic distributor and more like a session router.

The industry already has a name for the workaround, session affinity, and it already concedes the cost. Load-balancing approaches increasingly rely on consistent hashing, using a conversation identifier to keep related steps in a warm state. In plain English, the load balancer starts to behave less like a traffic distributor and more like a session router.

## Why the trust boundary forces isolation

The second challenge is harder because it turns on isolation rather than on the state alone. An agent can execute model-generated code shaped by user input, so the backend must be treated as a security boundary rather than a generic compute target. A shared kernel does not give untrusted, agent-generated code the tenant isolation that enterprise security teams require. Session affinity can preserve routing continuity, but it does not by itself provide per-tenant isolation for untrusted execution. For platform and security teams, that is the line where a tuned load balancer is no longer enough.

This is not a theoretical concern. When [Asana](https://www.upguard.com/blog/asana-discloses-data-exposure-bug-in-mcp-server) disclosed a flaw in its MCP server in June 2025, the server had been live since May 1, a window of about five weeks. A tenant-isolation check failed, and around 1,000 organizations could see project data belonging to other customers. Based on the reported details, security researchers traced the issue to a server that validated the user but did not consistently enforce the agent and tenant context behind cached responses. No external attacker was involved, and data still crossed organizational boundaries. The incident shows why user identity, agent context, and session state must be consistently bound together.

## The session as a unit of compute

Once that binding becomes a correctness and security requirement, the session becomes the unit that the platform schedules. The clearest evidence is in the lifecycle. A session now has a state it never had before. AWS [documents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html) that an AgentCore session remains Active while it processes work and sits Idle when it is provisioned but waiting. It reaches Terminated after a 15-minute idle timeout or an 8-hour maximum lifetime. That is the lifecycle of a long-running execution environment, not of a short-lived HTTP request.

![](https://cdn.thenewstack.io/media/2026/06/9a8ae380-model-b-control-plane-1024x518.png)

The economics follow the same logic. When billing is tied to active sessions, concurrency, idle time, and agent sizing become the cost drivers rather than request volume. That puts a new line item in front of platform teams and finance. The better mental model is no longer a traditional load balancer. It is closer to a virtual actor runtime, where an addressable identity is instantiated on demand, kept active while it is needed, and deactivated when idle, with one live instance per key.

## Four approaches to the same shift

All four platforms are moving away from treating stateful, untrusted agent work as ordinary load-balanced traffic. The key difference is the compute primitive each provider chooses for the isolated execution environment.

AWS AgentCore is the most opinionated of the four. Each session gets a dedicated [Firecracker](https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/) microVM with isolated compute, memory, and filesystem, and a request carrying the same `runtimeSessionId` is routed back to that microVM through a session header. When the session ends, the microVM is terminated and its memory sanitized.

The agents hosted on Microsoft Foundry implement a similar model through a different set of primitives. The platform creates a per-session VM-isolated sandbox on demand, runs it, and tears it down at session end, with no replica count and no warm pool to size. Each agent gets a dedicated Microsoft Entra identity, and sessions run a 15-minute idle timeout against a 30-day maximum lifetime.

Google [Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview) is the most instructive hybrid. Its runtime keeps request scaling within the reasoning loop, a managed environment with configurable minimum and maximum instance counts, and a `container_concurrency` that defaults to 9. Even where Google retains request scaling for the loop, it separates untrusted code execution into an isolated Code Execution sandbox and externalizes conversation state to Sessions and Memory Bank. The provider that kept the load balancer in the loop still would not point it at stateful untrusted work.

Anthropic provides the clearest decomposition of the architecture. Managed Agents virtualize the agent into three components: a session that logs everything that happens, a harness that runs the loop and routes tool calls, and a sandbox where code runs. The harness becomes a near-stateless control plane, while the sandbox becomes a callable, rebuildable resource. The [Cloudflare](https://blog.cloudflare.com/claude-managed-agents/) integration shows that the substrate can be decoupled. The agent loop runs on Anthropic while each tool call runs in a Cloudflare sandbox, which can be a full microVM or a lighter V8 isolate.

The four platforms converge on the routing and lifecycle model and diverge on the execution substrate, as the table shows.

| Platform | Compute primitive per session | What it means for an enterprise buyer |
| --- | --- | --- |
| AWS AgentCore | Dedicated Firecracker microVM, routed by session ID, 8-hour ceiling | The most opinionated answer, with isolation and routing fused at the microVM |
| Azure Foundry hosted agents | Per-session VM-isolated sandbox, dedicated Entra identity, 30-day max | Identity-led isolation suited to longer multi-day workloads |
| Google Agent Engine | Request-scaled loop plus a separate isolated code-execution sandbox | A hybrid that load-balances the reasoning and isolates the execution |
| Anthropic Managed Agents | Decoupled harness and sandbox, microVM or V8 isolate behind the loop | The most portable, with the substrate treated as a swappable layer |

No single architecture is the right answer for every enterprise workload. A multi-day research agent fits Azure’s longer-lived session, a code-heavy agent needs microVM-grade isolation, and high-volume automation favors a lighter isolate. Many enterprise platforms will end up combining more than one of these patterns.

## The binding the application still owns

The platform can isolate and route a session, but it does not know which human owns it. AgentCore explicitly states that it does not enforce session-to-user mappings, so the application backend must maintain the relationship between users and their session IDs and set per-user session limits. This is why the Asana incident is relevant to enterprise architecture.

> Isolation was maintained while the user-to-session binding broke.

In that case, isolation was maintained while the user-to-session binding broke. The platform solves isolation and lifecycle, and it hands back identity mapping, authorization, and tenant context to the application. For an enterprise buyer, the key question is who owns that binding and how it is tested under concurrent, multi-tenant load.

## How this differs from sticky sessions

A reasonable objection is that this appears to be sticky sessions combined with autoscaling on a microVM substrate. The distinction is worth drawing out. Traditional sticky sessions are usually performance optimizations, whereas in an agent runtime, session binding becomes a correctness and security requirement. Traditional load balancers route traffic to existing backends and do not own the lifecycle of the execution environment.

The new control plane provisions an environment when it first sees a session key, routes work to it, and tears it down after idle or lifetime limits. The primitive underneath is genuinely old, and its age is what makes the move legible. AWS open-sourced Firecracker at re:Invent in 2018 to pair VM-grade isolation with container speed. I [covered](https://thenewstack.io/how-firecracker-is-going-to-set-modern-infrastructure-on-fire/) it for *The New Stack* then, and ran more than a hundred microVMs on a single laptop to see that trade firsthand. The same microVM now powers Lambda and Fargate across trillions of executions a month. This is how cloud architecture tends to evolve, with existing primitives recombined around a new unit of abstraction.

> The agent session is becoming the operational unit of enterprise AI infrastructure.

In summary, the important shift is not that cloud providers have found a better load balancer for agents. It is that the agent session is becoming the operational unit of enterprise AI infrastructure. Traditional load balancing routed independent requests to interchangeable workers. A session-aware runtime routes work to an isolated environment, preserves state across turns, and owns the lifecycle of the execution context. The dispatch layer did not disappear when agents arrived. It became session-aware, stateful, and lifecycle-aware, making it a control plane rather than a conventional load balancer.

Three practical questions will shape what comes next, and enterprises will need to evaluate each. The economics of per-session billing will decide how costs scale with concurrency. The open-source effort to rebuild this routing model on Kubernetes will determine its portability. The argument between microVMs and lighter isolates will decide the trade-off between isolation and density. For enterprises building agents, a runtime that owns isolation, routing, and lifecycle turns background plumbing into a deliberate architectural choice. It gives platform, security, and operations teams a foundation they can standardize on rather than rebuild for every workload.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)