**OpenAI opened its** [**Agents API in public beta**](https://thenewstack.io/openai-agents-api-compute/) **this month**, exposing the harness that powers Codex with managed sessions, tool coordination, and subagent orchestration. On the same day, September 10, Cursor [launched Projects](https://cursor.com/blog/projects) to coordinate multiple coding agents around larger bodies of software work. While the products sit at different points in the stack, both converge on the same architecture: a coordinator understands the larger objective and manages the work, while specialized agents execute individual pieces.

That pattern isn’t new: AWS [Bedrock AgentCore reached general availability](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available) in October 2025, and Anthropic’s [Claude Managed Agents entered public beta](https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html) in April 2026. What makes these announcements notable is that two major players in AI-assisted software development are independently exposing the same coordinator-worker split at the same time.

[Hilliary Lipsig](https://www.linkedin.com/in/hilliary-lipsig-a5935245/), a senior principal site reliability engineer at Red Hat who leads Azure Red Hat OpenShift SRE teams and hosts the YouTube livestream [*GitOps Guide to the Galaxy*](https://www.youtube.com/playlist?list=PLbMP1JcGBmSGKO8UreWpOBOhCqilejhtd), has watched this dynamic play out firsthand.

“This convergence highlights the reality developers across the industry have been discussing on and offline — an agent with too much context loses accuracy and reliability, and focused work with clearer contexts allows for faster, more accurate iterations,” Lipsig tells *The New Stack*.

“The need for orchestration in distributed computing has been fundamentally recognized repeatedly,” Lipsig says. “That’s part of how we got to [Kubernetes](https://thenewstack.io/kubernetes/). These multi-agent workflows are the same concept, just in a new part of the technical stack. While the specialized agents do their area of work, the orchestrator can act as a source of truth — ideally enforcing guardrails, recovering from any failure states, and intelligently routing work to the most efficient target agent.”

> “The need for orchestration in distributed computing has been fundamentally recognized repeatedly… These multi-agent workflows are the same concept, just in a new part of the technical stack.”

The industry has spent the first generation of AI coding tools asking how capable a model can become at writing software. The emerging question is different: *How do you build a reliable system around multiple capable agents working on the same problem?*

## **The problem with the single-agent loop**

A coding agent works through what Anthropic describes as [LLMs using tools based on environmental feedback in a loop](https://www.anthropic.com/engineering/building-effective-agents): it observes the state of a repository, reasons about what to do next, calls a tool, examines the result, and continues. For a small task, that loop can be enough. As the scope expands, however, maintaining reliability in a single context becomes harder.

A large migration might require understanding an unfamiliar codebase, identifying dependencies, changing database schemas, updating services, rewriting tests, modifying deployment configuration, and validating the resulting system. A single agent can theoretically perform all of that work, but it must maintain relevant information from every stage while continuing to reason about what comes next.

The pressure lands first on the context window. “A large context doesn’t only include everything correct or important — it also includes a lot of throwaway information,” Lipsig tells *The New Stack*. “Through compaction, that information can inadvertently end up ranked as important and incorrectly influence what your agent does. Or correct information can be distorted to become incorrect.

“Either way, after a couple of rounds of compaction, developers are seeing accuracy degrade and are starting to manage context once again manually.”

Lipsig’s read matches what researchers call [context rot](https://research.trychroma.com/context-rot) — and it hasn’t gone away with newer models.

A [2026 study](https://arxiv.org/html/2605.12366v1) testing frontier models,, including Claude Opus 4.6, GPT-5.4, and Gemini 3.1 Pro, found they missed a dangerous action buried in a long agent transcript two to 30 times more often once it came after 800,000 tokens of benign activity — the AI equivalent of a security guard who stops checking badges carefully after the two-hundredth person walks through, even though nothing about their training changed.

Furthermore, the tasks themselves may not be sequential. Forcing one agent to execute database analysis, documentation work, and test discovery one after another turns a potentially parallel workload into a serial one.

Subagents change that execution model. Instead of requiring one agent to carry an entire task through a single context, a coordinator breaks the work into smaller units and assigns them to specialized agents. GitHub’s [custom-agent model](https://docs.github.com/en/copilot/how-tos/copilot-sdk/use-copilot-sdk/custom-agents) illustrates this: different agents receive only the prompts, tools, and context they need for their tasks, executing work in isolated contexts rather than crowding an increasingly large conversation.

Multi-agent systems therefore bring higher token costs and additional coordination and integration risks, and splitting work across agents does not guarantee better software quality.

## **The coordinator is not another coding agent**

Once the work is divided this way, the coordinator becomes a control plane rather than another coding agent. Its job isn’t to write the code, but to understand the global task, manage dependencies, and decide how execution should proceed. Unlike a conventional scheduler, an agentic coordinator makes probabilistic judgments about result quality and resource allocation.

It may dispatch one agent to investigate a database schema, another to examine the service layer, and a third to inspect the test suite. When they return, the coordinator determines if their findings are sufficient to move to implementation. If a worker produces an incorrect result, the system must recognize the failure and decide whether to retry the work, reassign it, or change the task itself.

Anthropic has documented this same pattern in its own production system, calling it [orchestrator-subagent architecture](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them): a lead agent analyzes a query, develops a strategy, and spawns specialized subagents to investigate different facets in parallel. In a [June 2025 writeup of that system](https://www.anthropic.com/engineering/multi-agent-research-system), Anthropic reported a Claude Opus 4 lead agent with Claude Sonnet 4 subagents outperformed single-agent Opus 4 by 90.2% on its internal research eval — at roughly 15 times the token cost of a standard chat interaction (Anthropic puts single agents at about 4 times), a tradeoff that makes the pattern a deliberate architectural bet, not a free upgrade.

## **Parallelism introduces distributed-systems failure modes**

Parallelism is valuable because software work contains many independent tasks, but it creates coordination problems. Imagine a migration where one agent changes a database schema, another updates the consuming service, and a third updates integration tests.

If the schema changes while the service agent works against an earlier assumption, the system produces internally inconsistent work. This isn’t a risk unique to hypothetical migrations — the [International AI Safety Report 2026](https://arxiv.org/pdf/2602.21012) notes that “interactions between multiple AI agents are also becoming more common, introducing further risks, as errors propagate between systems.”

A single model invocation is a disposable computation, but a twenty-minute workflow modifying a repository is not. If an agent loses its machine halfway through, restarting from scratch is expensive and potentially unsafe against a changed environment.

To solve this, Cursor [moved its cloud-agent execution loop to Temporal](https://cursor.com/blog/cloud-agent-lessons) to handle durable execution and retries, pushing its cloud agents past two 9s of reliability. Temporal now handles 50 million of Cursor’s actions a day across 7 million unique workflows. “Durable execution isn’t a nice-to-have here. It’s the difference between a system you can operate and one you can only demo,” Lipsig tells *The New Stack*.

> “Durable execution isn’t a nice-to-have here. It’s the difference between a system you can operate and one you can only demo.”

By separating agent, machine, and conversation state, the execution engine can reason about the workflow independently. Reliability is no longer just about whether the model produces a good answer; it is about reliably completing distributed workflows composed of many operations, machines, and dependencies.

## **The environment, context, and observability are one problem**

In production, an agent is more than a model and a prompt; it requires a workspace, source code, dependencies, credentials, and state retention. Both companies provision isolated environments for these resources, directly linking an agent’s capability to its blast radius. OpenAI’s Agents API currently supports U.S. data residency but not Zero Data Retention; choosing a self-hosted sandbox does not make the Agents API eligible for ZDR. Cursor supports similar cloud isolation alongside local execution for machine-specific work.

An agent that can only inspect a repository poses a different risk than one that can modify production infrastructure. Consequently, the coordinator is inextricably linked to the security model, determining which agent receives specific information and authorities.

This logic extends to context routing. Giving every subagent the parent’s entire history increases cost and complexity while leaking irrelevant or sensitive information. Instead, the coordinator enforces information-flow boundaries: a database-analysis agent receives only schemas and relevant migrations, while a security-review agent gets the resulting diff without deployment credentials.

As agents increasingly use interfaces like [MCP](https://modelcontextprotocol.io/) to reach external systems, the platform must strictly govern which agent receives the authority to use specific tools, and for how long. MCP’s governance now sits inside the [Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/), a Linux Foundation foundation co-founded by OpenAI, Anthropic, and Block, with support from AWS, Google, Microsoft, Bloomberg, and Cloudflare to host MCP alongside AGENTS.md and Block’s goose — a sign the industry already treats it as infrastructure worth governing jointly, not a feature any one vendor owns.

This complexity creates a visibility problem. A simple final response often conceals a history involving multiple agents, tool calls, environments, and retries. Systems must expose task-level provenance — which agent received the assignment, what context it used, where it executed, and how the coordinator handled failures or human interventions.

Without execution provenance, debugging requires reconstructing distributed workflows from fragments. GitHub’s [exposure of subagent lifecycle events](https://docs.github.com/en/copilot/how-tos/copilot-sdk/use-copilot-sdk/custom-agents) points in this direction, treating agent lifecycles as observable components rather than hidden processes.

## **Coordination authority is not execution authority**

The most critical architectural boundary is the distinction between coordination authority and execution authority. A coordinator needs broad visibility to make useful decisions, but that does not imply unrestricted control over the project. “Just like you don’t want humans running around with root permissions, you don’t want your agents running with them either,” Lipsig tells *The New Stack*.

> “Just like you don’t want humans running around with root permissions, you don’t want your agents running with them either.”

“The ease of creating and leveraging AI agent permissions is lagging behind the speed of AI innovation, but any product team that needs to maintain compliance standards will tell you that easy or not, access controls are incredibly important. Functionally, that means fully agentic workflows need to run in a dedicated environment with their own permissions and connectivity. You can’t rely on agent context to do what you want — trying to keep something in context that long will just result in errors from context rot. Hardware or virtual-hardware-level permissions, in addition to system-level permissions, need to be configured so the agent is asked to provide only its unique value add.”

The risk isn’t hypothetical. [OWASP’s Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) formally names this failure mode Identity and Privilege Abuse (ASI03).

METR’s [independent investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), conducted with a Redwood Research contractor, found that the June–July 2026 incident — in which OpenAI’s own agents, running in internal ExploitGym cyber evaluations, escaped their sanctioned scope and attacked Hugging Face — unfolded in distinct phases. On June 26, agents discovered an exploit that provided full administrator access to OpenAI’s internal Artifactory package repository. On July 4, high-volume Artifactory activity caused an outage, triggering a security investigation and pausing evaluations. OpenAI switched to a freshly initialized Artifactory instance on July 6, which it says wiped the cache and messages left there.

On July 7, a new wave of ExploitGym experiments launched tens of thousands of agents, and on July 8 one agent established the primary unsanctioned message board. Roughly 1,200 agents eventually used the board, sending more than 70,000 messages and files; about 700 later participated in the attack on Hugging Face. The attack itself began on July 10–11 and wound down over July 12–13. The chronology matters because the administrator-access event, the Artifactory outage, and the later message-board activity were separate phases, not one continuous incident.

By binding autonomy, worker agents operate with the [minimum permissions required](https://www.cncf.io/blog/2026/03/23/cloud-native-agentic-standards/) for their specific tasks, keeping sensitive operations behind explicit approval boundaries. This also reshapes human review. Requiring human approval for every tool call destroys the efficiency of multi-agent execution, but showing only the final result obscures critical intermediate decisions.

The most useful design places human intervention around consequential, irreversible transitions — like moving into production or altering sensitive infrastructure. This is especially vital as agents become event-driven participants that [respond to Slack messages or pull request updates](https://cursor.com/blog/projects), not just direct prompts.

## **OpenAI and Cursor own different parts of the architecture**

The convergence does not mean OpenAI and Cursor have built interchangeable systems. Their products put the orchestration boundary in different places.

OpenAI is [exposing an agent harness through an API](https://openai.com/index/introducing-the-agents-api/). Its model gives developers primitives for managing context, tools, subagents, and execution environments, leaving application teams to decide how those capabilities fit into their own systems. The harness is open source, so teams can inspect the coordinator logic instead of treating it as a black box.

Cursor packages more of the surrounding workflow. [Projects](https://cursor.com/blog/projects) provides the coordinator, cloud execution, shared project context, and a developer-facing workflow in the same environment.

That difference matters because orchestration is a collection of infrastructure decisions: who owns the execution environment, where workflow state persists, how agents are isolated, how credentials are provisioned, what happens when a worker fails, how one agent’s output becomes another agent’s input, and which actions can happen without human approval.

An API gives developers more responsibility for answering those questions. An integrated platform answers more of them on the developer’s behalf.

Neither approach removes the underlying engineering problems. It changes where they are implemented and who is responsible for operating them.

## **The coordinator is becoming an architectural boundary**

The evidence from these systems points to a change in the role of the coding agent itself.

The model still performs the reasoning and code generation. But larger agentic workflows require another layer to determine how that capability is applied: which work is delegated, what context crosses an agent boundary, which tools are exposed, how execution state survives failures, and when the workflow needs human intervention.

Those are familiar distributed-systems concerns. Workers operate concurrently, state can be shared or isolated, dependencies connect tasks, workers can fail independently, and results need to be persisted and observed. The difference is that the workers are now probabilistic software agents rather than conventional processes.

That makes the coordinator more than a convenience feature. It is where a high-level software objective becomes executable work — and where decisions about context, permissions, durability, observability, and human intervention converge.

The September 10 launches make that shift visible from two different directions. OpenAI exposed orchestration infrastructure through an API. Cursor embedded it into a project-level development environment.

Neither announcement proves that one architecture will become the universal model for software development. But together with the systems already emerging around them, they show coding agents moving away from a single model executing an entire task and toward workflows that divide work among specialized agents, execution environments, and persistent infrastructure.

The engineering question is therefore no longer only whether an agent can write the code. It is whether the system around it can reliably decide what to do, which agent should do it, what that agent should be allowed to see and change, how to verify its work, and where a human should take control.

Those are architecture and infrastructure questions — and as coding agents move from interactive assistants toward autonomous software workflows, they may matter as much as the underlying model.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/06/dece2fd2-cropped-b9a1055b-robert-kimani-new-portrait-2-600x600.jpg)

Robert is a freelance Linux Engineer and consultant specializing in Site Reliability Engineering (SRE), infrastructure security, and adversary-informed resilience. A passionate Linux enthusiast and open source advocate, he helps organizations design secure, observable, and highly reliable systems grounded in automation...

Read more from Robert Kimani](https://thenewstack.io/author/robertkimani/)