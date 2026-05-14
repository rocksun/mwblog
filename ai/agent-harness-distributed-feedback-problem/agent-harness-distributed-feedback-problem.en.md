*Coding agents perform better with a harness that gives them the tools, guidance, and feedback signals to know what to do, how to do it, and how to know if it works. In cloud-native systems, providing the feedback component is less straightforward.*

I’ve been sitting with [Addy Osmani’s recent post on agent harness engineering](https://addyosmani.com/blog/agent-harness-engineering/) for a few days. The argument is one I find myself agreeing with: a coding agent is the model plus everything wrapped around it (prompts, tools, context policies, sandboxes, subagents, hooks, feedback loops), and that scaffolding does more for the agent’s behavior than another model upgrade does. Addy points to data from Viv Trivedy showing that the same model, dropped into a different harness, moved from rank 30 to rank 5 on Terminal Bench 2.0. Once you’ve seen a few of those swings, it gets hard to keep treating model selection as the interesting variable.

What I want to add is a wrinkle that shows up when the agent’s job is to change code in a cloud-native system. The harness framing holds, and so does the idea that feedback loops are central to making it work. The hard part is what “feedback” actually means in a distributed system and what infrastructure must exist for an agent to receive it within its loop.

The components of an agent’s “harness” are not equal. Prompts shape what the agent attempts. Tools like MCP and CLIs determine what it can act on. Skills guide how it attempts a change and what tools it uses. Policies and sandboxes define the guardrails for its actions. All of these influence what the agent can do and how it behaves. None of them tells the agent whether the attempt worked. That is the job of the feedback signal. Feedback is what closes the loop, what turns the agent from an open-loop generator into something that can self-correct and finish work without intervention.

For the kinds of work Addy and others write about (a single application, runnable locally, gradeable through a browser), the infrastructure for that feedback is mostly straightforward. For distributed systems, providing the same kind of signal is much harder.

## What good feedback looks like in a harness

Addy uses a framing I find useful: success is silent, failures are verbose. If typecheck passes, the agent hears nothing. If it fails, the error gets injected into the loop and the agent self-corrects. The same shape holds for tests, lint, and any deterministic check. Hooks at lifecycle points (pre-commit, post-edit, pre-PR) separate “I told the agent to do X” from “the system enforces X.” Without enforced feedback, the agent’s other components are just suggestions.

[Anthropic’s work on long-running harnesses](https://www.anthropic.com/engineering/harness-design-long-running-apps) pushes this further. Their three-agent setup (planner, generator, evaluator) drove a Playwright session that clicked through the running app and graded it against criteria. Across multi-hour runs, the result was working full-stack applications. The load-bearing piece was the evaluator’s feedback.

This is the picture for single-application work, runnable locally, where “does this work” can be answered by spinning up the dev server and clicking around. Most production software does not fit that shape.

## What cloud native breaks

Production code in a [microservices architecture](https://thenewstack.io/how-to-apply-microservice-architecture-to-embedded-systems/) lives inside a distributed system. A change in one service must be applied to the real services it depends on: the database, the message bus, the config, and the auth layer. The signal an agent needs to know its change works is the system’s actual response at runtime, and none of that exists inside a local sandbox. Tests that “pass” without that feedback miss most of the validation surface.

![Infographic showing what passed tests validate](https://cdn.thenewstack.io/media/2026/05/b04a799c-1-1024x333.png)

Three workarounds show up in practice, and all three break the feedback loop at the same point.

**Mocks and stubs.** Fine for unit-level work. But the bugs that matter in distributed systems emerge from interactions between real services with real state, and mocks reproduce neither of these.

**CI after the PR opens.** Real environments exist there, but the signal arrives outside the agent’s loop. The agent finishes, opens a PR, and waits. Failures at this stage are expensive: the agent has lost its working context, a human is now in the loop, and cycle time has stretched from minutes to hours. The feedback exists, but it comes too late and too inefficiently.

**Full preview environments per branch.** Platform teams have done this for human PRs for years. The math stops working at agent volume: parallel agents easily generate ten times the branch volume, and ten times the previews (each a full system clone) is not a budget conversation anyone wants to have.

> “In cloud-native systems, the standard harness model gets the agent to “I think this works” and then stops.”

In cloud-native systems, the standard harness model gets the agent to “I think this works” and then stops. The feedback that would tell it otherwise either does not exist, arrives too late, or does not scale. The agent has no choice but to hand off to a human to validate the behavior and close the loop. The feedback component that the harness depends on needs better infrastructure to function as intended in a distributed system.

## The role of environments in a complete harness

If the feedback that matters in cloud-native systems is runtime response, the harness needs a runtime to point the agent to. Not a sandbox, which isolates the agent’s execution from the host, but an environment, which gives the agent a real, runnable, system-level surface to validate against. The sandbox protects the host from the agent. The environment provides the feedback the agent needs to validate whether its change works in the real system and correct it if it doesn’t. Both belong in the harness, and they do different jobs.

> “The sandbox protects the host from the agent. The environment provides the feedback the agent needs to validate whether its change works in the real system and correct it if it doesn’t.”

Four properties must be met for an environment to function as an effective harness at agent speed and scale.

**Cheap and fast.** Not a full staging clone. A lightweight ephemeral environment that shares stable infrastructure and isolates only what the agent’s change touches. If spinning one up costs as much as a full preview, the math fails. If it takes more than a few seconds, it falls outside the agent’s iteration window.

**Realistic.** The environment has to route real traffic through real services, with the agent’s changes layered on top. The agent should be debugging the same conditions that production exhibits.

**Programmable.** The agent has to spin one up, exercise it, read the results back, and tear it down. If a human has to provision or interpret, the loop is broken before it starts.

**Isolated.** The environment needs to provide realistic feedback in a single shared environment while remaining fully isolated from other changes to avoid collisions with other agents. One shared cluster needs to serve hundreds or thousands of agents working in parallel without contention.

None of these requirements is exotic. [Platform teams have been building](https://thenewstack.io/internal-platforms-are-products/) toward them for years in the service of human developers. What [changes for agentic development](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/) is treating them as part of the harness the agent itself drives, rather than infrastructure that sits beside the loop and gets consulted at PR time.

## What this enables

Once the agent has runtime feedback inside its loop, the validation surface expands well beyond what local checks can cover. The agent can run integration paths end-to-end against the actual call graph between services. It can verify contract behavior against real consumers and producers, not generated stubs. It can hit the real database, observe real transaction behavior, and catch migrations that break unrelated queries.

These are the checks most engineers run by hand today, mostly after the agent is done, through some combination of local reproduction, staging, and PR-stage CI. None of them are tractable when the harness ends at a local sandbox, which is what limits how far an agent can autonomously pursue a change.

With runtime feedback, the agent does not just produce a diff that compiles and passes unit tests. It produces a change with verified evidence: traces showing the code ran, tests showing the integration holds, and observability data showing nothing else regressed. The diff arrives at PR review already validated against the parts of the system that matter. The reviewer’s job shifts from “does this work” to “should we ship this,” which is a different and more valuable kind of attention.

![Infographic showing how a realistic environment validated eight out of ten unit tests before the agent handed off.](https://cdn.thenewstack.io/media/2026/05/0aefc422-2-1024x328.png)

## Closing the loop

Harness engineering has the right shape: coding agents need scaffolding around them to be useful, and feedback loops are central to that scaffolding. The components that shape an agent’s first attempt have come a long way, and the typecheck-and-test feedback that closes the loop on local work is well understood. What is still missing for engineering teams building distributed systems is the infrastructure that enables the same kind of feedback against a real, running system at agent speed and scale.

That is what we [work on at Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content): lightweight environments that share a baseline infrastructure, isolate per change, and provide agents with a programmable runtime to validate against. Realistic feedback at agent speed and scale, inside the development loop.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)