Regulated industries know this pattern well: A new capability emerges. Teams spin up point solutions, each one solving a discrete problem. Before long, the organization is managing fifteen tools that were never designed to work together and spending more engineering time on integration than on meaningful outcomes.

That is what happened with DevOps toolchains. And it is exactly what is starting to happen with agentic AI.

## The slow cost of DIY platforms

When AI coding tools started delivering real productivity gains, the instinct for many organizations was to go deeper. A code assistant here. An internal AI gateway there. A few open-source models, some custom orchestration, and suddenly the team is calling it a platform.

There’s a reason this happens. Technology teams are wired to build, and that instinct isn’t wrong. Building is how engineers learn, how teams develop expertise, and how genuinely novel problems get solved. The same DIY energy that shaped the early DevOps era produced some remarkable tools and practices. But divergent experimentation rarely serves the broader organization. Organizations don’t want some people to be AI-enabled. They want everyone to be AI-enabled, consistently, in a way that’s governable and scalable. That tension drives every [build vs. buy](https://thenewstack.io/build-vs-buy-the-platform-engineers-guide/) conversation right now.

> “Organizations don’t want some people to be AI-enabled. They want everyone to be AI-enabled, consistently, in a way that’s governable and scalable.”

Before going further, consider what you’re actually deciding.

Build means assembling agentic frameworks, orchestration layers, custom governance, and the underlying infrastructure needed to run it all, including the compute, storage, databases, and networking. The organization becomes the platform vendor.

Buy means adopting a platform that already unifies models, tools, orchestration, and governance across the SDLC. The organization becomes the platform consumer.

That distinction matters enormously in a regulated environment.

## The real complexity is in the orchestration layer

What makes [agentic AI](https://thenewstack.io/evolving-from-pre-ai-to-agentic-ai-apps-a-4-step-model/) different from earlier generations of tooling isn’t the model, but the orchestration sitting in front of it. The most important piece of any modern AI system is increasingly the agentic framework: the logic that decides which tools to invoke, in what sequence, with what guardrails, and with what accountability trail.

This is where the current wave of fragmentation is taking hold. Teams are installing their own agentic frameworks and coding tools, each making rational choices in isolation. But those choices accumulate over time. Every independently adopted framework creates a new integration surface, a new governance gap, and a new silo that the broader organization has to either absorb or work around.

Building an internal [agentic AI platform](https://thenewstack.io/agentic-ai-and-platform-engineering-how-they-can-combine/) in banking or insurance demands a multi-year orchestration engineering commitment with a regulatory surface area that most organizations underestimate:

Start with agentic framework management. Selection, integration, drift monitoring across agent behaviors, and deprecation are ongoing obligations with no off switch. This is followed by security hardening. Agents touching code and infrastructure must meet obligations well beyond a standard SaaS integration, including prompt injection defenses, sandboxing, SIEM and DLP integration, and red-team testing.

Under frameworks like DORA and the EU AI Act, an internal AI system functions as a regulated system, meaning the organization defines the risk classification, maintains the documentation, and produces audit evidence for the life of the system. Every agent embedded in the SDLC also creates a mini-product that teams must maintain across tool versions, framework changes, and org restructures.

> “Not every engineer building the platform may be available to modernize a legacy pipeline, remediate security debt, or accelerate a critical delivery program.”

Beyond those obligations sits the cost that rarely makes it into initial analyses. Not every engineer building the platform may be available to modernize a legacy pipeline, remediate security debt, or accelerate a critical delivery program.

## Learning from the DevOps era

The DevOps era offers a useful reference point. Teams didn’t set out to build fragmented toolchains; they made rational, incremental decisions. A better CI tool here. A preferred SCM there. A security scanner bolted on. A separate secrets manager. A different deployment orchestrator.

Each decision made sense in isolation, but collectively, they created sprawl. Integration burdens, inconsistent governance, duplicated efforts, and no single view of what was happening across the SDLC.

The industry spent the better part of a decade consolidating around platforms precisely because that sprawl was expensive and hard to audit. Agentic AI is following the same arc. Organizations that make a platform decision early, rather than a series of point decisions, will compress years of catch-up into months.

## Three questions to guide your decision

Rather than a generic build vs. buy debate, anchor on three questions.

**Is the requirement truly unique?** Build is defensible when the organization has workflows that no vendor supports, deployment patterns no platform can meet, and a genuine appetite to fund platform engineering as an enduring capability. Modern platforms, however, increasingly meet the needs of regulated organizations where they are, supporting cloud-hosted, self-managed, and dedicated single-tenant deployments to narrow the gap between platform convenience and enterprise control requirements. For goals like faster code review, pipeline migration, security triage, or test automation, platforms are already delivering results for peer organizations.

**How much regulatory surface area can the organization realistically own?** Building makes the organization the system owner under ICT risk frameworks, the AI provider under emerging AI regulations, and the entity accountable for model behavior, documentation, and monitoring. Buying doesn’t eliminate regulatory responsibility, but it offloads platform-level obligations to a vendor whose business depends on getting them right, freeing compliance cycles for how AI is used rather than how it is built.

**What is the time horizon?** If the board expects demonstrable AI value across multiple teams within 12–24 months, a multi-year internal build is misaligned with those expectations from day one.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/69f0c09c-cropped-298ecebd-bryanross-600x600.jpeg)

Bryan Ross is a field CTO for GitLab. An accomplished leader, seasoned technologist and public speaker with over 15 years of industry experience as a senior IT leader, he now helps customers realize business value from IT faster. Equally comfortable...

Read more from Bryan Ross](https://thenewstack.io/author/bryan-ross/)