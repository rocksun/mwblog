AI agents are reshaping software development. They can autonomously read codebases, write and edit files, run tests, and fix bugs, all from a single prompt, and you don’t even have to write the prompt yourself anymore. Before long, they’ll handle everything from booking business travel to processing procurement requests, using your credentials to get it done.

That’s powerful. It’s also a significant responsibility, and it poses distinct risks that software companies urgently need to address. The Center for AI Standards and Innovation, an arm of the National Institute of Standards and Technology (NIST), has grown sufficiently concerned about [agentic AI](https://thenewstack.io/playing-dd-with-ai-the-agentic-ai-developers-achilles-heel/) risks to begin studying how to track the development and deployment of these tools.

“AI agent systems are capable of taking autonomous actions that impact real-world systems or environments, and may be susceptible to hijacking, backdoor attacks, and other exploits,” [NIST](https://www.regulations.gov/document/NIST-2025-0035-0001) notes in a document on the topic. “If left unchecked, these security risks may impact public safety, undermine consumer confidence, and curb adoption of the latest AI innovations.”

Agentic AI reshapes and expands the attack surface, including agent-to-agent interactions that traditional security models were never designed to detect. It also links low-severity vulnerabilities together for a high-severity exploit.

> “Engineering leaders eager to use agents should understand not only what agents can do, but what agentic capabilities mean for their organization’s security posture.”

Security teams are already acutely aware of these risks, or should be. Engineering leaders eager to use agents should understand not only what agents can do, but what agentic capabilities mean for their organization’s security posture.

Understanding AI’s risks bridges the gap between engineering teams and their security counterparts, enabling teams to ship faster and more securely.

## Why agents change the threat model

The nature of large language models — and agentic AI in particular — creates a variety of security challenges, some entirely new, others twists on long-standing issues.

AI agents face some risks shared with other software, such as exploitable vulnerabilities in authentication systems or memory management processes. But NIST’s focus is on the novel, more dynamic dangers posed by machine learning models and AI agents.

One of the biggest risks of AI, [prompt-injection attacks](https://thenewstack.io/when-prompt-injections-attack-bing-and-ai-vulnerabilities/), is made significantly more complex by the non-deterministic nature of LLMs. This means that the same prompt-injection attack may succeed or fail on different attempts, making remediation difficult to validate and comprehensive defenses challenging to implement.

There’s a particular risk for models that include intentionally installed backdoors, leaving critical systems vulnerable. There are also concerns that even uncompromised models could pose a threat to the confidentiality, integrity, or availability of critical data sets.

Another challenge arises from the combination of capabilities within a single agent. AI agents merge language-model reasoning with tool access—the ability to read files, query databases, call APIs, execute code, and interact with external services.

The risks emerge not from any single capability but from their combination and an agent’s ability to execute these actions autonomously. Without proper guardrails, agents can delete codebases, expose sensitive data, and introduce cascading failures that are costly and difficult to unwind. Agents can even work around some guardrails to complete their assigned task.

> “The risks emerge not from any single capability but from their combination and an agent’s ability to execute these actions autonomously. Without proper guardrails, agents can delete codebases.”

Agents are more likely to be affected by these issues when they have access to private data, are exposed to untrusted content, and can communicate externally. This presents a materially different risk profile than one lacking any of these three elements. Some observers have described the combination as the “[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/).”

Additional risks include:

* **Unintended operations**, where agents execute actions beyond their intended scope due to misinterpreted instructions or prompt manipulation.
* **Privilege escalation** occurs when agents operating with broad permissions perform sensitive operations that exceed what the initiating user authorized.
* **Cascading failures**, where one compromised agent in a multi-agent system can corrupt others downstream.

## How to engineer against these risks

All of these risks have concrete countermeasures. The most effective approaches layer controls at three levels.

1. **Model level:** Maintain clear separation between system instructions and untrusted content using distinct messaging roles and randomized delimiters. Secondary classifiers provide an additional layer, scanning inputs and outputs for injection patterns and anomalous formatting. These are risk-reduction measures rather than complete solutions, which is precisely why the layers below matter.
2. **System level:** Apply least privilege across the board. [Agents should only access](https://thenewstack.io/agentic-access-is-here-your-authorization-model-is-probably-broken/) the tools required for their tasks, with credentials narrowly scoped and set to expire quickly. Inspect content entering the system for injection patterns, and screen outbound content for sensitive information such as credentials or PII. Enforce default-deny network controls, limiting external communication to explicitly approved endpoints. And design workflows to break the lethal trifecta – separating read-only and write-capable agents ensures no single agent can access sensitive data, process untrusted content, and communicate externally all at once.
3. **Human oversight level**: Require explicit approval for critical operations while allowing lower-risk actions to proceed with notification. Tiering your approach prevents approval fatigue that can lead to bypassed oversight. Users should be able to halt execution at any time, with rollback of partially completed work where possible. When an agent acts on behalf of a user, record both identities and evaluate permissions at their intersection. Log all agent actions, timestamps, identifiers, tools invoked, resources accessed, and outcomes, in sufficient detail to reconstruct events after the fact.

## Governance as a competitive advantage

The good news is that teams can meaningfully reduce these risks through layered controls. The risks are real, but so is the opportunity, and it would be a mistake to let one obscure the other.

Consider what agents look like when working for you rather than against you – including risk classification for your repositories and upcoming work. The right combination of data access, content processing, and external communication, when properly governed, is exactly what makes agents powerful tools. AI agents can monitor systems, apply consistent security rules without fatigue, and build quality, secure code at a speed and scale no manual process can match. They’re a force multiplier, but it works both ways, amplifying your weaknesses just as readily as your strengths.

Software engineers will always be necessary, but organizations that deploy agents with the proper governance and guardrails will have a meaningful advantage over those that don’t: faster development, faster remediation, and fewer security errors that damage software quality. The same combination that creates the lethal trifecta, when properly governed, is exactly what makes agents powerful tools.

Organizations that get the most from agentic AI will be those that clearly understand the threat model and build against it from the start. That understanding is what separates teams that deploy agents responsibly from those that learn the hard way.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/46e57e72-cropped-9c7b05d4-michelle_gill.jpeg)

Michelle Gill combines strategic vision with hands-on expertise to build and guide high-performing engineering teams within DevOps and the rapidly evolving fields of AI and data science. Currently at GitLab, she drives innovation in AI-powered workflows that enhance efficiency and...

Read more from Michelle Gill](https://thenewstack.io/author/michelle-gill/)