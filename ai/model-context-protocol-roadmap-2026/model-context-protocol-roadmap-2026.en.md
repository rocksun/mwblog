The Model Context Protocol ([MCP](https://modelcontextprotocol.io/)) has [emerged](https://thenewstack.io/why-the-model-context-protocol-won/) as one of the key building blocks of the agentic AI stack, serving as a common language for models to connect with external tools, files, and business systems.

Want an AI assistant to pull a file from Google Drive, query a company database, check a GitHub issue, or trigger an action in an internal app? That’s the kind of job MCP is meant to handle.

Now, the project’s [new 2026 roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) suggests the maintainers are turning their attention to a harder question: What needs to be fixed before MCP can hold up in real production use?

## The path to a shared protocol

MCP first appeared at the tail end of 2024, when Anthropic [introduced](https://www.anthropic.com/news/model-context-protocol) the protocol to enable AI models to interact with external tools and data sources in a more structured way.

The project’s [open source credentials](https://github.com/modelcontextprotocol) helped it gain traction among developers building AI assistants and agent-style applications. Rather than writing custom integrations for each system, teams could expose those services [via MCP servers,](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/) allowing models to interact with them using the same protocol.

Over the past year, a growing ecosystem of AI companies and developer platforms has begun adding support for MCP. Anthropic’s [own Claude assistants](https://code.claude.com/docs/en/mcp) use it to interact with external tools, while other vendors — [including OpenAI](https://community.openai.com/t/introducing-support-for-remote-mcp-servers-image-generation-code-interpreter-and-more-in-the-responses-api/1266973), [Microsoft](https://developer.microsoft.com/en-us/windows/agentic/), [Google](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services), and [Amazon](https://devops.com/aws-adds-mcp-support-to-amazon-q-developer-platform/) — have embraced the standard.

But as adoption spreads, so do the operational challenges of running the protocol in more serious environments. To address those growing pains, the project maintainers reviewed a range of potential improvements and identified four priority areas where most development effort and fast-tracked protocol proposals will be focused.

## Making MCP easier to run at scale

A recurring issue that has raised concerns among developers involves how MCP handles connections between clients and servers. In its current form, the protocol relies on long-lived, “stateful” sessions, which can make it harder to deploy MCP servers across multiple instances or behind load balancers, since the session state is typically stored on the server handling the connection, rather than shared across machines.

This priority area has been pegged as “transport evolution and scalability.” In plain terms, it means reworking how MCP handles those connections so deployments can scale more easily across distributed infrastructure.

Developers have already run into this limitation when trying to run MCP servers across multiple machines. In one [GitHub issue](https://github.com/modelcontextprotocol/typescript-sdk/issues/892) raised back in August, a developer attempting to build a stateless MCP server across multiple pods using Redis reported that the SDK does not provide a reliable way to map client session IDs to the server’s internal event streams. Without that mapping, sessions can’t be resumed if requests are routed to a different server instance — effectively forcing deployments to rely on in-memory state rather than distributed infrastructure.

That issue was [later referenced](https://github.com/modelcontextprotocol/typescript-sdk/issues/1058) by MCP maintainers in a broader tracking discussion about enabling stateless or near-stateless server architectures.

The roadmap suggests addressing these kinds of limitations through two main changes. First, evolving MCP’s transport and session model so that servers can scale horizontally without maintaining state on a single machine. And second, introducing a standard metadata format that servers can expose — likely via a *.well-known* endpoint — so tools and registries can discover what an MCP server does without first establishing a live connection.

[David Soria Parra](https://www.linkedin.com/in/david-soria-parra-4a78b3a), a member of technical staff at Anthropic and MCP lead maintainer, said the goal is to improve how the existing transport works rather than introduce new ones.

“One thing we want to be explicit about: we are not adding more official transports this cycle but evolve the existing transport,” Parra writes. “Keeping the set small is a deliberate decision grounded in the [MCP design principles](https://modelcontextprotocol.io/community/design-principles).”

## No task too small

The second-priority issue concerns “agent communication,” which refers to how MCP handles longer-running work triggered by AI agents.

In its current form, the protocol allows clients to start asynchronous Tasks, enabling agents to launch work in one request and retrieve the result later. But early production use has exposed gaps around how those tasks should behave — particularly how failed jobs should be retried and how long completed results should remain available.

Some of those questions surfaced during work on the [Tasks feature itself](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1686). In a GitHub pull request defining how Tasks should operate, [Luca Chang](https://www.linkedin.com/in/luca-chang/), a software engineer at AWS and MCP maintainer, [described the pattern](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1732) as allowing agents to start work in one request and retrieve the result later.

While that approach makes it easier for agents to run longer operations, it also raises questions around how those jobs are retried when something goes wrong and how long their results should persist.

The roadmap proposes clearer definitions around those lifecycle rules so MCP systems can manage agent-driven tasks more reliably.

Parra also notes that some of these gaps only become visible once developers begin using a feature in real production environments.

“This is the kind of iteration you can only do once something is deployed and tested in the real world,” he said. “We plan to take the same approach with other parts of MCP: ship an experimental version, gather production feedback, and iterate.”

## Reducing bottlenecks in MCP governance

Governance is also firmly on the agenda. As MCP adoption spreads across companies and developer communities, maintainers say the project needs clearer decision-making structures and contributor pathways.

This “governance maturation” priority area essentially focuses on refining how protocol changes are proposed and reviewed.

The goal, ultimately, is to ensure that MCP can continue to grow without relying on a small group of core maintainers to review every change as the ecosystem expands. [At present](https://modelcontextprotocol.io/community/sep-guidelines), every MCP proposal — known as a SEP (Specification Enhancement Proposal) — must be reviewed by the full group of core maintainers, regardless of the area it affects.

“That’s a bottleneck,” Parra said. “It slows down Working Groups that already have the expertise to evaluate proposals in their own area.”

## Preparing for the enterprise

The final priority focuses on what the roadmap calls “enterprise readiness,” a familiar phase for many open-source infrastructure projects as they begin to see wider adoption across the industry.

As organizations start integrating MCP into internal systems, they tend to encounter a predictable set of operational requirements — including audit trails, authentication tied to corporate identity systems, gateway controls, and configuration that can move cleanly between environments.

Unlike the other priorities, this area is intentionally less defined. The roadmap notes that enterprise readiness remains one of the least prescriptive parts of the current work plan, in part because the maintainers want input from the teams encountering these issues first-hand.

At present, there is no dedicated enterprise working group within the MCP project, for instance. Instead, the maintainers are encouraging contributors with experience in enterprise infrastructure to help shape these efforts.

“We want the people experiencing these challenges to help us define the work,” Parra said.

## On the horizon

Collectively, the four priorities highlight the kinds of issues that come to light once a piece of infrastructure moves beyond its embryonic stages. In MCP’s case, that means making the protocol easier to operate across multiple machines, clarifying how agents manage longer-running work, establishing clearer governance, and getting things ship-shape for the enterprise.

This list, however, is not exhaustive. The roadmap also highlights several areas “on the horizon,” including triggers and event-driven updates, new result types, and deeper work around security and authorization.

Those topics, while not an official “priority,” will likely move forward through community-led working groups rather than direct maintainer focus during this cycle.

“We’re focused on a limited set of items, but we still want protocol exploration to continue at a good pace,” Parra wrote.

For now, the emphasis is on tightening the core of the protocol — and inviting the broader developer community to help shape what comes next.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)