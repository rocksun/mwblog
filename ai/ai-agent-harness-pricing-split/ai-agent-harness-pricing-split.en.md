On March 30, Sycamore [announced](https://www.businesswire.com/news/home/20260330376116/en/Sycamore-Raises-$65M-to-Build-the-Trusted-Agent-Operating-System-for-the-Enterprise) a $65 million seed round to build what its founder calls an operating system for autonomous enterprise AI. On April 8, Anthropic launched [Managed Agents](https://www.anthropic.com/news/claude-managed-agents) in public beta at eight cents per session hour. Seven days later, OpenAI [shipped](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) its own model-native harness as an update to the open-source Agents SDK, with no additional first-party runtime fee beyond standard API and tool pricing.

Three moves in sixteen days, each betting on the same observation about the market. The harness is now the product. But the labs disagree, sharply and publicly, on how that product should be sold.

Anthropic has added a separately billed runtime on its own infrastructure. Google and Microsoft have packaged the layer for consumption across sessions, memory, code execution, and tool use. OpenAI is giving the runtime away as open source and charging only for the model and tool calls that already have meters. The category is forming fast, and the business model is not.

> The harness is now the product. But the labs disagree, sharply and publicly, on how that product should be sold.

## What a harness is, and why it became a market

The word “harness” entered wide circulation in February, when OpenAI published an engineering [blog post](https://openai.com/index/harness-engineering/) describing how a small team shipped a million-line production system in which zero lines of code were written by human hands. The term stuck because it named a real discipline that teams had been practicing without a label. Martin Fowler canonized it in early April with a long [essay](https://martinfowler.com/articles/harness-engineering.html) that defines harness engineering as everything surrounding an AI model, except the model itself.

A harness is the control layer around an agent that helps it operate reliably in production. It typically covers model invocation and context management, tool orchestration, sandboxed execution, persistent session and execution state, scoped permissions, error recovery, observability, and tracing. In that sense, it is analogous to the production infrastructure around containers: not the model itself, but the surrounding system that makes long-running agents safe, debuggable, and dependable.

For the last 18 months, cloud and framework vendors have offered partial managed components of this layer, but most teams shipping production agents still had to assemble too much themselves. Startups raised money to sell a ready-made version. Internal platform teams built their own from open-source parts. The harness became a market because the available pieces did not yet add up to a clean answer.

## What Anthropic shipped, and what it costs

Managed Agents is Anthropic’s answer to that gap, packaged as a beta API on the Claude Platform. Developers define the agent, tools, and guardrails, and Anthropic runs the execution environment with long-running sessions that stretch across multiple hours, sandboxed code execution, scoped permissions, end-to-end tracing, and MCP-based connections to third-party services.

The launch customers carry weight. Notion uses Managed Agents to run dozens of parallel delegation tasks. Rakuten deployed specialist agents across product, sales, marketing, finance, and HR. Sentry built an agent that takes a flagged bug and turns it into an open pull request without a human in between. Asana integrated the service into its AI Teammates feature, and Atlassian signed up as a launch customer.

Pricing is transparent in its comparison. Standard Claude Platform token rates apply to all model inference, with a usage-based fee of eight cents per session hour while the session is running. Multi-agent orchestration, self-evaluating outcomes, and long-term memory sit behind a separate research preview access request, meaning three of the most interesting capabilities are gated.

Anthropic also ships a Claude Agent SDK for programmatic building, so the managed-versus-open distinction runs between products rather than strictly between companies. But Managed Agents, the April 8 launch piece, is hosted only on Anthropic’s infrastructure.

## What OpenAI shipped, and what it costs

Seven days later, OpenAI shipped a different bet. The updated open-source Agents SDK adds a model-native harness and native sandbox execution, with configurable memory, sandbox-aware orchestration, Codex-style filesystem tools, and standardized MCP integrations. It targets long-horizon agents running across multiple hours and many tool calls, the same use case that Managed Agents target.

The delivery model is the inversion of Anthropic’s. OpenAI does not run the compute. Developers bring their own through a Manifest abstraction that supports seven sandbox providers, including Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, and Vercel, with storage across S3, GCS, Azure Blob, and Cloudflare R2. Externalized state lets runs survive a lost sandbox container, with snapshotting rehydrating the run in a new one. The harness coordinates, but the infrastructure belongs to the developer.

The pricing line is where the comparison sharpens. OpenAI’s announcement says the new capabilities use standard API pricing based on tokens and tool use, with no separate first-party runtime fee and no session-hour meter. The SDK itself is free and open source. The developer still pays real money for sandbox compute and storage to whichever providers they choose, so the total cost is not zero, but OpenAI has declined to add a runtime line item of its own. Depending on the workload shape, the total cost can land on either side of Anthropic’s bundled model.

OpenAI was explicit about why. Its announcement framed managed agent APIs as simplifying deployment at the cost of constraining where agents run and how they access sensitive data. That is a direct public disagreement with the path Anthropic, Google, and Microsoft have chosen.

## The labs agree on owning the layer. They disagree on how to bill it.

Google lists Vertex AI [Agent Engine](https://docs.cloud.google.com/agent-builder/agent-engine/overview) as a fully managed runtime with sessions, memory, code execution, and observability, each billed as a separate consumption line rather than a single per-hour fee. Microsoft ships [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) with consumption-based billing across models and tools, with specific session metering on tools like Code Interpreter rather than on the platform as a whole. AWS [announced](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership) in February that it will co-create a Stateful Runtime Environment with OpenAI, available through Bedrock in the coming months, alongside Bedrock [AgentCore](https://aws.amazon.com/bedrock/agentcore/) as the runtime primitives layer.

Each of these is a different pricing shape. Anthropic bundles compute, state, and orchestration into a session-hour fee. Google meters components separately, while Microsoft meters by model and tool. AWS will add another managed path once the OpenAI runtime ships. OpenAI’s first-party answer skips the runtime meter entirely.

The five vendors agree that the layer matters and that they want to own it. They disagree on whether that offering is a hosted service with its own meter, a collection of priced primitives, or an open-source SDK carried by model revenue. That disagreement is not a stalemate. It is a deliberate strategic divergence.

## The middleware arc, with a split running through it

Cloud infrastructure has seen this split before, and the outcome was not a clean absorption. Terraform remained open-source alongside AWS CloudFormation’s managed offering. Kubernetes remained open-source and became the de facto standard even as AWS, Google, and Microsoft shipped managed container services. In both cases, open source did not eliminate managed, and managed did not kill open source. They coexisted because they served genuinely different buyer profiles.

The lesson is that when one vendor ships free, open-source software and others ship paid, managed software, the market tends to split on infrastructure preferences rather than collapse. Teams that want hosted convenience go to the managed service. Teams that want control, portability, or multi-cloud flexibility go to the open-source stack. Both sustained real businesses in the cloud era.

What does change is the economics for independents selling a horizontal version of the layer. A free model-native harness from OpenAI puts more pricing pressure on independent frameworks than a paid managed service ever could. The cloud pattern is starting to run here, but with two compressions happening in parallel.

## What this means for startups that filled the gap

My read is that the risk profile for harness startups just got more specific. Sycamore’s pitch to Coatue and Lightspeed focused on trust, governance, and control in enterprise AI, with multi-model support baked in. That pitch is genuinely defensible against both the Anthropic-managed path and the OpenAI open-source path, because it targets a buyer who cares about independence from any single lab. Sycamore does not look like the vulnerable archetype here.

The archetype most exposed by these launches, as I see it, is the horizontal orchestration framework. LangChain, CrewAI, and VoltAgent compete more directly now with a free, model-native, well-supported harness from the lab whose models they depend on. The performance argument that model-agnostic frameworks have been making, that flexibility beats vendor lock-in, gets harder to land when the vendor in question is giving away an open-source harness that is better-aligned with its frontier models. The ones still pitching a horizontal model-agnostic orchestration layer to enterprise buyers probably have the harder conversation ahead.

Startups selling paid managed platforms face the squeeze from Anthropic, Google, and Microsoft. The strategic answer to both pressures looks the same to me. Differentiate into governance, compliance, vertical depth, or multi-model control, or compete on price against free on one side and bundled on the other.

## What this means for teams that built their own

The build-versus-buy calculus has two new reference points. Teams that want bundled infrastructure can benchmark their internal harness against Anthropic Managed Agents at eight cents per session hour plus tokens. Teams that already run their own infrastructure can benchmark against OpenAI’s SDK with no additional first-party runtime fee, in addition to whatever they pay their sandbox and storage providers. Different teams will find different benchmarks relevant, but neither existed a month ago.

For teams still in the prototype phase, building the scaffolding from scratch got harder to defend overnight. The infrastructure work that used to be differentiated engineering is now a service available through an API or a free SDK. For teams already in production, the internal system might still be more tuned to the workload. But the team maintaining it is now competing with a category that four frontier labs are actively investing in, which will make that work evolve more slowly, less prestigious, and harder to recruit for.

Build is still a valid choice. It just has to beat both benchmarks now, on workload fit and on team sustainability, rather than neither.

## What’s next

The harness was supposed to be the moat. For eighteen months, most teams shipping production agents built or assembled their own, and that work was the differentiation. The frontier labs have collectively decided not to sell model access and watch someone else capture the margin above it, but they have split on how to capture it themselves. Three of them charge for the runtime in one shape or another. One is giving the harness away and betting on model loyalty instead.

> The harness was supposed to be the moat.

The question to watch is which business model wins, or whether the market sustains all of them. OpenAI’s bet is that a free, open-source, model-native harness drives more model consumption than a paid managed runtime ever would, and that the Bedrock partnership covers enterprises that want hosted. Anthropic is betting on a paid, fully managed version, while Google and Microsoft are betting on packaging priced primitives within a broader platform. Not all of these can be right at the same scale, and the startups watching from outside need to know which way the volume moves before they commit to their differentiation strategy. Stay tuned as I decode the concepts of the agent harness and the runtime, which are constantly evolving.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)