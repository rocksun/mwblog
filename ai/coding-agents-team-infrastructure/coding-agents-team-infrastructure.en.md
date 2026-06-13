In the first week of June, three vendors pushed coding agents past the single-developer loop.

1. Cognition released [Devin Desktop](https://cognition.ai/blog/introducing-devin-desktop) on June 2.
2. The same day, Microsoft used Build 2026 to introduce [Rayfin](https://thenewstack.io/microsoft-build-2026-rayfin-replit-vibe-coding/).
3. And Augment Code announced [Cosmos](https://www.augmentcode.com/blog/cosmos-the-platform-for-ai-native-engineering-teams) for every team plan on June 3.

The three launches sit at different layers of the same emerging stack:

1. Devin Desktop gives a team a single console to manage them.
2. Rayfin governs which agent-built apps deploy into the enterprise.
3. Cosmos coordinates a fleet of agents.

Taken as a whole, the three mark a shift: The coding agent is becoming team infrastructure rather than a personal tool. It is a pattern is familiar to anyone who watched source control grow up.

Version control began as a private convenience on one workstation, and then Git and continuous integration turned it into shared infrastructure with branches, reviews, and policies the whole team answered to. Coding agents are making the same trip today. The reference points in this piece are the ones every engineering team already knows: The pull request, the CI pipeline, the access policy, and the control plane that ties them together.

## From a per-developer harness to a team one

A few weeks ago I argued that the [agentic coding tools have converged](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/), and that the contest had moved off the model and onto the harness, the workflow and approval layer wrapped around it. On public coding benchmarks such as [SWE-bench Verified](https://www.swebench.com/verified.html), the top systems now cluster closely enough that product differentiation increasingly comes from the harness, the planning step, the tool use, the review gate, and the path to production.

> The June launches break the one developer, one harness assumption.

That argument assumed one developer sitting at one harness. The June launches break the assumption by handing the harness to the whole team. A team harness has to do things a personal one never needed to. It has to remember decisions across people and sessions so the same naming convention does not get relitigated every Monday. It has to coordinate several agents working in parallel without stepping on each other. And it has to give a human somewhere to stand when judgment is required, the same role a reviewer plays on a pull request.

Think of it as the difference between a developer running scripts on a laptop and a team running those same jobs through a shared CI system with cached state and audit logs, where the accountability changes even when the work looks the same.

## Augment Cosmos, a control plane for the whole lifecycle

Cosmos, from [Augment Code](https://www.augmentcode.com/), attempts to sit above the agents that a team already runs and coordinate them across the software lifecycle. Augment describes agents that work across triage, spec, implementation, review, testing, deployment, and feedback, coordinating with one another and bringing in a human when judgment matters. Specialized agents share memory so what one learns does not die when its session ends.

The most fitting analogy is the CI/CD control plane. A pipeline does not write your code; it decides what runs, in what order, and what has to pass before a change ships. Cosmos plays that role for a fleet of agents, holding the shared context and the rules the agents operate under.

Consider an incident that pages an on-call engineer at 2 a.m. In Augment’s own incident-management story, a Cosmos agent has already picked up the alert, gathered context, and started investigating before the engineer joins, so the human reviews a head start rather than a blank page. The payoff here is shared memory and coordination, which allow the next agent to begin where the last one left off.

The so-called cold-start problem — where an agent has no context to work with — is the one Cosmos is built to attack. Agents are close to stateless between sessions, which is why a tool that wrote passable code in week one repeats the same mistakes in week twelve. A shared memory layer turns those scattered corrections into something the whole team reuses.

## Cognition Devin Desktop, the manager’s console

Devin Desktop comes at the same shift from the developer’s seat. [Cognition](https://cognition.ai/) calls it the next generation of Windsurf, and it makes an Agent Command Center the default surface of the IDE, so an engineer can manage local and cloud agents, pull requests, and context from one place. A feature called [Spaces](https://docs.devin.ai/desktop/spaces) lets related agents share context and collaborate on a task.

Cognition calls Devin Desktop agent-neutral. With support for the Agent Client Protocol (ACP), an open standard for agent interoperability, any ACP-compatible agent can run inside Devin Desktop alongside Devin, so a team could, in principle, drive Codex CLI on one task and a Claude-based agent on another from the same board. That neutrality runs through ACP adapters, not native hooks into every commercial Codex or Claude surface. It still matters because most teams already run a mix, and nobody wants a console that manages a single vendor’s agent.

Picture a tech lead carving a backlog into eight tickets on a Friday, handing each to a different agent, and spending Monday reviewing eight pull requests instead of writing the code by hand. Devin Desktop is built for that working day, with the full editor still there for the last-mile edit a human has to make. Where Cosmos leans toward an opinionated platform, Devin Desktop reads as a dashboard that respects the agents you have already chosen.

## Microsoft Rayfin, governance for what agents ship

Rayfin moves along a different axis. Rather than managing agents, it narrows the path for one thing agents increasingly produce, the application backend, and routes it into a governed home. Announced at Build 2026, Rayfin is an open-source SDK and CLI that lets developers and coding agents define a full application backend in code, the data models, business logic, authentication, and access policies, then deploy it to Microsoft Fabric.

Once an app lands in Fabric, it inherits the security, compliance, and governance the organization already runs, and its data sits in OneLake rather than in a fresh silo. Replit is the launch partner, so an agent in Replit can define the backend and ship it into a governed tenant. The problem Microsoft is naming is real. Agentic coding tools spin up applications faster than anyone can govern them, and each ungoverned app is another data island outside the controls that auditors care about.

The analogy from platform engineering is the paved road, the supported path that makes the compliant way the easy way. Rayfin is trying to be the paved road for agent-built backends, so an app arrives in production already within the data estate rather than being bolted on after a security review. This is org-level control of output rather than coordination of work, which is why it widens the story rather than repeating it. Rayfin is in preview, the Replit pairing is the first integration rather than a broad one, and the governance depth will become clearer as the preview runs.

## Where each platform fits

The three launches answer different questions, so the choice depends on which problem an engineering organization feels most strongly about first.

> A team drowning in agent-generated pull requests has a coordination problem. A team running five different agents has a management problem. A team whose agents keep deploying ungoverned apps has a control problem.

A team drowning in agent-generated pull requests has a coordination problem. A team running five different agents has a management problem. A team whose agents keep deploying ungoverned apps has a control problem. The table below maps each need to the platform built for it, along with the associated trade-offs.

| Scenario | Best-suited platform | Rationale and tradeoff |
| --- | --- | --- |
| Coordinating many agents across the full lifecycle with shared memory | Augment Cosmos | Built as a lifecycle control plane, heavier and enterprise-leaning |
| Managing a mix of third-party agents from one console | Cognition Devin Desktop | Agent-neutral via ACP, still an IDE-centric surface |
| Governing what agent-built apps deploy into the data estate | Microsoft Rayfin | Inherits Fabric governance, Fabric-bound and in preview |
| A solo developer who needs inline edits and autocomplete | The existing per-developer tools | None of these team layers earns its weight for one person |

In practice, the categories start to blur together. A large engineering organization could run Cosmos for coordination, manage some third-party agents via Devin Desktop, and still route agent-built apps through a governed backend such as Rayfin. These are layers, not alternatives, and most teams will end up holding more than one.

## The cost of remembering

Team memory is as much a security and governance surface as it is a productivity feature.

> The same layer that makes agents useful across an organization is the layer where lock-in hardens, because the context a company accumulates is far harder to move than the agent that reads it.

Once agents carry conventions, incident history, customer context, credentials, architectural decisions, and review feedback across sessions, a buyer has to ask where that memory lives, who can inspect it, how it gets revoked, and whether it leaves with the team when a contract ends. The same layer that makes agents useful across an organization is the layer where lock-in hardens, because the context a company accumulates is far harder to move than the agent that reads it.

## What’s next

For an engineering team, the reference points stay familiar. Cosmos serves as a CI control plane for agents, Devin Desktop functions as an operations console for a fleet, and Rayfin acts as the paved road that keeps output within the guardrails. The shift underneath all three is that the agent stops being a personal productivity tool and becomes something an organization defines policy around, the way it already does for source control and deployment.

For a buyer, the deciding factor is which platform hosts the team’s agents, the memories they share, and the approvals they record. If a standard like the Agent Client Protocol keeps that management layer portable, teams will assemble their own agent fleets across vendors. If it does not, the agentic SDLC hardens into rival control planes, each with its own memory, permissions, and path to production. GitHub and Cursor are already shaping their answers, and the open question for the next piece is whether this team layer converges on a single shape, as the single-player tools did, or splinters.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)