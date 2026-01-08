[A recent survey by JetBrains](https://www.jetbrains.com/lp/devecosystem-2024/) of more than 23,000 developers found that nearly half (49%) now use AI regularly for coding and other development-related tasks. Among those developers, 73% report saving up to four hours per week through AI assistance.

But a key question remains: What are developers actually doing with that extra time?

While [large language models (LLMs)](https://thenewstack.io/introduction-to-llms/) have proven remarkably effective as [coding assistants](https://thenewstack.io/ai-coding-assistants-12-dos-and-donts/), especially because developer frameworks are so well-documented, they still have blind spots. LLMs don’t inherently understand an organization’s existing applications, [data models or infrastructure](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/). As a result, the time savings from AI-assisted coding often get redirected elsewhere in the software development life cycle (SDLC).

According to [Atlassian’s “State of Developer Experience” survey 2025](https://www.atlassian.com/teams/software-development/state-of-developer-experience-2025), most developers are reinvesting their AI-driven time savings into improving code quality. That shift makes sense. As AI accelerates code generation, the sheer volume of new code has been increasing, bringing with it a higher need for review, testing and debugging.

[Research from Apiiro](https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/#:~:text=AI%2Dassisted%20teams%20didn%27t,Syntax%20Errors%20for%20Architectural%20Flaws) reinforces this point: Vulnerabilities introduced by AI coding assistants require significant human oversight. The trade-off is clear: Four times faster code generation can come with 10 times greater risk if not properly managed.

## The AI Security Paradox Explained

For developers, AI is being used not just for faster coding but also for [debugging](https://thenewstack.io/how-generative-ai-is-revolutionizing-debugging/) and vulnerability scanning. When used as both a coding assistant and as a debugger, it’s [important to not create a kind of recursive loop](https://thenewstack.io/vibe-coding-when-ai-writes-the-code-who-secures-it/) — AI writing code that’s then reviewed and fixed by the same AI. While efficient in theory, it can also compound assumptions and errors, just like a game of telephone.

In the rush to automate threat detection, code reviews and policy enforcement, security teams are increasingly deploying LLM-based agents to detect [threats like prompt injection, data exfiltration attempts or unauthorized queries](https://thenewstack.io/mitigating-safety-risks-with-ai-powered-applications/). But the same sophistication that makes these models capable of identifying nuanced patterns also makes them vulnerable to the very tactics they’re trained to catch.

For example: The AI system designed to detect prompt injection can itself be manipulated through prompt injection. A malicious actor doesn’t need to breach infrastructure or exploit a buffer overflow — they can simply convince the AI to overlook, reinterpret or “approve” something harmful.

## How the Recursive Security Paradox Unfolds

Let’s walk through a common sequence of events in this new security landscape:

1. **AI flags suspicious input.** An LLM integrated into a developer workflow detects an unusual instruction in a user prompt. It classifies the content as potentially malicious — a clever attempt at data leakage, for example.
2. **The developer asks the AI to explain its reasoning.** The AI’s flag seems overcautious, so a developer asks it to elaborate. Why was this prompt suspicious? The model begins to reason through its decision, generating a natural-language explanation.
3. **An attacker exploits the explanation loop.** The attacker crafts a secondary prompt designed to embed a hidden payload within the AI’s reasoning process. The model, attempting to be helpful, may interpret this input as part of its “analysis” and inadvertently override its own guardrails.
4. **AI explains away the suspicion.** In the worst case, the model justifies the malicious input as safe, allowing it to pass through internal checks. The AI has, in essence, talked itself out of being secure.

This recursive vulnerability — where AI systems manipulate or are manipulated through dialogue — creates an “infinite loop” of trust and deception. However, at its core, this is not a failure of technology; it’s a failure of boundary definition.

## How To Break the Loop for Secure AI Integration

AI systems are conversational by design. They interpret, reason and generate based on context. But when the boundaries between analysis and action are blurred, a [model can inadvertently become part of the attack surface](https://thenewstack.io/evil-models-and-exploits-when-ai-becomes-the-attacker/). Security logic becomes entangled with natural-language logic. And that’s the danger.

Despite the sophistication of today’s models, they are still pattern matchers, not sophisticated arbiters of nuance. They can be tricked, confused or persuaded — sometimes spectacularly.

This means that relying solely on LLMs for threat detection, vulnerability analysis or automated code approval introduces a new layer of systemic risk. For example, model drift can weaken security judgments over time, content poisoning can alter how a model perceives safe or unsafe behavior and adversarial prompts can reverse engineer filters and cause data leakage.

However, if you still want to use LLMs, you need to ensure you are breaking the loop. Enterprises at a minimum must adopt multimodel security reviews, or better yet, multilayered LLM-driven security reviews, to avoid the recursive trap. In addition, the chain of testing and debugging needs a non-AI enforcement mechanism.

## Best Practices for Mitigating AI Security Risks

Here are some practical best practices to apply:

* **Separation of concerns:** AI models that detect should not be the same models that build, explain or enforce.
* **Immutable policies:** Use hard-coded rule sets or non-AI validators for final approval of critical operations.
* **Observability and audit trails:** Every model decision — flagged, approved or overridden — should be logged and reviewed by a human.
* **Prompt provenance tracking:** Maintain lineage of how each input, intermediate response and output was generated and modified over time.

This structure helps ensure that AI remains an intelligent assistant, not the sole authority in the security chain.

## **From AI Loops to Enterprise-Ready Application Security**

While this paradox seems unique to AI, it mirrors challenges developers have faced for decades, particularly in the [Java and Spring framework ecosystems](https://thenewstack.io/spring-ai-transforms-java-for-genai-app-delivery/).

In traditional applications, developers have long relied on layered security: web filters, interceptors, controllers, service-level validations and access controls to guard against injection, spoofing and session hijacking. AI introduces new versions of these same problems, only now they exist in the semantic layer instead of the code layer.

Furthermore, AI-assisted coding has dramatically increased the volume of code commits. Enterprise security teams, already stretched thin for years, require additional support to manage this surge. Leveraging AI for security can help address the increased code volume. Yet, as the distinction between code logic and conversational logic blurs, security teams will still face considerable challenges. AI-assisted coding underscores the need for security models to evolve and shift left.

For developers, frameworks like [Spring Security](https://spring.io/projects/spring-security) can play a crucial role in bridging AI trust boundaries. Spring Security is a comprehensive and extensible support for both authentication and authorization that provides protection against attacks like session fixation, clickjacking, cross-site request forgery and more. When combined with the AI-assisted testing and debugging best practices, implementing an application platform like [Tanzu Platform](https://www.vmware.com/solutions/app-platform/ai) is highly recommended. Such platforms enable organizations to proactively manage the influx of [code generated by AI-assisted coding](https://thenewstack.io/ai-assisted-coding-a-double-edged-sword-for-security/) and maintain risk control.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/06/8c0d7ab0-camille-crowell-lee.jpg)

Camille Crowell-Lee is a solutions marketing leader who focuses on VMware Tanzu by Broadcom. She has been in technology marketing for over 17 years where she has built strategic marketing initiatives for hyperscale cloud providers and for ISVs, including containerization...

Read more from Camille Crowell-Lee](https://thenewstack.io/author/camille-crowell-lee/)