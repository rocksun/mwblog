[Airbyte](https://airbyte.com) on Tuesday launched Airbyte Agents, a new service that precomputes and indexes a company’s business data, allowing AI agents to query it directly rather than multiple APIs at runtime.

The core idea behind the launch is that the limiting factor for running agents in production isn’t the models or even the harness around them. It’s the underlying data. When agents are wired up to call live APIs across half a dozen SaaS tools to answer a single question, the result is high latency and bloated token spend.

> When agents are wired up to call live APIs across half a dozen SaaS tools to answer a single question, the result is high latency and bloated token spend.

Airbyte Agents is built around what the company calls the Context Store. Instead of letting an agent query across Salesforce, Zendesk, Jira, and Slack at runtime, the Context Store pulls those systems together ahead of time into a single index that preserves entity history and current state. Agents then run their lookups against that index. According to Airbyte, this approach takes a typical agent task from five or six API calls down to one or two and trims token usage along the way.

[Michel Tricot](https://www.linkedin.com/in/micheltricot/), Airbyte CEO and co-founder, tells *The New Stack*, “Developers are used to thinking in terms of services and APIs. With agents, you have to think in terms of state and context over time. That requires a different layer in the stack, one that sits between your data sources and the agent runtime and ensures consistency.”

![](https://cdn.thenewstack.io/media/2026/05/1c77263c-image-22-1024x503.png)

Credit: Airbyte.

The launch builds directly on what Airbyte has been doing since 2020. Co-founders Tricot and John Lafleur started the San Francisco-based company around an open-source data integration platform and a library of connectors used to push data into warehouses and lakehouses. Airbyte is now pointing that same connector library at a new buyer: teams building agents who need a clean, unified read layer rather than another analytics pipeline.

> “Most AI agent failures we see in production aren’t model failures, they’re data failures… Agents are forced to stitch together multiple API calls across disconnected systems, which introduces latency, inconsistency, and often conflicting results.”

Tricot says the current pattern for building agents breaks down at scale. “Most AI agent failures we see in production aren’t model failures, they’re data failures,” he says. “Agents are forced to stitch together multiple API calls across disconnected systems, which introduces latency, inconsistency, and often conflicting results.”

Customers can reach the Context Store in two ways. The first is an Airbyte MCP server, which lets humans and agents pull from the data through Claude, ChatGPT, Cursor, and other MCP-compatible tools without writing code. The second is an Agent SDK for engineering teams that want programmatic control over how their custom agents read from the store, what they can write back and how permissions are scoped.

> “RAG and APIs are retrieval patterns — they let you fetch data when you need it… What’s missing is a persistent, structured layer that maintains relationships and state across systems.”

As Tricot notes, the Context Store is a layer that existing retrieval approaches don’t provide. “RAG and APIs are retrieval patterns — they let you fetch data when you need it,” he says. “What’s missing is a persistent, structured layer that maintains relationships and state across systems. Without that, agents are constantly reconstructing context at runtime, which is inefficient and error-prone.”

![](https://cdn.thenewstack.io/media/2026/05/675d4dc7-image-21-1024x563.png)

Credit: Airbyte.

The Context Store features 50 connectors at launch, including Salesforce, HubSpot, Zendesk, Jira, and Slack. The remainder of Airbyte’s catalog will land in the coming months.

This move puts Airbyte into a very crowded field. Composio, for example, has built its business around a connector catalog and MCP gateway aimed specifically at AI agents, with hundreds of toolkits exposed through MCP. Zapier’s MCP server, too, connects its integration library to any MCP-compatible client.

Fivetran, Airbyte’s most direct competitor in the ELT space, has been pushing its platform toward AI workloads as well. Meanwhile, vertically integrated incumbents like Salesforce, with Agentforce, and ServiceNow are pitching their own clouds as the natural source of truth for an agent. Airbyte’s argument is that a connector-rich, vendor-neutral data layer makes more sense for companies whose data often already lives across many of these systems.

Airbyte is also wading into another increasingly busy segment with Automations, a visual builder for composing agentic workflows on top of the Context Store without code. It’s available in research preview. The visual agent builder market already includes open-source projects like Langflow and Flowise, alongside SaaS offerings from Zapier, Microsoft (with Copilot Studio), and a long list of startups. Airbyte’s pitch here is that Automations sits directly on top of the same Context Store and connector catalog that powers the rest of its platform, rather than reinventing both.

## Availability

Existing paying Airbyte customers get three months of Airbyte Agents access at metered usage limits, billed in a new unit the company is calling Agent Operations that covers reads, searches, write actions, and reasoning calls.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)