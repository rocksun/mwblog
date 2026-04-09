Anthropic on Wednesday [launched](https://claude.com/blog/claude-managed-agents) the public beta of [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), a new service that allows businesses to quickly build and deploy cloud-based agents on its platform.

Until now, Anthropic has mostly focused on providing its users with models to build their agents, but outside of Claude Code and Cowork, it hasn’t made its own infrastructure available for running those agents. With Claude Managed Agents, as the name implies, users can define the agents they want to run — either by describing the agent in natural language or through a YAML file — define their guardrails, and run them on Anthropic’s platform, with all of the infrastructure abstracted away.

As the Anthropic team notes in today’s announcement, “shipping a production agent requires sandboxed code execution, checkpointing, credential management, scoped permissions, and end-to-end tracing. That’s months of infrastructure work before you ship anything users see.”

The team promises that Managed Agents speeds this process up by 10x, in part because the service provides a full set of tools for sandboxing agents, and handling authentication and tool execution.

![](https://cdn.thenewstack.io/media/2026/04/00ee9869-claude-managed-agents-demo-video.gif)

Agents can run for multiple hours, the company says, and connections to third-party services are handled [through MCP servers](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

Some features of Managed Agents remain in a limited research preview, however. Those include advanced memory tooling, multi-agent orchestration, and the ability for the agents to self-evaluate and iterate until they reach a defined outcome.

Anthropic also stressed that it is offering governance tools, something that has held back many an enterprise from adopting agents in production environments. The platform will handle scoped permissions, identity management, and execution tracking, the company says.

![](https://cdn.thenewstack.io/media/2026/04/53795e13-69d53a1b570fa207204f0111_claude-blog-managed-agents-diagram-noborder-1024x1024.png)

*Credit: Anthropic.*

[Pricing](https://platform.claude.com/docs/en/about-claude/pricing) for the new service is pretty straightforward. Users pay for the models’ token use, based on Anthropic’s standard API pricing, with an additional $0.08 per session-hour for active runtime (measured in milliseconds). Idle time — when an agent is waiting for your next input or a tool — pain point does not count towards this runtime. When the agent performs a web search, Anthropic charges an extra $10 per 1,000 searches.

Clearly, this is a major milestone for Anthropic. With Claude Code, it built a large developer ecosystem around its models and coding harness, but it is now getting into the infrastructure layer for agents. That’s a very different market, but more than any of its competitors, Anthropic has put its focus on enterprise users. Managed Agents addresses a clear pain point that many businesses have faced when trying to put agents into production, whether for internal usage or to give to customers.


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)