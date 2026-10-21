**Kubernetes has always relied on agents**, just not the kind dominating today’s AI conversations. A controller watches the current state, compares it with a declared desired state, and takes action to close the gap. That resemblance makes [AI agents and Kubernetes](https://thenewstack.io/agentic-ai-kubernetes-management/) operators sound interchangeable. They are not.

This question is no longer theoretical. Over the past 18 months, agent tooling has moved from a side project to part of the cloud-native stack. CNCF has accepted agent frameworks into its Sandbox, and Kubernetes SIG Apps has taken on Agent Sandbox as a subproject for [running agent workloads safely](https://thenewstack.io/securing-kubernetes-ai-agents/).

Platform teams are already deciding what an agent can change in a live cluster, usually one pull request at a time and without a written policy. By default, the boundary between reasoning and execution is set by convention rather than design.

---

***KubeCon + CloudNativeCon takes place in Salt Lake City, Utah, November 9 to 12.* [Register now](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)*!***

---

A Kubernetes operator is designed to be predictable. It reconciles resources according to encoded rules, retries failed operations, and converges on declared state. An AI agent is useful when the desired outcome is clear but the path isn’t. It can investigate an unfamiliar situation, gather context from several systems, weigh tradeoffs, and propose a course of action.

A safer architectural pattern combines these strengths. The agent supplies reasoning and context. Operators, policy engines, and other deterministic systems retain control of execution.

## A reasoning layer for Kubernetes

![Workflow diagram illustrating how agents add reasoning while Kubernetes operators keep control out of the cluster.](https://cdn.thenewstack.io/media/2026/10/8319c569-figure1-shelby-brittain.png)





*Click to enlarge graphic.*

[kagent, an open source CNCF Sandbox project](https://kagent.dev/docs/kagent/introduction/what-is-kagent/), provides a concrete example of this pattern. It runs AI agents as Kubernetes resources and connects them to Kubernetes, Helm, observability, and custom tools. An agent can inspect resources, retrieve logs and events, query metrics, consult documentation, and coordinate specialized agents.

That does not mean every tool should be freely executable. Non-sensitive read operations can run automatically, while changes such as applying, patching, or deleting resources can [require explicit approval](https://kagent.dev/docs/kagent/examples/human-in-the-loop/). This separation lets the agent conduct a broad investigation without giving an uncertain reasoning process unrestricted authority over the cluster.

> “This separation lets the agent conduct a broad investigation without giving an uncertain reasoning process unrestricted authority over the cluster.”

The resulting operational loop looks like this: observe, diagnose, propose, approve, reconcile, and verify. The first three steps benefit from agentic reasoning. Kubernetes and its operators handle the reconciliation step. Verification closes the loop without assuming that a successfully accepted change produced the intended result.

## Karpenter shows the difference

Consider a cluster where [Karpenter provisions capacity](https://thenewstack.io/self-healing-gpu-nodes/) successfully, but the platform team still sees underutilized nodes, slow consolidation, Spot churn, or pending pods. Karpenter itself is already an operator. It evaluates scheduling constraints and reconciles NodePools and NodeClaims. Replacing that logic with an LLM would make a reliable control loop less predictable.

A kagent-based operations agent should work above Karpenter instead. It can inspect NodePool and EC2NodeClass (for EKS clusters) configuration, pending pods, Kubernetes events, Pod Disruption Budgets, Karpenter logs, and relevant Prometheus metrics. It can then ask why the observed behavior differs from the team’s goal.

![Diagram illustrating a bounded Karpenter improvement loop.](https://cdn.thenewstack.io/media/2026/10/57718106-figure2-shelby-brittain.png)





*Click to enlarge graphic.*

The investigation might find that a [Pod Disruption Budget is blocking consolidation](https://karpenter.sh/docs/concepts/disruption/), a do-not-disrupt annotation is keeping a node in place, or a disruption budget is preventing eviction. It might find that consolidateAfter is too aggressive for a bursty workload, producing avoidable churn. It could also identify instance constraints that leave Karpenter with too little flexibility when selecting Spot capacity.

> “Karpenter itself is already an operator. Replacing that logic with an LLM would make a reliable control loop less predictable.”

The agent’s output should not be a vague recommendation such as “optimize the NodePool.” It should present the evidence, identify the tradeoff, and produce a narrow configuration patch. A change to a NodePool disruption budget should explain the maximum number of nodes that could be affected. A consolidation change should state how long the team will observe workload stability. An expansion of instance choices should preserve architectural, availability-zone, and workload constraints.

The patch then passes through an approval or policy gate. Once approved, Karpenter reconciles using its existing scheduling and disruption logic. The agent watches the result over a defined period and checks whether consolidation improved without increasing pending-pod latency or harmful disruption. If it doesn’t meet the acceptance criteria, the system can recommend or initiate a rollback through the same controlled path.

## Argo CD applies the upgrade. The agent builds the case.

Consider a platform team upgrading a Helm chart managed by Argo CD. Changing the chart version in Git is straightforward. Understanding how that change will affect a running application takes more work. Argo CD can show which resources differ; an agent can help explain what those differences mean for the workload.

For example, a new chart version might rename a value that the team uses to configure its readiness probe. The agent can compare release notes, existing values, and rendered manifests to identify whether the upgrade would silently fall back to a default. It should turn that finding into a focused pull request that updates the chart version and affected values, explains the operational risk, and defines the checks required before rollout.

Once the pull request passes review and is merged, Argo CD renders the chart and synchronizes the resulting manifests under the application’s configured sync policy. The agent then checks Argo CD’s sync and health status alongside application metrics. A successful sync alone does not establish that the upgrade preserved latency, error rates, or availability.

If those checks fail, the agent can propose a Git revert or a recovery plan through the same approval process, accounting for any data or schema changes that a revert cannot undo. The division of responsibility stays clear: the agent investigates, proposes, and verifies; Argo CD reconciles the approved desired state.

## Autonomy should be earned

Teams can introduce this model progressively. Start with a read-only investigator. Next, allow the agent to generate patches or pull requests. Then permit approved, low-risk changes with explicit scope and rollback conditions. Only well-understood actions with measurable outcomes should become autonomous.

> “The important boundary is not whether an agent can call kubectl, Helm, or a cloud API. It is whether every action is authorized, bounded, observable, and reversible.”

The important boundary is not whether an agent can call kubectl, Helm, or a cloud API. It is whether every action is authorized, bounded, observable, and reversible.

Kubernetes can run agents that help manage Kubernetes, but only when each component keeps the job it is best equipped to perform. Agents reason about uncertain situations, operators reconcile declared state, and policy sets limits on both. Humans remain accountable for how quickly the system can move from recommendation to autonomy.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/2f802a33-vikram-seshadri-headshot-shelby-brittain.jpg)

Vikram Seshadri spent eight years in platform engineering in the fintech space, including a stint as Senior Vice President leading EKS platform engineering at Citi. Now a Senior Evangelist for Enterprise Platforms at DoiT, he helps engineering teams solve the...

Read more from Vikram Seshadri](https://thenewstack.io/author/vikram-seshadri/)