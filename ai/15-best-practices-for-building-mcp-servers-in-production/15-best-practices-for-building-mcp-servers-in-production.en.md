The generative AI landscape is experiencing a fundamental transformation in 2025, driven by the widespread adoption of the [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP). As organizations increasingly recognize the limitations of fragmented AI integrations, MCP has emerged as the universal standard for connecting AI agents with enterprise systems, data sources and tools.

As [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) evolve from simple chatbots to sophisticated autonomous systems capable of multi-system interactions, the foundational architecture provided by MCP becomes increasingly critical for successful [enterprise AI transformation](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/).

Here are the current 15 best practices for Model Context Protocol development, incorporating the latest specifications and current standards.

**1. Treat each server as a bounded context**

Model your MCP server around a single microservice domain and expose only the capabilities that belong to that domain. Keep tools cohesive and uniquely named, with clear, JSON-schema’d inputs and outputs, so the client/LLM can disambiguate actions.

MCP’s tools design expects clearly typed, discoverable operations with accurate write schemas that include enums when possible, and thoroughly documented failure modes.

**2. Prefer stateless, idempotent tool design**

Your server will be called by agents that may retry or parallelize the request. Make tool calls idempotent, accept client-generated request IDs, and return deterministic results for the same inputs. Use pagination tokens and cursors for list operations to keep responses small and predictable.

The spec’s [JSON-RPC](https://www.jsonrpc.org/) contract and [transport](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports) guidance assume robust request/response semantics.

**3. Choose the right transport and implement cancellation**

Support stdio for maximum client compatibility today, and add Streamable HTTP when you need networked, horizontally scalable servers or incremental results. Note that the SSE transport has been deprecated and replaced by [Streamable HTTP](https://thenewstack.io/how-mcp-uses-streamable-http-for-real-time-ai-tool-interaction/) in the 2025-06-18 specification.

Implement request cancellation and timeouts to prevent long-running calls from stranding resources. Stdio is the baseline and preferred for development and testing, while Streamable HTTP has first-class transport for remote and networked deployments used in production.

**4. Embrace elicitation for human-in-the-loop workflows, but with caution**

Use [elicitation](https://thenewstack.io/how-elicitation-in-mcp-brings-human-in-the-loop-to-ai-tools/) to fill in missing parameters or confirm risky actions, but never to harvest sensitive data. Keep prompts concise, validate responses against your tool’s schema, and fall back gracefully if the host doesn’t support elicitation yet.

This is new in the June 2025 revision of MCP and not universally supported by mainstream MCP clients, so gate it with capability checks.

**5. Build for security first (OAuth 2.1, sessions, scopes)**

Follow the MCP security [best practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) mentioned in the specification. OAuth 2.1 is now mandatory for HTTP-based transports as of the March 2025 specification update.

Don’t use session IDs for auth, generate non-predictable session identifiers, verify all authorized requests, and minimize data exposure. Implement proper authorization server metadata discovery and dynamic client registration. Never echo secrets in tool results or elicitation messages.

**6. Adopt a “for the agent and the human” UX with structured content**

Your responses must be LLM-parsable and human-readable. Use structured content with JSON schemas for the model alongside traditional content blocks for users. The June 2025 [MCP specification](https://modelcontextprotocol.io/specification/2025-06-18/changelog) introduced the `outputSchema` and `structuredContent` fields, which enable precise, typed outputs. Keep error messages actionable by incorporating machine-readable codes along with brief explanations.

**7. Instrument like any production microservice**

Emit structured logs with correlation IDs, include tool name and invocation ID, record latency, success/failure, and token-cost hints if known. Surface soft limits and rate limits explicitly so agents can budget calls.

These practices align with the “manage tool budget” advice from operational guides and are well-suited to the standard SRE tooling best practices.

**8. Version your surface area and advertise capabilities**

Use [semantic versioning](https://www.postman.com/api-platform/api-versioning/) for your server and for individual tools when breaking changes occur. At connection/handshake time, publish your tool list, resource types, and optional features (such as elicitation and structured content), so that clients can adapt their behavior programmatically. The spec’s discovery model and architecture overview expect capability-driven clients.

**9. Keep prompts, tools, and resources decoupled and independent**

Store reusable prompts server-side and expose them via the MCP prompts interface. It’s not a good idea to hardcode long templates into tools.

Treat “[resources](https://thenewstack.io/how-to-build-rag-applications-using-model-context-protocol/)” as read-only or minimally mutable context surfaces with explicit URIs, access rules, and pagination. This separation simplifies testing and lets clients compose clean workflows.

**10. Handle streaming and large outputs responsibly**

When using Streamable HTTP, emit incremental chunks for long operations and advertise total counts where feasible. For large payloads, return handles/URIs to resources instead of inlining megabytes into a single tool result. Streamable HTTP’s single-endpoint design with dynamic upgrades optimizes for both simple queries and complex streaming operations.

**11. Test with real hosts and failure injection**

Validate against multiple MCP clients/hosts, including those that only support stdio. Inject faults that include slow downstreams, partial failures, and malformed inputs.

Use the official quickstart and inspector tools to verify discovery, schema validation, and error paths end-to-end. Test both traditional content blocks and new structured content outputs to determine their effectiveness.

**12. Package and ship like a microservice**

Containerize your servers, clearly declare the transport and invocation commands, and publish minimal runtime images. Provide a README with tool catalog, schemas (including output schemas), examples, and security notes.

Community guidance and early adopters emphasize the importance of container packaging and submission hygiene for catalogs.

**13. Respect platform and ecosystem realities**

MCP adoption is growing across Microsoft Windows, IDEs and vendor ecosystems, but capabilities differ by host. OAuth 2.1 support and structured content features may not be universally available yet.

Check platform notes before relying on new features; implement graceful degradation and feature flags to ensure smooth operation.

**14. Mind API design fundamentals**

Behind your MCP layer, keep the [microservice](https://thenewstack.io/introduction-to-microservices/) API clean with least-privilege operations, clear resource lifecycles, eventual consistency where appropriate, and idempotent mutations.

MCP is just the adapter, while your core domain model still benefits from classic API discipline. The JSON-RPC foundation reinforces the expectation of predictable request/response semantics.

**15. Document risks and obtain explicit consent for impactful actions**

For anything that changes state or spends money, require confirmation via elicitation or a “dry-run” mode, and return a diff of intended changes before execution.

Use structured content to provide machine-readable change summaries alongside human-readable descriptions. This mirrors security guidance and the human-in-the-loop intent of the new spec features.

## Conclusion

The Model Context Protocol represents a watershed moment in enterprise AI and agent development, transforming how organizations approach the integration challenge that has long hindered the adoption of AI at scale. These 15 best practices provide a comprehensive framework for building MCP servers in production environments.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)