Board members and senior executives are pushing hard to accelerate AI adoption. As a result, significant numbers of organizations have moved quickly from experimentation to deployment, with [95% of US companies](https://www.bain.com/insights/survey-generative-ai-uptake-is-unprecedented-despite-roadblocks/) now using generative AI. However, the speed is beginning to outpace control.

The next wave of adoption centers on AI agents, with [62% of organizations already experimenting with them](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai). The efficiency and productivity gains coming from AI Agents are very real, especially in operational work. Because agents can autonomously make changes within enterprise systems, they have the potential to increase the pace of change across IT organizations. But this is a fast-evolving field, and without a robust governance framework, AI agents can expose organizations to fresh vulnerability. So how can organizations move fast and efficiently without adding risk, while ensuring they have the proper safeguards in place?

> “The efficiency and productivity gains coming from AI Agents are very real, especially in operational work.”

The potential for organizations to successfully establish effective AI governance typically rests on five core pillars.

## Pillar 1: People-first governance

As organizations shift to AI-driven operations, people should remain central as orchestrators of agents. AI can augment human capability, broaden scopes, and accelerate existing processes, but high-impact actions and decisions should remain subject to human oversight. Any action with business impact, potential risk, or no record of successful prior execution should default to human-in-the-loop review or to transparent execution. This includes changes to Tier 0 services, where it is not so much about the nature of the change (code, config, etc.) as about the potential impact on the business when Tier 0 services fail.

A people-first governance framework encourages transparency, accountability, and clear ownership over AI agents. Defined ownership and escalation routes enable seamless handover to human responders and accelerated remediation in the event of an AI incident.

## Pillar 2: Guardrails

Organizations should define a set of permitted, reviewed, and in some cases prohibited actions for [AI agents](https://thenewstack.io/ai-agents-or-skills-why-the-answer-is-both/) to mitigate risk. Responsibility for defining these actions sits at the executive level, typically with the office of the CISO, CTO or CIO. Permitted actions that pose minimal risk to systems should be encouraged to cement agents’ adoption and provide experience for handling more complex cases. Guardrails should be managed carefully for agents that access restricted environments or handle confidential data. High-risk activities, such as writing to critical systems or making changes, should require human oversight.

AI systems based on LLMs (with transformer architectures or similar) carry a risk of hallucinations, even when the temperature is set to zero. When agents generate inaccurate information, the consequences can extend beyond incorrect outputs to inappropriate system actions or misguided remediation attempts. Governance frameworks must account for those possibilities by clearly defining tool capabilities, usage boundaries, and escalation paths. If hallucinations occur, guardrails and evaluations should be reviewed and then fine-tuned.

## Pillar 3: Secure by design

While human oversight and guardrails strengthen governance over active AI agents, organizations must build agents to be secure by design from day one. This involves three core practices:

* **Apply the principle of “least privilege”**: Developers should grant agents the minimum access required to accomplish their tasks, while also limiting access to sensitive systems.
* **Ensure traceability and oversight**: Any interactions agents have with internal systems and tools require clear audit trails. This visibility is crucial whenever an agent makes a decision, as it can reveal flaws or incidents that require remediation.
* **Enforce authorization controls**: AI agents require authorization to use any tool or pass certain tokens. Engineers must implement this safeguard at the agent level, ensuring that any agent that goes to live deployment can introduce no new security risk.

## Pillar 4: Transparency

Organizations must embed transparency throughout AI-driven systems so that any harmful or unintended decisions can be analyzed. In practice, this means ensuring all agent activities are observable, including prompts and instructions, tool access, and resulting outcomes.

Transparency also requires each agent’s decision pathway to be understandable. This includes documenting inputs, data sources, and intermediate steps to reduce the risk of opaque system outputs. Clear traceability makes it easier for engineers to conduct [root cause analysis](https://thenewstack.io/machine-learning-for-automated-root-cause-analysis-promise-and-pain/), understand why an agent made a decision, and remediate as necessary.

## Pillar 5: Performance monitoring

The final pillar of AI governance is performance evaluation. At an engineering level, there are two important key metrics to consider as part of the service-level objectives set for AI Agents: did the agent succeed in the task, and how autonomous was the agent? To assess autonomy, engineers should [evaluate every action an agent took](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/) to gauge whether it encountered any blockers or needed human intervention. Together, these metrics create a baseline understanding of each agent’s performance and effectiveness.

At the board level, performance monitoring is focused on business impact. Executives want to measure productivity gains, time saved, and improvements in operational efficiency. Risk reduction can also be quantified by assessing how quickly critical alerts are flagged or by measuring incident response times. These metrics enable leaders to demonstrate the tangible business value of AI agents.

## Laying the foundation for the AI operations revolution

AI-driven systems are the next frontier in operations management. Companies that learn how to use AI agents effectively will be better equipped to succeed in today’s market. To win, enterprises need a governance framework that fosters innovation at speed while reducing the risks associated with this new way of working. Without robust governance, organizations risk agent malfunctions, accountability gaps, and eroded trust.

> “Without robust governance, organizations risk agent malfunctions, accountability gaps, and eroded trust.”

Building effective governance frameworks requires full organizational buy-in. Leaders across departments such as finance, marketing, IT, and DevOps must take responsibility for how AI is deployed in their own domains to strike a balance between innovation and security.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/04/42adea86-joaofreitas.png)

João Freitas is general manager and engineering lead for AI at PagerDuty. With about 20 years of experience in software development, machine learning and as a people manager, he was previously CTO at an AI startup and has taken several...

Read more from João Freitas](https://thenewstack.io/author/joao-freitas/)