With 2025 hailed as “the year of agents” by [NVIDIA CEO Jensen Huang](https://www.barrons.com/articles/nvidia-stock-ceo-ai-agents-8c20ddfb) and [OpenAI CPO Kevin Weil](https://www.axios.com/2025/01/23/davos-2025-ai-agents), AI agents are increasingly of interest to organizations across industries. These autonomous systems will often need to interact with databases, where much of the world’s valuable data resides.

According to [IDC’s “Data Age 2025” report](https://www.seagate.com/files/www-content/our-story/trends/files/Seagate-WP-DataAge2025-March-2017.pdf), enterprises will manage nearly 60% of the world’s data by 2025, most of it organized in databases. As a result, databases will be central to agentic architectures, and the success of agent deployments will depend on how well they connect and interact with them.

Enter the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/), originally developed by Anthropic. MCP has quickly become popular as a standardized method for connecting tools and data to [agentic systems](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/), offering a new approach to agent-database interoperability. But this raises key questions for AI developers: What do agentic architectures involving databases actually look like? And what should you consider when building one?

## A Quick Overview of Agents

Agents are [large language model (LLM)](https://thenewstack.io/what-is-a-large-language-model/)-based systems that have access to tools — functionalities or resources they can use to perform tasks beyond their native capabilities. What defines them is the ability to autonomously decide when and how to use these tools, whether independently, within a structured workflow or with a human in the loop.

[![Core components of an agent: perception, planning, tools and memory.](https://cdn.thenewstack.io/media/2025/08/dc7cc142-image1-1024x371.png)](https://cdn.thenewstack.io/media/2025/08/dc7cc142-image1-1024x371.png)

Core components of an agent: perception, planning, tools and memory.

Granting agents the ability to directly query and interact with database data enables a range of powerful use cases. Examples include generating application code based on available collections and schemas, or retrieving the latest customer information to resolve support issues.

This introduces several architectural design decisions to ensure performance, scalability and security. In particular, how database querying tools are exposed plays a critical role. When providing database querying capabilities to [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/), two main paths emerge: using standardized tools with MCP or building a custom integration tailored to specific needs.

## Path 1: Standardized Integration With MCP Servers

MCP servers offer a plug-and-play approach to integrating agents with databases. The [MongoDB MCP Server](https://www.mongodb.com/company/blog/announcing-mongodb-mcp-server), for example, simplifies connecting to a MongoDB database and querying data through MCP, making it easy for various agent-based assistants like Cursor, Windsurf, Claude Desktop or any MCP-enabled agentic system to interact with your data.

MCP provides agents with a standardized interface for database interaction. These servers can be deployed locally or remotely. A remote server allows multiple clients to access the same instance, making it ideal for shared environments. Your choice between local and remote deployment depends on your performance, scalability and security needs. Remote deployments, in particular, may require additional considerations such as authentication mechanisms to ensure secure access.

[![Architecture diagram showing an agent interfacing with the MongoDB MCP Server.](https://cdn.thenewstack.io/media/2025/08/a9215165-image2-1024x462.png)](https://cdn.thenewstack.io/media/2025/08/a9215165-image2-1024x462.png)

Architecture diagram showing an agent interfacing with the MongoDB MCP Server.

The upsides of this approach are:

* **Shift in ownership**: Using an officially supported server means the provider handles ongoing support and updates, giving agents access to continuously improved capabilities without the teams building and deploying those agents doing manual code updates.
* **Plugin-like integration:** An out-of-the-box solution is the fastest way for teams to prototype or deploy production-grade agents that interact with a database, similar to a plugin system.
* **Ideal for operational database usage**: This approach is well-suited for the most common database interactions, such as basic CRUD-style querying and database management operations.

The primary tradeoff with using prebuilt MCP servers is limited customization; compared to building a custom integration, you have less control over precisely how the tools behave under the hood. Although MCP simplifies integrating predefined tools with agents, it still requires careful consideration, as MCP isn’t inherently secure (more about this later).

## Path 2: Custom Integrations for Control and Flexibility

Building a custom implementation offers a more flexible route for teams requiring more fine-grained control over their database interactions. Frameworks like LangChain simplify and accelerate this process. For instance, the [MongoDB-LangChain integration package](https://github.com/langchain-ai/langchain-mongodb) provides tools for implementing [natural language queries](https://www.mongodb.com/docs/manual/natural-language-to-mongodb/), allowing developers to build AI applications and agents that interact with MongoDB. This enables intuitive interfaces for data exploration and autonomous agents, such as customer support assistants, to retrieve data.

This toolkit is customizable and extensible. Developers building agents can precisely define which database operations are exposed to the agent, including schema inspection, query generation, validation, or more complex scenarios, and specifically design how those tools are called.

The main advantages of this approach are:

* **Full control and ownership**: You keep complete control over tool behavior and the exact database operations your agent can perform.
* **Support for advanced use cases**: This approach allows support for advanced and domain-specific use cases that standard pre-built tools might not cover.
* **Custom optimization**: Custom implementations can be tightly aligned with internal data policies and specific business logic, hence being optimized for your requirements.

However, custom development typically comes with trade-offs like higher development overhead and full ownership responsibility for the integration. This path is ideal for teams building agents tailored to unique workflows, where agents are the core product, or where compliance, privacy or performance requirements exceed what standard solutions can support.

## Accuracy, Security, and Performance Considerations

Granting agents direct database access, whether through MCP or custom tools, introduces significant accuracy, security and performance challenges. As these technologies evolve, implementing preventive measures and adhering to best practices is critical for reliable and scalable agentic operations.

### Accuracy: Ensure Reliable Query Generation

Query accuracy heavily depends on the LLM’s capabilities and the quality of the provided schema or data samples. Ambiguous or incomplete metadata inevitably results in incorrect or suboptimal queries. When implementing agentic text-to-query systems, it’s important to enforce input/output validation, implement rigorous testing and establish guardrails or human review for complex, sensitive operations.

### Security: Maintain Protection and Guardrails

Direct database access by AI agents creates unprecedented privacy and data governance challenges. MCP presents new security threats, such as prompt injection and tool poisoning, due to LLMs’ inherent behavior. While relatively new, MCP-related threats and risk mitigations have been researched and documented by multiple organizations, including [Red Hat](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls) and [Writer](https://writer.com/engineering/mcp-security-considerations/). Strict guardrails should be enforced to mitigate risks of malicious activity and sensitive data exfiltration.

As a general best practice, agents must operate under strict least-privilege principles, using roles and policies that grant permissions only for their specific tasks.

Another critical concern involves sensitive information-sharing with LLM providers when agents access data. Organizations need architectural controls over what information (e.g., database names, collection names, data samples) reaches the LLM, with the ability to disable this entirely.

To address these security concerns, a layered access control model is essential.

* **Upstream**: Fine-grained role-based access ensures agents interact only with authorized services and data, in line with the principle of least privilege.
* **Downstream**: Additional restrictions can be applied to limit functionality or [enforce read-only access](https://github.com/mongodb-js/mongodb-mcp-server?tab=readme-ov-file#configuration). These controls reduce risk and ensure proper governance over agent-database interactions.

### Performance: Manage Unpredictable Agentic Workloads

The non-deterministic nature of LLMs makes agent workload patterns inherently unpredictable. Agents can frequently interact with the database, which can severely affect performance, creating a key operational challenge. In this context, It’s critical to choose a database that preserves its primary role while allowing agents to scale efficiently.

Isolating agentic workloads from other database operations offers two key benefits: First, it ensures that only designated instances handle agent workloads, preserving production performance while enabling flexible agent scalability. Second, it allows for tailored configurations on these instances, such as setting them to read-only mode, to optimize for specific use cases.

With MongoDB, this translates to using [replica sets](https://www.mongodb.com/docs/manual/core/workload-isolation/), which support independent scaling of read and write operations. In addition, [autoscaling](https://www.mongodb.com/docs/atlas/cluster-autoscaling/), along with [dedicated, optimized search nodes](https://www.mongodb.com/company/blog/product-release-announcements/search-nodes-now-public-preview-performance-scale-dedicated-infrastructure), further enhances agent performance for search-intensive tasks. Combining workload isolation with autoscaling is critical for deploying reliable and scalable agents.

## The Agentic Future Depends on Databases

As AI agents continue to evolve into powerful, autonomous systems, their ability to interact directly with enterprise data becomes essential. With databases housing the majority of the world’s information, enabling access is no longer optional. MCP offers a standardized, fast path to agent-database integration, ideal for common use cases. For deeper customization, building bespoke integrations provides granular control and extensibility.

Regardless of the path chosen, developers must prioritize accuracy, enforce strict security controls and ensure scalability. In this new era of agents, the real competitive edge lies in choosing a modern and flexible database that fits these requirements.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/3cfb1a95-cropped-17b02f8b-screenshot-2025-06-30-at-10.26.20%E2%80%AFam.png)

Thibaut Gourdel is a technical product marketing manager at MongoDB, where he focuses on MongoDB's integration with AI frameworks to support and accelerate developer adoption. With a background in data engineering, integration and applied AI, Thibaut brings expertise in practical...

Read more from Thibaut Gourdel](https://thenewstack.io/author/thibautgourdel/)