The ability to connect [AI agents](https://thenewstack.io/ai-agents/) to external systems defines their practical utility. Without tools, an agent is limited to generating text based on its training data. With tools, an agent becomes an autonomous actor capable of retrieving real-time information, executing code, calling APIs and interacting with enterprise systems. Google’s [Agent Development Kit (ADK)](https://thenewstack.io/what-is-googles-agent-development-kit-an-architectural-tour/) provides a comprehensive tool integration framework that determines how agents extend their capabilities beyond the language model.

For developers building [agentic applications](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/), understanding ADK’s tool architecture is essential. The patterns mirror familiar software development concepts: function interfaces, plugin systems and standardized protocols. This article explores the four categories of tools supported by ADK using analogies drawn from Python development, API design and application architecture. The goal is to provide clarity on when to use each tool type and how they interact with the agent runtime.

## What Are Tools in the Google Agent Development Kit?

Tools are executable functions that agents invoke to perform actions beyond text generation. When an agent determines that it needs external data or capabilities, it selects an appropriate tool, passes the required parameters and processes the returned result. This interaction follows the same request-response pattern you use when calling any function or API in your applications.

> Think of tools as the external libraries and services your application depends on.

Think of tools as the external libraries and services your application depends on. Just as a Python application might import a database client for persistence, a caching library for performance or an HTTP client for external API calls, an ADK agent invokes tools to extend its capabilities. The agent acts as the orchestrating logic, while tools serve as the specialized modules that handle specific functions.

ADK organizes tools into four distinct categories based on their origin and integration pattern: function tools, built-in tools, third-party tools and [MCP tools](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/). Each category serves different use cases and requires different integration approaches.

## 1. Function Tools: Building Custom Capabilities

Function tools are developer-defined functions that extend agent capabilities with custom logic. These are Python functions decorated with ADK’s tool interface, allowing the agent to discover and invoke them during execution. Function tools represent the most flexible integration pattern — you control the implementation, the inputs, the outputs and the behavior.

The analogy here is straightforward: Function tools are like utility functions or helper modules you write for any Python application. Just as you might create a dedicated module to handle invoice processing, geolocation lookups or proprietary business logic, function tools encapsulate specific capabilities that your agent needs but that don’t exist elsewhere.

Consider a financial analysis agent that needs to calculate custom risk metrics using proprietary formulas. No external service provides this capability. You implement the calculation logic as a function tool, expose it to the agent with clear parameter definitions and descriptions, and the agent invokes it whenever risk analysis is required. The agent understands what the tool does through its docstring and type hints — similar to the way developers understand function capabilities through documentation and IDE autocomplete.

Function tools run in the same process as the agent, making them fast and secure for sensitive operations. There’s no network overhead, no external authentication and no third-party dependencies. This makes function tools ideal for:

* **Proprietary business logic**: Operations that cannot be exposed externally or depend on internal algorithms unique to your organization.
* **Data transformations**: Calculations and processing specific to your domain that require custom implementation.
* **Internal system integration**: Direct library calls to internal systems without network exposure.
* **Secure operations**: Tasks requiring access to local resources or credentials that should not traverse a network.

Function tools are your custom modules — purpose-built, tightly controlled and imported directly into your agent’s runtime.

## 2. Built-in Tools: Leveraging Platform-Provided Capabilities

ADK includes a set of built-in tools that provide common capabilities out of the box. These tools handle frequent requirements — like web search, code execution and retrieval-augmented generation (RAG) — without requiring custom implementation. Google maintains these tools, ensuring reliability, performance and integration with underlying platform services.

In development terms, built-in tools resemble standard library modules or well-maintained packages from PyPI. Just as you might use Python’s `json` module instead of writing your own parser, or leverage `requests` instead of building HTTP handling from scratch, built-in tools offer production-ready capabilities without development overhead.

The current built-in tool set includes:

| Built-in Tool | Capability | Development Analogy |
| --- | --- | --- |
| Google Search | Real-time web search and information retrieval | A managed API client with authentication handled for you |
| Code Execution | Sandboxed Python execution for dynamic computation | A secure `exec()` environment with isolation and resource limits |
| Vertex AI Search | Enterprise search across structured and unstructured data | An indexed database with full-text search built in |

Built-in tools are designed for immediate productivity. You enable them through configuration rather than code, and they integrate seamlessly with the agent runtime. The tradeoff is flexibility — you accept the tool’s behavior as provided, without customization options.

For agents requiring standard capabilities like search or code execution, built-in tools eliminate development effort and maintenance burden. For specialized requirements, you layer custom function tools on top.

## 3. Third-Party Tools: Integrating External Ecosystems

ADK supports integration with tools from external frameworks, most notably [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/). This interoperability allows developers to use existing tool libraries without rewriting them for ADK’s interface. If your organization has already invested in LangChain tools or wants to access its extensive ecosystem, ADK provides an adapter layer that bridges the two frameworks.

This pattern mirrors the adapter and wrapper patterns common in software development. When two libraries have incompatible interfaces, you write an adapter that translates between them. ADK’s third-party tool support follows similar principles — a translation layer that enables external tools to participate in the agent runtime without native reimplementation.

The integration works through wrapper functions that adapt LangChain’s tool interface to ADK’s expectations. The agent interacts with these tools identically to native function tools; the adaptation happens behind the scenes. This approach offers several advantages:

* **Extensive tool library access**: Gain immediate access to LangChain’s extensive collection of pre-built tools covering databases, APIs and external services.
* **Investment preservation**: Protect existing investments in LangChain-based development without requiring rewrites.
* **Gradual migration path**: Move from LangChain to ADK incrementally, converting tools as needed rather than all at once.
* **Community-maintained tools**: Benefit from tools that evolve independently of ADK through community contributions.

Third-party tool integration is most valuable when migrating existing agents to ADK or when specific capabilities exist in external libraries but not in ADK’s built-in set. The trade-off involves additional abstraction layers and potential version compatibility considerations between frameworks.

## 4. MCP Tools: Standardized Integration for Interoperability

Model Context Protocol (MCP) tools represent ADK’s support for the emerging standard in AI tool interoperability. MCP defines a protocol for how AI agents discover, authenticate with and invoke tools across different platforms. ADK agents can connect to any MCP-compliant server and use its tools without custom integration code.

MCP tools bring the same standardization to AI agents that REST brought to web APIs — a universal interface enabling ecosystem-wide interoperability.

For developers, MCP’s significance becomes clear through comparison with API standardization. Before REST conventions became widespread, every web service required custom integration logic. After REST, developers could predict how to interact with any compliant API. MCP aims to achieve the same outcome for AI tools: Any compliant agent framework can invoke any compliant tool server using the same patterns.

The architecture involves three components:

* **MCP server**: Hosts one or more tools and exposes them through the standard protocol. Servers can be local processes, remote services or cloud-hosted endpoints.
* **MCP client**: Built into ADK, the client handles discovery and invocation of remote tools. It manages connection life cycle, authentication and response processing.
* **Transport layer**: Typically Server-Sent Events (SSE) over HTTP for real-time communication between client and server.

When an ADK agent connects to an MCP server, it discovers available tools through the protocol’s introspection mechanism. Each tool’s name, description and parameter schema become available to the agent. During execution, the agent invokes tools through the MCP client, which handles serialization, transport and response processing.

This pattern resembles plugin architectures, where a host application discovers and loads extensions at runtime. The agent doesn’t need to know the implementation details of the MCP server — only that it speaks the standard protocol. This enables:

* **Dynamic tool discovery**: Tools can be added, removed or updated on MCP servers without changing agent code.
* **Location flexibility**: Connect to tools hosted anywhere, including local processes, remote servers or cloud services.
* **Vendor neutrality**: Develop and consume tools without framework lock-in.
* **Ecosystem growth**: Shared standards encourage tool sharing and reuse across organizations.

MCP tools are particularly valuable for enterprise environments where tools may be maintained by different teams or external vendors. The protocol standardization ensures consistent behavior regardless of who implements the server.

## How to Select the Right ADK Tool for Your Needs

Choosing the right tool category depends on your specific requirements. The following decision framework maps common scenarios to appropriate tool types:

| Requirement | Recommended Tool Type | Rationale |
| --- | --- | --- |
| Proprietary business logic | Function tool | Full control, no external dependencies |
| Web search or code execution | Built-in tool | Production-ready, zero implementation effort |
| Existing LangChain investment | Third-party tool | Preserve existing work, gradual migration |
| Cross-platform interoperability | MCP tool | Standardized, vendor-neutral integration |
| Dynamic tool discovery | MCP tool | Runtime flexibility, decoupled deployment |
| High-security operations | Function tool | Process-local execution, no network exposure |

In practice, production agents often combine multiple tool types. An enterprise agent might use built-in tools for search, function tools for proprietary calculations and MCP tools for integration with external enterprise systems. ADK’s runtime handles this heterogeneity transparently — the agent selects tools based on capability, not implementation type.

## Understanding the Tool Invocation Flow in ADK

Understanding how agents select and invoke tools clarifies the runtime behavior. The flow follows a consistent pattern regardless of tool category:

1. **Prompt processing**: The agent receives a user request and determines that external capabilities are needed to fulfill it.
2. **Tool selection**: Based on tool descriptions and the current task, the agent selects the appropriate tool from available options.
3. **Parameter construction**: The agent extracts or generates the required parameters from conversation context and user input.
4. **Invocation**: ADK’s runtime executes the tool — locally for function tools, remotely for MCP tools or through adapters for third-party tools.
5. **Result processing**: The tool’s output returns to the agent for incorporation into its response or further processing.
6. **Iteration**: If needed, the agent may invoke additional tools based on intermediate results, chaining capabilities together.

This loop may execute multiple times within a single user interaction. An agent answering a complex question might first search the web for current information, then execute code to analyze the results, then query an internal database for context — each step invoking a different tool.

The agent’s ability to chain tools effectively depends on clear tool descriptions. When you define a function tool, the docstring and parameter annotations directly influence when and how the agent uses it. Ambiguous descriptions lead to incorrect tool selection; precise descriptions enable reliable automation.

## What’s Next

Tools transform AI agents from text generators into autonomous actors capable of interacting with the world. ADK’s tool architecture provides the flexibility to integrate capabilities from multiple sources — custom code, platform services, external frameworks and standardized protocols.

For developers building agentic applications, the patterns are familiar. Function tools behave like custom modules you import. Built-in tools resemble well-maintained libraries with batteries included. Third-party integrations mirror adapter patterns for cross-framework compatibility. MCP tools bring the standardization that has driven API ecosystem growth across the industry.

Understanding these categories enables informed architectural decisions when designing agent systems. The right tool type depends on control requirements, existing investments and interoperability needs. Most production systems will combine multiple types, leveraging each category’s strengths.

In upcoming articles, I will explore ADK’s tool calling mechanism based on supported categories. Stay tuned!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)