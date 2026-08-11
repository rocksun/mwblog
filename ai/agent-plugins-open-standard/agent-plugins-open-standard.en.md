[OpenAI](https://thenewstack.io/openai-aims-to-make-chatgpt-the-operating-system-of-the-future/), [AWS](https://aws.amazon.com/blogs/opensource/aws-supports-agent-plugins-an-open-standard-for-portable-agent-extensions/), [Cursor](https://thenewstack.io/cursor-3-demotes-ide/), [GitHub](https://thenewstack.io/github-agent-hq/) and [Microsoft](https://thenewstack.io/microsoft-scout-openclaw-runtime/) have backed [Agent Plugins](https://agent-plugins.org/#) 1.0.0, a portable package format for reusable components that extends AI agents.

Agentic infrastructure company [Vercel](https://vercel.com/home?utm_source=google&utm_medium=cpc&utm_campaign=24015397389&utm_campaign_id=24015397389&utm_term=vercel&utm_content=198458702299_816334546963&utm_source=google&utm_medium=cpc&utm_campaign=gg_s_vercel_acq_emea_brand-exact&utm_campaign_id=24015397389&utm_content=brand_exact&utm_term=vercel&gad_source=1&gad_campaignid=24015397389&gbraid=0AAAAACXzHouXxZSdS4kiM34b0S4nqGVRm&gclid=CjwKCAjwhNbTBhB4EiwAsFSg-iJmUmPtFH3JSrcMQCP-qSjDKmY6K86gRJGGVwAtJlU0QWKyxeRqmBoCTrIQAvD_BwE) initiated the Agent Plugins proposal along with the [project’s core specifications](https://vercel.com/blog/introducing-agent-plugins), and detailed its release on Thursday.

Agent Plugins is an open, vendor-neutral standard for plugins that packages AI Agent Skills (the open standard directory format built to make agent capabilities portable, modular and ‘[progressively loaded](https://www.mindstudio.ai/blog/progressive-disclosure-ai-agent-skill-design)’ across different agent clients and execution environments) and MCP servers into distributable plugins in order to extend them to other AI agent clients and runtimes, or other custom AI frameworks.

Although both Agent Skills and MCP servers can be reused across different clients (clients in this sense being any application, code editor, software tool or code runtime that a software platform hosts, executes, or connects to an AI agent), the clients themselves often package and discover agent skills and MCP servers in different ways and formats.

[Jonathan Hefner](https://www.linkedin.com/in/jonathanhefner/), member of technical staff at Vercel has [blogged](https://vercel.com/blog) to explain why this matters.

“Agent Plugins gives compatible clients a common format: a directory with a [plugin.json](https://docs.castopod.org/develop/en/plugins/reference/plugins-json/) manifest and fixed locations for its components. The format is intentionally small and easy to implement, and it leaves installation, distribution, policy, user experience, and client-specific capabilities to each client,” wrote Hefner.

He noted that Agent Plugins is a contract between the developers who act as authors building extensions for agents and the clients that load them, so that now the contract is “defined and open” for both sides to shape.

Hefner, along with colleagues [Eric Dodds](https://www.linkedin.com/in/ericdodds/), [Andrew Qu](https://www.linkedin.com/in/andrew-qu/), state that Agent Skills provides reusable instructions and resources for AI agents and [MCP servers](https://modelcontextprotocol.io/docs/getting-started/intro), to connect agents to tools and services. So why do developers need plugins anyway?

## Why do developers need agents to plug into plugins?

In practical real world use cases, software developers will need agents and skills to connect to live databases and a variety of data feeds to run queries, cross-reference schema metadata, and feed on real-time analytics. Plugin actions might be implemented to allow agents to forge essential connections to GitHub, Jira, Slack, Figma, or cloud hyperscalers at large.

Agents also make use of plugins to connect to USB or hardware interfaces (perhaps across distributed edge environments, but also desktops), to interact with local developer environments and microservices, or to (for example) draw down juice from a map or weather API, or a payment gateway or payment processing service such as [Stripe](https://stripe.com/), [Adyen](https://www.adyen.com/en_GB), or PayPal’s enterprise service [Braintree](https://www.paypal.com/us/braintree).

Hefner underlined the project’s status, confirming that it is openly licensed, and its maintainers, contribution process, and technical decisions are all public, so that no single company’s product roadmap sets the format’s direction.

He said that for plugin authors, Agent Plugins 1.0.0 means fewer client-specific conventions for the same component. Equally, for client implementers, the specification defines a small, deterministic contract for discovery, validation, and loading.

## Have we just won the battle, but lost the war?

Senior cloud platform engineer at industrial supplies company Grainger, [Pavan Madduri](https://www.linkedin.com/in/pavanmadduri/), tells *The New Stack* that Agent Plugins “solves the easy problem, not the difficult problem” as he sees it.

“Standardizing the packaging and discovery of Agent Skills and MCP servers in ChatGPT, Cursor, Copilot, and VS Code would actually be helpful plumbing – but at the same time, a plugin that is now running in six different client applications represents an additional point of failure for permissions management,” Madduri says.

> “The minute something becomes ‘write once, run anywhere’ for agents, it automatically becomes ‘compromise once, run everywhere’, and this specification specifically defers governance, installation policy, and permissions management to the client application.”

In his view, the minute something becomes ‘write once, run anywhere’ for agents, it automatically becomes ‘compromise once, run everywhere’, and this specification specifically defers governance, installation policy, and permissions management to the client application.

“Interoperability without trust and permissions management is not a security architecture; it’s just another distribution method for bugs and excessive permissions,” cautions Madduri.

## An important step toward making AI agents more interoperable

President and CTO of context-aware code creation and understanding toolset specialist [Adronite](https://www.adronite.com/), [Edward Rothschild](https://www.linkedin.com/in/ephraimrothschild/), tells *The New Stack* that he acknowledges the governance and security responsibility, but overall sees value here, saying that Agent Plugins 1.0.0 is an “important step toward making AI agents more interoperable” in modern stacks.

“The real value is in the ability to reduce the friction that has slowed enterprise AI adoption,” Rothschild says. “Rather than requiring plugin developers to package and maintain their integrations differently for every AI client or agent framework, a common standard makes those capabilities more portable across environments while still allowing organizations to maintain governance and security.”

As open standards mature, Rothschild calls for a groundswell of effort that sees standards bodies and commercial organizations alike both continuing to combine interoperability with strong identity, access controls, and operational visibility, giving developers the flexibility to code without introducing new management blind spots.

Founder of AI model hosting company [EmpirioLabs](https://empiriolabs.ai), [Adam Dalloul](https://www.linkedin.com/in/adam-dalloul/), tells *The New Stack* that his experience of working practice leads him to think that “agent infrastructure is nowhere near cloud and MLOps yet” today.

“We have personally had open source agent updates break production workflows after running smoothly for weeks, so versioning, testing and rollback cannot be an afterthought,” Dalloul says. “Being able to package a Skill and MCP server once and have it carry across Codex, ChatGPT, Cursor, GitHub Copilot, Kiro and VS Code is a real win, and honestly this common format should have existed already.”

> “Being able to package a Skill and MCP server once and have it carry across Codex, ChatGPT, Cursor, GitHub Copilot, Kiro and VS Code is a real win, and honestly this common format should have existed already.”

He harbors one misgiving here: the client-specific extensions.

“I voice that concern because if all of the useful behavior ends up inside vendor namespaces, the standard will look open on paper while the lock-in and fragmentation just move somewhere else,” adds Dalloul.

## Looking beyond, towards commands, hooks, and agents themselves

As stated, Agent Plugins 1.0.0 focuses on two component types: Agent Skills and MCP servers.

Herner confirms that other components, such as commands, hooks, and agents, remain with clients. The Technical Steering Committee may consider additional component types in future versions, as and when semantics converge and a demonstrated portability need emerges.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)