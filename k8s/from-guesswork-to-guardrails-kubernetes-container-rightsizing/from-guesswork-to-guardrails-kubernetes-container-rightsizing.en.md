In a Kubernetes cluster, CPU and memory requests are both a cost dial and a reliability dial. They’re how you tell the scheduler what a pod “needs,” and they’re what node autoscalers and [horizontal pod autoscalers (HPAs)](https://thenewstack.io/getting-started-with-kubernetes-autoscaling/) react to when deciding whether to add capacity or replicas.

The problem is that requests drift. They get set during early development or a past traffic shape, then workloads evolve, and the numbers don’t. Nobody wants to hand-tune requests forever, but a cost tool rewriting resources at the wrong time can be worse. As a result, rightsizing is clearly valuable, but hard to run continuously across a mixed production cluster without guardrails.

## What Container Rightsizing Is and Why It Pays Off

[Container](https://thenewstack.io/introduction-to-containers/) rightsizing is the practice of adjusting CPU and memory requests (and, where appropriate, limits) so they match real usage instead of historical guesses. When requests are inflated, Kubernetes reserves capacity that never gets touched. You lose pod density, the scheduler runs out of “room” sooner than it should, and the cluster scales out to satisfy declared demand rather than actual load.

That translates into more nodes and often larger instance types, because smaller nodes can’t fit the shapes you’ve asked for. In bigger environments, a few oversized “whale” containers can even push upstream infrastructure changes — extra node pools, larger subnets, more VPC/IP headroom — only to host capacity that sits idle. Rightsizing pulls that baseline back toward reality so packing improves, node growth slows and autoscalers operate on clean signals instead of sizing debt.

## Where to Start: Custom Approaches vs. a Managed Path

If you want to do this with native tooling, the usual on-ramp is Vertical Pod Autoscaler (VPA). In recommendation mode, VPA gives you per-container [request suggestions based on observed CPU and memory history](https://thenewstack.io/stop-setting-cpu-and-memory-requests-in-kubernetes/). Some teams periodically review those numbers and apply them through GitOps diffs; others pair VPA with open source rightsizers that generate pull requests (PRs) or YAML patches. A more DIY route is to scrape metrics from Prometheus, compute new requests in a script, and apply them on a cron, often with a human in the loop to approve changes for sensitive namespaces. These approaches are legitimate ways to get first savings, and they’re often enough for low-risk services or predictable batch workloads.

The gap shows up at scale. VPA and most OSS tools focus on *what* to change, but they don’t handle *when* to apply updates, *which* workloads are safe to touch automatically or *how* to avoid collisions with rollouts and autoscalers.

Out-of-the-box production-ready scheduling tools like nOps build on the same underlying idea as VPA (usage-based recommendations) but layer in scheduling plus guardrails so updates happen only in approved windows. These tools also keep rollback and action history attached to each resize, which is the part teams otherwise end up wiring themselves once they try to run rightsizing broadly in production.

## Workload and Container Rightsizing Patterns

Scheduling only makes sense once you know what kind of workload you’re sizing, with different workloads requiring different request baselines and different timing for applying changes. The table below is a quick pattern map to ground those differences before we move into the mechanics of scheduling strategy.

|  |  |  |
| --- | --- | --- |
| **Pattern** | **Characteristics** | **Sizing Approach** |
| **Steady workload** | Consistent CPU/memory usage | Use *P90 or P95 usage* for requests. Keep limits close. |
| **Spike-driven bursty services** (APIs, frontends) | Idle most of the time, sudden peaks | Use P50/P70 for requests + HPA for bursts. Higher CPU limits. |
| **Gradual growth** (CRON, workers, streaming) | Memory creeps up over time (leak/states) | Use peak memory → request = peak + 10–20%. Add alerts on sustained growth. |
| **Idle daemons / sidecars** | Low constant usage but large reserved footprint | Rightsize aggressively or merge/remove sidecars. |
| **Short-lived jobs / batch** | CPU bursty, memory predictable at start | Base sizing on container max usage. Consider resource QoS: BestEffort/Burstable. |
| **Unknown new workloads** | No baseline | Start high → measure → tune downward iteratively. |

## Rightsizing Based on the Workloads

Rightsizing across these patterns is clearly useful, but it also surfaces real hesitations and frictions about changing requests all the time in a live cluster and how they line up with rollouts, on-call and other controls they already trust.

Once recommendations exist, the timing of execution matters as much as the sizing itself. Scheduling allows you to define times and scopes where rightsizing is allowed to act, and everything outside that stays observation-only. It comes down to three practical choices: when to apply changes, when to block them and whether to run different configs for peak vs. off-peak. The strategies below are the common production defaults.

### 1. Rightsize Only on Weekends / Off-Peak Hours

Workloads behave differently at 2 p.m. on Tuesday than at 3 a.m. Saturday, so a common safe default is to apply rightsizing only in low-traffic windows. That pushes pod restarts and any autoscaler side effects into periods with minimal blast radius and leaves time to verify stability before peak load returns.

For example, teams can start with a weekend block (such as Sat 00:00–Sun 06:00 local time) or the cluster’s measured lowest-traffic hours.

There are a few standard ways to enforce that off-peak gate:

* **Argo CD/Flux scheduled GitOps sync:** Rightsizing recommendations become normal YAML/overlay updates, but Argo/Flux is set to sync those diffs only during the window so changes stay reviewable, and Git remains the source of truth.
* **Kubernetes CronJob + Kustomize/Helm patching:** A CronJob runs only in the window, pulls the latest recommendations and patches requests directly — a lightweight cluster-native batching mechanism without a GitOps gate.
* **Scheduled rightsizer automation:** The rightsizer keeps computing recommendations continuously but enforces the apply window internally, handling targeting and rollback in the same system instead of wiring that control layer yourself.

### 2. Freeze Rightsizing During Business Hours

This approach is the inverse of off-peak batching: Keep producing recommendations, but block any [request/limit](https://thenewstack.io/how-kubernetes-memory-requests-and-limits-actually-work/) writes during peak hours. The point is to avoid resizing-driven restarts or autoscaler ratio shifts when user traffic and rollout activity are highest.

A common starting rule is a weekday deny window (for example, Mon–Fri, 8 a.m.–6 p.m. local cluster time), often applied only to latency-sensitive namespaces.

|  |  |
| --- | --- |
| **Business-hour risk** | **Why it matters** |
| Traffic and load higher | Any restart or reschedule has immediate user impact. |
| Error detection harder | Peak variability makes resize regressions harder to spot quickly. |
| SRE/infra less available | Longer rollback loops raise the cost of a bad change. |

The practical invariant is simple: Outside the allowed window, rightsizing can observe and recommend, but it doesn’t apply.

### 3. Automatic Rollback During Peak Hours

This strategy assumes you don’t want one “forever” request baseline. Instead, you run an optimized baseline off-peak, then roll back to a known conservative baseline for peak hours. It’s the middle ground between continuous tuning and a full freeze. You still capture savings regularly, but you avoid carrying fresh, potentially aggressive requests into the busiest part of the day, which matters most for services with unpredictable peak behavior.

In practice the schedule is straightforward: Apply the latest recommendations at night or on weekends, then restore the prior “safe” configuration before traffic ramps.

This fits best for workloads that have a reliable quiet window but spiky or hard-to-predict peaks, where you want the cost wins off-peak without betting peak reliability on newly computed requests. Mechanically, rollback is just a scheduled profile switch typically done by flipping between “optimized” and “baseline” GitOps overlays, a CronJob that restores baseline requests at window close or a rightsizer that supports scheduled rollback.

## Results and Validation

Once scheduling and safeguards are in place, the final step is proving that rightsizing made the system better. Results typically fall across three dimensions: cost, reliability and operations.

|  |  |  |
| --- | --- | --- |
| **Dimension** | **Example Metrics** | **Purpose** |
| **Cost** | Rightsized %, $/service/day, utilization delta | Quantifies efficiency gains and distinguishes sustained savings from short-term noise. |
| **Reliability** | SLO burn rate, latency p95/p99, OOMKill frequency, autoscaler thrash | Confirms that optimization didn’t create regressions or trigger scaling churn. |
| **Operations** | Time-to-revert, diff-to-deploy duration, automation success rate | Measures how consistently rightsizing executes and recovers across scheduled windows. |

To interpret results accurately, compare identical workload periods — same weekday and hour — to remove natural traffic variance. When reversibility is automatic and regressions trigger immediate rollback, rightsizing becomes an auditable control loop, typically rerun every 30 to60 days.

## Scheduling in nOps: How It Maps to the Patterns Above

I’ve described scheduled rightsizing as a control layer on top of recommendation engines: pick eligible targets, define windows, and decide what “off-window” behavior should be.

My company [nOps](https://www.nops.io/compute-copilot/eks/) implements that model directly in its container and workload rightsizing features. The scheduling layer doesn’t change how recommendations are computed; it constrains when they can be applied and what happens outside the window. Recommendations continue to update from observed usage, but schedules gate when those updates are written back to requests/limits.

## Scope: What You Can Schedule

Scheduling in nOps can be applied at different scopes, depending on how your cluster is organized:

**Workload rightsizing schedules** target job-like or compute-heavy workloads (batch, ETL, analytics, Spark-style pipelines). The expectation is a predictable run/idle cycle, so schedules are typically aligned to those phases.

**Container rightsizing schedules** target long-running services and deployments where timing matters because resizes restart pods and affect autoscaler ratios.

In both cases, schedules are attached to explicit targets (clusters, namespaces, deployments, or container groups), rather than running clusterwide by default. That matches the “targeting the right workloads” approach described earlier.

Windows and Execution Behavior

A schedule defines one or more time windows where rightsizing is allowed to execute. Within a window, rightsizing can apply new requests/limits based on current recommendations. Outside a window, nOps supports two behaviors that correspond to the execution modes in this article:

* **Hold mode:** Configuration is kept fixed outside the window. Recommendations may continue to be computed, but no updates are pushed until the next scheduled run.
* **Rollback mode:** When the window closes, nOps restores the last known baseline configuration. This is intended for cases where you want temporary optimization during low-traffic periods but a predictable pre-peak baseline.

The important mechanical point is that the schedule governs application of changes, not just recommendation generation.

## Coordination With Scaling and Rollouts

Because rightsizing updates requests, it can change utilization ratios that horizontal pod autoscalers (HPAs) use and can trigger reschedules that node autoscalers respond to. Scheduling is the mechanism nOps uses to reduce those overlaps: You run resizes in windows that avoid rollout activity and autoscaler stabilization periods, and you keep critical services stable when traffic is high. That’s the same sequencing guardrail described in the “Performance and Conflict Handling” section.

## Adoption Path

A practical rollout looks like the staged approach outlined earlier:

1. Start with a narrow target (one namespace or a low-risk deployment class).
2. Set a conservative off-peak window.
3. Observe effects on restarts, latency and autoscaler behavior.
4. Expand targets or windows once results are stable.

nOps keeps a history of applied rightsizing actions, so teams can trace when schedules are executed and what they changed, which helps with verification and rollback decisions as rollout scope expands.

## The Bottom Line

Scheduled rightsizing is a way to make resource tuning behave like the rest of your production controls: scoped, time-bounded and reversible. Instead of treating CPU and memory baselines as something you revisit only when cost spikes or incidents hit, scheduling lets you keep them aligned with workload reality on a cadence that matches how each service runs. The net result is that you get the efficiency benefits of rightsizing without asking every workload to tolerate the same level of automation risk. Where continuous tuning is safe, let it run; where stability matters more, schedule conservatively; and where neither applies, leave the workload alone.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/47761f82-cropped-b90378d0-shouri-thallam.jpeg)

Shouri Thallam is a senior cloud optimization architect at nOps.io, specializing in AWS infrastructure and FinOps best practices. He holds multiple industry-leading certifications, including AWS Certified Solutions Architect (Professional), FinOps Certified Engineer, FinOps Certified Practitioner, Certified Kubernetes Application Developer and...

Read more from Shouri Thallam](https://thenewstack.io/author/shouri-thallam/)