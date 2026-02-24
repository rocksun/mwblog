The industry has spent the last few years optimizing AI agents’ code-generation capabilities. The focus has been on expanding context windows, fine-tuning models on repository-specific data, and developing complex prompting strategies. This has undoubtedly produced more capable coding agents. However, for most teams, that code-generation capability has not translated into significant gains in productivity.

Most engineering teams are stuck in a manual workflow. The agent generates the code, tests it locally, and submits a PR to the developer for review. Deploying the code, validating that it works, and feeding back any integration issues to the agent all happen at human pace. This workflow puts a hard ceiling on the productivity gains that agents can deliver by making developers into a validation bottleneck.

But some companies are enabling real autonomy for their agents and seeing the productivity gains that AI promises. Organizations like Stripe, Ramp, and the internal teams at OpenAI and Anthropic have come to the same realization: the quality of an agent’s output is directly proportional to the quality of the feedback loop it receives.

> “The quality of an agent’s output is directly proportional to the quality of the feedback loop it receives.”

To elevate engineers to architects and see the speed of [agentic code generation](https://thenewstack.io/better-llm-agent-quality-through-code-generation-and-rag/) translate into productivity, platform engineering teams need to reconsider their strategy. Instead of focusing on giving developers better coding agents, the more impactful lever may be giving agents better feedback infrastructure.

## The lesson from harness engineering

OpenAI recently documented how they [built a complete software product using Codex](https://openai.com/index/harness-engineering/) with a guiding principle of “Humans steer. Agents execute.” Their success was not driven purely by model intelligence or [prompt engineering](https://thenewstack.io/beyond-prompt-engineering-governing-prompts-and-ai-models/). It was driven by a heavy investment in the environment within which the agent operated.

A team of just three engineers generated a working product with internal users and millions of lines of code by designing environments, specifying intent, and building rigorous feedback loops. The primary job of the engineers shifted from writing implementation code to building the scaffolding that allowed agents to verify their own work. This approach is known as harness engineering.

Harness engineering involves equipping agents with the tools and constraints required to act effectively. OpenAI engineers would write a docstring and a set of assertions. The agent would then generate the implementation. If the assertions failed, the environment would automatically capture the traceback, feed it back to the model, and request a retry. This loop allows for dozens of iterations without human intervention.

The key lesson here is that for agents to behave like engineers, they need the same tools, environments, and constraints as engineers at the infrastructure level. By giving the agent a way to validate its own work, they transformed the model from a one-shot code generator into an engineer capable of iteration. The harness provided the signals the [agent needed to debug its own code](https://thenewstack.io/4-reasons-your-ai-agent-needs-code-interpreter/), verify its logic, and deliver fully functioning software.

## Stripe’s Minions and the feedback loop

We can see a similar pattern at Stripe. The company recently published a blog post detailing its internal agent framework, [Minions](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents). Reportedly, Minions produce over a thousand merged pull requests every week. Stripe did not achieve this volume simply by pointing a large language model at its monorepo.

The company built an MCP server called Toolshed, which exposes over 400 tools to its agents. Crucially, it gave agents full access to the development environment and built deterministic verification steps into the agent’s loop.

When a Stripe Minion writes code, the harness forces it through a gauntlet of verification steps. It begins with git operations, then moves to linting and formatting. If the agent generates code that violates the style guide, the linter rejects it immediately and returns the specific line number. The agent consumes this error message and corrects the syntax.

The Minion then moves on to type checking and testing. If a test fails, the error output is fed back into the context window for a fix. This functions as a closed-loop control system, with the development environment itself providing the error signal. This design allows the organization to trust agent output because the system prevents incorrect code from leaving the agent’s local context.

## The verification gap

Most engineering teams today do not operate at this level of sophistication. They often provide their agents with little more than a code editor and a terminal window.

This creates a verification gap. It is like hiring a senior engineer and not giving them access to staging environments, monitoring dashboards, test infrastructure, or code review, and expecting them to contribute effectively.

The feedback signals available to an agent define the ceiling of what it can accomplish autonomously. If an agent can only see the text in the editor, it is limited to fixing syntax errors. If it can see the compiler output, it can detect type errors. But to solve complex integration problems, it needs access to the same rich diversity of signals that human engineers rely on.

> “The feedback signals available to an agent define the ceiling of what it can accomplish autonomously… Without these signals, agents are prone to silent failures.”

Without these signals, agents are prone to silent failures. An agent might generate a SQL query that is syntactically correct and returns the correct data, but performs a full table scan, degrading production performance. Without access to an explain plan or execution metrics, the agent has no way of knowing that the code it wrote fails in production.

![A diagram titled "Feedback Signal Hierarchy" displaying a vertical stack of five boxes, with an upward-pointing arrow on the left labeled "AGENT PRODUCTIVITY."](https://cdn.thenewstack.io/media/2026/02/a5582016-feedback-signal-hierarchy.png)

## A hierarchy of feedback signals

To understand the impact of feedback signals on agents, it is worth mapping the hierarchy. Each level provides the agent with more context and raises the ceiling on their autonomy and, in turn, their productivity.

### Syntax and type checking

This is the baseline. Any competent agent loop effectively eliminates syntax and type errors by iterating against compiler or linter output. However, these represent the shallowest class of bugs. A program can be syntactically perfect and type-safe while completely failing in production.

### Unit tests

Agents that can run local unit tests can verify logic in isolation. This catches a significant volume of logical defects but misses the complexity of distributed systems. A unit test can confirm that a function correctly calculates a tax rate, but it cannot confirm that the tax service is reachable or that the authentication token is valid.

### Integration and API ests

This is where the verification gap widens. To verify that a new or updated service correctly calls an upstream dependency, the agent needs access to a running environment where those services interact. Agents frequently hallucinate API payloads or invent endpoints without this context.

### Observability data

Agents are rarely given access to traces and logs, yet these are critical tools for developers to debug complex failures. Giving an agent the ability to query logs or analyze a trace ID allows it to diagnose runtime behavior issues that static analysis will never catch.

### Visual and end-to-end verification

Finally, visual and end-to-end verification is required to validate any changes that fully impact the frontend. A backend agent might deploy a schema change that passes all service-level tests but breaks the user interface because a component expects a different data format. By equipping agents with isolated previews and tools to drive a browser, they can confirm that their changes function end-to-end and close the loop.

## What’s next

We have already crossed the threshold of model intelligence, enabling powerful engineering capabilities for agents. The limiting factor is now the richness of the feedback signals available to agents.

There is a strong case for treating agent feedback infrastructure as a first-class platform capability, much like CI/CD pipelines are treated now. This involves considering investments in standardized tool interfaces like MCP, structured outputs that make logs and errors easily consumable by machine, and [ephemeral environment solutions](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q1_26_sponsored_content) that allow agents to spin up the isolated spaces they need to test and iterate in parallel against real dependencies.

Teams that build infrastructure to enable these feedback loops will see velocity compound as models improve. Those that do not will always have a ceiling on the productivity they can generate from coding agents.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)