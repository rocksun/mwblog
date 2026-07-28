Software delivery lifecycle company (SDLC) Harness wants to put agents through the same pipelines and controls that all application code goes through to change the status quo that stalls agentic deployments.

According [to the 2026 Gartner](https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai) CIO and Technology Executive Survey, only 17% of organizations have deployed AI agents to date.

This week, Harness launched its AI Agent Development Lifecycle (DLC) service so developers can ship AI agents with the same governance, testing, and security they already rely on for application code.

## Agentic reality: Technically, a success, but practically useless

[Trevor Stuart](https://www.linkedin.com/in/trevorbstuart/), SVP and general manager at [Harness](https://www.harness.io/), tells *The New Stack* that getting an agent to work in a demo is the easy part, but knowing whether it will behave in production is a different problem entirely.

“The attack surface an agent creates is both larger and dynamic in nature,” Stuart says. “This makes companies hesitant to put it in production. Forcing the agent to stay in pre-production and sandbox environments – the end result is technically a success, but practically useless.”

He underscores this and says that part of delivering anything to production is ensuring that quality and rigor hold up under load. So the hardest part with agents is “keeping that quality bar intact” when the same input can produce a different answer every time.

Because application code is deterministic, developers can run the same test against the same code twice and get the same predictable result both times. Agents clearly think differently. An agent’s underlying [language model](https://thenewstack.io/llm/) decides how to complete a task, so the same agent, given the same input, can choose a different tool or take a different action from one run to the next.

A test that passes once offers no guarantee it will pass the next time. Incidents stop being reproducible on demand, which means the standard playbook for catching and fixing bugs doesn’t transfer either.

## It’s time to make the pipeline predictable

Given these cornerstones, if it feels like attempting to apply deterministic delivery controls to non-deterministic decision-making AI agents is tough, that’s probably because it is.

“Don’t think about trying to make the agent predictable; instead, make the pipeline around it predictable,” Stuart explains. “If we think about how continuous delivery has always worked, we look at whether tests have passed before something shipped. Now we look at [quality gates](https://www.perforce.com/blog/sca/what-quality-gates) and [eval scores](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) the same way: grade the response on correctness, safety, and performance, and wire that score straight into the pipeline as a pass-fail gate.”

> “Don’t think about trying to make the agent predictable; instead, make the pipeline around it predictable. Grade the [test] response on correctness, safety, and performance, and wire that score straight into the pipeline as a pass-fail gate.”

According to Stuart, that’s the real breakthrough here i.e. Harness is bringing deterministic mechanisms and governance to a process that’s dealing with non-deterministic outcomes. He takes care to openly state that we’re not going to make agents (or their output) reproducible, at least not in the immediate future.

“What we can make reproducible is the record of what happened: every model call, every tool call, every step it took, all captured,” Stuart qualifies. “That record is what lets an engineer actually tune the agent toward a better outcome instead of guessing.

He explains that this means “going beyond running evals” before something ships. It involves “testing and iterating on the agent while it’s live” so the developer can make changes quickly and then “see how they land with real usage” to keep refining. All of which means the agent keeps moving toward a better outcome for the customer.

That expanding attack surface initially referenced here is due to agents connecting to tools and APIs, spawning sub-agents, and inheriting trust from every model they touch. Stuart and team state that static scans were never designed for this kind of risk. Harness now aims to provide security capabilities to close that gap with five new products and capabilities spanning testing, deployment, operations, and governance.

## Five new agent control mechanisms

Harness AI Evals makes agent quality measurable, letting teams define eval datasets, wire up scoring functions, and set quality gates that automatically catch regressions whenever an agent or model changes. Harness Agent deployments extend the canary releases, approvals, and [OPA guardrails](https://www.wiz.io/academy/application-security/open-policy-agent-opa) that Harness already applies to Kubernetes deployments to managed agent runtimes.

Also new from Harness is AI configs, to support the release and management of prompts and model changes at runtime; AI asset catalog automatically discovers every agent, skill, and plugin built across an organization’s repositories and links each to an owner, so nothing ships or runs unaccounted for; and Harness AgentTrace, which records what happens during a single agent run and across a full multi-step session, showing which path an agent took, where it slowed down, and how different models or prompts affect the outcome.

Harness is also open-sourcing the foundational components behind AgentTrace, including harness-sdk and harness-evals, so developers can bring the same [tracing primitives](https://thenewstack.io/matt-biilmann-and-netlifys-quest-to-simplify-the-frontend/) into their own AI applications.

## Can developers get on with agentic deployments now?

Does all this mean that developers can now get on with agentic deployments with greater speed and confidence, and, crucially, in terms of quantifiable effectiveness, what’s the trade-off between software engineers using ad hoc pilots to test agents versus using the whole gamut of the Harness platform to oversee governed Agent DLC pipelines?

“There’s no perfect stat here, so I won’t pretend to give you a clean dollar figure,” Stuart concedes. “What we do know from our own 2026 [State of Engineering Excellence report](https://www.harness.io/state-of-engineering-excellence) is that close to a third of a developer’s day (31%), is going to AI-related work that shows up in no metric at all, and 94% of engineering leaders admit things like tech debt, validation time, and burnout are missing from what they track.”

> “There’s no single governance role sitting on top of everything. Ownership attaches the moment something gets built, and it stays traceable back to whoever’s responsible.”

## No single governance role sitting on top of everything

The pipeline shift that Stuart describes here is all about treating the agent and its underlying technology like a service.

“That mentality is what the AI asset catalog is built around,” Stuart concludes. “There’s no single governance role sitting on top of everything. Ownership attaches the moment something gets built, and it stays traceable back to whoever’s responsible. Further, everyone can discover what’s already been built, which reduces duplicate effort and unnecessary sprawl.”

In June 2026, Harness introduced its [Autonomous Worker Agents](https://www.harness.io/products/platform/worker-agents) offering to enable teams to build and run AI agents inside software delivery pipelines. Worker Agents run as governed steps within those pipelines, covered by the same controls Harness already applies to every deployment. Agent DLC extends that same context and governance across the full agent lifecycle.

The pipelines, policies, approvals, and evidence that already apply to an organization’s code now apply to its agents too, so eval gates, deployment approvals, and security checks run as stages within a single pipeline, from the moment an agent is created through everything it does afterward.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)