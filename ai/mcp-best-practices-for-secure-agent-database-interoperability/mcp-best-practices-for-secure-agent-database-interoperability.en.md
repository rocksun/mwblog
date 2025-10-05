The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), introduced by Anthropic in November 2024, has quickly become a foundational standard for modern AI systems. It is designed to standardize the way [large language model (LLM)](https://thenewstack.io/introduction-to-llms/)-based applications connect with diverse data sources and systems, particularly for [agentic use cases](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/). By enabling interoperability and modularity in complex AI ecosystems, MCP makes deployment easier, more flexible and more scalable.

However, the openness and flexibility that make [MCP so powerful](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) can come with great security risks. In fact, security was not a core consideration in MCP’s initial design, and given how nascent the [specification](https://modelcontextprotocol.io/specification/latest) still is, this has created a broad attack surface. This is especially significant for anyone who wants to incorporate MCP into applications holding sensitive, mission-critical data. As a result, security remains a major barrier to broader enterprise adoption of MCP. Let’s explore the key security challenges MCP presents and how to mitigate them with practical advice in the context of agent-database MCP interoperability.

## MCP Introduces New Attack Surfaces

The threat landscape for the Model Context Protocol reflects many traditional cybersecurity issues but introduces amplified risks due to the nature of agentic AI systems. Below are the three most common MCP-related security threats:

### **Prompt Injections**

This is the most common and broad attack vector for MCP-based interactions. It involves tricking the agent into unintended or malicious actions.

For example, direct prompt injections for taking advantage of an MCP server can be:  
[![](https://cdn.thenewstack.io/media/2025/10/b7cc5af9-screenshot-2025-10-01-at-10.50.42%E2%80%AFam-1024x245.png)](https://cdn.thenewstack.io/media/2025/10/b7cc5af9-screenshot-2025-10-01-at-10.50.42%E2%80%AFam-1024x245.png)Prompt injections come in many shapes and forms, including cases where tool descriptions are compromised (tool poisoning) or where retrieved data itself carries malicious instructions (retrieval-agent deception, or RADE). These threats are primarily caused by malicious or compromised MCP servers.

## **Malicious or Compromised MCP Servers**

MCP’s open protocol design allows any server to connect, but not all can be trusted. A rogue server can impersonate or tamper with genuine tools, enabling data theft or manipulation of outputs. If multiple MCP servers are connected to the same agent, even a single malicious server can interfere with others, making detection significantly harder.

Once a malicious or compromised server is connected, attackers can use prompt injection–style techniques such as tool poisoning and RADE, altering the way tools are perceived or retrieved to achieve the same effect as direct prompt injections.

Servers may be compromised in several ways. Supply chain vulnerabilities are common: backdoored packages, tampered libraries or malicious updates introduced via CI/CD pipelines. Additionally, rogue servers can appear in unvetted registries, posing as legitimate MCP servers to lure agents into unsafe actions.

### **Sensitive Data Exfiltration** (Credential Leaks)

MCP systems often require credentials to access external services. If these are improperly stored or exposed, attackers can exploit them. Additionally, data returned from connected services may be accidentally exposed to users or logged without safeguards, leading to potential data leakage.

While these are the most common threats, other risks also affect agentic systems:

* **System prompt leakage**: If attackers gain access to the system prompt, they may uncover vulnerabilities and use them to launch prompt injections.
* **Spiraling consumption**: Similar to denial-of-service (DoS) attacks, forcing an agent to make excessive LLM calls or process large amounts of data can drive up GPU or API costs and degrade performance.

## Secure Agent-Database MCP Best Practices

### **Authentication and Scoped Authorization (Principle of Least Privilege)**

Proper role-based access controls and strong authentication are essential for MCP servers that expose data or services. These measures ensure users and agents only access the tools they are authorized for and help prevent misuse by malicious servers.

The principle of least privilege applies: An agent should have only the permissions needed to perform its tasks, nothing more. Permissions may vary based on the user, which is why authenticating both the user and the agent is critical for tracing errors and detecting malicious activity.

There are two levels at which access should be controlled:

* **Upstream**: Apply strict role-based access to ensure agents only use the minimum necessary data or services. This includes enforcing read vs. write privileges and scoping access to specific databases or endpoints. For example, configuring the database with roles to limit agent capabilities follows the principle of least privilege and prevents unnecessary data exposure. This can be achieved through implementing custom database roles, resource policies for organization-wide controls and collection-level permissions.
* **Downstream**: Add further constraints after access is granted. These include enforcing read-only modes, disabling write operations, or sandboxing agent interactions with data. By enforcing a full read-only mode, even if upstream controls are bypassed, data remains protected.

**MCP Servers and Tool Vetting**

MCP servers can be installed and integrated into agentic tools in just a few clicks, effectively serving as a universal plugin system for AI. This ease of setup contributes to the rise of shadow AI, where not only AI apps are adopted, but additional MCP servers can be connected independently.

This makes compromised MCP servers a serious threat. Today, thousands of MCP servers are available on registries like [Glama](https://glama.ai/mcp/servers) or [Smithery](https://smithery.ai/), often with multiple versions for the same service. To minimize risk, always favor official servers from trusted sources. Agentic IDEs like Cursor and Windsurf also offer official, vetted lists you can use safely.

If you choose to use a third-party MCP server, such as one from GitHub, carefully vet the tool descriptions before connecting it. Look for signs of tool poisoning or potential data exfiltration risks.

In production environments, treat MCP servers like any other critical software. Require signed manifests and verify them with public keys when possible. If you’re developing custom MCP servers, follow DevSecOps best practices, including vulnerability scanning and malware detection.

### **Logging and Observability**

If there’s one priority to implement, it’s comprehensive monitoring. MCP servers allow agents to perform potentially sensitive actions against your databases. You need clear visibility into what goes in and out, ideally in real time.

Without visibility into prompt activity and tool usage, detecting misuse or malicious behavior becomes nearly impossible. The absence of audit trails leaves systems blind to abuse, data leaks or unauthorized actions. Real-time monitoring of data flow can detect sensitive information and prevent its leakage or misuse.

Centralized monitoring, anomaly detection and compliant log retention provide complete visibility, accountability and control over MCP server activity.

### **Compliance and Policy Enforcement**

Compliance is non-negotiable when using MCP in enterprise environments, particularly for organizations in highly regulated industries. Because MCP can enable AI systems to access sensitive data stores, every interaction must adhere to data protection laws and internal governance policies.

Key compliance requirements include:

* Maintaining audit logs that meet regulatory standards.
* Enforcing data residency rules to prevent cross-region access or exposure.
* Safeguarding privacy by blocking the disclosure of personally identifiable information (PII) in responses.

The general best practice is to integrate MCP into existing governance models and rely on enterprise-ready services and databases that support strong compliance controls.

## Securing Agent-Database Interoperability

As MCP systems become central to agent-database interoperability, the need for robust security becomes critical. MCP’s open design offers significant flexibility but also introduces risks such as prompt injection and server compromise. Developers can mitigate these threats by adopting best practices, including user and agent authentication, scoped authorization and comprehensive monitoring.

The [MongoDB MCP Server](https://www.mongodb.com/company/blog/announcing-mongodb-mcp-server), which standardizes the way agents connect to MongoDB deployments, provides a secure foundation, enabling enterprises to safely leverage the transformative power of agent-database integration.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/3cfb1a95-cropped-17b02f8b-screenshot-2025-06-30-at-10.26.20%E2%80%AFam.png)

Thibaut Gourdel is a technical product marketing manager at MongoDB, where he focuses on MongoDB's integration with AI frameworks to support and accelerate developer adoption. With a background in data engineering, integration and applied AI, Thibaut brings expertise in practical...

Read more from Thibaut Gourdel](https://thenewstack.io/author/thibautgourdel/)