The [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) has transformed how AI systems connect to external services. Yet, until recently, those interactions remained rigid and brittle. Tools would either succeed when all parameters were supplied before execution, or they would fail with vague errors. That one-shot model led to frustrating user experiences and limited the sophistication of AI workflows.

**Elicitation** enables an MCP server to pause and request structured input from the user at runtime, thereby transforming static tool invocation into an interactive conversation.

Elicitation was officially incorporated into the [MCP specification revision](https://modelcontextprotocol.io/specification/2025-06-18) dated June 18, 2025, and is currently in draft status. [FastMCP](https://gofastmcp.com/getting-started/welcome), an early MCP framework, incorporated elicitation handlers in its version 2.10.0, providing Python dataclass abstractions over JSON schemas and simplifying the developer experience. But currently, no major LLM provider SDK or hosted model endpoint natively supports elicitation — so developers must rely on custom client implementations or specialized frameworks to access this feature.

> Elicitation marks a shift toward collaborative AI workflows, where the system and human co-discover missing context.

Elicitation represents more than an incremental protocol update. It marks a shift toward collaborative AI workflows, where the system and human co-discover missing context rather than expecting all details upfront.

Python developers building MCP tools can now focus on core logic and delegate parameter gathering to the protocol itself, allowing for a more streamlined approach. Clients declare an elicitation capability during initialization, so servers know they may elicit input at any time. That standardized interchange liberates developers from generating custom UIs or creating ad hoc prompts, ensuring coherent behaviour across diverse MCP clients.

## The Elicitation Flow in Practice

Understanding elicitation requires visualizing how it transforms the traditional request-response cycle. The following sequence diagram illustrates a typical elicitation workflow, where a user requests flight status information:

[![](https://cdn.thenewstack.io/media/2025/07/872540e6-elicit-0-1024x845.png)](https://cdn.thenewstack.io/media/2025/07/872540e6-elicit-0-1024x845.png)

This diagram shows how elicitation creates a collaborative loop. Instead of the server failing when it lacks the required information, it pauses execution to gather necessary data from the user through the client interface, then continues processing. Note that the diagram doesn’t include an LLM. When involving an LLM, it receives the complete context and can provide intelligent analysis based on the dynamically collected information. We will explore this idea more in upcoming tutorials.

## Breaking Free from Traditional Request-Response Patterns

Traditional MCP tool patterns follow a predictable, limiting structure. When you invoke a tool, you must provide all required parameters immediately. If any parameter is missing or malformed, the tool fails to execute. This approach mirrors classic function calls in programming, but it translates poorly to human-AI interaction, where context often emerges through conversation rather than being known upfront.

Consider a restaurant booking tool. In the traditional pattern, if a user requests a table for December 25th without realizing the restaurant is closed that day, the tool simply returns an error. The user must then make another complete request with a different date. This creates friction, requires multiple round trips, and provides a poor experience that feels more like debugging code than having a helpful interaction.

> The tool becomes a collaborative partner rather than a rigid function that either succeeds or fails.

Elicitation changes this fundamental dynamic. Instead of failing when the requested date is unavailable, the tool can ask the user if they would like to try another date, suggest alternatives, and complete the booking in a single, natural workflow. The tool becomes a collaborative partner rather than a rigid function that either succeeds or fails.

This shift from one-shot execution to multi-turn conversation enables tools to handle ambiguity gracefully. Rather than requiring perfect input, tools can clarify requirements, gather missing information progressively, and adapt their behavior based on user responses. The protocol provides a standardized way for servers to request additional information through structured schemas, ensuring consistency across different clients while maintaining flexibility in implementation.

## Human-in-the-Loop as a First-Class Capability

Elicitation transforms human-in-the-loop (HITL) workflows from an afterthought to a core capability. Traditional AI systems often struggle with scenarios that require human judgment, approval, or additional context. Developers had to build custom solutions for each case, leading to inconsistent experiences and significant development overhead.

With elicitation, HITL patterns become natural extensions of tool functionality. A database migration tool can request confirmation before making irreversible changes. A document generation system can gather style preferences and content requirements through guided interactions. An incident response tool can collect severity assessments and stakeholder information as part of its workflow.

> Rather than trying to automate everything, elicitation acknowledges that many tasks benefit from human-in-the-loop.

The security model built into elicitation ensures that user agency remains paramount. Users always have clear options to accept, decline, or cancel requests. The protocol explicitly prohibits requesting sensitive information, such as passwords or API keys, thereby establishing trust boundaries that protect users while enabling useful interactions. Clients must clearly indicate which server is requesting information, thereby maintaining transparency about data flow.

This approach to HITL workflows respects human expertise while leveraging AI capabilities. Rather than trying to automate everything, elicitation acknowledges that many tasks benefit from human judgment, context and decision-making. It provides the infrastructure for AI and humans to collaborate effectively, each contributing their strengths to achieve better outcomes.

## Design Considerations for Effective Implementation

Successfully implementing elicitation requires thoughtful design. The schema-first approach encourages developers to think carefully about information architecture. What data is truly necessary? How can complex requirements be broken into simple, answerable questions? Clear schemas with descriptive titles and helpful descriptions guide users effectively.

The three-action response model (accept, decline, cancel) requires different handling strategies. Accepting continues the workflow with the provided data. Declining may trigger alternative paths or simplified workflows. Canceling could allow for later re-prompting or graceful degradation to basic functionality. Tools should handle all three cases intelligently, rather than treating decline or cancel as failures.

> Progressive disclosure patterns work particularly well in conjunction with elicitation.

Progressive disclosure patterns work particularly well in conjunction with elicitation. Begin with high-level questions to establish context, then drill down into specifics based on the responses. This approach reduces cognitive load and helps users provide accurate information by establishing context before requesting details.

State management becomes crucial for complex workflows. Tools must maintain context across multiple elicitation rounds, remembering previous responses and using them to inform subsequent requests. This creates coherent conversations rather than disconnected questions.

## Conclusion

Elicitation transforms MCP from a protocol for tool integration into a foundation for human-AI collaboration. By enabling dynamic, contextual interactions, it opens possibilities we are only beginning to explore. The future of AI lies not in replacing human judgment, but in augmenting it through thoughtful, interactive systems that respect user agency while providing powerful capabilities.

For developers ready to embrace this paradigm, elicitation offers the tools to build that future today. In the next part of this series, I will walk you through a practical use case of using elicitation with FastMCP. Stay tuned!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)