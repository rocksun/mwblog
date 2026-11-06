**AI is becoming woven into the fabric of digital operations** and incident management. On the one hand, AI can detect, triage, and remediate incidents faster, improve coordination between teams, prevent repeat incidents, and drive process redesign. In some organizations, AI is already moving beyond assisting teams to acting on their behalf, as agents pave the way for autonomous digital operations.

On the other hand, greater autonomy also introduces greater risk. Unlike traditional software systems, [AI-powered incident management](https://thenewstack.io/when-ai-fails-the-new-reality-of-incident-management/) tools and agents fail in ways that traditional ITOps and DevOps teams aren’t used to – less predictable and harder to detect. AI has specific failure modes, including hallucinations, groundedness issues, model drift, guardrail violations, or poor tool selection. When these incidents happen, there is often no big-bang failure to set alarm bells ringing. Instead, errors cascade across services into major issues, especially in multi-agent systems.

> “When these incidents happen, there is often no big-bang failure to set alarm bells ringing. Instead, errors cascade across services into major issues.”

The good news is that organizations can mitigate these risks by focusing on four key areas.

## 1. Deploy guardrails



No two organizations are at the same level of maturity when it comes to AI integration. Some are in the adoption and experimentation phase, while others are building ultra-complex workflows with whole [networks of specialized agents](https://thenewstack.io/openai-cursor-coordinator-agents/). The more autonomy an agent has, the further a single bad decision can travel before anyone notices.

As organizations’ AI use matures, they need guardrails in place to enforce policy and limit risk. That includes implementing controls to ensure agents stop, self-report, or hand off to a human when they start to drift from their intended behavior. ITOps and engineering teams can then intervene before small problems become significant ones. These controls must contain risk without creating unnecessary friction for engineering teams.

## 2. Use AI agents to monitor and respond

As organizations deploy larger numbers of agents, monitoring their behavior becomes too complex for humans alone. That creates a need for a new layer of oversight in the form of agents designed to monitor other AI systems. By assessing the signals AI systems generate, monitoring agents can identify abnormal behavior and determine when an issue needs to be escalated to a responder. In agentic systems, this responder may not be a human operator, but another AI agent designed for incident mitigation. [Almost 70% of incidents](https://www.techjournal.uk/p/pagerdutys-ai-chief-says-outage-response) stem from changes, so when AI is making changes at machine speed, organizations need to respond at the same pace.

> “Almost 70% of incidents stem from changes, so when AI is making changes at machine speed, organizations need to respond at the same pace.”

Consider a Site Reliability Engineering (SRE) agent designed to investigate as soon as it detects a system anomaly. By the time an on-call engineer is notified, the SRE agent could be investigating, triaging, and diagnosing. Connecting the agent to code, telemetry, infrastructure, and collaboration tools makes those investigations more accurate. Where an incident is a repeat, the agent could also trigger pre-approved mitigation workflows. That provides a pathway to AI-assisted incident management and, eventually, self-healing agentic systems.

## 3. Identify metrics

To know whether agents are behaving as intended, engineering teams need meaningful ways to measure performance. The relevance of each metric will depend on the AI agent and its associated work. However, in general, important metrics include task success (did the agent accomplish what it was supposed to?), groundedness (whether an agent’s responses are supported by the information given to it, or whether it is hallucinating), latency, tool selection, timeout rates, error rates, retry rates, step efficiency, cost, safety and ethical violations, human escalation rates, and many others. One option for [evaluating the performance](https://thenewstack.io/ai-agent-evaluation-loop/) of AI agents is to create a golden set of expected behaviors (e.g., a set of questions and answers) and ensure that the agent is operating as intended in the cases covered by the golden set.

## 4. Build in ongoing evaluation

Agent performance is not fixed. Behavior can shift if the model behind an agent is updated, and it can drift even when the underlying infrastructure remains healthy. Any decline in performance should be treated as an operational issue, with alerts routed to the right team before a problem escalates.

Evaluation should happen at two speeds: catching issues near real time and reviewing agent behavior after the fact. Post-incident reviews examine not only what went wrong, but how agents behaved in response. Did they escalate appropriately? Were the right tools selected? Was human intervention required when it should have been? As systems become more autonomous, agent evaluation must become an ongoing discipline.

## Start off small

AI has the potential to transform incident management, but organizations will only realize that opportunity when they can trust their AI agents. Building that trust starts with low-risk use cases such as triage and diagnosis, before gradually automating more of the incident lifecycle.

> “AI has the potential to transform incident management, but organizations will only realize that opportunity when they can trust their AI agents.”

Trust also comes from putting the right guardrails, monitoring, and evaluation processes in place. While human oversight will remain essential for complex incidents, the long-term direction is clear: engineers and AI agents will increasingly work together to resolve issues.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/04/42adea86-joaofreitas.png)

João Freitas is Chief AI Officer at PagerDuty. With about 20 years of experience in software development, machine learning and as a people manager, he was previously CTO at an AI startup and has taken several roles at Microsoft in...

Read more from João Freitas](https://thenewstack.io/author/joao-freitas/)