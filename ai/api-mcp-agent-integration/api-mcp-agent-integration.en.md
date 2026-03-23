Everyone is excited for the promise of “Digital coworkers” in this agentic era. Model Context Protocol (MCP) is all anyone can talk about these days when it comes to agentic enablement. But what if you have spent the last decade building APIs for your organization? Do you have to throw out all that work and adopt the MCP-first strategy?

Before you throw the baby out with the bathwater, let’s first consider the multiple approaches to API and MCP integrations that might serve us as we are building agentic applications.

## APIs: The old, reliable bridge

An API is often described as a bridge that lets two systems talk to each other, but I find it more helpful to think of APIs as selections on a restaurant menu. The contents of each dish are clearly marked, so you know what you are getting. If you order beef, you won’t receive pasta. Just like a menu, APIs are predefined by humans and accompanied by documentation that can be reviewed before use.

APIs do not allow for speculation. For example, if you want customer data in your application, you use the customer endpoints from the API. Selecting the customer endpoints means that you will get what you’re looking for–in this example, customer data, not weather forecast data.

> “An API is often described as a bridge that lets two systems talk to each other, but I find it more helpful to think of APIs as selections on a restaurant menu.”

The useful part of APIs is that they are specific and tightly structured, requiring code to follow a defined construct. For example, well-designed REST APIs follow a clear pattern of verbs (what the system can do) and nouns (the components in the system). Clear verb examples are “get,” “create,” “delete,” and noun examples are “file,” “user,” “invoice”. This separation is done so that machines have prescriptive, controlled ways of interacting based on the semantics of the APIs.

Before AI agents, building client applications that leverage APIs required custom code that aligned directly to each specific API. An application can only interact with the endpoints it is explicitly told to use. AI agents, on the other hand, when given an endpoint, will repeatedly call it, trying to understand how it works until they get a successful response.

They learn the API, but sometimes with disastrous consequences. Agents have been shown to overcall endpoints, retrieve sensitive data, or retry APIs until they accidentally break something. Even worse, some agents have leaked API credentials, as in the instance of [OpenClaw API key leaks](https://www.bitsight.com/blog/openclaw-ai-security-risks-exposed-instances%23:~:text=The%2520traffic%2520included%2520prompt%2520injection,'ve%2520read%2520the%2520source.%25E2%2580%259D).

Even with this new agentic paradigm, APIs still have a role to play in delivering successful agents. For example, if you have private data that can improve an agent’s accuracy but is highly sensitive and requires complex authorization structures, an API can ensure controlled access to it. However, you need to carefully consider your API strategy for agents, because there is a cost… literally.

For example, if you have a complex API with many fields, you need to document exactly how to use it for the agent. The agent may also choose to start exploring other endpoints in the API.

Providing information on how to use the API, as well as the specific API parameters, is additional information that an agent will need to carry throughout their session, which means you are compounding the tokens spent on API information and taking up more space in the context window.

Instead of relying on detailed APIs, which can consume a significant number of tokens, consider using Model Context Protocol (MCP). MCP provides a lighter-weight, specification-based integration alternative for agents, helping conserve your tokens throughout the session.

## MCP: The protocol for agentic interactions

[Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) is designed for a world in which AI agents, rather than humans, directly interact with tools, data sources, and applications. Since MCP is a universal AI integration standard, agents don’t need to understand custom client code (like with REST endpoints) to talk to an MCP server.

All integrations use the same protocol, so it’s more uniform than APIs. Also, each MCP server’s capabilities – tools, resources, prompts – are self-describing, so they announce their capabilities. You don’t need additional tools to resolve documentation issues in APIs.

MCP enables agents to discover and use tools dynamically with no documentation needed, [similar to how a USB is a universal way to connect new peripheral hardware](https://modelcontextprotocol.io/docs/getting-started/intro) without needing to download new software (usually). The agents can take action based on the standard and require no additional tools or solutions. With MCP, servers ‘advertise’ what they can do.

The agent-as-coworker can “see” the available capabilities and autonomously make a decision based on the descriptions provided by the MCP server. The AI agent will determine whether the tools are needed for its independently crafted plan for solving its problem.

So in essence, [MCP enables the agent](https://thenewstack.io/how-mcp-enables-agentic-ai-workflows/) to understand and find specific ‘tools’ to complete their task. Unlike APIs, tools accessed via MCP do not rely on separate, thorough documentation. APIs tell machines exactly what to do, and MCP tells AI agents what tools exist so agents can use them as they see fit.

If an API is a restaurant’s physical menu, then MCP is like a food-delivery application. A restaurant can only give you a menu for that specific location (API).  However, MCP provides the universal ‘app’ that allows the diner (agent) to browse, order from, and talk to *any* kitchen in the area using a single interface.

Instead of the diner needing a separate app for each restaurant, the MCP Client serves as the unified storefront. It brokers access to MCP Servers (the individual kitchens), allowing the AI to dynamically discover new ‘dishes’ (tools and data) without manual setup. By standardizing this handshake, MCP transforms the AI from a limited, single-menu option into an agent with citywide accessibility.

> “If an API is a restaurant’s physical menu, then MCP is like a food-delivery application, providing the universal ‘app’ that allows the diner (agent) to browse, order from, and talk to any kitchen.”

Given the non-deterministic nature of LLMs that use these MCP servers to access tools, IT organizations must consider MCP server control and governance by implementing an MCP Gateway.

## Define your agent integration strategy

Given the potential risks and governance headaches, why would you consider MCP integrations? Simple… because agents need dynamism. APIs are static, which can be overly inflexible for agent coworkers. That being said, APIs remain relevant to agents in specific instances where an organization requires a more controlled, deterministic approach for security or regulatory reasons.

You may ask, ‘Why don’t I just wrap my API with MCP?’ The Tanzu team has seen several successful uses of Spring AI to wrap APIs using the MCP tool command, thereby reducing the number of complex specs the agent has to understand and look up during interactions.

On the surface, that may look appealing because you won’t lose your decades of investments in APIs, and you will save your tokens. However, wrapping isn’t a panacea for agent-friendly APIs. It will depend on the individual analysis of each API. Instances where dynamic analysis across multiple data sources is needed to provide recommendations are good candidates for MCP wrapping (e.g., retail recommendation engines or real-time investment analysis).

These types of layered integrations might use an API for customer data and then add a separate MCP integration for real-time data. However, each use case will still need careful assessment.

Wherever you end up in your analysis, one thing is for certain. MCP servers and APIs are bound to proliferate for AI use cases over time. Organizations that are accountable for IT performance, costs, compliance, and security will need observability, guardrails, and auditability for their proliferating integrations.

This is where an application platform, such as [VMware Tanzu Platform](https://thenewstack.io/broadcom-debuts-vmware-tanzu-platform-10-at-explore-2024/), can help scale your API and MCP server ecosystem, publish MCP servers and APIs in a developer/agent marketplace, and provide visibility and lifecycle management capabilities that enable ongoing upgrades and optimization of your API and MCP integrations for AI.

In [this](https://broadcom.zoom.us/webinar/register/WN_vchyZyXwTaWZdgN-TG__kQ%23/registration) upcoming webinar, our colleague Adib Saikali will discuss how enterprises can approach their API and MCP integration strategy. [Join us](https://broadcom.zoom.us/webinar/register/WN_vchyZyXwTaWZdgN-TG__kQ%23/registration) at 9 a.m. Pacific on March 25!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/06/8c0d7ab0-camille-crowell-lee.jpg)

Camille Crowell-Lee is a solutions marketing leader who focuses on VMware Tanzu by Broadcom. She has been in technology marketing for over 17 years where she has built strategic marketing initiatives for hyperscale cloud providers and for ISVs, including containerization...

Read more from Camille Crowell-Lee](https://thenewstack.io/author/camille-crowell-lee/)

[![](https://cdn.thenewstack.io/media/2026/03/c92a6075-cropped-eb976d91-morganfine.jpg)

Morgan Fine is Director of Product Management at VMWare Tanzu and is based in Berkeley, California.

Read more from Morgan Fine](https://thenewstack.io/author/morgan-fine/)