**A joint IDC and Lenovo [study](https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html) reports that 88%** of AI proof-of-concept (POC) projects fail to reach production because of unclear objectives, unprepared data, and a lack of in-house agentic AI expertise. These result in a build-vs.-run split, where the team that designed and deployed AI agents, often an agentic AI partner, doesn’t get to run them over the business processes.

When the operating team, often experienced on demo, uses the agentic system without any external help, errors arise. Operational gaps can cause cascading failures and business catastrophes if a single agent deviates from normal behavior beyond the permissible range.

When asked about estimating whether an agentic AI system is production-ready or limited to demos, Serhii Semenchenko, the CTO of [Dedicatted](https://dedicatted.com/?utm_campaign=367253726-The%20New%20Stack&utm_source=the%20new%20stack&utm_medium=The%20New%20Stack%20Article), a Toronto-based AWS Premier Tier Partner for Agentic AI Specialization, tells *The New Stack*, “The demo is a clean environment where we have clean, prepared data. No edge cases, so everything is defined — input and output. “

He means the demo data is scripted with clean prompts, while the production environment is unpredictable. “Every single step should include the logging, tracing, monitoring, breakers, all the checks, and validation,” he adds. All these steps ensure failure preparedness.

Semenchenko shares a basic production checklist: “every single agent should have a timeout and every single step that agents, like, generate some output should be logged for traceability.” Broadly, he believes agentic AI systems should self-assess in production, decide whether to continue after a particular event or reschedule tasks.

## **Agent as a service**

Semenchenko then compares agentic AI systems to microservices architecture, where each agent has its own permissions rather than static or long-term broad access keys/tokens/credentials. He explains, “Agents use a specific set of permissions and the short-lived key that actually grants access to specific tools, which could be some other services or databases that act as a tool.”

According to Semenchenko, preventing an agent from calling tools that it shouldn’t call prevents data leaks, unintended use, and prompt injection attacks. He adds, “Every single agent should be treated as a separate service.”

To explain multi-agent orchestration, Semenchenko describes a handoff and offers this use case: “A router that gathers the inputs from the user, the system, and the platform — and decides what to do with the input data.”

He further explains that the router can decide what to do with input data, such as escalating to specialist agents for documentation, analysis, video, audio, livestream, etc., each with its own tools, such as third-party APIs.

He talks about the final agent, “that composes the outputs from all these tools and previous agents to provide the required output”. If the final step fails, the composer doesn’t invent the missing piece; it either retries or marks failure. This means that there’s a clean definition of who receives the work, what state survives a step, and what happens if it dies.

## **What persists beyond POC?**

Between all of this, if something corrupts an agent’s memory — known as memory poisoning — he talks about “guardrails”. All documents and data undergo deterministic checks to ensure data validity or trace inconsistencies to records, databases, and duplicates.

---

***Need agentic AI that runs in production, not just in demos? [Explore Dedicatted’s Custom Agentic AI Solutions](https://aws.amazon.com/marketplace/pp/prodview-4ftsk5yecz4qa).***

---

Semenchenko looks back on the multi-agent system they built for [CASSEN Testing Laboratories](https://dedicatted.com/insights/smarter-science-how-dedicatted-brought-agentic-ai-to-chemical-reporting-at-cassen-laboratories), an established chemical environmental testing and occupational health laboratory in Canada, which faced multi-day turnaround times for their reliable reports due to manual regulatory testing and lengthy processing.

The project had clear input and output expectations, but human-related edge cases emerged. He shared that the chemist group had a personal view of how the report and chemical compounds from their error-sample investigations should be presented. Things got even tougher in production when the report style was more in-house than domain-specific.

To solve this problem, Semenchenko reveals, “We adjusted our flow, adjusted the agent that composed this report. So, everything in the final, after these adjustments, reports look the same as if chemists had manually prepared them.”

Agentic AI projects must succeed in migration projects. Zivian Health, a U.S.-based compliance infrastructure for organizations managing NP/PA workforces across multiple states, migrated from [AWS to Azure](https://dedicatted.com/insights/building-a-compliance-ready-cloud-zivian-health-aws-to-azure-migration), a re-platforming under regulatory stakes.

Semenchenko tells The New Stack how AWS and Azure use completely different access systems and where least-privilege permissions matter. “So, everything should be mapped, adjusted, and validated first”, he says.

“The second thing is monitoring.” He reveals they “use cloud-agnostic tools to monitor and trace everything that happens on the agentic AI platform.” He also discusses models that are unavailable on both platforms during migration.

Semenchenko adds, “We should go through a validation suite. You need a data set covering all cases the platform should handle and all requirements. After the migration, you could validate every single agent, use case, and user flow.”

Semenchenko concludes the final stages of agentic AI projects: “Check if you achieve the same success rate, latency, and token cost.” If agentic AI projects succeed, they extend beyond the bubble to business use cases, as [PwC’s AI survey](https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html) found: about two-thirds (66%) of AI agents deliver value and improve productivity.

## **Unexpected 3 a.m. call**

An agent misbehaves at 3 a.m. in a pipeline and does something outside its scope. Semenchenko describes a common scenario where, “An agent could use different tools, and at some moment it could decide that the output of one tool is not enough, and will try to call it, like, 2, 3, 5 more times. Every single time it will decide that it’s not enough; it should call again, maybe some new data will appear.”

According to Semenchenko, certain breakers flag agent misbehavior. They use advanced monitoring to track anomalies; as he explains, “It will throw the error into the monitoring system.” The operator, based on the managed services contract — either the agentic AI partner or the client’s team — receives the alert.

When the operator is an agentic AI partner, Semenchenko shares, “We have dashboards, alerts, and then it depends on the client and depends on our responsibility.” He adds, “We actively monitor the system, and we could actively react to such cases that appear during the night.”

If the operator is the client team, he shares, “In other cases, the client will receive some error messages that we detected some anomalies, and something went wrong.” As a solution, the clients would use runbooks provided by the [partner] developers to tackle the 3 a.m. misbehavior themselves.

The benefit of having a partner operate agentic projects is continuous monitoring, handling unexpected events, and reporting. The partner takes full recovery responsibility and reduces the burden on the in-house team by immediately stopping the agent or revoking access — without waiting for morning. Furthermore, partners investigate edge cases to prevent future issues.

## **Commercial reality of agentic AI**

[Denys Yermakov](https://linkedin.com/in/denys-ddcttd?originalSubdomain=ca), the CEO of [Dedicatted](https://dedicatted.com/?utm_campaign=367253726-The%20New%20Stack&utm_source=the%20new%20stack&utm_medium=The%20New%20Stack%20Article), believes agent failure is often quieter on the commercial side. “You will have to have in place a lot of monitors, regression tests, other tests, different prompts, and different behavior of the agents,” he says.

According to Yermakov, how the company ships fixes matters as much as detection. He then points to outages caused by infrastructure issues or bad deployments. “The price of failure is going to be much higher compared to other platforms,” he says.

For change management, Yermakov emphasizes “Flexibility for the [Agentic AI] solution and adaptability for all the future change requests you might have.” He then talks about questioning the agentic AI partner about the project scope and discussing ownership of the code and platform. This matters because the team will eventually have to handle incident response and maintenance.

> “The demo is a clean environment where we have clean, prepared data. No edge cases, so everything is defined — input and output.”

Yermakov then opens some cards for verifying the right agentic AI partner’s expertise: “You can always start with some small piece of the POC concept or with a small piece of the demo environment, and the way the partner delivers that, that is crucial.” That would draw a fine line between a red flag service reseller and a green flag — real service provider.

“Because this part has to be delivered on real data, with a real workflow and with real challenges you face in your business. Not based on some mock data,” as he believes a predefined demo scenario irrelevant to the client’s business case is usually a reseller.

Yermakov gives a thumbs up to a partner who faces challenges on the client data layer during demos. “If the [agentic AI] partner comes with the right questions and approach, the right partner is here,” he adds.

## **Security stones for agentic AI success**

According to a [Modern Data Company](https://itbrief.news/story/ai-agents-outpace-trust-in-enterprise-data-survey-finds) survey, 75.9% of enterprise data leaders and practitioners across 66 nations cite data quality and trust as barriers to AI systems reaching production.

When asked about sensitive data shared among partners, Yermakov shares the business perspective, “It’s so important that your data stay within your perimeter and not leave your secure perimeter, which you already have in your platform.” He explains that traditional businesses with large-scale on-premises data face a challenge in adopting agentic AI because providers might use their data to train public models.

Semenchenko shows a technical picture of how they delivered a couple of healthcare projects where personally identifiable information (PII) around health is critical. He says, “The problem was that this PII shouldn’t be stored anywhere.” He explained how every agent would need this data to extract or process outputs.

Solving this problem, he adds, “We have an additional layer that actually cleans all the PII data from the output of agents. The traceable data goes to the observability platform. So no PII data in logs and monitoring.”

## **Build vs. hiring partners**

Yermakov emphasizes how new agentic AI is to enterprise systems. He tells TNS that enterprises are stuck on basic questions, like: “How do you have to set up everything? What should the platform look like? What are the benefits? What is the cost of users for this platform?”

AI partners have experience shipping systems after overcoming challenges. “They know how to solve problems and how to build some of the platforms efficiently with pretty predictable scenarios”, he adds.

“It’s quite important to build and architect all the platforms from the very beginning in the very right way, to not redo what you’ve implemented into the business processes.”

The operational reality hits during platform maintenance, which, according to Yermakov, must be adaptable and adjustable. He believes it’s critical to avoid early failures in every agentic AI project. “It’s so important to build your team, to build your knowledge in-house,” he says, talking about future platform maturity.

Further explaining whether to go in-house or outsource agentic AI projects, Yermakov says, “Once you figure out the area where you benefit the most from the AI, you have to think about this process from two different perspectives. From the business process of how the company operates on the business side and from the technical challenges you face.”

Yermakov shares the key to agentic AI project success — staffing — “Always the team effort of the in-house resources and the outsourcing resources.” He warns enterprises, “Outsourcing everything is not going to work for you because the outsourcing partner can’t understand your business in a very detailed way.”

Yermakov says SMEs and partners must engage from the start to achieve optimal knowledge transfer. The in-house team should own and safeguard the business process, while the partner architects and operates the core runtime.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/e86f3866-cropped-874219b8-bf2b0e02-00b9-4a36-958c-b76f1796dfe5-600x600.jpeg)

Venus Kohli is an electronics and telecommunications engineer turned technical content writer. She covers everything related to electronics, IT, and her favorite, quantum physics, for the engineers and decision-makers who build the technology. During college, her group project resulted in...

Read more from Venus Kohli](https://thenewstack.io/author/venus-kohli/)