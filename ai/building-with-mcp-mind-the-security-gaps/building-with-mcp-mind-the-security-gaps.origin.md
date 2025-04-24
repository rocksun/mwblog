# Building With MCP? Mind the Security Gaps
![Featued image for: Building With MCP? Mind the Security Gaps](https://cdn.thenewstack.io/media/2025/04/74f43954-mind-the-gap-mcp-security-2-1024x576.jpg)
Inherent security flaws are raising questions about the safety of AI systems built on the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/).

Developed by [Anthropic](https://www.anthropic.com/company), [MCP](https://modelcontextprotocol.io/introduction) is an open source specification for connecting large language model-based AI agents with external data sources — called MCP servers.

As the first proposed industry standard for [agent-to-API communication](https://thenewstack.io/its-time-to-start-preparing-apis-for-the-ai-agent-era/), interest in MCP has surged in recent months, leading to an explosion in MCP servers.

In recent weeks, developers have sounded the alarm that MCP lacks default authentication and isn’t secure out of the box — some say it’s a [security nightmare](https://equixly.com/blog/2025/03/29/mcp-server-new-security-nightmare/).

Recent [research from Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) shows that MCP servers are vulnerable to tool poisoning attacks, in which untrusted servers embed hidden instructions in tool descriptions.

Anthropic, OpenAI, Cursor, Zapier, and other MCP clients are susceptible to this type of attack, according to Invariant Labs, which demonstrated how to [exfiltrate WhatsApp chat histories](https://invariantlabs.ai/blog/whatsapp-mcp-exploited).

“MCP itself generally does not have a security issue per se, as the underlying vulnerability is actually a problem with the models,” [Luca Beurer-Kellner](https://www.linkedin.com/in/luca-beurer-kellner-0b345616a), Invariant Labs’s co-founder and CTO, told The New Stack.

“At the same time, MCP adoption is pushing more and more users to connect LLM systems to sensitive data sources and tools, which makes the security challenges of AI and agentic AI specifically all the more relevant,” he adds.

## MCP Security Concerns ‘Are Very Real’
MCP has been described as the “[USB-C port for AI](https://docs.anthropic.com/en/docs/agents-and-tools/mcp).” According to [MCP.so](https://mcp.so/servers), over 8,000 MCP servers are already in operation.

OpenAI’s [Sam Altman](https://thenewstack.io/what-openai-ceo-sam-altman-really-expects-in-ais-future/) recently [committed to adopting MCP](https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/) for their platform. Early adopters like [Digidop](https://www.digidop.com/blog/mcp-ai-revolution) report a 55% reduction in development time and complexity.

Yet, quick progress might be overlooking security risks. A [recent study](https://equixly.com/blog/2025/03/29/mcp-server-new-security-nightmare/) by API security firm Equixly found that 43% of MCP servers contained command injection flaws.

“The security concerns are very real,” [Kevin Swiber](https://www.linkedin.com/in/kevinswiber/), an API Strategist at Layered System, [shared on LinkedIn](https://www.linkedin.com/posts/kevinswiber_api-mcp-plugin-activity-7309598242646700032-zQHh?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA-8zTABlsmtYe-zC-Uf5z3oD5nm6qXDVVo).

Researchers have identified several key risks associated with MCP systems:

- Tool poisoning.
- Rug pulls (in which a trusted server changes tools, after having been approved by the client, to become malicious).
- Tool shadowing (one server alters the behavior of another).
- Remote command execution (when an attacker runs system commands).
Mitigation strategies include:

- Scanning MCP servers for vulnerabilities.
- Implementing authentication.
- Using a trusted identity provider.
- Applying least-privilege scoping to tool access.
## Zoning In On MCP Vulnerabilities
Tool poisoning attacks, a type of indirect prompt injection, can be used to hijack behaviors in MCP-based systems. This could expose sensitive secrets, such as SSH keys, or trigger unauthorized actions through other connected tools.

This risk stems from a core architectural issue: untrusted MCP servers can embed hidden instructions inside tool descriptions, which the AI model will process but users often won’t see.

“The underlying issue is that an agentic system is exposed to all connected servers and their tool descriptions,” said the Invariant Labs report, “making it possible for a rug-pulled or malicious server to inject the agent’s behavior with respect to other servers.”

Swiber told The New Stack, “A malicious actor could masquerade as a scheduling agent, when really all it’s doing is siphoning private communications to launch a sophisticated phishing attack. The risks range from basic privacy concerns to advanced data exfiltration.”

Invariant Labs identified how malicious packages can be modified post-installation to include untrustworthy code, a known supply chain risk.

“MCP servers carry the same supply chain risks as any third-party package,” an Anthropic spokesperson told The New Stack. “We recommend enterprises continue to follow security best practices when using third-party packages.”

A DevOps researcher [also highlighted](https://elenacross7.medium.com/%EF%B8%8F-the-s-in-mcp-stands-for-security-91407b33ed6b) cross-server tool shadowing and command injection vulnerabilities in MCP systems.

## Be Careful With Local MCP Servers
MCP servers generally fall into two categories: remote and local. And the most pressing concerns revolve around local MCP servers.

“MCP servers have some security challenges by design that developers must proactively address to ensure robust and secure communication,” [Alessio Dalla Piazza](https://www.linkedin.com/in/alessiodallapiazza), Equixly’s co-founder and CTO, told The New Stack.

Remote MCP servers are still evolving in terms of authorization and transport protocol, noted Swiber. As a result, developers are increasingly turning to local MCP servers, which are more clearly defined in the current specification.

The downside is that local MCP servers pose a significantly higher security risk because they often pull unvetted third-party packages from public registries like npm or PyPI — greatly increasing the likelihood of introducing malicious code.

“Local MCP servers run on the user’s operating system, often with the same permissions as the user,” added Swiber. “This opens the window to malicious actors.”

So, be careful with local MCP servers. “You probably shouldn’t blindly download and use MCP servers, because they may behave in ways that can compromise your data source,” [Erik Wilde](https://www.linkedin.com/in/erikwilde), principal consultant at INNOQ, [shared on LinkedIn](https://www.linkedin.com/posts/erikwilde_api-mcp-plugin-activity-7309515359361945601-fmey?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA-8zTABlsmtYe-zC-Uf5z3oD5nm6qXDVVo).

Developers should also ensure insecure functionalities are not inadvertently accessible, Piazza added. This includes the ability to read or write unprotected files, execute system commands or fetch remote resources.

If an MCP server doesn’t properly validate or display tool descriptions, it could be compromised. Invariant’s Beurer-Kellner recommended using tools like [mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) to verify that the servers in use are safe.

“We’re currently working with the community to establish standardized registries for MCP servers,” said an Anthropic spokesperson. “These registries will provide essential metadata about server implementations, enabling users to make informed decisions about which servers to support and integrate with.”

## Securing MCP: Authenticate, Authorize, Abstract
Tool poisoning is only the tip of the iceberg when it comes to LLM tool security.

“Many popular agent systems lack proper guardrails and guarantees about their behavior, making it very risky to connect them to sensitive tools and data,” said Beurer-Kellner. “Even the best LLMs these days still fall for injections and can be easily hijacked.”

Implementing proper authentication is really important. Looking to the future, Piazza hopes MCP will include built-in security measures, like standardized authentication and sandboxing by default.

“Until then, developers need to take attention, not only about the intended use by LLMs but also about potential malicious interactions, ensuring their MCP implementations are secure, authenticated, and verified,” he said.

For remotely exposed MCP servers, their security really hinges on the underlying API best practices that developers have — hopefully — already implemented.

Swiber urges teams to build MCP servers that interface with backend APIs to evaluate the [OWASP Top 10 API Security Risks](https://owasp.org/API-Security/editions/2023/en/0x11-t10/). Proper authorization, setting small scopes, rate limiting, and secure token storage are key activities, they added.

Piazza said that security measures for APIs should offer some protection: “If secure practices are already in place for underlying APIs, adding an exposure with another abstraction layer with MCP should not pose additional risks.”

That abstraction layer, however, must be deliberate, according to [Matt DeBergalis](https://www.linkedin.com/in/debergalis/), CTO and co-founder of [Apollo GraphQL](https://www.apollographql.com/). “AI agents can’t directly connect to production APIs — that’s a security and governance nightmare, ” DeBergalist told The New Stack.

“There needs to be an abstraction layer that enforces policies, handles authentication, manages rate limits and decouples the rapid iteration of AI systems from existing services,” he added.

Finally, there is the issue of identity and access management. As it’s designed, MCP places a lot of burden on the user to implement this.

Instead of asking every MCP to handle authentication and authorization itself, Aaron Parecki, Okta’s director of identity standards, [in a blog post](https://aaronparecki.com/2025/04/03/15/oauth-for-model-context-protocol), suggested treating the MCP server [as an OAuth resource server](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/205) and delegating the hard stuff — like token issuance — to an identity provider.

“The MCP authentication specification is still maturing,” said an Anthropic spokesperson. “We are actively refining it to better align with enterprise security requirements and existing authentication systems.”

## A Dash of Dissent
In the rush to embrace the MCP, companies shouldn’t abandon their usual procedures for providing reliable APIs.

“There are numerous business reasons enterprises have been thoughtfully using HTTP APIs to define and expose digital resources and capabilities present in their databases, files, and other systems for use across multiple internal, partner, and public applications over the last decade,” API Evangelist [Kin Lane](https://www.linkedin.com/in/kinlane/) told The New Stack.

“You will find none of these business reasons present in the current debate around MCP as these reasons are being circumvented to get your data training their models while convincing you that they’ll connect all of the dots.”

While it seems MCP is already off to the races, a dash of dissent is probably healthy for any hyped technology hyped at lightning speed.

## An Invitation to Help Shape MCP
[Agentic AI](https://thenewstack.io/ai-agents/), and MCP for that matter, is at an early stage. And as it gets more use, new threat vectors will likely emerge.
“Agentic security guardrail is actually a very hard problem to solve,” said Beurer-Kellner, adding that “the complexity of agent systems is about to explode and will continuously raise new security threats.”

Anthropic expects the protocol to improve over time, citing upcoming improvements like standardized registries for MCP servers, easier versioning and authentication add-ons. The company also invites community participation.

As an Anthropic spokesperson told The New Stack: “We continue to invite the community to actively participate in shaping MCP. We encourage people to follow along with discussions on GitHub — you can contribute ideas, report issues, and propose changes to the spec.”

Swiber, for one, is both intrigued and cautious: “It’s an exciting space, and I’m looking forward to seeing the standards mature with enterprise-grade security.”

Yet, they acknowledge, “This technology is still in its early days.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)