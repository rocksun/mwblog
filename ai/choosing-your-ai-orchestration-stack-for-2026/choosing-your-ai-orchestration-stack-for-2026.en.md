AI has advanced [at an incredible pace](https://blogs.nvidia.com/blog/ces-2025-jensen-huang/). Just a few months ago, we were still talking about agentic AI’s budding capability to perform actions on systems as the [latest breakthrough](https://duplocloud.com/blog/ai-help-desk-for-devops/).

Now that’s old news.

The latest talk is on formalizing an [AI agent’s capabilities](https://duplocloud.com/blog/the-agentic-help-desk-devops-ai/) into an orchestration layer (a layer that allows agents to operate safely in production environments) and giving it:

* Context
* Appropriate access to systems.
* A workbench of tools.
* The ability to speak to other agents effectively.
* A mechanism that depends on human approval for key actions.

This layer, or better defined as a tech stack, can even allow agents to operate safely in production environments. It’s a foundational component in the proliferation of AI.

It unlocks new capabilities.

These requirements in an orchestration layer have given way to a [battle of standards](https://thenewstack.io/a2a-mcp-kafka-and-flink-the-new-stack-for-ai-agents/), software stacks, and interoperability. Each is vying to improve AI’s reach and [make it more effective](https://duplocloud.com/blog/master-cloud-infrastructure-management/). The most prominent of these is [Model Context Protocol (MCP)](https://thenewstack.io/is-model-context-protocol-the-new-api/), which acts as a server hosting [tools](https://duplocloud.com/blog/devops-automation/), context, and more.

So they’re available for AI agents to use.

These standards in orchestration are meant to make AI agents more stable, reliable and idempotent.

We’re basically creating a hub for AI agents to find what they need without getting overwhelmed.

## **Key Insights**

1. AI agents are no longer only about “can they act?” but how they act. They need proper context, tooling, human controls and safe access to systems. Your orchestration stack is the foundation.
2. While MCP dominates the tool/context plane, alternatives like [Agent‑to‑Agent Protocol (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) for peer messaging and Open Agent Standard Framework (OASF) for life cycle are gaining traction. The smart move is a hybrid stack.
3. Deploying agents in production means dealing with versioning, audit logs, idempotency, human approval, and context pruning. MCP-style systems address all of these. But lock-in, interoperability and [evolving standards](https://thenewstack.io/why-are-agent-protocols-like-mcp-and-a2a-needed/) are valid risks to consider when choosing your orchestration layer.

## **The Battle for Orchestration Layer Standards**

MCP isn’t without its (constructive) critics, and others are finding their niche as well. They are well worth mentioning.

And yes, MCP has some heavyweight backers like Microsoft, Google and IBM. But other standards that both complement and compete with MCP are backed by the likes of Meta AI, AWS and Stripe.

This complementary/competitive nature makes for a fascinating arena for these standards to grow and adapt together. They shape the future of AI.

Let’s take a look:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Standard / Protocol** | **Scope** | **Primary Backers** | **Status (Oct 2025)** | **Key Repo / Spec** |
| **MCP** – Model Context Protocol | Secure, versioned tool + context sharing | Microsoft, Google, Vercel, IBM, Anthropic | De-facto leader | [modelcontextprotocol.org](https://modelcontextprotocol.org/) |
| **A2A** – Agent-to-Agent | Peer-to-peer message passing, capability discovery | OpenAI, Meta AI, Hugging Face | Growing fast | [github.com/a2aproject/A2A](https://github.com/a2aproject/A2A) |
| **OASF** – Open Agent Standard Framework | Full life cycle (spawn, orchestrate, retire) | Linux Foundation AI | Request for comments stage | [github.com/agntcy/oasf](https://github.com/agntcy/oasf) |
| **ACP** – Agent Communication Protocol | Lightweight JSON-RPC for tools | IBM, LangChain | Stable, but niche | [github.com/i-am-bee/acp](https://github.com/i-am-bee/acp) |
| **x402** | Micro-payments for tool calls | Solana, Ehereum, etc | Stable | [x402.org](https://x402.org/) |
| **AGNTCY** | Graph-based workflow definition | The Linux Foundation, Google Cloud, etc | Community-driven draft | <https://github.com/agntcy> |

What’s the takeaway?

MCP leads the agent protocol space with cross-vendor SDKs, the most comprehensive benchmarks (MCPToolBench++), and built-in enterprise audit logging — features now being matched or approached by A2A and AGNTCY.

The rest are still complementary with focused objectives (e.g., A2A for peer communication).

## **Critical Feedback**

The orchestration standards battle isn’t just a technical debate. It’s sparking heated discussions among AI leaders, developers and researchers.

As adoption surges, opinions range from enthusiastic endorsements to sharp critiques on lock-in risks, security gaps and interoperability challenges.

### **Pro-MCP Voices: The ‘USB-C of AI’ Camp**

MCP’s backers hail it as the foundational “USB-C for AI,” solving the N×M integration nightmare where every [agent-tool pair](https://duplocloud.com/blog/platform-engineering-best-practices/) needs custom code.

*“MCP is going crazy viral right now… USB-C moment for AI”***— @[minchoi](https://x.com/minchoi/status/1900931746448756879?s=20), March 2025**

Early adopters like Block, Apollo and Zed report [faster agent prototyping](https://catalogimages.wiley.com/images/db/pdf/9781394368488.excerpt.pdf), with Sourcegraph noting contextual code gen with more functional code.

### **Critics of MCP: Real engineering is the solution**

Detractors of MCP are saying it’s *increasing* token consumption,

*“MCP creates context rot. There’s an easy fix but it requires us to do actual engineering rather than spray and pray…”***— @[curiouslychase, November 2025](https://x.com/curiouslychase/status/1986048303507833254?s=20)**

Likewise, auth creates an MxN problem, increasing attach surface.

*“Each agent needs to authenticate with each tool individually. If you’re running 10 agents across 20 tools, that’s 200 separate OAuth flows.”***— @[GoKiteAI, June 2025](https://x.com/GoKiteAI/status/1933770964770095598?s=20)**

### **Community Sentiment (Oct 2025 Survey)**

[DuploCloud’s 2025 AI + DevOps Repor](https://duplocloud.com/ebooks/state-of-devops-2026)t, based on 135 engineering leaders, echoes these trends.

We found that 67% of teams increased AI investment in DevOps. And nearly 80% are exploring agentic, execution-ready automation.

Our report shows that DevOps success now depends on secure orchestration layers that deliver speed, compliance and human-in-the-loop control. These are the same traits fueling MCP-style adoption in production environments.

The Overall Consensus? MCP wins tools, and A2A owns collaboration. OASF could unify by 2026.

## **Trends Shaping the Battle**

The standards battle is accelerating amid explosive growth. The AI orchestration market is expected to hit [$11.47 billion in 2025](https://www.researchandmarkets.com/reports/5951945/artificial-intelligence-ai-orchestration) (23% compound annual growth rate).

Here’s the pulse, backed by data, examples, and forward signals:

* **From open source agentic projects to visual builders like n8n:** n8n v2 now ships native MCP nodes.
* **Use of MCP servers is proliferating**, from open source to commercial services at big names like Vercel AI Gateway, Azure MCP Hub, Google Context Broker and [IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention) Watson Orchestrate, all GA in Q3 2025.
* **Context engineering**: With token windows expanding to 1million+, MCP v1.3 introduces pruning, summary caching and semantic chunking to combat overload. They retain only relevant threads. This is critical for long-running swarms where context bloat previously caused 30 to 50% failure rates.

Additional trends accelerating the ecosystem:

* **Human-in-the-loop 2.0**: MCP approval hooks integrate Slack/Teams with service-level agreement timers (e.g., auto-escalate after 5 minutes). This blends autonomy with oversight. It’s standard in finance, where agents pause for CFO sign-off on transfers.

**An orchestration layer with such characteristics is a crucial requirement for AI agents to operate safely in production.**

## Why Code Your Own MCP Server? (vs. Pre-Baked Open Source)

Pre-baked servers (LangChain MCP, Vercel Gateway) are great for quick starts, but [custom servers](https://duplocloud.com/blog/ending-the-hero-culture-in-devops/) unlock substantially greater value for production:

1. **Full control and customization** (65% faster iteration, per Gartner): Tailor idempotency (if cached\_result: return it), add custom authorization or embed domain logic. Pre-baked can’t touch your proprietary workflows.
2. **Cost savings** (30-50% tokens): Integrate lightweight LLMs directly in tools; prune context at the server level. Open source hubs charge per-call or limit scale.
3. **Security/compliance** (enterprise must): Full audit trails, role-based access (RBAC) for tools and zero vendor data leaks. Pre-baked often log to third-party clouds.
4. **Scalability** (Handle more than 1,000 requests per second): Async processing, version pinning, and horizontal scaling.
5. **Extensibility and integration**: Chain with internal systems (ERP, CRM), add x402 payments or A2A peering. Pre-baked locks you into their ecosystem.

|  |  |  |
| --- | --- | --- |
| **Aspect** | **Pre-Baked Open-Source (LangChain/Vercel)** | **Custom MCP Server** |
| Setup Time | 5 mins | 20 mins |
| Cost/Month | $50+ (hosting + limits) | $10 (your infra) |
| Customization | Plugins only | Full source control |
| Security | Shared responsibility | Your vault |
| Scale | 100-500 RPS | 1k+ RPS |
| Vendor Lock | High (their updates) | None |

**Pro Tip:** Start with pre-baked for minimum viable product, migrate to custom for production. Full repo: [github.com/simple-mcp-agent](https://github.com/simple-mcp-agent).

## A2A: The Decentralized Challenger to MCP’s Throne

While MCP dominates tool discovery and context, A2A (Agent-to-Agent) is quietly becoming the de facto standard for peer communication. Think “WebRTC for AI agents.” Launched in late 2024 by OpenAI, Meta AI, and Hugging Face, A2A v0.9 already powers more than 120 SDKs. And it’s growing faster than MCP did at the same stage.

### **Why A2A Matters**

|  |  |  |
| --- | --- | --- |
| **Feature** | **MCP** | **A2A** |
| **Primary Focus** | Tool + context server | Peer messaging + capability negotiation |
| **Transport** | HTTP/2 + gRPC | WebSocket + optional QUIC |
| **Discovery** | Static catalog | Dynamic /.well-known/a2a-capabilities |
| **Security** | mTLS + JWT | OAuth 2.1 + mutual TLS + optional ZK-proof |
| **Latency (100-agent swarm)** | ~180 ms | 92 ms (A2A PeerBench) |

### **How A2A Complements (and Competes with) MCP**

MCP forms a tool plane (versioned, auditable) while A2A forms the communication plane (async, multimodal). This allows for more streamlined flows post-MCP.

Here’s an example of such a flow:

1. Agent discovers tools via MCP.
2. Negotiates task delegation via A2A.
3. Executes via MCP call.
4. Returns result over A2A stream.

### **Criticisms and Risks**

A2A is definitely still young, still without built-in logging, and depends on OASF or similar. It lacks decentralization, depending on Hugging Face’s registry, and must undergo rapid development and breaking changes to mature.

*“MCP gives you the hammer. A2A teaches agents to talk about which nail to hit.”***[— @surfer\_nerd, November 2025](https://x.com/surfer_nerd_/status/1988300454376468649?s=20)**

## The Road Ahead

The orchestration battle is intensifying, with convergence on hybrid stacks but rapid innovation at the edges.

From MCP 2.0’s upcoming release, OASF’s approval vote at The Linux Foundation, and a joint effort between Google, AWS the EU’s AI act imposing accountability, and Hugging Face to integrate A2A and ACP via RPC, expect 80% of enterprise AI to run on orchestrated agent stacks composed of these and new technologies that have yet to be invented.

Open, composable stacks prioritize reliability over hype.

## **Conclusion**

At DuploCloud, we’re excited to be part of the forefront of AI advancements, learning, stumbling, learning some more, and most importantly, creating and participating in the innovation that is shaping the future.

We’d love for you to [check out our AI Helpdesk](https://duplocloud.com/request-a-demo-2/). Or join our newsletter to see the latest ground we’re breaking.

## **FAQs**

### **What differentiates an orchestration layer from an agent framework or LLM?**

An orchestration layer sits around the LLM/agent. It gives the agent context (historical external state, tool catalog) and manages access to systems and tools. It also ensures human approval workflows and handles audit and logging. So agents behave in production-grade ways. Without it, agents are merely experimental and uncontrolled.

### **Is MCP enough on its own for every use case?**

Not exactly. MCP is strong in the “tool/context plane,” like versioned tool invocation, context sharing and audit logs. But for peer-to-peer communication (agents talking to agents), dynamic negotiation, edge cases (blockchain agents) other [standards like A2A may be needed](https://thenewstack.io/cloud-native-and-ai-why-open-source-needs-standards-like-mcp/). The smart strategy is stack layering, not betting solely on one protocol.

### **How do I evaluate which orchestration stack to use in my organization?**

Consider your priorities:

* Governance and audit (MCP + ACP)
* Low-code/visual workflows for speed (AGENTCY/n8n)

From there, map your tooling coverage, vendor lock-in risk, interoperability requirements and maturity of SDKs/backers.

### **What are the key risks of choosing an orchestration standard too early?**

There are several:

* Vendor lock-in and ecosystem capture.
* Incompatibility between evolving protocols.
* Security gaps (prompt injection, tool exfiltration) may occur if standards remain immature.
* Over-engineering or choosing heavyweight stacks too soon when needs are simpler.

Planning for flexibility and hybrid adoption is prudent.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/11/8ab68578-cropped-1ea063ec-cameron-mcdougle-scaled-1-600x600.jpg)

Cameron McDougle is a DevOps/MLOps engineer working in developer relations at DuploCloud, an AI-powered DevOps platform. He has worked with cloud infrastructure, automation and AI for six years and loves to surf.

Read more from Cameron McDougle](https://thenewstack.io/author/cameron-mcdougle/)