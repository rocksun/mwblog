*This post is a written deep-dive of the* [*talk I gave at the 2025 AI Engineer World’s Fair*](https://youtu.be/l65so0OoJeo?si=7RtwVDUnQRwpvbOJ) *in San Francisco. Based on my experience with software delivery and agents as co-founder of* [*Dagger*](https://dagger.io/) *and first employee at Docker.*

As LLMs generate ever more code — from more intelligent autocompletion to fully autonomous coding agents — the *cost* of writing code plummets. Pressure then shifts to the delivery pipeline, because every new line must still clear the test suite and code review on its way to production.

Software-delivery automation has always been a bottleneck — that’s why we launched Dagger — but the bottleneck is tightening now that anyone can churn out large volumes of decent code.

In April 2025, we [added native LLM calls to Dagger workflows](https://dagger.io/blog/llm). Teams can now delegate cognitively heavy tasks to LLMs: hardening a Dockerfile for [security and efficiency](https://thenewstack.io/devsecops-tools-that-offer-security-efficiency-and-quality/), diagnosing CI errors and suggesting fixes (or opening the PR directly), even picking up an open issue end-to-end. [We shared concrete examples in our documentation](https://docs.dagger.io/examples).

Let’s examine the pitfalls most teams hit when they embed LLMs — and how to avoid them. The lessons come from software-delivery automation but apply more broadly.

Most people begin by experimenting with flagship models (GPT-4o, Claude 4, Gemini 2.5…). These models are forgiving of sloppy prompts, so early results deliver a “wow” moment and create confidence that multi-agent workflows can tackle complex tasks.

Reality sets in with reliability. When a model ships bad code or fires the wrong tool, even 1-in-10 runs, trust collapses. You can’t introduce that level of variance into the [code that ships your product](https://thenewstack.io/agile-coding-production-requires-agile-security/).

We distilled four principles at Dagger that keep agentic workflows trustworthy in production.

## Scope AI Agents to Small, Well-Defined Tasks

Big models make it tempting to hand agents sprawling, open-ended objectives. Don’t. Shrink each agent’s mandate to the bare minimum and offset the narrow scope with a *long, explicit prompt* that spells out every constraint.

Counter-intuitively, the smaller the task, the longer the prompt. That extra context gives the model guardrails — and models themselves are efficient in helping you refine the prompt.

Think of the LLM as the *brain* and tools as the *hands and feet*. Adding tools feels empowering, but each one enlarges the context window and the chance of random behaviour. Fewer tools → smaller context, lower cost, more deterministic runs.

I often realize that the helpers I planned to expose as tools are cheaper to call outside the agent loop. Example: In our Dockerfile optimizer, a function that counts image layers and total size runs before the agent starts; we feed its output into the prompt instead of letting the agent call it.

Need a larger workflow? Chain micro-agents. A lightweight “triage agent” receives the request and delegates to specialized sub-agents, each with a razor-thin scope and toolset.

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python/tree/ad80f788b9a9c37ab76018824073103b88f154d7/examples/agent_patterns#agents-as-tools) illustrates these patterns.

## Give Every AI Agent a Repeatable Sandbox

Agents, like human developers, should **never** touch privileged environments. They need an isolated, reproducible workspace — secure, disposable, and with straightforward state management in and out.

Because nothing on the market met those requirements, we built [**container-use**](https://github.com/dagger/container-use/). Running as an [MCP server](https://modelcontextprotocol.io/introduction), it spins up a containerized dev environment for any coding agent — Claude Code, OpenAI Opex, Cursor, Goose — or for the agentic workflows you craft yourself.

Working with multiple agents at once? Each gets its own sandbox, so you can experiment freely without polluting local git branches. The sandbox is a [full container stack](https://thenewstack.io/webassembly-users-a-mix-of-backend-and-full-stack-developers/): the agent can run shell commands inside, and you can drop into a terminal at any point to inspect changes or replay commands.

## Trust Demands Full Observability

Transparency breeds trust; agents are no exception.

In most applications, function-level observability is a “nice-to-have” that lingers on the roadmap. With agentic workflows it becomes *mandatory*. The LLM ⇄ tool loop is otherwise a black box, and debugging demands answers to: Which tool was called? With what arguments? In what order? What was the sandbox state at step *n*?

Put simply, you can’t rely on smart agents with no visibility into their work.

Major model providers expose traces (e.g., OpenAI Traces), but don’t bolt on a siloed “AI observability” stack — make [your *existing* platform](https://thenewstack.io/the-3-paradoxes-of-cloud-native-platform-engineering/) AI-aware. That’s why we wired full LLM context (system/user messages, tool calls) into [**Dagger Cloud**](https://dagger.cloud): you can trace the entire delivery pipeline, LLM-driven or not.

The same philosophy applies to [**container-use**](https://github.com/dagger/container-use/): every sandbox session is fully instrumented, so agent behaviour is never opaque.

## AI Agent Reliability Lives or Dies by Evals

Of all four principles, this one matters most: to gauge prompt quality, agent success rates, tool efficacy, and model performance, you must invest early in **Evals** — short for *model evaluations*. Think of Evals as CI for agents.

Models evolve quickly. Even a “perfect” workflow drifts unless you measure it continuously. Run Evals whenever:

* The workflow code changes,
* You upgrade or swap a model,
* You tweak a prompt,
* You modify a tool.

Frequent runs expose an economic truth: big, capable models are also slow and pricey. With metrics in hand, you’ll often downshift to smaller models that, while less powerful, are cheaper and (with the right prompt) more efficient. The trade-off? Those prompts get longer and more meticulous — a useful forcing function for clarity.

As Alex on the Dagger team likes to say: **No matter the model or framework, you can’t outrun prompt engineering.** Early, automated Evals keep you from tearing everything down when large-model costs — or their quirks — hit a wall.

To conclude, [agentic workflows unlock remarkable speed and scale](https://thenewstack.io/cloud-native-and-open-source-help-scale-agentic-ai-workflows/), but only if they run inside tight scopes, clean sandboxes, transparent traces, and relentless Evals. Follow those four guardrails and you’ll turn eye-catching demos into pipelines you can stake production on — today and as models keep racing ahead.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/10/c9e45801-cropped-742c4b95-sam-alba.jpg)

Sam Alba is currently co-founder and vice president of engineering at Dagger, and is the former vice president of engineering at Docker. He joined Docker as the first employee in 2010. He spearheaded the engineering group, scaling it from three...](https://thenewstack.io/author/sam-alba/)