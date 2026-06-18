AI is already inside most enterprises’ IT stacks, but it’s had a somewhat shambolic and unsystematic early adolescence. Employees use personal tools, teams adopt different models, different company departments get forced into corners by vendors who push closed stacks, and agents are beginning to act inside systems that were built for people.

That makes AI invisible, fragmented, and hard to change later.

AI access and control platform company [Tailscale](https://tailscale.com/) announced on Tuesday the results of its work to address and redress these imbalances with new capabilities for [Aperture](https://tailscale.com/docs/aperture), the company’s flagship toolset designed to provide a stable layer for managing [AI across changing models](https://thenewstack.io/openai-releases-new-models-trained-for-developers/), tools, data sources, and agents.

Designed to enable software developers to control and orchestrate the arguably [almost too-dynamic state of AI](https://www.bbc.co.uk/news/articles/cx2124z7g45o), Aperture now offers a new chat interface, universal data connectors for both MCP and APIs, and sandbox support.

## What makes agents useful, also makes them risky

[Avery Pennarun](https://ca.linkedin.com/in/apenwarr), CEO and co-founder of Tailscale tells *The New Stack* that the “same mechanics” that makes AI agents useful also make them risky i.e. they can do in seconds what would take a person dozens of clicks, commands, and context switches.

But he advises that [the risk factor here](https://thenewstack.io/risk-mitigation-agentic-ai/) is not really a matter of pitting humans against agents and trying to place one above the other in terms of potential fragility. He says that the real risk is “giving any actor too much room” to act without clear boundaries.

“With agents, that risk moves faster,” [Pennarun](https://ca.linkedin.com/in/apenwarr) says. “With humans, the weak point is often the control model itself. If security depends on a developer approving a long stream of prompts, they will either get slowed down or hit approval fatigue and start approving things by reflex. That is not much of a security model.”

> “Agents need boring infrastructure around them – robust identity management, limited access controls, carefully tracked logs, and sandboxes – that boring outer shell is what lets them do useful work without making every developer’s laptop the place where all the risk lands,” Avery Pennarun, Tailscale CEO.

## Interestingly, agents need boring infrastructure

For Pennarun, the answer lies in making sure agents have what he calls “boring infrastructure around them”, by which he means robust identity management, limited access controls, carefully tracked logs, and (where necessary) sandboxes to execute in before they are exposed to mission-critical datasets, applications, or both.

“That boring outer shell is what lets them do useful work without making every developer’s laptop the place where all the risk lands,” Pennarun clarifies. “The answer is not agentic control or human control alone. Humans set the policy and boundaries up front. Infrastructure enforces them. Agents operate inside them.”

Aperture can be defined as a centralized AI gateway built to monitor and route LLM requests in a secure manner using Tailscale’s identity layer to automatically authenticate “users” (a cohort which we now obviously expand to include both humans and machines), eliminating the need to distribute API keys to authenticate with each AI model.

The gateway holds the API keys securely, meaning that when a developer (or a container) makes a request, Aperture verifies *who* they are via their Tailscale identity and then automatically routes requests to upstream LLM providers such as OpenAI, Anthropic, and Google without requiring changes to existing tools or workflows.

## Yeah, we use AI, dunno where

Given the amount of work-related activity currently happening on personal and free AI accounts, we might suggest that concerns here are validated i.e. organizations today can not see, govern, or recover the information streams at this level. Research [cited](https://www.axios.com/2025/02/04/shadow-ai-cybersecurity-enterprise-software-deepseek) by Axios found companies typically have 67 generative AI tools running across their systems, with 90% lacking proper licensing or approval.

Tailscale has reemphasized the fact that AI providers are bundling models, chat interfaces, data access, and execution environments into closed stacks. Those bundles can make the first deployment easier, but they can also leave organizations locked into one provider’s models, tools, and roadmap and pricing. In a market where model quality, speed, and cost keep changing, that lock-in can quickly become a disadvantage.

> “Aperture is built to give developers a practical way to manage AI without locking down their choices. It makes approved AI tools easier to use, connects them to internal data with identity preserved, and gives agents controlled environments to work in.”

“AI agents are also changing the risk model. They can write code, call tools, browse systems, manipulate files, and run commands. In many setups, they do that with the same permissions as the person running them, which can expose local files, credentials, and internal systems if something goes wrong,” said Pennarun and team.

## What it means for developers: a controlled environment for agents to work in

Aperture is built to give developers a practical way to manage AI without locking down their choices. It makes approved AI tools easier to use, connects them to internal data with identity preserved, and gives agents controlled environments to work in. It also keeps the AI stack essentially modular, so teams can keep experimenting with new models, interfaces, tools, and providers without starting over.

The new chat interface is a browser-based way to use approved AI models through Aperture. The interface supports switching between configured LLM providers and works with Aperture data connectors and sandboxes. The universal data connectors **help** AI tools reach internal systems, documents, APIs, and operational data without forcing every team to build its own integration path.

Teams can use Aperture’s chat UI, coding agents, agent frameworks, or implement custom interfaces through OpenWebUI or LibreChat. Sandbox support (available in private alpha at the time of writing) is designed to give AI agents controlled environments where they can complete work without acting directly on a user’s laptop, workstation, or unmanaged system.

Aperture is designed to work with API keys from major LLM providers and with tools, agents, and interfaces that can be configured to route through Aperture.

## AI stacks inevitably, constantly and persistently change

With the frontier model race apparently unlikely to slow down any time soon, the fact that the best model, interface, sandbox, and data connection will all keep constantly changing… combined with the need to juggle these balls across multi-cloud deployment instances (poly-cloud even, where one app is split into different component parts across more than one hyperscaler), organizations looking to harness AI effectively and securely will surely face challenges.

The central technology proposition with Tailscale Aperture is that it gives software developers a stable layer for identity, access, and control, so teams can keep changing tools without losing track of who is doing what.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)