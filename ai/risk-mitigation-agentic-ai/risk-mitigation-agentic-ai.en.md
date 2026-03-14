For enterprises, agentic AI systems potentially allow staff responsibilities to shift from execution to judgment, oversight, and strategy. This creates new opportunities, but is fraught with risk:

1. **Loss of human oversight and control**: Agentic systems can take sequences of autonomous actions, such as browsing the web, executing code, calling APIs, and managing files, often with minimal human checkpoints. This creates compounding risk: an early mistake can cascade into significant damage before anyone notices. Enterprises may struggle to audit what actions were taken, when, and why, making accountability and remediation difficult.
2. **Security and prompt injection vulnerabilities**: Agents that consume external data (web pages, emails, documents) are susceptible to prompt injection attacks, where malicious content in the environment hijacks the agent’s behavior. In an enterprise context, a compromised agent with access to internal systems, databases, or APIs could exfiltrate sensitive data, escalate privileges, or execute destructive actions while appearing to operate normally.
3. **Unpredictable and hard-to-reverse actions**: Unlike chatbots that only generate text, agentic systems take real-world actions: sending emails, modifying records, making purchases, and deploying code. Mistakes may be difficult or impossible to undo. The combination of broad tool access, long task horizons, and ambiguous instructions creates scenarios in which an agent pursues a goal in a technically correct but operationally catastrophic way.

In addition, agentic use can lead to over-reliance on agent judgment for sensitive decisions, data privacy risks from agents ingesting confidential context, and third-party supply chain risk when agents call external services.

> “An early mistake can cascade into significant damage before anyone notices. Enterprises may struggle to audit what, when, and why actions were taken.”

Because agentic AI is so new, we don’t have patterns or best practices to draw on. Instead, as IT professionals, we need to figure out the risk mitigations among us, and hopefully share what we’re learning publicly as we go. **[Kin Lane](https://www.linkedin.com/in/kinlane/)**, co-founder and chief community officer (CCO) for the open-source API company **[Naftiko](https://naftiko.io)**, sees the mitigation of agentic risk in systems-thinking terms. His broad thesis is that testing and mocking is how an enterprise can confidently and safely prepare for agentic systems.

## Behavior is the specification

One of the most well-known heuristics in systems thinking was coined by the late [Stafford Beer](https://en.wikipedia.org/wiki/Stafford_Beer), a British theorist, consultant, and professor at Manchester Business School. He frequently used the phrase, “The purpose of a system is what it does” — meaning that a system often functions in a way that is at odds with the intentions of those who design, operate, and promote it. “There is, after all,” Beer observed, “no point in claiming that the purpose of a system is to do what it constantly fails to do.”

If a system’s purpose is indeed revealed through its behavior rather than its design, then understanding what [Donella Meadows](https://donellameadows.org) refers to as the “and” — the relationships between components — requires being able to observe the system reliably.

> “The purpose of a system is what it does. There is, after all, no point in claiming that the purpose of a system is to do what it constantly fails to do.” – Stafford Beer

Observability tools like [Honeycomb](https://www.honeycomb.io) use distributed tracing and high-cardinality event data to provide insights into system behavior in production, allowing engineers to query and explore arbitrary dimensions of telemetry (spans, traces, and structured log fields) in real time. But for agentic systems, we also need confidence ahead of production.

Lane believes that can be found in the test suite; testing, he says, allows you to intentionally shape behavior and, in turn, the future of an API.

“People tend to see API testing as making sure it’s doing what it should,” he tells *The New Stack*. “But the combination of having a strong sandbox and using contract testing to get a strong feedback loop with your consumers allows iterating on what the future holds. Companies with good testing practice are much better at both inventing and dealing with the future. And they’re able to bring things to life in reliable, reproducible ways that producers and consumers agree on.”

It is this mentality that he brings to the work of defining [business capabilities](https://thenewstack.io/map-your-api-landscape-to-prevent-agentic-ai-disaster/) — essentially, discrete, composable units that describe what a system can do for a business (like ‘process payments’ or ‘manage inventory’) — for his clients. He builds sandboxes and mocks, thereby allowing their AI agents a safe place to play.

For his approach to work, the mocks need to be accurate representations of reality. “I should be able to switch the URL of the mock to production and reliably get live responses with the same structure,” he says. “That acts as a test; can I move from synthetic mock to production without breaking?”

Done well, mocks and contract tests reinforce each other. Fragile, unrealistic mocks indicate poor or nonexistent contract testing, not a failure of mocking itself. Without shared visibility between API producers and consumers, mocks and real APIs evolve independently, and that can break trust. When providers publish formal specs and examples, and use them in their own contract tests, everyone stays aligned.

To achieve this, Lane prefers open-source tooling, specifically [Microcks](https://microcks.io) and [OpenAPI](https://swagger.io/specification/), with [Bruno](https://docs.usebruno.com/testing/script/javascript-reference) for scripting.

## Shared mocks, shared reality

Microcks is an open-source API mocking and testing platform built in Java that has been running for ten years and was donated to the Cloud Native Computing Foundation (CNCF) more than three years ago. Built for enterprise scale, it is language agnostic, supporting REST/OpenAPI, AsyncAPI, Kafka, MQTT, WebSockets, gRPC, GraphQL, and more.

That breadth is invaluable since enterprise environments typically layer multiple API standards — which I referred to in a previous article in this series as [API sediment](https://thenewstack.io/ai-strategy-api-sediment/) — rather than standardize on one. Without a tool like Microcks, “You end up with a dedicated tool for each type of protocol or spec, which is a nightmare,” Microcks co-founder, [Yacine Kheddache](https://www.linkedin.com/in/yacinekheddache), told me. “For mocking purposes, developers are creating their own dummy mocks that are not representative of the real business service.”

The platform is built around a contract-first philosophy. A primary artefact (such as an OpenAPI spec) is imported, and Microcks uses it to auto-generate mock endpoints with no code required. To avoid bloating the primary spec with hundreds of examples, Microcks supports secondary artefacts, additional example sets sourced from Postman collections, HTTP archive recordings, an AI copilot, or hand-crafted YAML files. Bundling primary and secondary artefacts generates on-the-fly sandboxes that adopters have described as “sandbox as a service.”

A notable aspect is how Microcks encourages organization-wide collaboration. “It’s not only developers who are maintaining throwaway local mocks for unit tests. Teams build shared, versioned example datasets that everybody globally around the API service contributes to and reuses.”

Kheddache says. This allows parallel development across microservices teams: developers mock their dependencies, work independently, and simply swap in the real service when it becomes available.

Large adopters, including [Amadeus](https://amadeus.com/en), that use Microcks to [shift-left their mocking and contract testing approach](https://www.slideshare.net/slideshow/how-to-secure-your-apis-without-compromising-the-developer-experience-pdf/281499574) have reported significant gains in development speed.

## Microcks at BNP Paribas

The collaborative, shared ownership model Kheddache describes isn’t theoretical. At BNP Paribas, [32 squads across the French retail banking division are now using Microcks](https://microcks.io/blog/bnp-journey-with-microcks/), with over 500 developers and testers actively on the platform, and more than 2.5 million API calls processed through it every week.

BNP had a massive legacy mainframe sitting at the heart of core banking operations, which every team had to interact with directly whenever they needed to build or test against it. Slow, expensive, and placing unnecessary strain on infrastructure that costs serious money to run.

By mocking those mainframe-backed APIs in Microcks, BNP’s teams could develop and test in parallel without touching the mainframe, and only connect to real services when genuinely necessary. The result, according to the published case study, was that development and testing cycles were cut by two-thirds.

There was also an unexpected bonus: significantly reduced mainframe load translated directly into lower energy consumption, a meaningful contribution to the bank’s sustainability targets, and not the kind of outcome you’d typically associate with a testing tool. “The ability to deploy mock sandboxes everywhere, ready to use,” the BNP team noted, “was central to making that scale work.”

It’s the kind of outcome Kheddache had in mind when he described the broader promise of the platform. “When they adopt our approach, the wins are incredible,” he told me. “They are able to speed up development, mock all the dependencies, and everybody can work in parallel.”

For contract testing, Microcks can act as an API client, firing requests at a real endpoint and verifying it remains compliant with its contract across multiple versions. This is useful for catching breaking changes and certifying backward compatibility.

Microcks has also shifted toward supporting individual developers, not just centralized platform teams. A lightweight native binary (compiled via GraalVM) starts in under 200 milliseconds, and [Testcontainers](https://testcontainers.com) bindings exist for Java, Node, Go, and .NET (the last contributed by AXA Insurance). Developers can now run full integration tests locally, using the same shared example datasets as the central environment, closing the ‘works on my laptop’ gap.

Each Microcks simulation endpoint now also exposes a Model Context Protocol (MCP) link, making mock APIs accessible to LLMs and AI agents as tools. A second, currently unnamed, project is in development: a runtime proxy that translates OpenAPI, GraphQL, and gRPC specs into [MCP servers for production](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/) use, with secret management and custom tool shaping to make APIs more reliably usable by language models.

## AI fragments the feedback loop

Typically, in the context of testing and mocking, the more stakeholders using the sandbox, the more likely you are to achieve a comprehensive and reliable mock. Add generative AI into the mix, however, and as with the act of [programming itself](https://leaddev.com/ai/nobody-knows-what-programming-will-look-like-in-two-years), we are still trying to understand what a healthy feedback loop looks like. “Historically, healthy feedback came from having all the stakeholders in a workspace, a repo, or a meeting in the same room on the whiteboard. But AI further fragments things, so I’ve got to rethink that, and I don’t have a good answer yet,” Lane says.

> “That menu of internal and external APIs is what you’re capable of as a company. If you don’t have that in a catalogue, a sandbox, or a registry, so you can test, play, and understand it, your teams aren’t going to know what you’re capable of.” – Kin Lane

He is, however, certain that you should have mocks, not only for what you are producing but also for what you are consuming. “That menu of internal and external APIs is what you’re capable of as a company. If you don’t have that in a catalogue, a sandbox, or a registry, so you can test, play, and understand it, your teams aren’t going to know what you’re capable of.”

Tools like Microcks make contract-driven mocking easy, but collaboration and shared ownership are what make it work. As agentic systems take on more autonomy, that shared understanding of what a system can, and should, do becomes the foundation on which everything else rests.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)