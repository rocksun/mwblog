The transition from traditional web applications to agentic ecosystems is more than a change in the UI; it is a fundamental shift in the internet’s threat model. We are moving from a world where “bad input creates bad data” to one where “bad input creates bad actions.” As AI agents evolve from simple chatbots to autonomous *conductors* capable of calling APIs, reading sensitive files, and sending emails, our legacy security models are cracking under the pressure.

If you are building or deploying AI agents today, you are likely sitting on an IAM problem in disguise, considering that [agents are outnumbering humans 144:1](https://entro.security/blog/takeaways-nhi-secrets-risk-report/). In a recent global Enterprise Management Associates (EMA) survey on agentic, [95% of participants were in production or limited pilot programs](https://www.ory.com/resources/whitepapers/agentic-ai-identity-security-readiness) using AI agents. Here is how to navigate the shift from human-centric security to the Agent IAM era.

## 1. What’s the problem? (The identity vacuum)

The core problem is that AI agents currently operate in an *Identity Vacuum*. In most production environments, agents are given ambient, inherited access. They run as service accounts with broad permissions or, worse, inherit the full permissions of the human user who triggered them.

This creates three critical vulnerabilities:

* **The Action-Based Threat Model:** Unlike traditional apps, agents “do” things. If an LLM is tricked via prompt injection, it doesn’t just display a wrong answer; it executes a malicious tool call. [80% report seeing apps act outside of intended boundaries](https://www.osohq.com/learn/why-your-authorization-model-wont-survive-agentic-ai).
* **The RAG Attack Surface: [Retrieval-Augmented Generation (RAG)](https://thenewstack.io/advanced-retrieval-augmented-generation-rag-techniques/)** systems are vulnerable to indirect prompt injection. If an agent fetches a document containing malicious instructions, that document becomes the new “master” of the agent, overriding developer guardrails.
* **Non-Human Identity (NHI) Explosion:** We are seeing a massive surge in APIs, services, and autonomous agents that lack a centralized source of truth for identity. [39% report unauthorized access incidents](https://www.sailpoint.com/identity-library/ai-agents-attack-surface) with agents, and most teams have no way to revoke an individual agent’s access without breaking the entire service.

Anthropic’s Claude Mythos discovery recently highlighted [the stakes](https://www.ory.com/blog/anthropic-mythos-iam-identity-security-risk). The model identified thousands of zero-day vulnerabilities across major OSs and browsers, including bugs that had survived 20+ years of human review.

This matters because AI is now a force multiplier for vulnerability discovery. While AI can find bugs at machine speed, humans still remediate them at a “human pace” (meetings, backlogs, patch cycles).

> “While AI can find bugs at machine speed, humans still remediate them at a ‘human pace.'”

If your IAM infrastructure is homegrown or unmanaged open source, you cannot patch fast enough to keep up with an AI-powered attacker. Identity is the most exposed layer because it is the control plane; if the agent’s identity is compromised, the entire infrastructure is open for lateral movement. SailPoint research reports [33% have seen agents inappropriately handle restricted data](https://www.sailpoint.com/identity-library/ai-agents-attack-surface).

## 3. How do I fix the problem? (The agentic IAM blueprint)

Fixing agentic security requires moving the guardrails from the LLM prompt to the infrastructure. You cannot *talk* an agent into being secure; you must *authorize* it to be secure. Compounding the agentic problem, the majority of EMA survey participants [do not believe their IAM solutions are ready](https://www.ory.com/resources/whitepapers/agentic-ai-identity-security-readiness):

* 62% state not ready for agentic resiliency
* 49% claim not ready for agentic compliance
* 62% report not [ready for agentic scale](https://thenewstack.io/enabling-autonomous-agents-with-environment-virtualization/)
* 59% disclose not ready for agentic security

> “You cannot talk an agent into being secure; you must authorize it to be secure.”

### Treat agents as first-class identities

Agents must be treated as first-class non-human Identities. This means:

* **Authentication:** Agents should authenticate against an Identity Provider using scoped credentials.
* **Short-lived tokens:** Use OAuth2 to issue tokens that are interaction-scoped. If an agent is compromised, the token expires quickly, limiting the window of exploitation.
* **Relationship-based access control (ReBAC):** Use a graph-based permission model to define exactly what an agent can touch.

### Align retrieval with authorization

In RAG systems, the “view” permission must match the “retrieval” permission. Before an agent fetches a document to place in its context window, the system must check: *Does this specific Agent ID have permission to view this Document ID?* If not, the document is never retrieved, preventing the agent from ever seeing and being influenced by malicious payloads.

### Engineers as conductors

Shift your engineering mindset. Stop trying to hard-code every agent action. Instead, act as a *conductor*, orchestrating agents through Policy as Code. Use tools to visualize these complex permission chains so you can see exactly how an agent’s relationships resolve to ALLOW or DENY.

## 4. “Gotcha” problems & how to avoid them

Even with a solid plan, several [hidden costs](https://thenewstack.io/hidden-agentic-technical-debt/) and technical traps often emerge:

* **The inherited access trap:**
  + *Problem:* Developers often give agents *Admin* rights to simplify development.
  + *Fix:* Implement *Least Privilege Access* from day one. If an agent only needs to read Marketing docs, don’t give it access to the whole S3 bucket.
* **The feedback loop delay:**
  + *Problem:* As you add security layers, agent latency increases, leading users to bypass security for speed.
  + *Fix:* Use high-performance permission engines that can resolve complex queries in milliseconds, ensuring security doesn’t buffer the user experience.
* **The ghost agent problem:**
  + *Problem:* Agents are created for a task, the task ends, but the credentials remain active.
  + *Fix:* Implement automated lifecycle management. Use *Token Chain Revocation* so that if a parent orchestrator agent is flagged, all child agent tokens are instantly invalidated.
* **Visual blindness:**
  + *Problem:* Permission models for hundreds of agents become too complex to hold in a human brain.
  + *Fix:* Use visualization tools to audit your models. If you can’t see the graph, you can’t secure the graph.

## Summary: Identity is where you start

Security is a process, not a product. While LLM guardrails and prompt hardening are important, they are easily bypassed. The only hard boundary that stays firm in the face of an autonomous agent is the *Authorization Boundary*.

Treat your agents as identities, scope their world with ReBAC, and ensure your IAM stack is professionally managed to keep up with the AI-driven pace of discovery. The future of the internet is agentic; make sure your security is too.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/1fab2efa-justin_headshot-600x600.avif)

Justin Dolly is Chief Customer and Security Officer at Ory, overseeing the company’s long-term security strategy as well as customer success. He is a Certified Chief Information Security Officer (CCISO) with more than 20 years of experience in building and...

Read more from Justin Dolly](https://thenewstack.io/author/justin-dolly/)