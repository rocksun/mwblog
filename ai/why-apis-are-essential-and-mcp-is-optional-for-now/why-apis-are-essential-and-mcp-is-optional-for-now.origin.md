# Why APIs Are Essential and MCP Is Optional (for Now)
![Featued image for: Why APIs Are Essential and MCP Is Optional (for Now)](https://cdn.thenewstack.io/media/2025/05/0f4eef27-douglas-lopes-ehyv_xoz4ia-unsplash-1-1024x683.jpg)
[Douglas Lopes](https://unsplash.com/@douglasamarelo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-laptop-computer-sitting-on-top-of-a-wooden-desk-ehyV_XOZ4iA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
AI assistants are becoming increasingly central to product experiences, and a new standard has emerged to help build them: the Model Context Protocol (MCP). With adoption from major large language model (LLM) providers like Anthropic, OpenAI, and Gemini, the protocol has quickly gained traction among the broader software ecosystem, with companies left and right building their own MCP servers.

As someone involved in [building both MCP servers](https://thenewstack.io/tutorial-build-a-simple-mcp-server-with-claude-desktop/) and API integrations, I’ve seen this rapid adoption lead to confusion. Some developers and product managers view MCP as an API replacement, while others see MCP as inferior to APIs.

The reality is more nuanced: MCP and APIs are complementary. Many well-designed AI systems will need both, and some AI engineers may not build a system with enough complexity to warrant using MCP.

To help you understand which solution is right for your specific scenario, I’ll explain how each one works, its limitations, and how they work together.

**How MCP and APIs Fit Together**
At its core, MCP provides a standardized way for large language models to interact with external data sources, but those interactions typically happen through existing APIs. When an LLM invokes a tool from an MCP server to, for example, create a ticket in Jira, an API call is still made to the relevant Jira endpoint.

MCP’s value comes from its [management of context between LLMs and data](https://thenewstack.io/aws-brings-trusted-extension-support-to-managed-postgres/) sources. It provides a standardized framework for:

**Tool selection and invocation:**MCP allows LLMs to dynamically choose which tools to use based on user prompts rather than requiring hardcoded API calls.**Context retention:**The protocol helps LLMs retain, update, and get context, which is crucial for managing multistep workflows.**Simplified interactions:**MCP makes it easier for LLMs and applications to integrate by providing a standard protocol.
Meanwhile, [APIs still handle the core data](https://thenewstack.io/the-fundamentals-of-data-api-design/) transmission, authentication flows, and connections to different applications.

**MCP’s Security Challenges Require API-Level Solutions**
MCP’s flexible and [open architecture introduces unique security](https://thenewstack.io/the-3-ss-of-software-supply-chain-security-sboms-signing-slimming/) challenges. Developers want to use as many tools (API endpoints) as possible. This leads to keys that often have blanket access to sensitive services like email, confidential planning tools, and sales data. As another example, an LLM might mistake field labels (confusing “SN” for social security number rather than surname) and inadvertently expose sensitive data.

To prevent situations like these, engineers need to integrate access control levels, schema enforcement, and data loss prevention. The most effective approach for doing this involves combining MCP’s context [management capabilities with robust API infrastructure](https://thenewstack.io/ansible-vs-salt-which-is-best-for-configuration-management/).

For example, an API provider’s authentication method (e.g., OAuth 2.0) enables the LLM to confirm whether the user has the necessary permissions to access the underlying API endpoint. And the API provider’s response codes can help your LLM diagnose and tackle issues (such as alerting the user when a request fails and offering up a solution to address it).

**Most AI Use Cases Only Call for APIs**
I’m seeing AI teams adopting MCPs to paper over deeper issues, like disorganized retrieval systems, out of control prompt chains, and a lack of clear conventions across teams. Instead of fixing the architecture, they add another layer, resulting in more abstraction and less clarity.

These AI teams don’t need MCP yet; they just [need to clean up their prompts and data](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/) pipelines (by building robust API integrations). If a team is just using MCP to organize the infrastructure layer, it’s probably premature.

MCP is powerful when you’ve earned the complexity: juggling multiple models, sources, and downstream consumers, and need structured contracts. But until then, consider building consistency across your infrastructure first and then implementing automated policies for archiving, deduplication, and permissions management to reduce manual overhead and maintain order.

**Understanding When and How to Leverage Each Will Give You a Competitive Advantage**
As we build increasingly sophisticated AI assistants, it’s crucial to understand that MCP and APIs are complementary layers in an integration ecosystem. MCP provides the context management layer that helps LLMs interact more effectively with external systems, while [APIs offer secure](https://thenewstack.io/the-state-of-api-management-in-an-age-of-ai-insecurity/), reliable connections to those systems.

The companies that successfully build truly useful AI assistants will recognize this relationship and invest in robust API infrastructure, organized retrieval systems, and standardized conventions before they can build effective MCP implementations — if it’s even necessary.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)