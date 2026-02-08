Walk into any engineering leadership meeting today, and someone will question whether AI-generated code is secure or whether agents can be trusted in production. These are valid concerns, but they don’t determine whether your team ships faster. The bottleneck is context: the gap between what engineers carry in their heads and what AI can understand or communicate.

Companies that solve the context problem will move faster. Their tools will make fewer mistakes that require human correction, while teams that ignore it accumulate technical debt in the form of code that developers can’t fully explain. Security and quality matter, but they’re largely addressable at the technical layer; the real constraint is transferring engineers’ tacit knowledge into systems.

## Code quality tools are ready, but context isn’t

By 2025, AI [code review](https://thenewstack.io/traditional-code-review-is-dead-what-comes-next/) had truly arrived, and static application security testing (SAST) tools were already catching the obvious issues. Today, most companies run one or more AI reviewers on every change, and false positives are low enough that these tools have earned their keep. The mechanics just work. Claude Code and similar tools showed in 2025 that AI can write substantial, multifile changes that compile and run.

What doesn’t work is the handoff. An engineer spends weeks absorbing not just the technical architecture but also the unwritten rules that govern a codebase: when to prioritize performance over readability, which abstractions the team actually maintains, and how defensive to be about edge cases. When an AI agent writes or reviews code, it operates without that [accumulated knowledge](https://thenewstack.io/why-agentic-ai-needs-a-context-based-approach/). You can feed it documentation, but documentation is always incomplete; it records what someone thought to write down, not the [dozens of micro-decisions](https://thenewstack.io/how-to-find-success-with-code-reviews/) that shaped the current system.

## The two-way problem

[Getting context into AI tools](https://thenewstack.io/better-context-will-always-beat-a-better-model/) requires deliberate effort that most teams haven’t systematized. Engineers need to translate their implicit knowledge into something an agent can parse. Some companies are experimenting with detailed architecture documents that live in the repo specifically for AI consumption, while others are building specialized prompts that encode stylistic preferences. But these are stopgaps. The UX for context handoff remains clunky, and the tooling barely exists.

Extracting understanding back out of AI is just as thorny. When AI generates a code change, engineers still need to build a mental model of what happened so they can maintain the system later. Reading AI-generated code takes different cognitive work than reading human-written code: You’re reverse-engineering intent from output rather than following a colleague’s reasoning process. Skip that step, and you end up with a codebase that nobody fully understands.

## What changes in 2026, and which teams will ship faster

This year, new tools will emerge to solve context transfer. Not just better prompts or fancier retrieval-augmented generation (RAG) implementations, but interfaces for capturing and conveying the implicit knowledge that currently lives only in engineers’ heads. Think of it as infrastructure for the handoff itself.

Far from replacing engineers, this is about getting precise about which parts of their job require human judgment and which parts can be automated once the context problem is solved. Right now, engineers run Cursor and Claude and Aider simultaneously because the marginal gains outweigh the monthly budget per engineer. We’re still in the phase where every tool helps a little, and nothing costs enough to justify consolidation.

In 2026, that will continue; the real change will be in workflows. AI judges will assess pull request (PR) risk with enough accuracy to route changes intelligently: Some go to immediate human review, others to AI-only review, and some to post-merge review within 24 hours. Background agents that spin up in the cloud, clone your repo, execute changes, and return PRs will become more common for scoped outer-loop work like fixing CI, adding unit tests, or breaking up large PRs. These aren’t suited for big greenfield projects, but they’re efficient for the small, repetitive changes that currently require context-switching overhead.

Security and code quality still matter, but they’re largely solved at the technical level. The context gap is what actually determines how much of AI’s potential productivity gain your team captures this year. Teams that get these tools working well won’t just move faster; they’ll start hitting a rhythm where humans handle the judgment calls and creative work, and AI takes care of repetitive tasks, so changes are easier to make and maintain.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/1a291a8b-cropped-71222687-gregfoster-scaled-1-600x600.jpeg)

Greg Foster is the CTO and cofounder of Graphite, the AI code review platform helping teams like Snowflake, Figma, and Shopify ship faster and scale AI-generated code with confidence. Prior to Graphite, Greg was a dev tools engineer at Airbnb....

Read more from Greg Foster](https://thenewstack.io/author/greg-foster/)