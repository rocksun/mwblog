# Remote MCP Servers: Inevitable, Not Easy
![Featued image for: Remote MCP Servers: Inevitable, Not Easy](https://cdn.thenewstack.io/media/2025/05/b5587e00-remote-mcp-servers-1024x576.jpg)
As we move deeper into 2025, interest and excitement around Anthropic’s [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) has grown unabated. But there’s still a lot of uncertainty around it: Is it really a game-changer, or is it just the latest piece in the hype cycle? In this series, I’ve tried to help you answer these questions.

In part 1, I dove [deep into MCP](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype) — what it is, what it isn’t and why you need to make it part of your infrastructure. In part 2, I looked at the main reason there’s so much buzz around it: [enabling agentic AI workflows](https://thenewstack.io/how-mcp-enables-agentic-ai-workflows/). And in this third and final part, I’ll explain the problems with local MCP servers, the issues you’re likely to encounter on your remote MCP journey and why a familiar tool can help you solve them.

## Drawbacks of Local MCP Servers
Today, the vast majority of MCP servers are run locally and leverage the standard input/output (`stdio`
) transport for local communication. This means every MCP server must be installed locally alongside the MCP client. While great for quick testing, this greatly hampers the ability to have a larger network of tools agents for the following reasons:

**Limited interoperability**: The beauty of MCP is in its ability to help stand up a diverse ecosystem of resilient services for large language models ([LLMs](https://thenewstack.io/what-is-a-large-language-model/)) and agents. Local MCP servers can’t be easily shared across teams, tools or agents — even with a registry, each user must manually install and configure them, which fragments the ecosystem.**No central updates**: Updates require every client to reinstall or re-sync manually, increasing maintenance overhead and the risk of version drift across environments.**Harder to secure and audit**: It’s more difficult to apply centralized security policies, monitor usage or audit tool behavior when each instance is running locally and independently.**Poor developer experience for consumers**: Other developers or agents can’t simply “call” your server or discover its tools unless they clone your whole setup, which stifles reuse and composability.
With Anthropic’s recent updates to the MCP spec, it is clearly setting the stage for an explosion in growth in remote servers that will help address the above concerns. This is most evident in the addition of experimental support for a “streamable HTTP” transport to replace the existing HTTP+[SSE](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse) approach. This eliminates the hard requirement for persistent, stateful connections and defaults to a stateless MCP server.

Additionally, Anthropic recently updated the MCP spec to introduce [MCP authorization based on OAuth 2.1](https://modelcontextprotocol.io/specification/2025-03-26). While a necessary step for remote MCP servers, there has been a lot of [discussion](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/205) around the issues introduced by this approach — namely, requiring the MCP server to act as both the resource and authorization server.

## Scaling Challenges for Remote MCP
MCP servers going remote is inevitable, but not effortless. While the shift toward remote-first MCP servers promises extensibility and reuse, it also introduces a fresh set of operational and architectural challenges that demand attention. As we move away from tightly coupled local workflows and embrace distributed composability, we must confront a number of critical issues that threaten both developer experience and system resilience.

### Authentication and Authorization Woes
The MCP specification proposes OAuth 2.1 as a foundation for secure remote access, but its implementation details remain complex and problematic. MCP servers are expected to act as both authorization servers and resource servers. This dual responsibility breaks conventional security models and increases the risk of misconfiguration.

Unlike traditional APIs that can rely on well-established identity and access management (IAM) patterns, MCP introduces novel identity challenges, particularly when chaining tools across nested servers with varying access policies.

### Security Risks and Tool Poisoning Attacks
One of the more subtle but critical vulnerabilities in the MCP model has been recently outlined by [Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks). In what it calls “Tool Poisoning Attacks (TPAs),” malicious actors can inject harmful instructions directly into the metadata of MCP tools. Since these descriptions are interpreted by LLMs as natural context, a poisoned tool could quietly subvert agentic reasoning and coerce it to leak sensitive data, perform unintended actions or corrupt decision logic.

These risks are exacerbated when MCP servers are publicly discoverable or shared across organizational boundaries, and no clear boundary exists to verify or constrain which tools are trustworthy.

### Fragile Infrastructure: High Availability, Load Balancing and Failover
When local tools break, it’s a personal inconvenience; when remote MCP servers fail, it’s a systemic failure that can cascade across an entire agentic workflow. High availability becomes a hard requirement in this world, especially when tool chains depend on server chaining. A single upstream server going offline could stall the entire plan execution.

Yet today, MCP lacks a built-in mechanism for load balancing or failover. These are critical gaps that need addressing as we rely more heavily on distributed composition.

### Developer Onboarding and Ecosystem Fragmentation
With the proliferation of MCP servers, discoverability becomes a pressing concern. How do developers find trusted, maintained servers? How do they know what tools are available or how to invoke them? While Anthropic has hinted at a registry system in its road map, no robust discovery solution exists today.

Without clear strategies for documentation, onboarding and governance, developers are left to navigate a fragmented ecosystem where reusability and collaboration suffer.

### Context Bloat and LLM Bias
Remote composition sounds elegant until you realize that each server added to a session expands the LLM context window. Tool metadata, parameter schemas, prompt templates — it all adds up, especially in high-churn, multi-agent environments.

And once tools are injected into context, there’s no guarantee they’ll be used wisely. LLMs are often biased toward invoking tools that appear in context, even when unnecessary. This can lead to redundant calls, bloated prompt chains and inefficient workflows. This problem will be exacerbated by the increasing number of remote servers being registered.

## The Gateway Pattern: An Old Friend for a New Interface
To folks who live and breathe APIs, many of these challenges sound familiar. Authentication quirks? Load balancing? Developer onboarding? These are the kinds of problems that modern API management tooling — especially [API gateways](https://thenewstack.io/ai-gateways-vs-api-gateways-whats-the-difference/) — have been solving for well over a decade.

MCP doesn’t replace APIs. It simply introduces a new interface layer that makes APIs more LLM-friendly. In fact, many MCP servers are just clever wrappers around existing APIs. So, rather than reinvent the wheel, let’s explore how we can apply the battle-tested API gateway to the emerging world of remote MCP servers.

### Auth? Already Solved
Gateways are already great at managing authentication and authorization, especially in enterprise environments. Instead of relying on each MCP server to act as its own OAuth 2.1 provider (a pattern that introduces security and operational complexity), you can delegate auth to a central gateway that interfaces with proper identity providers and authorization servers.

This simplifies token handling, supports centralized policy enforcement and adheres to real-world IAM patterns that organizations already trust.

### Security, Guardrails and Trust Boundaries
The gateway could serve as a vital security layer that filters and enforces which MCP servers and tools are even eligible to be passed into an LLM context. This provides a natural checkpoint for organizations to implement allowlists, scan for tool-poisoning patterns and ensure that only vetted, trusted sources are ever included in agentic workflows.

In essence, a gateway becomes a programmable trust boundary that stands between your agents and the open-ended world of MCP. When used properly, this alone could neutralize a large class of tool-poisoning attacks.

### Resilience, Load Balancing and Observability Built In
When MCP servers are registered behind a gateway, you get automatic benefits: load balancing, failover, health checks and telemetry. Gateways are built for high availability, and they’re designed to route requests to the healthiest upstream server.

This is critical for agentic workflows where the failure of one link could disrupt the entire chain. Add in monitoring and circuit breakers, and you’ve got the makings of a reliable, observable infrastructure layer that MCP currently lacks.

### Gateway as Developer Experience Engine
Modern API gateways don’t just route traffic but anchor entire developer ecosystems. API portals, internal catalogs, usage analytics and onboarding flows are all well-supported in today’s API management stacks. There’s no reason MCP should be different.

Exposing MCP servers through something like a gateway-managed developer portal can offer consistent discovery, documentation and access control, turning a fragmented server sprawl into a curated marketplace of capabilities.

### Tackling Context Bloat and Client Overhead
The final two problems — LLM context bloat and bias — are tougher nuts to crack. But this is where a future, more intelligent gateway could shine.

Imagine the gateway not just as a proxy, but as an adaptive MCP server: one that connects to upstream MCP servers, inspects their tools and selectively injects relevant context based on the user’s prompt. It could maintain persistent upstream connections and handle tool registration dynamically, reducing the need for spawning redundant client processes and minimizing token bloat in the LLM context.

Tools like mcpx have started down this road already, but it makes sense to centralize and scale this capability in the gateway. After all, it’s already the [front door](https://thenewstack.io/api-gateway-checklist-how-strong-is-your-apis-front-door/) to your organization’s APIs.

## Conclusion
As AI agents evolve from novelties to core components of modern software, their need for structured, reliable access to tools and data becomes foundational. MCP introduces a powerful new interface for exposing that functionality that enables agents to reason, plan and act across services. But as MCP servers move toward a remote-first model, the developer and operational complexity rises dramatically.

From authentication and load balancing to context management and server discovery, the road to remote MCP isn’t without potholes. Yet, many of these challenges are familiar to those who’ve spent time in the world of API infrastructure. That’s why an API gateway, long trusted for securing, scaling and exposing HTTP services, may be the perfect solution to extend MCP into production-grade, enterprise-ready territory.

At Kong, we believe this convergence is already happening. With the Kong Konnect platform and the Kong AI Gateway, organizations can begin to apply proven gateway patterns to emerging AI interfaces like MCP. From scalable auth to load balancing and developer onboarding, much of what’s needed for remote MCP is already here.

*Want to learn more? See how Kong is solving real-world MCP server challenges today.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)