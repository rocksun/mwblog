Boris Cherny, who built Claude Code, recently [shared on X](https://x.com/bcherny/status/2044847849662505288) how to get the most out of it following the release of Opus 4.7. He left the most important tip for last:

“Make sure Claude has a way to verify its work. This has always been a way to 2-3x what you get out of Claude, and with 4.7 it’s more important than ever.”

That observation describes a pattern establishing itself as the standard model for developing software with coding agents. It is also a pattern that is easy to implement locally, against a single codebase with limited dependencies.

It is much more difficult against a cloud-native application with a complex topology. Closing that gap is the difference between coding agents that accelerate teams and those that bury them in review queues and manual validation.

## The pattern emerging across coding agents

Boris’s tip mirrors a pattern emerging across the industry. Every major [coding agent has shipped](https://thenewstack.io/crafting-ai-agents-platform/) infrastructure in the last six months whose explicit purpose is to let the agent check its own work before handing it off.

OpenAI’s Codex iterates in a loop within an isolated cloud container, editing code, running checks, and validating its changes against commands specified in the team’sAGENTS.md file. The validation loop is the product, not a feature on the side.

> “The validation loop is the product, not a feature on the side.”

[GitHub’s Copilot coding](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) agent runs in an ephemeral GitHub Actions environment that automatically executes the repo’s tests, linters, CodeQL, and secret scanning on every task. If anything fails, Copilot attempts to fix it before marking the task ready for review. Cursor’s cloud agents run in sandboxed VMs with shell and browser access so the agent can exercise its changes end-to-end and produce screenshots, videos, and logs as evidence of what it tested.

Claude Code exposes the same shape as composable primitives. Stop hooks prevent teams from completing a task until tests pass. Subagents can run dedicated validation passes that inspect work without modifying it. The verification loop is something the team assembles, but the building blocks are explicit and well-supported.

The convergence is not a coincidence. Every team [building a coding agent](https://thenewstack.io/how-zencoder-is-building-its-coding-agents/) has identified the same problem: a model that writes plausible code without checking it pushes the entire correctness problem back onto the developer. The productivity gain disappears into review overhead.

A coding agent that can verify its own work operates differently. It iterates on the task, catches its own mistakes, and hands over something the developer can reasonably trust. That’s where useful agent work lives, and it’s the bet every major agent vendor is now making.

## Cloud-native systems make the loop harder

All of this assumes the agent can run the change against a realistic environment that mirrors production. In modern cloud-native architectures, that assumption breaks quickly.

The code an agent is changing rarely fails in isolation. It fails at the seams. Services call other services. Async events fire through message buses. A schema change in one service cascades through its consumers. A new middleware header breaks callers three hops away.

> “The code an agent is changing rarely fails in isolation. It fails at the seams.”

The agent writing the change has no way to catch any of that with a mocked integration test. The mock returns whatever the agent told it to return.

Real validation in a distributed system means running the change in a realistic environment and observing what happens as actual requests flow through it. Full end-to-end. Real dependencies. Real traffic patterns.

Anything less pushes the problem back onto the developer. More review rounds. More iteration cycles. Broken staging environments that slow other developers and agents down. The occasional bug that makes it into production.

![Diagram of cloud-native distributed system compared with a monolithic system.](https://cdn.thenewstack.io/media/2026/04/23436a83-3-1024x529.png)

## Realistic feedback, without duplicating the stack

What cloud-native teams need is a feedback loop that lets their agents see how a change actually behaves. Not against mocks. Not against a simplified approximation of production. Against real services, real data paths, and real traffic patterns, close enough to production that the integration failures the agent is most likely to cause are the integration failures it can most easily catch.

That loop has to satisfy three constraints at once.

It has to be realistic. The agent is trying to verify a change that crosses service boundaries, so it needs an environment where those boundaries exist and behave the way they will in production. Anything less and the agent ends up validating a version of the system that will not match what its code actually runs against when it ships.

It has to be isolated. Multiple agents and multiple developers will be exercising changes concurrently, often in overlapping parts of the system. If one agent’s test run breaks the environment for everyone else, the loop has closed for that agent but opened a bigger one for the rest of the team. An agent’s validation work cannot become a coordination problem for the humans around it.

And it has to scale with the way agents actually work. A team running coding agents is not running one task at a time. It is running many tasks in parallel, each on a different branch, each needing its own realistic place to validate. A model that requires duplicating the entire application stack for every agent collapses the moment the team gets serious about throughput, both on cost and on the wall-clock time it takes to stand each stack up.

The environment has to feel like production to the agent, stay out of the way of everyone else using it, and be cost-efficient enough that a team can run as many of them as they have agents in flight.

![Diagram of each agent getting its own isolated environment, but sharing a cluster.](https://cdn.thenewstack.io/media/2026/04/860b19b8-2-1024x529.png)

## Agents need to know how to use the environment

Giving the agent a realistic environment is necessary, but on its own it does not close the loop. An agent with access to a production-like system, and no guidance about how to use it, behaves like a new engineer dropped into an unfamiliar codebase on day one. The access is there. The judgment about how to use it is not.

That judgment has two parts. One is the team’s operational knowledge: which upstream callers to exercise when a code path changes, which downstream dependencies actually affect the outcome, how to tell whether a failing request was caused by the change under review or by a flake three services away. The other is fluency with the tooling inside the environment itself: how to route traffic for testing, how to inspect state across services, which commands are available, how to read the logs the environment exposes. Generic testing know-how covers neither.

Agent skills are the vehicle for both. A skill captures how changes in a particular system should be validated and debugged, and how to drive the specific tools the environment provides to do that work. It is the team’s institutional knowledge, plus the operating manual for the environment, handed to the agent alongside access itself.

What this enables is the thing that matters. An agent that can validate its own work the way a senior engineer on the team would. Not just running tests, but exercising the right paths with the right tools, interpreting the right signals, and recognizing when something is wrong in a way that reflects how the system actually behaves.

Skills and environments have to ship together. An environment without a skill gives the agent access with no judgment. A skill without an environment gives the agent judgment with nothing to act on. Either one alone leaves the loop open.

![Diagram emphasizing that skill and environments are required for the validation workflow to work.](https://cdn.thenewstack.io/media/2026/04/7f878a16-1-1024x417.png)

## The inner loop is where the next leap lives

The next unlock for cloud-native teams using coding agents is not a smarter model. It is a real environment the agent can work against in their inner loop and the context to use it well.

What makes this more interesting over time is that the boundary between inner loop and outer loop starts to dissolve once agents are involved. When a test fails in CI, the natural next step for an agent is not to surface the failure and wait for a human. It is to drop the same change back into an inner-loop environment, reproduce the failure with real dependencies, debug it, and push a fix. The outer loop’s signal becomes the [inner loop’s](https://thenewstack.io/the-kubernetes-inner-loop-with-cloud-foundry-korifi/) starting condition.

It runs the other way too. An ad-hoc validation an agent runs once in the inner loop often deserves to outlive the task. Encoded into the outer loop, it becomes part of the team’s standing regression suite. The inner loop’s one-off experiment becomes the outer loop’s durable guard.

Both directions depend on the same foundation: a real environment the agent can reach from either loop, and the context to use it well. This is the approach we’re building toward at [Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content), so the validation cycle stays continuous wherever the signal arrives.

This feedback loop is what turns agents from [fast code generators](https://thenewstack.io/ai-code-generation-trust-and-verify-always/) into collaborators developers can trust. The teams that close it, across both loops, will be the ones getting the real benefits of coding agents while the rest are buried under their review queues.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)