There’s a pattern I’ve watched repeat for two years. A team builds an agent, hits reliability problems, upgrades the model, sees marginal improvement, and hits the same reliability problems in a slightly different form. The diagnosis is always the same: the model wasn’t smart enough. The fix is always to try a new, smarter model. The result is always the same: still broken.

This isn’t a model problem. It never was.

Andrej Karpathy figured this out months ago, [and in a post on X](https://x.com/karpathy/status/2039805659525644595), he noted a shift in how he was spending his AI compute: “a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge.” He wasn’t running a smarter model. He was building better infrastructure:  raw sources indexed into a directory, an LLM incrementally compiling them into a structured wiki with summaries, backlinks, and concept articles, tools handed to the agent as CLIs, outputs filed back into the base to enhance future queries. The model was constant. The infrastructure around it was the variable.

> “This isn’t a model problem. It never was.”

I keep coming back to the framing. The [model runs on context](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/). The quality of execution depends on the quality of the context it receives, the precision of the actions it’s permitted to take, and the feedback loops that let the system learn from what it got wrong. None of that lives in the model. It lives in the infrastructure underneath. And it turns out, most teams haven’t built it.

## The missing compile setup

Karpathy’s setup is built around one extra step. Raw data comes in. An LLM “compiles” it into a structured, queryable form. Then, agents operate over that compiled version with tools. That compilation step is where the work happens, and it’s what turns a mess of internal data into something an agent can reason over instead of guessing at.

Too many production agent systems still skip this step. They wire the [model directly to raw data](https://thenewstack.io/better-context-will-always-beat-a-better-model/) — databases, APIs, document stores — and expect it to compile at query time, within the context window, under latency pressure. What comes back is pattern-matched guesswork over a window full of noise.

The teams that got this right built the compilation step explicitly. Not a generic knowledge base: a structured representation of how their specific organization works. How things are named internally. What actual decision paths look like. What previous similar runs produced, and what was decided. The organizational equivalent of Karpathy’s wiki — built from operations, not from documentation.

This is harder to build than switching models and harder to maintain. It’s also the difference between an agent that operates in your organization’s actual reality and one that confidently operates in a hallucinated version of it.

## The tool retrieval problem

Karpathy notes that once his wiki reached meaningful scale — around 100 articles and 400,000 words the system remained usable because the LLM maintained indexes and summaries, and because he began adding tools, including a small search engine exposed to the LLM over a CLI. The point is not that context disappears. It is that retrieval, indexing, and tool interfaces become part of the system you have to engineer.

Production agent systems hit this wall hard. Consider a mid-size engineering org: GitHub, Jira, Confluence, a handful of cloud providers, monitoring and alerting tools, a CI/CD platform, internal deployment tooling. Each integration is a family of tools with its own schema, naming conventions, and expected invocation patterns. Dropping all of that into a single context window is slow and expensive, and it produces poor tool selection. The model pattern-matches across noise.

Standard vector retrieval compounds the problem. It matches the semantic similarity between a user query and stored tool descriptions. It works when vocabulary aligns. It breaks when it doesn’t: a developer asks “why did the deploy fail,” the right tool is something like get\_pipeline\_run\_logs, and the vector match between those two phrases is poor. The agent selects the plausible tool instead of the correct one.

The fix is to guess the answer first. Given the query, what would a working tool call look like? The system writes that hypothetical call, then matches against it instead of the raw question. “Why did the deploy fail” and “fetch pipeline logs” don’t look alike as text. But once you’re matching the shape of the right action instead of the words in the request, they line up.

This is a translation layer, from intent to action, and that translation is where most agent failures start. It’s an engineering problem, not a model problem. I’ve seen teams run this in production after watching vector retrieval fall apart at scale, and they say the same thing: switching from semantic similarity to hypothetical-invocation matching gave them more reliable tool selection than upgrading the model.

## The guardrails gap

The capability-without-constraint failure mode shows up across contexts, and the pattern is consistent: an agent with broad tool access, executing correctly from its own perspective, takes an action nobody intended. Not because it hallucinated. Because the boundary between what it could do and what it should do wasn’t enforced.

Three cases illustrate the shape of the problem.

Start with GTG-1002, still the most detailed public account I’ve seen. In November 2025, Anthropic disclosed that a Chinese state-sponsored group had manipulated Claude Code in a cyber-espionage campaign against roughly 30 organizations, infiltrating in a few cases. Anthropic reported that AI did roughly 80-90% of the tactical work, with humans stepping in only at strategic decision points, and that, at peak, the AI was firing off thousands of requests, sometimes several a second. No human team could keep pace. This wasn’t a model-quality failure. It was a failure of execution boundaries. Once the attacker fragmented the work and slipped past the safeguards, the system could take high-risk actions faster than any human could supervise.

Prompt injection is a different vector, same structural failure. Researchers have repeatedly demonstrated agents executing injected instructions from content they retrieved:  a malicious payload in a web page or document that redirects the agent’s next tool call. The model does what the injected instruction says because nothing in the execution layer distinguishes “instruction from user” from “instruction found in retrieved content.” The agent is working correctly. The architecture isn’t.

The third pattern is quieter and more common: over-permissioned agents operating across multiple write-capable systems. An agent with access to a CRM, an email client, and a calendar does something unexpected — updates records, sends a draft, books a meeting — because a workflow reached a branch that wasn’t anticipated and there was no scoped permission model to prevent it. Nobody intended this. Nobody wrote a rule against it. The agent had access, so it acted.

> “An agent with access to a CRM, an email client, and a calendar does something unexpected, because a workflow reached a branch that wasn’t anticipated and there was no scoped permission model to prevent it.”

What these have in common is that the model isn’t the failure point. The failure is the absence of an execution layer that defines, per action, what is permitted and enforces it regardless of what the model decides to do.

The architecture that addresses this intercepts every tool call before execution, masks [sensitive data before the LLM processes it](https://thenewstack.io/llm-integration-pitfalls-protecting-sensitive-data-in-the-ai-age/), blocks specific tool combinations at the execution layer rather than the prompt layer, enforces per-agent rate limits and role-based access, and generates a full audit trail with explicit reasoning for every invocation. Human checkpoints must be designed into high-stakes paths, and not as fallbacks, but as architecture.

We built our execution isolation layer at Mate around exactly this pattern. Every tool call gets validated, scoped, and logged before reaching the integration. The model never has direct write access to a downstream system;  it proposes actions to a layer that decides whether to execute them and at what scope.

Karpathy’s wiki points to the same discipline in miniature: health checks that find inconsistent data, impute missing fields, and suggest new connections. In an enterprise system, that linting layer needs permission boundaries. Some updates can be automatic; others should be routed to proposals, approvals, or review queues. The boundary between what an agent can change and what requires human judgment must be explicit.

## What the engineering work actually looks like

The teams producing reliable production agents spend most of their engineering effort on infrastructure. I see four areas coming up again and again.

**The context graph** **first**. Building and maintaining a compiled representation of org knowledge isn’t a one-time task. Schemas change. Systems get renamed. Personnel and processes shift. Teams that do this well treat the context graph as a product with an owner, an update cadence, and health checks, rather than a setup step that runs once at deploy time.

**Observability second.** Model-agnostic proxy layers are becoming standard: a single layer capturing full traces on every LLM call regardless of provider, enforcing per-tenant cost and rate limits, allowing model swaps without rearchitecting. Tracing for agents means capturing reasoning, not just requests: what the agent considered, which tool it selected and why, what came back, and what it did with the result. Without that, debugging is archaeology.

**Continuous evaluation third.** Per-agent, per-workflow datasets built from production traces rather than synthetic benchmarks. Two tracks: deterministic checks for things code can verify, like tool call correctness, rate limit compliance, scope violations, and model-as-judge for things it can’t, like reasoning coherence and response quality. When you promote a new prompt version or upgrade a model, you run it against real production data. The question isn’t “does it benchmark higher.” It’s “does it still work in this org’s actual context.”

**Configuration management fourth.** Prompt versions, model selections, and tool configurations need to be independently releasable and independently rollback-able. Changing which model an agent uses shouldn’t require a code deployment. Rolling back a prompt regression shouldn’t require an incident. The teams that figure this out early ship changes faster and break less. It’s the same ML engineering discipline that matured in recommendation systems five years ago, now applied to agent behavior, a practice most organizations are building from scratch.

## The differentiator isn’t reasoning

Karpathy’s shift from manipulating code to manipulating knowledge describes where the hard work actually lives in agent systems. The model executes over context. How that context is structured, retrieved, and scoped determines the outcome. What constrains the model’s actions determines safety. What measures and improves the system determines reliability.

All of that is infrastructure. None of it is solved by a more capable model.

The model is commoditizing faster than most teams realize. The reasoning gap between major providers is narrow and narrowing. The infrastructure gap between teams that have built context plumbing and guardrails and teams that haven’t is wide and widening.

> “The reasoning gap between major providers is narrow and narrowing. The infrastructure gap between teams that have built context plumbing and guardrails and teams that haven’t is wide and widening.”

A smarter model won’t help an agent that doesn’t know your organization. It won’t stop a prompt injection in a retrieved document. It won’t scope-limit an over-permissioned workflow. It won’t tell you that your tool retrieval accuracy dropped three weeks ago because someone renamed an integration.

The infrastructure does that. Build that first.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/d0cc2de9-asaf_weiner.jpeg)

Asaf brings a unique combination of product leadership experience from category-defining security companies and operational leadership from elite military units. Before Mate, he led core product areas at Wiz, helping shape its CSPM and Vulnerability Management offerings into category leaders...

Read more from Asaf Wiener](https://thenewstack.io/author/asaf-wiener/)