The anti-automation glitterati may now be preparing for [a new swathe of naysaying](https://www.bostonreview.net/reading-list/ai-and-the-specter-of-automation/) as agentic AI services are brought to bear inside enterprise software services. The validation for their doom-mongering could be ignited by organizations now [adopting large-scale AI agents](https://thenewstack.io/ai-agents-in-it-from-hype-to-hands-on-impact/) at a time when many of these technologies are still embryonic.

What developers need to remember is that AI agents can invoke tools, access sensitive data, and execute business workflow actions in real time across enterprise databases, financial records, messaging platforms, customer relationship management systems, and so on. If this stark reality means businesses are now applying agentic services without recognizing the security holes these actions open, then we may be headed for a fall.

## Simulated adversarial attacks

Aiming to quell the fears currently surfacing is real-time multimodal AI security and systemic governance platform company [Virtue AI](https://www.virtueai.com/) with its new Agent ForgingGround offering. The service has been created with built-in red teaming agents, an established cybersecurity practice that simulates adversarial attacks and identifies vulnerabilities that could be exploited by real-world malicious actors.

Agent ForgingGround serves as an [enterprise-scale testing ground](https://thenewstack.io/why-load-tests-lie-harsh-truth-about-ai-agent-performance/) for continuously evaluating and stress-testing AI agents (including multi-agent systems, in which agents may spawn sub-agents) before, during, and after deployment. The toolset on offer here also analyzes tool interactions and cross-system behavior.

A new component of AgentSuite (Virtue AI’s security, governance, and compliance platform for agentic AI), Agent ForgingGround, includes 50+ production-grade simulated enterprise environments such as Databricks, Gmail, Google Docs, PayPal, ServiceNow, and [Atlassian](https://thenewstack.io/how-atlassian-is-driving-the-ai-agent-assisted-workflow/).

## Manipulation & misconfiguration discombobulation

Because agents operate in dynamic, stateful environments, a small prompt manipulation or unintentional misconfiguration can escalate into tool misuse, data exfiltration, or unauthorized transactions. The company says that without a controlled testing layer, vulnerabilities and [zero-day exploits](https://thenewstack.io/zero-day-vulnerabilities-a-beginners-guide/) can only be discovered after deployment, when the operational and reputational stakes are significantly higher.

> Agents are dynamic systems that change as prompts evolve, tools are updated, or models are swapped out, so security testing cannot be a one-time event.

But even with the tools in place to analyze an agent’s state, behavior, and propensity to misbehave, how will developers know when to apply Agent ForgingGround in the software development lifecycle? Is this technology designed to run during pre-production testing, throughout continuous integration / continuous deployment (CI/CD) loops, or when?

CEO and founder of Virtue AI, [Bo Li,](https://www.linkedin.com/in/lxbosky/) tells *The New Stack* it’s both.

“Most teams start by running Agent ForgingGround in pre-production before an agent ever touches real systems, so they can stress-test behavior in a controlled environment. Over time, it can also become part of the CI/CD pipeline. Agents are dynamic systems that change as prompts evolve, tools are updated, or models are swapped out, so security testing cannot be a one-time event. It has to run continuously as the agent evolves,” Li says.

Unlike agent simulations that directly call existing MCP environments (such as LangWatch), the Virtue AI ForgingGround generates environments from the ground up. It serves as a high-fidelity agent simulator for evaluating and stress-testing agents in their own controlled, flexible digital worlds.

## An independent oversight layer

These environments mirror their real-world counterparts in both user and agent interfaces, enabling what Li and team promise: “realistic and transferable evaluation” of agent behaviors and risks. By functioning as an independent oversight layer, ForgingGround allows a built-in red-teaming agent to provide continuous red-teaming risk assessment across the full agent lifecycle, closing blind spots that internal testing can’t catch.

Working alongside Li to lead Virtue AI’s agent security business is [Wenbo Guo](https://www.linkedin.com/in/wenbo-guo-321999b8/).

A software engineer and assistant professor at UC Santa Barbara, Guo has seen developer workflows in action while testing an agent before it’s deployed. He says the process starts when a developer logs in to the Virtue AI platform and selects the environments in which the agent will operate, as well as the types of risks they want to test, such as prompt injection, tool injection, environment injection, skill injection, and their combinations.

“Effectively, these [red teaming strategies](https://thenewstack.io/ai-agents-are-a-security-ticking-time-bomb/) reflect realistic adversarial behavior, mirroring environment-manipulating tactics such as injected emails, unsolicited Slack messages, and malicious instructions embedded in shared documents. They then connect their agent to the simulated environments within Agent ForgingGround, in the same way they would connect it to real tools through MCP or another agent framework.

From there, our built-in red-teaming agents automatically begin stress-testing the system. At the end of the process, the developer receives a detailed report showing how the agent behaved, what vulnerabilities were discovered, and concrete recommendations for mitigation before the agent goes into production,” Guo tells The New Stack.

## Agentic chain reactions

In terms of how Agent ForgingGround tests multi-step agent workflows and chained tool calls, rather than just individual prompts, CEO Li reminds us that Most agent failures do not happen at the level of a single prompt; they happen across a chain of decisions as the agent calls multiple tools and reacts to changing context.

“Our system generates test scenarios dynamically while the agent is executing. The red-teaming agents push the system through multi-step workflows, chained tool calls, and evolving contexts so developers can see how the agent behaves across an entire execution path rather than just a single prompt,” Li tells The New Stack.

She further explains the kinds of failures and security vulnerabilities that developers typically discover during pre-production testing of agents. The most common categories are prompt injection, tool injection, and environment injection.

“What matters most is the consequence of those attacks. When an agent has access to enterprise tools and data, those vulnerabilities can lead to data exfiltration, arbitrary code execution, phishing campaigns, ransomware activity, or malware deployment. The severity ultimately depends on what systems the agent is connected to and what actions it is allowed to take,” Li tells us.

## Red-teaming goes SWAT-level

Agent ForgingGround has been engineered with 1,000+ proprietary red-teaming algorithms to optimize the attack strategies and injection points. Testing environments can also be configured to reproduce specific evaluation scenarios, with outcomes deterministically verified through environment states. This allows teams to rerun agent trajectories for benchmarking, debugging, and regression testing.

Virtue AI Agent ForgingGround is compatible with the agentic frameworks enterprises are already using, including Google ADK, OpenAI Agents SDK, LangChain, LangGraph, CrewAI, Amazon Bedrock AgentCore, Microsoft Agent Studio, GitHub Copilot, Claude Code, Cursor, Salesforce Agentforce, and others.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)