“The API landscape is a mess, and very few people understand it,” Kin Lane, API industry veteran and founder of [Naftiko](https://naftiko.io), tells *The New Stack*.

Some days it feels like we are [living in an XKCD cartoon](https://xkcd.com/927/).

![A three-panel comic titled "HOW STANDARDS PROLIFERATE: (SEE: A/C CHARGERS, CHARACTER ENCODINGS, INSTANT MESSAGING, ETC.)"](https://cdn.thenewstack.io/media/2026/02/0331e67d-standards.png)

*xkcd.com*

Organizations don’t typically migrate legacy systems from one spec to another as new ideas emerge. Instead, they accumulate layers of integration standards over time, with each era leaving behind systems that are too costly or risky to excavate. “I get a call from a 20-year veteran at a large enterprise, who says, ‘We still have [EDI](https://www.edibasics.com/edi-vs-api/) and [WSDLs](https://en.wikipedia.org/wiki/Web_Services_Description_Language), a lot of [Swagger](https://swagger.io) and [OpenAPI](https://www.openapis.org). We’re trying to do more [Async API](https://www.asyncapi.com/en). [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) is popping up, and we’re looking at [Agent Skills](https://agentskills.io/home), but we have a global business to run, and it’s got to be stable.’”

It was seeing this recurring pattern of API sediment that prompted Lane to found Naftiko.  
The evolution and splintering of API specifications

> “Organizations… accumulate layers of integration standards over time, with each era leaving behind systems that are too costly or risky to excavate.”

Lane argues that competing standards are a consequence of vendor ‘land grabs’, where competing vendors exploit specs to exert influence. I don’t disagree with his hypothesis, but I would add that the different standards also reflect when they were developed.

Web Services Description Language (WSDL) emerged from the Enterprise SOA movement of the 2000s as a formal contract language for web services. Governed by W3C but heavily influenced by IBM, Microsoft, and Oracle, it was technically open but reflected corporate middleware needs, with verbose XML schemas defining operations, messages, and bindings.

In the 2010s, REST APIs displaced SOAP, and lighter-weight specifications emerged:

* **Swagger**, originally created by [Tony Tam](https://www.linkedin.com/in/tonytam/) as a dictionary API for his startup Wordnik, became the dominant standard for HTTP/REST APIs. Compared to SOAP and WSDL, it struck a better balance — machine-readable enough for tooling and human-readable enough for documentation. It focused on synchronous request-response patterns. After Tam’s start-up was acquired by [SmartBear](https://smartbear.com/), Swagger was moved to the Linux Foundation and renamed OpenAPI.
* **API Blueprint**, created by Apiary, championed Markdown-based readability. It was elegant, human-friendly, and gained early traction, but after [Oracle acquired Apiary](https://www.oracle.com/corporate/pressrelease/oracle-buys-apiary-011917.html#:~:text=Creates%20the%20Most%20Comprehensive%20API,lifecycle%20and%20deliver%20integrated%20applications.%E2%80%9D) in 2017, development switched to maintenance mode as Oracle integrated it into its API Platform Cloud Service. Without foundation governance, there was no incentive for competitors to invest in tooling, and the community atrophied.
* **RAML (RESTful API Modeling Language)**, backed by MuleSoft, emphasizes modularity and reuse, which are crucial for large enterprises with hundreds of APIs. “I think RAML is a better spec than Swagger,” Lane told me, “but the MuleSoft people behaved so badly to others in the community that no one wanted to use it.” [Salesforce acquired MuleSoft](https://investor.salesforce.com/news/news-details/2018/Salesforce-Signs-Definitive-Agreement-to-Acquire-MuleSoft/default.aspx) for $6.5 billion in 2018, and RAML became a feature of the MuleSoft Anypoint Platform rather than shared infrastructure.

As asynchronous architecture patterns such as event-driven architectures, message queues, WebSockets, and streaming gained popularity in the late 2010s, OpenAPI’s request-response model no longer fit. Regarded as a sister spec to OpenAPI, [AsyncAPI](https://www.asyncapi.com/en) (also under Linux Foundation) borrowed OpenAPI’s structure, adapting it for pub/sub, streaming, and asynchronous messaging patterns.

As we entered the 2010s, [Smithy](https://smithy.io) (AWS) and TypeSpec (Microsoft) marked a shift toward protocol-agnostic API modeling. Rather than describing HTTP endpoints directly, they model services abstractly, then generate OpenAPI, code, or protocol-specific implementations. This reflects cloud providers’ need to maintain type safety while supporting multiple protocols (HTTP, gRPC, proprietary) from single definitions.

Smithy powers AWS’s service definitions. TypeSpec emerged from Microsoft’s experience with Azure APIs and emphasizes TypeScript-based syntax for broader developer accessibility. Both Smithy and TypeSpec are open source, but neither has truly open governance in the OpenAPI/AsyncAPI sense. AWS drives Smithy’s roadmap based on internal AWS needs. TypeSpec recently moved to a Linux Foundation working group, but Microsoft remains the dominant contributor. There’s no open governance — no multi-vendor steering committee, and no requirement for consensus from competing cloud providers.

This matters because Smithy and TypeSpec reflect their creators’ architectural assumptions: multi-region cloud services, polyglot microservices, auto-generated clients. They’re optimized for the problems that AWS and Azure experience, not necessarily problems faced by enterprises or startups. Without diverse governance, they risk becoming sophisticated tools that solve vendor-specific problems.

The SDK focus of Smithy and TypeSpec reveals something else: these specs assume developers consume APIs through generated code. They’re not optimized for the autonomous agents that LLM vendors hope will form the next wave of API consumers. As a result, the big LLM model providers are creating and pushing new standards:

* **MCP (Model Context Protocol, Anthropic/open community)** defines how AI models discover and invoke tools/APIs. Rather than describing what an API is, MCP outlines what an API *does for an agent* — emphasizing natural language descriptions, parameter semantics, and state management. It has seen rapid early adoption but has also been criticized for [security risks](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls) and [context window bloat](https://thenewstack.io/how-to-reduce-mcp-token-bloat/).
* **A2A (Agent-to-Agent)** was initially introduced by Google in April 2025. This open protocol is designed for multi-agent systems, allowing interoperability between AI agents from varied providers or those built using different AI agent frameworks.
* **Agent Skills (Anthropic)** packages capabilities with semantic descriptions optimized for LLM understanding — documentation written for AI comprehension rather than human reading.

While OpenAPI and AsyncAPI are strategic resources, MCP and A2A are more tactical. “Both MCP and A2A are very transactional, exciting, and in this moment,” Lane said. “They are also likely to give away all your value and data if you are not careful. You have to be very thoughtful in how you transact in those new realms.”

## The governance gap: API governance vs. AI access

The question is how you bridge the gap between the tactical needs of an individual team and the strategic needs of the overall enterprise. “I would see this at Postman all the time. Tractor company John Deere would come to us and say, ‘Our CIO, CTO’s office, and Centre of Excellence, manage SOAP, WSDLs, open API, and AsynchAPI across the org. Now we have teams with Postman Collections that run tests and automation, but they don’t understand the bigger picture. We need Postman to reconcile these two worlds for us.’”

The API economy saw developers craft APIs, treat them as products, rate-limit them, and understand who was using them and what they were doing with them. “MCP, however, wants to circumvent all of that,” Lane said. “It wants direct access to your data and files, so it’s throwing out that decade of design work in front of our file systems and databases, and instead letting the agents have it without much accounting or governance.”

In addition to wasting significant potential value, poor data governance poses a significant challenge when deploying LLMs for internal use. Organizations can inadvertently expose sensitive information across departments. That data was likely technically accessible before, but required manually searching through Google Drive or file shares to find it.

When LLMs gain access to these information repositories, they can surface and share sensitive data far more readily, effectively democratizing access in ways that may violate intended access controls. This was a point that [Nicolleta Curtis](https://www.linkedin.com/in/nicoletta-curtis-4ab48515?originalSubdomain=uk) emphasized to me in an [interview for *LeadDev*](https://leaddev.com/technical-direction/if-95-of-generative-ai-pilots-fail-whats-going-wrong). “Even with the basics, such as OneDrive and SharePoint, we found documents that were overshared or with open permissions,” she told me.

Organizations typically respond to this challenge in one of two ways: they underestimate either the severity of the data exposure risk or the operational burden that proper mitigation will place on their security teams. Implementing appropriate access controls and data boundaries after the fact requires substantial effort.

In large enterprises with legacy systems, retroactively tightening permissions often breaks existing workflows and integrations. This creates friction across the organization as teams suddenly lose access to information they’ve historically relied on, leading to productivity impacts and internal resistance to the new controls.

In [the first article in this series](https://thenewstack.io/map-your-api-landscape-to-prevent-agentic-ai-disaster/), Lane described his experience setting up API governance at Bloomberg, which involved:

* Mapping the existing landscape by crawling GitHub and Confluence for API evidence (WSDLs, XSDs, Swaggers, OpenAPI specs)
* Standardizing everything to OpenAPI 3.1 to get a complete account
* Identifying team boundaries, domains, and ownership across different business lines

Using this approach of comprehensive API mapping and governance with established standards like OpenAPI provides the best foundation for compliance, security, and Personally Identifiable Information (PII) management. For newer/smaller organizations, Lane suggested skipping the ‘baggage’ and going straight to newer approaches such as Agent Skills or MCP.

Whatever approach you favor, we both agree that you should resist the temptation to take a technology-first approach that ignores business outcomes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)