Over the past few years, I’ve reviewed thousands of APIs across startups, enterprises and global platforms. Almost all shipped [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) documents. On paper, they should be well-defined and interoperable. In practice, most fail when consumed predictably by AI systems. They were designed for human readers, not machines that need to reason, plan and safely execute actions.

When APIs are ambiguous, inconsistent or structurally unreliable, AI systems struggle or fail outright. The result is a growing gap between what organizations expect AI to do and what their [underlying API landscape](https://thenewstack.io/its-time-to-build-apis-for-ai-not-just-for-developers/) enables.

## **Integration, Not Intelligence, Is the Real Challenge**

As influential founder Tim O’Reilly [recently argued](https://www.oreilly.com/radar/integration-is-the-new-moat/), the real challenge in achieving value from AI is not making models smarter, but integrating them into existing systems and workflows. Intelligence is rapidly becoming a commodity. Integration is the moat.

Enterprise AI initiatives run aground on this reality repeatedly. Studies [show](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) companies eagerly experiment with AI, but only a small fraction of pilots reach production, and in some cases, [as low as 5](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)%.

An overlooked explanation is the state of the APIs AI systems must use. If those APIs are unclear, unsafe or incomplete, no amount of model capability can compensate.

[![](https://cdn.thenewstack.io/media/2025/12/44abdb2e-image2-1024x756.png)](https://cdn.thenewstack.io/media/2025/12/44abdb2e-image2-1024x756.png)

## **What We See When We Look at APIs at Scale**

To understand how APIs behave when consumed by intelligent systems, we analyzed more than [1,500 public APIs](https://github.com/jentic/jentic-public-apis/). Each API had to be parsed, validated and interpreted in a machine-first way, not just skimmed as human documentation.

The patterns that emerged were sobering:

[![](https://cdn.thenewstack.io/media/2025/12/12499152-image3-1024x417.png)](https://cdn.thenewstack.io/media/2025/12/12499152-image3-1024x417.png)

* **Servers often missing or misleading:** Many OpenAPI documents had no servers defined. When present, the first was often QA or sandbox rather than production.
* **Authentication unclear or absent:** Auth was frequently missing or under-specified in the OpenAPI description, making safe automation impossible.
* **Structural validity issues:** Missing path parameters, unresolved references, and incoherent schemas — all preventing reliable machine parsing.
* **Examples underused and untrustworthy:** [Examples](https://spec.openapis.org/oas/latest.html#example-object) were consistently underused, and where they existed, often contradicted the schema.

These are public APIs, where teams have every incentive to invest in quality. Inside large organizations with internal, lightly governed APIs, AI readiness is almost certainly worse.

## **Why Valid OpenAPI Is Not Enough**

For many teams, shipping a valid OpenAPI document is treated as the finish line. If the doc parses, renders properly and passes a linter, the API is considered “done.” For AI systems, that’s a dangerous assumption.

A syntactically valid OpenAPI document only guarantees conformance to the spec’s grammar. Linters focus on structural validity and basic practices; they don’t guarantee the API expresses intent clearly, models its domain coherently or can be reasoned over safely by machines. We repeatedly saw APIs that were technically valid yet operationally ambiguous or misleading.

AI systems operate on what is explicitly declared. When meaning is implicit, inconsistent or missing, models hallucinate or fail.

## **Structural Validity Is a Baseline, Not a Guarantee**

Validity doesn’t guarantee safety. An OpenAPI document can be fully valid yet expose dangerous patterns: sensitive operations without authentication, destructive actions hidden behind vague naming, inconsistent error models or misuse of HTTP methods that obscure intent.

[![](https://cdn.thenewstack.io/media/2025/12/ddd4c8d7-image7-1024x327.png)](https://cdn.thenewstack.io/media/2025/12/ddd4c8d7-image7-1024x327.png)

Take the example above. An AI system could interpret this as creating, replacing or partially updating a user. There’s no guarantee that the same assumption will be made every time an agent encounters the same ambiguity. For sensitive endpoints, this ambiguity [creates real security risks](https://thenewstack.io/ai-agents-are-creating-a-new-security-nightmare-for-enterprises-and-startups/).

## **From Human-Friendly Syntax to Machine-Rich Semantics**

Most APIs require developers to “fill in the gaps.” Missing intent is explained in prose documentation rather than in the OpenAPI document. Authentication rules and environmental/server details live outside the reference documentation. Examples are often sparse or incorrect. Humans compensate for this. Machines cannot.

AI systems rely heavily on the OpenAPI document itself. When critical meaning lives elsewhere, models either guess or fail, resulting in brittle automation and unsafe execution.

What AI systems need from APIs:

* **Interpretable:** Clear expression of intent
* **Composable:** Clear inputs and outputs with well-typed schemas
* **Safe: Explicit security requirements**
* **Predictable**: Error models, status codes, idempotency
* **Resilient**: Clear signals for success and failure
* **Discoverable**: Classification matching goals/user intent

Making the shift toward machine-rich semantics improves both AI capability and developer experience. But it requires treating OpenAPI as an executable contract, not a documentation artifact.

This gap between “valid” and “usable by intelligent systems” led us to define a framework for measuring API AI-readiness.

## The Six Dimensions of API AI-Readiness

We needed a way to systematically evaluate whether an API is usable by AI systems – not just whether it’s valid, but whether it can be understood, reasoned over, discovered and safely executed.

The framework evaluates APIs across six distinct dimensions. Each dimension measures a different property of readiness. No single dimension can compensate for a weakness in another. This ensures a balanced profile is required for higher readiness levels — an API that is semantically rich but structurally broken is unusable; an API that is valid but unsafe cannot be trusted by agents.

Together, these dimensions represent AI maturity, moving from foundational correctness to semantic clarity, operability, trust and discoverability.

[![](https://cdn.thenewstack.io/media/2025/12/a9fc2c89-image1.png)](https://cdn.thenewstack.io/media/2025/12/a9fc2c89-image1.png)

### Foundational Compliance

Is this API structurally sound, standards-compliant and free from critical specification or schema issues? This dimension measures structural validity, reference resolution, linting quality and schema integrity. If an API scores poorly here, it should not be exposed.

### Developer Experience (DX) and Tooling Compatibility

This evaluates usability for humans and automation pipelines: Documentation clarity, naming consistency, example coverage and correctness, response completeness and whether the API can be ingested cleanly by modern tooling. High scores reduce friction for developers and AI systems alike

### AI-Readiness and Agent Experience (AX)

This measures the semantic quality of an API and whether it clearly communicates intent and meaning to AI consumers: Descriptive coverage, schema expressiveness, operation naming quality, error standardization and metadata that helps models infer behavior.

### Agent Usability

Understanding an API is not enough. Agents must be able to use it safely and effectively. This dimension measures operational complexity, semantic overlap between operations, navigation patterns, idempotency and safety characteristics, and how well operations align with AI tool-calling models.

### Security

This dimension evaluates authentication coverage and strength, transport security, sensitive data handling and overall risk posture. It applies hard gating rules for catastrophic failures, such as hardcoded credentials or unprotected sensitive operations.

### AI Discoverability

An API must be findable and classifiable by agents. This dimension measures descriptive richness, intent-oriented phrasing, domain tagging, workflow references and machine-readable discovery signals. Importantly, discoverability is risk-aware; unsafe APIs have reduced visibility to prevent accidental misuse. Ensuring we can surface our capabilities toward agents “just in time” will be imperative to reduce and manage context bloat as more and more enterprise capabilities are made AI-ready.

## Not Guessing: How Scoring Changes the Conversation

Without measurement, AI-readiness discussions stall in opinion. The six dimensions provide a concrete roadmap. Once automated, teams can track progress, measure impact and prevent regressions.

### **Simple Changes That Dramatically Improve AI Outcomes**

Most AI-readiness gaps don’t require sweeping rewrites. Small, targeted changes produce outsized improvements for both developers and AI systems:

* **Fixing broken references and structural schema flaws:** Unresolved references ( `$ref`), contradictory types and malformed schemas silently break automation and undermine trust.
* **Using examples correctly and consistently:** Valid, schema-aligned examples help humans and AI infer correct request and response shapes. They’re often twice as effective as code samples in improving understanding.
* **Writing intent-clear summaries and descriptions:** Explicitly stating what an operation does, why it exists and what it returns dramatically improves machine reasoning and discoverability. Additionally, match HTTP method usage to intent (for example, use `DELETE` to delete a resource).
* **Applying authentication explicitly and appropriately:** Even public [APIs benefit from a clearly defined security posture](https://thenewstack.io/developers-are-key-to-stopping-rising-api-security-threat/). Sensitive operations must always be protected; non-sensitive ones should be intentionally open.
* **Standardizing error and pagination patterns:** Predictable failures and navigation make [APIs safer to automate and easier to compose into workflows](https://thenewstack.io/the-rise-of-ai-agents-how-arazzo-is-defining-the-future-of-api-workflows/). Example: Document error states using appropriate [HTTP status codes](https://datatracker.ietf.org/doc/html/rfc9110#name-status-codes), and use [RFC 9457 (Problem Details)](https://www.rfc-editor.org/rfc/rfc9457.html) to express error response structures.

[![](https://cdn.thenewstack.io/media/2025/12/612f3ef2-image6-1024x538.png)](https://cdn.thenewstack.io/media/2025/12/612f3ef2-image6-1024x538.png)

Improvements made for AI almost always improve the developer experience as well. AI-readiness isn’t a separate track — it’s an acceleration of good API design.

## **Making Executives Care About AI-Readiness**

Executives think about productivity, cost, compliance, risk and return on investment (ROI) — not OpenAPI quality. The connection to AI-readiness is direct: APIs are the execution layer of AI. Every agent action and automated decision becomes a series of API calls. When those APIs are ambiguous, inconsistent, or unsafe, AI programs stall in pilot, fail unpredictably in production or create avoidable compliance and security exposure.

Framing AI-readiness as fewer failed pilots, higher productivity, lower costs and safer automation is how to make executives care. It turns “API hygiene” from a technical nicety into a lever for AI ROI.

## **The Path Forward**

AI success doesn’t begin with a better model; it begins with interfaces that machines can understand, trust and safely use. That makes API AI-readiness an executive concern, not just a tooling detail.

*If you want a video walkthrough of how APIs can be made more usable for AI systems and agents, I’ve explored these ideas further in* [*a recent talk on the “Getting APIs to Work” channel*](https://www.youtube.com/watch?v=qzeR4wBcS4s)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/df494415-cropped-e53bc163-frank-kilcommins.jpeg)

Frank Kilcommins is head of enterprise architecture at Jentic, where he leads efforts to bridge APIs and AI through resilient, open standards-based design and tooling. Over his 15-plus years in technology, Frank has helped define how enterprises design, scale, and...

Read more from Frank Kilcommins](https://thenewstack.io/author/frankkilcommins/)