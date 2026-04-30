[SAS](https://www.sas.com/en_us/home.html) has spent 50 years building analytics and decisioning software for regulated industries like banks, insurers, government agencies, and manufacturers. Now, it is betting that governance will be its moat in the agent era.

As AI agents reshape how enterprise software is consumed, the company’s deep domain expertise and [governance](https://www.sas.com/en_us/insights/analytics/ai-governance.html) might be the assets that hold their value, regardless of which model or agent architecture wins in this AI era.

As SAS CTO Bryan Harris noted in his keynote at SAS’ Innovate ’26 conference in Grapevine, Texas, on Tuesday: “We empower people with technology to scale human observation and decision making. Since the beginning, SAS has been pioneering technological breakthroughs to help you close the information gap and gain a competitive advantage.”

But to do so in this age of AI, businesses — and especially the customers SAS serves — need to be able to trust AI and AI agents. It’s SAS’s job, Harris argues, to ensure that even though large language models are non-deterministic provide trustworthy results that are verified and validated.

> “Our role is to really make sure we can give you a trusted answer in the moments that matter with our software… agentic AI is just another evolution of that technology.”

“Our role is to really make sure we can give you a trusted answer in the moments that matter with our software — and agentic AI is just another evolution of that technology,” Harris said in a press briefing.

![](https://cdn.thenewstack.io/media/2026/04/09713dbd-img_3753-1024x767.jpg)

*Credit: The New Stack.*

## SAS analytics as an MCP-callable service

One core feature of SAS’s overall strategy — and one that SAS may have underplayed a bit at its event — is a new [Viya MCP Server](https://www.sas.com/en_sg/software/viya/mcp-server.html)*ˆ* that exposes its analytics and decisioning capabilities as tools any external AI agent can call via the Model Context Protocol (Viya is SAS’s cloud-native data and AI platform).

An organization running Claude, Copilot, or any custom agent can use this MCP server to, for example, invoke a SAS fraud detection model or run a supply chain optimization directly — all without bypassing the governance SAS wraps around its models and the data they rely on.

Most vendors adopting MCP are building agents that consume tools through the protocol. SAS is doing that too, but the more notable move is exposing its own analytics engine as the thing agents call. It’s positioning Viya not as the orchestrator but as the governed backend, making it the place where trusted models live, regardless of who’s asking.

## Agents, industry models, and governance

The MCP server wasn’t the only agentic announcement from SAS. The company also shipped an Agentic AI Accelerator, an open-source framework for building governed agents; a multi-agent system in its CI360 marketing platform; and a Supply Chain Agent that compresses multi-day sales and operations planning cycles into continuous optimization.

![](https://cdn.thenewstack.io/media/2026/04/380a3a42-img_3750-1024x768.jpg)

*Credit: The New Stack*

What makes the industry agents more than LLM wrappers is what’s underneath. SAS doesn’t build foundation models; it builds narrow, purpose-built models trained on domain-specific data. Its fraud detection models, for instance, are trained on consortium data contributed by major global banks, including millions of fraud events spanning card, digital wallet, and application fraud. The Supply Chain Agent sits on top of SAS’s existing optimization models. The MCP Server then makes all of that callable from outside.

That same logic extends to governance itself. SAS also announced AI Navigator, a standalone SaaS governance product arriving in Q3 on Azure Marketplace that inventories and governs AI use cases across vendors, including Claude, Copilot, open-source models, not just SAS’s own.

In a way, governance is its own product line within SAS, decoupled from the analytics platform.

![](https://cdn.thenewstack.io/media/2026/04/914786da-img_3733-1024x768.jpg)

*The SAS Viya platform with governance at its core. Credit: The New Stack*

“AI governance is too often thought of as a compliance measure,” says Reggie Townsend, vice president of AI ethics, governance, and social impact at SAS. “It’s a growth driver. Instead of fears of shadow AI putting the organization at risk, AI governance empowers people to push the limits of AI within a structured, transparent, and secure environment.”

> “AI governance is too often thought of as a compliance measure… It’s a growth driver. Instead of fears of shadow AI putting the organization at risk, AI governance empowers people to push the limits of AI within a structured, transparent, and secure environment.”

SAS has been on this path for a while. In 2024, for example, the company began integrating generative AI into Viya through copilots, a synthetic data project, and model cards for model transparency. By 2025, it had introduced agents but kept them scoped to its decisioning platform. “Bread and butter,” as SAS described it. Now, SAS is building on all of this, but also positioning the platform as infrastructure that other vendors’ agents can call.

SAS’s bet is that whoever controls trusted analytics and governance will matter even if agents become the new interface and if they don’t control the agent platform itself in the long run. That’s something a lot of AI-native startups already do by default as they integrate with the large model providers, but for large enterprise vendors, that’s not always a path the leadership team wants to back.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)