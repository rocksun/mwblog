Recently, I was working with a senior engineering leader at a large financial institution to review their DevSecOps platform engineering roadmap. Their team had deployed an AI coding agent into the development workflow. Merge requests (MRs) were being opened, pipelines were running, and velocity metrics were moving in the right direction.

Then, the internal audit and compliance team asked a seemingly straightforward question: For a specific agent-opened MR that updated a payment service dependency, can you show who approved the change, what inputs and prompts the agent used, what policy checks were evaluated at MR time, and how one might reproduce or unwind that exact unit of work?

The team didn’t have an answer.

The agent was producing output, but the delivery system had no concept of the agent’s work as a bounded, auditable transaction. A diff that passes CI and gets an approval proves a change happened.

It doesn’t prove what context the agent consumed, which policy decisions were evaluated before the MR was created, or whether you could reproduce the result in a subsequent pipeline run.

In regulated environments, “how” and “why” are the whole point.

> “I’ve watched the same dynamic play out across every platform and DevSecOps org I’ve been involved with. The budget line for agentic AI coding tools clears in weeks. The budget line for agent execution records, identity binding, and replay tooling either never shows up or is treated as compliance overhead.”

I’ve watched the same dynamic play out across every platform and DevSecOps org I’ve been involved with. The budget line for [agentic AI coding](https://thenewstack.io/inside-gemini-code-assist-googles-copilot-alternative/) tools clears in weeks. The budget line for agent execution records, identity binding, and replay tooling either never shows up or is treated as compliance overhead.

## The four compliance exceptions

As soon as agents start opening MRs in a regulated CI/CD environment, a predictable class of compliance exceptions appears. The types rarely vary across accounts:

**Provenance missing.** Nobody can show what inputs the agent consumed: the task spec, retrieved context references, tool calls, and repository state at invocation time.

**Identity attribution is unclear.** Nobody can distinguish agent-initiated changes from human-initiated changes because the agent acted under a shared service token, with no named human sponsor on the action.

**Decision chain not reconstructable.** Nobody can show which policy checks were evaluated before the MR was created, or why the agent chose one option over another, because the reasoning was captured only in an ephemeral trace.

**Rollback is not bounded.** Reverting turns into manual archaeology across commits and repos because the agent’s edits were coupled, and there is no clean transaction boundary to unwind.

Resolution means reconstruction: digging through chat logs, partial CI output, and whatever agent traces still exist. In most orgs, nobody tracks how many hours per week get burned on this — which is exactly why the cost stays invisible.

Here is a falsifiable check. Pick the last agent-opened MR that touched a dependency or an IaC file. Can your team produce, within one hour, a single evidence bundle that includes the exact task spec, the repo state reference, the policy checks evaluated at MR time, and the identity of the human sponsor who owned the action?

## Why CI logs fall short

A human-authored MR has a relatively bounded evidence set, including the diff, the approvals, and the pipeline results. An agent-authored MR needs all of that plus the task specification, retrieved context references, tool invocations, model version, policy evaluations, and enough state to replay the task with pinned inputs. CI logs don’t cover this. They show pipeline steps and outputs, not the agent’s context, tool calls, or the policy decisions evaluated before the MR was created.

As agent adoption spreads, the number of micro-decisions per MR increases while the capacity to document those decisions manually stays flat. That’s where the math breaks.

> “As agent adoption spreads, the number of micro-decisions per MR increases while the capacity to document those decisions manually stays flat. That’s where the math breaks.”

Once a non-human system begins authoring changes, the delivery system needs a durable record of what it saw, decided, and did, as part of its workflow, not a separate addition. Agents make this harder because their inputs are non-replicable. The context retrieved, the model version, and the reasoning won’t reproduce the same output if you run it again. The missing link is the binding agent context and actions to the MR as a persistent artifact rather than a side channel.

## When “ship first” works — and when it doesn’t

I’ve seen “ship first, governance later” work. A high-performing product team uses agents for narrow scopes — test generation, small refactors, documentation updates — with a strong human-review culture, a [limited blast radius](https://thenewstack.io/limiting-the-deployment-blast-radius/), and experienced engineers catching problems before they merge. When agents are constrained to low-risk scopes and every change routes through strong review and policy-as-code gates, the repo and pipeline often remain the system of record.

I’ve also seen the opposite failure. A large enterprise tried to build a stable workflow substrate for all automation before scaling usage. It turned into a multi-quarter platform effort with schema debates, replay promises they couldn’t meet, and a new [data retention problem](https://thenewstack.io/airbyte-agents-context-store/) once prompts started getting stored. Product teams bypassed the platform to meet deadlines, instead using lightweight agents with strict guardrails. Audit was satisfied, but the platform effort mostly delayed adoption while creating more governance surface area.

The pattern breaks when teams adopt the “ship first” ethos without the same review discipline, when prompt libraries proliferate with inconsistent logging, and when shared service tokens make identity attribution impossible across the portfolio. A tolerable local workaround becomes an enterprise liability the first time that an audit requests cross-portfolio evidence consistency.

### When speed outpaces governance

Competitive pressure rewards speed, while regulators reward reconstructability. Leadership has to hold both.

The cost of moving fast without a recorded execution layer isn’t a broken build. It’s an evidence gap discovered during a regulatory examination, a multi-week remediation with executive visibility, and a blast radius that compounds across every agent-initiated change that was never properly recorded.

> “The cost of moving fast without a recorded execution layer isn’t a broken build. It’s an evidence gap discovered during a regulatory examination.”

## Staffing the recorded execution work

The practical move is to name this work explicitly, “Recorded Execution for Agentic CI/CD,” and staff it like a product, with platform engineering, security, audit liaison, and developer experience at the table. The deliverables map directly to the four reconstruction failures above: an execution record schema capturing inputs, outputs, tool calls, model version, and policy outcomes; [identity binding that ties every agent](https://thenewstack.io/why-ai-agents-need-their-own-identity-not-yours/) action to a human sponsor; policy decision logs at MR and pipeline time; and replay and rollback primitives that make the unit of work re-runnable with pinned inputs.

Manage it with operational metrics: compliance exception queue depth for agent-initiated MRs, median time-to-evidence, replay success rate, and exception re-open rate after audit follow-ups. If you can only do one thing, build the execution record and replay path for the highest-risk use cases first, such as dependency changes, IaC modifications, and security configuration, then expand.

A final test: ask a team to pick one merged agent-authored change and perform a clean rollback as a single bounded unit, using only recorded artifacts. If the rollback requires Slack search, local clones, or recreating the prompt and hoping, you have your action plan.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/81408769-brianwald.png)

Brian Wald is Head of Global Field CTO org at GitLab. He leads a dynamic team of Field CTOs dedicated to transforming enterprise software development practices.

Read more from Brian Wald](https://thenewstack.io/author/brian-wald/)