**Over the past nine months**, Amazon, Microsoft, and Google have each introduced or renamed an enterprise agent platform. And all three have converged on the same core architecture. Runtime, memory, tool gateway, identity, observability, and governance now appear in [Amazon Bedrock AgentCore](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available), [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/overview), and the [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform), albeit under slightly different names. Each vendor presents these components as the foundation for production agents. What was a fragmented collection of libraries just 18 months ago is becoming a distinct platform layer.

To see where that shift may lead, consider the evolution of platform as a service. Between 2011 and 2016, developers built applications from virtual machines, load balancers, message queues, secret stores, and monitoring agents — each with its own API and operational model. [Cloud Foundry](https://thenewstack.io/open-source-platform-engineering-a-decade-of-cloud-foundry/) and Heroku unified those pieces around an application contract. Developers could think less about machines and more about applications. The agent ecosystem is approaching a similar inflection point, but it still lacks an equivalent contract — and no open-source project has stepped forward to define one.

To appreciate where this goes, we need to look at the evolution of platform as a service. Between 2011 and 2016, developers assembled applications from virtual machines, load balancers, message queues, secret stores, and monitoring agents, each with its own API and operational model. [Cloud Foundry](https://thenewstack.io/open-source-platform-engineering-a-decade-of-cloud-foundry/) and Heroku unified those pieces around an application contract. Developers stopped thinking about machines and started thinking about applications. The agent ecosystem has no equivalent contract, and no open project has claimed it.

## The plumbing a production agent still needs

Imagine a platform team putting a customer support agent into production this quarter. They choose a model provider, then a framework, and finally a place to store session state and long-term memory. They add a tool gateway so the agent can reach the ticketing system. An identity layer follows, so the agent acts on behalf of the person who asked, and a sandbox keeps generated code somewhere safe. Evaluation and tracing are considered last, once someone asks how quality regressions will surface before customers find them.

Each of those choices looks small on its own. When combined, they decide which cloud the workload lives in. Session state resides in a single provider’s managed store. The traces are logged in that same provider’s telemetry service, and the agent’s identity is derived from its directory. Moving that agent a year later means rebuilding the whole assembly, which is where enterprises were before PaaS gave applications a portable shape.

## What Cloud Foundry got right before it lost the market

Cloud Foundry reduced application deployment to a single command, and the platform took responsibility for everything after it. [Buildpacks](https://buildpacks.io/) detected the language and produced a runnable artifact. Service brokers provisioned a database or a message broker and bound the credentials into the application environment. Routing, logging, autoscaling, and health checks arrived as platform behavior, not as a queue of tickets aimed at an operations team.

What mattered was the contract, not the implementation. An application declared what it needed and stayed agnostic of where it ran. Buildpacks began life at Heroku back in 2011. Pivotal and Heroku started the Cloud Native Buildpacks project in January 2018, and the CNCF accepted it that October. A PaaS idea outlived the platform that produced it.

Cloud Foundry never became the dominant platform. Kubernetes did, and the Cloud Foundry community eventually rebuilt its abstraction on top of Kubernetes through [Korifi](https://www.cloudfoundry.org/technology/korifi/). The design principles traveled anyway, and enterprises running that platform in 2016 had portability that most agent teams cannot buy today.

## The same primitives across three clouds

Let me dissect the three platforms because the similarities are conveniently hidden behind the branding.

AgentCore reached general availability in October 2025 with seven composable services, namely runtime, gateway, memory, browser, code interpreter, identity, and observability. The runtime offers eight-hour execution windows with complete session isolation. The gateway connects to existing MCP servers and turns APIs and Lambda functions into agent-compatible tools, while observability exports through OpenTelemetry into CloudWatch.

Microsoft renamed Azure AI Foundry to Microsoft Foundry effective January 1, 2026. Foundry Agent Service covers the same ground. Microsoft documents hosted agents running in a session-isolated managed runtime, with Entra Agent ID handling identity. Managed memory spans session, user, and procedural scopes, and tracing is built on OpenTelemetry.

Google retired the Vertex AI name at Cloud Next 2026 and folded the platform into [Gemini Enterprise Agent Platform](https://thenewstack.io/google-gemini-agent-platform/). What was Agent Engine became Deployments, and Memory Bank, Sessions, Agent Registry, Policies, and Gateways sit alongside it under an agent-first information architecture.

The convergence is rational behavior rather than a conspiracy, since infrastructure companies build vertically integrated platforms because integration is where the margin lives. The consequence lands on customers rather than on the vendors. Identity, telemetry, and deployment all terminate within a single provider, which makes the operational layer beneath the agent the part that resists moving. Recently, I analyzed the runtime aspect of this problem in a piece about Google’s [Agent Substrate](https://thenewstack.io/kubernetes-ai-agent-runtime/).

## The contract an agent platform would inherit

Any agent platform can be tested by one question: what would a Cloud Foundry-style contract look like if it had been written for agents rather than for web applications? The mapping is close enough to be instructive and different enough to be interesting.

| PaaS abstraction | Agent platform equivalent | Where portability breaks today |
| --- | --- | --- |
| Application source | Agent code, instructions and evaluation suite | Each framework defines its own package shape |
| Buildpack | Framework detection and agent packaging | No shared build contract across SDKs |
| Backing service | Model, memory, retrieval or tool provider | Providers are wired into agent logic |
| Service binding | Authenticated attachment of tools and data | Credentials are issued by the host cloud |
| Router | Agent endpoint, MCP or A2A interface | The protocols exist but not the lifecycle |
| Logs and metrics | Traces, tool calls, cost and quality scores | GenAI conventions remain in development |
| Release promotion | Evaluate, version and progressively deploy | Evaluation couples to one vendor’s harness |
| Platform policy | Agent identity, permissions and approvals | Identity ties to the provider’s directory |

Real deployments will mix these rows rather than adopt them cleanly, and no team needs the complete set from day one.

### Package the agent as one deployable unit

The thing developers ship has to be versionable, testable, and movable as a single artifact. The code, the instructions, the tool dependencies, the memory contract, the permissions, and the evaluation suite all travel together, or none of them do. AWS gets close with its [harness](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/) export path. One command turns a configured harness into Strands code, and AWS says the export preserves the model, prompt, tools, memory wiring, and container environment. Customers can easily move from configuration to code without an architecture rewrite, which is the right instinct pointed at a single cloud.

### Bind capabilities rather than embed providers

The [Twelve-Factor App](https://12factor.net/) taught developers to treat databases and caches as attached resources reached through configuration. Models, memory stores, retrieval engines, browsers and tool gateways deserve the same treatment. An agent that names its model provider inside application logic has already given up portability, whatever the platform brochure claims.

### Make operations part of the abstraction

Rather than just enabling deployment, PaaS proved its value by offering built-in capabilities like routing, logging, autoscaling, and rollback. The questions that matter for agents look different, and they should be the ones enterprises must ask. Platform teams want to know whether the agent completed the task and whether it chose the right tools. They also want to know whether it exceeded its authority, what the run cost was, and whether quality regressed after a model update.

## How agents differ from applications

Agents are not web applications with a model attached, and a platform built on that assumption will fail in production. Three differences carry most of the weight here. Agent behavior is probabilistic, so two identical inputs can produce different tool calls. Agents act with delegated user authority, which turns a permissions bug into a real-world side effect rather than an error page. An agent’s dependencies can also change its behavior without any code deployment. A model update or a revised tool description alters what the agent decides to do.

The Twelve-Factor rule that processes should be stateless does not survive that. An agent platform needs disposable execution workers alongside durable, inspectable, and portable agent state. [LangGraph](https://docs.langchain.com/oss/python/langgraph/durable-execution) already demonstrates the combination in open source, with checkpointing at every step, first-class human interrupts, and execution that resumes after a crash. The control plane around it is part of the commercial LangSmith product, covering deployment, evaluation, and observability. The fragmentation appears within a single project.

## What the open protocols leave out

Most of the primitives a neutral platform would need already exist. The [Model Context Protocol](https://modelcontextprotocol.io/) standardizes how agents access tools and data. [A2A](https://a2a-protocol.org/) covers discovery and communication between independent agents. [OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/gen-ai/) is defining GenAI conventions for agent spans, tool calls, and token usage, though most of those attributes remain marked as in development. OCI images stay available as the packaging escape hatch for anything a managed runtime cannot host.

The vendors have already conceded that a neutral layer matters. The Linux Foundation [announced](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) the Agentic AI Foundation in December 2025. Its founding projects were MCP from Anthropic, goose from Block, and AGENTS.md from OpenAI, and AWS, Google, and Microsoft joined as platinum members. Google also moved A2A into the Linux Foundation.

Protocols are not the same thing as a lifecycle platform. A foundation that governs how agents talk to tools says nothing about versioning an agent. It says nothing about promoting that agent through environments, or rolling it back when an evaluation regresses. Enterprises running diligence on agent platforms can work through three plain questions. The first is governance: whether the project is controlled by a neutral foundation or by the vendor selling the managed version. The second is packaging, where the same agent artifact should run on two different clouds without a rewrite. The third is state, where memory has to live somewhere the enterprise can export from. No open project answers all three today.

## Where is this headed?

Kubernetes defined pods, deployments, and services, and those abstractions influenced how an entire industry thinks about running software. The equivalent agent abstractions have not been fixed yet. Whoever ends up owning the agent control plane will not merely own deployment. That owner defines what an agent is, which components it contains, and what a platform team is permitted to swap out.

In summary, hyperscalers are building robust platforms that effectively address operational questions. They also answer them inside a single cloud. If a neutral project assembles the same lifecycle atop the protocols already in place at the Linux Foundation, enterprises will regain the negotiating position that buildpacks and service brokers once gave them. An open, cloud-agnostic agent platform would benefit vendors as much as buyers, because a stable contract is what allowed the cloud-native ecosystem to grow beyond any single provider.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)