Enterprise security has traditionally operated on a relatively straightforward premise: establish identity, authenticate the requester, determine what that identity can access, and enforce those permissions.

AI agents introduce a fundamental complication. They don’t simply access systems. They interpret objectives, select tools, create sub-agents, make decisions, and execute actions, often using credentials and permissions inherited from humans.

The problem isn’t necessarily that an agent lacks proper credentials. It’s that those credentials may authorize actions the human never intended the agent to perform. And unlike conventional software, agents can change their execution paths dynamically in pursuit of an objective.

> “The problem isn’t necessarily that an agent lacks proper credentials. It’s that those credentials may authorize actions the human never intended the agent to perform.”

This creates a new operational requirement: security must evaluate not only who or what is acting, but what an agent is attempting to do, on whose authority, and under which policy. Meeting that requirement takes more than a security checkpoint. It requires a continuous agent security lifecycle.

## Defense-in-depth needs action-level authorization

Every passing day further shows that agent security is a defense-in-depth problem. Network security controls how agents communicate. Endpoint and runtime protections constrain where and how code executes. Infrastructure and silicon-based protections establish a foundation for trusted execution. Model guardrails help shape behavior. These layers complement each other, and enterprises need them to work together.

But consider an agent that attempts to delete a production database using a developer’s legitimate credentials. Network controls may see authorized traffic. The runtime may see an approved process. An identity provider may confirm that the credentials are valid. All three could be working as designed.

The missing question is whether this particular agent should be allowed to perform this particular action, even if the human whose credentials it inherited could legitimately do so.

That requires identity context and authorization at [the point of action](https://thenewstack.io/inside-out-agent-security/).

In practical terms, an authorization decision should consider the agent’s identity, the human or service that delegated its authority, the requested operation, the target resource, and applicable policy. Enforce that decision before the operation executes.

[The agent harness](https://thenewstack.io/kubecon-agent-harness-koordinator/) (the execution layer that connects an AI model to tools, application programming interfaces (APIs), files, and external systems) is an important place to apply that control. Other trusted enforcement points, including tool services and resource APIs, provide additional protection.

The goal isn’t to replace existing defenses. It’s to make authorization integral to agent execution. But even that is only a partial answer because what is needed is a new framework — an agent security lifecycle.

## Four disciplines, one continuous security lifecycle

A practical agent security architecture needs four interconnected disciplines:

**Observe. Enforce. Build. Deploy.**

![Diagram of the Agent Security Lifecycle](https://cdn.thenewstack.io/media/2026/10/33c4d2a1-image.png)

These aren’t sequential gates every organization must pass through. They form a continuous lifecycle, and organizations can enter at whichever point reflects their existing infrastructure and maturity.

A company with agents already running in production may begin by observing their behavior. A development team creating a new agent may start by building authorization directly into its architecture. An enterprise expanding an existing deployment may discover new activity that requires revisiting its policies.

Each stage informs the others. The cycle never really ends.

### Observe: Understand what agents actually do

Most enterprises have some form of application inventory. Increasingly, they’re extending that inventory to AI agents.

That’s a useful starting point, but knowing an agent exists isn’t the same as understanding what it does.

Security teams need visibility into the actions agents actually attempt:

* Which tools and APIs are being invoked?
* What commands are being executed?
* Which systems and sensitive resources are being accessed?
* What [credentials and delegated permissions](https://thenewstack.io/agent-workload-identity-authentication/) are being used?
* What sub-agents are being created, and what authority do they inherit?
* Which actions would violate a proposed security policy?

Architectural diagrams or agent configuration files alone can’t reliably answer these questions. The important evidence exists in execution, which is why [agent observability must extend](https://thenewstack.io/agentic-ai-observability-auditing/) beyond conventional logs and application monitoring. Security teams need to connect observed actions with identity, delegation, and authorization context.

> “Knowing an agent exists isn’t the same as understanding what it does. You can’t intelligently govern behavior you haven’t observed.”

Equally important, observation should support evaluating potential policies without immediately disrupting production activity. There are useful precedents here. When intrusion prevention systems and web application firewalls became widely adopted, organizations learned that immediately enabling aggressive blocking rules could interrupt legitimate applications. Monitoring first, establishing behavioral baselines, and progressively enforcing policies proved more practical.

AI agents require similar discipline, although their behavior can be substantially more dynamic.

For organizations already deploying agents, the priority may not be to block more activity. It may be to understand what activity is actually occurring.

**You can’t intelligently govern behavior you haven’t observed.**

### Enforce: Put deterministic boundaries around probabilistic behavior

Once organizations understand how agents behave, they can begin defining and enforcing boundaries.

The distinction between probabilistic AI behavior and deterministic security enforcement is critical. An agent might interpret instructions differently across executions. It may choose different tools, sequence operations differently, or discover alternative ways to accomplish an objective.

A security policy cannot depend on the model consistently choosing the safest option. Consider a coding agent with permission to work in a source repository. Reading a file might be permitted. Modifying a protected branch might require human approval. Deleting the repository might be prohibited.  All three actions could originate from the same authenticated agent operating in the same environment. But they require different authorization decisions.

> “The distinction between probabilistic AI behavior and deterministic security enforcement is critical. The objective is not to make agents incapable of acting. It’s to make the boundaries of their authority explicit, enforceable, and consistent.”

Effective enforcement means evaluating the attempted action against policy before execution. A simplified authorization request might contain:

* **Actor:** Coding agent 42
* **Delegated authority:** Developer account 17
* **Requested action:** Delete repository
* **Target:** Production source repository
* **Policy decision:** Deny

The important architectural distinction is that the permission check occurs at a trusted enforcement point, not merely within a prompt instructing the model to behave. For high-risk operations, the system may deny execution or require explicit human approval. Lower-risk operations may proceed automatically.

Enforcement also needs to account for agents attempting alternative execution paths. A harness-level check only protects actions routed through that harness. Robust designs therefore combine action-level authorization with independently enforced permissions at APIs, tool servers, and underlying resources.

The objective is not to make agents incapable of acting.

It’s to make the boundaries of their authority explicit, enforceable, and consistent.

### Build: Make identity and authorization part of the agent architecture

Observation and enforcement help organizations secure existing agents. But the greatest long-term benefit comes when those lessons influence how agents are built.

Today, developers may implement AI agents using different models, frameworks, tool protocols, and execution environments. If every team must independently design identity propagation, delegated permissions, authorization policies, and audit logging, security becomes inconsistent and difficult to maintain.

Instead, these capabilities should be available as reusable infrastructure. Software development kits (SDKs), APIs, and shared authorization services can make it easier to incorporate controls directly into agent applications. That means establishing several architectural expectations from the beginning.

An agent should have an identifiable execution context. Its authority should be explicitly delegated and constrained. Sensitive tool invocations should require authorization. Security decisions and consequential actions should be auditable.

Importantly, an agent shouldn’t automatically inherit every permission available to the human initiating it. Consider an employee using an AI assistant to reconcile invoices. The employee may have permission to review invoices, approve payments, and update vendor records. The agent’s assigned task requires only invoice retrieval and reconciliation. The correct architecture delegates the permissions required for that task, not the employee’s entire authority.

That distinction matters even more when an agent creates sub-agents or invokes tools under different service identities. Developers need mechanisms to preserve and constrain delegated authority throughout those interactions.

Security should also be portable across implementations. Organizations shouldn’t have to reconstruct their authorization architecture every time a development team adopts a new framework or model. This is why identity and authorization should be infrastructure, not application-specific features.

Done correctly, security becomes something developers build with, rather than something security teams attempt to bolt on after an application is complete.

### Deploy: Make consistent security possible at machine scale

Building a secure agent is one challenge. Operating thousands of agents across applications, departments, cloud environments, and business processes is another. At that scale, manually reviewing permissions or trusting individual development teams to implement controls consistently becomes unsustainable.

Agents may invoke new tools, coordinate with other agents, and participate in workflows that span multiple authorization domains. Security controls need to follow them. That requires a deployment architecture that consistently applies identity context, delegated authority, authorization policy, and audit requirements across supported environments.

The underlying model or framework shouldn’t determine whether security controls exist. Nor should adopting a new tool require rebuilding the entire security architecture. This is where framework-independent interfaces and centrally managed policy become especially valuable. Organizations can maintain consistent security expectations while allowing development teams to use the technologies best suited to their applications.

Deployment also changes the meaning of scale. With traditional applications, scale generally means handling more users, transactions, or workloads. With agents, scale can also mean more independent actors making more decisions, invoking more tools, and creating additional agents. The number of consequential actions can increase much faster than the number of deployed applications. Security architectures must therefore operate automatically and consistently at the pace of machine-generated activity.

Deployment creates something else: new evidence. Production activity reveals unexpected workflows, new dependencies, authorization gaps, and opportunities to refine policy. That information feeds directly back into observation and enforcement and informs how the next generation of agents is built.

The lifecycle continues.

## The shift from security as a checkpoint to security as infrastructure

The underlying security principles aren’t new. Least privilege, zero trust, separation of duties, identity federation, and defense in depth remain foundational.

What’s changing is how consistently those principles must be applied throughout an agent’s lifecycle, and how close enforcement must be to the actions agents take. Traditional security architectures often assume that controlling system access is enough to govern what happens afterward.

AI agents challenge that assumption because they can make consequential decisions independently within the access they’ve already been granted. As a result, the security model needs to evolve in three important ways.

First, visibility must be based on actual agent behavior rather than configuration alone.

Second, authorization must evaluate individual actions in the context of identity, delegation, and policy.

Third, these capabilities must become reusable infrastructure that accompanies agents from development through production and back into continuous improvement.

This is why treating agent security as a lifecycle, rather than a collection of isolated controls, matters. Observation supplies evidence. Enforcement establishes boundaries. Development incorporates those boundaries into applications. Deployment extends them consistently across environments and feeds new evidence into the cycle.

Each stage makes the others more effective.

## Securing the agentic era without slowing it down

Organizations face two tempting extremes. One is to trust agents too broadly, assuming that legitimate credentials and well-written instructions provide sufficient protection. The other is to constrain agents so aggressively that the productivity gains motivating their adoption disappear. Neither is a sustainable long-term strategy.

> “Success isn’t measured by how many agent actions an organization can block. It’s how many valuable actions it can confidently (and safely) enable.”

A better approach is to establish the visibility, accountability, and controls that make greater autonomy possible. That means knowing what agents actually do, enforcing what they’re permitted to do, building those controls into the development process, and deploying them consistently at scale. It also means recognizing that the work is never finished. New models, frameworks, tools, and workflows will continuously introduce new behaviors and risks.

Agent security cannot be a one-time approval at the beginning of a deployment. It must be a continuous discipline that evolves with the agents themselves. Success isn’t measured by how many agent actions an organization can block. It’s how many valuable actions it can confidently (and safely) enable.

It takes a continuous lifecycle, not a gatekeeper.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/d87899f3-greg_vesper_headshot.avif)

Greg Vesper is Chief Product Officer at Ory, leading strategy to secure human and non-human identities at planet scale. A pioneer in NASA e-commerce, cloud medical imaging, and hyperscale compliance, Greg now focuses on unlocking enterprise agentic computing through a...

Read more from Greg Vesper](https://thenewstack.io/author/greg-vesper/)