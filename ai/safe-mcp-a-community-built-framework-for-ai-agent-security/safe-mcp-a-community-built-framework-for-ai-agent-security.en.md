In cybersecurity, going solo rarely works. Historically, frameworks like [CVEs](https://www.cve.org/), [ATT&CK](https://attack.mitre.org/) and [software bills of materials (SBOMs)](https://thenewstack.io/sboms-sboms-everywhere/) have shown that shared languages of risk turn scattered efforts into coordinated victories. Now, with AI running faster than ever and growing its own “muscles and tools,” a similar shift is overdue.

AI agents can fetch data, take actions and make decisions in milliseconds. [Model Context Protocol (MCP)](https://thenewstack.io/why-the-model-context-protocol-won/) standardizes the way they connect to tools and APIs, which is powerful — and dangerous if misconfigured. A single over-privileged tool or malicious prompt can turn a convenience into an exploit.

That’s why [SAFE-MCP](https://github.com/SAFE-MCP/safe-mcp) emerged: A framework and open community that provides AI ecosystems with a common security baseline. And now it’s hit a critical milestone: It was recently formally adopted under the Linux Foundation and the OpenID Foundation, two of the world’s most trusted stewards of security standards. This instantly moved SAFE‑MCP from a promising draft into a foundation‑backed, community‑governed project with neutral governance.

This timing matters. With the National Institute of Standards and Technology (NIST), [the EU AI Act](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/), and other regulators demanding auditable safeguards for high-impact AI, it’s clear no single team can secure these systems on its own. The Cybersecurity and Infrastructure Security Agency (CISA)  and the European Union Agency for Cybersecurity (ENISA) have both highlighted rising security risks in AI systems in their 2025 guidance and threat-landscape reports. And major labs like OpenAI and Anthropic publicly frame tool-using AI agents as a key safety challenge. Collaboration is now a security requirement, and SAFE-MCP is the framework that enables it.

## **Why It Matters – MCP as the Connective Tissue of AI**

Let’s first figure out what MCP really is. Picture MCP as the nervous system of modern AI: It sends signals between the brain (the LLM) and the body (tools, APIs and data), coordinating how requests are issued and actions are executed. Without something like MCP, integrations tend to be one‑off, duplicated and difficult to manage or govern. With MCP, the signals flow cleanly: A request goes out, the right tool responds, and the agent gets the data it needs.

The beauty of MCP is its standardization. It defines a client-server architecture for AI agents, separating agent requests from tool execution and responses, and allowing systems built by different teams using different technologies to communicate seamlessly. But here’s the kicker: With great power comes great responsibility. Every connection MCP makes expands the attack surface. Most failures start quietly: A forgotten permission, a misrouted call or an AI that decides to get a little too creative with its access.

This is where SAFE-MCP comes into play. While MCP defines how AI agents connect, SAFE-MCP ensures that those connections don’t become playgrounds for attackers.

## **What SAFE‑MCP Actually Is (and Isn’t)**

SAFE-MCP is not a dusty PDF or a vague white paper. It’s a security analysis framework for the MCP: a living catalog of tactics, techniques and procedures (TTPs). With more than a dozen tactic categories and 80+ documented techniques, it provides a consistent way to analyze attacker goals, enabling conditions and mitigations in AI-agent systems.

In the same spirit as MITRE ATT&CK, SAFE-MCP gives teams a shared language for how MCP‑based systems can be attacked and defended, without acting as a control system itself. Think of it as a combination of a security handbook, a recipe book and a survival guide for AI agents. It says, “Here’s what can go wrong, how attackers might pull it off and how you can stop it.”

How SAFE-MCP was built and who built it make it unique. [Frederick Kautz](https://www.linkedin.com/in/fkautz/), [Arjun Subedi](https://www.linkedin.com/in/quantumbits/) and [Bishnu Bista](https://www.linkedin.com/in/bishnubista/), a group blending open source security experience, deep tech community organizing and global developer leadership guide the framework Together, they’ve shaped SAFE‑MCP into something rare: a community‑driven ecosystem. Weekly hackathons, bi‑weekly meetings and open collaboration sessions turn ideas into actionable defenses that evolve as fast as the technology itself.

The framework adapts MITRE ATT&CK for MCP agent‑tool orchestration, making it one of the first open frameworks focused specifically on this layer. Today, it spans threats such as prompt manipulation (SAFE-T1102), tool poisoning (SAFE-T1001), OAuth consent abuse (SAFE-T1007) and agent CLI weaponization (SAFE-T1111), each paired with practical mitigations and, where possible, mapped back to existing ATT&CK techniques.

Its adoption by the Linux Foundation and the OpenID Foundation brought SAFE‑MCP under neutral, foundation‑backed governance while preserving its hands-on, community-driven culture.

Contributors from Meta, eBay, Okta, Red Hat, Intel, American Express and independent research communities collaborate through pull requests across U.S., South Asian and African time zones, contributing code, detection rules and policy templates.

Through in-person hackathons at Venture Dock and VC Nest in Palo Alto, California, as well as Luma-hosted global events, more than 2,000 people have engaged with SAFE-MCP, creating a worldwide neighborhood-watch model for AI: many eyes on the system, shared responsibility and shared defense.

## **How SAFE‑MCP Keeps AI Agents in Check**

So, what does a safe AI agent actually look like? Think of it like airport security – a series of layers that work together to keep things running smoothly while preventing chaos. SAFE‑MCP doesn’t run those checkpoints for you, but it defines the patterns and controls that a secure MCP deployment should have.

These patterns are grounded in common MCP failure modes, where identity, intent and execution are distributed across clients, servers and tools rather than enforced in one place.

* **Identification and Intent —**Every tool call should start with verifying who or what is making the request – and why. SAFE‑MCP recommends OpenID Connect–backed identity, scoped tokens and least‑privilege access as the basic way to ensure unauthorized agents can’t slip through.\
* **Screening —** Once identity is confirmed, every interaction should be scanned for safety. Instead of relying on obscure internal codes, SAFE‑MCP catalogs techniques and mitigations for detecting prompt‑based manipulation, suspicious tool behavior and signs of poisoned or tampered responses – the digital equivalent of X‑ray scanners catching hidden risks before they cause damage.
* **Policy Enforcement —** Even when something looks legitimate, it doesn’t mean it should happen. SAFE‑MCP organizes guidance for context‑aware authorization, so real‑world systems can evaluate each request in near real time and enforce rules and timing, ensuring actions only occur when and where they make sense.
* **Observability and Response —** Finally, every good system needs eyes and reflexes. SAFE‑MCP highlights the need for instrumentation, audit trails and quarantine patterns, giving defenders a shared playbook for early detection and containment of misuse so issues are resolved before they spiral.

Together, these layers describe what a SAFE‑MCP‑aligned architecture should look like: AI agents can act quickly and intelligently, while the controls inspired by SAFE‑MCP keep their actions visible, verifiable and secure.

## **Broader Impact – How Open Security Scales**

SAFE-MCP offers something to every part of the ecosystem:

* Enterprises get clear, testable controls for audits and governance, which are useful for evidence and assurance.
* Developers get reusable mitigations and security patterns, which are easy to turn into checklists or test cases.
* Researchers get a public sandbox to test attacks and share defenses. It enables reproducible validation.
* Policymakers get a standards-aligned bridge between “AI safety” and real implementation. It supports enforceable expectations.

Adoption is accelerating. Contributors from major tech companies, public GitHub forks, and enterprise discussions all point to growing momentum. SAFE-MCP helps turn fragmented AI-agent risks into practical, auditable safeguards.

What makes SAFE-MCP work isn’t just its code or documentation – it’s the people. It scales because it’s open, modular and genuinely collaborative. Every new contributor strengthens the fabric of security for everyone else.

## **The Road Ahead – Collaboration Is the Real Firewall**

At its core, SAFE-MCP proves something simple: open collaboration beats secrecy. Every line of code, every test, every debate turns abstract “AI risk” into real defenses.

Here’s what matters most:

* SAFE-MCP is a foundation-backed, open standard that bridges AI security, identity and enterprise governance under one roof.
* It’s powered by people, not politics. Weekly hackathons and bi-weekly Linux Foundation calls keep it practical, current and tested in the real world, not just in slides or white papers.
* Collaboration is its competitive edge; shared knowledge consistently outpaces attackers.

So, what now?

Go take a look! Explore the SAFE-MCP framework on GitHub. Join a hackathon. Drop into a Linux Foundation call. Submit a pull request, a test case, or even a wild mitigation idea that just might work.

Because at the end of the day, AI security is about trust. And trust isn’t built by walls; it’s built by people showing up, working together and keeping the lights on for everyone else. SAFE-MCP is proof that when the community becomes the firewall, everyone sleeps a little better at night.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/b90ae4db-cropped-2e695ada-arjun-subedi.jpeg)

Arjun Subedi is a co-creator of SAFE-MCP, the open source security framework for AI agents using the Model Context Protocol. He is also the co-founder of Astha.ai, a company building infrastructure for secure and governed AI-agent ecosystems. Based in Silicon...

Read more from Arjun Subedi](https://thenewstack.io/author/arjun-subedi/)