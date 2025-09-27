The transformation of generative AI (GenAI) from conversational tools to autonomous, [action-oriented agents](https://thenewstack.io/5-factors-for-predictable-autonomy-with-agentic-ai/) marks a [significant inflection point](https://thenewstack.io/why-agentic-ai-orchestration-is-key-to-managing-ai-complexity/) for enterprise technology. As organizations move beyond initial experimentation, they confront a new set of [operational challenges](https://thenewstack.io/how-to-build-agentic-ai-that-ships/) centered on governance, security and scalability.

A familiar pattern is emerging, one that echoes the sprawl of virtual machines (VMs) and containers in previous technological waves. This new challenge is the uncontrolled proliferation of AI agents and their connections to critical business systems through Model Context Protocol (MCP) servers, creating a landscape of “shadow AI” that introduces significant risk.

Addressing this requires a new layer of infrastructure, a dedicated control plane for agentic AI. [MCP](https://thenewstack.io/is-model-context-protocol-the-new-api/) has rapidly become the standard for enabling this new generation of AI, providing a universal language for agents to interact with external tools and data sources.

Into this landscape enters [Obot.ai](https://obot.ai/), a company built by a team with a deep history in creating foundational enterprise infrastructure, aiming to provide the essential governance layer for this new ecosystem.

## The Team’s Legacy in Infrastructure Innovation

The journey of Obot.ai began as [Acorn Labs](https://thenewstack.io/acorn-a-lightweight-portable-paas-for-kubernetes/), a company initially focused on simplifying application deployment on Kubernetes. The team behind the venture, led by CEO [Sheng Liang](https://www.linkedin.com/in/shengliang/), carries a significant legacy in the cloud native world, having founded Cloud.com, which was acquired by Citrix, and Rancher Labs, which SUSE acquired.

Following their exit from Cloud.com, Liang reunited with co-founders [Shannon Williams](https://www.linkedin.com/in/smw355/), [Darren Shepherd](https://www.linkedin.com/in/ibuildthecloud/) and [Will Chan](https://www.linkedin.com/in/willchan00/) to create [Rancher Labs](https://thenewstack.io/rancher-labs-rio-an-application-deployment-engine-for-kubernetes/) in 2014. The company became synonymous with Kubernetes management, with Shepherd creating [k3s](https://k3s.io/), the most popular [lightweight Kubernetes distribution](https://thenewstack.io/ranchers-k3s-joins-cncf-sandbox-as-first-kubernetes-distribution/) that transformed edge computing deployments. Rancher achieved over 100 million downloads and 37,000 active teams before SUSE acquired the company for $800 million in December 2020.

This background is not merely a historical footnote but a central element of their current strategy. Their decision to pivot from a Kubernetes-centric product to an AI-focused platform validates that agentic AI is not just another workload to be containerized. Instead, it is a fundamentally new computing paradigm that demands its own purpose-built infrastructure and management plane. The team observed that applications built on large language models (LLMs) are designed with natural language prompts and that AI developers prefer to work with source code rather than binary containers, making their previous runtime an imperfect fit.

This [strategic realignment](https://obot.ai/acorn-labs-is-now-obot-ai/) and rebranding to Obot.ai was validated by a substantial [$35 million seed funding](https://obot.ai/obot-ai-secures-35m-seed-to-build-enterprise-mcp-gateway/) round. The investment was co-led by Mayfield Fund and Nexus Venture Partners, two venture capital firms with established track records in backing foundational enterprise technologies. A significant seed investment in an open source gateway for a protocol, rather than in a new foundational model, signals the maturation of the AI market.

The focus of sophisticated investment is expanding from the models themselves to the critical “plumbing” and infrastructure that make these models securely and efficiently usable within complex corporate environments. The funds are explicitly intended to accelerate the development of the company’s two core open source projects, the Obot MCP Gateway and the Nanobot MCP Agent Framework.

## The Obot MCP Gateway: A Control Plane for AI Agents

The Obot platform is an integrated system composed of three primary components. These are the MCP Gateway, a user-facing chat interface and a comprehensive Admin Dashboard for management. At its core, Obot is an enterprise-grade control plane designed to manage the life cycle and security of MCP servers.

The architectural pattern of the Obot MCP Gateway closely mirrors that of the API gateways that became indispensable during the rise of microservices. Just as those gateways provided a centralized point of control for a sprawling landscape of backend APIs, Obot provides an analogous control plane for the emerging ecosystem of MCP servers, which are the connective tissue between AI and enterprise systems.

[![](https://cdn.thenewstack.io/media/2025/09/f298af1b-obot-arch-1024x339.png)](https://cdn.thenewstack.io/media/2025/09/f298af1b-obot-arch-1024x339.png)

The gateway’s functionality is delivered through several key capabilities. It provides a centralized Registry that functions as a curated, internal catalog of approved MCP servers. This directly addresses the problem of tool sprawl by giving IT organizations a single source of truth for discoverable and documented AI tools. The platform also functions as a Secure Proxy, routing all communication between AI agents and MCP servers through a central chokepoint. This enables the enforcement of security policies, full audit logging and routing control, which is critical for preventing unauthorized data access and ensuring compliance.

Security is further enhanced through robust role-based access control (RBAC). Obot integrates with existing enterprise identity platforms using standards like OAuth 2.1, allowing administrators to define granular permissions that dictate which users or groups can access specific MCP servers. This enforces the principle of least privilege for both human users and the AI agents acting on their behalf.

Finally, the platform delivers comprehensive observability. By inspecting all proxied traffic, the gateway generates detailed audit trails and performance metrics, providing complete visibility into tool usage, which is essential for debugging, monitoring and meeting regulatory requirements.

[![](https://cdn.thenewstack.io/media/2025/09/6637eed9-obot-mcp-1024x556.jpg)](https://cdn.thenewstack.io/media/2025/09/6637eed9-obot-mcp-1024x556.jpg)

For its target audience of Kubernetes users, Obot is designed for seamless integration. The platform is delivered as a [containerized application](https://github.com/obot-platform/obot/pkgs/container/obot) and can be deployed onto any Kubernetes cluster using an official [Helm chart](https://github.com/obot-platform/obot/tree/main/chart). This approach aligns with established cloud native workflows, simplifying the installation, configuration and life cycle management of the entire platform. The architecture relies on proven, scalable technologies, utilizing PostgreSQL for storing structured metadata, such as user permissions and server configurations, and Amazon S3 for workspace storage. This self-hosted, open source model is a deliberate strategy to earn enterprise trust, allowing organizations to maintain complete control over their data and security posture by deploying the control plane within their own infrastructure.

## Nanobot: The Open Source Agent Development Framework

[![](https://cdn.thenewstack.io/media/2025/09/eaa13e6f-nanobot-300x225.png)](https://cdn.thenewstack.io/media/2025/09/eaa13e6f-nanobot-300x225.png)While Obot offers the management and governance framework, the company’s second major project, [Nanobot](https://www.nanobot.ai/), concentrates on developing AI agents.

Nanobot is a compact, open source MCP host that supplies the runtime environment, state management and identity features required to package an MCP server with a reasoning model into a fully functional, stateful agent.

This approach promotes a composable architecture where the agent’s “brain” (the LLM) is decoupled from its “body” (the tools exposed via MCP servers). Developers can construct new agents by simply defining a configuration that combines existing, preapproved MCP servers with a new system prompt, dramatically accelerating development and encouraging the reuse of secure components.

[![](https://cdn.thenewstack.io/media/2025/09/935cbb66-nanobot-1024x530.png)](https://cdn.thenewstack.io/media/2025/09/935cbb66-nanobot-1024x530.png)

Nanobot operates on a declarative model. Developers define what an agent should do through a YAML configuration file, specifying its tools and instructions, rather than writing complex imperative code to handle the conversational logic. A key feature of Nanobot is its support for [MCP-UI](https://mcpui.dev/), an extension to the MCP standard that allows agents to render rich, interactive user interfaces directly within a chat conversation.

This capability extends agentic AI beyond text-only interactions, enabling more intuitive and powerful user experiences with graphical components, such as forms, buttons or visual data representations. This focus on a richer user experience represents a strategic anticipation of AI’s evolution from a tool for technical users to a mainstream interface for a much broader audience.

## A Strategic Footing for the Enterprise AI Landscape

Obot.ai has strategically positioned itself to address a critical, emerging need in the enterprise AI landscape. By leveraging the team’s extensive experience in building foundational infrastructure for cloud computing, the company is applying proven principles of governance, security and open source collaboration to the new frontier of agentic AI.

The Obot MCP Gateway provides the essential control plane for IT organizations to manage the adoption of AI tools with confidence, while the Nanobot framework empowers developers to build the next generation of powerful, interactive agents. Together, these two projects form a symbiotic ecosystem.

Obot creates the secure and governed “app store” of enterprise tools, and Nanobot provides the “SDK and runtime” to build the agents that consume them. As MCP solidifies its role as the standard for AI interoperability, platforms like Obot.ai that provide the necessary layers of security and management are poised to become a foundational component of the enterprise AI stack.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)