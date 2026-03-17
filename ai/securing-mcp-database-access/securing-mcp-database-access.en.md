For 25 years, I’ve watched the database sit behind layers of protection: firewalls, VPNs, connection poolers, role-based access, and even change review boards. We built decades of tooling to make sure the wrong query never reaches production.

And now? We’re about to hand an AI agent a connection string, and that agent hallucinates column names.

That’s not a knock on AI. It’s a reality check. The [Model Context Protocol (MCP)](https://thenewstack.io/when-is-mcp-actually-worth-it/) gives LLMs a structured way to discover and invoke external tools. Database access is the natural next step, but it’s also the most dangerous.

Here’s the tension: MCP adoption is accelerating. Thousands of servers appeared across GitHub and public registries in 2025, and major vendors started experimenting with integrations. But the implementations are early, the security posture is inconsistent, and most teams connecting databases to AI agents haven’t grappled with the threat model.

This article is a primer on MCP database server administration for DBAs and platform architects. I’m going to show you why they are a different beast, what the spec actually secures, and what non-negotiable controls look like in practice.

The examples draw from gp-mcp-server, an open-source Spring Boot prototype I built to explore security patterns for Greenplum and PostgreSQL. It covers a lot of the common ground and gives us concrete code to talk about.

No smoke and mirrors, just real code, real security controls, and real architecture decisions.

## Why database access is the hardest MCP problem

Most MCP tools have a natural ceiling on what can go wrong. A file reader reads files, and a calendar tool manages events. The blast radius is predictable. Databases don’t have one.

SQL is expressive, composable, and in the wrong hands, destructive. A single valid query can dump sensitive tables, lock production resources, or exfiltrate data at scale.

> “The MCP server isn’t just an adapter. It’s the foundation everything else is built on. Get the foundation wrong, and the whole house comes down.”

Now pair that with an LLM that hallucinates confidently, falls for prompt injection, and optimizes for helpfulness over safety. Traditional database access assumes the caller understands what it’s doing. When an AI agent is that caller, that assumption breaks.

The MCP server isn’t just an adapter. It’s the foundation everything else is built on. Get the foundation wrong, and the whole house comes down.

## What the spec covers (and what it doesn’t)

You need to understand what the spec handles and what it leaves to you. That gap is where your engineering effort lives.

### The spec’s security evolution

The MCP spec moved fast, raising the security floor with each revision:

* 2024-11-05: Developers rolled their own auth. A nightmare.
* 2025-03-26: Standardized auth with OAuth 2.1 and PKCE.
* 2025-06-18: Mandatory Resource Indicators to stop token passthrough attacks.
* 2025-11-25: Enterprise IdP integration and machine-to-machine auth.

The direction is clear: tighter authentication, better enterprise controls. That’s the good news.

### The gap that actually matters

Here’s the bad news: the spec doesn’t govern server-to-database authorization. It defines how an AI client authenticates to your MCP server. It doesn’t touch how your server authenticates to the database. It doesn’t define what queries are permitted.

The spec treats the server as an intermediary, not a transparent token-forwarding proxy.

> “A proxy forwards identity. An intermediary enforces policy. It makes its own decisions.”

A proxy forwards identity. An intermediary enforces policy. It makes its own decisions.

The spec gives you the foundation, but you build the walls.

So how are teams actually building those walls? The answer depends on who you ask.

## The state of play

The database MCP server space is growing. Maturity varies wildly, and some of what’s out there is genuinely alarming.

### The reference implementation that got it wrong

Anthropic designed their original PostgreSQL MCP server as read-only. It wrapped queries in a transaction and rolled them back. Reasonable on the surface.

But Datadog Security Labs found a critical flaw: the server accepted semicolon-delimited multi-statement queries. An attacker could send COMMIT; DROP SCHEMA public CASCADE;. The COMMIT exits the wrapper transaction, and the DROP executes  
outside the safety mechanism.

> “Wrapping queries in a read-only transaction isn’t a security boundary. It’s like trying to imprison Magneto in a steel cage.”

The lesson: Wrapping queries in a read-only transaction isn’t a security boundary. It’s like trying to imprison Magneto in a steel cage. The defense itself is what the attacker uses against you.

How to stop this: The attack should never reach the database. A [production MCP server](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/) needs to enforce read-only mode by default and use policy-based controls to restrict which SQL statement types are permitted per role. The DROP should fail against the read-only database user at the connection level.

In gp-mcp-server, I built an additional safeguard: every query is parsed into an Abstract Syntax Tree (AST) using JSQLParser before execution, rejecting multi-statement queries outright. The attack dies in the parser before it ever reaches the database. That kind of layering is what defense in depth looks like in practice.

### The prompt injection nobody sees coming

This one’s more subtle. A researcher demonstrated an attack where a support ticket contained instructions to read a sensitive table. When an AI agent with elevated credentials reviewed the ticket, it followed the instructions and exfiltrated the data.

I call these the Snap Conditions. Three stones that have to be in the gauntlet for the attack to work:

* The Access Stone: The agent can reach private data.
* The Exposure Stone: Untrusted content enters the agent’s context.
* The Exfiltration Stone: The agent has a path to send data out.

All three have to be present. Remove any one, and the snap fails.

How to stop this: You can’t fix prompt injection with a single control. But you can remove the stones from the gauntlet:

* Policy controls: A mature MCP server needs a policy layer that defines allowed and denied SQL statement types per role, restricting what an agent can reach. In  
  gp-mcp-server, I built schema and table allowlists at the application layer for the same purpose.
* PII redaction: Mask sensitive data before it enters the [LLM’s context](https://thenewstack.io/better-context-will-always-beat-a-better-model/). Role-based column-level masking is the ideal, but even regex-based redaction makes a difference. In gp-mcp-server, I built a redaction engine that scans result sets for patterns like emails, SSNs, and custom tokens before the response goes out.
* Credential scoping: Enterprise implementations should map IdP roles directly to database users, so a readonly role gets readonly\_user credentials and an analyst gets analyst\_user. For environments where OAuth infrastructure isn’t in place yet, gp-mcp-server uses per-API-key connection pools with dedicated HikariCP instances to provide workload isolation.

### Hundreds of servers. Zero authentication.

Security scans in 2025 painted a grim picture. Researchers found hundreds of public MCP servers were exposed to the internet with no authentication or encryption. These weren’t edge cases or hobby projects. They were production-grade servers with direct database access and no audit trail.

How to stop this: Authentication has to be a first-class feature, not an afterthought. A production server should support multiple auth modes: development-only open access, Basic Auth for simple deployments, and OAuth 2.1 with enterprise IdP integration for real environments. TLS and mTLS should be fully supported.

In gp-mcp-server, I built structured API keys (gpmcp\_live\_{id}.{secret}) with the ID visible in logs for audit trails, the secret stored as a bcrypt hash, and method-level @PreAuthorize gating on every tool execution.

## The non-negotiables

The attack scenarios above show what goes wrong. Here’s what must go right. No database MCP server should touch production data without these controls. No exceptions.

### Principle zero: The agent is untrusted

Treat every query as hostile input. The LLM doesn’t understand your data model or compliance obligations. Trust nothing. Validate everything.

* Read-only connections: Non-negotiable privilege boundary at the database level. Every other control assumes this one exists.
* SQL validation: Policy-based filtering, AST-level parsing, and ideally both. Malformed or malicious queries die before they reach the database.
* Result constraints: Row limits, byte caps, timeouts. Token-aware truncation matters. 50,000 tokens back doesn’t give the LLM better answers. It wastes money and degrades reasoning.
* PII redaction: Server-side, before results enter the LLM’s context. Once data reaches the model, it’s ungovernable. There’s no “undo.”
* Credential isolation: Database credentials never appear in an MCP payload. Whether that’s OAuth token scoping or encryption at rest, an attacker who compromises the transport layer gets nothing useful.
* Authentication: Mandatory. Not optional. Not “we’ll add it later.” No key, no token, no query.

### The assembled stack

None of these controls work alone. Read-only connections don’t stop data exfiltration. SQL validation doesn’t redact PII. They work as a system.

Each control alone is a solo Avenger. Capable, but vulnerable. Stack them together, and you get the assembled team. The threat has to beat all of them simultaneously.

## Tool design is a security decision

The controls get you to the table. But how you structure the tools themselves shapes whether agents behave safely or recklessly.

The temptation is to expose a single execute\_query tool and let the LLM figure it out. That’s a security failure disguised as simplicity. An agent with only a raw query tool will generate whatever SQL it thinks is helpful. No guardrails. No guided workflow. No constraints on what it explores first.

The better approach is purpose-built tools organized around a deliberate workflow: Discover the Schema. Constrain the Query. Contain the Data. Instrument the System.

Discovery tools let the agent understand the schema before it writes SQL. Diagnostic tools return pre-computed, structured results instead of raw query output. This approach can deliver significant token savings, potentially reducing usage by an order of  
magnitude or more. That’s not just a cost win. Fewer tokens in the context window means less surface area for hallucination and less room for injected content to hide.

That decomposition is itself a security pattern. An agent with separate discovery, query, and diagnostic tools will naturally explore the schema before attempting ad-hoc SQL. An agent with built-in analytics tools has less reason to craft complex queries that push against policy boundaries. Tool design is prompt engineering by another name. Most teams aren’t pulling that lever yet.

In gp-mcp-server, I applied this principle with 12 tools focused on schema discovery, validated query execution, and data profiling, plus server-side cursor support for large result sets. I went deep on security and observability instead of wide across the DBA  
toolkit. A production implementation could expand that surface significantly with dozens of purpose-built tools covering diagnostics, analytics, and administration. Still, the principle holds: how you scope the tools determines how safely the agent operates.

## The most underappreciated security feature

One pattern that deserves more attention is user-defined tools via configuration. Custom SQL-backed tools, defined at runtime, no code changes required. Think about what that means. A database team can define precisely scoped tools.

Specific queries against specific tables with specific parameters. They hand those to AI agent users instead of open-ended query access. The agent gets the capability it needs. The database team retains full control over what SQL actually executes.

That’s the intersection of flexibility and governance that most MCP implementations are missing entirely. But even with all of these controls in place, the bigger picture matters more than any single feature.

> “The server between the AI agent and your data is the security boundary. Not the database’s own access controls. Not the LLM’s training. The MCP server.”

MCP database integration is here. The protocol is maturing. The use case is compelling. The patterns I’ve explored in gp-mcp-server show that secure-by-design is achievable: read-only defaults, policy-based access controls, layered authentication, and purpose-built tools that constrain agent behavior from the ground up.

But the broader space still ranges from “interesting experiment” to “actively dangerous.” The server between the AI agent and your data is the security boundary. Not the database’s own access controls. Not the LLM’s training. The MCP server.

The patterns exist, and the spec is ready. The implementations are open source and testable. The question isn’t whether AI agents will connect to your databases. It’s whether the security boundary will be in place when they do.

Discover the Schema. Constrain the Query. Contain the Data. Instrument the System.

That’s the blueprint.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/03/2e7b1e99-cropped-f02d5f98-dan-baskette-600x600.jpg)

Head of Technical Marketing | 25+ years building at the intersection of data platforms and developer experience (Sun Microsystems, EMC, Pivotal, VMware, Broadcom). When I’m not wiring AI agents to databases or hiking the Smokies, I’m insisting that everyone should...

Read more from Dan Baskette](https://thenewstack.io/author/dan-baskette/)