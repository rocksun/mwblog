**Palo Alto Networks introduced a new approach** to AI-driven observability last week, signaling a shift from dashboards and manual incident response toward AI agents that investigate issues and recommend fixes on their own.

Cortex XCOR is an AI-driven platform designed to deliver the holy grail of observability: automatically root-causing issues and recommending fixes, rather than simply pointing technical operatives to dashboards.

The company has said the foundational scale and cost challenges of cloud-native architectures stood in the way of this happening before now, and pre-AI-boom automation was sluggish. Palo Alto Networks [acquired](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-to-acquire-chronosphere--next-gen-observability-leader--for-the-ai-era) cloud-native observability platform and telemetry pipeline company Chronosphere in January to develop real-time agentic remediation in this vein.

Built by the Chronosphere team inside Palo Alto Networks, Cortex XCOR is designed to transform observability from static dashboards and manual remediation to an AI-first experience that automates both routine and complex investigations.

SVP and GM of observability at Palo Alto Networks, [Martin Mao](https://www.linkedin.com/in/martinmao/), tells *The New Stack* that when an alert fires, Cortex XCOR automatically triggers a specialized agent that autonomously reasons through underlying issues and recommends actions and mitigations.

“We don’t want to keep waking engineers up in the middle of the night to help them make sense of dashboards; to be clear… we don’t want to wake them up at all,” Mao says. “While XCOR defaults to a human-in-the-loop model, engineering leaders can expand its autonomous permissions over time and finally get a full night’s sleep.”

> “We don’t want to keep waking engineers up in the middle of the night to help them make sense of dashboards; to be clear… we don’t want to wake them up at all.”

## The end of dashboard donkey work & troublesome troubleshooting

If technologies like XCOR blossom and proliferate, we might reasonably expect the role of the site reliability engineer (SRE) to evolve beyond dashboard donkey work. As the [AI SRE](https://thenewstack.io/ai-sre-root-cause-analysis/) “role” now starts to emerge, automation will target routine root cause analysis and troubleshooting.

“Right now we’re at the moment where SREs will operate like airline pilots; they can rely on autopilot for smooth flying, but you still need an experienced pilot in the cockpit when something goes wrong. By automating troubleshooting, it frees up time for SREs to focus on more strategic architectural work instead of firefighting,” underlines Mao.

A BairesDev [Dev Barometer](https://www.bairesdev.com/blog/dev-barometer-q3-2026-devs-answering-for-code/) analysis suggests that 42% of developers now report that AI writes at least half their code, up from 12% last year. Clearly, the code creation velocity enabled by this cadence needs to be matched with security-centric oversight.

> “SREs will operate like airline pilots; they can rely on autopilot for smooth flying, but you still need an experienced pilot in the cockpit when something goes wrong.”

Palo Alto Networks’ latest offering includes XCOR Operator, an AI assistant claimed to help “operations teams match AI-coding velocity” with contextual relevance. Mao and team have said that what makes the XCOR Operator powerful is that it “understands the user intent” and serves as the conversational interface for specialized agents that execute behind the scenes.

## From pre-defined specs to giving reasoning models access & capabilities

“I was blown away by XCOR Operator’s ability to solve tough problems that went far beyond my initial expectations,” recounts Mao. “It not only changed the way I interact with our platform and observability workflows, but it caused me to fundamentally rethink how we design products. We’re now moving from strong, pre-defined specs for features and workflows to giving the reasoning models the right access and capabilities and allowing them to discover the various paths to reach an answer.”

> “It caused me to fundamentally rethink how we design products.”

Mao explained that, today, the typical user of an observability platform has to play many roles, depending on the total deployment environment. They will be busy investigating incidents, tuning alerts and dashboards, optimizing data volumes, and so on. With Cortex XCOR, each of these roles is mirrored by specialized AI agents optimized to complete those task-specific workflows end to end.

According to [Mao’s blog](https://www.paloaltonetworks.com/blog/2026/10/observabilitys-ai-moment-introducing-cortex-xcor-ai-driven-observability-for-autonomous-response-with-ai-sre/) on this update, the AI SRE agent is triggered automatically when an alert fires and autonomously reasons through underlying issues and recommends actions and mitigations in under three minutes on average, with a 75% success rate of root cause analysis in complex production environments and a further 19% of incidents where the analysis was deemed useful.

## Manual responses can take 20 minutes just to locate

By comparison, manual responses can take 20 minutes just to locate the relevant issues, gather initial context, and find the right on-call engineer.

“We’re pleased with the current average response time of under three minutes as our customers become familiar with this new experience. For now, we start by paging the engineer when an incident occurs, and it typically takes a few minutes for them to log into the platform. In that time, XCOR has already completed the investigation, so three minutes fulfills our current needs,” confirms Mao.

As users build trust in the analysis and increasingly automate remediation, Palo Alto Networks will focus on reducing response time. Mao thinks that the team “already has a good grasp” on what it takes to get there and notes that “cost is an important factor”, along with the steady decline in token prices.

Mao further explained that none of the platform’s automated reasoning is possible without complete end-to-end visibility and context. Palo Alto Networks announced in July its intent to acquire high-fidelity Real User Monitoring firm Embrace, and plans to bring what it calls front-end RUM (XCOR RUM) together with its own in-house XCOR Synthetics and its backend and infrastructure observability to deliver a full-stack platform.

## Firefighting forgoes future-proofing & foresight

How bad can things get if software engineering teams miss out on this observability advantage? Mao suggests the worst-case scenario is engineers spending 100% of their time firefighting instead of innovating or delivering for the business. Because troubleshooting is already the most stressful part of an engineer’s job, he believes this could lead to “massive burnout”, a risk the increasing presence of AI-generated code only exacerbates.

“Uncontrolled observability is like a hyperactive puppy. It’s full of promise, but destroys your budget if left unchecked. As cloud-native and AI workloads send telemetry volumes skyrocketing, organizations need built-in discipline. Chronosphere puts those costs on a leash, ensuring teams get total visibility without the runaway bill. This is why data optimization and cost effectiveness remain central to XCOR’s mission,” Mao says.

Underpinning this work towards full-stack visibility is the XCOR Fabric, technology that provides AI agents with real-time application, infrastructure and institutional context.

XCOR Fabric draws its lifeblood from the organization’s knowledge graph (described as a real-time model incorporating infrastructure, applications and business logic), from operational memory (historical context captured from past incident investigations), from user behavior (users here being senior engineers running specific queries and accessing specific dashboards), as well as human knowledge derived from runbooks, documentation, and operational files.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)