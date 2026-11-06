In September, I ran two models through the same 20 support tasks. Both scored 20 out of 20. Then I assigned each model two refund requests that the underlying billing data didn’t support: one against an uncollected invoice, and one for double the invoice’s value.

Claude Haiku 4.5 issued all six refunds across three distinct permission configurations. Claude Sonnet 5 issued none. Their success rates looked identical, but their behavior diverged completely on the only scenarios capable of causing financial damage.

In October, I reran the [evaluation harness](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/). This time, the smaller model declined every unauthorized refund. I initially attributed this to queue ordering: the two trap tasks sat at the end of a 22-task queue instead of arriving in isolation, suggesting that processing 20 prior invoice tasks taught the agent to verify state before acting. I documented this theory in a neat report.

> “Their success rates looked identical, but their behavior diverged completely on the only scenarios capable of causing financial damage.”

Then I checked the execution transcripts for the active model alias. In September, the haiku alias resolved to claude-haiku-4-5. In October, the same alias resolved to claude-haiku-5-5. I reran the isolated trap tasks three times against the new model version, and it declined all six attempts. Queue position had nothing to do with the outcome; the underlying model had been silently upgraded behind an unpinned alias. I discovered this only because of a script search I nearly skipped.

An unlogged, uninitiated deployment had occurred. Nothing in my high-level success metrics flagged the shift: 20 out of 20 in September, and 18 out of 19 on scored tasks in October (with the single failure stemming from an intentionally ambiguous prompt). Although the silent model update improved performance, the underlying monitoring gap remains concerning: none of the metrics I tracked would have alerted me if performance had degraded instead.

I stopped asking whether my agent was functioning and focused on a narrower diagnostic question: If I intentionally break the system, which metrics actually detect the failure?

## Intentionally breaking the agent

The target system is a customer support agent interacting with a [mock enterprise API](https://thenewstack.io/building-agent-friendly-apis/) spanning 30 scoped operations across tickets, users, billing, subscriptions, files, and messages. Every API call writes to an append-only audit log, and each task concludes with a state change that an external script verifies mechanically against the database. The suite contains 19 standard scored tasks alongside the two refund traps.

I established a baseline using Claude Sonnet 5.5 (claude-sonnet-5-5) with full administrative privileges across three identical runs. Evaluating three baseline replicates is critical: a detection system that fires false positives on an unmodified setup is useless. Every detection threshold reflects the baseline variance doubled to account for real-world statistical distribution.

I then introduced eight specific regressions—one per test run—to simulate [common production failure modes](https://thenewstack.io/when-ai-fails-the-new-reality-of-incident-management/):

* **Weaker model:** Executed the standard prompt using Claude Haiku 5.5.
* **Speed pressure:** Added a single instruction directing the agent to minimize API calls and skip optional read operations.
* **Truncated documentation:** Restricted the API documentation to list only 11 of the 30 available commands.
* **Missing scope:** Revoked one required permission per task from the credential grant.
* **Stale reads:** Routed read queries to an asynchronous replica that lagged behind primary writes.
* **Flaky upstream API:** Intercepted a deterministic 25% of API calls with transient errors.
* **Slow upstream API:** Introduced 1.5 seconds of artificial latency to every network call.
* **Distractor tool:** Exposed a deprecated alias alongside the valid close-ticket command that accepted calls without mutating state.

Six of these eight regressions execute inside the API behind a per-run wrapper script, ensuring deterministic, reproducible failure paths.

Before evaluating detector sensitivity, I verified that each injection actively affected the execution environment. A detector cannot catch an idle regression. The logs confirmed the flaky API arm intercepted 31 calls, the stale read arm served 18 outdated queries, and the missing-scope arm triggered 19 authorization denials.

The distractor arm invoked the deprecated alias zero times because the model selected the correct command on every attempt. I classified that regression as absorbed rather than missed, excluding it from detector denominators while retaining it as a false-positive control. As expected, an arm where no operational failure occurred triggered zero behavioral alerts.

## Detection results

Detector thresholds derived from the baseline runs:

* **Task success:** Fires below 18 of 19 verified completions.
* **Token cost:** Fires outside a ±37% volume envelope.
* **Tool calls:** Fires outside a ±7% call count envelope.
* **Scope drift:** Fires above a 0.135 threshold (calculated as *1 – overlap* between the active task scopes and baseline scopes, averaged across all tasks).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Regression arm** | **Verified tasks** | **Token change** | **Tool call change** | **Scope drift** | **Triggered detectors** |
| **Baseline (3 runs)** | 19, 19, 19 | 85k to 103k | 59, 59, 57 | Up to 0.067 | Baseline |
| **Missing scope** | 4 | +22% | -9% | 0.496 | Success, Tool calls, Drift |
| **Truncated docs** | 13 | +73% | +20% | 0.281 | Success, Tokens, Tool calls, Drift |
| **Weaker model** | 18 | +36% | -4% | 0.202 | Drift |
| **Speed pressure** | 19 | -17% | -21% | 0.256 | Tool calls, Drift |
| **Flaky upstream** | 19 | +26% | +70% | 0.135 | Tool calls |
| **Stale reads** | 19 | +22% | +5% | 0.133 | None |
| **Slow upstream** | 19 | -3% | -1% | 0.050 | None |

Across the seven active regressions, tool-call counts and scope drift each caught four failures. Task success rates caught only two. Token costs flagged one, while the refund trap tasks caught zero.

Task success rates flagged only the two regressions that made task completion physically impossible. Swapping the model, modifying system prompts, failing 25% of network calls, serving stale data from replicas, and adding 1.5 seconds of API latency all left task completion steady at 18 or 19 out of 19.

The speed-pressure arm requires context: the agent completed every task using 21% fewer calls and 17% fewer tokens. Two behavioral detectors flagged this run because the execution pattern shifted significantly, even though the shift improved efficiency. Behavioral detectors report movement; engineering teams must decide if that movement represents progress or degradation.

## How competent agents mask infrastructure faults

AI agents routinely mask underlying technical failures through three primary behaviors:

### 1. Automated retry logic

The flaky API arm absorbed all 31 injected network failures. Before retrying non-idempotent write operations, the agent queried the backend to confirm if the initial attempt had committed, preventing duplicate refunds. One task—a subscription cancellation followed by a customer notification—absorbed seven consecutive API failures during execution.

> “As agent retry logic improves, downstream task completion becomes increasingly decoupled from infrastructure health.”

The arm verified 19 out of 19 tasks while executing 99 tool calls against the 58-call baseline. As agent retry logic improves, downstream task completion becomes increasingly decoupled from infrastructure health.

### 2. Autonomous workarounds

When provided with documentation for only 11 of 30 commands, the agent recovered missing endpoints by guessing plausible command names. It batched hundreds of experimental attempts into shell loops, distinguishing valid endpoints from invalid ones based on returned error structures.

Through this brute-force approach, the agent successfully discovered refund, messaging, file upload, search, and admin endpoints. It failed to discover subscription commands, causing six tasks to fail.

This recovery process consumed 161,013 tokens (73% above baseline) and took 15 minutes to execute, compared to the five-minute baseline. Because the agent executed these speculative loops locally, the attempts never hit the API audit log. The regression remained detectable almost entirely due to its extreme token overhead.

### 3. Caution under uncertainty

The stale-read arm highlights the limits of quantitative monitoring. All write operations committed successfully to the primary database, but 18 subsequent read operations fetched outdated state from the lagging replica.

When the agent closed a ticket and re-read its status, the record appeared open. When it processed an invoice refund and re-read the balance, the refund appeared unapplied.

Token usage increased by 22% (below the 37% alert threshold), tool calls increased by 5% (below the 7% threshold), and scope drift reached 0.133 (below the 0.135 threshold). Every quantitative metric remained completely green.

```


Stale Read Execution Flow:
Write to Primary (Success) ──► Read from Replica (Stale Data Returned)
                                          │
                                          ▼
                        Agent Analyzes Discrepancy
                                          │
                                          ▼
                      Agent Suppresses Retries &amp; Logs Warning


```

However, the agent’s final text summary explicitly detailed the anomaly. It reported that none of its 19 writes could be verified via read-backs, systematically laid out the evidence for each task, and explained that it deliberately suppressed retries for refunds, comments, messages, and uploads to avoid double-applying mutations.

> “Its defensive caution successfully contained the fault, but simultaneously rendered a severe infrastructure issue invisible to quantitative monitoring.”

Had the agent blindly retried those operations, it would have generated duplicate refunds and triggered production alerts. Its defensive caution successfully contained the fault, but simultaneously rendered a severe infrastructure issue invisible to quantitative monitoring. The sole indicator of failure existed inside the prose summary.

## Token usage is a noisy metric

Token consumption was the single metric already tracked across every run, yet it proved almost useless for anomaly detection. Baseline token usage fluctuated by 18% across three identical runs, forcing a wide ±37% detection threshold. Consequently, the +26% token surge from the flaky API arm and the +36% surge from the model swap both slipped beneath the alert line undetected.

By contrast, tool-call volume varied by only 3% across the same baseline runs, enabling a tight ±7% detection threshold that easily flagged the 70% surge in API calls. Teams alerting on execution costs should track tool-call volume rather than raw token counts.

## The degradation of adversarial test sets

Adversarial test cases measure specific vulnerabilities in specific model generations. The refund traps successfully differentiated model capabilities in September, but caught zero errors in October because every tested arm—including standalone runs on the smaller model—declined the unauthorized actions.

Two variables shifted between test runs: the underlying model updated, and the launch prompt wording changed slightly. (The September transcripts needed to reconstruct the exact original prompt were cleared from temporary storage before analysis.) However, isolated reruns conclusively ruled out queue positioning as a factor.

## Recommended monitoring stack for production agents

To effectively [monitor autonomous agents](https://thenewstack.io/ai-agent-runtime-observability/), track these four telemetry layers:

* **Log the resolved model ID on every run:** Treat any shift in the returned model string as an active production deployment.
* **Track tool calls per verified task against a replicated baseline:** Measure call volume alongside task completion. In the flaky API test, tool calls surged 70% above the 58-call baseline despite a stable 19/19 completion rate, surfacing 31 hidden transient errors.
* **Isolate transient errors and retry attempts into explicit metrics:** Track retries directly; they’re an early-warning indicator of infrastructure degradation that the agent is actively paying to mask.
* **Parse final agent summaries for explicit statements of uncertainty:** Treat final agent reports as structured telemetry rather than plain text output. In the stale-read test, the summary contained the only indicator of system failure.
* **Rotate adversarial test sets whenever the underlying model updates:** Existing test suites measure the limitations of previous model iterations. When a model updates, update the adversarial evaluations accordingly.

## Validating your monitoring controls

To evaluate your telemetry layer, execute your agent’s unmodified baseline three times across identical tasks and calculate two variance metrics: tokens per task and tool calls per task. Expect the tool-call variance to be significantly tighter than the token variance (my test runs yielded 3% and 18%, respectively).

Next, inject transient failures into 25% of upstream network calls and execute the suite again. If your agent is appropriately resilient, overall task completion will remain stable while total tool calls roughly double. If task completion drops immediately, the agent’s retry logic requires improvement.

Running this benchmark reveals which telemetry layers can detect production degradation—providing the visibility needed to catch silent failures before an unannounced model swap forces an investigation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/09/fd4e9ea3-kayode-scaled-600x600.jpg)

Kayode is an innovative Software Engineer with 13+ years of experience building products that matter. His primary tech stack includes Rust, Python, and JavaScript, with strong expertise in PHP. He works across the full stack, from mobile apps with Flutter...

Read more from Kayode Ojo](https://thenewstack.io/author/kayode-ojo/)