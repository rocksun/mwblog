Operational fatigue, in the face of increasing complexity and risks, is a real problem. Can partnerships with skills-based AI agents offer a solution?

AI has quickly become a trusted collaborator or “copilot” throughout the software development lifecycle. Particularly in the operations space, sysadmins, DevOps, and site reliability engineering (SRE) teams have embraced conversational, prompt-based AI to aid in the still overwhelmingly manual execution of incident response. Generative AI is enabling operations and security teams to shift further from TicketOps.

Until now, the security, compliance, and always-on requirements of most ops teams have left them reluctant to move to the next stage of agentic AI. That could be about to change.

In the face of enterprise IT complexity and sprawl, [Phanidhar Koganti](https://www.linkedin.com/in/networkleader/), senior distinguished technologist in [Hewlett Packard Enterprise (HPE) hybrid cloud](https://www.hpe.com/uk/en/home.html), tells *The New Stack* that ops is entering its “Agentic Era,” where AI agents have specialized knowledge, capabilities, and workflows, referred to as [agent skills](https://agentskills.io/home). These agent fleets work to bridge persistent enterprise data and operational silos and, when expressly permitted and auditable, can take autonomous actions based on goal-oriented reasoning.

“The AI is able to point them in the right direction,” Koganti explains, but then “the human operator has to build trust by verifying.”

In his whitepaper “[**Copilots to Operators: The Agentic Evolution of Enterprise IT,**](https://www.hpe.com/psnow/doc/a00157919enw)” Koganti contends that this change must occur with the human operator in the loop, serving as the orchestrator.

HPE is releasing an enterprise-grade, multi-domain agentic operations system, including its agentic operations copilot, now in beta, as part of the OpsRamp IT operations management platform. Expected to go generally available later in 2026, this agentic ops application has, for some early adopters, cut time to root cause by at least half.

> Expected to go generally available later in 2026, this agentic ops application has, for some early adopters, cut time to root cause by at least half.

AI, as the amplifier of everything, has only made establishing AI for DevOps more urgent, as always-short-staffed operations teams scramble — and sometimes fail — to keep up with the speed of AI-produced code, and its inherent security risks. AI is likely the solution to this problem, as the data show.

## **Pressure is on for ops teams**

[Fewer than half of enterprises](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html) believe they are operationally prepared for AI adoption across infrastructure, data, risk, and talent. Which means so much of the success or failure of AI at scale rests on the shoulders of already overworked operations teams.

Respondents of a [recent study of cybersecurity and operations leaders](https://gurucul.com/blog/2025-pulse-of-ai-powered-soc-transformation-report-out-now/) find that the most pressing issues (they could select more than one) are:

* Alert fatigue – 76%
* Burnout and staffing shortages – 73%
* Manual and time-consuming alert investigations – 64%
* Tool sprawl and complexity – 59%
* Evolving threats outpacing detection – 55%

[Osterman Research](https://www.dropzone.ai/blog/osterman-report-2024-soc-trends-challenges-and-solutions) finds that 40% of alerts in large enterprises are never investigated due to sheer volume, while 73% of organizations experienced outages in 2025 that were directly linked to these ignored or suppressed alerts.

This increases exponentially alongside system complexity.

For the majority of enterprises taking the hybrid or multi-cloud route, a staggering [two-thirds lack confidence in real-time threat detection](https://campustechnology.com/articles/2026/02/04/cloud-complexity-outpacing-human-defenses-report-warns.aspx%2523:~:text=Despite%25252520rising%25252520budgets%25252520(62%25252525%25252520expect,tool%25252520sprawl%25252520absorbing%25252520investment%25252520gains.) and response capabilities. This [technological complexity is a direct driver of emotional exhaustion](https://www.researchgate.net/publication/384334140_The_impact_of_techno_complexity_on_work_performance_through_emotional_exhaustion). While engineers are likely to push through in the short term, it creates a cognitive drag that leads to long-term attrition. These highly specialized ops roles have always been tough to fill, and organizations are losing important shared institutional information.

Beyond employee retention, ops burnout also negatively impacts productivity and incident response time, increasing the likelihood of avoidable mistakes.

All while cybersecurity risks and code-generation speed are way up. It’s more code, more alerts, and simply not enough people.

## **Agentic root cause analysis**

Agentic AI for DevOps — the application of agentic AI solutions to operational tasks — offers an opportunity to help human operators lighten their workload, reduce alert noise, and dramatically improve response time.

But AI isn’t a silver bullet. Instead of reducing manual triage, many AI tools increase alert noise, which further erodes trust in the technology. A worrying [66% of AI tools are known to generate false positives](https://www.sans.org/white-papers/sans-2025-ai-survey-measuring-ai-impact-security-three-years-later), which only increases stress and errors. Stale data within models and a lack of transparency in how AI makes decisions are among the reasons for these false positives.

To create transparency across complex, distributed systems, any enterprise-grade operational agentic AI solution must break down cross-organizational data silos. Platform engineering has emerged as the preferred pathway not only to unite disparate data sets but also to establish guardrails and gates for quality, security, and compliance — for both human and agentic developers.

The [HPE whitepaper](https://www.hpe.com/psnow/doc/a00157919enw) contends that, when it’s done right, agentic operations can:

* Overcome ops silos with persona-based explainability
* Bridge data silos while reducing data duplication
* Enable proactive operations with multi-variate predictive analytics, like for adaptive thresholds
* Reduce operator burnout
* Avoid blind spots
* Track changes with auditability

Results from the HPE beta program for its agentic operations copilot show that AI agents make particularly good partners for root cause analysis, helping overcome blind spots. An ops team simply cannot know every release that happened in an enterprise environment across any given week, while machines don’t sleep and AI is particularly good at pattern recognition, as well as cross-organizational memory.

“During our beta program, a lot of our customers have told us that many issues that happen will typically be related to a change they made four or five days previously,” Koganti says. “They explicitly want us to track the changes they are making and take that as an additional context when agentically root case analyzing a particular issue.”

The whitepaper outlines the planning stages of how an agentic operator investigates across its root cause analysis:

* OODA feedback loops – observe, orient, decide, act
* Hypothesis generation – including extraction of metrics and logs
* Agentic skill dispatch – like a “trace analysis skill” can be applied to isolate a faulty microservice, a “metrics analysis skill” can be called upon to identify covariants and deviating patterns
* Synthesis – the agent presents a narrative, both of what it has found to be the likely culprit, and what it has ruled out

As SREs, DevOps, and sysadmin teams bring important institutional knowledge that is also fed back into the agentic memory, enabling both agents and humans to improve their cross-organizational understanding.

## **Skills-based AI agents**

The trick, Koganti argues, is not to apply a general large language model (LLM) to the specifics of enterprise operations. That’s where operational agent skills come in.

“You are not giving it 100% of the details, but you’re giving it high-level guidance on the skeleton. In the operations world, let’s say you get a particular type of alert with a particular symptom, like virtualization issues, then you know you have a knowledge or a skill saying that: For these kinds of alerts related to virtualization, you want to go and look at the CPU utilization in the VM and look at the storage IO with respect to a particular other detail and so on,” Koganti explains. “Providing high-level directional guidance, captured in skills,” is necessary, “because all this agentic stuff, if you leave it 100% to LLMs, they hallucinate anything.”

Agent skills are already popular among developers. HPE is trying to bring it to operations.

“That’s a unique thing, and we believe it’s only a matter of time until the rest of the vendors in the market will also align with that, similar to how Infrastructure as Code was adopted primarily from the developer side of the ecosystem at first,” he continues, as they look to encode curated ops skills past root cause analysis and incident investigation to include specific ones to deal with virtualization and networking.

## **Agentic auditability is key**

AI in ops has to work to close the trust gap. For compliance, cybersecurity, and operators’ demands, AI agents must be able to explain and substantiate their thought processes.

With this in mind, HPE’s brand of autonomous operators is being built with an audit trail, reasoning, and observability.

### Full audit trail

* Every conversation persists with tenant isolation
* User attribution per message, who said/did what
* All API calls are audit-logged through MCP tool invocations within the IT operations platform

### Transparent reasoning

* Hypotheses shown before conclusions
* A step-by-step plan is visible to the user
* Sources cited for every insight
* Tool calls disclosed with what data was queried

### Observability and traceability

* OpenTelemetry-based agent execution traces
* Decision path logging — why this agent, why this tool
* Reproducible evaluations that ensure the same inputs result in the same reasoning path

“Operators do get burnt out, especially in high pressure moments when these issues typically happen, and they do make a lot of mistakes, whereas the machine doesn’t miss a piece of data, doesn’t make any mistakes in gathering the right pieces of data, as well as doing a very fast and objective analysis,” says Koganti, on the value of agentic root cause analysis.

However, the HPE team is not going all in on agentic-driven remediation just yet. The AI operations agent will make a suggestion, but it won’t act without permission. Even so, this approach can cut the often-frustrating time to discover the root cause by up to half.

“The actual remediation, which involves, perhaps, touching the particular deployment — let’s say you want to reboot something — is up to the operator. OpsRamp does have the ability to automatically trigger selective fixes,” he continues, “that must be configured by the human. None of our agents will take autonomous actions. It is policy-driven, and that policy will be that it is human-configured.”

As the report contends, by adopting agentic skills, enterprises are beginning to move away from reactive fixes toward the proactive building of systems that fix themselves.

***Learn more about HPE’s agentic operations copilot feature in its new whitepaper, “[Copilots to Operators: The Agentic Evolution of Enterprise IT.](https://www.hpe.com/psnow/doc/a00157919enw)”***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)