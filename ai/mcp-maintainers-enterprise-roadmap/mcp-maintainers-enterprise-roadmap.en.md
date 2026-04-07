In a roundtable panel at the [MCP Dev Summit](https://events.linuxfoundation.org/mcp-dev-summit-north-america/) last week in New York, Model Context Protocol (MCP) [maintainers](https://www.linuxfoundation.org/blog/open-source-maintainers-what-they-need-and-how-to-support-them) from Anthropic, AWS, Microsoft, and OpenAI reassured us that the MCP spec is in safe hands at the [Agentic AI Foundation](https://aaif.io/) (AAIF) and will be addressing critical enterprise requirements for security, reliability, and governance.

Starting in December with contributions of MCP, [goose](https://github.com/block/goose), and [AGENTS.md,](http://agents.md) the AAIF has quickly grown to 170 members. MCP is the most popular project and has become the industry standard for connecting AI agents to data and applications.

The panel reassured MCP users that little has changed in how the project governs itself (it’s still a bottom-up, open source project). The AAIF provides a connection to enterprise users and their needs, which feeds back into protocol development to address concerns about using MCP in production.

“We see customers excited about the Foundation and about this being a neutral place to work on MCP and related projects,” said maintainer Claire Liguori, Sr Principal Engineer, AWS. “It’s great to be around the community and work within the entire developer ecosystem, and not just within our own companies.”

The broad adoption of MCP has identified significant areas for improvement, they said, especially for enterprise applications requiring strict security, scalability, reliability, and governance.

> “MCP is the seed. The foundation has a broad mandate beyond just MCP … It’s open to new protocols and technologies, just like early Cloud Native Computing Foundation (CNCF) was. But MCP itself should stay narrow: Connecting AI to data sources.” — Nick Cooper, OpenAI

“MCP is the seed,” said maintainer Nick Cooper, Technical Staff, OpenAI. “The foundation has a broad mandate beyond just MCP,” he continued. “It’s open to new protocols and technologies, just like the early [Cloud Native Computing Foundation](https://www.cncf.io/) (CNCF) was. But MCP itself should stay narrow: Connecting AI to data sources. Identity, observability, and governance should come in as other projects.”

AAIF is currently soliciting [new project proposals](https://github.com/aaif/project-proposals) related to agentic AI, Cooper added, but we need to be careful that the first accepted projects set the right direction.

“We see open challenges in security and authorization, and we’re happy to have AAIF bring the industry together and talk about the right solutions,” said maintainer David Soria Para, Technical Staff, Anthropic, and co-creator of MCP.

Authorization has been one of the most actively changing parts of the MCP spec over the past year, Para added. The maintainers are collaborating with Okta and others on authentication improvements.

But no single protocol will solve all security challenges — the ecosystem (gateways, registries, sandboxing, interceptors) must evolve alongside the protocol, Para said.

Moderator Sephen O’Grady of [RedMonk](https://redmonk.com/) said that MCP is the fastest-growing standard RedMonk has ever tracked. For example, he said, it took Docker about 13 months to get as established as MCP did in about 13 weeks.

Another proposed standard in the agentic AI space is the [Agent2Agent](https://a2a-protocol.org/latest/) (A2A) protocol, which enables AI agents to connect with one another.

MCP and A2A are large protocols learning from each other, and not directly competing, the panel noted. Future convergence is possible but not certain — “approaches are slightly different at the moment,” said Para. “But we are open to anything that makes the industry easier to work with through open standards.”

O’Grady referenced a widely debated social media post claiming “MCP is dead” because a command-line interface (CLI) with comparable functionality is available.

“We ship APIs, we ship SDKs, and we ship CLIs all to interact with Azure for a concrete experience with Microsoft, and that’s because we want to meet developers where there are, and we want to meet them at the scenario that they’re working in,” said maintainer Catie McCaffrey, Partner Software Engineer at Microsoft. “For local development scenarios, having an agent just interact with the Azure CLI or the GitHub CLI is a really wonderful use case.”

> “For local development scenarios, having an agent just interact with the Azure CLI or the GitHub CLI is a really wonderful use case … The focus of MCP going forward has to be on its utility in connecting things. MCP can evolve as long as it preserves the utility of what’s important.”

The panel said that both the MCP and CLI mechanisms for interacting with agents are important for different use cases and offer different developer experiences.

“The focus of MCP going forward has to be on its utility in connecting things. MCP can evolve as long as it preserves the utility of what’s important,” said Cooper. “Where the value lies for me is that there’s real utility in using MCP to connect these different systems. MCP should grow, evolve, and focus on that. And that’s why it’s important to behave neutrally and focus on the utility that MCP is delivering.”

The panel agreed that the MCP client needs attention and that MCP best practices require better documentation and communication. For example, don’t just wrap 500 API endpoints. That’s the number one anti-pattern. Instead, design the MCP interface for the agent as a new class of consumer (not just another developer). There are big quality differences between carefully designed servers and naive API wrappers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/01/9843bda4-cropped-6e8aff6e-eric-newcomer-intellyx-analystwithhand2023-s341x512.jpg)

Eric Newcomer is CTO at Intellyx. He has served as CTO for leading integration vendors WSO2 and IONA Technologies and as Chief Architect for major enterprises such as Citibank and Credit Suisse. He has created some of the best-known industry...

Read more from Eric Newcomer](https://thenewstack.io/author/eric-newcomer/)