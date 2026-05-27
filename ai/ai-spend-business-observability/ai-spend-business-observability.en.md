**[Kin Lane](https://www.linkedin.com/in/kinlane/), API industry analyst and co-founder of [Naftiko](https://naftiko.io)**, believes that the bill for AI is coming soon. It’s arriving on top of an overdue tab that has been quietly accumulating for almost a decade, as API sprawl and application proliferation have outpaced businesses’ ability to understand, govern, or cost what has been built.

“I was getting people to care about it for APIs and API management,” Lane tells *The New Stack*. “Then AI slammed into us, and all that was forgotten.”

As organizations pour resources into AI with mounting urgency, the same foundational reckoning is playing out on a larger scale and at a faster pace.

For Lane, the current generative AI rush draws a direct parallel with the early days of cloud migration. Back then, companies with strong engineering foundations, clear domain-driven design architectures, and psychologically safe, agile cultures handled the transition seamlessly. Those without them floundered.

Unchecked technical proliferation creates an environment of hidden liabilities—an issue we explored when examining how organizations must [map their API landscape to prevent agentic AI disasters](https://thenewstack.io/map-your-api-landscape-to-prevent-agentic-ai-disaster/). Without visibility into these foundational layers, companies are trying to build the future on top of a shifting swamp.

## **Watch the gap**

To understand why AI spend has become so hard to account for, Lane points to the persistent divide between engineering and business.

“There has been an IT-business divide for most of this century,” he says. “Business people throw requirements over the wall. Engineers build things, but they are often very disconnected from the customer.”

Agile can help, but too often we find some variation of faux-agile where the business and software people lack a common language. As a result, engineers struggle to articulate technical challenges in a way that business stakeholders understand, and vice versa.

“I go into a lot of business groups that don’t know what their engineers are saying or doing, or have any bridge to connect the dots,” Lane said. “Engineers are resistant to anything business-aligned, and business people are resistant to opening up GitHub to see what’s going on.”

## **Engineering observability vs. business observability**

GitHub is one example of a disconnect at the tooling level. Another is observability and traceability. Tools that show uptime, error rates, and security threats serve software engineers well, but tell the business almost nothing it needs to know. What does this system cost to run? What value is it generating? What are the environmental impacts? Which customers does it serve?

These questions rarely have answers because the tools and culture that would surface them were never built. Without those answers, a true understanding of the total cost of ownership for running APIs — let alone AI — simply does not exist in most organizations. “I think that’s what has allowed AI to run so rampant for so long,” Lane says. “No one’s been calculating the cost.”

This lack of visibility ties directly into the broader systemic issue of [AI strategy and API sediment](https://thenewstack.io/ai-strategy-api-sediment/), where forgotten, unmonitored legacy layers stifle innovation and silently drain corporate resources.

> “I’m hoping that AI can help us create this vocabulary for traceability and give those business stakeholders the ability to interact with, evolve, and tailor it to what their businesses need.”

Lane’s response is to expand technical observability, rather than replace it. “You should see dollar signs and customer sectors, lines of business, and products, instead of error rates and technical details,” Lane argues. “You should have more of a product view, not just a Kubernetes ops observability view.”

Business observability, as Lane defines it, shifts the lens from infrastructure to outcomes. It groups spend and usage data by domains such as product, customer segment, sales pipeline, or support function, and presents that information in terms that business stakeholders can act on. The goal is to make the engineers’ work more visible. This isn’t purely a UX change, though, since building it requires a shift in who owns that vocabulary and in what gets tagged, tracked, and surfaced.

Lane is optimistic that AI can help bridge the translation gap, acting as an interpreter between engineering telemetry and business language.

“I’m hoping that AI can help us create this vocabulary for traceability and give those business stakeholders the ability to interact with, evolve, and tailor it to what their businesses need,” he says.

## **The taxonomy of traceability and context engineering**

The mechanism that makes business observability possible is tagging—specifically, the practice of embedding structured metadata into HTTP headers so that every API call, every model inference, and every token consumed carries information about its business context.

Lane borrows the concept from UTM campaign parameters, the tagging system used in marketing analytics to attribute web traffic to specific campaigns, channels, and messages. “You need a similar strategy for traceability,” he says. “How do you build these headers, and how does it group downstream in ways that matter to the business?”

> “Engineers are going to lean towards those ops observability needs. We need sales, support, customer pain points, and all the problem statements associated with products.”

Where technical traceability tags for system health and routing, business traceability tags for cost center, product domain, customer segment, and revenue line. When aggregated, these tags allow organizations to answer critical questions, such as: How much does it cost to serve this customer? What share of our AI spend is attributable to this product line? Is this domain generating more value than it consumes?

Lane argues that this tagging vocabulary must not be owned by engineering. “Engineers are going to lean towards those ops observability needs. We need sales, support, customer pain points, and all the problem statements associated with products.” The taxonomy must be owned and governed by the business domains it describes, with domain experts defining the terms.

This aligns with established domain-driven design principles, treating the enterprise as a set of bounded contexts, each with its own stakeholders, language, and accountability. This structured discipline is a prerequisite for broader [risk mitigation in agentic AI](https://thenewstack.io/risk-mitigation-agentic-ai/), as autonomous agents cannot be safely deployed if the business cannot trace or bound their operational guardrails.

Applying domain-driven design to AI also solves a massive security headache: over-sharing. As explored in our deep dive on [maximizing your existing API investment through context engineering](https://thenewstack.io/mcp-api-governance-readiness/), the instinct when deploying autonomous systems is often to expose a platform’s full API surface to an agent. Lane argues instead for [strict “context engineering” via Model Context Protocol](https://thenewstack.io/mcp-api-governance-readiness/) (MCP) boundaries.

By narrowing down an agent’s access to only the specific tools, operations, and read/write slices required for the immediate business capability, companies can protect their data while sharpening agent focus. The GS1 Global Traceability Standard and architectures like the Common Architecture Language Model (CALM) offer precedents for structured traceability at this level, but the work of applying these frameworks to AI spend is only just beginning.

## **FinOps in the age of AI**

Standards and tooling do exist for calculating infrastructure costs. FinOps—the practice of bringing financial accountability to cloud spend—provides a framework for understanding what services cost, how they’re priced, and how usage maps to budget. But Lane argues that FinOps is underused and poorly integrated with the business context.

He identifies three converging pools of FinOps activity: SaaS management (what services do we use, and what do they cost per user?), container and compute costs (what does it cost to run this infrastructure?), and cloud billing (is our cloud spend under control?). AI adds a fourth and particularly complex dimension, with costs that vary by model, token, usage tier, and API call volume.

> “Everyone said the server bill was going to be much cheaper in the cloud. Fifteen years later, your bill is 10x what it used to be. AI is going to be 100x that.”

“If you don’t have FinOps in place for your models, clouds, and AI services, they’re going to be taking advantage of you rather than you managing them,” Lane warns, drawing a deliberate parallel with the early cloud era. “Everyone said the server bill was going to be much cheaper in the cloud. Fifteen years later, your bill is 10x what it used to be. AI is going to be 100x that.”

Lane’s response has been to begin building machine-readable FinOps profiles for the APIs and AI services organizations use. His project, FinOps Focus (aligned with the FinOps Foundation’s FOCUS specification), documents pricing models, usage tiers, and rate limits in a structured, programmatically accessible format.

To achieve this level of programmatic precision, teams must rely on standardized data contracts. This is where tools like [JSON Schema for AI reliability](https://thenewstack.io/json-schema-ai-reliability/) become indispensable, providing the predictable, machine-readable validation structures required to audit these complex transactions.

“They’re not going to do it for us,” Lane says of the vendors. “You need to budget and project your spend without relying on your vendors to give you the right answer, because they won’t.”

## **The MCP problem**

Lane’s concern doesn’t stop with existing AI services. He’s watching a new wave of sprawl emerge via MCP (Model Context Protocol) servers. “We just unleashed all these MCP servers, and there’s no documentation solution for it. So we created this whole wave of API sprawl that we can’t see, but we have to support and sustain.”

Crucially, Lane points out that “MCP is just an API—a long-lived HTTP connection serving up JSON. We’ve been doing that for years.”

However, the architectural physics have shifted. For the past 15 years, API design was outward-facing, built for a predictable stream of human developers. Agents invert this dynamic entirely.

> “Your API consumers aren’t just Bob and Fred.”

“Your API consumers aren’t just Bob and Fred,” Lane explains. “You have a DDoS of these agents. [*The Matrix* sentinels are trying to get in](https://thenewstack.io/mcp-api-governance-readiness/), rather than you trying to get out. That reversal in polarity is a big shift.”

Organizations that have treated OpenAPI specifications as an afterthought will find this influx incredibly difficult to manage. An OpenAPI spec shouldn’t just be documentation; it is the machine-readable ‘menu’ from which agent skills are dynamically derived.

This readiness can often be predicted by a surprisingly simple proxy: whether a company maintains a mature public or partner-facing API portal. Portals represent internal muscle memory for access control, rate limiting, and semantic clarity. Organizations that lack this framework hit a wall of political friction and operational anxiety when forced to adapt to the demands of autonomous agents.

## **What comes next**

Throughout this series, we’ve explored why the foundational work matters: mapping the service landscape, tagging for traceability, governing spend with FinOps discipline, defining data contracts, and establishing domain boundaries before the sprawl becomes unmanageable. “You can’t see what you don’t map out and define as artifacts,” Lane says.

For enterprises that find themselves lagging behind, the situation is not hopeless. Late adopters have a unique advantage: they can bypass decades of legacy database debt and build clean, modern data pipelines directly with cloud-native gateways and contemporary data warehouses such as Snowflake.

However, AI ultimately rewards consistency over reactivity. The enterprises currently thriving are those that made seemingly dull, compounding investments in governance, schema validation, and documentation standards years ago. As Lane notes, “The deeper your roots, the less you’re likely to respond in a knee-jerk or emotional way.”

Lane believes business traceability will eventually force spending, ROI, and business outcomes into the same frame as infrastructure decisions. But the conversation rarely happens until the check arrives. “That’s going to be in the next three to five years with AI,” he says. “We just spent a crazy amount of money on this. What was the ROI? That answer doesn’t exist yet.”

> “Technical observability has kept the lights on; business observability is what will keep the enterprise solvent.”

For organizations that want to get ahead of that reckoning, the path forward is clear: map your complete internal and SaaS landscape, implement machine-readable FinOps accounting, embed business context headers into every token transaction, and ensure the domain vocabulary is owned by the business itself. Technical observability has kept the lights on; business observability is what will keep the enterprise solvent.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)