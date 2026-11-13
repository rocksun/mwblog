![Abstract 3D digital visualization of glowing red and cyan network nodes and telemetry waveforms representing AI incident triage.](https://cdn.thenewstack.io/media/2026/11/16ba7ed5-getty-images-8pwk-ctbm2y-unsplash-1024x670.jpg)

**We’re a team of five engineers, and we used to wake the on-call engineer** three or four times a week over production incidents. Most were noise rather than serious outages, but at two in the morning, being overly cautious seemed preferable to letting a genuine problem slip through the cracks.

We’ve since reduced both unnecessary overnight interruptions and recurring issues by iterating on triage and following investigations through to fixes. [Specialized AI agents](https://thenewstack.io/durable-ai-agent-operations/) help us investigate incidents, organize follow-up work, and prepare changes, with engineers reviewing and correcting the work along the way.

What surprised us was how much more comfortable we became relying on the process. Engineers could inspect an assessment, challenge its assumptions, and use those corrections to improve how we handled later incidents. As follow-up fixes addressed recurring issues, we felt more confident about when to wake the on-call engineer.

That experience has made us question the shape of the work we give our agents. A [capable coding agent](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/) could potentially investigate an incident, raise a ticket, and prepare a fix, so why divide those responsibilities?

> “When an agent’s work needs correction, can you identify the responsibility involved and make a change you can evaluate independently?”

For us, it’s about improving one part of the workflow and judging whether the change helped. When an agent’s work needs correction, can you identify the responsibility involved and make a change you can evaluate independently?

## A shared workspace for people and agents

We’re building [Sugabots](https://sugabots.ai) as an open-source, self-hosted workspace where a team can work with several agents on the same task. Engineers can ask questions, contribute evidence, review findings, and bring in another agent, with those exchanges available to other participants.

We organize that work into shared environments called pods, with connections to [external systems through MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/). Each agent can have its own model and instructions, while the pod’s connections and tool policies define the access its agents share. The team can configure agents for specific responsibilities and refine their instructions as engineers review the work. Our incident workflow has helped us explore which responsibilities benefit from that separation.

## How we run incident triage in Sugabots

Our incident workflow depends on each engineer or agent being able to continue from the evidence, decisions, and corrections recorded during the investigation.

Our Sentry triage agent investigates new, regressed, or escalating issues and decides whether to [alert the on-call engineer](https://thenewstack.io/ai-sre-agent-autonomy-phases/), request an in-hours review, hand a small fix directly to an implementation agent, or keep the issue in Sentry for monitoring. It records follow-up work in Linear, where a backlog agent helps organize tickets, and the implementation agent can prepare a GitHub pull request for review.

![Workflow diagram of incident triage in Sugabots](https://cdn.thenewstack.io/media/2026/11/a2056af1-image1.png)

*Our incident workflow: agents handle distinct responsibilities while engineers contribute to the shared investigation. Engineers can take on any of the contributions shown.*

Engineers participate throughout, reviewing findings, challenging urgency assessments, correcting assumptions, and deciding whether to ship a proposed change. The investigation remains available as work moves between people and agents.

Safeguards back that growing confidence. The instructions call for urgent escalation when an issue could plausibly be a production outage, and urgency is uncertain. Issues classified as noise are archived until escalating, and Sentry retains a direct spike-alert route to incident.io as a backup.

The follow-up matters as much as the initial assessment. Previously, the on-call engineer might investigate an alert, determine it could wait until office hours, and return to other work. Recording the underlying problem in the backlog and prioritizing it gave the team a chance to resolve it before the next on-call engineer encountered the same alert.

Having the backlog agent record follow-up work in Linear gives the team a consistent way to prioritize fixes for the recurring issues behind the interruptions.

## Specialize around a decision

We configure each agent for a particular responsibility, choosing its model and instructions to suit the work and defining what a useful result looks like.

We chose Opus 5.5 for Sentry triage, and its instructions cover evidence gathering, classification, escalation, handoffs, and recovery from tool failures. This abbreviated excerpt shows the decisions we ask it to make:

Inspect the full Sentry issue, including customer impact, affected users, release, and event trend, then check for existing tickets or incidents.

Choose an outcome:

* **Urgent:** active customer harm requiring immediate attention; alert the on-call engineer through incident.io.
* **In-hours review:** a defect requiring engineering judgment that can wait; notify the on-call engineer at low urgency.
* **Auto-fix:** a small, non-urgent code change outside restricted areas such as authentication, billing, and migrations; brief the implementation agent to prepare a PR.
* **No action:** expected or transient noise; archive until escalating so a spike brings it back.

State the evidence and uncertainty behind the decision. Implementation briefs must stand alone and include the relevant findings and links.

The backlog manager’s instructions reflect the decisions involved in organizing follow-up work: checking for duplicates, looking up the current Linear cycle, and distinguishing actionable work from issues that need an engineer to clarify scope or make a design decision. Those rules provide defaults while preserving the team’s explicit choices about priority, assignment, and scheduling, and we can refine them independently of the criteria used to assess an incident’s urgency.

Triage and implementation make a useful comparison. Triage asks whether the available evidence justifies interrupting an engineer. Implementation asks what change would resolve the problem and how to verify it. Those decisions have different failure modes: a missed urgent incident, an unnecessary interruption, or a plausible fix that introduces another bug.

> “Triage asks whether the available evidence justifies interrupting an engineer. Implementation asks what change would resolve the problem and how to verify it. Those decisions have different failure modes.”

We’ve found it useful to maintain those responsibilities separately because we can refine how incidents are classified while keeping the implementation instructions stable. If an investigation leads to an ineffective fix, we can examine the assessment’s accuracy, the evidence preserved in the ticket, and how the implementation addressed the recorded problem. Each gives us a specific part of the workflow to improve.

Each responsibility also gives us concrete questions to evaluate:

* **Triage:** Did it escalate genuinely urgent incidents? Did it unnecessarily interrupt an engineer?
* **Backlog management:** Did it record the follow-up work, recognize existing tickets, and preserve enough evidence to act on it?
* **Implementation:** Did the proposed change address the problem, and what did an engineer need to correct before accepting it?

We need to evaluate the reduction in wake-up calls alongside how we handle genuinely urgent incidents, including any that triage missed. Fewer interruptions could reflect both better classification and fixes that reduce the volume of incidents arriving. Those outcomes help us judge how the workflow is performing and where to improve it.

The same question applies to the agents already in your workflow: when their output improves, can you explain what improved and what evidence supports that judgment? Separating responsibilities gives you a narrower decision to examine and a clearer basis for evaluating changes.

## Match permissions to responsibilities

Separating responsibilities also helps us decide which tool actions each agent needs and when an engineer should approve them.

Our triage instructions include specific write actions: creating Linear issues, sending alerts through incident.io, and archiving Sentry issues until escalating. Tool access needs to reflect those responsibilities, including which actions require an engineer’s approval.

Agent-specific instructions define responsibilities within the access available to the pod; they do not enforce separate permissions for agents sharing that pod.

In Sugabots, the team configures tool-level Off, Ask, and Allow policies on a pod’s connections, and every agent in that pod inherits those policies. Configuring them once gives the team a consistent set of rules for automatic actions, engineer approvals, and disabled tools, including when another agent joins the work.

Triage needs access to evidence and a way to escalate, while implementation needs enough access to prepare a change. Genuinely different access boundaries require separate enforcement, potentially through different pods with different tool policies or appropriately scoped connections. Merge and deployment authority also need explicit policies and, where available, appropriately scoped credentials.

## Separate the working context from the investigation

There are three things here with different useful lifetimes:

* **Configuration:** the maintained model, instructions, tools, and expectations for a responsibility.
* **Execution context:** the messages and tool results available to the model while it works on a particular task.
* **Shared history:** the record of evidence, hypotheses, corrections, and decisions that people and agents accumulate.

Consider an investigation where the agent rules out an outage and concludes that an issue can wait until office hours. After enough tool calls, its context may need to be compacted. A summary might preserve the conclusion while omitting the evidence that ruled out the outage.

That detail becomes important if an engineer challenges the assessment. Keeping the original history gives them a way to inspect the reasoning and evidence behind the summary. The agent can work with a compacted context while the fuller record remains available for inspection or retrieval.

To continue the investigation, the next agent needs the relevant evidence and corrections selected from that record and passed along in a brief, or retrieved as it works. Preserving the conversation gives us a source to draw from; selecting the working context remains an explicit part of the handover.

## Keep people in the investigation

The same distinction matters when work moves between engineers. An engineer may recognize a pattern the agent missed or explain why an apparently sensible fix would introduce a regression elsewhere in the codebase. That contribution needs to remain available to the engineer or agent continuing the investigation or preparing the fix.

In separate chats, people become responsible for carrying those corrections across. Even when both agents can inspect the same repository and tickets, each conversation contains a different account of what the team has learned.

![Diagram showing the reviewer and author relaying findings between their separate chats.](https://cdn.thenewstack.io/media/2026/11/b70aaf1b-image3.png)

*The reviewer and author relay findings and corrections between their separate chats.*

In Sugabots, engineers can contribute to the shared discussion, leaving their corrections alongside the findings that prompted them. The next engineer can see how the investigation changed direction, and an agent continuing the work can receive that correction with its brief.

![Diagram showing engineers and agents contributing to a shared discussion.](https://cdn.thenewstack.io/media/2026/11/b9bafbeb-image2.png)

*Engineers and agents contribute to a shared discussion that preserves their findings and corrections.*

**MCP gives the agent access to evidence, while a shared workspace gives the team access to the investigation.**

![Screenshot of a staged Sentry triage conversation in the Sugabots interface.](https://cdn.thenewstack.io/media/2026/11/50be6f13-image4-1024x640.png)

*A staged Sentry triage conversation rendered in the actual Sugabots interface. The messages, event counts, issue reference, and handoff are scripted demonstration data, showing how an engineer’s correction can remain alongside the assessment and implementation brief.*

## When is another specialist worth it?

Each additional specialist brings configuration to maintain and a handover whose context needs care. Splitting agents by language, service, or deployment environment is useful when that boundary helps the team maintain and evaluate the work.

Our current divisions follow responsibilities that already existed: the on-call engineer assessed urgency, the team organized follow-up work in the backlog, and engineers prepared and reviewed fixes. Giving agents distinct configurations for those responsibilities lets us improve each part of the workflow independently.

For a team trying this, I’d start with one recurring responsibility where you can describe a useful result and recognize a bad one. Write down the success criteria, including the errors that matter: for triage, that means examining missed urgent incidents as well as unnecessary escalations. Define the evidence the agent needs, choose a configuration that enforces the required tool access, and specify when an engineer should review its findings or approve an action.

Keep the investigation history, including the evidence behind decisions and the corrections engineers make, so the next engineer or agent can continue from it. Review those corrections to decide whether the instructions, available evidence, permissions, or handover need to change. Earlier investigations can then provide cases to revisit alongside new work, checking whether a change addresses the original mistake without introducing another.

> “Increasingly, I’m interested in whether we can define an engineering responsibility clearly enough that every investigation, correction, and reviewed fix helps us improve how we handle the next one.”

That may justify a dedicated agent, or it may be enough to load a reusable configuration when the job appears. The question is whether the separation makes the work easier to maintain and evaluate.

We started by wondering whether we should specialize our agents. Increasingly, I’m interested in whether we can define an engineering responsibility clearly enough that every investigation, correction, and reviewed fix helps us improve how we handle the next one.

## Try Sugabots

If you’d like to try this approach with your team, [Sugabots](https://sugabots.ai) is open source and self-hosted. Start with one recurring engineering task and a colleague who can review the agent’s work, then use the shared discussion and corrections to refine how it handles that responsibility.

If the project looks useful, [give Sugabots a star on GitHub](https://github.com/nitrictech/sugabots) and share it with a team that might benefit. Stars and recommendations go a long way in helping an open-source project reach the engineers who could use it or contribute to it.

The post [Why Nitric stopped asking one AI agent to do everything](https://thenewstack.io/specialized-ai-agent-workflows/) appeared first on [The New Stack](https://thenewstack.io).