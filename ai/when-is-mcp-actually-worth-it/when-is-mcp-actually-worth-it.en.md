[Model Context Protocol (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) has emerged as an open standard for connecting AI agents with external data and services. Since being introduced by Anthropic in November, it’s taken off: One directory lists more than 16,000 MCP servers.

“MCP is a powerful standard, but its value is most apparent in complex, high-stakes environments,” [Adel Zaalouk](https://www.linkedin.com/in/adelzaalouk/), AI product manager at [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), told The New Stack. “A key benefit of MCP is its ability to enable scalable, multitenant platforms.”

While [MCP enhances agents in many situations](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/), it’s not the best tool for every job. The emerging consensus is that MCP isn’t the best tool for deterministic or one-off integrations. When context is static or security is strict, [plain API calls often win](https://thenewstack.io/why-apis-are-essential-and-mcp-is-optional-for-now/).

In a blog post on [Medium](https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b), [Julien Simon](https://www.linkedin.com/in/juliensimon/), chief evangelist at [Arcee.ai](http://arcee.ai), which specializes in small language models, warned that MCP’s disregard for decades-long remote-procedure calling (RPC) system best practices could lead to “painful production failures” as enterprises build upon a fragmented constellation of third-party libraries.

So, when is MCP worth it? Below, we’ll dive deeper into some of these scenarios where MCP shines and where it’s not an ideal solution. We’ll also explore some emerging case studies and best practices to make the most of it in production.

## When MCP Makes Sense

There are a handful of cases where MCP servers shine, making it well worth adopting.

### Enhancing Agentic Workflows

MCP lets autonomous agents discover and invoke tools without rigid integrations, making it a powerful aid for development teams using AI agents to interact with external data, tools or other agents.

“MCP servers are exceptionally well-suited for complex agentic AI applications such as infrastructure automation, multiagent coordination and any scenario demanding rapid, secure access to heterogeneous enterprise resources under strict operational governance,” [Kevin Cochrane](https://www.linkedin.com/in/kevinvcochrane/), chief marketing officer at [Vultr](https://www.vultr.com/), a cloud infrastructure company, told The New Stack.

For teams already using multiple coding agents, MCP is a natural fit, said [Kun Chen](https://www.linkedin.com/in/kunchenxyz), lead principal engineer at [Atlassian](https://www.atlassian.com/).

“MCP is particularly worth adopting for teams already using agentic products, like Cursor or Rovo Dev, who are looking to delegate more mechanical or repetitive work to AI agents,” Chen told The New Stack. That might include creating to-do items, generating release notes or updating documentation, he added.

For individual contributors, using MCP can enhance workflows and improve productivity. “MCP is a great force multiplier,” [Toby Padilla](https://www.linkedin.com/in/tobypadilla/), principal product manager at [GitHub](https://github.com/), told The New Stack. “It can help an individual scale as it allows agents to drive existing platforms that were often built for humans.”

For example, [GitHub’s official MCP server](https://github.com/github/github-mcp-server) could allow an agent to review hundreds of issues and pull requests in minutes, Padilla said. MCP servers can also connect cloud services, such as creating a GitHub issue directly from a Slack chat.

### Providing Engineering Context

“Using MCP is a good way to introduce context into an agent’s workflow without needing to modify the agent itself,” [Tom Akehurst](https://www.linkedin.com/in/tomakehurst), CTO and co-founder at [WireMock](https://www.wiremock.io/), an API mocking tool, told The New Stack.

For example, the [Context7 MCP Server](https://github.com/upstash/context7) can pull current documentation or code libraries for AI editors, helping agents suggest more accurate code. A related project, [git-mcp](https://gitmcp.io/), exposes public GitHub repositories so agents can access up-to-date documentation and code contextually.

Beyond documentation, MCP also excels at syncing private data with [large language models (LLMs)](https://thenewstack.io/introduction-to-llms/), providing engineering context.

“AI-assisted coding is one of the use cases where we see huge adoption, and it makes sense to incorporate retrieval through MCP servers,” [Kacper Lukawski](https://www.linkedin.com/in/kacperlukawski/), senior developer advocate at [Qdrant](https://qdrant.tech/), a vector database, told The New Stack. This, he added, could help reference specific library versions, coding conventions or relevant examples.

### When No Other Standard Interface Exists

Not all platforms or workflows have a command line interface (CLI), API or popular integrations. This is a big area where MCP can help.

“MCP is worth adopting when it provides access to tools and services agents can’t already reach, or when it reflects user intents rather than mirroring existing CLIs,” [Viktor Farcic](https://www.linkedin.com/in/viktorfarcic/), developer advocate at [Upbound](https://www.upbound.io/), and host of the [DevOps Toolkit](https://www.youtube.com/@DevOpsToolkit) YouTube series, told The New Stack.

He shared a handful of good use cases where this is applicable:

* Bridging to services like Slack, [Google](https://cloud.google.com/?utm_content=inline+mention) Drive or email, where no CLI exists.
* Creating intent-focused tools like [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) EKS MCP that combine multiple APIs into meaningful operations.
* Building hybrid systems that mix deterministic code with agent decision-making for complex workflows, such as log analysis or Kubernetes deployment recommendations.

### Exposing Systems to Agents

Platforms and Software as a Service (SaaS) providers can also benefit by creating MCP servers as bridges to external AIs. “From a provider’s perspective, it’s worth considering MCP as an open standard to expose services to other AI agents,” Atlassian’s Chen said.

MCP can be useful for supporting “dynamic, real-time workflows,” according to [Gil Feig](https://www.linkedin.com/in/gilfeig), CTO of [Merge](https://www.merge.dev/), the unified API aggregator. “It’s also great at posting data into third-party systems.”

That could mean creating or updating support tickets, logging customer relationship management system interactions, triggering invoices in an enterprise resource planning (ERP) system or pushing updates into a project management tool.

MCP connections are especially useful for triggering APIs for fresh lookups or writing new data back into source systems, Feig added. For queries on older data, he advises maintaining a synced copy as an index for enterprise search, which avoids costly [semantic search](https://thenewstack.io/what-is-semantic-caching/).

By using MCP, multitenant platforms can avoid building custom integrations for each client. “The platform can simply connect to a customer-hosted MCP server that exposes their specific tools,” said Red Hat’s Zaalouk. “For providers serving numerous customers, each with unique tools and data, MCP offers a scalable solution.”

## When MCP Isn’t Worth It

On the other hand, in some cases, simpler solutions make MCP unnecessary and even overengineered.

### Replacing Deterministic Automations

MCP is overkill when workflows anticipate the same outcome each time. “MCP is not intended for deterministic workflows that don’t involve AI agents,” said Chen. “If your use case is simply about providing programmatic access to a service, traditional APIs are a better fit.”

Others agree APIs are better for routine automations, GitHub’s Padilla suggested. “LLMs and MCPs are great for dealing with ‘fuzzy’ requests or natural language,” he said. “If you need to accomplish the same task repeatedly, traditional programming and API calls are a better option.”

In these cases, traditional integration often wins, Feig noted: “MCP performs poorly compared to synced data for enterprise search that requires downloading content and handling complex access control lists.” APIs, he added, usually work best for static workflows.

### When Context Remains Static

Using MCP might be overkill if your engineering directives, like rules or preferences, remain relatively unchanged. “Introducing the MCP servers for context engineering makes sense only if we have enough knowledge that changes frequently, and when it is big enough that we prefer not to pass it on to each LLM call,” said Qdrant’s Lukawski.

Cochrane added that using MCP can be a sign of overengineering when requirements favor static, tightly coupled integrations: “In these settings, systems often operate in highly controlled environments with fixed functions, limited connectivity, and no need for dynamic discovery, multiagent orchestration or runtime composability.”

### Sidestepping Established CLIs

MCP is less relevant when agents can already execute CLI tools directly. “Ninety-five percent of MCPs fall into this category — they’re slower, more complex versions of tools that already work perfectly,” Upbound’s Farcic said, pointing to MCPs that mirror git commands or Kubernetes MCPs that replicate kubectl.

Akehurst also sees MCP as potentially overengineering for Infrastructure as a Service (IaaS), where an AI coding agent could just generate Terraform code to automate CI/CD.

### When Security Is Non-Negotiable

Unless MCP delivers clear productivity gains, it may not be worth [the risks](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/) of introducing it into an enterprise toolchain.

“In the enterprise, there are [significant security and compliance challenges with MCP](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/),” said Akehurst. Although work on MCP’s security architecture is ongoing, its vulnerabilities and lack of default controls may be too much for corporate governance.

“Many MCP servers are poorly built and maintained,” said Feig. Weak descriptions or incomplete implementations can lead to bad tool selections. “If you’re dealing with sensitive data and business-critical workflows, you may need to proceed with caution,” he added.

## MCP Can Deliver Real Value

Although MCP is new, some early case studies show tangible business value.

At GitHub, MCP servers help automate open source management duties. In a meta move, GitHub dogfoods its GitHub MCP server to manage the many contributions and issues submitted to the open source [GitHub MCP server](https://github.com/github/github-mcp-server) project.

“Internally, we use the GitHub MCP server to help classify and group those community contributions,” said Padilla. “It allows our small team to scale in a way that was impossible prior to MCP.”

Atlassian and WireMock are seeing similar momentum. Atlassian is experimenting with connecting agentic products to its remote MCP server to streamline tasks like Jira automation, while WireMock has attracted prospects with an MCP server that extends API mocking for coding agents.

Red Hat customers are also adopting MCP to scale secure data access. One European cloud provider used it to let non-technical users connect private data sources through a self-service AI platform built on OpenShift AI, according to Red Hat’s Zaalouk.

He added that one Red Hat customer, a large IT company, applied MCP to a multiagent underwriting system, allowing specialized agents to access different data sources without hard-coded integrations. “This streamlined a traditionally complex and human-intensive business process, leading to greater efficiency, reduced underwriting times, and more consistent decision-making,” he said.

Some projects are also exploring MCP for infrastructure management. For example, said Farcic, the [dot-ai MCP server](https://github.com/vfarcic/dot-ai) can translate a plain English request like, “I want an EKS cluster with monitoring” into the correct Kubernetes resources, reducing DevOps toil.

## Strategies for Operationalizing MCP

Although positive outcomes are being achieved using MCP, some patterns and best practices are emerging to help make the most of it in production — for both server providers and consumers.

### Tips for MCP Server Creators

For server designers, MCP tools require thoughtful planning beyond simply modeling pre-existing interfaces. “Simply wrapping existing REST APIs into MCP tools often results in AI agents struggling to use them effectively,” said Chen. More intuitive agent interfaces, he added, optimize token usage and deliver better results.

Others agree: Usable MCP tools require more than wrapping APIs. “Design MCPs around user intents, not API reflections,” said Farcic.

Akehurst cautioned, “Sometimes you need to reduce the range of abilities you’re making available via MCP to improve the odds of the AI behaving correctly. Curate a sparse set of non-overlapping tools, rather than just generating a one-to-one tool for every API call available.”

Clear directions help agents know when to invoke tools. One solution, advised Padilla, is to design with natural language in mind. “Match your tool names and descriptions as closely as possible to how people speak.”

Even simple naming conventions can help. For instance, GitHub’s `get_me` tool returns the authenticated user’s information. “When they say things like ‘show me my open issues,’ we can get the correct user’s information,” said Padilla. “Without that, the LLM was getting confused as to who ‘me,’ ‘my’ and ‘I’ was.”

Clear naming and logical organization should benefit agentic interactions with MCP, Cochrane said: “Logical grouping improves reasoning performance, reduces misuse and supports multiagent orchestration at scale.”

### Tips for MCP Server Users

For consumers, it’s important to keep humans in the loop. “Adoption should be approached with caution, keeping a human in the loop to ensure safety and reliability,” said Chen.

Some of this guidance can be programmed. For instance, GitHub has found that embedding custom instructions in the system prompt can help LLMs invoke the intended tools, according to Padilla. This could be a hint, he said, like “For GitHub actions, use the GitHub tools that are available to you.”

In addition to balancing human oversight with autonomous decision-making, visibility also matters. MCP servers should be deployed as shared services, not run locally, so all team members can access them remotely, said Lukawski. This eases maintenance and oversight.

But this sharing needs care, requiring policy enforcement, input validation, access controls and logging, said Cochrane. In effect, this means treating MCP with the same care you would take when exposing an API.

Cochrane also advised deploying MCP servers in a private, isolated cloud native environment and using private networking for internal tools. “Start small by wrapping existing BASH, Python or Go scripts with [FastMCP](https://gofastmcp.com/getting-started/welcome) to expose them as runtime tools without opening public end points or rewriting legacy code.”

## Knowing When To Use It

As with many tech trends, it boils down to knowing when (and how) to put MCP to use.

We’re already seeing strong cases emerge for enhancing software development productivity, especially for indeterministic reasoning in novel situations that focus on intent (rather than wrapping fully featured APIs) and giving AI coding agents more context on the fly.

But for programmatic automations that anticipate standardized results, MCP can cause unnecessary confusion and introduce security risks. Realizing return on investment also requires guidance, both as a creator and consumer of MCP servers.

All in all, these strategies are becoming increasingly important, as many place MCP at the heart of agentic AI’s architectural future.

“MCP will be for agentic AI what HTTP was for the web, enabling real-time interaction between autonomous agents and live enterprise systems,” said Vultr’s Cochrane. “Unless developers are working on niche services, MCP is something they can’t ignore.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)