**The fast pace of AI research** means organizations now have a wide range of models to choose from that can power AI agents to solve real business problems. But choosing a model doesn’t guarantee you effective agents or even good performance. For that, you need to run your agents in an environment that provides them with tools, state, security, and scale, with fast startup times and good integration with your existing business systems.

Picking the right agent runtime environment is like picking an enterprise app server but for AI systems — and [agents have very different needs](https://thenewstack.io/securing-kubernetes-ai-agents/) from traditional applications.

> Gartner predicts more than 40% of agentic projects will be canceled by 2027; not because models aren’t powerful enough to be useful but because of unclear business value, inadequate risk controls and ballooning costs.

Gartner predicts more than 40% of agentic projects will be canceled by 2027; not because models aren’t powerful enough to be useful but because of unclear business value, inadequate risk controls and ballooning costs.  Agents that deliver in proof-of-concept systems will fail in production if the runtime stack powering them can’t keep up and keep them under control.

## Agentic compute is different

It’s easy to think of an AI agent as just another microservice that takes unstructured input, runs APIs or queries, and returns messages. But infrastructure designed for traditional enterprise applications with predictable business logic or even cloud-native stateless workloads doesn’t fit agents with their bursty, long-running, stateful, non-deterministic, code-writing, tool-invoking behaviors that might be triggered by a system event or an email — not just a chat session.

Model inference needs GPUs for speed, but agents also need reliable, durable compute that supports stateful sessions for long-running processes, along with strong security and real-time visibility.

You still need to think about familiar issues like hosting, scaling, identity, and security, but all that is complicated by the unpredictable, multi-stage workflow of the agent reasoning loop.

An agent pulls in input from multiple sources, reasons over its context about the execution plan for accomplishing the goal, calls other tools or writes its own code, iterates over the results of those calls, and maybe builds on them or switches to another approach that requires another reasoning loop and eventually delivers output. That might be updating a system or sending an email rather than just displaying an answer.

Model performance is only one part of making that useful. Architecting a successful agent system that can run at enterprise scale requires considering the agent runtime, the application layer that agents call, and the tools, APIs, and MCP servers they consume.

---

### More on Microsoft Azure

---

You have to be able to integrate with business logic and existing systems, manage the usual quotas, rate limits and SLAs for APIs so agents don’t overload them — and you have to do all that while keeping up with AI developments that are moving too fast for you to build the infrastructure primitives you need to rely on from scratch every time.

## Requirements of modern agentic infrastructure

Instead, you should look for flexible infrastructure that fits the way the agent works. As with any technology, if you build on an existing platform like Azure Container Apps, you can save effort in areas where your business can differentiate. And while AI agents have flaws (from hallucinations to high token costs) that aren’t fully solved, you can pick an agent runtime environment that makes it easier to get useful results despite them.

Agentic compute needs fast startup and resume. Whether it’s a human typing into a chat prompt or system events automatically launching multiple agents, agent infrastructure needs to spin up quickly. If it takes a few seconds to spin up a container, the reasoning loop can’t start till that’s done.

It also needs to scale up and down responsively, without costing you anything when it’s not running.

Because agent workloads are long-running and event-driven, agents need to start up, do some work, go idle for hours or even days, and then resume instantly with their memory, context, caches, connections, identity, and security intact. That means persisting and restoring state so long-running agents don’t have to pay the same startup tax over and over again. Whether the last stage of the agent’s reasoning loop was successful or a failure, it has to take another approach; you don’t want it to do the same work again.

Rather than building your own custom microVM stack, the new [**Azure Container Apps Sandboxes**](https://learn.microsoft.com/en-us/azure/container-apps/sandboxes-overview) provide a temporary, secure, and stateful compute environment that spins up, executes code, snapshots disk and memory, then automatically idles and resumes just as fast. This is the stateful equivalent of [**Dynamic Sessions**](https://learn.microsoft.com/en-us/azure/container-apps/sessions), with sub-second startup from pre-warmed pools; you can burst out to hundreds (and eventually thousands) of concurrent sandboxes when you need them, then scale back down to zero.

An agent runtime needs to be secure by default because agents are only useful when they take action — and by definition, they’re likely to do unexpected things, write and execute their own untrusted code, and keep trying to achieve their goal (sometimes even when there’s a policy that should stop certain behaviors).

To give agents secure, auditable access to the resources they need, run them and the code they generate in a sandbox, rather than on a developer laptop with production credentials and admin rights. Identity, access control, and execution boundaries have to be enforced at the runtime layer, not bolted on in a hidden prompt.

ACA Sandboxes have egress and access policies, so you can control outbound calls and limit what URLs they can access. If you can’t use managed identity for all the services an agent needs to connect to you, you can protect secrets by injecting API keys through an external egress gateway instead of hard-coding them. Because the gateway is external, outbound call decisions are controlled by policy outside the sandbox, not by agent code that will relentlessly try any method to get through.

If agents are useful, you’re going to run a lot of them, often simultaneously. AI agents need strong isolation for each task, so every untrusted code execution happens in its own sandbox and no data leaks between tasks.

You can manage them as groups, but each ACA Sandbox has its own secure boundary, so details from one customer support agent won’t end up in a chat with a different customer. If the untrusted code [does turn out to be problematic](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants), isolated sandboxes at least contain the blast radius.

You don’t want to rely on fragile glue code or ad hoc orchestration that you have to rewrite any time systems change for the calls agents make to tools, APIs, cloud services, and other workflows. You also don’t want to rely on manual cleanup of resources no longer needed. A runtime with built-in agent tool execution makes agents more robust. It takes the drudgery out of connecting the agent environment to your other systems, enabling them to interact securely, in isolation, and at scale.

> “It’s not just about where the agent is running and what the capabilities of the agent are, but also what actions the agent can take.”

“It’s not just about where the agent is running and what the capabilities of the agent are, but also what actions the agent can take,” points out [**Vyom Nagrani**](https://www.linkedin.com/in/vyomnagrani/), who runs the team of PMs responsible for both Azure Container Apps and the [**Azure SRE Agent**](https://learn.microsoft.com/en-us/azure/sre-agent/overview) that’s built on ACA Sandboxes. Sandboxes have access to a connector framework with over 1,400 enterprise-grade connectors, enabling them to take actions not only on Azure and Microsoft services but also on third-party tools.

“The runtime provides those connectors, and it provides a managed way of authenticating against all of these third-party systems, so now you can build an agent which can talk to many, many, *many* different systems. It’s not boxed into one authentication boundary,” Nagrani tells *The New Stack*.

MCP servers are a built-in capability of the connector framework. “You can take any of these connectors; you can take any REST API and expose it as an MCP server, which then the agent can consume.” Or if you want to build a custom MCP server, you can host that in a sandbox too. ACA Sandboxes can be both where agents run and, if that’s appropriate, where the tools they use are hosted.

If you’re building a user interface to wrap your agents, the application layer that makes calls to the agents can run in [**Azure Container Apps Express**](https://learn.microsoft.com/en-us/azure/container-apps/express-overview), a new service now in public preview, Nagrani says.

“It’s a simplified app hosting stack for the app layer that responds to HTTP traffic and serves web traffic: that’s where the human interactivity comes in.”

## Putting it all together

ACA Sandboxes offers an agent runtime environment that answers the key questions architects need to consider: where agents and the ephemeral compute they need access to run; where the application layer that calls agents runs; and how agents get access to all the tools, APIs, services, MCP servers, and existing business logic they need to orchestrate.

Whether you’re a platform engineer, a software vendor or a startup building a new AI platform, treating agent runtimes as the new application server and MCP servers as the new APIs requires agent infrastructure that supports agent workloads effectively, allowing governance to shift left into the runtime layer where it can scale with the ever-increasing numbers of agents.

## How real platforms build on agent runtimes

Azure Container Apps is already a strong platform for running agents. Auger, a startup launched by the former CEO of Amazon’s global consumer business to help mid-size enterprises get their complex supply chains out of Excel spreadsheets, used it to build a multi-agent system that can give real-time answers about shipments and forecasts in a world where mines or critical shipping lanes might be closed at any time by war or weather.

Backend agents pull the unstructured data with all the details to answer those questions from different siloes, building ETL pipelines and creating an ontology of the supply chain ecosystem for each customer that includes functions and actions — all of which need to be audited and reversible. Frontend agents use that ontology to answer questions such as, “What happens if I build a new warehouse here or switch to a supplier in this country?”

ACA Sandboxes take the power of Azure Container Apps, which is built on, and make it easier for any organization to build their own agent service with strong isolation, dynamic scaling, fast startup, durable state, and connectors to a wide range of tools and services.

That’s just what the Foundry team was looking for when they started work on the [**Microsoft Foundry Agent Service**](https://azure.microsoft.com/en-us/products/ai-foundry/agent-service) managed agent runtime. ACA Sandboxes gave them a platform that delivers fast start/resume, built‑in tool execution (including for untrusted code), persistent state for long‑running agents, strong per‑agent isolation, and secure‑by‑default operations. Agent identity, “on‑behalf‑of” authentication to existing business services, and strict isolation are critical capabilities they didn’t have to build themselves.

> “It’s the same enterprise-grade infrastructure behind Microsoft’s own agentic products, now available for all Azure customers to build on.”

The Foundry Agent Service adds a layer of visibility and observability into agent actions and conversations, allowing customers to monitor agent performance and see where the system is doing well and where it needs improvement.

“Azure Container Apps Sandboxes package the hard parts of an agent runtime into a first-class Azure resource — sub-second start and resume, built-in execution of tools and untrusted code, and snapshot-based state that lets long-running agents pick up exactly where they left off. Every agent gets its own hardware-isolated environment with secure-by-default operations, so builders can focus on what their agents do, not on the plumbing underneath,” Nagrani points out.

“It’s the same enterprise-grade infrastructure behind Microsoft’s own agentic products, now available for all Azure customers to build on.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/e2700739-maryb.jpg)

After completing an MSc in Intelligent Knowledge Based Systems in 1990, Mary Branscombe was convinced that promising as the AI techniques she’d been studying were, they weren’t even close to being ready. Since then, she’s been a technology journalist for...

Read more from Mary Branscombe](https://thenewstack.io/author/marybranscombe/)