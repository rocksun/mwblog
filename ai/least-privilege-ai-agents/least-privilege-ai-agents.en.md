What happens when you give an AI support agent a permission it never needed, then assign it a task the underlying data does not support? The result is entirely predictable. During a test with customer invoices, an agent pulled up a record, confirmed the charge had failed, and no money had left the customer’s account, and refunded it anyway. It repeated the mistake five times without hesitation.

That was Claude Haiku 4.5 going six for six on tasks designed to catch that exact logic flaw. Claude Sonnet 5 identified all six edge cases on its own. Adding a single line to Haiku’s system prompt instructing it to verify transaction state before executing financial actions also resolved the issue.

I had two working fixes and felt reasonably confident until I realized I control neither variable. The moment someone reroutes support traffic to a cheaper model next quarter to [trim inference costs](https://thenewstack.io/ai-pipeline-token-optimization/), the first fix evaporates. If someone trims or rewrites the system prompt during an experiment, the second fix disappears, leaving no record of the safety guardrail it maintained.

> “The only safety control that survives your own cost-cutting is the permission you never granted in the first place.”

The only run that held up reliably was the one where the agent lacked the authority to make the decision. Because its role excluded `billing:refund`, the execution failed at the permission layer, making the underlying model completely irrelevant.

This is the core argument for least privilege in AI architectures. It isn’t just about malicious actors or leaked tokens; it is about preventing a well-behaved agent from faithfully executing a flawed instruction at machine speed with zero human oversight. The only safety control that survives your own cost-cutting is the permission you never granted in the first place.

## Roles are drawn in advance; agent work is not

A [standard service account](https://thenewstack.io/ai-agent-identity-crisis/) receives a role because a microservice performs one predictable job forever. The payment service handles payments; you scope it once, review it annually, and move on.

An agent’s workload changes on every invocation. The same support agent reads a ticket at 09:00, issues a refund at 09:04, and modifies a seat count at 09:11. The union of everything it might do over a week bears no relationship to what it needs in a single run.

Asking “how much of its permission set does an agent use?” yields a useless metric because that number reflects how generously you provisioned the credential. Grant 400 scopes, and utilization looks catastrophic; grant four, and it looks efficient. You end up measuring an arbitrary configuration choice rather than systemic risk.

A meaningful calculation evaluates the task distribution independently of the grant:

Over−scopefactor=|Unionofscopesexercisedacrossalltasks|Median(|scopesexercisedpertask|)Over – scopefactor = \frac{|Unionofscopesexercisedacrossalltasks|}{Median(|scopesexercisedpertask|)}

This metric represents the blast-radius multiplier. In a compromised run, an agent reaches the total union of scopes rather than the per-task subset. Across my test suite, that factor reached 11.0. The union across 20 tasks totaled 22 scopes, while the median task required only two.

## The experimental framework

I constructed a test environment with 30 scopes across nine domains of a mock enterprise API covering tickets, users, billing, subscriptions, files, messages, audit, admin, and search. Thirteen of these scopes modify or exfiltrate state. Every command maps to exactly one scope, and the system logs every attempt — whether allowed or denied.

The suite comprises 20 tasks, each ending in a state change verifiable mechanically rather than by evaluating the agent’s prose (e.g., closing a ticket, refunding an invoice, or calculating seat overages and commenting the total).

Before running any agent, I authored a reference solution for every task to serve two functions:

1. It confirms the task is solvable via the CLI, ensuring a run failure stems from the agent rather than an impossible environment.
2. It establishes the minimum required scope set by observing the exact endpoints a correct solution touches.

I evaluated four permission models that differed strictly by which credentials were active at the moment of execution:

* **Broad:** One long-lived credential holding all 30 scopes.
* **Role:** A static support-agent role holding 17 scopes derived from a typical job description.
* **Task:** Scopes issued per run based on a declared plan, expiring when the run completes.
* **Just-In-Time (JIT):** Starts at zero scopes, requesting each scope on demand with a stated rationale.

Each model ran against two LLM tiers — Claude Haiku 4.5 and Claude Sonnet 5 — totaling 160 runs. The test stack relies strictly on standard-library Python with zero external dependencies or API keys, allowing full reproduction of the reference runs and metrics.

## Blast radius against completion

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Permission model** | **Live scopes** | **Destructive scopes** | **Task completion (Haiku / Sonnet)** | **Call overhead** |
| **Broad grant** | 30 of 30 | 13 | 20/20 · 20/20 | Baseline |
| **Role-based** | 17 of 30 | 2 | 10/20 · 9/20 | Baseline |
| **Task-scoped** | 2 of 30 | 1 | 20/20 · 20/20 | Negligible |
| **JIT escalation** | 2 of 30 | 1 | 19/20 · 20/20 | +79% / +84% calls |

Task-scoping achieved complete task execution while holding one-fifteenth of the credentials compared to the broad grant. The occasional denied call and subsequent retry did not meaningfully increase overall API call volume, making the [reduction in blast radius](https://thenewstack.io/ai-agents-credential-crisis/) effectively free.

The minor completion gap under role-scoping did not stem from permission failures. Both models stalled on the same ten tasks. The single-task variance occurred because one task dataset contained three open tickets with identical subjects. Sonnet declined to guess which ticket to close under the role configuration, yet selected the lowest-numbered ticket under the other three models — even though the role grant contained every scope that task required. This represents standard run-to-run variance on an ambiguous prompt.

> “Role-based provisioning is simultaneously too broad and too narrow because it assigns permissions based on a job title rather than the underlying work.”

Role-based scoping performed worst across both axes: it held 8.5 times more credentials than task-scoping while completing half as many tasks. Comparing the role grant against actual task requirements explains why: it granted four scopes no task ever invoked while missing nine essential scopes. Expanding the role until every task passed required 26 scopes — compared to a median task requirement of two. Role-based provisioning is simultaneously too broad and too narrow because it assigns permissions based on a job title rather than the underlying work.

Under role-scoping, each model hit ten permission denials (one per blocked task) and failed every blocked run. These ten denials hit eight of the nine missing scopes (`billing:refund` and `files:upload` each blocked two tasks). The ninth missing scope, `admin:update_settings`, was never reached because the task failed a step earlier at `admin:read_settings`.

Under task-scoping, Haiku encountered one denial, and Sonnet hit six across four total tasks — yet all four tasks verified successfully. Because a task-scoped grant contains the primary permissions required, denials hit only optional exploratory paths the agent tried (such as querying a search endpoint instead of a list endpoint). Conversely, because a role grant lacks required scopes, its denials are terminal.

JIT escalation achieved the same low blast radius without advance declaration, but it cost ~80% more API calls.

## Evaluating the three defensive layers

|  |  |  |
| --- | --- | --- |
| **Configuration** | **Executed harmful refund** | **Caught issue via reasoning** |
| **Haiku 4.5 (No prompt hint)** | 6 of 6 | 0 of 6 |
| **Sonnet 5 (No prompt hint)** | 0 of 6 | 6 of 6 |
| **Haiku 4.5 (One-line system prompt hint)** | 0 of 6 | 6 of 6 |
| **Role arm (Lacking** **billing:refund****)** | 0 of 6 | 0 of 6 (Blocked by policy) |

Model capability cannot serve as a primary security control because you do not own the model lifecycle. The day an operations team routes traffic to a cheaper model to cut inference spend, your safety guarantees disappear without triggering an error in your test suite.

Similarly, system prompts are fragile controls. Prompts drift over time; an engineer might trim the prompt to save tokens or rewrite it for an experiment, silently stripping the guardrail.

> “A scope that was never granted holds firm regardless of which model runs behind it, how the prompt is modified, or whether the team remembers why the guardrail existed.”

A scope that was never granted holds firm regardless of which model runs behind it, how the prompt is modified, or whether the team remembers why the guardrail existed.

To be clear: this data does not show that agents are inherently reckless. Across standard workflows, agents invoked only 4% to 5% more scopes than the reference minimum — demonstrating disciplined execution. The problem is scale: when a well-behaved agent carrying 30 scopes encounters an edge case, it executes mistakes at a 30-scope scale.

## Requirements for a purpose-built agent identity model

1. **Scope credentials to the task, not the actor:** Task-scoped credentials yield identical completion rates with one-fifteenth the blast radius and no measurable overhead. The [execution run is the primary identity](https://thenewstack.io/agent-workload-identity-authentication/), not the agent.
2. **Tie credential expiration to the run lifecycle:** A task-scoped credential that outlives its task degrades into a broad credential. The median run in this test suite required permissions only for a single operation.
3. **Deploy escalation paths over static ceilings:** JIT permissions increased call volume by ~80%, which represents the operational cost of runtime discovery. Use declared scopes when a planner can predict them, use JIT escalation when it cannot, and treat every escalation as an auditable event.
4. **Design permission denials to redirect rather than block:** Denials under task-scoping were non-fatal because the grant contained the core permissions needed to finish the task. If permission denials consistently break your workflows, your scoping model is flawed, and widening the static grant is the wrong fix.

## Audit logs as primary security artifacts

Every experiment in this framework runs on an append-only log that tracks allowed and denied execution attempts. This log provides the primary telemetry needed to investigate operational incidents.

Denied calls are as critical as successful ones. A denied attempt signals that an agent’s active grant does not match its workflow — indicating either a scoping error or prompt injection. Under JIT escalation, every privilege expansion records a timestamp and an explicit rationale, replacing guesswork with concrete audit records when investigating why an agent accessed a resource.

The audit log also verified experimental integrity, proving no agent bypassed the API by directly modifying fixture states. A task that reports completion without a corresponding mutating call in the log indicates out-of-band tampering. All 160 runs remained consistent because the system verified the execution log directly.

Analyze one week of your agent’s production traffic and evaluate two metrics:

1. The total union of scopes exercised across all runs.
2. The median number of scopes exercised per individual run.

Divide the first number by the second. If the ratio approaches 1.0, your agent performs a single, static task, and a fixed credential is sufficient. If the ratio approaches 11.0, each run carries an order of magnitude more permission surface than it needs — leaving excess authority waiting to be exploited.

Finally, review the last destructive action your agent executed incorrectly and determine which layer should have prevented it. If you rely on the model or the prompt for safety, your security model is vulnerable to the next cost-optimization ticket. In these test runs, the cheaper model executed six out of six harmful financial actions with contradictory data displayed directly on screen. The only configuration that stopped execution every time was the one where the permission didn’t exist.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/09/fd4e9ea3-kayode-scaled-600x600.jpg)

Kayode is an innovative Software Engineer with 13+ years of experience building products that matter. His primary tech stack includes Rust, Python, and JavaScript, with strong expertise in PHP. He works across the full stack, from mobile apps with Flutter...

Read more from Kayode Ojo](https://thenewstack.io/author/kayode-ojo/)