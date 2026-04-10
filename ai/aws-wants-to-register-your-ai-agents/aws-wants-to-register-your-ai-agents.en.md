AWS on Thursday launched the AWS Agent Registry, a new service that aims to help enterprises discover, share, and reuse AI agents, tools, and skills across teams.

This new registry is part of [AWS AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/), the company’s model- and framework-agnostic solution for building and deploying agents, but while it will offer some additional features for agents that run on the AWS platform, the service is meant to index agents from any provider.

“No organization’s agent landscape lives entirely within one provider,” AWS notes in today’s announcement. “Agents are built across AWS services, other cloud platforms, and on-premises environments. A registry that only covers part of the stack leaves the rest invisible, and invisible agents can’t be discovered, governed, or reused.”

According to a recent survey by AI development platform [OutSystems](https://www.outsystems.com/1/state-ai-development/), virtually every enterprise company is now at least exploring how to use AI agents, but only about a third has a centralized approach to AI governance.

Since building AI agents is becoming increasingly easy — and employees can easily use off-the-shelf tools without asking IT for permission — managing all of those agents is a major challenge. A registry won’t solve all of those, but it should make it easier to get a start on reining in this agent sprawl, at least.

“Without a central registry, developers search externally for third-party tools or duplicate work a neighboring team already shipped. You lose visibility into what’s been built, who owns it, and whether it’s approved for use,” the AWS team argues in its announcement.

With a registry in place, developers can search the registry first to see if a capability is already available to them and then either reuse an existing one before building it themselves.

## A catalog for the agent era

The AWS Agent Registry will store the metadata for every agent, tool, MCP server, agent skill, and other collateral around those agents, including which protocols it uses, the capabilities they expose, and how to actually invoke them.

To register an agent, developers can either provide metadata through the AWS console, SDK or API. The easiest way, however, is to point the service to an MCP or Agent-2-Agent endpoint, and the registry will gather all of these details automatically.

Since the registry offers an API and MCP server itself, it’s also easy for clients like Claude Code or AWS’s own [Kiro IDE](https://thenewstack.io/kiro-is-awss-specs-centric-answer-to-windsurf-and-cursor/) (its answer to Windsurf and Cursor) to query the registry for available tools and other capabilities.

## Built-in governance

Given that this is an enterprise product, it also comes with its own governance features. “Without governance, anyone can register anything. You lose control over what becomes discoverable, can’t enforce standards, can’t track ownership, and can’t manage agents from development to retirement,” AWS writes.

So to manage who can publish to the registry, admins can define permissions for both who can publish and who can discover these agents. There is also an approval pipeline that can hook into existing approval workflows and, of course, a way to remove agents once they reach their end of life and retire to the great data center in the sky.

Over time, the plan is for the Registry to automatically discover any agents an organization builds inside of AWS and also offer more operational data about how those agents are used.

## Competition

AWS isn’t the first to market with an agent registry, of course. Microsoft announced Agent 365 at Ignite in November 2025, positioning it as a centralized control plane for discovering, governing, and monitoring AI agents across the enterprise. Paired with Entra Agent ID, which extends Zero Trust identity management to AI agents, Microsoft’s offering goes a bit further than AWS on detecting shadow AI.

Google Cloud, too, has a tool governance layer within Vertex AI Agent Builder, and Google-owned Apigee now integrates with what Google calls its Agent Registry.

On the open-source side, Solo.io contributed its [agentregistry project](https://aregistry.ai) to the CNCF, offering a more vendor-neutral catalog with semantic search, approval workflows, and support for both MCP and A2A.

When it comes to agent, MCP, and skills registries, the field is even broader, with the likes of Chainguard, Kore, JFrog, Kong, and many others all offering some variation on this theme.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)