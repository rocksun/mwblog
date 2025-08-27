Interest in generative AI (GenAI) is transitioning from developing models to creating agents that autonomously perform a broad range of tasks. But trouble awaits those unleashing the capabilities of [agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) without a firm grip on end-to-end reliability.

“Unreliable agents are not simply inefficient; they represent a significant source of operational, financial, legal and reputational risk,” [Mohith Shrivastava](https://www.linkedin.com/in/mohith-shrivastava/), principal developer advocate at Salesforce, told me in an interview. “With agentic AI being deployed at scale, reliability becomes the central architectural principle.”

## Avoiding the AI Agent ‘Reliability Tax’

An unreliable agent introduces far more than mere inefficiency. It is a liability that can trigger operational breakdowns, legal exposure and reputational damage. Shrivastava calls this the “reliability tax.”

Too many of today’s AI applications and agentic AI deployments are brittle, inconsistent and demand constant oversight. Hence, organizations face an ongoing investment in guardrails, retrieval pipelines, monitoring, governance and security hardening to fix unforeseen AI issues and prevent inaccuracies and hallucinations.

“We’ve moved from deterministic automation — where a system executes preprogrammed rules — to probabilistic autonomy, where agents perceive, reason and act on their own,” said Shrivastava. “This brings incredible potential but also introduces [entirely new failure modes](https://thenewstack.io/mcp-a-practical-security-blueprint-for-developers).”

## The 5 Pillars of Agentic AI Success

He stresses that reliability is a multidimensional element composed of five pillars:

* **Predictability:** Consistent actions within defined bounds.
* **Fidelity:** Accuracy grounded in verifiable sources.
* **Controllability:** Following explicit instructions and constraints.
* **Robustness:** Resilience in messy or adversarial conditions.
* **Safety and security:** Avoiding harm and resisting malicious exploitation.

Many designers do well on some of these pillars. But each one is essential. If one fails, cascading breakdowns are inevitable.

## Preventing Scope Creep and Hallucinations

Adherence to sound reliability principles must be balanced with the need to avoid scope creep. Shrivastava recommends beginning with a strategic scope definition before you build. That definition can then be enforced with:

* Zero trust identity and access control
* Tool use allowlists
* Human-in-the-loop checkpoints
* Logging and monitoring
* Emergency kill switches

Hallucination can be addressed with techniques like [Retrieval-Augmented Generation (RAG)](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary) without requiring model retraining. This helps reduce the amount of hallucination, whether it is in terms of faithfulness errors (contradicting context) or factuality errors (contradicting reality).

## Moving Beyond Prompt Engineering

Prompt engineering techniques like [chain-of-thought](https://towardsdatascience.com/short-and-sweet-enhancing-llm-performance-with-constrained-chain-of-thought-c4479361d995/) or [self-consistency](https://towardsdatascience.com/achieving-greater-self-consistency-in-large-language-models-6e6cb5f3c5b7/) are designed to ensure that agents follow commands. For true instruction adherence, however, developers must embrace context engineering. Just as prompt engineering goes well beyond simple prompting by carefully considering context and structure, context engineering architects the full context using a rigorous, iterative approach that optimizes instructions to ensure they achieve the desired result.

“Context engineering is the art and science of giving an AI agent the right information, the right tools and the right instructions, so that the agent is able to accomplish the given goal. Think of context as the agent’s runtime ‘RAM’ — the prompt, instructions, retrieved data and history,” said Shrivastava. “Overload it, poison it or create conflicts, and reliability suffers.”

Developers need tools they can use that put context engineering into practice. Such tools must be able to define topics that capture the exact tasks to be accomplished so that the AI agent understands the scope, triggers and desired outcomes for each scenario. These topics provide the structure for when and how the agent should act, ensuring that responses remain relevant and aligned to business goals.

From there, added Shrivastava, agents should be equipped with effective tools to accomplish a given goal. Memory can then be efficiently managed by summarizing ongoing conversations and reusing that context through prompt templates, conversation variables or context variables. As a result, diligent prompt engineering can refine the agent’s behavior within the framework of topics, instructions and scopes — and retrieval via RAG can dynamically [pull in relevant data](https://thenewstack.io/beyond-ai-models-data-platform-requirements-for-agentic-ai) to deliver precise, context-aware responses while keeping the context window optimized.

“Enterprises need a platform that provides all of the tools to accomplish the many aspects of context engineering in a way that is simple to manage,” said Shrivastava. “This must include built-in guardrails and governance that evaluates how well agents interpret topic instructions when generating responses.”

With all of these steps in place, it remains critical that agent performance is closely monitored and measurable. Developer tools, therefore, should provide deep observability, live health monitoring, consumption tracking and rich adoption analytics to support the validation and steady improvement of outcomes. For example, service agents configured with Agentforce from Salesforce have a feature to report the percentage of resolved conversations, escalations and abandoned conversations. Similarly, sales agents that come out of the box with Agentforce have analytics to report how sales revenue is impacted by the agent.

## The Right Platform and the Right Tools = Reliability

For enterprise agentic AI, reliability is no longer an optional feature. It has become a fundamental part of any architecture. This shift is necessary because agents now operate on probabilistic autonomy rather than deterministic scripts.

Achieving agent reliability requires a disciplined, end-to-end approach that goes beyond simply using the model. According to Shrivastava, it involves:

1. **Context engineering:** Carefully defining the agent’s scope, actions, memory, prompts and RAG usage.
2. **Tight governance:** Implementing strict controls like [zero trust security](https://thenewstack.io/what-is-zero-trust-security/ "zero trust security"), approved action lists (allowlists), human oversight (human-in-the-loop, or HITL) and comprehensive logging.
3. **Continuous evaluation:** Constantly monitoring and testing the agent’s performance in real-world scenarios.

“Organizations must plan for the ongoing cost of maintaining guardrails, data pipelines, testing and observability,” said Shrivastava. “Platforms that provide built-in tools for evaluation, RAG and performance analytics can help reduce this cost and enable the development of more advanced, self-correcting AI systems.”

Agentforce from Salesforce has built-in tools to help enterprises deploy agents at scale. The [Testing Center](https://www.salesforce.com/news/press-releases/2024/11/20/agentforce-testing-center-announcement/) part of Agentforce, for example, lets teams run scenario-based, dataset-driven evaluations (including synthetic test cases) in a sandbox before going live. This way, they can surface failure to follow instructions and tool-use errors early — shrinking the reliability tax. Agentforce provides all of the tools needed to implement autonomous AI agents at scale while adding the guardrails, governance and control called for in enterprise operations.

For more information, visit [Agentforce](https://www.salesforce.com/agentforce/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/08/302edea8-drewrobb.jpg)

Drew Robb has been a full-time freelance writer for more than 25 years. He specializes in IT, engineering and business. He has written hundreds of articles for The New Stack, Datamation, eWeek, Tech Republic, Power Magazine, World Trade and more....](https://thenewstack.io/author/drew-robb/)