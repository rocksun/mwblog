Engineering organizations are trying to deliver as fast as technology allows, bringing agentic AI into their developer platforms and working out how to use AI agents to maximize engineering productivity.

But when it comes to AI agents in an agentic developer platform, every team we talk with sees the role of those agents a little differently. Following hundreds of calls with our customers, we captured three types of roles.

## Role 1: AI agents as platform consumers

In this role, an agent is basically a user of the platform. It uses the platform as part of its task to read context and to run actions. When agents first showed up, a lot of companies said they treat their AI agents like employees, and in [a development platform](https://thenewstack.io/thomas-dohmke-interview-entire/) that makes the agent just another engineering resource consuming it.

![Diagram showing an AI agent reading context and running actions from an agentic SDLC platform.](https://cdn.thenewstack.io/media/2026/08/fcf5410b-image3-1024x458.png)

A typical case: an engineer asks Claude Code to add an endpoint to the payments service. Before it writes any code, the agent pulls the service owner, dependencies, and the standards it must meet from the platform, then spins up a preview environment via a self-service action and runs the tests.

> “A lot of companies said they treat their AI agents like employees, and in a development platform that makes the agent just another engineering resource consuming it.”

For this to work, the agent has to reason over real, current information about your systems, starting with the service catalog and extending to ownership, dependencies, standards, and current state. If you get the context wrong, there’s a good chance an [agent will get overconfident and do the wrong thing](https://thenewstack.io/hyland-enterprise-context-engine-agents/). Most teams solve this one agent at a time by providing local context. But then the same information ends up connected to agents in fragile ways, not to mention that none of them are governed. Compare that to a [context lake](https://docs.google.com/document/d/1UhFPYcyguR5W-v3eKRpsnpmKeYs82eCukAUwMVMdWIs/edit#) that provides every agent with a single governed source of truth. The platform also has to be reachable the way an agent works, which means being API- and MCP-first.

**What does it require from the platform?** An API and MCP-first interface, a governed [context layer the agent reads from](https://thenewstack.io/ai-agent-infrastructure-bottleneck/), and a set of self-service actions it can call.

## Role 2: AI agents as internal platform components

Platforms that can register agents and run them within workflows are using AI agents as part of a full business process. The agent runs within the platform, triggered by an event rather than requested by a person, and sits in the orchestration engine next to the deterministic steps.

![Diagram showing an AI agent as an internal platform component](https://cdn.thenewstack.io/media/2026/08/4ba94367-image2-1024x530.png)

Run a nightly scan that flags vulnerable dependencies across 40 services. The platform pulls the remediation agent from the registry and runs it once per service, so every owning team wakes up to an open PR awaiting review.

**What does it require from the platform?** An orchestration layer to run the agents, a registry to pull the right agent from, an identity per agent so the action is logged against the agent rather than a borrowed human credential, and a human-in-the-loop step where the risk is significant.

## Role 3: AI as a resource with its own lifecycle (a.k.a AgenticOps)

In this role, the agent is a resource like any other, as are the LLMs, MCP servers, and the skills that come with it. The platform provisions them, governs them, and hands them back, just as it does with a service, a database, or an environment.

![Diagram showing AI agents as a resource with a lifecycle, being requested by an engineer.](https://cdn.thenewstack.io/media/2026/08/24a4fd43-image1-1024x482.png)

For example, say an engineer needs an on-call triage agent. They pick the model, the tools, and the environment it runs in, either through a form or by describing what they need, and the platform provisions everything needed, a bit like a vending machine, with the addition of a well-governed agent, in the right standards.

> “That makes it a golden path problem. A golden path is the route that, by default, gets a team a resource the right way.”

That makes it a golden path problem. A golden path is the route that, by default, gets a team a resource the right way, and the agent lifecycle needs one: request it, get it provisioned and registered, and publish it for the next team. It is also what customers ask us for most, with an agent and skill registry raised by 47% of the organizations we spoke with through early 2026. I went into this in more depth in [our golden paths post](https://docs.google.com/document/d/1UhFPYcyguR5W-v3eKRpsnpmKeYs82eCukAUwMVMdWIs/edit#).

**What does it require from the platform?** A self-service path that provisions the runtime, issues the identity and scoped credentials, wires in the approved context, and registers the agent on the way out, plus a route to publish it for the next team.

## The three roles at a glance

| **Role** | **What the agent is** | **Example** | **What it requires from the platform** |
| --- | --- | --- | --- |
| **Role 1: AI agents as platform consumers** | A user of the platform, reading context and running actions as part of its task | Claude Code pulls the service owner, dependencies, and standards, then spins up a preview environment and runs the tests | A governed context layer, such as a context lake, and self-service actions it can call |
| **Role 2: AI agents as internal platform components** | A step inside a workflow, triggered by an event rather than requested by a person | A nightly scan flags a vulnerable dependency across 40 services, and the remediation agent opens a PR for each one | An orchestration layer to run agents in, a registry to pull the right agent from, an identity per agent, and a human in the loop where the risk is real |
| **Role 3: AI as reusable building blocks (AgenticOps)** | A resource the platform provisions, governs, and hands back | An engineer requests an on-call triage agent, picks the model and tools, and gets one back already registered | A self-service path that provisions the runtime, issues the identity and scoped credentials, wires in the approved context, and registers the agent |

## Sometimes the three roles connect

The chained case is an interesting one. An engineer requests a triage agent through role 3; it’s added to the agent registry as part of the creation workflow, and a week later, an incident workflow calls it as a component (role 2). When it runs, it reads service ownership and recent deploys out of the same context lake, which is role 1. It is the same agent throughout, and which role it is in depends on when you look at it.

> “It is the same agent throughout, and which role it is in depends on when you look at it.”

## What does a platform that covers all three look like?

That is what we built Port for. An agent can use Port as a user through a service account, reading the context lake and running self-service actions. Agents run within Port workflows as part of a business process. And AgenticOps runs as self-service workflows, so a team can request an agent and get a registered one back. All three sit on the same catalog, the same context, and the same audit trail.

If you want the full picture, it is in our playbook, [From Agentic Chaos to an AI-Native SDLC](https://docs.google.com/document/d/1UhFPYcyguR5W-v3eKRpsnpmKeYs82eCukAUwMVMdWIs/edit#).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/05/b2c4d92a-cropped-4ef5a0a4-matar-peles.png)

Matar Peles is a solutions engineer at Port, a no-code platform for internal developer portals. In his early career, Matar started in the Israel Defense Forces as a big data infrastructure team leader, where he provided managed big data solutions...

Read more from Matar Peles](https://thenewstack.io/author/matar-peles/)