Before the hype around [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) had a chance to die down, Anthropic pulled another winner out of its hat: [Agent Skills](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/).

Agents are full decision-making entities with system prompts, tool access, backing models (Claude, ChatGPT, etc.) and agentic loops that let them orchestrate workflows and manage state.

The [new Agent Skills](https://agentskills.io/home) are modular, declarative bundles of expertise — organized procedural knowledge packaged into reusable units that agents load progressively as needed.

This raises an interesting and fundamental architectural question: What should be an agent, and what should be a skill? The choice has real implications for scope management, context-window reliability, extensibility and evaluability.

The answer is not picking one over the other. It’s agents with skills.

## **Why Agents Can’t Scale Through Prompts Alone**

Early agentic systems hit predictable walls. Teams built specialized agents for each use case: a customer service agent, a coding agent, a research agent. When these agents needed new capabilities, developers updated system prompts or created an entirely new agent. This works, but it can quickly become unmanageable.

The pattern repeated across organizations: A new edge case required prompt modifications, which sometimes fixed the issue but often caused regressions elsewhere. Agents lacked mechanisms to learn from execution or transfer knowledge across contexts. Context windows became bloated with increasingly complex instructions or contradictions, causing agents to get distracted, confused or unable to reason about conflicting information.

Collectively, we used to think agents would look very different in different domains based on their prompts and tooling. But the model-agent relationship underneath is actually more universal than we thought. This realization suggested a different model: one general-purpose agent equipped with a library of specialized capabilities.

## **Why Agents Need Skills**

Skills allow us to iterate on domain expertise without architectural changes.

They are primarily declarative, meaning subject matter experts can contribute capabilities without modifying agent logic. A security team can package its compliance workflows into a skill. A [data engineering team](https://clickhouse.com/blog/agent-facing-analytics) can encode its ETL best practices. These contributions don’t require touching the agent’s core system prompt or decision-making loop.

When agents encounter new scenarios, skills provide a clear responsibility boundary. Teams can update a skill for one domain without risking regressions in another. Skills can be versioned, tested in isolation, and improved based on telemetry, all without the fragility of system prompt engineering.

Skills enable progressive loading, which introduces resources incrementally to help address context bloat. Anyone using agents has probably experienced what happens when context windows become bloated, and [research throughout 2025](https://www.anthropic.com/engineering/code-execution-with-mcp) demonstrated that overloading context windows causes surprising failure modes.

Progressive loading addresses this: At runtime, agents see only skills metadata (name and description). The full content loads only when the agent determines a skill is relevant to the current task. This means the amount of context bundled into skills can be effectively unbounded without compromising the agent’s reasoning ability.

## **A Real-World Example**

We faced this exact architectural decision while building [clickhouse.build](https://clickhouse.com/blog/clickhouse-build-agentic-cli-accelerate-postgres-clickhouse-apps), an agentic coding assistant that helps developers migrate analytical workloads from [Postgres to ClickHouse](https://thenewstack.io/postgres-clickhouse-the-oss-stack-to-handle-agentic-ai-scale/). Our command line interface (CLI) initially provided four specialized agents: a scanner that identifies analytical queries in codebases, a data migrator for setting up ClickPipes, a code migrator that adds ClickHouse interfaces while maintaining backwards compatibility and a QA agent to validate changes.

The scope was deliberately narrow: Postgres queries and TypeScript codebases. This specificity made the agents performant but limited their applicability. When Anthropic released Agent Skills in October 2025, we saw an opportunity to expand beyond this narrow scope without sacrificing quality.

By introducing Skills, we can now support other online transaction processing (OLTP) sources such as MySQL and [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), Python and Java codebases, and more flexible QA workflows without rewriting our core agents. Language client maintainers can develop Skills for their domains (Golang, Java, Python) without touching agent orchestration logic. We can build evaluations around specific skills and improve them in isolation.

Our agents maintain scope and quality through evaluations, while skills enable contribution from domain experts across the organization and protect context windows through progressive loading.

## **When To Build an Agent or a Skill**

So, when should something be an agent or a skill?

Build an agent when you need:

* Full workflow orchestration with multistep decision trees.
* State management across complex operations.
* Quality control through systematic evaluations.
* Scope boundaries that prevent misuse.

Build a skill when you need:

* Reusable procedural knowledge applicable across contexts.
* Domain expertise contributions from nondevelopers.
* Context window protection through selective loading.
* Capabilities that can evolve independently.

Many existing agents — effectively structured prompts with tool access — can likely become skills with minimal changes. But some use cases genuinely require the control, scope management and evaluability that full agents provide.

## **Agents Need a License To Skill**

The future of [agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) isn’t choosing between agents and skills. It’s agents equipped with the right skills at the right time; agents with a license to skill, if you will. The agents orchestrate, maintain scope and ensure quality through evaluations. The skills package expertise, protect context windows and enable contributions from domain experts.

This architecture is already reshaping production systems like clickhouse.build, and with skills emerging as an open standard alongside MCP, it’s positioned to become the default way forward.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/01/4191ee4f-pete-hampton.jpg)

Pete Hampton is a Principal Software Engineer at ClickHouse where he leads the development for the AI/ML team. Prior to this he worked on financial trading systems and big data pipelines.

Read more from Pete Hampton](https://thenewstack.io/author/pete-hampton/)