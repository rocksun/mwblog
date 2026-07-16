[Go](https://thenewstack.io/introduction-to-go-programming-language/) has emerged as the *lingua franca* [for cloud infrastructure](https://thenewstack.io/go-language-fuels-cloud-native-development/), used for everything from container orchestration and CI/CD pipelines to the command-line tools engineers rely on daily. Kubernetes, Docker, and Terraform are all written in it, and it remains a default choice for teams building backend services.

At the same time, [AI agents have become](https://thenewstack.io/coding-agents-team-infrastructure/) the focus of nearly every major software vendor, each racing to give developers a native way to build them. And that’s why Microsoft is now bringing its [Agent Framework](https://github.com/microsoft/agent-framework) to Go, giving cloud-native developers a first-party way to build AI agents in the language they already use for everything else.

Available in public preview from Friday, [Microsoft Agent Framework for Go](https://github.com/microsoft/agent-framework-go) essentially gives Go developers many of the same building blocks already available to their [Python](https://github.com/microsoft/agent-framework/tree/main/python) and [.NET](https://github.com/microsoft/agent-framework/tree/main/dotnet) counterparts: support for models from [Microsoft Foundry](https://thenewstack.io/microsoft-foundry-build-2026-ai-agents/), Azure OpenAI, Anthropic, and Gemini, tool-calling and MCP support for connecting agents to external systems, and the ability to coordinate multiple agents working together on a task.

> “Microsoft Agent Framework is designed for developers who are moving from single prompt calls to production agent systems.”

In a [blog post](https://devblogs.microsoft.com/go/) announcing the release on Friday, [Quim Muntal](https://www.linkedin.com/in/quimmuntaldiaz/), a senior software engineer at Microsoft, notes that the Agent Framework itself is for those building more capable, longer-running AI systems.

“Microsoft Agent Framework is designed for developers who are moving from single prompt calls to production agent systems,” Muntal writes. “Agents that use tools, keep context, coordinate with other agents, stream results, and can be observed and governed as part of real applications.”

That’s the same ground Go already occupies: services, command-line tools, background workers, and cloud-native applications where the language has long been the default. The Go SDK puts those capabilities directly in the hands of developers building in that space.

## How Microsoft’s agent framework arrived in Go

By way of a brief recap, [Microsoft introduced Agent Framework](https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/) in October 2025 as an open-source toolkit for building AI agents and multi-agent systems, unifying two earlier Microsoft projects, [AutoGen](https://thenewstack.io/building-multiagent-workflows-with-microsoft-autogen/) and [Semantic Kernel](https://thenewstack.io/microsoft-semantic-kernel-for-ai-dev-a-chat-with-john-maeda/), into a single supported platform.

It reached general availability [this past April](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/), and at Microsoft’s Build conference in June, [the company added](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/) a bunch of new features and tooling: an “agent harness” for production patterns like context management and human approval steps, hosted agents through Microsoft Foundry, a faster tool-calling method called CodeAct, and support for chaining multiple agents together through a new handoff pattern.

Throughout all of that, Agent Framework remained available only in .NET and Python. Some in the community [had requested support for Go](https://github.com/microsoft/agent-framework/discussions/1146), as well as Rust, with a Microsoft product manager [confirming](https://github.com/microsoft/agent-framework/discussions/1146#discussioncomment-14662163) way back in October 2025 that it was considering a Go version of the framework, but it was “at least a few months off.”

> “This is production-grade orchestration, not a chat loop wrapper.”

It’s still early days, but there are already some murmurings from the developer community about what the release does, and doesn’t, mean. In [a LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7481388476286881792/), AI engineer Pratik Dhanave calls it a milestone for Go-first engineers, singling out the SDK’s graph-based workflow orchestration, which supports patterns like conditional routing, subworkflows, checkpointing, and human-in-the-loop review.

“This is production-grade orchestration, not a chat loop wrapper,” he writes.

Dhanave also points to Microsoft’s own documentation of what the Go SDK doesn’t yet do: handoff orchestration and CodeAct, among other features, remain available in .NET but not yet ported to Go. “I appreciate this level of candor in a public preview,” he continues.

## Where Google, OpenAI, and Anthropic stand on Go

Google, for its part, has been following a similar trajectory, albeit at a different cadence. The company [debuted its own Agent Development Kit](https://thenewstack.io/googles-adk-is-a-new-open-source-framework-for-building-multiagent-systems/) (ADK) in April 2025 as a Python-only toolkit, then added [Go support that November](https://developers.googleblog.com/en/announcing-the-agent-development-kit-for-go-build-powerful-ai-agents-with-your-favorite-languages/), followed by its full [formal 1.0 launch this past March](https://developers.googleblog.com/adk-go-10-arrives/).

Go, of course, is a product of Google, emerging from the company’s open-source vaults [back in 2009](https://opensource.googleblog.com/2009/11/hey-ho-lets-go.html), a move that shaped much of the cloud-native world that followed. It went on to become the language behind Kubernetes and Docker, two projects that defined how modern infrastructure is built and deployed, which helped make Go the default choice for platform engineers. That pull extended well beyond Google into the [realm of AWS](https://aws.amazon.com/blogs/aws/now-available-version-1-0-of-the-aws-sdk-for-go/), Cloudflare, Microsoft, and countless other giants of the tech world.

Given that pull, demand for native Go support in agent tooling is hardly surprising. Go developers wanting to build agent services, embed AI capabilities into existing microservices, or write infrastructure tooling that can make its own decisions have had to make do without an official SDK in their own language: reaching for raw HTTP calls, spinning up a separate Python or Node.js process alongside their Go service, or relying on unofficial, community-maintained libraries of uneven quality and support.

So Microsoft is clearly catering to a well-established developer base. Other big-hitters in the AI realm, however, aren’t yet following suit. As of today, neither Anthropic’s [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) nor OpenAI’s [Agents SDK](https://developers.openai.com/api/docs/guides/agents) officially support Go, [despite community requests](https://github.com/anthropics/claude-agent-sdk-python/issues/498) for [such support](https://community.openai.com/t/golang-support-for-openai-agents-sdk/1368961).

Microsoft isn’t bringing AI agents to Go on its own. But its arrival means two of the biggest cloud vendors now offer first-party agent frameworks for one of the industry’s most widely used infrastructure languages. Anthropic and OpenAI, the two biggest names left in the foundation model space, are lagging.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)