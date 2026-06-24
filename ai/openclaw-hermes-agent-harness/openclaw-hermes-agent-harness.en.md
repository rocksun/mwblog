At Microsoft’s Build keynote this month, CEO Satya Nadella described a platform shift away from operating systems and apps, and toward agentic AI that doesn’t wait to be opened by a user. Then he showed the layer that makes the shift possible: [OpenClaw](https://github.com/openclaw/openclaw), an open-source harness and independent project released only months earlier, running natively on Windows inside Microsoft’s new execution containers. Built on top of it was [Scout, Microsoft’s always-on enterprise agent](https://thenewstack.io/microsoft-scout-openclaw-runtime/). A harness barely a year old, onstage as governed infrastructure.

Nvidia had made the case more bluntly at its [GTC conference](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/) in March, where Jensen Huang called OpenClaw “the operating system for personal AI.” The analogy sticks: A harness does for a language model what an OS does for a processor. A model can independently answer questions while a harness enables it to run continuously, remember what it learns, and call tools to act.

Two open projects have built that layer this year from different starting points. **OpenClaw** is built around the gateway, the part that connects an agent to the channels people already use. **Hermes Agent**, from Nous Research, is built around memory, the part that lets an agent learn a developer’s work and improve at it. The contest between them is over the control layer, not the model either one calls.

## The agent harness in plain English

At its core, an agent harness is the software that turns a model into a system capable of operating autonomously. It brings together a runtime that keeps the agent alive between tasks, a gateway that carries messages in and out, and a memory that persists across sessions. On top of those sit the tools the agent calls to act, the identity it runs under, the skills it can extend, and the policy and observability controls that decide what it may touch and what it must record. A coding assistant such as [Claude Code](https://docs.claude.com/en/docs/claude-code) or [Codex](https://openai.com/index/introducing-codex/) covers only part of this. It runs inside an interactive session and loses most of its working context once that session ends. A harness keeps the runtime, memory, and governance in place so the agent can run unattended.

> A harness keeps the runtime, memory, and governance in place so the agent can run unattended.

Nous Research and OpenClaw agree on that anatomy. They differ on which part they treat as the primary control point. OpenClaw starts with the gateway, so one agent can answer on WhatsApp, Discord, Slack, and other channels from a single place. Hermes starts with memory, so one agent can carry a developer’s context across weeks and refine its own skills.

## OpenClaw’s gateway-first design

OpenClaw began as an independent open-source project from Peter Steinberger, a developer known for his earlier work in PDF tooling, who released an early version late in 2025 and renamed it twice before settling on OpenClaw in January. It is built for breadth, centered on a central gateway that connects the agent to dozens of messaging channels. [ClawHub](https://github.com/openclaw/clawhub), its public skills marketplace, holds thousands of community skills that extend what the agent can do. The open-source momentum was real, with the repository near 380,000 GitHub stars by late June, though stars measure visibility rather than production use.

The more important development is who adopted that gateway. Steinberger [joined](https://techcrunch.com/2026/03/16/nvidias-version-of-openclaw-could-solve-its-biggest-problem-security/) OpenAI in February, and the project moved to an independent foundation with OpenAI as a sponsor rather than an owner.

At GTC in March, [Nvidia wrapped OpenClaw in NemoClaw](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/), an OpenShell runtime that sandboxes each agent and enforces policy from outside the agent’s reach.

At Build in June, Microsoft made OpenClaw native to Windows execution containers and shipped Scout, an agent on the OpenClaw gateway with its own Entra identity and connections into Teams, Outlook, and SharePoint. In each case, the platform vendor kept OpenClaw’s breadth and added the governance and identity the original project lacked.

> A security team can now scope which folders an agent reads and which stay hidden, rather than granting the broad access that made early OpenClaw deployments risky.

For enterprises, that changes the calculus. A security team can now scope which folders an agent reads and which stay hidden, rather than granting the broad access that made early OpenClaw deployments risky. Platform teams can offer a single governed agent that staff can access from the tools they already use. Breadth gave OpenClaw distribution, and the platform vendors supplied the controls that distribution needed to enter production.

## Hermes’ memory-first design

[Hermes Agent](https://github.com/nousresearch/hermes-agent) takes the other path. Nous Research, the lab behind the Hermes, Nomos, and Psyche model families, released it on February 25 under an MIT license, written in Python and built to run persistently on infrastructure the team owns: a VPS, a home server, or a laptop.

The defining capability of Hermes is persistent memory across sessions. It keeps a layered memory, develops new skills after a hard task, and refines those skills as it uses them. It also builds a profile of the developer it works for, so each session starts with more context than the last. The skills follow the [agentskills.io](https://agentskills.io) standard, which keeps them portable across agents rather than locked to one.

That depth has translated into measurable usage. Hermes surpassed 100,000 GitHub stars by mid-May and reached roughly 160,000 by late in the month. It overtook OpenClaw in OpenRouter’s daily token rankings on May 10, with the day’s total reported at 224 billion tokens, up from 186 billion, and placed Hermes first by total tokens.

By late June, OpenRouter’s app rankings also placed Hermes first by total tokens, past 22 trillion. GitHub stars, token volume, and platform endorsements measure different kinds of adoption, and they rarely move together. Nous has also made portability part of the pitch, shipping a `hermes claw migrate` command that imports an OpenClaw user’s settings, memories, skills, and keys in one step.

Developers can keep an agent that holds a codebase, its conventions, and prior decisions across weeks, instead of rebuilding that context each morning. Teams can move the agent between providers with a single command, since Hermes remains model-agnostic across hundreds of models. The tradeoff is operational, since the team that runs Hermes also has to secure and maintain the infrastructure it lives on.

## Breadth, depth, and where each fits

The choice resembles the familiar tradeoff between a managed cloud service and self-managed infrastructure. A managed service is convenient and vendor-governed, while self-managed infrastructure offers full control and operational responsibility.

Many enterprises will run both, depending on the workload. Neither project is limited to a single capability. OpenClaw includes memory and skills, and Hermes speaks across twenty-odd channels, so the distinction is one of emphasis rather than exclusivity. The table below maps the common cases, with the caveat that both are emerging platforms rather than finished products.

| Scenario | Stronger fit | Why, with the tradeoff |
| --- | --- | --- |
| Regulated enterprise that needs audit and policy control | OpenClaw under NemoClaw, or Microsoft Scout | Governance and identity are wrapped around the agent by Nvidia or Microsoft, though both are early and tie the buyer to their stack |
| Developer who wants an agent that learns their work and stays portable | Hermes | Persistent memory and self-improving skills are the design center, at the cost of running your own infrastructure |
| Team reaching users across many chat platforms | OpenClaw | The gateway and large skills marketplace cover breadth no rival matches, though skill quality varies and supply-chain risk is real |
| Organization standardizing on one provider’s cloud | Scout inside Microsoft 365 | Deepest integration within that ecosystem, and the least portability outside it |

Real deployments will not standardize on one approach. Nvidia’s NemoClaw blueprints already run Hermes agents under OpenShell as readily as they run OpenClaw. The governance layer is being built to sit beneath multiple agent projects rather than to pick one.

## Why the harness layer matters

Enterprise buyers should slow down on two questions before either agent touches production systems. The first question is one of accountability. When an agent can rewrite its own memory and skills between sessions, as Hermes does, the team needs to know who can explain a change in behavior and where that change is logged. The second question concerns ownership. When governance and identity come from a platform vendor, as they do with NemoClaw and Scout, the policy engine and the identity belong to that vendor, not to the team running the agent.

> Nvidia and Microsoft are competing to place governance, identity, and observability around whichever agent a customer chooses.

For the platform vendors, the prize is the runtime layer, which will outlast any single foundation model. Nvidia and Microsoft are competing to place governance, identity, and observability around whichever agent a customer chooses, which is why NemoClaw supports Hermes alongside OpenClaw.

Security is part of the same logic. Audits of OpenClaw’s [skill marketplace](https://thenewstack.io/openclaw-github-stars-security/) flagged 341 malicious entries among the skills they scanned, and security firms reported tens of thousands of exposed instances earlier this year – the gap that governed runtimes are meant to close.

## What’s next

The agent market is moving past model selection into the runtime, governance, and memory layers. OpenClaw showed that a broad gateway and a large skills ecosystem can attract developers and draw in OpenAI, Nvidia, and Microsoft. Hermes showed that persistent memory and self-improving skills can drive heavy daily usage without the same platform backing. Whether breadth and depth will remain in separate projects is already uncertain, since NemoClaw runs under a single set of controls and Hermes can import an OpenClaw setup.

### The next phase will turn on ownership.

Enterprises will need to know who controls the memory an agent accumulates, who governs the tools it can call, and who owns the runtime that keeps it alive. An agent that has learned a year’s worth of a developer’s habits creates a higher switching cost than one that merely connects to many applications. Memory, more than channel reach, is becoming the durable form of lock-in, which is why the runtime, governance, and memory layers are where the platform vendors will compete as they settle in beneath both projects.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)