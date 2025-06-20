The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is quickly becoming a standard for AI agents and servers, defining how agents discover, authenticate to and invoke remote tools and services. But securing OAuth-based MCP servers is trickier than it looks.

Recent updates to the MCP Security Best Practices specification, led by security experts including [Den Delimarsky](https://github.com/dend) and [Paul Carleton](https://www.linkedin.com/in/paulcarletonjr/?originalSubdomain=uk), have [highlighted critical gaps](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/) in current deployments, particularly around confused deputy attacks and token-handling vulnerabilities. In this article, I’ll walk through how to close these gaps and why proxy-enforced OAuth is essential for secure MCP architectures.

## **What the MCP Spec Requires — and What It Leaves Out**

The [MCP Security Best Practices specification](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) establishes clear requirements:

* **Place MCP servers behind a proxy** — Mandatory for production deployments
* **Enforce authentication and validate token audience and scopes** — Required for all protected resources
* **Prevent token passthrough** — Critical for avoiding vulnerabilities
* **Audit all access** — Essential for compliance and incident response

However, examining current MCP deployment patterns reveals a significant implementation gap. Many developers deploy MCP servers directly exposed to clients, implementing [OAuth](https://thenewstack.io/oauth-2-0-a-standard-in-name-only/) at the application level rather than through dedicated proxy infrastructure. This approach, while functionally adequate for basic authentication, fails to address the dynamic authorization requirements that the security specification anticipates including per-request policy evaluation, prevention of token passthrough and contextual trust enforcement beyond [static OAuth scopes](https://auth0.com/docs/get-started/apis/scopes).

The specification explicitly warns about the “confused deputy*“* problem, where an MCP server that calls downstream services can unintentionally perform privileged actions on behalf of an attacker. Recent updates to the security guidelines, contributed by security experts including [Delimarsky](https://www.linkedin.com/posts/activity-7333383043421716480-kzjS), emphasize three critical requirements: preventing confused deputy attacks through per-client user consent validation, eliminating token passthrough to maintain proper trust boundaries and preserving audit trails for every token use. These updates to the MCP Security Best Practices specification underscore the gap between basic OAuth implementation and production-ready MCP security.

## **Why VPNs Break Modern Agentic Architectures**

Traditional enterprise security models relied on VPN-based perimeter protection, but this approach creates fundamental incompatibilities with modern agentic access patterns. When organizations attempt to protect MCP servers using VPN requirements, they encounter a critical constraint: Hosted AI services like [Claude](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) or [ChatGPT](https://thenewstack.io/ai-agents-must-learn-from-chatgpts-data-wrongs/) cannot establish VPN connections to private networks.

This limitation forces an architectural choice: either restrict agentic access to fully internal deployments (eliminating the benefits of hosted AI services and access to frontier models) or expose MCP servers to public networks with robust application-layer security. The latter approach aligns directly with zero trust principles, where network location provides no inherent trust and all authorization decisions occur at the application layer.

The MCP specification acknowledges this reality by mandating proxy architectures rather than network-level controls. However, the specification doesn’t define how these proxies should implement the dynamic [authorization policies necessary for agentic access scenarios](https://thenewstack.io/agentic-access-is-here-your-authorization-model-is-probably-broken/).

## **Zero Trust: The Enforcement Layer MCP Needs**

The MCP Security Best Practices acknowledge many security challenges but stop short of mandating comprehensive solutions. While the specification requires proxy architectures and token validation, it doesn’t specify how to implement per-request context evaluation — a critical gap for agentic access.

This is where [zero trust security](https://thenewstack.io/what-is-zero-trust-security/ "zero trust security") principles become essential. Zero trust adds the contextual layer that OAuth and even well-implemented MCP proxies lack:

* **Who** is making the request (identity verification)
* **What** they’re trying to access (resource validation)
* **When** the request occurs (time-based policies)
* **Where** it originates from (location and device context)
* **Why** the action is needed (behavioral analysis)

**Zero Trust Core Principles Applied to MCP:**

* **Never trust, always verify**: Evaluate every MCP method call independently, even for agents with valid credentials.
* **Least privilege access**: Restrict actions beyond OAuth scopes using fine-grained context.
* **Assume breach**: Monitor for anomalous behavior, even from valid tokens.
* **Continuous verification**: Reassess each request as conditions evolve.
* **Context-aware authorization**: Validate requests against real-time conditions, not just static scopes.

## **Identity-Aware Proxies: Enforcing MCP Security in the Real World**

The [MCP specification](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) strongly recommends proxy architectures but doesn’t specify how to implement the enforcement logic. Identity-aware proxies (IAPs) provide the missing enforcement layer.

An IAP that understands MCP protocols can:

1. **Intercept and decode MCP requests** — including MCP-specific actions like `InvokeMethod`, enabling enforcement of prompt injection protections and data loss prevention (DLP) policies.
2. **Extract context** — such as identity, device posture, location and request specifics.
3. **Evaluate policies in real time** — using centrally defined rules.
4. **Enforce per-request decisions** — not just session-based checks.
5. **Audit every request** — with full context and decision rationale.

### **Basic Identity-Aware Proxy Flow for MCP Authentication**

![Basic Identity-Aware Proxy Flow for MCP Authentication](https://cdn.thenewstack.io/media/2025/06/9b844950-ztna-mcp.png)

Source: Pomerium

This architectural pattern translates to straightforward proxy configuration:

|  |  |
| --- | --- |
|  | # Basic IAP configuration for MCP  routes:    - from: https://mcp-server.company.com      to: http://internal-mcp-server:8080/mcp      name: Internal MCP Server      mcp: {} |

This enables:

* **Granular action control**: Evaluate method calls, not just scopes
* **Centralized enforcement**: Maintain consistent policy across services
* **Dynamic delegation**: Adjust permissions based on context

## **Reference Implementation: Identity-Aware Proxy Patterns**

Identity-aware proxies can bridge the MCP security specification and zero trust enforcement. Open source implementations like Pomerium demonstrate this approach, with MCP support available for organizations seeking reference architectures. Several vendors offer IAP capabilities suitable for MCP deployments, each with different strengths: open source solutions provide transparency and customization while commercial platforms offer enterprise support and integration.

### **MCP Spec Compliance Patterns**

* **Proxy architecture**: Intercepts MCP traffic and enforces method-level access control
* **OAuth 2.1 integration**: Supports Proof Key for Code Exchange (PKCE), dynamic client registration and prevents token passthrough
* **Token validation**: Ensures audience-specific, scope-appropriate access
* **Auditing**: Includes the method being called, tool parameters and authorization decisions within each log

### **Token Separation Pattern Preventing Passthrough Vulnerabilities**

![Token Separation Pattern Preventing Passthrough Vulnerabilities](https://cdn.thenewstack.io/media/2025/06/0e606bc1-ztna-oauth-mcp.png)

Source: Pomerium

This pattern implements proper token separation through configuration. The following example shows a Pomerium-specific configuration pattern for token separation:

|  |  |
| --- | --- |
|  | # Token separation pattern for upstream OAuth  routes:    - from: https://github-mcp.company.com        to: http://github-mcp:8080/mcp      name: GitHub MCP      mcp:        upstream\_oauth2:          client\_id: ${GITHUB\_CLIENT\_ID}          client\_secret: ${GITHUB\_CLIENT\_SECRET}          scopes: ['read:user', 'user:email']          # ... endpoint configuration |

Beyond enforcing proper trust boundaries, fronting MCP servers with an identity-aware proxy also protects sensitive third-party OAuth tokens for services like GitHub, Salesforce, etc. from being exposed to AI agents or large language models (LLMs). Without a proxy, these upstream tokens could be passed to agents where they might be stored, logged or even exposed in case of a breach. This risk is not theoretical: Recent legal cases, such as the OpenAI court order, have highlighted that LLM providers may retain all user data, including tokens.

A properly configured proxy will issue short-lived internal tokens that are valid only within the context of the current user session and for specific downstream calls, dramatically reducing the exposure surface for sensitive credentials.

### **Zero Trust Enhancement Patterns**

* **Per-request context evaluation**: Evaluates requests based on time, location, user status and more
* **Dynamic policy engine**: Uses policy languages for real-time, data-driven decisions
* **Session-independent authorization**: Authorizes each call separately
* **Behavioral monitoring**: Detects and restricts anomalous agent behavior

If you’d like to see a working example, the [Pomerium MCP demo](https://github.com/pomerium/mcp-app-demo) provides a reference implementation of these patterns, including secure OAuth 2.1 flows, token separation and zero trust policy enforcement for MCP servers.

### **Implementation Examples**

Reference implementations typically demonstrate:

* Working OAuth 2.1 flows for agents
* Configuration patterns for secure MCP deployment
* Sample policies (time-based, group-based, rate limiting)
* Monitoring and alerting tied to agent behavior

## **From Compliance to Confidence: A Secure MCP Roadmap**

### **Implementation Phases**

**Phase 1: MCP Security Compliance**

* Deploy proxy architectures
* Validate tokens and scopes per OAuth 2.1
* Log all access with full context
* Prevent token passthrough

**Phase 2: Enhanced Authorization**

* Add per-request policy evaluation
* Use context-aware decision-making
* Manage policies centrally
* Assess risk dynamically

**Phase 3: Operational Integration**

* Integrate MCP auth into existing IAM systems
* Monitor agent behavior continuously
* Plan incident response for autonomous access
* Set governance for agent permissions

### **Solution Evaluation Framework**

When evaluating IAP solutions for MCP security, consider policy expression flexibility, MCP protocol support, integration with existing identity systems, audit capabilities and operational overhead. Organizations should evaluate options based on their specific requirements for policy complexity, integration needs and operational model.

### **Operational Implications**

Security now requires:

* **Infrastructure** changes to support proxy and IAP components
* **Security expertise** in dynamic, behavior-based authorization
* **Monitoring and alerting** tuned for machine-driven agent behavior, not human workflows
* **Cross-functional alignment** between platform, app and security teams

The Model Context Protocol standardizes the way agents interact with tools and data. Implementation determines whether those interactions remain safe and auditable in production.

[OAuth 2.1 in MCP](https://modelcontextprotocol.io/specification/draft/basic/authorization) provides the foundation. Zero trust makes it secure.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/03/1c77cf58-nicktaylor.jpeg)

Nick is a developer advocate at Pomerium, a zero trust, identity-aware proxy platform that enables secure, clientless connections to web applications and services without a corporate VPN. With over a decade of open source contributions and five years of professional...

Read more from Nick Taylor](https://thenewstack.io/author/nick-taylor/)